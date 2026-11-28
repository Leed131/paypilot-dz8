"""One real, local-only judge call; intended to run inside the L10 container."""

from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parent.parent
FROZEN_SHA256 = "dd685f9722b0159230822dadc4e3d169aa9690e7eb758f466303645df99fbf8f"
MODEL = "ollama:qwen2.5:7b"
DIGEST = "845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e"
MAX_LOCAL_BYTES = 6_000_000_000


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    report = {"status": "running", "started_at": now(),
              "test": "local_judge_one_call", "case_id": "LB-11",
              "model_calls_attempted": 0,
              "container_marker_present": Path("/.dockerenv").exists(),
              "python_version": sys.version.split()[0],
              "note": "One recorded-answer adapter test, not a full agent/release gate."}
    return_code = 1
    try:
        raw = (ROOT / "sets/l09_labels_kit_v1.jsonl").read_bytes()
        if hashlib.sha256(raw).hexdigest() != FROZEN_SHA256:
            raise ValueError("Frozen calibration set changed; no model was called.")
        cases = [json.loads(line) for line in raw.splitlines() if line.strip()]
        matches = [case for case in cases if case.get("id") == "LB-11"]
        if len(matches) != 1:
            raise ValueError("Expected exactly one original LB-11 case.")
        case = matches[0]
        one = [json.loads(line) for line in (ROOT / "sets/l10_one.jsonl").read_bytes().splitlines()
               if line.strip()]
        if one != [case]:
            raise ValueError("l10_one does not contain exactly the original LB-11.")
        meta = case["additional_metadata"]
        model = os.environ.get("JUDGE_MODEL", MODEL)
        temperature = float(os.environ.get("TEMP", "0"))
        url = os.environ.get("OLLAMA_URL", "http://host.docker.internal:11434")
        if model != MODEL or not math.isfinite(temperature) or temperature != 0:
            raise ValueError("Self-test requires qwen2.5:7b and TEMP=0.")
        if os.environ.get("JUDGE_FORMAT", "schema") != "schema":
            raise ValueError("Self-test requires JUDGE_FORMAT=schema.")
        sys.path.insert(0, str(ROOT))
        from judge import judge, preflight
        runtime = preflight(model, url)
        installed = runtime["installed_model"]
        if installed.get("remote_host") or installed.get("remote_model"):
            raise ValueError("Remote model detected; this test must remain local.")
        if installed.get("digest") != DIGEST:
            raise ValueError("Model digest differs from the measured local 7B model.")
        size = installed.get("size")
        if type(size) is not int or not 0 < size <= MAX_LOCAL_BYTES:
            raise ValueError("Model file does not satisfy the 6 GB local size contract.")
        report.update(judge_model=model, temperature=temperature, judge_format="schema",
                      ollama_url=url, execution_location="local", runtime=runtime,
                      set_sha256=FROZEN_SHA256,
                      rubric_version=meta["rubric_version"],
                      judge_adapter_sha256=hashlib.sha256((ROOT / "judge.py").read_bytes()).hexdigest())
        report["model_calls_attempted"] = 1
        started = time.perf_counter()
        result = judge(case["input"], case["answer_under_test"], meta["rubric"],
                       model, temperature, meta["rubric_version"], url)
        report["elapsed_seconds"] = time.perf_counter() - started
        report["result"] = result
        backend = result.get("backend_metadata", {})
        if backend.get("remote_host") or backend.get("remote_model"):
            raise ValueError("Backend reported remote inference; reject this as a local test.")
        passed = not result.get("data_quality_errors") and result.get("verdict") == "PASS"
        report["status"] = "passed" if passed else "failed"
        report["expected_verdict"] = "PASS"
        return_code = 0 if passed else 2
    except Exception as exc:
        report.update(status="failed", error=str(exc), failure_type=type(exc).__name__)
    report["finished_at"] = now()
    directory = ROOT / "reports"
    directory.mkdir(exist_ok=True)
    path = directory / ("l10-docker-selftest-" + stamp + ".json")
    with path.open("x", encoding="utf-8") as out:
        json.dump(report, out, ensure_ascii=False, indent=2)
        out.write("\n")
    print(json.dumps({"status": report["status"], "case_id": "LB-11",
                      "model_calls_attempted": report["model_calls_attempted"],
                      "report": str(path)}, ensure_ascii=False))
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())

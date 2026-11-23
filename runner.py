"""Focused HW08 working gate, using the supplied course loader and assertions.

Unlike recorded-answer calibration, this runner calls an external course bank
stand. Each judge case generates five fresh answers and judges each answer once.
The gate is strict: every required run must pass with valid judge evidence.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import sys

import assertions as A
from loader import load, set_hash, summarise
from judge import judge, preflight
import stand

ROOT = Path(__file__).resolve().parent


def now():
    return datetime.now(timezone.utc).isoformat()


def working_cases(path, gate, only=None):
    """Reuse the course schema validator, then enforce HW08 gate separation."""
    cases = load(path)
    for case in cases:
        meta = case["additional_metadata"]
        assertion = meta["assertion"]
        if assertion == "tool_sequence":
            if meta.get("runs") != 1 or meta.get("gate") != "daily":
                raise ValueError("Threshold must use runs=1 and gate=daily: " + case["id"])
        elif assertion == "judge":
            if meta.get("runs") != 5 or meta.get("gate") != "release":
                raise ValueError("Judge cases must use runs=5 and gate=release: " + case["id"])
            if not meta.get("rubric_version") or not meta.get("rubric"):
                raise ValueError("Judge rubric/version missing: " + case["id"])
        else:
            raise ValueError("This focused runner supports tool_sequence and judge only.")
        if case.get("turns"):
            raise ValueError("This focused runner supports single-turn working cases only.")
    selected = [c for c in cases if gate == "all" or c["additional_metadata"]["gate"] == gate]
    if only:
        missing = set(only) - {c["id"] for c in selected}
        if missing:
            raise ValueError("Requested case IDs are absent from the selected gate: "
                             + ", ".join(sorted(missing)))
        selected = [c for c in selected if c["id"] in only]
    if not selected:
        raise ValueError("No matching cases; no gate result can be claimed.")
    return selected


def run_case(case, model, temperature, ollama_url):
    meta = case["additional_metadata"]
    result = {"id": case["id"], "assertion": meta["assertion"],
              "gate": meta["gate"], "required_runs": meta["runs"],
              "rubric_version": meta.get("rubric_version"), "runs": []}
    for number in range(1, meta["runs"] + 1):
        row = {"run": number, "started_at": now(), "passed": False}
        try:
            # Match the course runner's isolated fixture state for each repetition.
            stand.reset()
            answer = stand.chat(case["input"], customer_id=case.get("context", {}).get("customer_id"))
            if not isinstance(answer.get("answer"), str) or not answer.get("request_id"):
                raise ValueError("Stand returned no answer or request_id.")
            trace = stand.trace(answer["request_id"])
            row.update(answer=answer["answer"], request_id=answer["request_id"],
                       trace=trace, tool_calls=stand.tool_calls(trace))
            if meta["assertion"] == "tool_sequence":
                verdict = A.tool_sequence(trace, meta.get("must_include"),
                                          meta.get("must_exclude"),
                                          tuple(meta["before"]) if meta.get("before") else None)
                row.update(passed=verdict.passed, assertion_result=verdict.as_dict())
            else:
                output = judge(case["input"], answer["answer"], meta["rubric"],
                               model, temperature, meta["rubric_version"], ollama_url)
                # A malformed/unsupported verdict or evidence cannot pass a gate.
                row.update(judge=output,
                           passed=output.get("verdict") == "PASS" and not output.get("data_quality_errors"))
            row["status"] = "completed"
        except Exception as exc:
            row.update(status="failed", error=str(exc))
        row["finished_at"] = now()
        result["runs"].append(row)
        print("{} run {}/{}: {}".format(case["id"], number, meta["runs"],
              "PASS" if row["passed"] else "FAIL"), flush=True)
        if row["status"] == "failed":
            break
    result["passed"] = (len(result["runs"]) == meta["runs"]
                        and all(r["status"] == "completed" and r["passed"] for r in result["runs"]))
    return result


def exit_code(rows):
    """Fail closed when any selected case/run is absent, failed or ungraded."""
    return 0 if rows and all(row.get("passed") is True for row in rows) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set", nargs="?", default=os.environ.get("SET", "l09_escalation"))
    parser.add_argument("--gate", choices=["daily", "release", "all"],
                        default=os.environ.get("GATE") or "daily")
    parser.add_argument("--case", action="append", help="Select one ID; may be repeated.")
    parser.add_argument("--expected-profile", default="lesson-09",
                        help="Required active course profile; checks it without changing it.")
    parser.add_argument("--check-only", action="store_true", help="Validate locally; no stand or model calls.")
    args = parser.parse_args()
    try:
        if args.set != "l09_escalation":
            raise ValueError("Use l09_escalation for working gates; use tools/calibrate_run.py for recorded labels.")
        path = ROOT / "sets" / (args.set + ".jsonl")
        cases = working_cases(path, args.gate, set(args.case) if args.case else None)
        coverage = summarise(cases)
        if args.check_only:
            print(json.dumps({"status": "schema_valid", "gate": args.gate,
                              "coverage": coverage, "case_ids": [c["id"] for c in cases],
                              "expected_profile": args.expected_profile,
                              "live_validation_performed": False}, indent=2))
            return 0
        temperature = float(os.environ.get("TEMP", "0.7"))
        if not math.isfinite(temperature) or temperature < 0:
            raise ValueError("TEMP must be finite and nonnegative.")
        judge_cases = [c for c in cases if c["additional_metadata"]["assertion"] == "judge"]
        model = os.environ.get("JUDGE_MODEL", "ollama:qwen2.5:14b")
        ollama_url = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
        runtime = preflight(model, ollama_url) if judge_cases else None
        stand.health()
        profile = stand.profile()
        if profile.get("profile") != args.expected_profile:
            raise ValueError("Active profile differs from --expected-profile: "
                             + repr(profile.get("profile")))
        prompt_version = stand.prompt_version()
    except Exception as exc:
        print("Working gate preflight failed: " + str(exc), file=sys.stderr)
        return 1
    report = {"set": args.set, "set_hash": set_hash(path), "gate": args.gate,
              "started_at": now(), "service_url": stand.BASE,
              "profile": profile, "agent_prompt_version": prompt_version,
              "expected_profile": args.expected_profile,
              "judge_model": model if judge_cases else "not-used",
              "temperature": temperature if judge_cases else None,
              "runtime": runtime, "coverage": coverage,
              "rubric_versions": sorted({c["additional_metadata"]["rubric_version"] for c in judge_cases}),
              "aggregation_rule": "all required runs must PASS with valid evidence; no skipped cases",
              "judge_sampling": "one judge evaluation per fresh agent answer: five answers and five evaluations per judge case",
              "cases": []}
    folder = ROOT / "reports" / "working"
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    target = folder / ("working-" + args.set + "-" + args.gate + "-" + stamp + ".json")
    try:
        for case in cases:
            report["cases"].append(run_case(case, model, temperature, ollama_url))
            target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except KeyboardInterrupt:
        report["interrupted"] = True
    report["finished_at"] = now()
    report["passed"] = sum(row["passed"] for row in report["cases"])
    report["total_required_cases"] = len(cases)
    complete = len(report["cases"]) == len(cases)
    code = exit_code(report["cases"]) if complete and not report.get("interrupted") else 1
    report["status"] = "passed" if code == 0 else "failed"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Report: " + str(target))
    return code


if __name__ == "__main__":
    raise SystemExit(main())

"""Offline comparison of this project's dictionary calibration reports and journals."""
import argparse
import collections
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from judge import parse_output, SYSTEM_SHA256
from calibrate_run import validate_case_trigger


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def wilson(k, n):
    z = 1.96
    p = k / n
    denominator = 1 + z*z/n
    center = (p + z*z/(2*n)) / denominator
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / denominator
    return {"matches": k, "total": n, "agreement": p,
            "lower": center-half, "upper": center+half, "half_width": half}


def audit(path, cases, frozen_sha, rubric_sha):
    report = json.loads(path.read_text())
    if report.get("status") not in ("completed", "completed_with_data_quality_errors"):
        raise ValueError("Report is not complete.")
    for key, value in (("set_sha256", frozen_sha), ("rubric_sha256", rubric_sha),
                       ("system_prompt_sha256", SYSTEM_SHA256)):
        if report.get(key) != value:
            raise ValueError("Input/prompt identity differs: " + key)
    if report.get("runs") != 5 or report.get("cases_completed") != len(cases):
        raise ValueError("Expected a complete five-repeat report.")
    journal = path.with_suffix(".evaluations.jsonl")
    rows = [json.loads(line) for line in journal.read_text().splitlines() if line.strip()]
    if len(rows) != len(cases)*5 or len({(r["id"], r["run"]) for r in rows}) != len(rows):
        raise ValueError("Incomplete or duplicate journal records.")
    if report.get("evaluations_completed") != len(rows) or report.get("attempted_calls") != len(rows):
        raise ValueError("Report call counts differ from its journal.")
    if {r["id"] for r in rows} != set(cases):
        raise ValueError("Journal case IDs differ from the frozen set.")
    per_case = []
    for ident, case in cases.items():
        subset = [r for r in rows if r["id"] == ident]
        if {r["run"] for r in subset} != set(range(1, 6)):
            raise ValueError("Five repeat numbers are required for " + ident)
        for row in subset:
            parsed, errors = parse_output(row["raw_model_response"], case["answer_under_test"])
            result = dict(parsed, data_quality_errors=errors)
            if row.get("backend_metadata", {}).get("done") is not True:
                result["data_quality_errors"].append("backend_response_not_done")
            validate_case_trigger(result, case["additional_metadata"]["criterion_id"])
            errors = result["data_quality_errors"]
            if errors != row["data_quality_errors"] or any(row[k] != v for k, v in parsed.items()):
                raise ValueError("Stored parse differs from raw response: " + ident)
            if (row["status"] != "completed" or row["judge_model"] != report["judge_model"]
                    or row["judge_format"] != report["judge_format"]
                    or row["system_prompt_sha256"] != SYSTEM_SHA256):
                raise ValueError("Unexpected evaluation identity/status: " + ident)
        votes = collections.Counter(r["verdict"] for r in subset)
        valid = collections.Counter(r["verdict"] for r in subset if not r["data_quality_errors"])
        majority = next((v for v in ("PASS", "FAIL") if votes[v] >= 3), None)
        valid_majority = next((v for v in ("PASS", "FAIL") if valid[v] >= 3), None)
        meta = case["additional_metadata"]
        per_case.append({"id": ident, "label": meta["label"], "majority": majority,
                         "valid_majority": valid_majority, "agree": majority == meta["label"],
                         "valid_agree": valid_majority == meta["label"],
                         "stable": len(votes) == 1 and all(r["verdict"] in ("PASS", "FAIL") for r in subset),
                         "group": "disputed" if meta["disputed"] else "obvious_" + meta["label"]})
    agreement = wilson(sum(c["agree"] for c in per_case), len(cases))
    stability = wilson(sum(c["stable"] for c in per_case), len(cases))
    for key in ("matches", "total", "agreement", "lower", "upper"):
        if abs(agreement[key] - report["agreement"][key]) > 1e-12:
            raise ValueError("Stored aggregate differs: " + key)
    elapsed = report["elapsed_seconds"]
    if type(elapsed) not in (int, float) or not math.isfinite(elapsed) or elapsed <= 0:
        raise ValueError("Invalid elapsed time.")
    quotes = [r["quote"] for r in rows]
    return {"model": report["judge_model"], "temperature": report["temperature"],
            "format": report["judge_format"], "agreement": agreement,
            "evidence_valid_agreement": wilson(sum(c["valid_agree"] for c in per_case), len(cases)),
            "self_consistency": stability,
            "groups": {group: wilson(sum(c["agree"] for c in per_case if c["group"] == group),
                                      sum(c["group"] == group for c in per_case))
                       for group in sorted({c["group"] for c in per_case})},
            "false_pass": [c["id"] for c in per_case if c["label"] == "FAIL" and c["majority"] == "PASS"],
            "false_fail": [c["id"] for c in per_case if c["label"] == "PASS" and c["majority"] == "FAIL"],
            "invalid_evaluations": sum(bool(r["data_quality_errors"]) for r in rows),
            "nonempty_quotes": sum(bool(q) for q in quotes),
            "verbatim_nonempty_quotes": sum(bool(r["quote"]) and r["quote"] in cases[r["id"]]["answer_under_test"] for r in rows),
            "empty_quotes": sum(q == "" for q in quotes),
            "evaluations": len(rows), "elapsed_seconds": elapsed, "t_seconds": elapsed/len(rows),
            "cases": per_case}


def compare(first, second):
    raw = (ROOT / "sets/l09_labels_kit_v1.jsonl").read_bytes()
    cases = {c["id"]: c for c in map(json.loads, raw.splitlines())}
    rubric = (ROOT / "rubrics/escalation.rubric.hw08.kit.v1.json").read_bytes()
    a = audit(first, cases, sha(raw), sha(rubric))
    b = audit(second, cases, sha(raw), sha(rubric))
    ac = {c["id"]: c for c in a["cases"]}
    return {"method": "offline strict-parse and case-majority recomputation; no model calls",
            "first": a, "second": b,
            "second_correct_first_wrong": [c["id"] for c in b["cases"] if c["agree"] and not ac[c["id"]]["agree"]],
            "second_wrong_first_correct": [c["id"] for c in b["cases"] if not c["agree"] and ac[c["id"]]["agree"]],
            "wilson_intervals_overlap": max(a["agreement"]["lower"], b["agreement"]["lower"]) <= min(a["agreement"]["upper"], b["agreement"]["upper"]),
            "equivalence_established": False,
            "configuration_differences": {key: [a[key], b[key]] for key in ("model", "temperature", "format") if a[key] != b[key]},
            "caveats": ["Case, not repeat, is the statistical unit.",
                        "Overlap follows the course rule; it is not a paired significance test.",
                        "Different decoder modes compare whole configurations, not model weights alone."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", nargs="?", type=Path,
                        default=ROOT/"reports/l10/cloud/calibration-l09_labels_kit_v1-20261128T101156657431Z.json")
    parser.add_argument("second", nargs="?", type=Path,
                        default=ROOT/"reports/l10/local-7b/calibration-l09_labels_kit_v1-20261128T085923719424Z.json")
    parser.add_argument("--output", type=Path, help="Optional new JSON output; existing files are refused.")
    args = parser.parse_args()
    try:
        result = compare(args.first, args.second)
        if args.output:
            with args.output.open("x", encoding="utf-8") as out:
                json.dump(result, out, ensure_ascii=False, indent=2)
                out.write("\n")
        print(json.dumps({"first": {k: result["first"][k] for k in ("model", "format", "agreement", "t_seconds")},
                          "second": {k: result["second"][k] for k in ("model", "format", "agreement", "t_seconds")},
                          "wilson_intervals_overlap": result["wilson_intervals_overlap"],
                          "configuration_differences": result["configuration_differences"]}, ensure_ascii=False, indent=2))
    except Exception as exc:
        print("Comparison stopped: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

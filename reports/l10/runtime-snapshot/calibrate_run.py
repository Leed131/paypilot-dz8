"""Calibrate the frozen 30-case HW08 set, evaluating each recorded answer five times.

Native Python, no dependencies or bank stand required. Run --check-only first.
Human labels are compared locally and never sent to the model.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

if sys.version_info < (3, 8):
    raise SystemExit("Python 3.8 or newer is required. No model was called.")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from judge import SYSTEM_SHA256, SYSTEM_VERSION, judge, preflight, judge_format

SET_CONFIGS = {
    "l09_labels": {
        "rubric_version": "rubric.hw08.kit.v1.1",
        "rubric_path": "rubrics/escalation.rubric.hw08.kit.v1.1.json",
        "casewise": True,
        "reference_manifest_path": "annotations/accepted-reference-manifest.kit-v1_1.json",
    },
    "l09_labels_kit_v1": {
        "rubric_version": "rubric.hw08.kit.v1",
        "rubric_path": "rubrics/escalation.rubric.hw08.kit.v1.json",
        "casewise": True,
        "reference_manifest_path": "annotations/accepted-reference-manifest.kit-v1.json",
    },
    "l09_labels_kit_v1_1": {
        "rubric_version": "rubric.hw08.kit.v1.1",
        "rubric_path": "rubrics/escalation.rubric.hw08.kit.v1.1.json",
        "casewise": True,
        "reference_manifest_path": "annotations/accepted-reference-manifest.kit-v1_1.json",
    },
    "l09_labels_v1": {
        "rubric_version": "rubric.hw08.v1",
        "rubric_path": "rubrics/escalation.rubric.hw08.v1.json",
    },
    "l09_labels_v1_1": {
        "rubric_version": "rubric.hw08.v1.1",
        "rubric_path": "rubrics/escalation.rubric.hw08.v1.1.json",
    },
}

# These exact inputs contain assistant-authored answers. They remain available
# only for explicit historical reproduction, not actual-agent calibration.
LEGACY_SYNTHETIC_SET_HASHES = {
    "1989b89aec406c04727abecbc966e30cbfacef54ca7e863d75216615cce5a084",
    "28cb41ff169aa346463d726085d5d88fa431c16b415f7db1ef36419da69a18eb",
}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def wilson(k, n):
    if not n:
        return {"matches": k, "total": n, "agreement": None, "lower": None,
                "upper": None, "half_width": None, "plus_minus_percentage_points": None}
    p, z = k / n, 1.96
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return {"matches": k, "total": n, "agreement": p, "lower": centre - half,
            "upper": centre + half, "half_width": half,
            "plus_minus_percentage_points": half * 100}


def group_of(case):
    meta = case["additional_metadata"]
    return "disputed" if meta["disputed"] else "obvious_" + meta["label"]


def git(*args, binary=False):
    result = subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout if binary else result.stdout.decode("utf-8").strip()


def load_frozen_set(name):
    if name not in SET_CONFIGS:
        raise ValueError("Unknown frozen set. Choose one of: " + ", ".join(SET_CONFIGS))
    config = SET_CONFIGS[name]
    expected_version = config["rubric_version"]
    canonical = ROOT / "evals/sets" / (name + ".jsonl")
    compatibility = ROOT / "sets" / (name + ".jsonl")
    data = canonical.read_bytes()
    if compatibility.read_bytes() != data:
        raise ValueError("Canonical and compatibility label files differ; stop before judging.")
    cases = [json.loads(line) for line in data.decode("utf-8").splitlines() if line.strip()]
    if len(cases) != 30 or len({c["id"] for c in cases}) != 30:
        raise ValueError("Expected exactly 30 unique cases.")
    versions = set()
    for case in cases:
        meta = case["additional_metadata"]
        if meta.get("label") not in ("PASS", "FAIL") or type(meta.get("disputed")) is not bool:
            raise ValueError("Invalid human annotation: " + case["id"])
        if not case.get("input") or not case.get("answer_under_test") or not meta.get("rubric"):
            raise ValueError("Incomplete recorded fixture: " + case["id"])
        if meta.get("assertion") != "judge" or meta.get("runs") != 5 or meta.get("gate") != "release":
            raise ValueError("Invalid run/gate metadata: " + case["id"])
        if not meta.get("why_disputed" if meta["disputed"] else "ground_truth_from"):
            raise ValueError("Missing annotation explanation: " + case["id"])
        versions.add(meta.get("rubric_version"))
    groups = Counter(group_of(c) for c in cases)
    if groups != {"obvious_PASS": 10, "obvious_FAIL": 10, "disputed": 10}:
        raise ValueError("Expected exact 10/10/10 groups: " + str(groups))
    if versions != {expected_version}:
        raise ValueError("Unexpected rubric versions: " + str(versions))
    rubric_path = ROOT / config["rubric_path"]
    rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
    if rubric.get("version") != expected_version:
        raise ValueError("Packaged rubric version differs from case metadata.")
    source_metadata = {}
    acceptance_paths = []
    if config.get("casewise"):
        source_metadata = validate_casewise_rubric(cases, rubric)
        acceptance_paths, acceptance_metadata = validate_reference_acceptance(
            cases, data, rubric_path, config, source_metadata)
        source_metadata.update(acceptance_metadata)
    elif any(c["additional_metadata"]["rubric"] != rubric.get("instruction") for c in cases):
        raise ValueError("Per-case rubric text differs from the packaged rubric.")
    # A real repository commit must already contain the exact bytes being evaluated.
    repo_root = Path(git("rev-parse", "--show-toplevel")).resolve()
    checked_paths = []
    for path in [canonical, compatibility, rubric_path] + acceptance_paths:
        rel = path.relative_to(repo_root).as_posix()
        git("ls-files", "--error-unmatch", "--", rel)
        if git("show", "HEAD:" + rel, binary=True) != path.read_bytes():
            raise ValueError("Uncommitted or changed frozen input: " + rel)
        checked_paths.append(rel)
    label_paths = checked_paths[:2]
    # This hash excludes rubric wording/version and compares the frozen human
    # fixture/label content across procedural rubric revisions. The casewise
    # family also freezes the semantic criterion: it is part of the reference,
    # unlike procedural instruction wording.
    fixture_labels = [
        {"id": case["id"], "input": case["input"],
         "answer_under_test": case["answer_under_test"],
         "label": case["additional_metadata"]["label"],
         "disputed": case["additional_metadata"]["disputed"],
         **({"criterion": case["additional_metadata"]["criterion"]}
            if config.get("casewise") else {})}
        for case in sorted(cases, key=lambda item: item["id"])
    ]
    fixture_label_data = json.dumps(fixture_labels, ensure_ascii=False,
                                   sort_keys=True, separators=(",", ":")).encode("utf-8")
    return cases, {"set": name, "set_sha256": sha256(data),
        "set_hash": sha256(data)[:12], "rubric_version": expected_version,
        "fixture_label_sha256": sha256(fixture_label_data),
        "rubric_sha256": sha256(rubric_path.read_bytes()),
        "git_head": git("rev-parse", "HEAD"),
        "git_annotation_commit": git("log", "-1", "--format=%H", "HEAD", "--", *label_paths),
        "git_verified_input_paths": checked_paths, "group_sizes": dict(groups),
        **source_metadata}


def validate_casewise_rubric(cases, rubric):
    """Validate frozen per-case criteria and accepted reference provenance."""
    variants = rubric.get("criterion_variants")
    expected_ids = {"human_handoff", "no_outcome_promise",
                    "no_internal_review_reason", "combined"}
    if (not isinstance(variants, dict) or set(variants) != expected_ids
            or any(not isinstance(value, str) or not value.strip()
                   for value in variants.values())):
        raise ValueError("Casewise rubric must define the four expected criteria.")
    template = rubric.get("instruction_template")
    if not isinstance(template, str) or template.count("{criterion}") != 1:
        raise ValueError("Casewise rubric needs exactly one {criterion} placeholder.")
    triggers = rubric.get("triggers", [])
    trigger_ids = [item.get("id") if isinstance(item, dict) else item for item in triggers]
    if (len(trigger_ids) != 3 or set(trigger_ids) != expected_ids - {"combined"}):
        raise ValueError("Casewise rubric must retain the three supported triggers.")
    if len({(case["input"], case["answer_under_test"]) for case in cases}) != len(cases):
        raise ValueError("Duplicate recorded question/answer pairs in casewise set.")
    prompt_versions = {}
    source_kinds = {}
    criterion_ids = {}
    reference_origins = Counter()
    for case in cases:
        meta = case["additional_metadata"]
        ident = case["id"]
        criterion_id = meta.get("criterion_id")
        if criterion_id not in variants or meta.get("criterion") != variants[criterion_id]:
            raise ValueError("Case criterion differs from the packaged variant: " + ident)
        try:
            instruction = template.format(criterion=variants[criterion_id])
        except (KeyError, ValueError, IndexError) as exc:
            raise ValueError("Invalid casewise instruction template: " + str(exc))
        if meta.get("rubric") != instruction:
            raise ValueError("Per-case rubric differs from the packaged template: " + ident)
        if meta.get("reference_status") != "student_accepted":
            raise ValueError("Reference is not accepted by the student: " + ident)
        origin = meta.get("reference_origin")
        if origin not in {"prior_human", "assistant_proposed_student_accepted_in_batch"}:
            raise ValueError("Unsupported accepted-reference origin: " + ident)
        kind = meta.get("source_kind")
        prompt_version = meta.get("producing_agent_prompt_version")
        if kind == "authorized_course_kit":
            if prompt_version != "not_provided_in_authorized_kit":
                raise ValueError("Do not attribute a live bank prompt to kit answers: " + ident)
        elif kind == "live_course_agent":
            if (not isinstance(prompt_version, str) or not prompt_version.strip()
                    or prompt_version in {"not_provided_in_authorized_kit",
                                          "not_applicable_recorded_fixtures"}):
                raise ValueError("Missing producing prompt version for live answer: " + ident)
        else:
            raise ValueError("Casewise calibration requires kit or actual-agent source: " + ident)
        prompt_versions[ident] = prompt_version
        source_kinds[ident] = kind
        criterion_ids[ident] = criterion_id
        reference_origins[origin] += 1
    distinct_versions = set(prompt_versions.values())
    return {"calibration_scope": "per_case_criteria_authorized_kit_and_recorded_agent",
            "agent_prompt_version": (next(iter(distinct_versions)) if len(distinct_versions) == 1
                                     else "mixed_per_case_source_provenance"),
            "agent_prompt_versions_by_case": prompt_versions,
            "source_kinds_by_case": source_kinds,
            "source_kind_counts": dict(Counter(source_kinds.values())),
            "criterion_ids_by_case": criterion_ids,
            "reference_origin_counts": dict(reference_origins)}


def validate_reference_acceptance(cases, data, rubric_path, config, source_metadata):
    """Bind accepted references to the recorded student adoption and exact set."""
    manifest_path = ROOT / config["reference_manifest_path"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected = {"set_sha256": sha256(data), "cases": len(cases),
                "rubric_version": config["rubric_version"],
                "rubric_sha256": sha256(rubric_path.read_bytes()),
                "groups": dict(Counter(group_of(case) for case in cases)),
                "source_counts": source_metadata["source_kind_counts"],
                "reference_origin_counts": source_metadata["reference_origin_counts"],
                "criterion_counts": dict(Counter(source_metadata["criterion_ids_by_case"].values()))}
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise ValueError("Accepted-reference manifest differs from frozen " + key + ".")
    adoption_rel = manifest.get("student_acceptance_record")
    if not isinstance(adoption_rel, str) or not adoption_rel:
        raise ValueError("Accepted-reference manifest needs a student acceptance record.")
    adoption_path = (ROOT / adoption_rel).resolve()
    if ROOT.resolve() not in adoption_path.parents:
        raise ValueError("Student acceptance record must be inside the repository.")
    adoption = json.loads(adoption_path.read_text(encoding="utf-8"))
    if adoption.get("event") != "student_batch_acceptance" or not adoption.get("recorded_at"):
        raise ValueError("Invalid student acceptance record.")
    counts = source_metadata["reference_origin_counts"]
    if (adoption.get("prior_human_references_preserved") != counts.get("prior_human", 0)
            or adoption.get("assistant_proposals_adopted")
            != counts.get("assistant_proposed_student_accepted_in_batch", 0)):
        raise ValueError("Student acceptance counts differ from the accepted set.")
    for case in cases:
        meta = case["additional_metadata"]
        if (meta.get("reference_adoption") != adoption_rel
                or meta.get("reference_adopted_at") != adoption["recorded_at"]):
            raise ValueError("Case does not refer to the recorded student adoption: " + case["id"])
    draft_rel = adoption.get("accepted_draft_file")
    if not isinstance(draft_rel, str) or not draft_rel:
        raise ValueError("Student acceptance record needs the accepted draft path.")
    draft_path = (ROOT / draft_rel).resolve()
    if ROOT.resolve() not in draft_path.parents:
        raise ValueError("Accepted draft must be inside the repository.")
    if sha256(draft_path.read_bytes()) != adoption.get("accepted_draft_sha256"):
        raise ValueError("Accepted draft bytes differ from the student acceptance record.")
    reviewed_cases = [json.loads(line) for line in draft_path.read_text(encoding="utf-8").splitlines()
                      if line.strip()]
    if (len(reviewed_cases) != len(cases)
            or len({case["id"] for case in reviewed_cases}) != len(reviewed_cases)
            or {case["id"] for case in reviewed_cases} != {case["id"] for case in cases}):
        raise ValueError("Accepted set IDs differ from the reviewed draft.")
    reviewed_by_id = {case["id"]: case for case in reviewed_cases}
    for case in cases:
        ident = case["id"]
        reviewed = reviewed_by_id[ident]
        annotation = reviewed["annotation"]
        meta = case["additional_metadata"]
        for field in ("input", "answer_under_test", "context"):
            if case.get(field) != reviewed.get(field):
                raise ValueError("Reviewed draft " + field + " differs from accepted case: " + ident)
        if case.get("provenance") != reviewed.get("source"):
            raise ValueError("Reviewed draft provenance differs from accepted case: " + ident)
        if meta.get("criterion") != reviewed.get("criterion"):
            raise ValueError("Reviewed draft semantic criterion differs from accepted case: " + ident)
        if meta.get("label") != annotation.get("label"):
            raise ValueError("Reviewed draft label differs from accepted case: " + ident)
        disputed = annotation.get("disputed")
        if disputed is None:
            disputed = annotation.get("proposed_disputed")
        if type(disputed) is not bool or meta.get("disputed") != disputed:
            raise ValueError("Reviewed draft disputed flag differs from accepted case: " + ident)
        prior_human = annotation.get("human_confirmed")
        if type(prior_human) is not bool:
            raise ValueError("Reviewed draft lacks reference-origin confirmation: " + ident)
        expected_origin = ("prior_human" if prior_human
                           else "assistant_proposed_student_accepted_in_batch")
        if meta.get("reference_origin") != expected_origin:
            raise ValueError("Reviewed draft reference origin differs from accepted case: " + ident)
        labeled_on = (annotation.get("original_labeled_on") if prior_human
                      else adoption["recorded_at"][:10])
        if not labeled_on or meta.get("labeled_on") != labeled_on:
            raise ValueError("Reviewed draft annotation date differs from accepted case: " + ident)
        source = reviewed["source"]
        source_kind = source.get("kind", source.get("source"))
        prompt_version = source.get("producing_agent_prompt_version", source.get("agent_prompt_version"))
        if (meta.get("source_kind") != source_kind
                or meta.get("producing_agent_prompt_version") != prompt_version):
            raise ValueError("Reviewed draft producing provenance differs from accepted case: " + ident)
    return [manifest_path, adoption_path, draft_path], {
        "accepted_reference_manifest": config["reference_manifest_path"],
        "accepted_reference_manifest_sha256": sha256(manifest_path.read_bytes()),
        "student_acceptance_record": adoption_rel,
        "student_acceptance_record_sha256": sha256(adoption_path.read_bytes()),
        "student_acceptance_recorded_at": adoption["recorded_at"],
        "accepted_draft_sha256": adoption["accepted_draft_sha256"]}


def configuration():
    runs = int(os.environ.get("RUNS", "5"))
    if runs != 5:
        raise ValueError("HW08 requires RUNS=5; refusing a different run count.")
    temperature = float(os.environ.get("TEMP", "0"))
    if not math.isfinite(temperature) or temperature < 0:
        raise ValueError("TEMP must be a finite, nonnegative number.")
    return {"judge_model": os.environ.get("JUDGE_MODEL", "ollama:qwen2.5:14b"),
            "ollama_url": os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434"),
            "temperature": temperature, "runs": runs, "judge_format": judge_format(),
            "agent_prompt_version": os.environ.get("AGENT_PROMPT_VERSION", "not_applicable_recorded_fixtures"),
            "system_prompt_version": SYSTEM_VERSION, "system_prompt_sha256": SYSTEM_SHA256}


def majority(rows, evidence_valid=False):
    votes = Counter(r.get("verdict") for r in rows
                    if r.get("verdict") in ("PASS", "FAIL")
                    and (not evidence_valid or not r.get("data_quality_errors")))
    # The denominator remains the required five calls, even when some outputs are invalid.
    for verdict in ("PASS", "FAIL"):
        if votes[verdict] >= 3:
            return verdict
    return None


def validate_case_trigger(result, criterion_id):
    """Flag valid enum values that nevertheless address an unstated condition."""
    if (result.get("verdict") == "FAIL" and not result.get("data_quality_errors")
            and criterion_id != "combined" and result.get("trigger") != criterion_id):
        result["data_quality_errors"] = ["trigger_outside_case_criterion"]
    return result


def summarize(cases, evaluations):
    by_id = {c["id"]: [] for c in cases}
    for row in evaluations:
        by_id[row["id"]].append(row)
    rows = []
    for case in cases:
        observations = by_id[case["id"]]
        if len(observations) != 5 or any(r.get("status") != "completed" for r in observations):
            continue
        meta = case["additional_metadata"]
        pred = majority(observations)
        clean_pred = majority(observations, evidence_valid=True)
        rows.append({"id": case["id"], "label": meta["label"], "disputed": meta["disputed"],
                     "group": group_of(case), "verdicts": [r.get("verdict") for r in observations],
                     "majority": pred, "evidence_valid_majority": clean_pred,
                     "agree": pred == meta["label"], "evidence_valid_agree": clean_pred == meta["label"],
                     "stable": all(r.get("verdict") in ("PASS", "FAIL") for r in observations)
                               and len({r.get("verdict") for r in observations}) == 1,
                     "data_quality_errors": [dict(run=r["run"], errors=r["data_quality_errors"])
                                              for r in observations if r.get("data_quality_errors")]})
    matrix = {"positive_class": "FAIL", "true_positive": 0, "false_negative_miss": 0,
              "false_positive_false_alarm": 0, "true_negative": 0, "unresolved": 0}
    for row in rows:
        actual, predicted = row["label"], row["majority"]
        key = ("unresolved" if predicted is None else
               "true_positive" if actual == predicted == "FAIL" else
               "true_negative" if actual == predicted == "PASS" else
               "false_negative_miss" if actual == "FAIL" else "false_positive_false_alarm")
        matrix[key] += 1
    groups = {}
    for group in ("obvious_PASS", "obvious_FAIL", "disputed"):
        members = [r for r in rows if r["group"] == group]
        groups[group] = {"raw_verdict_agreement": wilson(sum(r["agree"] for r in members), len(members)),
                         "evidence_valid_agreement": wilson(sum(r["evidence_valid_agree"] for r in members), len(members))}
    stable_cases = sum(row["stable"] for row in rows)
    return {"cases_completed": len(rows), "cases": rows,
            "agreement": wilson(sum(r["agree"] for r in rows), len(rows)),
            "evidence_valid_agreement": wilson(sum(r["evidence_valid_agree"] for r in rows), len(rows)),
            "self_consistency": {"stable_cases": stable_cases, "total_cases": len(rows),
                                 "wilson_95": wilson(stable_cases, len(rows))},
            "groups": groups, "confusion_matrix": matrix,
            "disagreements": [r for r in rows if not r["agree"]],
            "unresolved_case_ids": [r["id"] for r in rows if r["majority"] is None],
            "invalid_evaluation_count": sum(bool(r.get("data_quality_errors")) for r in evaluations),
            "metrics_note": "Raw verdict agreement uses a majority of at least 3/5 binary verdicts, including verdicts whose evidence is invalid. Evidence-valid agreement requires at least 3/5 outputs with no schema/evidence errors. Unresolved cases count as non-matches, not as substituted labels. Partial-run metrics describe only fully evaluated cases and are not final 30-case results."}


def save_report(path, report):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set", nargs="?", default="l09_labels")
    parser.add_argument("--check-only", action="store_true", help="Check committed inputs, endpoint and installed model; never generate.")
    parser.add_argument("--allow-legacy-fixtures", action="store_true",
                        help="Explicitly permit historical synthetic inputs; does not satisfy actual-agent calibration.")
    args = parser.parse_args()
    try:
        cases, metadata = load_frozen_set(args.set)
        if metadata["set_sha256"] in LEGACY_SYNTHETIC_SET_HASHES and not args.allow_legacy_fixtures:
            raise ValueError("This is the legacy assistant-authored set, not actual-agent calibration. "
                             "Finish and freeze real-agent/authorized-kit labels first. "
                             "Use --allow-legacy-fixtures only for intentional historical reproduction.")
        settings = configuration()
        if "agent_prompt_versions_by_case" in metadata:
            # Frozen case provenance, not an environment override, defines the
            # producing versions of a mixed kit/live dataset.
            settings["agent_prompt_version"] = metadata["agent_prompt_version"]
        runtime = preflight(settings["judge_model"], settings["ollama_url"])
    except Exception as exc:
        print("Preflight failed: " + str(exc), file=sys.stderr)
        return 1
    if args.check_only:
        print(json.dumps({"status": "ready", "planned_evaluations": 150,
                          "model_generation_performed": False, **metadata, **settings,
                          "runtime": runtime}, ensure_ascii=False, indent=2))
        return 0
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    directory = ROOT / "reports"
    directory.mkdir(exist_ok=True)
    report_path = directory / f"calibration-{args.set}-{stamp}.json"
    journal_path = directory / f"calibration-{args.set}-{stamp}.evaluations.jsonl"
    report = {"status": "running", "started_at": utc_now(), "planned_evaluations": 150,
              **metadata, **settings, "runtime": runtime, "evaluation_journal": journal_path.name,
              "evaluations_completed": 0, "attempted_calls": 0,
              "unit_of_agreement": "case majority; 150 evaluations are not 150 independent cases"}
    run_started = time.perf_counter()
    evaluations = []
    save_report(report_path, report)
    try:
        with journal_path.open("x", encoding="utf-8") as journal:
            for case in cases:
                meta = case["additional_metadata"]
                for run in range(1, 6):
                    row = {"id": case["id"], "run": run, "started_at": utc_now()}
                    report["attempted_calls"] += 1
                    call_started = time.perf_counter()
                    try:
                        result = judge(case["input"], case["answer_under_test"], meta["rubric"],
                                       settings["judge_model"], settings["temperature"],
                                       meta["rubric_version"], settings["ollama_url"])
                        if SET_CONFIGS[args.set].get("casewise"):
                            validate_case_trigger(result, meta["criterion_id"])
                        row.update(result, status="completed", finished_at=utc_now())
                        report["evaluations_completed"] += 1
                    except BaseException as exc:
                        row.update(status="failed", finished_at=utc_now(), error=str(exc),
                                   data_quality_errors=["model_call_failed"])
                        raise
                    finally:
                        row["elapsed_seconds"] = time.perf_counter() - call_started
                        quote = row.get("quote")
                        row["quote_found"] = (bool(quote) and quote in case["answer_under_test"]) if isinstance(quote, str) else False
                        evaluations.append(row)
                        report["elapsed_seconds"] = time.perf_counter() - run_started
                        report["mean_call_seconds"] = sum(x["elapsed_seconds"] for x in evaluations) / len(evaluations)
                        report["quote_found_count"] = sum(x["quote_found"] for x in evaluations)
                        report["quote_check_note"] = "Empty quotes are counted separately; an allowed missing-handoff quote is not a fabricated quote. Substring presence does not establish semantic correctness."
                        report["empty_quote_count"] = sum(x.get("quote") == "" for x in evaluations)
                        journal.write(json.dumps(row, ensure_ascii=False) + "\n")
                        journal.flush()
                        os.fsync(journal.fileno())
                        report.update(summarize(cases, evaluations))
                        save_report(report_path, report)
                    print(f"{case['id']} run {run}/5: {row.get('verdict')}"
                          + (" [invalid evidence/schema]" if row.get("data_quality_errors") else ""), flush=True)
        report["status"] = ("completed_with_data_quality_errors" if report["invalid_evaluation_count"]
                            else "completed")
        report["finished_at"] = utc_now()
        save_report(report_path, report)
        print("Report: " + str(report_path))
        print(json.dumps({k: report[k] for k in ("status", "agreement", "evidence_valid_agreement", "self_consistency", "confusion_matrix")}, indent=2))
        return 2 if report["invalid_evaluation_count"] else 0
    except BaseException as exc:
        report.update(status="failed", finished_at=utc_now(), error=str(exc),
                      failure_type=type(exc).__name__)
        save_report(report_path, report)
        print("Calibration stopped; partial results preserved: " + str(report_path), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

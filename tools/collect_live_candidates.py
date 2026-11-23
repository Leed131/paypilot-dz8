"""Collect genuine course-agent answers before human labelling or judge calls.

Run only against the course test stand: fixture state is reset for each question.
Outputs are new, uniquely named collections; existing homework is not modified.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import uuid

if sys.version_info < (3, 8):
    raise SystemExit("Python 3.8 or newer is required.")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import stand

EXPECTED_PROFILE = "lesson-09"
EXPECTED_DEFECTS = {"D18", "D25", "D27"}
FORBIDDEN = {"label", "disputed", "expected_label", "expected_group", "intended_group", "why_disputed", "ground_truth_from"}


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def save_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def append(handle, value):
    handle.write(json.dumps(value, ensure_ascii=False) + "\n")
    handle.flush()
    os.fsync(handle.fileno())


def unlabelled(value):
    if isinstance(value, dict):
        if FORBIDDEN.intersection(value):
            raise ValueError("Question pool must not contain labels or intended groups.")
        for child in value.values():
            unlabelled(child)
    elif isinstance(value, list):
        for child in value:
            unlabelled(child)


def questions(path):
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not rows or len({r["id"] for r in rows}) != len(rows):
        raise ValueError("Question pool must have unique IDs and at least one question.")
    for row in rows:
        unlabelled(row)
        customer = row.get("context", {}).get("customer_id")
        if not isinstance(row.get("id"), str) or not re.fullmatch(r"LIVE-C[0-9]{3,}", row["id"]):
            raise ValueError("Candidate IDs must use the safe LIVE-C001 naming format.")
        if not isinstance(row.get("input"), str) or not row["input"].strip() or not isinstance(customer, str) or not customer:
            raise ValueError("Each question needs input and context.customer_id.")
        if not row["input"].startswith(customer + " "):
            raise ValueError("Input must start with its customer-ID prefix: " + row["id"])
        if "answer_under_test" in row:
            raise ValueError("Question pool must not contain a prewritten answer.")
    return rows


def configuration():
    profile = stand.profile()
    if profile.get("profile") != EXPECTED_PROFILE or set(profile.get("active", [])) != EXPECTED_DEFECTS:
        raise ValueError("Required course profile is lesson-09 with exactly D18,D25,D27. No configuration was changed.")
    prompt = stand._call("GET", "/api/_test/prompt")
    if not isinstance(prompt.get("version"), str) or not prompt["version"] or not isinstance(prompt.get("text"), str) or not prompt["text"]:
        raise ValueError("Stand must return the actual prompt version and full prompt text.")
    return {"observed_at": now(), "profile": profile, "agent_prompt": prompt,
            "agent_prompt_version": prompt["version"], "prompt_text_sha256": digest(prompt["text"]),
            "configuration_key": {"profile": profile["profile"], "active_defects": sorted(profile["active"]),
                                  "prompt_version": prompt["version"], "prompt_sha256": digest(prompt["text"])}}


def trace_prompt_versions(trace):
    found = []
    for span in stand.spans(trace):
        attributes = span.get("attributes") or {}
        for key in ("prompt.version", "agent.prompt.version", "gen_ai.prompt.version"):
            value = attributes.get(key)
            if value is not None:
                found.append({"span": span.get("name"), "attribute": key, "version": value})
    return found


def markdown(candidates):
    lines = ["# Live course-agent answers for human review", "",
             "These are unlabelled candidates. No judge was called and no class is suggested. Human assessment must precede judge evaluation.", ""]
    for row in candidates:
        lines += ["## " + row["id"], "", "**Customer question**", "", row["input"], "",
                  "**Recorded agent answer**", "", row["answer_under_test"], ""]
    return "\n".join(lines)


def git_head():
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], stderr=subprocess.DEVNULL).decode().strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", type=Path, default=ROOT / "sets/l09_candidate_questions.jsonl")
    parser.add_argument("--limit", type=int, help="Collect only the first N questions, without assuming their future labels.")
    parser.add_argument("--check-only", action="store_true", help="Validate the question file offline; no requests or state changes.")
    parser.add_argument("--preflight-only", action="store_true", help="Read health/profile/prompt only; no reset or agent request.")
    args = parser.parse_args()
    try:
        pool = questions(args.questions)
        if args.limit is not None:
            if not 1 <= args.limit <= len(pool):
                raise ValueError("--limit must be between 1 and the question-pool size.")
            pool = pool[:args.limit]
        if args.check_only:
            print(json.dumps({"status": "question_schema_valid", "planned_candidates": len(pool),
                              "stand_requests": 0, "judge_calls": 0, "labels_assigned": 0}, indent=2))
            return 0
        health = stand.health()
        initial = configuration()
        if args.preflight_only:
            print(json.dumps({"status": "ready", "service_url": stand.BASE, "planned_candidates": len(pool),
                              "profile": initial["profile"]["profile"], "agent_prompt_version": initial["agent_prompt_version"],
                              "prompt_text_sha256": initial["prompt_text_sha256"], "chat_requests": 0,
                              "state_reset": False, "judge_calls": 0}, indent=2))
            return 0
    except Exception as exc:
        print("Collection preflight failed: " + str(exc), file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + "-" + uuid.uuid4().hex[:8]
    folder = ROOT / "data/live-candidates" / stamp
    (folder / "sources").mkdir(parents=True, exist_ok=False)
    save_json(folder / "sources/initial-configuration.json", initial)
    manifest = {"status": "running", "started_at": now(), "service_url": stand.BASE,
                "question_file": str(args.questions), "question_file_sha256": hashlib.sha256(args.questions.read_bytes()).hexdigest(),
                "collector_git_commit": git_head(), "planned_candidates": len(pool), "case_attempts": 0,
                "selected_question_ids": [q["id"] for q in pool],
                "chat_requests_attempted": 0, "accepted_candidates": 0, "judge_calls": 0, "labels_assigned": 0,
                "health": health, "initial_configuration": {k: initial[k] for k in
                    ["observed_at", "profile", "agent_prompt_version", "prompt_text_sha256", "configuration_key"]},
                "initial_configuration_source": "sources/initial-configuration.json",
                "provenance_note": "Prompt/profile are checked before and after every call; trace prompt-version evidence is checked when exposed. No unobserved producing-model identity is invented.",
                "files": {"candidates": "candidates.jsonl", "journal": "collection-journal.jsonl", "review": "review.md", "sources": "sources/"}}
    candidates = []
    save_json(folder / "collection-manifest.json", manifest)
    failed = False
    with (folder / "candidates.jsonl").open("x", encoding="utf-8") as accepted, (folder / "collection-journal.jsonl").open("x", encoding="utf-8") as journal:
        for question in pool:
            source = {"id": question["id"], "started_at": now(), "input": question["input"], "context": question["context"]}
            manifest["case_attempts"] += 1
            manifest["active_candidate"] = question["id"]
            save_json(folder / "collection-manifest.json", manifest)
            print("Requesting {} ({}/{}); no judge is being called.".format(
                question["id"], manifest["case_attempts"], len(pool)), flush=True)
            try:
                source["reset_result"] = stand.reset()
                source["before"] = configuration()
                if source["before"]["configuration_key"] != initial["configuration_key"]:
                    raise ValueError("Configuration changed before the request.")
                save_json(folder / "sources" / (question["id"] + ".json"), source)
                manifest["chat_requests_attempted"] += 1
                save_json(folder / "collection-manifest.json", manifest)
                response = stand.chat(question["input"], session_id=None, customer_id=question["context"]["customer_id"])
                source["raw_response"] = response
                save_json(folder / "sources" / (question["id"] + ".json"), source)
                if not isinstance(response.get("answer"), str) or not response["answer"].strip() or not response.get("request_id"):
                    raise ValueError("Agent response is missing answer or request_id.")
                source["trace"] = stand.trace(response["request_id"])
                source["after"] = configuration()
                if source["after"]["configuration_key"] != source["before"]["configuration_key"]:
                    raise ValueError("Configuration changed during the request.")
                versions = trace_prompt_versions(source["trace"])
                source["trace_prompt_versions"] = versions
                if any(v["version"] != source["before"]["agent_prompt_version"] for v in versions):
                    raise ValueError("Trace prompt version does not match the observed producing configuration.")
                if response.get("prompt_version") not in (None, source["before"]["agent_prompt_version"]):
                    raise ValueError("Response prompt version does not match the observed configuration.")
                candidate = {"id": question["id"], "input": question["input"], "answer_under_test": response["answer"],
                             "context": question["context"], "provenance": {
                                 "source": "live_course_agent", "request_id": response["request_id"], "session_id": response.get("session_id"),
                                 "collected_on": now(), "profile": EXPECTED_PROFILE,
                                 "agent_prompt_version": source["before"]["agent_prompt_version"], "prompt_text_sha256": source["before"]["prompt_text_sha256"],
                                 "prompt_version_evidence": "configuration_before_after_and_trace" if versions else "configuration_before_after_only",
                                 "source_file": "sources/" + question["id"] + ".json"}}
                models = [a.get("gen_ai.request.model") or a.get("gen_ai.response.model") for a in stand.llm_calls(source["trace"])]
                candidate["provenance"]["observed_agent_models"] = sorted({x for x in models if isinstance(x, str) and x})
                candidates.append(candidate)
                append(accepted, candidate)
                manifest["accepted_candidates"] += 1
                source["status"] = "accepted"
            except BaseException as exc:
                source.update(status="rejected", error=str(exc), error_type=type(exc).__name__)
                manifest.update(status="failed", error=str(exc), error_type=type(exc).__name__)
                failed = True
            finally:
                source["finished_at"] = now()
                save_json(folder / "sources" / (question["id"] + ".json"), source)
                append(journal, {k: source.get(k) for k in ["id", "status", "started_at", "finished_at", "error", "error_type"]})
                save_json(folder / "collection-manifest.json", manifest)
                (folder / "review.md").write_text(markdown(candidates), encoding="utf-8")
            print("Collected {}/{}: {} ({})".format(manifest["accepted_candidates"], len(pool), question["id"], source["status"]), flush=True)
            if failed:
                break
    manifest.update(status="failed" if failed else "completed", finished_at=now())
    manifest.pop("active_candidate", None)
    save_json(folder / "collection-manifest.json", manifest)
    print("Collection: " + str(folder))
    print("Attach candidates.jsonl and collection-manifest.json for the next human-labelling step. No judge was called.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

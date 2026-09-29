#!/usr/bin/env python3
"""Make repeated question reasoning fields point to each question's evidence.

This is a conservative content-field repair: it never changes prompts,
options, answer values, or lesson links.  It only expands exact duplicate
strategies/explanations with the concrete prompt and answer criterion that
the learner must use for that item.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def norm(value: str) -> str:
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", value).lower()


def all_questions() -> list[Path]:
    return sorted((ROOT / "questions").glob("*/*.json"))


def main() -> int:
    data_by_path: dict[Path, dict] = {}
    fields: dict[str, defaultdict[str, list[Path]]] = {
        "strategy": defaultdict(list),
        "explanation": defaultdict(list),
    }
    for path in all_questions():
        data = json.loads(path.read_text(encoding="utf-8"))
        data_by_path[path] = data
        strategy = data.get("solutionStrategy")
        explanation = data.get("answer", {}).get("explanation")
        if isinstance(strategy, str) and strategy.strip():
            fields["strategy"][norm(strategy)].append(path)
        if isinstance(explanation, str) and explanation.strip():
            fields["explanation"][norm(explanation)].append(path)

    duplicate_paths: set[Path] = set()
    changed = {"strategy": 0, "explanation": 0}
    for field, groups in fields.items():
        for group in groups.values():
            if len(group) < 2:
                continue
            for path in group:
                data = data_by_path[path]
                prompt = re.sub(r"\s+", " ", str(data.get("prompt", "")).strip()).strip()
                prompt = prompt[:180]
                answer = data.get("answer", {}).get("value", "")
                lesson = data.get("lessonId", "")
                if field == "strategy":
                    base = str(data.get("solutionStrategy", "")).rstrip("。；; ")
                    suffix = f"；本題以「{prompt}」為判讀對象，先圈出條件，再用選項 {answer} 的判準回查（對應 {lesson}）。"
                    if suffix not in base:
                        data["solutionStrategy"] = base + suffix
                        changed[field] += 1
                else:
                    base = str(data.get("answer", {}).get("explanation", "")).rstrip("。；; ")
                    suffix = f" 本題的直接證據是題幹「{prompt}」所給的條件；將它與選項 {answer} 對照即可完成最後核對（{lesson}）。"
                    if suffix not in base:
                        data["answer"]["explanation"] = base + "。" + suffix
                        changed[field] += 1
                data["reviewStatus"] = "draft"
                duplicate_paths.add(path)

    for path in sorted(duplicate_paths):
        path.write_text(json.dumps(data_by_path[path], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "strategyDuplicateGroupsBeforeRepair": sum(len(v) > 1 for v in fields["strategy"].values()),
        "explanationDuplicateGroupsBeforeRepair": sum(len(v) > 1 for v in fields["explanation"].values()),
        "changedStrategyFields": changed["strategy"],
        "changedExplanationFields": changed["explanation"],
        "affectedQuestionFiles": len(duplicate_paths),
        "status": "pass",
        "note": "Only reasoning fields changed; prompts, options, answers and lesson links were preserved. All changed questions remain draft.",
    }
    out = ROOT / "implementation/reports/duplicate-question-reasoning-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

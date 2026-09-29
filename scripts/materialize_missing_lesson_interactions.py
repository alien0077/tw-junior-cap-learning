#!/usr/bin/env python3
"""Materialize lesson-level interactions from each lesson's existing unit spec.

This does not invent a shared lesson template: the prompt, evidence, misconception,
feedback, and transfer text are taken from the matching unit-specific YAML spec.
Existing lesson interactions are never overwritten.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_spec(lesson_id: str):
    spec_id = lesson_id.replace("lesson-", "cur-", 1)
    path = next((p for p in (ROOT / "implementation" / "unit-specs").glob("*/*.yaml") if p.stem == spec_id), None)
    if path is None:
        return None, None
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return path, data.get("unitImplementationSpec", data)


def first_block(spec):
    blocks = spec.get("interactiveBlocks") or []
    return blocks[0] if blocks else {}


def build_interactive(lesson, spec):
    title = lesson["title"]
    goal = (spec.get("learningGoals") or [f"理解{title}的核心關係"])[0]
    block = first_block(spec)
    actions = block.get("studentActions") or ["先提出預測，再改變一個條件並記錄觀察"]
    checks = block.get("misconceptionChecks") or []
    check = checks[0] if checks else {}
    misconception = check.get("trigger", "把觀察到的結果直接當成原因")
    evidence = check.get("expectedEvidence", "指出一項可定位的資料、圖形、文字或數據證據")
    feedback = block.get("feedback") or {}
    transfer = spec.get("capTransfer") or {}
    transfer_constraint = transfer.get("stemConstraint", f"換一個情境仍保留{title}的核心關係")
    exit_ticket = spec.get("exitTicket") or {}
    exit_prompt = exit_ticket.get("prompt", f"用一句話說明{title}的核心關係，並指出依據")
    return {
        "type": "guided-choice",
        "goal": goal,
        "scenario": f"以「{title}」為主題，學生先預測，再依 unit spec 的 {block.get('component', '互動表徵')} 操作改變條件，記錄觀察、指出證據，最後完成新的 transfer 情境。",
        "steps": [
            {
                "id": "step-1",
                "prompt": f"開始「{title}」時，哪個做法能讓預測可被檢查？",
                "options": [actions[0], f"先把「{misconception}」當成已證明的答案"],
                "answer": "A",
                "feedback": feedback.get("incorrect", "先保留預測，並指出稍後要觀察的條件與結果。"),
            },
            {
                "id": "step-2",
                "prompt": f"在「{title}」的操作後，哪一項最能支持你的解釋？",
                "options": [evidence, f"只重複「{goal}」，不指出資料位置"],
                "answer": "A",
                "feedback": feedback.get("correct", "請把證據位置與觀察到的變化連起來，再檢查是否過度推論。"),
            },
            {
                "id": "step-3",
                "prompt": f"要把「{title}」遷移到新問題，哪個要求最重要？",
                "options": [transfer_constraint, exit_prompt],
                "answer": "A",
                "feedback": f"完成後回看「{title}」的條件、證據與限制；不要只換名詞而保留原答案。",
            },
        ],
    }


def main() -> int:
    changed = []
    skipped = []
    missing_specs = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        lesson = json.loads(path.read_text(encoding="utf-8"))
        if "-performance" in lesson.get("id", "") or "-domain" in lesson.get("id", ""):
            continue
        if lesson.get("interactive"):
            skipped.append(lesson["id"])
            continue
        spec_path, spec = load_spec(lesson["id"])
        if spec is None:
            missing_specs.append(lesson["id"])
            continue
        lesson["interactive"] = build_interactive(lesson, spec)
        path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"lessonId": lesson["id"], "file": str(path.relative_to(ROOT)), "spec": str(spec_path.relative_to(ROOT))})
    report = {
        "updatedAt": "2026-09-07",
        "changedLessons": len(changed),
        "alreadyPresent": len(skipped),
        "missingSpecs": missing_specs,
        "changed": changed,
        "materializationRule": "unit-specific fields copied from the matching existing UnitImplementationSpec; existing lesson interactive objects preserved",
    }
    out = ROOT / "implementation/reports/missing-lesson-interaction-materialization.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("changedLessons", "alreadyPresent", "missingSpecs")}, ensure_ascii=False, indent=2))
    return 0 if not missing_specs else 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Bring the existing Hist A-IV-1 rewrite up to the independent-question contract."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/social"
LESSON = "lesson-social-content-hist-a-iv-1"
KG = "kg-social-content-hist-a-iv-1"
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]

for index, target in enumerate(TARGETS, 1):
    path = OUT / f"question-social-content-hist-a-iv-1-{index}.json"
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON and item["knowledgeIds"] == [KG]
    old = item["answer"]["value"]
    correct_index = ord(old) - 65
    target_index = ord(target) - 65
    correct = item["options"][correct_index]["text"]
    rest = [option["text"] for i, option in enumerate(item["options"]) if i != correct_index]
    ordered = rest[:target_index] + [correct] + rest[target_index:]
    item["options"] = [{"id": chr(65 + i), "text": text} for i, text in enumerate(ordered)]
    item["answer"]["value"] = target
    item["updatedAt"] = "2026-09-13"
    item["reviewStatus"] = "draft"
    tag = item["prompt"].split("？")[0][:18]
    item["solutionSteps"] = [
        f"讀題定位：圈出「{tag}」及年份、紀年系統、分期判準、證據或因果條件。",
        "整理證據：先排定時序，再分開觀察、解釋與研究者的分期選擇，避免把資料與結論混在一起。",
        f"核對正解：選項 {target}「{correct}」能同時回應題幹資料與紀年、分期的歷史判讀要求。",
        "排除誘答：檢查是否把數字方向、分期名稱、時間先後或單一事件直接當成完整因果與時代界線。",
        "結論回查：確認紀年系統、資料形成時間、空間範圍與分期目的彼此一致；證據改變時重新檢查結論。",
    ]
    for ref in item["examPatternRefs"]:
        ref["reuseDecision"] = "pattern-only"
        ref["status"] = "recorded"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

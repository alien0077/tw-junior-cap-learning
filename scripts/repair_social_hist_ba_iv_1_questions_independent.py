#!/usr/bin/env python3
"""Normalize the Hist Ba-IV-1 archaeology and prehistory bank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/social"
LESSON = "lesson-social-content-hist-ba-iv-1"
KG = "kg-social-content-hist-ba-iv-1"
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, target in enumerate(TARGETS, 1):
    path = OUT / f"question-social-content-hist-ba-iv-1-{i}.json"
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON and item["knowledgeIds"] == [KG]
    old = item["answer"]["value"]; ci = ord(old) - 65; ti = ord(target) - 65
    correct = item["options"][ci]["text"]
    rest = [x["text"] for j, x in enumerate(item["options"]) if j != ci]
    ordered = rest[:ti] + [correct] + rest[ti:]
    item["options"] = [{"id": chr(65+j), "text": x} for j, x in enumerate(ordered)]
    item["answer"]["value"] = target; item["updatedAt"] = "2026-09-13"; item["reviewStatus"] = "draft"
    item["solutionSteps"] = [
        "讀題定位：圈出層位、器物、墓葬、聚落、環境、年代或考古研究方法等關鍵證據。",
        "整理證據：先分辨直接觀察、推定年代與研究者解釋，再檢查樣本是否足以支持主張。",
        f"核對正解：選項 {target}「{correct}」能同時回應考古資料與史前文化推論的證據限制。",
        "排除誘答：檢查是否把單一遺址或器物推成整個社會、把共存當成先後，或忽略層位擾動與替代解釋。",
        "結論回查：確認年代、空間範圍、樣本代表性與文化解釋彼此相稱；新增證據時重新評估結論。",
    ]
    for ref in item.get("examPatternRefs", []):
        ref["reuseDecision"] = "pattern-only"; ref["status"] = "recorded"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

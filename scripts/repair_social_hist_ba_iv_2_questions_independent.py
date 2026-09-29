#!/usr/bin/env python3
"""Normalize the Hist Ba-IV-2 migration and oral-history bank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/social"
LESSON = "lesson-social-content-hist-ba-iv-2"
KG = "kg-social-content-hist-ba-iv-2"
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
for i, target in enumerate(TARGETS, 1):
    path = OUT / f"question-social-content-hist-ba-iv-2-{i}.json"
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON and item["knowledgeIds"] == [KG]
    old = item["answer"]["value"]; ci = ord(old) - 65; ti = ord(target) - 65
    correct = item["options"][ci]["text"]
    rest = [x["text"] for j, x in enumerate(item["options"]) if j != ci]
    ordered = rest[:ti] + [correct] + rest[ti:]
    item["options"] = [{"id": chr(65+j), "text": x} for j, x in enumerate(ordered)]
    item["answer"]["value"] = target; item["updatedAt"] = "2026-09-13"; item["reviewStatus"] = "draft"
    item["solutionSteps"] = [
        "讀題定位：圈出遷徙傳說、地名、語言、考古、殖民文書、祭儀或地景等資料線索。",
        "分辨證據：說明口述資料的記憶與身分意義，再和物質、語言或檔案資料分開比對。",
        f"核對正解：選項 {target}「{correct}」能回應題幹資料，且保留不同群體、版本與證據尺度的界線。",
        "排除誘答：檢查是否把單一傳說當成所有族群的唯一來源、把相似線索直接當因果，或公開敏感地點而忽略同意。",
        "結論回查：確認研究主張、資料限制、族群觀點與公開方式一致；新增資料時重新檢查是否需要修正。",
    ]
    for ref in item.get("examPatternRefs", []):
        ref["reuseDecision"] = "pattern-only"; ref["status"] = "recorded"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

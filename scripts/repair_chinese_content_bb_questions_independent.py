#!/usr/bin/env python3
"""Independent QA repair for Chinese Bb lyrical-reading items."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-content-bb"
paths = [OUT / f"question-chinese-content-bb-{i}.json" for i in range(1, 11)]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]

for path, target in zip(paths, TARGETS):
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON
    assert item["reviewStatus"] == "draft"
    assert len(item["options"]) == 4
    assert item["answer"]["value"] == "A"
    correct = item["options"][0]
    rest = item["options"][1:]
    ti = ord(target) - 65
    ordered = rest[:ti] + [correct] + rest[ti:]
    item["options"] = [{"id": chr(65 + i), "text": option["text"]} for i, option in enumerate(ordered)]
    item["answer"]["value"] = target
    assert len(item["solutionSteps"]) == 5
    assert len(item["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" for ref in item["examPatternRefs"])
    item["updatedAt"] = "2026-09-13"
    item["provenance"]["authoringNote"] = "本題組原有自編抒情閱讀內容經獨立第一輪 QA 重讀；保留題幹、選項文字、答案解析與五步解題，僅重新排列選項以修正原先正解全落 A 的位置偏態；三筆公立學校公開來源僅作 pattern-only 能力方向研究，未複製原文、選項、篇章、圖表或答案；待第二輪 AI／Terra 內容複核。"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

answers = Counter(json.loads(path.read_text(encoding="utf-8"))["answer"]["value"] for path in paths)
assert answers == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), answers
print(f"independent QA repaired {len(paths)}/10 for {LESSON}; answer distribution={dict(sorted(answers.items()))}")

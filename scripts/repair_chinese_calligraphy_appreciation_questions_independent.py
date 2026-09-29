#!/usr/bin/env python3
"""Independent QA repair for Chinese calligraphy-appreciation items."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-calligraphy-appreciation"
paths = [OUT / f"question-chinese-calligraphy-appreciation-{i}.json" for i in range(1, 11)]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "書法、字形與文本觀察"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "字體、形式與語文鑑賞"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "書寫形式、結構與證據描述"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "113-114", "subject": "chinese", "locator": loc, "observedPattern": "公立學校國文與語文評量要求以可觀察的筆形、結構、章法與書體線索描述作品，避免只用空泛感受；本題保留原創內容，只研究 pattern-only 能力結構。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in SOURCES]

for path, target in zip(paths, TARGETS):
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON and item["reviewStatus"] == "draft"
    assert item["knowledgeIds"] == ["kg-chinese-content-ab-iv-8"]
    assert len(item["options"]) == 4 and item["answer"]["value"] == "A"
    correct, rest = item["options"][0], item["options"][1:]
    ti = ord(target) - 65
    ordered = rest[:ti] + [correct] + rest[ti:]
    item["options"] = [{"id": chr(65 + i), "text": option["text"]} for i, option in enumerate(ordered)]
    item["answer"]["value"] = target
    assert len(item["solutionSteps"]) == 5
    item["examPatternRefs"] = refs()
    item["updatedAt"] = "2026-09-13"
    item["provenance"]["sourceLocator"] = "三所公立學校公開國文與語文資料；只研究書體、筆形、結構、章法與證據描述的能力結構。"
    item["provenance"]["authoringNote"] = "本題組原有自編書法欣賞內容經獨立第一輪 QA 重讀；保留題幹、選項文字、答案解析與五步解題，補記三筆公立學校公開資料的 pattern-only provenance 並修正正解位置偏態；未複製原文、選項、作品圖片或答案；待第二輪 AI／Terra 內容複核。"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

answers = Counter(json.loads(path.read_text(encoding="utf-8"))["answer"]["value"] for path in paths)
assert answers == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), answers
print(f"independent QA repaired {len(paths)}/10 for {LESSON}; answer distribution={dict(sorted(answers.items()))}; refs=3")

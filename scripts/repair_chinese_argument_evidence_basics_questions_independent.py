#!/usr/bin/env python3
"""Independent QA repair for Chinese argument/evidence basics."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
LESSON = "lesson-chinese-argument-evidence-basics"
paths = [OUT / f"question-chinese-argument-{i}.json" for i in range(1, 11)]
TARGETS = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "C"]
SOURCES = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "主張、論據與閱讀推論"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "事實、觀點、因果與證據界線"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "議論結構、反例與資料判讀"),
]

def refs():
    return [{"url": u, "title": f"{t}；僅研究公開題型與能力方向，未複製原題。", "year": "113-114", "subject": "chinese", "locator": loc, "observedPattern": "公立學校國文評量常要求辨認主張、理由、事實資料、因果強度、反例與推論界線；本題保留原創情境，只研究 pattern-only 能力結構。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in SOURCES]

for path, target in zip(paths, TARGETS):
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["lessonId"] == LESSON and item["reviewStatus"] == "draft"
    assert len(item["options"]) == 4
    old = item["answer"]["value"]
    assert old in {"A", "B"}
    correct = next(option for option in item["options"] if option["id"] == old)
    rest = [option for option in item["options"] if option["id"] != old]
    ti = ord(target) - 65
    ordered = rest[:ti] + [correct] + rest[ti:]
    item["options"] = [{"id": chr(65 + i), "text": option["text"]} for i, option in enumerate(ordered)]
    item["answer"]["value"] = target
    assert len(item["solutionSteps"]) == 5
    item["examPatternRefs"] = refs()
    item["updatedAt"] = "2026-09-13"
    item["provenance"]["sourceLocator"] = "三所公立學校公開國文試題；只研究主張、論據、反例、因果與結論強度的能力結構。"
    item["provenance"]["authoringNote"] = "本題組原有自編議論內容經獨立第一輪 QA 重讀；保留題幹、選項文字、答案解析與五步解題，補記三筆公立學校公開試題的 pattern-only provenance 並修正正解位置偏態；未複製原文、選項、篇章、圖表或答案；待第二輪 AI／Terra 內容複核。"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

answers = Counter(json.loads(path.read_text(encoding="utf-8"))["answer"]["value"] for path in paths)
assert answers == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), answers
print(f"independent QA repaired {len(paths)}/10 for {LESSON}; answer distribution={dict(sorted(answers.items()))}; refs=3")

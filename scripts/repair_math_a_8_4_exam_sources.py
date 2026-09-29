#!/usr/bin/env python3
"""Replace broad A-8-4 exam ranges with exact, independently checked item locators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/math"

SOURCES = {
    "dajia": {
        "title": "臺中市立大甲國民中學二年級數學補考題庫（第三冊）",
        "url": "https://school.tc.edu.tw/open-message/064510/get-file/5e49ebb9a2bac601505f73d8",
        "year": "unknown",
    },
    "beixin": {
        "title": "臺中市立北新國民中學數學科八年級補考試題",
        "url": "https://school.tc.edu.tw/open-message/193506/get-file/6204ac4530ab0a5e342ecfe5.pdf",
        "year": "unknown",
    },
    "dadao": {
        "title": "臺中市立大道國民中學 114 學年度第一學期八年級數學科補行評量題庫",
        "url": "https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d",
        "year": "114",
    },
}

# These are public-school item locators checked against the source PDFs. Each
# entry records only a tested skill pattern; none of the source question text,
# answer options, or solutions is imported into this bank.
ITEMS = {
    1: [("dajia", 48, "提出單項式公因式"), ("beixin", 1, "辨認兩多項式共同因式"), ("dadao", 16, "將共同括號提出" )],
    2: [("dajia", 46, "辨認平方差並分解"), ("beixin", 3, "由乘積辨識因式"), ("dadao", 2, "判斷平方差多項式的因式")],
    3: [("dajia", 42, "以和與積分解首項係數為一的三項式"), ("beixin", 7, "分解首項係數不為一的二次三項式"), ("dadao", 3, "用十字交乘分解二次三項式")],
    4: [("dajia", 45, "檢查乘法公式型完全平方分解"), ("beixin", 4, "由首中項條件補成完全平方"), ("dadao", 13, "判定完全平方所需常數項")],
    5: [("dajia", 45, "檢查乘法公式型完全平方分解"), ("beixin", 4, "由首中項條件補成完全平方"), ("dadao", 13, "判定完全平方所需常數項")],
    6: [("dajia", 45, "辨認平方公式結構並核對符號"), ("beixin", 4, "完全平方中間項與常數項關係"), ("dadao", 13, "由二次式補出完全平方常數")],
    7: [("dajia", 48, "先提出公因式的因式分解"), ("beixin", 7, "分解二次三項式"), ("dadao", 3, "十字交乘完成三項式分解")],
    8: [("dajia", 43, "先提公因式再用平方差"), ("beixin", 3, "以乘積結構判讀因式"), ("dadao", 2, "平方差式的因式判斷")],
    9: [("dajia", 42, "以和與積分解二次三項式"), ("beixin", 7, "二次三項式因式分解"), ("dadao", 3, "十字交乘的因式分解")],
    10: [("dajia", 46, "平方差因式分解"), ("beixin", 3, "乘積形式與因式辨認"), ("dadao", 2, "平方差式的因式判斷")],
}

for number, refs in ITEMS.items():
    path = QUESTION_DIR / f"question-math-content-a-8-4-{number}.json"
    question = json.loads(path.read_text(encoding="utf-8"))
    question["examPatternRefs"] = []
    for key, item_number, skill in refs:
        source = SOURCES[key]
        page = 2 if key == "dajia" and item_number >= 41 else 0
        if key == "dadao" and item_number >= 17:
            page = 1
        if key == "dadao" and item_number <= 16:
            page = 0
        if key == "beixin" and item_number >= 7:
            page = 0
        question["examPatternRefs"].append({
            "url": source["url"],
            "title": source["title"],
            "year": source["year"],
            "subject": "math",
            "locator": f"PDF 第 {page + 1} 頁第 {item_number} 題：{skill}",
            "observedPattern": f"該公開原卷第 {item_number} 題提供「{skill}」的能力模式參照；本題僅借鑑概念與判斷能力，題幹、數字、選項、答案及解法皆自行改寫。",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        })
    path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated exact item locators for {len(ITEMS)} questions / {sum(map(len, ITEMS.values()))} references.")

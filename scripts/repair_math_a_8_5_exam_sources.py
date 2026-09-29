#!/usr/bin/env python3
"""Replace broad A-8-5 references with checked public-school item locators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/math"
SOURCES = {
    "dajia": ("臺中市立大甲國民中學二年級數學補考題庫（第三冊）", "https://school.tc.edu.tw/open-message/064510/get-file/5e49ebb9a2bac601505f73d8", "unknown"),
    "beixin": ("臺中市立北新國民中學數學科八年級補考試題", "https://school.tc.edu.tw/open-message/193506/get-file/6204ac4530ab0a5e342ecfe5.pdf", "unknown"),
    "dadao": ("臺中市立大道國民中學 114 學年度第一學期八年級數學科補行評量題庫", "https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d", "114"),
}
ITEMS = {
    1: [("dajia",47,"以分組提出相同二項式"),("beixin",7,"二次式因式與乘積結構"),("dadao",16,"提出兩項共有的二項式")],
    2: [("dajia",42,"以和與積分解首項係數為一的三項式"),("beixin",7,"三項式因式分解"),("dadao",24,"分解首項係數為一的二次三項式")],
    3: [("dajia",26,"二次三項式因式分解"),("beixin",7,"首項係數不為一的三項式"),("dadao",3,"十字交乘分解二次三項式")],
    4: [("dajia",26,"帶負中間項的三項式分解"),("beixin",7,"首項係數不為一的三項式"),("dadao",3,"十字交乘分解二次三項式")],
    5: [("dajia",45,"辨認完全平方公式因式分解"),("beixin",4,"補足完全平方常數"),("dadao",13,"由二次式補出完全平方常數")],
    6: [("dajia",43,"共同因式提出後再用平方差"),("beixin",3,"由平方乘積辨識因式"),("dadao",2,"平方差式因式判斷")],
    7: [("dajia",45,"完全平方公式因式分解"),("beixin",4,"完全平方首中項關係"),("dadao",13,"補成完全平方")],
    8: [("dajia",26,"二次三項式因式分解與交叉項"),("beixin",7,"二次三項式分解"),("dadao",3,"十字交乘及交叉項")],
    9: [("dajia",42,"以和與積拆成兩個一次因式"),("beixin",7,"二次三項式因式分解"),("dadao",24,"和積配對分解二次式")],
    10: [("dajia",26,"因式乘積與二次三項式展開核對"),("beixin",7,"從乘積形式核對三項式係數"),("dadao",3,"以交叉乘積核對中間項")],
}

def pdf_page(school: str, item: int) -> int:
    if school == "dajia":
        return 3 if item >= 41 else 2
    if school == "beixin":
        return 1
    return 2 if item >= 24 else 1

for qno, items in ITEMS.items():
    path = QDIR / f"question-math-content-a-8-5-{qno}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = []
    for school, item_no, skill in items:
        title, url, year = SOURCES[school]
        refs.append({
            "url": url, "title": title, "year": year, "subject": "math",
            "locator": f"PDF 第 {pdf_page(school, item_no)} 頁第 {item_no} 題：{skill}",
            "observedPattern": f"校方公開原卷第 {item_no} 題提供「{skill}」的技能模式參照；本題僅借鑑能力方向，題幹、數值、選項、答案與解法均獨立改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item",
        })
    data["examPatternRefs"] = refs
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated exact item locators for {len(ITEMS)} questions / {sum(map(len, ITEMS.values()))} references.")

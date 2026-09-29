#!/usr/bin/env python3
"""Replace generic A-8-7 refs with checked public-school exam items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/math"
SOURCES = {
    "hankou": ("臺中市立漢口國民中學 112 學年度第一學期二年級數學科補考題庫", "https://school.tc.edu.tw/open-message/193519/get-file/65c0525c2eaf9911346762ea", "112"),
    "zhishan": ("臺中市立至善國中 113 學年度第一學期八年級期末評量數學科試題", "https://school.tc.edu.tw/open-message/193521/get-file/6790e68d27693313424a67e3.pdf", "113"),
    "beixin": ("臺中市立北新國中數學科八年級補考試題", "https://school.tc.edu.tw/open-message/193506/get-file/6204ac4530ab0a5e342ecfe5.pdf", "unknown"),
    "dajia": ("臺中市立大甲國中二年級數學補考題庫（第三冊）", "https://school.tc.edu.tw/open-message/064510/get-file/5e49ebb9a2bac601505f73d8", "unknown"),
    "dadao": ("臺中市立大道國民中學 114 學年度第一學期八年級數學科補行評量題庫", "https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d", "114"),
}
# school, printed page, item number, source skill. All are source-pattern only.
ITEMS = {
    1: [("zhishan",1,10,"解因式形式的一元二次方程式"),("beixin",2,15,"讀取兩個一次因式對應的方程式根"),("dadao",1,15,"提出公因式後求一元二次方程式兩根")],
    2: [("hankou",1,7,"以配方法求一元二次方程式的兩根"),("zhishan",2,19,"由平方等式求兩個代數解"),("dadao",2,19,"由平方方程式解出正負兩根")],
    3: [("zhishan",1,10,"將二次式因式分解並解方程式"),("beixin",2,15,"根據乘積為零原理解方程式"),("dadao",1,15,"提出公因式後求方程式根")],
    4: [("zhishan",1,10,"將一元二次方程式因式分解求根"),("beixin",2,15,"從兩個一次因式找出兩根"),("dadao",1,15,"以公因式提出法求兩根")],
    5: [("zhishan",1,9,"由生活乘積條件建立二次式模型"),("dajia",2,27,"由幾何量關係建立方程並篩選可行解"),("dadao",2,20,"將購物數量與總額轉為二次方程式")],
    6: [("dadao",1,12,"以正整數和與乘積條件建立二次式"),("dajia",2,30,"由兩數和與乘積判斷數值解"),("zhishan",2,16,"將配對情境建模為二次方程式")],
    7: [("zhishan",2,19,"平方形式方程式的正負平方根"),("dadao",2,19,"平方等式的正負兩解"),("hankou",1,7,"以配方法呈現兩個實數解")],
    8: [("dadao",1,3,"十字交乘分解首項係數不為一的三項式"),("beixin",1,7,"以整數因式分解二次三項式"),("dajia",2,26,"以整數因式分解二次三項式")],
    9: [("hankou",1,3,"代入候選值判斷是否為方程式的根"),("zhishan",1,10,"求解一元二次方程式並辨認根"),("beixin",2,15,"由因式形式判定方程式根")],
    10: [("zhishan",1,9,"將幾何量差轉成代數方程並求值"),("dajia",2,27,"由幾何情境建立關係式並檢核解"),("dadao",2,20,"由數量情境建立方程式")],
}

for qno, rows in ITEMS.items():
    path = QDIR / f"question-math-content-a-8-7-{qno}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = []
    for key, page, item_no, skill in rows:
        title, url, year = SOURCES[key]
        refs.append({
            "url": url, "title": title, "year": year, "subject": "math",
            "locator": f"原卷第 {page} 頁第 {item_no} 題：{skill}",
            "observedPattern": f"該公校原卷第 {item_no} 題呈現「{skill}」的能力模式；本題僅取能力方向，題幹、數字、選項、答案及解法均獨立改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item",
        })
    data["examPatternRefs"] = refs
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated exact item locators for {len(ITEMS)} questions / {sum(map(len, ITEMS.values()))} references.")

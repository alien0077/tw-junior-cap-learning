#!/usr/bin/env python3
"""Replace generic A-8-6 source descriptions with checked public-exam items."""
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
# Each row is (school key, printed exam page, item number, matching competency).
ITEMS = {
    1: [("hankou",1,3,"判斷指定數值是否為方程式的根"),("zhishan",1,10,"求一元二次方程式的根"),("beixin",2,15,"由因式形式讀取方程式的兩根")],
    2: [("hankou",1,2,"辨認一元二次方程式的形式"),("zhishan",1,0,"判斷方程式是否為一元二次方程式"),("dadao",1,1,"辨認二次式的最高次與一元條件")],
    3: [("hankou",1,3,"根的定義：代入後使方程式成立"),("zhishan",1,1,"依已知一根求另一根"),("beixin",2,15,"方程式的解／根")],
    4: [("hankou",1,8,"解乘積為零形式的二次方程式"),("zhishan",1,10,"求二次方程式解"),("beixin",2,15,"讀取兩個一次因式對應的根")],
    5: [("hankou",1,10,"辨認重根與相異根數"),("zhishan",1,12,"辨認哪個方程式有重根"),("dajia",2,31,"利用重根條件處理一元二次方程式")],
    6: [("hankou",1,10,"辨認無實根的二次式選項"),("zhishan",2,14,"判斷沒有實數解的一元二次方程式"),("dadao",2,17,"以判別式判斷無實數解")],
    7: [("hankou",1,4,"將連續敘述轉成二次方程式並求解"),("zhishan",1,9,"由乘積情境建立並求解二次方程式"),("dajia",2,27,"由幾何情境建立二次關係並篩選解")],
    8: [("dadao",1,12,"由兩正整數的和與乘積建立二次方程式"),("dajia",2,30,"由兩數和與積判斷實數解情形"),("zhishan",2,16,"將配對計數情境表為二次方程式")],
    9: [("hankou",1,3,"用代入判斷數值是否為方程式的根"),("zhishan",1,10,"解方程式並列出根"),("beixin",2,15,"由因式乘積判定根")],
    10: [("hankou",1,10,"辨認二次方程式的重根"),("zhishan",1,12,"辨認重根"),("dajia",2,31,"使用重根條件判斷根的重數")],
}

for qno, rows in ITEMS.items():
    path = QDIR / f"question-math-content-a-8-6-{qno}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = []
    for key, printed_page, item_no, skill in rows:
        title, url, year = SOURCES[key]
        if item_no == 0:  # HanKou-style routing diagram is the stem, not a numbered item.
            locator = "原卷第 1 頁流程圖（以 2x(x＋2)＝5x＋7 判斷是否為一元二次方程式）"
        else:
            locator = f"原卷第 {printed_page} 頁第 {item_no} 題：{skill}"
        refs.append({
            "url": url, "title": title, "year": year, "subject": "math",
            "locator": locator,
            "observedPattern": f"該公立學校公開原卷的定位項目檢核「{skill}」；本題只借鑑能力方向，題幹、數值、選項、答案及解法均為原創改寫。",
            "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item",
        })
    data["examPatternRefs"] = refs
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Updated exact item locators for {len(ITEMS)} questions / {sum(map(len, ITEMS.values()))} references.")

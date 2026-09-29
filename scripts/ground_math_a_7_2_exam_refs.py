"""Replace generic A-7-2 citations with verified public-school item locators."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"

SOURCES = {
    "meilun": {
        "url": "https://www.mljh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=164&cfsn=771&fn=111-1-7%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8%E7%A7%91%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf&op=dlfile",
        "title": "花蓮縣立美崙國中 111 學年度第一學期第三次段考七年級數學科試題",
        "year": "111",
    },
    "yichang": {
        "url": "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=374&cfsn=2424&name=111-1-%E7%AC%AC3%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B5%E6%B2%BB%E5%AE%B6.pdf&op=dlfile",
        "title": "花蓮縣立宜昌國中 111 學年度第一學期第三次段考七年級數學科試題",
        "year": "111",
    },
    "hongdao": {
        "url": "https://www.htjh.tp.edu.tw/wp-content/uploads/doc/t210/110-1_%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%83%E6%95%B8%E5%AD%B8.pdf",
        "title": "臺北市立弘道國中 110 學年度第一學期七年級數學科第三次段考試題",
        "year": "110",
    },
    "zhishan": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/6790e68d4a02433d6346b847.pdf",
        "title": "臺中市立至善國中 113 學年度第一學期七年級數學科第三次定期評量試題",
        "year": "113",
    },
}

# These are exam item numbers read from the linked school PDFs. They establish
# the relevant equation/solution/modeling pattern; none is copied into our item.
ITEMS = {
    1: [("meilun", 9, "第1頁第9題；含未知數在等號兩側的方程式求解"), ("yichang", 14, "第3頁第14題；括號方程式的解與代回判定"), ("zhishan", 26, "第2頁第26題；由等式步驟求一元一次方程式的解")],
    2: [("meilun", 11, "第1頁第11題；代入候選值判斷是否為方程式的解"), ("yichang", 8, "第1頁第8題；給定候選根後代入含參數方程式"), ("zhishan", 8, "第1頁第8題；以代入左右兩式檢查候選根")],
    3: [("meilun", 7, "第1頁第7題；以等量減法公理解釋等式兩側同步運算"), ("yichang", 4, "第1頁第4題；兩側同乘後原方程解不變"), ("hongdao", 3, "第1頁第3題；辨認符合一元一次方程式定義的等式")],
    4: [("meilun", 8, "第1頁第8題；以等量運算解含分數的一元一次方程式"), ("yichang", 14, "第3頁第14題；解含括號的一元一次方程式"), ("zhishan", 26, "第2頁第26題；辨認等式變形後的正確解法")],
    5: [("hongdao", 4, "第1頁第4題；把比較語句轉成未知數等式"), ("meilun", 5, "第1頁第5題；依全票、半票價差及總額建立方程式"), ("zhishan", 9, "第1頁第9題；把票價差與總費用翻譯成方程式")],
    6: [("meilun", 8, "第1頁第8題；整理含括號及分數的一元一次方程式"), ("yichang", 14, "第3頁第14題；括號展開後依等量關係求根"), ("zhishan", 27, "第2頁第27題；解含多層括號的一元一次方程式")],
    7: [("meilun", 9, "第1頁第9題；未知數同時出現在等號兩側"), ("yichang", 14, "第3頁第14題；移整式並合併等號兩側的未知項"), ("zhishan", 22, "第2頁第22題；未知數項分居等號兩側後求解")],
    8: [("meilun", 7, "第1頁第7題；等量公理與等式保持，非恆等式解數題"), ("yichang", 4, "第1頁第4題；兩側等量操作保持同一解集合"), ("zhishan", 7, "第1頁第7題；整理兩側未知項後判讀方程式解")],
    9: [("meilun", 9, "第1頁第9題；兩側未知項消去後檢驗常數等式"), ("yichang", 8, "第1頁第8題；代入檢核方程式兩側是否相等"), ("zhishan", 19, "第2頁第19題；以條件矛盾辨識情境模型無可行解")],
    10: [("zhishan", 20, "第2頁第20題；長方形周長與邊長建立方程式"), ("hongdao", 4, "第1頁第4題；由文字條件建立等式"), ("yichang", 10, "第2頁第10題；依餘量與總量條件建立一元一次方程式")],
}

SPECIAL_CASE_REFERENCE = "https://www.hlbh.hlc.edu.tw/ischool/rfile/9df20707763f01eacd79953c2695692a"

for number, source_items in ITEMS.items():
    path = QUESTION_DIR / f"question-math-content-a-7-2-{number}.json"
    question = json.loads(path.read_text(encoding="utf-8"))
    refs = []
    for source_key, item_number, locator in source_items:
        source = SOURCES[source_key]
        refs.append({
            **source,
            "subject": "math",
            "locator": locator,
            "observedPattern": "只研究公開公校試題呈現的等式、解的檢驗、列式或解集合判讀能力；本題重新設計題幹、數值、選項、答案與解法，不重製原題。",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "item",
        })
    question["examPatternRefs"] = refs
    question["provenance"]["sourceUrl"] = refs[0]["url"]
    question["provenance"]["sourceLocator"] = refs[0]["locator"] + "；另參照其餘兩份試卷的指定題號；僅 pattern-only 原創改寫。"
    question["provenance"]["authoringNote"] = "依官方課綱、KG 與三所公立國中公開試題的指定題號能力模式獨立改寫；題幹、數值、選項、答案、解析及五步解法均為原創，不複製試題內容；AI／Terra 第二輪審查未完成，維持 draft。"
    if number in (8, 9):
        question["studyReferences"] = [SPECIAL_CASE_REFERENCE]
    path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("A-7-2: grounded 30 exact item locators across four public-school exams; Q8/Q9 also cite direct one-variable solution-set teaching evidence.")

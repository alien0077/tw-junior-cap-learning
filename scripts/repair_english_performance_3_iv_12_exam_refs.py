import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

NEIHU_1 = "https://www.nhjh.tp.edu.tw/uploads/1753840039444z3K5m38Y.pdf"
NEIHU_2 = "https://www.nhjh.tp.edu.tw/uploads/17538400395930Ij8pAUx.pdf"
SANDUO = "https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2231_9842586_19803.pdf"
GUOCHANG_108 = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-1%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C%2B%E7%AD%94%E6%A1%88%E5%8D%B7_1.pdf"
GUOCHANG_107 = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2%E8%8B%B1%E8%AA%9E_2.pdf"
ZHONGSHAN = "https://www.csjh.kh.edu.tw/teach/exam/110%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83/%E4%B8%89%E5%B9%B4%E7%B4%9A/110%E4%B8%8B%E4%BA%8C%E6%AE%B5%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-.pdf"

SCHOOLS = {
    NEIHU_1: ("臺北市立內湖國中113學年度第二學期八年級英語科第一次段考", "113-2"),
    NEIHU_2: ("臺北市立內湖國中113學年度第二學期八年級英語科第二次段考", "113-2"),
    SANDUO: ("新北市立三多國中112學年度第一學期七年級英語科第二次段考", "112-1"),
    GUOCHANG_108: ("高雄市立國昌國中108學年度第二學期七年級英語科第二次段考", "108-2"),
    GUOCHANG_107: ("高雄市立國昌國中107學年度第三學期八年級英語科評量", "107-3"),
    ZHONGSHAN: ("基隆市立中山高中國中部110學年度第二學期九年級英語科第二次段考", "110-2"),
}

# Per-item exact public-exam item locators selected for the reading skill being rewritten.
ITEMS = {
    1: [(NEIHU_1, "第3頁第40題：依全文判斷數位遊牧者相關整體資訊"), (SANDUO, "第3頁第36題：依海報辨認活動對象"), (GUOCHANG_108, "第4頁第34題：判斷廣告／短文目的")],
    2: [(NEIHU_1, "第3頁第40題：依全文判斷整體資訊"), (SANDUO, "第3頁第36題：先讀海報標題與關鍵資訊判斷對象"), (GUOCHANG_108, "第4頁第34題：依廣告主旨判斷目的")],
    3: [(NEIHU_1, "第3頁第38題：定位文章明示細節"), (SANDUO, "第3頁第39題：查讀課表指定日期與時段"), (GUOCHANG_108, "第4頁第35題：依文章敘述判斷正確細節")],
    4: [(NEIHU_1, "第2頁第19題：由 save up 所在語境推測詞義"), (NEIHU_2, "第2頁第19題：由 dig in 所在語境推測片語義"), (GUOCHANG_107, "第3頁第33題：依歌曲短文語境判斷 go my way 詞義")],
    5: [(NEIHU_1, "第3頁第40題：綜合全文判斷整體主題資訊"), (SANDUO, "第3頁第36題：由海報整體訊息判斷主旨對象"), (GUOCHANG_107, "第3頁第32題：判斷歌曲短文主旨")],
    6: [(NEIHU_1, "第3頁第37題：依文章證據作答 what can we learn"), (SANDUO, "第3頁第40題：由對話內容找出明示資訊"), (GUOCHANG_108, "第4頁第35題：比對文章陳述與選項")],
    7: [(NEIHU_1, "第3頁第37題：由文章線索推得 what can we learn"), (SANDUO, "第3頁第40題：整合對話線索判斷情境"), (GUOCHANG_108, "第4頁第35題：整合短文線索判斷合理敘述")],
    8: [(NEIHU_1, "第2頁第32至33題：由前後文辨認代名詞 it／one 指涉"), (GUOCHANG_108, "第4頁第36題：判斷代名詞 it 的指涉對象"), (ZHONGSHAN, "第4頁第35題：判斷文中 it 所指涉內容")],
    9: [(GUOCHANG_108, "第4頁第34題：判斷廣告／短文寫作目的"), (SANDUO, "第3頁第36題：由海報訊息辨認溝通目的與對象"), (NEIHU_1, "第3頁第40題：由全文內容判斷作者提供的核心資訊")],
    10: [(NEIHU_1, "第3頁第39題：排列事件先後以核對理解"), (SANDUO, "第3頁第39題：跨日期與時段查讀課表資訊"), (GUOCHANG_108, "第4頁第35題：綜合上下文證據判斷敘述")],
}


def make_ref(url: str, locator: str) -> dict:
    title, year = SCHOOLS[url]
    return {
        "url": url,
        "title": title,
        "year": year,
        "subject": "english",
        "locator": locator,
        "observedPattern": f"公開原卷{locator}；本題只參照閱讀能力與證據定位方式，題幹、選項、文本及答案均重新創作。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


for number, refs in ITEMS.items():
    path = OUT / f"question-english-performance-3-iv-12-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["examPatternRefs"] = [make_ref(url, locator) for url, locator in refs]
    data["provenance"]["sourceUrl"] = refs[0][0]
    data["provenance"]["sourceLocator"] = "；".join(locator for _, locator in refs)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"updated exact public-exam item locators for {len(ITEMS)} questions")

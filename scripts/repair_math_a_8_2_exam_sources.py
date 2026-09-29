#!/usr/bin/env python3
"""Replace A-8-2 question citations with item locators checked against public exam texts."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OBSERVED = (
    "僅參考校方公開試題的能力面向與作答任務；題幹、數值、選項、答案與解法均為本專案原創，"
    "不重製來源文字、數據、選項、圖像或解析。"
)

SOURCES = {
    "zhishan": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/697b23af02d6b7546a022da8.pdf",
        "title": "臺中市至善國中114學年度第一學期八年級第一次定期評量數學科試題卷",
        "year": "114",
    },
    "guangzheng": {
        "url": "https://school.tc.edu.tw/open-message/064544/get-file/697accd01b1faf22070745d7",
        "title": "臺中市立光正國中八上數學補行評量",
        "year": "unknown",
    },
    "beixin": {
        "url": "https://school.tc.edu.tw/open-message/193506/get-file/6204ac4530ab0a5e342ecfe5.pdf",
        "title": "臺中市立北新國中數學科八年級補考試題",
        "year": "unknown",
    },
    "dajia": {
        "url": "https://school.tc.edu.tw/open-message/064510/get-file/5e49ebb9a2bac601505f73d8",
        "title": "臺中市立大甲國中二年級數學補考題庫",
        "year": "unknown",
    },
    "neihu": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1706771169882T0v5rPBd.pdf",
        "title": "臺北市立內湖國中112學年度第一學期八年級第一次段考數學科試題卷",
        "year": "112",
    },
    "taibao": {
        "url": "https://www.tpjh.cyc.edu.tw/modules/tad_uploader/index.php?cat_sn=104&cfsn=680&name=%E5%98%89%E7%BE%A9%E7%B8%A3%E7%AB%8B%E5%A4%AA%E4%BF%9D%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%AD%B8112%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F+%E6%95%B8%E5%AD%B8%E7%A7%91%E5%85%AB%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83.pdf&op=dlfile",
        "title": "嘉義縣立太保國中112學年度第一學期八年級數學科第一次段考",
        "year": "112",
    },
    "sanchong": {
        "url": "https://www3.schs.ntpc.edu.tw/var/file/0/1000/attach/60/pta_6922_1139592_11280.pdf",
        "title": "新北市立三重高中八年級數學補考題庫",
        "year": "unknown",
    },
    "chonglin": {
        "url": "https://cdn.store-assets.com/s/1339278/f/12631614.pdf",
        "title": "新北市立崇林國中110學年度第一學期八年級數學科第一次定期評量試卷",
        "year": "110",
    },
    "zhongshan": {
        "url": "https://csjh.kl.edu.tw/books/file/65/109-1-%E5%9C%8B%E4%BA%8C%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E6%95%B8%E5%AD%B8%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高中109學年度第一學期國中部二年級第一次段考數學科試題卷",
        "year": "109",
    },
}

# The item locators below were checked against the linked public-school papers.
# Keep three distinct schools per question; source roles are intentionally stated
# narrowly so an adjacent A-8-3 operation is not misrepresented as an A-8-2 item.
MAPPING = {
    1: [
        ("taibao", "第4題：判斷三次多項式化簡後最多項數的說法"),
        ("guangzheng", "第11題：判斷三次多項式化簡後的最大項數"),
        ("sanchong", "第6題：判斷四次多項式化簡後最多項數"),
    ],
    2: [
        ("guangzheng", "第17題：比較多個多項式的次數"),
        ("beixin", "第18題：由二次項係數條件判斷一次多項式"),
        ("dajia", "第20題：由二次項係數條件判斷一次多項式"),
    ],
    3: [
        ("zhishan", "第4題：讀取未按降冪排列的多項式各次項係數"),
        ("guangzheng", "第18題：判讀指定次項係數及未出現項的係數"),
        ("beixin", "第28題：判讀最高次項與未出現的三次項係數"),
    ],
    4: [
        ("zhishan", "第4題：判讀零次項係數與常數項"),
        ("guangzheng", "第18題：由多項式判讀帶符號的常數項"),
        ("dajia", "第19題：辨認多項式各項係數與常數項"),
    ],
    5: [
        ("neihu", "第5題：辨認多項式的二次項係數"),
        ("zhishan", "第4題：辨認多項式中的二次項與其他次項"),
        ("guangzheng", "第18題：辨認各次項並判斷缺項係數"),
    ],
    6: [
        ("neihu", "第6題：將多項式結果按降冪排列"),
        ("chonglin", "填充題第3題：將多項式按升冪排列"),
        ("zhongshan", "第8題：判斷多項式是否依次方排列"),
    ],
    7: [
        ("zhishan", "第3、4題：判讀多項式次數與項的結構"),
        ("guangzheng", "第11、17題：判讀多項式最多項數與最高次數"),
        ("taibao", "第4、26題：判讀多項式最多項數、次數與係數"),
    ],
    8: [
        ("zhishan", "第6題：辨認含分母變數、絕對值等式子是否為x的多項式"),
        ("guangzheng", "第10題：辨認x的多項式與非多項式式子"),
        ("dajia", "八年級補考題庫第41題：辨認含分母變數、絕對值或方程式的x多項式"),
    ],
    9: [
        ("chonglin", "填充題第3題：將多項式按升冪排列"),
        ("beixin", "第28題：判斷多項式是否為升冪排列"),
        ("zhongshan", "第8題：判斷多項式項次排列方向"),
    ],
    10: [
        ("zhishan", "第3、4題：判讀多項式次數、指定項係數與常數項"),
        ("guangzheng", "第17、18題：判讀最高次項、次數、係數與常數項"),
        ("dajia", "第19、20題：判讀多項式項係數、常數項與次數條件"),
    ],
}


def reference(source_id, locator):
    source = SOURCES[source_id]
    return {
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "subject": "math",
        "locator": locator,
        "observedPattern": OBSERVED,
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main():
    updated = []
    for number, mappings in MAPPING.items():
        path = ROOT / "questions" / "math" / f"question-math-content-a-8-2-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data.get("reviewStatus") == "draft", f"unexpected status: {path.name}"
        assert data.get("answer", {}).get("value") and data.get("answer", {}).get("explanation"), path.name
        assert data.get("solutionStrategy") and len(data.get("solutionSteps", [])) == 5, path.name
        refs = [reference(source_id, locator) for source_id, locator in mappings]
        assert len({ref["title"] for ref in refs}) == 3, path.name
        data["examPatternRefs"] = refs
        data["provenance"]["sourceUrl"] = refs[0]["url"]
        data["provenance"]["sourceLocator"] = "；".join(f"{ref['title']}，{ref['locator']}" for ref in refs)
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        updated.append(path.name)
    print(json.dumps({"updated": updated, "count": len(updated), "status": "sources-realigned; questions remain draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()

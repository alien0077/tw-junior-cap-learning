import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "zhishan": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/697b23af02d6b7546a022da8.pdf",
        "title": "臺中市至善國中 114 學年度第一學期八年級第一次定期評量數學科試題卷",
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
    "dadao": {
        "url": "https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d",
        "title": "臺中市立大道國中 114 學年度第一學期八年級數學科補行評量題庫",
        "year": "114",
    },
}

# Each locator names the source's actual item numbers and the related skill.
ITEMS = {
    1: [
        ("zhishan", "第 4 題：由未按降冪排列的多項式辨認項的次方與係數"),
        ("guangzheng", "第 11、14 題：三次多項式最多項數及化簡後的項結構"),
        ("beixin", "第 28 題：判讀多項式的項、排列及缺項"),
    ],
    2: [
        ("zhishan", "第 3 題：多項式相加時依最高次項判讀結果次數"),
        ("guangzheng", "第 17 題：比較不同多項式的最高次數"),
        ("beixin", "第 6、13 題：多項式乘法與加法的次數判讀"),
        ("dadao", "第 1 題：依最高次項辨認一次、二次與常數多項式"),
    ],
    3: [
        ("zhishan", "第 4 題：讀取指定次方項的係數"),
        ("guangzheng", "第 14、18 題：化簡後辨認各次項係數，含缺項係數為 0"),
        ("beixin", "第 28 題：判讀多項式未出現之次方項與係數"),
    ],
    4: [
        ("zhishan", "第 4 題：辨認零次項係數與常數項"),
        ("guangzheng", "第 14、18、22 題：分辨有號常數項及其與係數的關係"),
        ("beixin", "第 28 題：判讀含常數項的多項式結構"),
    ],
    5: [
        ("zhishan", "第 5 題：以多項式加減結果辨認同次項能否合併"),
        ("guangzheng", "第 12、13 題：合併同類項並排除常數項與 x 項混併"),
        ("dadao", "第 28 題：多項式相加時按相同次方合併各項"),
    ],
    6: [
        ("zhishan", "第 4 題：從非標準排列讀取各次項"),
        ("guangzheng", "第 14 題：化簡後判讀各次項並按次方整理"),
        ("beixin", "第 28 題：判斷多項式項次排列方向"),
    ],
    7: [
        ("zhishan", "第 3、4 題：分別判讀多項式次數及項的結構"),
        ("guangzheng", "第 11、17 題：由次數辨認多項式項數上限與最高次"),
        ("beixin", "第 6、13 題：辨認多項式次數在乘法、加法中的變化"),
        ("dadao", "第 1 題：依最高次項辨認多項式次數"),
    ],
    8: [
        ("zhishan", "第 6 題：判斷含分母變數、絕對值及一般代數式是否為指定變數的多項式"),
        ("guangzheng", "第 10 題：辨認多項式與含絕對值或方程式的非多項式選項"),
        ("beixin", "第 18 題：由一般式係數條件判斷多項式的次數"),
    ],
    9: [
        ("zhishan", "第 5、7 題：以代數式乘除及括號運算整理多項式"),
        ("guangzheng", "第 8 題：以長方形分割面積表示並組合含變數的代數式"),
        ("beixin", "第 20 題：以圖形面積變化建立並整理多項式"),
        ("dadao", "第 4 題：將兩個一次式相乘並整理同次項"),
    ],
    10: [
        ("zhishan", "第 3、4 題：辨認多項式次數、指定項係數及常數項"),
        ("guangzheng", "第 17、18 題：辨認最高次項、次數、係數與缺項係數"),
        ("beixin", "第 28 題：綜合判讀多項式最高次、缺項與常數項結構"),
        ("dadao", "第 1 題：由最高次項區分多項式次數與常數多項式"),
    ],
}


def make_ref(source_key, locator):
    source = SOURCES[source_key]
    return {
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "subject": "math",
        "locator": locator,
        "observedPattern": "只參考校方公開試卷所呈現的能力面向及作答任務；本題使用全新敘述、係數或情境，不複製原題文字、數據、選項或解析。學年度未見於試卷者明記 unknown。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


updated = []
for number, items in ITEMS.items():
    path = ROOT / "questions" / "math" / f"question-math-content-a-8-2-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = [make_ref(*item) for item in items]
    data["examPatternRefs"] = refs
    data["provenance"]["sourceUrl"] = refs[0]["url"]
    data["provenance"]["sourceLocator"] = "; ".join(
        f"{ref['title']}，{ref['locator']}" for ref in refs
    )
    data["provenance"]["authoringNote"] = (
        "依官方課綱／KG 的多項式概念，並以多所公立國中公開試題中所列題號的能力面向作 pattern-only 參照；"
        "本題題幹、數值、選項、正確答案說明與逐步解法為原創，未重製來源題目。"
        "來源與答案已作第一輪 AI 檢查，尚待版本融合、Terra 及完整發布 QA，維持 draft。"
    )
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    updated.append(path.name)

print(json.dumps({"updated": updated, "count": len(updated)}, ensure_ascii=False))

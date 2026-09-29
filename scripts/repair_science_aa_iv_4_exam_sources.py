#!/usr/bin/env python3
"""Replace Aa-IV-4 non-exam references with verified public-school exam items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/science"
SOURCES = {
    "neihu": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1706771265848lZjHm7hJ.pdf",
        "title": "臺北市立內湖國民中學112學年度第一學期八年級理化科第三次段考",
        "year": "112學年度",
    },
    "dawan": {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國民中學114學年度第一學期第三次段考二年級自然科試卷",
        "year": "114學年度",
    },
    "fuhe": {
        "url": "https://www.fhjh.ntpc.edu.tw/var/file/0/1000/img/156/149796265.pdf",
        "title": "新北市立福和國民中學113學年度第一學期第三次段考自然科試題",
        "year": "113學年度",
    },
    "kc114": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E7%90%86%E5%8C%96_2.pdf",
        "title": "高雄市立國昌國民中學114學年度第一學期二年級自然科第三次段考",
        "year": "114學年度",
    },
    "tnfsh": {
        "url": "https://www.tnfsh.tn.edu.tw/df_ufiles/256/108-%E8%A4%87%E9%81%B82-%E6%95%B8%E7%90%86%E8%B3%87%E5%84%AA%E7%8F%AD-%E5%8C%96%E5%AD%B8%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "國立臺南第一高級中學108年數理資優班化學科複選試題",
        "year": "108年",
    },
}

# Each locator was checked against the linked original PDF. Three distinct
# papers are retained per question; refs describe skill only, never copied text.
ITEMS = {
    1: [("neihu", "PDF第3頁第28題", "現代週期表依原子序排列"), ("dawan", "PDF第3頁第26題", "以質子數說明現代週期表排序"), ("fuhe", "PDF第9頁第32題題組引言", "辨識莫斯利以原子序排列現代週期表")],
    2: [("neihu", "PDF第3頁第28題題組", "讀取週期表橫列與元素位置"), ("dawan", "PDF第3頁第26題", "由週期表橫列與縱行資訊分類元素"), ("fuhe", "PDF第9頁第32題題組", "依週期表位置比較元素規律")],
    3: [("neihu", "PDF第3頁第29題", "族以相似化學性質分類"), ("dawan", "PDF第3頁第27題", "辨認第1族及第18族的族性質"), ("fuhe", "PDF第9頁第32題", "由週期表位置判斷族內元素性質")],
    4: [("dawan", "PDF第3頁第21題", "辨認金屬元素常見物理性質及反例"), ("neihu", "PDF第3頁第30題", "依族位置辨認鹼金屬及其性質"), ("kc114", "PDF第3頁第24題", "比較金屬與非金屬元素性質")],
    5: [("neihu", "PDF第3頁第30題", "根據週期表族位置判斷鹼金屬性質"), ("dawan", "PDF第3頁第29題", "把元素應用資料連結到週期表區域"), ("fuhe", "PDF第9頁第32題", "依週期表位置推論元素族性質")],
    6: [("kc114", "PDF第4頁第28題", "同一週期由左至右比較原子序"), ("neihu", "PDF第3頁第28題", "依週期表排列規則比較元素位置"), ("dawan", "PDF第3頁第26題", "以原子序判讀現代週期表排列")],
    7: [("neihu", "PDF第3頁第29題", "族內元素化學性質相似"), ("dawan", "PDF第3頁第27題", "由族別辨認元素性質規律"), ("fuhe", "PDF第9頁第32題", "根據同族位置比較元素化學性質")],
    8: [("neihu", "PDF第3頁第28題", "以週期表內容判斷排序及結構主張"), ("dawan", "PDF第3頁第26題", "依週期表資料判別敘述是否正確"), ("fuhe", "PDF第9頁第32題", "以位置證據比較化學性質主張")],
    9: [("tnfsh", "PDF第2頁第二大題第(1)小題", "依週期規律推估未發現元素及其性質"), ("fuhe", "PDF第9頁第32題題組引言", "辨別門得列夫與莫斯利對週期表的貢獻"), ("dawan", "PDF第3頁第26題", "檢核現代週期表形成者與排序依據")],
    10: [("neihu", "PDF第3頁第30題", "依族位置推論鹼金屬性質"), ("dawan", "PDF第3頁第29題", "結合週期表區域推論元素性質"), ("fuhe", "PDF第9頁第32題", "從週期表位置提出有邊界的性質推論")],
}

SOLUTIONS = {
    1: ("先鎖定元素身分的排序量，再用原子序定義排除粒子質量與物性混淆。", "現代週期表依原子序遞增排列，而原子序就是質子數。中子數可能因同位素而不同；熔點與密度是物性，不是元素排序座標，因此答案為C。", ["先辨認題目問的是週期表的排序依據，而不是元素性質。", "回想原子序的定義：原子核內的質子數就是原子序。", "現代週期表依原子序由小至大安排元素的位置。", "中子數可因同位素改變，熔點與密度也不決定元素位置。", "因此只有原子序（質子數）符合，正確選項是C。"]),
    2: ("從橫列辨識週期，再連結到電子層數；勿把同族規律誤用在同週期。", "同一橫列就是同一週期，國中原子模型中同週期元素具有相同的電子層數。最外層電子數會沿週期改變，質量數也不因此相同，所以答案為A。", ["題目給的是同一橫列，先將它辨認為週期而非族。", "週期號對應原子所占有的電子層數。", "因此同一週期的元素具有相同電子層數。", "最外層電子數沿週期改變，元素質量數也不會相同。", "符合週期特徵的是電子層數相同，正確選項為A。"]),
    3: ("先找同族原子的外層電子規律，再說明它如何影響鍵結與反應。", "同族元素的最外層電子數或排列方式通常相近；最外層電子參與鍵結與化學反應，因此化學性質常呈相似趨勢，但不代表原子序或密度相同，答案為D。", ["題目要解釋的是同一族元素化學性質為何相似。", "同族位置通常對應相近的最外層電子數或排列方式。", "最外層電子參與原子鍵結，會影響反應方式。", "相近外層結構能支持化學性質相似，但不推出原子序相同。", "所以最外層電子排列相近是主因，正確選項為D。"]),
    4: ("逐組核對元素分類；只有每個成員都屬金屬時，該組才符合題意。", "鈉、鎂、鋁在週期表中皆屬金屬。A與D含氟、氯、氧、碳或硫等非金屬；C的氦、氖、氬是惰性氣體而非金屬，因此答案為B。", ["逐一讀出每個選項的元素，不能只看其中一個熟悉元素。", "鈉、鎂、鋁均位於週期表金屬區，符合金屬分類。", "A與D都含非金屬元素，故整組不是全金屬。", "C所列氦、氖、氬是惰性氣體，也不是金屬元素。", "只有B的三種元素全屬金屬，正確選項為B。"]),
    5: ("先以週期定位列、再以族定位欄，最後核對氯的外層電子與分類。", "第3週期第17族的位置是氯；氯屬非金屬鹵素，最外層通常有7個電子。A、B描述第1族金屬特徵，D把位置錯認為氬，因此答案為C。", ["先用第3週期確認題目指定的是第三個橫列。", "再沿第17族縱欄找出交會位置，元素是氯。", "氯屬鹵素，是非金屬，不是第1族鹼金屬。", "第17族主族元素最外層通常有7個電子。", "只有C同時符合元素、分類與電子數，正確選項為C。"]),
    6: ("將週期表的排列規則套用到相鄰位置，並用質子數差驗證方向。", "現代週期表依原子序遞增排列；同一週期向右移一格通常就是下一個原子序，質子數增加1，因此答案為A。", ["先確認元素仍在同一週期，移動方向是由左向右。", "現代週期表按原子序由小至大依序排列。", "原子序等於質子數，相鄰元素的質子數通常差一。", "因此向右移一格，原子序增加1而非減少或不變。", "符合排列規則的是增加1，正確選項為A。"]),
    7: ("比較化學性質時優先找外層電子線索，不以顏色或熔點代替化學證據。", "同族元素通常有相近的最外層電子排列，因而表現出相似的化學反應趨勢。顏色或熔點相同並不能單獨證明化學性質相似，所以答案為D。", ["先確認題目要比較的是化學性質而非外觀或物理性質。", "化學反應與原子的最外層電子及鍵結方式密切相關。", "同族位置可提示外層電子排列相近，支持性質相似推論。", "顏色或熔點相同並不足以證明兩元素反應方式相同。", "所以應查同族與外層電子，正確選項為D。"]),
    8: ("把定位、可觀察結構與趨勢推論分開，結論強度不可超過表格證據。", "週期與族提供元素位置，外層電子及金屬／非金屬區域可支援趨勢判斷；合理做法仍須保留「通常、可能」等限制，不能只靠表格顏色或位置宣稱毫無例外，因此答案為B。", ["先在週期表中定位元素的週期與族，而非憑名稱猜測。", "再檢查外層電子與金屬、類金屬或非金屬區域資訊。", "依據已知週期性提出可能的性質，並區分觀察與推論。", "用通常或可能保留適當限制，不把趨勢說成絕對定律。", "符合證據推理步驟的是B，故選B。"]),
    9: ("抓住科學史中的規律、預測與後續驗證鏈，不把預測誤作免驗證結論。", "門得列夫依已知元素的週期規律，在表中留下空缺並預測未知元素及其性質；後續發現可與預測比較，讓證據支持或修正模型，因此答案為C。", ["先整理當時已知元素，尋找性質反覆出現的週期規律。", "規律顯示表格空缺可能對應尚未發現的元素。", "依空缺位置提出元素存在及其性質的可檢驗預測。", "新元素被發現後，將實際資料與預測逐項比較。", "可檢驗預測並接受證據檢查的是C，故選C。"]),
    10: ("先判斷週期表區域，再以外層電子推測反應傾向並保留不確定性。", "週期表右上方通常是非金屬區；最外層接近填滿的原子可能透過得電子或共用電子形成較穩定排列。這是趨勢而非對每種情境的絕對保證，所以答案為D。", ["先定位週期表右上方，判斷該區域多為非金屬元素。", "依題意確認最外層電子數已接近填滿狀態。", "得電子或共用電子都可能形成較穩定的外層排列。", "週期趨勢只能支持較可能的方向，不能保證所有反應。", "只有D符合區域、外層電子與證據限制，正確選項為D。"]),
}


def make_ref(key: str, locator: str, skill: str) -> dict[str, str]:
    source = SOURCES[key]
    pattern = f"原卷{locator}考查：{skill}。本題只借用能力方向，題幹、選項、答案及解說均重新撰寫。"
    return {
        "url": source["url"], "title": source["title"], "year": source["year"],
        "subject": "science", "locator": locator, "locatorLevel": "item",
        "pattern": pattern, "observedPattern": pattern,
        "reuseDecision": "pattern-only", "status": "recorded",
    }


def main() -> None:
    for number, rows in ITEMS.items():
        path = QDIR / f"question-science-content-aa-iv-4-{number}.json"
        question = json.loads(path.read_text(encoding="utf-8"))
        question["examPatternRefs"] = [make_ref(*row) for row in rows]
        question["solutionStrategy"], question["answer"]["explanation"], question["solutionSteps"] = SOLUTIONS[number]
        question["provenance"]["sourceUrl"] = SOURCES[rows[0][0]]["url"]
        question["provenance"]["sourceLocator"] = "；".join(
            f"{SOURCES[key]['title']}：{locator}（{skill}；pattern-only）"
            for key, locator, skill in rows
        )
        question["provenance"]["authoringNote"] = (
            "依三份公立學校原卷所呈現的單元能力方向獨立改寫，未複製原題、選項、圖表或解答；"
            "答案與五步解題維持原創，仍待完整學科、授權界線及第二輪AI複核。"
        )
        question["updatedAt"] = "2026-09-24"
        question["reviewStatus"] = "draft"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for key, source in SOURCES.items():
        if source["url"] not in catalog.setdefault("questionSourceUrls", []):
            catalog["questionSourceUrls"].append(source["url"])
        if not any(item.get("url") == source["url"] for item in catalog.setdefault("sources", [])):
            catalog["sources"].append({
                "institution": source["title"].split(source["year"])[0].strip(),
                "url": source["url"], "subjects": ["science"],
                "availableMaterial": source["title"],
                "researchUse": "Aa-Ⅳ-4週期表排序、族與週期、族性質、元素分類與週期規律的指定題號能力方向；逐題pattern-only改寫。",
                "licenseBoundary": "原卷公開查閱不等於可重製；不複製原題、原選項、原圖表或答案。",
            })
    catalog["updatedAt"] = "2026-09-24"
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

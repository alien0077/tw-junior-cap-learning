#!/usr/bin/env python3
"""Replace false Jf-IV-2 exam provenance with verified public-school items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/science"

SOURCES = {
    "neihu": {
        "url": "https://www.nhjh.tp.edu.tw/uploads/1659511832163bbfokDfl.pdf",
        "title": "臺北市立內湖國中110學年度第二學期第三次段考八年級自然科學（理化）試題卷",
        "year": "110學年度",
    },
    "guochang": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E7%90%86%E5%8C%96_1.pdf",
        "title": "高雄市立國昌國民中學113學年度第二學期第三次段考二年級理化科試題",
        "year": "113學年度",
    },
    "xiaogang108": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%87%AA%E7%84%B6/108-2-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf",
        "title": "高雄市立小港國民中學108學年度第二學期第三次段考二年級自然科試題",
        "year": "108學年度",
    },
    "xiaogang104": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%87%AA%E7%84%B6/104-2-3%202%E5%B9%B4%E5%8F%8A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國民中學104學年度第二學期第三次段考二年級自然科試題",
        "year": "104學年度",
    },
}

# Each tuple is (source, precise item locator, independently observed skill).
ITEMS = {
    1: [("neihu", "PDF第1頁第8題", "由烴類元素組成判讀完全燃燒產物"), ("xiaogang108", "試題第31題", "依烴類性質判斷完全燃燒產物"), ("guochang", "PDF第5頁第45題", "由燃燒反應式與生成物比較有機物" )],
    2: [("neihu", "PDF第1頁第8、10題", "比較烴類與醇類的元素組成和性質"), ("xiaogang108", "試題第27、31題", "辨認乙醇性質並比較烴類燃燒"), ("guochang", "PDF第1頁第4題及第5頁第45題", "判讀醇類性質及有機物燃燒" )],
    3: [("neihu", "PDF第1頁第10題", "依醇類水溶液性質辨認乙醇特徵"), ("xiaogang108", "試題第27題", "判讀乙醇分子式與水溶液性質"), ("guochang", "PDF第1頁第4題", "比較醇類溶水及水溶液性質" )],
    4: [("neihu", "PDF第1頁第12題", "由羧基與水溶液性質判斷有機酸"), ("xiaogang108", "試題第29題", "辨認有機酸的官能基與酸性"), ("guochang", "PDF第4頁第38題", "由溶解度、氣味及酸鹼資料辨認液體" )],
    5: [("neihu", "PDF第3頁第37至38題", "把氣味觀察與溶解、石蕊資料合併辨識液體"), ("xiaogang108", "試題第28題", "由生活中的果香線索判斷酯類"), ("guochang", "PDF第4頁第38題", "以氣味和性質資料辨識常見有機物" )],
    6: [("neihu", "PDF第3頁第37至38題", "以相同操作比較水溶性、氣味和酸鹼反應"), ("xiaogang108", "試題第29至32題", "比較烴類、有機酸及酯類的性質"), ("guochang", "PDF第4頁第38題", "從液體性質表推論物質類別" )],
    7: [("neihu", "PDF第1頁第8題", "依烴類完全燃燒產物進行反應推理"), ("xiaogang108", "試題第31題", "辨讀烴類完全燃燒的產物關係"), ("guochang", "PDF第5頁第45題", "由燃燒生成物反推有機物類型" )],
    8: [("neihu", "PDF第1頁第1題及第3頁第38題", "辨認有機酸與醇的酯化反應物及條件"), ("xiaogang108", "試題第32題", "判讀酯類生成及常見性質"), ("guochang", "PDF第1頁第3題及第4頁第34題", "由酸與醇形成酯類並辨識酯的組成" )],
    9: [("neihu", "PDF第1頁第9至10題", "辨認甲醇毒性與變性酒精中的醇類"), ("xiaogang104", "試題第21至22題", "辨認變性酒精所含有毒甲醇及乙醇用途"), ("guochang", "PDF第1頁第4題", "辨認工業酒精添加甲醇的安全風險" )],
    10: [("neihu", "PDF第1頁第4、5、7、10、12題", "由含碳例外、分子式及官能基分類有機物"), ("xiaogang108", "試題第27至32題", "從乙醇、有機酸與酯類性質建立分類依據"), ("guochang", "PDF第1頁第1至5題及第4頁第38題", "結合官能基與性質資料分類常見有機物" )],
}

DETAILS = {
    1: ("先用元素組成判讀燃燒產物，再逐元素核對。", "烷類只由碳、氫組成；題目指定完全燃燒，表示氧氣供應充足，主要生成二氧化碳和水。答案為 A。", ["烷類分子只有碳原子與氫原子，燃料本身不含氯、鈉或硫。", "完全燃燒時，碳原子氧化後形成二氧化碳。", "氫原子氧化後形成水，因此兩種主要產物分別含有 C、H。", "氧原子由外界氧氣供應；它不是把燃料中的氯或硫變成產物。", "只有 A 同時符合碳、氫完全燃燒的產物，故選 A。"]),
    2: ("比較分子組成與官能基，再判斷哪些性質共通、哪些不同。", "乙醇含羥基而烷類只有碳氫骨架，結構差異會影響溶解等性質；兩者碳氫部分完全燃燒仍形成二氧化碳與水。", ["先把乙醇寫成 C₂H₅OH，注意它含有碳、氫、氧。", "烷類只含碳、氫；乙醇的羥基是造成分子性質差異的重要結構。", "兩者均可燃，完全燃燒時碳生成 CO₂、氫生成 H₂O。", "含氧不代表不能燃燒，也不能據此說兩者溶解性相反或結構相同。", "因此 A 同時保留結構差異與共同燃燒產物，答案為 A。"]),
    3: ("從官能基的極性推論分子與水的作用，再比較非極性骨架。", "乙醇的羥基可與水形成氫鍵等分子間作用；烷類主要是非極性碳氫結構，所以乙醇通常較易與水混合。", ["在乙醇結構中先定位羥基（—OH），而不是把它誤認為離子。", "羥基具有極性，可與極性的水分子形成氫鍵等吸引作用。", "烷類主要由非極性 C—C、C—H 鍵構成，與水作用較弱。", "溶解差異源自分子結構與分子間作用，不是乙醇不含碳或變成鹽。", "故 A 正確說明羥基與水的作用，是最合理的解釋。"]),
    4: ("先讀指示劑觀察，再用水溶液酸鹼性解釋有機酸行為。", "醋酸在水中部分解離，溶液呈酸性；紫色石蕊轉紅支持酸性判斷，弱酸仍是酸。", ["把觀察結果記清楚：紫色石蕊加入醋酸水溶液後變紅。", "石蕊變紅是酸性溶液的指示，不是鹼性或金屬性證據。", "醋酸是弱酸，在水中部分解離並產生 H⁺（以水合氫離子形式存在）。", "部分解離不等於完全沒有離子，也不會使溶液變成中性。", "符合觀察與解離情形的是 A：溶液呈酸性，故選 A。"]),
    5: ("把氣味當作觀察資料而非身分或安全證明，尋找可驗證資訊。", "酯類常有果香，但相似香味也可能來自不同天然或合成物；氣味不能單獨證明成分、來源或安全性。", ["先把『聞到香味』限定為感官觀察，不能直接當成化學鑑定結果。", "果香可能來自某些酯，也可能來自其他天然或合成香料。", "天然／合成是來源分類，與毒性或安全性不是同一個判斷軸。", "應再查成分、濃度、標示與適用的安全資料，並考慮實際暴露途徑。", "A 要求以多項可查證資料判斷，其他選項都把香味或天然性誤當安全保證。"]),
    6: ("公平控制條件並用可量測性質比較，避免以印象代替證據。", "固定濃度、體積與溫度後，比較水溶性、導電性及 pH 等資料，才較能把性質差異與官能基／結構連結；未知樣品不做點火測試。", ["先列出欲比較的結構：烷類只有碳氫骨架，醇類有羥基，有機酸有羧基。", "控制各樣品濃度、取樣體積、溫度和測量程序，避免多個變因同時改變。", "記錄水溶性、導電性與 pH 等可觀察或可量測結果，並設重複測量。", "將每一類的結果與官能基對照；不要只聞氣味，也不對未知液體點火。", "A 同時控制條件並比較多項相關證據，最能支持結構與性質的關聯。"]),
    9: ("未知化學品先確認身分與危害，再控制暴露和點火風險。", "未知有機液體可能揮發、易燃或有毒；應查標示與安全資料、隔離火源並在適當通風下處理，不以人體感官測試。", ["先停止操作，不把無標示液體當成乙醇或其他已知物質。", "由教師或管理者確認容器標籤及安全資料中的毒性、揮發性與易燃性。", "依安全規範使用最少量、防護具及適當通風，並移開火源。", "不可直接聞、品嘗、徒手接觸或倒入飲料容器，也不可用點火辨認。", "A 包含辨識危害與降低暴露的核心措施，故選 A。"]),
    10: ("沿著『結構特徵—可檢驗預測—測量證據』建立推理。", "碳氫骨架與羥基、羧基等官能基會影響分子極性、溶解及反應；預測需由實驗或可靠資料檢驗，不能只靠名稱或分子量。", ["先取得可靠的結構式或分子模型，確認原子連接方式而非只看物質名稱。", "辨認碳氫骨架及主要官能基，據此提出極性和分子間作用的初步判斷。", "由結構推測可能的溶解、酸鹼或反應特性，並把預測寫成可檢驗主張。", "選擇安全且能區分假設的測量或查證資料，控制條件後比較結果。", "A 保留結構、性質預測與證據驗證三個環節，推理最完整。"]),
}


def make_ref(source_key: str, locator: str, skill: str) -> dict[str, str]:
    source = SOURCES[source_key]
    observed = f"原卷{locator}考查：{skill}。本題僅借用此能力方向，情境、題幹、選項與解析另行撰寫。"
    return {
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "locator": locator,
        "subject": "science",
        "pattern": observed,
        "observedPattern": observed,
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    for number in range(1, 11):
        path = QDIR / f"question-science-content-jf-iv-2-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["examPatternRefs"] = [make_ref(*item) for item in ITEMS[number]]
        data["provenance"]["sourceUrl"] = ITEMS[number][0][0] and SOURCES[ITEMS[number][0][0]]["url"]
        data["provenance"]["sourceLocator"] = "；".join(f"{SOURCES[key]['title']}：{locator}（{skill}）" for key, locator, skill in ITEMS[number]) + "。僅供 pattern-only 原創改寫。"
        data["provenance"]["authoringNote"] = "依公開公立學校原卷的單題能力方向獨立改寫；未複製原題、選項、圖表或答案。答案與五步解題為本題重新核對，仍待全庫第二輪 AI／Terra 複核。"
        if number in DETAILS:
            strategy, explanation, steps = DETAILS[number]
            data["solutionStrategy"] = strategy
            data["answer"] = {"value": "A", "explanation": explanation + "答案為 A。"}
            data["solutionSteps"] = steps
        if number == 6:
            data["options"][0]["text"] = "固定樣品濃度、體積與溫度，比較水溶性、導電性及 pH，再對照官能基；不對未知液體點火"
        if number == 7:
            data["prompt"] = "丙烷（C₃H₈）在氧氣充足時完全燃燒，哪一個反應式已正確配平？"
            data["options"] = [
                {"id": "A", "text": "C₃H₈＋5O₂ → 3CO₂＋4H₂O"},
                {"id": "B", "text": "C₃H₈＋3O₂ → 3CO₂＋4H₂O"},
                {"id": "C", "text": "C₃H₈＋4O₂ → 2CO₂＋4H₂O"},
                {"id": "D", "text": "C₃H₈＋5O₂ → 3CO＋4H₂O"},
            ]
            data["answer"] = {"value": "A", "explanation": "先守恆碳得 3CO₂，再守恆氫得 4H₂O；右側共有 3×2＋4＝10 個氧原子，因此左側需 5O₂。答案 A。"}
            data["solutionStrategy"] = "依序守恆碳、氫、氧，最後檢查反應物與生成物兩側原子數。"
            data["solutionSteps"] = ["先數反應物：丙烷有 3 個碳、8 個氫。", "生成物先放 3CO₂，使碳原子數相同。", "放 4H₂O，使氫原子數成為 8。", "生成物側氧原子共 6＋4＝10 個，故需 5O₂。", "逐項核對 C、H、O 數量相等，選 A。"]
        elif number == 8:
            data["prompt"] = "實驗室要合成帶有果香的乙酸乙酯，下列哪組反應物與條件最合理？"
            data["options"] = [
                {"id": "A", "text": "乙酸與乙醇，在濃硫酸作用下加熱"},
                {"id": "B", "text": "甲烷與氧氣，在室溫下混合"},
                {"id": "C", "text": "乙酸與氫氧化鈉，在冰浴中反應"},
                {"id": "D", "text": "乙醇與二氧化碳，照光即可反應"},
            ]
            data["answer"] = {"value": "A", "explanation": "酯化由有機酸和醇反應生成酯與水；乙酸提供乙酸根部分、乙醇提供乙基部分，濃硫酸催化並加熱可促進反應。答案 A。"}
            data["solutionStrategy"] = "先依酯的名稱拆出酸端與醇端，再核對酯化條件及生成物類型。"
            data["solutionSteps"] = ["從「乙酸乙酯」辨認酸端是乙酸。", "辨認醇端為乙醇，不能以烷類或無機鹼取代。", "套用有機酸＋醇 ⇌ 酯＋水。", "核對濃硫酸作催化／脫水條件、加熱促進反應。", "只有 A 同時符合反應物和條件。"]
        elif number == 7:
            data["solutionSteps"] = ["先確認丙烷分子式 C₃H₈，反應物含 3 個 C、8 個 H。", "在生成物二氧化碳前放係數 3，讓碳原子守恆。", "在水前放係數 4，讓 8 個氫原子守恆。", "右側氧原子總數為 3×2＋4＝10，因此左側需要 5 個 O₂。", "檢查兩側 C、H、O 數量相同，只有 A 完全配平。"]
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog.setdefault("questionSourceUrls", [])
    catalog.setdefault("sources", [])
    for source in SOURCES.values():
        if source["url"] not in catalog["questionSourceUrls"]:
            catalog["questionSourceUrls"].append(source["url"])
        if not any(entry.get("url") == source["url"] for entry in catalog["sources"]):
            catalog["sources"].append({
                "institution": source["title"].split(source["year"])[0].strip(),
                "url": source["url"],
                "subjects": ["science"],
                "availableMaterial": source["title"],
                "researchUse": "逐題研究烴類燃燒、有機物分類、醇／酸性質、酯化及生活情境；僅以題號定位作 pattern-only 原創改寫。",
                "licenseBoundary": "公開查閱不等於可重製；不複製原題、選項、圖表或答案。",
            })
    catalog["updatedAt"] = "2026-09-24"
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

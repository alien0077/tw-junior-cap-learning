#!/usr/bin/env python3
"""Rewrite the cross-scale science unit from public-school exam patterns.

The linked exams are used only for traceable item-level pattern research. All
question wording, contexts, options, answers, and explanations below are new.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEIHU = "https://www.nhjh.tp.edu.tw/uploads/1675416611615Uti9exJs.pdf"
DAWAN = "https://www.dwm.kh.edu.tw/upload/344/104_64183/106-1-3%E8%87%AA%E7%84%B6%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"
GUOCHANG = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6_2.pdf"

SOURCES = {
    NEIHU: ("臺北市立內湖國中", "111學年度第一學期第三次段考八年級理化試題卷", "只依公開原卷指定題目研究粒子模型、化學式、原子組成與原子結構的命題模式；不重製題幹、選項、圖表或答案。"),
    DAWAN: ("高雄市立大灣國中", "106學年度上學期第三次段考三年級自然科試題", "只依公開原卷指定題目研究銀河系、恆星、星空觀察與天文尺度的命題模式；不重製題幹、選項、圖表或答案。"),
    GUOCHANG: ("高雄市立國昌國中", "107學年度第一學期三年級第三次段考自然科考題", "只依公開原卷第36題研究長度單位辨識的命題模式；不重製題幹、選項、圖表或答案。"),
}

ITEMS = [
    {
        "answer": "D", "source": (NEIHU, 8, "printed page 2, question 8"),
        "prompt": "標本瓶標籤寫著「3O₂」；若另一標籤寫「2O₃」，兩瓶所代表的氧原子總數相同嗎？",
        "options": [("A", "不相同，3O₂有3個氧原子，2O₃有2個"), ("B", "不相同，前者有6個，後者有3個"), ("C", "相同，但兩者都只有2個氧原子"), ("D", "相同，兩者各代表6個氧原子")],
        "explanation": "化學式前的係數數分子，右下標數每個分子中的原子；3O₂是3×2=6個氧原子，2O₃是2×3=6個，因此總原子數相同。",
        "strategy": "先把係數與下標分開讀，再用「分子數×每分子原子數」計算；不要把兩個位置上的數字直接相加。",
        "steps": ["先圈出 O₂ 前面的係數 3，這表示有三個 O₂ 分子。", "再看 O 的右下標 2，確認每個氧分子各含兩個氧原子。", "把第一種標示換成乘法：3 個分子 × 每個 2 原子 = 6 個原子。", "另一標示有 2 個 O₃ 分子，每個含 3 原子，所以也是 2×3=6。", "兩邊都得到六個氧原子，選 D；分子種類與個數仍然不同，不能說兩瓶的物質相同。"],
    },
    {
        "answer": "B", "source": (NEIHU, 11, "printed page 2, question 11"),
        "prompt": "某粒子式為 Ca(OH)₂。只計算一個式量單位中的原子個數，Ca、O、H 的比例為何？",
        "options": [("A", "1：1：2"), ("B", "1：2：2"), ("C", "2：1：2"), ("D", "1：2：1")],
        "explanation": "括號外的下標2會乘上括號內每一種原子的個數；鈣沒有括號所以是1，氧與氫各被乘2，比例為1：2：2。",
        "strategy": "由外往內分配括號下標，先寫出各元素的原子數，再依題目順序排列；不要把下標只乘到括號最後一個符號。",
        "steps": ["將式子分成 Ca 與括號內的 OH 兩部分，避免漏看括號範圍。", "Ca 後沒有下標，因此一個單位含 1 個鈣原子。", "括號外的 2 同時作用於 O 和 H，所以氧原子數是 1×2=2。", "氫也在括號內，故氫原子數同樣是 1×2=2。", "按 Ca、O、H 排列得到 1：2：2，對應 B；這是原子個數比，不是質量比。"],
    },
    {
        "answer": "C", "source": (NEIHU, 7, "printed page 2, question 7"),
        "prompt": "模型顯示兩種原子重新排列後形成新物質。下列哪個結論最符合粒子模型能支持的範圍？",
        "options": [("A", "反應後原子種類必定改變，因為生成物不同"), ("B", "只要原子重新排列，生成物就一定是混合物"), ("C", "模型可支持原子重新組合形成新粒子的解釋，但不能只憑圖判定所有宏觀性質"), ("D", "圖中每個圓的大小可直接當成該原子的實際半徑比例")],
        "explanation": "化學變化可用原子重新排列、形成新粒子來解釋；粒子圖是模型，不會自動提供未標示的實際尺寸或完整物性。",
        "strategy": "把圖中直接畫出的粒子關係，和圖外尚未提供的性質分開；模型支持機制解釋，不等於所有現象都已量測。",
        "steps": ["先讀圖例確認不同符號代表不同原子，而連線或組合代表粒子如何構成。", "比較反應前後：原子可重新配對或結合，圖本身沒有顯示原子種類被轉換。", "檢查生成物是否由同一種粒子構成；不能因為有反應就直接判成混合物。", "圖上圓圈的大小若沒有比例尺，只是辨識符號，不能當作真實半徑量測。", "因此選 C：模型支持重新組合的解釋；密度、熔點等宏觀性質仍需另外測量。"],
    },
    {
        "answer": "A", "source": (NEIHU, 9, "printed page 2, question 9"),
        "prompt": "學生整理化學式時寫下四個例子，哪一項的元素符號次序符合常見化學式表示？",
        "options": [("A", "硝酸鉀：KNO₃"), ("B", "氧化鎂：OMg"), ("C", "氯化鈣：ClCa"), ("D", "碳酸鈉：CO₃Na₂")],
        "explanation": "常見離子化合物通常先寫金屬陽離子，再寫非金屬或原子團；硝酸鉀寫作 KNO₃。其餘選項元素／原子團順序錯置。",
        "strategy": "先辨認化合物所含的陽離子與陰離子，再檢查化學式是否先陽離子後陰離子；不要依中文名稱的字面順序排列符號。",
        "steps": ["逐項找出化合物中的金屬元素：鉀、鎂、鈣或鈉，確認它們通常作陽離子。", "檢查 A：鉀的符號 K 放在硝酸根 NO₃ 前，呈現陽離子在前的次序。", "檢查 B 與 C：氧化鎂和氯化鈣把陰離子符號放在金屬前，順序不合常見寫法。", "檢查 D：碳酸根是完整原子團 CO₃，碳酸鈉應先寫鈉離子 Na，再寫碳酸根。", "只有 A 的 KNO₃ 符合，故選 A；本題檢查表示慣例，不是靠中文名稱逐字翻譯。"],
    },
    {
        "answer": "D", "source": (NEIHU, 12, "printed page 2, question 12"),
        "prompt": "一個中性氧原子的原子序為 8、質量數為 18。下列哪項核對結果正確？",
        "options": [("A", "質子8、中子18、電子8"), ("B", "質子18、中子8、電子18"), ("C", "質子8、中子10、電子10"), ("D", "質子8、中子10、電子8")],
        "explanation": "原子序等於質子數；質量數為質子與中子總數，因此中子數18−8=10。中性原子的電子數等於質子數，為8。",
        "strategy": "先用原子序找質子，再以質量數減質子求中子，最後利用「中性」條件配平電子；不要把質量數誤當中子數。",
        "steps": ["把題目給的原子序 8 對應到質子數，原子核內有 8 個質子。", "質量數計算的是質子加中子，故中子數要用 18−8，而不是直接抄 18。", "相減得到 10，因此原子核內有 10 個中子。", "題目說原子中性，正電質子總量與負電電子總量相抵，電子數為 8。", "依序核對質子8、中子10、電子8，符合 D；若是離子，電子數才可能不同。"],
    },
    {
        "answer": "C", "source": (DAWAN, 27, "PDF page 3, question 27"),
        "prompt": "天文社把觀測地點由地球擴大到更大的宇宙結構，哪個敘述正確描述銀河系？",
        "options": [("A", "銀河系只包含太陽，不包含其他恆星"), ("B", "銀河系就是整個宇宙，兩者範圍相同"), ("C", "太陽系位於銀河系之中，銀河系只是宇宙中的一個星系"), ("D", "銀河系是環繞地球運行的行星群")],
        "explanation": "地球屬於太陽系，太陽系位於銀河系；銀河系是宇宙中眾多星系之一，並非整個宇宙。這些名稱描述由局部到整體的包含層級。",
        "strategy": "先把層級由小到大排成「地球—太陽系—銀河系—宇宙」，再判斷每個選項有沒有把包含關係倒置或把部分當整體。",
        "steps": ["先定位地球：它是太陽系中的行星，並非銀河系的中心或全部。", "再看太陽系：太陽與其行星系統位於銀河系內，銀河系還包含大量其他恆星與天體。", "把銀河系放進更大的尺度：它是眾多星系之一，宇宙包含的不只銀河系。", "因此 A 把太陽系縮成只有太陽，B 把一個星系誤當整個宇宙，D 則混淆星系與行星系。", "符合層級關係的是 C；這是結構分類，不是由圖上圓圈大小量出距離。"],
    },
    {
        "answer": "B", "source": (GUOCHANG, 36, "PDF page 4, question 36"),
        "prompt": "研究員比較地球到月球與地球到鄰近恆星的距離，哪種單位搭配最恰當？",
        "options": [("A", "兩者都用奈米，因為奈米是國際單位"), ("B", "月地距離可用公里或天文單位，恆星距離常用光年"), ("C", "恆星距離用年，因為光年是時間單位"), ("D", "月地距離用光年，恆星距離用公分，兩者較容易比較")],
        "explanation": "光年是光在一年內行進的距離，是長度單位；月地尺度通常用公里，太陽系尺度常用天文單位，恆星間距離可用光年。",
        "strategy": "先看題目要量的是長度還是時間，再按尺度選單位；名稱含「年」不代表光年是時間。",
        "steps": ["題目比較兩個天體間的位置間隔，待描述量是距離，也就是長度。", "月球與地球相鄰於太陽系內，用公里可表達；太陽系尺度也常用天文單位。", "恆星離我們極遠，若以公里列出會得到很長的數字，光年能讓數值尺度較合宜。", "光年定義為光在一年中走過的距離，所以量綱是長度而不是時間。", "選 B；選單位時兼顧物理量與數值尺度，不應只看詞語裡的「年」。"],
    },
    {
        "answer": "A", "source": (DAWAN, 28, "PDF page 3, question 28"),
        "prompt": "觀星紀錄指出，某顆北天亮星在數晚的照片中幾乎維持同一方向。哪項說法最合理？",
        "options": [("A", "北極星是恆星，北半球較容易觀察；它仍會自行發光"), ("B", "北極星是行星，因反射太陽光才固定在天空"), ("C", "北極星只在南半球可見，且不發光"), ("D", "恆星看似固定表示地球完全沒有自轉")],
        "explanation": "北極星是恆星，會自行發光；它靠近天球北極方向，因此北半球夜空中視位置變化較小，但地球仍在自轉。",
        "strategy": "分開判斷天體分類、光源性質與觀測者所在半球；「相對位置變化小」不等於「天體不發光」或「地球不轉」。",
        "steps": ["題幹只描述連續夜晚的視方向近似不變，這是觀測位置特徵，不直接說明它是否發光。", "辨認北極星屬恆星；恆星能自行發光，行星主要反射恆星光。", "它位於北天極附近，所以從北半球觀察時，周圍星軌看起來繞其附近轉動。", "地球自轉仍會造成星空周日運動，只是北極星附近的視位置變化較不明顯。", "只有 A 同時符合分類與觀測條件；不要把「看起來近乎固定」當成「地球靜止」的證據。"],
    },
    {
        "answer": "D", "source": (DAWAN, 33, "PDF page 3, question 33"),
        "prompt": "天文觀察社整理四句筆記，哪一句需要修正？",
        "options": [("A", "恆星主要由氫、氦等物質構成"), ("B", "行星的衛星可繞行星運行，而行星也隨行星系繞恆星運行"), ("C", "冥王星目前分類為矮行星"), ("D", "同一季節星座在夜空中改變位置，主要是地球每日自轉造成")],
        "explanation": "同一時刻每夜星空位置改變與地球自轉有關；但不同季節夜間可見星座改變，主要是地球繞太陽公轉，夜晚朝向宇宙的方向隨季節改變。",
        "strategy": "抓住題目中的時間尺度：一天內的東升西落對應自轉；相隔數月的季節星空差異要檢查公轉。",
        "steps": ["先為現象標上時間尺度：題目問的是季節之間的星座差異，不是單一晚上的移動。", "地球自轉約一天一圈，能解釋星體在一夜之中東升西落的視運動。", "地球同時繞太陽公轉；經過數月後，夜晚面向宇宙的方向改變。", "A、B、C 是天體組成、軌道層級與分類的敘述；D 把季節差異歸因於每日自轉。", "所以應修正 D：季節星空差異主要來自公轉造成的夜間觀測方向變化。"],
    },
    {
        "answer": "B", "source": (DAWAN, 26, "PDF page 2, question 26"),
        "prompt": "科展模型把微小粒子畫成彩色球，並把太陽系畫成更大的球。若圖上沒有比例尺，觀眾能直接得出哪個結論？",
        "options": [("A", "彩色球直徑可直接換算原子直徑"), ("B", "這張圖可用來表達不同層級或組成關係，但不能據畫面尺寸比較真實尺度"), ("C", "圖上最大的球必定質量最大"), ("D", "若兩個圖示相切，就表示兩個天體實際接觸")],
        "explanation": "粒子圖與天文示意圖是不同尺度的模型；若未提供共同比例尺，畫面尺寸只利於辨識，不是可量測的真實尺寸或接觸證據。",
        "strategy": "先找比例尺、單位與圖例；缺少尺度校準時，只解讀圖明確編碼的關係，不把版面大小當測量數據。",
        "steps": ["檢查圖面是否提供比例尺或每個圖形代表的實際長度；題目明確說沒有。", "因此彩色球和太陽系圓形的大小是繪圖者選擇，不能換算成原子或天體直徑。", "圖示仍可能用來表示層級、包含關係或標籤分類，這些訊息需依圖例確認。", "沒有距離資訊時，圖上相切不代表實物接觸，圖形較大也不能推出質量較大。", "B 僅使用模型能支持的結構訊息，沒有把未標示的真實尺度塞進圖中。"],
    },
]


def source_ref(url: str, item: int, locator: str) -> dict:
    institution, title, boundary = SOURCES[url]
    year = "111" if url == NEIHU else "106" if url == DAWAN else "107"
    return {
        "url": url,
        "title": f"{institution}{title}",
        "year": year,
        "subject": "science",
        "locator": locator,
        "observedPattern": f"僅參考第{item}題的命題能力與推理結構；{boundary}",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    if len(ITEMS) != 10:
        raise ValueError(f"預期 10 題，實際為 {len(ITEMS)} 題；停止避免 ID 越界")
    expected_paths = [ROOT / f"questions/science/question-science-content-cross-atoms-to-universe-{n}.json" for n in range(1, 11)]
    if any(not path.is_file() for path in expected_paths):
        raise FileNotFoundError("既有穩定題目 ID 不完整；停止避免部分寫入")
    for n, item in enumerate(ITEMS, 1):
        path = expected_paths[n - 1]
        data = json.loads(path.read_text(encoding="utf-8"))
        url, item_no, locator = item["source"]
        ref = source_ref(url, item_no, locator)
        data["prompt"] = item["prompt"]
        data["options"] = [{"id": key, "text": text} for key, text in item["options"]]
        data["answer"] = {"value": item["answer"], "explanation": item["explanation"]}
        data["examPatternRefs"] = [ref]
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": url,
            "sourceLocator": f"{SOURCES[url][0]}公開原卷 {locator}；只取題型與推理能力作 pattern-only 參考，題幹、選項、答案、圖表均重新創作。",
            "authoringNote": "依官方課綱、Knowledge Graph 與公立學校公開試題的 item-level pattern-only 證據獨立改寫；沒有複製原題、選項、圖表或答案。題目維持 draft，尚待單元版本融合、內容與發布審查。",
        }
        data["solutionStrategy"] = item["strategy"]
        data["solutionSteps"] = item["steps"]
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-09-24"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    entries = catalog["sources"]
    details = {
        NEIHU: ("臺北市立內湖國中", "111學年度第一學期第三次段考八年級理化試題卷", ["science"], "第7–12題；粒子模型、氧的不同表示、化學式、原子組成與原子結構", SOURCES[NEIHU][2]),
        DAWAN: ("高雄市立大灣國中", "106學年度上學期第三次段考三年級自然科試題", ["science"], "第26–28、33題；行星示意圖非實際比例、銀河系、北極星、恆星特性與季節星空判讀", SOURCES[DAWAN][2]),
        GUOCHANG: ("高雄市立國昌國中", "107學年度第一學期三年級第三次段考自然科考題", ["science"], "第36題；奈米、公里、天文單位與光年等長度單位判讀", SOURCES[GUOCHANG][2]),
    }
    for url, (school, material, subjects, use, boundary) in details.items():
        replacement = {"institution": school, "url": url, "subjects": subjects, "availableMaterial": material, "researchUse": use, "licenseBoundary": boundary}
        matches = [index for index, row in enumerate(entries) if row.get("url") == url]
        if matches:
            entries[matches[0]] = replacement
        else:
            entries.append(replacement)
    catalog["sources"] = entries
    catalog["questionSourceUrls"] = sorted(set(catalog.get("questionSourceUrls", [])) | {url for url, _, _ in (item["source"] for item in ITEMS)})
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rewritten": len(ITEMS), "itemLevelRefs": len(ITEMS), "allRemainDraft": True}, ensure_ascii=False))


if __name__ == "__main__":
    main()

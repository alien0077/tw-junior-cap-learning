import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/science"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "探究問題、資料蒐集與實驗設計能力方向"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "觀察紀錄、變因辨識與證據推理能力方向"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "多元資料判讀、問題形成與結論界線能力方向"),
]

DATA = [
    ("observed phenomenon", "校園池水在連續三天的早晨都出現少量泡沫。若要把觀察轉成可研究的問題，哪一項最合適？", ["池水泡沫的多寡是否與前一晚的降雨量有關？", "泡沫是不是一定代表水被污染？", "我覺得泡沫很奇怪，所以答案就是清潔劑。", "把池水全部倒掉就能知道原因。"], "A", "選項 A 把可觀察的泡沫多寡與可量化的降雨量連結，能蒐集資料比較；其餘選項不是過早下結論、缺少測量定義，就是沒有提出可檢驗關係。"),
    ("multiple sources", "研究校園樹蔭是否影響地表溫度時，哪一組資料最能形成互相核對的證據？", ["只憑同學的印象描述", "樹蔭與空曠地的溫度紀錄，加上同時段的氣象資料與地點照片", "只量一次最熱的地方", "只看網路文章，不做現場紀錄"], "B", "選項 B 同時提供溫度數據、氣象背景與現場位置證據，能比較並檢查是否有其他因素；單一印象或一次測量不足以支撐結論。"),
    ("operational definition", "要研究『教室通風較好』，哪個做法最能把概念轉成可記錄的指標？", ["請同學憑感覺打分", "把通風好定義成每分鐘窗邊風速達到某範圍，並記錄溫度與二氧化碳濃度", "只寫『空氣很舒服』", "看到窗戶打開就判定一定通風好"], "B", "選項 B 將抽象的通風概念轉成風速、溫度與二氧化碳濃度等可重複記錄的指標，才便於比較。"),
    ("sampling fairness", "比較操場不同位置的螞蟻數量，哪種取樣安排較不容易偏向某一區？", ["只挑看起來螞蟻最多的地方", "只在午餐後量一次", "把操場分成相同大小區塊，在各區隨機選相同數量的樣點並於相近時間觀察", "由一位同學憑印象挑三個點"], "C", "選項 C 同時處理空間分布、樣點數量、選點方式與時間差異，能降低只挑特殊位置造成的偏差。"),
    ("repeated observation", "觀察兩種紙張吸水性時，為何每種紙張要用多張樣本並重複測量？", ["讓結果看起來更複雜", "減少偶然差異，估計同種紙張的典型表現", "保證任何測量都不會有誤差", "可以不用記錄厚度與水量"], "B", "重複測量可降低偶然誤差並比較平均表現，但不能保證零誤差，也不能取代控制厚度、水量等條件。"),
    ("source reliability", "網路貼文說『某植物一定能驅蚊』，你要先做哪項查核再把它當成研究線索？", ["直接轉貼給全班", "確認作者、資料日期、實驗方法與是否有可檢查的原始證據，再與其他可靠來源比對", "只看按讚數", "把貼文中的『一定』改成大字體"], "B", "查核作者、時間、方法與原始證據，並與其他來源交叉比對，才能把網路說法和可驗證的觀察問題區分開。"),
    ("control variables", "探討不同顏色遮光布對盆栽生長的影響，哪項應列為控制條件？", ["遮光布顏色", "每週植株高度增加量", "盆栽種類、土壤量、澆水量與照射時間", "研究者想得到的答案"], "C", "遮光布顏色是自變因，高度增加量是應變因；植物、土壤、水量與時間應固定，才能將差異歸因於顏色。"),
    ("evidence boundary", "四個地點各觀察一次後，發現樹下比水泥地低 2°C。哪個結論最符合證據界線？", ["所有樹下永遠比所有水泥地低 2°C", "在這四個地點、這次測量與當時條件下，樹下測得溫度較低；仍需更多時段確認", "一定是樹吸收了全部熱能", "可據此證明天氣預報錯誤"], "B", "結論必須限定樣本、時間與條件，並指出需要重複觀察；不能把少量資料無限推廣或加入未測量的機制。"),
    ("data organization", "記錄校園噪音時，哪份表格最有利於後續比較？", ["只寫『很吵』", "欄位包含日期、時間、地點、測得分貝、天氣與附近活動", "只記錄最高的一次數字", "把不同地點的數字混在同一格"], "B", "選項 B 保留時間、地點、測量值與可能影響因素，能依條件分組比較並追溯資料來源。"),
    ("integrated inquiry", "你發現午休後回收桶旁常有較多果蠅。哪個研究流程最完整？", ["先認定是某種水果造成，然後只拍一張照片", "查閱果蠅習性資料，提出『殘渣量與果蠅數是否相關』，訂定樣點與時間，重複記錄並比較結果", "請同學投票決定原因，不需測量", "把回收桶移走後宣稱已證明原因"], "B", "選項 B 依序包含背景資料、可檢驗問題、取樣與時間規畫、重複觀察及比較證據，符合完整探究流程。"),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url,
        "title": f"{title}；僅取能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114",
        "subject": "science",
        "locator": locator,
        "observedPattern": "公開自然科試題常以觀察現象、資料來源、變因控制、取樣與證據界線要求學生形成問題並判讀探究設計；本題為獨立改寫。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"先讀情境並圈出本題的探究焦點：{topic}。",
        "區分觀察到的現象、想改變或比較的因素、要記錄的指標，以及可能需要固定的條件。",
        f"逐一檢查選項是否能蒐集可重複、可核對的證據；答案是 {answer}。",
        f"用題幹資料回查：{explanation}",
        "最後限制結論的樣本、時間與測量條件，並指出若證據不足就要增加來源、樣本或重複觀察。",
    ]
    return {
        "id": f"question-science-performance-po-iv-1-{index}",
        "subject": "science", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-science-performance-po-iv-1"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": {
            "origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "公立國中自然科公開評量；僅研究觀察、探究設計與資料判讀能力方向，不重製原題、選項、圖表或答案。",
            "authoringNote": "依官方課綱 KG 與三個公立學校公開自然科評量來源的能力方向獨立重寫；情境、數據設計、選項、答案與解析均為原創；待第二輪 AI/Terra 內容複核。",
        },
        "reviewStatus": "draft", "updatedAt": "2026-09-09",
        "lessonId": "lesson-science-performance-po-iv-1", "examPatternRefs": refs,
        "solutionStrategy": "先把日常觀察轉成可測量的問題，再檢查資料來源、取樣、控制條件、重複測量與結論界線；不可用單一印象或未查證說法代替證據。",
        "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-science-performance-po-iv-1-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")

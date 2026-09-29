import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-root-a"
KGS = ["kg-science-content-a", "kg-science-learning-content"]
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1", "title": "高雄市立鹽埕國民中學公開定期評量試題頁", "year": "113-114"},
    {"url": "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "title": "新北市立板橋國民中學公開定期評量試題頁", "year": "113-114"},
    {"url": "https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "title": "新北市立新莊國民中學公開定期評量試題頁", "year": "113-114"},
]


def refs():
    return [{**s, "subject": "science", "locator": "公開自然科段考的生活情境、變因控制、物質／能量模型與證據判讀題型；僅取能力方向", "observedPattern": "以短情境或可觀察資料要求學生區分現象、解釋、變因與證據，並用模型或守恆關係推理；本題重新設計情境與選項。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


ITEMS = {
    "04": ("要探究光線是否影響植物生長，哪一項最適合作為結果變因？", ["植物高度", "花盆顏色", "學生姓名", "教室編號"], "A", "植物高度是可量測的生長結果，可在不同光照條件間比較；其他選項不是生長結果。", "先分辨研究者改變的光照條件與要觀察的生長結果。"),
    "05": ("同一室內的金屬湯匙摸起來比木湯匙冷，最合理的解釋是什麼？", ["木頭沒有粒子", "金屬會製造冷能", "兩支湯匙所在室溫不同", "金屬較容易把手的熱傳走"], "D", "金屬的導熱性較好，手的熱較快傳入金屬，因此觸感較冷；這不表示金屬自行產生冷能。", "把觸感差異拆成實際溫度與熱傳遞速率兩個問題。"),
    "06": ("學生把同一項測量重複五次，主要好處是什麼？", ["可看出測量變異並提高結果可靠度", "能保證假說一定正確", "能消除所有可能誤差", "會改變原本測量的變因"], "B", "重複測量可看出數值分散情形並估計較可靠的結果，但不能保證假說正確，也不能消除系統誤差。", "區分重複測量能改善的可靠度與它無法保證的真實性。"),
    "07": ("哪項觀察最直接支持某物質可能已溶解在水中？", ["標籤寫著可溶", "固體不再可見且溶液均勻", "學生預期會發生反應", "容器因顏色而變重"], "B", "固體消失且溶液均勻是可直接觀察的現象，能支持溶解的推論；標籤、期待與無關的重量說法不是直接觀察。", "先分開『看見的現象』與『根據標籤或期待做出的解釋』。"),
    "08": ("理想比較中，相同大小的力作用在較小質量的物體上，會有什麼結果？", ["加速度一定變小", "加速度較大", "物體必定靜止", "質量會變成零"], "B", "在其他條件相同時，牛頓第二定律 a＝F／m 表示質量較小會得到較大的加速度；不能由此推出物體必定靜止。", "固定力的條件，檢查質量在公式分母的位置，再判斷加速度方向與大小。"),
    "09": ("下列哪項對食物鏈的說法最有根據？", ["能量在生物間傳遞，通常到較高營養階層時可利用量減少", "能量只會在消費者之間循環，不會進入生產者", "每一階層都能把全部能量傳給下一階層", "食物鏈中的物質與能量都會以完全相同方式循環"], "C", "能量主要由生產者取得並沿食物鏈傳遞，但各階層有代謝與散失，因此可傳到較高階層的可利用能量通常減少。", "分開追蹤能量流與物質循環，不把兩者混成同一種封閉循環。"),
    "10": ("比較兩地天氣時，為什麼應在同一時間記錄兩地資料？", ["使溫度計變重", "不必再寫測量單位", "降低時間差造成的混淆變因", "證明天氣預報一定正確"], "C", "同時測量可讓兩地在相近時間條件下比較，降低一天中天氣變化造成的混淆；它不能保證預報正確。", "找出比較中必須控制的時間條件，再排除與測量無關的說法。"),
    "16": ("下列哪項觀察最能支持樣品是混合物，而不是單一純物質？", ["樣品只有一種顏色", "樣品放在透明容器中", "同一樣品可分出具有不同成分特徵的部分", "樣品名稱只有兩個字"], "C", "若同一樣品能分出具有不同成分特徵的部分，才直接支持含有多種物質；顏色、容器與名稱不能單獨判定。", "以可分離且可觀察的成分證據判斷，不用外觀或名稱代替組成分析。"),
    "17": ("冰塊融化成水，且沒有產生新物質，主要是哪一種變化？", ["化學變化", "元素變成另一元素", "物理變化", "化合物分解成不同元素"], "C", "固態水變成液態水，物質仍是水，只是狀態改變，因此屬於物理變化。", "先檢查是否產生新物質，再判斷只是狀態改變還是組成改變。"),
    "18": ("要比較兩種粉末是否由相同物質組成，哪項策略最符合證據導向的判斷？", ["只看包裝顏色", "在相同條件下比較可測量的性質並記錄結果", "只聞一次就下結論", "依粉末名稱長短判斷"], "B", "相同條件下的可測量性質能提供可比較證據；外觀或單次主觀感受不足以確定組成。", "先控制比較條件，再選擇可重複、可記錄的性質作為證據。"),
}


def steps(prompt, answer, explanation):
    return [
        f"讀題定位：先圈出題目要判斷的現象、條件與結果；本題問題是「{prompt}」。",
        "建立判準：把觀察到的資料、操弄的變因與要解釋的結果分開，不先用選項名稱猜答案。",
        f"核對正確選項 {answer}：{explanation}",
        "逐項排除：檢查其他選項是否混淆物質與能量、忽略控制變因、把期待當觀察，或超出題目資料能支持的範圍。",
        f"最後回查：將選項 {answer} 放回完整題幹，確認它同時符合題目條件與解析；若資料或條件改變，必須重新推理。",
    ]


for number, (prompt, options, answer, explanation, strategy) in ITEMS.items():
    path = OUT / f"question-science-root-a-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "lessonId": LESSON,
        "knowledgeIds": KGS,
        "reviewStatus": "draft",
        "updatedAt": "2026-09-12",
        "solutionStrategy": strategy,
        "solutionSteps": steps(prompt, answer, explanation),
        "examPatternRefs": refs(),
    })
    data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立國中公開自然科定期評量頁僅作生活情境、變因控制、物質／能量模型與證據判讀的能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與公立學校公開試題能力方向獨立改寫；題幹、選項、答案、解析、策略與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} questions")

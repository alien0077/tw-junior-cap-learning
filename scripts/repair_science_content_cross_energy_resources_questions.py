import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-cross-energy-resources"
KG = "kg-science-content-cross-energy-resources"
SOURCES = [
    {"url": "https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "title": "國立中科實驗高級中學第五冊補行評量題庫國中自然科學", "year": "115"},
    {"url": "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelV6TDNCMFlWODBOalF6WHprd01UQTVPVFZmTXpJNE1qY3VjR1Jt&fname=WW54RPOKIC44VXMPVS0430WTVWB42514RKFGB1NOQP25CC40ZWROGH540054FGSSZTCCCDOOA404GDJGYWNK4000WSRKB1ICNPYT4040WSB0POVWECOK24OKMK4044ZXDGA0TS14QOKO40ICDGB024MP013504CCZWB4CDSWYSA4GHQKICCCZXZXIG10QKZWXSJGVX2020UWRKMK21GDNLRK", "title": "新北市立溪崑國民中學114學年度第二學期八年級科技領域補行評量題庫", "year": "114"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/3-%E8%87%AA%E7%84%B6_3.pdf", "title": "高雄市立國昌國民中學114學年度第一學期三年級自然科第二次段考試題", "year": "114"},
]


def refs():
    return [{**s, "subject": "science", "locator": "能量形式與轉換、能量守恆、功率、效率、發電方式、再生能源、儲能與供電限制", "observedPattern": "公開學校自然科試題常用發電系統、力學情境與生活能源比較，要求判讀能量流向、守恆、效率及再生能源的條件；本題只採能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-cross-energy-resources-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": "A", "explanation": explanation + "選 A。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然科資料僅供能量流、發電轉換、功率／效率與能源限制的能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開自然科資料的能力方向獨立改寫；題幹、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "手電筒使用電池點亮 LED，最完整的能量流描述是？", {"A": "電池的化學能轉為電能，再主要轉為光能，同時有部分能量成為熱", "B": "化學能消失後憑空產生光能", "C": "LED 將光能轉回化學能而電池不變", "D": "只要看見光，就表示全部輸入能量都成為光"}, "能量可轉換但總量守恆；LED 的有效輸出是光，電路與元件也會產生熱等非目標輸出。", "畫出來源、裝置、有效輸出與散失四個節點，再檢查能量是否有去向。", ["辨認電池提供的初始能量形式。", "追蹤電路中化學能轉成電能。", "把 LED 的光視為有效輸出。", "補上電阻與元件產生的熱等非目標輸出。", "所以選 A。"], "easy"),
    make(2, "水力發電站利用高處水庫的水發電，主要能量轉換順序哪一項較合理？", {"A": "水的重力位能→水的動能→渦輪機與發電機的機械／電能", "B": "電能→水的化學能→重力位能", "C": "水的熱能直接變成核能", "D": "水的質量消失後直接變成電能"}, "高處水具有重力位能，下降時轉為水流動能，再經渦輪和發電機轉為電能；實際系統還有摩擦與熱損失。", "沿著水從高處到發電機的實際路徑逐節點標註能量形式。", ["找出水庫高度提供的能量形式。", "追蹤水下降與流動造成的動能。", "加入渦輪機的轉動和發電機的電能輸出。", "檢查是否需要標示摩擦與熱等損失。", "所以選 A。"], "medium"),
    make(3, "輸入裝置的能量為 500 J，其中 350 J 成為有用輸出。此裝置效率是多少？", {"A": "70%", "B": "30%", "C": "150%", "D": "850%"}, "效率＝有用輸出能量÷輸入能量＝350÷500＝0.70，也就是 70%。", "先寫效率定義，再確認分子是有用輸出、分母是全部輸入。", ["寫出效率公式：有用輸出÷輸入。", "代入有用輸出 350 J。", "代入輸入能量 500 J。", "計算 350÷500＝0.70。", "換成百分比得到 70%，所以選 A。"], "medium"),
    make(4, "兩台設備都完成 600 J 的工作，甲用 3 秒、乙用 6 秒。哪一項正確？", {"A": "甲的平均功率為 200 W，乙為 100 W，甲完成得較快", "B": "甲乙功率相同，因為作功相同", "C": "甲功率為 2 W，乙為 1 W", "D": "乙功率較大，因為花費時間較久"}, "功率＝作功÷時間；甲 600÷3＝200 W，乙 600÷6＝100 W，甲每秒轉換的能量較多。", "比較功率時固定作功，直接用時間作分母並檢查單位。", ["寫出功率公式 P＝W/t。", "計算甲：600 J÷3 s。", "計算乙：600 J÷6 s。", "比較每秒完成的能量與時間。", "甲 200 W 大於乙 100 W，所以選 A。"], "medium"),
    make(5, "摩擦使機械系統發熱時，最符合能量守恆的說法是？", {"A": "可利用的有用輸出減少，但能量轉成熱等形式後總量仍守恆", "B": "摩擦使能量總量消失", "C": "摩擦會使系統憑空增加能量", "D": "只要產生熱，就代表輸入能量變多"}, "摩擦把部分原本可用於目標工作的能量轉成內能或熱，降低有用輸出比例，但不破壞能量守恆。", "區分總能量守恆與有用能量比例，不把『散失』當成消失。", ["列出輸入能量總量。", "辨認摩擦造成的熱是另一種能量去向。", "比較目標輸出是否因熱分流而減少。", "確認各形式能量加總仍與輸入相符。", "所以選 A。"], "easy"),
    make(6, "下列哪一項最能區分『能源』與『能量形式』？", {"A": "煤炭是可取得的能源來源；燃燒後可把其中化學能轉成熱能等形式", "B": "能源和能量是完全相同的名詞", "C": "熱能本身一定是能源來源", "D": "只要能量會轉換，就不需要任何能源來源"}, "能源是人類可取得、利用與轉換的來源；化學能、熱能和電能則是描述能量狀態或形式。", "先問『從哪裡取得』，再問『以什麼形式存在或轉換』。", ["找出題目中的燃料或來源。", "把煤炭辨認為可取得的能源。", "把燃燒前後的化學能與熱能分開。", "確認來源名稱和能量形式不是同一層次。", "所以選 A。"], "easy"),
    make(7, "太陽能與風力都屬再生能源，但某離島仍需蓄電池或其他電源，最合理的原因是？", {"A": "日照與風速會變動，輸入功率不一定能隨時配合負載需求", "B": "再生能源完全不能轉成電能", "C": "只要是再生能源，供電功率永遠固定", "D": "蓄電池會使能量守恆失效"}, "再生描述來源可自然補充，不代表瞬時供應穩定；天候變化與負載需求需要儲能或多來源調節。", "先分辨『可再生』和『供應穩定』是不同評估面向。", ["列出太陽能與風力的輸入條件。", "檢查日照和風速是否隨時間變化。", "比較變動輸入與使用者即時負載。", "說明蓄電池或備援來源如何調節時間差。", "所以選 A。"], "medium"),
    make(8, "某太陽能板輸入 1000 J，輸出電能 180 J；另一塊輸入 400 J，輸出電能 100 J。哪一項正確？", {"A": "第一塊效率 18%，第二塊效率 25%，不能只以輸出量判定效率", "B": "第一塊效率較高，因為輸出電能 180 J 較大", "C": "兩塊效率都為 25%，因為輸入不同不重要", "D": "效率可以超過 100%，所以第二塊為 250%"}, "第一塊 180÷1000＝18%；第二塊 100÷400＝25%。效率要比較比例，不是只看有用輸出絕對量。", "分別計算輸出／輸入，再比較百分比而非只比較輸出數字。", ["寫出兩塊的效率公式。", "計算第一塊 180÷1000＝0.18。", "計算第二塊 100÷400＝0.25。", "換成百分比並比較 18% 與 25%。", "第二塊效率較高，所以選 A。"], "hard"),
    make(9, "比較火力、風力與水力方案時，哪一種評估最完整？", {"A": "同時考慮能量來源、供應穩定度、轉換效率、建置條件、排放與生態影響", "B": "只要是再生能源就一定比其他方案適合", "C": "只看發電量，不需要考慮環境與地點", "D": "只用宣傳標語判斷哪種能源最乾淨"}, "能源決策是多條件問題；再生性重要，但供應、轉換、地點、環境與社會成本也會影響適用性。", "建立多欄比較表，避免把單一標籤當成全部決策。", ["列出各方案的來源與能量轉換路徑。", "比較供應是否受天候、地形或燃料影響。", "加入效率、排放、土地與生態資料。", "根據實際需求與條件說明取捨。", "所以選 A。"], "hard"),
    make(10, "能源方案報告的結論哪一項最符合科學表達？", {"A": "在目前的日照、負載與儲能條件下，方案甲有效率優勢，但仍需長期資料評估成本與供電穩定度", "B": "方案甲永遠是所有地區最好的能源", "C": "只要一次測得輸出，就能證明沒有轉換損失", "D": "再生能源不需任何維護或備援"}, "好的能源結論要把數據、適用條件與未解問題一起寫出，避免把單次測試推廣成無條件定律。", "使用『證據—條件—限制—後續資料』四段檢查結論。", ["列出方案甲實際測得的輸入與輸出資料。", "寫出結論適用的日照、負載和儲能條件。", "補上成本、維護與穩定度尚未確認的部分。", "提出需要長期或不同情境測試的後續工作。", "所以選 A。"], "medium"),
]

for index, target in {2: "B", 4: "C", 6: "D", 8: "B", 10: "C"}.items():
    q = Q[index - 1]
    option_map = {o["id"]: o["text"] for o in q["options"]}
    option_map["A"], option_map[target] = option_map[target], option_map["A"]
    q["options"] = [{"id": k, "text": option_map[k]} for k in ("A", "B", "C", "D")]
    q["answer"]["value"] = target
    q["answer"]["explanation"] = q["answer"]["explanation"].replace("選 A。", f"選 {target}。")
    q["solutionSteps"] = [s.replace("所以選 A。", f"所以選 {target}。") for s in q["solutionSteps"]]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

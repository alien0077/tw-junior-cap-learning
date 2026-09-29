import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-bb-iv-2"
KG = "kg-science-content-bb-iv-2"
SOURCES = [
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/106-1-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96.pdf", "title": "高雄市立國昌國民中學106學年度第一學期二年級自然科第三次段考", "year": "106"},
    {"url": "https://www.dwm.kh.edu.tw/upload/344/104_64183/109-1-3%E8%87%AA%E7%84%B6%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "title": "高雄市立大灣國民中學109學年度第一學期二年級自然科第三次段考", "year": "109"},
    {"url": "https://www.cajh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=70&cfsn=358&fn=112-1-3-8%E8%87%AA%E7%84%B6.pdf&op=dlfile", "title": "花蓮縣立吉安國民中學112學年度上學期八年級自然科第三次段考", "year": "112"},
]


def refs():
    return [{**s, "subject": "science", "locator": "卡與焦耳、Q＝mcΔT、比熱、質量／溫差比較、放熱負號與相變熱量", "observedPattern": "公開自然科評量常以熱量單位、比熱表格、加熱與冷卻資料及公式變形判斷能量大小；本題只取能力方向、資料型態與推理層次。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-bb-iv-2-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然科資料僅供熱量單位、比熱與公式判讀方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開自然科資料的熱量單位能力方向獨立改寫；題幹、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "在國中常用的熱量定義中，1 cal 約表示什麼？", {"A": "1 g 水升高 1℃ 所吸收的熱量", "B": "1 kg 水升高 1℃ 所吸收的熱量", "C": "1 g 任意物質升高 1℃ 的熱量", "D": "1 g 水沸騰所需的全部熱量"}, "A", "卡的傳統定義以 1 g 水升高 1℃ 所需熱量為基準，選 A。", "抓住定義中的物質、質量與溫度變化三項限制。", ["找出定義指定的物質是水。", "確認質量是 1 g。", "確認溫度上升 1℃。", "這三項合在一起對應約 1 cal。", "所以選 A。"], "easy"),
    make(2, "若取 1 cal≈4.2 J，50 cal 約等於多少焦耳？", {"A": "12 J", "B": "21 J", "C": "210 J", "D": "420 J"}, "C", "把 50 cal 乘以每卡約 4.2 J：50×4.2＝210 J，選 C。", "先確認換算方向，再做數值乘法並保留單位。", ["寫出 1 cal≈4.2 J。", "題目給 50 cal。", "計算 50×4.2。", "得到 210。", "單位換成 J，所以選 C。"], "easy"),
    make(3, "水的比熱取 1 cal/(g·℃)，100 g 水升高 5℃需吸收多少熱量？", {"A": "20 cal", "B": "100 cal", "C": "500 cal", "D": "5000 cal"}, "C", "Q＝mcΔT＝100×1×5＝500 cal，選 C。", "先把 m、c、ΔT 對應到公式，再逐項代入。", ["確認 m＝100 g。", "確認 c＝1 cal/(g·℃)。", "確認 ΔT＝5℃。", "計算 Q＝100×1×5＝500 cal。", "所以選 C。"], "easy"),
    make(4, "兩種物質質量相同、吸收熱量也相同；甲的溫度上升比乙小，表示甲的比熱如何？", {"A": "甲的比熱較大", "B": "甲的比熱較小", "C": "兩者比熱一定相同", "D": "只由甲的密度決定"}, "A", "由 Q＝mcΔT，在 Q 與 m 固定時，溫升較小代表每升高 1℃需較多熱量，即比熱較大，選 A。", "固定已知量後，看公式中比熱與溫度變化的反比關係。", ["確認兩物 Q 相同。", "確認兩物 m 相同。", "甲的 ΔT 較小。", "要吸收相同 Q，甲需較大的 c。", "所以選 A。"], "medium"),
    make(5, "兩杯水質量與初溫相同，比熱也相同；甲升高 10℃、乙升高 20℃。兩杯吸收熱量的關係為何？", {"A": "乙是甲的 2 倍", "B": "甲是乙的 2 倍", "C": "兩者相同", "D": "無法比較，因為不知道水的密度"}, "A", "Q＝mcΔT，m 與 c 相同時熱量與溫差成正比；乙的溫升兩倍，吸熱也兩倍，選 A。", "先找出相同因子，再比較 ΔT 的倍數。", ["列出兩杯的 Q＝mcΔT。", "m 與 c 在兩杯相同。", "甲 ΔT＝10℃、乙 ΔT＝20℃。", "乙的溫差是甲的 2 倍。", "所以乙吸熱是甲的 2 倍，選 A。"], "medium"),
    make(6, "水的比熱為 1 cal/(g·℃)，一杯水吸收 300 cal 後升高 3℃，這杯水的質量是多少？", {"A": "30 g", "B": "90 g", "C": "100 g", "D": "900 g"}, "C", "由 Q＝mcΔT 得 m＝Q/(cΔT)＝300/(1×3)＝100 g，選 C。", "未知量是質量時，先把公式整理成 m＝Q/(cΔT)。", ["寫出 Q＝mcΔT。", "移項得到 m＝Q/(cΔT)。", "代入 Q＝300、c＝1、ΔT＝3。", "計算 300÷3＝100 g。", "所以選 C。"], "medium"),
    make(7, "下列哪一組單位可同時表示熱量或能量？", {"A": "焦耳與卡", "B": "瓦特與秒", "C": "牛頓與公尺／秒", "D": "攝氏度與克"}, "A", "焦耳是 SI 能量單位，卡也是熱量常用單位；瓦特是功率，℃是溫度，選 A。", "逐一辨認物理量與單位，不把功率單位當成能量單位。", ["確認熱量屬於能量。", "焦耳是能量的 SI 單位。", "卡是熱量常用單位。", "瓦特表示每秒能量變化，屬功率。", "所以選 A。"], "easy"),
    make(8, "兩物質質量與材料不同，僅知道它們的溫度都上升 10℃，能否判斷誰吸收熱量較多？", {"A": "不能，還要知道質量與比熱，並比較 Q＝mcΔT", "B": "可以，溫升較大者一定吸熱較多", "C": "可以，溫度相同就表示吸熱相同", "D": "不能，因為熱量無法測量"}, "A", "吸收熱量由 Q＝mcΔT 決定；若質量與比熱不同，僅憑相同溫升不能比較 Q，選 A。", "先檢查公式中的所有變數是否已知，再判斷證據是否足夠。", ["寫出 Q＝mcΔT。", "題目只給兩物相同的 ΔT。", "m 與 c 都可能不同。", "因此 Q 仍可能不同。", "必須取得質量與比熱資料才能比較，選 A。"], "medium"),
    make(9, "某物體放出 80 J 熱量使周圍升溫；若只把該物體視為系統，它的熱量變化應如何記錄？", {"A": "＋80 J", "B": "−80 J", "C": "0 J", "D": "無法使用正負號表示"}, "B", "系統放出能量，對系統而言熱量變化記為負值，因此 ΔQ＝−80 J，選 B。", "先固定研究系統，再用『吸收正、放出負』判定符號。", ["指定研究對象是放熱的物體。", "物體的能量流向周圍。", "系統失去 80 J。", "以系統觀點記為 ΔQ＝−80 J。", "所以選 B。"], "easy"),
    make(10, "使用 Q＝mcΔT 計算顯熱時，ΔT 應代表什麼？", {"A": "末溫減初溫的溫度變化量", "B": "物體的絕對溫度總和", "C": "加熱時間的長短", "D": "物體的質量變化量"}, "A", "公式中的 ΔT 是溫度變化量，通常寫成 T末−T初；升溫為正，降溫為負，選 A。", "先辨認三角符號代表差值，再核對正負號與情境。", ["確認 Δ 表示變化量。", "寫出 ΔT＝T末−T初。", "升溫時末溫較高，ΔT為正。", "冷卻時末溫較低，ΔT為負。", "所以選 A。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

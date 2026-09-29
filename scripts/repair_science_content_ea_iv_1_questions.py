import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-ea-iv-1"
KG = "kg-science-content-ea-iv-1"
SOURCES = [
    {"url": "https://www3.schs.ntpc.edu.tw/var/file/0/1000/attach/62/pta_6928_7943048_11362.pdf", "title": "新北市立石碇高中國中部自然科題庫", "year": "113", "locator": "基本物理量、估讀、量筒與密度題型"},
    {"url": "https://www.nhjh.tp.edu.tw/uploads/1675416611640UMJ54uWL.pdf", "title": "臺北市立內湖國中111學年度上學期自然科學第一次段考", "year": "111", "locator": "測量單位、直尺估讀與最小刻度題組"},
    {"url": "https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E5%85%AB%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "title": "國立中科實驗高級中學國中自然科補行評量題庫", "year": "2026", "locator": "國際單位、排水法、密度與測量精度題型"},
]


def refs():
    return [{**s, "subject": "science", "observedPattern": "公立學校公開自然題常以單位辨識、直尺／量筒讀值、排水法、質量體積密度或基本與衍生量分類要求計算與判讀；本題只改寫能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-ea-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校公開自然題資料僅作物理量、單位、測量與計算的能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與公立學校公開試題能力方向獨立改寫，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-12", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "下列哪一項是『物理量』的完整表示？", {"A": "12", "B": "12 公尺", "C": "公尺", "D": "很長"}, "B", "物理量必須說明數值與單位；只有 12 不知道描述長度、時間或其他量，只有公尺也沒有大小。", "先檢查答案是否同時具有數值、單位和可辨認的物理意義。", ["找出每個選項是否含有數值。", "再檢查是否有適當單位。", "確認數值和單位合在一起能描述一個量。", "排除只有數字、單位或形容詞的選項。", "所以選 B。"], "easy"),
make(2, "跑步 60 m 用時 12 s，平均速率是多少？", {"A": "5 m/s", "B": "48 m/s", "C": "72 m/s", "D": "0.2 m/s"}, "A", "速率＝路程÷時間＝60 m÷12 s＝5 m/s；m/s 也符合距離除以時間的單位。", "先寫定義式，再代入數值並同步檢查單位。", ["寫出速率＝路程÷時間。", "代入 60 m 和 12 s。", "計算 60÷12＝5。", "保留單位 m/s。", "因此答案是 A。"], "easy"),
make(3, "下列哪個物理量主要由其他量依關係式計算得到，屬於衍生物理量？", {"A": "時間", "B": "溫度", "C": "密度", "D": "長度"}, "C", "密度可由質量除以體積得到，定義來自其他量的組合，因此是衍生物理量；其他選項可直接以適當工具量測。", "不要以單位長短分類，要看該量的定義是否由其他物理量組合而成。", ["逐項確認物理量的定義。", "找出需要質量與體積計算的量。", "套用密度＝質量÷體積。", "排除可直接讀取的時間、溫度和長度。", "故選 C。"], "medium"),
make(4, "某物質質量 240 g、體積 100 mL，密度是多少？", {"A": "0.42 g/mL", "B": "2.4 g/mL", "C": "24 g/mL", "D": "340 g/mL"}, "B", "密度＝質量÷體積＝240 g÷100 mL＝2.4 g/mL。", "先確認分子是質量、分母是體積，再檢查數量級與單位。", ["寫出密度公式。", "把 240 g 放在分子、100 mL 放在分母。", "計算 240÷100＝2.4。", "保留 g/mL 單位。", "所以選 B。"], "medium"),
make(5, "若一物體的質量加倍但材料與密度不變，體積會如何變化？", {"A": "加倍", "B": "減半", "C": "不變", "D": "變成零"}, "A", "由密度＝質量÷體積且密度固定，可得體積＝質量÷密度；質量加倍時體積也加倍。", "把已知的固定條件代入關係式，不只憑直覺比較數字。", ["寫出 V＝m÷ρ。", "確認密度 ρ 固定。", "將質量 m 增為原來兩倍。", "因此體積 V 也乘以兩倍。", "故選 A。"], "medium"),
make(6, "下列哪個單位最適合表示校園操場的長度？", {"A": "m", "B": "mg", "C": "s", "D": "mL"}, "A", "操場長度是長度物理量，公尺 m 的尺度適合校園空間；mg 是質量、s 是時間、mL 是體積。", "先判斷題目描述的物理量，再選對應且尺度合理的單位。", ["辨認操場描述的是距離或長度。", "列出長度常用單位。", "比較公尺與題目尺度是否合適。", "排除質量、時間和體積單位。", "所以選 A。"], "easy"),
make(7, "以排水法測量石塊體積時，量筒水面由 35.0 mL 升至 48.0 mL，石塊體積是多少？", {"A": "13.0 cm³", "B": "83.0 cm³", "C": "35.0 cm³", "D": "48.0 cm³"}, "A", "石塊排開的體積是 48.0−35.0＝13.0 mL；1 mL＝1 cm³，所以為 13.0 cm³。", "排水法取放入前後液面差，並在最後檢查 mL 與 cm³ 的等值關係。", ["記下放入前液面 35.0 mL。", "記下放入後液面 48.0 mL。", "用後者減前者得到 13.0 mL。", "換寫成 13.0 cm³。", "因此選 A。"], "medium"),
make(8, "某人說『速度是 5』，這筆紀錄最主要缺少什麼？", {"A": "數字", "B": "單位與計算來源", "C": "物體顏色", "D": "測量者姓名"}, "B", "5 可能是任何物理量的數值；速度紀錄至少要有單位，並應能追溯距離除以時間的來源，例如 5 m/s。", "檢查紀錄是否能讓他人辨識量的種類、單位與數值來源。", ["確認 5 本身不能辨認物理量。", "找出速度應使用距離／時間單位。", "補上 m/s 等適當單位。", "再追問距離和時間是否有記錄。", "所以缺少的是 B。"], "medium"),
make(9, "一把直尺最小刻度為 1 mm，測得鉛筆長度 12.4 cm。下列哪項判讀合理？", {"A": "最後一位可作合理估讀，但不應寫成 12.4000 cm", "B": "最小刻度 1 mm 所以只能寫 12 cm", "C": "可以直接寫到 12.40000 cm 且更精確", "D": "直尺不能測量任何長度"}, "A", "最小刻度限制可報告的精度，通常可在刻度間估讀一位；多寫位數不會增加儀器真正提供的資訊。", "先確認最小刻度，再決定可記錄的估讀位數與有效精度。", ["把 1 mm 換成 0.1 cm。", "確認刻度間可合理估讀一位。", "接受 12.4 cm 這種精度相符的紀錄。", "排除只寫整數或虛增多位小數。", "故選 A。"], "hard"),
make(10, "要把 0.24 m³ 的雨水量換成公升，結果是多少？", {"A": "2.4 L", "B": "24 L", "C": "240 L", "D": "2400 L"}, "C", "1 m³＝1000 L，因此 0.24 m³＝0.24×1000＝240 L。", "先寫單位換算關係，再乘上換算倍數並檢查數量級。", ["寫出 1 m³＝1000 L。", "將 0.24 m³ 乘以 1000。", "得到 240 L。", "檢查立方公尺換成公升後數值應變大。", "所以答案是 C。"], "medium"),
]

for index, target in {2: "B", 4: "C", 6: "D", 8: "B", 10: "C"}.items():
    q = Q[index - 1]
    m = {o["id"]: o["text"] for o in q["options"]}
    m["A"], m[target] = m[target], m["A"]
    q["options"] = [{"id": k, "text": m[k]} for k in ("A", "B", "C", "D")]
    q["answer"]["value"] = target
    q["solutionSteps"] = [s.replace("選 A", f"選 {target}").replace("為 A", f"為 {target}") for s in q["solutionSteps"]]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

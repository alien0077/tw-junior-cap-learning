import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-4"
KG = "kg-math-content-a-7-4"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "二元一次聯立方程式的辨識、代入與消去、情境建模、整數條件與直線交點", "observedPattern": "公立學校公開數學試題常以兩個未知數的條件建立方程組，透過代入或消去求解，並連結有序數對與兩直線交點；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-7-4-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供二元一次聯立方程式能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的聯立方程式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "下列哪一組是二元一次聯立方程式？", {"A": "x＋y＝7 且 2x−y＝1", "B": "x²＋y＝5 且 x＋y＝3", "C": "xy＝6 且 x−y＝2", "D": "x＋y＋z＝8 且 x−y＝1"}, "A", "A 含兩個未知數 x、y，兩式的未知數次數都為一次，符合二元一次聯立方程式，選 A。", "逐式檢查未知數種類與最高次數，不能只看到兩個等號就判定。", ["查看每個選項的未知數種類。", "確認 A 只有 x、y 兩個未知數。", "檢查每一項的次數都不超過一次。", "確認兩式以聯立方式同時成立。", "選 A。"], "easy"),
    make(2, "若 x＋y＝13 且 x−y＝1，則 (x，y) 為何？", {"A": "(5，8)", "B": "(6，7)", "C": "(7，6)", "D": "(8，5)"}, "C", "兩式相加得 2x＝14，所以 x＝7；代回 x＋y＝13 得 y＝6，選 C。", "先相加消去 y，再回代求另一個未知數，最後檢核兩式。", ["將 x＋y＝13 與 x−y＝1 相加。", "得到 2x＝14，解得 x＝7。", "代入 x＋y＝13 得 7＋y＝13。", "解得 y＝6。", "代回第二式 7−6＝1，選 C。"], "medium"),
    make(3, "在聯立方程式 x＋2y＝11、x＝y＋2 中，(x，y) 為何？", {"A": "(3，4)", "B": "(4，3)", "C": "(5，3)", "D": "(6，2)"}, "C", "將 x＝y＋2 代入第一式：y＋2＋2y＝11，得 y＝3，再得 x＝5，選 C。", "利用已經解出一個未知數的方程式作代入，減少兩個未知數同時運算。", ["取 x＝y＋2 作為代入式。", "代入 x＋2y＝11 得 y＋2＋2y＝11。", "合併得 3y＝9，故 y＝3。", "計算 x＝3＋2＝5。", "代回第一式 5＋6＝11，選 C。"], "medium"),
    make(4, "若 3a＋b＝17 且 a＋b＝9，則 a 為何？", {"A": "3", "B": "4", "C": "5", "D": "6"}, "B", "第一式減第二式得 2a＝8，因此 a＝4，選 B。", "兩式的 b 係數相同，直接相減可快速消去 b。", ["列出 3a＋b＝17。", "列出 a＋b＝9。", "用第一式減第二式消去 b。", "得到 2a＝8，解得 a＝4。", "代回 a＋b＝9 可找到 b＝5，選 B。"], "easy"),
    make(5, "某班買成人票 x 張、學生票 y 張，共 20 張；成人票 45 元、學生票 30 元，共付 780 元。哪組聯立方程式正確？", {"A": "x＋y＝20；45x＋30y＝780", "B": "x＋y＝780；45x＋30y＝20", "C": "45x＋30y＝20；x−y＝780", "D": "x＋y＝20；30x＋45y＝780"}, "A", "張數總和給 x＋y＝20，金額總和給 45x＋30y＝780，選 A。", "分別把『數量條件』與『金額條件』翻成一條方程式，再核對票種係數。", ["用 x、y 表示成人票與學生票張數。", "全班共 20 張得 x＋y＝20。", "成人金額為 45x，學生金額為 30y。", "總金額得 45x＋30y＝780。", "選 A。"], "medium"),
    make(6, "候選解為 (x，y)＝(2，4)，下列哪組方程式可由代入檢查確認成立？", {"A": "3x＋y＝10 且 x−y＝−2", "B": "3x＋y＝9 且 x−y＝−2", "C": "2x＋y＝10 且 x＋y＝6", "D": "x＋2y＝12 且 x−y＝2"}, "A", "代入 (2,4)：3×2＋4＝10 且 2−4＝−2，兩式皆成立，選 A。", "把有序數對中的第一個數代入 x、第二個數代入 y，逐式檢查。", ["取 x＝2、y＝4。", "檢查 A 第一式得 6＋4＝10。", "檢查 A 第二式得 2−4＝−2。", "兩式左右皆相等。", "選 A。"], "easy"),
    make(7, "若 x＋y＝18、2x＋y＝25，則 x 與 y 的值為何？", {"A": "(x，y)＝(5，13)", "B": "(x，y)＝(7，11)", "C": "(x，y)＝(9，9)", "D": "(x，y)＝(11，7)"}, "B", "第二式減第一式得 x＝7，再代入 x＋y＝18 得 y＝11，選 B。", "利用兩式 y 係數相同相減，再回代處理剩下未知數。", ["寫出 2x＋y＝25。", "減去 x＋y＝18 以消去 y。", "得到 x＝7。", "代回第一式得 7＋y＝18，y＝11。", "代回第二式驗證 14＋11＝25，選 B。"], "easy"),
    make(8, "下列哪個有序數對同時滿足 2x＋y＝8 與 x＋y＝5？", {"A": "(1，4)", "B": "(2，3)", "C": "(3，2)", "D": "(4，1)"}, "C", "兩式相減得 x＝3，再由 x＋y＝5 得 y＝2，所以有序數對為 (3,2)，選 C。", "先用兩式相減消去 y，再依有序數對順序寫成 (x,y)。", ["用 2x＋y＝8 減 x＋y＝5。", "得到 x＝3。", "代入 x＋y＝5 得 3＋y＝5。", "解得 y＝2。", "依序寫成 (3，2)，選 C。"], "medium"),
    make(9, "兩個連續整數的和為 41。若較小者為 x、較大者為 y，哪組條件正確？", {"A": "x＋y＝41 且 y＝x＋1", "B": "x−y＝41 且 y＝x＋1", "C": "x＋y＝41 且 y＝x＋2", "D": "xy＝41 且 y＝x＋1"}, "A", "兩數和為 41 給 x＋y＝41；連續整數相差 1，較大者 y＝x＋1，選 A。", "先把語句分成總和條件與連續條件，再分別寫成方程式。", ["較小者設為 x，較大者設為 y。", "總和條件寫成 x＋y＝41。", "連續且 y 較大表示 y＝x＋1。", "兩條件需同時成立。", "選 A。"], "easy"),
    make(10, "直線 2x＋y＝8 與直線 x−y＝1 的交點代表什麼？", {"A": "只滿足第一式的點", "B": "只滿足第二式的點", "C": "同時滿足兩式的有序數對", "D": "兩直線上所有點的集合"}, "C", "兩直線交點同時位於兩線上，因此其坐標同時滿足兩個方程式，選 C。", "把幾何交點與代數聯立解連結：交點坐標就是共同解。", ["辨認第一條直線上的點滿足第一式。", "辨認第二條直線上的點滿足第二式。", "交點同時在兩條直線上。", "所以其坐標同時滿足兩個方程式。", "選 C。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

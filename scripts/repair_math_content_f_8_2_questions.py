import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-f-8-2"
KG = "kg-math-content-f-8-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "graphs of linear functions, slope, intercepts, parallel lines, intersections, and point verification", "observedPattern": "公立學校公開數學試題常由一次函數圖形讀取斜率與截距、判斷點在線上、求坐標軸截距及比較平行或交會；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-f-8-2-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一次函數圖形、斜率、截距、平行與交會能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的一次函數圖形方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "直線 y＝2x−5 的斜率為何？", {"A": "−5", "B": "−2", "C": "2", "D": "5"}, "C", "一次函數 y＝ax＋b 的斜率是 x 的係數 a；此式 a＝2，所以選 C。", "先把式子辨認成 y＝ax＋b，再直接讀取 x 的係數，不把截距當成斜率。", ["寫出一般式 y＝ax＋b。", "比較 y＝2x−5 與一般式，找出 x 的係數。", "確認斜率 a＝2。", "辨認 −5 是 y 軸截距而非斜率。", "選 C，將 x 增加 1 時 y 增加 2 作圖形意義驗證。"], "easy"),
    make(2, "直線 y＝−3x＋4 與 y 軸交於哪一點？", {"A": "(−3,0)", "B": "(0,4)", "C": "(4,0)", "D": "(0,−3)"}, "B", "與 y 軸相交時 x＝0，代入得 y＝4，因此交點為 (0,4)，選 B。", "求 y 軸截距要令 x＝0，再將所得 y 值寫成有序對。", ["知道 y 軸上的點都滿足 x＝0。", "代入 y＝−3x＋4，得到 y＝4。", "組成坐標 (0,4)。", "區分 (0,4) 與 (4,0) 的軸向位置。", "選 B，代回直線方程式確認 −3×0＋4＝4。"], "easy"),
    make(3, "點 (3,2) 是否在直線 y＝−x＋5 上？", {"A": "在，因為 −3＋5＝2", "B": "在，因為 3＋5＝8", "C": "不在，因為 −3＋5＝2", "D": "不在，因為 3−5＝−2"}, "A", "將 x＝3 代入右式得 −3＋5＝2，恰好等於點的 y 值，所以在直線上，選 A。", "驗證點在線上只需代入 x，檢查算出的 y 是否等於坐標中的 y。", ["取點的 x 坐標 3。", "代入右式 y＝−3＋5。", "計算得到 y＝2。", "與點的 y 坐標 2 比較，兩者相同。", "選 A，確認不是只比較 x 或忽略負號。"], "medium"),
    make(4, "直線 y＝2x−6 與 x 軸的交點坐標為何？", {"A": "(0,−6)", "B": "(3,0)", "C": "(−3,0)", "D": "(0,3)"}, "B", "x 軸上的 y＝0；令 0＝2x−6，得 x＝3，所以交點為 (3,0)，選 B。", "求 x 軸截距要令 y＝0，解出 x 後以 (x,0) 表示。", ["知道 x 軸上的點滿足 y＝0。", "代入得 0＝2x−6。", "兩邊同加 6，得 2x＝6。", "除以 2 得 x＝3，寫成 (3,0)。", "選 B，將坐標代回原式得到 0。"], "medium"),
    make(5, "下列哪兩條直線互相平行？", {"A": "y＝2x＋1 與 y＝−2x＋4", "B": "y＝3x−2 與 y＝3x＋5", "C": "y＝x＋2 與 y＝2x＋2", "D": "y＝−x＋1 與 y＝x−1"}, "B", "不重合的直線斜率相同即平行；B 的兩條斜率都是 3，而截距不同，所以平行。", "先比較 x 係數判斷斜率，再確認截距不同以排除同一直線。", ["讀取 A 的斜率 2 與 −2，不同。", "讀取 B 的斜率皆為 3，且截距 −2、5 不同。", "檢查 C 斜率 1、2，不同。", "檢查 D 斜率 −1、1，不同。", "選 B，因為斜率相同且兩線不重合。"], "medium"),
    make(6, "直線通過兩點 (1,4) 與 (5,12)，其斜率是多少？", {"A": "1", "B": "2", "C": "4", "D": "8"}, "B", "斜率＝(12−4)÷(5−1)＝8÷4＝2，所以選 B。", "用縱坐標差除以橫坐標差，並維持同一順序避免分子分母錯配。", ["取兩點的 y 差 12−4＝8。", "取兩點的 x 差 5−1＝4。", "建立斜率 8÷4。", "計算得到 2。", "選 B，反向計算 (4−12)÷(1−5) 也得到 2。"], "easy"),
    make(7, "直線 y＝−x＋6 與 y＝x 的交點坐標為何？", {"A": "(2,2)", "B": "(3,3)", "C": "(4,4)", "D": "(6,0)"}, "B", "交點同時滿足兩式，令 −x＋6＝x，得 2x＝6、x＝3，再由 y＝x 得 y＝3，選 B。", "交點要同時符合兩個規則，先令兩個 y 表達式相等，再回代求另一坐標。", ["令兩直線的 y 值相等：−x＋6＝x。", "移項得 6＝2x。", "解出 x＝3。", "代入 y＝x 得 y＝3。", "選 B，代回兩式都得到 3。"], "hard"),
    make(8, "若直線 y＝4x＋b 通過點 (2,11)，b 為何？", {"A": "−3", "B": "1", "C": "3", "D": "19"}, "C", "將點代入 11＝4×2＋b，得 11＝8＋b，所以 b＝3，選 C。", "已知斜率與線上點時，把點的坐標代入求未知截距。", ["把 x＝2、y＝11 代入 y＝4x＋b。", "得到 11＝8＋b。", "兩邊同減 8。", "解出 b＝3。", "選 C，寫回 y＝4x＋3 並驗證點 (2,11)。"], "medium"),
    make(9, "直線 y＝−2x＋8 在 x 增加時，圖形呈現何種方向？", {"A": "由左下向右上", "B": "由左上向右下", "C": "水平直線", "D": "垂直直線"}, "B", "斜率 −2 為負，x 向右增加時 y 下降，所以圖形由左上向右下，選 B。", "用斜率正負判斷圖形由左至右的升降，不需要先畫出所有點。", ["讀取直線斜率 −2。", "判斷負斜率表示 x 增加、y 減少。", "在坐標平面中由左往右觀察。", "因此直線從左上往右下。", "選 B，取 x＝0、1 可得 y＝8、6 作局部驗證。"], "easy"),
    make(10, "一條直線斜率為 3 且通過點 (−1,2)，其方程式為何？", {"A": "y＝3x−1", "B": "y＝3x＋5", "C": "y＝−3x−1", "D": "y＝−3x＋5"}, "B", "設 y＝3x＋b，代入 (−1,2) 得 2＝−3＋b，所以 b＝5，方程式為 y＝3x＋5，選 B。", "先用斜率寫出部分形式，再代入已知點求截距，最後回代驗證。", ["由斜率 3 寫成 y＝3x＋b。", "代入 x＝−1、y＝2，得 2＝3(−1)＋b。", "化簡為 2＝−3＋b。", "解出 b＝5，得到 y＝3x＋5。", "選 B，代入 x＝−1 確認 y＝2。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

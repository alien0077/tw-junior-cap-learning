import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-s-iv-12"
KG = "kg-math-performance-s-iv-12"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "特殊角三角比、sin／cos／tan 定義、直角三角形邊長比、仰角測高與三角比互補關係", "observedPattern": "公開數學評量常由特殊角或直角三角形的對邊、鄰邊、斜邊建立三角比，並延伸到仰角與未知邊長；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-s-iv-12-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供特殊角、三角比與測量應用能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的三角比方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "sin 30° 的值是多少？", {"A": "1/2", "B": "√2/2", "C": "√3/2", "D": "1"}, "A", "30°-60°-90° 三角形的短股與斜邊比為 1:2，因此 sin30°=1/2，選 A。", "先回想特殊角 30° 的對邊／斜邊固定比例。", ["sin 定義為對邊÷斜邊。", "30° 特殊三角形對邊與斜邊比為 1:2。", "因此 sin30°=1÷2。", "寫成分數 1/2。", "所以選 A。"], "easy"),
    make(2, "cos 60° 的值是多少？", {"A": "1/2", "B": "√2/2", "C": "√3/2", "D": "1"}, "A", "60° 的鄰邊與斜邊比為 1:2，因此 cos60°=1/2，選 A。", "用 30°-60°-90° 邊比辨識 60° 的鄰邊。", ["cos 定義為鄰邊÷斜邊。", "60° 對應的鄰邊是短股。", "短股：斜邊=1:2。", "所以 cos60°=1/2。", "選 A。"], "easy"),
    make(3, "tan 45° 的值是多少？", {"A": "0", "B": "1/2", "C": "1", "D": "√3"}, "C", "45°-45°-90° 三角形兩股等長，tan45°=對邊÷鄰邊=1，選 C。", "45° 的兩股相等，正切就是相等長度的比。", ["tan 定義為對邊÷鄰邊。", "45°-45°-90° 中兩股等長。", "等長邊相除得 1。", "因此 tan45°=1。", "所以選 C。"], "easy"),
    make(4, "直角三角形中，某銳角 θ 的對邊長 8 公分、斜邊長 17 公分，sin θ 為何？", {"A": "8/17", "B": "15/17", "C": "8/15", "D": "17/8"}, "A", "sinθ=對邊/斜邊=8/17，選 A。", "先確認題目給的是對邊與斜邊，直接套 sin 定義。", ["辨認相對於 θ 的對邊為 8。", "斜邊為 17。", "套用 sinθ=對邊÷斜邊。", "計算得 8/17。", "所以選 A。"], "easy"),
    make(5, "直角三角形中，某銳角 θ 的鄰邊長 15 公分、斜邊長 17 公分，cos θ 為何？", {"A": "8/17", "B": "15/17", "C": "15/8", "D": "17/15"}, "B", "cosθ=鄰邊/斜邊=15/17，選 B。", "題目直接給鄰邊與斜邊，避免先求另一股。", ["辨認相對於 θ 的鄰邊為 15。", "斜邊為 17。", "套用 cosθ=鄰邊÷斜邊。", "得到 15/17。", "所以選 B。"], "easy"),
    make(6, "直角三角形中，某銳角 θ 的對邊長 5 公分、鄰邊長 12 公分，tan θ 為何？", {"A": "5/12", "B": "12/5", "C": "5/13", "D": "12/13"}, "A", "tanθ=對邊/鄰邊=5/12，選 A。", "正切不需要斜邊，只比較對邊與鄰邊。", ["相對於 θ 找出對邊 5。", "找出鄰邊 12。", "套用 tanθ=對邊÷鄰邊。", "得到 5/12。", "所以選 A。"], "easy"),
    make(7, "若直角三角形斜邊長 18 公分，且一銳角為 30°，則 30° 所對的邊長是多少？", {"A": "6 公分", "B": "9 公分", "C": "9√3 公分", "D": "18 公分"}, "B", "30° 所對的邊是斜邊的一半，故邊長=18×1/2=9 公分，選 B。", "利用 30° 特殊三角形的短股：斜邊=2×短股。", ["確認 30° 對邊是短股。", "30° 對邊與斜邊比為 1:2。", "斜邊為 18，短股為 18÷2。", "計算得到 9 公分。", "所以選 B。"], "medium"),
    make(8, "觀察一棵樹的仰角為 30°，觀察點到樹底的水平距離為 10 公尺，忽略眼睛高度，樹高約為多少？", {"A": "5 公尺", "B": "10 公尺", "C": "10√3/3 公尺", "D": "10√3 公尺"}, "C", "tan30°=樹高/10=√3/3，所以樹高=10√3/3 公尺，選 C。", "把仰角情境畫成直角三角形，水平距離是鄰邊、樹高是對邊。", ["建立 tan30°=對邊/鄰邊。", "對邊是樹高 h，鄰邊為 10。", "列式 h/10=√3/3。", "解得 h=10√3/3 公尺。", "所以選 C。"], "hard"),
    make(9, "若銳角 θ 滿足 sin θ=5/13，且 θ 為銳角，則 cos θ 為何？", {"A": "5/13", "B": "12/13", "C": "13/12", "D": "8/13"}, "B", "可視為對邊 5、斜邊 13 的直角三角形，另一股為 12（5-12-13），所以 cosθ=鄰邊/斜邊=12/13，選 B。", "把 sin 的分子分母視為對邊與斜邊，再用畢氏定理求鄰邊。", ["由 sinθ=5/13 取對邊 5、斜邊 13。", "求鄰邊²=13²-5²=169-25=144。", "鄰邊取正根為 12。", "cosθ=12/13。", "所以選 B。"], "medium"),
    make(10, "若銳角 θ 滿足 tan θ=√3，則 θ 為多少？", {"A": "30°", "B": "45°", "C": "60°", "D": "90°"}, "C", "特殊角中 tan60°=√3，且 θ 為銳角，所以 θ=60°，選 C。", "將正切值與 30°、45°、60° 的特殊值表比對。", ["列出特殊正切值：tan30°=√3/3、tan45°=1、tan60°=√3。", "題目給 tanθ=√3。", "對應角為 60°。", "60° 是銳角，符合條件。", "所以選 C。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-s-iv-3"
KG = "kg-math-performance-s-iv-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "平行線與斜率、垂直線斜率、水平與垂直直線、兩點斜率、直線方程式與坐標方向", "observedPattern": "公開數學評量常以直線方程式、兩點或坐標圖形判斷平行與垂直，並要求用斜率或截距寫出直線；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-s-iv-3-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供平行、垂直、斜率、直線方程式與坐標方向能力研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的垂直與平行方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "直線 y=-3x+2 與直線 y=-3x-5 的關係為何？", {"A": "垂直", "B": "平行且不重合", "C": "相交於原點", "D": "重合"}, "B", "兩直線斜率同為 -3，但 y 截距 2、-5 不同，因此平行且不重合，選 B。", "先比較斜率判斷方向，再比較截距排除重合。", ["讀取兩式的斜率都為 -3。", "斜率相同代表方向相同。", "比較截距 2 與 -5，確認不同。", "所以兩線不重合而互相平行。", "因此選 B。"], "easy"),
    make(2, "斜率為 4 的直線，若與另一條直線垂直，另一條直線的斜率是多少？", {"A": "4", "B": "-4", "C": "1/4", "D": "-1/4"}, "D", "非垂直於 y 軸的兩直線垂直時，斜率乘積為 -1；4m=-1，所以 m=-1/4，選 D。", "使用垂直斜率乘積 -1，並保留負號。", ["設另一條斜率為 m。", "垂直條件給 4m=-1。", "兩邊除以 4。", "得到 m=-1/4。", "所以選 D，負倒數是關鍵。"], "medium"),
    make(3, "若直線 L 與 y=(1/3)x-7 平行，則直線 L 的斜率為何？", {"A": "-7", "B": "-1/3", "C": "1/3", "D": "3"}, "C", "平行直線的斜率相等；已知直線 x 的係數為 1/3，所以 L 的斜率也是 1/3，選 C。", "將式子看成 y=mx+b，只取 x 的係數判斷斜率。", ["辨認已知直線形式 y=mx+b。", "讀出 m=1/3。", "平行要求斜率相同。", "因此 L 的斜率為 1/3。", "所以選 C。"], "easy"),
    make(4, "直線 x=-2 與直線 y=5 的關係為何？", {"A": "平行", "B": "垂直", "C": "重合", "D": "無法判斷"}, "B", "x=-2 是垂直線，y=5 是水平線；垂直線與水平線互相垂直，選 B。", "辨認 x 固定與 y 固定的幾何方向，不必硬套一般斜率公式。", ["x=-2 表示所有點的 x 坐標固定。", "因此圖形是垂直線。", "y=5 表示所有點的 y 坐標固定。", "因此圖形是水平線。", "水平線與垂直線互相垂直，選 B。"], "easy"),
    make(5, "兩條水平平行線 y=7 與 y=-1 之間的距離是多少？", {"A": "6", "B": "7", "C": "8", "D": "9"}, "C", "水平線間距等於 y 坐標差的絕對值：|7-(-1)|=8，選 C。", "水平線只比較 y 值，距離一定取非負的絕對值。", ["確認兩線都是水平線。", "讀取 y 值 7 與 -1。", "計算差 7-(-1)=8。", "取絕對值仍為 8。", "所以選 C。"], "easy"),
    make(6, "通過點 (-2,1) 與 (4,10) 的直線斜率是多少？", {"A": "1/2", "B": "3/2", "C": "2", "D": "5/2"}, "B", "斜率=(10-1)/(4-(-2))=9/6=3/2，選 B。", "用 y 差除以 x 差，並將分數約分。", ["計算 y 差 10-1=9。", "計算 x 差 4-(-2)=6。", "套用 m=Δy/Δx=9/6。", "約分得到 3/2。", "所以選 B，並確認分母是 x 坐標差。"], "medium"),
    make(7, "斜率為 -2 且通過 (0,-3) 的直線方程式為何？", {"A": "y=-2x+3", "B": "y=-2x-3", "C": "y=2x-3", "D": "y=2x+3"}, "B", "y=mx+b 中 m=-2；通過 (0,-3) 表示 y 截距 b=-3，所以 y=-2x-3，選 B。", "先把斜率放入 m，再利用 x=0 時的 y 讀出截距。", ["寫成 y=-2x+b。", "代入點 (0,-3)。", "-3=-2×0+b，所以 b=-3。", "得到 y=-2x-3。", "所以選 B。"], "medium"),
    make(8, "若兩條相異直線的斜率分別為 3 與 -1/3，則這兩條直線必定如何？", {"A": "平行", "B": "垂直", "C": "重合", "D": "都有相同 y 截距"}, "B", "斜率乘積 3×(-1/3)=-1，符合垂直條件；且題目說相異，不會是重合，選 B。", "計算斜率乘積並與 -1 比較，先判斷垂直再處理相異條件。", ["取兩條斜率 m1=3、m2=-1/3。", "計算 m1m2=3×(-1/3)=-1。", "乘積為 -1 表示兩線垂直。", "相異條件排除重合。", "所以選 B。"], "medium"),
    make(9, "直線 y=-5x+1 的一條平行線可能是哪一條？", {"A": "y=5x+1", "B": "y=-5x-6", "C": "y=(1/5)x+1", "D": "y=-6x+1"}, "B", "平行線斜率必須相同，只有 y=-5x-6 的斜率為 -5；截距不同所以確實不重合，選 B。", "先看 x 係數，再確認常數項不同。", ["已知直線斜率為 -5。", "逐項尋找斜率 -5 的式子。", "B 的斜率為 -5，截距 -6。", "截距與 1 不同，兩線不重合。", "所以選 B。"], "easy"),
    make(10, "在坐標平面上，線段 AB 的端點為 A(-1,4)、B(-1,-3)，AB 的方向為何？", {"A": "水平向右", "B": "水平向左", "C": "垂直方向", "D": "斜向右上"}, "C", "兩端點 x 坐標都為 -1，表示線段位於同一條垂直線上，因此方向為垂直，選 C。", "比較兩端點哪一個坐標固定；x 固定代表垂直方向。", ["讀取 A、B 的 x 坐標都為 -1。", "x 固定表示線段不左右改變。", "y 從 4 變到 -3，沿上下方向移動。", "因此 AB 是垂直線段。", "所以選 C。"], "easy"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

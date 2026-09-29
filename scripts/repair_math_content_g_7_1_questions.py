import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-g-7-1"
KG = "kg-math-content-g-7-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "Cartesian coordinates, quadrants, axes, reflections, translations, distance, and geometric area", "observedPattern": "公立學校公開數學試題常以坐標平面判讀位置、象限與軸上點，並結合對稱、平移、距離或矩形面積；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-g-7-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供平面直角坐標系、象限、軸上位置、對稱、平移、距離與面積能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的坐標幾何方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "點 P(−4,3) 位於哪一個象限？", {"A": "第一象限", "B": "第二象限", "C": "第三象限", "D": "第四象限"}, "B", "P 的 x 坐標為負、y 坐標為正，符合第二象限，選 B。", "先看 x、y 的正負，再依象限符號規則判斷，不以圖形位置猜測。", ["讀取 P 的 x 坐標 −4，判斷為負。", "讀取 y 坐標 3，判斷為正。", "列出第二象限的符號為 (負，正)。", "比對 P 的符號組合。", "選 B，確認 P 不在坐標軸上。"], "easy"),
    make(2, "點 Q 在 x 軸上且位於原點右方 5 個單位，Q 的坐標為何？", {"A": "(0,5)", "B": "(5,0)", "C": "(−5,0)", "D": "(5,5)"}, "B", "x 軸上的點 y＝0，原點右方 5 單位表示 x＝5，所以 Q＝(5,0)，選 B。", "先用所在軸決定另一坐標為 0，再用方向決定正負。", ["判斷 Q 在 x 軸，因此 y＝0。", "原點右方表示 x 為正。", "距離 5 單位給出 x＝5。", "組成有序對 (5,0)。", "選 B，檢查此點確實落在 x 軸正半部。"], "easy"),
    make(3, "點 A(−2,4) 與 B(3,4) 的水平距離是多少？", {"A": "1", "B": "3", "C": "5", "D": "6"}, "C", "兩點 y 坐標相同，水平距離為 x 坐標差的絕對值 |3−(−2)|＝5，選 C。", "同水平線上的距離只比較 x 坐標，取差值絕對值以確保距離為正。", ["確認 A、B 的 y 坐標都是 4。", "取 x 坐標 3 與 −2。", "計算差值 3−(−2)＝5。", "因為距離不能為負，取絕對值仍為 5。", "選 C，檢查從 −2 向右到 3 共 5 個單位。"], "easy"),
    make(4, "點 R(−3,−1) 對 x 軸反射後的坐標為何？", {"A": "(3,−1)", "B": "(−3,1)", "C": "(3,1)", "D": "(−3,−1)"}, "B", "對 x 軸反射時 x 不變、y 變號，所以 (−3,−1) 變為 (−3,1)，選 B。", "記住 x 軸對稱只改變縱坐標的正負，橫坐標保持不變。", ["寫出原點 R 的坐標 (−3,−1)。", "確認對 x 軸反射，x 坐標保持 −3。", "將 y 坐標 −1 改為 1。", "組成新坐標 (−3,1)。", "選 B，檢查兩點到 x 軸距離相等且位於軸兩側。"], "medium"),
    make(5, "點 S(2,−5) 對 y 軸反射後的坐標為何？", {"A": "(−2,−5)", "B": "(2,5)", "C": "(−2,5)", "D": "(5,2)"}, "A", "對 y 軸反射時 y 不變、x 變號，所以 S 變為 (−2,−5)，選 A。", "y 軸對稱只改變橫坐標的正負，縱坐標保持不變。", ["讀取 S 的坐標 (2,−5)。", "確認對 y 軸反射，y 仍為 −5。", "把 x＝2 改為 x＝−2。", "組成反射點 (−2,−5)。", "選 A，檢查兩點到 y 軸的距離同為 2。"], "medium"),
    make(6, "將點 T(−1,2) 向右平移 4 個單位、向下平移 3 個單位，所得點為何？", {"A": "(3,−1)", "B": "(−5,5)", "C": "(3,5)", "D": "(−5,−1)"}, "A", "向右使 x 加 4，向下使 y 減 3，得到 (−1＋4,2−3)＝(3,−1)，選 A。", "水平平移改變 x、垂直平移改變 y，依方向分別加減位移量。", ["寫出 T 的 x＝−1、y＝2。", "向右 4 單位：x＝−1＋4＝3。", "向下 3 單位：y＝2−3＝−1。", "組成新坐標 (3,−1)。", "選 A，回到原點方向檢查橫向右移、縱向下移。"], "medium"),
    make(7, "矩形四頂點為 (1,1)、(6,1)、(6,4)、(1,4)，此矩形面積是多少？", {"A": "8", "B": "12", "C": "15", "D": "20"}, "C", "水平邊長為 6−1＝5，垂直邊長為 4−1＝3，面積 5×3＝15，選 C。", "先從同水平與同垂直頂點求長寬，再套矩形面積公式。", ["找水平邊兩端 x 坐標 1、6，長為 5。", "找垂直邊兩端 y 坐標 1、4，寬為 3。", "確認四點形成矩形，長寬互相垂直。", "計算面積 5×3＝15。", "選 C，檢查面積單位應為平方單位。"], "medium"),
    make(8, "下列哪一點位於直線 x＝−2 上？", {"A": "(−2,7)", "B": "(7,−2)", "C": "(2,−7)", "D": "(−7,2)"}, "A", "直線 x＝−2 上所有點的 x 坐標固定為 −2，只有 A 符合，選 A。", "判讀垂直線方程式時只檢查 x 坐標，不要把 x、y 順序對調。", ["讀取直線條件 x＝−2。", "檢查 A 的 x 坐標為 −2。", "檢查 B、C、D 的 x 坐標分別為 7、2、−7。", "判斷只有 A 滿足固定橫坐標。", "選 A，確認 y 值可以是 7 並不影響在線條件。"], "easy"),
    make(9, "點 U(−4,−2) 與 V(−4,5) 的垂直距離是多少？", {"A": "3", "B": "5", "C": "7", "D": "9"}, "C", "兩點 x 坐標相同，垂直距離為 |5−(−2)|＝7，選 C。", "同垂直線上的距離只比較 y 坐標，取絕對值計算單位差。", ["確認兩點 x 都是 −4，表示在同一垂直線。", "取 y 坐標 5 與 −2。", "計算 5−(−2)＝7。", "距離取正值，仍為 7。", "選 C，檢查從 −2 向上到 5 共有 7 個單位。"], "easy"),
    make(10, "點 W(a,−3) 位於第三象限，a 應符合哪項條件？", {"A": "a＞0", "B": "a＜0", "C": "a＝0", "D": "a＝−3"}, "B", "第三象限的 x、y 都為負；W 的 y 已為 −3，因此 a 必須小於 0，選 B。", "由象限的符號條件建立未知坐標的不等式，而不是只挑一個數值。", ["列出第三象限的符號：x＜0 且 y＜0。", "觀察 W 的 y＝−3，已符合 y＜0。", "把 x 坐標 a 對應到第三象限條件。", "得到 a＜0。", "選 B，確認 a 不能等於 0，否則點會落在 y 軸上。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-g-8-1"
KG = "kg-math-content-g-8-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "distance between two points, horizontal and vertical differences, Pythagorean distance, and coordinate geometry applications", "observedPattern": "公立學校公開數學試題常以坐標兩點的水平／垂直差、畢氏定理與距離公式處理線段、矩形對角線、圓與幾何情境；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-g-8-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供兩點距離、坐標差、畢氏定理與坐標幾何應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的距離公式方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "點 A(−2,5) 與 B(4,5) 的距離是多少？", {"A": "4", "B": "5", "C": "6", "D": "7"}, "C", "兩點 y 坐標相同，距離為 |4−(−2)|＝6，所以選 C。", "先觀察是否為水平線段；若 y 相同，只需比較 x 坐標差。", ["確認 A、B 的 y 坐標都為 5。", "取 x 坐標 4 與 −2。", "計算 4−(−2)＝6。", "距離取絕對值，仍為 6。", "選 C，檢查從 −2 到 4 的格數為 6。"], "easy"),
    make(2, "點 C(3,−4) 與 D(3,2) 的距離是多少？", {"A": "2", "B": "5", "C": "6", "D": "7"}, "C", "兩點 x 坐標相同，距離為 |2−(−4)|＝6，選 C。", "先辨認垂直線段，再用 y 坐標差的絕對值求長度。", ["確認兩點 x 坐標都是 3。", "取 y 坐標 2 與 −4。", "計算 2−(−4)＝6。", "將結果視為正的距離 6。", "選 C，檢查從 −4 向上到 2 共有 6 單位。"], "easy"),
    make(3, "點 P(1,2) 與 Q(4,6) 的距離是多少？", {"A": "3", "B": "4", "C": "5", "D": "7"}, "C", "水平差 4−1＝3，垂直差 6−2＝4；距離為 √(3²＋4²)＝5，選 C。", "先求兩方向差，再套距離公式或畢氏定理，最後化簡平方根。", ["計算水平差 Δx＝4−1＝3。", "計算垂直差 Δy＝6−2＝4。", "建立距離 √(Δx²＋Δy²)＝√(3²＋4²)。", "計算 √25＝5。", "選 C，確認 3、4、5 直角三角形關係。"], "medium"),
    make(4, "點 R(−3,−2) 與 S(1,1) 的距離是多少？", {"A": "4", "B": "5", "C": "6", "D": "7"}, "B", "水平差 4、垂直差 3，距離 √(4²＋3²)＝5，選 B。", "負坐標相減時先正確計算差值，再用平方消除方向。", ["計算 Δx＝1−(−3)＝4。", "計算 Δy＝1−(−2)＝3。", "代入距離公式 √(4²＋3²)。", "得到 √25＝5。", "選 B，反向取差值也會得到相同距離。"], "medium"),
    make(5, "點 U(2,3) 與 V(8,3) 的中點為 M。線段 UV 的長度是多少？", {"A": "3", "B": "5", "C": "6", "D": "11"}, "C", "兩點在同一水平線，線段長度為 |8−2|＝6；中點資訊不影響長度，選 C。", "題目雖提供中點，仍先抓住兩點距離的必要資訊，避免被無關條件干擾。", ["確認 U、V 的 y 坐標相同。", "使用 x 坐標差 8−2。", "計算線段長度 6。", "檢查中點只描述位置，不改變端點距離。", "選 C，若求中點會得 (5,3)，兩側各 3 單位也能驗證總長 6。"], "easy"),
    make(6, "矩形頂點為 (−1,−2)、(5,−2)、(5,6)、(−1,6)，其對角線長度是多少？", {"A": "8", "B": "10", "C": "12", "D": "14"}, "B", "矩形長 6、寬 8，對角線為 √(6²＋8²)＝√100＝10，選 B。", "先由坐標差找長寬，再把對角線視為直角三角形斜邊。", ["計算水平邊長 5−(−1)＝6。", "計算垂直邊長 6−(−2)＝8。", "用畢氏定理求對角線 √(6²＋8²)。", "計算 √100＝10。", "選 B，檢查對角線必大於 8 且小於 6＋8。"], "hard"),
    make(7, "若點 A(−2,4) 與 B(x,4) 的距離為 9，且 B 在 A 的右方，x 為何？", {"A": "−11", "B": "−7", "C": "7", "D": "11"}, "C", "兩點 y 坐標相同，且 B 在右方，所以 x−(−2)＝9，解得 x＝7，選 C。", "先把水平距離寫成右端 x 減左端坐標，再依條件解未知數。", ["兩點 y 都是 4，確定為水平距離。", "因 B 在 A 右方，建立 x−(−2)＝9。", "化簡 x＋2＝9。", "解得 x＝7。", "選 C，代回 |7−(−2)|＝9。"], "medium"),
    make(8, "圓心 O(2,−1) 的圓半徑為 5，以下哪一點在圓上？", {"A": "(5,3)", "B": "(6,−1)", "C": "(2,5)", "D": "(−2,−5)"}, "A", "A 與圓心的差為 (3,4)，距離 √(3²＋4²)＝5；其餘點距離不等於 5，因此選 A。", "把每個候選點代入圓心距離公式，找到距離恰為半徑者。", ["寫出圓上條件：點到 O(2,−1) 的距離為 5。", "檢查 A：差為 (3,4)，距離 5。", "檢查 B：水平距離 4，不符合。", "其餘點距離也不等於 5，故 A 唯一符合。", "選 A，確認答案選項與半徑條件一致。"], "hard"),
    make(9, "兩點 E(0,0)、F(6,8) 的距離，與哪一個數相等？", {"A": "6＋8", "B": "√(6²＋8²)", "C": "6×8", "D": "8−6"}, "B", "兩點水平差 6、垂直差 8，直線距離為 √(6²＋8²)；不能直接相加，選 B。", "區分曼哈頓式的水平加垂直與直角坐標平面的線段距離，使用畢氏定理。", ["求水平差 6、垂直差 8。", "把兩差視為直角三角形兩股。", "斜邊即兩點直線距離。", "依畢氏定理寫成 √(6²＋8²)。", "選 B，化簡後為 10 也可作數值驗證。"], "medium"),
    make(10, "若點 X(a,2) 與 Y(4,6) 的距離為 5，且 a＜4，a 為何？", {"A": "0", "B": "1", "C": "7", "D": "9"}, "B", "距離式 (4−a)²＋(6−2)²＝25，得 (4−a)²＝9；a＝1 或 7，但 a＜4，取 a＝1，選 B。", "先建立平方距離方程，再列出正負平方根，最後用位置條件篩選。", ["代入距離公式：(4−a)²＋(6−2)²＝5²。", "化簡 (4−a)²＋16＝25，得到 (4−a)²＝9。", "取平方根得 4−a＝3 或 −3，候選 a＝1、7。", "使用 a＜4 排除 7，保留 a＝1。", "選 B，代回距離 √(3²＋4²)＝5。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

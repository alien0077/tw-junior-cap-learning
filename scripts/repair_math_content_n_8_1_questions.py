import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-8-1"
KG = "kg-math-content-n-8-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "square roots, principal roots, positive and negative roots, rational roots, simplification, and geometric applications", "observedPattern": "公立學校公開數學試題常要求辨認平方根與主平方根、解平方方程式、計算分數或小數的根，並將根號連結到邊長與面積；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-8-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供平方根、主平方根、正負根、分數小數與幾何應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的平方根方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "√49 的值是多少？", {"A": "−7", "B": "−49", "C": "7", "D": "49"}, "C", "√49 表示 49 的主平方根，取非負值 7，所以選 C。", "先確認根號符號代表主平方根，再找平方後等於被開方數的非負數。", ["找出平方後等於 49 的數：7²＝49。", "注意 −7 的平方也為 49，但不是主平方根。", "依主平方根定義取非負值 7。", "排除把被開方數 49 直接當答案。", "選 C，計算 7² 回驗。"], "easy"),
    make(2, "方程式 x²＝81 的所有實數解為何？", {"A": "x＝9", "B": "x＝−9", "C": "x＝9 或 x＝−9", "D": "x＝81 或 x＝−81"}, "C", "平方後等於 81 的數有 9 與 −9，因此 x＝±9，選 C。", "解平方方程式時要同時列出正、負兩個平方根，不可只取主平方根。", ["找出 81 的主平方根 9。", "平方方程式的解包含 9 與其相反數 −9。", "寫出 x＝9 或 x＝−9。", "代回兩個值，平方都為 81。", "選 C，區分 √81＝9 與方程式的兩個解。"], "easy"),
    make(3, "√(1／4) 的值是多少？", {"A": "−1／2", "B": "1／4", "C": "1／2", "D": "2"}, "C", "(1／2)²＝1／4，且主平方根取正值，所以 √(1／4)＝1／2，選 C。", "分子分母分別取主平方根，並檢查結果非負且平方回到原數。", ["找分子 1 的平方根為 1。", "找分母 4 的主平方根為 2。", "得到 √(1／4)＝1／2。", "確認 1／2 為非負數。", "選 C，平方 (1／2)² 回到 1／4。"], "medium"),
    make(4, "√0.81 的值是多少？", {"A": "0.09", "B": "0.9", "C": "9", "D": "−0.9"}, "B", "0.9²＝0.81，主平方根取非負值，所以 √0.81＝0.9，選 B。", "將小數平方或改寫成分數，找出平方後回到 0.81 的非負數。", ["觀察 0.9×0.9＝0.81。", "因此 0.9 是平方根。", "根號表示主平方根，取正的 0.9。", "排除 −0.9，它是方程式 x²＝0.81 的另一解但不是主根。", "選 B，平方驗證結果。"], "easy"),
    make(5, "若正方形面積為 64 平方公分，邊長為多少？", {"A": "4 公分", "B": "6 公分", "C": "8 公分", "D": "16 公分"}, "C", "正方形邊長是面積的主平方根，√64＝8，選 C。", "幾何長度必取正值，因此面積開平方後選主平方根。", ["建立邊長²＝64。", "取 64 的主平方根。", "計算 √64＝8。", "因邊長是長度，排除 −8。", "選 C，檢查 8×8＝64 平方公分。"], "easy"),
    make(6, "下列哪個數是 √20 的較簡單表示？", {"A": "2√5", "B": "4√5", "C": "√10", "D": "5√2"}, "A", "20＝4×5，√20＝√4×√5＝2√5，所以選 A。", "先從被開方數提出最大的完全平方因數，再保留不能再開的部分。", ["分解 20＝4×5。", "把 4 開平方得到 2。", "保留 √5。", "合併為 2√5。", "選 A，平方 (2√5)²＝20 驗證。"], "hard"),
    make(7, "下列哪個敘述正確？", {"A": "√(−9) 是實數", "B": "√9＝±3", "C": "√16＝4", "D": "√0＝1"}, "C", "主平方根 √16＝4；√9 是 3 而非 ±3，負數沒有實數平方根，√0＝0，因此選 C。", "分清主平方根、平方方程式解與實數根號的定義，逐項檢查。", ["檢查 A：負數在實數範圍沒有平方根。", "檢查 B：√9 是主根 3，±3 是 x²＝9 的解。", "檢查 C：4²＝16，成立。", "檢查 D：0²＝0，√0 不等於 1。", "選 C，確認只有一項符合根號定義。"], "medium"),
    make(8, "若 a＝√36，b 是方程式 x²＝36 的負解，則 a＋b 為何？", {"A": "−12", "B": "−6", "C": "0", "D": "12"}, "C", "a＝√36＝6，負解 b＝−6，所以 a＋b＝0，選 C。", "先分別處理主平方根與方程式的負解，再代入加法。", ["計算 a＝√36＝6。", "方程式 x²＝36 的負解為 b＝−6。", "建立 a＋b＝6＋(−6)。", "計算結果為 0。", "選 C，確認主根與負根互為相反數。"], "medium"),
    make(9, "比較 √12 與 3，何者較大？", {"A": "√12 較大", "B": "3 較大", "C": "兩者相等", "D": "無法比較"}, "A", "√12 與 3 都是非負數；比較平方得 12 與 9，因 12＞9，所以 √12＞3，選 A。", "比較非負數平方即可判斷大小，避免只靠不精確估算。", ["確認 √12 與 3 都是非負數。", "平方比較： (√12)²＝12，3²＝9。", "因 12＞9，所以 √12＞3。", "得到 √12 較大。", "選 A，注意選項與平方比較方向一致。"], "hard"),
    make(10, "若 √x＝5，x 為何？", {"A": "5", "B": "10", "C": "25", "D": "−25"}, "C", "兩邊平方得 x＝5²＝25；且 x 為非負，選 C。", "將主平方根等式兩邊平方，最後檢查被開方數的非負條件。", ["寫下 √x＝5。", "兩邊平方，左邊回到 x。", "計算右邊 5²＝25。", "得到 x＝25，符合平方根定義。", "選 C，檢查 √25＝5。"], "easy"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

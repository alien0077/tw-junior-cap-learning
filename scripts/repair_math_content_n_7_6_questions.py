import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-7-6"
KG = "kg-math-content-n-7-6"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "meaning of exponents, repeated multiplication, base and exponent, zero and first powers, and signed bases", "observedPattern": "公立學校公開數學試題常要求解讀指數記號、展開重複乘法、計算冪、辨認底數與指數，並處理括號與負號；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-7-6-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供指數意義、重複乘法、底數與指數及正負底數能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的指數方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "2⁴ 的值是多少？", {"A": "6", "B": "8", "C": "16", "D": "24"}, "C", "2⁴ 表示 2×2×2×2＝16，所以選 C。", "把指數記號展開成底數重複相乘，再逐步計算。", ["辨認底數為 2、指數為 4。", "展開為 2×2×2×2。", "前兩個 2 相乘得 4。", "後兩個 2 相乘得 4，再算 4×4＝16。", "選 C，確認不是把 2 與 4 相乘。"], "easy"),
    make(2, "在 5⁷ 中，底數與指數分別是什麼？", {"A": "底數 5，指數 7", "B": "底數 7，指數 5", "C": "底數 35，指數 1", "D": "底數 1，指數 35"}, "A", "指數記號中下方的大數 5 是底數，上方的 7 是指數，因此選 A。", "先定位數字的位置，再用『底數重複相乘的次數』理解指數。", ["觀察記號 5⁷。", "辨認下方的 5 是被重複相乘的數。", "辨認上方的 7 是重複次數。", "寫出底數 5、指數 7。", "選 A，展開為七個 5 相乘作驗證。"], "easy"),
    make(3, "下列哪個式子等於 3×3×3×3×3？", {"A": "3⁴", "B": "3⁵", "C": "5³", "D": "15³"}, "B", "3 重複相乘 5 次，寫成 3⁵，所以選 B。", "數底數出現的次數，該次數就是指數，不能交換底數與次數。", ["數出重複的底數都是 3。", "數出共有 5 個 3。", "把底數寫成 3。", "把重複次數寫成指數 5。", "選 B，展開 3⁵ 可回到原乘積。"], "easy"),
    make(4, "(−3)² 的值是多少？", {"A": "−9", "B": "−6", "C": "6", "D": "9"}, "D", "括號表示負數 −3 整體平方：(−3)×(−3)＝9，所以選 D。", "先確認括號把負號包含在底數內，再依負負得正計算。", ["辨認底數是整個 −3。", "展開 (−3)² 為 (−3)×(−3)。", "兩個負數相乘得到正數。", "計算絕對值 3×3＝9。", "選 D，注意不是 −(3²) 的寫法。"], "medium"),
    make(5, "−3² 的值是多少？", {"A": "−9", "B": "−6", "C": "6", "D": "9"}, "A", "沒有括號時，指數先作用在 3，之後保留前面的負號，−3²＝−(3²)＝−9，選 A。", "比較括號與負號的寫法，依運算優先順序先算冪次。", ["辨認式子沒有把 −3 放入括號。", "先計算 3²＝9。", "保留前面的負號，得到 −9。", "比較與 (−3)² 的差異。", "選 A，避免把無括號的負號誤當成底數。"], "hard"),
    make(6, "7⁰ 的值是多少？", {"A": "0", "B": "1", "C": "7", "D": "無法計算"}, "B", "任何非零數的 0 次方等於 1，因此 7⁰＝1，選 B。", "記住零次方的定義，再確認底數 7 確實不是 0。", ["確認底數 7 為非零數。", "套用非零數的零次方規則 a⁰＝1。", "得到 7⁰＝1。", "區分指數 0 與結果 0。", "選 B，檢查 7¹÷7¹ 也等於 1。"], "medium"),
    make(7, "4¹ 的值是多少？", {"A": "1", "B": "4", "C": "5", "D": "16"}, "B", "任何數的一次方等於本身，4¹＝4，所以選 B。", "把一次方理解為只出現一次底數，直接讀回底數。", ["辨認底數 4、指數 1。", "展開 4¹ 只有一個因數 4。", "因此結果保持為 4。", "排除把指數 1 當成相加或平方。", "選 B，確認 4¹＝4。"], "easy"),
    make(8, "比較 2⁵ 與 5²，下列何者正確？", {"A": "2⁵＜5²", "B": "2⁵＝5²", "C": "2⁵＞5²", "D": "無法比較"}, "C", "2⁵＝32，5²＝25，因此 2⁵＞5²，選 C。", "先分別計算兩個冪，再比較結果，不能只比較底數或指數。", ["計算 2⁵＝32。", "計算 5²＝25。", "比較 32 與 25。", "判定 32 大於 25。", "選 C，確認兩個冪的底數與指數都不同。"], "medium"),
    make(9, "若 2ⁿ＝32，n 為何？", {"A": "3", "B": "4", "C": "5", "D": "6"}, "C", "32＝2×2×2×2×2＝2⁵，所以 n＝5，選 C。", "將右邊數值寫成相同底數的重複乘法，再數出因數個數。", ["把 32 寫成 2 的乘冪。", "得到 32＝2×2×2×2×2。", "數出共有 5 個 2。", "因此指數 n＝5。", "選 C，代回 2⁵＝32 驗證。"], "medium"),
    make(10, "某正方形邊長為 3 公分，面積可用哪個指數式表示？", {"A": "3² 平方公分", "B": "2³ 平方公分", "C": "3³ 平方公分", "D": "3＋3 平方公分"}, "A", "正方形面積＝邊長×邊長＝3×3＝3² 平方公分，所以選 A。", "先寫出幾何量的乘法關係，再用指數表示相同因子的重複乘法。", ["確認正方形兩個互相垂直邊長都為 3 公分。", "建立面積 3×3。", "將兩個 3 的乘積寫成 3²。", "附上面積單位平方公分。", "選 A，計算面積數值為 9 平方公分。"], "easy"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

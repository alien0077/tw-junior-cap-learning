import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-7-7"
KG = "kg-math-content-n-7-7"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "laws of exponents, same-base multiplication and division, power of a power, and power of a product", "observedPattern": "公立學校公開數學試題常要求以指數律整理同底數乘除、冪的乘方與積的乘方，再以數值或代數式驗證；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-7-7-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供指數律、同底數乘除、冪的乘方與積的乘方能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的指數律方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "化簡 a³×a⁵（a≠0）為何？", {"A": "a⁸", "B": "a¹⁵", "C": "a²", "D": "2a⁸"}, "A", "同底數相乘時指數相加，a³×a⁵＝a³⁺⁵＝a⁸，所以選 A。", "確認底數相同後只處理指數相加，不把底數相乘或指數相乘。", ["辨認兩因式底數都是 a。", "套用同底數相乘律 aᵐ×aⁿ＝aᵐ⁺ⁿ。", "把指數 3 與 5 相加。", "得到 a⁸。", "選 A，展開後共有 8 個 a 相乘。"], "easy"),
    make(2, "化簡 b⁹÷b⁴（b≠0）為何？", {"A": "b¹³", "B": "b⁵", "C": "b³⁶", "D": "1／b⁵"}, "B", "同底數相除時指數相減，b⁹÷b⁴＝b⁹⁻⁴＝b⁵，選 B。", "確認除數不為 0，再用分子分母約去共同因子理解指數相減。", ["辨認分子分母底數都是 b。", "套用同底數相除律 bᵐ÷bⁿ＝bᵐ⁻ⁿ。", "計算 9−4＝5。", "得到 b⁵。", "選 B，將 b⁴ 個因子約去後剩 5 個 b。"], "easy"),
    make(3, "化簡 (x²)⁴ 為何？", {"A": "x⁶", "B": "x⁸", "C": "x¹⁶", "D": "4x²"}, "B", "冪的乘方指數相乘，(x²)⁴＝x²×⁴＝x⁸，所以選 B。", "看到括號外的指數時，將內外兩個指數相乘，不要相加。", ["辨認內層指數 2、外層指數 4。", "套用 (xᵐ)ⁿ＝xᵐⁿ。", "計算 2×4＝8。", "寫成 x⁸。", "選 B，展開可看到共有 8 個 x 因子。"], "medium"),
    make(4, "化簡 (2y)³ 為何？", {"A": "2y³", "B": "6y³", "C": "8y³", "D": "2³＋y³"}, "C", "積的乘方要各因數分別乘方：(2y)³＝2³y³＝8y³，選 C。", "將括號內乘積的每個因數都取同一個指數，再計算常數冪。", ["辨認括號內是 2×y 的乘積。", "套用 (ab)ⁿ＝aⁿbⁿ。", "得到 2³×y³。", "計算 2³＝8。", "選 C，寫成 8y³。"], "medium"),
    make(5, "計算 2³×2⁴ 的值。", {"A": "32", "B": "64", "C": "128", "D": "256"}, "C", "2³×2⁴＝2⁷＝128，所以選 C。", "先用同底數相乘合併指數，再計算最後的冪。", ["合併同底數：2³×2⁴＝2⁷。", "將 2⁷ 展開或逐次平方。", "計算 2⁷＝128。", "確認不是把 3×4 當成指數。", "選 C，直接計算 8×16 也得 128。"], "easy"),
    make(6, "計算 3⁵÷3² 的值。", {"A": "3", "B": "9", "C": "27", "D": "81"}, "C", "3⁵÷3²＝3³＝27，所以選 C。", "同底數相除先相減指數，再計算剩餘冪次。", ["套用同底數相除律，得 3⁵⁻²。", "計算指數 5−2＝3。", "得到 3³。", "計算 3×3×3＝27。", "選 C，將 243 除以 9 也得 27。"], "easy"),
    make(7, "化簡 (p³q²)² 為何？", {"A": "p⁵q⁴", "B": "p⁶q⁴", "C": "p⁶q²", "D": "p⁹q⁴"}, "B", "積的乘方與冪的乘方分別作用：(p³q²)²＝p⁶q⁴，選 B。", "先把乘積拆開，再將每個底數的指數乘以括號外指數。", ["把括號視為 p³ 與 q² 的乘積。", "將 p³ 平方得 p⁶。", "將 q² 平方得 q⁴。", "合併成 p⁶q⁴。", "選 B，確認兩個指數都乘上 2。"], "hard"),
    make(8, "若 5ᵐ×5²＝5⁹，m 為何？", {"A": "2", "B": "7", "C": "11", "D": "18"}, "B", "同底數相乘得 5ᵐ⁺²＝5⁹，因此 m＋2＝9，m＝7，選 B。", "先合併指數，再比較相同底數冪的指數。", ["使用同底數相乘律，左式變成 5ᵐ⁺²。", "因兩邊底數同為 5，令指數 m＋2＝9。", "兩邊同減 2。", "解得 m＝7。", "選 B，代回 5⁷×5²＝5⁹。"], "medium"),
    make(9, "化簡 (a⁴÷a)×a²（a≠0）為何？", {"A": "a⁴", "B": "a⁵", "C": "a⁶", "D": "a⁷"}, "B", "a⁴÷a＝a³，再乘 a² 得 a³×a²＝a⁵，所以選 B。", "依原式順序先處理同底數除法，再處理乘法，或合併指數 4−1＋2。", ["先將 a⁴÷a 化為 a⁴⁻¹＝a³。", "原式變為 a³×a²。", "同底數相乘，指數相加 3＋2＝5。", "得到 a⁵。", "選 B，檢查直接合併 4−1＋2 也為 5。"], "hard"),
    make(10, "若 x²×x³÷x⁴＝xⁿ（x≠0），n 為何？", {"A": "−1", "B": "0", "C": "1", "D": "9"}, "C", "同底數指數依序為 2＋3−4＝1，因此 n＝1，選 C。", "把乘法轉成指數相加、除法轉成指數相減，依序整理。", ["由 x²×x³ 得指數 2＋3＝5。", "再除以 x⁴，指數變為 5−4。", "計算 5−4＝1。", "因此原式為 x¹，n＝1。", "選 C，確認 x 非零使除法律合法。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

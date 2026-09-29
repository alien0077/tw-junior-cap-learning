import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-6"
KG = "kg-math-content-a-8-6"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "quadratic equations, roots, number of real solutions, algebraic modeling, and verification", "observedPattern": "公立學校公開數學試題常以二次項辨識、根的意義、代入驗根、因式分解與面積／整數情境建立一元二次方程式；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-8-6-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一元二次方程式、根與情境建模能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的一元二次方程式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "方程式 x²−9＝0 的實數解為何？", {"A": "x＝3", "B": "x＝−3", "C": "x＝3 或 x＝−3", "D": "沒有實數解"}, "C", "x²＝9，所以 x＝±3；平方後等於 9 的實數有 3 與 −3 兩個。", "先移項成平方等於常數，再記得平方根有正負兩個可能。", ["將 x²−9＝0 改寫成 x²＝9。", "取 9 的平方根。", "列出 x＝3 與 x＝−3。", "分別代回原式都得到 0。", "選 C，不能只保留正平方根。"], "easy"),
    make(2, "下列哪一個是標準的一元二次方程式？", {"A": "3x＋5＝0", "B": "x²＋4x−1＝0", "C": "xy＋2＝0", "D": "1／x＋3＝0"}, "B", "B 含一個未知數 x 的二次項且等於零；A 是一次式，C 有兩個未知數，D 含變數在分母。", "檢查未知數個數、最高次數與是否能寫成二次多項式等於零。", ["確認題目要求一個未知數。", "檢查 B 只有 x 且最高次為 2。", "確認 B 具備二次多項式等於 0 的形式。", "排除一次式、兩變數式與分母含變數的式子。", "選 B，符合一元二次方程式定義。"], "easy"),
    make(3, "在方程式 x²−5x＋6＝0 中，『方程式的根』代表什麼？", {"A": "使左式等於 1 的 x 值", "B": "使左式等於 0 的 x 值", "C": "多項式的最高次數", "D": "常數項 6"}, "B", "根是代入未知數後能使方程式成立的值；標準式右側為 0，因此要使左式也等於 0。", "把根的定義連回等式成立條件，而不是只看係數或次數。", ["確認方程式左側是 x²−5x＋6。", "根必須使左右兩邊相等。", "因右側為 0，所以左式也必須為 0。", "排除最高次與常數項等結構資訊。", "選 B，這是根的定義。"], "easy"),
    make(4, "方程式 x²−5x＋6＝0 的兩根為何？", {"A": "1、6", "B": "2、3", "C": "−2、−3", "D": "−1、−6"}, "B", "x²−5x＋6＝(x−2)(x−3)，令任一因式為零得 x＝2 或 x＝3。", "先因式分解，再使用零乘積性質取得兩個根。", ["找乘積 6、和 −5 的兩數 −2、−3。", "分解為 (x−2)(x−3)＝0。", "令 x−2＝0 得 x＝2。", "令 x−3＝0 得 x＝3。", "選 B，代回原式兩根都成立。"], "medium"),
    make(5, "方程式 x²＋4x＋4＝0 有幾個相異的實數解？", {"A": "0 個", "B": "1 個", "C": "2 個", "D": "4 個"}, "B", "x²＋4x＋4＝(x＋2)²，只有 x＝−2 一個相異實根，雖然它是重根。", "先辨認完全平方，再區分根的重複次數與相異根數。", ["將左式因式分解為 (x＋2)²。", "令 x＋2＝0 得 x＝−2。", "確認同一根重複兩次但數值相同。", "因此相異實數解只有 1 個。", "選 B，注意不是把重根算成兩個相異值。"], "medium"),
    make(6, "方程式 x²＋1＝0 有何種實數解情形？", {"A": "有兩個實數解 1、−1", "B": "有一個實數解 0", "C": "沒有實數解", "D": "所有實數都是解"}, "C", "x²＋1＝0 等於 x²＝−1；任何實數平方都不會是負數，因此沒有實數解。", "移項後檢查平方的可能範圍，避免把 x²＝1 的結論套錯。", ["將方程式改寫為 x²＝−1。", "回想實數平方必為 0 或正數。", "判斷不可能等於 −1。", "排除 ±1、0 與全體實數的說法。", "選 C，結論是沒有實數解。"], "medium"),
    make(7, "一個長方形長為 x＋3、寬為 x，面積為 28 平方公分；若 x 為正數，x 應為何？", {"A": "x＝3", "B": "x＝4", "C": "x＝5", "D": "x＝7"}, "B", "建立 x(x＋3)＝28，得 x²＋3x−28＝0＝(x＋7)(x−4)，解為 x＝−7 或 4；長度為正，所以 x＝4。", "先由面積建立二次方程式，再用因式分解並依情境排除負長度。", ["由面積寫 x(x＋3)＝28。", "整理為 x²＋3x−28＝0。", "分解為 (x＋7)(x−4)＝0。", "得到 x＝−7 或 x＝4，排除負的長度。", "選 B，代回 4×7＝28。"], "hard"),
    make(8, "兩個連續正整數的乘積為 20。若較小者為 x，哪個方程式正確？", {"A": "x＋(x＋1)＝20", "B": "x(x＋1)＝20", "C": "x²＋1＝20", "D": "2x＋1＝20"}, "B", "連續正整數可表示為 x 與 x＋1，乘積條件就是 x(x＋1)＝20。", "把『連續』翻成相差 1，把『乘積』翻成相乘。", ["令較小的正整數為 x。", "將較大者表示為 x＋1。", "把乘積寫成 x(x＋1)。", "令乘積等於 20。", "選 B，完整對應兩個文字條件。"], "easy"),
    make(9, "下列哪個數是方程式 2x²−8＝0 的根？", {"A": "1", "B": "2", "C": "3", "D": "4"}, "B", "代入 x＝2 得 2(2²)−8＝8−8＝0，因此 2 是根；另一根為 −2。", "將候選值代入原方程式，等於零才是根。", ["選取候選值 x＝2。", "計算 x²＝4。", "代入左式得到 2×4−8＝0。", "確認等式成立。", "選 B，完成驗根。"], "easy"),
    make(10, "若方程式 x²−6x＋9＝0 的圖形與 x 軸相切，這對方程式的根表示什麼？", {"A": "有兩個不同實根", "B": "沒有實根", "C": "有一個重複的實根 x＝3", "D": "所有 x 都是根"}, "C", "x²−6x＋9＝(x−3)²，圖形只在 x＝3 接觸 x 軸，表示一個重根 x＝3。", "將圖形與根的意義連結：與 x 軸交點的 x 座標就是實根。", ["辨認方程式可寫成 (x−3)²＝0。", "解得 x＝3。", "平方形式表示同一根出現兩次。", "圖形與 x 軸只有一個接觸點。", "選 C，正確描述重根與相切。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

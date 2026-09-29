import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-4"
KG = "kg-math-content-a-8-4"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "common-factor extraction, difference of squares, trinomial factoring, perfect squares, and verification", "observedPattern": "公立學校公開數學試題常以提出公因式、平方差、二次三項式、完全平方與乘法回驗評量因式分解；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-8-4-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供因式分解、乘法公式逆用與代數結構能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的因式分解能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "因式分解 6x²＋9x，結果為何？", {"A": "3x(2x＋3)", "B": "6x(x＋9)", "C": "x(6x＋9x)", "D": "3(2x²＋3x)"}, "A", "兩項的最大公因式是 3x，提出後得 3x(2x＋3)。", "先找係數與字母的最大公因式，再逐項除以它。", ["找 6 與 9 的最大公因數 3。", "找兩項共同的 x，得到公因式 3x。", "6x²÷3x＝2x、9x÷3x＝3。", "把結果寫成 3x(2x＋3)。", "選 A，乘回可還原原式。"], "easy"),
    make(2, "因式分解 x²−25，結果為何？", {"A": "(x−5)²", "B": "(x＋5)²", "C": "(x−5)(x＋5)", "D": "x(x−25)"}, "C", "x²−25 是 x²−5²，使用平方差公式得 (x−5)(x＋5)。", "辨認兩平方相減，不要誤用完全平方公式。", ["確認第一項是 x²、第二項 25＝5²。", "辨認平方差 A²−B²。", "套用 (A−B)(A＋B)。", "得到 (x−5)(x＋5)。", "選 C，展開後中間項互相抵消。"], "easy"),
    make(3, "一塊長方形地磚的面積可寫成 x²＋7x＋12，若以 x 表示其一邊，另一邊的因式表示為何？", {"A": "x＋2", "B": "x＋3", "C": "x＋4", "D": "x＋12"}, "C", "將面積多項式因式分解：x²＋7x＋12＝(x＋3)(x＋4)。若已知一邊為 x＋3，另一邊就是 x＋4。", "先把面積多項式分解成兩個邊長因子，再依題幹已知邊長挑出另一因子。", ["找乘積為 12、和為 7 的兩數 3 與 4。", "把面積寫成 (x＋3)(x＋4)。", "辨認題幹已知的一邊是 x＋3。", "讀出另一邊因式為 x＋4。", "選 C，乘回兩邊可還原面積多項式。"], "medium"),
    make(4, "因式分解 x²−10x＋25，結果為何？", {"A": "(x−5)²", "B": "(x＋5)²", "C": "(x−25)(x＋1)", "D": "(x−10)(x−15)"}, "A", "前後兩項是 x² 與 5²，中間項 −10x＝−2(x)(5)，所以是 (x−5)²。", "檢查首末項是否為平方，並用中間項正負確認括號符號。", ["辨認 x² 與 25 都是平方。", "取平方根 x 與 5。", "檢查中間項應為 −2×x×5＝−10x。", "因此兩括號都為 x−5。", "選 A，展開完全平方回驗。"], "medium"),
    make(5, "因式分解 4y²−12y＋9，結果為何？", {"A": "(2y＋3)²", "B": "(2y−3)²", "C": "(4y−3)²", "D": "(y−3)²"}, "B", "4y²−12y＋9＝(2y)²−2(2y)(3)＋3²，因此為 (2y−3)²。", "把首項與常數項取平方根，再檢查中間項。", ["首項 4y² 的平方根是 2y。", "常數 9 的平方根是 3。", "計算 −2×2y×3＝−12y。", "使用負號組成 (2y−3)²。", "選 B，展開可還原。"], "medium"),
    make(6, "因式分解 3a²＋12a＋12，結果為何？", {"A": "3(a＋2)²", "B": "3(a＋4)²", "C": "(3a＋2)²", "D": "3(a²＋12a＋12)"}, "A", "先提出公因式 3，得 3(a²＋4a＋4)，括號內是 (a＋2)²，所以結果為 3(a＋2)²。", "先提出最大公因式，再辨認括號內的完全平方。", ["找三項共同因數 3。", "提出 3 得 3(a²＋4a＋4)。", "辨認 a²＋4a＋4＝(a＋2)²。", "合成 3(a＋2)²。", "選 A，乘回檢查三項係數。"], "hard"),
    make(7, "因式分解 2x²＋8x＋6，結果為何？", {"A": "2(x＋1)(x＋3)", "B": "2(x＋2)(x＋3)", "C": "(2x＋2)(x＋6)", "D": "2(x²＋8x＋6)"}, "A", "先提出 2 得 2(x²＋4x＋3)，括號內因式分解為 (x＋1)(x＋3)。", "先提出公因式，再對首項為 1 的三項式找和與積。", ["三項最大公因式為 2。", "提出後得到 2(x²＋4x＋3)。", "找乘積 3、和 4 的數 1 與 3。", "得到 2(x＋1)(x＋3)。", "選 A，展開兩括號再乘 2 回驗。"], "medium"),
    make(8, "因式分解 x³−4x，結果為何？", {"A": "x(x−2)(x＋2)", "B": "x(x−4)", "C": "(x−2)³", "D": "x²(x−4)"}, "A", "先提出 x 得 x(x²−4)，再用平方差分解 x²−4＝(x−2)(x＋2)。", "多項式可連續使用不同方法，先公因式後平方差。", ["觀察兩項共有 x，提出得 x(x²−4)。", "辨認 x²−4＝x²−2²。", "分解為 (x−2)(x＋2)。", "合併為 x(x−2)(x＋2)。", "選 A，乘回可得到 x³−4x。"], "hard"),
    make(9, "若矩形面積為 x²＋5x＋6，且一邊長為 x＋2，另一邊長應為何？", {"A": "x＋2", "B": "x＋3", "C": "x＋6", "D": "x−3"}, "B", "x²＋5x＋6＝(x＋2)(x＋3)，已知一邊 x＋2，因此另一邊為 x＋3。", "把面積多項式因式分解成兩個邊長因子，再使用已知因子。", ["找乘積 6、和 5 的兩數 2 與 3。", "分解面積為 (x＋2)(x＋3)。", "對照已知一邊 x＋2。", "讀出另一個因子 x＋3。", "選 B，兩邊相乘回到原面積。"], "medium"),
    make(10, "下列哪一個是 9m²−16 的完整因式分解？", {"A": "(3m−4)(3m＋4)", "B": "(9m−4)(m＋4)", "C": "(3m−16)(3m＋1)", "D": "(9m−16)(m＋1)"}, "A", "9m²−16＝(3m)²−4²，使用平方差得 (3m−4)(3m＋4)，且兩因式不可再以整係數多項式分解。", "先把兩項辨成平方，再寫出一正一負的兩個因式。", ["確認 9m²＝(3m)²、16＝4²。", "套用平方差公式。", "寫成 (3m−4)(3m＋4)。", "檢查乘積的中間項 −12m＋12m 抵消。", "選 A，完成完整因式分解。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

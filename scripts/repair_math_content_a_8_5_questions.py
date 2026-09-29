import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-5"
KG = "kg-math-content-a-8-5"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "factorization methods, grouping, coefficient splitting, perfect squares, and complete factorization", "observedPattern": "公立學校公開數學試題常以提出公因式、分組、十字交乘、公式逆用及連續因式分解評量方法選擇與結果驗證；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-8-5-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供因式分解方法與結果驗證能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的因式分解方法方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "因式分解 ax＋ay＋bx＋by，最適合先使用哪種方法？", {"A": "分組分解法", "B": "只提出 a", "C": "平方差公式", "D": "完全平方公式"}, "A", "可分組為 a(x＋y)＋b(x＋y)，再提出共同的 (x＋y)，得 (a＋b)(x＋y)，因此先用分組分解法。", "尋找兩兩有共同括號的項，讓每組提出後出現相同二項式。", ["把前兩項與後兩項分成兩組。", "第一組提出 a 得 a(x＋y)。", "第二組提出 b 得 b(x＋y)。", "再提出共同因式 x＋y。", "選 A，完成分組分解。"], "medium"),
    make(2, "因式分解 x²＋9x＋20，結果為何？", {"A": "(x＋2)(x＋10)", "B": "(x＋4)(x＋5)", "C": "(x−4)(x−5)", "D": "(x＋1)(x＋20)"}, "B", "找乘積 20、和 9 的兩數 4 與 5，因此 x²＋9x＋20＝(x＋4)(x＋5)。", "使用十字交乘的乘積與和條件，先確認常數乘積再核對中間項。", ["找兩數乘積為 20。", "檢查 4×5＝20。", "檢查 4＋5＝9。", "組成 (x＋4)(x＋5)。", "選 B，展開驗證一次項為 9x。"], "easy"),
    make(3, "因式分解 6x²＋11x＋3，結果為何？", {"A": "(2x＋1)(3x＋3)", "B": "(3x＋1)(2x＋3)", "C": "(6x＋1)(x＋3)", "D": "(2x−1)(3x−3)"}, "B", "以首項係數 6 與常數 3 配對，(3x＋1)(2x＋3) 展開為 6x²＋11x＋3。", "用交叉乘積檢查中間項：3x×3 與 1×2x 相加要得到 11x。", ["確認首項因子可取 3x 與 2x。", "確認常數因子可取 1 與 3。", "交叉相乘得到 9x＋2x＝11x。", "寫成 (3x＋1)(2x＋3)。", "選 B，乘回三項式驗證。"], "hard"),
    make(4, "因式分解 2x²−7x＋3，結果為何？", {"A": "(2x−1)(x−3)", "B": "(2x＋1)(x−3)", "C": "(2x−3)(x−1)", "D": "(x−1)(2x−3)"}, "A", "(2x−1)(x−3) 展開為 2x²−6x−x＋3＝2x²−7x＋3。", "先配首項 2x、x 與常數 −1、−3，再用交叉項核對負號。", ["配出首項因子 2x 與 x。", "常數 3 的同號負因子取 −1、−3。", "交叉項為 −6x−x＝−7x。", "組成 (2x−1)(x−3)。", "選 A，確認常數乘積為 3。"], "medium"),
    make(5, "下列哪個方法最適合分解 4a²−12ab＋9b²？", {"A": "平方差公式", "B": "完全平方公式逆用", "C": "只提出 4", "D": "分組後不再整理"}, "B", "首末項是 (2a)²、(3b)²，中間項 −2(2a)(3b)，所以是 (2a−3b)²，適合完全平方公式逆用。", "檢查首末平方根與中間項是否符合兩倍乘積。", ["取首項平方根 2a。", "取末項平方根 3b。", "計算 −2(2a)(3b)＝−12ab。", "判斷為 (2a−3b)²。", "選 B，完成完全平方辨識。"], "medium"),
    make(6, "因式分解 12x³−27x，完整結果為何？", {"A": "3x(2x−3)(2x＋3)", "B": "3(4x³−9x)", "C": "x(12x²−27)", "D": "3x(2x−3)²"}, "A", "先提出 3x 得 3x(4x²−9)，再用平方差 4x²−9＝(2x−3)(2x＋3)。", "先找最大公因式，再對剩餘二次式繼續分解直到不能分。", ["找 12x³ 與 −27x 的最大公因式 3x。", "提出後得 3x(4x²−9)。", "辨認 4x²−9 是平方差。", "分解為 (2x−3)(2x＋3)。", "選 A，確認已完成連續分解。"], "hard"),
    make(7, "因式分解 5m²−20m＋20，結果為何？", {"A": "5(m−2)²", "B": "5(m＋2)²", "C": "(5m−2)²", "D": "5(m²−20m＋20)"}, "A", "提出 5 得 5(m²−4m＋4)，括號內是 (m−2)²，因此為 5(m−2)²。", "先提出數字公因式，再辨認完全平方結構。", ["找三項共同因數 5。", "提出後得到 5(m²−4m＋4)。", "比較 m²、−4m、4 與 (m−2)²。", "寫成 5(m−2)²。", "選 A，乘回確認中間項為 −20m。"], "medium"),
    make(8, "若將 3x²−x−2 因式分解，哪個結果正確？", {"A": "(3x＋2)(x−1)", "B": "(3x−2)(x＋1)", "C": "(3x＋1)(x−2)", "D": "(x−1)(3x＋2)"}, "A", "(3x＋2)(x−1) 展開為 3x²−3x＋2x−2＝3x²−x−2。", "配首項與常數因子後，用交叉項加總確認一次項。", ["首項配成 3x 與 x。", "常數 −2 配成 2 與 −1。", "交叉項 −3x＋2x＝−x。", "組成 (3x＋2)(x−1)。", "選 A，乘回驗證三個係數。"], "medium"),
    make(9, "長方形面積為 x²＋6x＋8，若一邊為 x＋2，另一邊用因式表示為何？", {"A": "x＋2", "B": "x＋4", "C": "x＋6", "D": "x＋8"}, "B", "x²＋6x＋8＝(x＋2)(x＋4)，已知一邊為 x＋2，另一邊為 x＋4。", "將面積多項式因式分解，再對照已知的一邊因子。", ["找乘積 8、和 6 的兩數 2 與 4。", "分解為 (x＋2)(x＋4)。", "比對已知因子 x＋2。", "讀出另一邊是 x＋4。", "選 B，乘回可還原面積。"], "easy"),
    make(10, "某同學說 2x²＋5x＋2＝(2x＋1)(x＋2)。用乘法回驗後，應如何判斷？", {"A": "正確，因為首項與常數相同即可", "B": "錯誤，正確因式為 (2x＋2)(x＋1)", "C": "錯誤，正確因式為 (2x＋1)(x＋2) 以外的形式", "D": "無法用展開判斷"}, "A", "(2x＋1)(x＋2) 展開為 2x²＋4x＋x＋2＝2x²＋5x＋2，因此同學的分解正確。", "把候選因式逐項展開，三個係數都相符才可確認。", ["計算 2x×x 得 2x²。", "計算交叉項 2x×2 與 1×x 得 4x＋x。", "計算常數 1×2 得 2。", "合併為 2x²＋5x＋2。", "選 A，完整回驗而非只看首末項。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

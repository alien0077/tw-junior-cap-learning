import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-7"
KG = "kg-math-content-a-8-7"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "solving quadratic equations by factoring and square-root methods, with geometric and integer applications", "observedPattern": "公立學校公開數學試題常以因式分解、平方根、二次方程式根的驗證與面積／連續整數情境要求求解並篩選合理答案；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-8-7-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一元二次方程式解法、根驗證與應用題能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的二次方程式解法方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "解方程式 x²−7x＋12＝0，兩根為何？", {"A": "1、12", "B": "2、6", "C": "3、4", "D": "−3、−4"}, "C", "x²−7x＋12＝(x−3)(x−4)，因此 x＝3 或 x＝4。", "先因式分解，再用零乘積性質分別令因式為零。", ["找乘積 12、和 −7 的兩數 −3、−4。", "分解為 (x−3)(x−4)＝0。", "令 x−3＝0 得 x＝3。", "令 x−4＝0 得 x＝4。", "選 C，將兩根代回原式驗證。"], "easy"),
    make(2, "解方程式 2x²−8＝0，實數解為何？", {"A": "x＝2", "B": "x＝−2", "C": "x＝2 或 x＝−2", "D": "沒有實數解"}, "C", "2x²＝8 得 x²＝4，所以 x＝±2。", "先除以係數化成平方，再取正負平方根。", ["兩邊同加 8 得 2x²＝8。", "兩邊同除以 2 得 x²＝4。", "取平方根得到 x＝2 或 x＝−2。", "代回原式兩個結果都使左式為 0。", "選 C，保留正負兩根。"], "easy"),
    make(3, "解方程式 x²＋2x−8＝0，x 為何？", {"A": "2 或 −4", "B": "4 或 −2", "C": "8 或 −1", "D": "−8 或 1"}, "A", "x²＋2x−8＝(x＋4)(x−2)，所以 x＝−4 或 x＝2。", "找常數乘積與一次項係數，再以零乘積性質求根。", ["找乘積 −8、和 2 的兩數 4 與 −2。", "分解為 (x＋4)(x−2)＝0。", "得到 x＝−4 或 x＝2。", "代回確認兩個值都使方程式成立。", "選 A，答案順序不影響根的集合。"], "medium"),
    make(4, "解方程式 x²−4x−5＝0，哪組解正確？", {"A": "x＝1 或 −5", "B": "x＝5 或 −1", "C": "x＝4 或 −5", "D": "x＝−4 或 5"}, "B", "x²−4x−5＝(x−5)(x＋1)，所以 x＝5 或 x＝−1。", "用兩數乘積 −5、和 −4 找因式，再逐一令因式為零。", ["找乘積 −5、和 −4 的兩數 −5 與 1。", "寫成 (x−5)(x＋1)＝0。", "解出 x＝5。", "解出 x＝−1。", "選 B，兩根代回皆使左式為零。"], "medium"),
    make(5, "長方形長為 x＋2、寬為 x，面積 15 平方公分；若 x 為正數，x 為何？", {"A": "2", "B": "3", "C": "5", "D": "−5"}, "B", "x(x＋2)＝15，整理為 x²＋2x−15＝(x＋5)(x−3)＝0；長度為正，取 x＝3。", "把面積轉成二次方程式，求出兩根後依長度正值篩選。", ["建立 x(x＋2)＝15。", "整理為 x²＋2x−15＝0。", "分解為 (x＋5)(x−3)＝0。", "得到 −5 或 3，排除負的長度。", "選 B，3×5＝15。"], "medium"),
    make(6, "兩個連續正整數的乘積為 56，較小者為何？", {"A": "6", "B": "7", "C": "8", "D": "9"}, "B", "令較小者 x，則 x(x＋1)＝56，得 x²＋x−56＝(x＋8)(x−7)＝0；正整數解為 x＝7。", "把連續整數建模成 x、x＋1，解完後用正整數條件選根。", ["令較小正整數為 x，較大為 x＋1。", "建立 x(x＋1)＝56。", "分解為 (x＋8)(x−7)＝0。", "候選根為 −8 與 7。", "選 B，只有 7 符合正整數條件。"], "medium"),
    make(7, "解方程式 (x−3)²＝16，實數解為何？", {"A": "x＝7", "B": "x＝−1", "C": "x＝7 或 x＝−1", "D": "x＝3 或 16"}, "C", "取平方根得 x−3＝4 或 x−3＝−4，因此 x＝7 或 x＝−1。", "平方等式取平方根時列出正負兩種情況，再分別解一次方程式。", ["從 (x−3)²＝16 開始。", "寫成 x−3＝4 或 x−3＝−4。", "第一種得到 x＝7。", "第二種得到 x＝−1。", "選 C，兩值代回平方都等於 16。"], "easy"),
    make(8, "解方程式 3x²−10x＋3＝0，x 為何？", {"A": "1、3", "B": "1／3、3", "C": "−1／3、−3", "D": "3、9"}, "B", "3x²−10x＋3＝(3x−1)(x−3)，所以 x＝1／3 或 x＝3。", "配首項 3x、x 與常數 −1、−3，先確認交叉項為 −10x。", ["找乘積 9、一次項 −10 的配置。", "分解為 (3x−1)(x−3)＝0。", "由 3x−1＝0 得 x＝1／3。", "由 x−3＝0 得 x＝3。", "選 B，兩根代回均成立。"], "hard"),
    make(9, "下列哪個數不是方程式 x²−x−6＝0 的解？", {"A": "−2", "B": "3", "C": "6", "D": "−2 或 3 以外的數"}, "C", "方程式因式分解為 (x−3)(x＋2)＝0，解為 3 與 −2；6 不在根集合中，因此不是解。", "先求完整根集合，再與候選值比較，避免只驗算一個因式。", ["分解 x²−x−6＝(x−3)(x＋2)。", "得到根 x＝3 與 x＝−2。", "逐一對照選項與這兩個根。", "確認 6 不在根集合中。", "選 C，代入 6 得 36−6−6＝24，不為 0。"], "hard"),
    make(10, "正方形面積比原來增加 21 平方公分，邊長由 x 增加為 x＋3；若原邊長為正數，x 為何？", {"A": "2", "B": "3", "C": "4", "D": "5"}, "A", "(x＋3)²−x²＝21，化簡 6x＋9＝21，得 x＝2，因此選 A。", "先用面積差建立式子，再化簡並檢查題目選項對應。", ["建立 (x＋3)²−x²＝21。", "展開並消去 x²，得 6x＋9＝21。", "兩邊同減 9 得 6x＝12。", "解得 x＝2。", "選 A，代回面積差為 25−4＝21。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

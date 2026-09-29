import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-3"
KG = "kg-math-content-a-8-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "addition, subtraction, multiplication, and division of polynomials with standard-form simplification", "observedPattern": "公立學校公開數學試題常要求同類項整理、括號分配、單項式乘除多項式與運算順序判斷；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-8-3-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": key, "text": value} for key, value in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供多項式四則運算、括號分配與標準形式整理能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的多項式運算能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "化簡 (3x²＋2x−1)＋(x²−5x＋4)，結果為何？", {"A": "4x²−3x＋3", "B": "4x²＋7x＋3", "C": "2x²−3x−5", "D": "3x²＋x＋3"}, "A", "合併同類項：3x²＋x²＝4x²、2x−5x＝−3x、−1＋4＝3。", "先去除括號，再按次數分組合併同類項。", ["把兩個括號前的加號保留各項符號。", "合併二次項 3x²＋x²。", "合併一次項 2x−5x。", "合併常數 −1＋4。", "選 A，依降冪排列完成。"], "easy"),
    make(2, "化簡 (5a²−3a＋2)−(2a²＋a−6)，結果為何？", {"A": "3a²−4a＋8", "B": "3a²−2a−4", "C": "7a²−2a＋8", "D": "7a²−4a−4"}, "A", "減去第二括號要改變其中每項符號，得 5a²−3a＋2−2a²−a＋6＝3a²−4a＋8。", "先將減號分配進整個括號，再合併同類項。", ["把第二個括號前的減號分配成 −2a²−a＋6。", "合併二次項 5a²−2a²。", "合併一次項 −3a−a。", "合併常數 2＋6。", "選 A，回查每一項符號都已翻轉。"], "medium"),
    make(3, "化簡 4(2y²−y＋3)，結果為何？", {"A": "8y²−4y＋12", "B": "8y²−y＋3", "C": "6y²−4y＋7", "D": "8y²＋4y＋12"}, "A", "用分配律將 4 乘入每一項：8y²−4y＋12。", "將單項式係數逐項分配，不只乘第一項。", ["把 4 看成括號外公因數。", "計算 4×2y²＝8y²。", "計算 4×(−y)＝−4y。", "計算 4×3＝12。", "選 A，確認三項都乘到 4。"], "easy"),
    make(4, "化簡 −3x(2x²−x＋4)，結果為何？", {"A": "−6x³＋3x²−12x", "B": "−6x³−3x²−12x", "C": "6x³−3x²＋12x", "D": "−6x²＋3x−12"}, "A", "−3x 逐項相乘得 −6x³、＋3x²、−12x。", "同時處理係數、字母次方與正負號，逐項相乘避免漏項。", ["計算 −3x×2x²＝−6x³。", "計算 −3x×(−x)＝＋3x²。", "計算 −3x×4＝−12x。", "依次數由高到低排列。", "選 A，檢查負負得正的中間項。"], "medium"),
    make(5, "化簡 (x＋2)(x²−3x＋4)，結果為何？", {"A": "x³−x²−2x＋8", "B": "x³＋5x²＋x＋8", "C": "x³−3x²＋4x＋2", "D": "x³−x²＋4x＋8"}, "A", "x 乘第一括號得到 x³−3x²＋4x，2 乘得到 2x²−6x＋8，合併為 x³−x²−2x＋8。", "分別用括號中的每一項相乘，再按次數合併。", ["用 x 乘第二括號得到 x³−3x²＋4x。", "用 2 乘第二括號得到 2x²−6x＋8。", "合併二次項 −3x²＋2x²。", "合併一次項 4x−6x。", "選 A，保留三次、二次、一次與常數項。"], "hard"),
    make(6, "化簡 (6m³−9m²＋3m)÷3m，結果為何？", {"A": "2m²−3m＋1", "B": "2m³−3m²＋m", "C": "2m²−3m", "D": "6m²−9m＋3"}, "A", "將每一項除以 3m：6m³÷3m＝2m²、−9m²÷3m＝−3m、3m÷3m＝1。", "對多項式每一項分別除以單項式，係數與次方各自相除。", ["確認除式 3m 可分配到每一項。", "計算 6m³÷3m＝2m²。", "計算 −9m²÷3m＝−3m。", "計算 3m÷3m＝1。", "選 A，按降冪整理。"], "medium"),
    make(7, "若 P＝2x²−x＋3、Q＝x²＋4x−1，則 P＋Q 為何？", {"A": "3x²＋3x＋2", "B": "x²＋3x＋4", "C": "3x²−5x＋4", "D": "2x²＋3x＋2"}, "A", "逐項相加：2x²＋x²＝3x²、−x＋4x＝3x、3−1＝2。", "把多項式視為整體後按同次項相加，保持每個係數。", ["將 P 與 Q 的同次項對齊。", "合併二次項得到 3x²。", "合併一次項得到 3x。", "合併常數得到 2。", "選 A，完成 P＋Q。"], "easy"),
    make(8, "化簡 2(x²−3x)−[x²−(x−4)]，結果為何？", {"A": "x²−5x−4", "B": "x²−5x＋4", "C": "3x²−7x−4", "D": "x²＋x＋4"}, "A", "先得 2x²−6x；方括號內 x²−x＋4，減去後為 −x²＋x−4，合併得 x²−5x−4。", "由內而外處理括號，再分配外層減號，最後合併同類項。", ["展開第一部分得 2x²−6x。", "先化簡方括號 x²−(x−4)＝x²−x＋4。", "將方括號前負號分配成 −x²＋x−4。", "合併得到 x²−5x−4。", "選 A，逐層回代檢查括號符號。"], "hard"),
    make(9, "若長方形長為 2x＋1、寬為 x−2，則其周長的多項式為何？", {"A": "6x−2", "B": "6x＋2", "C": "2x²−x−2", "D": "4x²＋2x−4"}, "A", "周長＝2[(2x＋1)＋(x−2)]＝2(3x−1)＝6x−2。", "先合併長寬得到半周長，再乘 2，避免把周長誤算成面積。", ["寫出周長公式 2(長＋寬)。", "代入得到 2[(2x＋1)＋(x−2)]。", "括號內合併為 3x−1。", "乘以 2 得 6x−2。", "選 A，確認結果是一次多項式。"], "medium"),
    make(10, "若 x＝2，則多項式 (x²＋3x−1)−2(x−1) 的值為何？", {"A": "5", "B": "6", "C": "7", "D": "8"}, "C", "先代入或化簡：4＋6−1−2(1)＝9−2＝7，因此答案為 7。", "可先處理括號與運算順序，再代入數值做最後核對。", ["把 x＝2 代入原式。", "計算 x²＋3x−1＝4＋6−1＝9。", "計算 2(x−1)＝2(1)＝2。", "用 9−2 得 7。", "選 C，確認代入與減法順序一致。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

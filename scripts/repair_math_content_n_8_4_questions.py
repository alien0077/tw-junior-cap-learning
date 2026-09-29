import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-8-4"
KG = "kg-math-content-n-8-4"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "arithmetic sequences, common differences, explicit terms, finding terms and positions, and contextual patterns", "observedPattern": "公立學校公開數學試題常要求辨認等差數列、公差、首項與通項，計算指定項或反推項次，並將固定增減情境建成等差數列；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-8-4-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供等差數列、公差、通項與情境應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的等差數列方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "等差數列 7、11、15、19、…… 的公差是多少？", {"A": "3", "B": "4", "C": "5", "D": "6"}, "B", "相鄰兩項相減 11−7＝4，公差為 4，選 B。", "以後項減前項並檢查多組相鄰項是否相同。", ["取第 2 項減第 1 項：11−7＝4。", "檢查第 3、2 項：15−11＝4。", "再檢查 19−15＝4。", "確認固定差為 4。", "選 B，判定這是等差數列。"], "easy"),
    make(2, "等差數列首項為 5，公差為 3，第 6 項是多少？", {"A": "17", "B": "18", "C": "20", "D": "23"}, "C", "a₆＝5＋(6−1)×3＝5＋15＝20，所以選 C。", "使用 aₙ＝a₁＋(n−1)d，注意公差只走 n−1 次。", ["找出 a₁＝5、d＝3、n＝6。", "代入公式 aₙ＝a₁＋(n−1)d。", "計算 (6−1)×3＝15。", "加上首項 5 得 a₆＝20。", "選 C，逐項列出 5、8、11、14、17、20 驗證。"], "medium"),
    make(3, "等差數列 18、14、10、6、…… 的公差是多少？", {"A": "−4", "B": "−3", "C": "3", "D": "4"}, "A", "14−18＝−4，且後續相鄰差也為 −4，因此選 A。", "保留相減順序『後項減前項』，負公差表示數列遞減。", ["計算第二項減第一項 14−18。", "得到 −4。", "檢查 10−14＝−4。", "確認每項向下減 4。", "選 A，避免只取差的絕對值。"], "easy"),
    make(4, "若等差數列 aₙ＝4n−1，a₇ 為何？", {"A": "23", "B": "27", "C": "28", "D": "31"}, "B", "a₇＝4×7−1＝28−1＝27，所以選 B。", "通項已給定，將指定項次直接代入 n 並依運算順序計算。", ["設定 n＝7。", "代入 aₙ＝4n−1。", "計算 4×7＝28。", "減去 1 得 27。", "選 B，確認下標與代入數值一致。"], "easy"),
    make(5, "等差數列首項為 9、公差為 2，哪一項等於 25？", {"A": "第 7 項", "B": "第 8 項", "C": "第 9 項", "D": "第 10 項"}, "C", "9＋(n−1)×2＝25，得 2(n−1)＝16、n−1＝8、n＝9，所以選 C。", "將指定數值代入等差通項，解一次方程式找項次。", ["建立 9＋(n−1)×2＝25。", "兩邊同減 9，得 2(n−1)＝16。", "兩邊除以 2，得 n−1＝8。", "解得 n＝9。", "選 C，代入 9＋8×2＝25。"], "medium"),
    make(6, "數列 3、8、13、18、…… 的第 10 項為何？", {"A": "43", "B": "48", "C": "53", "D": "58"}, "B", "首項 3、公差 5，a₁₀＝3＋9×5＝48，所以選 B。", "先找首項與公差，再用 n−1 次公差求指定項。", ["辨認 a₁＝3、d＝5、n＝10。", "計算需要增加的次數 n−1＝9。", "計算 9×5＝45。", "加上首項 3 得 48。", "選 B，確認選項與計算結果一致。"], "medium"),
    make(7, "若等差數列第 3 項為 12、第 7 項為 28，公差是多少？", {"A": "3", "B": "4", "C": "5", "D": "6"}, "B", "第 7 項比第 3 項多 4 個公差，28−12＝16，d＝16÷4＝4，選 B。", "兩項之間相隔 n₂−n₁ 次公差，用項差除以項次差。", ["計算項次差 7−3＝4。", "計算項值差 28−12＝16。", "建立 4d＝16。", "解得 d＝4。", "選 B，從第 3 項連加四次 4 到 28。"], "medium"),
    make(8, "某劇場第一排有 12 個座位，每往後一排增加 4 個座位。第 9 排有幾個座位？", {"A": "40", "B": "44", "C": "48", "D": "52"}, "B", "a₉＝12＋(9−1)×4＝12＋32＝44，所以選 B。", "把排數視為項次，固定增加量為公差，套用等差通項。", ["設定首項 a₁＝12、公差 d＝4。", "第 9 排需增加 9−1＝8 次。", "計算 8×4＝32。", "加上第一排 12 得 44。", "選 B，確認不是增加 9 次。"], "medium"),
    make(9, "等差數列首項為 −2，公差為 5，哪一項等於 28？", {"A": "第 5 項", "B": "第 6 項", "C": "第 7 項", "D": "第 8 項"}, "C", "−2＋(n−1)×5＝28，得 5(n−1)＝30、n＝7，所以選 C。", "由通項建立方程，解出整數項次後再回代檢查。", ["建立 −2＋(n−1)×5＝28。", "兩邊同加 2 得 5(n−1)＝30。", "除以 5 得 n−1＝6。", "解得 n＝7。", "選 C，計算第 7 項 −2＋6×5＝28。"], "hard"),
    make(10, "若三個連續的等差數列項為 x−3、x、x＋3，且第二項為 10，這三項的和是多少？", {"A": "27", "B": "30", "C": "33", "D": "36"}, "B", "第二項 x＝10，三項為 7、10、13，和為 30，所以選 B。", "先使用中間項的已知值求另外兩項，再相加；三項對稱時總和也等於 3x。", ["由第二項得到 x＝10。", "計算第一項 x−3＝7。", "計算第三項 x＋3＝13。", "相加 7＋10＋13＝30。", "選 B，或用 3×中間項＝3×10 驗證。"], "easy"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

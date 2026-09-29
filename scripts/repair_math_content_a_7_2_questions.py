import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-2"
KG = "kg-math-content-a-7-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "一元一次方程式的等量關係、移項、括號、唯一解、無解與恆等式及文字情境", "observedPattern": "公立學校公開數學試題常以等量平衡、代入驗算、括號方程式、文字情境及解的個數考查一元一次方程式理解；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-7-2-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一元一次方程式能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的一元一次方程式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "方程式 3x−4＝11 的解為何？", {"A": "3", "B": "5", "C": "7", "D": "15"}, "B", "兩邊同加 4 得 3x＝15，再同除以 3 得 x＝5，選 B。", "先消去常數項，再消去 x 的係數，最後代回驗算。", ["原式為 3x−4＝11。", "兩邊同加 4 得 3x＝15。", "兩邊同除以 3。", "得到 x＝5。", "代回 3×5−4＝11，選 B。"], "easy"),
    make(2, "若 x＝−2，下列哪一個方程式的左右兩邊會相等？", {"A": "5x＋3＝−7", "B": "3x−1＝−4", "C": "2x＋6＝1", "D": "x＋5＝−5"}, "A", "代入 x＝−2：5(−2)＋3＝−7，左右相等，所以選 A。", "把已知值逐項代入左右兩邊，直接比較計算結果。", ["將 x＝−2 代入 A。", "左邊 5(−2)＋3＝−7。", "右邊本來就是 −7。", "確認左右兩邊相等。", "選 A。"], "easy"),
    make(3, "在方程式 4x−7＝9 中，等號表示什麼？", {"A": "左邊一定比右邊大", "B": "x 必須是正數", "C": "等號兩側代表相同的值", "D": "兩邊可以任意刪除同一項"}, "C", "方程式的等號表示左右兩個式子的值相等，選 C；它本身不直接指定 x 的正負。", "先掌握等號的等量意義，再區分解方程的合法操作。", ["辨認等號左右各是一個代數式。", "等號宣告兩個代數式值相同。", "這不等於先知道 x 的正負。", "移項等操作仍須維持等量關係。", "選 C。"], "easy"),
    make(4, "解方程式 4y＋7＝23，y 應為何值？", {"A": "3", "B": "4", "C": "5", "D": "7"}, "B", "兩邊同減 7 得 4y＝16，再除以 4 得 y＝4，選 B。", "依逆運算順序隔離未知數，並以代入確認答案。", ["原式為 4y＋7＝23。", "兩邊同減 7 得 4y＝16。", "兩邊同除以 4。", "解得 y＝4。", "代回 4×4＋7＝23，選 B。"], "easy"),
    make(5, "小芸原有一些貼紙，送給同學 8 張後剩下 20 張。若原有 x 張，哪個方程式正確？", {"A": "x＋8＝20", "B": "x−8＝20", "C": "8x＝20", "D": "x＋20＝8"}, "B", "原有數量減去送出的 8 張等於剩下 20 張，因此 x−8＝20，選 B。", "先用事件順序畫出『原有→送出→剩下』，再把變化翻成運算。", ["把原有數量設為 x。", "送出 8 張代表數量減少 8。", "剩下的數量是 x−8。", "題目給剩下 20 張，列 x−8＝20。", "選 B。"], "easy"),
    make(6, "若 3(x−2)＝15，則 x 的值為何？", {"A": "3", "B": "5", "C": "6", "D": "7"}, "D", "兩邊同除以 3 得 x−2＝5，再同加 2 得 x＝7，選 D。", "先處理括號外的乘法，再使用加法逆運算。", ["原式為 3(x−2)＝15。", "兩邊同除以 3 得 x−2＝5。", "兩邊同加 2。", "得到 x＝7。", "代回 3(7−2)＝15，選 D。"], "medium"),
    make(7, "解方程式 5x＋2＝2x＋14，x 為何？", {"A": "2", "B": "4", "C": "6", "D": "8"}, "B", "兩邊同減 2x 得 3x＋2＝14，再減 2 得 3x＝12，故 x＝4，選 B。", "把未知項集中到一邊、常數集中到另一邊，避免移項符號錯誤。", ["兩邊同減 2x 得 3x＋2＝14。", "兩邊同減 2 得 3x＝12。", "兩邊同除以 3。", "解得 x＝4。", "代回左右皆為 22，選 B。"], "medium"),
    make(8, "方程式 2x＋6＝2x＋6 有幾個解？", {"A": "沒有解", "B": "只有 x＝0", "C": "所有數都是解", "D": "只有 x＝6"}, "C", "兩邊同減 2x 後得到 6＝6，成為恆等式；任何 x 代入都成立，所以有無限多個解，選 C。", "消去相同的未知項後，觀察剩下的是恆真、矛盾或可解等式。", ["兩邊同減 2x。", "得到 6＝6。", "這個等式不再限制 x。", "任意數值代入都能保持等號。", "選 C。"], "medium"),
    make(9, "方程式 4x＋1＝4x−3 有何結論？", {"A": "沒有解", "B": "x＝1", "C": "所有數都是解", "D": "x＝−1"}, "A", "兩邊同減 4x 後得到 1＝−3，矛盾，因此沒有任何 x 能成立，選 A。", "先消去相同的未知項；若留下矛盾的常數等式，即判定無解。", ["兩邊同減 4x。", "剩下 1＝−3。", "這是永遠不成立的矛盾。", "所以不存在能滿足原方程式的 x。", "選 A。"], "medium"),
    make(10, "一個長方形周長為 34 公分，寬為 6 公分，長為 x 公分。求 x 的方程式與長度。", {"A": "x＋6＝34，x＝28", "B": "2x＋6＝34，x＝14", "C": "x＋12＝34，x＝22", "D": "2(x＋6)＝34，x＝11"}, "D", "周長為 2(長＋寬)，所以 2(x＋6)＝34；除以 2 得 x＋6＝17，再減 6 得 x＝11，選 D。", "先建模寫出整個周長，再解方程並檢查 2(11＋6)＝34。", ["寫出長方形周長公式 2(長＋寬)。", "代入長 x、寬 6 得 2(x＋6)＝34。", "兩邊除以 2 得 x＋6＝17。", "兩邊減 6 得 x＝11 公分。", "代回周長確認後選 D。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

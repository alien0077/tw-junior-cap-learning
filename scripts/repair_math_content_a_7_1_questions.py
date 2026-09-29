import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-1"
KG = "kg-math-content-a-7-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "代數式中的變數、係數、常數項、同類項、代入值、分配律、方程式與情境表示", "observedPattern": "公立學校公開數學試題常以符號辨識、同類項合併、分配律、代入求值及生活情境建立代數式考查符號理解；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-7-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供代數符號能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的代數符號能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "在代數式 3x＋5 中，哪一個符號可以代表不同的數值？", {"A": "x", "B": "3", "C": "5", "D": "＋"}, "A", "x 是可代入不同數值的變數；3 是係數、5 是常數項，選 A。", "先分類符號的角色，再判斷哪個符號不是固定數字或運算記號。", ["觀察代數式 3x＋5。", "辨認 x 是字母符號。", "係數 3 與常數 5 是固定數字。", "加號是運算符號而非數值。", "選 A。"], "easy"),
    make(2, "在代數式 −7a＋4 中，a 的係數是多少？", {"A": "−7", "B": "7", "C": "4", "D": "−a"}, "A", "a 前面的乘數是 −7，因此 a 的係數為 −7，選 A。", "把含 a 的項視為『係數×a』，注意負號也屬於係數。", ["找出含 a 的項 −7a。", "將它寫成 (−7)×a。", "辨認 a 前的乘數。", "得到係數為 −7。", "選 A。"], "easy"),
    make(3, "在代數式 2b−9 中，常數項是哪一個？", {"A": "2", "B": "b", "C": "−9", "D": "2b"}, "C", "不含字母的項是常數項；2b−9 中常數項為 −9，選 C。", "先把各項分開，再找不含變數的項，保留其正負號。", ["以加減號分出 2b 與 −9。", "檢查各項是否含有 b。", "−9 不含字母。", "所以 −9 是常數項。", "選 C。"], "easy"),
    make(4, "化簡 5p＋2q−3p 後，結果為何？", {"A": "2p＋2q", "B": "8p＋2q", "C": "2p−q", "D": "5p−p＋2q"}, "A", "5p 與 −3p 是同類項，合併得 2p，並保留 2q，所以結果為 2p＋2q，選 A。", "只合併變數與次方完全相同的同類項，q 項不能與 p 項相加。", ["找出 p 的同類項 5p、−3p。", "計算係數 5＋(−3)＝2。", "保留不相同的 q 項 2q。", "寫成 2p＋2q。", "選 A。"], "medium"),
    make(5, "長方形長為 x＋4 公分、寬為 x＋1 公分，用 x 表示周長為何？", {"A": "2x＋5", "B": "4x＋10", "C": "x²＋5x＋4", "D": "4x＋5"}, "B", "周長＝2[(x＋4)＋(x＋1)]＝2(2x＋5)＝4x＋10 公分，選 B。", "先把長與寬相加，再乘二；括號能避免漏乘常數。", ["列出周長公式 2(長＋寬)。", "代入得到 2[(x＋4)＋(x＋1)]。", "括號內合併為 2x＋5。", "乘以 2 得 4x＋10 公分。", "選 B。"], "medium"),
    make(6, "若 x＝−3，則 2x²＋1 的值是多少？", {"A": "−17", "B": "−5", "C": "19", "D": "37"}, "C", "先平方再乘 2：2(−3)²＋1＝2×9＋1＝19，選 C。", "代入負數時用括號，並遵守先乘方、再乘法、後加法的順序。", ["以 (−3) 代入 x。", "計算 (−3)²＝9。", "乘以係數 2 得 18。", "加上 1 得 19。", "選 C。"], "medium"),
    make(7, "化簡 6r−(2r−5) 後，結果為何？", {"A": "4r−5", "B": "4r＋5", "C": "8r−5", "D": "8r＋5"}, "B", "負號分配後 6r−2r＋5＝4r＋5，所以選 B。", "括號前的負號要同時改變括號內每一項的符號。", ["確認括號前有負號。", "將 −(2r−5) 展開為 −2r＋5。", "把原式寫成 6r−2r＋5。", "合併同類項得到 4r＋5。", "選 B。"], "medium"),
    make(8, "下列哪一個是含有等號、可用來求未知數的方程式？", {"A": "4x＋1", "B": "4x＋1＝13", "C": "4＋1＝5", "D": "x＞2"}, "B", "方程式是含有未知數且以等號連結兩個式子的敘述，4x＋1＝13 符合，選 B。", "同時檢查是否有未知數與等號；只有數字等式不需解未知數。", ["查看每個選項是否含有字母未知數。", "再檢查是否有等號連結兩邊。", "B 同時具備 x 與等號。", "它可透過運算求出 x。", "選 B。"], "easy"),
    make(9, "下列哪一式與 4(2q−3) 等價？", {"A": "8q−3", "B": "8q−12", "C": "4q−12", "D": "8q＋12"}, "B", "用分配律將 4 乘入括號：4×2q−4×3＝8q−12，選 B。", "把括號外因數分別乘上括號內每一項，並保留第二項的負號。", ["將 4 分配給 2q 與 −3。", "計算 4×2q＝8q。", "計算 4×(−3)＝−12。", "合併成 8q−12。", "選 B。"], "medium"),
    make(10, "影印店每張彩色列印 18 元，另收一次設定費 35 元。列印 n 張的總費用可用哪一式表示？若 n＝4，費用是多少？", {"A": "18n＋35；107 元", "B": "35n＋18；158 元", "C": "18(n＋35)；702 元", "D": "53n；212 元"}, "A", "每張費用是 18n，加上一次性的 35 元得 18n＋35；n＝4 時為 72＋35＝107 元，選 A。", "先分辨按張數變動的費用與固定費，再代入檢查情境。", ["按張數計算變動費 18n。", "把一次性設定費 35 加上去。", "得到總費用 18n＋35。", "代入 n＝4，計算 72＋35＝107。", "選 A。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

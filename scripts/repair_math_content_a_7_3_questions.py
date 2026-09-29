import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-3"
KG = "kg-math-content-a-7-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "一元一次方程式的移項、括號、分數與小數係數、未知數兩側及生活應用", "observedPattern": "公立學校公開數學試題常以多步解方程、分配律、分數／小數係數和周長、費用情境考查等量推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-a-7-3-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一元一次方程式解法與應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的方程式解法能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "解方程式 4x＋7＝31，x 為何？", {"A": "4", "B": "6", "C": "8", "D": "10"}, "B", "兩邊同減 7 得 4x＝24，再除以 4 得 x＝6，選 B。", "先移除常數，再除以未知數係數，最後代回驗算。", ["原式為 4x＋7＝31。", "兩邊同減 7 得 4x＝24。", "兩邊同除以 4。", "得到 x＝6。", "代回 4×6＋7＝31，選 B。"], "easy"),
    make(2, "解方程式 9−2x＝−5，x 為何？", {"A": "−7", "B": "−2", "C": "2", "D": "7"}, "D", "兩邊同減 9 得 −2x＝−14，再除以 −2 得 x＝7，選 D。", "移項後要同時留意負係數，最後除以負數時符號會改變。", ["原式為 9−2x＝−5。", "兩邊同減 9 得 −2x＝−14。", "兩邊同除以 −2。", "解得 x＝7。", "代回 9−14＝−5，選 D。"], "medium"),
    make(3, "解方程式 (x＋5)/3＝7，x 為何？", {"A": "12", "B": "14", "C": "16", "D": "21"}, "C", "兩邊同乘 3 得 x＋5＝21，再同減 5 得 x＝16，選 C。", "先消除分母，再處理加法常數，避免把分母只乘到 x。", ["辨認整個 x＋5 除以 3。", "兩邊同乘 3 得 x＋5＝21。", "兩邊同減 5。", "得到 x＝16。", "代回 (16＋5)/3＝7，選 C。"], "medium"),
    make(4, "解方程式 6x−5＝3x＋13，x 為何？", {"A": "4", "B": "6", "C": "8", "D": "10"}, "B", "兩邊同減 3x 得 3x−5＝13，再加 5 得 3x＝18，故 x＝6，選 B。", "先將未知項集中，接著集中常數，保持等號兩邊同步操作。", ["兩邊同減 3x 得 3x−5＝13。", "兩邊同加 5 得 3x＝18。", "兩邊同除以 3。", "解得 x＝6。", "代回左右皆為 31，選 B。"], "medium"),
    make(5, "解方程式 2(3x−4)＝16，x 為何？", {"A": "4", "B": "6", "C": "8", "D": "10"}, "A", "先除以 2 得 3x−4＝8，再加 4 得 3x＝12，故 x＝4，選 A。", "可先消除括號外乘數，再依序處理常數與係數。", ["兩邊同除以 2。", "得到 3x−4＝8。", "兩邊同加 4 得 3x＝12。", "兩邊同除以 3 得 x＝4。", "代回 2(12−4)＝16，選 A。"], "medium"),
    make(6, "解方程式 0.4x＋2＝6，x 為何？", {"A": "5", "B": "8", "C": "10", "D": "15"}, "C", "兩邊同減 2 得 0.4x＝4，再除以 0.4 得 x＝10，選 C。", "先隔離小數係數項，也可把 0.4 視為 4/10 來檢查。", ["原式為 0.4x＋2＝6。", "兩邊同減 2 得 0.4x＝4。", "兩邊同除以 0.4。", "計算 x＝4÷0.4＝10。", "代回 0.4×10＋2＝6，選 C。"], "medium"),
    make(7, "一個長方形周長為 30 公分，寬為 5 公分，長為 x 公分。求 x 的解。", {"A": "5", "B": "8", "C": "10", "D": "15"}, "C", "列式 2(x＋5)＝30，除以 2 得 x＋5＝15，再減 5 得 x＝10，選 C。", "先用周長建立方程，再解出長並檢查長度為正。", ["周長公式為 2(長＋寬)。", "代入得 2(x＋5)＝30。", "兩邊除以 2 得 x＋5＝15。", "兩邊減 5 得 x＝10 公分。", "檢查 2(10＋5)＝30，選 C。"], "medium"),
    make(8, "解方程式 x/4−1＝5，x 為何？", {"A": "24", "B": "20", "C": "16", "D": "12"}, "A", "兩邊同加 1 得 x/4＝6，再同乘 4 得 x＝24，選 A。", "先移除分數項外的常數，再乘回分母。", ["原式為 x/4−1＝5。", "兩邊同加 1 得 x/4＝6。", "兩邊同乘 4。", "得到 x＝24。", "代回 24/4−1＝5，選 A。"], "easy"),
    make(9, "某計程車起跳費 40 元，每公里加收 15 元。若車程 x 公里、總費用 130 元，x 為何？", {"A": "4", "B": "6", "C": "8", "D": "10"}, "B", "費用方程式為 40＋15x＝130；減 40 得 15x＝90，故 x＝6，選 B。", "把固定費與按里程變動費分開，再由總費用反推里程。", ["固定起跳費為 40 元。", "里程費為 15x 元。", "列式 40＋15x＝130。", "減 40 得 15x＝90，除以 15 得 x＝6。", "代回總費用確認後選 B。"], "medium"),
    make(10, "解方程式 3x−2(x＋1)＝14，x 為何？", {"A": "12", "B": "14", "C": "16", "D": "18"}, "C", "先展開得 3x−2x−2＝14，即 x−2＝14，再加 2 得 x＝16，選 C。", "先用分配律處理負號括號，再合併同類項。", ["將 −2 分配到 x＋1，得 −2x−2。", "原式化為 3x−2x−2＝14。", "合併同類項得 x−2＝14。", "兩邊同加 2 得 x＝16。", "代回 48−2×17＝14，選 C。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

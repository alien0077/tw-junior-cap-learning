import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-3"
KG = "kg-math-performance-a-iv-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "一元一次不等式的等量操作、負數反向、數線端點、雙重限制與生活情境；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常要求將條件轉成不等式，注意乘除負數時方向改變，並把解集轉成數線或整數情境；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-a-iv-3-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供一元一次不等式能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的不等式解題方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "解不等式 3x+2<14，解集為何？", {"A":"x>4", "B":"x≤4", "C":"x≥4", "D":"x<4"}, "D", "兩邊減 2 得 3x<12，再除以正數 3，得到 x<4，因此選 D。", "先移除常數，再除以正係數；正數除法不會改變方向。", ["寫下 3x+2<14。", "兩邊同減 2，得 3x<12。", "兩邊同除以 3，方向維持不變。", "得到 x<4。", "所以選 D。"], "easy"),
make(2, "解不等式 -2x+5≥11，解集為何？", {"A":"x≥-3", "B":"x≤3", "C":"x≤-3", "D":"x≥3"}, "C", "兩邊減 5 得 -2x≥6，再除以負數 -2，方向反轉為 x≤-3，正確答案為 C。", "特別標記最後除以負數的步驟，避免忘記反轉不等號。", ["原式為 -2x+5≥11。", "兩邊同減 5，得 -2x≥6。", "兩邊同除以 -2。", "因除以負數，不等號反向，得 x≤-3。", "所以選 C。"], "medium"),
make(3, "解不等式 4-3x<10，解集為何？", {"A":"x>-2", "B":"x<-2", "C":"x≥-2", "D":"x≤-2"}, "A", "兩邊減 4 得 -3x<6，再除以負數 -3，方向反轉為 x>-2，所以選 A。", "先把常數移到右側，再清楚記住負係數造成的方向反轉。", ["由 4-3x<10 開始。", "兩邊同減 4，得 -3x<6。", "兩邊同除以 -3。", "除以負數使方向反轉，得到 x>-2。", "所以選 A。"], "medium"),
make(4, "雙重不等式 2≤x+3<7 的解集為何？", {"A":"-1<x≤4", "B":"-1≤x<4", "C":"1≤x<10", "D":"-5≤x<5"}, "B", "三部分同減 3，得到 -1≤x<4；左端包含 -1、右端不包含 4，正確答案為 B。", "對雙重不等式三段同時做同一運算，並分別保留端點的等號資訊。", ["寫下 2≤x+3<7。", "三段同時減 3。", "左側成為 -1≤x。", "右側成為 x<4。", "合併為 -1≤x<4，選 B。"], "medium"),
make(5, "入場費 5 元，每份點心 8 元，身上有 45 元，最多可買幾份？", {"A":"4 份", "B":"5 份", "C":"6 份", "D":"7 份"}, "B", "設份數為 x，5+8x≤45，得 8x≤40、x≤5；最多買 5 份，選 B。", "先把『不超過預算』寫成小於等於，再注意份數必須是非負整數。", ["設點心份數為 x。", "總花費為 5+8x，且不得超過 45。", "列出 5+8x≤45。", "解得 8x≤40，所以 x≤5。", "最大整數份數為 5，選 B。"], "medium"),
make(6, "若 x 為整數且 -2<x≤3，符合條件的 x 共有幾個？", {"A":"4 個", "B":"5 個", "C":"6 個", "D":"7 個"}, "B", "整數解為 -1、0、1、2、3，共 5 個，因此正確答案為 B。", "先列出嚴格大於 -2 的第一個整數，再列到包含 3 的端點。", ["下界 -2 不包含，所以從 -1 開始。", "依序列出 -1、0、1、2、3。", "上界 3 有等號，因此 3 要保留。", "逐一計數得到 5 個。", "所以選 B。"], "easy"),
make(7, "不等式 x≤2 在數線上的表示方式為何？", {"A":"2 實心點，向右延伸", "B":"2 空心點，向右延伸", "C":"2 實心點，向左延伸", "D":"2 空心點，向左延伸"}, "C", "≤ 包含 2，所以在 2 畫實心點；小於 2 的數在左側，應向左延伸，選 C。", "先看等號決定實心或空心，再看大小方向決定左右延伸。", ["辨認 ≤ 含有等號。", "含等號代表端點 2 是解，畫實心點。", "x 小於 2 的數位於數線左方。", "因此從 2 向左延伸。", "所以選 C。"], "easy"),
make(8, "解不等式 0.5x-1>2，解集為何？", {"A":"x>6", "B":"x≥6", "C":"x<6", "D":"x≤6"}, "A", "兩邊加 1 得 0.5x>3，再除以正數 0.5 得 x>6，正確答案為 A。", "將小數係數視為正數，移項後除以 0.5 並維持方向。", ["原式為 0.5x-1>2。", "兩邊同加 1，得 0.5x>3。", "0.5 是正數，所以除法不反向。", "計算 3÷0.5=6，得到 x>6。", "所以選 A。"], "medium"),
make(9, "x 為整數，且 3x-1≥8、2x+4<14，符合條件的 x 有幾個？", {"A":"1 個", "B":"2 個", "C":"3 個", "D":"4 個"}, "B", "第一式得 x≥3，第二式得 x<5；整數解為 3、4，共 2 個，所以選 B。", "分別解兩個限制，再取交集，最後只數符合的整數。", ["由 3x-1≥8 得 3x≥9，所以 x≥3。", "由 2x+4<14 得 2x<10，所以 x<5。", "合併限制為 3≤x<5。", "整數只能是 3 與 4。", "共有 2 個，選 B。"], "hard"),
make(10, "若 -3x≤12，解出 x 時應得到哪一個結果？", {"A":"x≤-4", "B":"x≤4", "C":"x≥4", "D":"x≥-4"}, "D", "兩邊同除以負數 -3，不等號反向，得到 x≥-4，因此正確答案為 D。", "把負數除法視為本題關鍵，先寫出反向，再計算數值。", ["原式為 -3x≤12。", "兩邊同除以 -3。", "除以負數使 ≤ 反向成 ≥。", "計算 12÷(-3)=-4，得到 x≥-4。", "所以選 D。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

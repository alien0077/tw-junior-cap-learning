import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-7-3"
KG = "kg-math-content-s-7-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "垂直、直角、點到直線距離、垂直平分線與等距性質", "observedPattern": "公開學校數學試題常以直角判定、最短距離、垂直平分線與幾何性質考查垂直概念；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-7-3-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供垂直與距離能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的垂直能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "兩條相交直線形成的四個角都是 90°，這兩條直線的關係為何？", {"A":"平行","B":"垂直","C":"重合","D":"對稱"}, "B", "兩條相交直線若形成直角，定義上互相垂直，選 B。", "先確認是否相交，再確認交角是否為 90°。", ["題目說兩線相交。","四個交角都為 90°。","90° 是直角。","相交成直角的兩線稱為垂直線。","選 B。"], "easy"),
make(2, "若直線 l 與直線 m 垂直，下列哪個符號表示正確？", {"A":"l ∥ m","B":"l = m","C":"l ⟂ m","D":"l ≈ m"}, "C", "垂直關係以 ⟂ 表示，因此 l ⟂ m，選 C。", "辨識幾何關係的專用符號，不要把平行符號與垂直符號混用。", ["題目給出的關係是垂直。","垂直的符號是 ⟂。","把兩條直線放入符號兩側。","得到 l ⟂ m。","選 C。"], "easy"),
make(3, "從平面上一點 P 向直線 L 作垂線，垂足為 H。點 P 到直線 L 的距離應如何表示？", {"A":"PH 的長度","B":"PL 的長度","C":"任意斜線段的長度","D":"直線 L 的全長"}, "A", "點到直線的距離定義為點到垂足的垂線段長度，所以是 PH，選 A。", "先找垂足，再取從點到垂足的垂線段，不選斜向連線。", ["確認 P 是直線外的點。","找出垂線與 L 的交點 H。","PH 與 L 垂直。","點到直線距離就是 PH 的長度。","選 A。"], "easy"),
make(4, "在所有連接點 P 與直線 L 上各點的線段中，哪一條最短？", {"A":"與 L 垂直的線段","B":"與 L 平行的線段","C":"任意斜線段","D":"直線 L 本身"}, "A", "從點到直線的垂線段是最短距離，因此與 L 垂直的線段最短，選 A。", "把問題轉成點到直線距離，使用垂線段最短的性質。", ["從 P 連到 L 上不同位置。","斜線段會形成三角形的斜邊。","垂線段是對應直角三角形的直角邊。","斜邊長於直角邊，故垂線段最短。","選 A。"], "medium"),
make(5, "線段 AB 長 10 公分，若直線 m 通過 AB 的中點且垂直 AB，則 m 與 AB 的交點距離 A、B 各是多少？", {"A":"A 為 5 公分，B 為 5 公分","B":"A 為 10 公分，B 為 0 公分","C":"A 為 0 公分，B 為 10 公分","D":"無法判定，因為 m 不一定通過中點"}, "A", "m 通過 AB 的中點，長度 10 被分成兩段相等，每段 5 公分，選 A。", "看到垂直且通過中點，先使用中點把全長平分。", ["AB 全長是 10 公分。","m 通過 AB 的中點。","中點把 AB 分成兩段等長。","10 ÷ 2 = 5。","選 A。"], "easy"),
make(6, "若點 X 在線段 AB 的垂直平分線上，則下列哪個關係一定成立？", {"A":"XA = XB","B":"XA = AB","C":"XB = AB/2","D":"X 一定在 AB 上"}, "A", "垂直平分線上的每一點到線段兩端點等距，因此 XA = XB，選 A。", "利用垂直平分線的等距性質，而不是誤以為 X 必在原線段上。", ["辨認 X 位於 AB 的垂直平分線。","垂直平分線通過 AB 中點且垂直 AB。","其上的點到 A、B 兩端點距離相等。","因此 XA = XB。","選 A。"], "medium"),
make(7, "下列哪個條件足以判斷一條直線是線段 AB 的垂直平分線？", {"A":"只通過 A 點","B":"只與 AB 平行","C":"垂直 AB 且通過 AB 中點","D":"與 AB 交於任意一點"}, "C", "垂直平分線必須同時垂直線段並通過其中點，選 C。", "垂直平分線是兩個條件的合稱，不能只檢查其中一項。", ["列出『垂直』條件。","列出『平分』代表通過中點。","檢查選項 C 同時具備兩條件。","其餘選項各缺少至少一項。","選 C。"], "medium"),
make(8, "兩條直線彼此平行且沒有交點，能否稱為互相垂直？", {"A":"能，因為平行線也可形成直角","B":"不能，垂直線必須相交成直角","C":"能，只要畫得夠長","D":"不能，因為垂直線一定重合"}, "B", "垂直要求兩線相交並形成 90°；平行線沒有交點，不符合定義，選 B。", "同時檢查相交和直角兩個必要條件。", ["垂直的第一條件是兩線相交。","平行線沒有交點。","沒有交點就不能形成交角。","因此不能判定為垂直。","選 B。"], "easy"),
make(9, "三角形 ABC 中，從頂點 A 向對邊 BC 作垂線，垂足為 D。AD 在三角形中稱為什麼？", {"A":"中線","B":"角平分線","C":"高","D":"中垂線"}, "C", "從頂點向對邊（或其延長線）作垂線的線段稱為高，因此 AD 是高，選 C。", "辨認線段的起點、終點與垂直條件，再區分中線、角平分線和高。", ["AD 從頂點 A 出發。","D 位於對邊 BC 上。","AD 與 BC 垂直。","頂點到對邊的垂線段就是三角形的高。","選 C。"], "medium"),
make(10, "小明說：『只要一條線段通過 AB 的中點，就一定是 AB 的垂直平分線。』哪個修正最正確？", {"A":"正確，通過中點就足夠","B":"錯誤，還必須與 AB 垂直","C":"錯誤，還必須與 AB 平行","D":"正確，因為所有中點線都垂直"}, "B", "垂直平分線同時需要通過中點與垂直 AB；只通過中點仍可能斜交，選 B。", "逐項核對定義中的必要條件，避免只抓到『平分』而漏掉『垂直』。", ["記下小明提供的條件：通過中點。","回想垂直平分線還要求與 AB 垂直。","通過中點的斜線不一定垂直 AB。","因此原說法少了一個必要條件。","選 B。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

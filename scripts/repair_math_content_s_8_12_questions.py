import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-12"
KG = "kg-math-content-s-8-12"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "尺規作圖、線段複製、角平分線、垂直平分線、等距點與作圖失敗診斷", "observedPattern": "公開學校數學試題常以作圖步驟、圓規等距性、交點條件及幾何理由考查尺規作圖與推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-12-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供尺規作圖與幾何推理能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的尺規作圖方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "作線段 AB 的垂直平分線，作圖完成後最重要的幾何性質是什麼？", {"A":"線上每一點到 A、B 等距","B":"線上每一點都在 AB 上","C":"線段 AB 被延長兩倍","D":"線一定與 AB 平行"}, "A", "垂直平分線上的每一點到線段兩端點 A、B 等距，選 A。", "先確認作圖目標的性質，再安排圓弧與直線步驟。", ["目標是找所有到 A、B 等距的點。","這些點形成 AB 的垂直平分線。","作圖後直線垂直 AB。","直線上各點到 A、B 距離相等。","選 A。"], "easy"),
make(2, "用圓規作線段 AB 的垂直平分線時，圓規半徑至少應大於 AB 長度的多少？", {"A":"AB 的一半","B":"AB 的兩倍","C":"AB 的三倍","D":"不必有任何限制"}, "A", "要讓以 A、B 為圓心的兩圓弧在上下方相交，半徑需大於 AB/2，選 A。", "從兩圓能否產生交點反推半徑條件。", ["兩圓心距離是 AB。","兩圓半徑相同，設為 r。","要相交需 2r>AB。","因此 r>AB/2。","選 A。"], "medium"),
make(3, "用同一半徑分別以 A、B 為圓心畫弧，為什麼要保留兩個弧的交點？", {"A":"兩個交點可確定一條直線","B":"一個交點就能形成完整直線","C":"交點越多代表半徑越大","D":"交點用來改變 AB 長度"}, "A", "上下兩個交點都到 A、B 等距，連接兩點才能確定垂直平分線，選 A。", "把作圖工具產生的點轉成幾何證據，不能只看單一交點。", ["兩弧交於上方一點。","若只取一點，無法唯一畫出目標直線。","保留另一側交點。","兩個點可決定一條直線。","選 A。"], "easy"),
make(4, "完成兩弧交點 P、Q 後，下一步應如何得到 AB 的垂直平分線？", {"A":"畫直線 PQ","B":"畫直線 AP","C":"把 AB 延長到 P","D":"只畫一個圓"}, "A", "P、Q 都到 A、B 等距，連接 P、Q 的直線就是 AB 的垂直平分線，選 A。", "依交點的共同幾何性質選擇能通過兩交點的直線。", ["確認 P、Q 是兩弧交點。","P、Q 都到 A、B 等距。","等距點的軌跡是 AB 的垂直平分線。","通過兩點畫直線 PQ。","選 A。"], "easy"),
make(5, "若 P 是兩圓弧的交點，且圓弧半徑都為 r，則下列哪組等式成立？", {"A":"PA=PB=r","B":"PA+PB=r","C":"PA=AB=r","D":"PB=AB=2r"}, "A", "P 在以 A、B 為圓心且半徑 r 的兩弧上，因此 PA=r、PB=r，選 A。", "查看 P 分別落在哪兩個圓上，再讀出半徑關係。", ["P 位於以 A 為圓心的圓弧上。","所以 PA 等於該圓半徑 r。","P 也位於以 B 為圓心的圓弧上。","所以 PB 也等於 r。","選 A。"], "easy"),
make(6, "作一個角的角平分線時，從頂點畫弧截兩邊得到 C、D，接著應如何處理？", {"A":"以 C、D 為圓心畫同半徑弧，連接頂點與新交點","B":"只延長其中一邊","C":"量出兩邊長後相減","D":"把角旋轉 90°"}, "A", "以 C、D 為圓心畫同半徑弧取得等距交點，再連接頂點與交點即可得到角平分線，選 A。", "追蹤等距構造：先在兩邊取等距點，再製造同時到兩點等距的點。", ["先以頂點為圓心畫弧取得 C、D。","以 C、D 為圓心畫相同半徑弧。","保留兩弧在角內的交點 E。","連接頂點與 E。","選 A。"], "medium"),
make(7, "若作垂直平分線時兩圓弧沒有交點，最可能的原因是什麼？", {"A":"圓規半徑太小","B":"AB 一定不是線段","C":"交點太多","D":"圓規半徑一定太大"}, "A", "若兩圓心距離為 AB，半徑小於或等於 AB/2 時可能沒有兩個交點，因此半徑太小，選 A。", "用兩圓相交的距離條件診斷作圖失敗。", ["檢查兩圓心 A、B 的距離。","檢查共同半徑 r。","若 2r≤AB，兩弧不會形成兩個交點。","增加圓規半徑使 2r>AB。","選 A。"], "medium"),
make(8, "為什麼只找到一個圓弧交點時，還不能完成垂直平分線？", {"A":"一個點不能唯一決定直線","B":"一個點一定不等距","C":"交點必須在線段 AB 上","D":"圓弧不能用圓規畫"}, "A", "單一點只能提供一個位置，無法唯一決定通過它的目標直線；需要第二個交點，選 A。", "區分『有一個等距點』與『確定整條等距點軌跡』。", ["一個交點 P 確實可滿足 PA=PB。","但通過 P 可畫出許多直線。","因此無法唯一確定垂直平分線。","需要另一個交點 Q 來決定 PQ。","選 A。"], "medium"),
make(9, "兩點 A、B 的等距點集合在平面上形成什麼圖形？", {"A":"線段 AB","B":"直線 AB","C":"AB 的垂直平分線","D":"以 A 為圓心的圓"}, "C", "平面上到 A、B 等距的所有點形成 AB 的垂直平分線，選 C。", "把單一作圖結果提升為軌跡概念，找出同時到兩點等距的集合。", ["任取等距點 P，使 PA=PB。","連接 P 與另一個等距點 Q。","所有這些點所在直線垂直 AB。","且通過 AB 中點。","選 C。"], "medium"),
make(10, "尺規作圖的步驟中，除了畫出圖形外，為什麼還要記錄圓心、半徑與交點？", {"A":"用來說明每一步的幾何理由並驗證結果","B":"只是讓圖看起來更複雜","C":"為了改變尺的長度","D":"因為圓規不能畫弧"}, "A", "記錄圓心、半徑與交點可追蹤等距關係，說明作圖確實達成目標，而非只憑外觀，選 A。", "把作圖程序和證明理由逐步對應，完成可檢查的幾何推理。", ["記錄圓心能知道距離從哪裡量。","記錄半徑能確認哪些長度相等。","記錄交點能建立後續直線或角平分線。","最後用這些關係驗證目標。","選 A。"], "easy"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

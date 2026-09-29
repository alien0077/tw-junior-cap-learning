import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-s-iv-9"
KG = "kg-math-performance-s-iv-9"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "三角形不等式、最大角與最長邊、SSS／SAS／ASA／HL 全等判定、等腰三角形與對應關係", "observedPattern": "公開數學評量常要求從邊角條件判斷三角形能否成立或全等，並將全等對應傳遞到角、邊與周長；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-s-iv-9-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供三角形成立、全等判定與幾何推理能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的幾何證明方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "三角形三邊長為 6 公分、10 公分與 x 公分，若 x 為整數，則下列哪一個 x 可能成立？", {"A": "3", "B": "5", "C": "16", "D": "17"}, "B", "三角形不等式要求 |10-6|<x<10+6，即 4<x<16；整數 5 符合，選 B。", "先用兩已知邊的差與和建立第三邊嚴格範圍。", ["取兩已知邊 6 與 10。", "第三邊須大於差 10-6=4。", "第三邊須小於和 10+6=16。", "檢查選項，只有 5 落在 4<x<16。", "所以選 B。"], "medium"),
    make(2, "一個三角形的三邊長為 5、8、11 公分，則最大的內角是下列哪一邊所對的角？", {"A": "5 公分邊", "B": "8 公分邊", "C": "11 公分邊", "D": "無法判定"}, "C", "三角形中邊越長，所對角越大；最長邊是 11 公分，因此最大角在 11 公分邊的對面，選 C。", "先比較邊長，不必先求角度數值。", ["列出三邊 5、8、11。", "找出最長邊 11。", "利用大邊對大角定理。", "最大內角必對著 11 公分邊。", "所以選 C。"], "easy"),
    make(3, "若兩個三角形的三組對應邊長分別為 6、9、13 公分，則兩三角形可由哪個判定得知全等？", {"A": "SSS", "B": "SAS", "C": "ASA", "D": "AA"}, "A", "三組對應邊分別相等，符合邊邊邊 SSS 全等判定，選 A。", "數清楚已知的是三邊，而不是只看其中兩邊。", ["確認三組對應邊均相等。", "沒有使用角的資料。", "三邊相等判定記為 SSS。", "將條件與選項比對。", "所以選 A。"], "easy"),
    make(4, "兩個三角形有兩個對應角及其夾邊分別相等，依哪個判定可知兩三角形全等？", {"A": "SSS", "B": "SAS", "C": "ASA", "D": "HL"}, "C", "兩角及其夾邊相等是角邊角 ASA 全等判定，選 C。", "辨認邊是否位於兩個已知角之間，這是 ASA 的關鍵。", ["確認已知兩個對應角相等。", "確認已知邊是兩角的夾邊。", "這三項排列為 Angle-Side-Angle。", "縮寫為 ASA。", "所以選 C。"], "medium"),
    make(5, "等腰三角形的兩腰各長 9 公分，底邊長 8 公分，則兩個底角具有什麼關係？", {"A": "互為餘角", "B": "互為補角", "C": "相等", "D": "一定都是直角"}, "C", "兩腰相等的三角形是等腰三角形，等腰三角形的兩個底角相等，選 C。", "從兩腰相等辨識等腰三角形，再套用底角定理。", ["確認兩腰長度都為 9。", "因此圖形為等腰三角形。", "等腰三角形底角相等。", "所以兩個底角大小相同。", "選 C。"], "easy"),
    make(6, "在全等三角形 ABC 與 DEF 中，若 A↔D、B↔E、C↔F，且 ∠C=57°，則 ∠F 為多少？", {"A": "33°", "B": "57°", "C": "123°", "D": "無法判定"}, "B", "全等三角形對應角相等；C 對應 F，因此 ∠F=∠C=57°，選 B。", "先依題目給的頂點對應配對，再傳遞角度。", ["讀取對應關係 C↔F。", "全等保證對應角相等。", "把 ∠C=57° 傳給 ∠F。", "得到 ∠F=57°。", "所以選 B。"], "easy"),
    make(7, "若兩個三角形全等，其中一個三角形周長為 31 公分，另一個三角形的周長為多少？", {"A": "15.5 公分", "B": "31 公分", "C": "62 公分", "D": "無法判定"}, "B", "全等三角形對應邊長相等，三邊總和也相等，因此另一個周長為 31 公分，選 B。", "把全等的邊長保持性加總到周長。", ["全等表示三組對應邊分別相等。", "將三組等長邊分別相加。", "兩個三角形的周長因此相同。", "已知一個為 31 公分。", "所以另一個也是 31 公分，選 B。"], "easy"),
    make(8, "三角形的兩邊長為 7 公分與 12 公分，第三邊 x 應滿足哪個範圍才能形成三角形？", {"A": "0<x<5", "B": "5<x<19", "C": "7<x<12", "D": "12<x<19"}, "B", "三角形不等式為 |12-7|<x<12+7，即 5<x<19，選 B。", "用已知兩邊的差與和，不要把端點 5、19 包含進去。", ["計算兩邊差 12-7=5。", "計算兩邊和 12+7=19。", "第三邊必須大於差。", "第三邊必須小於和。", "所以範圍為 5<x<19，選 B。"], "medium"),
    make(9, "若 △ABC≅△DEF，則下列哪一組對應關係正確？", {"A": "AB=EF", "B": "BC=EF", "C": "AC=DE", "D": "∠A=∠E"}, "B", "全等符號的頂點順序給出 A↔D、B↔E、C↔F，因此 BC 對應 EF，選 B。", "先讀全等符號的頂點順序，再逐一配對，不靠圖形位置猜測。", ["從 △ABC≅△DEF 讀出 A↔D。", "第二個頂點 B↔E。", "第三個頂點 C↔F。", "因此邊 BC 對應邊 EF。", "所以選 B。"], "medium"),
    make(10, "兩個直角三角形的斜邊與一股分別相等，則依哪個判定可判定全等？", {"A": "AAA", "B": "SSS", "C": "HL（斜邊股）", "D": "AA"}, "C", "直角三角形若斜邊與一股分別相等，可用 HL（斜邊股）全等判定，選 C。", "先利用直角條件，再辨認斜邊加一股的特殊判定。", ["確認兩個三角形都含直角。", "已知一組斜邊相等。", "另有一組股相等。", "直角三角形的特殊判定是 HL。", "所以選 C。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/math"
SOURCES = [
    ("https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "114年國中教育會考數學科公開試題", "數與量、根式表示、運算與推理能力方向；本題不宣稱一對一題號對應"),
    ("https://school.tc.edu.tw/open-message/193521/get-file/697b23af02d6b7546a022da8.pdf", "臺中市立至善國民中學114學年度第一學期第二次定期評量八年級數學科", "公開試卷頁面與年級已核對；參考根式計算、表示轉換與情境應用題型，不複製原題"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "高雄市立鹽埕國民中學114學年度第二學期第一次段考數學科", "公開試卷與年級已核對；參考根式、幾何量與代數推理題型，不複製原題"),
]

DATA = [
    ("principal square root", "正方形面積為 196 平方公分，若邊長為 √196，則邊長為何？", ["14", "−14", "98", "196"], "A", "因為 14²＝196，且邊長取正值，所以 √196＝14。"),
    ("simplify radical", "化簡 √72 的最簡根式為何？", ["6√2", "2√6", "8√2", "36√2"], "A", "72＝36×2，所以 √72＝√36×√2＝6√2。"),
    ("add like radicals", "計算 √12＋√27 的結果為何？", ["5√3", "√39", "7√3", "9√3"], "A", "√12＝2√3、√27＝3√3，因此相加為 5√3。"),
    ("compare equivalent forms", "下列哪一個關係正確？", ["3√2＝√18", "3√2＞√18", "3√2＜√18", "3√2＝√6"], "A", "√18＝√(9×2)＝3√2，兩式相等。"),
    ("multiply radicals", "計算 √6×√24 的結果為何？", ["12", "6√4", "√30", "30"], "A", "√6×√24＝√144＝12。"),
    ("divide and simplify", "化簡 √50 ÷ 5 的結果為何？", ["√2", "2√5", "√10", "10"], "A", "√50＝5√2，所以 √50÷5＝√2。"),
    ("square equation", "若 x 為正數且 x²＝49，則 x 為何？", ["7", "−7", "49", "√49±7"], "A", "x²＝49 的平方根為 ±7，但題目限定 x 為正數，所以 x＝7。"),
    ("perimeter with radicals", "長方形兩邊長分別為 √5 公分與 √20 公分，則周長為何？", ["6√5 公分", "5√5 公分", "2√25 公分", "√25 公分"], "A", "√20＝2√5，周長 2(√5＋2√5)＝6√5 公分。"),
    ("estimate", "√30 位於哪兩個連續整數之間？", ["5 與 6 之間", "4 與 5 之間", "6 與 7 之間", "30 與 31 之間"], "A", "因為 5²＝25＜30＜36＝6²，所以 5＜√30＜6。"),
    ("geometric application", "正方形邊長為 6 公分，則其對角線長為何？", ["6√2 公分", "12 公分", "36√2 公分", "3√2 公分"], "A", "由畢氏定理，對角線平方為 6²＋6²＝72，所以對角線為 √72＝6√2 公分。"),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{"url": url, "title": f"{title}；{locator}；本題為原創 pattern-only 改寫，未複製原題、選項、圖表或答案。", "year": "114", "subject": "math", "locator": locator, "observedPattern": "公開數學評量常結合根式化簡、比較、運算、方程、估算與幾何情境，測量表示轉換、運算順序、推理與回算；本題使用全新數值與題幹。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for url, title, locator in SOURCES]
    steps = [
        f"讀題定位：先圈出本題的數值、根式運算或幾何條件，確認本題主軸是「{topic}」。",
        "建立判準：先整理平方、乘除、同類根式、正負號、估算範圍或幾何關係，再決定要用的公式。",
        f"逐步計算並核對選項：依題目條件完成化簡、合併、比較或代入；正確選項為 {answer}。",
        f"檢查理由：{explanation} 再確認每一步的根號、係數、單位與正負號沒有誤讀。",
        "最後回算或估算驗證：把答案代回原條件，檢查數值合理性與單位；若題目數字或限制改變，必須重新計算。",
    ]
    return {"id": f"question-math-performance-n-iv-5-{index}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": options, "knowledgeIds": ["kg-math-performance-n-iv-5"], "difficulty": "medium", "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0], "sourceLocator": "公開數學評量能力方向參考；本題為獨立原創根式題，未複製原題文字、選項、圖表或答案；待第二輪 AI／Terra 內容複核。", "authoringNote": "依官方數學課綱 KG 與三個可追溯公開數學評量來源的能力、資料型態與推理層次重新設計；數值、選項、解析與五步解題均為原創。"}, "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-math-performance-n-iv-5", "examPatternRefs": refs, "solutionStrategy": "先辨認根式與題目限制，再用平方根性質、根式化簡、同類項合併、估算或畢氏定理計算，最後回算與檢查單位。", "solutionSteps": steps}


for index, row in enumerate(DATA, 1):
    (OUT / f"question-math-performance-n-iv-5-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")

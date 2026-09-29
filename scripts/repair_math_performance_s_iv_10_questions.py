import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-s-iv-10"
KG = "kg-math-performance-s-iv-10"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "AA／SAS／SSS 相似判定、相似比例、平行線截線比例、周長面積倍率與影子測高", "observedPattern": "公開數學評量常從角度或對應邊比例判斷三角形相似，並將相似比例延伸到平行線截線、周長、面積與實物測量；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-s-iv-10-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供三角形相似、比例與測量應用能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的三角形相似方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "若兩個三角形有兩組對應角分別相等，則兩三角形一定相似。這個判定稱為什麼？", {"A": "AA", "B": "SSS", "C": "SAS", "D": "HL"}, "A", "兩組對應角相等即可判定三角形相似，稱為 AA 相似判定，選 A。", "先辨認資料是兩個角，不要把全等判定與相似判定混用。", ["確認已知兩組角相等。", "三角形第三角也會相等。", "兩角條件足以確定形狀比例。", "此判定縮寫為 AA。", "所以選 A。"], "easy"),
    make(2, "三角形甲的三邊為 6、8、10 公分，三角形乙的三邊為 12、16、20 公分。乙與甲的對應邊長倍率為多少？", {"A": "1/2", "B": "2", "C": "3/2", "D": "4"}, "B", "乙的每一邊都是甲的 2 倍：12÷6=16÷8=20÷10=2，選 B。", "選一組對應邊相除，再用其他邊檢查倍率一致。", ["取 12 與 6 作對應邊。", "計算 12÷6=2。", "檢查 16÷8=2、20÷10=2。", "確認三邊倍率一致。", "所以倍率為 2，選 B。"], "easy"),
    make(3, "兩個相似三角形的對應邊比（小：大）為 3：5，若小三角形一邊長 9 公分，大三角形對應邊長是多少？", {"A": "12 公分", "B": "15 公分", "C": "18 公分", "D": "21 公分"}, "B", "小邊 3 份等於 9 公分，每份 3 公分；大邊 5 份為 15 公分，選 B。", "用已知小邊除以比例份數，再乘大邊份數。", ["小：大比例為 3:5。", "小邊 9÷3=3 公分／份。", "大邊有 5 份。", "大邊長=3×5=15 公分。", "所以選 B。"], "easy"),
    make(4, "在 △ABC 中，D 在 AB 上、E 在 AC 上，且 DE∥BC。若 AD=4、DB=3、AE=8，則 EC 為多少？", {"A": "4", "B": "5", "C": "6", "D": "7"}, "C", "AB=4+3=7；由 DE∥BC 得 AD/AB=AE/AC，即 4/7=8/AC，AC=14；EC=14-8=6，選 C。", "先補出完整邊長 AB，再用平行線造成的相似比例求 AC。", ["計算 AB=AD+DB=7。", "利用 DE∥BC 得 4/7=8/AC。", "交叉相乘 4AC=56，得 AC=14。", "EC=AC-AE=14-8=6。", "所以選 C。"], "hard"),
    make(5, "兩個相似三角形的對應邊長倍率為 4，則大三角形與小三角形的面積比為何？", {"A": "4:1", "B": "8:1", "C": "12:1", "D": "16:1"}, "D", "面積倍率是線性倍率平方，4²=16，因此大：小=16:1，選 D。", "先辨認題目給的是邊長倍率，再平方得到面積倍率。", ["線性倍率 k=4。", "面積倍率使用 k²。", "計算 4²=16。", "大圖形相對小圖形為 16 倍。", "所以比為 16:1，選 D。"], "medium"),
    make(6, "同一時間測得一根 2 公尺竹竿影長 3 公尺；建築物影長 21 公尺，估計建築物高多少？", {"A": "12 公尺", "B": "14 公尺", "C": "16 公尺", "D": "18 公尺"}, "B", "高度與影長成比例：建築物高/21=2/3，所以建築物高=21×2/3=14 公尺，選 B。", "建立高度比影長的相似比例，先約分再計算。", ["竹竿高影比為 2:3。", "同一時間光線角度相同，建築物比值也相同。", "建築物高=21×2/3。", "計算得到 14 公尺。", "所以選 B。"], "medium"),
    make(7, "若 △ABC∼△DEF，且 A↔D、B↔E、C↔F，AB=9 公分、DE=12 公分，則對應邊 BC=15 公分時，EF 為多少？", {"A": "18 公分", "B": "20 公分", "C": "21 公分", "D": "24 公分"}, "B", "相似倍率大／小=DE/AB=12/9=4/3；EF=15×4/3=20 公分，選 B。", "先由一組對應邊求倍率，再套到另一組對應邊。", ["確定 AB 對應 DE。", "求倍率 12/9=4/3。", "BC 對應 EF。", "計算 EF=15×4/3=20。", "所以選 B。"], "medium"),
    make(8, "下列哪一組條件足以判定兩三角形相似，而不必知道三邊長？", {"A": "一組對應邊相等", "B": "兩組對應角相等", "C": "一組對應角相等", "D": "兩三角形周長相等"}, "B", "兩組對應角相等可用 AA 判定三角形相似，不需先知道三邊長，選 B。", "檢查條件是否足以固定三角形形狀，單一邊或角都不足。", ["一組邊或一組角不能決定完整形狀。", "兩組角相等會連帶使第三角相等。", "這符合 AA 相似判定。", "因此不需知道三邊長。", "所以選 B。"], "medium"),
    make(9, "相似三角形甲、乙的周長比（甲：乙）為 3：7，若甲的周長為 21 公分，乙的周長是多少？", {"A": "35 公分", "B": "42 公分", "C": "49 公分", "D": "63 公分"}, "C", "周長比也是 3:7；甲 3 份為 21，每份 7，乙 7 份為 49 公分，選 C。", "周長是線性量，直接依給定周長比放大。", ["甲：乙周長比為 3:7。", "甲每份長度 21÷3=7 公分。", "乙有 7 份。", "乙周長=7×7=49 公分。", "所以選 C。"], "easy"),
    make(10, "若兩個三角形的三組對應邊長成比例，則可依哪個判定得知兩三角形相似？", {"A": "AA", "B": "SAS", "C": "SSS", "D": "HL"}, "C", "三組對應邊成比例是 SSS 相似判定，選 C。", "注意相似的 SSS 要求邊成比例，不是三邊分別相等的全等 SSS。", ["確認三組對應邊都提供比例關係。", "這是邊邊邊的相似條件。", "與全等的邊長相等區分開。", "相似判定縮寫為 SSS。", "所以選 C。"], "easy"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

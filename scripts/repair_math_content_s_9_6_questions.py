import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-9-6"
KG = "kg-math-content-s-9-6"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "圓心角、弦、切線、圓周角、弦心距與圓內接四邊形", "observedPattern": "公立學校公開數學試題常以圓的構造、角度關係、切線與弦的性質及可計算的直角三角形情境考查幾何推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-9-6-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供圓的幾何性質能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的圓幾何能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "圓 O 在點 A 的切線為 l，半徑 OA 與 l 的夾角必為多少？", {"A": "90°", "B": "45°", "C": "60°", "D": "180°"}, "A", "切線與接觸點的半徑互相垂直，所以 OA 與 l 的夾角為 90°，選 A。", "先辨認 l 是接觸點的切線，再套用半徑垂直切線定理。", ["確認 A 是圓與直線 l 的接觸點。", "找出通過接觸點的半徑 OA。", "回想半徑與切線互相垂直。", "得到夾角為 90°。", "選 A。"], "easy"),
    make(2, "同一圓中，弦 AB 與弦 CD 等長。它們所對的圓心角 ∠AOB 與 ∠COD 有何關係？", {"A": "一定互為補角", "B": "前者是後者兩倍", "C": "兩角相等", "D": "無法判定"}, "C", "同圓中等弦所對的圓心角相等，因此 ∠AOB＝∠COD，選 C。", "將線段長短關係轉換成同圓的圓心角關係，不要把弦誤當成弧。", ["確認 AB、CD 位於同一圓。", "題目給出兩弦等長。", "使用同圓等弦對等圓心角。", "得到 ∠AOB＝∠COD。", "選 C。"], "easy"),
    make(3, "圓心 O 到弦 AB 的垂線交 AB 於 M。下列哪項必然成立？", {"A": "M 是圓心", "B": "AM＝MB", "C": "OA＝AB", "D": "OM＝AB"}, "B", "圓心到弦的垂線會平分弦，所以 AM＝MB，選 B。", "看到圓心、弦與垂線三個條件時，直接辨認『圓心到弦的垂線平分弦』。", ["確認 AB 是弦，O 是圓心。", "確認 OM 垂直 AB。", "套用圓心到弦的垂線平分弦。", "把 AB 分成相等的 AM 與 MB。", "選 B。"], "easy"),
    make(4, "AB 為圓的直徑，C 在圓周上。圓周角 ∠ACB 為何？", {"A": "30°", "B": "45°", "C": "90°", "D": "180°"}, "C", "直徑所對的圓周角為直角，因此 ∠ACB＝90°，選 C。", "先看所對弦是否為直徑；直徑是判斷圓周角的關鍵證據。", ["確認 AB 通過圓心，是直徑。", "確認 C 位於圓周上。", "辨認 ∠ACB 是 AB 所對的圓周角。", "使用直徑所對圓周角為 90°。", "選 C。"], "easy"),
    make(5, "圓心角 ∠AOB＝110°，它所對的弧 AB 的度數為何？", {"A": "55°", "B": "110°", "C": "220°", "D": "360°"}, "B", "圓心角的度數等於所對弧的度數，所以弧 AB 為 110°，選 B。", "區分圓心角與圓周角；本題是圓心角，與弧度數相同。", ["確認頂點 O 是圓心。", "判定 ∠AOB 是圓心角。", "回想圓心角度數等於所對弧度數。", "將 110° 直接對應到弧 AB。", "選 B。"], "easy"),
    make(6, "同一圓中，圓周角 ∠ACB 與 ∠ADB 都對著同一段弧 AB。若 ∠ACB＝38°，則 ∠ADB 為何？", {"A": "19°", "B": "38°", "C": "76°", "D": "142°"}, "B", "同弧所對的圓周角相等，因此 ∠ADB＝∠ACB＝38°，選 B。", "先確認兩角的端點相同且對應同一弧，再使用同弧所對圓周角相等。", ["讀出兩角都以 A、B 為端點。", "確認 C、D 位於同一圓周。", "判定兩角對同一段弧 AB。", "套用同弧圓周角相等。", "選 B。"], "medium"),
    make(7, "從圓外點 P 向圓作兩條切線，接觸點為 A、B。若 PA＝8 公分，PB 為多少？", {"A": "4 公分", "B": "8 公分", "C": "16 公分", "D": "無法判定"}, "B", "同一外點引圓的兩條切線段長相等，所以 PB＝PA＝8 公分，選 B。", "看到同一外點的兩條切線，先用切線段相等，不需計算半徑。", ["確認 PA、PB 都從 P 出發。", "確認 A、B 是兩條切線的接觸點。", "套用同一外點兩切線段相等。", "將 PA＝8 對應到 PB。", "選 B。"], "medium"),
    make(8, "圓半徑為 13 公分，圓心到弦 AB 的距離為 12 公分。若 M 是垂足，則半弦 AM 為多少？", {"A": "3 公分", "B": "5 公分", "C": "12 公分", "D": "25 公分"}, "B", "OM 垂直且平分弦，直角三角形 OMA 的斜邊 OA＝13、OM＝12，因此 AM＝√(13²－12²)＝5 公分，選 B。", "先用幾何性質找出半弦，再在直角三角形套畢氏定理。", ["由圓心到弦的垂線得 AM＝MB。", "確認 OMA 是直角三角形。", "列出 OA²＝OM²＋AM²。", "計算 AM＝√(169－144)＝5 公分。", "選 B。"], "hard"),
    make(9, "四邊形 ABCD 內接於同一圓，若 ∠A＝112°，則對角 ∠C 為多少？", {"A": "68°", "B": "78°", "C": "112°", "D": "248°"}, "A", "圓內接四邊形的對角互補，所以 ∠C＝180°－112°＝68°，選 A。", "先確認四邊形四個頂點都在圓上，再使用對角和為 180°。", ["辨認 ABCD 是圓內接四邊形。", "找出 A 與 C 是對角。", "列出 ∠A＋∠C＝180°。", "計算 ∠C＝180°－112°＝68°。", "選 A。"], "medium"),
    make(10, "圓 O 的弦 AB 長 16 公分，圓心 O 到弦的垂足 M 恰為 AB 的中點。若 OA＝10 公分，OM 為多少？", {"A": "6 公分", "B": "8 公分", "C": "12 公分", "D": "18 公分"}, "A", "AM＝8 公分，且 OMA 為直角三角形；OM＝√(10²－8²)＝6 公分，選 A。", "先把弦長除以二得到半弦，再用半徑作斜邊建立直角三角形。", ["由 M 為 AB 中點得 AM＝16÷2＝8 公分。", "確認 OM 垂直 AB，OMA 為直角三角形。", "以 OA＝10 作斜邊列式 10²＝OM²＋8²。", "解得 OM＝√36＝6 公分。", "選 A。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

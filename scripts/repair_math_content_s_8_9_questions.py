import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-9"
KG = "kg-math-content-s-8-9"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "平行四邊形對邊、對角、鄰角、對角線與平行四邊形判定", "observedPattern": "公開學校數學試題常以平行四邊形的邊角關係、對角線交點及反向判定考查圖形性質；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-9-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供平行四邊形基本性質與判定能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的平行四邊形方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "平行四邊形 ABCD 中，哪一組對邊必定互相平行？", {"A":"AB∥CD 且 BC∥AD","B":"AB∥BC 且 CD∥AD","C":"AC∥BD","D":"只有 AB∥CD"}, "A", "平行四邊形的定義是兩組對邊分別平行，因此 AB∥CD 且 BC∥AD，選 A。", "先用頂點循環順序找相對邊，不把相鄰邊誤認成對邊。", ["沿 A-B-C-D 讀取四邊。","AB 的對邊是 CD。","BC 的對邊是 AD。","兩組對邊都平行。","選 A。"], "easy"),
make(2, "平行四邊形中，對邊的長度有何關係？", {"A":"兩組對邊分別相等","B":"只有一組對邊相等","C":"四邊都一定相等","D":"對邊一定互相垂直"}, "A", "平行四邊形的兩組對邊分別平行且等長，選 A。", "對邊是相對位置，不是相鄰位置；使用平行四邊形基本性質。", ["找第一組對邊 AB、CD。","找第二組對邊 BC、AD。","平行四邊形的每組對邊等長。","所以 AB=CD、BC=AD。","選 A。"], "easy"),
make(3, "平行四邊形的兩組對角有何關係？", {"A":"對角互補","B":"對角相等","C":"對角一定為 90°","D":"對角和為 90°"}, "B", "平行四邊形的對角相等，鄰角互補，選 B。", "先分清對角與鄰角，再套用相應性質。", ["對角是不共邊的兩個角。","平行四邊形中對角相等。","鄰角才會互補。","因此本題答案是對角相等。","選 B。"], "easy"),
make(4, "平行四邊形的一個內角為 68°，與它相鄰的內角是多少？", {"A":"68°","B":"90°","C":"112°","D":"292°"}, "C", "鄰角互補，所以相鄰角=180°−68°=112°，選 C。", "題目問鄰角，要使用 180° 相加而不是對角相等。", ["確認兩角共用一邊，是鄰角。","鄰角和為 180°。","列式 x+68=180。","解得 x=112°。","選 C。"], "medium"),
make(5, "平行四邊形 ABCD 的對角線 AC、BD 交於 O，哪個關係必定成立？", {"A":"AO=OC 且 BO=OD","B":"AO=BO 且 OC=OD","C":"AC 垂直 BD","D":"AC=BD"}, "A", "平行四邊形的對角線互相平分，所以 AO=OC、BO=OD，選 A。", "找到對角線交點後，使用『互相平分』而非誤用矩形或菱形特性。", ["辨認 AC、BD 是兩條對角線。","O 是它們的交點。","平行四邊形對角線互相平分。","因此 AO=OC、BO=OD。","選 A。"], "medium"),
make(6, "若平行四邊形 ABCD 的 AB=12 公分，則 CD 為多少？", {"A":"6 公分","B":"12 公分","C":"24 公分","D":"無法判定"}, "B", "對邊等長，CD=AB=12 公分，選 B。", "找出題目給邊的對邊，再使用等長性質。", ["AB 的對邊是 CD。","平行四邊形對邊等長。","因此 CD=AB。","代入 AB=12 得 CD=12。","選 B。"], "easy"),
make(7, "一個四邊形若有一組對邊平行且等長，通常可判定它是什麼？", {"A":"平行四邊形","B":"一定是正方形","C":"一定是菱形","D":"一定是梯形且不能平行"}, "A", "四邊形有一組對邊平行且等長，即可判定為平行四邊形，選 A。", "使用平行四邊形的反向判定，不要求兩組條件都先給出。", ["確認圖形是四邊形。","檢查有一組對邊平行。","檢查同一組對邊等長。","符合平行四邊形判定定理。","選 A。"], "medium"),
make(8, "平行四邊形的兩條對角線交點 O 將 AC 分成 AO=5 公分、OC=多少？", {"A":"2.5 公分","B":"5 公分","C":"10 公分","D":"無法判定"}, "B", "對角線互相平分，AO=OC，因此 OC=5 公分，選 B。", "先辨認 O 是對角線交點，再使用互相平分。", ["AC 被 O 分成 AO 與 OC。","平行四邊形對角線互相平分。","所以 AO=OC。","已知 AO=5，得到 OC=5。","選 B。"], "easy"),
make(9, "下列哪個條件足以判定一個四邊形是平行四邊形？", {"A":"四邊都相等","B":"兩條對角線互相平分","C":"有一個直角","D":"有一組鄰邊相等"}, "B", "四邊形的兩條對角線互相平分，是平行四邊形的判定條件，選 B。", "區分能保證平行的條件與只描述長度或角度的單一條件。", ["檢查選項 A：四邊等長可能是菱形，但需其他證據。","檢查 C、D：一個角或一組邊不足。","選項 B 直接給對角線互相平分。","這是平行四邊形判定。","選 B。"], "medium"),
make(10, "若平行四邊形的一個對角為 75°，則與它相對的角及相鄰的角分別是多少？", {"A":"相對 75°，相鄰 105°","B":"相對 105°，相鄰 75°","C":"相對 75°，相鄰 75°","D":"相對 105°，相鄰 105°"}, "A", "對角相等為 75°；鄰角互補為 180°−75°=105°，選 A。", "同時使用兩條性質，先處理對角，再處理鄰角。", ["對角相等，所以相對角是 75°。","鄰角和為 180°。","計算 180−75=105°。","整理為相對 75°、相鄰 105°。","選 A。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-1"
KG = "kg-math-content-s-8-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "角的構成與命名、角度分類、量角器讀值、直角／平角與角度加減", "observedPattern": "公開學校數學試題常以角的頂點與邊、角名順序、量角器、特殊角與相鄰角度關係考查角的表示與測量；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供角的表示、分類與量測能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的角能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "一個角由哪些幾何元素組成？", {"A":"一個頂點和兩條以頂點為端點的射線","B":"兩個頂點和一條直線","C":"三個端點和一條線段","D":"只有一個圓弧"}, "A", "角由共同端點（頂點）的兩條射線組成，選 A。", "先找兩條邊，再確認它們是否共用一個端點。", ["辨認角的兩條邊。","兩條邊必須是射線。","檢查它們是否共用端點。","共同端點就是角的頂點。","選 A。"], "easy"),
make(2, "在 ∠ABC 中，角的頂點是哪一點？", {"A":"A","B":"B","C":"C","D":"無法判定"}, "B", "三字母角名的中間字母代表頂點，所以 ∠ABC 的頂點是 B，選 B。", "讀三字母角名時固定先看中間字母。", ["寫出角名 A-B-C。","找出中間位置的字母 B。","中間字母代表兩射線共同端點。","因此 B 是頂點。","選 B。"], "easy"),
make(3, "若兩條射線 BA 與 BC 形成一個角，哪兩個角名可表示同一個角？", {"A":"∠ABC 與 ∠CBA","B":"∠ABC 與 ∠BAC","C":"∠ABC 與 ∠ACB","D":"∠BAC 與 ∠BCA"}, "A", "∠ABC 與 ∠CBA 的中間字母都是 B，兩邊都指向 A、C，因此表示同一角，選 A。", "比較中間字母是否相同，再確認兩側字母是同一對射線。", ["找出 ∠ABC 的頂點 B。","找出 ∠CBA 的頂點也為 B。","兩個名稱的兩側字母都是 A、C。","只是將兩條邊的順序互換。","選 A。"], "easy"),
make(4, "量角器量得一個角為 90°，這個角稱為什麼？", {"A":"銳角","B":"直角","C":"鈍角","D":"平角"}, "B", "等於 90° 的角是直角，選 B。", "把量得的數值和特殊角定義逐一比對。", ["讀取量角結果 90°。","銳角小於 90°。","直角等於 90°。","因此該角是直角。","選 B。"], "easy"),
make(5, "一個角的兩邊形成一條直線，這個角的度數是多少？", {"A":"45°","B":"90°","C":"180°","D":"360°"}, "C", "兩條反向共線射線形成平角，平角為 180°，選 C。", "看到兩邊合成一直線，就聯想到平角。", ["確認兩邊是反向射線。","反向射線的邊界合成一條直線。","這種角稱為平角。","平角的標準度數是 180°。","選 C。"], "easy"),
make(6, "若兩個角互為餘角，其中一角為 35°，另一角為多少？", {"A":"45°","B":"55°","C":"145°","D":"215°"}, "B", "餘角和為 90°，所以另一角為 90°−35°=55°，選 B。", "先寫出餘角總和，再用減法求未知角。", ["餘角的總和是 90°。","設未知角為 x。","列式 x+35=90。","計算 x=90−35=55。","選 B。"], "medium"),
make(7, "兩個角互為補角，其中一角為 120°，另一角為多少？", {"A":"30°","B":"60°","C":"120°","D":"240°"}, "B", "補角和為 180°，另一角為 180°−120°=60°，選 B。", "把補角的 180°總和作為回查基準。", ["補角的總和是 180°。","設另一角為 x。","列式 x+120=180。","計算 x=180−120=60。","選 B。"], "medium"),
make(8, "用量角器量角時，哪個步驟最先要做？", {"A":"把量角器中心對準頂點，基準線貼齊一邊","B":"先看最大刻度再猜角度","C":"把量角器中心放在線段中點","D":"任意選一組刻度讀取"}, "A", "量角器中心要對準角的頂點，基準線要與其中一邊重合，才能正確讀值，選 A。", "量角先定位中心與零刻度，再讀與另一邊相交的刻度。", ["找出角的頂點。","把量角器中心放在頂點上。","讓基準線與一邊重合。","確認使用貼齊邊的正確零刻度。","選 A。"], "medium"),
make(9, "兩個相鄰角在一直線同側，已知其中一角為 65°，另一角為多少？", {"A":"25°","B":"65°","C":"115°","D":"295°"}, "C", "一直線同側的相鄰角形成平角，和為 180°，所以另一角為 180°−65°=115°，選 C。", "先辨認線性對角關係，再用平角總和計算。", ["兩角共用一邊且外側邊形成直線。","因此兩角和是平角 180°。","設另一角為 x。","x=180−65=115。","選 C。"], "medium"),
make(10, "135° 的角屬於哪一類？", {"A":"銳角","B":"直角","C":"鈍角","D":"周角"}, "C", "135° 大於 90° 且小於 180°，所以是鈍角，選 C。", "用 90° 和 180° 作為分類界線。", ["讀取角度 135°。","比較 135 與 90：較大。","比較 135 與 180：較小。","介於 90° 和 180° 的角是鈍角。","選 C。"], "easy"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

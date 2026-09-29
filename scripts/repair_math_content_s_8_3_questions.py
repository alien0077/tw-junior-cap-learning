import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-3"
KG = "kg-math-content-s-8-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "平行線、截線、同位角、內錯角、同側內角與平行線判定", "observedPattern": "公開學校數學試題常以截線造成的角位置、相等／互補關係及反向判定考查平行線推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-3-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供平行線與截線角度能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的平行線能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "在同一平面上，兩條直線永遠不相交，這兩條直線稱為什麼？", {"A":"垂直線","B":"平行線","C":"相交線","D":"角平分線"}, "B", "同一平面上不相交的兩條直線稱為平行線，選 B。", "先檢查是否共面，再看是否存在交點。", ["確認題目說兩線在同一平面。","檢查兩線是否有交點。","題目說永遠不相交。","這符合平行線的定義。","選 B。"], "easy"),
make(2, "直線 l 與直線 m 平行，哪個符號表示正確？", {"A":"l ⟂ m","B":"l ∥ m","C":"l = m","D":"l ∠ m"}, "B", "平行關係使用 ∥ 符號，所以寫作 l ∥ m，選 B。", "把幾何關係與專用符號配對。", ["題目給出平行關係。","平行的符號是 ∥。","將 l、m 放在符號兩側。","得到 l ∥ m。","選 B。"], "easy"),
make(3, "兩條平行線被同一條截線截過時，同位角有何關係？", {"A":"一定互補","B":"一定相等","C":"一定相差 90°","D":"一定都是直角"}, "B", "平行線被截線截過時，同位角相等，選 B。", "先確認兩線平行且由同一截線相交，再套用角關係。", ["辨認兩條目標線。","確認它們互相平行。","確認有同一條截線。","同位角在對應位置，度數相等。","選 B。"], "easy"),
make(4, "兩條平行線被截線截過時，內錯角的關係為何？", {"A":"相等","B":"和為 90°","C":"和為 180°","D":"沒有固定關係"}, "A", "平行線的內錯角相等，選 A。", "以『內部、截線兩側、錯開位置』定位角對，再使用平行線性質。", ["找出兩個角都位於兩平行線內部。","確認它們在截線的兩側。","這是一對內錯角。","平行線的內錯角相等。","選 A。"], "easy"),
make(5, "兩條平行線被截線截過時，同側內角的和為多少？", {"A":"90°","B":"120°","C":"180°","D":"360°"}, "C", "平行線的同側內角互為補角，和為 180°，選 C。", "先定位同側內角，再使用補角關係。", ["確認兩角位於兩平行線之間。","確認兩角在截線同一側。","它們是同側內角。","同側內角和為平角 180°。","選 C。"], "easy"),
make(6, "若一條截線與兩條直線形成一對相等的同位角，通常可判定兩條直線有何關係？", {"A":"垂直","B":"平行","C":"重合","D":"無法判定任何關係"}, "B", "同位角相等是判定兩直線平行的充分條件，因此選 B。", "分辨正向性質與反向判定：由角關係回推線的關係。", ["題目給出同位角相等。","同位角由同一截線形成。","使用平行線的反向判定。","可推出兩條直線平行。","選 B。"], "medium"),
make(7, "兩條平行線被截線截過，某個同位角為 68°，其對應的同位角是多少？", {"A":"22°","B":"68°","C":"112°","D":"180°"}, "B", "平行線的同位角相等，因此對應角也是 68°，選 B。", "判斷角對類型後直接套用相等關係。", ["確認兩線平行。","確認兩角是同位角。","同位角度數相等。","原角為 68°，對應角也為 68°。","選 B。"], "easy"),
make(8, "兩條平行線被截線截過，某個同側內角為 110°，另一個同側內角是多少？", {"A":"70°","B":"90°","C":"110°","D":"250°"}, "A", "同側內角和為 180°，另一角為 180°−110°=70°，選 A。", "先寫同側內角的固定總和，再做補角計算。", ["確認兩角是同側內角。","列出兩角和 180°。","設未知角為 x，x+110=180。","計算 x=70。","選 A。"], "medium"),
make(9, "下列哪一組位置描述的是內錯角？", {"A":"兩角在兩線外部且截線同側","B":"兩角在兩平行線內部且截線兩側","C":"兩角共用頂點且一邊重合","D":"兩角都在同一個交點外側"}, "B", "內錯角位於兩目標線之間，且分居截線兩側，選 B。", "用『內部』和『錯側』兩個條件同時定位。", ["內錯角必須在兩線之間。","因此先排除外部的 A。","再檢查是否在截線兩側。","B 同時符合內部與錯側。","選 B。"], "medium"),
make(10, "直線 p、q 被同一截線截過，某對同側內角和為 180°。在適當的相交條件下，可判定 p、q 為何？", {"A":"平行","B":"垂直","C":"一定重合","D":"不能使用角關係判斷"}, "A", "同側內角互補是兩直線平行的反向判定，因此 p、q 平行，選 A。", "先確認角的類型，再使用同側內角互補的逆命題。", ["確認兩角是同側內角。","題目給出它們的和是 180°。","同側內角互補可作平行判定。","因此 p 與 q 平行。","選 A。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

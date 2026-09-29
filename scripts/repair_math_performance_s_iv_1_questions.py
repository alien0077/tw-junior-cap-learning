import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-s-iv-1"
KG = "kg-math-performance-s-iv-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "平行四邊形、矩形、菱形、三角形全等與等腰三角形、垂直平分線、角平分線、圓切線、內角和", "observedPattern": "公開數學評量常要求從幾何定義或符號性質辨識平行四邊形與特殊四邊形，再運用全等、等距、角平分與多邊形內角和完成推理；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-s-iv-1-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供幾何定義、特殊四邊形、全等、圓與多邊形能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的幾何形體方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "平行四邊形 ABCD 中，若 ∠A=68°，則 ∠C 為何？", {"A": "22°", "B": "68°", "C": "112°", "D": "136°"}, "B", "平行四邊形的對角相等，因此 ∠C=∠A=68°，選 B。", "先辨認 A、C 是對角，再使用對角相等，不要誤用鄰角互補。", ["確認 A 與 C 位於平行四邊形的對角位置。", "使用平行四邊形對角相等性質。", "將 ∠A=68° 傳給 ∠C。", "得到 ∠C=68°。", "所以選 B；若問鄰角才會使用 180° 減法。"], "easy"),
    make(2, "矩形 PQRS 的對角線 PR、QS 相交於 O。下列哪一項一定正確？", {"A": "PR 垂直 QS", "B": "PR=QS 且 O 為兩者中點", "C": "PR 是 ∠P 的角平分線", "D": "四條邊都相等"}, "B", "矩形的兩條對角線等長，且互相平分，所以 PR=QS 且 O 同時是兩條對角線的中點，選 B。", "把矩形性質拆成對角線長度與互相平分兩部分逐一比對。", ["辨認 PQRS 是矩形。", "矩形對角線具有等長性質。", "矩形對角線也會互相平分。", "因此 O 是 PR、QS 的共同中點。", "所以選 B；垂直與四邊等長不是一般矩形必然性質。"], "medium"),
    make(3, "菱形 ABCD 的兩條對角線交於 O。下列哪一項必定成立？", {"A": "AC=BD", "B": "AC 與 BD 互相垂直", "C": "所有內角都相等", "D": "只有一組對邊平行"}, "B", "菱形的對角線互相垂直平分，因此 AC⊥BD，選 B。", "先使用菱形的特殊性質，避免把矩形的對角線等長誤套到菱形。", ["確認圖形是菱形，四邊等長。", "回憶菱形對角線互相平分且垂直。", "因此 AC 與 BD 垂直。", "其他選項並非所有菱形必然具備。", "所以選 B。"], "medium"),
    make(4, "若兩個三角形的三組對應邊長分別相等，依哪一個判定可知兩三角形全等？", {"A": "ASA", "B": "AAS", "C": "SAS", "D": "SSS"}, "D", "三組對應邊分別相等是邊邊邊判定，縮寫為 SSS，選 D。", "數清楚已知的是幾條邊，不要因為沒有角資料而自行補角。", ["確認已知資料是三組對應邊。", "沒有使用角相等條件。", "三邊相等的全等判定記為 SSS。", "將條件與選項縮寫逐一比對。", "所以選 D。"], "easy"),
    make(5, "線段 AB 的垂直平分線上任一點 P，必定滿足哪個關係？", {"A": "PA=PB", "B": "PA⊥PB", "C": "∠PAB=90°", "D": "P 是 AB 的中點"}, "A", "垂直平分線上的點到線段兩端點等距，所以 PA=PB，選 A。", "區分『線上的任一點』與『垂足或中點』，核心性質是到端點等距。", ["確認 P 位於 AB 的垂直平分線上。", "使用垂直平分線等距定理。", "得到 P 到 A、B 的距離相等。", "寫成 PA=PB。", "所以選 A；P 不必是 AB 的中點。"], "easy"),
    make(6, "若射線 BD 是 ∠ABC 的角平分線，且 ∠ABC=84°，則 ∠ABD 為多少？", {"A": "21°", "B": "42°", "C": "84°", "D": "168°"}, "B", "角平分線把原角分成兩個相等角，因此 ∠ABD=84°÷2=42°，選 B。", "看到角平分線就把整角平均分成兩份，再確認所問的是其中一份。", ["確認 BD 將 ∠ABC 分成 ∠ABD 與 ∠DBC。", "兩個小角相等。", "用 84° 除以 2。", "得到 ∠ABD=42°。", "所以選 B。"], "easy"),
    make(7, "圓 O 在切點 T 的切線為直線 l。下列哪一項必定正確？", {"A": "OT∥l", "B": "OT⊥l", "C": "OT=l", "D": "T 是圓心"}, "B", "圓的切線在切點處垂直於通過切點的半徑，因此 OT⊥l，選 B。", "抓住切線與半徑的交會位置是切點，使用垂直而非平行。", ["辨認 OT 是通過切點 T 的半徑。", "l 是在 T 的切線。", "切線與切點半徑互相垂直。", "因此 OT⊥l。", "所以選 B；圓心是 O，不是 T。"], "medium"),
    make(8, "一個八邊形的內角和為何？", {"A": "720°", "B": "900°", "C": "1080°", "D": "1260°"}, "C", "n 邊形內角和=(n-2)×180°；八邊形為 6×180°=1080°，選 C。", "先確認邊數，再套用多邊形內角和公式。", ["辨認邊數 n=8。", "從一個頂點可分成 n-2=6 個三角形。", "每個三角形內角和 180°。", "計算 6×180°=1080°。", "所以選 C。"], "easy"),
    make(9, "正五邊形的每一個內角是多少？", {"A": "90°", "B": "108°", "C": "120°", "D": "135°"}, "B", "正五邊形內角和=(5-2)×180°=540°，五個內角相等，每角為 540°÷5=108°，選 B。", "先求總內角和，再利用正多邊形各角相等平均分配。", ["計算五邊形內角和 3×180°=540°。", "正五邊形的五個內角相等。", "用 540°÷5。", "得到每角 108°。", "所以選 B。"], "medium"),
    make(10, "等腰三角形 ABC 中，AB=AC，若頂角 ∠A=46°，則底角 ∠B 為何？", {"A": "46°", "B": "67°", "C": "92°", "D": "134°"}, "B", "AB=AC 表示底角 B、C 相等；兩底角和為 180°-46°=134°，所以 ∠B=134°÷2=67°，選 B。", "先用等腰三角形底角相等，再用三角形內角和求單一底角。", ["由 AB=AC 判斷 ∠B=∠C。", "三角形剩餘兩角總和為 180°-46°=134°。", "把 134° 平分給兩個底角。", "得到 ∠B=67°。", "所以選 B。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

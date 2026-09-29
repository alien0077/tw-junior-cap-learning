import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-7-5"
KG = "kg-math-content-n-7-5"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "number-line order, opposite numbers, absolute value, distance, interval location, and arithmetic movement", "observedPattern": "公立學校公開數學試題常以數線判讀正負位置、大小順序、相反數、絕對值與兩點距離，並把加減視為向左右移動；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-7-5-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供數線位置、順序、相反數、絕對值、距離與加減移動能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的數線方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "數線上點 A 在 −3 的位置，點 B 在 2 的位置。哪一點在較右方？", {"A": "A", "B": "B", "C": "兩點相同", "D": "無法判斷"}, "B", "數線向右數值變大，2 大於 −3，所以 B 在較右方，選 B。", "先比較兩個數值，再用數線向右變大的方向判斷位置。", ["讀取 A 的數值 −3。", "讀取 B 的數值 2。", "比較 −3 與 2，得到 2 較大。", "數線上較大的數在右方。", "選 B，確認兩點不是同一位置。"], "easy"),
    make(2, "下列哪個數最接近數線上的原點 0？", {"A": "−2.5", "B": "1.2", "C": "−0.8", "D": "1.5"}, "C", "與 0 的距離由絕對值表示：2.5、1.2、0.8、1.5 中 0.8 最小，所以 −0.8 最接近，選 C。", "比較到原點的距離，不直接比較數字正負或大小。", ["列出各數到 0 的距離，即其絕對值。", "得到 2.5、1.2、0.8、1.5。", "找出最小距離 0.8。", "回到原數，對應 −0.8。", "選 C，檢查負號只影響方向，不影響距離。"], "medium"),
    make(3, "−5 的相反數在數線上位於哪個位置？", {"A": "−10", "B": "−5", "C": "0", "D": "5"}, "D", "相反數到原點距離相同但方向相反，−5 的相反數為 5，選 D。", "以原點為對稱中心，把數線位置反射到另一側並改變正負號。", ["讀取原數 −5。", "相反數的絕對值相同。", "把位置從原點左方移到右方。", "將 −5 改為 5。", "選 D，確認 −5＋5＝0。"], "easy"),
    make(4, "數線上兩點 P(−2) 與 Q(6) 的距離是多少？", {"A": "4", "B": "6", "C": "8", "D": "−8"}, "C", "兩點距離為 |6−(−2)|＝8，距離必為正，選 C。", "用兩坐標差的絕對值求數線上兩點距離。", ["寫出 P＝−2、Q＝6。", "計算 Q−P＝6−(−2)＝8。", "取絕對值得 8。", "確認距離不使用負號表示。", "選 C，檢查從 −2 向右走到 6 共 8 單位。"], "easy"),
    make(5, "若 x＜−1，以下哪個數一定也小於 x？", {"A": "x＋2", "B": "x−2", "C": "−x", "D": "x＋1"}, "B", "x−2 比 x 少 2，一定在數線左方；其餘選項不一定小於 x，選 B。", "用數線移動理解代數式：減去正數向左移，加上正數向右移。", ["把 x 視為數線上的任意位置。", "x−2 表示從 x 向左 2 單位。", "向左的位置必小於原本 x。", "檢查 x＋1、x＋2 會向右，−x 則視 x 正負而定。", "選 B，確認條件 x＜−1 不會改變結論。"], "medium"),
    make(6, "數線上從 −4 出發向右移 7 個單位，最後到達哪個數？", {"A": "−11", "B": "−3", "C": "3", "D": "11"}, "C", "向右代表加 7，−4＋7＝3，所以選 C。", "把向右移寫成加法，從起點加上位移量。", ["設定起點為 −4。", "向右移表示數值增加。", "建立 −4＋7。", "計算結果為 3。", "選 C，從 −4 經 0 到 3 共移 7 格。"], "easy"),
    make(7, "下列哪個不等式正確表示數線上 −1、3、−4 的大小關係？", {"A": "−4＜−1＜3", "B": "3＜−1＜−4", "C": "−1＜−4＜3", "D": "−4＜3＜−1"}, "A", "數線由左至右遞增，−4 在最左、−1 居中、3 最右，所以 −4＜−1＜3，選 A。", "把數字依數線左到右排序，負數比較時絕對值較大者更左。", ["比較負數 −4 與 −1，−4 較小。", "確認正數 3 大於所有這兩個負數。", "排列為 −4、−1、3。", "寫成 −4＜−1＜3。", "選 A，回到數線方向檢查順序。"], "easy"),
    make(8, "若 |a|＝4 且 a＜0，a 為何？", {"A": "−4", "B": "−1／4", "C": "4", "D": "0"}, "A", "絕對值為 4 的數是 4 或 −4，條件 a＜0 篩選出 −4，選 A。", "先由絕對值列出正負兩個候選，再用正負條件選擇。", ["由 |a|＝4 列出 a＝4 或 a＝−4。", "使用條件 a＜0。", "排除正數 4。", "保留 a＝−4。", "選 A，確認 |−4|＝4。"], "medium"),
    make(9, "數線上點 M 在 −6，點 N 是 M 向左移 3 個單位後的位置。N 的數值為何？", {"A": "−9", "B": "−3", "C": "3", "D": "9"}, "A", "向左移 3 表示 −6−3＝−9，所以選 A。", "向左使數值減少，從已知位置扣除位移量。", ["讀取 M＝−6。", "向左代表數值變小。", "建立 −6−3。", "計算得到 −9。", "選 A，檢查 −9 在數線上確實位於 −6 左方。"], "easy"),
    make(10, "數線上 A、B 的中點是 2，且 A 位於 −3，B 應位於哪個數？", {"A": "−1", "B": "5", "C": "7", "D": "8"}, "C", "中點公式 (−3＋B)÷2＝2，得 −3＋B＝4，所以 B＝7，選 C。", "用中點是兩端點平均建立方程式，再解出未知端點。", ["建立 (−3＋B)÷2＝2。", "兩邊乘以 2，得 −3＋B＝4。", "兩邊同加 3，解得 B＝7。", "檢查 −3 與 7 的平均為 2。", "選 C，確認 7 位於中點 2 的右方。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

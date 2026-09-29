import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-f-8-1"
KG = "kg-math-content-f-8-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "linear-function rules, rate of change, tables, function values, equations, and contextual interpretation", "observedPattern": "公立學校公開數學試題常由表格、情境或兩點關係建立一次函數，要求讀取斜率、截距、函數值、交會條件與變化率；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-f-8-1-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供一次函數規則、表格、變化率、交會與情境應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的一次函數能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "下列哪個式子表示 y 隨 x 作一次函數關係？", {"A": "y＝3x−2", "B": "y＝x²＋1", "C": "y＝1／x", "D": "y＝√x＋4"}, "A", "一次函數可寫成 y＝ax＋b 且 a、b 為常數；只有 y＝3x−2 符合。", "先辨認 x 的最高次為 1，再檢查是否能整理成 ax＋b 的形式。", ["寫出一次函數的一般形式 y＝ax＋b。", "檢查 A，y＝3x−2 中 x 的次數為 1。", "檢查 B、C、D，分別含平方、倒數或根號，不是一次式。", "確認 A 的係數 3 與常數 −2 都是固定數。", "選 A，回查題目問的是一次函數關係而非任意函數。"], "easy"),
    make(2, "某函數的對應表為 x＝0、1、2 時，y＝5、8、11。若關係為一次函數，y 與 x 的關係式為何？", {"A": "y＝2x＋5", "B": "y＝3x＋2", "C": "y＝3x＋5", "D": "y＝5x＋3"}, "C", "x 每增加 1，y 增加 3，所以斜率為 3；x＝0 時 y＝5，截距為 5，故 y＝3x＋5，選 C。", "先由等量 x 間隔求變化率，再用 x＝0 的函數值找截距。", ["比較相鄰 y 值：8−5＝3、11−8＝3。", "因此每增加 1 個 x，y 增加 3，斜率為 3。", "由 x＝0 時 y＝5，得截距 b＝5。", "組合成 y＝3x＋5。", "選 C，代入 x＝1 得 8，與表格相符。"], "medium"),
    make(3, "若 y＝−2x＋7，當 x＝4 時，y 為多少？", {"A": "−1", "B": "1", "C": "7", "D": "15"}, "A", "代入 x＝4 得 y＝−2×4＋7＝−8＋7＝−1，所以選 A。", "先保留負號與乘法，再把 x 的值代入規則計算。", ["寫下規則 y＝−2x＋7。", "以 x＝4 代入，得 y＝−2×4＋7。", "先算乘法 −2×4＝−8。", "計算 −8＋7＝−1。", "選 A，將 x＝4、y＝−1 代回原式確認等式成立。"], "easy"),
    make(4, "若 y＝4x−3，當 y＝17 時，x 為多少？", {"A": "4", "B": "5", "C": "6", "D": "8"}, "B", "17＝4x−3，兩邊加 3 得 20＝4x，再除以 4 得 x＝5，選 B。", "把已知的 y 值代入後，依逆運算順序解一次方程式。", ["將 y＝17 代入 y＝4x−3，得到 17＝4x−3。", "兩邊同加 3，得 20＝4x。", "兩邊同除以 4。", "解出 x＝5。", "選 B，代回 4×5−3＝17 檢查。"], "easy"),
    make(5, "方案甲的費用為 y＝2x＋20 元，方案乙為 y＝5x＋8 元；x 為使用次數。兩方案費用相同時，x 為多少？", {"A": "2", "B": "3", "C": "4", "D": "6"}, "C", "令 2x＋20＝5x＋8，移項得 12＝3x，所以 x＝4，選 C。", "比較兩個一次函數時令輸出相等，建立方程式後解出交會的輸入值。", ["把兩方案費用設為相等：2x＋20＝5x＋8。", "兩邊同減 2x，再同減 8，得 12＝3x。", "兩邊同除以 3，得 x＝4。", "確認 x 是使用次數，符合非負整數條件。", "選 C，代入兩式都得到 28 元。"], "medium"),
    make(6, "水箱注水量 y（公升）與時間 x（分鐘）符合 y＝6x＋10。下列何者表示每分鐘增加的水量？", {"A": "6 公升", "B": "10 公升", "C": "16 公升", "D": "x 公升"}, "A", "一次函數 y＝6x＋10 的 x 係數 6 是變化率，表示每分鐘增加 6 公升；10 是初始量，選 A。", "區分斜率代表每單位輸入的變化量，截距代表 x＝0 時的初始值。", ["找出規則中的 x 係數 6。", "把 x 增加 1，y 的增加量為 6×1＝6。", "辨認常數 10 是起始水量，不是每分鐘增加量。", "附上單位，得到每分鐘 6 公升。", "選 A，檢查 y(1)−y(0)＝16−10＝6。"], "medium"),
    make(7, "直線型函數通過點 (0,4) 與 (2,10)。其關係式為何？", {"A": "y＝2x＋4", "B": "y＝3x＋4", "C": "y＝3x＋2", "D": "y＝4x＋3"}, "B", "斜率為 (10−4)÷(2−0)＝3；通過 x＝0、y＝4，所以截距為 4，關係式是 y＝3x＋4，選 B。", "用兩點求斜率，再用其中一點或 y 軸截距求常數項，最後回代兩點。", ["計算斜率 (10−4)÷(2−0)＝3。", "因為點 (0,4) 在圖上，x＝0 時 y＝4，所以截距為 4。", "寫出 y＝3x＋4。", "代入 x＝2 得 y＝10，符合第二點。", "選 B，兩個已知點都能通過才算完成驗證。"], "hard"),
    make(8, "某停車場收費函數 y＝30x＋20，其中 x 為停車小時數。20 在此規則中代表什麼？", {"A": "每小時費用", "B": "入場基本費", "C": "停車小時數", "D": "最多可停 20 小時"}, "B", "x＝0 時 y＝20，常數項代表不計時數仍先收取的基本費，因此選 B。", "把 x＝0 代入規則，觀察常數項的實際意義，再與 x 係數區分。", ["辨認 x 是停車小時數，30 是每小時增加費用。", "令 x＝0，得到 y＝20。", "因此 20 是尚未計入小時費用時的固定起始費。", "排除把 20 誤當成小時數或上限的說法。", "選 B，確認總費用由基本費加上 30x 組成。"], "medium"),
    make(9, "函數 y＝−3x＋12 中，x 增加 2 時，y 如何改變？", {"A": "增加 6", "B": "減少 3", "C": "減少 6", "D": "減少 12"}, "C", "斜率 −3 表示 x 每增加 1，y 減少 3；x 增加 2 時 y 減少 3×2＝6，選 C。", "用斜率乘以輸入變化量，負號用來判斷輸出是增加還是減少。", ["找出斜率 −3。", "確認 x 的變化量為 2。", "計算 y 的變化量 −3×2＝−6。", "把負的變化量解讀為減少 6。", "選 C，直接比較 y(x) 與 y(x＋2) 也得到差 −6。"], "medium"),
    make(10, "某計程車費用 y＝25x＋85 元，x 為行駛公里數。若預算不超過 210 元，最多可行駛幾公里？", {"A": "4 公里", "B": "5 公里", "C": "6 公里", "D": "8 公里"}, "B", "25x＋85≤210，得 25x≤125，再得 x≤5；因此最多 5 公里，選 B。", "把預算限制寫成一次不等式，解出上限後再考慮距離的實際意義。", ["建立費用不超過預算：25x＋85≤210。", "兩邊同減 85，得 25x≤125。", "兩邊同除以正數 25，得 x≤5。", "把上限解讀為最多行駛 5 公里。", "選 B，代入 5 得 210 元，符合不超過預算。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-9-10"
KG = "kg-math-content-s-9-10"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "三角形中線、重心二比一、座標平均、面積分割與平衡點意義", "observedPattern": "公立學校公開數學試題常以中線交點、頂點到重心的二比一關係、座標平均與面積分割考查重心推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-9-10-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供三角形重心能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的重心能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "三角形的重心是哪些線的交點？", {"A": "三邊垂直平分線", "B": "三條中線", "C": "三個內角平分線", "D": "三條高的延長線"}, "B", "三角形重心是三條中線的共同交點，選 B。", "先抓住重心的定義，再與外心、內心、垂心的構造區分。", ["回想重心的定義。", "每條中線連接頂點與對邊中點。", "三條中線必共點。", "共同交點稱為重心。", "選 B。"], "easy"),
    make(2, "重心 G 在中線 AM 上，M 是 BC 的中點。AG：GM 為何？", {"A": "1：1", "B": "1：2", "C": "2：1", "D": "3：1"}, "C", "重心把每條中線由頂點到對邊中點分成 AG：GM＝2：1，所以選 C。", "確認比例方向是『頂點到重心』比『重心到中點』，避免顛倒。", ["確認 AM 是中線。", "辨認 A 是頂點、M 是對邊中點。", "套用重心二比一性質。", "得到 AG：GM＝2：1。", "選 C。"], "easy"),
    make(3, "若中線 AM 長 18 公分，從頂點 A 到重心 G 的長度是多少？", {"A": "6 公分", "B": "9 公分", "C": "12 公分", "D": "16 公分"}, "C", "AG 是整條中線的 2/3，所以 AG＝18×2/3＝12 公分，選 C。", "先把二比一轉成頂點段占整條中線的 2/3。", ["寫出 AG：GM＝2：1。", "整條 AM 對應 2＋1＝3 份。", "AG 占 AM 的 2/3。", "計算 18×2/3＝12 公分。", "選 C。"], "medium"),
    make(4, "三角形頂點為 A(0,0)、B(6,0)、C(0,9)，其重心座標為何？", {"A": "(2,3)", "B": "(3,2)", "C": "(6,9)", "D": "(0,3)"}, "A", "重心座標是三頂點坐標的平均：(0＋6＋0)/3＝2，(0＋0＋9)/3＝3，因此為 (2,3)，選 A。", "分別平均三個 x 坐標與三個 y 坐標，不能只平均兩個頂點。", ["列出三個 x 坐標 0、6、0。", "列出三個 y 坐標 0、0、9。", "計算 xG＝6/3＝2。", "計算 yG＝9/3＝3。", "選 A。"], "medium"),
    make(5, "D 是 BC 的中點，G 是 △ABC 的重心。G 在中線 AD 上的位置為何？", {"A": "AD 的中點", "B": "距 A 為 AD 的 1/3", "C": "距 A 為 AD 的 2/3", "D": "D 點本身"}, "C", "重心距頂點 A 為中線 AD 的 2/3，因此 AG＝2/3 AD，選 C。", "以頂點 A 為比例起點，使用重心二比一而不是從 D 反向讀取。", ["確認 D 是 BC 中點，所以 AD 是中線。", "重心位於 AD 上。", "套用 AG：GD＝2：1。", "得到 AG＝2/3 AD。", "選 C。"], "easy"),
    make(6, "三角形的三條中線是否一定交於同一點？", {"A": "不一定，只有等腰三角形才會", "B": "一定，交點就是重心", "C": "只有直角三角形才會", "D": "一定互相平行"}, "B", "任意三角形的三條中線必共點，該共同交點稱為重心，選 B。", "把『中線必共點』視為重心的基本定理，不以三角形特殊形狀為前提。", ["確認題目談的是任意三角形。", "回想三條中線的共點性。", "共點不需要等腰或直角條件。", "共同交點命名為重心。", "選 B。"], "easy"),
    make(7, "若重心 G 到對邊中點 M 的距離 GM 為 4 公分，則同一中線的 AG 為多少？", {"A": "2 公分", "B": "4 公分", "C": "6 公分", "D": "8 公分"}, "D", "AG：GM＝2：1，所以 AG＝2×4＝8 公分，選 D。", "用已知的重心到中點段反推頂點到重心段。", ["確認 GM 是中線的後一段。", "寫出 AG：GM＝2：1。", "令 GM 的 1 份為 4 公分。", "AG 是 2 份，等於 8 公分。", "選 D。"], "easy"),
    make(8, "下列哪種方法可用來檢核候選點 G 是否為三角形 ABC 的重心？", {"A": "只確認 G 到 A、B 等距", "B": "確認 G 是兩條中線的交點", "C": "確認 G 在一條邊上", "D": "確認 G 到三邊距離相等"}, "B", "兩條中線的交點必同時落在第三條中線上，因此可確認 G 是重心；其餘條件分別對應外心、邊界或內心概念，選 B。", "用中線交點檢核重心，不要把等距條件混成外心或內心。", ["先找出各對邊的中點。", "由兩個頂點連到對邊中點形成兩條中線。", "檢查候選點 G 是否同時在兩條中線上。", "兩線交點即為三線共同交點。", "選 B。"], "medium"),
    make(9, "三角形三頂點坐標為 (1,2)、(7,2)、(4,8)，重心的 y 坐標是多少？", {"A": "2", "B": "4", "C": "8/3", "D": "12"}, "B", "重心 y 坐標為 (2＋2＋8)/3＝12/3＝4，所以選 B。", "只計算題目要求的 y 坐標，但仍要平均三個頂點的 y 值。", ["擷取三頂點 y 坐標 2、2、8。", "將三個 y 值相加得 12。", "除以頂點數 3。", "得到 yG＝4。", "選 B。"], "medium"),
    make(10, "三角形的一條中線把三角形分成兩個區域。這兩個區域的面積有何關係？", {"A": "一定相等", "B": "大區域是小區域兩倍", "C": "只在正三角形相等", "D": "無法由中線判定"}, "A", "中線兩側三角形共享相同的高，且底邊是被中點分成的兩段等長，因此兩區域面積相等，選 A。", "從底邊等分與同高兩個條件推導面積，不要誤以為需要正三角形。", ["中線通過對邊中點。", "對邊被分成兩段等長。", "兩小三角形對同一直線有相同高。", "面積＝底×高÷2，底相等且高相同。", "選 A。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

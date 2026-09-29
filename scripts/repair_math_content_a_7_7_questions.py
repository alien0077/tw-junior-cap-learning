import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-7"
KG = "kg-math-content-a-7-7"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"一元一次不等式、數線端點、負數乘除反向、雙重不等式與生活條件","observedPattern":"公立學校公開數學試題常以不等號辨識、數線表示、負係數反向、雙重不等式及至少／至多情境考查不等式解集；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-7-7-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供一元一次不等式能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的不等式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"下列哪一個是含有未知數的不等式？",{"A":"3x＋1＞7","B":"3x＋1＝7","C":"3＋1＝4","D":"x＝2"},"A","A 使用大於號連結含有 x 的兩個式子，屬於不等式，選 A。","先看是否含未知數，再辨認連接符號是否為不等號。",["檢查各選項是否含有 x。","辨認 A 使用 ＞。","大於號表示兩邊大小關係而非相等。","因此 A 是不等式。","選 A。"],"easy"),
make(2,"不等式 x≥−1 在數線上應如何表示？",{"A":"−1 空心點，向右","B":"−1 實心點，向右","C":"−1 空心點，向左","D":"−1 實心點，向左"},"B","x≥−1 包含端點 −1，且是比 −1 大的數，所以用實心點並向右，選 B。","先判斷是否包含端點，再由大小方向決定陰影方向。",["看到 ≥，端點 −1 要包含。","包含端點用實心點。","x 大於 −1 表示向右。","組合成實心點、向右射線。","選 B。"],"easy"),
make(3,"解不等式 x＋5≤12，解集為何？",{"A":"x≤7","B":"x≥7","C":"x≤17","D":"x≥17"},"A","兩邊同減 5 得 x≤7，所以選 A。","像解方程式一樣使用等量運算，但保留不等號方向。",["原式為 x＋5≤12。","兩邊同減 5。","左邊剩 x，右邊為 7。","得到 x≤7。","選 A。"],"easy"),
make(4,"解不等式 −3x＜9，x 的解為何？",{"A":"x＜−3","B":"x＞−3","C":"x＜3","D":"x＞3"},"B","兩邊同除以負數 −3 時不等號反向，得到 x＞−3，選 B。","遇到負數乘除一定反向，先寫出操作再判斷方向。",["原式為 −3x＜9。","兩邊同除以 −3。","因除以負數，不等號反向。","得到 x＞−3。","選 B。"],"medium"),
make(5,"某活動至少需要 25 人參加。若 x 表示參加人數，哪個不等式合適？",{"A":"x＞25","B":"x≤25","C":"x≥25","D":"x＜25"},"C","『至少 25』包含 25 且可以更多，應寫 x≥25，選 C。","把關鍵詞至少轉成包含等號的方向。",["找出條件詞『至少』。","至少表示不小於指定數值。","因此 x 大於或等於 25。","寫成 x≥25。","選 C。"],"easy"),
make(6,"若不等式 x−4＞−1，哪個數一定是它的解？",{"A":"2","B":"3","C":"4","D":"5"},"D","移項得 x＞3；選項中只有 5 大於 3，所以選 D。","先求完整解集，再逐一判斷候選數是否符合嚴格不等號。",["原式為 x−4＞−1。","兩邊同加 4 得 x＞3。","比較候選數與 3。","5 符合大於 3，3 不包含在解集中。","選 D。"],"easy"),
make(7,"解雙重不等式 −2≤x＋3＜4，解集為何？",{"A":"−5≤x＜1","B":"−1≤x＜7","C":"−5≤x＜7","D":"−2≤x＜4"},"A","三段同減 3 得 −5≤x＜1，選 A。","雙重不等式的三個部分要同步做同一運算。",["原式為 −2≤x＋3＜4。","三段同時減 3。","左邊變 −5，中間變 x，右邊變 1。","得到 −5≤x＜1。","選 A。"],"medium"),
make(8,"在數線上表示 x＜4 時，端點 4 應使用哪種記號？",{"A":"實心點，向左","B":"空心點，向左","C":"實心點，向右","D":"空心點，向右"},"B","x＜4 不包含 4，所以端點用空心點；小於 4 的數在左方，選 B。","先辨認嚴格不等號，再確認數線方向。",["看到 ＜，4 不屬於解集。","不包含端點用空心點。","小於 4 的數位於左側。","所以畫向左的射線。","選 B。"],"easy"),
make(9,"若 2x＋3≥3，x＝0 是否為解？",{"A":"是，代入後等號成立","B":"否，代入後左邊小於右邊","C":"否，因為 x 必須為正數","D":"無法判定"},"A","代入 x＝0 得 2×0＋3＝3，符合 ≥，因此 x＝0 是解，選 A。","直接代入候選值，不能把 ≥ 誤讀成必須嚴格大於。",["將 x＝0 代入左邊。","計算 2×0＋3＝3。","比較 3≥3 成立。","等號端點被包含在解集中。","選 A。"],"easy"),
make(10,"解不等式 7−2x≤1，x 為何？",{"A":"x≤3","B":"x≥3","C":"x≤−3","D":"x≥−3"},"B","兩邊同減 7 得 −2x≤−6，再除以負數 −2 並反向，得 x≥3，選 B。","先移除常數，再處理負係數並反向不等號。",["原式為 7−2x≤1。","兩邊同減 7 得 −2x≤−6。","兩邊同除以 −2。","不等號反向成 x≥3。","選 B。"],"medium")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

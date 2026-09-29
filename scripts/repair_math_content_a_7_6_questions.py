import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-6"
KG = "kg-math-content-a-7-6"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"二元一次聯立方程式與坐標平面、直線斜率截距、交點、平行線及截距三角形","observedPattern":"公立學校公開數學試題常把聯立方程式轉成直線圖形，判讀點在線上、斜率截距、交點、平行與坐標軸截距；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-7-6-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供二元一次聯立方程式幾何意義能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的聯立方程式幾何能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"點 (3，4) 是否在直線 x＋y＝7 上？",{"A":"是","B":"否，左邊為 6","C":"否，左邊為 8","D":"無法判定"},"A","代入 x＝3、y＝4，左邊 3＋4＝7，符合方程式，所以在直線上，選 A。","把點的兩個坐標依序代入方程式，檢查等號是否成立。",["取 x＝3、y＝4。","代入左邊 x＋y。","計算 3＋4＝7。","與右邊 7 相等。","選 A。"],"easy"),
make(2,"方程式 x＝−2 在坐標平面上代表哪種圖形？",{"A":"水平直線","B":"垂直直線","C":"拋物線","D":"通過原點的斜線"},"B","x 坐標固定為 −2、y 可取任意值，因此是通過 (−2,0) 的垂直直線，選 B。","看哪個坐標被固定：固定 x 是垂直線，固定 y 是水平線。",["觀察方程式只固定 x。","x 永遠等於 −2。","y 可自由變動。","所有點排列成垂直方向。","選 B。"],"easy"),
make(3,"直線 y＝−3x＋5 的斜率與 y 截距分別為何？",{"A":"3、5","B":"−3、−5","C":"−3、5","D":"5、−3"},"C","與 y＝mx＋b 比較，m＝−3、b＝5，選 C。","先整理成斜截式，再辨認 x 的係數與常數項。",["確認方程式已是 y＝mx＋b。","讀出 x 的係數 m＝−3。","讀出常數 b＝5。","依題目順序寫斜率、y 截距。","選 C。"],"easy"),
make(4,"兩直線 y＝2x＋1 與 y＝7−x 的交點為何？",{"A":"(1，3)","B":"(2，4)","C":"(2，5)","D":"(3，7)"},"C","令兩式的 y 相等：2x＋1＝7−x，得 x＝2，再代回 y＝5，所以交點為 (2,5)，選 C。","交點的同一坐標必同時滿足兩條直線方程式。",["令 2x＋1＝7−x。","整理得 3x＝6，x＝2。","代入 y＝2x＋1。","得到 y＝5。","寫成 (2，5)，選 C。"],"medium"),
make(5,"直線 y＝4x＋3 與 y＝4x−2 的關係為何？",{"A":"平行且不重合","B":"垂直","C":"相交於 (0,0)","D":"完全重合"},"A","兩線斜率同為 4，但 y 截距分別為 3、−2，因此平行且不重合，選 A。","比較斜率判方向，再比較截距判斷是否為同一直線。",["讀出第一線斜率 4、截距 3。","讀出第二線斜率 4、截距 −2。","斜率相同表示方向相同。","截距不同表示不是同一條線。","選 A。"],"easy"),
make(6,"若聯立方程式的兩條直線方程式完全相同，幾何上代表什麼？",{"A":"沒有交點","B":"只有一個交點","C":"兩條垂直線","D":"兩線重合，有無限多個共同點"},"D","兩條方程式代表同一條直線，所有線上點都同時滿足兩式，因此有無限多組解，選 D。","把代數的方程式相同轉成幾何上的同一直線。",["比較兩個方程式的所有係數。","確認它們可化成完全相同的式子。","因此代表同一條直線。","同一直線上每一點都是共同解。","選 D。"],"medium"),
make(7,"直線 3x＋y＝10 上的點 (2，y) 中，y 為何？",{"A":"2","B":"4","C":"6","D":"8"},"B","代入 x＝2：3×2＋y＝10，得 6＋y＝10，所以 y＝4，選 B。","固定 x 後直接用直線方程式解出另一個坐標。",["取 x＝2。","代入 3x＋y＝10。","得到 6＋y＝10。","兩邊減 6 得 y＝4。","代回檢核後選 B。"],"easy"),
make(8,"直線 2x＋y＝8 與兩坐標軸圍成的三角形面積為何？",{"A":"8 平方單位","B":"12 平方單位","C":"16 平方單位","D":"32 平方單位"},"C","令 y＝0 得 x＝4；令 x＝0 得 y＝8。三角形面積＝1/2×4×8＝16，選 C。","先求兩個軸截距，再用直角三角形面積公式。",["令 y＝0 求 x 截距 4。","令 x＝0 求 y 截距 8。","兩截距與原點形成直角三角形。","面積＝4×8÷2＝16。","選 C。"],"medium"),
make(9,"若兩條非垂直直線相交於 (4，−1)，這個交點對聯立方程式代表什麼？",{"A":"兩個方程式的共同解","B":"只有第一式的解","C":"兩線的 y 截距","D":"兩線斜率的平均"},"A","交點同時位於兩條直線上，因此 (4,−1) 同時滿足兩個方程式，是聯立方程式的共同解，選 A。","把幾何位置翻譯成代數條件：在兩線上就是同時滿足兩式。",["確認點在第一條直線上。","確認同一點也在第二條直線上。","因此其坐標代入兩式皆成立。","這正是聯立方程式共同解的定義。","選 A。"],"easy"),
make(10,"聯立方程式 2x＋y＝6、x−y＝0 的圖形交點為何？",{"A":"(1，1)","B":"(2，2)","C":"(3，0)","D":"(0，6)"},"B","由 x−y＝0 得 x＝y；代入 2x＋y＝6 得 3x＝6，x＝2、y＝2，選 B。","先利用較簡單的直線關係 x＝y，再代入另一式。",["由 x−y＝0 得 x＝y。","代入 2x＋y＝6 得 3x＝6。","解得 x＝2。","因 x＝y，得到 y＝2。","寫成 (2，2)，選 B。"],"medium")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

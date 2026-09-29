import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-5"
KG = "kg-math-content-a-7-5"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"二元一次聯立方程式的代入、消去、特殊解情形與票價、幾何及數量應用","observedPattern":"公立學校公開數學試題常以代入消去法、情境聯立建模、唯一解與相依方程式判讀考查二元一次聯立方程式；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-7-5-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供二元一次聯立方程式解法與應用能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的聯立方程式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"解聯立方程式 x＋y＝11、x−y＝3，(x，y) 為何？",{"A":"(4，7)","B":"(7，4)","C":"(8，3)","D":"(6，5)"},"B","兩式相加得 2x＝14，所以 x＝7；代回得 y＝4，選 B。","先相加消去相反的 y 項，再回代。",["將兩式相加。","得到 2x＝14。","解得 x＝7。","代入 x＋y＝11 得 y＝4。","檢核 7−4＝3，選 B。"],"easy"),
make(2,"若 3x＋y＝14 且 x＝4，y 為何？",{"A":"1","B":"2","C":"3","D":"4"},"B","把 x＝4 代入 3x＋y＝14，得 12＋y＝14，所以 y＝2，選 B。", "先代入已知的 x，再解一元一次方程式。",["以 x＝4 代入第一式。","得到 3×4＋y＝14。","化為 12＋y＝14。","解得 y＝2。","代回確認後選 B。"],"easy"),
make(3,"若 x＝y＋2 且 2x＋y＝13，則 (x，y) 為何？",{"A":"(3，5)","B":"(4，3)","C":"(5，3)","D":"(6，1)"},"C","代入得 2(y＋2)＋y＝13，3y＝9，所以 y＝3，x＝5，選 C。","先代入再整理。",["代入 x＝y＋2。","得到 2(y＋2)＋y＝13。","整理為 3y＋4＝13，得 y＝3。","回代得 x＝5。","檢核 10＋3＝13，選 C。"],"medium"),
make(4,"解聯立方程式 2x＋3y＝12、x＋y＝5，(x，y) 為何？",{"A":"(1，4)","B":"(2，3)","C":"(3，2)","D":"(4，1)"},"C","第一式減去第二式的 2 倍得 y＝2，再由 x＋y＝5 得 x＝3，選 C。","用倍乘消去 x。",["將第二式乘 2 得 2x＋2y＝10。","用第一式減去它，得到 y＝2。","代回 x＋y＝5。","解得 x＝3。","檢核 6＋6＝12，選 C。"],"medium"),
make(5,"成人票每張 50 元、學生票每張 30 元，共售 20 張、收入 760 元。成人票有幾張？",{"A":"6 張","B":"8 張","C":"10 張","D":"12 張"},"B","x＋y＝20、50x＋30y＝760；代 y＝20−x 得 20x＋600＝760，x＝8，選 B。","先用總張數代換一個未知數，再用金額式求解。",["列 x＋y＝20。","列 50x＋30y＝760。","以 y＝20−x 代入金額式。","得 20x＝160，所以 x＝8。","選 B。"],"medium"),
make(6,"解聯立方程式 3x＋2y＝16、x−2y＝0，(x，y) 為何？",{"A":"(2，1)","B":"(3，2)","C":"(4，2)","D":"(5，1)"},"C","第二式得 x＝2y，代入第一式 6y＋2y＝16，y＝2，x＝4，選 C。","利用 x 與 y 的簡單關係代入。",["由 x−2y＝0 得 x＝2y。","代入 3x＋2y＝16。","得 6y＋2y＝16。","解得 y＝2，再得 x＝4。","檢核兩式後選 C。"],"medium"),
make(7,"解聯立方程式 y＝2x−1、x＋y＝8，(x，y) 為何？",{"A":"(2，5)","B":"(3，5)","C":"(4，7)","D":"(5，9)"},"B","代入得 x＋2x−1＝8，3x＝9，x＝3，y＝5，選 B。","把已知的 y 表示式代入另一式。",["取 y＝2x−1。","代入 x＋y＝8。","得到 3x−1＝8，故 3x＝9。","解得 x＝3、y＝5。","代回確認後選 B。"],"easy"),
make(8,"某矩形長比寬多 4 公分，周長為 32 公分。若長為 x、寬為 y，長與寬各為何？",{"A":"長 8、寬 4", "B":"長 10、寬 6", "C":"長 12、寬 8", "D":"長 14、寬 10"},"B","x−y＝4 且 2x＋2y＝32，即 x＋y＝16；相加得 2x＝20，x＝10，y＝6，選 B。","先把文字條件轉成差與周長兩式，再消去。",["長比寬多 4 得 x−y＝4。","周長得 2x＋2y＝32，化為 x＋y＝16。","兩式相加得 2x＝20。","解得 x＝10、y＝6。","檢核差與周長後選 B。"],"medium"),
make(9,"下列哪個有序數對是 2x＋y＝11、x＋2y＝10 的解？",{"A":"(2，7)","B":"(3，5)","C":"(4，3)","D":"(5，2)"},"C","代入 (4,3)：2×4＋3＝11 且 4＋2×3＝10，兩式皆成立，選 C。","逐一把候選有序數對代入兩式，必須同時成立。",["取選項 C 的 x＝4、y＝3。","檢查第一式得 8＋3＝11。","檢查第二式得 4＋6＝10。","確認兩式同時成立。","選 C。"],"easy"),
make(10,"聯立方程式 4x＋2y＝10、2x＋y＝5 的解有何情形？",{"A":"無解","B":"唯一解","C":"剛好兩組解","D":"無限多組解"},"D","第一式除以 2 正好得到第二式，兩式代表同一直線，因此有無限多組解，選 D。","比較兩式是否只是非零倍數，判斷是否為同一條方程線。",["觀察第一式 4x＋2y＝10。","兩邊同除以 2 得 2x＋y＝5。","這與第二式完全相同。","兩式沒有提供獨立限制，解有無限多組。","選 D。"],"medium")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

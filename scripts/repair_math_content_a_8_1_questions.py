import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-1"
KG = "kg-math-content-a-8-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"平方和、平方差、差平方、二項式乘法、恆等式與幾何／估算情境","observedPattern":"公立學校公開數學試題常以乘法公式展開、公式辨識、數值估算、正方形面積與代數式化簡考查二次式結構；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-8-1-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供二次式乘法公式能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的乘法公式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"展開 (x＋5)²，結果為何？",{"A":"x²＋5x＋25","B":"x²＋10x＋25","C":"x²＋25","D":"x²＋10x＋5"},"B","利用 (x＋5)²＝x²＋2×5x＋5²，得 x²＋10x＋25，選 B。","辨認為和的平方，記得中間項是兩倍乘積。",["套用 (a＋b)²＝a²＋2ab＋b²。","令 a＝x、b＝5。","計算 2ab＝10x。","計算 b²＝25。","合併得 x²＋10x＋25，選 B。"],"easy"),
make(2,"展開 (a−4)²，結果為何？",{"A":"a²−4a＋16","B":"a²＋8a＋16","C":"a²−8a＋16","D":"a²−16"},"C","(a−4)²＝a²−2×4a＋4²＝a²−8a＋16，選 C。","差的平方中間項為負的兩倍乘積，不能只把兩項各自平方。",["套用 (a−b)²＝a²−2ab＋b²。","令 a 為字母 a、b＝4。","中間項為 −8a。","常數平方為 16。","得到 a²−8a＋16，選 C。"],"easy"),
make(3,"化簡 (3x＋2)(3x−2)，結果為何？",{"A":"9x²＋4","B":"6x²−4","C":"9x²−4","D":"9x²−12x＋4"},"C","這是平方差 (A＋B)(A−B)＝A²−B²，令 A＝3x、B＝2，得 9x²−4，選 C。","先辨識共軛二項式，使用平方差可省去四項相乘。",["確認兩括號首項相同、次項相反。","套用 (A＋B)(A−B)＝A²−B²。","令 A＝3x、B＝2。","計算 A²＝9x²、B²＝4。","得到 9x²−4，選 C。"],"medium"),
make(4,"展開 (x＋6)(x＋2)，結果為何？",{"A":"x²＋8x＋12","B":"x²＋12x＋8","C":"x²＋4x＋12","D":"x²＋8"},"A","逐項相乘：x²＋2x＋6x＋12＝x²＋8x＋12，選 A。","不是平方公式時，將每一項與另一括號每一項相乘，再合併同類項。",["計算 x×x＝x²。","計算 x×2＝2x。","計算 6×x＝6x。","計算 6×2＝12 並合併 2x＋6x。","得到 x²＋8x＋12，選 A。"],"easy"),
make(5,"展開 (2y−3)²，結果為何？",{"A":"4y²−12y＋9","B":"4y²−6y＋9","C":"2y²−12y＋9","D":"4y²＋12y＋9"},"A","(2y−3)²＝(2y)²−2×(2y)×3＋3²＝4y²−12y＋9，選 A。","先把整個 2y 視為第一項，再套差的平方。",["令 A＝2y、B＝3。","平方第一項得 4y²。","中間項為 −2×2y×3＝−12y。","平方第二項得 9。","合併得 4y²−12y＋9，選 A。"],"medium"),
make(6,"下列哪個恆等式正確？",{"A":"(u＋v)²＝u²＋v²","B":"(u−v)²＝u²−v²","C":"(u＋v)²＝u²＋2uv＋v²","D":"(u＋v)(u−v)＝u²＋v²"},"C","和的平方公式為 u²＋2uv＋v²，因此選 C；其餘漏掉中間項或符號錯誤。","逐一對照平方和、平方差的標準公式與中間項。",["回想 (u＋v)² 的完整公式。","確認中間項必為 2uv。","確認最後一項為 v²。","對照選項 C 完全符合。","選 C。"],"easy"),
make(7,"正方形邊長為 101 公分，用 (100＋1)² 估算其面積，結果為何？",{"A":"10001 平方公分","B":"10100 平方公分","C":"10201 平方公分","D":"10401 平方公分"},"C","(100＋1)²＝100²＋2×100×1＋1²＝10000＋200＋1＝10201，選 C。","把接近整百的數拆成和，再用平方公式快速計算。",["將 101 寫成 100＋1。","套用和的平方公式。","計算 10000、200 與 1。","相加得到 10201 平方公分。","選 C。"],"medium"),
make(8,"化簡 (t＋3)(t−4)，結果為何？",{"A":"t²＋t−12","B":"t²−t−12","C":"t²−7t＋12","D":"t²＋7t−12"},"B","逐項相乘得 t²−4t＋3t−12＝t²−t−12，選 B。","分別處理四個乘積，特別注意 3×(−4) 的負號。",["計算 t×t＝t²。","計算 t×(−4)＝−4t。","計算 3×t＝3t。","計算 3×(−4)＝−12並合併同類項。","得到 t²−t−12，選 B。"],"medium"),
make(9,"化簡 (z＋1)²−z²，結果為何？",{"A":"1","B":"2z＋1","C":"z²＋1","D":"2z"},"B","(z＋1)²＝z²＋2z＋1，減去 z² 後剩 2z＋1，選 B。","先完整展開平方，再觀察 z² 項相消。",["展開 (z＋1)² 得 z²＋2z＋1。","寫出 (z²＋2z＋1)−z²。","消去相反的 z² 項。","剩下 2z＋1。","選 B。"],"medium"),
make(10,"化簡 (2m＋5)²−(2m−5)²，結果為何？",{"A":"20m","B":"40m","C":"4m²＋25","D":"100"},"B","令 A＝2m、B＝5，原式為 (A＋B)²−(A−B)²＝4AB＝4×2m×5＝40m，選 B。","把兩個平方的差轉為公式，避免分別展開後再相減。",["辨認為 (A＋B)²−(A−B)²。","套用結果 4AB。","令 A＝2m、B＝5。","計算 4×2m×5＝40m。","選 B。"],"hard")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

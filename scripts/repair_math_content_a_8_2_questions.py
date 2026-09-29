import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-8-2"
KG = "kg-math-content-a-8-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"多項式的項、次數、係數、常數項、同類項、標準式、降冪排列與多項式辨識","observedPattern":"公立學校公開數學試題常以多項式的結構辨識、最高次數、項與係數、同類項、標準排列及幾何面積表示考查代數表徵；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-8-2-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供多項式意義能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的多項式能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"在多項式 5x³−2x＋7 中，共有幾項？",{"A":"2 項","B":"3 項","C":"4 項","D":"5 項"},"B","以加減號分項為 5x³、−2x、7，共 3 項，選 B。","按加減號切分項，負號要跟著後面的項。",["將式子分成 5x³、−2x、7。","確認每段是一個項。","共數得 3 段。","常數 7 也算一項。","選 B。"],"easy"),
make(2,"多項式 4a⁵−a²＋7a−1 的次數為何？",{"A":"1","B":"2","C":"4","D":"5"},"D","最高次項 4a⁵ 的次數為 5，所以多項式次數是 5，選 D。","找出變數最高次方，不要以係數大小判斷次數。",["列出各項次數 5、2、1、0。","找最大次數。","最高次數為 5。","係數 4 不影響次數。","選 D。"],"easy"),
make(3,"在多項式 −9x³＋4x−6 中，x³ 項的係數為何？",{"A":"−9","B":"9","C":"−6","D":"3"},"A","x³ 項是 −9x³，乘在 x³ 前面的數為 −9，選 A。","先定位指定次方的項，再讀取其前面的有號數字。",["找出含 x³ 的項。","該項為 −9x³。","辨認 x³ 前面的乘數。","保留負號得到 −9。","選 A。"],"easy"),
make(4,"在多項式 5y⁴−2y²−6 中，常數項為何？",{"A":"5","B":"−2","C":"y²","D":"−6"},"D","不含 y 的項是 −6，因此常數項為 −6，選 D。","找不含變數的項，並保留其正負號。",["分出 5y⁴、−2y²、−6。","檢查各項是否含 y。","只有 −6 不含變數。","因此 −6 是常數項。","選 D。"],"easy"),
make(5,"下列哪一組是同類項？",{"A":"3x² 與 −7x²","B":"4a 與 4a²","C":"5mn 與 5m","D":"2x²y 與 2xy²"},"A","同類項必須含有相同變數及相同次方；3x² 與 −7x² 符合，選 A。","逐項比較變數種類與每個變數的次方，不只比較係數。",["檢查 A 的變數都是 x。","確認兩項的 x 次方都為 2。","係數可不同而不影響同類項判定。","所以 A 是同類項組。","選 A。"],"medium"),
make(6,"將 2x＋5x³−1＋3x² 化為降冪排列的標準形式，結果為何？",{"A":"5x³＋3x²＋2x−1","B":"−1＋2x＋3x²＋5x³","C":"5x³＋2x＋3x²−1","D":"3x²＋5x³＋2x−1"},"A","依次數 3、2、1、0 排列，得 5x³＋3x²＋2x−1，選 A。","先辨認各項次數，再從最高次排到常數項。",["列出 5x³、3x²、2x、−1。","依次數標成 3、2、1、0。","由高次到低次排列。","寫成 5x³＋3x²＋2x−1。","選 A。"],"medium"),
make(7,"多項式 7t²−3t＋1 有幾項、次數為何？",{"A":"2 項，次數 2","B":"3 項，次數 1","C":"3 項，次數 2","D":"4 項，次數 2"},"C","項為 7t²、−3t、1，共 3 項；最高次為 2，選 C。","分別回答項數與最高次數，避免把常數項漏掉。",["按加減號分出三項。","數得項數為 3。","比較次方 2、1、0。","最高次數為 2。","選 C。"],"easy"),
make(8,"下列哪一個不是 x 的多項式？",{"A":"3x²−1","B":"x⁴＋2x","C":"7−5x³","D":"1/x＋2"},"D","1/x 可寫成 x⁻¹，含負次方，不符合多項式次方須為非負整數，選 D。","檢查變數的次方是否為 0 或正整數，分母中的變數會造成負次方。",["觀察各選項中的 x 次方。","A、B、C 的次方皆為非負整數。","D 的 1/x 等於 x⁻¹。","負次方不能作為多項式項次。","選 D。"],"medium"),
make(9,"長方形長為 x＋4、寬為 x−2，用 x 表示面積，哪個多項式正確？",{"A":"x²＋2x−8","B":"x²−2x−8","C":"x²＋6x＋8","D":"x²＋2x＋8"},"A","面積＝(x＋4)(x−2)＝x²−2x＋4x−8＝x²＋2x−8，選 A。","把幾何量相乘後，用二項式逐項相乘並合併同類項。",["列面積 (x＋4)(x−2)。","計算 x×x＝x²。","計算 x×(−2)與 4×x。","計算 4×(−2)並合併，得 x²＋2x−8。","選 A。"],"medium"),
make(10,"若一多項式的最高次項為 −2z⁴，另有 5z² 與 9，哪個敘述正確？",{"A":"次數為 2","B":"最高次項係數為 4","C":"常數項為 −2","D":"次數為 4、常數項為 9"},"D","最高次項 −2z⁴ 表示次數 4；不含 z 的常數項是 9，選 D。","分開判讀最高次項提供的次數與係數，以及獨立的常數項。",["查看最高次項 −2z⁴。","讀出多項式次數為 4。","找不含 z 的項 9。","確認常數項為 9。","選 D。"],"medium")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

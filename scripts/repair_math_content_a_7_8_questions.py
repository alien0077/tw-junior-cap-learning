import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-a-7-8"
KG = "kg-math-content-a-7-8"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]
def refs():
    return [{**s,"subject":"math","locator":"一元一次不等式解集、整數限制、預算、年齡、周長、方案比較與數量上限","observedPattern":"公立學校公開數學試題常將不等式轉成預算、年齡、周長、費用與數量限制，並要求考慮整數解與最大／最小值；本題只取能力方向。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def make(i,prompt,options,answer,explanation,strategy,steps,difficulty):
    return {"id":f"question-math-content-a-7-8-{i}","subject":"math","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in options.items()],"knowledgeIds":[KG],"difficulty":difficulty,"answer":{"value":answer,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三份公立學校公開數學試題僅供一元一次不等式解與應用能力方向研究；未複製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三筆公立學校公開數學試題的不等式應用能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-10","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
Q=[
make(1,"解不等式 5x＋1≤21，哪個解集正確？",{"A":"x≤4","B":"x≥4","C":"x≤22","D":"x≥22"},"A","兩邊同減 1 得 5x≤20，再除以 5 得 x≤4，選 A。","先隔離未知數，再把解集方向與邊界寫清楚。",["原式為 5x＋1≤21。","兩邊同減 1 得 5x≤20。","兩邊同除以正數 5。","得到 x≤4。","選 A。"],"easy"),
make(2,"每份材料 22 元，另有固定包裝費 8 元，預算不超過 120 元。最多可買幾份？",{"A":"4 份","B":"5 份","C":"6 份","D":"7 份"},"B","設份數 n，22n＋8≤120，得 22n≤112，n≤112/22＝5.09；n 為整數，最多 5 份，選 B。","先列總費用不等式，再依份數必須是整數取最大可行值。",["列出 22n＋8≤120。","移除固定費得 22n≤112。","除以 22 得 n≤5.09…。","份數只能是整數，最大可取 5。","檢查 22×5＋8＝118，選 B。"],"medium"),
make(3,"小安今年 x 歲，四年後至少 18 歲。現在的年齡至少為多少？",{"A":"12 歲","B":"13 歲","C":"14 歲","D":"22 歲"},"C","四年後年齡 x＋4≥18，所以 x≥14，現在至少 14 歲，選 C。","把時間變化寫成代數式，再將『至少』轉為 ≥。",["今年年齡為 x。","四年後為 x＋4。","至少 18 歲列 x＋4≥18。","兩邊減 4 得 x≥14。","選 C。"],"easy"),
make(4,"長方形寬為 3 公分、長為 x 公分；若周長不超過 22 公分，x 的最大值為何？",{"A":"5 公分","B":"7 公分","C":"8 公分","D":"11 公分"},"C","2(x＋3)≤22，除以 2 得 x＋3≤11，所以 x≤8，最大值為 8，選 C。","將幾何限制轉成周長不等式，再求長的上限。",["寫出周長 2(長＋寬)。","列 2(x＋3)≤22。","兩邊除以 2 得 x＋3≤11。","減 3 得 x≤8。","選 C。"],"medium"),
make(5,"方案甲月費 60 元、每次使用 8 元；方案乙月費 90 元、每次使用 5 元。使用 x 次時，何時方案甲不比方案乙貴？",{"A":"x≤10","B":"x≥10","C":"x≤30","D":"x≥30"},"A","甲不比乙貴：60＋8x≤90＋5x，得 3x≤30，所以 x≤10，選 A。","先把兩方案各自表示成費用，再依『不比貴』寫 ≤。",["甲費用為 60＋8x。","乙費用為 90＋5x。","列 60＋8x≤90＋5x。","整理得 3x≤30，故 x≤10。","選 A。"],"medium"),
make(6,"解不等式 −3x＋9≥0，哪個解集正確？",{"A":"x≥3","B":"x≤3","C":"x≥−3","D":"x≤−3"},"B","兩邊同減 9 得 −3x≥−9，再除以負數 −3 反向，得 x≤3，選 B。","最後一步除以負數時務必翻轉不等號。",["原式為 −3x＋9≥0。","兩邊同減 9 得 −3x≥−9。","兩邊同除以 −3。","不等號反向成 x≤3。","選 B。"],"medium"),
make(7,"某電影院規定兒童票數 x 不得超過成人票數的 2 倍；成人票有 5 張。哪個不等式表示限制？",{"A":"x≥10","B":"x≤10","C":"x＜10","D":"x＋5≤2"},"B","兒童票不得超過 2×5＝10 張，表示 x≤10，選 B。","先算成人票的兩倍，再把『不超過』翻成 ≤。",["成人票數為 5。","其兩倍為 10。","兒童票數不得超過此數。","寫成 x≤10。","選 B。"],"easy"),
make(8,"若 1≤2x＋3＜9，整數 x 的解有幾個？",{"A":"2 個","B":"3 個","C":"4 個","D":"5 個"},"C","三段同減 3 得 −2≤2x＜6，再除以 2 得 −1≤x＜3；整數為 −1、0、1、2，共 4 個，選 C。","先解雙重不等式，再列出整數而非只看實數區間長度。",["三段同減 3 得 −2≤2x＜6。","三段同除以正數 2。","得到 −1≤x＜3。","列整數 −1、0、1、2。","共 4 個，選 C。"],"medium"),
make(9,"停車場入場費 25 元，每小時 35 元；若預算至多 130 元，最多可停幾小時？",{"A":"2 小時","B":"3 小時","C":"4 小時","D":"5 小時"},"B","25＋35h≤130，得 35h≤105，所以 h≤3，最多 3 小時，選 B。","將固定費加上時數費列出預算不等式。",["固定入場費為 25。","時數費為 35h。","列 25＋35h≤130。","移項得 35h≤105，再除以 35 得 h≤3。","選 B。"],"easy"),
make(10,"社團先收 120 元，每月活動費 35 元，總預算不超過 400 元，最多可參加幾個月？",{"A":"6 個月","B":"7 個月","C":"8 個月","D":"9 個月"},"C","120＋35m≤400，得 35m≤280，m≤8，所以最多 8 個月，選 C。","先扣除一次性費用，再用每月費用求整數月數上限。",["列總費用 120＋35m≤400。","兩邊減 120 得 35m≤280。","除以 35 得 m≤8。","月份為整數，最大為 8。","選 C。"],"medium")]
for question in Q:
    (OUT/f"{question['id']}.json").write_text(json.dumps(question,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(Q)} questions")

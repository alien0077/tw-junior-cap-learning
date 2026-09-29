import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-8"
KG = "kg-math-content-s-8-8"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "三角形內角和、外角、等腰／等邊三角形、邊角大小關係與三角不等式", "observedPattern": "公開學校數學試題常以角度計算、外角關係、等腰條件、對邊對角與三角不等式考查三角形基本性質；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-8-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供三角形基本性質能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的三角形性質方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "三角形 ABC 中，∠A=52°、∠B=68°，∠C 為多少？", {"A":"50°","B":"60°","C":"70°","D":"80°"}, "B", "三角形內角和為 180°，∠C=180°−52°−68°=60°，選 B。", "用三角形 180° 總和扣除已知兩角，並核對選項字母。", ["寫出三角形內角和 180°。","先相加已知角 52+68=120。","用 180−120=60。","把 60° 對照選項。","選 B。"], "easy"),
make(2, "三角形 ABC 在 C 點的外角為 125°，遠端兩內角中 ∠A=55°，則 ∠B 為多少？", {"A":"55°","B":"60°","C":"70°","D":"125°"}, "C", "外角等於兩個遠端內角和，所以 125°=55°+∠B，∠B=70°，選 C。", "使用外角定理，而不是把外角直接當成相鄰內角。", ["辨認 C 點外角與遠端內角 A、B。","列出外角=∠A+∠B。","125=55+∠B。","解得 ∠B=70°。","把 70° 對照選項，選 C。"], "medium"),
make(3, "等腰三角形的兩腰相等，若頂角為 40°，每一個底角為多少？", {"A":"40°","B":"60°","C":"70°","D":"80°"}, "C", "兩底角相等，且兩底角和=180°−40°=140°，每個為 70°，選 C。", "先用等腰三角形的底角相等，再用內角和平均分配。", ["頂角為 40°。","剩餘兩底角和為 180−40=140°。","等腰條件使兩底角相等。","140÷2=70°。","選 C。"], "medium"),
make(4, "等邊三角形的每一個內角是多少？", {"A":"45°","B":"60°","C":"90°","D":"120°"}, "B", "三個內角相等且總和 180°，每角=180°÷3=60°，選 B。", "利用三邊相等帶來三角相等，再平均分配內角和。", ["等邊三角形有三個相等內角。","三角形內角和是 180°。","將 180° 平分成三份。","每角為 60°。","選 B。"], "easy"),
make(5, "下列哪一組長度可以組成三角形？", {"A":"2、3、5","B":"3、4、6","C":"1、2、4","D":"2、2、5"}, "B", "任兩邊和必須大於第三邊；3+4>6、3+6>4、4+6>3，所以 3、4、6 可以，選 B。", "只需檢查最短兩邊和是否大於最長邊，其他兩項會自動成立。", ["找每組的最長邊。","檢查最短兩邊和是否大於最長邊。","A：2+3=5，不大於 5。","B：3+4=7，大於 6。","因此選 B。"], "medium"),
make(6, "在同一三角形中，若邊 AB 大於邊 AC，則哪個角較大？", {"A":"∠A 大於 ∠B","B":"∠C 大於 ∠B","C":"∠B 大於 ∠C","D":"無法比較"}, "B", "大邊對大角；AB 的對角是 ∠C，AC 的對角是 ∠B，AB>AC 所以 ∠C>∠B，選 B。", "先找每條邊的對角，再套用大邊對大角。", ["找 AB 的對角為 ∠C。","找 AC 的對角為 ∠B。","已知 AB>AC。","所以 ∠C>∠B。","選 B。"], "medium"),
make(7, "三角形一個外角為 120°，兩個遠端內角相差 20°。較大的遠端內角是多少？", {"A":"50°","B":"60°","C":"70°","D":"100°"}, "C", "設較大角 x、較小角 x−20，則 x+(x−20)=120，2x=140，x=70°，選 C。", "把外角拆成兩遠端內角的和，再配合差量列方程。", ["設較大角為 x。","較小角為 x−20。","外角定理給 x+(x−20)=120。","解得 2x=140，x=70。","選 C。"], "medium"),
make(8, "等腰三角形兩底角各為 65°，頂角是多少？", {"A":"40°","B":"50°","C":"60°","D":"65°"}, "B", "頂角=180°−65°−65°=50°，選 B。", "先利用兩底角相等確認兩個 65°，再用三角形內角和。", ["兩底角各為 65°。","兩底角和為 130°。","頂角補足 180°。","180−130=50°。","選 B。"], "easy"),
make(9, "若三角形三邊中最長邊為 9，哪個角必為最大角？", {"A":"最長邊的兩端角之一","B":"最長邊的對角","C":"任意角都可能","D":"最短邊的對角"}, "B", "三角形中最長邊所對的角最大，因此是最長邊的對角，選 B。", "關係是『邊與其對角』，不能選最長邊的端點角。", ["找出最長邊。","不要看它的端點，而要找對面頂點。","連接對面頂點形成的角就是對角。","大邊對大角。","選 B。"], "easy"),
make(10, "某三角形兩邊長為 7 與 10，第三邊 x 為整數。下列哪個 x 不可能？", {"A":"4","B":"6","C":"16","D":"17"}, "D", "三角不等式要求 |10−7|<x<10+7，即 3<x<17；整數 17 不符合，選 D。", "用兩邊差與兩邊和建立第三邊的嚴格範圍。", ["兩邊差為 10−7=3。","兩邊和為 10+7=17。","第三邊必須滿足 3<x<17。","4、6、16 符合，17 不符合嚴格小於。","選 D。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

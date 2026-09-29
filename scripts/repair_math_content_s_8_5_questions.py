import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-5"
KG = "kg-math-content-s-8-5"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "三角形全等、對應頂點／邊／角、SSS／SAS／ASA／AAS／RHS 判定與不足條件反例", "observedPattern": "公開學校數學試題常以三角形配對、全等判定必要位置、直角三角形與反例辨識考查幾何推理；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-5-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供三角形全等判定能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的三角形全等方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "若 △ABC 與 △DEF 的對應關係為 A↔D、B↔E、C↔F，則哪一組邊互為對應邊？", {"A":"AB 與 DE","B":"AB 與 EF","C":"BC 與 DF","D":"AC 與 DE"}, "A", "由頂點配對 A↔D、B↔E，可得邊 AB 對應 DE，選 A。", "先把三個頂點一一配對，再用邊的兩端點同步移換。", ["列出 A 對 D。","列出 B 對 E。","邊 AB 的兩端點換成 D、E。","所以對應邊是 DE。","選 A。"], "easy"),
make(2, "兩個三角形的三組對應邊長分別為 5、7、9 公分且相等，依哪個判定可知兩三角形全等？", {"A":"SSS","B":"SAS","C":"ASA","D":"RHS"}, "A", "三組對應邊相等符合邊邊邊判定 SSS，選 A。", "先統計已知邊與角的數量，不要因為邊長有數字就誤判為 SAS。", ["已知第一組邊相等。","已知第二組邊相等。","已知第三組邊相等。","三組全是邊，沒有指定角。","使用 SSS，選 A。"], "easy"),
make(3, "兩個三角形有兩邊及其夾角分別相等，哪一項最能說明其全等？", {"A":"兩邊夾角相等，為 SAS","B":"兩邊任意角相等，為 SSA","C":"三角相等，為 AAA","D":"一邊兩角相等，為 AAS"}, "A", "兩邊及夾在其中的角相等是 SAS 判定，選 A。", "關鍵在角是否位於兩條已知邊的夾角位置。", ["找出兩組等長邊。","定位題目指定的角。","確認角的兩側正是這兩組邊。","資料排列為邊、角、邊。","選 A。"], "medium"),
make(4, "兩個三角形有兩角及其夾邊分別相等，這是何種判定？", {"A":"SSS","B":"SAS","C":"ASA","D":"SSA"}, "C", "兩角中間的邊相等，形成角邊角 ASA 判定，選 C。", "辨認那條邊是否連接兩個已知角。", ["確認有兩個相等角。","找出兩角共同夾住的邊。","該邊也相等。","排列為角、邊、角。","使用 ASA，選 C。"], "medium"),
make(5, "若兩個三角形有兩角及一個非夾邊分別相等，哪個判定可用？", {"A":"AAS","B":"SAS","C":"SSS","D":"AAA"}, "A", "兩角及非夾邊相等是角角邊 AAS 判定，選 A。", "先確認已知邊不是兩角之間的夾邊，才能區分 AAS 與 ASA。", ["列出兩個已知角。","定位已知的那一條邊。","確認它不在兩角之間。","資料排列為角、角、邊。","使用 AAS，選 A。"], "medium"),
make(6, "兩個直角三角形的斜邊及一股分別相等，能用哪個判定？", {"A":"RHS","B":"AAA","C":"SSA（一般情況）","D":"只有 SSS"}, "A", "直角三角形的斜邊與一股相等，使用 RHS（直角－斜邊－股）判定，選 A。", "先確認兩個三角形都含直角，再辨認斜邊與一股的組合。", ["兩個圖形都是直角三角形。","找出各自的斜邊。","確認斜邊相等。","再確認一股相等。","符合 RHS，選 A。"], "medium"),
make(7, "兩個三角形的三個角分別相等，為什麼不能只靠這項資料判定全等？", {"A":"AAA 只保證形狀相同，大小未固定","B":"角度不能用來比較三角形","C":"三角形沒有三個角","D":"AAA 一定會使邊長不等"}, "A", "AAA 可判定相似，但同形狀可以有不同大小，故不能直接判定全等，選 A。", "檢查資料是否包含至少一個尺度長度，分清相似與全等。", ["三角相等代表形狀角度一致。","但沒有給出任何實際邊長。","可將其中一圖等比例放大。","放大後角仍相等但不全等。","選 A。"], "medium"),
make(8, "兩個三角形有兩邊及一個非夾角相等（SSA），通常為何不能直接判定全等？", {"A":"可能有兩種不同形狀符合資料","B":"SSA 一定代表相似","C":"因為三角形不能有兩邊","D":"只要角不是 90° 就一定全等"}, "A", "SSA 一般不能唯一決定三角形，可能出現兩個不同形狀，因此不足以判定全等，選 A。", "檢查角的位置，避免把非夾角誤當成 SAS。", ["辨認兩邊已知相等。","確認已知角不在兩邊之間。","所以資料是 SSA，不是 SAS。","SSA 可能產生不同構形。","選 A。"], "medium"),
make(9, "若 △ABC ≅ △DEF，且 ∠B=72°、EF=8 公分，則下列哪項一定正確？", {"A":"∠E=72° 且 BC=8 公分","B":"∠D=72° 且 AB=8 公分","C":"∠F=72° 且 AC=8 公分","D":"∠E=108° 且 BC=16 公分"}, "A", "順序 A↔D、B↔E、C↔F，所以 ∠B=∠E=72°，邊 BC 對應 EF，BC=8 公分，選 A。", "同時使用頂點順序配對角與邊，再逐項核對。", ["由順序得到 B 對 E。","因此 ∠E=∠B=72°。","由順序得到 BC 對 EF。","所以 BC=EF=8 公分。","選 A。"], "medium"),
make(10, "下列哪組資料足以判定兩個直角三角形全等？", {"A":"兩個銳角分別相等","B":"一個銳角與一股相等","C":"斜邊與一股分別相等","D":"兩股成比例"}, "C", "直角三角形的斜邊與一股分別相等符合 RHS 判定，足以判定全等，選 C。", "把直角這個共同條件列入，再找能鎖定尺度的長度資料。", ["兩個三角形都有直角。","檢查選項 C 提供斜邊相等。","再提供一股相等。","這是 RHS 的完整條件。","選 C。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

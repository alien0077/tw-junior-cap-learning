import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-8-4"
KG = "kg-math-content-s-8-4"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]

def refs():
    return [{**s, "subject": "math", "locator": "全等圖形、剛體移動、對應頂點、SSS／SAS／ASA／AAS 判定與全等／相似辨析", "observedPattern": "公開學校數學試題常以三角形對應、全等判定條件、符號順序與全等後邊角推理考查幾何證據；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-8-4-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供全等圖形與三角形判定能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公立學校公開數學試題的全等能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "兩個圖形的形狀與大小完全相同，只需平移、旋轉或翻轉即可重合，這兩個圖形稱為什麼？", {"A":"全等圖形","B":"相似圖形","C":"對稱圖形","D":"平行圖形"}, "A", "能透過剛體移動完全重合，表示對應長度與角度都相同，稱為全等圖形，選 A。", "先判斷是否能完全重合，再區分全等與只有形狀相同的相似。", ["列出允許的剛體移動：平移、旋轉、翻轉。","這些移動不改變長度與角度。","題目說移動後完全重合。","符合全等圖形定義。","選 A。"], "easy"),
make(2, "下列哪一種操作一定不會改變圖形的長度與角度？", {"A":"等比例放大","B":"平移","C":"沿一軸伸長","D":"任意壓扁"}, "B", "平移是剛體移動，不改變圖形的大小與角度；放大或伸長會改變長度，選 B。", "辨認剛體移動與會改變尺度的變形。", ["平移只改變位置。","各點移動相同距離與方向。","點與點間距離不變。","角度也因此保持。","選 B。"], "easy"),
make(3, "兩個三角形的三組對應邊分別相等，足以判定兩三角形全等的判定是什麼？", {"A":"SSS","B":"SAS","C":"ASA","D":"AAA"}, "A", "三組對應邊相等是邊邊邊判定，記為 SSS，選 A。", "把已知資料分類成邊 S 或角 A，再辨認判定型態。", ["三組資料都是邊長。","沒有使用角度資料。","三邊對應相等。","這正是 Side-Side-Side。","選 A。"], "easy"),
make(4, "兩個三角形有兩組對應邊相等，且夾角也相等，使用哪個全等判定？", {"A":"SSS","B":"SAS","C":"ASA","D":"AAA"}, "B", "兩邊及其夾角相等是邊角邊判定 SAS，選 B。", "關鍵是角必須位於兩條已知邊之間，不能只看到兩邊一角就忽略位置。", ["找出兩組相等邊。","確認已知角位於這兩邊之間。","資料排列為 Side-Angle-Side。","因此使用 SAS 判定。","選 B。"], "medium"),
make(5, "兩個三角形有兩角及其夾邊分別相等，最適合使用哪個判定？", {"A":"SSS","B":"SAS","C":"ASA","D":"SSA"}, "C", "兩角及夾在兩角之間的邊相等，是角邊角判定 ASA，選 C。", "辨認兩個角之間的那一條邊是否為夾邊。", ["分類已知資料為兩個角與一條邊。","確認該邊連接兩個已知角。","排列為 Angle-Side-Angle。","所以判定是 ASA。","選 C。"], "medium"),
make(6, "若 △ABC ≅ △DEF，對應頂點的順序表示 A 對應哪一點？", {"A":"D","B":"E","C":"F","D":"無法判定"}, "A", "全等符號兩邊的頂點按順序對應，所以 A 對應 D，B 對應 E，C 對應 F，選 A。", "先逐位置配對符號兩側的字母，不以圖形紙面方向猜測。", ["讀取第一個三角形順序 A-B-C。","讀取第二個三角形順序 D-E-F。","第一位置 A 對第二位置 D。","因此 A 的對應點是 D。","選 A。"], "easy"),
make(7, "若 △ABC ≅ △DEF，且 AB=7 公分，則哪個長度一定等於 7 公分？", {"A":"DE","B":"EF","C":"DF","D":"只有 BC"}, "A", "由頂點順序 A↔D、B↔E，所以邊 AB 對應 DE，長度相等為 7 公分，選 A。", "先配對端點，再把對應邊的長度相等寫出來。", ["由全等順序得到 A 對 D。","由全等順序得到 B 對 E。","因此 AB 對應 DE。","全等圖形對應邊等長。","選 A。"], "medium"),
make(8, "兩個三角形三邊比例相同，但其中一個是另一個的 2 倍。它們的關係最可能是什麼？", {"A":"一定全等","B":"相似但不全等","C":"一定垂直","D":"沒有任何關係"}, "B", "對應邊成固定比例 2，形狀相同但大小不同，屬相似而非全等，選 B。", "比較對應長度是相等還是成比例，這是全等與相似的核心差異。", ["檢查三邊比例是否相同。","比例為 2，表示有尺度放大。","長度不是逐一相等。","因此不能稱全等，但可稱相似。","選 B。"], "medium"),
make(9, "已知兩三角形有兩組邊相等及一組非夾角相等（SSA），通常能否單獨判定全等？", {"A":"能，SSA 永遠是充分條件","B":"不能，可能形成不同形狀","C":"能，因為所有兩邊都相等","D":"只能判定它們平行"}, "B", "SSA 一般不足以唯一決定三角形，可能產生兩種不同形狀，因此不能單獨判定全等，選 B。", "檢查角的位置是否為兩已知邊的夾角，避免把 SSA 誤當 SAS。", ["辨認資料為兩邊與一個角。","確認角不是兩邊的夾角。","這是 SSA 而非 SAS。","SSA 一般無法唯一鎖定形狀。","選 B。"], "medium"),
make(10, "兩個三角形的三個角分別相等，為什麼通常不能直接判定全等？", {"A":"AAA 只保證形狀相同，大小可能不同","B":"角度相等會破壞邊長","C":"三角形不能比較角度","D":"AAA 一定代表三邊相等"}, "A", "AAA 可判定相似，卻不能決定尺度；同角度的三角形可能大小不同，因此不能直接判定全等，選 A。", "問自己是否有至少一個長度尺度，區分角度資訊和大小資訊。", ["三角形三角和固定，三角相等代表形狀相同。","但角度沒有提供實際長度。","可把其中一個三角形按比例放大。","放大後仍角相等但不全等。","選 A。"], "medium"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

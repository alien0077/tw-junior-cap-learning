import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-7-1"
KG = "kg-math-content-s-7-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [
        {
            **source,
            "subject": "math",
            "locator": "簡單圖形、點線角、線段／射線／直線辨識與幾何符號命名",
            "observedPattern": "公開學校數學資料常以圖形元素、端點與延伸方向、字母命名及角的頂點位置考查幾何語言轉譯；本題只取能力方向。",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "paper",
        }
        for source in SOURCES
    ]


def make(number, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {
        "id": f"question-math-content-s-7-1-{number}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": key, "text": value} for key, value in options.items()],
        "knowledgeIds": [KG],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCES[0]["url"],
            "sourceLocator": "三份公立學校公開數學資料僅供簡單圖形與幾何符號能力方向研究；未複製原題、選項、圖表或答案。",
            "authoringNote": "依官方課綱、KG 與公立學校公開數學資料的幾何語言能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-10",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": strategy,
        "solutionSteps": steps,
    }


QUESTIONS = [
    make(1, "幾何圖形中，若只想標示一個位置，最適合用哪一種記號？", {"A": "一個大寫英文字母，例如 P", "B": "兩個箭頭，例如 ↔", "C": "一段括號，例如 [PQ]", "D": "三個連續角符號"}, "A", "幾何中的點代表一個位置，通常以一個大寫英文字母標示，例如 P，選 A。", "先判斷題目描述的是位置還是延伸中的圖形，再選相應的符號。", ["辨認題目只要求標示一個位置。", "一個位置對應一個點。", "點通常用一個大寫英文字母命名。", "P 符合點的命名方式。", "選 A。"], "easy"),
    make(2, "線段 MN 和線段 NM 的關係，哪一項正確？", {"A": "一定是不同線段，因為字母順序不同", "B": "是同一線段，因為兩個端點相同", "C": "NM 是射線，MN 才是線段", "D": "只有 M 是端點"}, "B", "線段由兩個端點決定，MN 與 NM 都連接同一對端點，所以表示同一線段，選 B。", "檢查兩個名稱是否使用同一對端點；線段的字母順序不表示方向。", ["找出 MN 的兩個端點 M、N。", "再找出 NM 的兩個端點 N、M。", "確認兩者端點集合相同。", "線段沒有固定的起點方向。", "選 B。"], "easy"),
    make(3, "射線 AB 的 A 點是端點。若改寫成射線 BA，哪個資訊改變了？", {"A": "端點由 A 改成 B", "B": "線段長度變成兩倍", "C": "兩條射線都沒有端點", "D": "角的頂點必定改成 A"}, "A", "射線名稱的第一個字母表示端點，因此射線 AB 的端點是 A，射線 BA 的端點變成 B，選 A。", "看到射線先讀第一個字母，再判斷交換字母是否換了端點。", ["讀取射線 AB 的第一個字母 A。", "確認 A 是射線 AB 的端點。", "讀取射線 BA 的第一個字母 B。", "因此端點從 A 換成 B。", "選 A。"], "medium"),
    make(4, "一個圖形向左右兩個方向都無限延伸，且沒有端點，應稱為什麼？", {"A": "點", "B": "線段", "C": "射線", "D": "直線"}, "D", "沒有端點並向兩方延伸的是直線，選 D；線段有兩端點，射線只有一端點。", "用端點數量和延伸方向判斷，不用圖上畫出的長短判斷。", ["檢查圖形是否有端點。", "題目說沒有端點。", "檢查延伸方向是否為兩方。", "無端點且雙向延伸符合直線定義。", "選 D。"], "easy"),
    make(5, "在 ∠PQR 中，哪一點是頂點？", {"A": "P，因為它排在第一個", "B": "Q，因為它在三個字母中間", "C": "R，因為它排在最後一個", "D": "P 和 R 都是頂點"}, "B", "三字母角名的中間字母代表兩條邊的共同端點，所以 ∠PQR 的頂點是 Q，選 B。", "角的三字母命名先找中間字母，再把它對回兩邊交會的位置。", ["圈出角名 PQR 的中間字母。", "中間字母是 Q。", "角的中間字母表示頂點。", "P、R 表示兩邊上的方向點。", "選 B。"], "easy"),
    make(6, "從 C 點出發，經過 D 點向同一方向延伸的圖形，應用哪個名稱表示？", {"A": "線段 CD", "B": "射線 CD", "C": "射線 DC", "D": "直線 CD"}, "B", "圖形從 C 出發並經過 D 向一方延伸，是射線；第一個字母 C 是端點，因此寫成射線 CD，選 B。", "先判斷只有一端點一方向，再把端點放在射線名稱第一個位置。", ["題目描述一個端點與一個延伸方向。", "這種圖形是射線。", "端點是 C。", "射線名稱第一個字母要寫 C，方向點寫 D。", "選 B。"], "medium"),
    make(7, "下列哪一個敘述能正確辨認線段？", {"A": "只有一個端點，向一方無限延伸", "B": "有兩個端點，長度可由兩端點決定", "C": "沒有端點，向左右無限延伸", "D": "只有一個位置，沒有長度"}, "B", "線段有兩個端點，兩端點之間的距離就是線段長度，選 B。", "把三種線形放在同一張檢核表，比較端點數量和延伸方向。", ["檢查 A：一端點一方向是射線。", "檢查 B：兩端點且有限長度是線段。", "檢查 C：無端點雙向延伸是直線。", "檢查 D：一個位置是點。", "選 B。"], "easy"),
    make(8, "若 A、B、C 三點中 B 是兩條邊的共同端點，哪兩個角名可表示同一個角？", {"A": "∠ABC 與 ∠CBA", "B": "∠ABC 與 ∠ACB", "C": "∠BAC 與 ∠ABC", "D": "∠CAB 與 ∠BCA"}, "A", "∠ABC 與 ∠CBA 的中間字母都為 B，兩邊分別指向 A、C，因此表示同一個以 B 為頂點的角，選 A。", "比較兩個角名的中間字母與兩側端點；頂點相同且兩側互換才是同一角。", ["找出 ∠ABC 的中間字母 B。", "找出 ∠CBA 的中間字母 B。", "兩者的兩側字母都是 A、C，只是順序相反。", "因此兩個名稱指向同一對邊與同一頂點。", "選 A。"], "medium"),
    make(9, "學生把『一端點並向右延伸』的圖形命名為線段 XY。哪個回饋最適當？", {"A": "正確，因為線段一定向右", "B": "錯誤，應先確認它是射線，線段必須有兩個端點", "C": "正確，因為畫得越長越接近線段", "D": "錯誤，所有圖形都只能用一個字母"}, "B", "一端點加一個方向代表射線，不是線段；線段必須有兩個端點，選 B。", "遇到圖形命名錯誤，先用定義核對端點數量，再檢查延伸方向。", ["記錄題目給出的端點數量為一個。", "記錄圖形向一方延伸。", "一端點一方向符合射線。", "線段需要兩個端點，原命名不合定義。", "選 B。"], "medium"),
    make(10, "下列哪一項最能說明為什麼不能只看圖形畫得長短來判斷直線或線段？", {"A": "紙面上的圖形只是表示法，應依端點與延伸方向判斷", "B": "所有畫得長的圖形都是直線", "C": "所有畫得短的圖形都是線段", "D": "只要有箭頭就一定是線段"}, "A", "圖形在紙面上只能畫出有限長度，真正的分類依端點數量與是否向一方或兩方延伸判斷，因此選 A。", "把視覺長短和幾何定義分開，尋找能在不同畫法下仍成立的判準。", ["確認紙面無法真的畫出無限延伸。", "因此畫面長短不是可靠證據。", "改查端點數量。", "再查箭頭代表的延伸方向。", "選 A。"], "medium"),
]

for question in QUESTIONS:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(QUESTIONS)} questions")

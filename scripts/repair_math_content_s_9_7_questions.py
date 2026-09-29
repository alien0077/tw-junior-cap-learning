import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-s-9-7"
KG = "kg-math-content-s-9-7"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "點與圓位置、直線與圓交點、切線、弦、弦心距與切線長", "observedPattern": "公立學校公開數學試題常用圓心距離與半徑比較點或直線位置，並以切線、弦及直角三角形計算長度；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-s-9-7-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供點、直線與圓的關係能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的圓幾何能力方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "圓心 O 到點 P 的距離為 4 公分，圓半徑為 6 公分。點 P 位於圓的哪個位置？", {"A": "圓外", "B": "圓周上", "C": "圓內", "D": "無法判定"}, "C", "OP＝4 小於半徑 6，所以 P 在圓內，選 C。", "比較圓心到點的距離與半徑，不要只看點的圖示位置。", ["讀出 OP＝4 公分。", "讀出半徑 r＝6 公分。", "比較 4 與 6，得到 OP＜r。", "距離小於半徑代表點在圓內。", "選 C。"], "easy"),
    make(2, "一條直線到圓心的垂直距離為 3 公分，圓半徑為 5 公分。這條直線與圓有幾個交點？", {"A": "0 個", "B": "1 個", "C": "2 個", "D": "無限多個"}, "C", "直線到圓心的距離 3 小於半徑 5，因此直線穿過圓內部，與圓有兩個交點，選 C。", "用圓心到直線的最短距離和半徑比較來分類交點數。", ["找出圓心到直線距離 d＝3。", "找出半徑 r＝5。", "判斷 d＜r。", "直線會割圓，產生兩個交點。", "選 C。"], "easy"),
    make(3, "若直線到圓心的距離恰好等於圓半徑，直線與圓的關係為何？", {"A": "相離", "B": "相切", "C": "相交於兩點", "D": "完全重合"}, "B", "圓心到直線的距離等於半徑時，直線只有一個接觸點，稱為切線，選 B。", "記住 d＝r 是相切的臨界狀態，交點數為一個。", ["設圓心到直線距離為 d。", "題目給 d＝r。", "比較三種情況可知這是臨界位置。", "直線與圓只有一個公共點。", "選 B。"], "easy"),
    make(4, "圓半徑為 7 公分，一條直線到圓心的距離為 9 公分。直線與圓有幾個交點？", {"A": "0 個", "B": "1 個", "C": "2 個", "D": "7 個"}, "A", "距離 9 大於半徑 7，直線在圓外側，與圓沒有交點，選 A。", "先比較 d 與 r；d＞r 表示相離。", ["記下 d＝9 公分。", "記下 r＝7 公分。", "判斷 d＞r。", "直線與圓相離，公共點數為 0。", "選 A。"], "easy"),
    make(5, "半徑 5 公分的圓中，一條弦到圓心的距離為 3 公分。這條弦長為多少？", {"A": "6 公分", "B": "8 公分", "C": "10 公分", "D": "16 公分"}, "B", "圓心到弦的垂線平分弦，半弦為 √(5²－3²)＝4 公分，因此弦長為 8 公分，選 B。", "先求半弦，再乘二；不可把直角三角形中的半弦直接當整條弦。", ["半徑作為直角三角形斜邊 5。", "圓心到弦距離為一直角邊 3。", "求半弦＝√(25－9)＝4。", "整條弦＝2×4＝8 公分。", "選 B。"], "medium"),
    make(6, "直線 l 在 T 點與圓相切。下列哪項必然成立？", {"A": "OT 平行 l", "B": "OT 垂直 l", "C": "OT 等於 l 的長度", "D": "T 是圓心"}, "B", "切點的半徑 OT 必垂直切線 l，所以選 B。", "看到『相切』與『切點半徑』時，直接連結半徑垂直切線的性質。", ["確認 T 是切線 l 的接觸點。", "連接圓心 O 與 T。", "使用切點半徑與切線垂直。", "得到 OT⊥l。", "選 B。"], "easy"),
    make(7, "一條直線與圓相交於 A、B 兩點，線段 AB 在圓的幾何名稱是什麼？", {"A": "半徑", "B": "直徑", "C": "弦", "D": "切線"}, "C", "兩端點 A、B 都在圓周上的線段稱為弦；只有通過圓心才特別稱為直徑，選 C。", "先看線段兩端是否在圓周，再確認是否有通過圓心的額外條件。", ["確認 A、B 是直線與圓的兩個交點。", "所以 A、B 都在圓周上。", "兩個圓周點連成的線段是弦。", "題目沒有說 AB 通過圓心，不能稱直徑。", "選 C。"], "easy"),
    make(8, "圓半徑為 10 公分，直線到圓心的距離為 6 公分。若弦的中點為 M，圓心 O 到 M 的距離為多少？", {"A": "4 公分", "B": "6 公分", "C": "8 公分", "D": "16 公分"}, "B", "弦的中點到圓心的垂線距離就是圓心到弦的距離，因此 OM＝6 公分，選 B。", "辨認 M 是弦的中點後，直接把它與圓心到弦的最短距離對應。", ["題目給直線到 O 的距離為 6。", "弦是直線在圓內的部分。", "圓心到弦的垂線會通過弦中點 M。", "所以 OM 等於給定的最短距離 6。", "選 B。"], "medium"),
    make(9, "下列哪一條弦必然是圓內最長的弦？", {"A": "離圓心最遠的弦", "B": "通過圓心的弦", "C": "長度等於半徑的弦", "D": "與切線平行的弦"}, "B", "通過圓心的弦是直徑，長度為 2r，是圓內最長的弦，選 B。", "用弦心距判斷：弦越靠近圓心越長，距離為零時就是直徑。", ["回想圓內弦長與弦心距的關係。", "通過圓心的弦弦心距為 0。", "弦心距最小時弦長最大。", "該弦即為直徑，長度 2r。", "選 B。"], "medium"),
    make(10, "圓半徑為 5 公分，圓外點 P 到圓心 O 的距離為 13 公分。從 P 作圓的切線，切線段長為多少？", {"A": "5 公分", "B": "8 公分", "C": "12 公分", "D": "18 公分"}, "C", "切點 T 使 OT⊥PT，OPT 為直角三角形；PT＝√(13²－5²)＝√144＝12 公分，選 C。", "把切線段、半徑與外點距離組成直角三角形，再用畢氏定理求未知股。", ["連接外點 P 與切點 T 及圓心 O。", "使用半徑 OT 垂直切線 PT。", "列出 OP²＝OT²＋PT²，即 13²＝5²＋PT²。", "解得 PT＝√144＝12 公分。", "選 C。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

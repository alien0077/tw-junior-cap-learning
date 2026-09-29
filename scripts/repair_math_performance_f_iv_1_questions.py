import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-f-iv-1"
KG = "kg-math-performance-f-iv-1"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "常數函數、一次函數的函數值、斜率、截距、表格關係與生活情境建模", "observedPattern": "公開數學評量常由式子、兩點、對應表或費用情境判讀一次函數的斜率與截距，並要求代值、找截距或辨識水平線；本題只取能力方向與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-f-iv-1-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校／公開會考數學試題僅供一次函數、常數函數、斜率與截距能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的一次函數方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "若一次函數 f(x)=-2x+7，則 f(5) 為何？", {"A": "-5", "B": "-3", "C": "3", "D": "17"}, "B", "把 x=5 代入：f(5)=-2×5+7=-10+7=-3，所以選 B。", "先把函數輸入值完整代入，再依乘法與加減順序計算。", ["確認函數規則為 f(x)=-2x+7。", "以 5 取代式中的 x。", "得到 -2×5+7。", "先算 -10，再加 7 得 -3。", "所以選 B，並檢查代入的是 5 而不是函數值。"], "easy"),
    make(2, "直線 y=1/2 x-4 的斜率為何？", {"A": "-4", "B": "-1/2", "C": "1/2", "D": "4"}, "C", "一次函數 y=mx+b 中，x 的係數 m 就是斜率；本式 m=1/2，選 C。", "先整理成 y=mx+b 的形式，再直接讀取 x 的係數。", ["辨認本式已是 y=mx+b。", "找出 x 前面的係數。", "該係數為 1/2。", "截距 -4 不影響斜率。", "所以選 C。"], "easy"),
    make(3, "下列哪一個關係是常數函數？", {"A": "y=3x-1", "B": "y=-2x+5", "C": "y=6", "D": "y=x/3"}, "C", "常數函數的輸出不隨 x 改變，形式可寫成 y=b；只有 y=6 符合，選 C。", "觀察式子是否含有 x 項；沒有 x 且輸出固定，就是常數函數。", ["檢查各選項是否含 x。", "A、B、D 的輸出都會隨 x 改變。", "C 的輸出永遠是 6。", "因此 C 的函數值與輸入無關。", "所以選 C。"], "easy"),
    make(4, "通過點 (2,5) 與 (6,13) 的一次函數，其斜率為何？", {"A": "1", "B": "2", "C": "3", "D": "4"}, "B", "斜率=(13-5)/(6-2)=8/4=2，所以選 B。", "用後點減前點的 y，再除以對應的 x 差；順序前後一致即可。", ["取兩點的 y 差：13-5=8。", "取兩點的 x 差：6-2=4。", "套用斜率公式 Δy/Δx。", "計算 8/4=2。", "所以選 B，並確認分母不是 y 差。"], "medium"),
    make(5, "直線 y=-3x+9 與 x 軸交點的 x 坐標為何？", {"A": "-3", "B": "0", "C": "3", "D": "9"}, "C", "x 軸上的點 y=0，代入 0=-3x+9，得 3x=9，所以 x=3，選 C。", "找 x 軸交點時先設定 y=0，再解一次方程。", ["確認 x 軸上所有點的 y 座標都是 0。", "令 -3x+9=0。", "移項得 -3x=-9，或 3x=9。", "解得 x=3。", "所以選 C。"], "medium"),
    make(6, "某共享單車收費為起始 20 元，每使用 1 小時加收 12 元。使用 5 小時的費用為何？", {"A": "60 元", "B": "72 元", "C": "80 元", "D": "92 元"}, "C", "費用函數為 y=20+12x；代入 x=5 得 20+60=80 元，選 C。", "先辨認固定費是截距、每小時費是斜率，再代入使用時間。", ["固定起始費為 20 元。", "5 小時的變動費為 12×5=60 元。", "將固定費與變動費相加。", "總費用 20+60=80 元。", "所以選 C，不能把 20 元也乘以 5。"], "medium"),
    make(7, "某一次函數滿足 x=1 時 y=4、x=3 時 y=10，則此函數為何？", {"A": "y=2x+2", "B": "y=3x+1", "C": "y=3x-1", "D": "y=4x"}, "B", "斜率=(10-4)/(3-1)=3；代入 (1,4) 得 4=3×1+b，所以 b=1，函數為 y=3x+1，選 B。", "先用兩點求斜率，再用其中一點求截距，最後代回另一點驗算。", ["由兩點求斜率：(10-4)/(3-1)=3。", "設函數為 y=3x+b。", "代入 (1,4)：4=3+b，得 b=1。", "寫出 y=3x+1。", "代入 (3,10) 可驗算，故選 B。"], "hard"),
    make(8, "常數函數 y=-4 的圖形是何種直線？", {"A": "通過原點的斜直線", "B": "斜率為 -4 的直線", "C": "平行 x 軸的水平直線", "D": "平行 y 軸的垂直直線"}, "C", "y=-4 不論 x 為何都固定，所有點的 y 座標相同，因此圖形是平行 x 軸的水平直線，選 C。", "看哪個座標固定；y 固定代表水平，x 固定才代表垂直。", ["觀察函數沒有 x 項。", "所以每個輸入都得到 y=-4。", "圖上所有點的 y 座標相同。", "y 相同的點會形成水平線。", "所以選 C。"], "easy"),
    make(9, "直線 y=2x-8 與 y 軸交點的座標為何？", {"A": "(0,-8)", "B": "(-8,0)", "C": "(0,2)", "D": "(2,0)"}, "A", "y 軸上的點 x=0；代入 y=2×0-8=-8，因此交點為 (0,-8)，選 A。", "找 y 軸截距時令 x=0，並記得座標順序是 (x,y)。", ["確認 y 軸上的 x 座標為 0。", "代入得到 y=2×0-8。", "計算 y=-8。", "組成座標 (0,-8)。", "所以選 A，不能把 x 與 y 順序交換。"], "easy"),
    make(10, "正比關係 y=kx 通過點 (4,10)。當 x=6 時，y 為何？", {"A": "12", "B": "15", "C": "16", "D": "24"}, "B", "由 10=4k 得 k=10/4=5/2；x=6 時 y=(5/2)×6=15，選 B。", "正比題先用已知點求比例常數 k，再代入新的 x。", ["把已知點 (4,10) 代入 y=kx。", "得 10=4k，所以 k=5/2。", "把 x=6 代入 y=kx。", "計算 y=(5/2)×6=15。", "所以選 B，並確認正比圖形通過原點。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-2"
KG = "kg-math-performance-a-iv-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "一元一次方程式的等量操作、括號、分數／小數係數、文字建模、無解與恆等式；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常要求將文字條件列式，依等量公理解未知數，並以代回或矛盾檢查答案；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-a-iv-2-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供一元一次方程式能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的方程式解題方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "解方程式 3x+4=19，x 為何？", {"A":"4", "B":"6", "C":"7", "D":"5"}, "D", "兩邊減 4 得 3x=15，再除以 3 得 x=5，所以選 D。", "先移除常數項，再除以未知數的係數。", ["寫下 3x+4=19。", "兩邊同減 4，得 3x=15。", "兩邊同除以 3，得 x=5。", "將 x=5 代回，3×5+4=19。", "所以選 D。"], "easy"),
make(2, "解方程式 5x-7=18，x 為何？", {"A":"6", "B":"7", "C":"5", "D":"4"}, "C", "兩邊加 7 得 5x=25，再除以 5 得 x=5，正確答案為 C。", "把減去的 7 加回去，再處理係數 5。", ["原式為 5x-7=18。", "兩邊同加 7，得 5x=25。", "兩邊同除以 5，得 x=5。", "代回左邊 25-7=18。", "所以選 C。"], "easy"),
make(3, "解方程式 2(x+3)=14，x 為何？", {"A":"3", "B":"4", "C":"5", "D":"7"}, "B", "先兩邊除以 2 得 x+3=7，再減 3 得 x=4，因此選 B。", "括號外有共同係數時，先用除法消去係數可減少展開錯誤。", ["觀察括號外係數為 2。", "兩邊同除以 2，得到 x+3=7。", "兩邊同減 3，得到 x=4。", "檢查 2(4+3)=14。", "所以選 B。"], "easy"),
make(4, "解方程式 4x-5=2x+9，x 為何？", {"A":"7", "B":"5", "C":"2", "D":"14"}, "A", "兩邊減 2x 得 2x-5=9，再加 5 得 2x=14，故 x=7，選 A。", "先把未知數集中在一側，再把常數集中到另一側。", ["由 4x-5=2x+9 開始。", "兩邊同減 2x，得 2x-5=9。", "兩邊同加 5，得 2x=14。", "兩邊同除以 2，得 x=7。", "代回 28-5=14+9，成立，選 A。"], "medium"),
make(5, "解方程式 x/3+2=5，x 為何？", {"A":"3", "B":"6", "C":"9", "D":"12"}, "C", "兩邊減 2 得 x/3=3，再乘以 3 得 x=9，所以選 C。", "先孤立分數項，最後乘上分母消除分數。", ["原式為 x/3+2=5。", "兩邊同減 2，得 x/3=3。", "兩邊同乘 3，得 x=9。", "代回 9/3+2=5。", "所以選 C。"], "medium"),
make(6, "長方形長為 x+2 公分、寬為 x 公分，周長 28 公分，x 為何？", {"A":"5", "B":"6", "C":"7", "D":"8"}, "B", "周長為 2[(x+2)+x]=28，化簡得 4x+4=28，所以 x=6，正確答案為 B。", "先用長方形周長公式列式，再整理同類項解未知數。", ["周長公式是 2(長+寬)。", "代入得到 2[(x+2)+x]=28。", "括號內合併為 2x+2，左式為 4x+4。", "兩邊減 4 再除以 4，得到 x=6。", "寬為 6、長為 8，周長 28，選 B。"], "medium"),
make(7, "解方程式 0.4x+3=7，x 為何？", {"A":"4", "B":"7", "C":"10", "D":"16"}, "C", "兩邊減 3 得 0.4x=4，再除以 0.4 得 x=10，因此選 C。", "先移除常數，再用小數係數除法；可將 0.4 改寫成 4/10 輔助檢查。", ["原式為 0.4x+3=7。", "兩邊同減 3，得 0.4x=4。", "兩邊同除以 0.4，得 x=10。", "代回 0.4×10+3=7。", "所以選 C。"], "medium"),
make(8, "解方程式 3(x-2)+4=2x+9，x 為何？", {"A":"9", "B":"10", "C":"11", "D":"12"}, "C", "展開左式得 3x-2=2x+9，兩邊減 2x 再加 2，得到 x=11，選 C。", "先正確分配括號係數，再集中未知數與常數。", ["將 3 分配到括號，左式成為 3x-6+4。", "合併常數得 3x-2=2x+9。", "兩邊同減 2x，得 x-2=9。", "兩邊同加 2，得 x=11。", "代回 3(11-2)+4=31，右式 22+9=31，選 C。"], "medium"),
make(9, "方程式 2x+3=2x+7 的解為何？", {"A":"x=4", "B":"所有數都是解", "C":"無解", "D":"x=2"}, "C", "兩邊同減 2x 後得到 3=7，形成矛盾，因此沒有任何 x 能滿足，正確答案為 C。", "先消去相同的未知項，觀察剩餘的常數是否矛盾。", ["從 2x+3=2x+7 開始。", "兩邊同減 2x，未知項完全消去。", "剩下 3=7。", "這個等式不可能成立。", "因此方程式無解，選 C。"], "medium"),
make(10, "方程式 4(x+1)=4x+4 的解為何？", {"A":"只有 x=1", "B":"所有數都是解", "C":"無解", "D":"只有 x=4"}, "B", "展開左式為 4x+4，與右式完全相同；對所有 x 都成立，所以選 B。", "化簡兩邊並比較是否成為恆等式，而不是任意指定一個 x。", ["展開左式 4(x+1)，得到 4x+4。", "右式本來就是 4x+4。", "兩邊化簡後完全相同。", "因此任意數代入都會成立。", "所以所有數都是解，選 B。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

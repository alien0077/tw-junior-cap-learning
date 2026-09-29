import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-4"
KG = "kg-math-performance-a-iv-4"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "二元一次聯立方程式的代入／消去、文字情境建模、唯一解、無解、無限多解與圖形交點；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常把兩個未知量放入總量、價格、幾何或圖形交點情境，要求列出兩個條件並檢查共同解；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-a-iv-4-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供二元一次聯立方程式能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的聯立方程式解題方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "若 x+y=10 且 x-y=2，則 (x,y) 為何？", {"A":"(4,6)", "B":"(5,5)", "C":"(8,2)", "D":"(6,4)"}, "D", "兩式相加得 2x=12，所以 x=6；代回 x+y=10 得 y=4，正確答案為 D。", "先相加消去 y，再把求出的 x 代回任一原式。", ["列出 x+y=10。", "列出 x-y=2。", "兩式相加，得到 2x=12。", "求得 x=6，代回得 y=4。", "所以選 D。"], "easy"),
make(2, "解聯立方程式 2x+y=11、x-y=1，(x,y) 為何？", {"A":"(4,3)", "B":"(3,4)", "C":"(5,1)", "D":"(2,7)"}, "A", "由 x-y=1 得 y=x-1，代入 2x+y=11 得 3x=12，故 x=4、y=3，選 A。", "先由含係數 1 的方程式解出 y，再代入另一式。", ["由 x-y=1 解得 y=x-1。", "代入 2x+y=11，得到 2x+x-1=11。", "整理為 3x=12，所以 x=4。", "代回 y=x-1，得到 y=3。", "所以選 A。"], "medium"),
make(3, "成人票 120 元、學生票 80 元，共售出 7 張，收入 680 元。成人票售出幾張？", {"A":"2 張", "B":"3 張", "C":"4 張", "D":"5 張"}, "B", "設成人票 x、學生票 y，x+y=7 且 120x+80y=680；代入 y=7-x 得 40x=120，所以 x=3，選 B。", "先用張數總和消去一個未知數，再把價格條件代入。", ["設成人票 x 張、學生票 y 張。", "列出 x+y=7 與 120x+80y=680。", "由第一式得 y=7-x。", "代入第二式得 120x+80(7-x)=680，解得 x=3。", "成人票 3 張，選 B。"], "medium"),
make(4, "長方形的長比寬多 3 公分，且周長為 34 公分，長與寬各為多少？", {"A":"長 8、寬 9", "B":"長 10、寬 7", "C":"長 11、寬 6", "D":"長 12、寬 5"}, "B", "半周長為 17，長寬和為 17；再配合長寬差 3，解得長 10、寬 7，因此選 B。", "把周長轉為半周長，再用長寬差形成第二個線性條件。", ["半周長為 34÷2=17，所以長+寬=17。", "長比寬多 3，所以長-寬=3。", "兩式相加得 2長=20，長=10。", "寬=17-10=7。", "所以選 B。"], "medium"),
make(5, "聯立方程式 x+2y=8、2x-y=1 的解為何？", {"A":"(1,4)", "B":"(2,3)", "C":"(3,2)", "D":"(4,1)"}, "B", "第一式乘 2 得 2x+4y=16，減去第二式得 5y=15，所以 y=3、x=2，正確答案為 B。", "將一式乘倍數製造相同的 x 係數，再相減消元。", ["把 x+2y=8 乘以 2，得 2x+4y=16。", "用新式減去 2x-y=1，得到 5y=15。", "求得 y=3。", "代回 x+2(3)=8，得到 x=2。", "所以選 B。"], "medium"),
make(6, "某班男生比女生少 4 人，全班共有 28 人。若男生為 x、女生為 y，哪一組方程式正確？", {"A":"x+y=28、x-y=4", "B":"x+y=4、y-x=28", "C":"x+y=28、y-x=4", "D":"x-y=28、x+y=4"}, "C", "總人數給 x+y=28；女生比男生多 4 人給 y-x=4，所以正確答案為 C。", "先分辨總量條件與差量方向，再將文字關係翻成方程式。", ["男生 x、女生 y。", "全班共 28 人，所以 x+y=28。", "男生比女生少 4，等價於女生比男生多 4。", "因此 y-x=4。", "兩式合併，選 C。"], "easy"),
make(7, "聯立方程式 x+y=5、2x+2y=12 的解為何？", {"A":"(1,4)", "B":"(2,3)", "C":"所有滿足 x+y=5 的數對", "D":"無解"}, "D", "第二式除以 2 會得到 x+y=6，與第一式 x+y=5 矛盾，因此無解，選 D。", "先化簡其中一式，再比較兩式是否描述同一條件或互相矛盾。", ["將第二式 2x+2y=12 除以 2。", "得到 x+y=6。", "第一式要求 x+y=5。", "同一個 x+y 不可能同時等於 5 與 6。", "所以無解，選 D。"], "medium"),
make(8, "聯立方程式 x-y=3、2x-2y=6 的解有幾組？", {"A":"0 組", "B":"1 組", "C":"2 組", "D":"無限多組"}, "D", "第二式除以 2 後就是第一式，兩式代表同一條直線，因此有無限多組解，選 D。", "將倍數方程式約去共同因數，檢查兩式是否完全相同。", ["把 2x-2y=6 的各項除以 2。", "得到 x-y=3。", "這正好等於第一式，沒有新增限制。", "所有在 x-y=3 上的數對都同時成立。", "因此有無限多組解，選 D。"], "medium"),
make(9, "兩直線 y=3x-2 與 y=x+4 的交點為何？", {"A":"(2,6)", "B":"(3,7)", "C":"(4,8)", "D":"(5,9)"}, "B", "在交點兩式的 y 相等，所以 3x-2=x+4，得 2x=6、x=3，再得 y=7，選 B。", "把共同的 y 值相等化成一元方程式，再回代求另一座標。", ["令兩條直線的 y 值相等。", "得到 3x-2=x+4。", "整理得 2x=6，所以 x=3。", "代入 y=x+4，得到 y=7。", "交點為 (3,7)，選 B。"], "medium"),
make(10, "停車場汽車與機車共 20 輛，輪子共 56 個。汽車有幾輛？", {"A":"6 輛", "B":"7 輛", "C":"8 輛", "D":"9 輛"}, "C", "設汽車 x、機車 y，x+y=20、4x+2y=56；以 y=20-x 代入得 2x=16，所以 x=8，正確答案為 C。", "用車輛總數消去機車數，再以輪子總數解出汽車數。", ["設汽車 x 輛、機車 y 輛。", "列出 x+y=20 與 4x+2y=56。", "由第一式得 y=20-x。", "代入第二式得 4x+2(20-x)=56，解得 x=8。", "汽車有 8 輛，選 C。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

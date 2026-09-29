import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-n-iv-2"
KG = "kg-math-performance-n-iv-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "負數數線方向、絕對值、正負數四則、運算順序、分數與生活溫度情境；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常把負數放入數線、溫度、收支或混合運算情境，要求判斷方向、符號與運算順序；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-n-iv-2-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供負數與四則運算能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的數線與負數方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "計算 (-15)+8 的值為何？", {"A":"-23", "B":"-7", "C":"7", "D":"23"}, "B", "負數加正數可視為向右移 8 格，-15+8=-7，所以選 B。", "先比較絕對值大小，再決定結果符號與相差量。", ["兩數符號相反。", "比較 15 與 8，較大絕對值是 15。", "結果符號取負。", "計算 15-8=7，得到 -7。", "所以選 B。"], "easy"),
make(2, "計算 (-4)×(-6) 的值為何？", {"A":"-24", "B":"-10", "C":"10", "D":"24"}, "D", "負數乘負數為正，4×6=24，因此答案為 D。", "先判斷符號，再計算絕對值的乘積。", ["兩個因數都是負數。", "負乘負的結果是正數。", "計算絕對值 4×6=24。", "合併符號與數值得到 24。", "所以選 D。"], "easy"),
make(3, "計算 (-36)÷9 的值為何？", {"A":"-4", "B":"-3", "C":"4", "D":"45"}, "A", "負數除以正數仍為負，36÷9=4，所以結果為 -4，選 A。", "先用乘除符號規則判斷正負，再做絕對值除法。", ["被除數為負、除數為正。", "異號相除結果為負。", "計算 36÷9=4。", "得到 -4。", "所以選 A。"], "easy"),
make(4, "計算 -3-(-8) 的值為何？", {"A":"-11", "B":"-5", "C":"5", "D":"11"}, "C", "減去負數等於加上其相反數，-3-(-8)=-3+8=5，選 C。", "先把減去負數改寫成加法，再按數線方向計算。", ["看到 -(-8) 代表加上 8。", "原式改寫為 -3+8。", "從 -3 向右 8 格。", "抵達 5。", "所以選 C。"], "easy"),
make(5, "計算 -6+2×5 的值為何？", {"A":"-20", "B":"4", "C":"20", "D":"16"}, "B", "先乘法 2×5=10，再算 -6+10=4，正確答案為 B。", "依先乘除後加減的順序，避免先把 -6 與 2 相加。", ["先找出乘法 2×5。", "計算得 10。", "原式變成 -6+10。", "相加得到 4。", "所以選 B。"], "easy"),
make(6, "|-9|+|4| 的值為何？", {"A":"-13", "B":"-5", "C":"5", "D":"13"}, "D", "|-9|=9、|4|=4，兩者相加為 13，因此選 D。", "絕對值先轉成距離的非負數，再進行加法。", ["-9 到原點的距離是 9。", "4 到原點的距離是 4。", "所以 |-9|+|4|=9+4。", "計算得到 13。", "所以選 D。"], "easy"),
make(7, "下列哪個數較大？", {"A":"-2/3", "B":"-3/5", "C":"兩者相等", "D":"無法比較"}, "B", "-2/3≈-0.667、-3/5=-0.6；在數線上 -0.6 位於右側，所以 -3/5 較大，選 B。", "負分數比較可先轉小數，或通分後注意負號方向。", ["將 -2/3 與 -3/5 通分為 -10/15 與 -9/15。", "-9/15 位於 -10/15 的右側。", "數線右側的數較大。", "因此 -3/5 較大。", "所以選 B。"], "medium"),
make(8, "清晨氣溫為 -4°C，夜間比清晨低 7°C，夜間氣溫為何？", {"A":"-11°C", "B":"-3°C", "C":"3°C", "D":"11°C"}, "A", "夜間比 -4°C 再低 7°C，計算 -4-7=-11°C，正確答案為 A。", "『降低』代表在數線向左移，應以減法表示。", ["起始溫度是 -4°C。", "降低 7°C 表示減去 7。", "列式 -4-7。", "計算得到 -11。", "所以選 A。"], "easy"),
make(9, "計算 (-2/3)+(5/6) 的值為何？", {"A":"-1/6", "B":"1/6", "C":"1/2", "D":"7/6"}, "B", "-2/3=-4/6，故 -4/6+5/6=1/6，選 B。", "先通分成相同分母，再只計算分子。", ["最小公分母為 6。", "-2/3 改寫為 -4/6。", "相加為 -4/6+5/6=1/6。", "分數已最簡。", "所以選 B。"], "medium"),
make(10, "計算 [(-12)÷3]-[(-2)×4] 的值為何？", {"A":"-12", "B":"-4", "C":"4", "D":"12"}, "C", "前一括號為 -4，後一括號為 -8；-4-(-8)=4，所以選 C。", "先各自完成括號內的乘除，再處理減去負數。", ["計算 (-12)÷3=-4。", "計算 (-2)×4=-8。", "原式變成 -4-(-8)。", "改寫為 -4+8=4。", "所以選 C。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

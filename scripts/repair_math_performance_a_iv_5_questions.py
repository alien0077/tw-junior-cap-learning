import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-5"
KG = "kg-math-performance-a-iv-5"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "多項式合併、分配律、乘法公式、立方和與因式分解；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常要求辨識同類項、展開乘法公式、利用平方差或立方和快速化簡，並以因式分解檢查結果；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-a-iv-5-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供多項式與乘法公式能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的代數運算方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "化簡 (2x+3)+(x-5)，結果為何？", {"A":"x-2", "B":"3x+8", "C":"x+2", "D":"3x-2"}, "D", "去括號後合併同類項：2x+3+x-5=3x-2，所以選 D。", "先處理括號的正號，再把 x 項與常數項分開合併。", ["將兩個括號直接相加。", "合併 x 項：2x+x=3x。", "合併常數：3-5=-2。", "得到 3x-2。", "所以選 D。"], "easy"),
make(2, "化簡 (5a-2b)-(2a+3b)，結果為何？", {"A":"3a+b", "B":"3a-5b", "C":"7a+b", "D":"7a-5b"}, "B", "減去第二個括號要使兩項變號：5a-2b-2a-3b=3a-5b，正確答案為 B。", "看到括號前的減號就先整個括號變號，再合併同類項。", ["寫成 5a-2b-2a-3b。", "合併 a 項，得到 3a。", "合併 b 項，得到 -5b。", "化簡結果為 3a-5b。", "所以選 B。"], "medium"),
make(3, "計算 3x²·(-2x³)，結果為何？", {"A":"-6x⁵", "B":"6x⁶", "C":"-6x⁶", "D":"-x⁵"}, "A", "係數 3×(-2)=-6，同底數 x 的次方相加 2+3=5，因此結果為 -6x⁵，正確答案為 A。", "分開處理係數與同底數次方；乘法時次方相加。", ["先算係數 3×(-2)=-6。", "同底數 x 相乘，指數相加 2+3=5。", "合併得到 -6x⁵。", "檢查選項，-6x⁵ 在 A。", "所以選 A。"], "easy"),
make(4, "展開 4(2x-3)+2(x+5)，結果為何？", {"A":"10x-2", "B":"10x+2", "C":"6x-2", "D":"6x+2"}, "A", "分配律得 8x-12+2x+10=10x-2，因此正確答案為 A。", "先逐項分配括號外係數，再合併 x 項與常數。", ["4 乘入括號，得 8x-12。", "2 乘入括號，得 2x+10。", "合併 x 項得到 10x。", "合併常數 -12+10=-2。", "所以選 A。"], "easy"),
make(5, "展開 (x+3)²，結果為何？", {"A":"x²+9", "B":"x²+3x+9", "C":"x²+6x+9", "D":"x²+6x+6"}, "C", "平方和公式 (x+3)²=x²+2·x·3+3²=x²+6x+9，選 C。", "套用 (p+q)²=p²+2pq+q²，不要漏掉中間項。", ["辨認 p=x、q=3。", "計算 p²=x²。", "計算 2pq=2·x·3=6x。", "計算 q²=9並合併成 x²+6x+9。", "所以選 C。"], "easy"),
make(6, "展開 (2x-5)²，結果為何？", {"A":"4x²-25", "B":"4x²-20x+25", "C":"4x²-10x+25", "D":"2x²-20x+25"}, "B", "平方差形式為 (2x)²-2·(2x)·5+5²=4x²-20x+25，所以選 B。", "使用 (p-q)²=p²-2pq+q²，第二項一定帶負號。", ["令 p=2x、q=5。", "p²=(2x)²=4x²。", "-2pq=-2·2x·5=-20x。", "q²=25，合併得 4x²-20x+25。", "所以選 B。"], "medium"),
make(7, "化簡 (3x+2)(3x-2)，結果為何？", {"A":"9x²-4", "B":"9x²+4", "C":"6x²-4", "D":"9x²-12x+4"}, "A", "這是平方差 (3x)²-2²=9x²-4，正確答案為 A。", "辨識兩括號只差一個正負號，直接使用平方差公式。", ["辨認形式 (p+q)(p-q)。", "令 p=3x、q=2。", "套用 p²-q²。", "計算 (3x)²-2²=9x²-4。", "所以選 A。"], "easy"),
make(8, "因式分解 8x²-18，結果為何？", {"A":"2(4x²-9)", "B":"2(2x-3)²", "C":"2(2x-3)(2x+3)", "D":"(4x-9)(2x+2)"}, "C", "先提出公因式 2 得 2(4x²-9)，再用平方差分解為 2(2x-3)(2x+3)，所以選 C。", "先提出整體公因式，再辨認剩下的平方差。", ["8x² 與 18 的最大公因數是 2。", "提出 2，得到 2(4x²-9)。", "辨認 4x²-9=(2x)²-3²。", "套用平方差，得到 2(2x-3)(2x+3)。", "展開回查為 8x²-18，選 C。"], "medium"),
make(9, "若 x≠-3，化簡 (x²-9)/(x+3) 的結果為何？", {"A":"x+3", "B":"x-3", "C":"x²-3", "D":"x-9"}, "B", "x²-9=(x-3)(x+3)，約去非零的 x+3 後得 x-3，正確答案為 B。", "先因式分解平方差，再確認分母不為零才能約分。", ["辨認 x²-9=x²-3²。", "因式分解為 (x-3)(x+3)。", "題目給 x≠-3，所以 x+3 不為 0。", "約去 x+3，剩下 x-3。", "所以選 B。"], "medium"),
make(10, "展開 (2x+1)(4x²-2x+1)，結果為何？", {"A":"8x³-1", "B":"8x³+1", "C":"8x³+4x²+1", "D":"4x³+1"}, "B", "這是 (p+q)(p²-pq+q²)=p³+q³，令 p=2x、q=1，得到 8x³+1，選 B。", "辨識立方和公式，確認中間兩項會相消。", ["令 p=2x、q=1。", "確認第二因式為 p²-pq+q²。", "套用立方和公式，得到 p³+q³。", "計算 (2x)³+1³=8x³+1。", "所以選 B。"], "medium"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

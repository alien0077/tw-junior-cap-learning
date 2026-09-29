import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-6"
KG = "kg-math-performance-a-iv-6"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "一元二次方程的因式分解、平方根、判別式、公式法、根與係數、文字建模與參數推理；僅作公開試題能力方向研究。", "observedPattern": "公開數學評量常要求從二次式的結構找根，或依判別式與根的關係判斷解的型態，再把條件轉成生活或參數問題；本題只採能力與資料型態。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(n, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-performance-a-iv-6-{n}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開公立學校／公開會考數學試題僅供一元二次方程能力方向研究；本題未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱、KG 與三筆公開數學試題的二次方程解題方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
make(1, "方程式 x²-5x+6=0 的兩根為何？", {"A":"-2、-3", "B":"1、6", "C":"-1、-6", "D":"2、3"}, "D", "x²-5x+6=(x-2)(x-3)，所以兩根為 2、3，選 D。", "找出乘積為 6、和為 5 的兩數，再用因式分解驗證。", ["找兩數乘積為 6。", "同時檢查兩數和為 5。", "得到 2 與 3。", "將式子分解為 (x-2)(x-3)=0。", "所以兩根為 2、3，選 D。"], "easy"),
make(2, "方程式 x²-9=0 的解為何？", {"A":"x=3", "B":"x=-3", "C":"x=±3", "D":"x=±9"}, "C", "x²=9，因此 x 可為 3 或 -3，正確答案為 C。", "先移項得到平方等於正數，再記得平方根有正負兩個。", ["由 x²-9=0 得 x²=9。", "對兩邊開平方。", "平方根包含正值與負值。", "得到 x=3 或 x=-3。", "所以選 C。"], "easy"),
make(3, "方程式 2x²-8x=0 的解為何？", {"A":"x=0 或 4", "B":"x=2 或 4", "C":"x=-4 或 0", "D":"只有 x=4"}, "A", "提出公因式 2x，得 2x(x-4)=0，所以 x=0 或 4，選 A。", "先提出最大公因式，再使用零乘積性質分別令各因式為零。", ["原式含有公因式 2x。", "提出後得 2x(x-4)=0。", "由零乘積性質，2x=0 或 x-4=0。", "得到 x=0 或 x=4。", "所以選 A。"], "easy"),
make(4, "方程式 x²+4x+4=0 的解有何特徵？", {"A":"兩個相異正根", "B":"兩個相異負根", "C":"一個正根與一個負根", "D":"只有一個重根 x=-2"}, "D", "x²+4x+4=(x+2)²，因此只有重根 x=-2，正確答案為 D。", "辨認完全平方，或用判別式等於零確認重根。", ["觀察常數 4 是 2²。", "中間項 4x=2·x·2，符合完全平方。", "改寫為 (x+2)²=0。", "所以 x=-2 且重複一次。", "因此選 D。"], "medium"),
make(5, "二次方程式 2x²+3x-2=0 的判別式 Δ 為何？", {"A":"-7", "B":"1", "C":"25", "D":"41"}, "C", "a=2、b=3、c=-2，Δ=b²-4ac=9-4(2)(-2)=25，所以選 C。", "先對照標準式取 a、b、c，再代入判別式並注意 c 的負號。", ["辨認 a=2、b=3、c=-2。", "寫出 Δ=b²-4ac。", "代入得 3²-4·2·(-2)。", "計算 9+16=25。", "所以選 C。"], "medium"),
make(6, "解方程式 2x²-3x-2=0，兩根為何？", {"A":"2、-1/2", "B":"-2、1/2", "C":"1、-2", "D":"4、-1"}, "A", "(2x+1)(x-2)=0，因此 x=2 或 x=-1/2，正確答案為 A。", "找出可分解的兩個一次因式，再由零乘積性質取根。", ["將 2x²-3x-2 分解為 (2x+1)(x-2)。", "令第一因式 2x+1=0，得 x=-1/2。", "令第二因式 x-2=0，得 x=2。", "把兩個根代回原式皆為 0。", "所以選 A。"], "medium"),
make(7, "一個長方形面積為 48 平方公分，長比寬多 2 公分。若寬為 x，x 應為多少？", {"A":"4", "B":"6", "C":"8", "D":"-8"}, "B", "x(x+2)=48，得 x²+2x-48=0=(x+8)(x-6)，寬不能為負，所以 x=6，選 B。", "把幾何條件列成二次方程，再用長度必須為正排除負根。", ["寬為 x，長為 x+2。", "面積條件給 x(x+2)=48。", "整理為 x²+2x-48=0。", "分解為 (x+8)(x-6)=0，候選為 -8、6。", "長度取正值，所以 x=6，選 B。"], "medium"),
make(8, "若二次方程式 x²-7x+10=0 的兩根為 r、s，則 r+s 為何？", {"A":"5", "B":"7", "C":"10", "D":"-7"}, "B", "由根與係數關係，兩根和為 -b/a=-(-7)/1=7，因此選 B。", "直接使用韋達定理的根和公式，先辨認標準式係數。", ["標準式為 ax²+bx+c=0。", "本題 a=1、b=-7。", "根和 r+s=-b/a。", "計算 -(-7)/1=7。", "所以選 B。"], "easy"),
make(9, "方程式 x²+2x+5=0 有幾個實數解？", {"A":"0 個", "B":"1 個", "C":"2 個", "D":"無限多個"}, "A", "判別式 Δ=2²-4·1·5=-16<0，所以沒有實數解，正確答案為 A。", "用判別式的正負判斷實根個數，不必勉強因式分解。", ["辨認 a=1、b=2、c=5。", "計算 Δ=b²-4ac=4-20=-16。", "判別式小於 0。", "因此圖形不與 x 軸相交，沒有實數根。", "所以選 A。"], "medium"),
make(10, "若方程式 x²-8x+k=0 的兩根相差 2，則 k 為何？", {"A":"12", "B":"14", "C":"15", "D":"16"}, "C", "兩根和為 8 且相差 2，所以兩根為 3、5；根積 k=3·5=15，選 C。", "先用根和與差求出兩根，再用根積等於常數項。", ["由根和關係得到兩根和為 8。", "兩根相差 2，設較小根為 t，則另一根為 t+2。", "t+(t+2)=8，解得 t=3，另一根為 5。", "根積等於 k，所以 k=3·5=15。", "因此選 C。"], "hard"),
]

for q in Q:
    (OUT / f"{q['id']}.json").write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

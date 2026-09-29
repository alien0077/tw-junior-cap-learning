import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-performance-a-iv-1"
KG = "kg-math-performance-a-iv-1"
SOURCES = [
    {
        "url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf",
        "title": "114 年國中教育會考數學科公開試題",
        "year": "114",
    },
    {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2",
        "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科",
        "year": "112",
    },
    {
        "url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
        "title": "高雄市立鹽埕國民中學 114 學年度下學期第一次段考三年級數學科",
        "year": "114",
    },
]


def refs():
    return [
        {
            **source,
            "subject": "math",
            "locator": "符號表示、代數運算、奇偶性、代數推理與簡短證明的公開試題能力方向；僅作題型研究定位。",
            "observedPattern": "公開數學評量常要求把文字條件轉成符號、執行基本運算，再用反例或代數關係判斷命題；本題只採能力方向與資料型態。",
            "reuseDecision": "pattern-only",
            "status": "recorded",
            "locatorLevel": "paper",
        }
        for source in SOURCES
    ]


def make(number, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {
        "id": f"question-math-performance-a-iv-1-{number}",
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
            "sourceLocator": "三份公開公立學校／公開會考數學試題僅供符號表達、代數推理與證明的能力方向研究；本題未複製原題、選項、圖表或答案。",
            "authoringNote": "依官方課綱、KG 與三筆公開數學試題的能力方向獨立改寫；題幹、數值、選項、答案、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-09-10",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": strategy,
        "solutionSteps": steps,
    }


QUESTIONS = [
    make(1, "若 n 為偶數，哪一種表示法一定正確？", {"A": "n=2k+1（k 為整數）", "B": "n=k/2（k 為整數）", "C": "n=k²+1（k 為整數）", "D": "n=2k（k 為整數）"}, "D", "偶數能被 2 整除，因此可寫成 2k，其中 k 為整數；正確答案為 D。", "先把『偶數』翻成整除 2 的符號形式，再檢查 k 是否仍可取任意整數。", ["把 n 視為任意偶數。", "偶數的定義是存在整數 k，使 n=2k。", "比較四個選項的形式。", "只有 D 直接符合 2k 的一般表示。", "所以選 D。"], "easy"),
    make(2, "若 m 為奇數，哪一個式子可表示所有可能的 m？", {"A": "m=2k（k 為整數）", "B": "m=2k+1（k 為整數）", "C": "m=k²（k 為整數）", "D": "m=k+2（k 為偶數）"}, "B", "奇數比某個偶數多 1，可表示成 2k+1（k 為整數），所以正確答案為 B。", "使用偶數的一般式後加 1，並確認 k 取整數時不會漏掉負奇數。", ["先寫出任意偶數的形式 2k。", "奇數就是偶數加 1。", "因此 m=2k+1。", "檢查 k=-1 時得到 -1，仍是奇數。", "所以選 B。"], "easy"),
    make(3, "已知 x>0，下列哪一項必定為正數？", {"A": "x-x", "B": "-x²", "C": "x²", "D": "-x"}, "C", "正數的平方仍為正，x²>0；A 等於 0，B 與 D 為負數，因此正確答案為 C。", "先判斷每個式子的符號，再排除與『必定為正』不符的選項。", ["由 x>0 知道 x 是正數。", "x-x=0，不是正數。", "-x 與 -x² 都小於 0。", "正數平方後仍大於 0，所以 x²>0。", "因此選 C。"], "easy"),
    make(4, "令 a=3，哪一個等式的左右兩邊數值相等？", {"A": "2a+1=5", "B": "a²-2=7", "C": "3a-1=10", "D": "a²+a=9"}, "B", "代入 a=3：a²-2=9-2=7，只有 B 成立。", "把已知數值代入每個選項，逐項驗算，不依靠式子外觀判斷。", ["將 a=3 代入 A，左式為 7，不是 5。", "將 a=3 代入 B，左式為 9-2=7。", "B 的右式也是 7，所以 B 成立。", "其餘選項不需作為正解，但可用代入排除。", "因此選 B。"], "easy"),
    make(5, "為什麼任意兩個連續整數的乘積一定是偶數？", {"A": "兩數的和一定是偶數", "B": "兩數中必有一個是偶數", "C": "兩數都一定是奇數", "D": "兩數的差一定是偶數"}, "B", "連續整數一奇一偶，其中必有一個可寫成 2k；乘積含有因數 2，所以一定是偶數，正確答案為 B。", "先用相鄰整數的奇偶交替性找出因數 2，再把它連結到乘積的偶性。", ["設兩數為 n 與 n+1。", "連續整數不可能同時為奇數，必有一個是偶數。", "偶數可寫成 2k，因此乘積含有因數 2。", "含有因數 2 的整數就是偶數。", "所以選 B。"], "medium"),
    make(6, "若 n 為整數，哪一個式子一定可被 3 整除？", {"A": "n+1", "B": "2n+1", "C": "(n-1)+n+(n+1)", "D": "n²+1"}, "C", "(n-1)+n+(n+1)=3n，而 n 為整數，所以 3n 一定是 3 的倍數；正確答案為 C。", "先合併同類項，把看似三項的式子化成 3 的倍數。", ["寫下原式 (n-1)+n+(n+1)。", "合併三個 n 得 3n。", "-1 與 +1 抵消。", "因 n 為整數，3n 是 3 的整數倍。", "因此選 C。"], "medium"),
    make(7, "已知 a>b 且 c>0，下列哪一個不等式必定成立？", {"A": "ac>bc", "B": "ac<bc", "C": "a+c<b+c", "D": "a/c<b/c"}, "A", "不等式兩邊同乘正數 c，方向不變，因此 ac>bc；正確答案為 A。", "判斷施加的運算是否為正數乘法或除法，正數不會使不等號反向。", ["已知 a>b。", "c>0，表示 c 是正數。", "不等式同乘正數 c 時方向保持不變。", "得到 ac>bc。", "所以選 A。"], "medium"),
    make(8, "下列哪一個等式正確使用了分配律？", {"A": "3(x+2)=3x+2", "B": "3(x+2)=3x+6", "C": "3(x+2)=x+6", "D": "3(x+2)=3x+5"}, "B", "分配律要求 3 同時乘括號內兩項，3(x+2)=3x+6，因此正確答案為 B。", "將括號外的係數分別乘到括號內每一項，再整理結果。", ["辨認括號外的公因數是 3。", "3 乘 x 得 3x。", "3 乘 2 得 6。", "把兩個結果相加，得到 3x+6。", "所以選 B。"], "easy"),
    make(9, "下列敘述哪一項可用一個反例否定？", {"A": "所有偶數都可寫成 2k（k 為整數）", "B": "若 x=0，則 x²=0", "C": "所有整數的平方都是奇數", "D": "連續整數中至少有一個是偶數"}, "C", "取整數 2 作反例，2²=4 是偶數，不是奇數，因此『所有整數的平方都是奇數』可被否定，正確答案為 C。", "面對『所有』的命題，只需找一個符合前提卻不符合結論的例子。", ["鎖定含有『所有』的命題 C。", "選取最簡單的整數反例 n=2。", "計算 n²=2²=4。", "4 是偶數，違反 C 所說的奇數結論。", "所以選 C。"], "medium"),
    make(10, "若 x+y=10 且 x-y=4，則 x 等於多少？", {"A": "3", "B": "5", "C": "6", "D": "7"}, "D", "兩式相加得 2x=14，所以 x=7；正確答案為 D。", "利用加法消去 y，再除以 x 的係數，最後代回原條件檢查。", ["列出 x+y=10。", "列出 x-y=4。", "兩式相加，y 與 -y 抵消，得到 2x=14。", "兩邊除以 2，得到 x=7。", "代回 7+y=10 可得 y=3，條件一致，所以選 D。"], "medium"),
]

for question in QUESTIONS:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"rewrote {len(QUESTIONS)} questions")

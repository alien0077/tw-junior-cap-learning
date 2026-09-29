import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-7-2"
KG = "kg-math-content-n-7-2"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "prime factorization, standard form, exponents, reconstructing integers, and factor-count reasoning", "observedPattern": "公立學校公開數學試題常要求把整數分解為質因數冪次、由標準分解式還原數值、比較冪次或判斷因數結構；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-7-2-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供質因數分解、標準分解式、冪次與因數結構能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的質因數分解方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "60 的質因數分解式為何？", {"A": "2×3×10", "B": "2²×3×5", "C": "2×3²×5", "D": "4×15"}, "B", "60＝2×30＝2×2×15＝2²×3×5，且 2、3、5 都是質數，所以選 B。", "先不斷除以最小質數，再把重複的質因數用冪次表示。", ["用 2 除 60，得 30。", "再用 2 除 30，得 15。", "將 15 分解為 3×5。", "整理重複的 2 為 2²，得到 2²×3×5。", "選 B，乘回 4×3×5 確認等於 60。"], "easy"),
    make(2, "84 的標準質因數分解式為何？", {"A": "2²×3×7", "B": "2×3²×7", "C": "2²×3×14", "D": "4×21"}, "A", "84＝2×42＝2×2×21＝2²×3×7，標準式中的底數都是質數，因此選 A。", "先分解成質數，再檢查每個底數是否為質數且不再保留合數因子。", ["以 2 除 84 得 42。", "再以 2 除 42 得 21。", "將 21 分解為 3×7。", "合併成 2²×3×7。", "選 A，計算 4×3×7＝84 驗證。"], "easy"),
    make(3, "若 180＝2²×3²×5，則 180 的質因數 3 出現幾次？", {"A": "1 次", "B": "2 次", "C": "3 次", "D": "5 次"}, "B", "3² 表示兩個 3 相乘，所以質因數 3 出現 2 次，選 B。", "把冪次看成該質因數重複相乘的次數，不把指數當成數值本身。", ["找出分解式中的 3²。", "解讀指數 2 為 3×3。", "因此質因數 3 出現兩次。", "區分 3²＝9 與出現次數 2。", "選 B，回寫 180＝2×2×3×3×5。"], "easy"),
    make(4, "下列哪一個是 126 的正確標準質因數分解式？", {"A": "2×3²×7", "B": "2²×3×7", "C": "2×3×7²", "D": "6×3×7"}, "A", "126＝2×63＝2×3²×7，因此選 A。", "逐一用小質數試除，再將剩餘部分繼續分解，避免把 6 當成質數。", ["126 可被 2 整除，得 63。", "63＝3×21＝3×3×7。", "整理為 2×3²×7。", "確認底數 2、3、7 都是質數。", "選 A，乘回 2×9×7＝126。"], "medium"),
    make(5, "數 N 的標準質因數分解式為 2³×5²，N 為何？", {"A": "100", "B": "150", "C": "200", "D": "250"}, "C", "N＝2³×5²＝8×25＝200，所以選 C。", "先分別計算各冪次，再相乘還原原數。", ["計算 2³＝8。", "計算 5²＝25。", "把兩個結果相乘 8×25。", "得到 N＝200。", "選 C，確認 200 的質因數只有 2、5 且冪次正確。"], "easy"),
    make(6, "下列哪一個分解式不是標準質因數分解式？", {"A": "2²×3×5", "B": "3×7²", "C": "2×5×11", "D": "4×3×7"}, "D", "4 不是質數，標準質因數分解式必須只使用質數作底數；D 應再寫成 2²×3×7，選 D。", "檢查每個乘積因子是否都是質數，遇到合數就繼續分解。", ["回顧標準式要求所有底數都是質數。", "檢查 A 的底數 2、3、5，均為質數。", "檢查 B、C，底數也都為質數。", "檢查 D，因 4＝2²，4 不是質數。", "選 D，將 4 改寫後才是標準形式。"], "medium"),
    make(7, "若 A＝2³×3、B＝2²×3²，哪個數比較大？", {"A": "A 比 B 大", "B": "B 比 A 大", "C": "A、B 相等", "D": "無法比較"}, "B", "A＝8×3＝24，B＝4×9＝36，所以 B 比 A 大，選 B。", "冪次比較不一定能直接看指數，先還原兩數或以數值估算再判斷。", ["計算 A＝2³×3＝8×3＝24。", "計算 B＝2²×3²＝4×9＝36。", "比較 24 與 36。", "判定 36 大於 24。", "選 B，回查每個冪次沒有抄錯。"], "medium"),
    make(8, "數 72 的標準質因數分解式中，所有質因數的指數總和是多少？", {"A": "3", "B": "4", "C": "5", "D": "6"}, "C", "72＝2³×3²，指數總和為 3＋2＝5，選 C。", "先完成標準分解，再將各質因數的冪次相加，而不是把底數相加。", ["把 72 分解：72＝8×9。", "寫成 2³×3²。", "找出指數 3 與 2。", "計算指數總和 3＋2＝5。", "選 C，區分題目問指數總和而不是質因數總和。"], "hard"),
    make(9, "若 M＝2²×3×7，M 的值為何？", {"A": "42", "B": "56", "C": "84", "D": "98"}, "C", "M＝4×3×7＝12×7＝84，因此選 C。", "依冪次、乘法順序逐步還原，並用估算檢查結果範圍。", ["先算 2²＝4。", "將 4 與 3 相乘得 12。", "再乘以 7 得 84。", "確認所有因子均已使用一次。", "選 C，回寫 84 的分解確實為 2²×3×7。"], "easy"),
    make(10, "若 2ᵃ×3²＝36，a 為何？", {"A": "1", "B": "2", "C": "3", "D": "4"}, "B", "3²＝9，故 2ᵃ×9＝36，得到 2ᵃ＝4＝2²，所以 a＝2，選 B。", "先處理已知冪次，再除去相同因子，最後用 2 的冪次還原未知指數。", ["計算 3²＝9。", "將等式化為 2ᵃ×9＝36。", "兩邊同除以 9，得到 2ᵃ＝4。", "把 4 寫成 2²，故 a＝2。", "選 B，代回 2²×3²＝4×9＝36。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

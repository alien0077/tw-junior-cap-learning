import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "math"
LESSON = "lesson-math-content-n-8-3"
KG = "kg-math-content-n-8-3"
SOURCES = [
    {"url": "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf", "title": "114 年國中教育會考數學科公開試題", "year": "114"},
    {"url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2", "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科", "year": "112"},
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科", "year": "114"},
]


def refs():
    return [{**s, "subject": "math", "locator": "sequence terms, position indexing, pattern recognition, recursive rules, explicit rules, and contextual sequences", "observedPattern": "公立學校公開數學試題常要求讀取數列項次、找相鄰項規律、由通項求指定項、辨認遞迴關係與將生活情境編成數列；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-math-content-n-8-3-{i}", "subject": "math", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開數學試題僅供數列項次、規律、通項、遞迴與情境應用能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開數學試題的數列方向獨立改寫；題幹、數值、選項、解析與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-10", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}


Q = [
    make(1, "數列 4、8、12、16、…… 的第 5 項是多少？", {"A": "18", "B": "20", "C": "22", "D": "24"}, "B", "每項比前一項多 4，第 5 項為 16＋4＝20，所以選 B。", "先比較相鄰項找規律，再由已知最後一項往後推。", ["列出前四項 4、8、12、16。", "觀察相鄰項都增加 4。", "從第 4 項 16 再增加 4。", "得到第 5 項 20。", "選 B，確認不是把項次 5 與數值相乘。"], "easy"),
    make(2, "數列 5、10、20、40、…… 的下一項是多少？", {"A": "45", "B": "50", "C": "60", "D": "80"}, "D", "每項都是前一項的 2 倍，40×2＝80，所以選 D。", "比較相鄰項的商而非只看差值，確認規律是倍增。", ["計算 10÷5＝2。", "計算 20÷10＝2、40÷20＝2。", "判定每項乘以 2。", "計算下一項 40×2＝80。", "選 D，回查前三次都符合倍增規則。"], "easy"),
    make(3, "數列 2、5、8、11、…… 的相鄰兩項差是多少？", {"A": "2", "B": "3", "C": "4", "D": "5"}, "B", "5−2＝3、8−5＝3、11−8＝3，因此相鄰兩項差為 3，選 B。", "用後項減前項，至少檢查兩組相鄰項以確認規律。", ["取第 2 項減第 1 項：5−2＝3。", "取第 3 項減第 2 項：8−5＝3。", "再檢查 11−8＝3。", "確認相鄰差固定為 3。", "選 B，避免把相鄰項相加。"], "easy"),
    make(4, "若數列通項為 aₙ＝3n−1，a₄ 為何？", {"A": "8", "B": "10", "C": "11", "D": "12"}, "C", "將 n＝4 代入 aₙ＝3n−1，得 a₄＝3×4−1＝11，選 C。", "通項給出任意項的規則，只要把指定項次代入 n。", ["找出指定項次 n＝4。", "代入 aₙ＝3n−1。", "計算 3×4＝12。", "減去 1 得 a₄＝11。", "選 C，確認下標 4 沒有代錯成 3。"], "easy"),
    make(5, "若數列第一項 a₁＝7，且 aₙ₊₁＝aₙ＋5，則 a₃ 為何？", {"A": "12", "B": "17", "C": "22", "D": "27"}, "B", "a₂＝7＋5＝12，a₃＝12＋5＝17，所以選 B。", "依遞迴規則從已知第一項逐項產生後項。", ["寫出已知 a₁＝7。", "用規則求 a₂＝a₁＋5＝12。", "再用規則求 a₃＝a₂＋5。", "計算 a₃＝17。", "選 B，確認每一步都使用前一項而非第一項。"], "medium"),
    make(6, "數列 1、4、9、16、…… 的第 6 項是多少？", {"A": "25", "B": "30", "C": "36", "D": "49"}, "C", "這是平方數列 1²、2²、3²、4²、……，第 6 項為 6²＝36，選 C。", "將各項與自然數平方對照，確認項次 n 對應 n²。", ["辨認 1＝1²、4＝2²、9＝3²。", "確認 16＝4²，規律為第 n 項 n²。", "把 n＝6 代入。", "計算 6²＝36。", "選 C，檢查第 5 項應為 25。"], "medium"),
    make(7, "下列哪一組數最可能形成『前一項減 2』的數列？", {"A": "15、13、11、9", "B": "15、17、19、21", "C": "2、4、8、16", "D": "1、3、6、10"}, "A", "A 中 13−15＝−2、11−13＝−2、9−11＝−2，符合每項減 2，選 A。", "逐項計算相鄰差，找出固定為 −2 的選項。", ["檢查 A 的相鄰差皆為 −2。", "檢查 B，相鄰差為＋2。", "檢查 C，是乘以 2。", "檢查 D，差值逐次改變。", "選 A，確認規律在每一對相鄰項都成立。"], "medium"),
    make(8, "某座位編號每排比前一排多 6 個，第一排有 8 個座位。第 5 排有幾個座位？", {"A": "26", "B": "32", "C": "38", "D": "40"}, "B", "各排為 8、14、20、26、32，第 5 排有 32 個，選 B。", "把情境轉成首項與固定增加量的數列，逐項推到指定排數。", ["設定第 1 排為 8。", "第 2 排 8＋6＝14。", "第 3、4 排依序為 20、26。", "第 5 排 26＋6＝32。", "選 B，確認共增加 4 次而非 5 次。"], "medium"),
    make(9, "數列第 n 項為 aₙ＝2n＋3。哪一項等於 19？", {"A": "第 6 項", "B": "第 7 項", "C": "第 8 項", "D": "第 9 項"}, "B", "令 2n＋3＝19，得 2n＝16、n＝8；所以應為第 8 項，選 C。", "把指定數值代入通項方程式，解出項次並對照選項。", ["建立 2n＋3＝19。", "兩邊同減 3，得 2n＝16。", "兩邊同除以 2，得 n＝8。", "將 n＝8 對應到第 8 項。", "選 C，代入 2×8＋3＝19。"], "hard"),
    make(10, "數列 2、6、12、20、…… 的下一項最合理為何？", {"A": "24", "B": "28", "C": "30", "D": "32"}, "C", "各項可寫成 1×2、2×3、3×4、4×5，下一項為 5×6＝30，所以選 C。", "觀察每項能否表示成相鄰自然數的乘積，而不只檢查表面差值。", ["將 2 寫成 1×2。", "將 6、12、20 分別寫成 2×3、3×4、4×5。", "辨認下一項應為 5×6。", "計算 5×6＝30。", "選 C，確認相鄰因數都各增加 1。"], "hard"),
]

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

"""Keep A-8-2 original questions within polynomial meaning and attach verified public exam patterns."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "questions/math"
PATTERN = "只參考公立學校公開考卷中同類概念的作答任務；本題敘述、數值、選項與解答均重新設計，不複製原卷。"

def ref(url, title, year, locator):
    return {"url": url, "title": title, "year": year, "subject": "math", "locator": locator,
            "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "item"}

q5 = json.loads((BASE / "question-math-content-a-8-2-5.json").read_text(encoding="utf-8"))
q5["provenance"]["sourceUrl"] = "https://www.nhjh.tp.edu.tw/uploads/1706771169882T0v5rPBd.pdf"
q5["provenance"]["sourceLocator"] = "臺北市立內湖國中112學年度第一學期八年級第一次段考第5題，辨認多項式的次項與相關係數；臺中市立光正國中八上補行評量第18題，檢查各項次數、係數與常數項；臺中市立大道國中114學年度八年級補行評量第1題，辨認二次多項式與最高次項。均只作題型參照。"
q5["examPatternRefs"] = [
    ref("https://www.nhjh.tp.edu.tw/uploads/1706771169882T0v5rPBd.pdf", "臺北市立內湖國中112學年度第一學期八年級第一次段考數學科試題卷（翰林版）", "112", "第5題：辨認多項式中的二次項係數"),
    ref("https://school.tc.edu.tw/open-message/064544/get-file/697accd01b1faf22070745d7", "臺中市立光正國中八上數學補行評量", "unknown", "第18題：依指數辨認各項次數，並判斷係數與常數項"),
    ref("https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d", "臺中市立大道國中114學年度第一學期八年級數學科補行評量題庫", "114", "第1題：辨認二次多項式及其最高次項")
]
(BASE / "question-math-content-a-8-2-5.json").write_text(json.dumps(q5, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

q9 = json.loads((BASE / "question-math-content-a-8-2-9.json").read_text(encoding="utf-8"))
q9["prompt"] = "將多項式 3x⁴−2x+6 改寫成升冪排列，哪個選項正確？"
q9["options"] = [
    {"id": "A", "text": "6−2x+3x⁴"}, {"id": "B", "text": "3x⁴−2x+6"},
    {"id": "C", "text": "6+2x−3x⁴"}, {"id": "D", "text": "−2x+6+3x⁴"}
]
q9["answer"] = {"value": "A", "explanation": "升冪依指數由小到大排列：常數項指數為0、−2x為一次項、3x⁴為四次項，因此為 6−2x+3x⁴。B 是降冪；C 改了符號；D 沒有按次數遞增排列。"}
q9["solutionStrategy"] = "先為每項標出指數（常數為0），再按由小到大排列；最後逐項檢查符號、係數和原項完整保留。"
q9["solutionSteps"] = [
    "拆出三項：3x⁴、−2x、+6，保留各自符號。",
    "標記指數：3x⁴ 為4次，−2x 為1次，+6 為0次。",
    "升冪由小到大，因此順序是常數、一次項、四次項。",
    "抄回原係數和正負號，得到 6−2x+3x⁴。",
    "核對三項均出現且符號未變，選 A。"
]
q9["provenance"]["sourceUrl"] = "https://cdn.store-assets.com/s/1339278/f/12631614.pdf"
q9["provenance"]["sourceLocator"] = "新北市立崇林國中110學年度八年級第一學期第一次段考第3題直接要求將多項式按升冪排列；基隆市立中山高中109學年度國中部二年級第一次段考第8題辨認多項式排列與各項名稱；臺中市立大道國中114學年度八年級補行評量第1題辨認多項式項次。只參照概念任務，不沿用原題。"
q9["provenance"]["authoringNote"] = "本題僅改寫公立學校公開考卷所呈現的升冪排序概念任務；題幹、式子、選項、答案與逐步解法均為原創。publisher textbook fusion、Terra及最終發布QA尚未完成，維持draft。"
q9["examPatternRefs"] = [
    ref("https://cdn.store-assets.com/s/1339278/f/12631614.pdf", "新北市立崇林國中110學年度八年級第一學期第一次段考數學科試題", "110", "第3題：將多項式按升冪排列"),
    ref("https://csjh.kl.edu.tw/books/file/65/109-1-%E5%9C%8B%E4%BA%8C%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E6%95%B8%E5%AD%B8%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf", "基隆市立中山高中109學年度第一學期國中部二年級第一次段考數學科試題卷", "109", "第8題：讀取多項式各項名稱與排列方式"),
    ref("https://school.tc.edu.tw/open-message/064519/get-file/698ae03c3cd80e32ef01bd8d", "臺中市立大道國中114學年度第一學期八年級數學科補行評量題庫", "114", "第1題：依多項式項次判定次數與最高次項")
]
(BASE / "question-math-content-a-8-2-9.json").write_text(json.dumps(q9, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("updated A-8-2 Q5 and Q9 to curriculum-aligned original items with item-located public-school exam patterns")

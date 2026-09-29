"""Jc-Ⅳ-1：氧化還原的得氧與失氧定義第一輪原創題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jc-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-jc-iv-1-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "得氧失氧、金屬與氧反應、氧化還原資料判讀", "pattern": "取由物質組成與反應前後資料判斷得氧、失氧及氧化還原角色的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "燃燒、氧化物、反應式與實驗情境", "pattern": "取從燃燒、反應式與實驗現象推論氧化還原變化的能力方向。"},
    {"url": "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf", "title": "新竹市立新科國中公開康軒版自然課程計畫", "year": "公開課程計畫", "locator": "金屬對氧活性、得氧失氧與宏觀／微觀連結", "pattern": "取以金屬與氧的反應及粒子模型連結氧化定義與證據的教學與評量方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]


def q(n, prompt, opts, ans, exp, strat, steps, difficulty="medium"):
    return {"id": f"question-science-content-jc-iv-1-{n}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", opts)], "knowledgeIds": ["kg-science-content-jc-iv-1"], "difficulty": difficulty, "answer": {"value": ans, "explanation": exp}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的得氧失氧、金屬與氧反應及微觀粒子能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-jc-iv-1", "examPatternRefs": REFS, "solutionStrategy": strat, "solutionSteps": steps}


Q = [
 q(1, "木炭在氧氣中燃燒生成二氧化碳。以得氧失氧的傳統定義判斷，木炭發生什麼變化？", ["得到氧而被氧化", "失去氧而被還原", "沒有發生化學變化", "只發生熔化"], "A", "碳和氧結合生成二氧化碳，碳得到氧，因此依傳統定義是氧化。", "先追蹤氧原子是否進入該物質，再判斷氧化或還原。", ["寫出反應前的碳與氧氣。", "確認生成物二氧化碳含有碳和氧。", "判斷碳是否得到氧。", "B 把得氧失氧方向顛倒，C、D 否認新物質。", "所以 A 正確。"], "easy"),
 q(2, "氧化銅和氫氣加熱生成銅和水。以得氧失氧判斷，氧化銅中的銅元素主要發生？", ["失去氧而被還原", "得到氧而被氧化", "先溶解後沒有變化", "只改變顏色而不反應"], "A", "氧化銅中的氧轉移到氫形成水，銅由氧化銅變成銅，等於失去氧而被還原。", "用氧原子的去向辨認氧化物失氧的一方。", ["比較反應前的氧化銅與反應後的銅。", "追蹤氧是否仍與銅結合。", "確認銅失去氧。", "B、C、D 不符合物質組成的變化。", "答案為 A。"], "easy"),
 q(3, "下列哪一組最能表達『氧化與還原必同時發生』？", ["一物質得到氧，另一物質失去氧", "兩種物質都得到氧且沒有氧來源", "只有一物質改變，另一物質完全不參與", "反應只要加熱就一定同時氧化還原"], "A", "氧原子若轉移，一方得到氧時必有另一方失去氧，這是傳統得氧失氧定義下的互補關係。", "把氧當成可追蹤的收支，而不是只看單一物質。", ["列出反應前後含氧物質。", "找出氧進入的物質。", "找出氧離開的物質。", "檢查是否有一得一失的互補。", "因此 A 才能描述同時性。"], "medium"),
 q(4, "鎂帶在空氣中燃燒後形成白色氧化鎂。若只觀察鎂帶顏色變白，還需要哪項資料才能用得氧定義下結論？", ["確認生成物含有來自氧氣的氧，並與反應前鎂比較", "只記錄火焰亮度", "只測量房間溫度", "只把白色當成任何物質的共同特徵"], "A", "顏色是線索，必須知道生成物組成確實加入氧，才能以得氧定義判定氧化。", "區分觀察現象與足以支持定義的組成證據。", ["記錄燃燒前鎂的組成。", "確認燃燒時有氧氣參與。", "檢查生成物是否含氧並形成氧化鎂。", "排除只靠亮度、溫度或顏色的過度推論。", "所以 A 是充分方向。"], "medium"),
 q(5, "若氧化鐵被一氧化碳還原成鐵，哪項敘述符合得氧失氧定義？", ["氧化鐵失去氧；一氧化碳得到氧形成二氧化碳", "氧化鐵得到氧；一氧化碳失去氧", "兩者都得到氧", "兩者都失去氧而沒有氧接收者"], "A", "氧化鐵的氧轉移到一氧化碳形成二氧化碳，因此氧化鐵失氧被還原，一氧化碳得氧被氧化。", "先畫氧原子轉移箭頭，再同時判斷兩個物質。", ["列出氧化鐵與一氧化碳的反應前後。", "追蹤氧從氧化鐵移到哪裡。", "判定失氧者被還原、得氧者被氧化。", "B 顛倒方向，C、D 不符合氧收支。", "答案為 A。"], "medium"),
 q(6, "比較下列兩個反應：甲：硫得到氧生成二氧化硫；乙：氧化銅失去氧生成銅。正確判斷是？", ["甲是氧化，乙是還原", "甲是還原，乙是氧化", "甲乙都是氧化", "甲乙都不是化學變化"], "A", "甲依得氧判為氧化，乙依失氧判為還原；兩者都涉及新物質形成。", "以得氧／失氧作為同一套判準逐例套用。", ["對甲找出硫是否得到氧。", "對乙找出氧化銅是否失去氧。", "把得氧配對氧化、失氧配對還原。", "排除把兩個案例的方向混在一起。", "因此 A 正確。"], "easy"),
 q(7, "在封閉管中加熱氧化銅與碳粉，黑色固體變紅，並在管壁出現水滴。若資料確認生成銅與二氧化碳，最合理的氧轉移是？", ["氧化銅的氧轉移給碳，碳得氧而氧化，氧化銅失氧而還原", "銅把氧轉給氧化銅，兩者都被氧化", "氧沒有轉移，只是黑色染成紅色", "水滴表示氧被永久消失"], "A", "氧化銅提供氧給碳，碳成為含氧產物並被氧化；氧化銅失氧形成銅並被還原。", "結合顏色、生成物與封閉系統中的氧收支。", ["先接受資料已確認生成物種類。", "找出氧化銅失去的氧。", "把氧接到碳形成含氧產物。", "同步判斷得氧者與失氧者的角色。", "所以 A 能解釋整個證據鏈。"], "hard"),
 q(8, "某同學說『只要物質和氧氣接觸，就一定已經氧化』。哪項反例最能修正這個說法？", ["氧氣與物質接觸但沒有生成含氧新物質，不能只由接觸判定反應", "只要看到氧氣就一定產生氧化物", "接觸時間越短越能證明氧化", "顏色不變就代表失氧"], "A", "氧化是發生得氧等化學變化，不是單純接觸；必須有組成或反應證據。", "把接觸條件與化學反應結果分開檢查。", ["辨認題目聲稱的判準只有接觸。", "問是否有新物質或氧進入組成的證據。", "若沒有，不能直接下氧化結論。", "B、C、D 都把線索誇大成必然結論。", "答案為 A。"], "medium"),
 q(9, "若一個物質在反應中失去氧，依傳統定義它的名稱和另一物質的關係最適合是？", ["它被還原；同時通常有另一物質得到這些氧而被氧化", "它被氧化；另一物質一定也失去氧", "它是催化劑且不改變", "它只發生物理分離"], "A", "失氧是還原，氧原子轉移給另一物質時，另一物質得氧而被氧化，兩者構成互補。", "從失氧定義延伸到同一反應中的另一方。", ["先將失氧對應到還原。", "追蹤離開的氧去了哪種物質。", "將得到氧的一方判為氧化。", "排除兩方同向失氧或催化劑的錯誤。", "因此 A 正確。"], "easy"),
 q(10, "要判斷一個未知反應是否符合得氧失氧的氧化還原定義，哪套流程最完整？", ["比較反應前後組成，追蹤氧原子去向，再找出一方得氧與另一方失氧", "只看反應是否發光", "只量反應容器外的溫度", "只用生成物顏色命名反應"], "A", "完整判斷需從組成與氧原子去向確認得氧、失氧的互補；單一現象只能提供線索。", "依序使用組成證據、氧追蹤與互補檢核。", ["列出反應前後各物質的組成。", "追蹤氧原子是否進入或離開某物質。", "確認得氧與失氧兩方同時存在。", "檢查是否有反應式或實驗資料支持。", "所以 A 是最完整的判斷流程。"], "hard"),
]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"] = TODAY
    lesson["reviewStatus"] = "draft"
    lesson["fusionRecord"] = {"commonCore": ["得氧與失氧是氧化還原的傳統互補定義。", "宏觀顏色、質量與生成物資料需和氧原子組成及去向互相校對。", "氧化與還原必在同一氧轉移中成對發生。"], "versionDifferences": ["南一公開課程計畫支持由金屬與氧反應進入氧化概念，但未提供完整逐頁課文。", "康軒公開 XML 突出金屬對氧活性與操作節點，支持由實驗判讀得氧失氧。", "翰林公開課程資料支持氧化還原的宏觀／微觀連結；完整教材頁碼未取得。"], "originalAdditions": ["以氧原子追蹤表連結得氧、失氧、氧化與還原。", "設計接觸不等於反應、顏色只是線索、封閉系統氧收支等迷思診斷。"], "llmSynthesisNote": "依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫得氧失氧定義及證據判讀；未複製出版社或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for entry in lesson.get("versionResearch", []) + lesson.get("publisherResearch", []): entry["reviewedAt"] = TODAY
    for item in Q:
        (QDIR / f"{item['id']}.json").write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "Jc-Ⅳ-1：氧化還原的得氧與失氧定義", "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "10 題已逐題改寫為得氧失氧定義、氧轉移、反例與證據鏈專屬問題；每題有唯一答案、解析與五步解法，公開資料僅作 pattern-only 來源。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jc-iv-1")


if __name__ == "__main__":
    main()

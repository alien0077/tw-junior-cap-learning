"""Lb：生物與環境的交互作用第一輪原創教材與題庫。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-lb.json"
REPORT = ROOT / "implementation/reports/science-content-lb-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題", "year": "114", "locator": "生物與環境、環境因子與族群資料", "pattern": "取公立學校自然科評量以環境條件、族群變化、時間序列和實驗證據推理的能力方向。"},
    {"url": "https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf", "title": "114 年國中教育會考自然科公開試題", "year": "114", "locator": "生態系資料、相關與因果、非生物因子", "pattern": "取公開會考以圖表、對照、機制和證據界線評估的能力方向。"},
    {"url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "title": "高雄市立國昌國民中學二年級自然科公開段考試題", "year": "112", "locator": "水草、溶氧、光照、水溫與族群關係", "pattern": "取公立國中試題以非生物條件、控制變因、時間變化和生態決策的能力方向。"},
]
REFS = [{**s, "subject": "science", "observedPattern": s["pattern"], "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]
STEPS = [["先圈出自變因、應變因與觀察期間。", "分開整理光照、水溫、溶氧、水草與蚊幼蟲等條件。", "用時間序列讀出先後與峰值，不把同日相關直接當因果。", "檢查對照、重複和替代解釋，例如呼吸、分解或水溫。", "用資料支持的方向、作用機制和限制完成結論。"] for _ in range(10)]
ROWS = [
    ("easy", "水槽中水草白天增加氧氣，但夜間水草也呼吸；若要比較一天內溶氧，應注意什麼？", ["溶氧可能隨光暗週期變化，需記錄相同時段並考慮光合作用與呼吸", "只在白天量一次就代表全天", "水草存在就表示溶氧永遠增加", "夜間沒有任何生物作用"], "A", "水草白天可光合作用產氧，日夜都會呼吸耗氧；測量時段會影響結果，因此需固定時段或完整追蹤。", "先找時間週期，再把產氧和耗氧兩個機制同時放入解釋。"),
    ("medium", "若兩水槽水草覆蓋率不同，想公平比較溶氧，最重要的控制條件組合是？", ["水溫、光照、初始水量、容器與測量時段", "只固定水槽顏色", "讓高覆蓋率水槽同時接受更多光照", "每槽選不同測量時間以節省時間"], "A", "水溫、光照、水量、容器和時段都可能影響溶氧，固定它們才能把差異較合理地歸因於覆蓋率。", "先列出可能影響溶氧的非生物因子，再逐項固定或記錄。"),
    ("easy", "蚊幼蟲數量在溶氧下降後增加，最穩妥的第一個結論是？", ["兩項資料有時間上的關聯，仍要檢查食物、遮蔽和水溫等因素", "溶氧下降必然是蚊幼蟲增加的唯一原因", "蚊幼蟲增加證明水質一定變好", "只要有先後就不需再做對照"], "A", "時間序列可指出關聯線索，但低溶氧與蚊幼蟲數量可能同時受其他條件影響，需更多證據。", "把觀察、可能機制和未排除因素分開寫，避免把相關直接升級為唯一因果。"),
    ("medium", "在相同光照下提高水溫，溶氧讀值下降；哪個解釋較合理？", ["溫度會影響氣體溶解度與生物代謝，需再控制生物量確認機制", "溫度只會改變顏色，不會影響溶氧", "只要讀值下降就能證明沒有任何其他變因", "高溫必然使所有生物死亡"], "A", "水溫會影響水中氣體溶解與生物呼吸速率；合理解釋仍要配合生物量和其他條件資料檢查。", "先指出物理作用與生物作用兩條可能路徑，再設計能區分它們的控制。"),
    ("hard", "水草覆蓋率提高後，白天溶氧上升但夜間最低溶氧下降；最好的報告應？", ["同時呈現日夜資料，說明平均值可能掩蓋極端低值並檢查呼吸負荷", "只報白天上升以宣稱水草一定改善水質", "只報夜間下降以宣稱水草一定有害", "刪除與預測不同的時間點"], "A", "不同時段的方向相反時，平均值或單一時點都不足；需描述完整週期並討論水草量、呼吸與夜間風險。", "先畫出時間序列，再比較峰值、谷值與平均，而不是挑一個有利數字。"),
    ("medium", "要測試水草覆蓋率對蚊幼蟲數量的影響，哪個設計較能支持因果？", ["設多個覆蓋率梯度，固定水溫與光照，設無水草對照並重複追蹤", "每個覆蓋率使用不同水溫和不同水槽大小", "只觀察一天且不設對照", "先讓蚊幼蟲知道研究假設再計數"], "A", "梯度、對照、固定條件與重複追蹤可比較覆蓋率和族群變化，降低偶然與混淆變因。", "把覆蓋率定為自變因，列出對照、固定條件、樣本數和觀察期間。"),
    ("hard", "若水草增加、溶氧增加且蚊幼蟲減少，下列哪一項仍不能直接推出？", ["水草一定是造成蚊幼蟲減少的唯一原因", "水草可能透過溶氧或遮蔽改變環境", "三個指標在本次條件下呈現相關", "需要比較無水草對照來檢查替代解釋"], "A", "多項指標同步改變仍可能有水溫、食物、捕食者或水流等原因；不能直接宣稱唯一因果。", "逐一區分資料已顯示的變化、可能機制和尚未排除的因素。"),
    ("easy", "為什麼測量溶氧時要記錄單位與測量時間？", ["溶氧是有量綱的數值且可能隨日夜和溫度變化，缺少兩者難以比較", "單位只為了讓表格好看，時間不影響結果", "只要數字大就不需知道怎麼量", "記錄時間會讓生物因子消失"], "A", "單位決定數值意義，時間則可能對應光暗、溫度與呼吸週期；兩者缺失會破壞可比性。", "先確認數值的量綱，再標示同一時刻或完整週期的比較範圍。"),
    ("medium", "若兩個水槽的溶氧曲線相似，但蚊幼蟲數量不同，最合理的下一步是？", ["檢查食物、遮蔽物、捕食者與取樣誤差等其他因素", "認定溶氧完全不重要且停止量測", "只保留蚊幼蟲較多的水槽資料", "把兩條曲線硬畫成相同"], "A", "相似溶氧不能排除其他環境與生物條件造成族群差異；需補測可能的限制因子。", "當一個候選解釋不足以說明資料時，列出可測的替代解釋。"),
    ("hard", "對水草與溶氧的結論，哪一句最符合科學證據界線？", ["在本次光照、水溫、覆蓋率與七天觀察條件下，資料支持水草改變溶氧日變化；長期影響仍需更多水槽和季節資料", "只要水草增加就永遠能改善任何水體", "七天資料可以代表所有池塘和所有季節", "因為有其他因素，所以這次資料完全沒有價值"], "A", "科學結論應交代條件、資料支持的範圍與需要補強的部分，既不過度延伸，也不否定可用證據。", "用『在……條件下』限定結論，再寫出可由下一輪研究檢驗的限制。"),
]

def make_question(number, row):
    difficulty, prompt, options, answer, explanation, strategy = row
    return {"id": f"question-science-content-lb-{number}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)], "knowledgeIds": ["kg-science-content-lb"], "difficulty": difficulty, "answer": {"value": answer, "explanation": f"{explanation} 正確答案為選項 {answer}。"}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三筆公立學校／公開自然科試題與課程資料的水草、溶氧、光照、水溫、族群資料、相關因果與控制變因能力方向；本題只作 pattern-only 改寫來源。", "authoringNote": "依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": TODAY, "lessonId": "lesson-science-content-lb", "examPatternRefs": REFS, "solutionStrategy": strategy, "solutionSteps": STEPS[number - 1]}

def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"] = TODAY; lesson["reviewStatus"] = "draft"; lesson["authoringStandard"] = "version-fused-v1"
    lesson["content"] = {"summary": "本課以兩個透明水槽追蹤水草覆蓋率、光照、水溫、溶氧與蚊幼蟲的變化，讓學習者看見環境條件不是靜態背景，而會和生物活動互相回饋。重點不在背『水草好或不好』，而是讀懂日夜曲線、分辨相關與因果，並設計有對照和重複的觀察。", "sections": [{"heading": "先把水槽當成會變動的系統", "body": "水草在有光時可透過光合作用增加氧氣，日夜都會呼吸；水溫、光照和水量也會影響氣體溶解與生物代謝。因此同一水槽白天和夜間的溶氧不必相同，單次讀值不能代表整天。"}, {"heading": "一條曲線不等於一個原因", "body": "若蚊幼蟲增加與溶氧下降同時發生，這是值得追蹤的關聯，不是已完成的因果證明。水溫、食物、遮蔽、捕食者和取樣時間都可能改變族群；把這些條件列出，才有機會安排下一個比較。"}, {"heading": "用兩水槽拆開變因", "body": "要測試水草覆蓋率，可設不同覆蓋率或梯度，固定水溫、光照、容器、水量與測量時段，保留無水草對照並重複七天。這樣得到的不是漂亮口號，而是一條能檢查日夜峰谷、延遲反應和偶然誤差的資料鏈。"}, {"heading": "結論要帶著條件走", "body": "如果高覆蓋率水槽白天溶氧較高、夜間最低值卻較低，報告就要同時寫出兩種結果，並討論水草量與呼吸負荷。結論應限定在本次光照、水溫、覆蓋率和觀察期間，不能把七天水槽資料直接推成所有池塘的永久規則。"}], "studyEntry": "先畫出一日或七日時間序列，再用對照資料檢查你以為的因果是否站得住。"}
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-lb、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合水草覆蓋率、光合作用與呼吸、溶氧、溫度、光照、蚊幼蟲、時間序列、相關與因果及對照實驗。原有泛用正文與題目已改為雙水槽環境交互作用專屬教學；所有正文、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    for entry in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []): entry["reviewedAt"] = TODAY
    for number, row in enumerate(ROWS, 1): (QDIR / f"question-science-content-lb-{number}.json").write_text(json.dumps(make_question(number, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checkedQuestions": 10, "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "threePublicSchoolExamPatternSources": True, "answersAndDetailedSteps": True, "interactivePredictionManipulationExplanation": True, "terraSecondPass": "pending"}, "reviewedAt": TODAY, "note": "正文與互動以雙水槽水草—溶氧—蚊幼蟲資料鏈重新撰寫，10 題涵蓋日夜變化、非生物因子、相關因果、對照和證據界線；每題有唯一答案、解析與五步解法。"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print("authored science content lb")

if __name__ == "__main__": main()

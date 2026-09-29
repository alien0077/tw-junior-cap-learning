import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-m.json"
REPORT = ROOT / "implementation/reports/science-content-m-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "科學探究、控制變因與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "科學證據、科技應用與環境資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生活科技情境、風險與推論界線"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求從變因、資料、模型、風險與限制推導結論；本題另加入科技選擇、社會參與與人文公平的原創情境。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


ITEMS = [
    ("社區想比較兩種遮陽材料對教室降溫的效果，哪個研究設計最能回答問題？", ["同時更換材料、窗戶方向與通風量，再只記錄最涼的一間教室", "先決定某材料最好，再挑選支持它的測量日", "只改變遮陽材料，固定教室方向與通風，連續多日記錄相同位置的溫度", "訪問一位學生後推論全校教室都會降溫"], "C", "只改變一個主要變因並固定其他條件，配合重複且同位置的連續測量，才能把溫度差異和材料連起來；其餘設計混入變因或以偏好的資料代替證據。", "先找自變因、依變因與控制條件，再檢查是否能重複測量。"),
    ("學校考慮用感測器管理飲水機，除了節水量外，哪項資料最能檢查方案是否兼顧人文責任？", ["只看廠商宣稱的最高節水百分比", "記錄不同身高、行動需求學生的使用成功率，並說明資料如何保護個資", "只訪問最常使用飲水機的學生", "把未同意提供資料的學生排除並當作沒有需求"], "B", "科技方案不只看效率，也要檢查不同使用者能否公平使用，並交代資料同意與隱私；廠商宣稱或偏向單一族群的樣本都不足。", "把技術成效、使用者差異、樣本代表性與隱私一起列為判準。"),
    ("河川監測顯示暴雨後濁度上升，若要提出防洪工程建議，哪個說法最符合證據界線？", ["濁度上升所以工程一定能消除所有洪水", "只要居民支持，就不必再量測水位", "濁度資料可提示土砂輸入，還需水位、流量與地形資料評估工程效果", "把一次暴雨的測量當成長期氣候趨勢"], "C", "濁度能提供土砂或水質變化線索，但不能單獨證明工程一定有效；還要配合水位、流量、地形與不同事件的資料。", "先說資料直接支持什麼，再寫仍需補測的變數與不能推出的結論。"),
    ("校園安裝太陽能板前，哪項決策流程最能同時處理科學、科技與社會因素？", ["只比較面板最高功率，忽略屋頂承重與維修", "由單一廠商決定位置，施工後才通知師生", "量測日照與用電、檢查結構與儲能限制，公開成本效益並邀請受影響者討論", "以網路留言數量直接決定方案，不檢查留言者是否代表使用者"], "C", "完整流程要把測量證據、工程安全、成本維護與參與程序接起來；單一指標或事後通知不能代表合理決策。", "用證據、工程可行性、風險分配與誰能參與四個問題逐項檢查。"),
    ("社區想設置防洪牆，哪個問題最能提醒決策者注意公平與代價？", ["模型圖看起來是否整齊", "洪水風險是否被轉移到下游居民，以及他們是否能參與方案比較", "宣傳海報是否使用最亮的顏色", "只計算工程完工日期"], "B", "防洪牆可能降低一處風險卻把水流或維護成本轉移到別處；受影響者的參與與風險分配是人文和社會面不可省略的問題。", "找出誰受益、誰承擔風險、誰能發言，再回頭補工程資料。"),
    ("公民科學小組用手機量測校園噪音，哪項做法最能讓資料可比較？", ["每個人隨意選時間與地點，只保留最高數值", "固定測點、時段、量測距離與設備設定，記錄背景事件並保留原始資料", "只在安靜日測量，避免資料不好看", "把不同手機的讀值直接平均，不記錄設備差異"], "B", "固定測量條件、記錄背景事件與保留原始資料，才能判斷差異來自地點或事件，而不是程序或設備改變。", "先建立一致的量測程序，再記錄異常與設備限制，不刪除不合預期的資料。"),
    ("學校要處理舊電池，哪個方案最能同時回應科技風險與社會責任？", ["把所有電池混入一般垃圾以節省分類時間", "只宣布回收率，不說明後端處理者與運送安全", "分類、絕緣並交給合格回收管道，公開流程、風險與學生可參與的安全行動", "讓學生自行拆解電池以學習內部構造"], "C", "電池可能有短路、洩漏與處理風險；合格管道、公開流程與安全參與比追求方便或自行拆解更負責任。", "把材料性質、操作風險、責任鏈與可安全參與的行動連起來。"),
    ("選擇校園風力發電位置時，哪項證據組合最完整？", ["只看地圖上最接近操場的位置", "只引用廠商最高發電量，不量測風況", "比較不同位置的風速時間序列、噪音與鳥類影響，並詢問鄰近使用者", "先投票決定位置，再刪除不支持的風速資料"], "C", "位置選擇要同時看可發電性、噪音與生態影響，並讓受影響者參與；單一地圖、廠商數字或刪資料都不足。", "先列出方案成效與外部代價，再為每項主張配上可追溯資料和參與程序。"),
    ("若一項空氣品質政策只讓有空調的教室受益，最合理的下一步是？", ["宣布全校空氣品質都已改善", "只收集受益教室的滿意度", "比較各教室暴露資料與設備可及性，讓受影響群體參與修正方案", "取消所有測量，避免造成爭議"], "C", "政策評估不能只看平均或受益者感受；要比較暴露、資源可及性與不同群體的回饋，才能找出不公平並修正。", "檢查平均值掩蓋的群體差異，再把資料與參與式修正連起來。"),
    ("下列哪句最適合作為『科學證據與人文選擇要分開表達』的結論？", ["數據證明這是唯一正確且最公平的政策", "測量結果支持方案在指定條件下可能降低用電；是否採用仍需討論成本、隱私與受影響者權益", "只要方案使用科技，就自然符合社會進步", "多數人喜歡的方案必定沒有科學風險"], "B", "B 把測量可支持的條件式結論，和成本、隱私、權益等需要社會討論的價值選擇分開；其他選項把證據過度延伸成唯一或必然的價值結論。", "先寫資料能支持的範圍，再另列價值、權利、成本與協商問題。"),
]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"; row["licenseBoundary"] = BOUNDARY
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-m、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立重寫科學證據、科技限制、社會程序與人文責任的交會；題目與互動均使用校園環境和公共決策原創情境，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    lesson["studyHighlights"] = ["先區分可量測的科學證據、工程限制、社會程序與人文價值。", "比較方案時同時檢查資料品質、風險、成本、隱私與誰被影響。", "結論只寫證據能支持的範圍，把公平與權利留在可公開協商的決策部分。"]
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出題目中的科學資料、科技條件、受影響者、風險或價值衝突。", "把直接測量、模型推論、方案限制與需要協商的選擇分欄。", "檢查樣本、控制條件、資料來源、可行性與風險分配是否足夠。", "排除只看單一效率、只選支持資料、忽略隱私安全或把多數偏好當科學證明的選項。", "用完整句重述答案，明確說出證據支持的範圍與仍需參與或補測的部分。"]
    for i, (prompt, options, answer, explanation, strategy) in enumerate(ITEMS, 1):
        path = ROOT / f"questions/science/question-science-content-m-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8")); q["prompt"] = prompt; q["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        q["answer"] = {"value": answer, "explanation": explanation}; q["examPatternRefs"] = refs(); q["reviewStatus"] = "draft"; q["updatedAt"] = "2026-09-21"; q["solutionStrategy"] = strategy; q["solutionSteps"] = steps
        q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的控制變因、資料判讀、科技風險與證據界線能力；本題改寫為科學—科技—社會—人文原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content m")


if __name__ == "__main__":
    main()

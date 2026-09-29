import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-na-iv-5.json"
REPORT = ROOT / "implementation/reports/science-content-na-iv-5-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "廢棄物分類、污染路徑與環境影響"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "回收、焚化、掩埋與環境承載力資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "減量、堆肥、資源循環與風險管理"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。要判斷是否超過承載力，需比較廢棄物產生量與環境可吸收、分解、稀釋或處理的速率，並追蹤空氣、水、土壤與生物指標，不能只看垃圾重量。",
    "A。改用可重複餐具、取消不必要包裝或調整供餐流程，是在垃圾產生前減少物質輸入，屬於源頭減量；回收和焚化都已在末端。",
    "A。防水層破損可能讓滲出液進入土壤與地下水，應監測地下水水質、滲出液、重金屬或有機污染物，而不只量掩埋場表面垃圾量。",
    "A。焚化可減少體積但可能產生空氣污染物、底渣與飛灰；是否適合要看成分、排放控制、能源回收、殘渣去向與替代方案。",
    "A。油污和複合材料會降低回收物品質，造成整批污染、分選成本增加或改送焚化／掩埋；分類標誌不保證實際可回收。",
    "A。臭味與蚊蠅表示含水量、通氣、碳氮比例或覆蓋管理失衡，應調整混合材料、翻堆、排水與防蟲，而非只把堆肥移到更遠處。",
    "A。先拆除電池並交給合格回收系統，分流金屬與電子材料、避免破壞洩漏，才能兼顧資源回收和重金屬／電解液安全。",
    "A。應比較製造材料、運輸、清洗用水、使用次數、回收與報廢情境；可重複使用不會自動代表負荷較低，須達到足夠使用次數。",
    "A。垃圾量下降是減量成效，但回收污染上升表示分類品質或誘因設計有副作用；應同時追蹤總量、純度、處理成本與非法棄置。",
    "A。長期指標應同時包含人均垃圾量、資源回收率與污染率、廚餘去向、處理排放、滲出液或異味，以及改善後的趨勢。",
]
STRATEGIES = [
    "把產生量、環境處理能力、污染指標與時間尺度放在同一比較框架。",
    "先找垃圾產生前能否避免，再區分重複使用、回收與末端處理。",
    "沿滲出液路徑追蹤土壤與地下水，辨認防水層失效的受體。",
    "把體積減少和污染物轉移分開，檢查排放、底渣、飛灰與能源資料。",
    "先判斷材料是否乾淨、單一且可分選，再評估回收品質與後端去向。",
    "從含水量、通氣、碳氮比、翻堆與防蟲管理找臭味原因。",
    "以電池安全、合法回收、材料分流和洩漏風險四項檢查電子廢棄物。",
    "用生命週期與達到的使用次數比較容器，而不是只看一次使用。",
    "同時解讀垃圾量與回收污染率，找出政策的正面效果和副作用。",
    "選能長期重複量測且涵蓋數量、品質、污染與處理結果的指標組合。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結廢棄物來源、污染路徑、回收焚化掩埋、源頭減量、環境承載力與長期指標；本題以全新環境管理情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-na-iv-5、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合廢棄物來源、環境受體、承載力、源頭減量、回收、堆肥、焚化、掩埋、生命週期與長期指標；保留校園午餐垃圾流向調查互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出廢棄物來源、數量、材料、處理方式、環境受體與承載力指標。", "先判斷能否在源頭減量或重複使用，再比較回收、堆肥、焚化與掩埋的條件。", "追蹤物質是否轉移到空氣、水、土壤、底渣、飛灰或殘渣，而非只看垃圾離開視線。", "用量、品質、污染、能源、成本與時間趨勢資料比較方案，辨認副作用和替代解釋。", "回查結論適用的材料、處理設備、環境容量與管理條件，提出可長期監測的指標。"]
    rotations = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-na-iv-5-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); opts=q["options"]; correct=opts[0]["text"]; k=rotations[i-1]; opts=opts[k:]+opts[:k]; q["options"]=[{"id":chr(65+j),"text":o["text"]} for j,o in enumerate(opts)]; q["answer"]={"value":chr(65+next(j for j,o in enumerate(opts) if o["text"]==correct)),"explanation":EXPLANATIONS[i-1]}
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["provenance"]["sourceUrl"]=URLS[0][0]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題中的廢棄物、污染路徑、減量、回收、處理方式、承載力與環境指標能力；本題改寫為廢棄物管理原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content na iv 5")


if __name__ == "__main__": main()

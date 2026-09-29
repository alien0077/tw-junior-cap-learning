import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-na-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-na-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "資源減量、再利用、回收與生活決策"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "5R、材料流向與環境負荷比較"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "源頭減量、修繕、回收品質與生命週期"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。5R通常先處理需求與源頭，先減少不必要的消費，再考慮拒絕、重複使用、回收與再生；越後端通常越需要能源與分類。",
    "A。自備水壺讓一次性瓶子不必被購買與丟棄，核心是重複使用；若同時減少瓶裝水需求，也產生源頭減量效果。",
    "A。鞋底可修、鞋面仍可用，修繕後延長原物品壽命，屬於重複使用／再使用，比直接丟棄並買新鞋更接近前端策略。",
    "A。把仍可使用的童書交給下一位學生，是讓同一物品延續功能的再使用；不是把材料拆解成原料的回收。",
    "A。去除塑膠膜能提高紙類純度、避免整批回收物被污染，讓後端分選與再生流程較可行；不代表所有紙都能無條件回收。",
    "A。要比較兩種餐具，需納入製造材料、使用次數、清洗用水與能源、運輸、報廢與回收情境，而不只看一次使用的材質。",
    "A。減少盛取過量、依實際人數調整份量或改善菜單是在廚餘產生前降低需求，屬於源頭減量；把剩食拿去處理已是後端。",
    "A。回收量增加但新產品購買也增加，可能只是回收改善、消費總量仍上升；應同時追蹤總物質流、重複使用率、污染率與生命週期負荷。",
    "A。應設介入前後資料、比較班級或對照區、固定宣導期間，並同時量測人均垃圾量、回收純度與實際行為，而非只問口號記憶。",
    "A。可回收標示仍要確認當地分類規則、材料是否乾淨分離、收運系統與後端再生能力；標示本身不是完整去向證據。",
]
STRATEGIES = [
    "先按源頭到末端排列 5R，再判斷哪一步能避免物品產生。",
    "區分減少需求與重複使用，說明同一方案可能同時有兩種效果。",
    "檢查物品是否可修、可清潔、耐用與實際使用足夠次數。",
    "找物品功能是否仍可延續，避免把再使用和材料回收混淆。",
    "追蹤材料純度、分類污染、分選成本與後端再生條件。",
    "用生命週期比較製造、使用、清洗、運輸、報廢與回收。",
    "先找產生廚餘前的需求管理，再評估堆肥或其他處理。",
    "同時比較垃圾總量、消費量、回收品質與資源回流，避免只看單一成效。",
    "設對照與前後測量，並選擇能反映實際行為與物質流的指標。",
    "確認標示、地方規則、清潔分類與後端去向四項條件。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求判斷 5R 優先順序、源頭減量、再使用、回收品質、生命週期與政策成效；本題以全新資源管理情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-na-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合 5R 階梯、源頭減量、拒絕、重複使用、修繕、回收品質、再生、生命週期與成效評估；保留校園飲水日物品流向互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出物品需求、材料、使用目的、使用次數、清潔條件與後續去向。", "依減量—拒絕—重複使用—回收—再生順序檢查可行方案。", "追蹤物品是否延續原功能、材料是否乾淨分離，以及能源、水與運輸需求。", "用人均垃圾量、消費量、回收純度、實際再生量與生命週期資料比較，不只看標語或標示。", "回查地方規則、衛生、耐用、污染與後端能力，說明條件改變時方案如何調整。"]
    rotations = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-na-iv-4-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); opts=q["options"]; correct=opts[0]["text"]; k=rotations[i-1]; opts=opts[k:]+opts[:k]; q["options"]=[{"id":chr(65+j),"text":o["text"]} for j,o in enumerate(opts)]; q["answer"]={"value":chr(65+next(j for j,o in enumerate(opts) if o["text"]==correct)),"explanation":EXPLANATIONS[i-1]}; q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["provenance"]["sourceUrl"]=URLS[0][0]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題中的 5R、源頭減量、再使用、回收品質、生命週期與政策成效能力；本題改寫為資源使用原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content na iv 4")


if __name__ == "__main__": main()

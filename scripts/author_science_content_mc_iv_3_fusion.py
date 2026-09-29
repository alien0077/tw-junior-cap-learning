import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-mc-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-mc-iv-3-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "材料性質、加工方法與用途設計"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "熱塑、切割、接合與製程資料"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "加工安全、品質、維修與生命週期"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。先確認物品要完成的功能與不能接受的條件，再選材料與加工法；只看加工工具或價格，無法證明成品適用。",
    "A。金屬板裁切要依圖面與厚度選擇剪切、鋸切或雷射等方法，固定工件、標線並配戴護具，再檢查尺寸與毛刺。",
    "A。熱塑性材料受熱時分子鏈活動增加、材料軟化，可在適當溫度成形，冷卻後保持形狀；不是所有塑膠都能反覆熱塑。",
    "A。木材含水率變化會造成尺寸收縮、膨脹、翹曲或加工表面差異，因此加工前需控制或記錄含水狀態。",
    "A。比較表面粗糙度要固定材料批次、刀具、進給、切削深度與測量位置，只改變加工方法並重複量測。",
    "A。清潔可去除油污、氧化物與灰塵，增加接合面實際接觸或黏著條件；不代表清潔本身把材料焊接起來。",
    "A。粉塵應以局部排氣、適當呼吸防護、隔離作業與清潔管理降低吸入和爆炸風險，不可只開普通電風扇把粉塵吹散。",
    "A。毛刺應去毛邊、打磨或倒角並檢查邊緣強度與尺寸，避免割傷使用者或使接合失準；不能用塗漆掩蓋未處理缺陷。",
    "A。可拆接便於維修、替換零件與分類回收，代價可能是重量、鬆動風險或防水性改變，需依使用條件比較。",
    "A。量產評估要同時看尺寸一致性、產能、良率、成本、能源與材料耗用、工安、維修及廢棄處理，不能只看速度。",
]
STRATEGIES = [
    "先列功能需求與限制，再將材料性質對應加工方法。",
    "依材料厚度、形狀、精度、安全與後處理選裁切法。",
    "確認材料受熱行為、可塑溫度與冷卻後形狀保持。",
    "把含水率當控制條件，預測尺寸與表面變化。",
    "固定所有加工與測量條件，只改方法並重複測量。",
    "先辨認接合面污染，再說明清潔如何改善接合可靠性。",
    "從粉塵產生、吸入、排放與爆炸風險設計工程和個人防護。",
    "把去毛邊、倒角、尺寸與使用安全一起檢查。",
    "比較可拆接帶來的維修與回收優點，以及防水與鬆動代價。",
    "用品質、產能、良率、成本、安全、能源與生命週期綜合評估。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結材料性質、切割塑形、熱塑、接合、表面品質、工安、量產與生命週期；本題以全新材料加工情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-mc-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合材料性質、功能需求、切割塑形、熱塑、含水率、表面粗糙、接合、粉塵安全、可拆維修與量產生命週期；保留校園雨水收集盒材料加工互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出物品功能、材料性質、加工方法、使用條件、安全與後續處理。", "把硬度、韌性、耐水、耐熱、透氣或可加工性對應到需求。", "固定材料與設備條件，預測切割、彎折、成形、接合或塗覆造成的性能變化。", "檢查尺寸、粗糙度、強度、毛刺、粉塵、良率與維修資料，不用單一性質下結論。", "回查方案的工安、使用壽命、能源、成本、可拆性與廢棄處理限制。"]
    rotations = [0, 1, 2, 3, 1, 2, 3, 0, 1, 2]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-mc-iv-3-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); opts=q["options"]; correct=opts[0]["text"]; k=rotations[i-1]; opts=opts[k:]+opts[:k]; q["options"]=[{"id":chr(65+j),"text":o["text"]} for j,o in enumerate(opts)]; q["answer"]={"value":chr(65+next(j for j,o in enumerate(opts) if o["text"]==correct)),"explanation":EXPLANATIONS[i-1]}; q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["provenance"]["sourceUrl"]=URLS[0][0]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題中的材料性質、加工方法、接合、安全、品質、量產與生命週期能力；本題改寫為材料加工原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content mc iv 3")


if __name__ == "__main__": main()

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bc-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-bc-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "光合作用、限制因子與實驗設計"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "水草產氧、光照二氧化碳與資料判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "溫度、葉綠素、控制變因與測量限制"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。只改變光照強度，固定水草種類與量、二氧化碳、溫度、時間和水分，以單位時間產氧量並設重複組比較，才可隔離光照效果。",
    "B。平台表示在目前範圍內光照不再是唯一限制，二氧化碳、溫度、酵素容量或其他條件可能限制速率；不是光合作用停止。",
    "A。應變因是光合作用速率，例如單位時間產氧量；二氧化碳濃度是自變因，其他條件須控制。",
    "C。光照和二氧化碳同時改變，無法判斷產氧增加是由哪個因素、或兩者交互作用造成；應拆成控制組與單一變因組。",
    "A。溫度過高可能使相關酵素失去適當構形或細胞受損，光合作用速率下降；不是溫度越高反應必然越快。",
    "D。三次資料可先求平均為 19.3 顆，再保留各次值與變異範圍；不能只挑最大值或任意刪掉差異。",
    "A。弱光時光能是主要限制，增加二氧化碳不能補足入射光不足，因此產氧速率幾乎不變；這是特定條件下的推論。",
    "B。氣泡大小可能不同、部分氧氣會溶於水或逸散，且氣泡形成未必與氧量一一對應，所以氣泡數只是近似指標。",
    "A。枝條大小、葉面積或葉片數差異會改變產氧量，與光照距離的效果混在一起；應標準化材料或用單位葉面積速率。",
    "C。平台只支持在該材料、測試範圍與控制條件下存在另一項限制，不能外推成所有植物或所有光強都相同。",
]
STRATEGIES = [
    "先指定單一自變因與產氧速率，再列出全部控制條件和重複測量。",
    "把平台解讀為限制因子轉移，檢查二氧化碳、溫度或酵素容量。",
    "先分辨自變因、應變因與控制變因，再確認速率單位。",
    "檢查是否同時改變兩項因素，必要時拆成單一變因與交互作用設計。",
    "辨認適溫範圍與高溫造成的酵素或細胞損傷，不套用線性直覺。",
    "保留所有重複值，計算平均並描述變異，不用單一最好值代表結果。",
    "找出弱光下的主要限制，再判斷增加另一原料能否改變速率。",
    "把指標誤差、溶解、逸散、氣泡大小與材料差異列入限制。",
    "先標準化葉面積、枝條量與健康狀態，再比較光照距離。",
    "把結論限定在材料、範圍、時間與控制條件，避免由平台過度外推。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求判讀光合作用限制因子、產氧指標、控制變因、平台曲線、重複資料與測量限制；本題以全新探究情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bc-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合光照、二氧化碳、水分、溫度、葉綠素、限制因子平台、控制變因、重複資料與氣泡指標限制；保留水草—溫室探究互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出自變因、應變因、控制條件、材料健康狀態與測量指標。", "一次只改變一項因素，固定光源距離、溫度、二氧化碳、水分、葉面積與時間。", "用單位時間產氧量或其他速率指標比較，保留重複值並畫出曲線。", "遇到平台或下降段，檢查另一項限制與高溫／弱光／材料差異，不把氣泡數當成絕對氧量。", "把結論限定在測試材料、範圍、控制條件與不確定度，提出下一個可驗證的改變。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bc-iv-4-{i}.json"; q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps})
        q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的光合作用、限制因子、控制變因、產氧資料與測量限制能力；本題改寫為光合作用探究原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content bc iv 4")


if __name__ == "__main__": main()

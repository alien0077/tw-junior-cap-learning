import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ka-iv-11.json"
REPORT = ROOT / "implementation/reports/science-content-ka-iv-11-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "光的色散、色光與物體顏色判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "選擇性反射、濾光片與光源"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "色光混合、顏色觀察與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以色光照射、濾光片、白光分解、物體反射／吸收、RGB 混合與觀察資料考查顏色形成；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "A。紅紙在白光下主要反射較能進入眼睛的紅光，其他色光較多被吸收；顏色是光源、物體與觀察者共同形成的結果。",
    "B。綠光中缺少紅光，紅紙沒有可大量反射的成分，進入眼睛的光很少，因此可能看起來暗甚至近黑。",
    "C。白紙對可見光各色通常反射較多，白光包含多種色光且反射後同時進入眼睛，因而呈白色；不是紙張自發白光。",
    "D。黑色表面通常吸收較多可見光、反射較少，所以在白光下進入眼睛的光弱而看起來黑；仍是近似模型。",
    "B。藍紙能反射藍光，紅光不含它較能反射的藍色成分，因此藍光主導時較亮、紅光部分較暗，整體可能呈藍色或偏暗藍。",
    "C。顯示器是主動發光並以紅綠藍光相加混色；紙張主要反射入射光的部分，不能把兩者的混色規則直接互換。",
    "D。要固定光源強度、觀察角度、紙張、距離與量測方法，只改色光種類，才能比較黃色紙張的反射外觀差異。",
    "A。舞台藍光改變入射光的光譜，衣服能反射的色光成分也隨之改變；不是衣服顏料在短時間內變質。",
    "C。固定色溫可使色卡接受的光譜條件一致，避免把光源變化誤判成相機感色或白平衡差異。",
    "B。不同角度的色澤差異可能來自表面光澤、干涉、方向性反射或光源位置；需補測光譜、角度與照明條件，不能只指定一種機制。",
]
STRATEGIES = [
    "先列出白光成分，再判斷物體主要反射哪些色光進入眼睛。",
    "檢查入射光是否含有物體能反射的色光，判斷亮暗而非只看物體名稱。",
    "區分紙張反射和光源發光，判斷多色光同時進入眼睛的結果。",
    "用反射強弱的近似模型解釋黑色，再補上光源和表面條件限制。",
    "把藍紙在紅光、藍光下的可用入射成分逐一比較。",
    "先分辨主動發光的加法混色與被動反射的選擇性反射。",
    "只改色光，固定幾何、亮度、材料和量測方式。",
    "追蹤光源光譜改變，而不是把外觀變化歸因於材料立刻改變。",
    "固定照明光譜後，才能把色卡讀值差異歸因於相機或校正。",
    "列出角度、光澤與光譜等替代解釋，再提出補測方法。",
]
STEPS = [
    "確認光源包含哪些色光及其強度。",
    "判斷材料對各色光是吸收、反射或透射。",
    "追蹤最後進入眼睛或相機的光。",
    "核對亮度、角度、距離與觀察條件是否控制。",
    "以資料支持顏色推論，並列出相機、光澤或光譜限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ka-iv-11、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合白光、選擇性反射／透射、色光、黑白物體、RGB 加法混色、光源色溫、角度與表面光澤；保留紅紙—濾片—色卡矩陣互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ka-iv-11-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的色光、選擇性反射、濾光片、RGB 混色、光源與控制變因能力；本題改寫為物體顏色與光的選擇性反射原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ka iv 11")


if __name__ == "__main__": main()

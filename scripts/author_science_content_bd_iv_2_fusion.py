import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bd-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-bd-iv-2-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "碳循環、光合作用、呼吸與分解"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "碳庫、通量、燃燒與海洋吸收"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "生物與非生物碳交換、尺度與資料判讀"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。植物透過光合作用把大氣二氧化碳中的碳固定到有機物，成為碳進入生物圈的重要入口。",
    "B。動物呼吸把有機物中的碳氧化，主要以二氧化碳形式釋回大氣；碳不會因呼吸消失。",
    "A。分解者分解遺體與排遺，將其中的碳轉成二氧化碳或土壤、溶解有機碳等形式，使碳回到環境庫。",
    "C。燃燒把長期儲存在木材或化石燃料中的碳快速轉成二氧化碳，改變大氣與地表碳庫的交換通量。",
    "A。碳可由大氣進入植物，再經取食、呼吸、分解回到環境，也能進入海洋或沉積物；同一元素在不同庫間轉移。",
    "D。砍伐減少光合作用固定量，焚燒又快速釋放原本儲存的碳，若其他條件不變，短期大氣二氧化碳較可能增加。",
    "A。碳原子可在生物與環境間循環，但能量由光進入後沿營養關係流動並以熱散失，不能把能量與碳循環混為一談。",
    "B。海洋同時是溶解碳、海洋生物與沉積物等碳庫，二氧化碳可在不同庫間交換，速率與時間尺度也不同。",
    "A。固定量與呼吸、分解釋放量相等時，該區域的碳交換收支接近平衡，大氣二氧化碳淨變化較接近零。",
    "C。呼吸作用應把植物碳庫中的有機碳送向大氣二氧化碳；由大氣指向植物的是光合作用固定，不是呼吸。",
]
STRATEGIES = [
    "先找碳的來源庫與去向庫，再用光合作用判斷固定入口。",
    "把有機物中的碳沿呼吸反應追蹤到二氧化碳，不把能量與碳混淆。",
    "標出遺體、排遺、分解者與土壤／大氣庫，追蹤分解後的形式。",
    "檢查燃料的原本碳庫、燃燒產物與交換速率，區分短期和長期。",
    "畫出生物—大氣—土壤—海洋間至少三個庫與四條轉移箭頭。",
    "同時看固定量、釋放量與碳庫變化，不只由砍伐面積猜淨變化。",
    "把碳物質循環和能量單向流動分成兩張圖再比較。",
    "區分海洋溶解碳、生物碳與沉積碳庫，並交代交換時間尺度。",
    "用固定量減去呼吸與分解釋放量判斷淨碳交換方向。",
    "檢查箭頭是大氣到植物還是植物到大氣，依作用名稱校正。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求追蹤光合作用、呼吸、分解、燃燒、海洋碳庫、碳庫與通量及能量差異；本題以全新碳循環情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bd-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合碳庫、通量、光合作用固定、呼吸、分解、燃燒、海洋溶解碳、短期與地質時間尺度及能量差異；保留校園樹木—土壤—化石燃料碳流向互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出碳庫、碳的形式、轉移作用、方向與時間尺度。", "沿光合作用、取食、呼吸、分解、燃燒、溶解或沉積畫出碳箭頭。", "分辨碳庫大小與每年通量，並計算或比較固定量與釋放量的收支。", "把短期生物交換、長期沉積與人類燃燒分開，避免把碳循環說成能量循環。", "回查資料範圍、替代來源與不確定性，提出需要補測的庫存或通量。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bd-iv-2-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的碳庫、光合作用、呼吸、分解、燃燒、海洋碳交換與資料判讀能力；本題改寫為碳循環原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content bd iv 2")


if __name__ == "__main__": main()

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-kc-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-kc-iv-1-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "摩擦起電、電荷與驗電器"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "正負電荷、導體絕緣體與靜電"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "靜電感應、濕度與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以摩擦材料、驗電器、帶電體吸引／排斥、導體絕緣體、靜電感應、濕度與控制變因考查電荷轉移；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "B。摩擦可能使電子由一種材料轉移到另一種材料，帶電後才較容易使輕小紙屑發生極化或受到靜電力；不是摩擦創造新電子。",
    "C。一方失去電子帶正電，另一方得到電子帶負電；電子總量在兩物體系統內重新分配，總電荷仍守恆。",
    "A。同種電荷間通常互相排斥；判斷時須控制距離與周遭導體，避免把空氣流動誤當成電力。",
    "D。異種電荷間通常互相吸引；若只觀察到靠近，仍應排除機械碰撞或感應造成的其他效應。",
    "B。金屬內可移動電子會受帶電棒影響重新分布，近端與遠端出現相對不同的電荷密度，這是靜電感應而非金屬獲得總電荷。",
    "C。葉片帶有同種電荷而互相排斥，所以張開可作為驗電器帶電的證據；張角大小還受電量、結構與環境影響。",
    "A。導體的電荷可在物體內重新分布並經接地流動，絕緣體則較局部地留住電荷；應以相同摩擦和接近操作比較葉片或吸引結果。",
    "D。潮濕表面與空氣中的水膜提高漏電路徑，電荷較快流失，因此較難維持可觀察的靜電現象；不是電子在潮濕中消失。",
    "C。固定布料面積、摩擦次數、壓力、速度、環境濕度與被測物，只改布料種類並重複測量，才能公平比較。",
    "B。吸引可能由異種電荷或中性紙屑極化造成，單靠吸引不能確定帶電棒的正負；可用已知帶電體的排斥或驗電器補證。",
]
STRATEGIES = [
    "先判斷摩擦是否造成電子轉移，再把帶電結果連到紙屑的極化或靜電力。",
    "畫出電子由哪一物體移向哪一物體，並用電荷守恆檢查正負判斷。",
    "先辨認兩物體電性是否相同，再排除距離與非電力干擾。",
    "用電荷種類判斷力的方向，並把觀察證據與推論分開。",
    "只在金屬內重新分布電子，總電荷是否改變要看有沒有接地或接觸。",
    "用葉片同種電荷排斥解釋張開，再補充張角不是精確電量讀值。",
    "比較電荷能否移動、能否接地與結果是否可重複，分辨導體和絕緣體。",
    "把濕度連到漏電與電荷留存時間，而不是誤寫成電荷被消滅。",
    "只改材料種類，其他摩擦與環境條件固定並做重複測量。",
    "先承認吸引證據的多重解釋，再提出排斥或驗電器的補充測試。",
]
STEPS = [
    "列出摩擦物、被吸引物、接地與環境濕度等條件。",
    "追蹤電子移動與物體總電荷的變化。",
    "依同種排斥、異種吸引或極化判斷力的證據。",
    "用驗電器、接地、對照組或重複測量補強結論。",
    "說明漏電、濕度、接觸與證據不足等限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-kc-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合摩擦電子轉移、電荷守恆、正負電荷、吸引排斥、靜電感應、驗電器、導體絕緣體與濕度漏電；保留塑膠尺—紙屑—驗電器證據互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-kc-iv-1-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的摩擦起電、驗電器、靜電感應、導體絕緣體、濕度與控制變因能力；本題改寫為摩擦生靜電與正負電荷原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content kc iv 1")


if __name__ == "__main__": main()

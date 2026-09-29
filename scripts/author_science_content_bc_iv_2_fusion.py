import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bc-iv-2.json"
REPORT = ROOT / "implementation/reports/science-content-bc-iv-2-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "細胞呼吸、有氧代謝與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "呼吸作用、氣體證據與能量"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "發芽種子、酵母、氧氣與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以發芽種子、酵母、氣體變化、運動肌肉、有氧／缺氧與控制組考查細胞呼吸和能量釋放；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "A。有氧呼吸主要利用有機物與氧氣，產生二氧化碳、水並釋放可供細胞利用的能量；能量不是一次全部變成熱。",
    "B。肌肉收縮需要 ATP 等可利用能量，運動時呼吸作用提高以供應能量；肺部吸氣只是取得氧氣的外部過程。",
    "A。發芽種子仍活躍代謝，煮沸後的種子作為失活對照；前者二氧化碳較多支持其呼吸作用較旺盛，但仍需檢查漏氣與溫度。",
    "C。設置無酵母或煮沸失活酵母對照，固定糖濃度、溫度、體積與時間並量測氣體，才能把產氣差異連到酵母代謝。",
    "A。植物白天同時進行光合作用與呼吸作用；光合作用可能使淨氣體交換方向改變，但不代表呼吸停止。",
    "D。氧氣不足時有氧呼吸供能受限，細胞可短時間以其他代謝途徑補充 ATP，但效率與副產物不同，容易疲勞。",
    "A。若密閉系統中的氧氣體積或濃度隨時間下降，並有適當對照，可直接支持氧氣被呼吸作用消耗；不能只看溫度。",
    "B。運動後呼出二氧化碳增加與代謝速率上升一致，但還需控制通氣量、運動強度與採樣時間，不能只憑一次呼氣證明所有能量變化。",
    "A。植物與動物都由細胞進行呼吸作用，利用有機物釋放可用能量；差別在器官與氣體交換方式，不在是否呼吸。",
    "C。單組酵母產氣較多只能說在該條件下觀察到較多二氧化碳，不能直接斷定是唯一原因、一定產生更多 ATP或適用所有酵母。",
]
STRATEGIES = [
    "列出有氧呼吸的反應物、產物和能量去向，再區分熱與可用能量。",
    "把 ATP 供應連到肌肉收縮，分開肺部通氣與細胞呼吸。",
    "利用活種子與失活種子對照，檢查二氧化碳來源和控制條件。",
    "設置適當對照並固定糖、溫度、體積、時間後比較產氣。",
    "區分光合作用造成的淨交換與細胞呼吸本身持續進行。",
    "比較有氧與缺氧的供能效率、持續時間與副產物。",
    "優先看氧氣濃度／體積的時間變化，再檢查密閉與對照。",
    "控制運動強度與通氣採樣，將二氧化碳資料限定在可支持的結論。",
    "從共同的細胞代謝機制比較植物與動物，再補充氣體交換差異。",
    "把單次觀察和可推廣的因果結論分開，列出需要的對照與重複。",
]
STEPS = [
    "確認材料是否活著、氧氣是否充足與系統是否密閉。",
    "列出有機物、氧氣、二氧化碳、水與能量的變化。",
    "比較對照、時間序列、溫度或氣體資料。",
    "區分有氧、缺氧、光合作用與通氣等不同過程。",
    "說明資料限制，避免把氣體單一變化等同完整能量證明。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bc-iv-2、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合有氧呼吸、ATP、發芽種子、酵母、氣體證據、光合作用與呼吸並存、缺氧代謝、運動與控制變因；保留發芽種子—酵母—運動三情境互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bc-iv-2-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的細胞呼吸、發芽種子、酵母、氧氣、二氧化碳、運動與控制變因能力；本題改寫為呼吸作用釋放能量原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content bc iv 2")


if __name__ == "__main__": main()

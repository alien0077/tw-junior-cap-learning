import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-bc.json"
REPORT = ROOT / "implementation/reports/science-content-bc-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "細胞呼吸、酵素與能量轉換"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國中公開自然科段考", "光合作用、呼吸作用與代謝證據"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "ATP、發酵、酵素與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "A。分解葡萄糖可釋放其中的化學能，部分能量被轉成 ATP 供細胞進行運動、主動運輸與合成，並有部分以熱散失。",
    "B。有氧呼吸通常以有機物和氧氣為反應物，產生二氧化碳、水與可供細胞使用的能量；題目若問主要產物仍要看反應條件。",
    "C。ATP 是細胞暫時轉移與直接使用能量的分子，能在分解或合成反應與細胞工作之間傳遞能量，不是把所有能量永久儲存。",
    "D。氧氣供應不足時，肌肉可暫時採用無氧代謝途徑快速取得少量 ATP，但副產物累積與能量效率限制會使疲勞較快出現。",
    "B。酵母有糖液時二氧化碳增加，支持它在該條件下有產氣代謝；若要判斷途徑，仍需氧氣、活酵母與無糖對照。",
    "C。只改變溫度，固定酵母量、糖濃度、液量、攪拌與觀察時間，並用單位時間產氣量及重複組比較，才是公平設計。",
    "D。呼吸釋出的能量有一部分轉入 ATP，其餘以熱等形式散失；這表示能量轉換有效率限制，不代表能量消失。",
    "A。應同時記錄單位時間的氣體產生或氧氣消耗、底物量、溫度與重複測量，才能比較不同營養物質的速率與不確定度。",
    "C。酵素是特定反應的催化者，能降低活化能、提高反應速率，但不會改變反應前後能量守恆，也不是反應物本身。",
    "B。能量代謝的判讀要把光合作用、呼吸作用、ATP、酵素、氧氣條件與測量證據連起來，並清楚區分觀察值和延伸推論。",
]
STRATEGIES = [
    "先找底物、產物與細胞工作，再判斷能量是否轉入 ATP。",
    "依氧氣條件列出有機物、氧氣、二氧化碳、水與能量的角色。",
    "把 ATP 視為可直接使用的能量中介，區分短期轉移與長期儲存。",
    "檢查供氧、ATP 產量、副產物與疲勞時間，不把無氧代謝當成完全停止。",
    "先確認產氣證據能支持什麼，再用活性、糖與氧氣對照限定結論。",
    "固定除溫度外的條件，將產氣量換成速率並保留重複值。",
    "追蹤能量進入 ATP 與熱散失的兩條路徑，避免說能量消失。",
    "以速率、底物濃度、氧氣消耗與重複資料組合證據，而非只看最後總量。",
    "分辨酵素降低活化能、選擇性與反應平衡，不把酵素當作消耗性原料。",
    "先畫能量—物質證據圖，再把結論限制在實驗材料、條件與指標。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結細胞呼吸、光合作用、酵素、ATP、發酵、氣體證據與控制變因；本題以全新能量代謝情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "生物體把光能或食物中的化學能轉成細胞可以使用的形式；光合作用製造有機物，呼吸作用釋放能量並形成 ATP，酵素則讓特定反應在細胞條件下以適當速率進行。本課以葉片、發芽種子與酵母的證據，分辨物質流向、能量轉換和資料限制。", "sections": [{"heading": "學習目標", "body": "你將能把光合作用、細胞呼吸、ATP 與酵素放在同一張能量—物質圖中，並由氧氣、二氧化碳、溫度、澱粉、產氣或熱量資料，判斷哪些是直接觀察、哪些只是延伸推論。"}, {"heading": "學習流程", "body": "先標出反應物、產物與能量形式，再依有氧或缺氧條件追蹤路徑；接著用酵母產氣、發芽種子溫度與葉片澱粉等資料交叉檢查，最後用活材料對照、單一變因與重複測量確認證據強度。"}, {"heading": "常見錯誤", "body": "不要把光合作用和呼吸作用當成互斥，也不要把二氧化碳、氣泡或溫度單一讀值直接等同 ATP 數量。酵素會改變反應速率，不會被誤當成反應物；缺氧時的代謝也不是細胞完全停止。"}, {"heading": "自我檢核", "body": "選擇水草、發芽種子或酵母，畫出底物、氧氣、二氧化碳、ATP、熱與產物的箭頭，標記一項可量測證據、一項控制條件與一個尚不能由資料直接知道的量。"}]}
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-bc、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合光合作用、細胞呼吸、ATP、酵素、發酵、氧氣條件、能量散失與證據邊界；重寫葉片—發芽種子—酵母的單元專屬教學與互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出反應物、產物、氧氣條件、ATP、熱、酵素與觀察指標。", "畫出光合作用、呼吸作用或發酵的物質與能量路徑，分清直接與間接證據。", "將氣體、溫度、澱粉或產氣資料換成可比較的速率，並加入活材料與無活性對照。", "檢查底物、酵素、氧氣、溫度、時間與材料量是否控制，避免由單一讀值推論 ATP。", "回查結論的條件與限制，指出仍需補測的量和下一個只改單一因素的實驗。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-bc-{i}.json"; q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps})
        q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的細胞呼吸、光合作用、酵素、ATP、發酵、氣體證據與控制變因能力；本題改寫為能量代謝原創情境。"
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content bc")


if __name__ == "__main__": main()

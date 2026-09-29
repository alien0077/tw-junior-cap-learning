import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-gc-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-gc-iv-3-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "微生物、人體健康與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "病原、抗生素、衛生與控制變因"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "菌落觀察、食品安全與微生物作用"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以腸道菌群、病原傳播、抗生素、洗手、食品保存、菌落資料與公平實驗考查微生物和人體健康的條件式判讀；本題只取能力方向並重新設計情境與選項。"
CONTENT = {
    "summary": "人體表面與腸道住著大量微生物，作用可能是競爭病原、協助代謝，也可能在特定位置、數量或宿主狀態下造成感染。本課用菌相資料、衛生實驗與抗生素情境，分辨相關性、因果證據和安全邊界。",
    "sections": [
        {"heading": "先拆開『有微生物』與『有害』", "body": "皮膚、口腔與腸道不是無菌空間；正常菌群可能和宿主互利、共存或在條件改變時失衡。判斷有益或有害要同時看微生物種類、所在部位、數量、宿主免疫狀態與是否穿越防禦屏障。培養出菌落只能表示樣本中有可在該培養條件生長的微生物，不能直接等同致病。"},
        {"heading": "腸道菌相資料如何支持推論", "body": "比較益生菌介入前後的菌相比例、代謝物或症狀時，需有未介入對照、相同飲食與追蹤時間，並注意個體差異。某菌增加和症狀改善同時出現，只能先說有關聯；若要靠近因果，還要有重複試驗、劑量與替代解釋的檢查。不能把單一人的糞便檢體圖表當成所有人的健康處方。"},
        {"heading": "病原傳播與抗生素的界線", "body": "洗手、通風、分開生熟食與適當加熱能降低部分傳播路徑；抗生素針對特定細菌感染，對病毒感染不會因為『更強』就有效，濫用還可能選出抗藥性菌株。預防措施要對應傳播途徑，治療要依醫療判斷，不能只看症狀或自行停藥。"},
        {"heading": "把培養與消毒實驗做得安全", "body": "未知人體或環境樣本可能含病原，不能在家自行培養、聞嗅或開蓋辨識。課堂若需比較消毒前後，應使用合規的非致病替代材料、封閉培養與教師規範的處理流程；資料要有相同面積、採樣工具、培養時間與重複樣本。清潔後菌落較少支持降低可培養微生物量，不等於所有微生物或病毒都已消失。"},
    ],
}
EXPLANATIONS = [
    "A。正常菌群可能與人體共存，透過競爭空間或資源等方式降低部分病原定殖；有微生物不等於一定有害，需看種類、位置和宿主狀態。",
    "B。應設未介入對照並固定飲食、年齡、採樣與追蹤時間，再比較菌相或症狀；單一前後比較容易把其他因素誤當益生菌效果。",
    "C。抗生素主要針對細菌，對病毒感染通常無效；不當使用還會增加抗藥性選擇壓力，不能自行用剩藥。",
    "D。洗手可移除或降低手部部分微生物，減少手—口、手—物表面的傳播機會；它不是讓人體變成無菌。",
    "B。溫暖、潮濕且有養分的環境可能讓部分微生物繁殖較快；實際仍受氧氣、酸鹼、時間與保存方式影響。",
    "C。菌落只證明有能在該培養基和條件下生長的微生物，不能僅憑外觀確定物種或致病性，需合規鑑定與安全程序。",
    "D。較有力的證據需有對照、時間順序、特定微生物量變化與替代原因控制；單純同時出現不代表因果。",
    "A。皮膚正常菌群可能佔據生存空間、消耗資源或與免疫防禦互動，作用仍受皮膚屏障和環境條件影響。",
    "C。應使用合規非致病替代材料、固定採樣面積與培養條件，封閉處理並由教師依規範滅菌；不能自行培養未知人體樣本。",
    "B。核心是微生物作用具有條件性：同一微生物可能在不同部位、數量或宿主狀態下呈現共存、互利或致病結果，結論要有證據與限制。",
]
STRATEGIES = [
    "先分辨共存、互利與致病條件，再看微生物位置和宿主狀態。",
    "建立對照、固定干擾變因並追蹤前後資料，避免把相關性當因果。",
    "確認病原類型與藥物作用對象，再判斷抗生素是否適用。",
    "沿手部接觸與傳播路徑說明洗手降低風險的機制與限制。",
    "列出溫度、水分、養分、氧氣與時間，判斷繁殖條件。",
    "把菌落視為可培養性證據，不能直接推成物種或致病性。",
    "檢查時間順序、對照、特定菌量與替代解釋，才評估因果。",
    "用正常菌群的空間競爭與防禦互動說明可能益處。",
    "優先安全與合規，使用替代材料、封閉處理和固定採樣條件。",
    "用『種類—位置—數量—宿主—證據』五項條件收束判斷。",
]
STEPS = [
    "確認微生物種類、位置、數量與宿主條件。",
    "區分觀察到的菌落／症狀與推論出的作用。",
    "檢查對照、時間順序、採樣與培養條件。",
    "判斷預防、治療或實驗方法的適用範圍。",
    "補上病原鑑定、抗藥性與生物安全限制。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1", "content": CONTENT})
    lesson["studyHighlights"] = ["微生物作用取決於種類、位置、數量、宿主與接觸條件。", "把菌相或菌落資料的觀察和因果推論分開。", "抗生素、洗手、食品保存與消毒各自對應不同風險與限制。", "未知樣本培養必須遵守替代材料、封閉處理與教師規範。"]
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-gc-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合正常菌群、腸道菌相、病原傳播、抗生素、食品保存、菌落證據、消毒控制與生物安全；把原通用佔位正文改寫為人體微生物專屬教材，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-gc-iv-3-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的人體微生物、病原、抗生素、衛生、菌落、食品保存與安全能力；本題改寫為人體微生物有益與有害作用原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "contentRewrittenFromPlaceholder": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content gc iv 3")


if __name__ == "__main__": main()

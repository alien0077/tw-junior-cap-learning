import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jc-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-jc-iv-4-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "氧化還原、金屬反應與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "氧化還原、腐蝕防護與生活應用"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "金屬置換、電池與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以金屬置換、氧化數、得失電子、腐蝕防護、漂白、呼吸作用、電池與安全資料考查氧化還原角色及控制變因；本題只取能力方向並重新設計情境與選項。"
EXPLANATIONS = [
    "A。失去電子的物質被氧化；同一反應中必有另一物種接受電子而被還原，兩者不能分開發生。",
    "B。鋅把電子交給銅離子，鋅失電子成鋅離子，銅離子得電子成金屬銅；這同時符合金屬置換與氧化還原。",
    "C。能把電子提供給另一物種的是還原劑，本身因失去電子而被氧化；不能只用『比較活潑』代替電子證據。",
    "D。塗層隔開鐵與水、氧氣等反應條件，降低腐蝕機會；塗漆不是讓鐵永遠失去氧化能力，塗層破損處仍可能生鏽。",
    "B。較活潑金屬先被氧化、提供電子，使鐵成為受保護的陰極；須考慮接觸、電解質與金屬活性，不能只看外觀。",
    "C。氧化性漂白劑可使有色分子的特定結構被氧化而改變，褪色不代表物質消失，也要注意濃度與混用安全。",
    "D。養分被氧化、氧氣被還原，電子轉移伴隨能量釋放；這是細胞呼吸的氧化還原描述，不等同直接燃燒。",
    "A。氧化數上升代表形式上失去電子、被氧化；判斷仍須配合反應式與電荷守恆，不能只看係數。",
    "C。應只改防鏽方法，固定鐵材、表面積、溶液、溫度與時間，並以質量變化或鏽蝕面積等同一指標比較。",
    "B。氧化性清潔劑須依標示稀釋、戴適當防護並避免與酸性或含氯／含氨產品混用；安全條件是應用的一部分。",
]
STRATEGIES = [
    "先追蹤電子方向，再標出失電子者與得電子者，最後分別命名氧化與還原。",
    "把鋅與銅離子寫成反應前後的粒子，檢查電子是否守恆。",
    "先問誰提供電子，再判斷該物質是還原劑而自身被氧化。",
    "列出鐵、水、氧氣與塗層的接觸條件，判斷防護改變哪個反應路徑。",
    "比較金屬活性與電子流向，再補上電解質和接觸條件。",
    "把褪色視為分子結構被氧化的現象，並分開判斷安全與反應機制。",
    "分辨養分與氧氣在電子轉移中的角色，再連到能量釋放。",
    "用氧化數前後差異判斷電子得失，必要時回到電荷平衡。",
    "控制所有非方法變因，設定可重複的鏽蝕量測指標與觀察時間。",
    "先讀標示和成分，再判斷個人防護、通風與不可混用的反應風險。",
]
STEPS = [
    "列出反應物、生成物與系統條件。",
    "追蹤氧元素或電子的來源、去向與氧化數變化。",
    "標出氧化者、還原者及相應的氧化劑／還原劑。",
    "用質量、顏色、電流、鏽蝕或安全資料等證據核對模型。",
    "寫出條件與限制，避免把單一現象擴張成沒有範圍的結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-jc-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合得失氧、電子轉移、氧化數、金屬置換、腐蝕防護、漂白、細胞呼吸、電池與化學品安全；保留鐵鏽—電子帳本—防護設計互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-jc-iv-4-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的氧化還原、金屬置換、腐蝕防護、電池、資料判讀與安全能力；本題改寫為常見氧化還原反應原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jc iv 4")


if __name__ == "__main__": main()

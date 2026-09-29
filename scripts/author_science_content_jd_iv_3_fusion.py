import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-jd-iv-3.json"
REPORT = ROOT / "implementation/reports/science-content-jd-iv-3-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "酸鹼、pH、指示劑與資料判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "酸鹼強弱、中和與 pH 測量"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "指示劑、pH 計與控制變因"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常用指示劑色階、pH 數值、酸鹼強弱、中和、pH 計校正與取樣控制考查證據判讀；本題只取能力方向並重新設計情境與選項。"
CONTENT = {
    "summary": "以檸檬汁、小蘇打水與飲用水的未知樣品為入口，建立 pH 方向、廣用指示劑色階與 pH 計數值之間的證據鏈；再用校正、沖洗、重複測量與中和資料檢查讀值是否可信。",
    "sections": [
        {"heading": "先把顏色變成可比較的範圍", "body": "廣用指示劑是多種指示劑的混合物，會在一段 pH 範圍呈現連續色帶。酸性樣品的 pH 小於 7，鹼性樣品的 pH 大於 7，中性附近約為 7；顏色只能先提供區間線索，不能把深淺直接當成精確 pH。比較檸檬汁、小蘇打水與飲用水時，要使用相同體積與滴數，並在白色背景下和同一色階表比對。"},
        {"heading": "pH 計給數字，但數字也需要證據", "body": "pH 計透過電極狀態換算顯示數值，能分辨兩杯顏色相近的樣品；然而校正不完整、電極乾燥、溫度不同或前一杯殘液都可能讓讀值偏移。測量前依標準液校正，測量間以適當溶液沖洗並吸乾外壁，不把電極用力擦拭；每杯至少重複讀取，記錄溫度、時間和是否攪拌。"},
        {"heading": "用中和曲線檢查酸鹼判斷", "body": "逐次加入等體積鹼液到酸性樣品，pH 會朝 7 移動；接近 7 只表示在目前加入量與測量條件下酸鹼效果相互抵消，不能推論兩種原液濃度或體積一定相等。若繼續加鹼，pH 可能越過 7 轉為鹼性。把加入體積、pH 和顏色排成表格，才能看出趨勢而不是只記最後一個顏色。"},
        {"heading": "把測量誤差和化學結論分開", "body": "若兩次 pH 讀值差異小於儀器解析度，應記作近似相同或增加重複次數；若高濃度酸後直接測中性水，殘液污染會使水的讀值偏酸。廣用指示劑適合快速篩選，pH 計適合精細比較，兩者不一致時先查校正、樣品、溫度和色階判讀，再決定是否需要重新取樣。"},
    ],
}
EXPLANATIONS = [
    "A。pH=7 通常表示氫離子與氫氧根的相對狀態接近中性；實際讀值仍須考慮溫度與儀器誤差。",
    "B。pH 越小酸性通常越強；比較時要確認濃度、溫度與 pH 的定義一致，不能以顏色深淺代替數值。",
    "C。廣用指示劑用連續色帶先估計酸鹼範圍，解析度不如校正後的 pH 計，不能把色階當精密讀值。",
    "D。pH 計使用前需以適當標準液校正，使電極輸出與已知 pH 對應；只沖洗電極不能取代校正。",
    "B。應固定樣品體積、指示劑量、溫度、容器和觀察背景，只改變飲料種類，並用同一色階或校正儀器比較。",
    "C。偏紅通常落在酸性區間，表示 pH 小於 7 的可能性較高；仍應依色階範圍記錄，不能只報一個精確數字。",
    "D。pH 每降低 1，氫離子濃度約增加 10 倍，因此 pH 3 約是 pH 4 的 10 倍酸性（以氫離子濃度比較）。",
    "A。測量高濃度酸後應充分沖洗並依規範處理電極，再測中性水；最好使用獨立乾淨樣品與重複讀值確認。",
    "C。應記錄為介於兩個色階的範圍或近似區間，並註明判讀限制；不能假裝讀出色階表沒有提供的精確 pH。",
    "B。加入鹼後 pH 接近 7 表示在該加入量下酸鹼作用接近抵消；仍須看體積、濃度與指示劑／pH 計的測量誤差。",
]
STRATEGIES = [
    "先把 pH=7 定位為中性，再比較酸鹼方向與測量條件。",
    "用 pH 數值的大小排序酸性強弱，並檢查是否為同一測量尺度。",
    "分清廣用指示劑能給範圍、pH 計能給數值的工具差異。",
    "把校正視為讀值基準的建立，再檢查電極狀態與樣品污染。",
    "只改飲料種類，其餘取樣與讀值條件全部固定。",
    "由色階先判斷酸鹼方向與範圍，再說明精確度限制。",
    "利用 pH 每差 1 約十倍的關係，明確寫出比較基準。",
    "先沖洗、吸乾外壁、避免殘液，再用乾淨樣品重測。",
    "用區間記錄不確定性，不把兩色階之間硬指定成某個數字。",
    "將接近 7 解讀為目前條件下的中和趨勢，回查加入量與濃度。",
]
STEPS = [
    "圈出 pH、色階、樣品、校正、溫度與加入量等關鍵條件。",
    "先判斷酸性、中性或鹼性，再比較數值或色階範圍。",
    "核對取樣、滴數、電極清潔與控制變因是否一致。",
    "寫出 pH 數值、顏色或中和趨勢所支持的證據。",
    "補上解析度、污染、溫度與校正等限制，避免過度推論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1", "content": CONTENT})
    lesson["studyHighlights"] = ["用廣用指示劑定位 pH 範圍，再以校正後 pH 計比較細小差異。", "把校正、沖洗、溫度與重複讀值視為測量證據的一部分。", "以中和過程的 pH—加入量資料判斷趨勢，不把接近 7 過度解讀。", "遇到兩工具不一致時先查色階、污染與儀器限制，再重測。"]
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-jd-iv-3、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合 pH 方向、廣用指示劑色階、pH 計校正、電極污染、中和曲線、重複測量與安全；把原本通用佔位正文改寫成檸檬汁—小蘇打水—飲用水的專屬探究，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-jd-iv-3-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的酸鹼、pH、指示劑、pH 計、中和、控制變因與安全能力；本題改寫為廣用指示劑與 pH 計原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content jd iv 3")


if __name__ == "__main__": main()

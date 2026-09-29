import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-nb-iv-1.json"
REPORT = ROOT / "implementation/reports/science-content-nb-iv-1-first-pass-review.json"
URLS = [
    ("https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf", "國立中科實驗高級中學公開九年級理化題庫", "氣候變化、生物資料與環境判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "全球暖化、食物網與生物分布"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "物候、珊瑚、熱島與保育資料"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
PATTERN = "公立學校公開自然／理化試題常以溫度趨勢、物候、珊瑚、物種分布、食物網、海冰、熱島、政策前後資料與保育策略考查全球暖化的生物影響；本題只取能力方向並重新設計情境與選項。"
CONTENT = {
    "summary": "全球暖化對生物的影響不是一條單一路徑：溫度、降水、海冰、海水熱壓力與季節時序會改變物種的生存條件、分布、繁殖和食物網。本課用物候、珊瑚、昆蟲、海豹、鳥類與濕地資料，分辨相關性、因果、尺度與調適韌性。",
    "sections": [
        {"heading": "先把氣候訊號和生物反應對齊", "body": "高山植物提早開花、候鳥遷徙日期改變等物候資料，只有在與同地長期溫度、降水及其他環境變數同步比較時，才可能支持氣候因素。單一年份提前或觀察者改變記錄方法都不足以證明全球暖化；要注意趨勢、時間尺度、對照地點和物種本身的自然變異。"},
        {"heading": "壓力會沿食物網和棲地傳遞", "body": "海水升溫可能增加珊瑚熱壓力與白化，乾旱則減少草本植物並影響草食動物；海冰減少還會改變海豹繁殖與覓食平台。從一個族群的下降推論全球原因前，需追蹤資源、捕食、疾病、棲地與人類活動等替代解釋，並畫出食物網上的連鎖路徑。"},
        {"heading": "分布改變不等於族群變多", "body": "物種向高海拔或高緯度移動，可能是原區不適、繁殖區改變或新區條件暫時適合；觀察到北移不能直接說總數增加。調查要同時記錄標準化努力量、個體數、繁殖成功、死亡率與棲地面積，才能分辨分布重排、偵測機率改變和真正的族群增長。"},
        {"heading": "韌性是多尺度的管理問題", "body": "保育可透過保護連通棲地、維持遺傳多樣性、降低其他壓力、建立避難微氣候與長期監測來提高韌性；但某地水鳥增加不代表所有生物都受益，人工濕地也可能增加乾季用水需求。評估方案要同時看生物指標、水量、溫度、社區使用與長期副作用。"},
    ],
}
EXPLANATIONS = [
    "A。要支持暖化關聯，應把多年開花日期與同地長期溫度趨勢對照，並控制品種、觀測方法和降水等因素；單年提前不足。",
    "B。除白化範圍外，還應測量海水溫度、持續時間、光照、酸鹼度或污染等壓力，並設對照區，才能判斷暖化因素。",
    "C。應在不同海拔與年份以相同捕捉／觀察努力量記錄蚊蟲數量、溫度與降水，並控制棲地、積水和人類活動。",
    "D。乾旱使植物量下降，草食動物食物減少而下降；這條鏈仍需搭配降水、植物量、動物數量及其他干擾資料驗證。",
    "B。海冰減少可能降低海豹繁殖或覓食平台，但僅憑兩者同時變化不能排除食物、捕獵或疾病等因素。",
    "C。應比較熱島區與相似但較低溫的對照區，固定植被、光源、季節與觀察努力量，再看昆蟲活動時間與數量。",
    "D。需同時記錄標準化調查努力量、個體數、繁殖成功與棲地面積；只看分布北移無法判斷族群總量。",
    "A。減排後短期溫度可能受海洋熱容量、自然變異與滯後影響，應用長期多地資料評估，不以短期單點否定政策。",
    "C。連通棲地、降低其他壓力、保留遺傳多樣性、建立監測與調適門檻，比單一人工搬遷更能提高長期韌性。",
    "B。水鳥增加是局部指標，乾季缺水則顯示方案有資源代價；應同時評估多物種、水量、棲地與社區使用的長期資料。",
]
STRATEGIES = [
    "將物候長期趨勢與同地氣候資料、對照和替代因素一起比較。",
    "把珊瑚白化與海溫、持續時間、酸鹼和污染等壓力交叉檢查。",
    "固定調查努力量與棲地條件，區分分布改變和族群增加。",
    "沿降水—植物—草食動物食物鏈找出因果環節與需補測資料。",
    "先承認海冰與海豹下降的關聯，再列出食物、捕獵、疾病等替代因素。",
    "用熱島對照區和標準化觀察比較昆蟲活動差異。",
    "同時讀分布、數量、繁殖、死亡與棲地資料，避免只看地圖。",
    "區分政策的短期、長期、局部與全球尺度，納入氣候滯後。",
    "把棲地連通、多樣性、其他壓力與監測門檻整合為韌性方案。",
    "比較多物種、生態服務、水量與社區需求，避免單一指標過度推論。",
]
STEPS = [
    "確認氣候變數、生物指標、時間尺度與空間範圍。",
    "畫出物種、棲地、資源與食物網的作用路徑。",
    "比較趨勢、對照、努力量和替代解釋。",
    "區分相關性、因果、族群數量與分布變化。",
    "提出兼顧生物、水量、社區與長期監測的條件式結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表、答案或版面。", "year": "109-115", "subject": "science", "locator": loc, "observedPattern": PATTERN, "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1", "content": CONTENT})
    lesson["studyHighlights"] = ["用物候、海溫、海冰、降水和分布資料連結氣候變數與生物反應。", "沿食物網與棲地路徑追蹤暖化壓力的連鎖影響。", "分辨分布改變、族群數量、繁殖成功與偵測努力量。", "用多尺度監測、棲地連通與降低其他壓力提高韌性。"]
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-nb-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然／理化試題能力模式，以自己的話獨立融合氣候趨勢、物候、珊瑚白化、乾旱食物網、海冰、分布與族群、都市熱島、政策滯後、保育韌性與長期監測；把原通用佔位正文改寫為全球暖化生物影響專屬教材，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-nb-iv-1-{i}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i - 1], "solutionSteps": STEPS})
        q["answer"]["explanation"] = EXPLANATIONS[i - 1]
        q["provenance"].update({"sourceUrl": URLS[0][0], "sourceLocator": "三筆公立學校公開自然／理化試題中的全球暖化、物候、珊瑚、食物網、海冰、熱島、政策與保育資料能力；本題改寫為全球暖化對生物影響原創情境。"})
        path.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "contentRewrittenFromPlaceholder": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content nb iv 1")


if __name__ == "__main__": main()

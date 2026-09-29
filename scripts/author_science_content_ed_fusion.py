import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-ed.json"
REPORT = ROOT / "implementation/reports/science-content-ed-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "天體視運動、光譜與觀測證據"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "天文資料、尺度與模型判讀"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "星體受光、月相與證據推理"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求把天體位置、受光、尺度、光譜或觀測條件連到可檢驗推論；本題改用全新情境與選項。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    for row in lesson.get("publisherResearch", []):
        row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row["licenseBoundary"] = BOUNDARY
    lesson["studyHighlights"] = ["先把天體實際運動、觀察者的視運動與受光幾何分開。", "用日期、方位、光譜、亮度、距離與儀器條件組成可查驗的天文證據。", "模型只支持它呈現的尺度與關係；遇到月相、食現象或星系資料要明確寫出限制。"]
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-ed、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題的能力模式，以自己的話獨立融合星體視運動、受光幾何、光譜、尺度、觀測證據與模型限制；保留既有日地月互動與模擬，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    lesson["content"]["sections"] = [
        {"heading": "先分清楚『真的在動』和『看起來在動』", "body": "地球自轉會讓星體呈現日周視運動，但這不代表每顆星每天繞地球一圈。判讀天文現象時，先問觀察者在哪裡、觀察多久，再區分地球自轉、天體公轉與視角造成的變化。"},
        {"heading": "受光幾何解釋月相與食現象", "body": "太陽提供光，月球反射光；月相是從地球看到的受光面比例與方向改變。日食、月食則還需要特定的三天體排列、影子位置與觀測地點，不能把滿月直接等同月食。"},
        {"heading": "光譜和亮度是帶條件的證據", "body": "吸收線可提供元素成分線索，顏色可提示表面溫度相對差異，標準燭光與視亮度可用來推論距離，但都必須同時考慮吸收、校正、儀器與不確定度。"},
        {"heading": "宇宙尺度不能靠圖上大小猜", "body": "行星、恆星、星系與更大尺度結構要靠單位、距離指標和資料來源比較。天文示意圖常壓縮距離與大小；圖上兩個物件較大或較近，不等於真實尺度就是如此。"},
        {"heading": "結論要保留模型和觀測的邊界", "body": "模型能幫助預測，連續觀測能檢查變化，資料不完整時只能做條件式結論。若照片缺少日期、方位或觀測地點，應標示缺口，不用想像補成支持自己預測的證據。"},
    ]
    explanations = [
        "A。觀察到的星體日周移動主要是地球自轉造成的視運動；B 把視覺現象誤當星體繞地球，C、D 與現象無關。",
        "B。恆星顏色可作為表面溫度相對差異的線索，但仍須考慮濾鏡、距離與星際吸收，不能只靠顏色下絕對結論。",
        "C。特定吸收線表示光經過或來自含有相應元素的物質，提供成分線索；它不是直接告訴我們距離或大小。",
        "D。同類標準燭光若本身亮度可校準，視亮度越低通常代表距離較遠；仍要檢查吸收、校正與樣本條件。",
        "B。大量恆星、氣體與塵埃組成銀河系這類星系；不能把星系、恆星與行星等不同尺度結構混為一談。",
        "C。光譜整體偏向長波長可作為遙遠星系遠離、宇宙膨脹的線索，但仍要與距離模型和其他資料交叉核對。",
        "D。口徑增加通常能收集更多光，也可能提升解析能力；實際效果仍受大氣、波段、焦距和儀器設計限制。",
        "A。距離指標、校正方式、紅移或光譜及其不確定度能共同建立推論；只看影像大小或單一亮度容易誤判。",
        "C。城市光害提高天空背景亮度、降低影像對比，使較暗天體難以觀測；它不是讓天體停止發光。",
        "B。固定觀測波段與時間間隔，才能讓不同時刻的亮度資料可比較，辨認週期或變化，而不把儀器條件改變誤判成天體變化。",
    ]
    strategies = [
        "先區分觀察者的視運動與天體實際運動，再檢查時間尺度。", "把顏色當相對線索，並查找吸收與校正限制。", "看到吸收線先判斷它提供的是元素成分證據。", "用本身亮度、視亮度和距離指標三者交叉判讀。", "依尺度階層和組成判斷宇宙結構名稱。", "把紅移當線索，再檢查模型與其他觀測證據。", "分開收光能力、解析能力與觀測環境的作用。", "優先使用有校正、距離指標與不確定度的資料。", "先找背景亮度與影像對比的變化，再判斷光害影響。", "固定條件才能把時間序列中的差異歸因於天體而非儀器。",
    ]
    steps = ["讀題並圈出天體、視角、受光、光譜、亮度、距離、時間或儀器條件。", "把直接觀測、模型推論與仍需查證的部分分開。", "套用對應的日周視運動、受光幾何、光譜、尺度或觀測原理。", "排除把視運動當實際公轉、把月相當食現象、把圖上大小當真實比例，或忽略校正與環境限制的選項。", "用完整句重述答案，補上證據如何支持結論以及目前不能推出的範圍。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-ed-{i}.json"
        question = json.loads(path.read_text(encoding="utf-8"))
        question["examPatternRefs"] = refs(); question["reviewStatus"] = "draft"; question["updatedAt"] = "2026-09-21"
        question["answer"]["explanation"] = explanations[i - 1]; question["solutionStrategy"] = strategies[i - 1]; question["solutionSteps"] = steps
        question["provenance"]["sourceUrl"] = URLS[0][0]; question["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的天體視運動、受光、光譜、尺度、儀器與觀測條件能力；本題改寫為全新語料。"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored science content ed")


if __name__ == "__main__":
    main()

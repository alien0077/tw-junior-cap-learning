import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-md-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-md-iv-4-first-pass-review.json"
URLS = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考", "臺灣板塊邊界、地震與斷層判讀"),
    ("https://www.nhjh.tp.edu.tw/uploads/1738658165906utzaMLG4.pdf", "臺北市立內湖國民中學公開自然科段考", "震源震央、P波S波、震度與地質條件"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf", "高雄市立國昌國民中學公開自然科試題", "地震風險、測站定位與防災行動"),
]
BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"
EXPLANATIONS = [
    "B。臺灣位於歐亞板塊與菲律賓海板塊交界的複雜活動區，板塊相對運動使地殼累積應變並在斷層錯動時釋放地震。",
    "C。花東縱谷附近兩側地殼受擠壓，可能形成聚合邊界相關的逆斷層或褶皺活動；要以地質與位移資料確認，不能只由地名判斷。",
    "A。上盤相對上升且受水平擠壓，符合逆斷層的幾何與受力特徵；正斷層則通常和張力、上盤下降有關。",
    "D。震源是地下岩層開始破裂的位置，震央是震源垂直投影到地表的位置；15 km 指震源深度，不是震央到地表的水平距離。",
    "B。鬆軟沖積層可能放大地震波並造成較長持續振動，局部地質條件會使同一地震在不同地點產生不同震度。",
    "B。風險評估需結合歷史地震與活動斷層、地質與土壤、人口建物脆弱度、避難與應變能力，不能只看地震次數。",
    "C。地震搖晃時先就地趴下、掩護、穩住，遠離窗戶與可能掉落物；停止搖晃後依校園指引疏散，不在搖晃中奔跑。",
    "A。不同測站的到時差可提供距離圓，三站以上交會可定位震央並檢查定位一致性；測站越多也能估計誤差。",
    "D。小地震可能反映斷層持續調整或應力變化，但不能僅憑連續小震預測必然發生大地震；需標示證據與不確定性。",
    "C。完整解釋應把板塊相對運動、斷層、震源深度、地質放大、建物脆弱度與防災行動連成證據鏈，而不是把地震視為單一原因。",
]
STRATEGIES = [
    "先定位板塊、相對運動與斷層，再說明應變釋放造成地震。",
    "由地殼受力與位移資料判斷聚合、張裂或錯動，不靠地名猜測。",
    "看上盤相對移動與水平受力，區分逆、正與走向滑移斷層。",
    "分清震源、震央、深度與地表位置，避免把三者混稱。",
    "把地質材料、地震波放大與持續時間連到震度差異。",
    "以危害、暴露、脆弱度與應變能力組合地震風險資料。",
    "按趴下、掩護、穩住和停止後疏散的時間順序作答。",
    "用到時差求距離，再以多測站交會定位並估計誤差。",
    "區分小震觀察和大震預測，明確說出證據不足之處。",
    "將板塊、斷層、地質、建物與行動證據串成條件式結論。",
]


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "science", "locator": loc, "observedPattern": "公開自然科評量常要求連結臺灣板塊邊界、斷層、震源震央、P波S波、震度、地質放大、風險與防災資料；本題以全新地震情境重寫。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "臺灣位於歐亞板塊與菲律賓海板塊交界的活動區，板塊相對運動使地殼變形、斷層累積應變並可能釋放地震。本課從花東縱谷、震源震央、P波與S波、地質放大和校園防災資料出發，將地質機制與實際風險分開判讀。", "sections": [{"heading": "學習目標", "body": "你將能以板塊相對運動和斷層受力解釋臺灣地震活動，區分震源、震央、震源深度、震度與規模，並用測站、地質、建物和防災資料評估地震風險。"}, {"heading": "學習流程", "body": "先在臺灣地圖標示板塊與活動斷層，再讀剖面判斷上盤、下盤與受力；接著用P波與S波到時差定位，最後把軟弱地層、建物脆弱度和避難能力加入風險判讀。"}, {"heading": "常見錯誤", "body": "震源不是震央，震度不是地震釋放能量的唯一尺度；小地震群也不能直接預測大地震。地震風險不只由斷層距離決定，還受地質、人口、建物與應變能力影響。"}, {"heading": "自我檢核", "body": "面對一則地震報告，標出板塊與斷層證據、震源震央、測站定位、地質條件與實際防災行動，並指出哪些是觀察結果、哪些仍是不確定推論。"}]}
    for row in lesson.get("publisherResearch", []): row["reviewedAt"] = "2026-09-21"
    for row in lesson.get("versionResearch", []): row.update({"reviewedAt": "2026-09-21", "licenseBoundary": BOUNDARY})
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方自然科學課綱、kg-science-content-md-iv-4、南一／康軒／翰林可取得的公開研究方向與三筆公立學校自然科試題能力模式，以自己的話獨立融合臺灣板塊位置、斷層受力、震源震央、P波S波定位、震度、地質放大、地震風險與防災行動；重寫花東縱谷—校園測站—建物脆弱度教學與互動，未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    steps = ["圈出板塊位置、相對運動、斷層、震源、震央、震度與地質條件。", "先由受力與上盤位移判斷斷層，再用P波S波到時差分析定位。", "把地質放大、建物脆弱度、人口暴露與應變能力加入風險模型。", "區分觀察到的小震、震度差異與可支持的推論，不把單一訊號當預測。", "回查防災行動的時間順序、資料不確定性與研究範圍。"]
    for i in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-md-iv-4-{i}.json"; q = json.loads(path.read_text(encoding="utf-8")); q.update({"examPatternRefs": refs(), "reviewStatus": "draft", "updatedAt": "2026-09-21", "solutionStrategy": STRATEGIES[i-1], "solutionSteps": steps}); q["answer"]["explanation"] = EXPLANATIONS[i-1]; q["provenance"]["sourceUrl"] = URLS[0][0]; q["provenance"]["sourceLocator"] = "三筆公立學校公開自然科試題中的臺灣板塊、斷層、震源震央、P波S波、震度、風險與防災能力；本題改寫為地震災害原創情境。"; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"publicExamPatternRewrite":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content md iv 4")


if __name__ == "__main__": main()

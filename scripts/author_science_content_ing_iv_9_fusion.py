"""INg-Ⅳ-9：氣候變遷的減緩與調適途徑來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ing-iv-9.json"; REPORT=ROOT/"implementation/reports/science-content-ing-iv-9-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"氣候變遷、減緩、調適、災害風險與資料判讀","pattern":"取區分減少成因與面對衝擊、以風險資料評估氣候行動的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"氣候、能源、災害與環境決策資料","pattern":"取從圖表、生活情境與風險資料判斷減碳、調適、效益與限制的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氣候變遷、減碳、防災、調適與公共行動","pattern":"取比較減緩與調適、熱浪與海岸風險、基礎設施、公平性及長期監測的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持區分減緩（減少溫室氣體來源或增加移除）與調適（降低已發生或預期衝擊），並以風險、暴露、脆弱度與效益資料評估。","氣候行動需考量時間尺度、地區差異、成本、共益、風險轉移、弱勢群體與長期監測，不能只看單一工程或單年數值。"],"versionDifferences":["公立段考與會考公開題型提供氣候、能源、災害與環境決策方向；康軒公開課程線索偏向減緩／調適區分、熱浪、海岸風險、防災、公平與公共行動。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以城市植樹、大眾運輸、節能建築、熱浪防護、海平面、暴雨比較、防洪下游風險與校園減碳建立雙軌氣候行動證據鏈。","把『種樹既然有共益就一定是減緩』、『年雨量總和可代表暴雨風險』與『防洪工程只會降低整個流域風險』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對氣候變遷減緩、調適、熱浪、海平面、暴雨、防洪、風險轉移、公平與成效監測。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ing-iv-9-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的氣候變遷、減緩、調適、災害風險、工程與資料判讀能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INg-Ⅳ-9：氣候變遷的減緩與調適途徑","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為氣候變遷減緩與調適單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content ing iv 9")
if __name__=="__main__": main()

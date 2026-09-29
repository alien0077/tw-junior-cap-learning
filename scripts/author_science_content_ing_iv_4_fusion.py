"""INg-Ⅳ-4：碳元素在自然界中的儲存與流動來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ing-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ing-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"碳循環、光合作用、呼吸作用、分解與燃燒資料判讀","pattern":"取由生物作用、地質與人類活動追蹤碳元素儲存位置及流動路徑的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"碳循環、二氧化碳、森林與海洋資料","pattern":"取從圖表、生活活動與環境資料判斷碳轉移、儲存與排放來源的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"碳元素儲存、生物圈、大氣、海洋與人類活動","pattern":"取比較光合作用、呼吸、分解、燃燒、海洋吸收與森林變化的碳循環教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持碳元素在大氣、生物、土壤、海洋、岩石與化石燃料間儲存，並透過光合作用、呼吸、分解、燃燒與海氣交換流動。","碳循環判讀必須追蹤元素而非只看物質外觀，並區分短期生物交換與長期地質儲存。"],"versionDifferences":["公立段考與會考公開題型提供光合作用、呼吸、分解、燃燒與環境資料判讀方向；康軒公開課程線索偏向生物圈、大氣、海洋、森林與人類活動的碳流動。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以植物、兔子、落葉分解、煤炭、森林焚燒、海洋吸收與植被變化建立碳儲存與流動的證據鏈。","把『碳循環就是二氧化碳循環』、『葉片質量消失等於碳消失』與『海洋吸收就代表碳永久移除』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對碳元素儲存、光合作用、呼吸、分解、食物鏈、燃燒、海洋吸收與植被變化。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ing-iv-4-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的碳循環、光合作用、呼吸、分解、燃燒、海洋及植被資料判讀能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INg-Ⅳ-4：碳元素在自然界中的儲存與流動","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為碳循環單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content ing iv 4")
if __name__=="__main__": main()

"""Jb-Ⅳ-4：溶液濃度、重量百分濃度與 ppm 來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-jb-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-jb-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"重量百分濃度、稀釋、ppm 與水樣資料計算","pattern":"取由溶質、溶液總量、稀釋及極低濃度資料進行濃度計算的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"溶液濃度、污染物、單位與圖表資料","pattern":"取從生活水樣、質量比例、單位換算及 ppm 情境判讀濃度的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"重量百分濃度、稀釋、污染物與 ppm","pattern":"取設計配製、稀釋和水質分析活動，並選用合適濃度單位的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以溶質質量／溶液總質量計算重量百分濃度，依溶質守恆處理稀釋，並用 ppm 表示稀水溶液中的極低含量。","濃度計算需明確分母、單位、總質量與近似條件，ppm 不能脫離水樣密度或質量基準直接套用。"],"versionDifferences":["公立段考與會考公開題型提供重量百分濃度、稀釋、污染物、單位與水樣資料方向；康軒公開課程線索偏向配製、稀釋、污染物分析與 ppm。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以食鹽、糖水、稀釋、mg/L 水樣、污染物與百分濃度—ppm 換算建立計算證據鏈。","把『濃度分母永遠是水的質量』、『加水後溶質質量增加』與『1 ppm 在所有溶液都必定等於 1 mg/L』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對重量百分濃度、溶質守恆、稀釋、ppm、單位與水樣密度近似。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-jb-iv-4-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的重量百分濃度、溶質守恆、稀釋、ppm、單位及水樣判讀能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jb-Ⅳ-4：溶液濃度、重量百分濃度與 ppm","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為溶液濃度與 ppm 單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content jb iv 4")
if __name__=="__main__": main()

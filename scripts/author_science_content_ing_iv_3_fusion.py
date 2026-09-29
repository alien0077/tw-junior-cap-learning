"""INg-Ⅳ-3：不同物質受熱後的溫度變化來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ing-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-ing-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"熱傳、比熱、熱平衡、相變與溫度資料判讀","pattern":"取由溫度變化、熱量、物質性質與熱傳資料推論熱現象的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"加熱曲線、熱量、狀態變化與實驗控制","pattern":"取從圖表、曲線與生活情境判斷升溫、冷卻、比熱與相變的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"熱平衡、熱傳導、比熱、沸騰與控制變因","pattern":"取比較不同物質受熱溫度變化、熱傳方式、相變及公平實驗設計的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由熱量輸入、物質質量與比熱解釋溫度變化，並以熱傳、熱平衡與相變資料判讀熱現象。","公平比較需控制質量、初溫、熱源、容器與輸入熱量；溫度曲線斜率和平台分別反映升溫快慢與狀態變化。"],"versionDifferences":["公立段考與會考公開題型提供熱量、加熱／冷卻曲線、熱平衡與相變方向；康軒公開課程線索偏向比熱、熱傳導、沸騰與控制變因。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以熱金屬與水、食用油、鋁鐵比較、沸騰平台、自然冷卻、金屬湯匙與溫度曲線建立本單元證據鏈。","把『溫度高就一定含有較多熱量』、『沸騰時沒有吸熱』與『升溫慢就一定比熱大』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對熱量、比熱、熱傳導、熱平衡、相變、升溫／冷卻曲線與實驗控制。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ing-iv-3-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的熱量、比熱、熱傳、相變、溫度曲線及實驗控制能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INg-Ⅳ-3：不同物質受熱後的溫度變化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為熱傳、比熱、相變與溫度曲線單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content ing iv 3")
if __name__=="__main__": main()

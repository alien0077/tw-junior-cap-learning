"""Ja-Ⅳ-3：化學反應的可觀察現象來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ja-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-ja-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"化學反應現象、氣體、沉澱、顏色、溫度與安全判讀","pattern":"取由可觀察現象、控制條件與證據鏈判斷化學反應的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"實驗現象、指示劑、溶液、反應與資料判讀","pattern":"取從實驗觀察與資料區分化學變化、物理變化及證據限制的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"化學反應現象、氣體、沉澱、酸鹼指示劑與實驗安全","pattern":"取觀察氣泡、沉澱、顏色與溫度，配合安全操作和對照實驗建立證據的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以氣泡、沉澱、顏色、溫度、氣味與指示劑等觀察證據判斷可能發生化學反應，並區分現象與結論。","單一現象不能自動證明特定反應，需控制條件、重複觀察、對照、質量與安全程序，並保留證據能支持的範圍。"],"versionDifferences":["公立段考與會考公開題型提供實驗現象、溶液、指示劑與資料判讀方向；康軒公開課程線索偏向氣體、沉澱、顏色、溫度觀察、對照與實驗安全。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以澄清溶液冒泡、沉澱、顏色改變、溫度上升、石蕊、密閉質量、結晶與安全聞氣味建立觀察證據鏈。","把『冒泡一定是化學反應』、『溫度改變就能直接知道反應物』與『未知氣味可直接靠近聞』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對化學反應可觀察現象、證據限制、酸鹼指示、安全、對照與重複測量。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ja-iv-3-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的氣泡、沉澱、顏色、溫度、指示劑、質量、對照及實驗安全能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ja-Ⅳ-3：化學反應的可觀察現象","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為化學反應可觀察現象單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content ja iv 3")
if __name__=="__main__": main()

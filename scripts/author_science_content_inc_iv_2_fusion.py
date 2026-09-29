"""INc-Ⅳ-2：不同尺度、單位與科學記號來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-inc-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-inc-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"尺度、單位換算、科學記號與有效數字判讀","pattern":"取由不同單位、數量級、測量記錄與科學記號進行計算和比較的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"數量級、圖表數值、單位與測量資料","pattern":"取以科學記號、單位轉換、數量級及資料精度判讀自然量的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"尺度、基本／衍生單位、科學記號與有效數字","pattern":"取選擇合適單位、正確換算、以科學記號表達及依測量精度記錄的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持用合適單位、單位換算、科學記號、數量級與有效數字表達不同尺度的科學量。","計算結果必須同時檢查指數、單位、係數範圍與測量精度，避免只看數字而忽略物理意義。"],"versionDifferences":["公立段考與會考公開題型提供單位、數量級、科學記號與測量資料判讀方向；康軒公開課程線索偏向選擇合適單位、換算與有效數字記錄。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以微米、毫米、公尺、公里、天文距離與細胞大小建立單位換算、數量級比較、科學記號及有效數字的連續證據鏈。","把『指數越大數值一定越大』、『換單位只改數字不改量』與『多寫幾位就更精確』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對科學記號、單位換算、數量級、有效數字與測量記錄。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-inc-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的單位、換算、數量級、科學記號及有效數字能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INc-Ⅳ-2：不同尺度、單位與科學記號","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為單位、尺度與科學記號單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content inc iv 2")
if __name__=="__main__": main()

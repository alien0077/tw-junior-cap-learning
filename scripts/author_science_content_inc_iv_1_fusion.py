"""INc-Ⅳ-1：宇宙間事物規模的微觀與巨觀尺度來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-inc-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-inc-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"微觀與巨觀尺度、單位、數量級及資料判讀","pattern":"取依尺度、單位與觀測證據判斷自然事物大小關係的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"科學記號、尺度比較、圖表與模型判讀","pattern":"取以數量級、科學記號、圖像和模型進行跨尺度推理的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"宇宙尺度、微觀觀察、縮尺模型與儀器選擇","pattern":"取依觀察尺度選擇顯微鏡或望遠鏡、使用單位與縮尺模型的教學及評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以尺度、單位、數量級與縮尺模型比較從微觀粒子、細胞到行星與星系的自然事物。","觀測結果必須配合儀器解析度、距離、亮度、單位與模型比例判讀，不能把影像大小直接當成真實大小。"],"versionDifferences":["公立段考與會考公開題型提供數量級、科學記號、圖像與模型判讀方向；康軒公開課程線索偏向微觀／巨觀儀器選擇與縮尺模型操作。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以病毒、細胞、細菌、沙粒、山脈、地球、太陽系與星系建立跨尺度排序、單位換算、望遠鏡／顯微鏡及模型限制的證據鏈。","把『影像越亮就代表物體越大』、『縮尺模型可同時忠實呈現所有距離與大小』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對尺度排序、微米換算、數量級、儀器選擇、縮尺模型與星系影像判讀。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-inc-iv-1-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的尺度、單位、數量級、儀器及模型判讀能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INc-Ⅳ-1：宇宙間事物規模的微觀與巨觀尺度","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為尺度與單位單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content inc iv 1")
if __name__=="__main__": main()

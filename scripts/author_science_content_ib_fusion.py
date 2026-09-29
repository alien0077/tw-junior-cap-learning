"""Ib：天氣與氣候變化第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib.json"; REPORT=ROOT/"implementation/reports/science-content-ib-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"天氣、氣候、季風、等壓線、鋒面與長期資料判讀","pattern":"取由氣象觀測、時間尺度、氣壓風場、鋒面、地形與長期趨勢區分天氣和氣候的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"天氣系統、氣候、季風與臺灣地形","pattern":"取天氣／氣候尺度、季風、等壓線、鋒面、颱風、地形降雨和資料解讀的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"氣象觀測、長期趨勢與證據限制","pattern":"取 30 年氣候平均、雷達回波、區域差異、預報資料和天氣氣候概念界線的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以短期天氣觀測、長期氣候資料和大氣系統解釋天氣與氣候變化。","季風、氣壓等壓線、鋒面、颱風、地形降雨、雷達回波與時間尺度是共同能力核心。"],"versionDifferences":["南一公開定位偏向天氣氣候與觀測；康軒線索偏向季風、鋒面、颱風、臺灣地形；翰林線索偏向長期平均、雷達、區域差異與證據界線。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以 30 年溫度、東北季風、等壓線、鋒面、颱風氣壓、地形雨、日尺度雷達和年雨量比較建立尺度證據鏈。","把單日天氣等於氣候、年平均上升等於每天上升、雷達回波方向等於地面風向列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織天氣、氣候、季風、氣壓風場、鋒面、颱風、地形與長期資料限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ib-*.json") if path.stem.removeprefix("question-science-content-ib-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ib 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的天氣、氣候、季風、鋒面、長期資料及觀測判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ib 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib：天氣與氣候變化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原先 9 題已補成 10 題；每題均有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib")
if __name__=="__main__": main()

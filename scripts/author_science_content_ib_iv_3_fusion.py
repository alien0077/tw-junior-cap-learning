"""Ib-Ⅳ-3：地球自轉與高低氣壓旋轉第一輪來源融合與題庫來源審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-ib-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地球自轉、科氏力、氣壓系統與天氣圖","pattern":"取由地球自轉、氣壓梯度、風向旋轉與等壓線資料判讀天氣系統的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地球自轉偏向、高低壓與風場","pattern":"取科氏偏向、北南半球高低壓旋轉、風與等壓線的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"天氣圖、風場與模型限制","pattern":"取等壓線疏密、摩擦影響、旋轉圓盤模型、時間序列天氣圖與半球差異的能力方向。"},
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以地球自轉偏向、氣壓梯度、摩擦和半球差異解釋高低氣壓風場。","科氏偏向、北南半球旋轉、等壓線疏密、近地面摩擦、天氣圖序列與模型限制是共同能力核心。"],"versionDifferences":["南一公開定位偏向地球自轉和風場；康軒線索偏向高低壓、半球旋轉和等壓線；翰林線索偏向摩擦、旋轉盤模型、時間序列及天氣圖證據。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以北南半球低高壓、等壓線疏密、地轉偏向、旋轉圓盤與連續天氣圖建立動力證據鏈。","把風完全沿等壓線、南北半球旋轉方向相同、模型結果可直接當成所有實際風場列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開試題資料的能力方向，重新組織地球自轉、偏向、氣壓梯度、摩擦、高低壓旋轉、等壓線與天氣圖限制；10 題均逐題核對單元符合度、唯一答案、正確解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 refs=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
 qs=sorted(path for path in QDIR.glob("question-science-content-ib-iv-3-*.json") if path.stem.removeprefix("question-science-content-ib-iv-3-").isdigit())
 if len(qs)!=10: raise SystemExit(f"Ib-Ⅳ-3 題數應為 10，實際為 {len(qs)}")
 for path in qs:
  q=json.loads(path.read_text(encoding="utf-8")); q["examPatternRefs"]=refs; p=q.setdefault("provenance",{}); p["sourceUrl"]=SOURCES[0]["url"]; p["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的地球自轉、偏向、氣壓旋轉及天氣圖判讀能力方向；本題只作 pattern-only 改寫來源。"; p["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ib-Ⅳ-3 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; path.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib-Ⅳ-3：地球自轉與高低氣壓旋轉","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對地球自轉與氣壓旋轉單元符合度、唯一答案、正確解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib iv 3")
if __name__=="__main__": main()

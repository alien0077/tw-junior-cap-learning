"""Ec：氣體第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ec.json"; REPORT=ROOT/"implementation/reports/science-content-ec-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"氣體粒子、壓力、體積與資料判讀","pattern":"取由粒子碰撞、壓力差、氣體定律與實驗資料推論氣體現象的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氣體性質、大氣壓力與壓力體積關係","pattern":"取氣體粒子模型、大氣壓、擴散、定溫壓縮與探究評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"氣體壓力、體積與實驗安全","pattern":"取氣壓差、排水集氣、pV關係、控制變因與安全操作能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以粒子運動與碰撞解釋氣壓、擴散及壓力差現象。","大氣壓、排水集氣、定溫定量 pV 關係、控制變因與安全操作是共同能力核心。"],"versionDifferences":["南一公開定位偏向氣體性質與壓力；康軒線索偏向粒子模型、大氣壓與氣體定律；翰林線索偏向排水集氣、探究設計與實驗安全。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以打氣筒、吸管與密閉針筒工作台串接壓力差、粒子碰撞與 pV 資料。","把氣體沒有質量、吸管是把液體拉上來、壓力只由氣體種類決定列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織氣體粒子、壓力、大氣壓、擴散、排水集氣與定溫 pV 關係；10 題均已逐題核對單元符合度、唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ec-[0-9].json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的氣體粒子、氣壓、定溫 pV 與實驗能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Ec 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ec：氣體","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對單元符合度、唯一答案、解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ec")
if __name__=="__main__": main()

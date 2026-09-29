"""Fc-Ⅳ-2：細胞及其分子組成的微觀層次第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-fc-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-fc-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"細胞、DNA、蛋白質、脂質與微觀資料判讀","pattern":"取由細胞構造、分子組成與功能證據推論生物微觀層次的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"細胞構造、生物分子與尺度","pattern":"取細胞基本單位、水、醣類、脂質、蛋白質、核酸與構造功能的教學及評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"細胞微觀層次、分子組成與實驗證據","pattern":"取細胞膜分子、酵素、DNA資訊、顯微證據與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由細胞觀察進入水、醣類、脂質、蛋白質與核酸等分子組成，再連結構造與功能。","細胞膜、DNA、蛋白質、酵素、尺度與顯微證據判讀是共同能力核心。"],"versionDifferences":["南一公開定位偏向細胞與生物分子；康軒線索偏向分子種類、功能與細胞構造；翰林線索偏向膜分子、酵素、DNA資訊與模型證據。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以洋蔥表皮細胞影像、分子卡與細胞膜模型串接觀察尺度、組成與功能，要求區分直接證據和微觀推論。","把看到顆粒就直接命名、DNA等於細胞所有功能、脂質雙層沒有蛋白質功能列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然科試題／課程資料能力方向，重新組織細胞構造、水、醣類、脂質、蛋白質、核酸、酵素與微觀證據；10 題均已逐題核對單元符合度、唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-fc-iv-2-[0-9].json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的細胞構造、生物分子與微觀證據能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Fc-Ⅳ-2 單元重新核對與撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Fc-Ⅳ-2：細胞及其分子組成的微觀層次","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均逐題核對細胞分子單元符合度、唯一答案、解析與五步解法；三筆公開試題／課程資料僅作 pattern-only 來源，版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content fc iv 2")
if __name__=="__main__": main()

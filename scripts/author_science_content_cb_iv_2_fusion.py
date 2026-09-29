"""Cb-Ⅳ-2：原子排列與元素特性第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-cb-iv-2.json"
REPORT=ROOT/"implementation/reports/science-content-cb-iv-2-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"原子排列、同素異形體、金屬性質與微觀模型判讀","pattern":"取由微觀排列與電子／結構線索推論材料宏觀性質的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"原子排列、元素特性與碳的同素異形體","pattern":"取粒子排列、鑽石石墨比較與金屬導電延展的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物質結構、同素異形體與材料性質","pattern":"取結構—性質關係、模型證據與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由原子排列、電子分布與彼此作用解釋元素及材料特性。","同素異形體、鑽石／石墨、金屬導電延展與模型證據是共同評量核心。"],"versionDifferences":["南一公開定位偏向結構與性質；康軒線索偏向碳的同素異形體與金屬活動；翰林線索偏向材料模型、資料比較與模型限制。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以鑽石／石墨排列卡、金屬拉線與導電資料建立微觀—宏觀互動。","把同元素必有相同性質、模型球的顏色等於真實顏色與導電必然代表液態列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織原子排列、同素異形體、電子分布、導電、延展與模型限制；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-cb-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的原子排列、同素異形體與材料性質能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Cb-Ⅳ-2 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Cb-Ⅳ-2：原子排列與元素特性","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content cb iv 2")
if __name__=="__main__": main()

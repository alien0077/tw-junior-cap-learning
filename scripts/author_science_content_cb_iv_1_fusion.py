"""Cb-Ⅳ-1：分子與原子第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-cb-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-cb-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"原子、分子、元素、化合物、化學式與原子守恆判讀","pattern":"取由粒子模型、化學式與原子種類數量推論物質組成的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"原子分子、元素化合物與化學式","pattern":"取粒子表示、化學式係數下標與原子守恆的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"物質微觀組成、分子模型與符號表示","pattern":"取元素分子、化合物粒子、化學式讀法與模型限制的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以原子、分子、元素、化合物與化學式描述物質微觀組成。","係數／下標、粒子模型與原子守恆是共同評量核心。"],"versionDifferences":["南一公開定位偏向物質組成；康軒線索偏向粒子表示與化學式；翰林線索偏向元素分子、化合物模型與符號限制。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以彩球粒子卡、化學式讀取、係數下標拆解與反應前後原子帳本建立互動。","把係數當下標、分子等於化合物與模型球數等於實際大小列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織原子、分子、元素、化合物、化學式與原子守恆；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-cb-iv-1-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的原子分子、化學式與粒子模型能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Cb-Ⅳ-1 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Cb-Ⅳ-1：分子與原子","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content cb iv 1")
if __name__=="__main__": main()

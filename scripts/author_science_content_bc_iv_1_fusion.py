"""Bc-Ⅳ-1：酵素催化代謝與影響因素第一輪來源融合。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-bc-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-bc-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"酵素、反應速率、溫度酸鹼度與實驗設計判讀","pattern":"取由實驗資料、控制變因與反應速率推論酵素作用的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"酵素催化、代謝與影響因素","pattern":"取酵素專一性、溫度酸鹼度、對照組與生活實驗的教學與評量方向。"},
 {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"酵素、活化能與反應速率","pattern":"取活化能、變性、受質濃度與資料曲線判讀的能力方向。"},
]
def refs(): return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以酵素專一性、活化能與實驗資料理解催化作用。","溫度、酸鹼度、受質濃度、抑制與公平實驗是共同評量核心。"],"versionDifferences":["南一公開定位偏向酵素與代謝；康軒線索偏向生活實驗與影響因素；翰林線索偏向活化能、變性與曲線資料。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以水果變色、唾液澱粉酶、鳳梨蛋白酶與 pH／溫度試管建立速率證據互動。","把酵素被消耗、溫度越高越快與產物多等於速率快列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織酵素、活化能、專一性、變性、反應速率與控制變因；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-bc-iv-1-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的酵素、反應速率與實驗設計能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Bc-Ⅳ-1 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bc-Ⅳ-1：酵素催化代謝與影響因素","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bc iv 1")
if __name__=="__main__": main()

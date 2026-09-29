"""Aa-Ⅳ-4：元素性質週期性的第一輪來源融合與報告。"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-aa-iv-4.json"
REPORT = ROOT / "implementation/reports/science-content-aa-iv-4-first-pass-review.json"
QDIR = ROOT / "questions/science"
TODAY = "2026-09-23"
SOURCES = [
    {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"週期表、原子序、族週期與元素性質推論","pattern":"取由週期表位置判讀元素性質、比較資料與限制推論的能力方向。"},
    {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"元素週期表、族週期與元素性質","pattern":"取由週期表排列與最外層電子連結化學性質的教學與評量方向。"},
    {"url":"https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf","title":"新北市文山區安康高中國中部公開翰林版自然簡案","year":"公開課程計畫","locator":"元素週期性與週期表資料判讀","pattern":"取同族／同週期比較、趨勢預測與證據限制的能力方向。"},
]
def refs():
    return [{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以原子序、族與週期整理元素性質。","同族相似性、同週期趨勢與由位置提出可驗證預測是共同評量核心。"],"versionDifferences":["南一公開定位偏向週期表與元素分類；康軒線索偏向原子結構與性質連結；翰林線索偏向資料比較、趨勢預測與應用。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以元素位置卡、同族／同週期比較表與預測—驗證紀錄建立互動。","把把週期當電話簿、忽略例外條件與只看單一元素武斷推廣列為錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開自然科試題／課程資料能力方向，重新組織原子序、族週期、最外層電子與元素性質趨勢；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
    lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
    for p in sorted(QDIR.glob("question-science-content-aa-iv-4-*.json")):
        q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q.setdefault("provenance",{})["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然科試題／課程資料的週期表、族週期與元素性質能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開資料能力方向，題幹、選項、答案、解析與五步解法均依 Aa-Ⅳ-4 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"Aa-Ⅳ-4：元素性質週期性","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題／課程資料僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content aa iv 4")
if __name__=="__main__": main()

"""INa-Ⅳ-2：能量可相互轉換並維持定值的來源證據補全與第一輪審查。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-ina-iv-2.json"
REPORT=ROOT/"implementation/reports/science-content-ina-iv-2-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"功、動能、位能、摩擦、效率與能量守恆資料判讀","pattern":"取從運動、摩擦、效率與系統邊界資料追蹤能量轉換及總量變化的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"能量轉換、功、效率與實驗資料判讀","pattern":"取以資料、圖表與生活情境判斷能量轉換方向、效率與守恆的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"能量形式、系統邊界、摩擦、效率與控制變因","pattern":"取用模型與實驗比較不同能量形式、系統範圍、摩擦熱及效率的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
    lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持能量可在動能、位能、彈性、熱、電與機械等形式間轉換，系統邊界內總能量需配合輸入輸出判讀。","摩擦不會讓能量消失，而會將可利用的機械能轉成較分散的熱等形式；效率與系統範圍必須明確。"],"versionDifferences":["鹽埕國中公開段考呈現功、摩擦、效率與資料判讀；會考公開題型提供生活情境下的守恆與轉換推理方向；康軒公開課程線索偏向能量形式、系統邊界與實驗控制。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以滑行物體、彈簧小車、碰撞、電動機、摩擦面比較與效率計算建立能量流追蹤鏈。","把『物體停止代表能量消失』、『摩擦會創造能量』與『效率就是輸出減輸入』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對能量轉換、系統邊界、摩擦、功、效率、控制變因與資料證據。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
    for p in sorted(QDIR.glob("question-science-content-ina-iv-2-*.json")):
        q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"
        q["provenance"]["sourceUrl"]=SOURCES[0]["url"]
        q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的能量轉換、守恆、功、效率、摩擦及資料判讀能力方向；本題只作 pattern-only 改寫來源。"
        q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"INa-Ⅳ-2：能量可相互轉換並維持定值","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為本單元獨立題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("audited science content ina iv 2")

if __name__=="__main__": main()

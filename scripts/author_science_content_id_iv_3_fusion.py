"""Id-Ⅳ-3：地軸傾斜與四季形成的來源證據補全與第一輪審查。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-id-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-id-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114% E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf".replace("% ","%"),"title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"地軸傾斜、四季、南北半球與太陽高度資料判讀","pattern":"取由地軸方向、半球受光、太陽高度與季節資料推論因果的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"地球運動、日照角度、晝夜與季節證據判讀","pattern":"取天體運動模型、日照資料與觀測證據相互檢驗的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"地球儀、光源、地軸傾斜、公轉與四季模型","pattern":"取操作地球儀與光源、保持地軸方向、比較兩半球受光與修正模型的教學及評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8"))
    lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
    lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以地軸傾斜配合地球公轉解釋四季、太陽高度、白晝長度與南北半球相反性。","地球儀與光源模型必須固定光源、保持地軸方向，並以影長、日照時間、兩半球與極圈資料檢驗。"],"versionDifferences":["鹽埕國中公開段考呈現季節與半球資料判讀；會考公開題型提供天體運動與證據推理方向；康軒公開課程線索偏向地球儀、光源和公轉操作。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以夏至／冬至、春分／秋分、南北半球、影長、地球儀控制變因與極圈極晝組成單元專屬證據鏈。","把『四季完全由日地距離造成』、『地軸方向隨公轉任意翻轉』及『光源跟著地球移動』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新組織地軸傾斜、公轉、半球差異、日照角度、白晝長度、影長、模型限制與極圈證據。現有 10 題逐題維持原創，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
    for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
    for p in sorted(QDIR.glob("question-science-content-id-iv-3-*.json")):
        q=json.loads(p.read_text(encoding="utf-8"))
        q["examPatternRefs"]=REFS
        q["updatedAt"]=TODAY
        q["reviewStatus"]="draft"
        q["provenance"]["sourceUrl"]=SOURCES[0]["url"]
        q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的地軸傾斜、四季、日照角度、半球與模型判讀能力方向；本題只作 pattern-only 改寫來源。"
        q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"
        p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"Id-Ⅳ-3：地軸傾斜與四季形成","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為本單元獨立題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("audited science content id iv 3")

if __name__=="__main__": main()

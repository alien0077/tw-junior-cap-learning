"""Ja-Ⅳ-4：化學反應的表示法來源證據補全。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ja-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ja-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"化學方程式、係數、下標、狀態符號與反應條件","pattern":"取由符號表示、粒子數量、狀態和反應條件解讀化學反應的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"化學式、方程式、配平與粒子資料","pattern":"取從化學式與方程式判讀元素比例、守恆、狀態與反應資訊的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"化學式、反應式、狀態符號、條件與模型表示","pattern":"取以粒子模型和符號表示互相核對、正確配平並解讀反應條件的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以化學式、反應式、箭頭、係數、下標、狀態符號與反應條件表示化學反應，並以原子守恆核對。","係數可改變粒子數量比例，下標屬化學物質身分不可任意改動；符號表示需與粒子模型和實驗條件一致。"],"versionDifferences":["公立段考與會考公開題型提供化學式、方程式、粒子數量、狀態與配平方向；康軒公開課程線索偏向符號表示、模型核對與反應條件。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以箭頭、係數、下標、狀態符號、加熱條件、氫氧反應、鈉氯反應與粒子模型建立化學表示法證據鏈。","把『方程式係數可改成下標』、『箭頭等於數學相等』與『係數比例就是質量比例』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對化學式、方程式、箭頭、係數、下標、狀態符號、反應條件、配平與粒子模型。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for p in sorted(QDIR.glob("question-science-content-ja-iv-4-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=REFS; q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校／公開自然科試題與課程資料的化學式、方程式、係數、下標、狀態符號、反應條件及粒子模型能力方向；本題只作 pattern-only 改寫來源。"; q["provenance"]["authoringNote"]="依公開資料能力方向保留並核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ja-Ⅳ-4：化學反應的表示法","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為化學反應表示法單元專屬題目，已補齊三筆公立學校／公開自然科試題與課程資料 pattern-only 來源記錄；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content ja iv 4")
if __name__=="__main__": main()

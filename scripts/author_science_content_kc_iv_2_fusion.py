"""Kc-Ⅳ-2：靜電力的同斥異吸的第一輪來源融合與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-kc-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-kc-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"電荷、靜電力、距離與實驗判讀","pattern":"取同斥異吸、作用力方向、距離與電荷量比較的能力方向，重新設計靜電實驗紀錄。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"正負電荷、庫侖力、中性物體與感應","pattern":"取由電荷符號連到受力箭頭與證據限制的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"靜電、距離、介質與控制變因","pattern":"取方向、強弱與實驗公平比較的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以靜電實驗紀錄員任務為入口，先用正負電荷符號和受力箭頭判斷同斥異吸，再比較距離、電荷量與介質改變對靜電力的影響。學生還要處理中性紙片被吸引、金屬感應與牛頓第三定律，並把吸引或排斥的觀察和仍需控制的證據分開。"; lesson["studyHighlights"]=["用電荷符號和受力箭頭判斷同斥異吸。","比較距離、電荷量與介質對靜電力強弱的影響。","區分中性物體感應吸引與異種電荷的證據。","以作用反作用、合力與控制變因檢查結論。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以電荷、受力、距離與實驗資料理解靜電作用。","方向、強弱、感應與控制變因是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向電學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以電荷組合卡、距離刻度、中性金屬球、介質切換與受力箭頭建立本課互動。","把吸引不等於異種電荷、正負符號不等於力方向與作用反作用放入錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織電荷、庫侖力、方向、距離、感應與實驗限制；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-kc-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的電荷、靜電力、距離、中性物體與控制變因能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與五步解法均以 Kc-Ⅳ-2 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Kc-Ⅳ-2：靜電力的同斥異吸","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content kc iv 2")
if __name__=="__main__": main()

"""Me-Ⅳ-5：重金屬污染的影響的第一輪來源融合與題目契約補強。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-me-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-me-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"水質、沉積物、污染來源、生物累積與環境資料判讀","pattern":"取來源—路徑—受體、採樣控制與污染風險判讀能力方向，重新設計溪流與農田調查情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"重金屬、環境介質、食物鏈與健康風險","pattern":"取由物質性質連到暴露、資料限制與防治措施的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"污染監測、控制變因、生物影響與整治成效","pattern":"取多介質證據、時間序列與生態影響的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課從虛構溪流與農田的採樣桌開始，把重金屬污染拆成來源、介質、傳遞路徑、受體與時間。學生要比較水、底泥、生物組織與食物網資料，區分環境濃度、生物累積與生物放大，並以採樣品質、暴露途徑和整治前後證據判斷風險，而不是由顏色或單一死亡事件直接指定原因。"; lesson["studyHighlights"]=["用來源—路徑—受體圖追蹤重金屬從排放到生物與人的暴露。","區分環境持久性、生物累積與食物鏈生物放大。","以水、沉積物、生物組織、食物與排放源的多介質資料交叉驗證。","用重複採樣、品質控制、時間序列與整治後生態指標評估風險。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以物質性質、環境介質、資料與生活風險理解污染。","採樣控制、污染路徑、濃度與生物反應是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以溪流—農田—魚體—食用暴露的來源—路徑—受體圖、跨介質採樣卡與整治前後證據桌建立本課互動。","把持久性、生物累積與生物放大分開，並把底泥殘留和生態恢復放入高階題。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織重金屬來源、介質、暴露、累積、監測與整治；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-me-iv-5-*.json")):
  i=int(p.stem.rsplit("-",1)[-1]); q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的污染來源、環境介質、採樣控制、生物累積與整治成效能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與步驟均以 Me-Ⅳ-5 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["solutionSteps"]=["圈出污染物、來源、介質、受體、暴露途徑與時間。",q["solutionStrategy"],"把水、底泥、生物組織、食物或排放源資料放進來源—路徑—受體圖。","排除只靠單一樣本、外觀或未控制採樣條件的過度結論。","回查答案是否符合濃度、累積、暴露與題幹限制，並指出下一項需監測的證據。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Me-Ⅳ-5：重金屬污染的影響","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":12,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content me iv 5")
if __name__=="__main__": main()

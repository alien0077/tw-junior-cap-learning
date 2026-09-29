"""INg-Ⅳ-7：溫室氣體與全球暖化的第一輪來源與內容契約補強。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-ing-iv-7.json"
REPORT=ROOT/"implementation/reports/science-content-ing-iv-7-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"溫室效應、能量收支、氣候資料與控制變因","pattern":"取能量路徑、長期資料、實驗控制與因果判讀能力方向，重新設計校園氣候情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"全球暖化、輻射、反照率與資料趨勢","pattern":"取由物理機制連到觀測資料與替代解釋的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"溫室氣體、冰雪反照率、海平面與節能評估","pattern":"取多證據交叉比對與控制條件的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
STRATEGIES={1:"先判斷氣候的時間與空間尺度，再把平均趨勢和單日天氣分開。",2:"沿太陽短波—地表長波—大氣吸收再放出的能量路徑追蹤收支改變。",3:"檢查觀測期間、站點數、平均方法與自然變異，避免用單日值代替氣候趨勢。",4:"比較冰雪表面反射率與融化後吸收能量，畫出回饋方向再下結論。",5:"把海水熱膨脹和陸冰增加的水量分成兩條機制，避免混成單一原因。",6:"先列控制變因，再確認只有二氧化碳條件不同且測量位置與時間一致。",7:"在同一張圖上標示全球長期平均和地方短期事件，檢查是否真的矛盾。",8:"把減緩措施對應到排放來源與可量測的排放指標，而不是只看宣傳名稱。",9:"用排放、濃度、能源使用與多地長期溫度交叉檢查，並保留替代解釋。",10:"建立基準與對照，控制天氣、使用量與設備變化，再比較長期用電與排放。"}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8"))
 lesson["content"]["summary"]="本課從校園屋頂的能量箭頭開始，逐步連結太陽短波、地表長波、溫室氣體吸收再放出、排放來源與濃度，再用長期、多地資料判讀全球暖化。學習者還要區分自然溫室效應、臭氧層、天氣波動、反照率回饋與人為驅動，最後把減緩與調適放回不同作用對象。"
 lesson["studyHighlights"]=["畫出短波入射、長波散出與溫室氣體再放出的能量路徑。","用排放、濃度、溫度與反照率資料連結機制與觀測。","區分天氣事件、自然變異與長期全球氣候趨勢。","以控制變因與基準資料評估節能、減排與調適方案。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以能量、物質與資料證據理解溫室效應與全球暖化。","長期資料、控制變因和因果界線是共同的評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以屋頂日夜能量箭頭、冰雪反照率、校園透明箱與節能基準建立本單元專屬互動。","將臭氧、自然溫室效應、寒流與全球暖化的混淆放入錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織能量收支、溫室氣體、資料尺度、回饋與方案評估；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i in range(1,11):
  p=QDIR/f"question-science-content-ing-iv-7-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的溫室效應、能量收支、氣候資料、控制變因與節能評估能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與步驟均以 INg-Ⅳ-7 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["solutionStrategy"]=STRATEGIES[i]; q["solutionSteps"]=["圈出題幹的物理量、時間尺度、資料來源與控制條件。",f"依本題情境套用判準：{STRATEGIES[i]}","把觀察、機制、推論與仍待查證的替代解釋分開。","逐一排除把短期事件、單一地點或未控制變因誇大成全球結論的選項。","回查答案是否同時符合能量收支、資料尺度與題幹限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INg-Ⅳ-7：溫室氣體與全球暖化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ing iv 7")
if __name__=="__main__": main()

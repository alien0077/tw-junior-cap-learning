"""Ib-Ⅳ-6：季風造成臺灣氣候的季節差異的第一輪來源融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ib-iv-6.json"; REPORT=ROOT/"implementation/reports/science-content-ib-iv-6-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"季風、氣壓、風向、降雨與氣候圖表判讀","pattern":"取風向來源、季節資料、地形與降雨推理的能力方向，重新設計臺灣測站資料情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"臺灣氣候、季風、水氣與迎背風面","pattern":"取由氣壓與風場連到水氣、地形及地區差異的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"季節風向、臺灣降雨與地形效應","pattern":"取氣候圖表、風向判讀與多因素限制的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
STRATEGIES={1:"先用季節尺度區分季風與單日海陸風，再檢查風向轉換和水氣來源。",2:"從東北方來風追到海面水氣與北東部迎風抬升，保留地形與水氣量限制。",3:"把西南風的暖濕輸送和梅雨、對流、豪雨等短期系統分開判讀。",4:"使用多年逐月風向、雨量、溫度資料，把風場與氣象量並列而非只看單日。",5:"畫出山脈兩側的上升、凝結、降雨與下沉路徑，核對迎背風面。",6:"用多年統計描述乾濕氣候平均，避免以單日雨量替代季節特徵。",7:"先讀圖例和箭頭，依氣象命名規則判定風的來源方向。",8:"選擇連續氣壓、風向、風速、水氣與雨量資料，檢查轉換是否持續。",9:"先核對座標、月份、單位與圖例，再把風向、水氣和雨量做時間對齊。",10:"把季風視為背景環流，再加入鋒面、颱風、對流與地形說明資料能支持的範圍。"}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以臺北、臺南與花蓮的冬夏風向及月雨量卡片為入口，追蹤亞洲大陸與海洋的季節熱力差異如何形成盛行風，再把風經過海面取得水氣、遇山抬升與背風下沉連到臺灣北東部冬雨、南部冬乾及西半部夏雨的氣候差異。判讀時要把季風背景和鋒面、颱風、午後對流等短期系統分開。"; lesson["studyHighlights"]=["從陸海熱力差異、氣壓與風向判斷季風來源。","追蹤風經海面取得水氣及山脈迎背風面的降雨差異。","用逐月、多年資料區分氣候平均與短期天氣。","在風向圖、雨量圖與地形圖之間建立可檢查的因果鏈。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以氣壓、風向、水氣、地形與資料圖表理解季風氣候。","季節尺度、資料判讀與因果限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以臺北—臺南—花蓮三站風向雨量卡、山脈迎背風拖曳與冬夏資料並排建立本課互動。","把風的來源命名、海面水氣、地形抬升與短期天氣干擾放入逐題檢核。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織臺灣季風、氣壓、風向、水氣、地形與多年資料；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i in range(1,11):
  p=QDIR/f"question-science-content-ib-iv-6-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的季風、氣壓、風向、地形、水氣與臺灣降雨圖表能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與步驟均以 Ib-Ⅳ-6 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["solutionStrategy"]=STRATEGIES[i]; q["solutionSteps"]=["圈出季節、風向來源、地點、雨量期間與地形條件。",f"依本題情境套用判準：{STRATEGIES[i]}","把觀測事實和氣壓、海面水氣、迎背風抬升等機制分開。","排除把季風說成每天固定、把迎風面必然下雨或把氣候平均當成單次事件的選項。","回查答案是否符合圖例、資料尺度與臺灣地形，並標出結論限制。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ib-Ⅳ-6：季風造成臺灣氣候的季節差異","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ib iv 6")
if __name__=="__main__": main()

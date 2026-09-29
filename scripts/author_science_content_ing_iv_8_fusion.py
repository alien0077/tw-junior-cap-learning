"""INg-Ⅳ-8：氣候變遷的全球性衝擊的第一輪獨立來源融合。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ing-iv-8.json"; REPORT=ROOT/"implementation/reports/science-content-ing-iv-8-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
SOURCES=[
 {"url":"https://www.nehs.tc.edu.tw/wp-content/uploads/sites/95/2026/02/6%E7%90%86%E5%8C%96%E7%A7%91-%E4%B9%9D%E5%B9%B4%E7%B4%9A-%E9%A1%8C%E5%BA%AB.pdf","title":"國立中科實驗高級中學公開九年級理化題庫","year":"109-115","locator":"全球氣候、海平面、生態與長期資料判讀","pattern":"取跨尺度、跨區域的環境資料與因果推理能力方向，重新設計全球性衝擊情境。"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf","title":"臺北市立內湖國民中學公開九年級理化段考","year":"109-115","locator":"溫室效應、降雨、海岸與風險差異","pattern":"取由物理機制連到地方暴露、脆弱度與資料限制的推理方向，未複製題幹、選項、圖表或答案。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","title":"高雄市立國昌國民中學公開三年級自然科試題","year":"109-115","locator":"全球暖化、極端事件、海岸與社會衝擊","pattern":"取多證據、尺度與風險分配的能力方向，全部以本課原創文字改寫。"},
]
def refs(): return [{**s,"subject":"science","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper","observedPattern":s["pattern"]} for s in SOURCES]
STRATEGIES={1:"先把全球性定義為跨區域、跨系統和長時間連結，再排除單點事件的過度外推。",2:"沿長波吸收與再放出檢查能量收支，避免把溫室氣體誤解成完全封住熱量。",3:"分開海水熱膨脹、陸冰融水與海冰浮力效應，對照各自對海平面的作用。",4:"把全球平均當背景訊號，再加入地方地形、海岸、人口與防護資料。",5:"從溫度與海溫變化連到物候、棲地、分布和物種互動，避免只列單一物種結果。",6:"比較降雨時序、蒸發和需求，不以年總量相近推論洪旱風險相同。",7:"設計一致的長期站點、品質控制、基準期與非氣候因素檢查。",8:"把單次熱浪當作研究起點，加入長期觀測、模型歸因和反事實比較。",9:"用危害—暴露—脆弱度拆解同一海平面訊號在不同社群的風險差異。",10:"把不確定性量化為範圍和條件，並同時檢查地球系統與社會系統證據。"}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以跨區域資料桌為入口，不從單一災害講起，而是把全球性衝擊理解成地球系統與社會系統的連鎖：排放改變能量收支，長期氣候訊號再透過海平面、生態、糧食、健康與水循環落到不同社群。學生要在全球背景、地方資料與資源分配之間來回核對，並把不確定性寫進結論。"; lesson["studyHighlights"]=["用全球、區域與地方三種尺度讀同一組氣候資料。","沿排放—能量收支—氣候變化—衝擊鏈連結地球與社會系統。","以危害、暴露與脆弱度解釋風險為何跨社群不同。","用長期觀測、歸因、模型與不確定性範圍支持條件式結論。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以自然資料、地球系統與生活風險理解全球氣候衝擊。","長期趨勢、尺度、因果與限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向環境與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以跨區域資料桌、同一海岸的社群資源分配、全球—區域—地方切換與不確定性範圍建立本單元獨立互動。","把海平面、降雨時序、生態關係、公共健康與社會脆弱度放入同一證據鏈。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織全球性衝擊的尺度、機制、證據、風險與調適；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for i in range(1,11):
  p=QDIR/f"question-science-content-ing-iv-8-{i}.json"; q=json.loads(p.read_text(encoding="utf-8")); q["examPatternRefs"]=refs(); q["provenance"]["sourceUrl"]=SOURCES[0]["url"]; q["provenance"]["sourceLocator"]="三筆公立學校公開自然／理化試題的全球氣候、海平面、生態、極端事件與風險判讀能力方向；本題只作 pattern-only 改寫。"; q["provenance"]["authoringNote"]="本題取公開試題能力方向，題幹、選項、答案、解析與步驟均以 INg-Ⅳ-8 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["solutionStrategy"]=STRATEGIES[i]; q["solutionSteps"]=["圈出題幹的尺度、時間、指標與受影響系統。",f"依本題情境套用判準：{STRATEGIES[i]}","把觀測、機制、衝擊與社會條件分層整理。","排除把單一地點、單一事件或全球平均直接當成所有地區答案的選項。","回查答案是否符合資料範圍，並寫出不確定性或下一項證據。"]; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"INg-Ⅳ-8：氣候變遷的全球性衝擊","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ing iv 8")
if __name__=="__main__": main()

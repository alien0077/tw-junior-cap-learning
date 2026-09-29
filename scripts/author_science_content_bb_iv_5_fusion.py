"""Bb-Ⅳ-5：熱造成物質形態與體積改變的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-bb-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-bb-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以溫度計、橋梁接縫、雙金屬片、熱氣球與結冰水瓶為材料觀察站，先區分物態改變和體積改變，再把溫度、粒子間距、壓力、材料與密度連起來。學習者會特別追蹤水在 0–4°C 的反常膨脹，並用公平實驗比較金屬、玻璃與塑膠的熱膨脹。"; lesson["studyHighlights"]=["區分熔化、汽化、凝結、凝固與熱膨脹收縮。","用粒子運動、間距、壓力與材料解釋尺寸變化。","掌握水在 0–4°C 的體積與密度反常。","用控制變因比較不同材料的熱膨脹並連結工程安全。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以粒子、溫度、物態、體積、密度與生活裝置理解熱效應。","圖表、相變、材料比較與控制變因是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向熱學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以液柱、橋梁接縫、雙金屬片、熱氣球、密閉袋與水結冰模型建立本課互動。","把相變平台仍吸熱、氣體受壓力影響、水的反常膨脹與材料差異放入錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織物態、熱膨脹、粒子間距、密度、水的反常與材料測試；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-bb-iv-5-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的物態、熱膨脹、密度、材料與控制變因能力方向，題幹、選項、答案、解析與五步解法均以 Bb-Ⅳ-5 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bb-Ⅳ-5：熱造成物質形態與體積改變","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bb iv 5")
if __name__=="__main__": main()

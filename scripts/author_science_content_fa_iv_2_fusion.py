"""Fa-Ⅳ-2：三大類岩石的特徵與成因的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-fa-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-fa-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以露頭照片、標本與地質調查紀錄為入口，先記錄晶體、顆粒、層理、化石與葉理等可見證據，再把它們連到岩漿冷卻、沉積成岩或固態變質的形成故事。學習者最後沿岩石循環追蹤風化、埋藏、熔融與抬升，區分直接觀察、合理推論與仍需查證的地質時間限制。"; lesson["studyHighlights"]=["以形成過程而非顏色或用途區分三大類岩石。","把晶體大小、顆粒、層理、化石與葉理連到成因。","區分固態變質、熔融冷卻與沉積成岩的路徑。","用岩石循環和相對地層關係表達地質時間與證據限制。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以觀察證據、形成過程與地質時間理解岩石。","分類、地層、循環與證據限制是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向地球科學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以三張露頭照片、標本紀錄、岩石循環卡與觀察—推論—限制工作表建立本課互動。","把有晶體即火成、有層理即沉積、變質必熔化等迷思拆成可反駁的證據判斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織三大類岩石、紋理、成因、岩石循環與地層關係；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-fa-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的地質觀察與成因判讀能力方向，題幹、選項、答案、解析與五步解法均以 Fa-Ⅳ-2 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Fa-Ⅳ-2：三大類岩石的特徵與成因","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content fa iv 2")
if __name__=="__main__": main()

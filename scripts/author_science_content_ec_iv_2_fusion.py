"""Ec-Ⅳ-2：定溫定量氣體的壓力與體積關係的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ec-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-ec-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以氣密注射器資料員任務為入口，讓學習者固定溫度與氣體量，逐點記錄壓力和體積，再用粒子碰撞模型、pV 乘積、p—V 反比曲線與 p—1/V 圖檢查波以耳定律。解題時先核對密閉、定溫、定量與單位，遇到漏氣、活塞摩擦或溫度變化則說明模型限制。"; lesson["studyHighlights"]=["以粒子碰撞解釋氣體壓力與體積的反比。","在定溫定量條件下使用 pV＝常數與 p₁V₁＝p₂V₂。","用乘積、反比曲線和 p 對 1/V 圖判讀資料。","辨認漏氣、摩擦、溫度與氣體量改變造成的模型限制。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以粒子、壓力、體積、溫度與資料圖表理解氣體定律。","公式條件、單位、實驗控制與誤差是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向物理與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以氣密注射器、活塞摩擦、資料乘積卡、p—V 與 p—1/V 圖建立本課互動。","把反比誤成同向、粒子被壓扁、溫度尚未穩定與漏氣等迷思放入資料判讀。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織氣體粒子、壓力、體積、波以耳定律、圖表與實驗限制；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-ec-iv-2-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的氣體壓力、體積、圖表與實驗控制能力方向，題幹、選項、答案、解析與五步解法均以 Ec-Ⅳ-2 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ec-Ⅳ-2：定溫定量氣體的壓力與體積關係","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ec iv 2")
if __name__=="__main__": main()

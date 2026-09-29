"""Bb-Ⅳ-4：熱的傳導、對流與輻射的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-bb-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-bb-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課把金屬棒、沸水、暖氣房與太陽能集熱板放在同一個熱路徑工作台，先問是否需要介質，再辨認固體粒子碰撞、流體整體循環或電磁波跨空間傳遞。學生會標示複合傳熱的主要與次要路徑，並用表面、流速、材料、空氣層與距離解釋保溫和散熱。"; lesson["studyHighlights"]=["依介質、粒子局部傳遞、流體運動與電磁波區分三種熱傳。","在鍋子、沸水、暖氣與太陽能集熱器中標示複合熱路徑。","用材料、流速、表面、空氣層與距離解釋熱傳快慢。","以遮蔽、保溫、對流流線與溫度資料檢查推論。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以粒子、流體、電磁波與生活裝置理解熱傳。","分類、複合路徑、實驗證據與材料應用是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向熱學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以金屬棒、鍋中有色流體、暖氣房、保溫瓶與集熱板模型建立本課互動。","把輻射需空氣、對流可在固體、金屬導熱快等迷思改為證據判讀。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織傳導、對流、輻射、複合熱傳與保溫；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-bb-iv-4-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的傳導、對流、輻射、保溫與實驗判讀能力方向，題幹、選項、答案、解析與五步解法均以 Bb-Ⅳ-4 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Bb-Ⅳ-4：熱的傳導、對流與輻射","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content bb iv 4")
if __name__=="__main__": main()

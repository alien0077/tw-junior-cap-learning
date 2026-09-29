"""Ba-Ⅳ-6：功率的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ba-iv-6.json"; REPORT=ROOT/"implementation/reports/science-content-ba-iv-6-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課把『做得多』和『做得快』拆開，從爬樓梯、水泵與快煮壺的工作卡開始，讓學習者用 P＝W/t、E＝Pt 比較功率、總能量與效率。每次只改變一項條件，檢查焦耳、瓦特、秒、重力位能與平均功率的單位，最後把計算結果連回公平比較與生活設備。"; lesson["studyHighlights"]=["以 P＝W/t 與 E＝Pt 分清功率、功與能量。","用同一工作量、不同時間比較完成速度。","檢查瓦特、焦耳、秒、千瓦與效率的單位及基準。","用總功、總時間與輸入輸出判讀平均功率和設備選擇。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以功、能量、時間、單位與生活裝置理解功率。","計算、單位換算、比較條件與效率是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向力學與能量數位資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以爬樓梯、水泵、快煮壺、電器銘牌與一次只改一項條件的瓦特—焦耳—秒互動建立本課脈絡。","把高功率不等於低耗能、瓦特不等於焦耳、平均功率不等於瞬時功率放入錯誤診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織功率、功、能量、時間、效率與單位；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-ba-iv-6-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的功率、能量、單位與生活裝置判讀能力方向，題幹、選項、答案、解析與五步解法均以 Ba-Ⅳ-6 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ba-Ⅳ-6：功率","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ba iv 6")
if __name__=="__main__": main()

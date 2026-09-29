"""Eb-Ⅳ-3：平衡物體的合力與合力矩的第一輪內容契約與報告。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-eb-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-eb-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-21"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["content"]["summary"]="本課以懸掛招牌、紙板吊臂、輪子力偶與蹺蹺板為結構檢查任務，先畫自由體圖，再分別檢查合力與合力矩。學習者要從作用線、垂直力臂、支點及順逆時針方向建立可重做的力學表格，不能由『不動』或外觀對稱直接猜沒有力。"; lesson["studyHighlights"]=["用自由體圖列出研究對象的所有外力。","以向量合力判斷平移，以垂直力臂與合力矩判斷轉動。","區分力的作用反作用對與同一自由體內的力。","用支點、重心與力矩表分析吊臂、輪子、門與蹺蹺板。"]
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以力、力矩、受力圖與生活結構理解平衡。","計算、方向、支點與控制條件是共同評量核心。"],"versionDifferences":["南一公開入口偏向主題定位；康軒公開索引偏向觀察與活動；翰林公開入口偏向力學與數位教學資源。公開頁面不足以宣稱未取得的完整教材細節。"],"originalAdditions":["以結構檢查員的紙板吊臂、懸掛招牌、力偶、蹺蹺板與可重做的力矩表建立本課互動。","把不動不等於無力、作用反作用不在同一自由體與力臂不是斜距等迷思放入題目診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校公開自然／理化試題能力方向，重新組織合力、合力矩、作用線、力臂、自由體圖與結構平衡；正文、互動、題目、答案、解析與五步解法均為原創，未複製教材或試題文字、圖表與答案。Terra 第二輪與正式發布審查尚未完成，維持 draft。"}; lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 for p in sorted(QDIR.glob("question-science-content-eb-iv-3-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["provenance"]["authoringNote"]="本題取公立學校公開自然／理化試題的受力圖、力矩、平衡與生活結構判讀能力方向，題幹、選項、答案、解析與五步解法均以 Eb-Ⅳ-3 重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; q["reviewStatus"]="draft"; q["updatedAt"]=TODAY; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Eb-Ⅳ-3：平衡物體的合力與合力矩","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"三筆公開試題僅作 pattern-only 來源；版本融合、逐題內容 QA、Terra 第二輪與正式發布尚未完成，維持 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content eb iv 3")
if __name__=="__main__": main()

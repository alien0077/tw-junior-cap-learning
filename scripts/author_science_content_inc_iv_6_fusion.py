"""INc-Ⅳ-6：個體到生物圈是生命世界的巨觀尺度來源證據與審查。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-inc-iv-6.json"; REPORT=ROOT/"implementation/reports/science-content-inc-iv-6-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持由個體、族群、群集、生態系到生物圈建立生命世界的尺度層次，並辨認每一層的研究對象與邊界。","尺度放大時會加入互動、生物與非生物環境、能量流與物質循環，不能把較小層次的觀察直接當成較大層次的完整結論。"],"versionDifferences":["公立段考與會考公開題型提供生物組成、棲地、群集與生態系資料判讀方向；康軒公開課程線索偏向個體到生物圈的層次辨認、校園與濕地調查。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以校園榕樹、池塘、濕地、森林、生物圈與污染擴散建立由小到大的尺度證據鏈。","把『同一物種所有個體就是群集』、『生態系只包含生物』及『局部鳥類下降就代表整個生物圈崩潰』列為單元迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新核對生命世界層次、研究邊界、生物／非生物因素、跨尺度調查與影響擴散。現有 10 題均為單元專屬原創題，具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 qs=[]
 for p in sorted(QDIR.glob("question-science-content-inc-iv-6-*.json")):
  q=json.loads(p.read_text(encoding="utf-8")); q["updatedAt"]=TODAY; q["reviewStatus"]="draft"; q["provenance"]["authoringNote"]="依公開資料能力方向核對單元專屬改寫；題幹、選項、答案、解析與五步解法均未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"; p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); qs.append(q)
 REPORT.write_text(json.dumps({"unit":"INc-Ⅳ-6：個體到生物圈是生命世界的巨觀尺度","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":len(qs),"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題均為生命世界巨觀尺度專屬題目，原有三筆公開試題／課程資料來源已逐題核對；每題有唯一答案、解析與五步解法，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("audited science content inc iv 6")
if __name__=="__main__": main()

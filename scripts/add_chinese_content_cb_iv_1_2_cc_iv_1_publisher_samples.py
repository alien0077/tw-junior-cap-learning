#!/usr/bin/env python3
"""Record public-school evidence for Chinese Cb-IV-1/2 and Cc-IV-1."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
URLS={"nani":"https://course.cyc.edu.tw/upfile/course112/file_school/15391708959992156.pdf","kanghsuan":"https://www.yfms.tyc.edu.tw/uploads/1632969569049hbdSdsTC.pdf","hanlin":"https://w.pnjh.tyc.edu.tw/wwwdata/academic/plan/111/5-1-1-1.pdf"}
LICENSE="只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材正文、題目、答案或版面。"
SAMPLES=[
{"lessonId":"lesson-chinese-content-cb-iv-1","title":"Cb-Ⅳ-1：親屬道德儀式典章制度","core":["親屬、道德、儀式、制度需分層判讀","文本價值要放回時代與社群脈絡","古今比較須保留證據與差異"],"diff":["南一重視文化線索分類與討論","康軒突出角色規範、行動後果與古今比較","翰林強調資料蒐集、文化報告與反思"],"obs":[["nani","以親屬、倫理、儀式、典章制度連結篇章理解、討論與多元評量","文化分類卡；制度與人物行動對照","實作、習作、口頭、紙筆"],["kanghsuan","以古文、語錄、寓言和文化文本分析道德、家庭、儀式與制度","角色／規範／後果表；古今制度比較","實作、口頭、自評、習作"],["hanlin","以家庭、社群、禮俗與文化制度連結詩文、資料蒐集與報告","親屬／社群關係圖；文化報告","討論、資料蒐集、報告、學習單"]]},
{"lessonId":"lesson-chinese-content-cb-iv-2","title":"Cb-Ⅳ-2：個人家庭鄉里國族社群關係","core":["先判斷個人、家庭、鄉里、國族與社群尺度","群體敘述需保留個人差異與文本視角","觀點比較要有證據並尊重不同立場"],"diff":["南一重視關係尺度與多元文化","康軒以角色行動、群體張力與提問為入口","翰林延伸到資料整理、報告與分享"],"obs":[["nani","以個人、家庭、鄉里、國族及社群建立不同尺度閱讀","關係尺度圖；多元觀點討論","實作、習作、口頭、紙筆"],["kanghsuan","以樂府、現代文本與社會材料分析個人和群體關係","階層圖；角色觀點比較","朗讀、實作、口頭、習作"],["hanlin","以家庭、鄉里、國族與社群文化安排資料整理與主題報告","社群關係網；觀點雙欄表","資料蒐集、報告、學習單"]]},
{"lessonId":"lesson-chinese-content-cc-iv-1","title":"Cc-Ⅳ-1：藝術信仰思想文化","core":["藝術形式、信仰實踐與思想觀點要分層互證","文化理解需避免把自身價值直接套入他者","評量需包含形式、脈絡、比較與反思"],"diff":["南一連結藝術、信仰、思想與歷史社群脈絡","康軒強調形式賞析、文化比較與複眼閱讀","翰林延伸到資料整理、主題探索與作品分享"],"obs":[["nani","以藝術、信仰與思想文化連結文體、歷史、社群與報告","文化分類；主題報告","實作、口頭、資料蒐集、報告"],["kanghsuan","以古典詩文、非韻文和文化材料進行形式賞析與比較","形式—思想—文化表；賞析短文","實作、口頭、自評、習作"],["hanlin","以詩文、生活文化與藝術思想安排資料整理和主題探索","作品觀察卡；文化時間線","資料蒐集、實作、報告、學習單"]]}]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8"));existing={x.get("lessonId") for x in d["units"]};added=[]
 for s in SAMPLES:
  records=[]
  for pub,concepts,reps,assessment in s["obs"]:
   records.append({"publisher":pub,"sourceUrl":URLS[pub],"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"公立校方課程計畫；{concepts}；核讀 2026-09-20。","accessedAt":"2026-09-20","observedConcepts":concepts.split("；"),"observedRepresentations":reps.split("；"),"observedAssessment":assessment.split("、"),"licenseBoundary":LICENSE})
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":records,"fusionReview":{"commonCore":s["core"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"逐單元融合、內容／版權審查與 Terra 複核前維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str)and "unit samples"in x["reason"]:x["reason"]=re.sub(r"Four hundred thirty-eight unit samples","Four hundred forty-one unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()

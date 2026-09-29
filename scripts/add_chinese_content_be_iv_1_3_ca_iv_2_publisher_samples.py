#!/usr/bin/env python3
"""Record public-school evidence for Chinese Be-IV-1/3 and Ca-IV-2."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
URLS={"nani":"https://course.cyc.edu.tw/upfile/course109/sub1/14492227285956996.pdf","kanghsuan":"https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/20file/file/196_69_511%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%9C%8B%E6%96%87.pdf","hanlin":"https://tea.japs.tp.edu.tw/~japsteagif/doc/doc_110-1/plan_110-1_3th.pdf"}
LICENSE="只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材正文、題目、答案或版面。"
SAMPLES=[
{"lessonId":"lesson-chinese-content-be-iv-1","title":"Be-Ⅳ-1：自傳簡報新聞稿等生活應用","core":["生活應用文本要先判斷讀者、目的、格式與資訊需求","自傳、簡報、新聞稿的語域與結構不同","成品需以讀者可用性與資料正確性檢核"],"diff":["南一重視生活文本格式與實用溝通","康軒突出成果分享、生活任務與口頭表達","翰林以自我展現、團體任務與溝通能力遷移"],"obs":[["nani","以自傳、簡報、新聞稿等格式處理生活溝通與資訊組織","讀者／目的／格式表；成品檢核","實作、口頭、習作、紙筆"],["kanghsuan","以科技資訊和生活主題安排簡報、新聞與作品分享","簡報結構卡；新聞訊息層次","口頭、實作、分享、學習單"],["hanlin","以自我展現、團體任務和溝通技巧支援生活應用寫作","任務角色表；作品發表","實作、口語、作品、同儕回饋"]]},
{"lessonId":"lesson-chinese-content-be-iv-3","title":"Be-Ⅳ-3：簡報讀書報告演講稿劇本等學習應用","core":["學習應用文本需配合研究問題、讀者與發表情境","簡報、讀書報告、演講稿、劇本的結構與口語功能不同","評量需檢查資料來源、組織、表達與回應問題"],"diff":["南一強調共讀、簡報報告與Q&A","康軒連結文本學習、作品演出與分享","翰林突出讀書報告、團體任務和領導溝通"],"obs":[["nani","以共讀、簡報、讀書報告、演講稿與劇本安排閱讀成果","書籍重點卡；簡報與Q&A","小組討論、口頭分享、報告"],["kanghsuan","以文本、舞台劇與資訊整理進行學習應用輸出","文本—觀點—表演腳本表；成果分享","口頭、實作、作品、紙筆"],["hanlin","以讀書報告、簡報與團體任務培養領導、溝通與發表","任務分工表；報告簡報","團體任務、簡報、口頭、學習紀錄"]]},
{"lessonId":"lesson-chinese-content-ca-iv-2","title":"Ca-Ⅳ-2：科技文明演進與生存環境文化","core":["科技文本需同時看發展歷程、生活影響與環境代價","文明進步不是單一路線，要比較不同群體與時間尺度","結論需有文本資料、環境脈絡與永續限制"],"diff":["南一把科技文明放進文本議題與環境閱讀","康軒連結科技資訊、社會責任與生活問題","翰林突出資料整理、環境議題與主題報告"],"obs":[["nani","以科技、環境與社會文本理解文明演進及生存環境文化","時間線；科技影響利弊表","討論、學習單、報告、紙筆"],["kanghsuan","以科技資訊和公共議題進行檢索、統整、解釋與省思","科技—社會—環境因果圖；演講","實作、口頭、自評、習作"],["hanlin","以科技文明、環境與文化資料安排主題探索和視覺化報告","資料來源表；圖文專題","資料蒐集、實作、報告、紙筆"]]}]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8"));existing={x.get("lessonId") for x in d["units"]};added=[]
 for s in SAMPLES:
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":[{"publisher":p,"sourceUrl":URLS[p],"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":f"公立校方課程計畫；{c}；核讀 2026-09-21。","accessedAt":"2026-09-21","observedConcepts":c.split("；"),"observedRepresentations":r.split("；"),"observedAssessment":a.split("、"),"licenseBoundary":LICENSE}for p,c,r,a in s["obs"]],"fusionReview":{"commonCore":s["core"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"逐單元融合、內容／版權審查與 Terra 複核前維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-21";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str)and "unit samples"in x["reason"]:x["reason"]=re.sub(r"Four hundred forty-one unit samples","Four hundred forty-four unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()

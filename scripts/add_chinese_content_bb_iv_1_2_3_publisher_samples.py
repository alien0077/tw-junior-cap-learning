#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Bb-IV-1/2/3."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; REPORT=ROOT/"implementation/reports/publisher-chapter-evidence-samples.json"
NANI="https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/9file/file/124_1_5111%E5%9C%8B%E8%AA%9E%E6%96%87.pdf"
KANG="https://course.tn.edu.tw/course/114J%E9%87%91%E5%9F%8E%E5%9C%8B%E4%B8%ADC5-1%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%28%E8%AA%BF%E6%95%B4%29%E8%A8%88%E7%95%AB%E6%99%AE%E9%80%9A%E7%8F%AD%E5%85%AB%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%870718155545.pdf"
HANLIN="https://hakka.mtjh.kh.edu.tw/113plan/5/c2.pdf"
LICENSE="只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"
def S(p,u,l,c,r,a):return(p,u,l,c,r,a)
SAMPLES=[
 {"lessonId":"lesson-chinese-content-bb-iv-1","title":"Bb-Ⅳ-1：自我與人際交流感受","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以小詩、現代散文和文言文本連結自我感受、人際交流、生活經驗與自我反思，安排口語、習作與自我檢核；核讀 2026-09-20。",["感受需由文本語句、情境與人物互動具體化","自我感受和人際觀點要區分並能互相理解","反思要回到文本與生活證據"],["感受詞與文本細節配對","人物／關係觀點卡","生活經驗反思短文"],["口語","習作","自我檢核","紙筆"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；把自我、人際、生活與價值思辨放入現代文本及議題學習，採實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["交流感受要兼顧說話者和他人立場","文本感受可轉成價值判斷與問題解決","多元評量要檢查理解、表達與反思"],["角色立場比較","情境對話與回饋","價值思辨學習單"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"高雄市公立國中翰林版課程計畫；以現代散文、人物與家庭／社群文本處理自我及人際感受，透過學習單、口語表達和主題寫作完成遷移；核讀 2026-09-20。",["人物情感要連結關係情境與文化脈絡","口語分享需尊重不同經驗與觀點","主題寫作能呈現感受如何轉成具體表達"],["人物關係圖","情緒／觀點證據表","主題寫作與分享"],["學習單","口語表達","主題寫作"]),
 ],"common":["感受題不能只找情緒詞，要整合情境、關係、語氣與文本細節","自我與他人觀點可不同，但解釋必須有文本或生活證據","遷移活動要讓學生把理解轉成對話、反思或寫作"],"diff":["南一偏向文本細節、生活連結與自我檢核","康軒將感受放入價值思辨、情境溝通和問題解決","翰林突出人物／家庭關係、主題寫作與口語分享"]},
 {"lessonId":"lesson-chinese-content-bb-iv-2","title":"Bb-Ⅳ-2：社會群體家國民族情感","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；將社會群體、家國民族情感連結多元文化、家庭倫理、社群關係及文本反思，安排討論、習作和紙筆評量；核讀 2026-09-20。",["群體情感要分辨個人經驗、社群認同與公共價值","家國民族文本需注意歷史文化脈絡與多元觀點","結論要避免把單一角色感受當成所有人的立場"],["群體關係網","文本觀點與文化脈絡對照","多元觀點討論／短文"],["課堂討論","習作","紙筆","自我評量"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；以社會群體與家國民族情感連結環境、文化、能源與公共議題，採實作、口頭、自評、習作和紙筆檢核；核讀 2026-09-20。",["群體認同需和公共議題、責任及生活選擇連結","文化差異要以文本證據理解而非貼標籤","討論與寫作要呈現理由、回應與價值取捨"],["群體／公共議題資料卡","觀點—證據—回應表","價值思辨與報告"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"高雄市公立國中翰林版課程計畫；在家庭、鄉里、國族及社會文本中討論群體情感和文化內涵，以學習單、口語表達、主題寫作與課堂分享評量；核讀 2026-09-20。",["群體情感可從人物關係延伸到社會文化","不同群體觀點要並列比較再形成自己的判斷","寫作需交代情感來源與公共意義"],["家庭／社群／國族層次圖","文化觀點比較","主題寫作與發表"],["學習單","口語表達","主題寫作","分享"]),
 ],"common":["先區分個人、家庭、社群、國族等尺度，再判斷情感與價值主張","群體情感分析要保留不同觀點，不以單一敘述代表整體","公共議題表達需同時提出文本證據、理由和對他者的回應"],"diff":["南一較重視多元文化、家庭社群和文本反思","康軒把群體情感接到環境、公共議題與價值取捨","翰林由人物關係延伸到文化層次、主題寫作與發表"]},
 {"lessonId":"lesson-chinese-content-bb-iv-3","title":"Bb-Ⅳ-3：物自然生命感悟","sources":[
  S("nani",NANI,"桃園市公立國中課程計畫；以自然、生命與環境文本引導觀察、感悟、倫理思考及生活連結，安排討論、自評、習作和紙筆評量；核讀 2026-09-20。",["自然描寫不只呈現景物，也承載生命觀與倫理問題","感悟要由具體意象、事件和語氣推導","生活連結需區分文本觀點與個人延伸"],["自然意象與感受卡","環境／生命倫理問題表","觀察札記與反思"],["討論","自我評量","習作","紙筆"]),
  S("kanghsuan",KANG,"臺南市公立國中康軒版八年級課程計畫；把自然與生命感悟結合環境美學、動物互動、能源及生活價值思辨，採實作、口頭、自評、習作和紙筆評量；核讀 2026-09-20。",["自然文本需同時讀景物、生命互動和作者態度","感悟能轉成環境倫理與生活決策的理由","活動要讓觀察、解釋與行動建議彼此銜接"],["自然觀察紀錄","人與環境互動圖","倫理討論與行動提案"],["實作","口頭","自我評量","習作／紙筆"]),
  S("hanlin",HANLIN,"高雄市公立國中翰林版課程計畫；以自然景物、生命經驗與文本情感連結家庭社群和主題寫作，透過學習單、口語表達與作品分享評量；核讀 2026-09-20。",["自然與生命感悟要連結敘事者或人物的經驗","景物細節可支撐情感和價值轉折","主題寫作要交代觀察證據與個人反思"],["景物—情感—價值鏈","生命經驗對照表","主題寫作與口頭分享"],["學習單","口語表達","主題寫作","分享"]),
 ],"common":["感悟不是任意抒情，必須由自然／生命細節、語氣和情境推導","先區分文本明示觀點與自己的延伸，再談倫理或生活應用","評量要包含觀察證據、價值思辨和可說明的反思"],"diff":["南一強調自然文本、觀察和生命倫理的反思","康軒將感悟延伸到環境美學、能源與行動提案","翰林較突出景物、人物經驗、主題寫作和分享"]},
]
def main():
 d=json.loads(REPORT.read_text(encoding="utf-8")); existing={x.get("lessonId") for x in d["units"]}; added=[]
 for s in SAMPLES:
  rec={"lessonId":s["lessonId"],"title":s["title"],"evidenceStatus":"chapter-level-recorded-pending-fusion-review","sources":[{"publisher":p,"sourceUrl":u,"sourceKind":"public-school-course-plan-identifying-publisher-material","locator":l,"accessedAt":"2026-09-20","observedConcepts":c,"observedRepresentations":r,"observedAssessment":a,"licenseBoundary":LICENSE} for p,u,l,c,r,a in s["sources"]],"fusionReview":{"commonCore":s["common"],"differencesToReview":s["diff"],"originalSynthesisBoundary":"本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
  if rec["lessonId"] not in existing:d["units"].append(rec);added.append(rec["lessonId"])
 d["unitCount"]=len(d["units"]);d["updatedAt"]="2026-09-20";REPORT.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 bp=ROOT/"implementation/reports/blockers.json";b=json.loads(bp.read_text(encoding="utf-8"))
 for x in b.get("blockers",[]):
  if isinstance(x.get("reason"),str) and "unit samples" in x["reason"]:x["reason"]=re.sub(r"Four hundred twenty-six unit samples","Four hundred twenty-nine unit samples",x["reason"])
 bp.write_text(json.dumps(b,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"unitCount":d["unitCount"],"added":added},ensure_ascii=False))
if __name__=="__main__":main()

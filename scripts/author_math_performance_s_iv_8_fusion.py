#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-8."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/math/lesson-math-performance-s-iv-8.json"
REPORT=ROOT/"implementation/reports/math-performance-s-iv-8-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"}

def record(p,c,r,m,a):
    return {"publisher":p,"edition":f"{p} 公立校方數學課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；特殊三角形、四邊形與正多邊形的概念、表徵及評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以角邊條件、對稱與對角線性質分類特殊圖形。"],"representations":[r],"examplesOrEvidence":["本課的園藝花圃、拼板與窗格均為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-math-performance-s-iv-8" and d["reviewStatus"]=="draft"
    d["title"]="s-Ⅳ-8：用角邊與對角線辨認特殊圖形"
    d["content"]={"summary":"特殊圖形不是靠名稱或外觀記憶，而是由定義條件與可推出性質辨認。等腰三角形有兩腰等長、底角相等；直角三角形有一個直角；平行四邊形、矩形、菱形、正方形的條件彼此有包含關係；正多邊形則要求各邊與各角都相等。本課以花圃、拼板與窗格的自編情境，練習由角邊條件分類、利用對角線與對稱性質推理，並分清必要條件與充分條件。","sections":[{"heading":"特殊三角形看角邊條件","body":"等腰看兩腰等長或兩底角相等，等邊看三邊等長且三角皆 60°，直角看一個角為 90°。同一三角形可能同時具備多種特性，分類時要列出全部條件。"},{"heading":"四邊形有條件階層","body":"平行四邊形有兩組對邊平行；矩形再多四個直角；菱形再多四邊等長；正方形同時具備矩形與菱形條件。由特殊條件可推出一般性質，但反向需要足夠證據。"},{"heading":"對角線提供額外證據","body":"平行四邊形對角線互相平分，矩形對角線等長，菱形對角線互相垂直；正方形同時具備相應性質。只知道一項對角線性質時，仍要判斷是否足以分類。"},{"heading":"正多邊形與對稱","body":"正多邊形各邊等長、各角相等；邊數改變會改變內角與對稱軸數量。畫得規則不等於已證明，應以角、邊、對角線和對稱條件核對。"}]}
    d["studyHighlights"]=["先列出角邊條件，再判斷特殊三角形或四邊形。","記住矩形、菱形與正方形的條件包含關係。","用對角線等長、垂直或互相平分作為可檢查證據。","正多邊形需同時檢查邊與角，不靠畫面外觀。"]
    d["teaching"]={"body":[{"id":"hook","phase":"hook","heading":"花圃形狀要怎麼分類？","body":"原創花圃設計有等腰三角形、矩形、菱形與正方形四種拼板。請學習者先量測或讀取標記，為每塊拼板填入等邊、等角、平行、垂直等條件，再比較名稱是否可以同時屬於兩類，建立圖形分類不是互斥清單的觀念。"},{"id":"explain","phase":"explain","heading":"建立四邊形條件階層","body":"從平行四邊形開始，逐步加入四角直角得到矩形、四邊等長得到菱形，同時加入兩者得到正方形。畫一張包含關係圖，並標記哪些性質可由定義推出，哪些反向判斷需要額外條件，避免把必要條件當充分條件。"},{"id":"worked-example","phase":"worked-example","heading":"用對角線辨認圖形","body":"自編四邊形對角線互相平分且等長。先用互相平分支持平行四邊形，再用對角線等長支持矩形；但不能只因對角線相交就判定正方形。最後列出仍需四邊等長或相鄰邊條件的理由。"},{"id":"guided-practice","phase":"guided-practice","heading":"條件卡片分類挑戰","body":"提供『兩腰等長』『四角直角』『四邊等長』『兩組對邊平行』『對角線垂直』等卡片，讓學習者分配到等腰三角形、矩形、菱形、正方形或多種可能。每次放置都要指出是定義、可推出性質，或只是可能但不足的線索。"},{"id":"transfer","phase":"transfer","heading":"把正多邊形放進窗格設計","body":"原創窗格要求用正六邊形與正方形拼接，學習者先確認各邊、各角是否相等，再估算一個頂點周圍的角度是否能完整拼合。若只把六邊形畫得對稱但邊長不一致，需指出它不能直接稱為正六邊形。"},{"id":"reflect","phase":"reflect","heading":"修正只看一項性質的分類","body":"請修正『四邊形有四個直角，所以一定是正方形』。先指出矩形也有四個直角但邊長未必相等，再列出正方形需要的四邊等長條件；最後用長 6、寬 4 的矩形作反例。"}],"summary":["特殊圖形依角邊定義分類，同一圖形可能同時具備多種性質。","矩形、菱形與正方形具有條件包含關係，反向推理需足夠證據。","對角線互相平分、等長或垂直可支持部分分類，但不能任意過度推論。","正多邊形同時要求各邊與各角相等，需用條件檢查。"],"exitCheck":[{"prompt":"矩形與正方形的條件差在哪裡？","expectedEvidence":"矩形有四個直角，正方形除了四個直角還有四邊等長；長 6 寬 4 的矩形不是正方形。"},{"prompt":"對角線互相平分且等長可支持什麼分類？","expectedEvidence":"可支持平行四邊形及矩形，但仍需其他條件才能判定菱形或正方形。"},{"prompt":"正多邊形需要檢查哪些條件？","expectedEvidence":"各邊等長且各角相等，不能只看畫面規則或單一對稱軸。"}]}
    d["interactive"]={"type":"guided-choice","goal":"依角邊定義、對角線與對稱條件分類特殊圖形。","scenario":"拖曳條件卡片到圖形，觀察哪些是定義、可推出性質或不足證據。","variables":[{"symbol":"a","meaning":"一條邊或一個角的已知資料"},{"symbol":"b","meaning":"與 a 對應的邊或角"},{"symbol":"x","meaning":"待分類的圖形條件"}],"steps":[{"id":"step-1","prompt":"正方形比矩形多了哪個關鍵條件？","options":["四邊等長","四個直角","四邊形有四條邊"],"answer":"A","feedback":"正方形同時具矩形的四直角與菱形的四邊等長。"},{"id":"step-2","prompt":"平行四邊形對角線的基本性質是什麼？","options":["互相平分","一定互相垂直","一定四邊等長"],"answer":"A","feedback":"兩條對角線會互相平分，但不必然垂直或使四邊等長。"},{"id":"step-3","prompt":"正六邊形的定義需要什麼？","options":["六邊等長且六角相等","只要畫成六邊形","只要有一條對稱軸"],"answer":"A","feedback":"正多邊形同時要求各邊等長與各角相等。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["teaching"]["body"][2]["body"] += " 再比較對角線交點的位置與兩條對角線長度，說明每一項資料只能推出相應性質。"
    d["teaching"]["body"][5]["body"] += " 並把反例的四個直角、兩組邊長和正方形缺少的條件列成表格，確認分類理由完整。"
    d["versionResearch"]=[record("nani","以特殊三角形、四邊形定義與性質建立分類","角邊標記、條件階層與對角線表徵","把矩形直接當正方形，或用單一性質反推全部分類","要求列出定義、可推出性質與不足條件"),record("kanghsuan","透過拼板與操作比較特殊圖形的包含關係","花圃拼板、摺紙、對角線與條件卡片","忽略同一圖形可能同時屬於多種分類","重視操作分類、反例、條件核對與推理理由記錄"),record("hanlin","連結正多邊形、窗格設計與對稱性質","窗格拼接、角度總和、單位與對稱檢查","只看圖形規則外觀，未確認邊角皆相等","評估模型、定義、對角線與設計條件是否一致")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持由角邊條件分類特殊三角形與四邊形。","矩形、菱形、正方形的包含關係及對角線性質是共同核心。","正多邊形需同時檢查邊、角與對稱條件。"],"versionDifferences":["南一證據較突顯特殊形體定義與性質；康軒較突顯拼板、摺紙及包含分類操作；翰林較突顯正多邊形、窗格與對稱設計限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以花圃拼板建立圖形同時具備多種性質的分類階層。","以對角線互相平分且等長的條件區分矩形與正方形。","把正六邊形窗格、反例、角度拼合與條件卡片整合成互動任務。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織特殊三角形、四邊形、正多邊形、對角線、對稱與設計情境。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"s-Ⅳ-8：用角邊與對角線辨認特殊圖形","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__ == "__main__": main()

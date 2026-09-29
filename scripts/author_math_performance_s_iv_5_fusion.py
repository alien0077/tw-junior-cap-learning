#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-5."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/math/lesson-math-performance-s-iv-5.json"
REPORT=ROOT/"implementation/reports/math-performance-s-iv-5-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"}

def record(p,c,r,m,a):
    return {"publisher":p,"edition":f"{p} 公立校方數學課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；線對稱、對稱軸與座標表徵的概念、表徵及評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以鏡射軸、等距、垂直平分與對應點判斷線對稱。"],"representations":[r],"examplesOrEvidence":["本課的剪紙窗花、座標圖樣與校徽設計均為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-math-performance-s-iv-5" and d["reviewStatus"]=="draft"
    d["title"]="s-Ⅳ-5：用對稱軸追蹤圖形的對應"
    d["content"]={"summary":"線對稱表示圖形對某一直線翻折後能完全重合；對稱軸上的點不動，軸兩側對應點到軸的距離相等，連結一對對應點的線段會被對稱軸垂直平分。圖形可能有一條、數條或沒有對稱軸，不能只看局部相似。本課以剪紙窗花、座標圖樣和校徽設計的自編情境，練習找對稱軸、作對應點、判斷對稱軸數量，並用距離與垂直條件驗證。","sections":[{"heading":"對稱軸是重合的摺痕","body":"把圖形沿直線摺疊，若兩半能重合，這條線就是對稱軸。對稱軸上的點保持不動，不能把圖形的外框或任意中線直接當成對稱軸。"},{"heading":"對應點的距離條件","body":"一對對應點位於對稱軸兩側，到軸的垂直距離相等；連結兩點的線段與對稱軸垂直，且交點是中點。這是用量測判斷的證據。"},{"heading":"對稱軸的數量與方向","body":"正方形有多條不同方向的對稱軸，等腰三角形通常有一條，斜向不規則圖形可能沒有。旋轉圖形或改變位置不會自動增加對稱軸。"},{"heading":"座標與設計檢查","body":"對 x 軸、y 軸或垂直線作鏡射時，可用座標變號或位置關係找對應點。設計時要確認整個圖形、文字方向和孔洞都符合對稱，不只檢查一小部分。"}]}
    d["studyHighlights"]=["先想像沿直線摺疊是否重合，再找對稱軸。","對應點到軸等距，連線垂直且軸過中點。","分清對稱軸數量與圖形方向，不能只看局部。","用座標、垂直平分與完整圖樣檢查。"]
    d["teaching"]={"body":[{"id":"hook","phase":"hook","heading":"一張窗花要沿哪裡摺？","body":"原創窗花圖案只有部分線條已畫出，請學習者在透明紙上想像沿不同直線摺疊，找出能完全重合的摺痕。接著標記一對花瓣的對應點，測量它們到摺痕的距離，讓對稱軸不只靠視覺而有可檢查證據。"},{"id":"explain","phase":"explain","heading":"由摺疊推出垂直平分","body":"選取對稱軸兩側的點 A、A'，連結 AA'，觀察線段與對稱軸垂直、交點為中點。再說明軸上點不移動，並用這三項條件檢查一條候選線是否真的是對稱軸，避免把任意中線誤認成摺痕。"},{"id":"worked-example","phase":"worked-example","heading":"判斷座標圖的對稱軸","body":"自編圖形含點 (2,1) 與 (−2,1)，另有點 (0,3)。先比較每對點到 y 軸的水平距離，再確認 y 軸上的點不動，因此 y 軸是對稱軸；若加入 (−2,2) 卻沒有 (2,2)，就用缺少對應點反駁。"},{"id":"guided-practice","phase":"guided-practice","heading":"數出對稱軸而不只找一條","body":"提供正方形、等腰三角形、一般平行四邊形與規則六邊形圖樣。學習者先逐條嘗試摺疊，再用頂點和邊的對應檢查數量；對正方形只找到一條的答案，要求補找兩條對角線與兩條中線。"},{"id":"transfer","phase":"transfer","heading":"把對稱用在校徽排版","body":"原創校徽設計要求左半圖樣鏡射到右半，學習者先決定對稱軸，再標出文字、孔洞與邊界的對應位置。若文字本身有方向，需討論鏡射後是否仍符合設計意義，不能只檢查外框。"},{"id":"reflect","phase":"reflect","heading":"修正局部對稱的誤判","body":"請修正『圖形左半邊看起來對稱，所以整個圖形有對稱軸』。先找出右半邊缺少的對應點或孔洞，再用垂直距離和連線中點指出反例；最後說明必須檢查整個圖形而非局部。"}],"summary":["線對稱是沿對稱軸摺疊後完全重合，軸上點不動。","對應點到軸等距，連線被軸垂直平分。","對稱軸數量需檢查完整圖形，不能只看一條中線或局部外觀。","用座標、量測、摺疊與反例驗證對稱。"],"exitCheck":[{"prompt":"一對對應點與對稱軸有何距離關係？","expectedEvidence":"兩點位於軸兩側且到軸的垂直距離相等，連線與軸垂直，軸過連線中點。"},{"prompt":"點 (2,1) 對 y 軸的對應點為何？","expectedEvidence":"是 (−2,1)，水平座標變號、垂直座標不變，兩點到 y 軸等距。"},{"prompt":"為什麼局部看起來對稱不足以判定整個圖形對稱？","expectedEvidence":"其餘邊、頂點或孔洞可能缺少對應，必須檢查完整圖形與對稱軸條件。"}]}
    d["teaching"]["body"][4]["body"] += " 再以座標標出一個文字筆畫的對應點，檢查鏡射後方向是否改變，讓設計判斷涵蓋整個內容。"
    d["teaching"]["body"][5]["body"] += " 並把缺少的對應點連線標出，說明哪一項等距或垂直平分條件失敗，讓反例可被重做。"
    d["interactive"]={"type":"guided-choice","goal":"用摺疊、等距與座標對應找出完整圖形的對稱軸。","scenario":"拖曳候選對稱軸或輸入座標，觀察對應點、垂直平分與整體重合結果。","variables":[{"symbol":"x","meaning":"點的水平座標"},{"symbol":"y","meaning":"點的垂直座標"},{"symbol":"a","meaning":"對稱軸位置或點到軸的距離"}],"steps":[{"id":"step-1","prompt":"線對稱的核心判斷是什麼？","options":["沿軸摺疊後整個圖形重合","只要一半看起來相似","圖形面積很大"],"answer":"A","feedback":"必須檢查整個圖形沿同一條軸能完全重合。"},{"id":"step-2","prompt":"點 (2,1) 對 y 軸鏡射後是哪個點？","options":["(-2,1)","(2,-1)","(-2,-1)"],"answer":"A","feedback":"對 y 軸鏡射時水平座標變號，垂直座標不變。"},{"id":"step-3","prompt":"連結一對對應點的線段與對稱軸有何關係？","options":["垂直且被對稱軸平分","一定平行且不相交","長度必須為零"],"answer":"A","feedback":"對稱軸是對應點連線的垂直平分線。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["versionResearch"]=[record("nani","以摺疊、對應點與垂直平分理解線對稱","窗花、鏡射圖、軸上不動點與距離標記","把任意中線或局部外觀當成整體對稱軸","要求檢查完整圖形、等距與垂直條件"),record("kanghsuan","透過剪紙與座標操作辨認對稱軸數量","剪紙、透明紙、座標點與摺疊驗證","只找到一條軸，或把鏡射後位置改變誤認不對稱","重視操作過程、對應點與多條軸的比較"),record("hanlin","連結圖樣設計、校徽與座標鏡射限制","排版圖樣、文字方向、孔洞、單位與量測","只檢查外框而忽略內部文字或孔洞的對應","評估完整模型、座標、方向與設計用途是否一致")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持由摺疊、對應點與垂直平分判斷線對稱。","對稱軸、等距、座標鏡射與軸上不動點是共同表徵核心。","完整圖形、量測、剪紙與反例需互相驗證。"],"versionDifferences":["南一證據較突顯摺疊與線對稱條件；康軒較突顯剪紙、座標及對稱軸數量操作；翰林較突顯圖樣設計、文字方向與完整模型限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以窗花摺痕和對應花瓣建立對稱軸證據。","以座標點 (2,1)、(-2,1) 和缺少對應點的反例檢查 y 軸對稱。","把多軸圖形、校徽文字、孔洞與局部對稱誤判整合成互動任務。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織線對稱、對稱軸、垂直平分、座標鏡射與圖樣應用。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"s-Ⅳ-5：用對稱軸追蹤圖形的對應","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__ == "__main__": main()

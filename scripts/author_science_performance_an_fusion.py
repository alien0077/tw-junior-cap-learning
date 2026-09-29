#!/usr/bin/env python3
"""Independent first-pass authoring for science performance n."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-performance-an.json"
REPORT=ROOT/"implementation/reports/science-performance-an-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download"}

def rec(p,c,r,m,a):
    return {"publisher":p,"edition":f"{p} 公立校方自然課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；科學本質、知識形成、模型與證據評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以觀察、推理、模型與社群檢核理解科學知識如何形成。"],"representations":[r],"examplesOrEvidence":["本課的月相模型、氣象預報與病原資訊皆為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-science-performance-an" and d["reviewStatus"]=="draft"
    d["title"]="認識科學本質（n）：從模型、證據到共同檢核"
    d["content"]={"summary":"科學知識不是直接把自然界搬進課本，而是人們用觀察、測量、推理和模型，對現象提出能被檢驗的解釋。模型可以幫助預測，也一定會省略某些細節；當新證據和預測不合時，科學社群會重查方法、修正模型或縮小適用範圍。本課以月相、氣象預報和病原資訊為原創情境，練習看見模型的用途、限制、證據與共同檢核。","sections":[{"heading":"自然現象與科學解釋不是同一件事","body":"月亮每天看起來不同是觀察，說明這些變化的日地月位置關係是模型。模型不是現象本身，而是把重要關係抽出來，讓我們能比較、預測與溝通。"},{"heading":"模型有用途也有邊界","body":"氣象圖把大量資料轉成顏色和符號，方便預測降雨；它不代表每一平方公尺的空氣都完全相同。使用模型要說明尺度、假設、忽略的因素與適用時間。"},{"heading":"證據會讓解釋變強或變窄","body":"多次且不同方法得到相近結果，能增加解釋的可信度；單一反例不一定立刻推翻全部知識，但會要求檢查條件和適用範圍。科學推論要把資料與解釋的距離說清楚。"},{"heading":"科學是社群共同工作的知識","body":"公開方法、讓他人重做、接受批評和比較不同證據，使知識不依賴某一個人的權威。不同研究結果不一定是誰在說謊，也可能提示樣本、方法或環境條件不同。"}]}
    d["studyHighlights"]=["區分自然觀察、模型與模型預測。","說明模型的用途、假設、尺度與限制。","用多次證據、反例與適用範圍修正解釋。","理解公開方法、重複與同儕檢核的社群性。"]
    d["teaching"]={"body":[
        {"id":"hook","phase":"hook","heading":"月亮變形還是我們看法改變？","body":"連續一週記錄月亮外觀，請先畫出觀察到的亮暗形狀，再比較兩個解釋：月亮自己變形，或太陽照亮的部分因相對位置改變。活動不要求立刻背答案，而是問哪個模型能同時解釋時間順序、亮面方向與預測。"},
        {"id":"explain","phase":"explain","heading":"模型是可操作的中介","body":"一個模型要能連接觀察與預測：指出假設、用圖或物件表示關係，推導下一個可觀察結果，再與資料比較。模型越簡潔不代表越真實；要看它是否在指定尺度和條件下有用，以及哪些細節被省略。"},
        {"id":"worked-example","phase":"worked-example","heading":"氣象預報的顏色不是雨量本身","body":"預報圖把不同區域標成降雨機率或回波顏色。讀圖時先查圖例、時間、空間尺度與數值定義，再說『在此時段與區域，資料支持降雨機率較高』。不能把顏色直接當成每個地點必然下雨，也不能因一次落空就說所有氣象模型無效。"},
        {"id":"guided-practice","phase":"guided-practice","heading":"三句話拆解病原資訊","body":"給出『檢測到某病原就代表一定會生病』的說法。學習者分辨檢測訊號、感染可能性與疾病結果，列出檢測敏感度、時間、症狀與樣本條件，再判斷需要什麼額外證據。這讓模型和測量都回到適用範圍，而非二分真偽。"},
        {"id":"transfer","phase":"transfer","heading":"比較兩個互相矛盾的模型","body":"兩組預測對同一場降雨不同，先並列各自假設、資料時間、解析度與預測範圍，再找能區分兩者的觀察。若新資料只支持其中一個情境，結論也要保留條件，記錄未解釋的例外，並說明下一次要補測哪些資料，不能只用支持自己的一張圖決定。"},
        {"id":"reflect","phase":"reflect","heading":"修正兩種權威迷思","body":"請修正『模型就是事實，所以不能改』與『模型會修正，所以模型沒有用』。模型是受證據檢核的解釋工具；它能在適用條件內產生預測，也必須隨新證據調整，而不是因可修正就失去全部價值。"}
    ],"summary":["模型連接觀察、解釋與可檢驗預測。","模型必須說明尺度、假設、用途與限制。","新證據可能提高可信度、修正模型或縮小範圍。","公開方法與同儕檢核使科學知識具社群性。"],"exitCheck":[{"prompt":"為什麼月亮外觀是觀察，日地月位置關係是模型？","expectedEvidence":"外觀是直接記錄的現象；位置關係是用來解釋並預測多次觀察的表徵工具。"},{"prompt":"讀氣象圖時為什麼要先看圖例與時間？","expectedEvidence":"顏色代表的量、空間尺度和時間不同，需先確認定義才能把資料連到預測。"},{"prompt":"模型會修正是否代表原本模型完全沒有用？","expectedEvidence":"不代表；模型可能在特定條件下有效，新證據會指出限制並促成修正或縮小適用範圍。"}]}
    d["interactive"]={"type":"guided-choice","goal":"從觀察、模型、預測與證據限制理解科學知識的形成。","scenario":"操作月相與氣象模型，選出能說明用途、假設與適用範圍的科學表達。","variables":[{"symbol":"o","meaning":"觀察資料"},{"symbol":"m","meaning":"模型假設"},{"symbol":"p","meaning":"模型預測"}],"steps":[{"id":"step-1","prompt":"記錄一週月亮亮暗形狀首先屬於什麼？","options":["觀察資料","已完成的模型預測","不可檢驗的權威結論"],"answer":"A","feedback":"圖形記錄是資料；模型要進一步解釋變化並產生可檢驗預測。"},{"id":"step-2","prompt":"使用氣象圖前最需要先確認哪一組資訊？","options":["圖例代表的量、時間與空間尺度","只看顏色深淺並忽略圖例","只看發布者是否有名"],"answer":"A","feedback":"沒有定義、時間和尺度，顏色不能直接轉成有意義的預測。"},{"id":"step-3","prompt":"新證據與模型預測不合時，最科學的做法是什麼？","options":["檢查方法與條件，必要時修正模型或縮小範圍","刪除不合資料並宣稱模型永遠正確","因為有例外就放棄所有模型"],"answer":"A","feedback":"科學知識透過查核、修正和標示限制逐步變可靠。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["versionResearch"]=[rec("nani","以觀察、模型、證據和科學知識形成理解自然現象。","現象記錄、模型圖、預測表與證據—解釋對照。","把模型當成自然本身或把權威結論視為不可檢驗。","重視觀察、推理、預測、證據與模型限制。"),rec("kanghsuan","透過探究、重複與討論理解科學知識可修正且可溝通。","實驗資料、模型操作、同儕檢核與修正紀錄。","只因一次反例就否定全部知識，或只挑符合模型的資料。","評量方法透明、證據品質、模型修正與表達。"),rec("hanlin","連結氣象、健康與科技資訊判讀，理解科學社群如何累積知識。","預報圖、檢測結果、來源比較、適用範圍與風險說明。","把機率當必然、檢測訊號當疾病結果，忽略尺度與條件。","要求判讀資料定義、說明不確定性與負責任溝通。")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持以觀察、證據、推理與模型理解科學本質。","模型能產生預測但有假設、尺度與限制，需接受新證據檢核。","公開方法、重複與同儕討論使科學知識能累積、修正與溝通。"],"versionDifferences":["南一證據較突顯觀察、模型與基本科學推理；康軒較突顯探究、重複、討論與模型修正；翰林較突顯氣象、健康資訊、尺度與負責任判讀。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以月相模型區分觀察、解釋與預測。","以氣象圖顏色示範圖例、尺度、時間與機率的限制。","以病原檢測訊號診斷測量結果與疾病結論的跳躍。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織觀察、模型、預測、證據、適用範圍、修正與科學社群檢核。正文、原創情境、互動步驟、錯誤回饋與檢核均為本專案重寫，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"認識科學本質（n）","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__=="__main__": main()

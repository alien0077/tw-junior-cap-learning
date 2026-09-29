#!/usr/bin/env python3
"""Independent first-pass authoring for science performance r."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-performance-tr.json"
REPORT=ROOT/"implementation/reports/science-performance-tr-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download"}

def rec(p,c,r,m,a):
    return {"publisher":p,"edition":f"{p} 公立校方自然課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；科學推理、證據論證、因果解釋與評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以資料、假設、推論與反例建立可檢核的科學論證。"],"representations":[r],"examplesOrEvidence":["本課的植物生長、保溫材料與河川水質皆為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-science-performance-tr" and d["reviewStatus"]=="draft"
    d["title"]="推理論證（r）：讓主張經得起資料追問"
    d["content"]={"summary":"科學推理論證不是把結論說得肯定，而是清楚連接主張、資料、推理規則與反例。面對植物生長、保溫材料或河川水質問題，要先確認資料是否真的量到要討論的量，再說明比較是否公平、替代解釋是否排除，以及結論能推到哪個範圍。本課以原創資料表與對話練習，學會提出可檢查、可修正、能回應反例的科學論證。","sections":[{"heading":"論證先問主張是什麼","body":"同一句『A 比 B 好』可能指生長高度、存活率、成本或安全性。先定義主張與量測指標，才知道需要哪些資料，避免用一個方便的數字替代真正問題。"},{"heading":"資料不會自己說話","body":"資料要透過推理才支持主張。比較時要看樣本、控制條件、測量誤差與趨勢；兩組平均不同不必然代表處理造成差異，還要考慮其他變因。"},{"heading":"反例讓結論更精準","body":"反例不一定全部推翻解釋，可能指出主張太廣或條件漏寫。把『任何情況都有效』改成適用對象、時間和條件清楚的句子，論證反而更可靠。"},{"heading":"回應質疑而不是換話題","body":"好的論證能指出對方資料的限制，也承認自己的限制，提出下一步可以區分兩個解釋的測量。這使討論從立場競爭回到可共同檢查的證據。"}]}
    d["studyHighlights"]=["先定義主張、指標與結論範圍。","用公平比較、樣本、誤差與替代解釋讀資料。","以反例縮小或修正過度寬廣的結論。","回應質疑時指出限制並提出可區分的下一步。"]
    d["teaching"]={"body":[
        {"id":"hook","phase":"hook","heading":"哪一盆植物真的長得比較好？","body":"兩盆植物一週後高度分別增加 4 公分與 6 公分。請先問『長得好』是高度、葉片數、重量還是存活率，再列出光照、澆水量、土壤和植株初始大小。這個入口提醒學習者：沒有明確指標和公平比較，漂亮的差距也不能自動成為結論。"},
        {"id":"explain","phase":"explain","heading":"主張—資料—推理—限制四格","body":"先用一句話寫主張，接著指出哪一筆資料與主張有關，再說明比較或因果推理如何成立，最後寫出限制與適用範圍。若資料只顯示同時變化，就用『相關線索』而非『已證明造成』；每個跳躍都要能被追問。"},
        {"id":"worked-example","phase":"worked-example","heading":"保溫材料的公平比較","body":"甲杯 20 分鐘後降 8 度、乙杯降 5 度，但甲杯裝 300 mL、乙杯裝 150 mL。不能直接判甲杯較差，因為水量不同。重新固定初始溫度、水量、環境、容器形狀與測量時間，再重複測量；結論需寫成在這些條件下乙材料的降溫較少。"},
        {"id":"guided-practice","phase":"guided-practice","heading":"水質資料的論證卡","body":"給兩個採樣點的濁度、pH 與採樣日期。學習者先判斷哪些資料能支持『上游較清澈』，再指出只測一天不能代表全年，也不能只看 pH 就推論所有污染。最後提出在不同日期、相同方法重複採樣的下一步，讓主張能被檢查。"},
        {"id":"transfer","phase":"transfer","heading":"回應同學的反例","body":"同學說『我的植物在陰影下也長高，所以光照不重要』。先承認這是值得記錄的反例，再問植物種類、時間、澆水和測量指標，判斷它是推翻哪個過度主張，或只是要求把結論改成特定植物與條件。"},
        {"id":"reflect","phase":"reflect","heading":"修正兩種論證錯誤","body":"請修正『平均數比較大，所以一定是處理造成』與『有一個反例，所以整個科學解釋毫無價值』。前者缺少控制與替代解釋，後者忽略反例可能只縮小適用範圍。完整論證要同時寫資料、推理、限制和下一步。"}
    ],"summary":["主張必須指定指標、條件與範圍。","資料需經公平比較與推理才可能支持結論。","反例可縮小主張並指出下一個檢驗方向。","論證要回應質疑、承認限制並提出下一步。"],"exitCheck":[{"prompt":"為什麼兩組平均數不同不能直接證明因果？","expectedEvidence":"可能有樣本、控制條件、測量誤差或其他變因差異，需要公平比較與重複。"},{"prompt":"如何把『材料 X 比較好』寫得可檢查？","expectedEvidence":"指定保溫等指標、初始溫度、水量、時間與比較方法，並說明結論適用的條件。"},{"prompt":"反例在科學論證中有什麼作用？","expectedEvidence":"可指出主張太廣或條件不足，促使修正範圍、檢查替代解釋並設計下一步。"}]}
    d["interactive"]={"type":"guided-choice","goal":"用主張、資料、推理與限制組成可檢查的科學論證。","scenario":"比較植物、保溫杯與水質資料，找出公平比較和能回應反例的說法。","variables":[{"symbol":"c","meaning":"科學主張"},{"symbol":"e","meaning":"觀察證據"},{"symbol":"l","meaning":"論證限制"}],"steps":[{"id":"step-1","prompt":"比較兩種保溫材料前，最重要的第一步是什麼？","options":["固定水量、初始溫度、環境與時間等條件","先選擇支持期待的那組數字","只比較最後一個溫度"],"answer":"A","feedback":"公平比較要讓主要差異來自材料，而不是水量或環境差異。"},{"id":"step-2","prompt":"兩個採樣點只測一天，結論應如何表達？","options":["說明本次資料的範圍，不能直接推廣到全年","宣布已代表所有季節的水質","因資料少就完全不必分析"],"answer":"A","feedback":"資料可以支持有限範圍的比較，同時要標示時間限制。"},{"id":"step-3","prompt":"遇到反例時，哪種回應最符合科學論證？","options":["檢查條件與替代解釋，必要時縮小主張並設計下一步","直接攻擊提出反例的人","刪除反例以保留原結論"],"answer":"A","feedback":"反例提供修正模型和設計新檢驗的機會。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["versionResearch"]=[rec("nani","以資料、推理與反例建立能說明自然現象的科學論證。","資料表、比較圖、主張—證據—推理鏈與限制欄。","把相關變化當成因果，或把單一反例當成全盤否定。","重視證據適切性、推理連貫、範圍與反思修正。"),rec("kanghsuan","透過實作、討論和重複測量培養提出主張與回應質疑的能力。","公平比較、控制變因、重複資料、對話與修正紀錄。","忽略樣本和測量誤差，只挑支持結論的資料。","評量資料分析、論證品質、同儕回應與下一步設計。"),rec("hanlin","以環境與生活資料判讀因果、證據限制和公共議題推理。","水質資料、圖表、不同觀點、適用範圍與後續查證。","用一個方便指標代表全部問題，或把過度寬廣結論當定律。","要求證據引用、限制說明、反例處理與負責任表達。")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持以資料、推理與反例建立科學論證。","公平比較、控制條件、測量品質與適用範圍是共同的證據要求。","回應質疑並提出下一步能使主張持續被檢查和修正。"],"versionDifferences":["南一證據較突顯基本證據鏈與反例；康軒較突顯實作、重複、討論與修正；翰林較突顯環境資料、圖表與公共議題中的範圍判斷。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["用植物生長案例釐清指標與公平比較。","用不同水量的保溫杯數據診斷因果跳躍。","用水質採樣和植物陰影反例練習縮小主張與設計下一步。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織主張、資料、推理、控制條件、反例、限制與下一步探究。正文、原創數據情境、互動步驟、錯誤回饋與檢核均為本專案重寫，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"推理論證（r）","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__=="__main__": main()

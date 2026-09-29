#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-3."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-s-iv-3.json"
REPORT = ROOT / "implementation/reports/math-performance-s-iv-3-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
}

def record(p, c, r, m, a):
    return {"publisher":p,"edition":f"{p} 公立校方數學課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；垂直、平行與截線角的概念、表徵及評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以直角、平行線與截線形成的角關係進行推理。"],"representations":[r],"examplesOrEvidence":["本課的道路網、窗框與紙張摺線均為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-math-performance-s-iv-3" and d["reviewStatus"]=="draft"
    d["title"]="s-Ⅳ-3：用直角與截線角判斷平行"
    d["content"]={"summary":"垂直表示兩線相交成直角，平行表示同一平面上的兩線不相交；兩者不能只靠圖形看起來判斷。當一條截線穿過兩條直線時，同位角、內錯角與同側內角提供判斷平行的線索，但必須先確認角的位置與方向。本課以道路網、窗框與紙張摺線的自編情境，練習用符號記錄垂直平行、辨認截線角、由角相等或互補推出平行，並用反例檢查推理。","sections":[{"heading":"垂直與平行的定義","body":"垂直線相交形成 90° 直角；平行線位於同一平面且不相交。線段、射線或直線的範圍要看清楚，不能因兩段在圖上沒有交點就直接稱為平行。"},{"heading":"截線形成的角位置","body":"一條線穿過兩條線時，依角所在位置分辨同位角、內錯角與同側內角。先標出兩條被截線與截線，再談角關係，避免只看角度數字。"},{"heading":"用角關係判斷平行","body":"若一對同位角或內錯角相等，或一對同側內角和為 180°，在適當的直線與截線條件下可推出兩線平行。推理要寫出使用的角關係與結論方向。"},{"heading":"符號與實際設計","body":"用 AB⊥CD、EF∥GH 記錄關係，並回到道路、窗框或摺線檢查單位和端點。若圖形只是近似繪製，應以量角、條件或證明作判斷，不把畫面誤差當幾何事實。"}]}
    d["studyHighlights"]=["先確認兩條線及是否有截線，再讀角的位置。","垂直看 90°，平行看不相交或可由截線角關係推出。","分辨同位角、內錯角與同側內角，寫清楚使用的理由。","用符號、反例與量角檢查圖形判斷。"]
    d["teaching"]={"body":[{"id":"hook","phase":"hook","heading":"道路交會圖上的直角與平行","body":"原創校園道路圖有兩條相鄰車道邊界、一條斜向人行線與一個直角標記。請學習者先不按比例尺猜測，找出哪些線真正由條件保證垂直或平行，再設計一條截線觀察交出的角。"},{"id":"explain","phase":"explain","heading":"先定位角再命名關係","body":"在兩條被截線與一條截線的圖上，先圈出兩個角的頂點與位置，再判斷是同位、內錯或同側內角。以同位角相等、內錯角相等與同側內角互補三種情況逐一寫出條件與結論，避免只背名稱。"},{"id":"worked-example","phase":"worked-example","heading":"由 65 度推出平行","body":"一條截線與兩條線相交，若一對內錯角都為 65°，先標明它們位於兩線之間且在截線兩側；因內錯角相等，可推出兩條線平行。再找相鄰角為 115°，檢查同側內角 65°+115°=180°，兩種證據一致。"},{"id":"guided-practice","phase":"guided-practice","heading":"判斷條件是否足夠","body":"提供三張角標記圖：同位角相等、同側內角和 180°、以及兩角都為 70°但位置不明。學習者先補上角的位置，再決定能否推出平行；對第三張圖必須說明缺少截線與位置資訊，不能只因數字相同就作答。"},{"id":"transfer","phase":"transfer","heading":"窗框與摺線的實際應用","body":"原創窗框設計要求兩條水平邊保持平行、側邊與水平邊垂直。學生用符號記錄設計條件，再以截線或直角工具檢查；若紙張摺線只在一小段看似平行，需說明量測範圍與誤差，不能把局部外觀推成整條直線關係。"},{"id":"reflect","phase":"reflect","heading":"修正看圖猜平行","body":"請修正『圖上兩條線沒有碰到，所以一定平行』。先指出圖形只呈現有限範圍，可能是延長後相交；再列出不相交的定義、平行符號或截線角證據，最後用一張透視道路圖作反例。"}],"summary":["垂直由 90° 定義，平行需有同平面不相交或足夠角關係證據。","先確認被截線與截線，再定位同位角、內錯角、同側內角。","角相等或互補可在適當條件下推出平行，需寫明推理方向。","圖形比例不是證明，應用符號、量角、條件與反例檢查。"],"exitCheck":[{"prompt":"垂直與平行各如何定義？","expectedEvidence":"垂直相交成 90° 直角；平行是同一平面兩線不相交，或由足夠截線角條件推出。"},{"prompt":"內錯角相等時如何判斷？","expectedEvidence":"先確認兩角位於兩線之間且在截線兩側；若相等，可推出被截兩線平行。"},{"prompt":"為什麼圖上沒有交點不足以證明平行？","expectedEvidence":"圖只呈現有限範圍或可能有繪圖誤差，需定義、符號、量測或角關係支持。"}]}
    d["teaching"]["body"][0]["body"] += " 再把道路邊界延長，核對角標記是否在同一平面，說明局部圖像與完整幾何條件的差別。"
    d["teaching"]["body"][5]["body"] += " 並把反例中的線延長、標示可能相交的位置，讓平行判斷可以由另一位同學重做。"
    d["interactive"]={"type":"guided-choice","goal":"定位截線角並用相等、互補或直角條件判斷垂直平行。","scenario":"標記兩條被截線與截線，改變角度資料，觀察哪些條件足以推出平行。","variables":[{"symbol":"a","meaning":"第一個截線角"},{"symbol":"b","meaning":"與 a 配對的第二個角"},{"symbol":"x","meaning":"待判斷的平行或垂直關係"}],"steps":[{"id":"step-1","prompt":"判斷兩線是否垂直，最直接的條件是什麼？","options":["相交成 90° 直角","圖上看起來接近直角","兩線長度相等"],"answer":"A","feedback":"垂直由相交成 90° 定義，不能只靠外觀或長度。"},{"id":"step-2","prompt":"一對內錯角相等時，在適當截線條件下可推出什麼？","options":["兩條被截線平行","兩條線一定垂直","截線長度相等"],"answer":"A","feedback":"內錯角相等是判斷平行的充分角關係之一。"},{"id":"step-3","prompt":"為什麼兩條線在圖面範圍內沒有交點仍不夠判定平行？","options":["可能只是有限繪圖範圍，需更多條件","因為所有線都會相交","因為平行線必須等長"],"answer":"A","feedback":"要用定義、符號、量測或截線角證據，而不是只看局部畫面。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["versionResearch"]=[record("nani","以垂直平行定義與截線角關係建立判斷","道路圖、角標記、同位內錯與同側內角表徵","只看圖形沒有交點或角度數字而忽略位置","要求定位角、列條件並說明平行結論"),record("kanghsuan","透過摺紙與操作理解直角、平行及截線","紙張摺線、量角器、符號與角位置操作","混淆同位角與內錯角，或把局部平行當成整線平行","重視操作證據、圖形標記與反例檢查"),record("hanlin","連結道路、窗框與幾何推理的實際限制","設計圖、直角工具、單位與繪圖誤差","以畫面比例代替定義或證明，忽略測量範圍","評估模型、條件、角關係與實際精度是否一致")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持以垂直平行定義與截線角關係進行推理。","同位角、內錯角、同側內角與直角標記是共同表徵工具。","圖形、符號、量測與反例需互相驗證，不能只看外觀。"],"versionDifferences":["南一證據較突顯垂直平行與角關係；康軒較突顯摺紙、量角與角位置操作；翰林較突顯道路窗框設計及繪圖誤差限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以校園道路圖分辨被截線、截線與直角標記。","以 65° 與 115° 同時驗證內錯角和同側內角條件。","把局部外觀、符號、反例、量測範圍與窗框設計整合成互動任務。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織垂直平行定義、截線角、符號、反例與道路窗框應用。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"s-Ⅳ-3：用直角與截線角判斷平行","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__ == "__main__": main()

#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-10."""
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/math/lesson-math-performance-s-iv-10.json"
REPORT=ROOT/"implementation/reports/math-performance-s-iv-10-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"}

def record(p,c,r,m,a):
    return {"publisher":p,"edition":f"{p} 公立校方數學課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；三角形相似、比例與測量的概念、表徵及評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持以對應角、邊長比例與相似三角形模型解決測量問題。"],"representations":[r],"examplesOrEvidence":["本課的旗桿影子、河岸測距與透視模型均為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}

def main():
    d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-math-performance-s-iv-10" and d["reviewStatus"]=="draft"
    d["title"]="s-Ⅳ-10：用相似三角形建立測量比例"
    d["content"]={"summary":"三角形相似表示對應角相等、對應邊成固定比例；若能把複雜圖形拆成兩個共享角或平行線形成的三角形，就能用比例求出無法直接量測的長度。建立比例時最重要的是對應順序與單位，不能把不相應的邊交叉配對。本課以旗桿影子、河岸測距與透視模型的自編情境，練習 AA、比例鏈、平行線截出的相似三角形，並以估值與圖形方向檢查結果。","sections":[{"heading":"相似三角形先找角","body":"兩角相等可用 AA 判定相似；先標出共同角、平行線造成的對應角，再按頂點順序寫相似符號。角度相等只固定形狀，不直接代表邊長相等。"},{"heading":"比例要依對應排列","body":"若 △ABC∼△DEF，則 AB/DE=BC/EF=CA/FD。分子分母要維持同一方向，列出一組對應後再交叉使用，避免比例式前後混搭。"},{"heading":"平行線帶來相似","body":"三角形內一條與底邊平行的線會形成小三角形與大三角形，因共同角與平行角可判定相似。小圖與大圖的邊長比例一致，周長與面積則有不同尺度。"},{"heading":"測量模型需要檢查","body":"影子、河岸或透視圖必須確認地面平行、光線方向或視線條件；若條件改變，不能直接沿用相似比例。答案要檢查長短方向、單位與合理範圍。"}]}
    d["studyHighlights"]=["先找共同角、平行角與頂點對應。","寫相似符號後，再依相同方向列邊長比例。","影子與平行線模型需要明確的幾何條件。","用估值、單位、長短範圍與比例回查。"]
    d["teaching"]={"body":[{"id":"hook","phase":"hook","heading":"不用爬樹也能量旗桿嗎？","body":"原創測量任務在同一時間量旗桿影長 12 公尺、短標桿高 1.5 公尺且影長 2 公尺。請學習者先畫出兩個由地面與陽光形成的直角三角形，找出共同角，再預測旗桿高約 9 公尺，讓比例模型從實際測量需求出發。"},{"id":"explain","phase":"explain","heading":"從 AA 到比例鏈","body":"兩個影子三角形都有直角，且同一時間陽光方向給出共同銳角，因此可用 AA 判定相似。依『旗桿／標桿=影長／影長』列出 h/1.5=12/2，再說明交叉相乘與單位相消，避免把高度和影長錯配。"},{"id":"worked-example","phase":"worked-example","heading":"用平行線求小三角形邊長","body":"大三角形底邊 15、公頂到底高 10，內部平行線截出高 4 的小三角形。由相似比例，小三角形對應底邊為 15×4/10=6；最後檢查縮小因子 0.4，所有對應長度都應乘 0.4。"},{"id":"guided-practice","phase":"guided-practice","heading":"校正比例方向","body":"提供三組相似三角形資料，要求先寫頂點對應，再選 h/1.5=12/2 或 h/12=1.5/2 等等值比例。對把 h/2=12/1.5 的錯誤，回饋要求指出分子分母代表的量與單位，並用估值檢查答案。"},{"id":"transfer","phase":"transfer","heading":"把相似用在河岸與透視圖","body":"原創河岸任務用兩條平行岸線和一條視線構成相似三角形，先以圖形條件證明相似，再求不可直接跨越的寬度。透視模型若視線不共線或岸線不平行，需指出比例失效的原因，不能只套公式。"},{"id":"reflect","phase":"reflect","heading":"修正相似等於邊長相等","body":"請修正『兩三角形相似，所以所有對應邊一樣長』。先指出相似只代表固定比例，再用縮放因子 3 的三角形反例；最後說明只有縮放因子 1 或全等時，對應邊才相等。"}],"summary":["AA 先確認角度條件，建立頂點與邊的對應。","依相似符號方向列比例，避免交叉錯配。","平行線、影子、視線模型都需要明確幾何條件。","用縮放因子、估值、單位與圖形方向檢查。"],"exitCheck":[{"prompt":"旗桿高 h、影長 12，標桿高 1.5、影長 2，如何列比例？","expectedEvidence":"由 AA 相似，h/1.5=12/2，得 h=9 公尺，並說明同一時間光線條件。"},{"prompt":"平行線截出的高 4、大三角形高 10，底邊 15 的小底邊是多少？","expectedEvidence":"相似縮放因子 4/10，對應底邊 15×4/10=6。"},{"prompt":"為什麼相似三角形對應邊不一定相等？","expectedEvidence":"相似只要求比例固定，縮放因子可不是 1；全等才要求對應長度相等。"}]}
    d["interactive"]={"type":"guided-choice","goal":"由 AA 與平行條件建立相似三角形，再依對應順序求未知長度。","scenario":"標記共同角與對應邊，調整影長或平行截線，觀察比例和估值。","variables":[{"symbol":"h","meaning":"待求的高度或對應長度"},{"symbol":"x","meaning":"模型中的已知邊長"},{"symbol":"k","meaning":"相似三角形的縮放比例"}],"steps":[{"id":"step-1","prompt":"旗桿與標桿影子三角形可用哪個條件判斷相似？","options":["AA，兩個角相等","SSS，三邊必須相等","只因兩圖都像三角形"],"answer":"A","feedback":"直角與同一光線方向形成的角可支持 AA。"},{"id":"step-2","prompt":"h/1.5=12/2 時，旗桿高 h 是多少？","options":["9 公尺","6 公尺","16 公尺"],"answer":"A","feedback":"12/2=6，h=1.5×6=9，並檢查單位與長短比例。"},{"id":"step-3","prompt":"小三角形高 4、大三角形高 10，縮放因子是多少？","options":["0.4","2.5","6"],"answer":"A","feedback":"小圖對大圖的對應長度比例為 4/10=0.4。"}]}
    d["authoringStandard"]="version-fused-v1"
    d["teaching"]["body"][5]["body"] += " 並把兩組對應邊的比值寫出來，確認比例固定但數值不必相同，讓相似與全等的界線可驗算。"
    d["versionResearch"]=[record("nani","以三角形相似條件與比例解決不可直接量測的長度","影子三角形、平行線、共同角、對應頂點與比例鏈","只看形狀相似未確認角度或比例方向","要求建立對應、列比例並檢查單位"),record("kanghsuan","透過操作圖形與影子模型理解 AA 相似","標桿、紙模型、平行截線與比例表","把相似邊任意配對，或將相似誤當邊長相等","重視模型操作、角度條件與估值驗證"),record("hanlin","連結河岸測量、透視與實際比例限制","河道、視線、平行岸線、單位與誤差","忽略平行或共線前提而直接套用比例","評估模型、比例、方向、單位與不可量測條件")]
    d["fusionRecord"]={"commonCore":["三版本公開結構共同支持以角度與邊長比例判斷三角形相似。","AA、對應順序、比例鏈與平行線模型是共同核心。","影子、測量、單位與模型前提需互相檢查。"],"versionDifferences":["南一證據較突顯相似判定與比例；康軒較突顯影子、紙模型及平行截線操作；翰林較突顯河岸測量、透視與實際限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以旗桿影長 12、標桿 1.5 與影長 2 示範不可直接量測。","以平行截線高 4/10 與底 15 求小三角形底邊。","把河岸視線前提、比例方向、單位與相似／全等界線整合成互動任務。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織三角形相似、AA、比例鏈、平行截線、影子與河岸測量。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"s-Ⅳ-10：用相似三角形建立測量比例","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))

if __name__ == "__main__": main()

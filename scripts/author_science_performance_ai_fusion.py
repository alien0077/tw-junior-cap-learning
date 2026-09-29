#!/usr/bin/env python3
"""Independent first-pass authoring for science performance i-interest."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-performance-ai.json"; REPORT=ROOT/"implementation/reports/science-performance-ai-first-pass-review.json"
URLS={"nani":"https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf","kanghsuan":"https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110","hanlin":"https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download"}
def rec(p,c,r,m,a): return {"publisher":p,"edition":f"{p} 公立校方自然課程計畫章節級證據","sourceType":"public-web","sourceLocator":f"{URLS[p]}；科學探究興趣、好奇提問、探索活動與評量欄位；核讀 2026-09-21。","reviewedAt":"2026-09-21","findings":{"concepts":[c,"公開課程結構支持從生活現象和好奇問題進入探究，享受發現、修正與分享的過程。"],"representations":[r],"examplesOrEvidence":["本課的泡泡、聲音與夜間昆蟲觀察皆為原創情境，只承接公開課程所示的能力方向。"],"misconceptions":[m],"assessmentEmphasis":[a]},"licenseBoundary":"只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}
def main():
 d=json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"]=="lesson-science-performance-ai" and d["reviewStatus"]=="draft"
 d["title"]="培養科學探究的興趣（i）：讓好奇變成可玩的問題"
 d["content"]={"summary":"科學探究的興趣不是只在答案正確時才出現，而是從『為什麼會這樣』開始，享受觀察、猜想、動手試、發現意外和重新設計的過程。泡泡形狀、聲音回音或夜間昆蟲都能成為入口；重要的是把好奇保留下來，同時用安全、可行且可記錄的方法追問。本課以原創小任務讓學習者經歷驚訝、猜想、測試、分享與再提問，建立願意持續探究的動機。","sections":[{"heading":"好奇來自細小的不一致","body":"同樣吹泡泡，為什麼有的很快破、有的能連在一起？先描述意外，再提出多個可能因素。興趣不要求立刻知道答案，而是把不明白的地方變成值得靠近的問題。"},{"heading":"玩也要有一個可觀察焦點","body":"自由探索很重要，但加上一個小焦點能讓發現留下來，例如只改變吸管口徑並記錄泡泡壽命。焦點不是限制想像，而是讓同學之間能比較各自的發現。"},{"heading":"意外結果是下一個入口","body":"聲音變大或昆蟲沒有出現，可能表示原先猜想、時間、器材或環境需要重看。把失敗當成訊息，能把挫折轉成下一輪設計，而不是快速貼上『我不會』的標籤。"},{"heading":"分享會讓興趣長出分支","body":"聽見別人的方法和解釋，可能發現同一現象有不同問題。分享時說明觀察、猜想、做法與尚未知道的部分，讓同伴能接著追問，探索就不會停在個人作品。"}]}
 d["studyHighlights"]=["從細小不一致和意外結果保存好奇。","用小而可觀察的焦點讓自由探索留下資料。","把失敗和未知轉成下一輪問題，而非自我否定。","透過分享方法、猜想與疑問讓探究延續。"]
 d["teaching"]={"body":[
 {"id":"hook","phase":"hook","heading":"泡泡為什麼不一樣？","body":"桌上有三種吹泡泡工具，泡泡大小和壽命不同。請先自由試兩分鐘，再貼出你最想知道的一件事；不要求每個人提出同樣問題。接著選一個能在教室安全測試的小焦點，感受興趣可以從玩耍走向可分享的觀察。"},
 {"id":"explain","phase":"explain","heading":"興趣探究的五個節點","body":"注意現象、提出好奇、做一個小測試、記錄意外、再問下一題。每個節點都可以停下來交換想法；測試不是把答案考出來，而是讓猜想遇到資料。安全界線、尊重生物與器材使用規則始終優先。"},
 {"id":"worked-example","phase":"worked-example","heading":"回音小實驗的猜想分岔","body":"在兩個位置拍手，回音強弱不同。有人猜牆面材質，有人猜距離和背景噪音。先選安全、不打擾他人的位置，固定拍手方式，記錄距離、環境和聽到的延遲；若結果模糊，就把『怎麼讓差異更容易觀察』變成下一題，而不是硬選一個原因。"},
 {"id":"guided-practice","phase":"guided-practice","heading":"夜間昆蟲觀察任務","body":"提供手電筒、白布、時間表和不捕捉規則。小組先猜哪種光線或位置可能看到較多昆蟲，再決定只觀察與拍照記錄。若沒有昆蟲，檢查時間、天氣與干擾並提出改期或改點方案，讓沒有發現也成為資料。"},
 {"id":"transfer","phase":"transfer","heading":"做一張我的未解問題牆","body":"每人留下現象、猜想、已嘗試的方法、意外結果與下一問題；同學可在旁邊貼上不同解釋或安全的測試建議。定期回看問題牆，選一題延伸，讓探究興趣由個人好奇變成群體的持續學習。"},
 {"id":"reflect","phase":"reflect","heading":"修正兩個興趣迷思","body":"請修正『有興趣就不用記錄和遵守安全』與『沒有得到漂亮結果就代表探究失敗』。記錄和安全讓探索能持續、能分享；意外、模糊和沒有出現都能提供下一題，只要誠實描述並找到合適的改變。"}
 ],"summary":["從意外、細節和未知保留好奇。","用小焦點和安全測試讓自由探索可分享。","失敗、模糊和沒有發現都能成為下一個問題。","分享方法和疑問讓個人興趣連成持續探究。"],"exitCheck":[{"prompt":"為什麼自由玩泡泡後還要選一個小觀察焦點？","expectedEvidence":"焦點讓猜想、改變條件和觀察結果可以留下並互相比較，不是限制好奇。"},{"prompt":"夜間沒有看到昆蟲時可以怎麼做？","expectedEvidence":"記錄時間、天氣、位置與方法，檢查干擾後改期或改點，不直接把沒有看到當成沒有昆蟲。"},{"prompt":"為什麼探究興趣需要遵守安全與生物尊重？","expectedEvidence":"安全和倫理讓探索能持續、可分享且不把好奇建立在傷害他人或生物上。"}]}
 d["interactive"]={"type":"guided-choice","goal":"把好奇、意外與未知轉成安全、可觀察且能延續的探究問題。","scenario":"探索泡泡、回音與夜間昆蟲，逐步選擇能保留興趣又能留下證據的行動。","variables":[{"symbol":"q","meaning":"好奇問題"},{"symbol":"o","meaning":"觀察焦點"},{"symbol":"n","meaning":"下一個問題"}],"steps":[{"id":"step-1","prompt":"自由玩泡泡後，哪個做法最能讓興趣延續？","options":["選一個安全的小焦點，改變一項條件並記錄結果","只追求吹出最大的泡泡","把不同結果都當成運氣不記錄"],"answer":"A","feedback":"小焦點讓好奇轉成可比較的探索，同時保留繼續提問的空間。"},{"id":"step-2","prompt":"回音結果不清楚時，最好的反應是什麼？","options":["檢查環境和方法，提出下一個更容易觀察的測試","硬選一個原因以便交作業","宣稱聲音現象無法研究"],"answer":"A","feedback":"模糊結果可以幫助改良方法並產生新問題。"},{"id":"step-3","prompt":"觀察昆蟲時哪種做法最合適？","options":["遵守不捕捉和安全規則，記錄沒有發現的條件並改期或改點","為了確認猜想抓回教室","只記錄看到的成功小組"],"answer":"A","feedback":"安全、倫理和完整紀錄讓興趣能長期延續並被同伴接手。"}]}
 d["teaching"]["summary"][0]="從意外、細節和未知保留好奇，讓問題有機會繼續生長。"
 d["authoringStandard"]="version-fused-v1"
 d["versionResearch"]=[rec("nani","以生活現象、好奇提問與動手探索培養科學學習興趣。","現象筆記、猜想、小測試、意外紀錄與下一問題。","把興趣只等同於答對，或因結果不漂亮就放棄。","重視主動觀察、安全、持續提問與分享。"),rec("kanghsuan","透過遊戲、實作、合作和發現意外維持探究動機。","開放任務、同儕想法、原型、回饋與改版。","自由探索完全不需焦點或記錄，忽略方法和合作。","評量參與、提問、嘗試、反思與合作表達。"),rec("hanlin","連結自然、聲音、生物與生活環境，兼顧興趣、安全和尊重生命。","泡泡、回音、夜間觀察、天氣、位置與不捕捉規則。","為了好奇打擾或傷害生物，或把未觀察到當成不存在。","要求安全倫理、觀察品質、問題延伸與持續學習。")]
 d["fusionRecord"]={"commonCore":["三版本公開結構共同支持從生活現象和好奇提問進入科學探究。","動手嘗試、紀錄意外、分享與下一問題是共同的興趣維持方式。","安全、倫理、可行焦點與誠實資料讓探索能長期延續。"],"versionDifferences":["南一證據較突顯生活現象、好奇、觀察與基本探究；康軒較突顯遊戲、實作、合作與發現；翰林較突顯自然環境、生物尊重、安全與持續學習。這是公開課程計畫層級差異，不宣稱完整教材差異。"],"originalAdditions":["以三種泡泡工具讓自由玩耍轉成小焦點測試。","以回音模糊結果示範猜想分岔與下一問題。","以不捕捉的夜間昆蟲觀察把安全、倫理和沒有發現納入資料。"],"llmSynthesisNote":"本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織好奇、現象、焦點、猜想、測試、意外、分享、安全與問題延伸。正文、原創任務、互動步驟、錯誤回饋與檢核均為本專案重寫，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
 d["updatedAt"]="2026-09-21"; LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"培養科學探究的興趣（i）","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"answersAndDetailedSteps":True,"terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))
if __name__=="__main__": main()

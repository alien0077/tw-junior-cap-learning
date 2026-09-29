import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","方法改變、預測與探究能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","實驗設計、控制與創新能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","資料比較、安全與方法修正能力方向")]
DATA=[
("prediction","改變紙橋形狀前，最完整的做法是？",["預測承重如何變、說明受力理由，並固定紙量與加重程序","只選最奇怪的形狀","同時改變紙張、長度與砝碼","先做完再補寫預測"],"A","A 把創意連到理由和可公平檢查的預測。"),
("control","比較平面、波浪、管狀紙橋時，哪項應固定？",["紙張材質、長度、寬度、加重方式與失效定義","每種形狀使用不同紙量","每組自行決定何時停止","只固定最後最高值"],"A","A 避免多因素同時改變，才能解釋形狀造成的差異。"),
("dissolution","想用旋轉容器改變糖溶解方法，先應做什麼？",["預測旋轉對接觸和時間的影響，再固定水量、溫度、糖量與停止定義","同時換容器、糖粒和水溫","只看哪杯最漂亮","先宣布旋轉一定更快"],"A","A 把方法改變轉成有機制和控制的測試。"),
("photo method","用照片取代尺量影子時，最重要的控制是？",["固定相機位置、比例尺、時間與光源，並用尺量交叉檢查","每次從不同角度拍","只選最清楚照片","刪除不符合預期的影子"],"A","A 處理照片比例、角度和環境造成的偏差，讓新舊方法可比較。"),
("hypothesis","創新版方法不符預測時，哪個處理最合理？",["檢查假設、指標與程序，提出能區分原因的第二版測試","修改資料使預測成立","直接宣布創意沒有價值","換成無關問題"],"A","A 把不符預測轉成可用的設計線索。"),
("fair test","一次改變三項條件後結果變好，主要限制是？",["無法知道是哪一項改變造成結果，需分階段或拆開測試","三項一起改比較科學","結果變好就不需解釋","只要增加口號即可"],"A","A 指出因果歸因不清，應設計能分辨各因素的比較。"),
("safety","使用重物測試新紙橋時，哪項最合適？",["逐步加重、保持安全距離、設定停止條件並記錄失效","一次堆到最高節省時間","為了創新取消護具","橋塌後繼續操作"],"A","A 同時保留可測試程序和安全底線。"),
("innovation","哪項最符合有證據的科學創新？",["用較少材料設計隔熱結構，預測保溫效果並以同條件測試","只讓外觀更奇特","換成昂貴材料但不測量","把失敗資料刪除"],"A","A 創新有目的、預測、資源考量和可驗證測試。"),
("cross-check","新照片法與尺量結果不同時，先查什麼？",["查比例尺、角度、時間、光源與兩種方法的定義，再重測","只採用照片結果","把兩數平均不查原因","宣稱其中一種一定造假"],"A","A 先定位方法差異，再判斷是真實變化或測量問題。"),
("next iteration","第二版方法仍失敗，最有用的紀錄是？",["保留失敗條件、已排除的假設與下一個可區分原因的測試","只寫創意很棒","改寫成成功報告","不留下原始資料"],"A","A 讓失敗成為下一輪設計可用的證據。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以方法改變、預測、控制、創新、安全與資料修正要求設計推理；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出方法創新核心「{topic}」。","列出改變條件、預測理由、控制變因、測量指標、安全與比較範圍。",f"逐項比對哪個方案能接受公平測試；正確答案是 {ans}。",f"核對理由：{exp}","最後說明若結果不符預測，如何保留資料、修正假設並設計下一輪可區分的測試。"]
 return {"id":f"question-science-performance-ti-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-ti-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究方法改變、預測、控制、創新與安全能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-ti-iv-1","examPatternRefs":refs,"solutionStrategy":"先寫方法改變和預測，再檢查控制、安全、公平比較與失敗後的修正。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-ti-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")

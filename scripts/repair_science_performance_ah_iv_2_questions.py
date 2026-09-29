import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","科學應用、資料與決策能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","探究方法、方案比較與風險能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","環境議題、證據與責任決策能力方向")]
DATA=[
("goal","比較校園降溫方案前，第一步最適合做什麼？",["列出降溫目標、預算、能源、安全、可及性與受影響者","只選降溫數字最大的方案","先投票再找資料","只問最有權力的人"],"A","A 先界定目標和限制，避免單一指標假裝代表整個決策。"),
("indicator","比較飲水設備時，哪組指標較完整？",["水質、維護頻率、濾芯成本、使用率與停機風險","只看外觀顏色","只問一位使用者喜不喜歡","只比較購買價格"],"A","A 同時涵蓋安全、維護、成本、使用和風險，能支持較完整方案比較。"),
("uncertainty","資料不足但社區必須先做決定，哪個做法較負責任？",["小規模試行、設定監測指標與停止警訊，再依資料修正","直接全面施工且不留回頭路","補填缺少的數據","因為不確定就永遠不做任何事"],"A","A 將不確定性轉成可監測、可逆的決策設計，不假裝全知。"),
("tradeoff","河川整治方案同時影響防洪、生態、通行與成本，應如何處理？",["列出多重指標和受影響者，說明不同價值取捨再比較","只看防洪數字最高者","只用工程師一人決定","把生態和公平刪除以簡化表格"],"A","A 不把效率偷偷當成唯一價值，讓證據與取捨透明。"),
("pilot","校園飲水設備試行時，哪項安排最能檢查長期問題？",["設定試行範圍與週期，定期測水質、故障、使用率並收集不同使用者回饋","只在啟用當天拍照","只記錄最順利的一天","先宣布永久成功"],"A","A 把效果、故障和使用者經驗放入持續監測，避免一次滿意度代替長期安全。"),
("fairness","若降溫設備只裝在一棟樓，決策報告至少應說明什麼？",["哪些人受益、哪些人承擔噪音或能源成本，以及如何改善不公平","只公布平均溫度","只說設備很新","把沒有設備的樓棟排除"],"A","A 把分配影響和代價公開，公平不是一個平均數就能代表。"),
("evidence","科學資料能支持公共決策，但不能單獨決定哪件事？",["誰應承擔代價、何種公平最重要與可接受風險","方案的測量溫度","水質檢測結果","設備耗電量"],"A","A 數據能比較效果和風險，價值、責任與公平仍需利害關係人討論。"),
("monitor","試行方案出現水質警訊時，最適當的行動是？",["依預先設定的停止門檻暫停使用、回查原因並公開處理方式","為維持形象繼續使用","刪除警訊紀錄","把責任推給使用者"],"A","A 把安全門檻和回查程序化，優先保護使用者並維持證據透明。"),
("reversibility","為何在不確定時偏好可回頭的試行？",["若結果不符預期能及早停止或調整，降低一次全面決策的代價","可免除任何資料蒐集","代表方案一定成功","可以不告知受影響者"],"A","A 可逆性降低錯誤決策的傷害，但仍需要監測、告知和回饋。"),
("communication","負責任的決策報告應包含什麼？",["目標、證據、未知、風險、受影響者、價值取捨與修正方式","只公布成功數字","只列專家姓名","把不確定性全部刪掉"],"A","A 讓資料和價值選擇透明，社群才能檢查、參與和要求修正。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以資料、方案、環境、風險與證據界線要求應用科學做決定；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出決策核心「{topic}」。","列出目標、限制、證據指標、受影響者、風險、不確定性與可逆性。",f"逐項比對方案是否有可檢查的理由；正確答案是 {ans}。",f"核對理由：{exp}","最後回查哪些部分可由數據支持、哪些需要公平與責任討論，並寫出監測或修正行動。"]
 return {"id":f"question-science-performance-ah-iv-2-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-ah-iv-2"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究科學應用、方案比較、風險與責任決策能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-ah-iv-2","examPatternRefs":refs,"solutionStrategy":"先界定目標和限制，再比較證據、指標、風險、可逆性、公平與受影響者，最後設計試行和監測。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-ah-iv-2-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")

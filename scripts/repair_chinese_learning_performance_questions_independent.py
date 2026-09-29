#!/usr/bin/env python3
"""Independently rewrite Chinese learning-performance questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-learning-performance"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","閱讀任務、證據與方法"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","文本理解、推論與限制"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","方法說明、資料與遷移"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量要求把閱讀任務拆成關鍵資訊、直接事實、推論、主旨、語氣、證據鏈、條件、受眾與結論限制；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("任務定位","閱讀通知「因雨取消操場活動，請各班改至教室完成分組討論」時，最先應標出？",["原因、取消的活動、替代地點與要做的事","通知用了幾個逗號","校長的個人興趣","所有班級過去的出席率"],"A","通知的行動資訊包括原因、原活動、替代地點與新的任務，能直接支持讀者下一步。","先判斷閱讀目的是採取行動，再抓原因、時間地點、對象與任務欄位。"),
 ("合理推論","短文寫「小芸帶傘出門，鞋底沾著泥，回家後先擦乾門口」；哪項是合理推論？",["她一定在雨中走了兩小時","她可能走過潮濕或泥濘的地方","她一定不喜歡晴天","她家門口永遠有積水"],"B","帶傘、泥鞋與擦門口支持曾經遇到潮濕或泥濘，但不能推成確定時間、喜好或長期狀態。","把直接線索列出，再用『可能』寫最小而合理的推論，避免補入文本沒有的細節。"),
 ("主旨整合","文章先描述減少一次性餐具，再說明清洗與借用制度，最後主張先試辦一個月；主旨最接近？",["只介紹餐具外觀","以制度配合減量目標，先試辦再評估可行性","清洗工作一定很容易","作者反對所有試辦"],"C","主旨需整合目標、制度與試辦主張，不能只摘一個環節或過度解讀作者態度。","依文章推進整理問題、方法、限制或評估與最後主張。"),
 ("語氣程度","「這項規定或許能改善秩序，但仍應先聽取晚歸學生的經驗」最接近？",["完全肯定規定有效","完全否定規定","保留可能性並要求納入受影響者經驗","宣布規定已經取消"],"D","或許表示不確定，但表示仍應聽取經驗，顯示作者支持先補充證據而非直接定案。","分別圈出可能性詞、轉折詞與行動要求，再判斷立場強度。"),
 ("證據鏈","要支持「圖書館延長開放值得試行」，哪組資料最能形成可檢查證據鏈？",["一位同學說很方便","延長前後借閱量、晚間使用者調查、成本與安全紀錄","社群按讚數最多的留言","只列出圖書館很安靜"],"A","前後數據、使用者調查、成本與安全紀錄分別檢查需求、效益與限制，能支持試行後評估。","把主張拆成需求、結果、成本與風險，為每一部分尋找直接且可追溯資料。"),
 ("條件例外","操作說明寫「確認電量後按下開關，若指示燈閃爍，先拔除電源並通知老師」；哪項是條件或例外？",["確認電量","按下開關","若指示燈閃爍時改採拔電與通知","操作說明的標題"],"B","若指示燈閃爍限定特殊情況，觸發不同處理方式，是條件與例外流程。","找出若、如果、除非等觸發詞，再把一般步驟與例外步驟分開。"),
 ("受眾改寫","把完整校務通知改成手機提醒時，哪項原則最重要？",["保留可行動的時間、地點、對象與要求，刪去不影響行動的長背景","把所有細節刪掉只留標題","加入未經證實的提醒","改成只有校方看得懂的術語"],"C","手機提醒需縮短但不能刪掉行動所需核心資訊，應依受眾與媒介重排內容。","先列不可省略的任務欄位，再調整句長、順序與顯示方式，最後回查資訊完整。"),
 ("限制檢查","主張「使用同一種筆記格式就能讓所有學生學得更好」，哪項資料最能檢查限制？",["格式的顏色是否漂亮","不同學習需求、科目與學生使用後的比較結果及訪談","筆記本封面材質","老師是否喜歡該格式"],"D","比較不同學生、科目與結果，才能檢查統一格式是否有適用條件與例外，避免全稱推論。","先找主張中的『所有』，再設計能涵蓋不同對象與情境的比較資料。"),
 ("樣本範圍","資料只來自一個班級的一週觀察，哪項結論最恰當？",["全校學生都一定如此","這個班級在該週的觀察呈現某種趨勢，仍需更多班級與時間驗證","這份資料完全沒有價值","可以直接預測下學期結果"],"A","結論應限制在一個班級與一週的資料範圍，若要推廣需增加樣本與時間。","先照資料的對象與期間寫結論，再檢查是否擅自擴大到全校或未來。"),
 ("方法遷移","要讓同學能依同樣方法重做一道閱讀題，解題說明應包含？",["只公布正確選項","題目任務、找證據、判斷推論範圍、排除選項與回讀檢核","只寫『仔細閱讀』","只描述自己的心情"],"B","可遷移的方法需讓讀者知道任務、證據、推論界線、排除與驗證步驟，才能在新題重做。","把個人直覺拆成可觀察步驟，附上判斷依據與檢查點，而不是只給答案。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與任務、直接線索、推論詞、條件、樣本或受眾線索。",f"拆解方法：把答案分成可觀察證據、推論範圍與可重做的步驟；本題核心是「{explanation}」",f"核對正解：選項 {target} 與資料能支持的結論範圍一致，且提供可執行的學習方法。","排除誘答：檢查是否把單一樣本推廣、忽略例外、刪掉必要資訊，或用空泛口號代替證據。","回讀驗證：假設換一篇文本或另一位學習者，確認方法仍能被重做並在關鍵處回到證據。"]
 item={"id":f"question-chinese-learning-performance-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-learning-performance"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究閱讀任務、證據、推論、方法說明、受眾與結論限制能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫學習表現題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-learning-performance-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")

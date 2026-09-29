#!/usr/bin/env python3
"""Independently rewrite Chinese language-arts domain questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; LESSON="lesson-chinese-language-arts-domain"
SOURCES=[
 ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf","新北市立石碇國中公開國文試題","語文理解、表達與查證"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf","高雄市立鹽埕國中公開國文段考","新聞、詩文與口語溝通"),
 ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf","國立卓蘭高中附設國中部公開課程與試題資料","篇章、媒介與修訂"),]
def refs(): return [{"url":u,"title":f"{t}；僅研究公開題型與能力方向，未複製原題。","year":"113-114","subject":"chinese","locator":l,"observedPattern":"公立學校國文評量結合公告、新聞、詩文、討論、資料查證、受眾調整、表格閱讀與作文修訂，要求在語境中整合理解與表達；本題採全新語料。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,l in SOURCES]
DATA=[
 ("公告目的","公告寫「週五前繳交閱讀紀錄，逾期請向導師說明」；溝通目的最恰當是？",["分享導師的個人故事","要求讀者在期限前完成行動，並說明逾期處理方式","描寫閱讀紀錄的外觀","評論學生的文學品味"],"A","公告提供期限、行動與例外處理，主要目的是讓讀者依規定完成任務。","先找公告的對象、期限、要求與後續處理，再判斷它要讀者做什麼。"),
 ("新聞證據","新聞標題說「全校都喜歡新午餐」，正文只調查 25 位學生；讀者應保持？",["立刻相信標題","只要 25 人就能代表所有人","要求查看樣本、調查方法與結論範圍，不把標題當全校事實","因為數字少就認定午餐難吃"],"B","樣本與全校的範圍不一致，讀者需查方法與限制，不能直接接受全稱標題。","比較主張範圍與資料範圍，再追問樣本代表性、問卷設計與原始結果。"),
 ("正式建議","向校長提出改善圖書館建議，哪個開頭最適合？",["校長您好，我覺得你們都做得不好。","根據近一個月借閱紀錄與學生問卷，我們建議先試辦晚間延長開放。","圖書館真的很棒，請您一定同意。","我今天想講很多事情，先從別的話題開始。"],"C","C以禮貌稱呼、資料依據與可評估的試辦主張開頭，適合正式建議。","先交代對象與資料，再提出範圍清楚、可試辦與可檢核的主張。"),
 ("詩句效果","「落日貼近山脊，歸鳥收起喧聲」若分析寫作效果，最應注意？",["只計算每句字數","光線位置與聲音變化共同營造傍晚安靜氛圍","證明山脊真的會移動","判斷作者的數學成績"],"D","貼近與收起把視覺、聲音變化連結，營造由喧鬧轉安靜的傍晚畫面。","先分辨意象與動詞，再說明它們如何共同形成畫面、節奏或情感。"),
 ("討論回應","討論校園雨具架時，一人提出使用數據，另一人提出安全疑慮；最佳回應是？",["只採用數據，安全不重要","只採用安全疑慮，完全不看使用需求","把兩者都記下，追問雨具架位置、容量與安全規格後再評估","請其中一人停止發言"],"A","好的討論要保留需求與風險，補充可查證的設計條件後比較方案。","先重述雙方觀點，再把抽象疑慮轉成位置、容量、動線與規格等可檢查問題。"),
 ("來源查證","網路文章主張某飲料能提升記憶力，卻沒有作者、日期或研究資料；下一步最適合？",["直接轉傳給同學","只看留言數量","尋找原始研究與可靠機構資料，先標記目前不可查證","買來喝一週就能證明"],"B","缺少作者、日期與研究資料時，應尋找可追溯來源並保留不確定，不以人氣或個人試喝代替研究。","先列出來源缺口，再找原始研究、發布機構、方法與限制。"),
 ("受眾提醒","把「雨天路滑，請減速慢行」改寫給低年級學生，哪項最合適？",["雨天路面摩擦係數降低，請調整步態速度。","雨天走路慢一點，看到水地繞開，並扶好欄杆。","你們不要再粗心大意了。","路滑，反正小心就好。"],"C","C保留安全行動，用低年級容易理解的詞與順序呈現，沒有責備或空泛提醒。","先列核心安全行動，再依年齡調整詞彙、句長與具體程度。"),
 ("表格與建議","說明文用表格列出三個月份回收量，文末提出減少垃圾建議；讀者應如何閱讀？",["只看文末建議，不看數據","先讀數據的時間與單位，再比較變化，最後檢查建議是否回應資料","只看最高數字就判斷所有月份","把表格當成裝飾"],"D","表格提供變化證據，文末建議需與數據及問題連結，先讀欄位與單位才能檢查推論。","先讀表頭、期間、單位與趨勢，再把建議與具體資料一一對照。"),
 ("作文修訂","作文段落順序是「提出結果、補充原因、再介紹問題」；最優先的修訂方向是？",["先增加華麗形容詞","先調整資訊順序，讓問題或背景先出現，再說原因與結果","只修改最後一個錯字","把所有段落刪成一句"],"A","資訊順序會影響讀者理解因果與問題背景，應先重組篇章，再處理局部文字。","先畫出問題、原因、證據與結果的關係，再調整段落順序與連接詞。"),
 ("成果整合","小組完成專題後，哪種成果最能同時展現理解、表達與反思？",["只交一張漂亮封面","展示研究問題、資料與結論，口頭說明選擇，並附上限制與下一步反思","只列出組員姓名","只背誦別人的報告"],"B","完整成果要呈現理解內容、清楚表達推理，並能說明限制與後續改進。","檢查成果是否同時回答做了什麼、如何知道、如何表達及還能怎麼改進。"),]
TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,(tag,prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
 target=TARGETS[i-1]; oi=ord(answer)-65; ti=ord(target)-65; correct=options[oi]; rest=[v for j,v in enumerate(options) if j!=oi]; options=rest[:ti]+[correct]+rest[ti:]
 steps=[f"讀題定位：圈出「{tag}」與對象、目的、證據、語氣、媒介或修訂線索。",f"整合語文功能：把理解、表達、查證與受眾需求放回完整情境；本題核心是「{explanation}」",f"核對正解：選項 {target} 能同時符合文本證據、溝通目的與表達分寸。","排除誘答：檢查是否把標題當事實、把個人感覺當證據、忽略受眾，或只修字詞不處理篇章。","回讀驗證：從讀者或聽眾角度重述，確認資訊可理解、主張可查核、行動可執行。"]
 item={"id":f"question-chinese-language-arts-domain-{i}","subject":"chinese","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"knowledgeIds":["kg-chinese-learning-focus"],"difficulty":"medium","answer":{"value":target,"explanation":explanation},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三所公立學校公開國文資料；只研究公告、新聞、詩文、討論、查證、受眾、表格與修訂的整合語文能力。","authoringNote":"依官方語文領域課綱、單元 KG 與三個公立學校公開來源，重新撰寫語文領域總論題；未複製原文、選項、篇章或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-13","lessonId":LESSON,"examPatternRefs":refs(),"solutionStrategy":strategy,"solutionSteps":steps}
 (OUT/f"question-chinese-language-arts-domain-{i}.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} independent questions for {LESSON}")

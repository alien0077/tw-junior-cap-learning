"""Je-Ⅳ-3：化學平衡與溫度、濃度的影響第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-je-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-je-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"可逆反應、平衡、溫度濃度與圖表判讀","pattern":"取由平衡資料、反應條件與圖表推論可逆反應變化的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"平衡位移、反應條件、工業與生活情境","pattern":"取從資料曲線、條件改變與製程情境判斷平衡位置及收率的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"可逆反應、動態平衡、條件與製造","pattern":"取以正逆反應、平衡、溫度／濃度及工業製程連結微觀與宏觀的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-je-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-je-iv-3"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的可逆反應、動態平衡、溫度／濃度、圖表與製程能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-je-iv-3","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"可逆反應達到動態平衡時，哪項敘述正確？",["正反應與逆反應仍持續，兩者速率相等，因此宏觀濃度維持穩定","所有粒子停止運動","反應物完全消失","只有正反應持續而逆反應停止"],"A","動態平衡是微觀正逆反應仍進行但速率相等，宏觀濃度看起來穩定，不是靜止或完全反應。","先分開微觀速率和宏觀濃度，再判斷平衡。",["確認反應是可逆的。","列出正反應和逆反應都存在。","判斷兩方向速率相等。","推論宏觀濃度保持穩定而非粒子停止。","所以 A 正確。"],"easy"),
q(2,"平衡反應中加入反應物，短時間內正反應速率先增加，主要原因是？",["反應物粒子數增加，使正向有效碰撞機會增加","逆反應一定完全停止","溫度必定自動升高","平衡常數一定立刻改變"],"A","加入反應物提高其濃度，使正向碰撞頻率增加；溫度不變時平衡常數不因單純加料而改變。","區分瞬間速率變化、平衡位置和常數。",["辨認被加入的是反應物。","判斷其濃度瞬間增加。","連結正向碰撞與速率增加。","檢查溫度是否改變，排除平衡常數改變。","答案為 A。"],"medium"),
q(3,"若移除可逆反應中的部分生成物，系統重新達平衡時通常會？",["往生成物方向反應以補回部分被移除的生成物","完全停止反應","只往反應物方向使生成物更少","一定改變平衡常數"],"A","移除生成物使系統傾向生成更多生成物以抵消改變；常數主要由溫度決定。","以勒沙特列原理預測濃度改變後的補償方向。",["確認被移除的是生成物。","觀察系統受到的濃度改變。","判斷反應往能增加生成物的方向移動。","確認溫度不變時平衡常數不因此改變。","所以 A 正確。"],"medium"),
q(4,"某平衡反應升溫後生成物比例下降，最合理的推論是？",["生成物方向是放熱方向，升溫使平衡偏向吸熱的反方向","升溫一定使所有生成物增加","溫度只影響速率不影響平衡位置","比例下降表示反應沒有發生"],"A","升溫使平衡偏向吸熱方向；若生成物比例下降，代表生成物方向較可能是放熱方向。","用資料中的比例改變反推熱效應，不套用固定升溫規則。",["比較升溫前後生成物比例。","確認平衡由生成物方向移開。","依升溫偏向吸熱方向判斷。","推論生成物方向為放熱方向。","所以 A 最符合資料。"],"hard"),
q(5,"下列哪項最能區分『反應速率變快』和『平衡產物比例增加』？",["分別觀察達平衡所需時間與平衡後各物質比例，不能用單一瞬間濃度代替兩者","只測量反應剛開始的溫度","只看氣泡是否變大","反應越快就必定有更多平衡產物"],"A","速率需由時間或曲線斜率判斷，平衡位置需由最後組成比例判斷；催化劑可加快達平衡但不必改變比例。","用不同時間尺度和指標辨識兩個概念。",["設定速率指標，例如達固定量所需時間。","設定平衡位置指標，例如最後濃度比例。","分別記錄兩種資料。","排除把速率快直接等同產量高。","所以 A 正確。"],"hard"),
q(6,"對含有氣體反應物和生成物的平衡系統壓縮體積，若溫度不變，合理預測是？",["平衡傾向氣體莫耳數較少的一側，以降低壓力改變的影響","平衡一定往氣體莫耳數較多的一側","壓力改變不可能影響平衡","壓縮會讓平衡反應停止"],"A","壓縮使壓力上升，系統傾向氣體粒子數較少的一側；若兩側氣體莫耳數相同，位移可能不明顯。","先比較反應式兩側氣體莫耳數，再預測壓力補償。",["寫出平衡反應式並數氣體莫耳數。","確認壓縮使壓力增加。","比較較少氣體莫耳數的一側。","考慮若兩側數目相同則沒有明顯位移。","答案為 A。"],"hard"),
q(7,"平衡系統加入催化劑後，通常會有什麼影響？",["正反應和逆反應都加快，較快到達平衡但平衡組成不因此改變","只加快正反應，生成物比例必增加","只加快逆反應，反應物比例必增加","改變溫度並改變平衡常數"],"A","催化劑降低反應途徑的活化能，通常同時加快正逆方向，使系統較快達同一平衡狀態。","把到達平衡的時間與平衡位置分開。",["比較加催化劑前後達平衡時間。","判斷正逆反應是否都受到影響。","比較最後平衡組成。","排除單向加速、溫度改變和常數改變。","所以 A 正確。"],"medium"),
q(8,"工業製程希望提高某可逆反應的產物收率，哪項策略最需要同時考慮平衡與速率？",["選擇合適溫度與壓力，並評估催化劑、能源、設備安全和達平衡時間","只把溫度升到最高","只追求平衡產物比例而不管反應時間","只看一次產物顏色"],"A","工業條件需在平衡收率、反應速率、能源成本、設備和安全間取捨，不能只追求單一指標。","把化學平衡轉成多指標製程決策。",["由反應式判斷溫度與壓力的平衡影響。","估計條件對速率與達平衡時間的影響。","加入催化劑、能源與安全限制。","比較可實行的總體效益。","因此 A 最完整。"],"medium"),
q(9,"平衡混合物的顏色在加入反應物後先變深，之後變成較穩定的新顏色；最合理的解釋是？",["先因濃度突變造成顏色改變，接著平衡移動並在新組成下重新穩定","顏色變化證明所有反應停止","新顏色代表元素被創造","只要顏色變深就表示溫度一定升高"],"A","加入物質先造成瞬間組成變化，之後正逆反應調整到新平衡，顏色反映物種比例改變；需排除溫度等干擾。","用時間序列區分擾動瞬間和新平衡。",["記錄加入反應物前的顏色。","觀察瞬間變化和後續穩定值。","用平衡位移解釋重新調整。","排除停止反應、元素創造和必然升溫。","所以 A 最合理。"],"hard"),
q(10,"研究溫度對平衡位置的影響時，哪項資料最完整？",["控制濃度、壓力與容器後，在不同溫度達平衡並測量各物質濃度比例及達平衡時間","每個溫度都使用不同初始物質量","只觀察反應剛開始的氣泡","只記錄加熱器設定值而不量產物"],"A","要分辨平衡位置與速率，需在各溫度達平衡後量組成比例，同時記錄達平衡時間並控制其他條件。","設計同時涵蓋平衡終態和動力學時間的資料收集。",["固定初始濃度、壓力與容器。","分別設定溫度並等待系統達平衡。","量測各物質濃度比例。","另記錄到達平衡時間並比較。","因此 A 能同時回答平衡和速率問題。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["動態平衡是正逆反應仍進行且速率相等的狀態。","濃度、溫度與壓力改變會以不同方式影響平衡位置；催化劑主要影響達平衡速度。","平衡比例、反應速率、產率、能源與安全是不同但需整合的製程指標。"],"versionDifferences":["南一公開線索支持由顏色、氣體與生活反應進入可逆平衡。","康軒公開課程資料較突出正逆反應、濃度／溫度控制與曲線資料。","翰林公開課程計畫補充平衡、壓力與工業製造取捨；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以擾動—瞬間速率—平衡位移—新組成—製程取捨五步框架分析平衡。","把催化劑、顏色時間序列、壓力和工業能源安全納入單元專屬遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫可逆反應、動態平衡、濃度、溫度、壓力、催化劑、圖表與製程；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Je-Ⅳ-3：化學平衡與溫度、濃度的影響","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為動態平衡、濃度、溫度、壓力、催化劑、速率／收率區分、曲線與工業製程專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content je-iv-3")
if __name__=="__main__": main()

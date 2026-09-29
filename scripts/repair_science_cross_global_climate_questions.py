import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'questions/science'
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學公開自然科評量","year":"113-114"},
 {"url":"https://www.cp.ptc.edu.tw/storage/134523/134523_114_B-23_7A.pdf?1774770497=","title":"屏東縣新園國中公開自然領域教學計畫","year":"114"},
 {"url":"https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTmw4Mk9UazRNell4WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSKOSSICDGB040WSHDNPMLOOPOUSUSKLDGA4A4FCVW0021JH20B0RKZWOO30LKKKQOJCTWICZTA1LKQPSWYWKORK00POPO","title":"新北市立泰山國中公開自然領域課程計畫","year":"114"},
]
DATA=[
("小島國家面臨海平面上升時，哪項組合最能降低社區風險？",["沿岸預警、避難規劃、濕地保護與必要的防護工程","只增加冷氣使用","只等待災害發生後修復","刪除潮位資料"],"A","氣候風險需要結合預警、暴露管理、生態緩衝與工程調適，並依地區條件規劃。","從預防、應變、生態系與工程四個面向檢查。"),
("全球平均溫度上升可能造成冰雪融化與海水熱膨脹，兩者共同影響哪項？",["海平面上升","地球自轉停止","月球消失","所有地區降雨相同"],"A","陸冰融化增加海水量，海水受熱膨脹，兩者都會促成海平面上升。","辨認不同機制但相同結果的累加效應。"),
("氣候變遷對農業的衝擊不能只看平均溫度，還應加入哪些資料？",["降雨時序、乾旱與熱浪頻率、作物需水量及土壤條件","只看城市人口","只看月球相位","只看單日風向"],"A","農業風險與水分、極端事件、作物生理和土壤保水等因素共同相關。","把氣候危害與作物暴露、脆弱度連結。"),
("同樣面對洪水，低窪且排水不足的社區風險較高，主要因為？",["暴露與脆弱度較高","該社區必定沒有降雨","洪水在低處不會流動","風速決定所有風險"],"A","風險會受危害、暴露人口與基礎設施脆弱度共同影響，低窪排水不足會提高衝擊。","分開危害本身與受影響對象的條件。"),
("各國共同減少溫室氣體排放，最能對應氣候行動的哪個層次？",["減緩全球氣候變遷的成因","只處理單一家庭室內溫度","調整潮汐週期","避免所有自然災害"],"A","減少全球溫室氣體排放是在降低氣候變遷的驅動因素，屬於減緩。","辨認措施是否作用於全球成因，而非局部衝擊。"),
("若不同國家歷史排放量與受災能力差異很大，設計政策時應加入哪項考量？",["公平性與責任分配","只比較國土面積","忽略弱勢群體","只採用單一國家資料"],"A","氣候政策需同時考量歷史責任、能力差異、受影響族群與資源分配，才能降低不平等。","把科學風險與社會公平一併納入決策。"),
("全球氣候資料顯示平均值上升，但某地單一年份偏冷，最合理的說法是？",["單年波動不會否定長期趨勢，需看足夠長的序列","全球暖化因此已停止","單一地點即可代表全球","平均值一定是錯的"],"A","短期自然變異可能造成單年偏冷，判斷氣候趨勢需使用長期、多地資料。","區分天氣年際變化與長期氣候訊號。"),
("在全球氣候模型比較中，使用不同排放情境的主要目的為何？",["呈現不同政策與排放路徑下的可能結果","保證某一預測必然發生","避免使用觀測資料","把不確定性刪除"],"A","情境不是單一命運，而是依排放與社會假設推估可能範圍，能協助規劃。","先看情境假設，再解讀結果範圍與限制。"),
("城市以樹蔭、綠屋頂和透水鋪面降低熱島效應，這些措施共同作用於？",["降低地表吸熱並增加遮蔭與蒸散","增加化石燃料燃燒","使太陽輻射消失","讓所有降雨停止"],"A","植被遮蔭、蒸散與透水面可改變熱收支與地表水分，降低局部熱島。","將措施連結到熱收支、水分與城市暴露。"),
("評估全球氣候調適方案時，哪種證據最能支持長期決策？",["多地長期監測、情境比較、成本效益與受影響族群回饋","一次活動照片","只看宣傳標語","刪除不利資料"],"A","長期監測與多種證據能檢查成效、成本與公平影響，並支援後續修正。","建立時間序列、替代情境、成本與社會回饋的交叉證據。"),
]
for i,(prompt,opts,ans,ex,strategy) in enumerate(DATA,1):
 p=D/f'question-science-content-cross-global-climate-adaptation-{i}.json'; old=json.loads(p.read_text()); text=opts[ord(ans)-65]
 old.update({'prompt':prompt,'options':[{'id':chr(65+j),'text':x} for j,x in enumerate(opts)],'answer':{'value':ans,'explanation':ex+f' 正確答案為選項 {ans}：「{text}」。'},'solutionStrategy':strategy,'solutionSteps':['定位概念：圈出全球氣候變遷題目的危害、暴露、脆弱度、減緩或調適。','整理證據：分開全球趨勢、地方差異、情境假設與政策公平性。',f'套用原理：{ex}',f'排除干擾：檢查尺度、因果鏈、不確定性與資料完整性，正確選項是「{text}」。',f'最後回查：答案「{text}」符合題幹，沒有把局部或單次資料誇大成全球必然結論。'],'reviewStatus':'draft','updatedAt':'2026-09-09','examPatternRefs':[dict(s,subject='science',locator='climate data interpretation, risk, mitigation, adaptation, and evidence evaluation',observedPattern='公立學校公開自然科資料以氣候趨勢、資料尺度、風險與環境決策評量推理；本題僅取能力方向。',reuseDecision='pattern-only',status='recorded',locatorLevel='paper') for s in SOURCES]})
 p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(f'rewrote {len(DATA)} questions')

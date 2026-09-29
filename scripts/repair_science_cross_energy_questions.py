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
("太陽能板供電給電動車時，主要能量轉換順序為何？",["輻射能轉電能，再轉動能並伴隨熱能","化學能直接變質量","聲能變光能且沒有損耗","熱能消失"],"A","太陽能板把輻射能轉成電能，馬達再把電能轉成車輪的動能，過程常有熱散失。","依能量流向從來源、裝置到輸出排列。"),
("水力發電的能量來源主要是水的哪種能量？",["重力位能轉成動能，再由發電機轉成電能","只有聲能","化學能直接變成核能","光能必定先變成電能"],"A","高處水的重力位能在下落時轉為動能，推動渦輪與發電機產生電能。","找出水位差、流動與發電機的先後關係。"),
("比較兩種燈具效率時，若輸入電能相同，最合理的輸出指標是？",["有用光能占輸入能量的比例","燈具外殼顏色","包裝大小","只看通電時間"],"A","效率應比較有用輸出能量與輸入能量的比例，不能只看外觀或使用時間。","先定義有用輸出，再用輸出／輸入比較。"),
("電池使用後電壓下降，最合理的說法是？",["化學能可提供的能量逐漸減少，仍需考慮電池狀態與負載","能量完全消失","電流一定變成聲音","電池質量必定變成零"],"A","電池內部反應物與內阻等狀態會影響可輸出的電壓與能量，不能說能量消失。","把能量轉換與電池實際狀態分開判斷。"),
("若要比較不同燃料的發電環境影響，哪組資料最完整？",["發電量、排放、用水、土地與燃料生命週期","只看火焰顏色","只看燃料價格一天變化","只問操作者感覺"],"A","能源評估需同時考量有用輸出與生命週期造成的排放、資源及土地影響。","建立多面向指標，不用單一特徵代表整體表現。"),
("摩擦煞車使車輪停止時，機械能主要轉換成哪種形式？",["內能與少量聲能","消失不見","只變成質量","變成月光"],"A","摩擦把車輪與路面的機械能轉為內能，並可能產生聲音。","追蹤摩擦前後的能量去向，注意能量守恆。"),
("探究太陽能板傾角對輸出功率的影響時，哪項應固定？",["光源強度、照射時間與面板面積","只固定輸出功率","每次換不同面板且不記錄","同時改變傾角與光源距離"],"A","只改變傾角並固定光源、時間、面板與量測方法，才能公平比較功率。","分辨操縱變因、依變因與控制變因。"),
("電網尖峰時段鼓勵移轉用電，最直接的能源管理目的為何？",["降低尖峰供電壓力並提高系統利用率","增加所有設備待機耗電","使能源沒有任何損耗","讓發電需求完全消失"],"A","把部分需求移到離峰可降低尖峰負載，改善發電與輸配電系統的使用效率。","判斷措施作用在需求時間與系統負載。"),
("蓄電池充電時，輸入的電能主要儲存成哪種形式？",["化學能","只有光能","聲音能","重力位能必定增加"],"A","充電讓電池內部發生可逆化學反應，將部分電能儲存為化學能。","區分充電時的輸入、儲存形式與放電時的輸出。"),
("若某能源裝置輸入 1000 J、輸出有用能量 700 J，其效率為何？",["70%","30%","100%","170%"],"A","效率＝有用輸出／輸入×100%＝700÷1000×100%＝70%。","先寫效率公式，再代入同單位能量並檢查不超過 100%。"),
]
for i,(prompt,opts,ans,ex,strategy) in enumerate(DATA,1):
 p=D/f'question-science-content-cross-energy-resources-{i}.json'; old=json.loads(p.read_text()); text=opts[ord(ans)-65]
 old.update({'prompt':prompt,'options':[{'id':chr(65+j),'text':x} for j,x in enumerate(opts)],'answer':{'value':ans,'explanation':ex+f' 正確答案為選項 {ans}：「{text}」。'},'solutionStrategy':strategy,'solutionSteps':['定位概念：圈出能量與能源題目的來源、轉換、輸出或效率量。','整理證據：分開輸入能量、有用輸出、損耗、控制變因與環境代價。',f'套用原理：{ex}',f'排除干擾：依能量守恆、效率公式與系統邊界檢查，正確選項是「{text}」。',f'最後回查：答案「{text}」符合題幹，沒有把損耗誤寫成能量消失。'],'reviewStatus':'draft','updatedAt':'2026-09-09','examPatternRefs':[dict(s,subject='science',locator='energy conversion, efficiency, systems, and investigation design',observedPattern='公立學校公開自然科資料以能量流程、效率計算與變因控制評量資料判讀；本題僅取能力方向。',reuseDecision='pattern-only',status='recorded',locatorLevel='paper') for s in SOURCES]})
 p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(f'rewrote {len(DATA)} questions')

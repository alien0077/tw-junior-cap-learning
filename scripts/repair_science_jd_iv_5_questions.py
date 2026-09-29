import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
 ("清潔劑標示『強鹼、具腐蝕性』，使用時最適當的做法是？", ["依標示戴護目鏡與手套、保持通風，不與其他清潔劑任意混合", "用手直接測試滑不滑，再決定是否安全", "把它與漂白水混合以增強效果", "把剩餘藥液倒入飲料瓶方便攜帶"], "A", "強鹼和腐蝕性物質可能傷害皮膚與眼睛，也可能與其他藥品產生危險反應；應遵守標示、使用防護具並妥善保存。", "先看危害標示，再選擇能降低接觸與混合風險的操作。"),
 ("水壺內的碳酸鈣水垢可用檸檬酸清除。這個生活應用主要利用哪種概念？", ["酸與碳酸鹽反應可使水垢溶解並產生氣體等反應現象", "鹼與水垢一定會放出氧氣", "檸檬酸會把水垢變成金屬", "只要加熱就能使所有水垢消失"], "A", "水垢主要含碳酸鈣，酸可與碳酸鹽反應，使固體溶解並可能產生二氧化碳；使用時仍要依產品說明並充分沖洗。", "辨認水垢成分與酸的反應類型，不把清潔效果誤說成單純加熱或物理擦除。"),
 ("土壤酸化時，農業上可能施用石灰資材調整酸鹼性。下列說法最合理的是？", ["鹼性石灰可部分中和酸性土壤，但用量仍需依檢測與專業建議", "石灰越多越好，任何土壤都不必檢測", "石灰會把酸性土壤永久變成中性", "酸化土壤只能用強酸處理"], "A", "石灰等鹼性材料可與酸性物質反應，但土壤條件、作物與用量不同，應先檢測並依建議施用，避免過度改變環境。", "先判斷中和方向，再加入劑量、土壤檢測與副作用等實務條件。"),
 ("不小心把強酸濺到皮膚，第一個正確處置通常是？", ["立即用大量流動清水沖洗並依校內或醫療安全流程求助", "立刻用強鹼液體自行中和", "用紙巾用力擦拭後繼續實驗", "先用嘴吹乾再觀察是否疼痛"], "A", "強酸接觸皮膚時應盡快以大量流動清水沖洗並求助，不能自行用另一種腐蝕性物質中和，以免反應放熱或增加傷害。", "安全題先排除會增加接觸、摩擦或放熱的作法，再選立即稀釋移除並求助的措施。"),
 ("若誤食強酸或強鹼，哪項做法較安全？", ["不要自行催吐或飲用另一種化學品，立即聯絡緊急醫療並攜帶產品資訊", "喝大量醋或清潔劑自行中和", "立刻催吐直到沒有不適", "先等待幾小時再決定是否求助"], "A", "誤食腐蝕性物質可能再次傷害食道，不能自行催吐或用另一種化學品中和；應立即求助並提供產品名稱與成分。", "區分皮膚暴露與誤食情境，遵循急救與醫療指示，不把課堂中和示範套用到人體。"),
 ("胃酸過多時，市售制酸劑可能含弱鹼性成分。下列說法最恰當的是？", ["它可暫時中和部分胃酸，但應依標示使用，反覆不適仍需就醫", "制酸劑越多越能保證治癒所有胃病", "制酸劑是強酸，所以會增加胃酸", "只要感到不適就把不同藥物混合服用"], "A", "制酸劑可降低部分胃酸造成的不適，但不能取代病因診斷；用藥需遵守標示或醫療人員指示。", "先判斷酸鹼中和方向，再加上藥品劑量、適用範圍與就醫界線。"),
 ("螞蟻叮咬處感到刺痛，若確認是輕微局部反應，哪項觀念較合理？", ["可依可靠醫療建議處理，不能只因酸鹼概念就任意塗抹化學藥品", "一定要用強鹼直接灌入傷口", "用濃酸可以保證立刻止痛", "任何叮咬都應自行混合酸鹼液體"], "A", "生活中的酸鹼中和可作為概念例子，但人體處置仍要考慮傷口、過敏與毒性，應依醫療建議，避免自行使用腐蝕性物質。", "把課本化學模型與真實健康安全分開，優先判斷是否需要專業處置。"),
 ("檢查未知清潔液時，哪種方法最適合初步判斷其酸鹼性？", ["依安全規範取少量樣品，用適當指示劑或 pH 工具測量，避免直接接觸", "用舌頭品嚐", "把所有清潔液混在一起觀察", "用手觸摸後以滑感判斷強度"], "A", "指示劑或 pH 工具能提供酸鹼性的可觀察證據；未知清潔液可能腐蝕或有毒，不能以品嚐、觸摸或混合測試。", "選擇可量測、少量、低接觸且可重複的檢驗方法。"),
 ("家中同時使用酸性除垢劑與含漂白成分的清潔劑，最需要避免什麼？", ["任意混合，因為可能產生有害氣體或危險反應", "閱讀標示並分開使用", "保持通風並依說明沖洗", "使用後將容器清楚標示並妥善收存"], "A", "不同清潔劑混合可能產生有害氣體或劇烈反應，應遵守標示、分開使用並保持通風，不能用化學直覺自行配製。", "先辨識產品成分與警語，再排除混合未知化學品的高風險行為。"),
 ("將酸鹼鹽類生活應用融入校園宣導，哪種做法最能兼顧科學與安全？", ["比較產品標示、pH 或指示劑資料與正確處置流程，不讓學生直接接觸危險藥品", "讓學生以氣味猜測化學品", "用強酸強鹼競賽誰反應最快", "只記住酸鹼名稱，不討論危害與廢液處理"], "A", "生活應用學習應把酸鹼性、用途、危害標示、個人防護與廢液處理連在一起，避免以直接接觸或刺激性操作取代證據。", "同時檢查概念理解、證據取得與安全流程，選出可教學又可控風險的設計。"),
]
PUBLIC_REFERENCES = [
 {"url":"https://www.tkgsh.tn.edu.tw/uploads/16660625035014NkoDaeu.pdf","title":"臺南市立臺南女子高級中學國中部教育會考模擬考公開試題","year":"111"},
 {"url":"https://school.tc.edu.tw/open-message/193524/get-file/60efac0478be9779be7cde4a.pdf","title":"臺中市立三光國民中學八年級自然科公開補行評量題庫","year":"109"},
 {"url":"https://schoolweb.tn.edu.tw/~yhjh_www/uploads/tadnews/tmp/1152/%E5%85%AB%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A3%9C%E8%80%83%E9%A1%8C%E5%BA%AB.pdf","title":"臺南市立鹽行國民中學八年級自然科公開補考題庫","year":"111"},
]
PUBLIC_NOTE_REFERENCES = [
 {"url":"https://market.cloud.edu.tw/resources/web/1801577","title":"教育雲公開教學資源：進入實驗室～安全是一種基本態度（臺北市立仁愛國中）","year":"2019"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject":"science","locator":ref["title"],"observedPattern":"研究公立學校公開試題中的酸鹼鹽生活應用、產品標示、指示劑與危險處置能力方向；未複製原題文字、選項、圖表或答案。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"})
for ref in PUBLIC_NOTE_REFERENCES:
    ref.update({"subject":"science","locator":ref["title"],"observedPattern":"補充實驗室安全教學脈絡；未作為公開試題來源，未複製原文。","reuseDecision":"context-only","status":"recorded","locatorLevel":"resource"})
TARGET_ANSWERS = "ABCDBCDACB"
for i,(prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
    path=ROOT/"questions/science"/f"question-science-content-jd-iv-5-{i}.json"
    item=json.loads(path.read_text()); item.pop("publicNoteRefs", None); correct=options[ord(answer)-65]
    target=TARGET_ANSWERS[i-1]
    distractors=[text for option_index,text in enumerate(options) if option_index != ord(answer)-65]
    position=ord(target)-65
    arranged=distractors[:position]+[correct]+distractors[position:]
    item.update({"prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(arranged)],"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}：「{correct}」。"},"solutionStrategy":strategy,"solutionSteps":["圈出酸、鹼、鹽、用途、危害標示與處置情境。","先判斷化學概念，再檢查是否符合產品標示與人體／環境安全。",f"套用原理：{explanation}",f"排除任意混合、直接接觸或過度承諾療效的選項，答案為「{correct}」（選項 {target}）。","回查操作是否可由可靠資料支持，並把課堂模型與真實安全流程分開。"],"examPatternRefs":PUBLIC_REFERENCES,"reviewStatus":"draft"})
    path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n")
print(f"rewrote {len(DATA)} questions")

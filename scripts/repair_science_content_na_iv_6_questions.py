import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-na-iv-6"
KG = "kg-science-content-na-iv-6"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學公開自然科評量", "year": "113-114"},
    {"url": "https://www.cp.ptc.edu.tw/storage/134523/134523_114_B-23_7A.pdf?1774770497=", "title": "屏東縣新園國中公開自然領域教學計畫", "year": "114"},
    {"url": "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTmw4Mk9UazRNell4WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSKOSSICDGB040WSHDNPMLOOPOUSUSKLDGA4A4FCVW0021JH20B0RKZWOO30LKKKQOJCTWICZTA1LKQPSWYWKORK00POPO", "title": "新北市立泰山國中公開自然領域課程計畫", "year": "114"},
]

def refs():
    return [{**s, "subject": "science", "locator": "environment, sustainability, evidence comparison, and natural-science data reasoning", "observedPattern": "公開自然科評量與課程資料常以資源、環境變化、污染、保育與人類活動的資料情境測量變因、證據、尺度與推論；本題只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for s in SOURCES]

def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {"id": f"question-science-content-na-iv-6-{i}", "subject": "science", "type": "single-choice", "prompt": prompt, "options": [{"id": k, "text": v} for k, v in options.items()], "knowledgeIds": [KG], "difficulty": difficulty, "answer": {"value": answer, "explanation": explanation}, "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公開自然科試題／課程資料僅供人類發展、環境保護與科學資料判讀能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開自然科資料的能力方向獨立改寫；題幹、選項、解析、資料與五步解法均為原創，待第二輪 AI／Terra 內容複核。"}, "reviewStatus": "draft", "updatedAt": "2026-09-12", "lessonId": LESSON, "examPatternRefs": refs(), "solutionStrategy": strategy, "solutionSteps": steps}

Q = [
make(1, "A town plans to build a factory beside a river. Which evidence should be compared before approval?", {"A": "Jobs and products, plus water use and possible pollutant discharge.", "B": "Only the factory's paint color.", "C": "Only the number of trucks on the first day.", "D": "The factory name without any measurements."}, "A", "A compares development benefits with resource use and environmental risk, which is necessary for a balanced decision.", "把發展利益與環境成本放在同一系統邊界內比較，不能只選單一好處。", ["確認情境同時有 factory development 與 river protection。", "列出可能的 benefit、water use 與 pollutant evidence。", "檢查 A 是否包含經濟與環境兩側資料。", "排除 B、C、D，因為它們只看外觀、單日或沒有測量。", "選 A，確認決策基於可比較的多面向證據。"], "medium"),
make(2, "A city replaces a grass field with a parking lot. Which change is most reasonable to predict during heavy rain?", {"A": "More surface runoff and less water soaking into the ground.", "B": "More sunlight being produced underground.", "C": "The parking lot will create new forests immediately.", "D": "Rainfall will stop before reaching the city."}, "A", "Impermeable pavement reduces infiltration and can increase surface runoff during heavy rain.", "從地表材料改變推理入滲與逕流，避免把相關環境結果誇大到沒有物理依據。", ["找出 grass field 變成 parking lot 的變因。", "判斷鋪面較不透水，入滲能力下降。", "把降雨條件與 surface runoff 增加連結。", "排除 B、C、D，因為它們與水循環或時間尺度不符。", "選 A，確認預測由材料與水流證據支持。"], "medium"),
make(3, "A recycling program reports that mixed waste fell from 1,000 kg to 700 kg per month, while total waste stayed at 1,500 kg. What is supported?", {"A": "Mixed waste decreased, but total waste did not decrease.", "B": "All waste disappeared.", "C": "Total waste fell to 700 kg.", "D": "Recycling caused every household to produce less waste."}, "A", "The data show mixed waste fell by 300 kg, while total waste remained 1,500 kg; broader household causation is not established.", "分開讀不同指標與數值，避免把一項下降誤當成總量下降或因果已證明。", ["列出 mixed waste 的前後數值。", "確認 total waste 仍是 1,500 kg。", "用數據支持 mixed waste decreased 的結論。", "排除 B、C、D，因為它們錯讀總量或超出資料能推論的範圍。", "選 A，確認結論同時保留兩個指標。"], "hard"),
make(4, "A forest plan protects a wetland while allowing visitors on a marked boardwalk. Which idea does this best demonstrate?", {"A": "Human use can be planned to reduce damage to a sensitive habitat.", "B": "Any human visit always destroys every ecosystem.", "C": "Wetlands have no value to organisms.", "D": "Protection requires removing all observation activities."}, "A", "A boardwalk concentrates movement and can reduce trampling while allowing limited public use and observation.", "從設計措施與棲地敏感性推論取捨，不把保護與人類使用視為只能二選一。", ["找出 wetland、marked boardwalk 與 visitor use 三項條件。", "推論集中動線可降低踩踏範圍。", "檢查 A 是否保留使用與減少傷害兩個面向。", "排除 B、C、D，因為它們是絕對化或否定生態價值。", "選 A，確認結論符合管理措施的功能。"], "medium"),
make(5, "A factory installs a filter and measures river oxygen before and after treatment. Why is the before-after comparison useful?", {"A": "It checks whether the treatment is associated with a change in water quality under the measured conditions.", "B": "It proves the filter will solve every pollution problem everywhere.", "C": "It removes the need to measure any other variable.", "D": "It shows oxygen has no relation to aquatic life."}, "A", "Before-after measurements provide evidence about change under the tested conditions, but they do not justify universal claims.", "說明比較能支持的範圍，並保留控制條件與外推界線。", ["確認測量對象是 treatment 前後的 river oxygen。", "將比較結果連到 water quality change。", "檢查 A 的 under measured conditions 保留證據界線。", "排除 B、C、D，因為它們過度外推、取消控制或否定指標意義。", "選 A，確認結論既有證據又不誇大。"], "hard"),
make(6, "A new road reduces travel time but cuts through a wildlife corridor. Which additional indicator would best assess the environmental cost?", {"A": "Changes in animal crossings and road-kill records.", "B": "The road's lane paint brightness only.", "C": "The mayor's speech length.", "D": "The number of construction photographs."}, "A", "Animal crossings and road-kill records directly measure effects on movement and survival in the corridor.", "選與生態機制直接相連的指標，再與交通利益並列評估。", ["確認 road 的 benefit 是 travel time reduction。", "找出 wildlife corridor 受影響的生態過程。", "選能測量 movement 與 survival 的 crossing、road-kill records。", "排除 B、C、D，因為它們不能反映動物影響。", "選 A，確認指標能補足發展效益的環境面。"], "medium"),
make(7, "A community compares solar panels and diesel generators. Which question best supports a life-cycle comparison?", {"A": "What are the energy use, emissions, materials, and disposal impacts from production to end of use?", "B": "Which device has the most attractive shape?", "C": "Which advertisement uses larger letters?", "D": "Which one was mentioned first in a speech?"}, "A", "A life-cycle comparison includes impacts from production through use and disposal, not only operation.", "先界定生命週期邊界，再比較各階段的資源與排放證據。", ["圈出 solar panels 與 diesel generators 的比較任務。", "辨認 life-cycle 必須涵蓋 production、use 與 disposal。", "檢查 A 還包含 energy、emissions 與 materials。", "排除 B、C、D，因為外觀、廣告與發言順序不是生命週期證據。", "選 A，確認比較範圍完整。"], "hard"),
make(8, "A stream survey finds fewer insect species downstream of a construction site, but water temperature was also higher there. What is the best conclusion?", {"A": "The pattern suggests a relationship, but temperature and other factors must be controlled before claiming one cause.", "B": "Construction alone definitely caused the loss.", "C": "Insects cannot live in any stream.", "D": "The survey proves water temperature never matters."}, "A", "Two conditions changed downstream, so the observation suggests an association but does not isolate construction as the single cause.", "依據多變因資料保留因果界線，指出需要控制或比較的條件。", ["列出 insect diversity、construction 與 temperature 三項資訊。", "確認下游同時存在兩個可能變因。", "判斷資料能支持 pattern，但不能單獨證明唯一因果。", "排除 B、C、D，因為它們過度確定或否定普遍現象。", "選 A，確認結論符合研究設計限制。"], "hard"),
make(9, "A city wants economic growth and cleaner air. Which policy combines development with environmental protection?", {"A": "Support efficient public transit and require emission monitoring for new industries.", "B": "Build more factories without measuring emissions.", "C": "Ban every form of transportation immediately.", "D": "Ignore air data if employment rises."}, "A", "Efficient transit can support mobility while emission monitoring makes industrial environmental costs measurable and manageable.", "找同時處理發展需求與空氣證據的政策，而不是絕對禁止或忽略資料。", ["確認目標有 economic growth 與 cleaner air。", "檢查 A 的 transit support 與 emission monitoring。", "說明前者處理移動效率，後者追蹤污染風險。", "排除 B、C、D，因為它們無監測、絕對禁止或忽視空氣資料。", "選 A，確認政策把發展與保護放在同一決策框架。"], "medium"),
make(10, "A village restores a mangrove area and later records more young fish near the roots. Which evidence would strengthen the conclusion that restoration helped?", {"A": "Compare fish counts with earlier records and a similar unrestored site under similar sampling effort.", "B": "Count fish only once after restoration.", "C": "Ask whether residents like the mangrove color.", "D": "Use a different net and different sampling time every survey."}, "A", "Earlier data and a comparable control site with similar sampling effort help distinguish restoration effects from timing or measurement changes.", "強化證據要有前後比較、對照地點與一致取樣，而不是單次觀察。", ["確認觀察是 restoration 後 young fish 增加。", "列出需要排除的替代解釋：季節、地點與取樣差異。", "檢查 A 包含 earlier records、unrestored site 與 similar effort。", "排除 B、C、D，因為它們沒有比較、只看偏好或改變測量條件。", "選 A，確認證據能更有力地支持因果推論。"], "hard"),
]

LOCALIZED = [
    ("城鎮計畫在河流旁興建工廠，核准前應比較哪些證據？", ["A 就業與產品效益，以及用水量和可能排放污染物的資料", "B 只看工廠油漆的顏色", "C 只看第一天進出的卡車數量", "D 只看工廠名稱，不做任何測量"], "A", "合理決策要同時比較發展效益、資源使用與環境風險，不能只看單一好處或外觀。"),
    ("城市把草地改成停車場後，大雨期間最合理的預測是什麼？", ["A 地表逕流增加，雨水入滲地下的量減少", "B 地下會產生更多陽光", "C 停車場會立刻形成新的森林", "D 雨水在到達城市前會停止降落"], "A", "不透水鋪面會降低入滲能力，因此降雨時較可能增加地表逕流；這是由地表材料與水循環的關係推得。"),
    ("回收計畫顯示每月混合垃圾由 1000 公斤降至 700 公斤，但總垃圾量仍是 1500 公斤。哪個結論受到資料支持？", ["A 混合垃圾減少，但總垃圾量沒有減少", "B 所有垃圾都消失了", "C 總垃圾量降至 700 公斤", "D 回收使每個家庭都產生較少垃圾"], "A", "資料只顯示混合垃圾減少 300 公斤，總量仍為 1500 公斤；不能據此推論垃圾消失或已證明每戶的因果。"),
    ("森林計畫保護濕地，同時讓遊客使用劃定的木棧道。這最能說明什麼概念？", ["A 妥善規劃人類使用，可以減少對敏感棲地的傷害", "B 任何人類進入都一定會摧毀所有生態系", "C 濕地對生物沒有價值", "D 保護環境必須移除所有觀察活動"], "A", "木棧道集中行走路線，可減少踩踏範圍，讓有限度的參訪與棲地保護同時存在；其他選項是絕對化說法。"),
    ("工廠安裝過濾器，並測量處理前後河水的溶氧量。為什麼這項前後比較有用？", ["A 可檢查在測量條件下，處理措施是否伴隨水質變化", "B 可證明這個過濾器能解決世界各地所有污染", "C 從此不必測量任何其他變因", "D 可證明溶氧與水中生物沒有關係"], "A", "前後測量能提供特定條件下的變化證據，但不能把單一處理結果無限制外推到所有污染問題。"),
    ("新道路縮短通勤時間，卻穿越野生動物廊道。哪個額外指標最能評估環境成本？", ["A 動物穿越次數的變化與路殺紀錄", "B 只看道路標線的明亮程度", "C 市長演講的長度", "D 施工照片的張數"], "A", "穿越紀錄與路殺數量直接反映動物移動與存活受到的影響，能補足交通效益以外的環境證據。"),
    ("社區比較太陽能板與柴油發電機，哪個問題最能支持生命週期比較？", ["A 從製造、使用到淘汰，能源、排放、材料與處置各造成什麼影響", "B 哪個裝置外形最好看", "C 哪則廣告使用較大的字", "D 哪個在演講中先被提到"], "A", "生命週期要涵蓋生產、使用與處置等階段，不能只比較運轉時的表現或廣告外觀。"),
    ("溪流調查發現施工地點下游的昆蟲種類較少，但下游水溫也較高。最恰當的結論是什麼？", ["A 這顯示可能有關聯，但要控制水溫等因素後，才能主張單一原因", "B 可以確定只有施工造成種類減少", "C 昆蟲不能生活在任何溪流", "D 調查證明水溫永遠不重要"], "A", "下游同時改變了施工情況與水溫，因此可說有關聯線索，卻不能把施工單獨視為唯一原因；需要控制或比較其他變因。"),
    ("城市希望經濟成長並改善空氣品質，哪項政策同時兼顧發展與環境保護？", ["A 支持高效率大眾運輸，並要求新產業監測排放", "B 不測排放就擴建更多工廠", "C 立刻禁止所有交通方式", "D 只要就業增加就忽略空氣資料"], "A", "大眾運輸可支持移動需求，排放監測則使產業的環境成本可量測、可管理；這比絕對禁止或忽略資料更能兼顧兩端。"),
    ("村落復育紅樹林後，根部附近記錄到較多幼魚。哪項證據能強化「復育有幫助」的結論？", ["A 與復育前紀錄及相似但未復育地點比較，並維持相近取樣量", "B 復育後只數一次魚", "C 詢問居民是否喜歡紅樹林的顏色", "D 每次調查都更換網具與取樣時間"], "A", "復育前後資料、相似的未復育對照地點與一致取樣量，可排除季節或測量改變造成的假象，使因果推論更有力。"),
]

for question, (prompt, options, answer, explanation) in zip(Q, LOCALIZED):
    question["prompt"] = prompt
    question["options"] = [{"id": option[0], "text": option[2:]} for option in options]
    question["answer"]["value"] = answer
    question["answer"]["explanation"] = explanation

target_letters = {1: "C", 3: "D", 4: "B", 5: "C", 7: "D", 9: "C"}
for index, target in target_letters.items():
    question = Q[index]
    old = question["answer"]["value"]
    correct = next(option for option in question["options"] if option["id"] == old)
    wrong = [option for option in question["options"] if option["id"] != old]
    order = [letter for letter in "ABCD" if letter != target]
    question["options"] = [{"id": letter, "text": option["text"]} for letter, option in zip(order + [target], wrong + [correct])]
    question["answer"]["value"] = target
    question["solutionSteps"][-1] = question["solutionSteps"][-1].replace(f"選 {old}", f"選 {target}")

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

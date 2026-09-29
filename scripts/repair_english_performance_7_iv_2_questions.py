import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"

refs = [
    {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
        "title": "高雄市立國昌國中110學年度第一學期第一次段考三年級英語科試題",
        "year": "110-1",
        "subject": "english",
        "locator": "PDF第3頁第24至26題：閱讀寄宿家庭介紹，整合文本線索辨認資訊與主旨",
        "locatorLevel": "page",
        "observedPattern": "閱讀短文時需將熟悉的生活／文化概念當作暫時線索，再以段落明示細節核對理解；本站不沿用原卷人物或題幹。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
    {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國中105學年度第二學期第一次段考三年級英文科試題",
        "year": "105-2",
        "subject": "english",
        "locator": "PDF第5頁第51至53題：依研究文章判斷主旨、證據與片語意義",
        "locatorLevel": "page",
        "observedPattern": "把既有知識用於理解科普說明時，仍須逐項對照研究方法、數據和作者結論，不能讓熟悉印象取代文本。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
    {
        "url": "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
        "title": "基隆市立武崙國中110學年度第二學期九年級第二次段考英文科試題",
        "year": "110-2",
        "subject": "english",
        "locator": "PDF第2頁第23題：依春節紅包文化判讀句意",
        "locatorLevel": "page",
        "observedPattern": "節慶文化背景能協助理解句子中的祝福意圖；解讀仍受題幹明示語句限定，避免把個人經驗套成普遍規則。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
    },
]

answer_keys = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
answer_fragments = [
    "carry pollen between flowers",
    "strong wind and rain can make an outdoor event unsafe",
    "the red envelope is a customary way to share good wishes",
    "sun's position changes the angle of light and shadow length",
    "validate payment or entry for the ride",
    "yeast can produce gas while the dough rests, making it rise",
    "rain may discourage cycling, but the chart alone does not prove the cause",
    "revise the prediction toward gardening and keep reading for confirmation",
    "horse travel was slower and the route distance affected delivery time",
    "the examples support the prediction, so keep it provisionally",
]
options = [
    ["Bees can carry pollen between flowers, which can help many garden plants reproduce.", "Garden soil always contains enough water, whatever the weather.", "Bees make honey, so every garden must have a beehive.", "Most flowers grow only when planted in rows."],
    ["The event will probably move to an indoor room today.", "Strong wind and rain can make an outdoor event unsafe, so organizers may choose a later date.", "Typhoons usually arrive at the same time every year.", "Postponed means the event has been canceled forever."],
    ["An envelope is usually used to mail a greeting card.", "The color red always means that a family is celebrating a birthday.", "The red envelope is a customary way to share good wishes during the holiday.", "Every child receives the same amount of money in every family."],
    ["The object's color determines whether its shadow grows longer.", "A shadow changes length only when the object itself moves.", "Shadows become longest whenever the sky is cloudy.", "The sun's position changes the angle of light and shadow length."],
    ["The card can validate payment or entry for the ride, depending on the transit system.", "The card is mainly used to reserve a seat for a later train.", "The passenger taps it to send a message to station staff.", "The card tells the passenger which platform to use without signs."],
    ["Resting makes the dough cold enough to freeze before baking.", "Yeast can produce gas while the dough rests, making it rise before baking.", "Resting changes flour into sugar without any other ingredient.", "The instruction means the cook should stop following the recipe."],
    ["Rainy days make every student choose a bus, even when no bus is available.", "The chart proves that rain is the only reason bicycle use decreases.", "Rain may discourage cycling, but the chart alone does not prove the cause.", "The number of bicycles on the chart tells us how much rain fell."],
    ["Keep the sports prediction and ignore the paragraph about seeds.", "Add sports facts until the paragraph seems to fit the first guess.", "Assume the writer made a mistake and stop reading immediately.", "Revise the prediction toward gardening and keep reading for confirmation."],
    ["Horse travel was slower and the route distance affected delivery time.", "A rider could send the letter instantly as soon as it was written.", "Horseback travel was always faster than trains on every route.", "The delivery took longer because letters were too heavy to carry."],
    ["Reject the prediction because separate bins cannot contain recyclable items.", "The examples support the prediction, so keep it provisionally and check later details.", "Replace it with a prediction about a concert, without rereading.", "Ignore the examples and rely only on what you knew before reading."],
]
strategies = [
    "由標題提出可驗證的自然概念預測，區分授粉與單純產蜜。",
    "把災害常識用來解釋公告決策，同時不把延期誤讀成改場或永久取消。",
    "用節慶背景理解紅包的祝福功能，避免把一家經驗推成人人相同。",
    "連結光源位置與影長變化，檢查標題預測是否符合基本光學關係。",
    "從乘客進站前的操作推測交通卡功能，保留不同系統可能有差異。",
    "先辨認麵團含酵母，再用發酵知識解釋靜置這一步的目的。",
    "背景知識只能提出合理假設；分清圖表呈現的相關現象與尚未證實的原因。",
    "遇到與預測衝突的新線索時，依段落證據修正主題假設而非硬套舊想法。",
    "將交通史常識作為解釋信使耗時的線索，並把路程等條件一併考慮。",
    "比較預測與列舉材料的文本證據，先暫時確認，再繼續閱讀找反例。",
]
steps = [
    ["先讀標題 How Bees Help Gardens，判斷文章要解釋蜜蜂與花園的關係。", "回想與題目直接相關的知識，而非列舉所有蜜蜂特徵。", "蜜蜂在花間活動時能搬運花粉，授粉可幫助許多植物繁殖。", "排除B（只談土壤供水）、C（只談蜂蜜）與D（只談種植排列），它們都未連結授粉與種子形成。", "答案A最能形成可由內文驗證的預測；閱讀後仍要檢查作者是否如此說明。"],
    ["圈出因果連接詞 Because，找到原因是颱風逼近、結果是戶外活動延期。", "用天候常識推想颱風會帶來強風與豪雨，戶外場地可能不安全。", "答案B把背景知識連到延期的安全考量，且沒有超出公告已知範圍。", "A把延期改成換室內；C把決策變成每年固定時間；D把延期誤作永久取消。", "選B：背景知識協助理解決策理由，但公告並未說明一定改期到何日。"],
    ["定位句中 red envelopes 與 Lunar New Year，辨認題目問的是文化意義。", "回想此節慶中紅包常承載祝福的習俗，不把金額或家庭做法當成共同規則。", "答案C解釋紅包如何傳達祝願，正好補足句子描述的文化功能。", "A只說一般信封用途；B把紅色硬連到生日；D臆測每個家庭金額一致。", "選C：文化背景幫助理解祝福意圖，但個別家庭做法仍可能不同。"],
    ["只根據標題 Why Shadows Change Length 提出初步預測，暫不假定文章細節。", "調用光線與影子的基本關係：光源角度改變，影子長短也會改變。", "答案D指出太陽位置改變入射角，因而可能影響影長，與標題相符。", "A混淆物體顏色；B忽略光源角度；C把陰天直接當作影子變長的充分條件。", "選D作為合理起點；若正文提供其他光源或條件，再依新證據修正。"],
    ["讀出關鍵行為 tap their cards before entering the station，判斷它與乘車流程相關。", "利用熟悉的大眾運輸經驗推測卡片會記錄進站或支付，但不同城市規則可能不同。", "答案A最貼近乘客在閘口前感應卡片的用途，且措辭保留系統差異。", "B把進站操作誤當訂位；C推成聯絡員工；D說卡片可代替站內指標，皆缺乏線索。", "選A：背景知識提供最可能功能，不代表所有交通卡只具單一用途。"],
    ["留意 recipe 中的 dough 與 before baking，先辨認這是烘焙步驟說明。", "確認配方指的是含酵母的麵團；此條件會影響背景知識能否套用。", "酵母在適當條件下產生氣體，使麵團膨起，因此答案B能解釋靜置目的。", "A把靜置誤作冷凍；C忽略酵母與配方；D將操作指令當成停止作業。", "選B作為含酵母配方的合理解釋；若食譜使用其他膨發方式，需以正文為準。"],
    ["先描述圖表直接顯示的事實：雨天騎車的學生比較少。", "想到雨水可能影響舒適與安全，形成一個待查的原因假設。", "答案C既使用生活經驗，也提醒單張圖表不能單獨證明因果。", "A把相關說成唯一原因；B假定人人都搭公車；D把騎乘人數誤當降雨量。", "選C：可提出合理解釋，但要有額外資料才能判定雨是否造成差異。"],
    ["記下原預測是運動隊，再找第一段的新線索：種子與陽光。", "比較新線索與運動主題，發現兩者不吻合，不能用舊知硬接。", "答案D依證據把預測轉向植物栽種，並保留繼續閱讀確認的空間。", "A拒看反證；B強塞運動內容；C未查證就指責作者，都不是有效閱讀策略。", "選D：背景知識可提出假設，文本出現相反線索時就要修正。"],
    ["圈出 before trains existed 和 messenger on horseback，辨識交通時代線索。", "想想馬匹移動速度、停靠與路線距離如何影響送信時間。", "答案A提出慢速交通及路程的合理解釋，但仍視實際距離等條件而定。", "B套用現代即時通訊；C誇大馬匹速度；D與信使必須運送信件的情境矛盾。", "選A作為暫時推論；若文章提供旅程長度或天候，應再納入判斷。"],
    ["把預測寫清楚：文章可能談分類回收材料。", "找正文列出的具體例子，而非只看自己原有印象。", "玻璃、紙張和鐵鋁罐分別進不同箱，與材料分類預測一致。", "A否認例子；C無證據地改換主題；D拒絕使用文本，都和新線索不符。", "選B：目前證據支持原預測，可暫時保留並在後文繼續檢查。"],
]

for number, key in enumerate(answer_keys, start=1):
    path = QUESTION_DIR / f"question-english-performance-7-iv-2-{number}.json"
    item = json.loads(path.read_text(encoding="utf-8"))
    if number == 1:
        item["prompt"] = "An article titled 'How Bees Help Gardens' will explain why flowers produce seeds. Which background knowledge best connects the title with that result?"
    elif number == 6:
        item["prompt"] = "A recipe for yeast bread says, 'Let the dough rest before baking.' Why might background knowledge help?"
    item["options"] = [{"id": letter, "text": text} for letter, text in zip("ABCD", options[number - 1])]
    item["answer"]["value"] = key
    item["solutionStrategy"] = strategies[number - 1]
    item["solutionSteps"] = steps[number - 1]
    item["answer"]["explanation"] = steps[number - 1][-1]
    item["examPatternRefs"] = refs
    primary = refs[(number - 1) % len(refs)]
    item["provenance"] = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": primary["url"],
        "sourceLocator": primary["locator"],
        "authoringNote": "題幹情境、選項、答案、策略與詳解均為原創；公校試題只用於核對閱讀推論與背景知識運用的能力型態，不複製原卷。內容維持draft。",
    }
    item["reviewStatus"] = "draft"
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"unit": "english-performance-7-iv-2", "questions": len(answer_keys), "answerKeys": answer_keys, "status": "draft"}, ensure_ascii=False))

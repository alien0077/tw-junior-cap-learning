import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"

SOURCES = {
    "zhongshan": {
        "url": "https://csjh.kl.edu.tw/books/file/263/110-1%E5%9C%8B%E4%B8%80%E8%8B%B1%E8%AA%9E%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        "title": "基隆市立中山高級中學國中部110學年度第1學期第1次段考七年級英文科試題卷",
        "year": "110-1",
        "locator": "PDF第1頁第8題：聽取位置關係後，在球體圖像中辨識物件相對位置",
        "pattern": "以聽到的方位關係對照圖像位置；本題另創修理工作桌與工具配置。",
    },
    "jian": {
        "url": "https://www.cajh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=66&cfsn=309&fn=112-1-1-7%E8%8B%B1%E8%AA%9E.pdf&op=dlfile",
        "title": "花蓮縣立吉安國民中學112學年度第1學期第1次段考七年級英語科試題",
        "year": "112-1",
        "locator": "PDF第1頁第一大題第1題：依聽到的句子辨認人物與物件構成的圖像",
        "pattern": "將聽到的名詞及人物關係配對到圖像；本題改成社區植物工作坊的數量盤點。",
    },
    "dashe": {
        "url": "https://www.dam.kh.edu.tw/upload/68/101_28414/111-1-1%E4%B8%80%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf",
        "title": "高雄市立大社國民中學111學年度第1學期第1次段考七年級英語科試題與解答",
        "year": "111-1",
        "locator": "PDF第1頁第一大題第4題：從人物與寵物圖像辨認人物正在進行的活動",
        "pattern": "以人物動作及周邊物件辨識正在發生的活動；本題改寫成戶外維修站的工作分配。",
    },
    "sanduo": {
        "url": "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mek15TDNCMFlWOHpOVEUxWHpZM09ETTRPREpmT1RNME9UWXVjR1Jt&fname=WW54RPOKRK4411HH50LKKPHG1430WT24KLB0XSXSTXA1LK40NKROSTB4WW54A0OKWW5400HHA404LK14MOPKTSLOOPB0QLYWXTYTXWA0SWZWCDVWSSOKXSFCUS00HH25DGA0DCZWFCMO40201434ZWMKUTGDUT21SSUSJGB0GGA401USTWLKUXJHGG04DC14MKB4JDIGKLEG35WWMLXTPOFCSSRO54SWUSDCROFCNOXW41KKWW04DHHG",
        "title": "新北市立三多國民中學113學年度第1學期第2次段考七年級英語科試題",
        "year": "113-1",
        "locator": "PDF第1頁第一部分聽力第一大題第2題：依商品推車圖像辨認內容物與場景",
        "pattern": "比對圖像中的物品與場景描述，排除只對上一項細節的選項；本題另創校園器材借還台。",
    },
    "yanchao": {
        "url": "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立燕巢國民中學111學年度第1學期七年級第2次段考英文科試題卷",
        "year": "111-1",
        "locator": "PDF第1頁非選擇測驗第27題：依單幅情景圖以英文敘述時間、地點、人物、行動與心情",
        "pattern": "將場景中的人物、行動與前後線索組成連貫圖像敘述；本題另創公共圖書交換日情境。",
    },
}

ITEMS = [
    ("C", "zhongshan", "相對位置", "Image description: On a repair table, a folded map is beneath a lamp. A screwdriver is to the left of the map, and a cup is to the right. Which sentence matches the scene?", ["The lamp is under the map.", "The cup is between the map and the screwdriver.", "The screwdriver is left of the map.", "The map is inside the cup."], "先以map為中心定位：螺絲起子在左、杯子在右，地圖在燈下。只有C符合明確方位；其他選項把上下、左右或包含關係顛倒。", ["把地圖當作定位基準，不要先猜整張圖的方向。", "逐一整理圖中文字：lamp在map上方，screwdriver在左，cup在右。", "對照選項中的介系詞，確認left of與場景一致。", "排除把right/left、under及inside錯置的句子。", "選C；相對位置題先固定參照物，再逐一核對介系詞。"]),
    ("A", "jian", "數量與類別", "Image description: At a community seed table, two children hold small pots. Three empty trays sit behind them, and one watering can is beside the trays. How many children are holding pots?", ["Two.", "Three.", "Four.", "One."], "題目問的是拿著盆子的children，不是桌上的托盤數或澆水壺數。圖像描述明確指出兩位孩子各拿一盆，因此答案為A。", ["先圈出問題限定的對象：children holding pots。", "從描述找對應人物數量，不把後方trays算進去。", "確認兩位孩子都拿著小盆，沒有第三位人物。", "比對選項，排除托盤的3及水壺的1。", "選A；數量題要按名詞類別計數，避免把相鄰物件混入。"]),
    ("D", "dashe", "動作與角色", "Image description: Beside a trail sign, one volunteer tightens a loose wheel on a handcart while another holds the cart steady. A third person checks a paper list. What is the first volunteer doing?", ["Reading the trail map aloud.", "Loading food into the cart.", "Writing a name on the list.", "Repairing the cart wheel."], "第一位志工手上正在鎖緊鬆動的輪子，所以他在修理手推車；扶住車子的是另一位，查看清單的是第三人。", ["先辨認題目指的是first volunteer，別把不同人物的動作混在一起。", "將tightens與loose wheel連起來，找出直接動作。", "用另外兩人的行動確認角色區分：一人扶車、一人看清單。", "排除讀地圖、裝食物和寫名單等圖中未描述的活動。", "選D；多人圖像題先鎖定人物，再把動詞與手中物件配對。"]),
    ("B", "sanduo", "物品與用途", "Image description: At the school equipment desk, a student returns a blue badminton racket, two shuttlecocks, and a stopwatch. A sign above the desk says 'Sports Gear—Return Here.' What is the scene mainly about?", ["Students buying lunch after practice.", "Returning borrowed sports equipment.", "A science experiment with a timer.", "Choosing a new school uniform."], "球拍與羽球是運動器材，碼表也放在寫著Sports Gear—Return Here的櫃台；核心事件是歸還借用器材，不是購買或實驗。", ["不要只看到stopwatch就直接判斷成實驗。", "把三樣物品分類：球拍與羽球明確屬於運動用品。", "閱讀標示的Return Here，判斷學生正在歸還而非購買。", "排除制服、午餐及科學實驗等與標示不符的場景。", "選B；主旨要整合物件、動作和標示，不能只憑單一物品。"]),
    ("C", "yanchao", "人物與事件順序", "Image description: In three frames at a book-swap table, Leo places a label on a book, checks the title with a classmate, and then hands the book to a younger student. Which event happens last?", ["Leo writes the label.", "Leo checks the title.", "Leo gives the book to a younger student.", "The younger student chooses a seat."], "三格依序呈現貼標籤、核對書名、交書給年幼學生。題目問最後發生的事件，故答案是交書；選項D沒有圖像依據。", ["先按照frame順序標記開始、接著、最後。", "第一格是貼標籤，第二格是和同學核對書名。", "找到第三格的動作：Leo把書交給年幼學生。", "排除把前兩格事件當成最後，及畫面未出現的選項。", "選C；連續圖先排序畫格，再回答時間詞所問的那一格。"]),
    ("A", "jian", "顏色與物件配對", "Image description: A picnic blanket has a white thermos, a purple lunch box, and a striped towel. A child is reaching for the thermos. Which item is purple?", ["The lunch box.", "The towel.", "The thermos.", "The blanket."], "描述把purple直接修飾lunch box；其他物品分別是white或striped，沒有線索說毯子是紫色。", ["先找出問題的顏色詞purple。", "回到圖像描述，查看哪一個名詞緊接purple。", "確認同句中thermos是white、towel是striped，避免混淆。", "不替未描述顏色的blanket自行補資料。", "選A；顏色題要保留形容詞與物件的配對，不可只記顏色。"]),
    ("D", "dashe", "缺漏資訊的證據", "Image description: Four hikers sit at a rest stop. Their backpacks, maps, and snack boxes are on the bench, but every bottle holder is empty and no drink is visible. What do they need most?", ["Another map.", "More backpacks.", "Extra snack boxes.", "Drinking water."], "畫面已有地圖、背包與點心，且明確指出水壺袋是空的、沒有飲料；最有根據的缺漏是飲用水。", ["先盤點已出現的地圖、背包與食物。", "注意否定線索：every bottle holder is empty、no drink is visible。", "把空缺和休息中的健行者需求連結，判斷飲水最切題。", "排除圖中已具備的物品，不以常識添加不必要物品。", "選D；缺漏題要用畫面明示的不存在證據，而非猜測人物想要什麼。"]),
    ("B", "zhongshan", "遮擋下的方向判讀", "Image description: A bicycle is parked behind a bench. A helmet rests on the bench, and a tree stands in front of it. Which statement is true?", ["The tree is behind the bicycle.", "The bicycle is behind the bench.", "The helmet is under the bench.", "The bench is inside the tree."], "場景明確說bicycle在bench後方、helmet在bench上、tree在bench前方。只有B照原方向描述；A顛倒前後，C、D改變物件關係。", ["選一個中心物件bench作參照。", "逐項記錄關係：bicycle behind bench、helmet on bench、tree in front。", "找出重述相同關係的選項B。", "排除把behind改成in front、on改成under或荒謬的inside關係。", "選B；前後位置題要注意代名詞it指涉哪個物件，並保持方向不反轉。"]),
    ("C", "yanchao", "連續圖推測下一步", "Image description: In a garden sequence, Ava loosens the soil, places a seed in a small hole, and covers it. What is the most reasonable next action?", ["Pull the seed out to check its color.", "Move the garden bed indoors immediately.", "Water the planted spot.", "Pick flowers from the new seed."], "播種並覆土後，合理的下一步是澆水；種子不會立即長成花，拔出檢查或搬進室內都沒有情境支持。", ["依序回看鬆土、放種子、覆土三個已完成步驟。", "判斷這組動作的目的為完成播種並讓種子開始生長。", "選擇接在覆土後、符合照料流程的澆水。", "排除立即採花等違反植物生長時間的選項。", "選C；預測下一步要延續已知程序，但不要延伸成畫面沒有支持的長期結果。"]),
    ("A", "sanduo", "多線索完整描述", "Image description: At a rainy bus stop, a woman holds a clear umbrella over a child carrying a violin case. Route 8 is shown on the sign; two wet bicycles are locked to the rail, and the bench is empty. Which sentence includes only details supported by the scene?", ["A woman shelters a child with a violin case at the Route 8 stop, while two bicycles are parked nearby.", "A man and two children board Route 8 after leaving their dry bicycles inside the bus.", "The child plays the violin beside a crowded bench as three buses arrive.", "A woman sells umbrellas while the child rides one bicycle to school."], "A整合可見人物、雨傘、提琴盒、8號路線與兩輛腳踏車，沒有增添畫面外的事件。其餘選項改變人物、數量、動作或場景狀態。", ["把題目要求的完整場景拆成幾類：人物、物件、位置與交通標示。", "逐一核對：woman、child、violin case、Route 8、two bicycles。", "再檢查選項是否加入看不見的上車、演奏、售賣或到站事件。", "選擇涵蓋多項已知細節且沒有不受支持增補的句子。", "選A；整合描述以證據完整度為準，細節多不代表可以自行編故事。"]),
]


def make(index, item):
    answer, source_key, skill, prompt, options, explanation, steps = item
    source = SOURCES[source_key]
    ref = {
        **source,
        "subject": "english",
        "observedPattern": source["pattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }
    ref["title"] = source["title"] + "；只參照圖像辨識／描述能力，不複製原卷內容。"
    provenance = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": source["url"],
        "sourceLocator": source["locator"] + "；本題人物、場景、文字與選項均重新創作。",
        "authoringNote": "僅取公立學校公開英語試題的圖像辨識、方位／動作／場景推論或連續圖敘述能力型態作pattern-only參考；未重製原卷題幹、選項、圖片或答案。",
    }
    return {
        "id": f"question-english-performance-2-iv-10-{index}",
        "subject": "english",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "knowledgeIds": ["kg-english-performance-2-iv-10"],
        "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" 正確答案：{answer}。"},
        "provenance": provenance,
        "reviewStatus": "draft",
        "updatedAt": "2026-09-24",
        "lessonId": "lesson-english-performance-2-iv-10",
        "examPatternRefs": [ref],
        "solutionStrategy": f"{skill}：先鎖定問題要找的人物、物件、關係或時間，再逐項用圖像描述核對證據；不補入畫面未提供的資訊。",
        "solutionSteps": steps,
    }


for index, item in enumerate(ITEMS, 1):
    path = OUT / f"question-english-performance-2-iv-10-{index}.json"
    path.write_text(json.dumps(make(index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(ITEMS)} original picture-description questions")

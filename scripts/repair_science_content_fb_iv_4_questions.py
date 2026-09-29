import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions" / "science"
LESSON = "lesson-science-content-fb-iv-4"
KG = "kg-science-content-fb-iv-4"
SOURCES = [
    {"url": "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf", "title": "高雄市立鹽埕國民中學公開自然科評量", "year": "113-114"},
    {"url": "https://www.cp.ptc.edu.tw/storage/134523/134523_114_B-23_7A.pdf?1774770497=", "title": "屏東縣新園國中公開自然領域教學計畫", "year": "114"},
    {"url": "https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=119&file=WVhSMFlXTm9MelkzTDNCMFlWOHhNamcwTmw4Mk9UazRNell4WHpjNE1qQXhMbkJrWmc9PQ%3D%3D&fname=WSGGRPQK20QO41KKLOLK54TXXSMO25JGKLB0NO24CCA1XW40YSYWEGB40054ROEGDGKKDH00DG04ICHCIGNKTS34OPB035MKQP35NOTSUWZWCDUWFH10YWFCRKPOSSYX24XWJG34XSKOSSICDGB040WSHDNPMLOOPOUSUSKLDGA4A4FCVW0021JH20B0RKZWOO30LKKKQOJCTWICZTA1LKQPSWYWKORK00POPO", "title": "新北市立泰山國中公開自然領域課程計畫", "year": "114"},
]


def refs():
    return [{**source, "subject": "science", "locator": "Moon phases, observation timing, Sun-Earth-Moon geometry, and evidence-based model interpretation", "observedPattern": "公開自然科評量與課程資料常用連續觀測、位置示意與週期資料，要求學生由日月地幾何關係判讀月相，而非把月相誤作月球自發明暗。此處只取能力方向。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for source in SOURCES]


def make(i, prompt, options, answer, explanation, strategy, steps, difficulty):
    return {
        "id": f"question-science-content-fb-iv-4-{i}",
        "subject": "science",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": key, "text": value} for key, value in options.items()],
        "knowledgeIds": [KG],
        "difficulty": difficulty,
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0]["url"], "sourceLocator": "三份公立學校公開自然科評量／課程資料僅供月相觀測、週期資料與日月地模型能力方向研究；未複製原題、選項、圖表或答案。", "authoringNote": "依官方課綱 KG 與三筆公立學校公開自然科資料的月相判讀能力方向獨立改寫；題幹、選項、解析、資料與五步解法均為原創，待第二輪 AI／Terra 內容複核。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-09-12",
        "lessonId": LESSON,
        "examPatternRefs": refs(),
        "solutionStrategy": strategy,
        "solutionSteps": steps,
    }


Q = [
    make(1, "A student observes the Moon from the same place at the same time each night. The bright part grows from a thin crescent to a full disk over several days. What is the best explanation?", {"A": "The Moon makes its own light stronger each night.", "B": "The Sun illuminates the Moon, and changing Sun-Earth-Moon positions change the visible lit fraction.", "C": "Clouds permanently paint a larger bright area on the Moon.", "D": "The Moon becomes physically larger before a full moon."}, "B", "The Moon reflects sunlight. As the Moon orbits Earth, the geometry changes which fraction of its sunlit half is visible from Earth; the Moon does not produce changing amounts of its own light or change size in this cycle.", "先把觀察到的亮面變化拆成光源、幾何位置與月球大小三個可能因素，再選能同時解釋週期與視覺變化的機制。", ["找出題幹的變化是亮面可見比例，不是月球直徑。", "確認月球的光來自反射太陽光。", "把月球繞地球運動造成的日、地、月相對位置改變連到可見亮面。", "排除自發光、雲彩塗色與月球實際變大的說法。", "選 B，回查它能解釋由新月細弦到滿月的連續規律。"], "easy"),
    make(2, "Two nights are both described as having a crescent Moon, but on the first night the crescent is waxing and on the second it is waning. Which additional evidence would distinguish them most reliably?", {"A": "The Moon's name in a storybook.", "B": "Whether the illuminated fraction is increasing or decreasing across consecutive observations.", "C": "The number of clouds during only one night.", "D": "The color of the observer's telescope."}, "B", "Waxing and waning describe the direction of change in illuminated fraction. A sequence of observations supplies that evidence; a single cloud count, telescope color, or a name does not.", "題目不是只分辨細弦外觀，而是判斷亮面正在增加還是減少，因此必須使用時間序列。", ["圈出 waxing 與 waning 的差別是變化方向。", "確認單一夜晚的外觀可能相似，不能直接判定方向。", "找能比較連續夜晚亮面比例的資料。", "排除故事名稱、單夜雲量與望遠鏡顏色等無關資訊。", "選 B，因為增加或減少的趨勢才是可靠判據。"], "medium"),
    make(3, "A diagram places the Sun at the left, Earth in the middle, and the Moon on the opposite side of Earth. Which phase is most likely shown, ignoring the slight tilt of the Moon's orbit?", {"A": "Full moon, because the side facing Earth is mostly illuminated.", "B": "New moon, because the Moon is between Earth and the Sun.", "C": "First quarter, because exactly half the Moon is always dark.", "D": "The phase cannot be inferred from any relative positions."}, "A", "With Earth between the Sun and Moon, the Moon's Earth-facing hemisphere is the hemisphere receiving sunlight, so it appears nearly full. A new moon occurs when the Moon is between the Sun and Earth.", "以光源位置與面向地球的半球判讀，不以選項中的固定口訣取代模型。", ["先定位太陽光的方向。", "確認月球位於地球背向太陽的一側。", "判斷月球受光面是否朝向地球。", "排除把『月球在中間』才是新月的錯誤位置描述。", "選 A，因為地球位於日月之間時看見接近完整受光面。"], "medium"),
    make(4, "A student says, 'The Moon is not visible on a new-moon night because it receives no sunlight.' Which correction is scientifically best?", {"A": "The Moon receives sunlight, but the sunlit side mostly faces away from Earth.", "B": "The Moon stops existing for one night.", "C": "The Moon turns off its reflected light by choice.", "D": "Earth blocks all sunlight from reaching the Moon every month."}, "A", "At new moon the Moon is near the Sun-Earth line with its illuminated half facing away from Earth. It still receives sunlight; the visible side is mostly the unlit half and is also near the Sun's direction in the sky.", "修正迷思時要分開『是否受光』與『從地球看見多少受光面』。", ["辨認原句把看不見誤等同於沒有受光。", "定位新月時月球在太陽與地球之間附近。", "判斷受光半球朝向太陽而非主要朝向地球。", "排除月球消失、停止反光與地球每月完全遮光的說法。", "選 A，確認它保留光照事實並解釋可見面很暗。"], "easy"),
    make(5, "A calendar records the first-quarter Moon on day 7 and the full Moon on day 14 of an observation cycle. Which conclusion is supported by these data?", {"A": "The complete phase cycle lasts exactly 14 days.", "B": "The full Moon occurs about one quarter-cycle after the first quarter in this record.", "C": "The Moon's orbit stops at the full Moon.", "D": "Every phase always lasts exactly one day."}, "B", "The record places first quarter and full moon about seven days apart, which is approximately a quarter of a roughly month-long phase cycle. It does not establish a complete cycle of 14 days or one-day phases.", "只做資料能支持的局部推論，避免把兩個日期誤當成完整週期。", ["讀取 day 7 與 day 14 的時間差。", "把 first quarter 到 full 的順序放入月相週期。", "判斷七天約為一個月相週期的四分之一。", "排除完整週期 14 天、軌道停止與每相一天等過度結論。", "選 B，確認結論只涉及資料所示的相鄰階段。"], "medium"),
    make(6, "At the same clock time, a student sees the Moon in a different part of the sky on successive nights. Which factor is most directly related to this shift?", {"A": "The Moon moves along its orbit around Earth while Earth also rotates.", "B": "The Moon changes its mass every night.", "C": "The Sun turns off for a few hours.", "D": "The stars push the Moon to a random location."}, "A", "The Moon's orbital motion changes its position relative to Earth from night to night, while Earth's rotation determines the daily apparent motion. A regular shift is not evidence for changing mass or random pushing.", "把『每天同時刻的位置』看成天體運動的觀測證據，分辨規律運動與任意變化。", ["確認觀察控制了 clock time，仍看到位置改變。", "找出會改變月地相對位置的月球公轉。", "保留地球自轉對當天視運動的影響。", "排除質量改變、太陽熄滅與隨機推動等無證據假說。", "選 A，確認它同時符合週期性與觀測條件。"], "medium"),
    make(7, "A model uses a lamp, a ball, and a small bead to represent the Sun, Earth, and Moon. When the bead is moved around the ball, what should the learner observe to model Moon phases?", {"A": "The bead's own color changes by itself.", "B": "The visible fraction of the bead's lamp-lit side changes with its position.", "C": "The lamp becomes brighter whenever the bead is behind the ball.", "D": "The ball produces light toward the lamp."}, "B", "The lamp represents the Sun and illuminates one half of the bead. Moving the bead changes the direction from which the observer sees that lit half, modeling the changing visible fraction.", "先對應模型元件，再追蹤光線、受光面與觀察者視線三者的關係。", ["建立 lamp、ball、bead 分別代表的天體。", "確認 lamp 只提供光，bead 的一半受光。", "移動 bead 並觀察從 ball 位置看見多少受光面。", "排除顏色自變、燈光任意變亮與球體發光等錯誤模型。", "選 B，確認模型保留月相的幾何核心。"], "easy"),
    make(8, "A student takes a photograph of the Moon through a telescope. The right side is bright in one photograph and the left side is bright three nights later. Which explanation is most defensible?", {"A": "The Moon's illuminated hemisphere changed because the Sun disappeared and reappeared.", "B": "The viewing geometry changed as the Moon moved in its orbit, changing which lit portion faced Earth.", "C": "The telescope reversed the Moon's orbit.", "D": "The Moon's solid surface moved from right to left."}, "B", "The Sun continues to illuminate the Moon, while the Moon's orbital position changes the portion of the sunlit hemisphere visible from Earth. The apparent side change is not a rearrangement of the solid surface.", "使用時間差與亮面方向作幾何推論，避免把影像方向或表面外觀當成月球本體變形。", ["比較兩張照片真正改變的是亮面方向。", "確認太陽仍是固定光源，無須假設消失。", "連結月球公轉造成的觀察幾何改變。", "排除望遠鏡改變軌道與月面固體左右搬移。", "選 B，確認解釋同時符合光照連續性與週期運動。"], "hard"),
    make(9, "Why can an observer on Earth not see a lunar eclipse at every full moon?", {"A": "The Moon emits no reflected light at full moon.", "B": "The Moon's orbital plane is slightly tilted, so the Sun, Earth, and Moon are not aligned for every full moon.", "C": "Full moons occur only during daytime.", "D": "Earth has no shadow."}, "B", "A lunar eclipse requires a close alignment in which the Moon passes through Earth's shadow. The Moon's tilted orbit means most full moons pass above or below the shadow.", "由必要條件『滿月加上進入地影』判斷，分辨有滿月不代表三者每次都精確成一直線。", ["先列出月食需要滿月與地影遮蔽。", "確認只有日、地、月接近直線才會進入地影。", "加入月球軌道相對黃道面的傾角。", "排除無反射光、只在白天滿月與地球無影子的說法。", "選 B，確認它解釋大多數滿月沒有月食的原因。"], "hard"),
    make(10, "A class compares a month of Moon sketches made at different times. Which practice would make the conclusion about a repeating phase pattern strongest?", {"A": "Record date, time, observing location, weather, and the illuminated shape for every sketch.", "B": "Keep only the most attractive drawing.", "C": "Change the observation time each night without recording it.", "D": "Choose the phase name before looking at the sketch."}, "A", "Consistent, traceable records of date, time, location, conditions, and illuminated shape allow the class to identify a repeating pattern and distinguish observation from interpretation.", "把月相研究當作可重現的觀測活動，先建立紀錄品質再判斷週期。", ["確認研究目標是辨認重複的亮面變化。", "列出每次觀測需要的時間、地點、天候與圖像資料。", "保持紀錄格式一致，讓不同日期可比較。", "排除只留漂亮圖、改時間不記錄與先猜答案等偏差。", "選 A，確認證據可追溯且足以支持週期結論。"], "medium"),
]

# 題庫交付為繁體中文；保留原先每題的推理骨架，但重新以臺灣國中語境表述。
LOCALIZED = [
    ("學生連續幾天在同一地點、同一時刻觀察月球，發現亮面從細弦逐漸變成接近圓盤。下列哪個解釋最合理？", ["A 月球自行發出的光每天變強", "B 太陽照亮月球，而日、地、月相對位置改變了地球看見的受光比例", "C 雲層永久把月面塗亮得更大", "D 滿月前月球本身會變大"], "B", "月球反射太陽光。月球繞地球運動時，地球看到的受光半球比例會改變；月球並不是自行發光變強，也沒有在這段週期中實際變大。"),
    ("兩個晚上都看見細弦月，但第一晚亮面正在增加，第二晚亮面正在減少。要最可靠地分辨兩者，還需要哪項證據？", ["A 故事書替月球取的名稱", "B 連續觀測中亮面比例是增加還是減少", "C 其中一晚的雲量", "D 觀測者望遠鏡的顏色"], "B", "盈虧描述的是受光面比例的變化方向；連續觀測才能判斷正在增加或減少，單晚雲量、名稱或望遠鏡顏色都不能提供這項證據。"),
    ("示意圖中太陽在左側、地球在中央、月球位於地球另一側。忽略月球軌道的微小傾角，圖中最可能是哪個月相？", ["A 滿月，因為朝向地球的月面大多受光", "B 新月，因為月球位在太陽與地球之間", "C 上弦月，因為月球永遠有一半背光", "D 只看相對位置無法判斷月相"], "A", "地球位於太陽與月球之間時，朝向地球的半球大致是受光面，因此接近滿月；月球位於太陽與地球之間才是新月附近。"),
    ("學生說：「新月晚上看不見月球，是因為月球沒有受到陽光照射。」下列哪項修正最科學？", ["A 月球仍受到陽光照射，但受光面大多背向地球", "B 月球會在一個晚上消失", "C 月球會自行關掉反射光", "D 地球每個月都會擋住所有照向月球的陽光"], "A", "新月時月球仍有朝向太陽的受光半球，只是朝向地球的一面多為背光面，且月球在天空中接近太陽方向，所以不易看見。"),
    ("觀測日誌記錄第 7 天為上弦月、第 14 天為滿月。根據這筆資料，哪個結論受到支持？", ["A 完整月相週期恰好是 14 天", "B 這筆紀錄中，上弦月到滿月約相隔四分之一個月相週期", "C 月球到滿月時會停止公轉", "D 每個月相永遠只維持一天"], "B", "資料顯示兩個月相相隔約七天，可作為約四分之一月相週期的近似；它不能證明完整週期是 14 天，也不能推出每個月相只有一天。"),
    ("學生連續幾晚在同一時刻觀察，發現月球出現在天空的不同位置。哪個因素與這項位移最直接相關？", ["A 月球繞地球公轉，而地球也在自轉", "B 月球每天改變質量", "C 太陽每天會熄滅幾小時", "D 星星把月球隨機推到不同位置"], "A", "月球公轉會改變它相對地球的位置，地球自轉則造成一天內的視運動；規律的逐夜位移不是質量改變或隨機推動的證據。"),
    ("用燈、球和小珠分別代表太陽、地球和月球。把小珠繞著球移動時，應觀察什麼現象來模擬月相？", ["A 小珠的顏色自行改變", "B 從球的位置看，小珠受燈照亮部分的可見比例改變", "C 小珠在球後方時，燈會自行變亮", "D 球會把光線射回燈"], "B", "燈代表太陽，固定照亮小珠的一半；小珠位置改變後，從地球位置看見的受光比例不同，這就是月相變化的幾何核心。"),
    ("學生用望遠鏡拍攝月球，第一張照片右側較亮，三天後第二張照片左側較亮。哪個解釋最有根據？", ["A 月球受光半球隨公轉位置改變，因此地球看到的亮面方向改變", "B 太陽消失又重新出現，才造成亮面轉移", "C 望遠鏡把月球的公轉方向反轉", "D 月球固體表面從右側搬到左側"], "A", "太陽持續照亮月球，月球公轉改變觀察幾何，使地球看見的受光部分改變；這不是月面固體左右搬移，也不需要假設太陽熄滅。"),
    ("為什麼地球上的觀測者不會在每一次滿月都看到月食？", ["A 滿月時月球不會反射太陽光", "B 月球軌道略有傾角，多數滿月時日、地、月沒有精確排列，月球會從地影上方或下方通過", "C 滿月只會在白天出現", "D 地球沒有影子"], "B", "月食除了需要滿月，還需要月球通過地球影子；月球軌道有傾角，因此多數滿月時三者沒有精確成一直線。"),
    ("班級比較一個月內不同時間繪製的月球觀測圖。哪種做法最能支持「月相會重複變化」的結論？", ["A 每張圖都記錄日期、時間、地點、天候與亮面形狀", "B 只保留畫得最漂亮的一張", "C 每晚改變觀測時間卻不記錄", "D 先決定月相名稱再看圖"], "A", "完整且可追溯的觀測紀錄，才能辨認重複模式並區分觀察與解釋；只留漂亮圖、改變時間不記錄或先猜答案都會造成偏差。"),
]

for question, (prompt, options, answer, explanation) in zip(Q, LOCALIZED):
    question["prompt"] = prompt
    question["options"] = [{"id": option[0], "text": option[2:]} for option in options]
    question["answer"]["value"] = answer
    question["answer"]["explanation"] = explanation

# 分散正確選項位置，避免學生只靠固定字母猜答；重新排列後同步修正解法最後一步。
target_letters = {1: "C", 3: "D", 5: "C", 7: "D", 9: "C"}
for index, target in target_letters.items():
    question = Q[index]
    old = question["answer"]["value"]
    correct = next(option for option in question["options"] if option["id"] == old)
    wrong = [option for option in question["options"] if option["id"] != old]
    order = [letter for letter in "ABCD" if letter != target]
    reordered = [wrong[0], wrong[1], wrong[2], correct]
    question["options"] = [{"id": letter, "text": option["text"]} for letter, option in zip(order + [target], reordered)]
    question["answer"]["value"] = target
    question["solutionSteps"][-1] = question["solutionSteps"][-1].replace(f"選 {old}", f"選 {target}")

for question in Q:
    (OUT / f"{question['id']}.json").write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(Q)} questions")

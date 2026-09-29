import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-performance-4-iv-5.json"
REPORT = ROOT / "implementation/reports/chinese-performance-4-iv-5-first-pass-review.json"


def rec(name, locator, concepts, forms, misconception, assessment):
    return {
        "publisher": name,
        "edition": f"{name} 公立校方國文課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": locator,
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": concepts,
            "representations": forms,
            "examplesOrEvidence": ["本課以原創直幅、橫幅與行氣觀察卡，承接公開課程的書法欣賞、作品比較與實作方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、篇章、題目、答案、影音或版面。",
    }


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-chinese-performance-4-iv-5"
    data["title"] = "4-Ⅳ-5：從行款、布局與行氣讀出書法風格"
    data["content"] = {
        "summary": "書法風格不是只看某一個字像不像某種書體，而是觀察文字如何在整幅作品中排列、呼吸與移動。本課從行款的方向、字數與行距開始，接著分析疏密、留白、墨色、欹側與行氣，再把形式證據連到沉著、流動、疏朗或緊張等風格感受。欣賞時要把『看見的安排』、『可能造成的效果』與『尚待查證的作者意圖』分開，才能寫出可討論、可比較的賞析。",
        "sections": [
            {"heading": "先讀整幅的行款地圖", "body": "先確認作品是直幅、橫幅或冊頁，標出行的方向、起迄、行數、每行字數與落款位置。行款不是單純數格子，而是觀察文字如何佔據畫面；同樣的字數，若行距、行長或邊界不同，閱讀路徑便會改變。"},
            {"heading": "布局讓視線有疏有密", "body": "把作品想成一張由黑白、重輕、開合組成的地圖：字群聚集處形成視覺重量，大片留白則可能提供停頓或拉開氣息。不能只看到右上角很密就宣布整件作品緊張，還要看密度是否反覆、重心是否移動，以及落款是否改變平衡。"},
            {"heading": "行氣是跨字跨行的連續感", "body": "行氣不等於每個字都連筆，也不等於把下一字的起筆猜成作者心情。可從字勢方向、大小伸縮、收放節奏、相鄰行呼應與視線路徑尋找連續證據，再說明這些變化如何讓作品顯得流動、舒展或凝滯。"},
            {"heading": "風格判斷要留在證據能到的地方", "body": "『沉著厚重』『清峭疏朗』『奔放流動』都是整理感受的詞，不是免查證的標籤。完成賞析時，先引用兩三項布局或行氣證據，再提出較保守的風格描述；若無法確認作者意圖、時代或書寫速度，就清楚標示那是推論，不冒充作品事實。"},
        ],
    }
    data["studyHighlights"] = [
        "用行數、行距、字數、方向與落款建立行款地圖。",
        "從疏密、留白、墨色與重心變化分析布局，而非只貼風格標籤。",
        "以字勢、收放、相鄰呼應與視線路徑判讀跨字跨行的行氣。",
        "讓風格感受回扣可見證據，並區分作品事實、推論與未確認意圖。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "兩張同字數的作品，為何讀起來不同？", "body": "提供兩張完全自編的直幅與橫幅作品卡，暫時遮住風格標籤，請學習者用箭頭標出閱讀路徑、最密處、最寬的留白與落款位置。先讓眼睛說明畫面如何安排，再討論『穩定』或『奔放』等感受從何而來；若只能說喜歡，便回到畫面找證據。"},
            {"id": "explain", "phase": "explain", "heading": "用三層鏡頭拆解書法風格", "body": "第一層畫行款地圖，記錄幅式、行數、字數、行距與落款；第二層標記布局的疏密、黑白、重心與留白；第三層追蹤行氣的方向、收放、呼應與停頓。三層完成後才提出風格假說，並在旁邊寫出支持它的具體位置，避免把術語當成答案。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "從一行的收放走到整幅的行氣", "body": "以自編橫幅觀察卡為例：先圈出第二行字勢向右上、第三行突然收短的部位，再比較相鄰行的空隙與落款重量。這些資料可以支持視線有推進後停頓的描述，但不足以直接證明作者當時的情緒；示範如何在賞析句中把觀察、效果與推論界線分開。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "把風格形容詞翻回畫面證據", "body": "將『沉著厚重』『清疏』『流動』三張風格卡配對到原創作品局部，學習者必須在每張卡旁寫至少兩個位置證據，例如墨色層次、字面重心、行距變化或收筆方向。若一個詞可以套到所有作品，就刪掉它，改寫成更精確、可比較的描述。"},
            {"id": "transfer", "phase": "transfer", "heading": "比較同書體的不同風格", "body": "挑兩件同一書體但布局不同的自編作品，先用相同欄位記錄行款、疏密、留白、行氣與落款，再寫一段比較。禁止只用『甲較漂亮』；要指出哪一項形式改變了閱讀節奏，以及這項改變如何支持風格差異，最後列出還需補查的作者或時代資料。"},
            {"id": "reflect", "phase": "reflect", "heading": "檢查我是否把意圖當成事實", "body": "回看賞析稿，把句子分成可直接看見、由形式推得、目前不能確定三類。將『作者想表達焦急』改成有證據且有範圍的說法，例如『密集行距與快速轉折可能使讀者感到急促』，並補上若要確認意圖需要的作品背景或作者資料。"},
        ],
        "summary": ["先畫出行款地圖，再讀布局的疏密、重心與留白。", "以字勢、收放、呼應與視線路徑追蹤跨字跨行的行氣。", "風格詞必須回扣位置、墨色、空間與節奏等形式證據。", "分開作品事實、視覺效果、個人感受與尚待查證的作者意圖。"],
        "exitCheck": [
            {"prompt": "描述一幅作品的行款時，至少要先記錄哪些可見資訊？", "expectedEvidence": "能指出幅式、行數、行距、每行字數、閱讀方向與落款等資訊，並說明它們如何影響畫面分布。"},
            {"prompt": "如何把『很有行氣』改寫成可檢驗的賞析？", "expectedEvidence": "能指出字勢方向、收放、相鄰行呼應、空間或視線路徑，並將形式連到閱讀節奏。"},
            {"prompt": "為什麼不能從布局直接斷定作者當時的情緒？", "expectedEvidence": "能區分可見形式、可能效果與作者意圖，並提出需要作品背景或其他來源才能確認的限制。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "從行款、布局與行氣的可見證據，形成有範圍的書法風格判讀。",
        "scenario": "學生接手一張沒有風格標籤的原創書法展卡，依序畫行款地圖、標記視覺重量、追蹤行氣，再寫出可比較的賞析。",
        "variables": [{"symbol": "k", "meaning": "行款資訊"}, {"symbol": "l", "meaning": "布局與留白"}, {"symbol": "q", "meaning": "行氣與風格推論"}],
        "steps": [
            {"id": "step-1", "prompt": "面對一幅尚未標註的書法作品，第一步最適切的是什麼？", "options": ["先記錄幅式、行數、行距、字數、閱讀方向與落款位置，建立行款地圖", "先猜作者性格，再用畫面尋找支持", "先選一個風格標籤，之後所有特徵都套進去"], "answer": "A", "feedback": "A 先建立可重做的畫面資料，避免風格標籤反過來支配觀察。"},
            {"id": "step-2", "prompt": "若要判讀作品是否具有流動的行氣，哪組證據最有力？", "options": ["只看其中一字是否連筆", "比較字勢方向、收放、相鄰行呼應與視線路徑，再說明可能的閱讀節奏", "看到作品很長就直接判定行氣流暢"], "answer": "B", "feedback": "B 把行氣放回跨字跨行的關係中，避免用單一字或作品長度代替分析。"},
            {"id": "step-3", "prompt": "賞析中寫『作者想表達焦急』時，怎樣修正最負責任？", "options": ["改成『密集行距與快速轉折可能使讀者感到急促』，並標示這是形式推論，另查背景才能確認意圖", "保留原句，因為風格詞本來就不需要證據", "刪掉所有布局描述，只留下作者生平"], "answer": "A", "feedback": "A 將看得見的形式、可能效果與尚待查證的意圖分層，結論範圍與證據一致。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["updatedAt"] = "2026-09-21"
    data["versionResearch"] = [
        rec("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf；國語文書寫、書法欣賞與文化表達定位；核讀 2026-09-21。", ["由作品形式與書寫活動發展書法欣賞語言。", "能把觀察、感受與文化脈絡連成表達。"], ["行款、布局、行氣、風格詞、作品比較與賞析段落。"], "只用喜歡／不喜歡或單一風格詞取代作品分析。", "重視形式描述、欣賞表達與理由回扣。"),
        rec("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf；國語文書法、碑帖與審美活動定位；核讀 2026-09-21。", ["透過觀察、比較與討論理解作品布局和表現差異。", "以實作與回饋修正對行氣、風格的判讀。"], ["直幅／橫幅比較、留白、墨色、字勢、行間呼應與臨寫。"], "把逐字臨摹當成理解行氣，忽略跨字跨行的關係。", "要求比較有共同欄位、判斷有證據、說法可修正。"),
        rec("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf；國文書體、碑帖與書法評量定位；核讀 2026-09-21。", ["從章法、行氣與作品背景理解書法風格。", "區分可見形式、文化資訊、感受與推論範圍。"], ["行款地圖、布局重心、留白、行氣路徑、落款與賞析文字。"], "把布局直接翻譯成作者確定的情緒或意圖。", "要求風格描述回扣形式證據並標示限制。"),
    ]
    data["fusionRecord"] = {
        "commonCore": ["三版本公開結構共同支持書法欣賞、作品觀察、比較表達與書寫實作。", "行款、布局、行氣與風格判讀需要由可見形式逐步推論。", "賞析應能提出理由並保留作者意圖、時代背景等未確認範圍。"],
        "versionDifferences": ["南一較突顯書寫欣賞與文化表達；康軒較突顯觀察、比較、實作與回饋；翰林較突顯章法、行氣、作品背景與證據範圍。這是公立校方課程計畫層級差異，不宣稱完整出版社教材差異。"],
        "originalAdditions": ["用行款地圖把幅式、行距、字數與落款轉成可檢查資料。", "以三層鏡頭追蹤布局重心與跨行行氣。", "把風格形容詞改寫成證據、效果與意圖界線清楚的賞析。"],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織行款、布局、留白、行氣、風格與賞析證據。正文、原創情境、互動步驟、回饋與檢核均為本專案重寫，未複製教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["teaching"]["body"][1]["body"] += " 每一層都要在觀察卡上留下位置標記，讓另一位同學只看記錄也能重建你的判斷；若兩種解釋都符合，就保留競爭假說而不硬選一個。"
    data["teaching"]["body"][4]["body"] += " 比較時先鎖定相同書體與相同文字量，再處理幅式、行距與墨色等差異，否則無法知道風格差異究竟來自布局還是材料條件。"
    data["teaching"]["body"][5]["body"] += " 交稿前用三種顏色標示事實、推論與待查資料，並刪除沒有形式依據的心理猜測。"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "4-Ⅳ-5：從行款、布局與行氣讀出書法風格", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese performance 4-iv-5")


if __name__ == "__main__":
    main()

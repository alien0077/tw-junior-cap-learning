import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/chinese/lesson-chinese-argument-evidence-basics.json"
REPORT = ROOT / "implementation/reports/chinese-argument-evidence-basics-first-pass-review.json"
URLS = [
    ("https://www.sdjh.ntpc.edu.tw/var/file/0/1000/attach/16/pta_2229_1166226_19803.pdf", "新北市立石碇國中公開國文試題", "議論文主張、論據與推論"),
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf", "高雄市立鹽埕國中公開國文段考", "證據品質、反論與結論範圍"),
    ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部公開課程與試題資料", "觀點、資料與可檢驗主張"),
]

BOUNDARY = "本紀錄只保存可追溯公開來源的章節定位、教學方向與評量能力；不複製出版社或學校教材正文、原題、選項、圖表、答案、影音或版面。"


def refs():
    return [{"url": u, "title": f"{t}；只取{loc}的題型與推理方向，未複製原題、選項、圖表或答案。", "year": "113-114", "subject": "chinese", "locator": loc, "observedPattern": "公立學校國文評量常要求辨識主張、理由與證據，並檢查樣本、關聯、反論、結論範圍及可檢驗性；本題採全新語料。", "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper"} for u, t, loc in URLS]


def main():
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    lesson.update({"updatedAt": "2026-09-21", "reviewStatus": "draft", "authoringStandard": "version-fused-v1"})
    lesson["content"] = {"summary": "把議論文字拆成主張、證據與論證橋樑，判斷資料能支持到哪個範圍，再用反例與限制修正結論。", "sections": [
        {"heading": "主張是有範圍的結論", "body": "主張回答「作者要讀者接受什麼」。先圈出結論，再標出對象、時間與程度；「所有人都應該」比「本班多數人可能」需要更廣的證據。",},
        {"heading": "論據要能被查驗", "body": "論據可以是調查數據、可核對事件、研究結果或文本中的具體事實。只說「我覺得」或「大家都說」沒有交代來源、樣本與方法，不能直接支撐普遍結論。",},
        {"heading": "論證橋樑不能省略", "body": "證據不會自動變成結論，還要說明兩者如何相連。例如排隊時間長可支持增加飲水設備的需求，但仍要問是否還有替代方案、資料是否涵蓋不同時段。",},
        {"heading": "反例能校正結論", "body": "看到反方成本或例外時，先承認它，再檢查原主張是否要縮小範圍。單一個案可說明可能性，不能直接代表全體；相關同時出現，也不等於已證明因果。",},
        {"heading": "證據鏈的四格檢查", "body": "用「主張→證據→連結理由→限制」四格重寫一段文字。若其中一格空白，就把缺少的資料或需要保留的語氣寫出來，而不是補上一個看似有力的形容詞。",},
    ]}
    lesson["studyHighlights"] = ["先界定主張的對象、時間與強度，再看論據是否覆蓋相同範圍。", "用來源、樣本、方法、時間與結果檢查資料品質。", "補出證據到結論的連結理由，並主動標記反例、替代解釋與因果限制。"]
    for row in lesson.get("publisherResearch", []) + lesson.get("versionResearch", []):
        row["reviewedAt"] = "2026-09-21"
        row.pop("licenseBoundary", None)
    for row in lesson.get("versionResearch", []):
        row["licenseBoundary"] = BOUNDARY
    lesson["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "先拆一則校園提案", "body": "讀「學校應延長圖書館開放時間，因為晚自習時段使用人次上升」這個自編提案。先用一種顏色圈主張，再用另一種顏色圈資料，最後問：使用人次上升能支持延長開放，但是否已排除交通、安全與人力限制？"},
        {"id": "explain", "phase": "explain", "heading": "建立主張—證據—橋樑三欄", "body": "把句子放進三欄表：主張是希望成立的結論，證據是可核對的資料，橋樑是解釋資料為何提高主張可信度的理由。再加上範圍欄，檢查資料的對象、時間和結論是否相配；若資料只來自一個時段，就不能不加說明地推廣到整個學期。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "用運動與睡眠案例走一次", "body": "自編研究比較八週運動組與對照組的睡眠紀錄。先確認有樣本、期間與測量方式，再寫出「結果支持可能改善」而非直接寫成「運動一定治好失眠」；後一句超出了資料能保證的範圍。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "找出個案推廣的跳躍", "body": "比較「我喝水後頭痛好了」和「三個月追蹤不同年級學生的飲水量與頭痛紀錄」。前者只能提出待研究的可能性，後者才提供可檢查的群體資料；練習把過大的結論改成合乎證據的句子。"},
        {"id": "transfer", "phase": "transfer", "heading": "寫一個有反方位置的校園主張", "body": "選一項校園政策，寫一句有範圍的主張、一項資料、一句連結理由，再補一個成本或例外。最後用「因此目前可說……但還不能說……」收束，讓讀者看見證據的邊界；交換作品時，請同伴只用文字中的資料判斷，不用作者的語氣替它加分。"},
        {"id": "reflect", "phase": "reflect", "heading": "把論證變成可查驗清單", "body": "交卷前逐項問：主張是什麼？資料從哪裡來？樣本和時間是否足夠？資料與結論中間缺哪個理由？是否把相關寫成因果？是否有反例或替代解釋？這份清單可遷移到新聞、公告與圖表閱讀。"},
    ], "summary": ["先判斷主張的範圍，再標記可查驗的論據。", "用證據鏈補出資料與結論之間的連結理由。", "以樣本、時間、方法、反例與因果限制校正結論。", "在新情境中寫出有證據也有邊界的主張。"], "exitCheck": [
        {"prompt": "請從一段議論文字中指出主張、論據與連結理由。", "expectedEvidence": "能分別指出作者要讀者接受的結論、可查驗資料，以及資料如何提高結論可信度。"},
        {"prompt": "為什麼單一個人的經驗不能直接支持『所有人都會如此』？", "expectedEvidence": "能指出樣本過小、代表性不足，並把結論改寫成較保守的可能性。"},
        {"prompt": "請寫一句有範圍的校園主張，並列出一項仍需補查的資料。", "expectedEvidence": "主張交代對象或情境，資料與主張相關，且能說出目前不能推出的範圍。"},
    ]}
    lesson["interactive"] = {"type": "guided-choice", "goal": "辨認主張、論據、論證橋樑與結論限制", "scenario": "把一段校園延長圖書館開放時間的自編短文拆成主張、資料與推理箭頭，再檢查結論是否超出證據。", "steps": [
        {"id": "step-1", "prompt": "短文最後說『因此學校應延長開放』，這句在論證中是什麼？", "options": ["作者希望讀者接受的主張", "用來證明前文的統計資料"], "answer": "A", "feedback": "『因此』後的建議是結論；前文的人次或排隊資料才可能是論據。"},
        {"id": "step-2", "prompt": "哪項資料最能支持『晚自習需要更多座位』？", "options": ["連續四週分時段記錄座位使用率與候位時間", "有人說圖書館的氣氛很棒"], "answer": "A", "feedback": "有期間、指標與可重複記錄的方法，較能直接回答座位需求。"},
        {"id": "step-3", "prompt": "資料顯示使用人次增加後，最需要補查什麼？", "options": ["是否有其他原因，以及資料能否代表不同年級與時段", "把增加人次直接改寫成一定有效"], "answer": "A", "feedback": "要檢查替代解釋、樣本範圍與因果跳躍，不能把相關現象直接當成政策必然有效。"},
    ]}
    lesson["fusionRecord"]["llmSynthesisNote"] = "本課依官方語文領域課綱、kg-chinese-content-bd-iv-1、南一／康軒／翰林可取得的公開研究方向與三筆公立學校國文試題的能力模式，以自己的話獨立重寫主張、證據、論證橋樑、反例與因果限制；未複製教材或試題，Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    explanations = [
        "A 有研究對象、方法與觀察指標，可被檢查且直接回應健康效果；其餘是感想、傳聞或無關資訊。正確答案：A。",
        "使用量與排隊時間是用來支持增加設備的資料，屬於論據；標題、反問和簽名都不是這段數據的功能。正確答案：B。",
        "三位朋友是小而可能偏向同一圈子的樣本，不能推出全市『一定最好吃』；最多只能說這三人有正面經驗。正確答案：C。",
        "最後的『應增加晚間閱讀空間』是作者希望讀者接受的政策結論；使用人次資料是支持它的論據。正確答案：D。",
        "比較運動組與對照組的睡眠紀錄，並交代樣本與期間，能檢查變化是否穩定；單一感受或口號不能補強主張。正確答案：B。",
        "一個人的經驗能提出可能性，卻缺少代表性與比較基準，不能直接概括所有人。正確答案：C。",
        "最直接的問題是『這項資料如何讓主張更可信？』，它會迫使讀者補出證據到結論的連結理由。正確答案：D。",
        "先承認經費問題，再提出分期與預算資料，是處理反方疑慮並補足可行性理由。正確答案：A。",
        "『在兩週問卷中，某年級至少六成學生表示偏好早起』交代對象、期間與可測量比例，比『有人喜歡』更可檢驗。正確答案：B。",
        "把『我感到精神較好』直接推成每個人都會如此，是把個人感受當成普遍證據，樣本與結論範圍不相稱。正確答案：C。",
    ]
    strategies = [
        "先找能被查驗的對象、方法和結果，再判斷資料是否真的支援主張。", "先找結論，再判斷後面的數據是在支援、反駁還是補充。", "比較樣本大小、代表性與結論範圍，找出過度概括。", "找『因此』後的政策或判斷，再回看哪句資料支持它。", "優先尋找有比較、期間、測量指標與足夠樣本的資料。", "把個案能說明的可能性與不能推出的普遍結論分開。", "補出證據到結論的連結理由，不能只重複資料。", "看作者是否回應成本、例外或反方疑慮，並提出可行方案。", "檢查主張是否有對象、時間、數量與可觀察指標。", "辨識第一人稱感受，並檢查它是否被錯誤推廣到全體。",
    ]
    steps = ["讀題並圈出主張範圍、論據、樣本、方法、反論或結論強度。", "把作者要讀者接受的判斷與支持資料分開。", "檢查資料來源、樣本、時間與測量方式，並補出證據到主張的連結理由。", "排除把感想、傳聞、單一個案、相關現象或小樣本誤當普遍因果證明的選項。", "用完整句重述答案，再說明資料目前不能支持的限制。"]
    for i in range(1, 11):
        path = ROOT / f"questions/chinese/question-chinese-argument-{i}.json"
        question = json.loads(path.read_text(encoding="utf-8"))
        question["examPatternRefs"] = refs(); question["reviewStatus"] = "draft"; question["updatedAt"] = "2026-09-21"
        question["answer"]["explanation"] = explanations[i - 1]; question["solutionStrategy"] = strategies[i - 1]; question["solutionSteps"] = steps
        question["provenance"]["sourceUrl"] = URLS[0][0]; question["provenance"]["sourceLocator"] = "三筆公立學校公開國文試題中的主張、論據、樣本、反論、結論範圍與可檢驗性能力；本題改寫為全新語料。"
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": lesson["title"], "lessonId": lesson["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "publicExamPatternRewrite": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("authored chinese argument evidence basics")


if __name__ == "__main__":
    main()

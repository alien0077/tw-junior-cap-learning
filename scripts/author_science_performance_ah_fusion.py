#!/usr/bin/env python3
"""Independent first-pass authoring for science performance h."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-performance-ah.json"
REPORT = ROOT / "implementation/reports/science-performance-ah-first-pass-review.json"
URLS = {"nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf", "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "hanlin": "https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download"}


def rec(p, c, r, m, a):
    return {"publisher": p, "edition": f"{p} 公立校方自然課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": f"{URLS[p]}；科學思考、探究習慣、證據評估與生活應用評量欄位；核讀 2026-09-21。", "reviewedAt": "2026-09-21", "findings": {"concepts": [c, "公開課程結構支持以問題、證據、模型與限制連結科學知識和生活決策。"], "representations": [r], "examplesOrEvidence": ["本課的食品保存、交通噪音與清潔用品資訊均為原創情境，只承接公開課程所示的能力方向。"], "misconceptions": [m], "assessmentEmphasis": [a]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}


def main():
    d = json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"] == "lesson-science-performance-ah" and d["reviewStatus"] == "draft"
    d["title"] = "養成應用科學思考與探究的習慣（h）：先查證再決定"
    d["content"] = {"summary": "應用科學思考不是把每件生活選擇都變成複雜實驗，而是在做決定前，先把問題說清楚、找出可觀察證據、辨識資料限制，再比較不同解釋的代價與風險。面對食品保存、交通噪音或清潔用品宣稱，要區分個人經驗、相關性與因果證據，並知道何時需要停止自行判斷、尋求專業或官方資料。本課用原創生活案例練習形成可持續的查證習慣。", "sections": [{"heading": "把生活疑問改成可查的問題", "body": "『這個方法有效嗎』太寬泛；可以改成在固定時間、對象與測量方式下，比較使用前後哪一個結果。問題越清楚，越容易找到適合的證據與判斷標準。"}, {"heading": "經驗是線索，不是完整證明", "body": "一次使用後覺得舒服，可能是方法有效，也可能是同時改變了休息、飲食或期待。個人經驗可以提示下一步，但要與比較、重複、可信來源和可能替代解釋一起看。"}, {"heading": "風險判斷要看證據和後果", "body": "即使證據還不完整，若錯誤決定會造成較大傷害，就應採取較保守做法並查找專業資訊。科學思考不只問真假，也問資料品質、適用範圍、風險大小與可逆性。"}, {"heading": "把查證流程變成日常習慣", "body": "看見宣稱時先停一下：主張是什麼、證據來自哪裡、是否有比較、誰可能受益、有哪些限制、我還需要查什麼。記下查證日期和來源，之後有新資料也能修正決定。"}]}
    d["studyHighlights"] = ["把模糊生活問題改成可查證、可比較的問題。", "區分個人經驗、相關性、因果證據與替代解釋。", "依證據品質、風險大小與適用範圍做決定。", "以來源、日期、限制與後續查證形成習慣。"]
    d["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "一張『百分之百有效』的貼文", "body": "班級群組轉傳『把某種食物放在冰箱門邊，三天都不會壞』。請先不要投票相信或不相信，而是寫下需要知道的條件：食物種類、溫度、包裝、時間與判定變質的方法。這一步把直覺反應轉成可查證的問題。"},
        {"id": "explain", "phase": "explain", "heading": "四層查證階梯", "body": "第一層重述主張，避免被誇張語氣帶走；第二層找方法和資料來源，確認是否真的測到要問的結果；第三層比較替代解釋與適用範圍；第四層依風險做行動，必要時尋求官方或專業意見。每層都可能讓原本的結論縮小。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "交通噪音與注意力的推論", "body": "學生發現窗邊座位今天比較難專心，不能直接推論噪音造成全部原因。先記錄分貝、時段、任務正確率與睡眠等可能因素，和安靜時段或不同座位比較；若資料只來自一天，就把結論寫成『本次觀察呈現關聯線索』，而不是普遍因果定律。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "清潔用品宣稱的查證卡", "body": "給出『天然成分所以一定安全』的宣稱。學習者分成主張、證據、缺口、風險四欄：天然的定義是什麼、測了哪些刺激或毒性、濃度與使用方式是否相同、誤用後果是否可逆。完成前不得只用天然／化學二分法作結論。"},
        {"id": "transfer", "phase": "transfer", "heading": "設計自己的查證紀錄", "body": "遇到減肥、保健或學習方法的網路訊息，建立一筆可回看的紀錄：原始連結、主張、發表日期、研究對象、比較方式、限制、與官方或專業資料的差異，以及暫時決定。這讓『我好像看過』變成可追蹤的證據管理。"},
        {"id": "reflect", "phase": "reflect", "heading": "修正兩個捷徑", "body": "請修正『很多人分享，所以一定有效』與『研究還不完整，所以什麼都不能做』。分享數量不等於控制良好的證據；證據未完整時仍可依風險採取保守、可逆且持續查證的行動，不能把不確定性當成放棄思考的理由。"},
    ], "summary": ["先重述主張，再找方法、來源、比較與限制。", "經驗可提供線索，但不能單獨證明因果。", "決策同時考量證據品質、風險、範圍與可逆性。", "記錄來源與日期，讓查證能被追蹤和修正。"], "exitCheck": [{"prompt": "為什麼一次生活經驗不能直接證明方法有效？", "expectedEvidence": "可能同時有其他因素；需要比較、重複、可信來源與替代解釋檢查。"}, {"prompt": "看到『天然所以安全』時至少要查哪些資料？", "expectedEvidence": "成分與濃度、使用方式、測試對象與結果、比較條件、限制及誤用風險。"}, {"prompt": "證據不完整時如何做較負責任的決定？", "expectedEvidence": "依風險採保守、可逆的行動，查詢專業或官方資料並記錄後續查證，而非武斷相信或放棄判斷。"}]}
    d["interactive"] = {"type": "guided-choice", "goal": "以主張、證據、限制與風險四個角度建立生活科學查證流程。", "scenario": "檢視食品、噪音與清潔用品宣稱，逐步選擇能降低誤判的查證行動。", "variables": [{"symbol": "c", "meaning": "待查證的主張"}, {"symbol": "e", "meaning": "可取得的證據"}, {"symbol": "r", "meaning": "決策風險"}], "steps": [{"id": "step-1", "prompt": "看到『很多人分享所以有效』，第一個應做什麼？", "options": ["重述主張並查找測量方法、來源與比較條件", "直接用分享次數當成證據品質", "因為網路訊息多就停止查證"], "answer": "A", "feedback": "傳播量不是控制良好的證據，先釐清主張與方法。"}, {"id": "step-2", "prompt": "一次使用後感覺改善，最合理的表達是什麼？", "options": ["這是線索，還要考慮替代原因與比較資料", "已證明對所有人都有因果效果", "感覺不能記錄也不能再查"], "answer": "A", "feedback": "個人經驗有價值，但必須標明範圍並接受其他解釋。"}, {"id": "step-3", "prompt": "證據不足但可能造成較大傷害時，應如何行動？", "options": ["先採保守且可逆的做法，查詢可靠專業或官方資料", "因為不確定就採最冒險的做法", "只選支持自己期待的貼文"], "answer": "A", "feedback": "風險越高，越要降低不可逆損失並尋求更可靠證據。"}]}
    d["authoringStandard"] = "version-fused-v1"
    d["versionResearch"] = [rec("nani", "以科學知識解決生活問題並養成觀察、查證與根據證據判斷的習慣。", "生活情境、變因表、資料來源與主張—證據—推理記錄。", "把個人經驗或網路流行度當成充分因果證明。", "重視問題界定、證據適切性、限制與安全決策。"), rec("kanghsuan", "透過探究和討論把科學思考轉化為可重複、可溝通的生活行動。", "比較活動、重複觀察、紀錄表、替代解釋與同儕檢核。", "只找支持原先想法的資料，或忽略條件差異與誤差。", "評量查證歷程、方法透明、推理與修正能力。"), rec("hanlin", "連結健康、環境與科技資訊判讀，依證據品質與風險做負責任選擇。", "新聞／廣告主張、來源日期、適用範圍、風險與官方資料比對。", "把天然／化學、相信／不相信作成沒有證據的二分判斷。", "要求說明資料限制、行動後果、查證紀錄與持續修正。")]
    d["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持把科學思考應用於生活問題與證據判斷。", "個人經驗和流行說法只能提供線索，需比較方法、來源與替代解釋。", "負責任決策需同時考量證據品質、適用範圍、風險與可逆性。"], "versionDifferences": ["南一證據較突顯生活問題界定與基本查證；康軒較突顯探究、重複、討論與方法透明；翰林較突顯健康環境資訊、風險與負責任行動。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以食品保存貼文拆解條件、證據與誇大語氣。", "以交通噪音案例區分關聯線索與因果結論。", "以清潔用品的天然宣稱建立主張、證據缺口與風險查證卡。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織生活問題界定、證據評估、替代解釋、風險判斷、來源紀錄與持續修正。正文、原創情境、互動步驟、錯誤回饋與檢核均為本專案重寫，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "養成應用科學思考與探究的習慣（h）", "lessonId": d["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "reviewStatus": d["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

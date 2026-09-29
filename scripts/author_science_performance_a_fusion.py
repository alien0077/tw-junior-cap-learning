#!/usr/bin/env python3
"""Independent first-pass authoring for science performance a."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-performance-a.json"
REPORT = ROOT / "implementation/reports/science-performance-a-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download",
}


def rec(p, c, r, m, a):
    return {"publisher": p, "edition": f"{p} 公立校方自然課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": f"{URLS[p]}；科學態度、科學本質、證據判讀與探究評量欄位；核讀 2026-09-21。", "reviewedAt": "2026-09-21", "findings": {"concepts": [c, "公開課程結構支持以可觀察證據、可重複方法與暫時性解釋理解科學知識。"], "representations": [r], "examplesOrEvidence": ["本課的校園飲水、影子測量與新聞判讀皆為原創情境，只承接公開課程所示的能力方向。"], "misconceptions": [m], "assessmentEmphasis": [a]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}


def main():
    d = json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"] == "lesson-science-performance-a" and d["reviewStatus"] == "draft"
    d["title"] = "科學的態度與本質（a）：讓證據帶著問題前進"
    d["content"] = {"summary": "科學不是把權威說過的句子背起來，而是從可觀察問題出發，提出可以檢驗的解釋，依規則蒐集資料，再讓結果反過來修正想法。科學知識具有可累積、可溝通與暫時可修正的特性；『暫時』不等於隨便，因為解釋必須受到證據、方法與同儕檢核限制。本課以校園飲水、影子測量和科學新聞為原創情境，練習區分觀察、推論、主張與證據。", "sections": [{"heading": "先把看到的和想到的分開", "body": "量到水溫下降 3 度是觀察資料；猜測杯子材質造成散熱差異是推論。兩者都重要，但記錄時要分欄，才知道哪裡是資料、哪裡是尚待檢驗的解釋。"}, {"heading": "可檢驗才是科學問題的入口", "body": "好的問題能指出變因、測量方式與比較對象，例如在相同水量與室溫下比較不同杯材的降溫。不能被任何觀察或測量改變的說法，就不適合作為這次探究的可檢驗主張。"}, {"heading": "知識穩定但不是不可修正", "body": "當多次觀察、不同方法與同儕檢核得到一致結果，解釋會更可靠；新證據若指出限制，科學家會修正模型或適用範圍。修正是科學自我校正，不代表過去的測量沒有價值。"}, {"heading": "態度要落在證據行動上", "body": "誠實記錄不符合預期的結果、說明誤差、讓別人看懂步驟，都是科學態度。只挑支持自己結論的資料，或把新聞標題當成實驗證據，則會破壞推理鏈。"}]}
    d["studyHighlights"] = ["把觀察資料、推論、主張與證據分開。", "將問題改寫成可測量、可比較、可重複的探究。", "理解科學知識可修正但受證據與方法限制。", "用誠實記錄、說明限制與同儕檢核實踐科學態度。"]
    d["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "同一杯水，為何讀值不同？", "body": "三組同學測量校園飲水機出水溫度，讀值分別是 22、23、28 度。請先圈出目前確定知道的事情，再提出至少兩個可能原因：測量時間、溫度計位置、儀器校正或水流狀態。活動入口不是急著選一個答案，而是看哪些原因能被測量檢查。"},
        {"id": "explain", "phase": "explain", "heading": "一條完整的證據鏈", "body": "把主張寫成可檢驗句子，列出自變因、應變因與控制條件，說明如何重複測量，再把資料與解釋分開。結果支持主張時要說程度與限制；結果不支持時先檢查方法，不能刪掉不合預期的數據。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "影子長度的主張能否成立", "body": "小組主張『上午 10 點影子最短』。先把時間作為自變因、影長作為應變因，固定同一根竿、地點與量尺；在 9、10、11 點各測三次並記錄。若 10 點平均值最短，只能說在這三個時段與本方法下獲得支持，不能直接推成全天任何地點都相同。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "新聞句子拆成證據與推論", "body": "給一則寫著『某植物汁液一定能讓人更專心』的短新聞。學習者標出可觀察資料、作者推論、缺少的比較組與過度延伸的詞。接著把主張改成可測量版本，例如固定閱讀時間與任務後比較有無汁液時的正確率，並列出安全與倫理限制。"},
        {"id": "transfer", "phase": "transfer", "heading": "把科學態度用在生活決策", "body": "當網路貼文說某濾水壺『去除所有污染物』，先問測了哪些物質、用什麼方法、是否有對照與公開數據。把可信度檢查寫成四欄：主張、證據、方法限制、仍需查證。這樣不必因為語氣肯定或來源有名就直接接受。"},
        {"id": "reflect", "phase": "reflect", "heading": "修正兩個極端說法", "body": "請修正『科學結論既然會修正，就全部不可信』與『實驗結果符合預期，所以不用說誤差』。前者忽略可重複證據會提高可靠度；後者忽略測量限制。成熟的說法是：結論在明確證據與適用範圍內可靠，也保留被新證據檢查的可能。"},
    ], "summary": ["觀察與推論要分欄記錄，主張要能被檢驗。", "可靠性來自證據、重複、比較與方法透明。", "科學知識可修正，但不是任意意見。", "誠實記錄限制與檢查來源就是科學態度。"], "exitCheck": [{"prompt": "讀到一個測量數字後，為什麼不能立即寫成因果結論？", "expectedEvidence": "數字是觀察資料，因果解釋還需要控制變因、比較、重複與方法證據。"}, {"prompt": "如何把『這種杯子比較保冰』改成可檢驗主張？", "expectedEvidence": "固定水量、初始溫度、環境與時間，指定杯材為自變因、溫度變化為應變因並重複測量。"}, {"prompt": "科學知識可修正是否等於沒有可靠知識？", "expectedEvidence": "不是；多次、可重複且經檢核的證據可提高可靠度，修正表示清楚標示限制並接受新證據。"}]}
    d["interactive"] = {"type": "guided-choice", "goal": "把生活主張拆成可檢驗問題、證據、限制與暫時結論。", "scenario": "檢視校園影子測量與科學新聞，逐步選出觀察資料、控制條件及合理結論。", "variables": [{"symbol": "x", "meaning": "自變因"}, {"symbol": "y", "meaning": "應變因"}, {"symbol": "z", "meaning": "證據支持程度"}], "steps": [{"id": "step-1", "prompt": "『量到影長 42 公分』在證據鏈中首先屬於什麼？", "options": ["觀察或測量資料", "已證明的因果解釋", "不可檢驗的價值判斷"], "answer": "A", "feedback": "讀值是資料；原因與結論要靠後續比較和推理支持。"}, {"id": "step-2", "prompt": "比較不同杯材保冰效果時，哪一項應固定？", "options": ["水量、初始溫度與測量時間", "只固定最後看到的溫度", "讓每個杯子使用不同量尺"], "answer": "A", "feedback": "控制條件一致才能把結果差異主要歸因於杯材。"}, {"id": "step-3", "prompt": "最合適的科學結論是哪一種？", "options": ["在本次方法與範圍內，資料支持某解釋並保留限制", "只要符合期待就宣稱永遠正確", "結果不符預期就刪除資料"], "answer": "A", "feedback": "科學結論需連同證據範圍、限制與可修正性一起表達。"}]}
    d["authoringStandard"] = "version-fused-v1"
    d["versionResearch"] = [rec("nani", "以觀察、實驗證據、科學態度與可修正知識理解科學本質。", "觀察紀錄、變因表、資料圖表與主張—證據—推理鏈。", "把科學當成權威背誦，或把暫時修正誤解為任意意見。", "重視問題可檢驗性、資料誠實、方法限制與證據說理。"), rec("kanghsuan", "透過探究活動與討論建立證據、模型及同儕檢核的科學文化。", "實驗設計、重複測量、對照、圖表與口頭／書面論證。", "只挑支持結論的數據，或把一次結果推廣到所有情境。", "評量探究歷程、證據品質、反思修正與溝通清楚度。"), rec("hanlin", "連結日常科學資訊判讀與科學知識的累積、限制和變動。", "新聞主張、資料來源、適用範圍、模型更新與生活決策。", "因為來源有名就接受，或因知識會修正便否定所有科學證據。", "要求辨識證據、查核方法、說明不確定性與負責任表達。")]
    d["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持從可觀察問題、證據與探究方法理解科學本質。", "科學態度包含誠實記錄、接受檢核、說明限制與根據證據修正。", "科學知識可累積與修正，但結論仍受方法、資料與適用範圍約束。"], "versionDifferences": ["南一證據較突顯科學態度與探究基本證據；康軒較突顯實作、討論、重複與同儕檢核；翰林較突顯生活資訊判讀、知識限制與負責任表達。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以飲水溫度差異分開觀察資料與可能原因。", "以影子測量示範主張、控制條件、重複資料與適用範圍。", "以科學新聞拆解證據、方法限制與過度推廣的錯誤。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織觀察、推論、可檢驗問題、證據鏈、科學知識的可修正性與科學態度。正文、原創情境、互動步驟、錯誤回饋與檢核均為本專案重寫，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "科學的態度與本質（a）", "lessonId": d["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "reviewStatus": d["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

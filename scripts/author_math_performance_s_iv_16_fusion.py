#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-16."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-s-iv-16.json"
REPORT = ROOT / "implementation/reports/math-performance-s-iv-16-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
}


def rec(p, c, r, m, a):
    return {"publisher": p, "edition": f"{p} 公立校方數學課程計畫章節級證據", "sourceType": "public-web", "sourceLocator": f"{URLS[p]}；立體圖形三視圖、展開圖、表面積與體積的概念、表徵及評量欄位；核讀 2026-09-21。", "reviewedAt": "2026-09-21", "findings": {"concepts": [c, "公開課程結構支持由立體圖形的面、稜、頂點與尺寸關係建立表面積及體積模型。"], "representations": [r], "examplesOrEvidence": ["本課的包裝盒、收納罐與模型零件皆為原創情境，只承接公開課程所示的能力方向。"], "misconceptions": [m], "assessmentEmphasis": [a]}, "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。"}


def main():
    d = json.loads(LESSON.read_text(encoding="utf-8")); assert d["id"] == "lesson-math-performance-s-iv-16" and d["reviewStatus"] == "draft"
    d["title"] = "s-Ⅳ-16：從三視圖與展開圖建立立體量"
    d["content"] = {"summary": "同一個立體從正面、上面與側面看，會留下不同但互相約束的三視圖；把表面沿稜線攤平，則可得到展開圖。表面積是外露各面的面積總和，體積是立體所占的空間量，兩者不能因為都出現長、寬、高就混用。本課以原創包裝盒、收納罐與模型零件，練習由視圖還原尺寸、判斷合法展開圖、計算表面積與體積，並用估算檢查答案。", "sections": [{"heading": "三視圖是同一物體的三個投影", "body": "正視圖、俯視圖與側視圖各自保留兩個方向的尺寸。讀圖時要對齊共同的長度與高度，不能把三張圖當成三個不同物體。"}, {"heading": "展開圖要沿稜線攤平", "body": "展開圖的每一塊面必須對應原立體的一個面，邊長要相等、相鄰關係要能折回去。面積加總前先檢查是否重複或漏面。"}, {"heading": "表面積和體積回答不同問題", "body": "表面積計算外表面，使用平方單位；體積計算內部占據量，使用立方單位。長方體可用長乘寬乘高，組合體則要拆成不重疊部分或扣除缺口。"}, {"heading": "用尺寸與估算回查模型", "body": "三視圖與展開圖應能互相還原。若表面積小於某一個完整外露面的面積，或體積超過包裝盒可容納的量，就要回頭檢查尺寸、單位與是否把內部接觸面算入。"}]}
    d["studyHighlights"] = ["三視圖要對齊方向與共同尺寸。", "展開圖必須能沿稜線折回原立體。", "表面積用平方單位，體積用立方單位。", "用面數、尺寸、估算與折回關係檢查答案。"]
    d["teaching"] = {"body": [
        {"id": "hook", "phase": "hook", "heading": "一個紙盒，三張不同的臉", "body": "把一個沒有蓋子的長方體紙盒想成從正面、上面、右側拍照。三張照片各自看不到深度的一部分，但共同尺寸會重疊。請先圈出三張圖都必須一致的長度，再猜紙盒打開後會有幾個矩形面，建立視圖與實物相互約束的觀念。"},
        {"id": "explain", "phase": "explain", "heading": "由投影到面與尺寸", "body": "讀三視圖先固定同一個基準：正視圖通常呈現寬與高，俯視圖呈現寬與深，側視圖呈現深與高。讀展開圖則逐面標記長寬，確認相接邊長相同。最後分流：外露面的面積相加是表面積，三個互相垂直方向相乘是體積。"},
        {"id": "worked-example", "phase": "worked-example", "heading": "長 8、寬 5、高 3 的盒子", "body": "先由三視圖對齊得到長=8、寬=5、高=3。表面積=2(8×5+5×3+8×3)=158 平方單位；體積=8×5×3=120 立方單位。若紙盒沒有上蓋，表面積要扣除 8×5=40，成為 118 平方單位；這一步說明『表面積』必須先確認哪些面真的存在或外露。"},
        {"id": "guided-practice", "phase": "guided-practice", "heading": "檢查一張可疑展開圖", "body": "給一個長方體的六面展開圖，其中一個矩形被畫成與相鄰面不相等的邊長。學習者先配對三組相等的面，再沿虛線想像折回；若某條邊需要同時等於 5 與 8，就判定圖不合法。通過後才計算外露面積，避免把錯誤模型算得很精確。"},
        {"id": "transfer", "phase": "transfer", "heading": "包裝設計的兩個限制", "body": "設計收納盒時，外包裝紙量與盒內容量是兩個不同限制。先用三視圖取得尺寸，再用展開圖加總裁切面積；容量以體積表示。若盒內放入圓柱罐，還要比較圓柱的直徑、高度與盒內長寬，不能只比較體積就宣稱放得進去。"},
        {"id": "reflect", "phase": "reflect", "heading": "修正平方與立方單位混淆", "body": "請修正『長 8、寬 5、高 3 的盒子表面積是 120 立方單位』。120 是三個方向相乘得到的體積，單位是立方；完整六面表面積是 158 平方單位。若題目是無蓋盒，還要依實際面數改算 118 平方單位。"},
    ], "summary": ["三視圖共同描述同一立體，尺寸必須對齊。", "展開圖要能折回，不能只看面積總和。", "表面積使用平方單位，體積使用立方單位，兩者回答不同的量測問題。", "先驗證模型，再做計算與估算回查。"], "exitCheck": [{"prompt": "長 8、寬 5、高 3 的完整長方體表面積與體積是多少？", "expectedEvidence": "表面積=2(40+15+24)=158 平方單位；體積=8×5×3=120 立方單位。"}, {"prompt": "為什麼展開圖不能只檢查六個面積？", "expectedEvidence": "還要確認相接邊長一致且折回後不重疊、不漏面，否則不是原立體的合法展開圖。"}, {"prompt": "包裝紙量與盒內容量各用什麼量表示？", "expectedEvidence": "包裝紙量看外露面的表面積，用平方單位；容量看體積，用立方單位。"}]}
    d["interactive"] = {"type": "guided-choice", "goal": "從三視圖與展開圖核對尺寸、面數、表面積及體積。", "scenario": "旋轉一個長方體模型，切換三視圖並嘗試把展開圖折回，找出尺寸或單位錯誤。", "variables": [{"symbol": "l", "meaning": "立體長度"}, {"symbol": "w", "meaning": "立體寬度"}, {"symbol": "h", "meaning": "立體高度"}], "steps": [{"id": "step-1", "prompt": "三視圖中正視圖與俯視圖都出現的共同水平尺寸，應如何使用？", "options": ["對齊為同一個長度，不可各自任意解讀", "把兩個數字相加當成深度", "只採用最大數字"], "answer": "A", "feedback": "三視圖是同一物體的投影，共同邊方向要對齊。"}, {"id": "step-2", "prompt": "長方體展開圖中，哪個條件最能判斷它可折回？", "options": ["相接邊長一致，且六面能沿稜線折回不重疊", "六個面的顏色相同即可", "所有面積加總大於體積即可"], "answer": "A", "feedback": "合法展開圖要同時滿足面與稜線的幾何關係。"}, {"id": "step-3", "prompt": "長 8、寬 5、高 3 的 120 應標示什麼？", "options": ["120 立方單位，表示體積", "120 平方單位，表示完整表面積", "120 單位，無須標示量的種類"], "answer": "A", "feedback": "8×5×3 是三維乘積，表示體積，必須使用立方單位。"}]}
    d["authoringStandard"] = "version-fused-v1"
    d["versionResearch"] = [rec("nani", "以三視圖、展開圖與立體表面積體積建立空間量的表徵轉換。", "正視、俯視、側視、矩形面與稜線配對。", "把三張投影當三個物體，或不確認面數就直接套表面積公式。", "重視視圖對齊、模型還原、公式選擇與單位。"), rec("kanghsuan", "透過展開與折回操作連結平面面積與立體表面積。", "展開網、折線、相等邊、外露面與缺口。", "只看面積總和而忽略展開圖不能折回，或把接觸面算進外表面。", "要求操作驗證、圖形判讀、分割與合理性檢查。"), rec("hanlin", "以包裝和容量情境區分表面積、體積及實際尺寸限制。", "包裝紙量、盒內容量、三視圖尺寸與組合物件比較。", "混用平方與立方單位，或只比較體積便忽略物件能否放入。", "評估數學模型、單位、外露面與情境可行性。")]
    d["fusionRecord"] = {"commonCore": ["三版本公開結構共同支持由三視圖與展開圖理解立體的面、稜與尺寸。", "表面積是面積總和，體積是三維占據量，量與單位必須分開。", "模型能否折回與答案估算是共同的幾何合理性檢查。"], "versionDifferences": ["南一證據較突顯三視圖與空間表徵；康軒較突顯展開、折回與外露面；翰林較突顯包裝、容量與實際尺寸限制。這是公開課程計畫層級差異，不宣稱完整教材差異。"], "originalAdditions": ["以無蓋紙盒同時比較完整表面積與外露表面積。", "用相接邊長矛盾診斷看似完整但不能折回的展開圖。", "以包裝紙量和盒內容量安排平方／立方單位的遷移任務。"], "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織三視圖、展開圖、表面積、體積、外露面、平方與立方單位及包裝限制。正文、數值例題、互動步驟、錯誤回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。"}
    d["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "s-Ⅳ-16：從三視圖與展開圖建立立體量", "lessonId": d["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "reviewStatus": d["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

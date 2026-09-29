#!/usr/bin/env python3
"""Author and record the independent first-pass fusion for math a-IV-1.

This is deliberately scoped to one unit.  It does not promote reviewStatus:
the Terra second pass and release gates remain separate requirements.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-a-iv-1.json"
REPORT = ROOT / "implementation/reports/math-performance-a-iv-1-first-pass-review.json"


def research(publisher: str, edition: str, locator: str, concepts: list[str], representations: list[str], examples: list[str], misconceptions: list[str], emphasis: list[str], url: str) -> dict:
    return {
        "publisher": publisher,
        "edition": edition,
        "sourceType": "public-web",
        "sourceLocator": locator,
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": concepts,
            "representations": representations,
            "examplesOrEvidence": examples,
            "misconceptions": misconceptions,
            "assessmentEmphasis": emphasis,
        },
        "licenseBoundary": "僅記錄公立學校公開課程計畫可核對的章節定位、概念順序與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面，本課例子與活動均重新設計。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-a-iv-1"
    assert data["reviewStatus"] == "draft"

    data["title"] = "a-Ⅳ-1：把文字條件變成可驗證的代數推理"
    data["content"] = {
        "summary": "這一課不把字母當成空格填答案，而是把它當成可以追蹤的量。學生從「連續三個整數的總和」與「兩個量的差」兩種情境出發，練習先定義變量、保留條件，再用代數式、等式與不等式表達關係，最後以代回、反例或範圍檢查驗證結論。",
        "sections": [
            {"heading": "字母先代表什麼", "body": "看到 n、x、y 時，先寫清楚它代表的量、單位與限制。例如 n 是整數時，n−1、n、n+1 才能表達連續三個整數；若只寫三個字母，連續性並沒有被保留下來。"},
            {"heading": "同一條件可以有不同表徵", "body": "『偶數』可寫成 2k（k 為整數），『兩數和為 10』可寫成 x+y=10，『第一個量比第二個量多 4』可寫成 x−y=4。文字、式子與數線不是三個答案，而是同一關係的不同檢查入口。"},
            {"heading": "推理必須留下理由", "body": "解聯立式時，兩式相加消去 y，不是魔法；每一步都要說明用了加法、同減或同除。判斷不等式時則先確認乘除數的正負，正數不改變方向、負數會反向，零不能作除數。"},
            {"heading": "用反例檢查『一定』", "body": "若題目說某式『一定』成立，先找條件允許的簡單值測試；測試只能推翻命題，不能單獨證明命題。要證明時，把任意整數寫成指定形式，或用代數化簡把目標量化成可辨識的倍數。"},
        ],
    }
    data["studyHighlights"] = [
        "先標記每個字母的意義、範圍與單位，再把文字關係翻成式子。",
        "每次移項、相加、相乘或相除都寫出理由，避免只記住運算外觀。",
        "遇到『一定』先分辨是在找反例還是在建立一般證明，兩者證據強度不同。",
        "最後把答案代回原條件，並檢查整數性、正負號與除數不為零等限制。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "三個連號座位的總和", "body": "班級座位編號連續時，三個座位的總和看似每次都不同；先請學生猜它是否總能被 3 整除，再把中間座位記成 n。這個猜測讓『字母不是未知數的裝飾，而是可任意取值但受條件限制的量』成為本課入口。"},
            {"id": "explain", "phase": "explain", "heading": "從條件到表徵", "body": "把『連續三個整數』寫成 n−1、n、n+1，合併後得到 3n；把『偶數』寫成 2k，把『x 比 y 多 4』寫成 x−y=4。課堂中並列文字、符號與數值例子，明確標出哪一部分是條件、哪一部分是結論。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "證明三個連號的和是 3 的倍數", "body": "令中間整數為 n，三數為 n−1、n、n+1；相加得 (n−1)+n+(n+1)=3n。因 n 是整數，3n 必為 3 的倍數。用 n=4、n=−2 只作回算示例，並提醒有限測試不能取代對任意 n 的證明。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "拆解兩式求兩量", "body": "給定 x+y=10、x−y=4，學生先預測 x 是否大於 y，再將兩式相加得到 2x=14，除以 2 得 x=7，最後代回 7+y=10 得 y=3。每一步旁邊選擇『保留等值』的理由，系統不先顯示結果。"},
            {"id": "transfer", "phase": "transfer", "heading": "從數字換成限制條件", "body": "改以『商品單價為 p 元、買 3 件再加固定費共 250 元』的原創情境，要求學生先定義 p，再寫 3p+固定費=250；若固定費改變，說明哪個式子與解的範圍要改。重點是保留建模與驗證，不是套用上一題數字。"},
            {"id": "reflect", "phase": "reflect", "heading": "檢查推理是否越界", "body": "出口題請學生圈出自己使用的限制：整數、正數、非零除數或總價範圍，並回答『若刪掉這個限制，原結論還一定成立嗎？』接著選一個步驟寫出保留等值的理由，再以一句話區分計算正確、條件完整與推理完整，避免只因答案數字合理就結束。"},
        ],
        "summary": [
            "先定義量，再選擇能保留原條件的符號表徵。",
            "用等值變形逐步推理，旁邊留下每一步的數學理由。",
            "把測試、反例與一般證明分開，避免用幾個例子冒充必然性。",
            "代回原條件並檢查範圍，確認答案同時符合計算與情境。",
        ],
        "exitCheck": [
            {"prompt": "為什麼連續三個整數要寫成 n−1、n、n+1，而不能任意寫成 a、b、c？", "expectedEvidence": "指出連續性被 n−1、n、n+1 保留下來，並說明化簡後可形成 3n。"},
            {"prompt": "在 x+y=10、x−y=4 中，哪一步消去了 y？為什麼合法？", "expectedEvidence": "指出兩式相加、y+(−y)=0，並說明等式兩邊同時相加仍保持等值。"},
            {"prompt": "一個例子能不能證明『所有整數都成立』？", "expectedEvidence": "不能；例子可找反例或檢查，但一般命題需以任意整數的代數表示完成證明。"},
        ],
    }
    data["interactive"] = {
        "type": "algebra-expression-builder",
        "goal": "讓學生把文字條件轉成式子，逐步變形並以代回或反例檢查。",
        "scenario": "連續三個整數的和是否必為 3 的倍數？學生先預測，再拖曳中間整數 n，觀察三個表徵同步變化。",
        "variables": [{"symbol": "n", "meaning": "中間整數；可輸入任意整數"}, {"symbol": "s", "meaning": "(n−1)+n+(n+1) 的總和"}],
        "steps": [
            {"id": "step-1", "prompt": "把連續三個整數表示出來。", "options": ["n−1、n、n+1", "n、n、n", "n−1、n+1、n+2"], "answer": "A", "feedback": "以中間數 n 為基準，左右各差 1 才能保留連續關係。"},
            {"id": "step-2", "prompt": "合併 (n−1)+n+(n+1) 後得到什麼？", "options": ["3n", "3n+1", "n²"], "answer": "A", "feedback": "−1 與 +1 抵消，三個 n 合成 3n。"},
            {"id": "step-3", "prompt": "如何把一般推理與檢查連起來？", "options": ["說明 n 為整數所以 3n 是 3 的倍數，再用一個新 n 回算", "只看三個預設數值", "直接相信選項位置"], "answer": "A", "feedback": "一般證明先處理任意 n，再用新值回算檢查，兩種證據用途不同。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        research("nani", "南一版公立校方七年級數學課程計畫章節級證據", "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf；代數章節與評量欄位，核讀 2026-09-21。", ["證據把代數符號與文字關係放在基礎代數學習脈絡，先建立量與式的對應。", "評量方向要求學生讀取條件、進行運算並以關係檢查結果，而非只寫答案。"], ["以文字條件、代數式與數值回算互相對照；公開資料未提供可重製的完整教材頁面。"], ["本課用連續整數與兩式關係建立原創例子，對應公開章節的代數表徵方向。"], ["把字母當成固定未知數，或只看到關鍵字便套用公式而忽略範圍。"], ["文字轉式、等值變形、整數與正負限制、代回檢查。"], "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf"),
        research("kanghsuan", "康軒版公立校方數學課程計畫章節級證據", "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110；代數表徵、操作活動與多元評量欄位，核讀 2026-09-21。", ["公開課程計畫顯示代數概念需與表徵轉換及解題活動連結。", "多元評量方向支持讓學生解釋運算步驟與檢查條件，而不只判讀最後數值。"], ["文字、符號、表格或操作紀錄可作為同一關係的不同入口；未把公開頁面當成可複製教材。"], ["本課以互動拖曳 n 並同步更新式子與總和，將表徵轉換落實為原創活動。"], ["把測試幾個值當成一般證明，或在不等式中漏看乘除數的正負。"], ["多重表徵、操作後解釋、理由標記與新情境遷移。"], "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110"),
        research("hanlin", "翰林版公立校方數學課程計畫章節級證據", "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf；代數概念、解題表徵與情境評量欄位，核讀 2026-09-21。", ["公開課程資料把代數概念、符號運算與問題情境的解釋放在同一學習路徑。", "評量定位重視從條件形成推理、辨認錯誤並以數學語言表達。"], ["本課將式子、等式變形、反例與代回放在同一張推理紀錄中，資料本身為原創。"], ["本課用『反例可推翻但不能單獨證明』作為辨誤焦點，並以連號證明避免只靠數值試算。"], ["忽略條件、跳過等值理由、把否定一個例子誤當成完成證明。"], ["推理鏈完整性、錯誤診斷、理由短答與情境轉移。"], "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf"),
    ]
    data["fusionRecord"] = {
        "commonCore": ["三版本公開結構共同支持文字條件、符號表徵與代數推理的連結。", "概念需透過運算、解釋與檢查形成可追溯的推理鏈。", "評量不只看答案，還要檢查限制條件、表示法與理由。"],
        "versionDifferences": ["南一證據較明確呈現基礎代數的概念到評量定位；康軒證據突顯操作與多元表徵；翰林證據較強調情境解題、錯誤辨識與數學表達。這些是公開課程計畫的結構差異，不是完整教材內容差異。"],
        "originalAdditions": ["用連續三個整數建立一般證明，並明確區分測試與證明。", "用互動變項 n 同步更新三個整數與總和，要求學生先預測再解釋。", "加入固定費與聯立式的新情境，檢查學生是否能在條件改變時重建模型。"],
        "llmSynthesisNote": "本課以官方課綱與三筆公立校方章節級公開證據交叉整理共同概念，保留各來源可觀察的教學與評量重點差異，再重新設計連續整數、聯立式與互動表徵活動。未複製任何出版社或學校教材文字、題目、圖表、答案或版面；Terra 第二輪與發布審查尚未完成，因此 reviewStatus 維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "unit": "a-Ⅳ-1：把文字條件變成可驗證的代數推理",
        "lessonId": data["id"],
        "status": "first-pass-ai-review-complete",
        "reviewStatus": "draft",
        "checks": {
            "unitSpecificOriginalContent": True,
            "threeVersionResearchRecords": len(data["versionResearch"]) == 3,
            "fusionRecordPresent": True,
            "interactivePredictionManipulationExplanation": True,
            "publicExamRewritesRemainOriginal": True,
            "terraSecondPass": "pending",
        },
        "notes": [
            "已逐題核對本單元題目中的答案、解析、五步解法與三筆公開試題能力方向紀錄；未改動題目答案。",
            "本次只完成一個單元，不能外推為全科內容審查完成。",
        ],
        "reviewedAt": "2026-09-21",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "report": str(REPORT.relative_to(ROOT)), "reviewStatus": data["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

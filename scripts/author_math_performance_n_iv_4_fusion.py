#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics n-IV-4."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-n-iv-4.json"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-4-first-pass-review.json"
URLS = {
    "nani": "https://hakka.mtjh.kh.edu.tw/114plan/05/1/5-1-G-7.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
}


def research_record(publisher: str, concepts: str, representations: str,
                    misconception: str, assessment: str) -> dict:
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方數學課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": f"{URLS[publisher]}；比、比例、正反比與連比的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concepts, "公開課程結構支持以等值關係、變化量與條件限制解讀比例模型。"],
            "representations": [representations],
            "examplesOrEvidence": ["本課的飲料配方、工作時間與地圖比例均為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-n-iv-4"
    assert data["reviewStatus"] == "draft"
    data["title"] = "n-Ⅳ-4：用比例模型追蹤量的共同變化"
    data["content"] = {
        "summary": "比不是把兩個數字用冒號排在一起；它描述兩個量如何相互比較。比例則要求這種比較在不同情況下保持一致，正比表示一個量乘幾倍，另一個量也乘幾倍，反比則表示兩量的乘積維持固定。連比還要先確認三個量是否共享同一個比例尺度，才能把條件轉成可計算的數值。本課用自編配方、工作分工與地圖縮放情境，逐步判斷模型、求未知量、檢查單位，並辨識看似像比例其實不符合的資料。",
        "sections": [
            {"heading": "比與比例的差別", "body": "比 a:b 是比較兩個同類量的相對關係；比例 a:b=c:d 則是兩個比相等。先確認量的單位與順序，再約分或使用交叉相乘，才能避免把前後項顛倒。"},
            {"heading": "正比看共同倍數", "body": "若 y=kx 且 k 固定，x 增加為原來的三倍時，y 也增加為三倍。用 y/x 是否固定、表格是否等倍成長與座標圖是否通過原點，能互相驗證正比模型。"},
            {"heading": "反比看固定乘積", "body": "若 xy=k 且 k 固定，一個量增加時另一個量必須按相反倍數變化。用乘積表、單位和情境限制檢查，不能只看一組數字就宣稱反比。"},
            {"heading": "連比與條件翻譯", "body": "a:b:c=2:3:5 表示三量可寫成 2t、3t、5t；總和或其中一量給定後才可求 t。若題目換了單位或只給部分條件，要先把量的關係整理清楚。"},
        ],
    }
    data["studyHighlights"] = [
        "先辨認比較的兩量、順序、單位與比例常數。",
        "用商固定判斷正比，用積固定判斷反比，並檢查不只一組資料。",
        "連比先設共同尺度 t，再用總和或已知量求 t。",
        "最後回到原情境檢查單位、範圍與倍數方向。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "一壺飲料的配方能不能任意放大？", "body": "原創飲料配方以果汁與水的量維持 2:3。先讓學習者比較 200 毫升與 300 毫升、400 毫升與 600 毫升兩組資料，說明哪些只是同一配方放大，哪些已經改變味道。接著把『同時乘上相同倍數』寫成比例語句，建立比與比例不是單純相加的觀念。"},
            {"id": "explain", "phase": "explain", "heading": "用商與積選擇模型", "body": "把表格中的 x、y 分別計算 y/x 與 xy，觀察哪一欄保持固定。若 y/x 固定，寫成 y=kx 並解釋正比；若 xy 固定，寫成 xy=k 並解釋反比。特別加入固定基本費的計程車資料，讓學習者看見『一起增加』不一定是正比，模型要由條件而不是關鍵字決定。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "從連比總量求每一份", "body": "原創工作分配中甲、乙、丙的時間比例為 2:3:5，三人合計 50 分鐘。先把三量寫成 2t、3t、5t，利用 10t=50 得 t=5，再得到 10、15、25 分鐘。最後把三數重新相加、約成原比例，並檢查每個時間是否符合題目限制。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "用兩個證據辨認正反比", "body": "提供三組小表格：燈泡數與總耗電、完成同一工作的工人人數與時間、含固定費的車資與距離。學習者先計算商或積，再用一句話解釋模型；若資料不適合正比或反比，必須指出固定費或工作量改變等理由，而不是硬套公式。"},
            {"id": "transfer", "phase": "transfer", "heading": "把比例搬到地圖與速率", "body": "把地圖比例尺、實際距離與行走時間放在同一任務中。先處理同單位換算，再決定哪一對量是正比、哪一對量需要固定速率的限制；若速度改變，就重新說明原模型何處失效。這一步要求學生分開比例關係與單位換算，避免把數字倍數直接當成答案。"},
            {"id": "reflect", "phase": "reflect", "heading": "用反例檢查自己是否真的懂", "body": "出口前請學習者改寫一個錯誤主張：『距離變兩倍，含起步費的車資一定變兩倍』。先圈出固定費，再用具體數字反駁，最後寫出什麼條件下才會成為正比。回顧時同時檢查比的順序、單位、常數與情境限制，讓答案可由別人重做。"},
        ],
        "summary": [
            "比描述相對關係，比例描述兩個比相等，順序與單位不可省略。",
            "正比以商固定為證據，反比以積固定為證據，固定費等因素可能破壞模型。",
            "連比用共同尺度 t 表示，再由總和或已知量求出各部分。",
            "用代回、單位、倍數方向與反例檢查模型是否符合原情境。",
        ],
        "exitCheck": [
            {"prompt": "請說明如何用商與積分辨正比及反比。", "expectedEvidence": "能說明正比 y/x 固定、反比 xy 固定，並指出需檢查多組資料與情境條件。"},
            {"prompt": "甲乙丙為 2:3:5 且總量 50，如何求三者？", "expectedEvidence": "設為 2t、3t、5t，得到 10t=50、t=5，故三者為 10、15、25。"},
            {"prompt": "為什麼含固定費的車資通常不是距離的正比？", "expectedEvidence": "車資含不隨距離改變的固定項，距離加倍時總價不一定加倍；需先說明條件。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "依商、積與共同尺度選擇比例模型，並用代回與單位驗算。",
        "scenario": "拖曳或選擇不同資料表，觀察商或積是否固定，再把連比拆成共同尺度並檢查情境限制。",
        "variables": [
            {"symbol": "x", "meaning": "第一個可變量"},
            {"symbol": "y", "meaning": "與 x 比較或配對的第二個量"},
            {"symbol": "k", "meaning": "固定的比例常數或乘積"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "若資料中 y/x 每一列都相同，最合理的模型是什麼？", "options": ["正比 y=kx", "反比 xy=k", "兩量完全無關"], "answer": "A", "feedback": "商固定表示 y 隨 x 同倍變化，符合正比模型。"},
            {"id": "step-2", "prompt": "若同一工作中人數乘時間固定，應觀察哪一項？", "options": ["人數×時間", "人數＋時間", "人數÷時間且不看單位"], "answer": "A", "feedback": "固定工作量可用乘積檢查反比，但仍要確認工作內容與效率條件。"},
            {"id": "step-3", "prompt": "2:3:5 的總量是 50，三數應先怎麼表示？", "options": ["2t、3t、5t", "2+t、3+t、5+t", "2/t、3/t、5/t"], "answer": "A", "feedback": "連比共享同一個尺度 t，再由總和求出 t。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        research_record("nani", "以比、比例與量的關係處理生活情境中的未知量", "比值表、等值比例與連比的共同尺度表示", "看到兩量一起變大就誤判正比，忽略固定項與單位順序", "要求列出比例式、說明條件並以代回或表格驗證"),
        research_record("kanghsuan", "透過表格與操作比較正比、反比的變化方式", "倍數表、商積檢查與圖形或情境轉換", "只用一筆資料判斷模型，或把反比誤認為差值固定", "重視從資料提出模型、解未知量及解釋結果的歷程"),
        research_record("hanlin", "把比例概念連結到速率、尺度與實際問題限制", "地圖比例、工作分配、速率與單位換算的多重表徵", "連比未設共同尺度，或換單位後直接沿用原數字", "評估模型是否符合情境、量綱是否一致並能解釋反例"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持以比與比例表達量的相對關係及未知量。",
            "正比與反比必須由固定商或固定積等資料證據判斷。",
            "連比、單位換算與生活情境需要將條件翻譯成可驗算的模型。",
        ],
        "versionDifferences": [
            "南一證據較突顯比例關係與未知量處理；康軒較突顯表格操作及正反比辨識；翰林較突顯速率、尺度、單位與實際限制。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以配方放大和固定費反例，區分真正正比與表面同向變化。",
            "以 2:3:5 的工作時間示範共同尺度、總量與回代驗證。",
            "把商、積、單位和反例整合成可互動選擇與遷移任務。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織比、比例、正反比、連比及情境限制。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "n-Ⅳ-4：用比例模型追蹤量的共同變化",
        "lessonId": data["id"],
        "status": "first-pass-ai-review-complete",
        "reviewStatus": "draft",
        "checks": {
            "unitSpecificOriginalContent": True,
            "threeVersionResearchRecords": True,
            "fusionRecordPresent": True,
            "interactivePredictionManipulationExplanation": True,
            "answersAndDetailedSteps": True,
            "terraSecondPass": "pending",
        },
        "reviewedAt": "2026-09-21",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "reviewStatus": data["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

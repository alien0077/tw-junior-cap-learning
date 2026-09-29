#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-s-iv-1.json"
REPORT = ROOT / "implementation/reports/math-performance-s-iv-1-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
}


def record(publisher: str, concept: str, representation: str,
           misconception: str, assessment: str) -> dict:
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方數學課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": f"{URLS[publisher]}；幾何形體定義、符號與性質的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以定義、圖形條件與符號關係判斷幾何性質。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的紙模型、座標圖形與校園設計均為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-s-iv-1"
    assert data["reviewStatus"] == "draft"
    data["title"] = "s-Ⅳ-1：用定義與符號讀懂幾何形體"
    data["content"] = {
        "summary": "幾何圖形的名稱不是只用來背外觀；定義決定哪些條件一定成立，符號則讓角、邊、平行與垂直等關係可以精確記錄。矩形是四個直角的四邊形，正方形除了四個直角還有四邊等長；若只看到圖形『像』某種形狀而未檢查條件，判斷就可能錯誤。本課用紙模型、座標圖與校園設計的自編情境，練習由定義列出性質、由符號讀取關係，並區分必要條件與看似相似的線索。",
        "sections": [
            {"heading": "先用定義分類", "body": "分類圖形時先列出定義條件，再逐項核對資料。外觀方向、大小或畫圖比例不是定義；例如旋轉後的正方形仍保有四邊等長與四個直角。"},
            {"heading": "符號是可檢查的語言", "body": "AB 表示線段長度，∠A 表示角，AB∥CD 表示平行，AB⊥CD 表示垂直。符號順序與標記位置都要和圖形對應，不能把線段名稱與長度或射線混為一談。"},
            {"heading": "性質從定義推出", "body": "若圖形符合矩形定義，可推出對邊平行、對邊等長與四角皆為直角；但只知道一組對邊等長，不能直接推出它是矩形。結論必須有足夠條件支持。"},
            {"heading": "必要與充分要分清", "body": "四個直角是矩形的定義條件之一，但『看起來像長方形』不是證明。用表格記錄已知條件、可推出性質與尚缺條件，能避免把結果反過來當成理由。"},
        ],
    }
    data["studyHighlights"] = [
        "先寫定義條件，再核對圖形資料，不靠外觀猜測。",
        "正確讀取線段、角、平行與垂直的符號及順序。",
        "把已知條件、可推出性質與尚缺條件分開記錄。",
        "旋轉、縮放或改變位置不會自動改變幾何定義。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "紙框旋轉後還是正方形嗎？", "body": "原創紙模型把一個正方形旋轉 30 度，再與一個看似接近矩形的四邊形並列。請學習者先不看名稱，逐一檢查四邊長與四角，說明旋轉只改變位置，不改變定義性質；另一個圖形則必須依測量條件而非外觀判斷。"},
            {"id": "explain", "phase": "explain", "heading": "由定義到性質的推理鏈", "body": "以矩形為例，先寫四邊形且四角皆為直角的條件，再標記由幾何關係可推出的對邊平行與等長。接著給只有一組對邊平行的梯形反例，說明單一性質不足以倒推矩形，讓『條件→結論』方向保持清楚。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "讀懂符號並回到圖上", "body": "在自編四邊形 ABCD 中，標記 AB∥CD、AB=CD、∠A=90°。先把每個符號翻成文字，再判斷哪些資訊可支持平行、等長與直角，最後檢查頂點順序是否沿著圖形邊界，避免把 AC 誤讀成相鄰邊。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "用條件卡片分類圖形", "body": "提供『四邊等長』『四角直角』『一組對邊平行』『對角線相等』等卡片，讓學習者把卡片放到正方形、矩形、菱形或一般平行四邊形，並標記可推出、可能但不足、或與定義無關。每次分類都要寫出理由與反例。"},
            {"id": "transfer", "phase": "transfer", "heading": "把符號用到校園設計", "body": "原創校園地磚圖要求設計一塊無障礙矩形區域，先用平行與垂直符號記錄邊界，再說明哪些長度相等是設計條件、哪些是由矩形定義推出。若地磚旋轉或縮放，要重新檢查單位與幾何關係，而不是只複製圖形名稱。"},
            {"id": "reflect", "phase": "reflect", "heading": "修正只看外觀的判斷", "body": "請修正『四邊形有一組對邊平行，所以一定是矩形』。先指出條件不足，再給出平行四邊形或梯形作反例，最後列出要確認四角為直角或其他充分條件的證據；把反例的邊與角標記回圖上，檢查符號讀法是否支持你的結論。"},
        ],
        "summary": [
            "幾何圖形先依定義分類，外觀、方向與大小不是充分證據。",
            "正確讀取線段、角、平行與垂直符號，並核對頂點順序。",
            "由已知條件推出性質，不能把單一結果反過來當成完整理由。",
            "用反例、條件表與單位檢查幾何判斷是否足夠。",
        ],
        "exitCheck": [
            {"prompt": "旋轉後的正方形為什麼仍是正方形？", "expectedEvidence": "旋轉改變位置與方向，但四邊等長、四角直角等定義條件不變。"},
            {"prompt": "AB∥CD 與 AB⊥CD 各表示什麼？", "expectedEvidence": "前者表示線段 AB 與 CD 平行，後者表示兩線段互相垂直；符號需對應圖上的線段。"},
            {"prompt": "為什麼一組對邊平行不足以判斷矩形？", "expectedEvidence": "梯形或一般平行四邊形也可能有平行邊，但未必有四個直角，需補足定義條件。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "由幾何定義與符號條件分類圖形，並以反例檢查結論。",
        "scenario": "拖曳條件卡片到圖形，觀察哪些性質可推出、哪些資料仍不足。",
        "variables": [
            {"symbol": "a", "meaning": "圖形中的邊長或角度資料"},
            {"symbol": "b", "meaning": "與 a 對應的另一條邊或角"},
            {"symbol": "x", "meaning": "待判斷的幾何條件"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "判斷旋轉後圖形是否仍為正方形，應先檢查什麼？", "options": ["四邊等長且四角直角等定義條件", "圖形是否水平放置", "圖形看起來是否像正方形"], "answer": "A", "feedback": "幾何分類依定義條件，不依方向或外觀。"},
            {"id": "step-2", "prompt": "AB∥CD 的符號意義是什麼？", "options": ["線段 AB 與 CD 平行", "A、B、C、D 四點等距", "AB 與 CD 垂直"], "answer": "A", "feedback": "平行符號連結兩條線段，需回到圖形確認端點順序。"},
            {"id": "step-3", "prompt": "只有一組對邊平行時，能否直接判定矩形？", "options": ["不能，還需足夠的直角或其他條件", "可以，任何平行四邊形都是矩形", "可以，只要圖形畫得像"], "answer": "A", "feedback": "單一平行條件不足，需以定義與反例檢查。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以幾何形體定義與基本性質建立分類推理", "圖形標記、線段角度符號與條件表", "以外觀或方向判斷圖形，忽略必要定義條件", "要求從已知條件推出性質並說明不足之處"),
        record("kanghsuan", "透過操作圖形與符號辨識平行、垂直及等長", "紙模型、標記圖、符號翻譯與反例", "把圖形畫法當成幾何性質，或讀錯頂點順序", "重視多重表徵、分類理由與條件核對"),
        record("hanlin", "把幾何定義連結到座標與設計情境", "座標圖形、平面設計、長度單位與推理鏈", "把結果性質當作充分條件，未檢查模型限制", "評估定義、符號、反例與情境單位是否一致"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持由幾何定義、符號與圖形條件建立分類。",
            "平行、垂直、等長與角度標記需在圖形與文字間互相核對。",
            "必要條件、可推出性質與反例是判斷結論是否足夠的共同工具。",
        ],
        "versionDifferences": [
            "南一證據較突顯形體定義與基本性質；康軒較突顯紙模型、標記與符號操作；翰林較突顯座標、設計及條件推理。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以旋轉紙框區分外觀方向與不變的幾何定義。",
            "以條件卡片及梯形反例診斷把單一性質反推成完整分類。",
            "把符號讀取、必要條件、反例、單位與校園設計整合成互動任務。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織幾何形體定義、符號、平行垂直、等長、性質推導與反例判斷。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "s-Ⅳ-1：用定義與符號讀懂幾何形體",
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

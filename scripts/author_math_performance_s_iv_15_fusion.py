#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics s-IV-15."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-s-iv-15.json"
REPORT = ROOT / "implementation/reports/math-performance-s-iv-15-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf",
}


def record(publisher, concept, representation, misconception, assessment):
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方數學課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": f"{URLS[publisher]}；空間線面關係、立體圖形表徵與評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以立體圖形中的方向、交會與垂直條件判讀線線、線面及面面關係。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的教室、置物架與盒狀模型為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main():
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-s-iv-15" and data["reviewStatus"] == "draft"
    data["title"] = "s-Ⅳ-15：用截面與方向理解空間線面關係"
    data["content"] = {
        "summary": "在立體空間裡，兩條直線可能相交、平行或成為不在同一平面的異面直線；直線與平面可能相交、平行或垂直；兩平面也可能平行或相交。判斷不能只看透視圖上有沒有碰到，而要追問是否共面、方向是否一致，以及是否有足夠的垂直證據。本課用盒狀模型、截面、置物架與建築隔間改寫公開課程能力，逐步練習讀圖、說理、辨識錯誤與檢查答案。",
        "sections": [
            {"heading": "先確認你正在看三維空間", "body": "透視圖會把深度壓在紙面上，圖上不相交不代表空間中平行。先標出同一個平面、同一條稜線與深度方向，再判斷是否可能共面。"},
            {"heading": "異面直線不是平行線", "body": "平行直線必須共面且不相交；異面直線不在同一平面，即使看起來都朝相近方向，也不能稱為平行。兩線相交則先看交點與夾角。"},
            {"heading": "線面垂直需要兩條平面內證據", "body": "若一條直線與平面內兩條相交直線都垂直，才能推出這條直線垂直於平面。只找到一個直角，通常不足以支持線面垂直。"},
            {"heading": "截面與投影是檢查工具", "body": "取與平面適當的截面可把空間關係轉成平面圖，但投影會隱藏深度。完成判斷後要回到原立體圖，確認線段是否屬於同一平面與條件是否完整。"},
        ],
    }
    data["studyHighlights"] = [
        "用共面性區分相交、平行與異面直線。",
        "線面垂直要找到平面內兩條相交且都垂直的直線。",
        "面面平行需判斷沒有共同點並追蹤一致方向。",
        "用截面整理證據，再回立體圖檢查深度與單位語言。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "教室裡的燈管、牆面與地板", "body": "請想像一支直立燈管、一面牆和水平地板：燈管可能垂直地板，也可能與牆面相交。先不要急著說平行，請指出哪些線在同一面上、哪些方向需要從側面觀察，建立三維關係必須說明證據的習慣。"},
            {"id": "explain", "phase": "explain", "heading": "把三種關係分成可檢查的問題", "body": "判斷兩線先問是否相交；不相交再問是否共面，才可分成平行或異面。判斷線面則問直線是否與面相交、是否完全不碰，若要說垂直，還要找平面內兩條相交直線作為證據；兩面則看是否有共同交線或是否保持同向。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "盒狀模型的垂直證明", "body": "在盒狀模型 ABCD-A'B'C'D' 中，AA' 是直立稜線，AB 與 AD 是底面 ABCD 內相交的兩條邊。若模型標示 AA'⊥AB 且 AA'⊥AD，因 AB、AD 同在底面且相交，所以可推出 AA'⊥平面 ABCD。注意：只寫 AA'⊥AB 只能得到一條線的證據，不能單獨推出線面垂直。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "三張關係卡片逐張判讀", "body": "第一張給兩條同一牆面內不相交的水平線，判為平行；第二張給一條地板邊線與不在同一面的天花板斜邊，先檢查共面性，避免誤稱平行；第三張給直立線和底面兩條相交邊的直角標記，要求寫出完整線面垂直理由。每張都要保留『相交、共面、方向、證據』四個詞。"},
            {"id": "transfer", "phase": "transfer", "heading": "把空間證據帶到建築與截面", "body": "設計電梯井時，井壁可視為平面、導軌可視為直線。從正面投影看兩條導軌不相交，仍要用側面或截面確認它們是否共面且方向一致；若要確認導軌垂直底板，需尋找底板內兩條相交方向的垂直證據，而不是只量一個角。"},
            {"id": "reflect", "phase": "reflect", "heading": "修正兩個常見直覺錯誤", "body": "請改寫『透視圖上沒有交點，所以兩線平行』與『一條直線和一條平面內直線垂直，所以直線垂直平面』。前者缺少共面條件，可能是異面；後者只具一條垂直證據，還要找到平面內另一條相交直線並確認也垂直。"},
        ],
        "summary": ["先辨認空間與共面性，再談平行或異面。", "線面垂直必須使用平面內兩條相交直線的證據。", "截面能整理關係，但不能取代回看原立體圖。", "答案要寫出判斷條件，不只寫一個符號。"],
        "exitCheck": [
            {"prompt": "為什麼兩條不相交直線不能直接判為平行？", "expectedEvidence": "還要確認兩線共面；不共面且不相交的是異面直線。"},
            {"prompt": "要證明 AA' 垂直底面 ABCD，至少需要哪些資料？", "expectedEvidence": "AA' 分別垂直於底面內相交的 AB 與 AD，才能使用線面垂直判定。"},
            {"prompt": "投影圖與原立體圖要如何互相檢查？", "expectedEvidence": "投影先整理方向，之後回原圖確認深度、共面性、交點與所有垂直標記。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "依共面性與垂直證據判斷異面直線、線面垂直及面面平行。",
        "scenario": "在盒狀模型中切換正面、側面與截面，逐步選出足夠的空間幾何證據。",
        "variables": [{"symbol": "x", "meaning": "觀察到的空間關係"}, {"symbol": "y", "meaning": "共面或垂直證據數量"}, {"symbol": "z", "meaning": "最後的幾何分類"}],
        "steps": [
            {"id": "step-1", "prompt": "兩條直線不相交，且沒有任何一個平面同時包含它們，應判為何種關係？", "options": ["異面直線", "平行直線", "相交直線"], "answer": "A", "feedback": "不相交且不共面就是異面；平行線必須先滿足共面。"},
            {"id": "step-2", "prompt": "若 AA' 已垂直平面 ABCD 內的 AB，還缺哪項關鍵證據？", "options": ["AA' 也垂直於與 AB 相交的 AD", "只要把圖放大即可", "只要 AA' 不在底面即可"], "answer": "A", "feedback": "線面垂直判定需要平面內兩條相交直線都與該直線垂直。"},
            {"id": "step-3", "prompt": "判斷兩平面平行時，哪個敘述最完整？", "options": ["兩平面沒有共同點，且方向保持一致", "在一張投影圖看不到交線", "只量到一組相等長度"], "answer": "A", "feedback": "投影可能藏住交線；要回到三維關係確認沒有共同點與一致方向。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以立體圖形中的線線、線面與面面關係建立空間方向判讀。", "盒狀模型、稜線、平面標記與垂直符號的互相轉換。", "把透視圖中不相交誤當成平行，或只用一個直角宣稱線面垂直。", "重視讀圖、條件列舉、關係分類與說理完整性。"),
        record("kanghsuan", "透過截面與投影連結平面幾何和空間幾何的表示。", "正面、側面、截面和立體模型之間的方向追蹤。", "忽略深度造成的異面關係，或把投影上的平行當作空間平行。", "要求比較不同視圖、指出證據並檢查空間條件。"),
        record("hanlin", "以生活建築與立體模型應用線面垂直、平行及交會判斷。", "牆面、地板、導軌與稜線的情境化幾何語言。", "混用相交、平行、異面與垂直術語，未說明共面性。", "評估模型、完整證明、截面選擇與答案合理性。"),
    ]
    data["fusionRecord"] = {
        "commonCore": ["三版本公開結構共同支持從立體模型判讀線線、線面與面面關係。", "共面性、方向與垂直條件是空間幾何分類的共同證據。", "截面和投影可作為表徵工具，但必須回查原立體關係。"],
        "versionDifferences": ["南一證據較突顯立體圖形與基本關係分類；康軒較突顯截面、投影與不同視圖；翰林較突顯建築生活情境與完整說理。這是公開課程計畫層級差異，不宣稱完整教材差異。"],
        "originalAdditions": ["用教室燈管、盒狀模型與電梯導軌串接線線、線面及面面判斷。", "用 AA'、AB、AD 的雙垂直證據示範線面垂直推理。", "以異面直線與投影誤判作為互動選擇題的錯誤診斷。"],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織共面性、異面直線、線面垂直、面面平行、截面與投影等概念。正文、盒狀模型例題、互動步驟、錯誤回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({"unit": "s-Ⅳ-15：用截面與方向理解空間線面關係", "lessonId": data["id"], "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "checks": {"unitSpecificOriginalContent": True, "threeVersionResearchRecords": True, "fusionRecordPresent": True, "interactivePredictionManipulationExplanation": True, "answersAndDetailedSteps": True, "terraSecondPass": "pending"}, "reviewedAt": "2026-09-21"}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lesson": str(LESSON.relative_to(ROOT)), "reviewStatus": data["reviewStatus"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

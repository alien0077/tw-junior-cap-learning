#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics n-IV-9."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-n-iv-9.json"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-9-first-pass-review.json"
URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf",
}


def record(publisher: str, concept: str, representation: str,
           misconception: str, assessment: str) -> dict:
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方數學課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": f"{URLS[publisher]}；計算工具、近似值與誤差的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以真值、近似值、誤差範圍與精度需求判斷數值結果。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的量測讀值、圓周估算與材料裁切均為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-n-iv-9"
    assert data["reviewStatus"] == "draft"
    data["title"] = "n-Ⅳ-9：用誤差與精度判斷近似值"
    data["content"] = {
        "summary": "計算機可以快速產生近似數，但螢幕上的位數不等於答案就完全正確。誤差是近似值與真值之間的差距，實際題目常只能知道量落在某個範圍，或只能以指定精度記錄。本課以量測讀值、圓周計算與材料裁切的自編情境，區分絕對誤差、相對誤差、截位與四捨五入，並練習依需求選擇合適位數、單位與誤差說明。",
        "sections": [
            {"heading": "近似值不是隨便取的數", "body": "真值可能無法完整寫出，或儀器只能讀到某一刻度；近似值必須附上精度或範圍。先說明數字如何得到，再說明還可能偏離多少，答案才可被解讀。"},
            {"heading": "絕對誤差與相對誤差", "body": "若知道真值，絕對誤差可用 |近似值−真值| 表示；相對誤差則把誤差與真值比較，適合判斷不同尺度的結果。真值未知時不能假裝算出精確誤差，應改用誤差上限或量測範圍。"},
            {"heading": "截位、四捨五入與有效精度", "body": "截位直接捨去後面位數，四捨五入則看下一位；兩者可能造成不同方向的偏差。題目指定小數位、有效位數或測量刻度時，要依規則呈現，不以更多位數掩蓋精度限制。"},
            {"heading": "選擇符合目的的結果", "body": "工程裁切、距離估算與統計報告需要不同精度。最後要檢查單位、誤差方向、四捨五入方式與是否會影響決策，讓計算機成為可解釋的工具而不是答案黑盒子。"},
        ],
    }
    data["studyHighlights"] = [
        "先區分真值、近似值、誤差與可報告的精度。",
        "知道真值才可直接算絕對誤差；未知時改用範圍或誤差上限。",
        "分辨截位與四捨五入，依題目和測量刻度決定位數。",
        "用單位、誤差方向與實際用途檢查近似結果。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "量測桌面的兩個讀值都能用嗎？", "body": "原創木工任務量到桌長 120.4 公分，儀器最小刻度為 0.1 公分；另一位同學報告 120.437891 公分。請學習者比較兩份報告的資訊是否真的更精確，再說明儀器刻度如何限制最後位數，建立近似值必須附精度的觀念。"},
            {"id": "explain", "phase": "explain", "heading": "把誤差寫成距離與比例", "body": "以真值 10、近似值 9.8 示範絕對誤差 |9.8−10|=0.2；再說明相對誤差為 0.2/10=0.02，也就是 2%。接著標示真值未知時不能直接套這個分母，而應用刻度造成的誤差範圍，避免把估計當真值。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "比較截位與四捨五入", "body": "把 3.1469 取到小數第二位：截位為 3.14，因第三位是 6，四捨五入為 3.15。分別計算與原數的差，觀察截位偏小、四捨五入較接近的理由；最後依題目指定方法選擇報告值，不混用名稱。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "用誤差需求選位數", "body": "給出圓周計算的計算機結果 31.415926 公分，並提供三種用途：課堂估算、紙板裁切、精密比較。學習者先讀取允許誤差與單位，再決定 31.4、31.42 或保留更多位數；每個選擇都要寫出理由，而非單純選最長數字。"},
            {"id": "transfer", "phase": "transfer", "heading": "比較不同尺度的量測", "body": "原創任務比較長 2 公尺的誤差 1 公分與長 20 公分的誤差 0.5 公分。先算絕對誤差，再用相對誤差比較哪項量測比例上更不穩定；最後討論在不同用途下，不能只看誤差的數字大小。"},
            {"id": "reflect", "phase": "reflect", "heading": "修正『位數越多越準』", "body": "請學習者反駁『計算機顯示 3.1415926535，所以報告越多位數越可靠』。先指出輸入資料與儀器精度的限制，再寫出符合用途的近似值、單位及誤差說明，最後用反例說明多出的位數可能只是計算顯示而非測量資訊。"},
        ],
        "summary": [
            "近似值需要精度或範圍說明，螢幕位數不等於真實資訊量。",
            "知道真值可算絕對與相對誤差，真值未知時應報告誤差上限。",
            "截位與四捨五入的規則不同，位數依題目與儀器刻度決定。",
            "以單位、誤差比例與實際用途判斷報告結果是否合適。",
        ],
        "exitCheck": [
            {"prompt": "真值 10、近似值 9.8 的絕對誤差與相對誤差如何求？", "expectedEvidence": "絕對誤差為 0.2，相對誤差為 0.2/10=0.02，即 2%，並說明需知道真值。"},
            {"prompt": "3.1469 取到小數第二位的截位與四捨五入各為何？", "expectedEvidence": "截位為 3.14；四捨五入看第三位 6，得到 3.15。"},
            {"prompt": "為什麼計算機顯示更多位數不一定代表量測更準？", "expectedEvidence": "精度受輸入資料、儀器刻度與模型限制；多出的顯示位數可能沒有實際測量證據。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "依真值、精度與用途選擇近似表示，並計算或估計誤差。",
        "scenario": "切換真值已知或未知、改變刻度與報告位數，觀察誤差和用途是否相稱。",
        "variables": [
            {"symbol": "x", "meaning": "原始真值或計算結果"},
            {"symbol": "a", "meaning": "要報告的近似值"},
            {"symbol": "e", "meaning": "允許的誤差或儀器刻度限制"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "真值 10、近似值 9.8 時，絕對誤差是多少？", "options": ["0.2", "9.8", "19.8"], "answer": "A", "feedback": "絕對誤差取近似值與真值差的絕對值。"},
            {"id": "step-2", "prompt": "3.1469 四捨五入到小數第二位應選哪個？", "options": ["3.15", "3.14", "3.1"], "answer": "A", "feedback": "小數第三位是 6，因此第二位 4 要進位成 5。"},
            {"id": "step-3", "prompt": "真值未知但儀器刻度為 0.1，報告結果最需要附上什麼？", "options": ["測量精度或誤差範圍", "任意增加十位小數", "只寫計算機畫面"], "answer": "A", "feedback": "沒有真值時不能假裝算精確誤差，應說明刻度造成的限制。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以近似值、誤差與精度處理數值結果", "真值近似值表格、絕對差與誤差範圍", "把計算機顯示當真值，或未分辨截位和四捨五入", "要求列出精度規則、誤差計算與結果限制"),
        record("kanghsuan", "透過測量與數值操作理解誤差方向及大小", "刻度讀值、數線區間、計算機與四捨五入", "只看誤差絕對數字，不比較量的尺度或用途", "重視估算歷程、單位及合適位數的判斷"),
        record("hanlin", "連結工具估算、相對誤差與實際測量決策", "圓周、裁切、尺度比較與允許誤差情境", "以更多位數掩蓋資料精度不足，或真值未知仍報精確誤差", "評估模型、精度、單位與決策風險是否一致"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持以近似、誤差與精度描述數值結果。",
            "截位、四捨五入、計算機估值與測量範圍需要清楚區分。",
            "單位、相對尺度與實際用途決定報告位數是否合適。",
        ],
        "versionDifferences": [
            "南一證據較突顯近似與誤差概念；康軒較突顯測量操作、數線與位數；翰林較突顯計算工具、相對誤差與實際決策。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以木工量測刻度反駁『計算機位數越多越準』。",
            "以 3.1469 對照截位與四捨五入的方向及差異。",
            "把絕對誤差、相對誤差、未知真值、單位與用途整合成互動判斷。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織計算工具、近似值、絕對／相對誤差、截位、四捨五入與測量精度。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "n-Ⅳ-9：用誤差與精度判斷近似值",
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

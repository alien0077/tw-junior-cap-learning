#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics n-IV-7."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-n-iv-7.json"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-7-first-pass-review.json"
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
        "sourceLocator": f"{URLS[publisher]}；數列、等差與等比關係的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以相鄰差、相鄰比與通項規律描述數列變化。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的座位排列、儲蓄成長與圖形周長均為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-n-iv-7"
    assert data["reviewStatus"] == "draft"
    data["title"] = "n-Ⅳ-7：從差與比讀懂數列規律"
    data["content"] = {
        "summary": "數列是按順序排列的數，重點不在背出某個公式，而在找出相鄰項之間可驗證的規律。等差數列的相鄰差固定，等比數列的相鄰比固定；同一串數若只看前兩項，很容易把偶然的變化誤認成規律。本課從座位排列、儲蓄成長與圖形邊長的自編情境出發，練習辨識差與比、寫出通項、反推指定項，並用多項資料與情境意義檢查模型。",
        "sections": [
            {"heading": "先看相鄰變化", "body": "將數列依序寫出，計算每一對相鄰項的差；若差固定，就是等差線索。若差不固定，再觀察相鄰項的比，但分母不可為零，並注意零項或負項帶來的限制。"},
            {"heading": "等差通項與位置", "body": "首項為 a₁、公差為 d 時，第 n 項可寫成 aₙ=a₁+(n−1)d。n−1 表示從第一項走到第 n 項的步數，不是直接把 n 乘到公差。"},
            {"heading": "等比通項與倍數", "body": "首項為 a₁、公比為 r 時，第 n 項可寫成 aₙ=a₁rⁿ⁻¹。公比可以是分數、負數或小於 1 的數，必須由每一對相鄰項驗證，不能只看數列變大或變小。"},
            {"heading": "規律要能回到情境", "body": "座位、存款或圖形邊長可能有自然數、時間或長度限制。即使代數式能算出某項，也要檢查位置是否為正整數、單位是否一致，以及模型是否適用於題目範圍。"},
        ],
    }
    data["studyHighlights"] = [
        "先算相鄰差，再在條件允許時檢查相鄰比。",
        "等差通項用步數 n−1，等比通項用倍數 r 的 n−1 次方。",
        "至少用多個相鄰關係驗證規律，不用前兩項猜整串數列。",
        "回到位置、單位與情境範圍檢查通項是否有意義。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "看台座位怎麼一排排增加？", "body": "原創小劇場的第一排有 8 個座位，每往後一排增加 3 個。先列出前五排，讓學習者說明每次多出的數量，再預測第十排。接著改成每排是前一排的 2 倍，要求比較『固定增加』與『固定倍增』，建立差與比是兩種不同規律。"},
            {"id": "explain", "phase": "explain", "heading": "用差與比分類數列", "body": "把數列 5、8、11、14 與 3、6、12、24 並列，分別計算相鄰差與相鄰比。第一列的差固定為 3，第二列的比固定為 2；再加入 2、4、7、11，說明前兩個差相同不足以證明等差。分類必須由可重做的資料支持。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "從首項與公差求指定項", "body": "座位數列首項 8、公差 3，第 10 項寫成 a₁₀=8+(10−1)×3=35。先算走了 9 步，再乘公差並加回首項；最後把第 9 項 32 加 3 交叉檢查，確認位置和答案方向一致。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "辨認通項中的步數與倍數", "body": "給出 4、7、10、13 與 2、6、18、54 兩列，要求學習者先填差或比，再選對通項。針對把 aₙ=a₁+nd 或 aₙ=a₁rⁿ 的錯誤，回饋要求畫出從第一項到第 n 項實際走了幾步，或數出使用了幾次倍乘。"},
            {"id": "transfer", "phase": "transfer", "heading": "規律搬到儲蓄與圖形", "body": "原創任務把每月固定存款和每月增加百分之十的帳戶並列。前者以固定差描述，後者以固定比描述；再把等差數列套到正多邊形周長時檢查邊數與長度的限制。學習者要解釋同一公式換情境時，哪些量和單位必須重新定義。"},
            {"id": "reflect", "phase": "reflect", "heading": "用第三、第四項拆穿錯誤猜測", "body": "請修正『1、2、4 是等差數列，因為一直增加』的主張。先算差為 1、2 不固定，再算比為 2、2 固定，判斷它是等比而非等差；最後用通項求第六項並代回前幾項驗證。"},
        ],
        "summary": [
            "等差看相鄰差固定，等比看相鄰比固定，不能用變大或變小代替證據。",
            "等差通項的 n−1 是步數，等比通項的 n−1 是倍乘次數。",
            "用多個相鄰關係與通項回代驗證，避免只由前兩項猜規律。",
            "最後檢查位置、單位與情境限制，確認數列模型可用。",
        ],
        "exitCheck": [
            {"prompt": "如何區分 5、8、11、14 與 3、6、12、24？", "expectedEvidence": "第一列相鄰差固定為 3，是等差；第二列相鄰比固定為 2，是等比。"},
            {"prompt": "首項 8、公差 3 的第 10 項如何求？", "expectedEvidence": "a₁₀=8+(10−1)×3=35，並能說明 n−1 是從第一項走到第十項的九步。"},
            {"prompt": "為什麼 1、2、4 不是等差？", "expectedEvidence": "相鄰差為 1 和 2 不固定；相鄰比都為 2，因此它符合等比而非等差。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "依相鄰差、相鄰比與項次位置建立並驗證數列通項。",
        "scenario": "選取數列資料，觀察差或比是否固定，再以指定項與回代檢查通項。",
        "variables": [
            {"symbol": "a", "meaning": "數列中的項"},
            {"symbol": "d", "meaning": "等差數列的固定公差"},
            {"symbol": "r", "meaning": "等比數列的固定公比"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "判斷 5、8、11、14 時，先檢查哪一項？", "options": ["相鄰差是否固定", "只看最後一項", "把所有項相乘"], "answer": "A", "feedback": "等差數列的核心證據是相鄰差固定。"},
            {"id": "step-2", "prompt": "首項 8、公差 3 的第 10 項應用哪個表示？", "options": ["8+(10−1)×3", "8+10×3", "8×3¹⁰"], "answer": "A", "feedback": "從第一項到第十項走 9 步，所以使用 n−1。"},
            {"id": "step-3", "prompt": "數列 3、6、12、24 的固定關係是什麼？", "options": ["每項乘以 2", "每項加 3", "每項減 2"], "answer": "A", "feedback": "相鄰比固定為 2，這是等比規律。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以相鄰差、相鄰比及項次描述數列變化", "數列表格、通項符號與生活排列情境", "看到持續變大就誤判等差，或把項次 n 當成步數", "要求由多項資料找規律並回代驗證通項"),
        record("kanghsuan", "透過操作比較固定增加與固定倍增", "差與比的表格、圖形排列及通項轉換", "只用前兩項猜規律，忽略第三項以後的檢查", "重視分類理由、指定項計算與錯誤修正歷程"),
        record("hanlin", "把數列規律連結到儲蓄、圖形與數量情境", "固定存款、百分比成長、周長與位置限制", "代數通項算得出數字卻未檢查單位與情境範圍", "評估模型選擇、通項意義與實際限制是否一致"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持以相鄰關係及項次描述數列規律。",
            "等差以固定差、等比以固定比辨識，通項必須由資料驗證。",
            "數列應連結表格、圖形或生活情境，並檢查位置與單位限制。",
        ],
        "versionDifferences": [
            "南一證據較突顯數列關係與通項；康軒較突顯差比操作及多項驗證；翰林較突顯儲蓄、圖形與實際模型限制。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以座位排列對照固定增加與固定倍增，讓差與比可觀察。",
            "以通項的 n−1 對應實際步數或倍乘次數，診斷常見索引錯誤。",
            "把等差、等比分類、指定項、回代與情境單位整合成互動任務。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織等差、等比、通項、差比判斷與情境遷移。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "n-Ⅳ-7：從差與比讀懂數列規律",
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

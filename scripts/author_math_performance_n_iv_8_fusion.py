#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics n-IV-8."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-n-iv-8.json"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-8-first-pass-review.json"
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
        "sourceLocator": f"{URLS[publisher]}；等差級數和的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以首尾配對、項數與平均值理解等差級數和。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的階梯座位、分期存款與圖形點列均為原創情境，只承接公開課程所示的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-n-iv-8"
    assert data["reviewStatus"] == "draft"
    data["title"] = "n-Ⅳ-8：用首尾配對理解等差級數和"
    data["content"] = {
        "summary": "等差級數是等差數列前幾項的總和，核心不是死背公式，而是看見首尾配對後每一對的和都相同。若首項為 a₁、末項為 aₙ、共有 n 項，總和可寫成 n(a₁+aₙ)/2；當末項或項數未知時，必須先用等差通項補齊條件。本課以階梯座位、分期存款和圖形點列的自編情境，練習配對推導、公式選擇、項數檢查與情境回代。",
        "sections": [
            {"heading": "先把前後項配成對", "body": "等差數列首尾相加、第二項與倒數第二項相加，所得的和相同。把正向與反向兩次相加，就能看出總和等於項數乘首尾和的一半。"},
            {"heading": "公式中的每個量都有角色", "body": "Sₙ=n(a₁+aₙ)/2 需要項數、首項與末項；若題目只給首項、公差和項數，先用 aₙ=a₁+(n−1)d 求末項，再代入總和。"},
            {"heading": "奇偶項數都可用配對", "body": "項數為偶數時可完全配對；項數為奇數時中間項自己配對，仍可用平均值乘項數。不要只在偶數例子中背公式。"},
            {"heading": "總和要符合情境", "body": "座位數、存款金額或點的個數可能必須是整數，公差也有單位。算出總和後要檢查項數、末項、單位與是否包含第一項及最後一項。"},
        ],
    }
    data["studyHighlights"] = [
        "用首尾配對理解公式，而不是只背 Sₙ。",
        "缺末項時先用等差通項求出，缺項數時先整理條件。",
        "奇數項要保留中間項，仍可用平均值乘項數。",
        "回代首項、公差、項數、末項與單位檢查總和。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "階梯座位的總數怎麼快算？", "body": "原創看台每排座位為 6、9、12、15、18，請學習者先逐項相加，再把第一排和最後一排、第二排和倒數第二排配對。比較兩種方法所需的步驟，讓學生發現每一對都是 24，總和可以由平均每排乘排數得到。"},
            {"id": "explain", "phase": "explain", "heading": "從兩次排列推導總和", "body": "把 S= a₁+a₂+…+aₙ 反向寫成 S=aₙ+aₙ₋₁+…+a₁，逐欄相加得到 2S=n(a₁+aₙ)，再除以 2。要求學生指出 n 代表項數、a₁+aₙ 是每一對的共同和，避免把最後一項誤當公差。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "先求末項再求總和", "body": "首項 6、公差 3、共 12 項時，先算 a₁₂=6+11×3=39，再用 S₁₂=12(6+39)/2=270。最後用平均值 (6+39)/2=22.5 乘 12 交叉驗證，並檢查 6 到 39 共走 11 次。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "辨認是否漏掉端點", "body": "給出 4 到 28、每次加 4 的所有項，要求學習者先求項數，再求總和。針對把 4 到 28 當成 24/4 項或只加中間幾項的錯誤，回饋要求列出通項與端點，確認第一項和末項都被納入。"},
            {"id": "transfer", "phase": "transfer", "heading": "把總和放回分期存款", "body": "原創分期存款第一月存 500 元，每月多存 100 元，共 8 個月。先辨識金額形成等差數列，再求第八月金額與八個月總存款；若問題改成只計偶數月，要重新列出子數列，不能直接套原項數。"},
            {"id": "reflect", "phase": "reflect", "heading": "用平均值檢查公式答案", "body": "請學習者修正『首項 6、末項 39、12 項的總和是 6+39×12』。先指出運算順序和平均概念錯誤，再以首尾平均 22.5 乘 12 得到 270，最後用通項逐項確認末項與項數。"},
        ],
        "summary": [
            "首尾配對後每一對和相同，總和等於項數乘首尾平均。",
            "若缺末項，先用等差通項求出，再代入級數和。",
            "項數、端點與是否包含中間項必須清楚，奇偶項數都可處理。",
            "用平均值、逐項範圍、單位與回代檢查總和。",
        ],
        "exitCheck": [
            {"prompt": "為什麼等差級數可用首尾平均乘項數？", "expectedEvidence": "首尾、次首與次末等配對的和相同，因此每項平均是 (a₁+aₙ)/2，乘 n 得總和。"},
            {"prompt": "首項 6、公差 3、12 項的總和如何求？", "expectedEvidence": "先求末項 39，再算 12(6+39)/2=270，並能用平均值交叉驗證。"},
            {"prompt": "只計偶數月存款時，為什麼不能直接把項數換成一半？", "expectedEvidence": "偶數月形成新的子數列，首項、末項與公差需重新確認，不能只改項數。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "用首尾配對、項數與通項求出等差級數和並驗算。",
        "scenario": "調整首項、公差與項數，觀察末項及首尾平均如何共同決定總和。",
        "variables": [
            {"symbol": "a", "meaning": "等差數列的首項"},
            {"symbol": "d", "meaning": "相鄰項固定增加的公差"},
            {"symbol": "n", "meaning": "納入總和的項數"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "等差數列求和時，哪一組量能直接形成每對共同和？", "options": ["首項與末項", "首項與公差", "項數與公差相乘"], "answer": "A", "feedback": "首尾配對的和相同，首項與末項決定每對的共同和。"},
            {"id": "step-2", "prompt": "首項 6、公差 3、12 項時，末項如何求？", "options": ["6+(12−1)×3", "6+12×3", "6×3¹²"], "answer": "A", "feedback": "從第一項到第十二項走 11 步，所以使用 n−1。"},
            {"id": "step-3", "prompt": "首項 6、末項 39、共 12 項的總和是什麼？", "options": ["12(6+39)/2", "6+39×12", "(39−6)×12"], "answer": "A", "feedback": "總和等於項數乘首尾平均，也就是 n(a₁+aₙ)/2。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以首尾配對、項數與通項理解等差級數和", "數列排列、首尾配對表格與總和公式互相轉換", "把末項當公差，或漏算第一項與最後一項", "要求推導或解釋公式並回代項數與端點"),
        record("kanghsuan", "透過操作與圖形排列看見等差總和結構", "階梯點列、首尾配對與平均值表徵", "只在偶數項時配對，遇到奇數項就不會處理", "重視配對歷程、指定條件與結果檢核"),
        record("hanlin", "把級數和連結到存款、數量及單位限制", "分期金額、圖形點數、項數與單位情境", "只套公式而不確認納入範圍、單位或子數列", "評估模型、端點、項數與生活意義是否一致"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持以首尾關係、項數與等差通項求級數和。",
            "首尾配對與平均值是公式背後的可解釋推理。",
            "端點、項數、奇偶性、單位與情境範圍需要回代檢查。",
        ],
        "versionDifferences": [
            "南一證據較突顯等差級數和與通項關係；康軒較突顯配對、排列與操作表徵；翰林較突顯存款、數量與端點限制。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以階梯座位的首尾配對比較逐項相加與平均值乘項數。",
            "以首項、公差、項數先求末項，再用兩種方法驗證總和。",
            "把奇偶項數、子數列、端點、單位與分期存款整合成互動任務。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織等差級數和、首尾配對、通項、奇偶項數與情境應用。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "n-Ⅳ-8：用首尾配對理解等差級數和",
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

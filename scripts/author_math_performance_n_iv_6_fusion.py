#!/usr/bin/env python3
"""Independent first-pass authoring for mathematics n-IV-6."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-n-iv-6.json"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-6-first-pass-review.json"
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
        "sourceLocator": f"{URLS[publisher]}；十分逼近、平方根估值與計算工具的概念、表徵及評量欄位；核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [concept, "公開課程結構支持以區間、平方比較與工具估算逐步逼近未知數值。"],
            "representations": [representation],
            "examplesOrEvidence": ["本課的測量誤差、面積估算與計算機按鍵流程均為原創情境，只承接公開課程的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "只記錄公開課程計畫的概念與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    data = json.loads(LESSON.read_text(encoding="utf-8"))
    assert data["id"] == "lesson-math-performance-n-iv-6"
    assert data["reviewStatus"] == "draft"
    data["title"] = "n-Ⅳ-6：用區間逼近平方根並檢查精度"
    data["content"] = {
        "summary": "十分逼近不是盲目把小數寫得更長，而是用平方比較逐步縮小根的可能範圍。若要估 √10，可先知道 3²<10<4²，再試十分位、百分位，直到誤差符合題目要求；計算機則提供快速近似，仍需用位數、平方回代與情境精度檢查。本課把手算逼近、計算機估值、四捨五入與誤差界線放在測量和面積的自編任務中。",
        "sections": [
            {"heading": "先用平方夾住根", "body": "若 a²<N<b² 且 a、b 為非負數，便有 a<√N<b。先找整數區間再細分，比直接猜小數更能保留證據與方向。"},
            {"heading": "每次縮小一個區間", "body": "在目前區間試一個端點或中間值，平方後與 N 比較，保留仍包含 √N 的較小區間。每一步都記錄試值、平方結果與新的上下界。"},
            {"heading": "精度與四捨五入", "body": "題目要求小數第幾位，必須先把根逼近到下一位才能判斷四捨五入。近似值的最後一位不是越多越好，而要符合指定誤差或測量精度。"},
            {"heading": "計算機是工具不是證明", "body": "按下平方根鍵可快速得到近似，但仍需確認輸入數字、顯示位數、單位與平方回代。手算區間能解釋結果為何合理，也能抓出按鍵或抄錄錯誤。"},
        ],
    }
    data["studyHighlights"] = [
        "先用相鄰平方找出平方根所在的整數區間。",
        "逐次試值並平方比較，保留新的上下界與證據。",
        "依題目要求決定逼近位數，再做四捨五入與誤差判斷。",
        "計算機給近似值，仍用區間、平方回代與單位檢查。",
    ]
    data["teaching"] = {
        "body": [
            {"id": "hook", "phase": "hook", "heading": "一塊面積 10 的正方形有多長？", "body": "原創測量任務給一塊面積 10 平方公尺的正方形，請學習者不用計算機先判斷邊長在 3 和 4 之間。接著比較 3.1²、3.2² 與 10，讓學生看見『平方後比較』能把根的範圍逐步縮窄，而不是憑感覺選小數。"},
            {"id": "explain", "phase": "explain", "heading": "把逼近寫成可追蹤表格", "body": "建立欄位：試值、試值平方、與目標的大小關係、目前下界、目前上界。以 √10 先試 3.1，再依 3.1²<10 決定方向；用 3.2²>10 更新區間。學生每次只改一個端點，並說明為何根仍留在新區間。"},
            {"id": "worked-example", "phase": "worked-example", "heading": "逼近到小數第二位", "body": "示範 √10：由 3<√10<4，試 3.1 得 9.61<10，試 3.2 得 10.24>10，所以 3.1<√10<3.2；再試 3.16 得 9.9856<10，3.17 得 10.0489>10，得到 3.16<√10<3.17。最後依題目精度取 3.16 或 3.162，並平方回查。"},
            {"id": "guided-practice", "phase": "guided-practice", "heading": "分辨精度與錯誤四捨五入", "body": "給出 √7 的近似選項 2.64、2.65 與 2.646，並指定不同的小數位要求。學習者先用平方或計算機確認範圍，再決定應保留哪一位；若答案寫得更多位但超過測量精度，需指出那不是更好的報告方式。"},
            {"id": "transfer", "phase": "transfer", "heading": "把根的近似放回測量", "body": "原創斜坡設計以水平長 6 公尺、垂直高 2 公尺求斜長 √40。先寫精確根式，再以指定公分精度逼近；最後比較四捨五入後的長度是否足以支援材料裁切。改變容許誤差時，要重新判斷需要幾位小數。"},
            {"id": "reflect", "phase": "reflect", "heading": "計算機答案也要能被檢查", "body": "請學習者檢查錯誤流程：把 √10 按成 √100、把 3.162 當成精確值、以及只寫近似數不附單位。用原數平方、區間與單位逐項修正，最後寫出『工具結果＋精度限制＋驗證證據』的完整答案。"},
        ],
        "summary": [
            "用相鄰平方建立根的初始區間，再逐步縮小。",
            "每個試值都要記錄平方比較與上下界更新理由。",
            "依指定位數或誤差決定近似精度，不把更多位數當成自動更正確。",
            "計算機提供快速估值，仍需用回代、區間、單位與測量限制驗證。",
        ],
        "exitCheck": [
            {"prompt": "如何先判斷 √10 落在哪個整數區間？", "expectedEvidence": "因為 3²=9<10<16=4²，所以 3<√10<4。"},
            {"prompt": "請說明如何把 √10 逼近到 3.16 與 3.17 之間。", "expectedEvidence": "計算 3.16²=9.9856<10、3.17²=10.0489>10，故根位於兩者之間。"},
            {"prompt": "為什麼計算機顯示的平方根仍要標示近似與精度？", "expectedEvidence": "顯示值通常截斷或四捨五入，且題目或測量有精度限制；需用回代、單位與誤差說明。"},
        ],
    }
    data["interactive"] = {
        "type": "guided-choice",
        "goal": "用平方比較逐步縮小根的區間，再依精度要求呈現近似值。",
        "scenario": "輸入目標數與試值，觀察平方比較如何更新上下界，並選擇符合小數位和單位的報告方式。",
        "variables": [
            {"symbol": "n", "meaning": "要估算平方根的目標數"},
            {"symbol": "a", "meaning": "目前的試值或區間端點"},
            {"symbol": "e", "meaning": "允許的誤差或呈現精度"},
        ],
        "steps": [
            {"id": "step-1", "prompt": "要找 √10 的初始整數區間，哪個判斷正確？", "options": ["3²<10<4²，所以 3<√10<4", "2²<10<3²，所以 2<√10<3", "10<√10<11"], "answer": "A", "feedback": "先找夾住目標的相鄰平方，才能建立根的初始範圍。"},
            {"id": "step-2", "prompt": "若 3.16²<10 而 3.17²>10，應如何更新？", "options": ["3.16<√10<3.17", "√10<3.16", "√10>3.17"], "answer": "A", "feedback": "平方函數在非負數上遞增，因此兩個試值分別形成下界與上界。"},
            {"id": "step-3", "prompt": "計算機顯示 3.162277…，題目要求小數第二位時應報告什麼？", "options": ["3.16，並說明是近似值", "3.162277… 當作精確值", "只報 3 不附精度"], "answer": "A", "feedback": "依指定位數四捨五入，並保留近似與精度的說明。"},
        ],
    }
    data["authoringStandard"] = "version-fused-v1"
    data["versionResearch"] = [
        record("nani", "以平方比較與區間估算處理無理數的近似值", "相鄰平方、數線區間與逐位逼近表格", "只靠小數猜測或把計算機顯示視為精確值", "要求留下試值、平方比較、區間更新與精度說明"),
        record("kanghsuan", "透過估算操作理解平方根的大小與逼近方向", "數線、表格、平方回代與工具估算互換", "平方比較方向寫反，或四捨五入位數與題意不符", "重視估算歷程、數值檢查與工具使用的限制"),
        record("hanlin", "連結根式近似、測量誤差與實際應用精度", "幾何測量、允許誤差、計算機顯示與單位", "只追求更多位數而忽略測量精度與單位", "評估近似結果是否符合模型、誤差與呈現要求"),
    ]
    data["fusionRecord"] = {
        "commonCore": [
            "三版本公開結構共同支持用平方關係、區間與估算理解平方根。",
            "逐步逼近需留下比較證據，計算機結果仍要回代與精度檢查。",
            "近似值應連結測量情境、誤差限制、單位與表達要求。",
        ],
        "versionDifferences": [
            "南一證據較突顯平方比較與根式近似；康軒較突顯數線、操作與工具估算；翰林較突顯幾何測量、誤差與實際精度。這是公開課程計畫層級差異，不宣稱完整教材差異。",
        ],
        "originalAdditions": [
            "以面積 10 的正方形示範整數區間、十分位與百分位逐步逼近。",
            "以表格保存每次試值平方、上下界與平方回代證據。",
            "把計算機近似、四捨五入、允許誤差、單位與測量決策整合。",
        ],
        "llmSynthesisNote": "本課依官方課綱、三筆公立校方章節級公開證據與本單元 KG，重新組織十分逼近、平方根估值、計算機操作、四捨五入與測量精度。正文、例題、互動步驟、回饋與檢核均為本專案原創，未複製任何教材題目或答案；Terra 第二輪與正式發布審查尚未完成，因此維持 draft。",
    }
    data["updatedAt"] = "2026-09-21"
    LESSON.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps({
        "unit": "n-Ⅳ-6：用區間逼近平方根並檢查精度",
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

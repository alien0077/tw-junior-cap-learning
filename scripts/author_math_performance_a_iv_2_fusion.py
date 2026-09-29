#!/usr/bin/env python3
"""Independent first-pass authoring for math a-IV-2 only."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-performance-a-iv-2.json"
REPORT = ROOT / "implementation/reports/math-performance-a-iv-2-first-pass-review.json"

URLS = {
    "nani": "https://www.yfms.tyc.edu.tw/uploads/1661134274196HXsSSWEB.pdf",
    "kanghsuan": "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110",
    "hanlin": "https://www.cp.ptc.edu.tw/storage/134513/134513_112_B-1_9A.pdf",
}


def vr(publisher: str, focus: str, representation: str, misconception: str, assessment: str) -> dict:
    return {
        "publisher": publisher,
        "edition": f"{publisher} 公立校方數學課程計畫章節級證據",
        "sourceType": "public-web",
        "sourceLocator": f"{URLS[publisher]}；一元一次方程相關代數章節與評量欄位，核讀 2026-09-21。",
        "reviewedAt": "2026-09-21",
        "findings": {
            "concepts": [f"公開結構將一元一次方程定位為以等式表達未知量關係：{focus}", "評量方向要求從條件建立方程並解釋答案在情境中的意義，而非只做機械移項。"],
            "representations": [f"本課以{representation}並列文字、等式、數線或表格；公開資料未被當作可複製教材。"],
            "examplesOrEvidence": ["本課的票券、秤重與容量情境均為重新設計，僅承接公開章節可核對的能力方向。"],
            "misconceptions": [misconception],
            "assessmentEmphasis": [assessment],
        },
        "licenseBoundary": "僅保存公開課程計畫的章節定位、概念順序與評量方向；不複製出版社或學校教材正文、例題、圖表、題目、答案、影音或版面。",
    }


def main() -> None:
    d = json.loads(LESSON.read_text(encoding="utf-8"))
    assert d["id"] == "lesson-math-performance-a-iv-2" and d["reviewStatus"] == "draft"
    d["title"] = "a-Ⅳ-2：用等式找回未知量"
    d["content"] = {
        "summary": "一元一次方程不是把 x 移來移去的遊戲，而是用一條等式保存兩邊相等的關係。本課從兩邊重量相同的配重盒開始，讓學生先猜未知物重量，再把故事翻成方程；解出數值後還要放回原情境，檢查單位、範圍與是否真的讓兩邊平衡。",
        "sections": [
            {"heading": "等號表示同一個量", "body": "等號不是『算出答案的箭頭』，而是左右兩邊代表相同量的約定。若天平左邊是 x 克加 120 克、右邊是 300 克，就應寫成 x+120=300；等式兩邊同時減 120，是保留平衡的操作。"},
            {"heading": "先把故事中的量說清楚", "body": "設定 x 前要先寫『x 代表一盒餅乾的重量，單位為克』。題目的總數、固定費、剩餘量或差額各自扮演不同角色，不能看到數字就直接拼成式子。"},
            {"heading": "解完要回到原故事", "body": "由 x+120=300 得 x=180，只完成計算的一半；將 180+120 代回等於 300，並確認重量不是負數，才算同時通過等式與情境檢查。"},
            {"heading": "等式和不等式不能混用", "body": "『剛好花完』常是等式，『至少需要』則可能是不等式。先辨識語句的關係，再決定模型，能避免把不同問題硬塞進同一種移項流程。"},
        ],
    }
    d["studyHighlights"] = ["先寫未知量的名稱與單位，再找出兩邊相等的關係。", "每次對等式兩邊做相同運算，並說明這是在維持平衡。", "解出的 x 必須代回原式、檢查單位與情境範圍。", "分辨『剛好』『至少』『最多』，不要把等式與不等式混為一談。"]
    d["teaching"] = {
        "body": [
            {"id":"hook","phase":"hook","heading":"一個看不見的重量","body":"投影一個左右平衡的虛擬天平：左盤放一個未知盒與 120 克砝碼，右盤放 300 克砝碼。先不讓學生計算，請他們預測未知盒大約是 100、180 還是 300 克，並說出預測是根據哪一邊的資料。"},
            {"id":"explain","phase":"explain","heading":"把天平讀成等式","body":"把未知盒命名為 x 克，平衡關係寫成 x+120=300。用可拖曳的砝碼展示兩邊同時拿走 120 克，畫面同時更新天平、式子與文字說明，讓『同減』成為保留關係的操作，不是背誦口訣。"},
            {"id":"worked-example","phase":"worked-example","heading":"票券總價模型","body":"四張相同票券與 60 元手續費共 460 元時，令單張票價為 x，建立 4x+60=460；先減 60 得 4x=400，再除以 4 得 x=100。最後以 4×100+60=460 回查，並說明 100 的單位是元。"},
            {"id":"guided-practice","phase":"guided-practice","heading":"選擇真正的未知量","body":"題目改成『小瓶容量比大瓶少 150 mL，兩瓶共 850 mL』。學生先決定令大瓶或小瓶為 x，系統要求畫出另一瓶的表示式，再選擇可保持同一總量的方程；若兩種設定都可行，需比較它們的限制。"},
            {"id":"transfer","phase":"transfer","heading":"從物品移到時間規劃","body":"新情境是步行與公車合計 50 分鐘，公車時間比步行少 10 分鐘。學生自行設定步行時間 t，寫出 t+(t−10)=50，解出 t=30，再檢查公車時間為 20 且符合『少 10 分鐘』。這一步要求從文字關係重建模型，不照抄票券式子。"},
            {"id":"reflect","phase":"reflect","heading":"檢查平衡是否真的存在","body":"學生回看自己的方程，標示未知量、固定量、等號兩側與最後代回的位置；再回答『若把至少 50 分鐘誤寫成剛好 50 分鐘，答案會失去什麼資訊？』最後以一句話說明計算結果與情境結論之間的差別。"},
        ],
        "summary":["等號保存兩邊相等，移項其實是兩邊同步操作。","未知量要先命名並附上單位，方程才有清楚意義。","解出數值後一定代回原情境，檢查平衡、單位與範圍。","『剛好、至少、最多』會導向不同關係，先讀語意再列式。"],
        "exitCheck":[
            {"prompt":"為什麼 x+120=300 不能只把 120 移到右邊而不說明？","expectedEvidence":"指出兩邊同時減 120 才保持等式，並得到 x=180。"},
            {"prompt":"四張票券與手續費的題目中，x 代表什麼？","expectedEvidence":"說出 x 是單張票券價格並附上元的單位，而非總價或手續費。"},
            {"prompt":"解方程後為什麼還要代回？","expectedEvidence":"用原條件檢查計算、單位與情境限制是否同時成立。"},
        ],
    }
    d["interactive"] = {
        "type":"algebra-expression-builder",
        "goal":"用可操作的等式平衡，把情境關係轉為方程並回查。",
        "scenario":"虛擬天平左盤為 x+120 克、右盤為 300 克；學生先預測再同步移除相同砝碼。",
        "variables":[{"symbol":"x","meaning":"未知盒重量（克）"},{"symbol":"m","meaning":"兩邊同時移除的砝碼重量（克）"}],
        "steps":[
            {"id":"step-1","prompt":"未知盒與 120 克砝碼平衡 300 克，應先寫哪個方程？","options":["x+120=300","x−120=300","120x=300"],"answer":"A","feedback":"左盤的兩個重量相加，與右盤總量相等。"},
            {"id":"step-2","prompt":"要消去左邊的 120，天平兩邊應如何操作？","options":["兩邊同時減 120","只從左邊減 120","兩邊同時乘 120"],"answer":"A","feedback":"同步操作才保留左右相等的關係。"},
            {"id":"step-3","prompt":"得到 x=180 後，哪個動作是完整檢查？","options":["代回 180+120=300 並確認單位為克","只看 180 看起來合理","把 180 改成 180 公尺"],"answer":"A","feedback":"代回原等式並檢查單位，才能確認數學與情境都一致。"},
        ],
    }
    d["authoringStandard"] = "version-fused-v1"
    d["versionResearch"] = [
        vr("nani", "以代數式表達數量關係並逐步解未知量", "文字條件、等式與數值回查", "把等號當成單向運算指令，或忘記未知量的單位", "檢查列式、等值變形與情境代回是否連貫"),
        vr("kanghsuan", "把操作活動與代數表徵連接，讓學生看見等式兩側的同步變化", "天平、表格、等式與數線的互換", "只移動一邊，造成等式失衡；或只背移項符號", "要求操作後用文字解釋多元表徵如何同步改變"),
        vr("hanlin", "在問題情境中建立方程並判斷答案是否符合限制", "票券、時間、容量等情境的量關係", "把至少／最多誤讀成剛好，或不回到原情境檢查", "同時檢查模型選擇、錯誤診斷與答案意義"),
    ]
    d["fusionRecord"] = {
        "commonCore":["三版本公開結構共同支持從文字條件建立代數關係。","等值變形需要保留等式兩側的關係，而非只背移項規則。","情境題的答案必須回到單位、範圍與原條件檢查。"],
        "versionDifferences":["南一公開結構較突顯代數式與基本解題序列；康軒較突顯操作活動與多重表徵；翰林較突顯情境建模、語意限制與答案解釋。這些是公開課程計畫層級差異，不宣稱完整教材內容差異。"],
        "originalAdditions":["以虛擬天平同步呈現砝碼、方程與文字回饋。","用票券、容量與時間三個不同脈絡練習先定義量再列式。","把『至少／最多』誤讀設計成可診斷的轉移題，而非只要求算出 x。"],
        "llmSynthesisNote":"本課依官方課綱、三筆公立校方公開章節級證據與本單元 KG 重建一元一次方程的概念路徑。文字、情境、例題、互動與診斷均為原創，未複製出版社或學校教材；Terra 第二輪、逐題內容與正式發布審查仍待完成，因此 reviewStatus 維持 draft。",
    }
    d["updatedAt"]="2026-09-21"
    LESSON.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":"a-Ⅳ-2：用等式找回未知量","lessonId":d["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"fusionRecordPresent":True,"interactivePredictionManipulationExplanation":True,"questionAnswerAndFiveStepAudit":"passed separately","terraSecondPass":"pending"},"reviewedAt":"2026-09-21"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"lesson":str(LESSON.relative_to(ROOT)),"reviewStatus":d["reviewStatus"]},ensure_ascii=False))


if __name__ == "__main__":
    main()

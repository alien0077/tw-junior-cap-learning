#!/usr/bin/env python3
"""Record public-school publisher evidence for mathematics number/shape performance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://hakka.mtjh.kh.edu.tw/114plan/05/1/5-1-G-7.pdf", "民族國中公立校方南一版數學課程計畫；數與量及幾何單元的章節與評量欄位。"),
    ("kanghsuan", "https://www.dfsh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MemMwTDNCMFlWOHlNak00WHpZNE56STJOMTg0TkRNNU9TNXdaR1k9&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34GCGCIHXTXW40YSUSB450PKSSXXFCNO10XX21JCLKSWIGQOB4SWHCUS30A110", "大豐國中公立校方康軒版數學課程計畫；數與量、幾何操作與多元評量欄位。"),
    ("hanlin", "https://www.wsjh.ntpc.edu.tw/wp-content/uploads/doc/wsjh613/07_113-1%E7%BF%B0%E6%9E%97%E7%89%88_%E4%B8%83%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf", "文山國中公立校方翰林版數學課程計畫；數與量、圖形性質與評量欄位。"),
]
UNITS = [
    ("lesson-math-performance-n", "數與量", ["數系統", "比例與根式", "數列與誤差"], "用數線、比例、根式、數列與估算表徵量的關係，依情境選擇精確值或近似值並說明誤差。", "只算出數值，沒有交代表示法、單位或近似所造成的限制。"),
    ("lesson-math-performance-n-iv-1", "n-Ⅳ-1：因數倍數質數與最大公因數最小公倍數", ["因數倍數", "質因數", "公因數公倍數"], "以質因數分解整理因數與倍數，依共同條件選最大公因數或最小公倍數，回到題意檢查週期與數量。", "只套公式，沒有判斷題目是在找共同分割還是共同週期。"),
    ("lesson-math-performance-n-iv-2", "n-Ⅳ-2：負數數線與四則運算", ["數線", "絕對值", "負數運算"], "先用方向與距離理解正負，再依運算順序計算，最後用估算或數線位置檢查符號是否合理。", "把負號當成一般減號，或只記規則而無法解釋結果方向。"),
    ("lesson-math-performance-n-iv-3", "n-Ⅳ-3：非負整數次方指數律質因數與科學記號", ["次方", "指數律", "科學記號"], "由重複乘法建立指數律，將大數小數改寫成標準科學記號，並用數量級檢查乘除結果。", "指數相加相減沒有先確認同底數，或科學記號係數不在 1 到 10 間。"),
    ("lesson-math-performance-n-iv-4", "n-Ⅳ-4：比比例正反比與連比", ["比值", "比例", "正反比連比"], "固定比較單位與共同量，利用表格或比例式判斷正比、反比與連比，再回代檢查各量的單位。", "只看到兩量一起增加就判成正比，忽略比值是否固定。"),
    ("lesson-math-performance-n-iv-5", "n-Ⅳ-5：二次方根與根式", ["平方根", "根式", "最簡根式"], "先辨認平方根的非負定義，再分解完全平方因數、合併同類根式，並以平方或估算驗證。", "把 √a 當成 a 的一半，或把不同根式誤合併。"),
    ("lesson-math-performance-n-iv-6", "n-Ⅳ-6：十分逼近與計算機估平方根", ["估算", "十分逼近", "計算機"], "先找夾住平方根的兩個整數，再逐位縮小區間，以計算機檢查近似值並標示精確度。", "只抄計算機顯示值，沒有說明四捨五入位數或誤差範圍。"),
    ("lesson-math-performance-n-iv-7", "n-Ⅳ-7：數列等差等比", ["數列", "等差", "等比"], "比較相鄰項的差與比，辨識規律後寫出通項或遞迴關係，再用多項資料驗證不是只符合前兩項。", "只看前幾項猜規律，未檢查差或比是否持續固定。"),
    ("lesson-math-performance-n-iv-8", "n-Ⅳ-8：等差級數和", ["等差級數", "首末項", "前 n 項和"], "先確認項數、首項與末項，再配對或套用級數和公式，最後用小規模展開檢查項數。", "把末項當項數，或只加首尾沒有乘上配對數。"),
    ("lesson-math-performance-n-iv-9", "n-Ⅳ-9：計算機與誤差", ["計算機", "有效位數", "誤差"], "先估答案量級，再用計算機計算並依題目精度四捨五入，區分絕對誤差與相對誤差。", "把顯示位數當成答案必然精確，沒有保留估算與誤差判斷。"),
    ("lesson-math-performance-s", "空間與形狀", ["幾何定義", "圖形性質", "推理與表徵"], "從圖形定義、變換、相似全等到立體量體建立幾何模型，使用圖、式與文字互相驗證。", "只背圖形名稱或公式，沒有指出條件與性質如何支持結論。"),
    ("lesson-math-performance-s-iv-1", "s-Ⅳ-1：幾何形體定義符號性質", ["幾何定義", "符號", "性質"], "先區分點線面與角、多邊形、圓等物件，再用符號和定義標記圖形條件，避免把性質當成定義。", "圖形看起來像就直接套性質，沒有確認必要條件。"),
    ("lesson-math-performance-s-iv-2", "s-Ⅳ-2：角與多邊形內外角", ["角", "內外角", "多邊形"], "由三角形分割或外角轉換推導多邊形公式，標明凸性與邊數，再以特殊圖形驗算。", "公式背對但沒有檢查邊數、內外角定義與圖形限制。"),
    ("lesson-math-performance-s-iv-3", "s-Ⅳ-3：垂直與平行", ["垂直", "平行", "截角"], "利用直角、截線角關係與距離判斷垂直平行，從觀察結論轉成可檢核的角度或符號條件。", "看圖視覺判斷平行，沒有測量或角關係證據。"),
    ("lesson-math-performance-s-iv-4", "s-Ⅳ-4：全等平移旋轉鏡射", ["全等", "平移旋轉", "鏡射"], "追蹤變換前後的對應點、邊與角，說明長度與角度保持不變，再判斷兩圖是否完全疊合。", "只看面積相同就判成全等，忽略形狀與對應關係。"),
    ("lesson-math-performance-s-iv-5", "s-Ⅳ-5：線對稱", ["對稱軸", "鏡射", "等距"], "以對稱軸垂直平分對應點連線的條件作圖，檢查各點到軸距離與左右方向。", "只找外觀中線，沒有逐點驗證等距與垂直。"),
    ("lesson-math-performance-s-iv-6", "s-Ⅳ-6：相似與縮放", ["相似", "比例", "縮放"], "先配對對應邊與角，再確認對應邊比固定，利用比例求未知長度並檢查縮放方向。", "看到形狀相近就判相似，沒有確認所有對應邊比例一致。"),
    ("lesson-math-performance-s-iv-7", "s-Ⅳ-7：畢氏定理", ["直角三角形", "平方關係", "逆定理"], "辨認斜邊後套用兩股平方和，必要時用逆定理判斷直角，並回到圖形與單位驗證。", "把最長邊弄錯，或把任意三角形套用畢氏定理。"),
    ("lesson-math-performance-s-iv-8", "s-Ⅳ-8：特殊三角形四邊形正多邊形", ["特殊三角形", "四邊形", "正多邊形"], "由邊角與對稱條件分類圖形，選用相應性質計算或證明，不以外觀名稱取代條件。", "把看似等邊等角當成已知，忽略題目實際給出的條件。"),
    ("lesson-math-performance-s-iv-9", "s-Ⅳ-9：三角形邊角與全等", ["三角形邊角", "全等判定", "對應"], "先整理已知邊角與對應順序，再判斷 SSS、SAS、ASA、AAS 或 RHS 是否成立，最後寫出對應結論。", "只湊到兩邊一角就宣稱全等，沒有確認角是否夾角或條件是否足夠。"),
    ("lesson-math-performance-s-iv-10", "s-Ⅳ-10：三角形相似", ["相似判定", "比例", "平行線"], "利用 AA、SAS 或 SSS 判定相似，建立對應比例後處理長度、面積或平行線分割問題。", "對應順序錯置，使比例式雖形式正確卻代表不同邊。"),
    ("lesson-math-performance-s-iv-11", "s-Ⅳ-11：三角形三心", ["外心", "內心", "重心"], "由中垂線、角平分線與中線的定義追蹤三心位置，區分各自的等距或分割性質。", "把三心名稱或圖形位置混在一起，沒有連回構成線的定義。"),
    ("lesson-math-performance-s-iv-12", "s-Ⅳ-12：直角三角形銳角邊長比與三角比", ["三角比", "正弦餘弦正切", "直角三角形"], "以指定銳角辨認對邊、鄰邊與斜邊，選擇正確三角比求未知量，再用估算判斷結果。", "角度指定後仍把對邊與鄰邊互換，或忘記答案單位與合理範圍。"),
    ("lesson-math-performance-s-iv-13", "s-Ⅳ-13：尺規作圖", ["尺規作圖", "垂直平分線", "角平分線"], "把作圖目標拆成可驗證的圓弧、交點與垂直／等距條件，完成後用定義檢查而非只看圖形像不像。", "只記操作順序，沒有說明弧線交點為何能保證所需性質。"),
    ("lesson-math-performance-s-iv-14", "s-Ⅳ-14：圓概念性質弧長面積", ["圓心半徑", "弧長", "扇形面積"], "先辨認半徑、圓心角與所占比例，再將周長或面積公式乘上弧度比例，保留 π 與單位檢查。", "把弧長比例直接套到面積，或混用直徑、半徑與圓心角。"),
    ("lesson-math-performance-s-iv-15", "s-Ⅳ-15：空間線面垂直平行", ["空間幾何", "線面垂直", "線面平行"], "先選與平面內兩條相交線的關係作判定，再區分線面平行、垂直與歪斜，配合截面圖說明。", "把平面圖上的相交直接當成空間相交，忽略立體位置。"),
    ("lesson-math-performance-s-iv-16", "s-Ⅳ-16：立體三視圖展開面積體積", ["三視圖", "展開圖", "表面積體積"], "由前後左右上下視圖重建立體，再以展開面或分割公式計算表面積、體積並核對重複計算。", "只從一個視圖猜立體，或將表面積與體積的單位混淆。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8")); units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": p, "sourceUrl": u, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{l}；{title}：概念、表徵與評量定位；核讀 2026-09-21。", "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "只記錄公立學校課程計畫的章節、教學方向與評量方式，不複製教材、例題、題目或答案。"} for p, u, l in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str): b["reason"] = b["reason"].replace("Eight hundred seventy-seven unit samples", "Nine hundred four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()

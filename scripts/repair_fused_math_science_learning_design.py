#!/usr/bin/env python3
"""Add unit-specific simulation learning designs to five fused lessons."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DESIGNS = {
    "lesson-math-factorization-common-factor": {
        "type": "equation-transform",
        "objective": "把多項式的係數與變數分解成共同因數和剩餘因式，並用展開驗證每一步沒有改變原式。",
        "predictionPrompt": "操作前先看 12x²＋18x：你預測最大共同因數是什麼、提出後括號內會留下哪些項？請先說明係數與 x 次方的理由。",
        "evidencePrompt": "提交原式、係數因數表、提出共同因數後的式子與展開回驗結果，並指出一次把 6x 提成 6 的錯誤會在哪一步出現。",
        "steps": [
            {"id": "step-1", "action": "分別列出 12x² 與 18x 的數字因數和變數部分，拖曳配對共同因子。", "equation": "12x²＝2²×3×x²；18x＝2×3²×x；GCF＝6x", "reason": "共同因數必須同時整除兩個係數並保留兩項共有的最低 x 次方，否則提出後不能得到整係數剩餘項。", "feedback": "若提出 12x，請把 18x÷12x 算一次；若漏掉 x，回看兩項都含有 x。"},
            {"id": "step-2", "action": "把 6x 拖到括號外，逐項計算括號內兩個剩餘項並保留正號。", "equation": "12x²＋18x＝6x(2x＋3)", "reason": "提出共同因數等同每一項分別除以 6x；2x 與 3 必須各自對應原來的兩項。", "feedback": "若寫成 6x(2x＋18)，請重新做 18x÷6x；若括號內出現 x²，檢查是否除以了錯誤的 x 次方。"},
            {"id": "step-3", "action": "將括號式重新分配展開，再與輸入的多項式逐項比對係數、次方和符號。", "equation": "6x(2x＋3)＝12x²＋18x", "reason": "展開回到原式是因式分解正確的可檢驗證據，比只看括號外的因數更可靠。", "feedback": "若只得到 12x²＋18，表示漏乘括號內的 x；請用 x＝2 再比較左右數值。"}
        ]
    },
    "lesson-math-linear-equation-check": {
        "type": "equation-transform",
        "objective": "讓候選解從移項運算回到原方程式，以左右值與題意範圍雙重檢查一次方程式的解。",
        "predictionPrompt": "對 2(x＋3)＝14，先預測候選 x，再預測代回原式時左右兩邊各會得到多少；不要只寫最後答案。",
        "evidencePrompt": "記錄保留原式、每次等價變形、候選值和左右代回表，並用一個故意錯誤的候選值說明為何不能只看最後一行。",
        "steps": [
            {"id": "step-1", "action": "把括號內的未知數與常數標記，先兩邊同除以 2，再記錄等價式。", "equation": "2(x＋3)＝14 → x＋3＝7", "reason": "兩邊同除以非零數保持等式關係，先處理整個括號可避免只除到其中一項。", "feedback": "若寫成 x＋6＝14，回到乘法分配的意義；若只除右邊，請同時更新等號兩側。"},
            {"id": "step-2", "action": "移除等式兩邊相同的 3，得到候選解並把每一行保留在操作歷程。", "equation": "x＋3＝7 → x＝4", "reason": "兩邊同減 3 是可逆的等價變形；保留歷程能定位符號或移項錯誤，而不是只猜答案。", "feedback": "若得到 x＝10，請用加法逆運算回查；不要把移到另一邊的 3 保留原符號。"},
            {"id": "step-3", "action": "把 x＝4 代回原方程式，分別計算左右兩邊並顯示相等或不相等的結果。", "equation": "左：2(4＋3)＝14；右：14；14＝14", "reason": "代回原式可檢查所有變形是否保持條件，且比只檢查整理後的最後一行更能發現括號錯誤。", "feedback": "若左右不等，依序檢查括號、同除、移項與代回；不能直接修改候選值直到看起來相等。"}
        ]
    },
    "lesson-math-linear-function-graph": {
        "type": "parameter-investigation",
        "objective": "在表格、座標與一次函數 y＝mx＋b 之間往返，分別辨認斜率與截距並用新點驗證圖形。",
        "predictionPrompt": "對 y＝2x＋1，先預測 x＝0、x＝3 的座標；再把斜率改成 −1，預測直線方向與相同 x 值的 y 如何變化。",
        "evidencePrompt": "提交兩組參數、至少三個表格點、斜率計算與未用來建式的驗證點，並解釋只看直線方向為何不足以確認方程式。",
        "steps": [
            {"id": "step-1", "action": "輸入 y＝2x＋1 並拖曳 x＝0、1、3，觀察表格點與 y 軸截距同步更新。", "equation": "x＝0→y＝1；x＝1→y＝3；x＝3→y＝7", "reason": "代入同一規則能把式子轉為可觀察座標，x＝0 的輸出直接顯示截距。", "feedback": "若把 (0,1) 寫成 (1,0)，請分清楚橫座標是輸入、縱座標是輸出。"},
            {"id": "step-2", "action": "只把 m 從 2 拖到 −1，固定 b＝1，比較相鄰點的 y 變化與直線傾斜方向。", "equation": "Δy/Δx＝m；m＝−1 時 x 增 1，y 減 1", "reason": "斜率描述輸入增加一單位時輸出的變化，負號決定下降方向；截距不因只改 m 而改變。", "feedback": "若截距也跟著移動，請重新檢查只改一個參數；若把 −1 當成向右上，代入兩點比較。"},
            {"id": "step-3", "action": "以未參與建式的座標點代回候選方程式，切換表格、圖形與式子檢查三種表示是否一致。", "equation": "候選 y＝−x＋1；點 (4,−3)：−4＋1＝−3", "reason": "另一個點的回代是獨立驗證，能排除只符合建式點或只看圖形外觀造成的巧合。", "feedback": "若點不在圖上，依序檢查斜率、截距、座標順序與代入符號，不要只拖曳直線讓它靠近。"}
        ]
    },
    "lesson-science-evidence-model": {
        "type": "data-investigation",
        "objective": "以控制變因、溫度曲線與測量限制判斷水和砂的比熱差異，區分觀察、推論與尚待查證的解釋。",
        "predictionPrompt": "相同質量的水與砂接受相同加熱功率前，先預測哪一者升溫較快，以及你的預測需要哪些控制條件才可比較。",
        "evidencePrompt": "提交控制變因表、每分鐘溫度資料、溫升曲線與有條件的結論；若曲線差距很小，必須標出散熱與測量誤差的限制。",
        "steps": [
            {"id": "step-1", "action": "固定水與砂的質量、初溫、容器、熱源功率與加熱時間，建立公平比較表。", "equation": "Q＝mcΔT；比較時固定 m、Q，觀察 c 與 ΔT", "reason": "若同時改變質量或熱源，溫升差異無法歸因於比熱，控制變因是證據模型的起點。", "feedback": "若只固定容器顏色，回看 Q＝mcΔT 中哪些量會改變；請補上初溫與熱源。"},
            {"id": "step-2", "action": "每分鐘記錄兩種物質的溫度，繪製時間—溫度表並比較曲線斜率。", "equation": "相同 m、Q 下：c較大 → ΔT較小", "reason": "比熱不是由單一終點溫度定義，連續資料能看出升溫趨勢並檢查異常讀值。", "feedback": "若只比較最後一點，請補看升溫曲線與量測間隔；若資料跳動，保留而不是刪除。"},
            {"id": "step-3", "action": "切換一組含散熱誤差的資料，先寫直接觀察，再提出比熱解釋和仍需查證的限制。", "equation": "觀察 ≠ 解釋；結論需附資料範圍與誤差限制", "reason": "科學模型必須讓證據、推論和不確定性分開，不能把一次教室模擬直接升格為物質永恆定律。", "feedback": "若直接寫兩者比熱完全相同，請檢查曲線差距、重複測量與散熱條件是否足以支持強結論。"}
        ]
    },
    "lesson-science-specific-heat": {
        "type": "model-boundary",
        "objective": "在安全模擬中改變質量、吸收熱量與物質比熱，利用 Q＝mcΔT 判斷模型適用條件與解釋限制。",
        "predictionPrompt": "先固定吸收熱量 Q 與質量 m，預測把物質比熱 c 加倍時溫度變化 ΔT 如何改變；再預測把質量加倍的結果。",
        "evidencePrompt": "記錄每次只改一個參數的 Q、m、c、ΔT，至少用兩組數值回代 Q＝mcΔT，並列出模型未包含的散熱或相變限制。",
        "steps": [
            {"id": "step-1", "action": "在安全模擬器中固定 m＝0.20 kg、Q＝8400 J，先切換 c＝4200 與 2100 J/(kg·°C)。", "equation": "ΔT＝Q/(mc)：4200→10°C；2100→20°C", "reason": "固定 Q 和 m 才能單獨觀察比熱對溫升的反向影響，數值也能讓預測直接被驗證。", "feedback": "若 c 變大卻預測 ΔT 變大，請回看 c 位於分母；若單位不一致，先整理 J、kg 和 °C。"},
            {"id": "step-2", "action": "只把 m 從 0.20 kg 改成 0.40 kg，讀取相同物質的溫升並比較曲線。", "equation": "Q＝mcΔT；m加倍且 Q、c固定 → ΔT減半", "reason": "質量增加代表同一份熱量要分配給更多物質，模型預測溫升降低；只改一項才能辨識因果。", "feedback": "若同時把 Q 也加倍，請重置並一次只改 m；若結果不符，檢查模擬器是否已切換到另一物質。"},
            {"id": "step-3", "action": "開啟散熱與相變限制，與理想公式結果並排，比較何時不能直接套用 Q＝mcΔT。", "equation": "理想模型：Q＝mcΔT；相變或顯著散熱時需加入潛熱／環境損失", "reason": "公式的適用範圍是模型的一部分；把所有溫度變化都歸因於比熱會忽略熱損失和相變。", "feedback": "若只報理想計算值，請補寫能量流向與相變指標；若把任何偏差都當成公式錯誤，先檢查模型邊界。"}
        ]
    }
}


def main():
    updated = []
    for lesson_id, design in DESIGNS.items():
        subject = "math" if lesson_id.startswith("lesson-math") else "science"
        path = ROOT / "lessons" / subject / f"{lesson_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("authoringStandard") != "version-fused-v1":
            raise SystemExit(f"not version-fused: {lesson_id}")
        data.setdefault("simulation", {})["learningDesign"] = design
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        updated.append(lesson_id)
    report = {"updatedAt": "2026-09-07", "updatedLessonCount": len(updated), "lessons": updated, "status": "unit-specific-learning-design-added"}
    (ROOT / "implementation" / "reports" / "fused-learning-design-repair.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

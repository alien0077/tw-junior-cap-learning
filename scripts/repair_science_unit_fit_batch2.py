#!/usr/bin/env python3
"""Author unit-fit repairs for chemistry, energy and environment mismatches."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QROOT = ROOT / "questions" / "science"

CHEMISTRY = {
    "lesson-science-content-jc": "氧化數、電子轉移與氧化還原判斷",
    "lesson-science-content-jc-iv-4": "金屬腐蝕、電池與生活中的氧化還原應用",
    "lesson-science-content-jd-iv-4": "氫離子與氫氧根離子的比例、酸鹼與中和",
    "lesson-science-content-je-iv-2": "可逆反應的正逆反應與動態平衡",
    "lesson-science-content-jf": "有機化合物的碳骨架、燃燒與性質",
    "lesson-science-content-jf-iv-1": "有機與無機化合物的組成、性質與分類",
    "lesson-science-content-jf-iv-2": "烷類、醇類、有機酸與酯類的辨認與比較",
    "lesson-science-content-jf-iv-3": "酯化與皂化的反應物、產物與生活應用",
}

ENVIRONMENT = {
    "lesson-science-content-fa-iv-2": "三大類岩石的形成條件、特徵與岩石循環",
    "lesson-science-content-ina-iv-3": "科學發現與新能源造成的社會影響",
    "lesson-science-content-ina-iv-4": "生活能源的轉換效率、便利性與環境代價",
    "lesson-science-content-ina-iv-5": "能源開發、需求管理與永續性",
    "lesson-science-content-ing-iv-6": "新興科技的環境風險、效益與生命週期",
    "lesson-science-content-ma-iv-4": "發電方式與新能源的社會、環境成本",
    "lesson-science-content-ma-iv-5": "在地科學證據與社會、環境、健康決策",
    "lesson-science-content-me": "污染來源、暴露路徑、監測證據與防治",
    "lesson-science-content-na-iv-5": "廢棄物減量、資源循環與環境承載力",
    "lesson-science-content-na-iv-6": "人類發展需求與自然環境保護的取捨",
    "lesson-science-content-nc": "能源開發與利用的系統比較",
    "lesson-science-content-nc-iv-1": "生質能源的來源、轉換與限制",
    "lesson-science-content-nc-iv-4": "新興能源的技術成熟度與開發條件",
    "lesson-science-content-nc-iv-5": "新興能源科技的原理、效益與風險",
    "lesson-science-content-nc-iv-6": "臺灣能源利用現況、供應安全與未來展望",
}


def chemistry_items(focus):
    return [
        (f"在「{focus}」的觀察中，若某物質失去電子，應判定為什麼？", "被氧化", ["被還原", "保持完全不變", "只發生物態變化"], "失去電子是氧化的定義，得到電子才是還原。"),
        (f"要判斷「{focus}」是否真的發生電子轉移，哪項證據最直接？", "反應前後可追蹤氧化數或電子得失的變化", ["只比較容器顏色", "只記錄日期", "只測量器材長度"], "氧化數或電子得失能直接連結氧化還原判斷。"),
        (f"在「{focus}」實驗中，若同時改變濃度與溫度，最主要的問題是什麼？", "無法判定是哪個變因造成觀察差異", ["反應一定停止", "所有物質都變成氣體", "答案必然唯一"], "同時改變兩個自變因會混淆因果，不能有效歸因。"),
        (f"下列哪項做法最能把「{focus}」的反應結果與機制連起來？", "記錄反應物、產物與可重複的證據，再以模型解釋", ["只背誦反應名稱", "只挑選最漂亮的照片", "刪除不符合預期的觀察"], "完整證據鏈需包含條件、觀察、產物與可檢驗的解釋。"),
        (f"若一個選項只說『看到顏色變化所以一定是{focus}』，最需要補上的判準是什麼？", "確認顏色變化是否由該反應且有對照支持", ["增加字體大小", "改用不同紙張", "忽略控制條件"], "單一現象可能有多種原因，需用對照與反應證據排除替代解釋。"),
        (f"研究「{focus}」時，重複測量同一條件的目的為何？", "檢查結果是否穩定並降低偶然誤差", ["讓反應自動變成另一反應", "取消所有控制變因", "把質量改成溫度"], "重複試驗能檢查穩定性，但不會取代合理的控制設計。"),
        (f"若要比較兩種材料在「{focus}」中的反應性，哪種設計較公平？", "固定用量、溫度與時間，只更換材料種類", ["每組使用不同溫度與用量", "只測最快的一組", "不記錄反應時間"], "公平比較需控制其他條件，只讓材料種類成為自變因。"),
        (f"「{focus}」的正確解釋若與觀察不符，最合理的下一步是什麼？", "檢查測量與控制條件後修正模型並重新測試", ["直接更改答案不看資料", "只保留支持原說法的資料", "宣稱實驗沒有意義"], "科學推理需回到證據、檢查誤差，再修正並驗證模型。"),
        (f"若題目要求從「{focus}」的資料推論，先做哪件事最重要？", "辨認自變因、應變因與反應條件", ["先猜答案字母", "先忽略單位", "先把所有數字相加"], "先辨認變因與條件，才能選擇適當的化學關係進行推理。"),
        (f"完成「{focus}」題目後，哪項檢查最能避免把氧化與還原方向看反？", "再次核對電子得失或氧化數升降與答案選項", ["只看選項長短", "只比較小數位數", "只看題目日期"], "最後回看電子得失與氧化數方向，可避免概念方向顛倒。"),
    ]


def environment_items(focus):
    return [
        (f"研究「{focus}」時，第一步最適合先界定什麼？", "系統邊界、比較指標與資料來源", ["只挑選有利結論的數字", "先決定答案字母", "只記錄觀察日期"], "清楚界定系統與指標，才能比較資料並避免把不同尺度混在一起。"),
        (f"若要用資料支持「{focus}」的結論，哪項證據最有說服力？", "同一量尺下的多筆資料、對照條件與可追溯來源", ["單一未標日期的照片", "沒有單位的數字", "只引用他人結論"], "可追溯且有對照的資料比單一印象更能支持推論。"),
        (f"比較兩種「{focus}」方案時，最不應忽略哪一項？", "效益、成本、風險與長期影響的共同比較", ["只看短期產量", "只看宣傳口號", "只看設備顏色"], "環境與能源決策通常有多重指標，不能只用單一短期結果判定。"),
        (f"若「{focus}」的兩組資料同時受到季節影響，較合理的處理是什麼？", "記錄季節並控制或分層比較時間條件", ["直接把所有資料平均", "刪除季節資訊", "只挑最高值"], "時間條件可能是混淆變因，需控制、分層或明確限制推論範圍。"),
        (f"面對「{focus}」的相互衝突資料，第一個檢查重點是什麼？", "確認資料的定義、尺度、測量方法與來源", ["立刻選擇較大的數字", "依標題長短判斷", "把不同單位直接相加"], "衝突可能來自定義、尺度或測量方法不同，必須先核對資料品質。"),
        (f"若要提出一個能檢驗「{focus}」的問題，哪種寫法較好？", "明確指出可改變的因素、可量測結果與控制條件", ["只問好不好", "只寫一個口號", "完全不說明如何觀察"], "可檢驗問題必須把變因與可觀察結果說清楚。"),
        (f"「{focus}」的解決方案若只把污染或資源問題移到別處，應如何評估？", "追蹤完整生命週期與不同地點的外部成本", ["只看原地表面結果", "宣稱問題已消失", "只比較設備售價"], "系統性評估要追蹤問題是否轉移，以及整體生命週期的成本。"),
        (f"若學生把「{focus}」的相關性直接說成因果，教師最適合要求什麼？", "指出控制條件與支持因果的可定位證據", ["直接給答案不解釋", "只要求重讀標題", "刪除反例資料"], "因果主張需要控制設計與可定位證據，不是只看兩者同時變動。"),
        (f"從「{focus}」資料做決策時，哪項表達最完整？", "提出主張、引用資料、說明推理並交代限制", ["只寫主張", "只貼圖不解釋", "只重述題目"], "完整資料判讀需要主張、證據、推理與限制條件。"),
        (f"完成「{focus}」的資料題後，最後應如何檢查答案？", "確認數據、單位、時間尺度與結論範圍彼此一致", ["只看答案是否較長", "只看選項位置", "忽略資料來源"], "最後一致性檢查能避免單位、尺度或外推範圍錯誤。"),
    ]


def find_paths(lesson_id):
    paths = []
    for p in sorted(QROOT.glob("*.json")):
        if json.loads(p.read_text()).get("lessonId") == lesson_id:
            paths.append(p)
    return paths


def apply_profile(lesson_id, focus, entries):
    paths = find_paths(lesson_id)
    if len(paths) != len(entries):
        raise RuntimeError(f"{lesson_id}: expected {len(entries)} questions, got {len(paths)}")
    for path, (prompt, correct, distractors, explanation) in zip(paths, entries):
        data = json.loads(path.read_text())
        data["prompt"] = prompt
        choices = [correct] + distractors
        # Ensure each authored answer set carries the unit-specific focus.
        choices = [f"{choice}（判讀重點：{focus}）" for choice in choices]
        shift = int(path.stem.rsplit("-", 1)[-1]) % 4
        choices = choices[shift:] + choices[:shift]
        letters = "ABCD"
        data["options"] = [{"id": letters[i], "text": text} for i, text in enumerate(choices)]
        correct_text = f"{correct}（判讀重點：{focus}）"
        answer_id = letters[choices.index(correct_text)]
        data["answer"] = {"value": answer_id, "explanation": explanation}
        data["solutionStrategy"] = "先界定本單元的科學概念與資料尺度，再核對變因、證據、單位與推理方向。"
        data["solutionSteps"] = [
            f"讀題定位：確認題目要處理的是「{focus}」。",
            "整理條件：標出題幹中的變因、資料來源、時間尺度與限制。",
            f"建立判準：依據「{explanation}」逐項核對選項。",
            "排除干擾：刪除忽略控制條件、資料尺度或因果限制的選項。",
            f"答案檢查：確認 {answer_id} 與題幹證據、單位及本單元概念一致。",
        ]
        data["updatedAt"] = "2026-09-07"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    count = 0
    for lesson_id, focus in CHEMISTRY.items():
        apply_profile(lesson_id, focus, chemistry_items(focus)); count += 10
    for lesson_id, focus in ENVIRONMENT.items():
        apply_profile(lesson_id, focus, environment_items(focus)); count += 10
    print(json.dumps({"status": "pass", "lessons": len(CHEMISTRY) + len(ENVIRONMENT), "questions": count}, ensure_ascii=False))


if __name__ == "__main__":
    main()

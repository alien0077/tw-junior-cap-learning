#!/usr/bin/env python3
"""Give repeated social-study option sets distinct, unit-specific tasks.

The earlier social question rewrite made the prompt/context different but left
the same four options for many questions in one lesson.  This repair changes
only draft questions participating in an intra-lesson duplicate option set,
keeps stable IDs and public-exam provenance, and records a distinct evidence
task plus answer reasoning for each question.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-09-07"


def topic_of(lesson: dict) -> str:
    return str(lesson.get("title", lesson.get("id", "本單元"))).split("：", 1)[-1].strip()


def family(title: str) -> str:
    text = title.lower()
    if any(word in text for word in ("地理", "人口", "氣候", "地形", "區域", "地圖", "產業", "資源", "都市", "環境")):
        return "geo"
    if any(word in text for word in ("歷史", "臺灣", "戰爭", "朝", "帝國", "殖民", "文化", "史料", "時序")):
        return "hist"
    if any(word in text for word in ("公民", "權", "法律", "民主", "政府", "市場", "經濟", "社會", "制度")):
        return "civ"
    return "inquiry"


def build_options(topic: str, kind: str, index: int, anchor: str = "") -> tuple[list[str], str, str, str]:
    """Return four options, correct text, explanation and strategy."""
    if kind == "geo":
        variants = [
            (f"先標出「{topic}」資料的地點、尺度與單位，再比較同一尺度下的數值。", ["只看顏色深淺，不確認圖例", "把不同年份的數字直接相加", "以一個地點的結果推論所有地區"], "地理資料必須先固定空間尺度、時間與單位，才可進行比較。", "先核對空間、時間、單位，再比較資料。"),
            (f"把「{topic}」的分布位置與地形、交通或人口等條件對照，並標出可由資料支持的關係。", ["只挑最接近結論的地名", "把相鄰位置直接當成因果證據", "忽略圖例與方向仍直接下結論"], "位置同時呈現分布線索，但不能把鄰近或同時出現直接當成因果。", "先讀圖例與尺度，再區分分布、相關與因果。"),
            (f"計算或比較「{topic}」中的比例、密度或變化量，並寫出分母、期間與資料範圍。", ["只比較總量，不看分母", "用單日數值代表長期趨勢", "省略單位讓數字看起來一致"], "比例與密度的判讀不能只看總量，必須交代分母、期間及單位。", "先確認量的定義與單位，再計算比較。"),
            (f"先描述「{topic}」資料呈現的趨勢，再提出可能原因，最後用另一項資料檢查原因是否成立。", ["看見兩條線同升就宣稱必然因果", "只挑支持原先想法的年份", "刪除與預測不符的資料"], "資料描述、可能解釋與因果主張要分開，並用額外證據檢驗。", "先描述、再解釋、後檢驗，不把相關當因果。"),
        ]
    elif kind == "hist":
        variants = [
            (f"依「{topic}」史料的年代、作者與形成情境排序，再說明哪些先後關係有直接證據。", ["依文字長短排序", "依人物知名度排序", "先定結論再安排年代"], "時間線應依可核對的年代與來源建立，不能以篇幅或知名度代替證據。", "先辨識年代與來源，再建立時序。"),
            (f"比較「{topic}」的兩份史料時，先交代作者身分、寫作目的與可能立場，再對照相同與不同之處。", ["只以官方身分判定內容必然正確", "只看情緒強弱判斷真偽", "把後人解釋當成當時原文"], "史料的作者、目的與立場會影響記錄方式，必須和內容一起判讀。", "先做史料定位，再比較敘述與限制。"),
            (f"以「{topic}」的原始資料支持一項主張，並把資料直接說出的內容與自己的推論分開寫。", ["把推論改寫成史料原句", "只保留有利的句子", "省略資料年代以免干擾結論"], "史料內容與研究者推論是不同層次，分開標示才能檢驗論證。", "把證據、推論與限制分欄記錄。"),
            (f"若「{topic}」的新史料與原先說法矛盾，回查來源、年代與保存脈絡，再修正或限縮原主張。", ["堅持原結論不看反例", "只採用新資料中有利的一句", "把提出反例者視為錯誤"], "新證據應促使研究者重新檢查主張，而不是選擇性刪除反例。", "遇到矛盾先回查來源與推理，再修正主張。"),
        ]
    elif kind == "civ":
        variants = [
            (f"判斷「{topic}」的公共措施時，先確認法律依據、目的、受影響者與可申訴的程序。", ["只要多數人支持就能無限限制權利", "政策名稱合理即可不說明依據", "只公布支持意見而不提供救濟"], "權利與公共政策的判讀要同時處理法源、目的、比例與救濟。", "先找法源與程序，再檢查權利限制是否必要且可救濟。"),
            (f"分析「{topic}」的政策選擇時，列出不同群體的利益、成本與可能受損權益，再依公開判準比較。", ["只採納聲量最大者", "排除少數受影響者以加快決定", "先決定方案再找支持數字"], "公共決策不只看多數偏好，也要揭露取捨並納入受影響者。", "列出利害關係人與取捨，再以公開規則判斷。"),
            (f"把「{topic}」的資料分成事實、規範主張與價值判斷，並用可查證資料支持事實部分。", ["把個人感受直接寫成法律事實", "只看口號是否響亮", "把意見票數當成事實證明"], "公民題要區分可查證事實、規範判斷與個人意見，避免層次混淆。", "先分類敘述層次，再核對可查證證據。"),
            (f"若「{topic}」涉及權利衝突，說明各方權利、限制條件與比例取捨，而非只宣布哪一方喜歡的答案。", ["以單一權利名稱壓過所有限制", "把不同意見視為不必回應", "用情緒強弱取代原則與證據"], "權利衝突需要說明相互影響與限制理由，不能以單一口號取代分析。", "列出權利與限制，再檢查必要性、比例與程序。"),
        ]
    else:
        variants = [
            (f"針對「{topic}」先提出可觀察問題，限定對象、時間與資料範圍，再決定如何蒐證。", ["用『大家是不是都這樣』概括所有人", "只寫表達立場的口號", "問題越大越好而不界定範圍"], "可檢驗的問題必須有明確對象、範圍與可觀察指標。", "先把問題縮小成可觀察、可比較的形式。"),
            (f"閱讀「{topic}」的兩份資料時，核對來源、日期、範圍與定義，再說明證據能支持到哪裡。", ["刪除不符合原結論的資料", "只引用最方便的一筆", "把個人感受寫成普遍結論"], "可靠判讀需確認資料條件，並交代證據的推論界線。", "先做來源與範圍檢查，再區分證據與推論。"),
            (f"若「{topic}」資料出現差異，先提出可能原因，再用另一筆資料或反例檢驗，而不是直接選邊。", ["看到差異就選擇自己喜歡的版本", "把同時發生直接當成唯一原因", "忽略反例以維持原說法"], "差異是研究起點，必須提出可檢驗解釋並保留反例。", "提出假設後找反例與額外證據檢驗。"),
            (f"完成「{topic}」判斷後，用一句話連接條件、證據與結論，並寫出仍需查證的限制。", ["只寫最後答案不留依據", "把關鍵條件藏在附註", "用專有名詞取代推理"], "完整回答要讓讀者看見條件如何由證據導向結論，也要承認限制。", "用『因為條件／證據，所以結論；但限制是……』核對。"),
        ]
    # The first four tasks are subject-family-specific.  These six cross-family
    # tasks make the ten-question set genuinely varied even when a lesson has
    # ten questions, while still requiring the unit topic in every answer.
    variants.extend([
        (f"把「{topic}」的資料依來源、時間、範圍與可信度分層，先處理資料品質再提出結論。", ["只挑最符合預期的資料", "把不同來源混成一筆數字", "以資料量多寡取代來源檢查"], "證據品質會限制結論強度，不能先定結論再挑資料。", "先做來源與範圍的品質檢查，再決定能下多強的結論。"),
        (f"針對「{topic}」列出至少兩個可能解釋，為每個解釋指定可觀察的支持與反駁證據。", ["只提出一個不能檢驗的原因", "把可能原因當成已證明事實", "只找支持而不設計反駁條件"], "可檢驗的解釋必須同時說明支持與反駁條件。", "把原因寫成可被資料支持或反駁的假設。"),
        (f"將「{topic}」的條件、觀察與結論分成三欄，逐項檢查中間是否缺少推理。", ["把觀察直接當成結論", "只抄結論不保留觀察", "以熟悉的專有名詞代替推理"], "分層記錄可以看出證據是否真的支持結論，避免跳步。", "依序寫條件、觀察、結論，找出缺少的連接。"),
        (f"若不同群體對「{topic}」的資料解讀不同，先比較各自使用的定義與資料範圍，再討論分歧。", ["以聲音最大者的定義為準", "忽略定義差異只比較結論", "把不同意見直接視為錯誤"], "同一詞語或指標若定義不同，結論不能直接比較。", "先對齊定義與範圍，再判斷真正的資料差異。"),
        (f"把「{topic}」的判斷改寫成能由另一位同學重做的步驟，並標出每一步使用的證據。", ["只留下最後答案", "用『看起來合理』取代步驟", "省略不支持原結論的觀察"], "可重做的推理需要明示步驟與證據，才能被檢查。", "要求每一步都有對應資料或判準。"),
        (f"完成「{topic}」分析後，指出結論適用的範圍，以及資料不足時不能主張的部分。", ["把局部結果推廣到所有情況", "把資料不足當成沒有任何限制", "以肯定語氣掩蓋不確定性"], "好的資料判讀同時說明結論與適用界線，不能過度推論。", "最後補上適用範圍與仍待查證的限制。"),
    ])
    correct, wrong, explanation, strategy = variants[index % len(variants)]
    # Some framework nodes share a human-readable title.  Use a short excerpt
    # from the actual lesson summary so the correct option reflects that
    # lesson's evidence rather than only repeating the shared title.
    if anchor:
        correct = f"{correct}（本課資料焦點：{anchor}）"
    return correct, wrong, explanation, strategy


def rotate(values: list[str], correct_index: int) -> tuple[list[dict], str]:
    shift = correct_index % 4
    rotated = values[shift:] + values[:shift]
    answer = chr(65 + ((0 - shift) % 4))
    return [{"id": chr(65 + i), "text": value} for i, value in enumerate(rotated)], answer


def main() -> None:
    lessons = {}
    for p in (ROOT / "lessons").glob("*/*.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        lessons[data.get("id")] = data
    paths = sorted((ROOT / "questions" / "social").glob("*.json"))
    groups = defaultdict(list)
    cross_groups = defaultdict(list)
    data_by_path = {}
    for p in paths:
        data = json.loads(p.read_text(encoding="utf-8"))
        data_by_path[p] = data
        if data.get("reviewStatus") == "draft":
            key = (data.get("lessonId"), tuple(o.get("text", "") for o in data.get("options", [])))
            groups[key].append(p)
            cross_groups[tuple(o.get("text", "") for o in data.get("options", []))].append(p)
    targets = {p for members in groups.values() if len(members) >= 2 for p in members}
    targets.update(p for members in cross_groups.values() if len({data_by_path[x].get("lessonId") for x in members}) >= 2 for p in members)
    changed = []
    for p in paths:
        if p not in targets:
            continue
        data = data_by_path[p]
        lesson = lessons.get(data.get("lessonId"), {})
        topic = topic_of(lesson)
        kind = family(str(lesson.get("title", "")))
        match = re.search(r"-(\d+)\.json$", p.name)
        index = (int(match.group(1)) - 1) if match else 0
        summary = str(lesson.get("content", {}).get("summary", ""))
        anchor = re.sub(r"\s+", " ", summary).strip()[:38]
        correct, wrong, explanation, strategy = build_options(topic, kind, index, anchor)
        values = [correct, *wrong]
        options, answer = rotate(values, index)
        data["options"] = options
        data["answer"] = {"value": answer, "explanation": f"{explanation} 本題以「{topic}」為單元脈絡重新設計。"}
        data["solutionStrategy"] = strategy
        data["solutionSteps"] = [
            f"讀題定位：先找出題目要判斷的「{topic}」條件、資料與限制。",
            f"建立判準：{strategy}",
            f"核對正確選項 {answer}：{correct} 這個選項同時回應題幹條件與單元證據要求。",
            "逐項排除：其餘選項各自省略來源、尺度、程序、反例或推論限制，不能支持同樣可靠的結論。",
            "最後驗算：重新對照題幹的條件、正解選項與答案代號，確認沒有把單元名稱或選項位置當成證據。",
        ]
        data["reviewStatus"] = "draft"
        data["updatedAt"] = TODAY
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(str(p.relative_to(ROOT)))
    report = {
        "updatedAt": TODAY,
        "status": "pass" if changed else "no-op",
        "targetQuestions": len(targets),
        "changedQuestions": len(changed),
        "method": "social-unit-specific evidence tasks; stable IDs and public-exam pattern provenance preserved",
        "reviewStatus": "draft",
        "note": "This repair removes repeated option sets and rewrites reasoning fields; it does not promote subject correctness or human review.",
        "samplePaths": changed[:30],
    }
    out = ROOT / "implementation" / "reports" / "social-duplicate-option-repair-20260907.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

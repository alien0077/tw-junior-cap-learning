#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Ab-IV-4/5/6."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
COMMON_LICENSE = "只記錄公立學校課程計畫的教材版本、章節學習重點與評量方向，不複製教材正文、例題、題目、答案或版面。"

SAMPLES = [
    {
        "lessonId": "lesson-chinese-content-ab-iv-4",
        "title": "Ab-Ⅳ-4：6500常用語詞認念",
        "sources": [
            ("nani", "https://course.cyc.edu.tw/upfile/course109/sub1/14536054569425830.pdf", "嘉義縣永慶國中南一版第一冊課程計畫；Ab-Ⅳ-4 與常用語詞認念並列於學習內容，教學進度以語文常識、課文朗讀、詞語理解、學習單與紙筆／口頭活動支持正確認讀；核讀 2026-09-20。", ["常用語詞的正確認讀", "詞語在課文中的音義連結", "從詞語認念進入閱讀理解"], ["詞語卡與課文句子", "朗讀、聆聽與詞界標示", "詞義和語境對照"], ["課文朗讀", "口頭提問", "學習單", "紙筆練習"]),
            ("kanghsuan", "https://w3.qnm.kh.edu.tw/curriculum/111/plan/%E7%89%B9%E6%95%99%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%9C%8B%E6%96%871B.pdf", "高雄市公立國中資源班課程計畫；公開資料明列康軒版第二冊，安排重要詞彙形音義辨識與文本理解、提問及短文表達，並採紙筆、檔案與口語評量；核讀 2026-09-20。", ["重要詞彙的形音義認讀", "詞語放回文本辨識", "認讀結果支援口語和短文理解"], ["文本重要詞彙標記", "詞音與詞義配對", "閱讀理解提問"], ["紙筆評量", "檔案評量", "口語評量"]),
            ("hanlin", "https://course.cyc.edu.tw/upfile/course110/sub1/14826950037937810.pdf", "嘉義縣公立國中翰林版八上國文課程計畫；各課將常用語詞認念放入課文朗讀、課程討論、閱讀學習單與作品活動，要求由語詞讀音進入段落和表達；核讀 2026-09-20。", ["語詞認念與文本節奏", "詞語音義和段落意義的連結", "由朗讀、討論到表達"], ["課文朗讀與聆聽音檔", "詞語在段落中的位置", "學習單與口語表達"], ["課程討論", "閱讀學習單", "朗誦", "口語表達"]),
        ],
        "common": ["正確認讀常用語詞要保留詞界、讀音與句中義", "認念不是孤立背音，而要能回到課文或短文理解", "朗讀、口頭說明與書面活動都可檢查認讀是否真正成立"],
        "diff": ["南一較突出課文朗讀與詞語理解的連接", "康軒以重要詞彙形音義和多元評量支持文本理解", "翰林把認念放入朗讀、討論、學習單與作品表達的連續活動"],
    },
    {
        "lessonId": "lesson-chinese-content-ab-iv-5",
        "title": "Ab-Ⅳ-5：5000常用語詞使用",
        "sources": [
            ("nani", "https://course.cyc.edu.tw/upfile/course109/sub1/14536054569425830.pdf", "嘉義縣永慶國中南一版第一冊課程計畫；Ab-Ⅳ-5 列入常用語詞使用，與課文句意、閱讀策略、口語表達及段落寫作一起安排，評量包含學習單、作業和課堂表現；核讀 2026-09-20。", ["常用語詞在句子中的正確使用", "詞義、搭配與段落語意", "由閱讀理解轉成口語和書面表達"], ["詞語與句子搭配", "段落語意線索", "仿寫和短文輸出"], ["學習單", "作業", "口語表達", "段落寫作"]),
            ("kanghsuan", "https://www.se.curriculum.chc.edu.tw/years/110/plans/286/views/4-1-1.pdf", "彰化縣二林高中國中部公立課程計畫；公開資料呈現 Ab-Ⅳ-5 常用語詞使用，將詞語應用放在文本、句意和學習策略中，並以作業、口語、紙筆或學習紀錄檢核；核讀 2026-09-20。", ["語詞在不同語境中的使用", "詞性、語意與搭配限制", "詞語使用和表達任務"], ["句子填換與語意比較", "詞語搭配表", "生活情境與文本改寫"], ["作業評量", "口語表達", "紙筆／學習紀錄"]),
            ("hanlin", "https://course.cyc.edu.tw/upfile/course110/sub1/14826950037937810.pdf", "嘉義縣公立國中翰林版八上國文課程計畫；各課將常用語詞使用連結文句邏輯、寫作手法學習單、討論和主題創作，要求學生在新句中遷移詞義與搭配；核讀 2026-09-20。", ["詞語使用和文句邏輯", "搭配、語氣與段落主旨", "從課文詞語到創作遷移"], ["詞語搭配與句意", "閱讀學習單", "主題寫作與作品分享"], ["課程討論", "學習單", "主題寫作", "口頭與書面表達"]),
        ],
        "common": ["詞語使用必須同時檢查詞性、搭配、語境與語氣", "近義詞不能只以大概意思互換，需用句中證據排除不合者", "評量要讓學生在新句或新情境中實際使用並說明理由"],
        "diff": ["南一把詞語使用接到句意、閱讀策略與段落寫作", "康軒公立課程呈現語詞應用與學習策略、作業和口語紀錄的連接", "翰林較突出由課文學習單、討論到主題創作的遷移"],
    },
    {
        "lessonId": "lesson-chinese-content-ab-iv-6",
        "title": "Ab-Ⅳ-6：常用文言詞義語詞結構",
        "sources": [
            ("nani", "https://course.cyc.edu.tw/upfile/course109/sub1/14536054569425830.pdf", "嘉義縣永慶國中南一版第一冊課程計畫；Ab-Ⅳ-6 列入常用文言文詞義及語詞結構，結合文言課文、句法、閱讀理解與字典查證，安排口頭問答、學習單及紙筆練習；核讀 2026-09-20。", ["文言詞義需依上下文判斷", "雙字語詞的結構與詞性", "由詞義和句法進入篇章理解"], ["文言句與現代語譯對照", "偏正、動賓、主謂等結構標記", "字典義和語境義比較"], ["口頭問答", "學習單", "紙筆測驗", "文言文閱讀"]),
            ("kanghsuan", "https://w3.qnm.kh.edu.tw/curriculum/111/plan/%E7%89%B9%E6%95%99%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD/%E8%B3%87%E6%BA%90%E7%8F%AD-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%9C%8B%E6%96%871B.pdf", "高雄市公立國中資源班課程計畫；教材版本明列康軒版第二冊，從文言文本重要詞彙形音義、背景、文意和提問表達切入，採直接／交互／問題解決教學及紙筆、檔案、口語評量；核讀 2026-09-20。", ["文言詞彙的形音義", "詞義由文本脈絡和句法共同決定", "理解詞語後回答文本問題"], ["文言句分層標記", "詞義與背景資料對照", "提問、短文和口頭表達"], ["紙筆評量", "檔案評量", "口語評量", "文本提問"]),
            ("hanlin", "https://www.mtjh.tp.edu.tw/wp-content/uploads/doc/mtjh212/114_%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%28%E5%9C%8B%E6%96%87%E7%A7%91%29%E9%83%A8%E5%AE%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "臺北市民族實驗國中公立課程計畫；公開單元安排 Ab-Ⅳ-6 文言詞義及語詞結構，於論語等非韻文單元結合句子理解、提問、口語表達與學習單／作業評量；核讀 2026-09-20。", ["文言詞義和語詞結構", "古典語錄文本的句子理解", "詞義判斷支援觀點與口語表達"], ["文言句和語詞結構圖", "古今詞義對照", "學習單、提問與分組報告"], ["學習單", "口語表達", "作業評量", "分組報告"]),
        ],
        "common": ["文言詞義不能固定套字典第一義，需回到上下文、詞性與句法", "雙字語詞要標出核心成分及結構，再驗證現代語譯", "評量需同時檢查詞義、結構和篇章理解，而不是只背翻譯"],
        "diff": ["南一較強調字典查證、句法與文言閱讀連接", "康軒以重要詞彙形音義、文本背景與問題解決教學支持理解", "翰林把文言詞義放入論語等非韻文的提問、學習單和表達活動"],
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item.get("lessonId") for item in data["units"]}
    added = []
    for sample in SAMPLES:
        records = []
        for publisher, url, locator, concepts, representations, assessment in sample["sources"]:
            records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-20", "observedConcepts": concepts, "observedRepresentations": representations, "observedAssessment": assessment, "licenseBoundary": COMMON_LICENSE})
        record = {"lessonId": sample["lessonId"], "title": sample["title"], "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": sample["common"], "differencesToReview": sample["diff"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公立學校章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
        if record["lessonId"] not in existing:
            data["units"].append(record)
            added.append(record["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-20"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blocker_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blocker_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(r"Four hundred twelve unit samples", "Four hundred fifteen unit samples", reason)
    blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()

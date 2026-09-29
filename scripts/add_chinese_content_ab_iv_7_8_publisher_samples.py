#!/usr/bin/env python3
"""Record independent public-school publisher evidence for Chinese Ab-IV-7/8."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
COMMON_LICENSE = "只記錄公立學校課程計畫或公開教學資源的教材版本、章節學習重點與評量方向，不複製教材正文、碑帖圖像、例題、題目、答案或版面。"

SAMPLES = [
    {
        "lessonId": "lesson-chinese-content-ab-iv-7",
        "title": "Ab-Ⅳ-7：文言字詞虛字古今義變",
        "sources": [
            ("nani", "https://www.chjh.tyc.edu.tw/uploads/neilfilefolder/9file/file/124_1_5111%E5%9C%8B%E8%AA%9E%E6%96%87.pdf", "桃園市公立國中普通班國語文課程計畫；公開學習內容直接列出 Ab-Ⅳ-7，並將文言字句理解、篇章寓意、提問回饋與紙筆／口語評量放在同一教學脈絡；核讀 2026-09-20。", ["文言字詞要放回句子判讀", "虛字功能需由語氣與句法辨識", "古今義變要以文本證據而非現代直覺說明"], ["文言句與語譯對照", "虛字位置、停頓與語氣標記", "古義／今義例句並列比較"], ["紙筆測驗", "口語問答", "課本應用練習", "學習單"]),
            ("kanghsuan", "https://fsjh.chc.edu.tw/storage/074521/open_files/01%E6%95%99%E5%8B%99%E8%99%95/002%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/109%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E7%89%B9%E6%95%99%E8%AA%B2%E7%A8%8B/108%E4%B8%8B%E7%A6%8F%E8%88%88%E國中---%E5%88%86%E6%95%A3%E5%BC%8F%E8%B3%87%E6%BA%90%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%28%E6%99%AE%E6%95%99%E3%80%81%E7%89%B9%E9%9C%80%E3%80%81%E8%AA%BF%E6%95%B4%E8%A8%88%E7%95%AB%E3%80%81%E8%87%AA%E6%88%91%E6%AA%A2%E6%A0%B8%E8%A1%A8%29.pdf", "彰化縣福興國中公立資源班課程計畫；資料列明康軒版國文教材與 Ab-Ⅳ-7，並以課文動畫、學習單、問答、觀察及紙筆調整支持古今義與文言字句理解；核讀 2026-09-20。", ["文言字詞和古今義辨識", "文本理解需要簡化、重整與語境提示", "回答、觀察與紙筆可共同檢查理解"], ["課文動畫與句意提示", "古今詞義分類", "問答、學習單與情境化練習"], ["紙筆", "問答", "觀察", "檔案／學習單"]),
            ("hanlin", "https://www.curriculum.chc.edu.tw/storage/164/110/5-7-%E5%9C%8B%E8%AA%9E%E6%96%87.pdf/Go8bL8272DkbZSBkIKB7cjbselE8qpVsFtUIUjGh.pdf", "彰化縣公立國中翰林版七年級國文教學進度總表；在文言神話、寓言自學文本中安排 Ab-Ⅳ-7 字句義、故事主旨與成語來源，並以學習單、口語表達、圖畫創作、小組發表和專題報告評量；核讀 2026-09-20。", ["文言字句義和故事情節互相驗證", "虛字及古今義要服務於寓意理解", "語詞理解可轉化為成語、改寫或發表"], ["文言故事字句細讀", "成語典故與古今語義連結", "故事改寫、漫畫或口頭分享"], ["學習單", "口語表達", "圖畫創作", "小組發表／專題報告"]),
        ],
        "common": ["文言字詞、虛字與古今義必須以句中位置、語氣、詞性和上下文共同判斷", "現代常用義不能直接取代古文義，需用語譯或前後句證據核對", "評量應從辨識延伸到解釋篇章、口語回應或改寫，而非只背單字表"],
        "diff": ["南一校方課程偏重字句、虛字語氣和篇章意義的整合判讀", "康軒資源班資料突出提示、分層與多元評量對古今義理解的支援", "翰林把文言字句放入神話寓言的故事理解，再轉成成語、創作與發表"],
    },
    {
        "lessonId": "lesson-chinese-content-ab-iv-8",
        "title": "Ab-Ⅳ-8：各體書法名家碑帖認識欣賞",
        "sources": [
            ("nani", "https://fsjh.chc.edu.tw/storage/074521/open_files/01%E6%95%99%E5%8B%99%E8%99%95/002%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/110%E5%AD%B8%E5%B9%B4%E5%BA%A6%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E5%9C%8B%E6%96%87/%E5%9C%8B%E6%96%87%E4%B8%83%E5%B9%B4%E7%B4%9A.pdf", "彰化縣福興國中公立南一版國文課程計畫；課程內容列入 Ab-Ⅳ-8，將字體演變、書法欣賞、書寫活動與校外書法展資源連結，並以觀察、作品與表達檢核；核讀 2026-09-20。", ["不同書體要從結構、筆勢與時代線索辨識", "名家碑帖欣賞需以可觀察的形式證據描述", "欣賞可延伸臨寫、比較與個人作品說明"], ["篆隸楷行草的形體比較", "碑帖局部特徵觀察卡", "臨寫、作品註記與展覽觀察"], ["作品呈現", "口語表達", "觀察紀錄", "書法展／學習單"]),
            ("kanghsuan", "https://market.cloud.edu.tw/resources/web/1807317", "臺北市士林國中公立康軒版國語混成教學資源；頁面明列教材版本康軒版與 Ab-Ⅳ-8，並以字體演變、書法欣賞、簡報／數位素材和學生創作發表支援形式觀察；核讀 2026-09-20。", ["字體演變提供書體判讀的時間線", "書法欣賞要比較形式特徵而非只認名家", "數位觀察可銜接主動創作與作品發表"], ["字體演變時間線", "局部放大與筆畫方向觀察", "數位簡報、創作與說明"], ["作品創作", "發表", "課堂討論", "學習紀錄"]),
            ("hanlin", "https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/113%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E4%BC%8D%E3%80%81%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E5%AD%B8%E7%BF%92%E8%A8%88%E5%8A%83%28%E5%85%AB%E5%B9%B4%E7%B4%9A%29.pdf", "高雄市公立國中領域課程計畫；公開資料列出國文課程的書法／碑帖欣賞與作品學習活動，將筆畫、結構、臨寫和多元作品評量放在語文表達學習中；核讀 2026-09-20。", ["碑帖欣賞要連結筆畫、結構與整體章法", "臨摹是觀察後的轉化，不等同機械複製", "作品評量可同時看形式證據與作者說明"], ["碑帖局部與整幅章法對照", "臨摹前後差異標註", "作品分享與欣賞理由"], ["作品評量", "朗誦／口頭說明", "學習單", "課堂發表"]),
        ],
        "common": ["書體與碑帖判讀要以筆畫、結構、欄式／章法及可見風格證據說明", "名家與年代只是線索，不能代替對作品本身的觀察", "學習成果應包含比較、欣賞理由、臨寫或創作後的反思說明"],
        "diff": ["南一校方課程較突出字體演變、展覽觀察與書寫作品的連接", "康軒公開資源以數位放大、演變時間線與主動創作支援欣賞", "翰林課程較強調碑帖局部到整幅章法、臨寫轉化和作品說明"],
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item.get("lessonId") for item in data["units"]}
    added = []
    for sample in SAMPLES:
        records = []
        for publisher, url, locator, concepts, representations, assessment in sample["sources"]:
            records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-or-public-teaching-resource-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-20", "observedConcepts": concepts, "observedRepresentations": representations, "observedAssessment": assessment, "licenseBoundary": COMMON_LICENSE})
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
            blocker["reason"] = re.sub(r"Four hundred fifteen unit samples", "Four hundred seventeen unit samples", reason)
    blocker_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()

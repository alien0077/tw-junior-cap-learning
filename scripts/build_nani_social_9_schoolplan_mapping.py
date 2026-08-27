import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://course.cyc.edu.tw/upfile/course113/sub1/15652604549479625.pdf"
volumes = [
    ("5", "9", "上", {
        "geography": ["漠南非洲的自然環境和文化發展", "漠南非洲的經濟發展", "歐洲與俄羅斯的自然環境與區域特色", "歐洲與俄羅斯的經濟發展與區域結盟", "北美洲的區域特色與經濟發展", "中南美洲的區域特色與經濟發展"],
        "history": ["西亞與非洲的古文明", "希臘與羅馬的古文明", "普世宗教的起源與發展", "近代歐洲的興起", "多元世界的互動", "革命的時代"],
        "civics": ["選擇與消費", "價格與資源分配", "廠商競爭下的市場", "交易與專業分工", "貨幣發展與匯率", "科技發展下的支付工具"],
    }),
    ("6", "9", "下", {
        "geography": ["地名怎麼來？", "聚落的命名與商品行銷", "從產地到餐桌", "食品安全面面觀"],
        "history": ["現代國家的建立", "帝國主義與第一次世界大戰", "戰間期與第二次世界大戰", "冷戰與今日世界"],
        "civics": ["全球化的影響", "國際社會的參與", "智慧財產的保障與運用", "現代公民與媒體識讀"],
    }),
]
roots = {"geography": "kg-social-content-geography", "history": "kg-social-content-history", "civics": "kg-social-content-civics"}
out_volumes = []
total = 0
for volume, grade, semester, groups in volumes:
    entries = []
    for area, labels in groups.items():
        for i, label in enumerate(labels, 1):
            entries.append({"chapterCode": f"{volume}-{area[:3]}-{i}", "chapterLabel": label, "knowledgeIds": [roots[area]], "relation": "primary", "confidence": "medium", "notes": "民和國中 113 學年度公開課程計畫由南一出版社設計，明列南一版九年級社會單元；KG 先掛社會分科根節點，逐碼對照待核驗。"})
    total += len(entries)
    out_volumes.append({"volume": volume, "grade": grade, "semester": semester, "entries": entries})
out = {"id": "mapset-social-nani-schoolplan-9-2026", "subject": "social", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": url, "locator": "嘉義縣民和國民中學 113 學年度九年級第一、二學期社會領域地理歷史公民教學計畫表；文件標示設計者為南一出版社，列出第 5、6 冊單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫為 113 學年度；雖標示南一出版社設計，仍不等同 115 年出版社正式目次。"}, "mappingMethod": "school-plan-unit-index-to-official-social-kg-conservative-cross-reference", "volumes": out_volumes, "status": "verified", "notes": f"保存 {total} 筆九年級單元 metadata；逐章課綱代碼仍待核驗。"}
(ROOT / "textbook-mapping/social/nani-schoolplan-9-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote", total, "entries")

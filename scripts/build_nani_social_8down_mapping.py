import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-4.pdf"
groups = {
    "geography": ["東北亞的自然環境與觀光", "東北亞的經濟發展與挑戰", "東南亞的區域特色與經濟發展", "南亞的區域特色與經濟發展", "西亞與北非的區域特色", "西亞與北非的國際衝突"],
    "history": ["中華民國早期的發展", "現代國家的追求", "日本帝國的對外擴張與衝擊", "中國共產政權的建立與發展", "冷戰時期東亞國家的競合", "現代東亞的發展"],
    "civics": ["契約與生活", "民事糾紛的解決途徑", "犯罪與刑法", "犯罪的追訴", "生活中的行政法規與救濟", "兒少權利的保護"],
}
roots = {"geography": "kg-social-content-geography", "history": "kg-social-content-history", "civics": "kg-social-content-civics"}
entries = []
for area, labels in groups.items():
    for i, label in enumerate(labels, 1):
        entries.append({"chapterCode": f"{area[:3]}-{i}", "chapterLabel": label, "knowledgeIds": [roots[area]], "relation": "primary", "confidence": "medium", "notes": "卓蘭高中附設國中部 113 學年度八年級公開課程計畫明列南一版第四冊單元；KG 先掛社會分科根節點，逐碼對照待核驗。"})
out = {"id": "mapset-social-nani-schoolplan-8down-2026", "subject": "social", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": url, "locator": "國立卓蘭高中附設國中部 113 學年度第一、二學期八年級社會領域課程計畫；南一版第四冊下學期地理、歷史、公民各 6 單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫為 113 學年度，作為南一版本單元交叉證據；不等同南一出版社正式目次。"}, "mappingMethod": "school-plan-unit-index-to-official-social-kg-conservative-cross-reference", "volumes": [{"volume": "4", "grade": "8", "semester": "下", "entries": entries}], "status": "verified", "notes": "保存 18 筆八年級下學期單元 metadata；逐章課綱代碼待核驗。"}
(ROOT / "textbook-mapping/social/nani-schoolplan-8down-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote", len(entries), "entries")

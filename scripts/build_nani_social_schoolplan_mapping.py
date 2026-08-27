import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.yfms.tyc.edu.tw/uploads/1632969569628TUZJ6ptO.pdf"
groups = {
    "geography": ["臺灣的人口成長與分布", "臺灣的人口組成與多元文化", "臺灣的農業", "臺灣的工業與國際貿易", "聚落與交通", "區域發展與空間差異"],
    "history": ["日治時期的統治方針", "日治時期的殖民統治與現代化", "日治時期的社會與文化", "戰後臺灣的政治發展", "戰後臺灣的外交與兩岸關係", "戰後臺灣的經濟與社會文化"],
    "civics": ["公民與公民德性", "志願團體", "勞動參與", "多元文化與社會", "社會規範", "公平正義與社會安全"],
}
roots = {"geography": "kg-social-content-geography", "history": "kg-social-content-history", "civics": "kg-social-content-civics"}
entries = []
for area, labels in groups.items():
    for i, label in enumerate(labels, 1):
        entries.append({"chapterCode": f"{area[:3]}-{i}", "chapterLabel": label, "knowledgeIds": [roots[area]], "relation": "primary", "confidence": "medium", "notes": "永豐高中國中部 109 學年度公開教科書改選報告列為南一版國中社會(一下)單元；KG 先掛社會分科根節點，逐碼對照待核驗。"})
out = {"id": "mapset-social-nani-schoolplan-2026", "subject": "social", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": url, "locator": "桃園市立永豐高中國中部 109 學年度教科書改選報告；南一版國中社會(一下)地理、歷史、公民各 6 單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開報告為 109 學年度，作為南一版本單元交叉證據；不等同南一出版社正式目次。"}, "mappingMethod": "school-plan-unit-index-to-official-social-kg-conservative-cross-reference", "volumes": [{"volume": "2", "grade": "7", "semester": "下", "entries": entries}], "status": "verified", "notes": "保存 18 筆單元 metadata（地理、歷史、公民各 6）；南一其他冊別仍待公開可核驗單元來源。"}
(ROOT / "textbook-mapping/social/nani-schoolplan-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote", len(entries), "entries")

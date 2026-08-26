import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/111-2-8-4.pdf"
groups = {
    "geography": ["中國的人口分布與自然環境", "中國的人口成長與遷移", "中國的產業轉型與區域差異", "全球化下的中國", "大洋洲與兩極地區（一）", "大洋洲與兩極地區（二）"],
    "history": ["商周至隋唐時期的國家與社會", "商周至隋唐時期的民族與文化", "宋元時期的國際互動與交流", "明清時期東亞世界的變動與交流", "晚清的外力衝擊與政治變革", "晚清的城市新風貌與新文化"],
    "civics": ["人民與國家", "法治的基本概念", "我國的政府", "依法行政的政府", "刑法與犯罪", "犯罪與追訴"],
}
roots = {"geography": "kg-social-content-geography", "history": "kg-social-content-history", "civics": "kg-social-content-civics"}
entries = []
for area, labels in groups.items():
    for i, label in enumerate(labels, 1):
        entries.append({"chapterCode": f"{area[:3]}-{i}", "chapterLabel": label, "knowledgeIds": [roots[area]], "relation": "primary", "confidence": "medium", "notes": "卓蘭高中附設國中部 111 學年度第一學期八年級公開課程計畫明列南一版教科書單元；KG 先掛社會分科根節點，逐碼對照待核驗。"})
out = {"id": "mapset-social-nani-schoolplan-8-2026", "subject": "social", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": url, "locator": "國立卓蘭高中附設國中部 111 學年度第一學期八年級社會領域課程計畫；南一版八年級上學期地理、歷史、公民各 6 單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫為 111 學年度，作為南一版本單元交叉證據；不等同南一出版社正式目次。"}, "mappingMethod": "school-plan-unit-index-to-official-social-kg-conservative-cross-reference", "volumes": [{"volume": "3", "grade": "8", "semester": "上", "entries": entries}], "status": "verified", "notes": "保存 18 筆八年級上學期單元 metadata（地理、歷史、公民各 6）；南一其他冊別仍待公開可核驗單元來源。"}
(ROOT / "textbook-mapping/social/nani-schoolplan-8-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote", len(entries), "entries")

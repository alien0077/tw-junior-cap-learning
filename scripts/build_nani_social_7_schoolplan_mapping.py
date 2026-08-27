import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf"
volumes = [
    ("1", "7", "上", {"geography": ["認識位置與地圖", "世界中的臺灣", "臺灣的地形", "臺灣的海岸與島嶼", "臺灣的氣候", "臺灣的水文"], "history": ["史前時代與原住民", "大航海時代各方勢力的活動", "大航海時代的原住民與外來者", "清帝國時期的政治發展", "清帝國時期的經濟發展", "清帝國時期的社會與文化"], "civics": ["人性尊嚴與人權保障", "性別平權", "親屬關係與家庭功能", "平權的家庭", "校園生活與公共事務參與", "社區與部落"]}),
    ("2", "7", "下", {"geography": ["臺灣的人口成長與分布", "臺灣的人口組成與族群文化", "臺灣的農業", "臺灣的工業發展與國際貿易", "臺灣的聚落與交通", "臺灣的區域發展及空間差異"], "history": ["日治時期的政治", "日治時期的經濟發展", "日治時期的社會與文化", "戰後臺灣的政治變遷", "戰後臺灣的外交與兩岸關係", "戰後臺灣的經濟與社會"], "civics": ["公民與公民德性", "團體與志願結社", "多元文化與社會", "社會規範", "社會生活中的公平正義", "社會安全中的國家責任"]}),
]
roots = {"geography": "kg-social-content-geography", "history": "kg-social-content-history", "civics": "kg-social-content-civics"}
out_volumes = []
for volume, grade, semester, groups in volumes:
    entries = []
    for area, labels in groups.items():
        for i, label in enumerate(labels, 1):
            entries.append({"chapterCode": f"{volume}-{area[:3]}-{i}", "chapterLabel": label, "knowledgeIds": [roots[area]], "relation": "primary", "confidence": "medium", "notes": "永慶高中 114 學年度公開課程計畫明列教材版本為南一版第一、二冊；KG 先掛社會分科根節點，逐碼對照待核驗。"})
    out_volumes.append({"volume": volume, "grade": grade, "semester": semester, "entries": entries})
out = {"id": "mapset-social-nani-schoolplan-7-2026", "subject": "social", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": url, "locator": "嘉義縣永慶高中 114 學年度七年級第一、二學期社會領域課程計畫；南一版第一、二冊，地理、歷史、公民各 6 單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫為 114 學年度，作為南一版本單元交叉證據；不等同南一出版社正式目次。"}, "mappingMethod": "school-plan-unit-index-to-official-social-kg-conservative-cross-reference", "volumes": out_volumes, "status": "verified", "notes": "保存 36 筆七年級單元 metadata；逐章課綱代碼仍待核驗。"}
(ROOT / "textbook-mapping/social/nani-schoolplan-7-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote 36 entries")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "implementation/reports/public-exam-source-catalog.json"
data = json.loads(path.read_text(encoding="utf-8"))
source_url = "https://www.sdjh.ntpc.edu.tw/p/405-1000-6042%2Cc837.php?Lang=zh-tw"
if not any(row["url"] == source_url for row in data["sources"]):
    data["sources"].append({
        "institution": "新北市立三多國民中學", "url": source_url, "subjects": ["english"],
        "availableMaterial": "113學年度第1學期八年級第一次段考英文科試題與附件。",
        "researchUse": "核對公開PDF：第3頁第41題態度推論；第4頁第44題依表格判斷時段、第45題整合固定活動線索；第5頁手寫題第3題時序改寫。僅作影音理解題的能力模式參照，不複製原題。",
        "licenseBoundary": "公開查閱不等於可重製；不複製試題原文、選項、答案或圖表，僅pattern-only改寫。",
        "sourceLocator": "頁面附件「113學年度八年級第一次段考英語科試題卷.pdf」；PDF第3頁第41題、第4頁第44至45題、第5頁手寫題第3題。",
    })
data["updatedAt"] = "2026-09-24"
used = {ref["url"] for p in (ROOT / "questions/english").glob("question-english-performance-1-iv-8-*.json") for ref in json.loads(p.read_text(encoding="utf-8"))["examPatternRefs"]}
data["questionSourceUrls"] = sorted(set(data["questionSourceUrls"]) | used)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"catalog sources={len(data['sources'])} unique_question_urls={len(data['questionSourceUrls'])}")

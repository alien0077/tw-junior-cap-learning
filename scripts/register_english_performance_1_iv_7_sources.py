import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "implementation/reports/public-exam-source-catalog.json"
data = json.loads(path.read_text(encoding="utf-8"))
url = "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=432&cfsn=2875&fn=113-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile"

if not any(source["url"] == url for source in data["sources"]):
    data["sources"].append({
        "institution": "花蓮縣立宜昌國民中學", "url": url, "subjects": ["english"],
        "availableMaterial": "113學年度第一學期九年級第一次段考英文試題與答案；公開PDF共6頁，另附答案頁。",
        "researchUse": "閱讀題組PDF第3頁第27、30、31題（用途、主旨、明示事實），第4頁第36、37題（原因及圖表比較）；逐題依公開原卷文本定位，僅作pattern-only改寫。",
        "licenseBoundary": "公開查閱不等於可重製；不複製原卷文章、題幹、選項、答案、圖表或情境，只吸收閱讀能力與題型結構。",
        "sourceLocator": "PDF第3頁第27、30、31題；第4頁第36、37題；答案見原卷末頁答案區。",
    })

for source in data["sources"]:
    if source["url"] == "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf":
        source["researchUse"] = "閱讀題組PDF第3至4頁第33題主旨、第34題後續推論、第35題代名詞指涉與第36題文章主題；另有既錄聽力問答定位。只用閱讀能力結構作pattern-only改寫。"
        source["sourceLocator"] = "PDF第3至4頁第33至36題；閱讀主旨、事件推論、指涉及說明文主題；另含PDF第2頁第10題聽力基本問答。"

data["updatedAt"] = "2026-09-24"
used_urls = {ref["url"] for question_path in (ROOT / "questions/english").glob("question-english-performance-1-iv-7-*.json") for ref in json.loads(question_path.read_text(encoding="utf-8"))["examPatternRefs"]}
data["questionSourceUrls"] = sorted(set(data["questionSourceUrls"]) | used_urls)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"catalog sources={len(data['sources'])} unique_question_urls={len(data['questionSourceUrls'])}")

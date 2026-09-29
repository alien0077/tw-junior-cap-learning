"""Register every already-used public pattern URL in the source catalog.

This is a provenance index repair only.  It does not import exam text or
answers; question-level pattern notes remain the authoritative rewrite record.
"""
import json
from datetime import date
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
catalog_path = ROOT / "implementation/reports/public-exam-source-catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
known = {row.get("url") for row in catalog.get("sources", [])}
refs = defaultdict(lambda: {"subjects": set(), "titles": set(), "locators": set()})
for path in sorted((ROOT / "questions").rglob("*.json")):
    item = json.loads(path.read_text(encoding="utf-8"))
    for ref in item.get("examPatternRefs", []):
        url = ref.get("url")
        if not url or url in known:
            continue
        refs[url]["subjects"].add(item.get("subject", "unknown"))
        refs[url]["titles"].add(ref.get("title", "公開學校試題型來源"))
        refs[url]["locators"].add(ref.get("locator", "paper-level locator"))

new_sources = []
for url, info in sorted(refs.items()):
    title = sorted(info["titles"])[0]
    host = urlparse(url).hostname or "公開學校來源"
    institution = (
        "國中教育會考（公辦公開試題）"
        if "國中教育會考" in title
        else title.split("公開")[0].strip() or host
    )
    new_sources.append({
        "institution": institution,
        "url": url,
        "subjects": sorted(info["subjects"]),
        "availableMaterial": title,
        "researchUse": "公開題型、資料型態與推理層次的 pattern-only 來源；題幹、選項、圖片與答案不複製。",
        "licenseBoundary": "公開查閱不等於可重製；保留 URL 與紙本／頁級定位，內容由本專案重新撰寫。",
        "sourceLocator": sorted(info["locators"])[0],
    })
catalog["sources"].extend(new_sources)
catalog["updatedAt"] = date.today().isoformat()
catalog["questionSourceUrls"] = sorted({row.get("url") for row in catalog.get("sources", []) if row.get("url")})
catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
report = {"status": "pass", "newCatalogEntries": len(new_sources), "catalogEntries": len(catalog["sources"]), "rule": "index existing public pattern URLs only; no exam text or answers copied"}
(ROOT / "implementation/reports/public-exam-source-catalog-repair.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))

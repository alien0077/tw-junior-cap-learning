#!/usr/bin/env python3
"""Extract official curriculum code/page evidence from downloaded PDFs."""
import json, re
from pathlib import Path
from pypdf import PdfReader
try:
    import fitz  # PyMuPDF fallback for PDFs with slow/poor pypdf extraction
except ImportError:
    fitz = None

ROOT = Path(__file__).resolve().parents[1]
pdfs = {
    "chinese": ("https://stv.naer.edu.tw/data/course_outline/pta_18510_4703638_59125.pdf", Path("/private/tmp/m4-pdfs/chinese.pdf")),
    "english": ("https://stv.naer.edu.tw/data/course_outline/pta_18518_3555074_59836.pdf", Path("/private/tmp/m4-pdfs/english.pdf")),
    "social": ("https://stv.naer.edu.tw/data/course_outline/pta_18535_6408773_60398.pdf", Path("/private/tmp/m4-pdfs/social.pdf")),
    "science": ("https://stv.naer.edu.tw/data/course_outline/pta_18538_240851_60502.pdf", Path("/private/tmp/m4-pdfs/science.pdf")),
    "math": ("https://stv.naer.edu.tw/data/course_outline/%E6%95%B8%E5%AD%B8%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E6%89%8B%E5%86%8A%EF%BC%88113%E5%B9%B43%E6%9C%88%E6%9B%B4%E6%96%B0%E7%89%88%EF%BC%89_0326.pdf", Path("/private/tmp/m4-pdfs/math.pdf")),
}
pattern = re.compile(r"\b[A-Z]{1,2}-Ⅳ-\d+\b")
out = {"generatedAt": "2026-08-27", "method": "pypdf-text-extraction", "subjects": {}}
for subject, (url, path) in pdfs.items():
    if not path.exists():
        out["subjects"][subject] = {"sourceUrl": url, "status": "download-pending"}
        continue
    reader = PdfReader(str(path))
    matches = {}
    for page_no, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        for code in sorted(set(pattern.findall(text))):
            matches.setdefault(code, []).append(page_no)
    out["subjects"][subject] = {"sourceUrl": url, "pageCount": len(reader.pages), "codeCount": len(matches), "codes": matches}
(ROOT / "data/m4-official-code-index-summary.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: {"pages": v.get("pageCount", 0), "codes": v.get("codeCount", 0), "status": v.get("status", "ready")} for k,v in out["subjects"].items()}, ensure_ascii=False))

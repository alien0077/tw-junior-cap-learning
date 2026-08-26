import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
src_math = "https://course.cyc.edu.tw/course/pub/cou_down.php?fn=162242714270391276285h4g84z7jymt3dbsqp59w6ttv5eszg466x6xz6.pdf&q_year=115"
src_science = "https://course.cyc.edu.tw/course/pub/cou_down.php?fn=1622427011662883296spsgx99mvemp965fk6ttatcjwb78ke77p298ewc.pdf&q_year=115"

def write_mapset(path, ident, subject, source, volumes, root, note):
    vs = []
    for volume, grade, semester, labels in volumes:
        vs.append({"volume": volume, "grade": grade, "semester": semester, "entries": [{"chapterCode": f"{volume}-{i}", "chapterLabel": label, "knowledgeIds": [root], "relation": "primary", "confidence": "medium", "notes": note} for i, label in enumerate(labels, 1)]})
    out = {"id": ident, "subject": subject, "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": source, "locator": "嘉義縣大吉國中 115 學年度公開課程計畫，列明南一版冊次與章節／單元", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫可核驗冊次與章節；不等同出版社正式目次。"}, "mappingMethod": "school-plan-chapter-index-to-official-kg-conservative-cross-reference", "volumes": vs, "status": "verified", "notes": note}
    (ROOT / path).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")

write_mapset("textbook-mapping/math/nani-schoolplan-9-2026.json", "mapset-math-nani-schoolplan-9-2026", "math", src_math, [("5", "9", "上", ["比例線段與相似形", "圓的性質", "推理證明與三角形的心"]), ("6", "9", "下", ["二次函數", "統計與機率", "立體幾何圖形"])], "kg-math-learning-content", "保存 6 筆南一版九年級數學章節 metadata；逐章課綱代碼待核驗。")
write_mapset("textbook-mapping/science/nani-schoolplan-7-2026.json", "mapset-science-nani-schoolplan-7-2026", "science", src_science, [("1", "7", "上", ["生命的發現", "生物體的營養", "生物體內的運輸", "生物體的協調作用", "生物體內的恆定"]), ("2", "7", "下", ["新生命的誕生", "遺傳", "形形色色的生物", "生物與環境的交互作用", "生物多樣性與生態保育"])], "kg-science-learning-content", "保存 10 筆南一版七年級自然科學章節 metadata；逐章課綱代碼待核驗。")
print("wrote math 6 and science 10 entries")

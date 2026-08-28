import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sources = {
    "8": "https://course.cyc.edu.tw/course/pub/cou_down.php?fn=162242707900549718653n48ev87u5tctgzxyc9ymmc5ix9rfjk2mxaspg.pdf&q_year=115",
    "9": "https://course.cyc.edu.tw/course/pub/cou_down.php?fn=1622427075369416915bm29gruv5y3dm73c7b767z6e2hzmn7ym92u77vu.pdf&q_year=115",
}
lessons = {
    "8": {
        "3": ["We Visited Our Relative Yesterday", "I Read a Special Book Last Week", "All Animals Were Going to the Party", "I Want to Take a Working Holiday", "Spending Time in Taiwan Is a Wonderful Experience", "The Power Of AI Will Shape The Future"],
        "4": ["Your House Is Bigger, But I Like Mine", "The Dish Is the Most Delicious of All", "I Want to Live More", "A Friend Bought Some Fruit for Us", "Some of the Most Useful Ideas Come from Nature", "People Believe That the Kingdom Will Fall If the Ravens Leave"],
    },
    "9": {
        "5": ["Have You Ever Been To A Concert?", "Fun Runs Are Held All Around the World", "The News Is Interesting, But Is It True?", "Taiwan’s Baseball Team Shows How Hard Work Pays Off", "Do You Know Any Animals That Are Color-blind?", "The Students Here Are Different from the Ones I Know in the US"],
        "6": ["A Firefighter’s Job Means A Lot to us, Doesn’t It?", "Taiwanese Products Are Too Good to Miss", "People Around the World Have Been Amazed by Moai", "I Will Remember Everything We Did Together"],
    },
}
for grade, vols in lessons.items():
    entries = []
    for volume, labels in vols.items():
        for i, label in enumerate(labels, 1):
            entries.append({"chapterCode": f"{volume}-lesson-{i}", "chapterLabel": f"Lesson {i}: {label}", "knowledgeIds": ["kg-english-learning-content"], "relation": "primary", "confidence": "medium", "notes": "嘉義縣大吉國中 115 學年度公開課程計畫明列南一版英文冊次與 Lesson 標題；KG 先掛英文內容根節點，逐碼對照待核驗。"})
    book_nums = sorted(vols)
    out = {"id": f"mapset-english-nani-schoolplan-{grade}-2026", "subject": "english", "publisher": "nani", "academicYear": "115", "source": {"type": "book-inspection", "url": sources[grade], "locator": f"嘉義縣大吉國中 115 學年度英文科課程計畫，南一版第 {book_nums[0]}、{book_nums[1]} 冊逐課 Lesson 標題", "verifiedAt": "2026-08-26", "verifiedBy": "Codex public school-plan verification", "confidence": "medium", "editionNote": "校方公開課程計畫可核驗冊次與逐課標題；不等同南一出版社正式目次，部分 PDF 文字擷取標題保留原始不完整字串。"}, "mappingMethod": "school-plan-lesson-index-to-official-english-kg-conservative-cross-reference", "volumes": [{"volume": volume, "grade": grade, "semester": "上" if volume == book_nums[0] else "下", "entries": [{**e, "chapterCode": f"{volume}-{e['chapterCode'].split('-',1)[1]}"} for e in entries if e["chapterCode"].startswith(volume + "-")]} for volume in vols], "status": "verified", "notes": f"保存 {len(entries)} 筆逐課 Lesson metadata；逐章課綱代碼仍待核驗。"}
    (ROOT / f"textbook-mapping/english/nani-schoolplan-{grade}-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(grade, len(entries))

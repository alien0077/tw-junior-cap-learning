#!/usr/bin/env python3
"""Replace the Europe/Russia environment template set."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-geo-bh-iv-1"
KID = "kg-social-content-geo-bh-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/819/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F.pdf"

rows = [
    ("西歐沿海冬季較內陸溫和，若比較同緯度地區，最值得優先考慮哪項因素？", ["海洋調節與暖流影響", "城市人口數一定較少", "地名的文字長度", "所有地區的日照完全相同"], "A", "海洋具有調節作用，西歐沿海也可能受到北大西洋暖流與盛行風影響；判讀仍須配合資料。"),
    ("地中海型氣候常見的降水與溫度特徵為何？", ["夏季較乾燥、冬季較多雨", "全年高溫多雨且沒有乾季", "全年寒冷且降水都為降雪", "夏季降水最多、冬季完全無雨"], "A", "地中海型氣候通常夏季炎熱乾燥、冬季溫和多雨，適合部分耐旱作物。"),
    ("若地圖顯示阿爾卑斯山區地勢高、聚落較少，最合理的解釋為何？", ["高山地形增加交通與耕作限制", "高山地區必然沒有任何水源", "地勢高會使所有居民無法工作", "聚落分布只由國界決定"], "A", "高山地形會增加交通與農業開發難度，但也可能提供水源、觀光等其他利用條件。"),
    ("伏爾加河向南流入裡海，若要分析沿岸聚落分布，最應考量什麼？", ["河流提供交通、用水與農業等條件", "河流會使沿岸氣候全部相同", "只要靠近河流就一定成為首都", "河流方向能直接決定居民語言"], "A", "河流可能提供交通、生活用水與農業條件，但聚落形成仍受到地形、歷史與經濟等因素影響。"),
    ("俄羅斯北部高緯度地區常有嚴寒與凍土現象，對農業最可能造成什麼限制？", ["生長季較短，部分地區耕作條件較差", "全年都能種植相同作物", "凍土會使所有河流消失", "高緯度必然沒有任何植物"], "A", "高緯度低溫與凍土會縮短生長季、限制根系與耕作，但不同地區仍有環境差異。"),
    ("歐洲河網密集且海岸線曲折，歷史上可能有利於哪項活動？", ["區域間交通、港口貿易與人口往來", "使所有地區的產業完全相同", "讓內陸地區不需要道路", "消除各地自然環境差異"], "A", "河流與海岸可提供水運及港口條件，有利於交通、貿易與人口交流，但不能消除地區差異。"),
    ("若一張氣候圖顯示某地冬季降水明顯多於夏季，且夏季溫暖乾燥，該地最可能屬於哪種氣候？", ["地中海型氣候", "極地氣候", "全年濕熱的熱帶雨林氣候", "全年乾燥無明顯季節差異的氣候"], "A", "冬雨夏乾是判讀地中海型氣候的重要線索，仍可再用溫度資料確認。"),
    ("比較歐洲西部與俄羅斯內陸的冬季氣溫時，俄羅斯內陸通常較寒冷，最合理的原因為何？", ["距海較遠，大陸性較強且高緯度範圍廣", "俄羅斯內陸一定位於赤道附近", "歐洲西部沒有任何冬季", "氣溫只由國家面積決定"], "A", "距海遠會減弱海洋調節，大陸性較強；俄羅斯也有廣大的高緯度地區，需綜合位置分析。"),
    ("若規劃歐洲山區觀光道路，哪項自然環境資料最需要先調查？", ["坡度、地質、降雪與可能的災害風險", "景點名稱的字數", "只看夏季一天的氣溫", "只比較道路標誌的顏色"], "A", "山區道路需考量坡度、地質、積雪與災害等條件，才能評估安全與工程限制。"),
    ("閱讀歐洲與俄羅斯自然環境地圖時，哪種方法最能避免過度推論？", ["同時比較位置、地形、氣候與水文資料，再提出有條件的結論", "只看一種顏色就判定所有環境特徵", "把一個城市的氣候套用到整個區域", "忽略圖例與比例尺"], "A", "地理判讀要結合圖例、比例尺與多項自然資料，並限制結論的適用範圍。"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, _answer, explanation) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-geo-bh-iv-1-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    rotated = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(rotated)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；歐洲與俄羅斯自然環境背景及地圖判讀能力方向之獨立改編；官方答案表：{ANSWER}；課綱定位：{CURRICULUM}；非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Europe/Russia environment questions")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 115 年翰林公開教材樣書目次可核驗章名；KG 先保守掛至社會三大領域穩定節點，
# 待取得逐章課綱代碼時再細化，避免把出版社章名誤當成課綱節點。
volumes = {
    ("1", "7", "上"): [("地理", "認識位置與地圖"), ("地理", "世界中的臺灣"), ("地理", "地形"), ("地理", "海岸與島嶼"), ("地理", "天氣與氣候"), ("地理", "水文"), ("歷史", "史前臺灣與原住民文化"), ("歷史", "大航海時代各方勢力的競逐"), ("歷史", "大航海時代臺灣原住民與外來者"), ("歷史", "清帝國統治政策的變遷"), ("歷史", "清帝國時期農商業的發展"), ("歷史", "清帝國時期社會文化的變遷")],
    ("2", "7", "下"): [("地理", "人口成長與分布"), ("地理", "人口組成與族群文化"), ("地理", "農業"), ("地理", "工業與國際貿易"), ("地理", "聚落體系與都市發展"), ("地理", "區域發展與差異"), ("歷史", "日治時期的政治"), ("歷史", "日治時期的經濟"), ("歷史", "日治時期的社會與文化"), ("歷史", "戰後臺灣的政治"), ("歷史", "戰後臺灣的外交"), ("歷史", "戰後臺灣的經濟與社會")],
    ("3", "8", "上"): [("地理", "中國的自然環境"), ("地理", "中國的人口"), ("地理", "中國的產業活動與轉型"), ("地理", "中國的經濟發展與全球關聯"), ("地理", "東北亞的自然環境與文化"), ("地理", "東北亞的經濟發展與挑戰"), ("歷史", "商周至隋唐時期的國家與社會"), ("歷史", "商周至隋唐時期的民族與文化"), ("歷史", "宋元多民族並立的時期"), ("歷史", "明清時期東亞世界的變動"), ("歷史", "西力衝擊下的東亞世界"), ("歷史", "晚清社會文化的調適與變遷")],
    ("4", "8", "下"): [("地理", "東南亞"), ("地理", "南亞"), ("地理", "西亞與北非的自然環境與文化"), ("地理", "西亞與北非的衝突與轉變"), ("地理", "漠南非洲的自然環境與文化"), ("地理", "漠南非洲的產業與經濟發展"), ("歷史", "中華民國的建立"), ("歷史", "舊傳統與新思潮"), ("歷史", "現代國家的挑戰"), ("歷史", "現代國家的變局"), ("歷史", "共黨政權在中國"), ("歷史", "當代東亞的局勢")],
    ("5", "9", "上"): [("地理", "古代文明的誕生"), ("地理", "古希臘羅馬文化的開展"), ("地理", "普世宗教的發展"), ("地理", "近代歐洲的興起"), ("地理", "歐洲與俄羅斯的自然環境"), ("地理", "歐洲與俄羅斯的產業與文化"), ("地理", "北美洲"), ("地理", "中南美洲"), ("歷史", "漠南非洲的自然環境與文化"), ("歷史", "漠南非洲的產業與經濟發展"), ("歷史", "多元世界的互動"), ("歷史", "近代歐洲的變革")],
    ("6", "9", "下"): [("地理", "臺灣與鄉鎮市區地名"), ("地理", "臺灣聚落地名"), ("地理", "臺灣農業生產與運銷"), ("地理", "臺灣飲食文化與食品安全"), ("歷史", "革命的年代"), ("歷史", "民族主義與帝國主義"), ("歷史", "第一次世界大戰與戰間期"), ("歷史", "第二次世界大戰與戰後情勢")],
}

urls = [
    "https://website.hle.com.tw/market/jr/%E6%95%99%E6%9D%90/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/%E7%BF%B0%E6%9E%97%E5%9C%8B%E4%B8%AD%E5%9C%B0%E7%90%86%E4%B8%83%E4%B8%8A%E8%AA%B2%E6%9C%AC.pdf",
    "https://website.hle.com.tw/market/jr/%E6%95%99%E6%9D%90/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/%E7%BF%B0%E6%9E%97%E5%9C%8B%E4%B8%AD%E6%AD%B7%E5%8F%B2%E4%B8%83%E4%B8%8B%E8%AA%B2%E6%9C%AC.pdf",
    "https://website.hle.com.tw/market/jr/%E6%95%99%E6%9D%90/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/%E7%BF%B0%E6%9E%97%E5%9C%8B%E4%B8%AD%E6%AD%B7%E5%8F%B2%E5%85%AB%E4%B8%8A%E8%AA%B2%E6%9C%AC.pdf",
    "https://website.hle.com.tw/market/jr/%E8%A1%8C%E9%8A%B7%E7%B6%B2%E7%AB%99/112/%E6%95%99%E6%9D%90/%E6%AD%B7%E5%8F%B2/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/111%E5%9C%8B%E4%B8%AD%E7%A4%BE%E6%9C%832%E4%B8%8B%E6%AD%B7%E5%8F%B2%E8%AA%B2%E6%9C%AC.pdf",
    "https://website.hle.com.tw/market/jr/%E6%95%99%E6%9D%90/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/%E7%BF%B0%E6%9E%97%E5%9C%8B%E4%B8%AD%E5%9C%B0%E7%90%86%E4%B9%9D%E4%B8%8A%E8%AA%B2%E6%9C%AC.pdf",
    "https://website.hle.com.tw/market/jr/%E6%95%99%E6%9D%90/%E6%95%99%E6%9D%90%E6%A8%A3%E6%9B%B8/%E7%BF%B0%E6%9E%97%E5%9C%8B%E4%B8%AD%E5%9C%B0%E7%90%86%E4%B9%9D%E4%B8%8B%E8%AA%B2%E6%9C%AC.pdf",
]
area = {"地理": "kg-social-content-geography", "歷史": "kg-social-content-history", "公民": "kg-social-content-civics"}
out = {"id": "mapset-social-hanlin-official-2026", "subject": "social", "publisher": "hanlin", "academicYear": "115", "source": {"type": "official-publisher-page", "url": urls[0], "locator": "翰林官方教材樣書 PDF 公開目次（六冊；社會由地理、歷史、公民分篇）", "verifiedAt": "2026-08-26", "verifiedBy": "Codex official-publisher verification", "confidence": "high", "editionNote": "僅保存目次 metadata；KG 先掛社會領域穩定節點，逐章課綱代碼待後續交叉核驗。", "additionalUrls": urls}, "mappingMethod": "official-publisher-toc-to-social-area-kg-conservative-cross-reference", "volumes": [], "status": "verified", "notes": "章名取自官方公開教材樣書目次；area-level KG 對照不宣稱出版社背書。"}
for (v, g, sem), rows in volumes.items():
    out["volumes"].append({"volume": v, "grade": g, "semester": sem, "entries": [{"chapterCode": f"{kind}-{i}", "chapterLabel": label, "knowledgeIds": [area[kind]], "relation": "primary", "confidence": "medium", "notes": "官方目次章名；目前僅完成領域層級 KG 對照，逐章代碼待核驗。"} for i, (kind, label) in enumerate(rows, 1)]})
(ROOT / "textbook-mapping/social/hanlin-official-2026.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print("wrote", sum(len(v) for v in volumes.values()), "entries")

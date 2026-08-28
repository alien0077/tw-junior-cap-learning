import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_70_5116%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E8%87%AA%E7%84%B6%E9%A0%98%E5%9F%9F.pdf"
books = {
    ("3", "8", "上"): [("1", "基本測量"), ("2", "物質的世界"), ("3", "波動與聲音"), ("4", "光"), ("5", "溫度與熱"), ("6", "元素與化合物")],
    ("4", "8", "下"): [("1", "化學反應"), ("2", "氧化還原"), ("3", "酸、鹼、鹽"), ("4", "反應速率與平衡"), ("5", "有機化合物"), ("6", "力與壓力")],
}
out = {"id":"mapset-science-nani-schoolplan-2026","subject":"science","publisher":"nani","academicYear":"115","source":{"type":"book-inspection","url":url,"locator":"桃園市忠明國中公開自然領域課程計畫；南一版國中自然 8 上／8 下教材章節","verifiedAt":"2026-08-26","verifiedBy":"Codex public school-plan verification","confidence":"medium","editionNote":"校方公開課程計畫作為版本與章節交叉證據；不等同南一出版社正式目次。"},"mappingMethod":"school-plan-chapter-index-to-official-science-kg-conservative-cross-reference","volumes":[],"status":"verified","notes":"保存 12 筆章節 metadata；未擷取教材內文，其餘南一冊別仍待公開章節證據。"}
for (v,g,s), rows in books.items():
    out["volumes"].append({"volume":v,"grade":g,"semester":s,"entries":[{"chapterCode":f"ch-{c}","chapterLabel":label,"knowledgeIds":["kg-science-learning-content"],"relation":"primary","confidence":"medium","notes":"校方課程計畫列出的南一版自然章節；逐章課綱碼待核驗。"} for c,label in rows]})
(ROOT/"textbook-mapping/science/nani-schoolplan-2026.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("wrote",sum(len(x) for x in books.values()),"entries")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_70_5116%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E8%87%AA%E7%84%B6%E9%A0%98%E5%9F%9F.pdf"
books = {
    ("5", "9", "上"): [("4", "電流、電壓與歐姆定律"), ("5", "地球的環境"), ("6", "板塊運動與岩層的祕密"), ("7", "浩瀚的宇宙")],
    ("6", "9", "下"): [("1", "電與生活"), ("2", "電與磁"), ("3", "變化莫測的天氣"), ("4", "全球氣候變遷與調適")],
}
out = {"id":"mapset-science-hanlin-schoolplan-9-2026","subject":"science","publisher":"hanlin","academicYear":"115","source":{"type":"book-inspection","url":url,"locator":"桃園市忠明國中公開自然領域課程計畫；翰林版國中自然 9 上／9 下教材章節與單元","verifiedAt":"2026-08-26","verifiedBy":"Codex public school-plan verification","confidence":"medium","editionNote":"校方公開課程計畫作為翰林版本與章節交叉證據；不等同出版社正式目次。"},"mappingMethod":"school-plan-chapter-index-to-official-science-kg-conservative-cross-reference","volumes":[],"status":"verified","notes":"保存 8 筆章節 metadata；其餘章內單元待取得完整公開目次後再細化。"}
for (v,g,s), rows in books.items():
    out["volumes"].append({"volume":v,"grade":g,"semester":s,"entries":[{"chapterCode":f"ch-{c}","chapterLabel":label,"knowledgeIds":["kg-science-learning-content"],"relation":"primary","confidence":"medium","notes":"校方課程計畫列出的翰林版自然章節；逐章課綱碼待核驗。"} for c,label in rows]})
(ROOT/"textbook-mapping/science/hanlin-schoolplan-9-2026.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("wrote",sum(len(x) for x in books.values()),"entries")

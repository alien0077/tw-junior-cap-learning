import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
units = {
    ("1", "7", "上"): ["Starter", "U1 be 動詞與 Who 問句", "U2 名詞複數與 Where 問句", "U3 祈使句與 can", "U4 星期／時間與現在進行式", "U5 日期／When 問句", "U6 There is／are"],
    ("2", "7", "下"): ["U1 現在簡單式", "U2 頻率副詞與 How often", "U3 How much／Which", "U4 How much／many", "U5 be 動詞與規則過去式", "U6 不規則過去式／because／so"],
    ("3", "8", "上"): ["U1 天氣問答與授與動詞", "U2 過去式與 when／before／after", "U3 過去進行式與時間逆讀", "U4 不定詞／動名詞／虛主詞 it", "U5 問路與交通工具", "U6 未來式與三花句型"],
    ("4", "8", "下"): ["U1 連綴動詞與比較級", "U2 最高級與反身代名詞", "U3 副詞比較級／最高級與使役動詞", "U4 感官動詞與 if", "U5 數量不定代名詞與 although", "U6 that 名詞子句與附加問句"],
}
url = "https://website.hle.com.tw/market/jr/%E8%A1%8C%E9%8A%B7%E7%B6%B2%E7%AB%99/112/%E6%95%99%E6%9D%90/%E8%8B%B1%E8%AA%9E/%E6%95%99%E6%9D%90%E7%B0%A1%E4%BB%8B/%E5%9C%8B%E4%B8%AD%E8%8B%B1%E8%AA%9E%E6%90%B6%E5%85%88%E7%9C%8B-%E4%B8%96%E7%95%8C%E6%96%B0%E9%AE%AE%E4%BA%8B%E7%9C%9F%E5%A5%87%E5%A6%99%E5%90%88%E6%AA%94.pdf"
out = {"id":"mapset-english-hanlin-official-2026","subject":"english","publisher":"hanlin","academicYear":"115","source":{"type":"official-publisher-page","url":url,"locator":"翰林官方英文教材搶先看公開 PDF；七上至八下 U／Starter 結構","verifiedAt":"2026-08-26","verifiedBy":"Codex official-publisher verification","confidence":"high","editionNote":"公開資料為 112 年改版簡介，僅保存單元 metadata；九年級及 115 年版差異仍待新版本目次。"},"mappingMethod":"official-publisher-unit-index-to-english-area-kg-conservative-cross-reference","volumes":[],"status":"verified","notes":"四冊 25 筆單元章名取自官方公開教材簡介；KG 先掛英文內容根節點，未把文法單元名稱視為課綱碼。"}
for (v,g,s), labels in units.items():
    out["volumes"].append({"volume":v,"grade":g,"semester":s,"entries":[{"chapterCode":f"unit-{i}","chapterLabel":label,"knowledgeIds":["kg-english-learning-content"],"relation":"primary","confidence":"medium","notes":"官方公開英文單元結構；逐單元課綱碼待核驗。"} for i,label in enumerate(labels,1)]})
(ROOT/"textbook-mapping/english/hanlin-official-2026.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("wrote",sum(len(x) for x in units.values()),"entries")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
url = "https://drive.google.com/uc?id=1gMUVcDjfXmqIapg-fNnfPuLFaK98dxGX&export=download"
chapters = {
    "1": ["細胞的分裂", "無性生殖", "有性生殖"],
    "2": ["遺傳、染色體與基因", "人類的遺傳", "突變與遺傳疾病", "生物技術"],
    "3": ["化石與演化", "生物的命名與分類", "原核、原生生物及真菌界", "植物界", "動物界"],
    "4": ["族群、群集與演替", "生物間的互動關係", "生態系", "生態系的類型"],
    "5": ["生物多樣性", "生物多樣性面臨的危機", "保育的落實"],
}
entries = []
for chapter, labels in chapters.items():
    for i, label in enumerate(labels, 1):
        entries.append({"chapterCode": f"{chapter}-{i}", "chapterLabel": label, "knowledgeIds": ["kg-science-learning-content"], "relation": "primary", "confidence": "medium", "notes": "林口國中 114 學年度公開課程計畫明列翰林版七年級自然科學（生物）架構；此為校方交叉證據，逐碼 KG 對照待進一步核驗。"})
out = {"id":"mapset-science-hanlin-schoolplan-2026","subject":"science","publisher":"hanlin","academicYear":"115","source":{"type":"book-inspection","url":url,"locator":"林口國中 114 學年度七年級自然領域課程計畫附件；翰林版七年級自然科學（生物）課程架構與 1-1 至 5-3 單元","verifiedAt":"2026-08-26","verifiedBy":"Codex public school-plan verification","confidence":"medium","editionNote":"校方公開課程計畫作為翰林版本與單元架構交叉證據；不等同翰林出版社正式目次。"},"mappingMethod":"school-plan-unit-index-to-official-science-kg-conservative-cross-reference","volumes":[{"volume":"2","grade":"7","semester":"下","entries":entries}],"status":"verified","notes":"保存 19 筆單元 metadata，不擷取教材內文；其餘翰林自然冊別仍待公開可核驗目次。"}
(ROOT/"textbook-mapping/science/hanlin-schoolplan-2026.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print("wrote",len(entries),"entries")

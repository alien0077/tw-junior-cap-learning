#!/usr/bin/env python3
"""Independently normalize the Hist Ib-IV-2 question bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ib-iv-2"; KG="kg-social-content-hist-ib-iv-2"
TARGETS=["A","B","C","D","A","B","C","D","B","C"]
FOCI=[
 ("新統治體制與多方調整","制度移入不只是官方命令，也要看地方菁英、居民與既有社會如何利用、協商或抵抗。"),
 ("戶籍、警察與道路","行政與交通系統同時帶來治理能力和生活規訓，不能只用現代化或控制其中一詞概括。"),
 ("土地調查與權利變化","測量和登記會重新界定納稅者與土地權利，必須比較地主、佃農與原有使用者的不同處境。"),
 ("學校與家庭選擇","教育制度傳遞國家語言與歷史，也提供識字和職能；入學機會與家庭選擇並不一致。"),
 ("防疫建設與生活管理","公共衛生可能降低疾病卻增加檢查與隔離，收益和管理成本需同時納入。"),
 ("產業政策與勞動爭議","產量或出口增加不等於所有人受益，應追查資本、工資、工時、土地與環境的分配。"),
 ("地方菁英與行政協商","地方仕紳和商人可能合作也可能爭取利益，角色會依政策、資源和時段變化。"),
 ("抗爭、請願與執行落差","抵抗不只有武力，請願、談判和地方執行調整也能改變政策效果，需查結果的範圍。"),
 ("港口、山區與城鄉差異","新制度和技術以不同速度進入各地，空間差異不能被單一城市經驗取代。"),
 ("官方報告與地方記憶","年度報告、報紙、家族文書和口述各有目的與視角，應交叉比較而非只採官方成功敘事。"),
]
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%9A%84%E7%A4%BE%E6%9C%83.pdf","title":"高雄市立鹽埕國民中學公開段考社會科；僅研究制度、資料判讀與歷史推理題型，未複製原題。","year":"114","locator":"公開段考社會科 PDF；第 1 題至第 10 題型範圍：制度、社會變化與因果界線","observedPattern":"由制度與多方生活材料要求學生分析政策效果、群體差異與證據範圍。"},
 {"url":"https://affairs.kh.edu.tw/1126/upload/file_list/149","title":"高雄市立文府國民中學公開社會科試題入口；僅研究多資料互證題型，未複製原題。","year":"113-114","locator":"公開試題與解答入口；第 1 題至第 10 題型範圍：治理、社會變遷與多重證據","observedPattern":"比較官方文件、地方記錄與不同群體觀點，區分直接記錄、推論與待補證主張。"},
 {"url":"https://www.dwm.kh.edu.tw/view/index.php?MainMenuId=64182&MainType=0&SubMenuId=64184&SubType=104&WebID=344","title":"高雄市立大灣國民中學公開段考試題入口；僅研究政策、地方社會與多方角色題型，未複製原題。","year":"113-114","locator":"公開段考試題入口；第 1 題至第 10 題型範圍：政策效果、文化變遷與多方角色","observedPattern":"從歷史材料分析制度、利益與生活變化，不以單一來源包辦結論。"},
]
def refs(): return [{**x,"subject":"social","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for x in SOURCES]
for i,target in enumerate(TARGETS,1):
 p=OUT/f"question-social-content-hist-ib-iv-2-{i}.json"; d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]==LESSON and d["knowledgeIds"]==[KG]
 old=d["answer"]["value"]; oi=ord(old)-65; ti=ord(target)-65; correct=d["options"][oi]["text"]; rest=[x["text"] for j,x in enumerate(d["options"]) if j!=oi]; ordered=rest[:ti]+[correct]+rest[ti:]
 d["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; focus,reason=FOCI[i-1]
 d["answer"]={"value":target,"explanation":f"本題聚焦「{focus}」。{reason} 正確答案為選項 {target}：「{correct}」。"}; d["solutionStrategy"]=f"先定位{focus}的時間、制度、角色與資料，再分開政策目標、實際執行與群體成本；{reason}"
 d["solutionSteps"]=[f"讀題定位：圈出制度、地點、群體與任務，確認本題正在檢核「{focus}」。","建立判準：把官方政策、地方執行、生活經驗與資源分配分層，並標記來源。",f"核對正解：選項 {target}「{correct}」符合題幹，因為{reason}","逐項排除：檢查其餘選項是否把建設等同人人受益、把官方敘事當全境實況，或忽略女性、勞工、佃農與地方居民。","結論回查：重新核對時段、地區、群體與證據強度；若加入地方材料，必須重新檢查結論。"]
 d["examPatternRefs"]=refs(); d["updatedAt"]="2026-09-13"; d["reviewStatus"]="draft"; d["provenance"]["authoringNote"]="依官方課綱、歷 Ib-Ⅳ-2 知識圖譜及三所公立學校公開社會科試題的制度、政策效果與多方證據能力方向獨立改寫；未複製原題文字、選項、圖片或答案，待逐題學科與 Terra 複核。"
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

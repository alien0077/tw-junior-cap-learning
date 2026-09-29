#!/usr/bin/env python3
"""Independently normalize the Hist Ib-IV-1 question bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ib-iv-1"; KG="kg-social-content-hist-ib-iv-1"
TARGETS=["A","B","C","D","A","B","C","D","B","C"]
FOCI=[
 ("通商口岸與多方利益","開放後的貿易同時牽涉外商、買辦、工匠與官府，利益增加不代表權力和成本平均分配。"),
 ("不平等條約與有限主權","特權改變司法、關稅或行政空間，但不能由單一條款直接推論所有主權機能都消失。"),
 ("外交報告與地方主動性","外國報告有觀察位置與政治目的，必須和地方檔案、商人家書或工廠記錄互證。"),
 ("協定關稅與財政選擇","關稅制度會影響財政和貿易，但仍需連結執行機關、地方市場與不同群體的結果。"),
 ("工業、技術與勞動","工廠或鐵路的出現同時改變技術、資本與勞動關係，不能只用『現代化』一詞概括。"),
 ("外交衝突與地方生活","戰爭和談判會透過治安、物價、徵募與移動影響居民，地方經驗是政治史的一部分。"),
 ("翻譯者與中介角色","通事、買辦與地方菁英可能促成協商，也可能受到不同權力約束，不能被寫成透明管道。"),
 ("制度移植與在地調整","外來制度或技術進入後會受本地法律、資源與社會關係改造，形式相似不等於效果相同。"),
 ("多重證據與晚清社會","官方、外國與民間材料各有盲點，應比較形成背景與缺席群體，而非選一份當唯一真相。"),
 ("衝突、協商與不確定性","接觸同時可能包含壓力、合作和地方策略，結論要限定時間、地點與可由材料支持的範圍。"),
]
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%9A%84%E7%A4%BE%E6%9C%83.pdf","title":"高雄市立鹽埕國民中學公開段考社會科；僅研究近代東亞資料判讀與歷史推理題型，未複製原題。","year":"114","locator":"公開段考社會科 PDF；第 1 題至第 10 題型範圍：制度、衝突與多重資料","observedPattern":"以條約、制度與不同角色材料要求學生判斷主權、利益與證據範圍。"},
 {"url":"https://affairs.kh.edu.tw/1126/upload/file_list/149","title":"高雄市立文府國民中學公開社會科試題入口；僅研究近代交流與多資料互證題型，未複製原題。","year":"113-114","locator":"公開試題與解答入口；第 1 題至第 10 題型範圍：跨區交流、制度與多重證據","observedPattern":"比較官方文件、地方記錄與角色觀點，區分直接記錄、推論與待補證主張。"},
 {"url":"https://www.dwm.kh.edu.tw/view/index.php?MainMenuId=64182&MainType=0&SubMenuId=64184&SubType=104&WebID=344","title":"高雄市立大灣國民中學公開段考試題入口；僅研究政治衝突與社會變化題型，未複製原題。","year":"113-114","locator":"公開段考試題入口；第 1 題至第 10 題型範圍：政治回應、文化變遷與多方角色","observedPattern":"從歷史情境分析不同群體、利益與制度變化，不以單一來源包辦結論。"},
]
def refs(): return [{**x,"subject":"social","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for x in SOURCES]
for i,target in enumerate(TARGETS,1):
 p=OUT/f"question-social-content-hist-ib-iv-1-{i}.json"; d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]==LESSON and d["knowledgeIds"]==[KG]
 old=d["answer"]["value"]; oi=ord(old)-65; ti=ord(target)-65; correct=d["options"][oi]["text"]; rest=[x["text"] for j,x in enumerate(d["options"]) if j!=oi]; ordered=rest[:ti]+[correct]+rest[ti:]
 d["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; focus,reason=FOCI[i-1]
 d["answer"]={"value":target,"explanation":f"本題聚焦「{focus}」。{reason} 正確答案為選項 {target}：「{correct}」。"}
 d["solutionStrategy"]=f"先定位{focus}的時間、角色、制度與資料，再分開直接證據、推論和成本；{reason}"
 d["solutionSteps"]=[f"讀題定位：圈出材料中的條約、港口、角色或生活線索，確認本題正在檢核「{focus}」。","建立判準：把外交制度、地方執行、群體利益與資料形成背景分層。",f"核對正解：選項 {target}「{correct}」符合題幹，因為{reason}","逐項排除：檢查其餘選項是否把接觸寫成單向、把特權誇大成全部主權消失，或忽略地方與勞動者。","結論回查：重新核對時間、地點、角色與證據強度；若新增地方檔案或民間材料，必須重新檢查結論。"]
 d["examPatternRefs"]=refs(); d["updatedAt"]="2026-09-13"; d["reviewStatus"]="draft"; d["provenance"]["authoringNote"]="依官方課綱、歷 Ib-Ⅳ-1 知識圖譜及三所公立學校公開社會科試題的近代東亞制度、衝突與多方證據能力方向獨立改寫；未複製原題文字、選項、圖片或答案，待逐題學科與 Terra 複核。"
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

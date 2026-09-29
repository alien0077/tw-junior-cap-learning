#!/usr/bin/env python3
"""Normalize the Hist Cb-IV-2 Han social-activity bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-cb-iv-2"; KG="kg-social-content-hist-cb-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-cb-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出同鄉、親族、地緣、宗族、祠堂、借貸、婚姻、土地、勞動或地方組織等線索。","拆分功能：分別辨認社會網絡的支持、資源分配、排除門檻與衝突調解功能，再和官方制度資料比對。",f"核對正解：選項 {target}「{correct}」能說明漢人社會活動的多重功能，不把單一村落推成所有地區的唯一模式。","排除誘答：檢查是否把宗族等同全部社會、把合作只看成互助，或忽略外人、女性、佃戶與不同階層的經驗。","結論回查：確認資料的地區、時期、群體與組織層次一致；加入其他村落或身分資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

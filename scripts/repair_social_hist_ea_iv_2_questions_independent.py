#!/usr/bin/env python3
"""Normalize the Hist Ea-IV-2 infrastructure and industry bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-ea-iv-2"; KG="kg-social-content-hist-ea-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-ea-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出鐵路、港口、工場、產地、出口、糖廠、土地、搬遷、勞動或產業政策等線索。","比較分配效果：分開檢查運輸效率、產業產量、國家目標與不同居民、商人、工人或小船業者受到的影響。",f"核對正解：選項 {target}「{correct}」能以多項資料評估建設與政策的收益、成本及地區差異。","排除誘答：檢查是否把出口增加等同全民受益、把單一企業年報推成全臺趨勢，或忽略搬遷、勞動與環境代價。","結論回查：確認指標、時間、地區、受影響群體與資料來源一致；補入地方或勞工資料後重新檢查政策效果。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

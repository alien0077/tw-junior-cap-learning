#!/usr/bin/env python3
"""Normalize the Hist Eb-IV-2 urban-culture bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-eb-iv-2"; KG="kg-social-content-hist-eb-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-eb-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出道路、排水、街區、行政中心、商業區、電車、住宅、菁英、租屋或公共服務等線索。","比較都市經驗：分開檢查空間分布、交通可及性、生活方式與不同階層的受益和負擔。",f"核對正解：選項 {target}「{correct}」能說明都市現代化的基礎設施效果與地區、階層差異。","排除誘答：檢查是否把中心建設當成全城生活、把菁英回憶推成全民經驗，或把電車沿線繁榮當成所有居民受益。","結論回查：確認資料的城市、時期、空間範圍與群體相稱；補入周邊聚落或勞工資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

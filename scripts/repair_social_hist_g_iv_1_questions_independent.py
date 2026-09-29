#!/usr/bin/env python3
"""Normalize the Hist G-IV-1 local-history inquiry II bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-g-iv-1"; KG="kg-social-content-hist-g-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-g-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出假設、鐵路、聚落、商店、工業城、農業、樣本、郊區、移入家庭、比較控制或資料缺口等線索。","修正研究設計：先把因果主張拆成可比較條件，再檢查時間、地點、群體、產業與資料代表性。",f"核對正解：選項 {target}「{correct}」能回應反例、比較條件或樣本偏差，讓地方史結論可被檢驗。","排除誘答：檢查是否只沿用原假設、只看市中心、把同在鐵路沿線當成相同結果，或忽略郊區與移入家庭。","結論回查：確認比較單位、資料範圍、因果機制與不確定處一致；新增資料後重新檢查主張。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

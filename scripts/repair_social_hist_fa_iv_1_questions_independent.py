#!/usr/bin/env python3
"""Normalize the Hist Fa-IV-1 postwar governance-transition bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fa-iv-1"; KG="kg-social-content-hist-fa-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fa-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出接收、行政區、官署、戶籍、警察、學校、基層人員、公告或居民反應等線索。","拆分政權轉變：先比較制度名稱與行政延續，再檢查人員、地方執行、政策落地及不同居民的經驗。",f"核對正解：選項 {target}「{correct}」能同時說明政權移轉的制度變化與延續，不把官方公告等同所有居民態度。","排除誘答：檢查是否只看名稱改變、把接收公告當全民歡迎，或忽略地方行政、警察與學校的實際轉接。","結論回查：確認資料的時間、機構、基層執行與群體範圍相稱；補入地方檔案或民間資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

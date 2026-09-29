#!/usr/bin/env python3
"""Normalize the Hist Cb-IV-1 Indigenous-society change bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-cb-iv-1"; KG="kg-social-content-hist-cb-iv-1"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-cb-iv-1-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出親族、年齡組織、祭儀、家庭生計、交易、官府分類、教育或社會變化等線索。","多方比對：把族人自述、生活實踐、官方文書與外部觀察分開，檢查各自的形成目的與盲點。",f"核對正解：選項 {target}「{correct}」能說明社會延續與變化並存，且保留不同家庭、群體與時期的差異。","排除誘答：檢查是否以單一官員記錄代表所有族人、把一項生計改變推成文化消失，或忽略族群內部多樣性。","結論回查：確認主張的群體、時間、資料來源與變化程度相稱；補入不同群體資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

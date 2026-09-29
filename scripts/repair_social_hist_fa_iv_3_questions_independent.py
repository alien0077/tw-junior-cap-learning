#!/usr/bin/env python3
"""Normalize the Hist Fa-IV-3 Indigenous-policy bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-fa-iv-3"; KG="kg-social-content-hist-fa-iv-3"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-fa-iv-3-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出行政類別、教育、戶籍、土地、森林、水土保持、開發、傳統領域、生活路徑或部落聲音等線索。","分辨政策與生活：先比較政策文件的目標、分類與執行，再檢查族人實際使用土地、教育與身分制度的經驗。",f"核對正解：選項 {target}「{correct}」能同時處理國家政策的制度效果、土地權利與部落觀點，不把政策報告當成生活改善的充分證據。","排除誘答：檢查是否把行政分類當成自然身分、把開發限制只看成保育，或只採政府資料而忽略口述、地圖與傳統領域證據。","結論回查：確認政策、時期、群體與土地尺度相稱；補入部落資料與多方地圖後重新檢查結論。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

#!/usr/bin/env python3
"""Normalize the Hist Hb-IV-2 trade and cultural-exchange bank."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/social"; LESSON="lesson-social-content-hist-hb-iv-2"; KG="kg-social-content-hist-hb-iv-2"; TARGETS=["A","B","C","D","B","C","D","A","B","C"]
for i,target in enumerate(TARGETS,1):
 path=OUT/f"question-social-content-hist-hb-iv-2-{i}.json"; item=json.loads(path.read_text(encoding="utf-8")); assert item["lessonId"]==LESSON and item["knowledgeIds"]==[KG]
 old=item["answer"]["value"]; ci=ord(old)-65; ti=ord(target)-65; correct=item["options"][ci]["text"]; rest=[x["text"] for j,x in enumerate(item["options"]) if j!=ci]; ordered=rest[:ti]+[correct]+rest[ti:]
 item["options"]=[{"id":chr(65+j),"text":x} for j,x in enumerate(ordered)]; item["answer"]["value"]=target; item["updatedAt"]="2026-09-13"; item["reviewStatus"]="draft"
 item["solutionSteps"]=["讀題定位：圈出港口帳冊、絲織品、香料、陶瓷、稅收、轉運、外來器物、地方詞彙、碑記、會館、墓地、宗教場所或通婚等線索。","交叉驗證交流：先分辨貨物流動、稅收網絡、語言借用、宗教實踐與人口關係，再檢查各資料的形成背景。",f"核對正解：選項 {target}「{correct}」能以多種物質、文字與社會資料支持商貿影響或跨文化交流的有界結論。","排除誘答：檢查是否只憑外來器物宣稱文化中心、把地方詞彙當唯一來源，或忽略地方居民、女性與不同商人群體。","結論回查：確認交流方向、時間、港口範圍與資料相稱；補入考古、帳冊或地方社群資料後重新檢查。"]
 for ref in item.get("examPatternRefs",[]): ref["reuseDecision"]="pattern-only"; ref["status"]="recorded"
 path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(TARGETS)} independent questions for {LESSON}")

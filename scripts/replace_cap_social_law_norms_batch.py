#!/usr/bin/env python3
"""Replace one civics law/norm lesson with independently adapted CAP-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-social-content-civ-bc-iv-1"
KID = "kg-social-content-civ-bc-iv-1"
SOURCE = "https://www.grow22.com/download/114/114_cp/04_114P_Society.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("下列何者最能呈現法律規範的特徵？", ["政府依法要求駕駛人遵守速限，違反可能受處罰", "朋友約定見面時互相點頭", "家人鼓勵晚輩尊敬長者", "同學習慣排隊購買午餐"], "A", "法律由有權機關制定並具有國家強制力，違反可能依法受到處罰。", "第36題法院與法律規範題型改編"),
    ("下列何者較屬於社會習俗，而非法律規範？", ["依交通號誌停車", "依法繳納所得稅", "進入他人住宅前先敲門", "依法院判決履行義務"], "C", "進入住宅前敲門通常是禮貌與習俗，並非一般情況下由法律直接規定的行為。", "第36題法律與其他規範區分題型改編"),
    ("小安在圖書館輕聲交談，是因為館內約定保持安靜；若違反，通常會受到何種制裁？", ["國家刑罰", "館方勸導或請其離開", "法院立即判刑", "剝奪全部公民權"], "B", "圖書館規則通常以管理與勸導維持秩序，與國家法律的強制制裁不同。", "第36題規範與制裁題型改編"),
    ("若要確認一項行為是否違反法律，最應先查閱哪項資料？", ["當事人的個人喜好", "同學的口頭猜測", "現行法規與適用條文", "社群留言的按讚數"], "C", "法律判斷須依現行法規與適用條文，不能只靠個人喜好或網路猜測。", "第38題法律權利與資料判讀題型改編"),
    ("下列哪項最能說明道德規範與法律規範可能不同？", ["違反道德可能受到輿論譴責，但不一定有法律處罰", "所有道德要求都由法院執行", "所有法律都只靠個人自律", "道德與法律永遠沒有任何關聯"], "A", "道德常透過內心自律與社會評價維持，未必具有法律的國家強制制裁。", "第36題法律與其他規範差異題型改編"),
    ("某校訂定校規要求學生上課準時，這項規範與國家法律相比，主要差異為何？", ["校規通常由學校在管理權限內訂定，適用範圍較特定", "校規一定高於憲法", "校規可以任意處以刑罰", "校規適用全世界所有人民"], "A", "校規主要規範校內成員與校園生活，適用範圍和制裁方式不同於國家法律。", "第36題規範適用範圍題型改編"),
    ("法院受理民事爭議並依法律作成判決，最能說明法律具有哪項功能？", ["解決社會紛爭並保障權利", "取消所有社會習俗", "使每個人想法完全相同", "只負責安排節慶活動"], "A", "法院依法律處理爭議，可確認權利義務並提供制度化的紛爭解決途徑。", "第36題法院參訪與法律功能題型改編"),
    ("社區居民約定每週末輪流打掃公共區域，這項規範若沒有法律或契約依據，主要依靠什麼維持？", ["居民自律與彼此信任", "法院自動派警察監督", "國家刑法立即處罰", "國際組織強制執行"], "A", "社區約定通常靠成員自律、互信與社會評價維持，不當然具有國家強制力。", "第36題社會規範與法律制裁題型改編"),
    ("下列哪項情況最可能同時涉及法律規範與道德判斷？", ["拾得他人財物後依法返還，也被認為是誠實的表現", "選擇喜歡的午餐口味", "決定週末閱讀哪本書", "選擇房間的窗簾顏色"], "A", "拾得物返還可能涉及法律上的義務，也常被視為誠實的道德行為。", "第38題權利義務與規範整合題型改編"),
    ("比較法律、道德與習俗時，哪種方法最可靠？", ["只看規範名稱是否嚴格", "比較制定來源、適用範圍與制裁方式", "只看多數人是否喜歡", "只看違反者是否道歉"], "B", "比較規範的來源、適用範圍與制裁方式，才能辨識法律與其他社會規範的差異。", "第36題法律與其他規範比較題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "social" / f"question-social-content-civ-bc-iv-1-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    options = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考社會科；{locator}；官方答案表：{ANSWER}；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style Social Studies law/norm questions")

#!/usr/bin/env python3
"""Replace the civ-AA citizenship questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "social"
LESSON_ID = "lesson-social-content-civ-aa"
KG_ID = "kg-social-content-civ-aa"
SOURCE_URL = (
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/"
    "114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83"
    "%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83.pdf"
)


def rotate_options(options, answer_letter):
    answer_index = ord(answer_letter) - ord("A")
    shift = (4 - answer_index) % 4
    rotated = options[shift:] + options[:shift]
    return [{"id": chr(ord("A") + i), "text": text} for i, text in enumerate(rotated)]


QUESTIONS = [
    {
        "prompt": "下列哪一項最能說明公民身分的意義？",
        "options": ["只代表個人的興趣", "表示個人與政治共同體之間具有權利與義務關係", "只由居住地的天氣決定", "只代表家庭中的排行"],
        "answer": "B",
        "explanation": "公民身分涉及個人與政治共同體的法律及公共關係，通常包含參與、保障等權利與遵守規範等義務。",
    },
    {
        "prompt": "學校選舉學生代表時，所有符合相同資格的學生都能投票。這項安排主要展現哪個原則？",
        "options": ["身分平等與公平參與", "由成績決定投票權", "以家庭背景分配票數", "只有幹部才能表達意見"],
        "answer": "A",
        "explanation": "相同資格者享有相同參與機會，反映平等與公平；不能任意依成績或家庭背景差別對待。",
    },
    {
        "prompt": "公民享有表達意見的自由，但在公共討論中仍應如何行動？",
        "options": ["可散播明知不實的指控", "可完全不理會他人權利", "應以合理方式表達並尊重他人的權益", "只要人數多就能禁止少數發言"],
        "answer": "C",
        "explanation": "權利行使並非毫無界線，應兼顧事實、公共秩序與他人權益，不能以自由之名侵害他人。",
    },
    {
        "prompt": "小林的家庭文化、語言背景與學校生活都影響他對自己的理解。下列哪個說法較合理？",
        "options": ["公民身分只能由單一文化決定", "個人可以同時具有多種身分認同", "家庭背景必然決定政治立場", "不同身分不可能和平共存"],
        "answer": "B",
        "explanation": "身分認同可能受到家庭、語言、文化、學校與社群等多重經驗影響，這些認同可以並存。",
    },
    {
        "prompt": "社區討論公共設施時，主持人讓不同立場的公民提出理由並回應。這最能體現哪項公民能力？",
        "options": ["服從多數而不必說明", "理性溝通與公共參與", "避免接觸不同意見", "以私人關係取代共同規則"],
        "answer": "B",
        "explanation": "公民參與需要表達立場、聆聽他人、提出理由並共同討論，而不是只服從結果或依私人關係決定。",
    },
    {
        "prompt": "若公共規則限制某項行動，哪一項判斷最符合民主法治原則？",
        "options": ["只要管理者想限制就可以", "限制應有公共目的、明確依據並避免過度侵害權利", "少數人不必遵守任何規則", "規則越模糊越容易公平"],
        "answer": "B",
        "explanation": "民主法治下的權利限制應有正當公共目的與明確依據，並符合必要與適度原則，不能任意或過度。",
    },
    {
        "prompt": "下列哪一項較接近公民的公共責任？",
        "options": ["只要求別人遵守規則", "關心公共事務並在共同規範下負責任地參與", "遇到不同意見就退出所有討論", "把公共資源視為個人專用"],
        "answer": "B",
        "explanation": "公民責任包括遵守合理規範、關心公共事務、尊重他人並以負責任方式參與共同生活。",
    },
    {
        "prompt": "一名長期居住者積極參與社區服務，但居民身分與公民身分在概念上仍可能不同。下列說法何者合理？",
        "options": ["所有居住者在任何制度下都具有完全相同的公民資格", "居住與公民身分是不同概念，具體權利須依制度判斷", "參與志工就自動取得所有政治權利", "沒有公民身分就不能有任何公共責任"],
        "answer": "B",
        "explanation": "居住、社區成員與公民是可相關但不完全相同的身分；具體資格與權利需依適用制度及規範判斷。",
    },
    {
        "prompt": "為了讓少數意見也能被看見，班級議案要求提案者說明理由，並保留不同意見紀錄。這項做法有何意義？",
        "options": ["讓少數意見必然否決所有決議", "兼顧多數決與少數權利的表達", "讓投票結果完全不必執行", "用紀錄取代任何公共討論"],
        "answer": "B",
        "explanation": "民主程序可採多數決形成決定，但也應保障少數表達、提出理由與被記錄的機會，避免多數壓制。",
    },
    {
        "prompt": "下列哪一項最符合公民身分與國家認同的關係？",
        "options": ["國家認同只能依血緣判定", "公民可以對共同體產生認同，也可以對公共政策提出批判", "認同國家就不能批評政府", "沒有相同興趣就不能成為共同體成員"],
        "answer": "B",
        "explanation": "公民對共同體的認同可以與批判、監督公共權力並存；認同不表示必須無條件接受所有政策。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-social-content-civ-aa-{index}",
        "subject": "social",
        "type": "single-choice",
        "prompt": item["prompt"],
        "options": rotate_options(item["options"], item["answer"]),
        "knowledgeIds": [KG_ID],
        "difficulty": "medium",
        "answer": {"value": item["answer"], "explanation": item["explanation"]},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE_URL,
            "sourceLocator": (
                "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考社會科；"
                "參考公民身分、權利義務、平等、法治、公共參與與國家認同題型"
            ),
            "authoringNote": (
                "Substantive rewrite with new contexts, options, and explanations; "
                "no reproduction of public-exam wording, figures, or answer key. "
                "待第二輪 AI／Terra 內容複核。"
            ),
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }


def main():
    for index, item in enumerate(QUESTIONS, start=1):
        path = QUESTION_DIR / f"question-social-content-civ-aa-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()

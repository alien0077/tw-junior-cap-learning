#!/usr/bin/env python3
"""Replace the civ-A civic-identity and community questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "social"
LESSON_ID = "lesson-social-content-civ-a"
KG_ID = "kg-social-content-civ-a"
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
        "prompt": "小組討論班級活動時，成員來自不同家庭與社團。下列哪一種做法最能呈現多重身分認同？",
        "options": ["只准以單一身分代表自己", "承認自己同時屬於家庭、班級與社團，並依情境說明感受", "要求所有人使用相同興趣", "以家庭背景決定誰能發言"],
        "answer": "B",
        "explanation": "個人可以同時擁有多種群體歸屬，且不同情境可能凸顯不同身分；多重認同不等於只能選一種。",
    },
    {
        "prompt": "社區要規劃公共閱讀角，居民提出不同需求。哪一項最符合公民參與？",
        "options": ["由少數人決定後禁止提問", "先蒐集需求、公開討論，再依共同規則做成決議", "只採納聲音最大者的意見", "因意見不同而取消整個計畫"],
        "answer": "B",
        "explanation": "公共事務應讓受影響者有表達與討論機會，並以公開資訊與共同程序形成可檢驗的決議。",
    },
    {
        "prompt": "下列哪一項最能說明公民身分同時包含權利與責任？",
        "options": ["只享有公共服務，不必遵守規範", "可使用公共設施，也應遵守使用規則並尊重他人", "只要繳費就能排除其他人", "公共事務完全與個人無關"],
        "answer": "B",
        "explanation": "公民享有參與與使用公共資源的權利，也有遵守共同規範、尊重他人權益的責任。",
    },
    {
        "prompt": "班級想成立文化交流社團，為避免把文化簡化成刻板印象，哪一項做法較適當？",
        "options": ["只用單一代表描述整個群體", "邀請不同成員分享經驗，並說明個人經驗不代表所有人", "把傳聞當成文化規則", "禁止成員提出不同看法"],
        "answer": "B",
        "explanation": "文化群體內部具有差異，應透過多元經驗與可靠脈絡理解，不能把單一個案或傳聞推論成全體特徵。",
    },
    {
        "prompt": "某社群為新成員訂定公開且一致適用的借用規則，這項規則最主要的功能是什麼？",
        "options": ["依家庭收入決定資格", "讓成員知道權利義務與共同期待", "讓管理者可以任意改變標準", "保證所有人有完全相同的需求"],
        "answer": "B",
        "explanation": "社群規範可使成員預先知道參與條件、權利與責任；規則仍須合理且不能歧視。",
    },
    {
        "prompt": "小華同時認同學校、居住社區與喜愛的運動社團。下列哪一項推論合理？",
        "options": ["多重認同必然互相衝突", "不同認同可以並存，也可能在不同情境發揮作用", "只能保留最早形成的認同", "社群認同與個人選擇完全無關"],
        "answer": "B",
        "explanation": "個人身分認同具有多層次，群體歸屬可以並存；是否衝突要看具體情境，不能一概而論。",
    },
    {
        "prompt": "社區志工排班時，有居民因年齡被直接排除，但沒有檢查其實際能力。這種做法主要涉及哪個問題？",
        "options": ["以刻板印象取代個別判斷", "增加公共討論的證據", "保障所有人的平等參與", "建立透明且一致的資格標準"],
        "answer": "A",
        "explanation": "只依年齡推定能力，未考量個別差異，是以刻板印象做決定，也可能造成不合理的排除。",
    },
    {
        "prompt": "居民對公園改造方案意見不同，主持人要求各方提出資料、說明影響並回應他人。這種程序重視什麼？",
        "options": ["只追求快速表決", "以理由與證據進行公共討論", "讓主持人取代所有居民決定", "避免任何不同意見出現"],
        "answer": "B",
        "explanation": "公共討論不只是表達偏好，也要提出理由、證據並回應受影響者，才能形成較有品質的共同判斷。",
    },
    {
        "prompt": "新住民家庭參加社區活動時，主辦單位提供翻譯、清楚說明流程並開放提問。這最能促進什麼？",
        "options": ["以協助取代平等參與", "降低參與障礙並尊重多元身分", "要求所有家庭放棄原有文化", "只讓熟悉規則的人決定活動內容"],
        "answer": "B",
        "explanation": "提供必要資訊與溝通支持可降低參與障礙，同時保留成員表達與共同決策的權利。",
    },
    {
        "prompt": "班級分配公共器材時，採用公開登記、輪流使用與相同借用期限。這種安排主要展現哪項原則？",
        "options": ["依人際關係分配", "以透明且平等的規則處理公共資源", "由最有經驗者永久占有", "避免任何人知道分配方式"],
        "answer": "B",
        "explanation": "公開、可預期且一致適用的程序，有助於讓公共資源分配受到檢驗，也較能保障成員平等使用。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-social-content-civ-a-{index}",
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
                "參考公民身分認同、社群參與、公共討論、共同規範與平等參與題型"
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
        path = QUESTION_DIR / f"question-social-content-civ-a-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()

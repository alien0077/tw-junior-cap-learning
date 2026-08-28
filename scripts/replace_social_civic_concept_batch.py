#!/usr/bin/env python3
"""Replace the civ-AA-iv-1 civic-concept questions with originals."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "social"
LESSON_ID = "lesson-social-content-civ-aa-iv-1"
KG_ID = "kg-social-content-civ-aa-iv-1"
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
        "prompt": "下列哪一項最可能屬於公共議題，而不只是個人偏好？",
        "options": ["某人喜歡的音樂", "社區是否增設無障礙通道", "個人早餐選擇", "某人的房間布置"],
        "answer": "B",
        "explanation": "無障礙通道涉及許多人的通行權與公共資源配置，會影響共同生活，因此屬於公共議題。",
    },
    {
        "prompt": "公民概念中的「權利」較適合如何理解？",
        "options": ["任何人想做什麼都不受限制", "受到制度保障、可合理主張的利益或自由", "只有管理者才擁有的命令", "不需要考慮他人的私人願望"],
        "answer": "B",
        "explanation": "權利是受到規範與制度保障、個人可以合理主張的利益或自由；行使時仍須兼顧他人權益與公共規範。",
    },
    {
        "prompt": "下列哪一項最能表現「法治」而非「人治」？",
        "options": ["管理者可依喜好臨時改變標準", "相同規則公開適用，決定可依據規範檢驗", "有關係的人可以免除所有規定", "只要多數人同意就不必有任何程序"],
        "answer": "B",
        "explanation": "法治強調權力與人民都受公開、可預期的規範拘束，決定不能只依個人好惡或關係。",
    },
    {
        "prompt": "班級討論中，少數同學的意見沒有被採納，但仍可提出理由並被記錄。這較符合哪項民主概念？",
        "options": ["多數決不必尊重少數", "多數決與少數權利保障並存", "少數意見應被禁止", "投票後所有理由都失去意義"],
        "answer": "B",
        "explanation": "民主程序可用多數決形成決定，但也應保障少數表達、說明理由與被尊重的機會。",
    },
    {
        "prompt": "若學校分配社團經費，哪一項做法較符合公平概念？",
        "options": ["所有社團不論需求都得到完全相同金額", "公開評估共同標準與實際需求後分配", "由最受歡迎社團獨占經費", "只依負責人的私人關係決定"],
        "answer": "B",
        "explanation": "公平不一定等於每者完全相同，而是使用公開、合理且能考量需求的標準，避免任意與偏私。",
    },
    {
        "prompt": "公民社會中的團體自主運作並關心公共事務，這表示什麼？",
        "options": ["所有團體都由政府直接指揮", "人民可透過組織合作表達需求與參與公共生活", "團體可以免除所有法律責任", "只有營利組織能參與公共事務"],
        "answer": "B",
        "explanation": "公民社會提供人民自發組織、合作與表達公共關懷的空間，但團體仍須遵守合理規範。",
    },
    {
        "prompt": "某項政策可能使多數人方便，卻讓少數人承受重大不利。分析時最應先注意什麼？",
        "options": ["只計算支持者人數", "檢查政策影響、權利保障與是否有較少傷害的替代方案", "只看宣傳口號是否好聽", "因為是多數決就不必檢討"],
        "answer": "B",
        "explanation": "公共決策不能只看多數偏好，也要評估不同群體的影響、權利與比例性，尋找較合理的替代方案。",
    },
    {
        "prompt": "下列哪一項是公民責任與權利相互連結的例子？",
        "options": ["要求使用公園卻破壞設施", "享有發言機會，也負責任地以理由表達並尊重他人", "只享有投票結果，不必了解議題", "要求公共服務但拒絕遵守共同規則"],
        "answer": "B",
        "explanation": "公共參與的權利伴隨負責任表達、理解議題與尊重他人的責任，權利與責任並非互相排斥。",
    },
    {
        "prompt": "同一項公共規範若對不同群體造成不同影響，公民判讀時應如何處理？",
        "options": ["只看規範名稱就判定公平", "比較實際影響、正當目的與是否存在不合理差別待遇", "只詢問制定者的私人感受", "只要文字相同就一定沒有歧視"],
        "answer": "B",
        "explanation": "形式上相同的規則仍可能產生不同影響，應檢查目的、實際效果與差別待遇是否有合理依據。",
    },
    {
        "prompt": "面對一則主張「大家都這樣想」的公共訊息，具備公民概念的判讀方式是什麼？",
        "options": ["直接把它當成全民共識", "要求說明資料來源、代表範圍與是否存在不同意見", "只看轉發次數判斷真實性", "因為語氣肯定就不必查證"],
        "answer": "B",
        "explanation": "公共主張需要檢查資料來源、樣本或代表範圍與反面意見，不能把口號、轉發量或肯定語氣當成充分證據。",
    },
]


def build_question(index, item):
    return {
        "id": f"question-social-content-civ-aa-iv-1-{index}",
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
                "參考公民概念、公共議題、權利義務、法治、公平、民主與公民社會題型"
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
        path = QUESTION_DIR / f"question-social-content-civ-aa-iv-1-{index}.json"
        path.write_text(json.dumps(build_question(index, item), ensure_ascii=False, indent=2) + "\n")
    print(f"replaced {len(QUESTIONS)} questions for {LESSON_ID}")


if __name__ == "__main__":
    main()

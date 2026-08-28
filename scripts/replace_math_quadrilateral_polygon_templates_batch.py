#!/usr/bin/env python3
"""Replace repeated templates for special quadrilaterals and polygons."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
SOURCE_URL = (
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/"
    "114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83"
    "%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
)


UNITS = {
    "s-8-10": {
        "lesson": "lesson-math-content-s-8-10",
        "kg": "kg-math-content-s-8-10",
        "title": "正方形、長方形、箏形的基本性質",
        "items": [
            ("正方形的四邊與四角有何特徵？", ["四邊等長、四角皆為直角", "只有對邊等長", "四角皆為 60°", "只有一邊等長"], "A", "正方形具有四邊等長及四個直角。"),
            ("長方形長 9、寬 12 公分，其對角線長為何？", ["13", "15", "18", "21"], "B", "對角線=√(9²+12²)=15 公分。"),
            ("菱形兩條對角線長 10、24 公分，面積為何？", ["60", "120", "240", "340"], "B", "菱形面積=10×24÷2=120 平方公分。"),
            ("箏形的兩組鄰邊中，至少有什麼關係？", ["各組鄰邊分別等長", "兩組對邊都平行", "四邊都不等長", "四角都必為直角"], "A", "箏形有兩組鄰邊分別等長。"),
            ("正方形邊長 7 公分，周長為何？", ["14", "21", "28", "49"], "C", "周長=4×7=28 公分。"),
            ("長方形的兩條對角線有何關係？", ["等長且互相平分", "垂直但不等長", "只有一條存在", "必與邊重合"], "A", "長方形對角線等長，且互相平分。"),
            ("若一個四邊形四邊等長，但不一定有直角，最可能是哪一種？", ["菱形", "長方形", "梯形", "一般三角形"], "A", "四邊等長的平行四邊形是菱形，不必有直角。"),
            ("正方形面積為 81 平方公分，邊長為何？", ["8", "9", "18", "27"], "B", "邊長=√81=9 公分。"),
            ("下列哪項可用來判定一個平行四邊形是長方形？", ["一個內角為直角", "只有一邊較長", "兩鄰邊不等長", "一條對角線存在"], "A", "平行四邊形有一個直角，即可判定四角皆為直角，是長方形。"),
            ("箏形的一條對角線若垂直平分另一條對角線，這項性質可用於什麼？", ["判讀對角線交點與面積", "直接判定四角皆直角", "求出所有邊必相等", "判定它是三角形"], "A", "箏形對角線的垂直平分關係可協助分割面積與判讀交點。"),
        ],
    },
    "s-8-2": {
        "lesson": "lesson-math-content-s-8-2",
        "kg": "kg-math-content-s-8-2",
        "title": "凸多邊形的內角和",
        "items": [
            ("五邊形的內角和為何？", ["360°", "540°", "720°", "900°"], "B", "n 邊形內角和=(n−2)×180°，五邊形為 540°。"),
            ("六邊形的內角和為何？", ["540°", "720°", "900°", "1080°"], "B", "六邊形內角和=(6−2)×180°=720°。"),
            ("凸多邊形的外角和為何？", ["90°", "180°", "270°", "360°"], "D", "任意凸多邊形每個頂點取一外角，外角和為 360°。"),
            ("正八邊形每一個內角為何？", ["120°", "135°", "140°", "150°"], "B", "內角和=1080°，每角=1080÷8=135°。"),
            ("一個凸多邊形內角和為 900°，它有幾條邊？", ["5", "6", "7", "8"], "C", "(n−2)×180=900，n−2=5，所以 n=7。"),
            ("正六邊形每一個外角為何？", ["45°", "60°", "90°", "120°"], "B", "外角和 360°，正六邊形每角=360÷6=60°。"),
            ("四邊形有三個內角 80°、95°、105°，第四角為何？", ["70°", "80°", "90°", "100°"], "B", "四邊形內角和 360°，第四角=360−80−95−105=80。"),
            ("從一個頂點連結凸七邊形的對角線，可將其分成幾個三角形？", ["4 個", "5 個", "6 個", "7 個"], "B", "從一頂點可分成 n−2=5 個三角形。"),
            ("正多邊形的所有外角有何關係？", ["皆相等", "皆互為補角", "一半相等", "一定為直角"], "A", "正多邊形各邊、各角相等，因此各外角也相等。"),
            ("若凸多邊形邊數增加 1，內角和增加多少？", ["90°", "180°", "270°", "360°"], "B", "內角和公式每增加一邊，增加一個三角形，故增加 180°。"),
        ],
    },
}


def build_question(unit, index, item):
    prompt, options, answer, explanation = item
    config = UNITS[unit]
    return {
        "id": f"question-math-content-{unit}-{index}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(ord("A") + i), "text": text} for i, text in enumerate(options)],
        "knowledgeIds": [config["kg"]],
        "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE_URL,
            "sourceLocator": (
                "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；"
                f"參考 {config['title']} 題型與官方課綱 KG {config['kg']}"
            ),
            "authoringNote": (
                "Substantive rewrite with new values, contexts, options, and explanations; "
                "no reproduction of public-exam wording, figures, or answer key. "
                "待第二輪 AI／Terra 內容複核。"
            ),
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-29",
        "lessonId": config["lesson"],
    }


def main():
    count = 0
    for unit, config in UNITS.items():
        for index, item in enumerate(config["items"], start=1):
            path = QUESTION_DIR / f"question-math-content-{unit}-{index}.json"
            path.write_text(json.dumps(build_question(unit, index, item), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            count += 1
    print(f"replaced {count} quadrilateral/polygon template questions")


if __name__ == "__main__":
    main()

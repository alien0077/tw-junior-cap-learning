import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf", "高雄市立鹽埕國民中學公開英文段考", "comparison, cultural context, and reading inference"),
    ("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw", "新北市立北投國民中學公開定期評量試題頁", "short texts, social conventions, and supported comparison"),
    ("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php", "新北市立新埔國民中學公開段考試題頁", "functional language, cultural situations, and inference"),
]

DATA = [
    ("greeting comparison", "Text A says people often bow slightly when greeting. Text B says people commonly shake hands. What difference is directly stated?", ["The two texts describe different common greeting actions.", "One text says people never greet anyone.", "Both texts require the same greeting action.", "The texts compare only their weather."], "A", "Text A describes a slight bow and Text B describes a handshake, so the supported difference concerns greeting actions."),
    ("meal etiquette", "At a meal, one family waits until everyone has food before eating. Another family begins when each person is served. What is a fair comparison?", ["The families follow different starting customs at meals.", "One family does not care about food.", "The families must dislike each other.", "Neither family eats together."], "A", "The passages describe different moments for starting a meal; they do not support assumptions about feelings or relationships."),
    ("time convention", "A visitor reads: 'In Town X, arriving ten minutes early is polite. In Town Y, guests usually arrive at the agreed time.' What can be concluded?", ["The texts present different expectations about arrival time.", "People in Town Y never make appointments.", "Being early is always rude everywhere.", "The towns use different clocks."], "A", "The stated expectations differ, but the text does not say that either practice is universally right or wrong."),
    ("gift giving", "In one community, gifts are opened immediately. In another, people wait until the guest leaves. Which response is most respectful when visiting?", ["Learn the host's custom and follow it rather than assuming your own way.", "Open every gift immediately to show confidence.", "Refuse all gifts from every community.", "Tell the host that only one custom is acceptable."], "A", "Asking or observing the host's custom avoids imposing one practice and shows cultural respect."),
    ("public behavior", "A guide says silence is expected on a train in Place A, while quiet conversation is acceptable in designated areas in Place B. What is the safest action?", ["Check the local notice and adjust your voice to the place.", "Speak loudly in both places.", "Assume every train has the same rule.", "Ignore other passengers and play music."], "A", "The two rules differ by place, so reading the local notice and adjusting behavior is the respectful choice."),
    ("family activity", "A comparison chart shows that families in Region P often share a large weekend lunch, while families in Region Q often meet for an evening walk. Which statement is supported?", ["The chart gives different common family activities in the two regions.", "Every family in P eats lunch together every weekend.", "Families in Q never eat together.", "The regions have no family traditions."], "A", "The chart supports a comparison of common activities, not an absolute claim about every family."),
    ("language and politeness", "A student notices that a direct request is normal among close friends in one setting but a soft phrase such as 'Could you...' is expected with elders. What should the student learn?", ["Relationship and setting can affect how a request is phrased.", "Direct requests are always impolite.", "Soft phrases have no meaning.", "Age never affects communication."], "A", "The example shows that audience and setting can influence the level of politeness used in a request."),
    ("similarity with difference", "Place A and Place B both have a spring family gathering, but Place A serves rice cakes and Place B serves sweet bread. What is the best comparison?", ["They share a seasonal family gathering but have different traditional foods.", "They have no similar activity at all.", "Their foods must taste exactly the same.", "Only Place B has families."], "A", "The comparison preserves both the similarity in the gathering and the difference in food."),
    ("avoid judgment", "A classmate says, 'Their custom is strange because it is not ours.' Which reply encourages fair comparison?", ["It is different from ours; let's learn when people use it and what it means to them.", "Yes, unfamiliar customs are always wrong.", "We should copy it without learning anything.", "No custom can ever be discussed."], "A", "The reply separates unfamiliarity from wrongness and asks for context and meaning instead of judging."),
    ("integrated comparison", "A table lists greetings, meal starts, and public voice levels for two places. Which study note is most accurate?", ["Place A and Place B differ in several practices, so visitors should check local expectations in each situation.", "One place has no culture because its rules differ.", "All three practices are identical in both places.", "A single custom tells us everything about every person there."], "A", "The note summarizes several differences and draws the practical lesson to check context without stereotyping every person."),
]


def make(index, row):
    topic, prompt, choices, answer, explanation = row
    options = [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)]
    refs = [{
        "url": url, "title": f"{title}；僅取文化比較與情境閱讀能力方向，未複製原題、選項、圖表或答案。",
        "year": "113-114", "subject": "english", "locator": locator,
        "observedPattern": "公開英文評量常透過兩地生活情境、短文與對話測量相同點、差異、合宜回應、推論及避免過度概括；本題為獨立改寫。",
        "reuseDecision": "pattern-only", "status": "recorded", "locatorLevel": "paper",
    } for url, title, locator in SOURCES]
    steps = [
        f"Read both cultural descriptions and identify the comparison focus: {topic}.",
        "Make two columns for the places, recording only the stated practice, audience, time, or setting.",
        f"Check whether the choice states a supported similarity or difference; the correct answer is {answer}.",
        f"Use the passage rather than personal preference: {explanation}",
        "Reject stereotypes and value judgments; explain how the comparison can guide respectful behavior in a real situation.",
    ]
    return {
        "id": f"question-english-content-c-iv-3-{index}", "subject": "english", "type": "single-choice", "prompt": prompt,
        "options": options, "knowledgeIds": ["kg-english-content-c-iv-3"], "difficulty": "medium",
        "answer": {"value": answer, "explanation": explanation + f" Correct answer: {answer}"},
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCES[0][0],
            "sourceLocator": "Public-school English assessment materials; this item studies cultural comparison and respectful contextual reading patterns only and does not reproduce an original question, option, image, or answer.",
            "authoringNote": "Written independently from the official English curriculum KG and three public-school English assessment sources; comparisons, options, explanations, and transfer task are original; pending second-round AI/Terra content review."},
        "reviewStatus": "draft", "updatedAt": "2026-09-09", "lessonId": "lesson-english-content-c-iv-3", "examPatternRefs": refs,
        "solutionStrategy": "Separate the two settings, map their stated practices, and select a comparison supported by the text while avoiding stereotypes or treating one custom as universally correct.", "solutionSteps": steps,
    }


for index, row in enumerate(DATA, 1):
    (OUT / f"question-english-content-c-iv-3-{index}.json").write_text(json.dumps(make(index, row), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"rewrote {len(DATA)} questions")

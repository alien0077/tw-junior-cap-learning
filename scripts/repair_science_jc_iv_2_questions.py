import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('燃燒三要素', '物質要持續燃燒，通常需要哪三項條件？', ['可燃物、助燃物與達到著火溫度', '水、二氧化碳與低溫', '只有燃料而不需氧氣', '光線、聲音與磁場'], '可燃物、助燃物與達到著火溫度', '燃燒需有可燃物、助燃物（常為氧氣）及足以開始反應的溫度，缺一通常無法持續。'),
('滅火原理', '用濕抹布覆蓋小火焰能滅火，主要是？', ['隔絕空氣並帶走熱量，使燃燒條件被破壞', '增加可燃物供應', '讓火焰獲得更多氧氣', '使燃料變成助燃物'], '隔絕空氣並帶走熱量，使燃燒條件被破壞', '滅火是移除燃燒三要素之一或使溫度降至著火點以下，不是把火焰推走。'),
('氧化判斷', '鐵在潮濕空氣中生鏽，最適當的分類是？', ['鐵與氧等物質反應形成新物質，屬於氧化相關的化學變化', '鐵只發生形狀改變', '鐵被水完全溶解成氧氣', '這一定是物理熔化'], '鐵與氧等物質反應形成新物質，屬於氧化相關的化學變化', '生鏽產生與原物質不同的鐵氧化物，屬於氧化相關化學變化，水分通常會影響速率。'),
('助燃性', '將燃燒中的木條伸入氧氣較充足的環境，可能觀察到？', ['燃燒變得較旺，因為氧氣是常見助燃物', '氧氣一定使所有物質立刻爆炸', '氧氣會使火焰完全消失', '木條質量一定增加而不產生氣體'], '燃燒變得較旺，因為氧氣是常見助燃物', '氧氣本身通常不作為燃料，但可助燃；實際現象仍受濃度、材料與溫度影響。'),
('質量變化', '在開放空間燃燒鎂帶後，固體產物質量可能增加，主要因為？', ['鎂與空氣中的氧結合，氧原子進入固體產物', '燃燒使鎂創造新的質量', '氧氣被完全消滅且不進入產物', '質量增加只由光線造成'], '鎂與空氣中的氧結合，氧原子進入固體產物', '氧化反應會使反應物與氧結合；開放系統中有氣體從環境進入，固體質量可能增加。'),
('密閉系統', '若在密閉容器中測量燃燒前後總質量，理想情況下應？', ['總質量近似守恆，但物質組成與能量狀態改變', '總質量必然增加一倍', '燃燒後所有物質消失', '密閉容器中不可能發生反應'], '總質量近似守恆，但物質組成與能量狀態改變', '密閉系統可觀察質量守恆；燃燒是化學反應，物質重新組合並可能放出能量。'),
('氧化還原', '燃燒時可燃物與氧氣反應，較適當的概念描述是？', ['可燃物被氧化，氧氣參與反應並可能被還原', '只有氧氣發生物理位移', '燃燒不涉及電子或物質轉換', '氧氣一定是燃料'], '可燃物被氧化，氧氣參與反應並可能被還原', '氧化還原可用得氧失氧或電子轉移理解；燃燒通常是快速氧化反應。'),
('實驗控制', '比較不同燃料的燃燒時間，哪項設計較公平？', ['固定燃料質量、容器、氧氣供應與點火方式，只更換燃料種類', '同時改變燃料質量、容器與燃料種類', '只憑火焰顏色判斷時間', '先選最快燃料再挑資料'], '固定燃料質量、容器、氧氣供應與點火方式，只更換燃料種類', '燃燒時間受質量、供氧、容器與點火方式影響，需控制非研究變因並重複測量。'),
('安全操作', '酒精燈火焰失控時，較適當的處理是？', ['用燈帽蓋熄並依實驗室規範處理，不直接用嘴吹', '拿燃燒中的燈移動奔跑', '直接用手抓火焰', '再添加酒精讓火焰穩定'], '用燈帽蓋熄並依實驗室規範處理，不直接用嘴吹', '燃燒實驗需隔絕空氣並遵守器材安全規範；直接吹或搬動燃燒器材可能擴大火勢。'),
('證據界線', '燃燒後出現新固體與氣體，最嚴謹的結論是？', ['觀察支持發生化學反應並產生新物質，仍需分析成分才能確定反應式', '只要出現火焰就能知道所有產物', '可直接證明反應沒有氧氣參與', '新物質一定只有一種'], '觀察支持發生化學反應並產生新物質，仍需分析成分才能確定反應式', '新物質是化學變化的重要證據，但要判斷產物種類與完整反應式仍需更多測量。'),
]
TARGET_ANSWERS = "ABCDBCDACB"

def make(i, row):
    tag, prompt, opts, answer, reason = row
    target = TARGET_ANSWERS[i - 1]
    position = ord(target) - 65
    distractors = [t for t in opts if t != answer]
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」與題目中的燃料、氧氣、溫度、質量或安全條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合燃燒與氧化概念。', '排除誘答：分清可燃物、助燃物與氧化劑、開放與密閉系統，以及觀察證據與完整產物分析。', '最後回查：確認反應條件、質量系統邊界與安全操作都和題幹一致。']
    return {'id': f'question-science-content-jc-iv-2-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-2'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究燃燒三要素、氧化還原、質量守恆、實驗控制與安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-2', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '燃燒實驗認識氧化', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先檢查燃燒三要素，再判斷氧化、質量系統邊界、控制變因與安全操作。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-2-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

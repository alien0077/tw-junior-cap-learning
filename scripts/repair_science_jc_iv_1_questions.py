import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('得氧氧化', '物質在反應中得到氧，依傳統定義屬於？', ['氧化', '還原', '中和且不涉及氧', '物理凝固'], '氧化', '以得氧判斷時，物質與氧結合屬氧化；現代觀點也可用電子轉移描述。'),
('失氧還原', '氧化銅被碳加熱還原成銅時，氧化銅的變化是？', ['失去氧，發生還原', '得到氧，發生氧化', '只發生熔化', '沒有物質改變'], '失去氧，發生還原', '氧化銅失去氧成為銅，依得氧失氧定義是還原；碳則取得氧形成含氧產物。'),
('同時發生', '氧化還原反應的核心特徵是？', ['一種物質氧化的同時，另一種物質通常被還原', '所有物質都只得氧', '反應只改變物理狀態', '氧化與還原不可能同時出現'], '一種物質氧化的同時，另一種物質通常被還原', '氧化還原是成對過程，電子或氧的轉移需在反應物之間配合。'),
('氧化劑', '在氧化銅被碳還原的反應中，氧化銅較接近扮演？', ['氧化劑，提供氧並使碳被氧化', '還原劑，只失去氧', '催化劑且完全不改變', '溶劑'], '氧化劑，提供氧並使碳被氧化', '氧化劑使別的物質氧化，自己則被還原；氧化銅提供氧並失去氧。'),
('還原劑', '若某物質能使另一物質失去氧，自己同時得到氧，這物質稱為？', ['還原劑', '氧化劑', '指示劑', '沉澱劑'], '還原劑', '還原劑使別的物質還原，自己通常被氧化；得氧失氧定義可直接判斷此角色。'),
('金屬生鏽', '鐵在潮濕空氣中生鏽，可用得氧失氧觀點描述為？', ['鐵與氧結合而被氧化', '鐵失去氧而被還原', '鐵只發生物理切割', '水分一定是還原劑且不含氧'], '鐵與氧結合而被氧化', '生鏽包含鐵與氧及水分等因素的化學變化，鐵得到氧可視為氧化。'),
('方程式判讀', '反應 2Mg + O₂ → 2MgO 中，鎂的角色與變化是？', ['鎂得到氧而被氧化', '鎂失去氧而被還原', '鎂是催化劑不變', '鎂只發生狀態改變'], '鎂得到氧而被氧化', '鎂與氧形成氧化鎂，依得氧定義鎂被氧化；氧則參與形成氧化物。'),
('電子觀點', '從電子轉移觀點看，物質失去電子通常稱為？', ['氧化', '還原', '沉澱', '溶解'], '氧化', '現代氧化定義常用失電子，還原則為得電子；兩者在反應中成對發生。'),
('實驗證據', '判斷加熱後氧化物是否被還原，哪項證據較有力？', ['分析反應前後物質組成與含氧狀態，而非只看顏色', '只看火焰亮度', '只看容器大小', '先選結論再挑照片'], '分析反應前後物質組成與含氧狀態，而非只看顏色', '顏色可提供線索但不一定唯一；組成、質量與氣體產物等證據較能支持得氧失氧判斷。'),
('控制變因', '比較不同還原劑還原氧化銅的效果，較公平的實驗應？', ['固定氧化銅質量、加熱條件與時間，只改變還原劑並分析產物', '同時改變氧化銅質量、溫度與還原劑', '只觀察火焰顏色一次', '先決定最有效還原劑再挑資料'], '固定氧化銅質量、加熱條件與時間，只改變還原劑並分析產物', '需控制反應物量與加熱條件，並以產物組成或含氧狀態作為可檢驗指標。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的得氧、失氧、電子或反應物角色。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合氧化還原定義。', '排除誘答：分清氧化與還原、氧化劑與還原劑、化學變化與物理變化，並檢查反應是否成對。', '最後回查：確認證據、方程式與控制變因足以支持結論，沒有只靠顏色或單一現象推論。']
    return {'id': f'question-science-content-jc-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究得氧失氧、氧化還原、氧化劑還原劑與反應判讀的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '氧化還原的得氧與失氧定義', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先用得氧失氧判斷，再以電子觀點與氧化劑／還原劑角色交叉核對。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

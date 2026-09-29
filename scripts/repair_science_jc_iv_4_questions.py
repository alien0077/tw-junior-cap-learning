import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8期第一次段考三年級自然.pdf'
# The URL above is normalized below so the source remains readable in generated records.
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('氧化還原', '某物質在反應中失去電子，應判定為？', ['被氧化', '被還原', '只發生物態變化', '沒有發生化學變化'], '被氧化', '失去電子是氧化，得到電子是還原；兩者通常在同一氧化還原反應中成對發生。'),
('金屬置換', '鋅片放入硫酸銅溶液後，若生成銅並有鋅離子進入溶液，較合理的描述是？', ['鋅被氧化、銅離子被還原', '鋅被還原、銅被氧化', '兩種金屬都沒有電子轉移', '只有水發生物理變化'], '鋅被氧化、銅離子被還原', '鋅失去電子形成鋅離子，銅離子得到電子析出銅，呈現置換型氧化還原。'),
('還原劑角色', '在金屬置換反應中，能提供電子給另一物種的物質通常是？', ['還原劑，自己被氧化', '氧化劑，自己被還原', '催化劑且不改變', '溶劑'], '還原劑，自己被氧化', '還原劑使另一物種得到電子而被還原，自己則失去電子而被氧化。'),
('腐蝕防護', '在鐵表面塗漆可減緩生鏽，主要是因為？', ['隔絕水與氧氣，降低腐蝕反應接觸機會', '讓鐵失去所有電子', '使鐵變成不含原子的物質', '增加鐵與氧氣接觸面積'], '隔絕水與氧氣，降低腐蝕反應接觸機會', '鐵鏽形成通常需要水與氧等條件；塗層可隔離環境，但破損處仍可能腐蝕。'),
('犧牲陽極', '以較活潑金屬連接並保護鐵製品，可能利用哪項原理？', ['較活潑金屬優先失去電子被氧化，降低鐵被氧化的機會', '較不活潑金屬優先被還原且完全不反應', '讓鐵獲得更多氧氣', '使腐蝕反應變成物理熔化'], '較活潑金屬優先失去電子被氧化，降低鐵被氧化的機會', '犧牲陽極提供較容易被氧化的材料，保護目標金屬；實際效果也受電解質與接觸狀況影響。'),
('漂白作用', '某些漂白劑能使有色物質褪色，可能涉及？', ['氧化有色分子，使其結構或吸收光的特性改變', '把顏料全部變成重力', '只改變溶液體積', '一定只是過濾作用'], '氧化有色分子，使其結構或吸收光的特性改變', '漂白可能透過氧化破壞發色結構；不同漂白劑機制與安全性不同，不能任意混用。'),
('呼吸氧化', '細胞利用氧氣分解養分並釋放能量，從氧化還原角度可描述為？', ['養分被氧化，氧氣作為電子接受者被還原', '養分與氧氣都被還原', '只有水發生氧化', '完全沒有電子轉移'], '養分被氧化，氧氣作為電子接受者被還原', '細胞呼吸是分階段的氧化還原過程，養分電子逐步轉移至最終接受者。'),
('電子判讀', '在反應中某元素氧化數上升，通常代表？', ['該元素被氧化，失去電子的傾向增加', '該元素被還原且得到電子', '該元素只發生溶解', '反應必然不是化學反應'], '該元素被氧化，失去電子的傾向增加', '氧化數上升常用來判斷氧化，下降則常用來判斷還原；需配合完整反應式。'),
('實驗證據', '比較兩種防鏽方法時，哪項設計較能支持結論？', ['固定鐵片材質、表面積、時間與環境，只改變防護方法並量化鏽蝕程度', '同時改變鐵片大小、時間與防護材料', '只憑肉眼看一次顏色', '先決定最好方法再選照片'], '固定鐵片材質、表面積、時間與環境，只改變防護方法並量化鏽蝕程度', '防鏽比較要控制腐蝕條件並使用可重複、可量化的指標，避免主觀判讀。'),
('混合安全', '使用氧化性清潔劑時，哪項做法較適當？', ['依標示使用，避免與未知或還原性清潔劑混合並保持通風', '任意混合以增加氧化力', '用密閉容器加熱混合物', '直接用手測試反應'], '依標示使用，避免與未知或還原性清潔劑混合並保持通風', '氧化還原混合可能快速放熱或產生有害物質，應遵守標示與安全規範。'),
]

TARGET_ANSWERS = 'ABCDBCDACB'

def make(i, row):
    tag, prompt, opts, answer, reason = row
    target = TARGET_ANSWERS[i - 1]
    correct_index = opts.index(answer)
    distractors = [text for index, text in enumerate(opts) if index != correct_index]
    position = ord(target) - 65
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': text} for j, text in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」與題目中的電子、氧化數、金屬、氧氣或防護條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合氧化還原與生活應用。', '排除誘答：分清氧化與還原、氧化劑與還原劑、腐蝕防護與漂白機制，並檢查安全限制。', '最後回查：確認反應角色、控制變因與證據強度都和題幹一致。']
    return {'id': f'question-science-content-jc-iv-4-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-4'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究常見氧化還原反應、金屬腐蝕、防護、漂白與生活應用的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-4', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '常見氧化還原反應與應用', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先追蹤電子轉移判斷氧化還原角色，再連結腐蝕、漂白與實驗控制及安全。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-4-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

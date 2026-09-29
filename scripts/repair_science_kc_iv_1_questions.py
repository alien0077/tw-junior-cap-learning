import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
TARGET_ANSWERS = 'BCADBCADCB'
DATA = [
('摩擦起電', '兩種不同材料互相摩擦後能吸引輕小紙屑，最合理的解釋是？', ['電子重新分布或轉移，使物體帶有淨電荷', '摩擦使物體產生新的質子', '紙屑被重力變成帶電物', '物體溫度升高就必然帶正電'], '電子重新分布或轉移，使物體帶有淨電荷', '摩擦起電主要涉及電子轉移或重新分布，原子核中的質子不會因一般摩擦離開物體。'),
('電荷守恆', '摩擦起電後一物體帶正電、另一物體帶負電，較合理的描述是？', ['電子從一物體轉移到另一物體，總電荷仍近似守恆', '摩擦創造了等量正負質子', '兩物體都失去所有電子', '正電荷會自行消失'], '電子從一物體轉移到另一物體，總電荷仍近似守恆', '摩擦可使電子由一方移到另一方，電荷重新分配而非無中生有。'),
('同種相斥', '兩個帶同種電荷的物體靠近時，通常會？', ['互相排斥', '互相吸引', '完全沒有作用力', '其中一個必然變成中性'], '互相排斥', '靜電作用的基本規則是同種電荷相斥、異種電荷相吸。'),
('異種相吸', '帶正電的棒靠近帶負電的球，通常觀察到？', ['兩物體互相吸引', '兩物體互相排斥', '電荷必然都變成正電', '只有球受到力而棒不受力'], '兩物體互相吸引', '異種電荷產生吸引作用；依作用力與反作用力，兩物體都受到大小相等方向相反的力。'),
('中性導體感應', '帶電棒靠近但未接觸中性金屬球，金屬球內部可能發生？', ['自由電子重新分布，靠近端呈現較有利於吸引的電性', '金屬球所有電子消失', '金屬球必然獲得同量淨電荷', '金屬球質量改變'], '自由電子重新分布，靠近端呈現較有利於吸引的電性', '導體中的自由電子可移動，外加電荷會造成感應極化；未接觸時不代表一定產生淨電荷。'),
('驗電器', '帶電物體接觸驗電器金屬球後，金屬箔片張開主要表示？', ['電荷在導體上分布，使同種電荷的箔片互相排斥', '箔片因重力變輕', '驗電器產生了所有電荷', '金屬箔片受到磁力必然張開'], '電荷在導體上分布，使同種電荷的箔片互相排斥', '接觸後電荷可在導體上分布，兩片箔帶同種電荷而互相排斥。'),
('導體絕緣體', '下列哪項最能區分導體與絕緣體在靜電實驗中的差異？', ['導體的自由電子較易移動，絕緣體的電荷較局部', '絕緣體一定沒有任何電子', '導體不能帶電', '兩者只差在顏色'], '導體的自由電子較易移動，絕緣體的電荷較局部', '導體與絕緣體都由帶電粒子組成，差別在電荷移動的容易程度。'),
('濕度影響', '相同材料摩擦後在潮濕環境較不易保留靜電，可能原因是？', ['水分增加表面漏電與電荷移動的機會', '潮濕使電子不存在', '水分把所有正電變成重力', '濕度只影響物體顏色'], '水分增加表面漏電與電荷移動的機會', '表面水分可能提高導電與漏電，讓摩擦後累積的電荷較快散去；仍需控制材料與摩擦方式。'),
('實驗控制', '比較兩種布料摩擦起電效果，哪項設計較公平？', ['固定摩擦次數、力度、環境與被摩擦物，只更換布料', '同時更換摩擦次數、力度與布料', '只看吸引紙屑的主觀印象', '先知道結果再挑選觀察'], '固定摩擦次數、力度、環境與被摩擦物，只更換布料', '摩擦起電受材料、接觸面、次數、力度與濕度影響，需控制條件才能比較。'),
('證據界線', '帶電棒吸引中性紙屑，最嚴謹的結論是？', ['觀察到靜電作用或極化造成的吸引，不能僅由此判定紙屑帶相反淨電荷', '紙屑一定原本帶相反電荷', '可證明所有中性物體都不受力', '吸引必然來自磁力'], '觀察到靜電作用或極化造成的吸引，不能僅由此判定紙屑帶相反淨電荷', '中性物體也可能因極化受到吸引，單一吸引現象不足以判定其原有淨電荷。'),
]

def make(i, row):
    tag, prompt, opts, answer, reason = row
    correct_index = opts.index(answer)
    distractors = [text for index, text in enumerate(opts) if index != correct_index]
    target = TARGET_ANSWERS[i - 1]
    position = ord(target) - 65
    arranged = distractors[:position] + [answer] + distractors[position:]
    options = [{'id': chr(65+j), 'text': t} for j, t in enumerate(arranged)]
    aid = target
    steps = [f'讀題定位：圈出「{tag}」與題目中的材料、接觸方式、電荷或環境條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合靜電與電荷模型。', '排除誘答：分清電子轉移與質子、同種相斥與異種相吸、淨電荷與極化。', '最後回查：確認實驗比較有控制摩擦與環境條件，且結論沒有超出觀察證據。']
    return {'id': f'question-science-content-kc-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-kc-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason + f' 正確答案為選項 {aid}：「{answer}」。'}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究摩擦起電、正負電荷、靜電感應、導體與驗電器的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-13', 'lessonId': 'lesson-science-content-kc-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '摩擦生靜電與正負電荷', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先判斷電子移動與電荷守恆，再分辨相斥、相吸、極化與控制變因。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-kc-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

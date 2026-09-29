import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('波速計算', '一列波的頻率為 5 Hz、波長為 2 m，波速是多少？', ['10 m/s', '2.5 m/s', '7 m/s', '0.4 m/s'], '10 m/s', '波速 v=fλ=5×2=10 m/s；頻率表示每秒振動次數，波長表示相鄰同相位點距離。'),
('波長定義', '波長最適合定義為什麼？', ['相鄰兩個同相位點之間的距離，例如波峰到下一個波峰', '波峰到相鄰波谷的垂直高度', '一秒內完成的振動次數', '波動離開介質的總時間'], '相鄰兩個同相位點之間的距離，例如波峰到下一個波峰', '波長是空間週期，可由相鄰波峰、相鄰波谷等同相位點間的距離表示；波峰到波谷是半個波長的水平間隔。'),
('頻率週期', '某波每秒完成 4 次完整振動，頻率與週期分別是多少？', ['4 Hz、0.25 s', '0.25 Hz、4 s', '4 s、0.25 Hz', '0.25 s、4 Hz'], '4 Hz、0.25 s', '頻率 f=4 Hz，週期 T=1/f=0.25 s；頻率與週期互為倒數。'),
('振幅判讀', '在頻率與波長相同的兩列波中，甲的振幅較大，通常代表什麼？', ['介質振動的最大位移較大，傳遞能量可能較多，但波速不必因此改變', '甲的頻率一定較高', '甲的波長一定較長', '甲不再需要介質'], '介質振動的最大位移較大，傳遞能量可能較多，但波速不必因此改變', '振幅是平衡位置到波峰或波谷的最大位移；在相同介質與條件下，振幅改變不必改變頻率、波長或波速。'),
('波峰波谷', '在橫波圖上，平衡位置上方最高點與下方最低點分別稱為？', ['波峰與波谷', '波谷與波峰', '波長與週期', '振幅與頻率'], '波峰與波谷', '波峰是相對平衡位置的最高點，波谷是最低點；振幅是平衡位置到其中一點的最大垂直距離。'),
('介質與波速', '同一列機械波進入不同介質後，若介質性質改變，最可能如何？', ['波速可能改變，頻率由波源決定而通常維持，波長隨之調整', '波速、頻率與波長永遠全部不變', '只有振幅可以存在，其他量消失', '波會變成電磁波'], '波速可能改變，頻率由波源決定而通常維持，波長隨之調整', '跨介質時波源頻率通常維持，介質決定波速，依 v=fλ 關係波長會改變；機械波仍需要介質。'),
('圖表判讀', '若在同一介質中逐漸提高波源頻率，波速近似固定，波長應如何變化？', ['波長變短，因為 λ=v/f', '波長變長，因為 λ=vf', '波長不變且波速變零', '波長與頻率完全無關'], '波長變短，因為 λ=v/f', '同一介質中 v 近似固定，頻率增加時 λ=v/f 變小；不能把頻率與波長同向增加。'),
('實驗設計', '用繩波研究頻率對波長的影響，哪項設計較公平？', ['固定繩張力、繩材與波源振幅，只改變頻率並量測波長', '同時改變張力、繩長、頻率與振幅', '只用目測比較波形一次', '先選出符合公式的波長'], '固定繩張力、繩材與波源振幅，只改變頻率並量測波長', '要研究頻率效應，繩的張力與材料會影響波速，應固定它們，再量測不同頻率下的波長。'),
('單位換算', '波長 50 cm、頻率 6 Hz，若先將波長換成公尺，波速是多少？', ['3.0 m/s', '300 m/s', '0.083 m/s', '12 m/s'], '3.0 m/s', '50 cm=0.50 m；v=fλ=6×0.50=3.0 m/s，先統一長度單位可避免千倍錯誤。'),
('證據界線', '下列哪項最符合波動量研究的判讀？', ['用 v=fλ 串連波速、頻率與波長，並說明介質、振幅、單位與測量誤差條件', '只看波峰高度就能決定波速', '頻率越大所有介質波速必定越大', '一次波形照片就能推論所有波動'], '用 v=fλ 串連波速、頻率與波長，並說明介質、振幅、單位與測量誤差條件', '波動量的關係式要配合介質與量測條件，振幅不等同波速；結論需揭露單位、誤差與適用範圍。'),
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
    steps = [f'讀題定位：圈出「{tag}」以及頻率、週期、波長、振幅、介質或單位。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合波動量定義或 v=fλ 關係。', '排除誘答：分清頻率與週期、波長與振幅、波速與振動速度，並先統一單位。', '最後回查：確認介質、控制變因、公式代入與測量誤差都沒有被忽略。']
    return {'id': f'question-science-content-ka-iv-1-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ka-iv-1'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究波峰、波谷、波長、頻率、週期、波速、振幅與波動實驗的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ka-iv-1', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '波峰、波谷、波長、頻率、波速與振幅', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先辨識波動量定義與單位，再用 f=1/T、v=fλ 或圖形關係計算，最後檢查介質與控制變因。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ka-iv-1-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

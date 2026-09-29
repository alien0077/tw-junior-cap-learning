import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('放電能量', '化學電池放電時，主要的能量轉換為？', ['化學能轉換成電能，並伴隨部分熱等損耗', '電能直接創造化學物質而無反應', '聲音能量變成質量', '重力能量必然變成光'], '化學能轉換成電能，並伴隨部分熱等損耗', '放電時自發氧化還原反應提供電子流，化學能轉為電能；實際還有內阻造成的能量損耗。'),
('充電能量', '可充電電池充電時，外加電能主要用來？', ['推動較不自發的反應，使化學能重新儲存', '讓所有電子消失', '把熱能直接變成質量', '使電池永遠不會老化'], '推動較不自發的反應，使化學能重新儲存', '充電利用外加電能逆向推動部分電化學反應，能量以化學形式儲存，但效率與壽命有限。'),
('反應方向', '同一可充電電池放電與充電時，電極反應方向通常？', ['大致相反，但電池內部材料與條件會影響可逆程度', '永遠完全相同且不需外加能量', '充電時沒有任何氧化還原', '只由外殼顏色決定'], '大致相反，但電池內部材料與條件會影響可逆程度', '充電需逆轉部分放電反應；實際電池可能有副反應與不可逆變化。'),
('電壓曲線', '電池放電一段時間後端電壓逐漸下降，可能表示？', ['反應物消耗、內阻或濃度條件改變，使輸出能力降低', '電子被永久消滅', '電池一定還能無限輸出相同電流', '電壓下降代表化學能增加'], '反應物消耗、內阻或濃度條件改變，使輸出能力降低', '放電曲線受反應物、內阻、負載與溫度等因素影響，不能只歸因於一個機制。'),
('可逆與不可逆', '一次電池不適合反覆充電，主要可能因為？', ['放電反應包含不可逆變化或充電時產生副反應與安全風險', '一次電池完全沒有化學能', '所有電子都不能移動', '充電只會讓外殼變色'], '放電反應包含不可逆變化或充電時產生副反應與安全風險', '可逆性取決於電極、電解質與反應設計；不適用的電池強行充電可能漏液、發熱或損壞。'),
('內阻影響', '接上較大電流負載時，電池端電壓可能下降，主要可用哪項解釋？', ['內阻造成電流通過時的電壓損失', '負載使電池質量變成零', '電流越大內阻必然消失', '端電壓只由導線顏色決定'], '內阻造成電流通過時的電壓損失', '實際電池可視為理想電壓源與內阻，電流增加時內部壓降可能更明顯。'),
('充電效率', '充電輸入的電能通常大於之後可取出的電能，可能因為？', ['部分能量轉成熱、聲音或副反應，存在能量損耗', '能量守恆在電池中失效', '電能全部消失沒有任何形式', '充電一定創造更多能量'], '部分能量轉成熱、聲音或副反應，存在能量損耗', '實際充放電有電阻與副反應，效率不會達到理想的百分之百。'),
('測量設計', '比較兩種電池的放電壽命，哪項條件應固定？', ['負載電阻、初始充電狀態、溫度、測量頻率與截止電壓', '每種電池使用不同負載且不記錄', '只比較外觀大小', '先決定壽命再挑測量時間'], '負載電阻、初始充電狀態、溫度、測量頻率與截止電壓', '放電壽命取決於負載與判定標準，需固定相關條件才能比較電池本身差異。'),
('安全操作', '替可充電電池充電時，最重要的原則是？', ['使用相容充電器與規定電流電壓，避免短路、過熱與損壞電池', '用更高電壓可保證更安全', '把電池刺穿檢查內部', '將不同規格電池任意並聯充電'], '使用相容充電器與規定電流電壓，避免短路、過熱與損壞電池', '充電條件需符合電池規格；過充、短路或過熱可能造成損壞與安全事故。'),
('證據界線', '充電後電池可再次點亮燈泡，最嚴謹的結論是？', ['在該次條件下電池恢復部分可輸出能量，不能推論容量與壽命完全恢復', '電池已恢復成全新狀態', '所有一次電池都能安全充電', '充電效率必然是百分之百'], '在該次條件下電池恢復部分可輸出能量，不能推論容量與壽命完全恢復', '重新輸出只支持部分功能恢復；完整容量、循環壽命與安全性需長期、多次測試。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的放電、充電、負載、電壓、能量或安全條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合電池放電／充電模型。', '排除誘答：分清化學能與電能、可逆與不可逆、端電壓與容量，以及理想模型與實際損耗。', '最後回查：確認電池規格、測量條件與證據範圍都和題幹一致。']
    return {'id': f'question-science-content-jc-iv-6-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-6'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究化學電池放電與充電、能量轉換、內阻、效率與安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-6', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '化學電池的放電與充電', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先分辨放電與充電的能量方向，再檢查電極反應、內阻、效率、負載與安全條件。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-6-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('電解定義', '電解是指利用外加電能使什麼發生？', ['原本不易自發的氧化還原反應', '所有物質的物理凝固', '電子永久消失的反應', '不含離子的純水自動導電'], '原本不易自發的氧化還原反應', '電解以外加電能推動非自發或難以自發的氧化還原反應，能量由電能轉入化學能。'),
('電池與電解', '原電池與電解槽的主要差異較接近？', ['原電池自發反應產生電能，電解槽消耗電能推動反應', '兩者都只把熱能變成聲音', '電解槽不涉及氧化還原', '原電池不需要電解質'], '原電池自發反應產生電能，電解槽消耗電能推動反應', '兩者都含電極與電解質，但能量轉換方向與反應自發性不同。'),
('陽陰極', '在電解槽中，陽極與陰極的定義依據是？', ['陽極發生氧化，陰極發生還原', '陽極永遠負、陰極永遠正', '兩極都只發生還原', '兩極只依顏色命名'], '陽極發生氧化，陰極發生還原', '陽極與陰極以反應類型定義；在電解槽中通常陽極接正端、陰極接負端，但不可混淆極性與反應定義。'),
('離子移動', '電解熔融或水溶液時，陽離子通常移向？', ['陰極，並在陰極得到電子而還原', '陽極並失去所有質量', '電源外殼', '不移動且不參與反應'], '陰極，並在陰極得到電子而還原', '帶正電的離子受電場吸引移向陰極，常在陰極發生還原；實際水溶液還需考量競爭反應。'),
('氯化銅電解', '電解氯化銅溶液時，銅離子若在陰極得到電子，會形成？', ['銅金屬析出', '氯氣在陰極生成', '氧氣在銅片內生成', '水分子變成鈉'], '銅金屬析出', 'Cu²⁺得到電子可還原成 Cu，金屬沉積位置與電極反應及溶液條件有關。'),
('電鍍', '電鍍時，被鍍物通常接在哪一極以使金屬離子在其表面還原析出？', ['陰極', '陽極', '不接電源', '電解質外部'], '陰極', '被鍍物作為陰極，金屬離子在表面得到電子還原成金屬；陽極可能提供金屬離子。'),
('電極材料', '若以可溶性金屬作電鍍陽極，常見作用是？', ['陽極金屬氧化成離子，補充溶液中的金屬離子', '陽極金屬完全不參與反應', '陽極只吸收電子而不失去原子', '使水變成塑膠'], '陽極金屬氧化成離子，補充溶液中的金屬離子', '可溶性陽極可被氧化溶解，協助維持電解質中金屬離子濃度。'),
('變因控制', '比較不同電流對電鍍質量的影響，哪項設計較公平？', ['固定電解質、電極面積、距離、時間與溫度，只改變電流', '同時改變電流、時間與電極面積', '只看表面亮度一次', '先決定質量增加再挑資料'], '固定電解質、電極面積、距離、時間與溫度，只改變電流', '電鍍量受電流、時間、離子濃度與電極條件影響，需控制其他因素。'),
('氣體判讀', '電解水時陰極與陽極產生的氣體體積比例，理想情況下可用來判斷？', ['氫氣與氧氣的生成量具有特定比例，反映水的組成', '水只由氧氣組成', '兩極產生的必然都是氫氣', '氣體與電極反應無關'], '氫氣與氧氣的生成量具有特定比例，反映水的組成', '水電解涉及陰極還原與陽極氧化，理想生成量比例可連結化學式與電子守恆。'),
('安全操作', '電解實驗使用電源與溶液時，哪項做法較適當？', ['先關閉電源再調整電極，使用低電壓並避免短路與接觸未知產物', '通電時直接用手移動電極', '為提高反應任意提高電壓', '把產生氣體直接點燃測試'], '先關閉電源再調整電極，使用低電壓並避免短路與接觸未知產物', '電解可能產生可燃或刺激性物質，需依規範控制電壓、通風與操作順序。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的外加電源、電極、離子、沉積或氣體。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合電解原理與電極反應。', '排除誘答：分清陽極／陰極的反應定義與極性、外電路電子與溶液離子、原電池與電解槽。', '最後回查：確認變因控制、產物判讀與安全操作都和題幹一致。']
    return {'id': f'question-science-content-jc-iv-7-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-7'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究電解、電池差異、電極反應、電鍍、氣體與安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-7', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '電解實驗與電解原理', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先判斷電解槽的能量方向，再依陽極氧化、陰極還原追蹤離子與產物，最後檢查安全。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-7-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

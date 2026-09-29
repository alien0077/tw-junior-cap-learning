import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('電池功能', '鋅銅電池能輸出電流，最主要是把哪種能量轉換成電能？', ['氧化還原反應的化學能', '聲音的能量', '重力直接變成電子', '光線必然變成電流'], '氧化還原反應的化學能', '電池利用自發氧化還原反應，將化學能透過電子轉移轉換為電能。'),
('鋅電極', '在常見鋅銅原電池中，鋅較容易失去電子，因此鋅電極通常發生？', ['氧化，放出電子', '還原，吸收電子', '只發生物理熔化', '不參與任何反應'], '氧化，放出電子', '氧化可用失去電子表示；鋅原子變成鋅離子並把電子送入外電路。'),
('電子流向', '鋅銅原電池接通外電路時，電子通常由哪裡流向哪裡？', ['由鋅電極經外電路流向銅電極', '由銅電極流向鋅電極', '由電解質直接流入塑膠線', '電子不會移動'], '由鋅電極經外電路流向銅電極', '鋅是電子來源，電子經導線到銅電極；溶液中則主要由離子移動維持電荷平衡。'),
('電極角色', '在原電池中，銅電極表面可能發生還原反應，較適當的描述是？', ['溶液中的陽離子在銅表面得到電子而被還原', '銅一定失去所有電子', '銅電極只負責吸收水分', '還原反應不需要電子'], '溶液中的陽離子在銅表面得到電子而被還原', '陰極是發生還原的電極；在鋅銅電池模型中，銅提供反應表面與電子接收位置。'),
('電解質作用', '鋅銅電池中的電解質溶液主要功能之一是？', ['提供可移動離子並維持電荷平衡，使反應能持續', '阻止所有離子移動', '取代外電路中的金屬線傳遞電子', '讓電池不需氧化還原反應'], '提供可移動離子並維持電荷平衡，使反應能持續', '電解質中離子移動，外電路則主要由電子傳遞；兩者共同完成電池迴路。'),
('電壓差異', '更換電極材料可能改變電池電壓，主要因為？', ['不同材料失去或得到電子的傾向不同，造成電位差改變', '材料顏色決定電子數量', '所有金屬的反應性完全相同', '電壓只由導線長度決定'], '不同材料失去或得到電子的傾向不同，造成電位差改變', '電極材料的氧化還原傾向不同，會影響兩電極間的電位差與輸出電壓。'),
('串聯電池', '將相同方向的多個電池串聯，通常可使總電壓？', ['在理想近似下相加', '一定變成零', '只等於其中最小電壓', '與電池數量完全無關'], '在理想近似下相加', '串聯電池的電位差可依方向相加；實際輸出還會受內阻、接觸與負載影響。'),
('反應停止', '鋅銅電池使用一段時間後電壓下降，可能原因是？', ['反應物消耗、離子濃度改變或內阻增加', '電子被永久創造完畢', '銅與鋅質量都必然增加', '電解質不再含任何粒子'], '反應物消耗、離子濃度改變或內阻增加', '電池不是無限能源，反應物與界面條件變化會使電壓或可輸出電流降低。'),
('實驗控制', '比較不同電解質對鋅銅電池電壓的影響，較公平的做法是？', ['固定電極、距離、面積、溫度與測量儀器，只更換電解質', '同時改變電極、溶液與導線長度', '只看燈泡亮度一次', '先決定哪種溶液最好再選資料'], '固定電極、距離、面積、溫度與測量儀器，只更換電解質', '控制電池結構與測量條件，才能把輸出差異主要歸因於電解質。'),
('安全判讀', '製作簡易電池時，哪項做法較安全且合理？', ['使用低電壓、少量已知溶液並避免短路與直接接觸化學品', '將電池直接接上市電插座', '用嘴咬住導線測試電流', '任意混合未知化學品提高電壓'], '使用低電壓、少量已知溶液並避免短路與直接接觸化學品', '電化學實驗需控制電壓、避免短路與化學品暴露，並依實驗室安全規範操作。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的電極、電子、離子、電解質或電路條件。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合原電池的氧化還原流程。', '排除誘答：分清氧化與還原、電子與離子、外電路與電解質，以及理想模型與實際內阻。', '最後回查：確認電極角色、反應方向、控制變因與安全操作均對應題幹。']
    return {'id': f'question-science-content-jc-iv-5-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-5'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究鋅銅電池、氧化還原、電子流向、電解質、電壓與安全的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-5', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '鋅銅電池與電池原理', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先判斷氧化與還原電極，再追蹤電子、離子與電壓來源，最後核對電池條件與安全。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-5-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

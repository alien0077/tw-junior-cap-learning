import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('對氧活性', '金屬對氧活性較大，通常表示它？', ['較容易與氧反應形成氧化物', '完全不會失去電子', '一定不能導電', '只會發生物理熔化'], '較容易與氧反應形成氧化物', '對氧活性描述金屬與氧反應的傾向，不等同於金屬是否導電或是否容易熔化。'),
('燃燒現象', '鎂帶在氧氣中燃燒比在空氣中更旺，合理原因是？', ['氧氣濃度較高，燃燒反應速率可能增加', '氧氣是燃料而鎂是助燃物', '空氣中完全沒有氧氣', '鎂在氧氣中不會發生氧化'], '氧氣濃度較高，燃燒反應速率可能增加', '氧氣是常見助燃物；濃度與溫度等條件會影響金屬氧化反應速率。'),
('氧化膜', '鋁表面形成緻密氧化膜後，可能出現哪項效果？', ['氧化膜阻隔部分氧氣與鋁接觸，使後續腐蝕變慢', '鋁完全不再含有氧化物', '氧化膜使鋁變成非金屬', '氧化膜一定讓燃燒更劇烈'], '氧化膜阻隔部分氧氣與鋁接觸，使後續腐蝕變慢', '緻密氧化膜可形成保護層；膜的完整性與環境條件仍會影響保護效果。'),
('活性比較', '比較鐵、銅、鎂在相同氧氣條件下的反應，較適合用哪項證據判斷相對活性？', ['控制質量與表面狀態後比較反應難易、速率或產物證據', '只比較金屬顏色', '讓每種金屬使用不同溫度後直接排名', '只看樣品大小不記錄反應'], '控制質量與表面狀態後比較反應難易、速率或產物證據', '金屬活性比較需控制表面積、質量、溫度與氧氣條件，以可觀察反應證據判斷。'),
('產物判讀', '金屬燃燒後生成固體氧化物，最能支持哪項描述？', ['金屬與氧結合形成新物質，發生氧化反應', '金屬只被切成更小顆粒', '氧氣沒有參與反應', '固體產物一定是原金屬'], '金屬與氧結合形成新物質，發生氧化反應', '產生新固體且含氧狀態改變支持化學變化與氧化，但完整成分仍需分析。'),
('質量變化', '金屬在開放空氣中氧化後固體質量增加，最合理的原因是？', ['氧元素從空氣進入固體產物', '質量由火焰創造', '金屬失去所有原子', '天平會自動增加數值'], '氧元素從空氣進入固體產物', '開放系統中氧氣成分加入固體，故產物質量可能比原金屬大。'),
('表面積', '同質量金屬粉末比金屬塊更容易快速與氧反應，可能因為？', ['粉末總表面積較大，與氧接觸機會較多', '粉末沒有質量', '金屬塊不含原子', '表面積越大氧氣越少'], '粉末總表面積較大，與氧接觸機會較多', '反應速率會受接觸面積影響；粉末也可能增加操作與燃燒安全風險。'),
('條件控制', '比較金屬在氧氣中燃燒的劇烈程度，哪項條件應固定？', ['金屬質量、形狀表面積、氧氣濃度、溫度與點火方式', '每種金屬使用不同質量與溫度', '只固定觀察者位置', '先知道活性順序再選反應時間'], '金屬質量、形狀表面積、氧氣濃度、溫度與點火方式', '反應劇烈程度受多項因素影響，固定非研究變因才能比較金屬本身的對氧活性。'),
('安全操作', '加熱金屬粉末或金屬帶進行燃燒實驗時，較適當的是？', ['使用護目鏡、夾具與規定量，遠離可燃物並遵守教師指示', '直接用手拿燃燒中的金屬', '把氧氣瓶口對準同學', '為了更旺而任意增加粉末量'], '使用護目鏡、夾具與規定量，遠離可燃物並遵守教師指示', '金屬燃燒可能高溫、強光或產生飛濺，需依規範使用器材與控制樣品量。'),
('證據界線', '某金屬在一次實驗中未明顯燃燒，最嚴謹的判讀是？', ['在該次溫度、氧氣、表面與時間條件下未觀察到明顯燃燒，不能直接判定它完全不與氧反應', '可證明金屬永遠不會氧化', '代表金屬一定沒有氧化膜', '可直接排出所有其他因素'], '在該次溫度、氧氣、表面與時間條件下未觀察到明顯燃燒，不能直接判定它完全不與氧反應', '反應未見明顯現象可能受條件與偵測靈敏度影響，結論需限定實驗範圍。'),
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
    steps = [f'讀題定位：圈出「{tag}」與題目中的金屬、氧氣、溫度、表面積或產物。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合金屬對氧活性與燃燒概念。', '排除誘答：分清助燃物與可燃物、反應速率與活性、氧化膜與完全不反應，並檢查控制條件。', '最後回查：確認安全操作與證據界線都符合題幹，沒有由單次未燃燒過度推論。']
    return {'id': f'question-science-content-jc-iv-3-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-jc-iv-3'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究金屬燃燒、對氧活性、氧化膜、表面積與比較實驗的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-jc-iv-3', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '金屬燃燒與對氧活性', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先比較金屬與氧的反應條件，再檢查活性、速率、氧化膜、表面積與實驗控制。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-jc-iv-3-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

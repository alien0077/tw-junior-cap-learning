import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'questions/science'
URL = 'https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA = [
('真空光速', '光在真空中的速率與進入透明介質後相比，通常如何？', ['真空中的光速最大，進入介質後速率通常降低', '真空中的光速為零，玻璃中最大', '所有介質中的光速完全相同', '光只在空氣中能傳播'], '真空中的光速最大，進入介質後速率通常降低', '真空光速 c 是上限；透明介質與光的交互作用使相速度通常降低，介質不同也會造成速率差異。'),
('介質比較', '在空氣與玻璃中比較光速，哪項判斷較合理？', ['玻璃的折射率通常較大，因此光在玻璃中的速率通常比在空氣中小', '空氣折射率比玻璃大且光速較小', '介質密度越大就代表光完全不能通過', '所有透明物質的折射率都相同'], '玻璃的折射率通常較大，因此光在玻璃中的速率通常比在空氣中小', '近似關係 v=c/n；玻璃折射率通常大於空氣，所以光在玻璃中的速率較慢，且仍能傳播。'),
('折射率計算', '若某透明材料折射率 n=1.5，真空光速取 3.0×10^8 m/s，光在材料中的速率約為？', ['2.0×10^8 m/s', '4.5×10^8 m/s', '3.0×10^8 m/s', '1.5×10^8 m/s'], '2.0×10^8 m/s', '使用 v=c/n=(3.0×10^8)/1.5=2.0×10^8 m/s；折射率大於 1 時介質中速率低於真空光速。'),
('顏色與介質', '白光進入透明介質時，不同顏色的光可能有略不同速率，這有何結果？', ['折射程度可能不同，形成色散現象', '所有顏色必定沿完全相同路徑且不折射', '光速差異會使光變成聲音', '顏色只由介質溫度決定'], '折射程度可能不同，形成色散現象', '材料對不同波長的折射率可能不同，導致不同顏色折射角不同；三稜鏡分光就是常見例子。'),
('介面判讀', '光從空氣斜射進玻璃時，除了速率改變，通常還可能發生什麼？', ['傳播方向改變而產生折射，且部分光可能反射', '光的能量必定全部消失', '光會在介面停止且不再傳播', '只會改變顏色而方向與速率不變'], '傳播方向改變而產生折射，且部分光可能反射', '斜射跨越介面時，光速改變會使方向改變；介面也可能同時產生反射，能量不必全部透射。'),
('實驗控制', '比較不同透明材料中的光速或折射率時，哪項設計較公平？', ['使用同一光源與波長，固定入射角與幾何位置，校正儀器後重複測量', '每種材料使用不同光源與不同入射角', '只看一次折射方向不量角度', '先挑最符合公式的讀值'], '使用同一光源與波長，固定入射角與幾何位置，校正儀器後重複測量', '不同波長、入射角與量測幾何會影響結果；控制條件並重複測量才能比較材料性質。'),
('折射率界線', '若某材料折射率接近 1，表示什麼？', ['在該波長下光速接近真空光速，折射偏折通常較小，但仍需看入射角', '光在材料中必定比真空快', '材料一定不透明', '材料內沒有任何粒子'], '在該波長下光速接近真空光速，折射偏折通常較小，但仍需看入射角', '折射率 n 接近 1 表示 v=c/n 接近 c；偏折角還與入射角及另一側介質折射率有關。'),
('資料可信度', '以飛行時間測量光速時，哪項資料最能降低誤差？', ['使用已知距離、精確計時、多次重複並記錄儀器解析度與環境條件', '只測極短距離一次且不記錄時間單位', '把反射回程距離當成單程距離', '忽略儀器延遲而只報一個漂亮數字'], '使用已知距離、精確計時、多次重複並記錄儀器解析度與環境條件', '光速極快，飛行時間測量對距離、計時與儀器延遲敏感；重複與校正能讓結果更可信。'),
('生活應用', '光纖能傳送訊號，主要利用哪項光學現象降低光從纖芯逸出？', ['全反射', '只靠聲音共振', '光在真空中停止', '磁力把光吸回纖芯'], '全反射', '當光由高折射率纖芯向低折射率包覆層且入射角足夠大時可全反射，使光在纖芯中傳播。'),
('證據界線', '下列哪項最符合光速與介質研究的科學判讀？', ['速率與折射率要在指定波長、溫度與介質條件下比較，並說明模型與測量誤差', '只要知道材料名稱就能精確預測所有光速', '折射率是所有顏色與溫度下固定不變', '一次目測折射方向即可取代量測'], '速率與折射率要在指定波長、溫度與介質條件下比較，並說明模型與測量誤差', '光速與折射率具有波長、溫度和材料條件，實驗結論要標示適用範圍與不確定性。'),
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
    steps = [f'讀題定位：圈出「{tag}」以及真空、介質、折射率、波長、入射角或量測誤差。', f'建立判準：{reason}', f'核對答案：選項 {aid}「{answer}」符合光速、折射率與介面判讀原理。', '排除誘答：分清光速、折射方向、折射率與反射，並確認公式、單位與測量路徑沒有偷換。', '最後回查：確認材料、波長、入射條件及模型適用範圍都與題幹一致。']
    return {'id': f'question-science-content-ka-iv-7-{i}', 'subject': 'science', 'type': 'single-choice', 'prompt': prompt, 'options': options, 'knowledgeIds': ['kg-science-content-ka-iv-7'], 'difficulty': 'medium', 'answer': {'value': aid, 'explanation': reason}, 'provenance': {'origin': 'original', 'license': 'All rights reserved', 'sourceUrl': URL, 'sourceLocator': '公立國中段考自然科；研究真空與介質光速、折射率、色散、折射反射、光纖與實驗誤差的能力方向。', 'authoringNote': '依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'}, 'reviewStatus': 'draft', 'updatedAt': '2026-09-08', 'lessonId': 'lesson-science-content-ka-iv-7', 'examPatternRefs': [{'url': URL, 'title': '公立國中段考自然科；僅研究題型與能力方向，未複製原題。', 'year': '114', 'subject': 'science', 'locator': '光速與影響因素', 'observedPattern': '能力方向研究後原創改寫', 'reuseDecision': 'pattern-only', 'status': 'recorded', 'locatorLevel': 'paper'}], 'solutionStrategy': '先確認光所處介質與折射率，再用 v=c/n 或介面幾何判斷速率與方向，最後檢查波長、入射角與量測誤差。', 'solutionSteps': steps}

for i, row in enumerate(DATA, 1):
    (OUT / f'question-science-content-ka-iv-7-{i}.json').write_text(json.dumps(make(i, row), ensure_ascii=False, indent=2) + '\n')
print('rewrote', len(DATA), 'questions')

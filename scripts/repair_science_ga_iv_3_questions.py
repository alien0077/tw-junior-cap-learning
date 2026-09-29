import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = [
 ("ABO 血型由 Iᴬ、Iᴮ、i 三種等位基因共同形成。下列哪項基因型與表現型配對正確？", ["Iᴬi：A 型", "IᴬIᴮ：O 型", "ii：AB 型", "Iᴮi：A 型"], "A", "Iᴬ 對 i 顯性，Iᴮ 對 i 顯性；IᴬIᴮ 為共顯性而表現 AB 型，ii 才是 O 型。", "先寫出三種基因型與四種表現型的對照，再逐一檢查選項。"),
 ("A 型父親的基因型為 Iᴬi，B 型母親的基因型為 Iᴮi。子女可能出現哪些血型？", ["A、B、AB、O 四種皆可能", "只有 A 型與 B 型", "只有 AB 型", "只有 O 型"], "A", "父親可提供 Iᴬ 或 i，母親可提供 Iᴮ 或 i，組合為 IᴬIᴮ、Iᴬi、Iᴮi、ii，因此四種表現型皆可能。", "先列出雙親各自可形成的配子，再用棋盤格組合並轉換成表現型。"),
 ("O 型母親與 AB 型父親生育子女時，在不考慮突變的情況下，子女不可能是哪一型？", ["O 型", "A 型", "B 型", "A 型或 B 型以外的 AB 型與 O 型"], "D", "O 型母親只能提供 i，AB 型父親可提供 Iᴬ 或 Iᴮ，子女只能是 Iᴬi（A 型）或 Iᴮi（B 型），不會是 AB 或 O 型。", "固定只能提供一種配子的親本，再列出另一親本的兩種配子。"),
 ("若一對父母都是 A 型，子女卻是 O 型，對雙親基因型最合理的推論是？", ["雙親都必須帶有 i，即 Iᴬi × Iᴬi", "至少一方一定是 IᴬIᴬ", "其中一方必定是 AB 型", "O 型子女不可能由 A 型雙親產生"], "A", "O 型子女基因型必為 ii，因此雙親各自都要提供 i；A 型雙親可為 Iᴬi，兩者配對才可能產生 ii。", "從子代表現型反推必需的基因，再檢查雙親是否各能提供該基因。"),
 ("ABO 血型常被用來說明複等位基因與共顯性。下列敘述何者正確？", ["族群中有三種等位基因，但一個人的同一基因座通常只帶其中兩個；Iᴬ與Iᴮ可共顯性", "每個人同一基因座可同時帶三種等位基因", "Iᴬ與Iᴮ相遇一定只表現 A 型", "i 對 Iᴬ與 Iᴮ都顯性"], "A", "複等位基因是指族群中同一基因座有三種以上等位基因；個體仍通常有兩個，Iᴬ與Iᴮ同時存在時表現 AB 型。", "區分『族群中的等位基因種類』與『個體攜帶的兩個等位基因』。"),
 ("父母基因型為 IᴬIᴮ 與 ii，子女的基因型可能是？", ["Iᴬi 或 Iᴮi", "IᴬIᴮ 或 ii", "只有 IᴬIᴮ", "只有 ii"], "A", "AB 型親本可提供 Iᴬ或 Iᴮ，O 型親本只能提供 i，因此子女只能形成 Iᴬi 或 Iᴮi，表現為 A 型或 B 型。", "先寫出每位親本的配子集合，再做一對一配對。"),
 ("某家庭已有一名 AB 型子女。這個子女從雙親得到的等位基因最合理是？", ["一個 Iᴬ 與一個 Iᴮ", "兩個 i", "一個 Iᴬ 與一個 i", "一個 Iᴮ 與一個 i"], "A", "AB 型的基因型是 IᴬIᴮ，表示子女分別從雙親得到 Iᴬ與 Iᴮ；它不是由兩個隱性 i 組成。", "先由表現型查基因型，再回推雙親各提供哪一個等位基因。"),
 ("用棋盤格預測血型時，若雙親都是 Iᴬi，四個格子的基因型比例應為？", ["IᴬIᴬ：Iᴬi：ii = 1：2：1", "IᴬIᴬ：Iᴬi：ii = 2：1：1", "只有 Iᴬi", "IᴬIᴬ：ii = 1：1"], "A", "雙親各可提供 Iᴬ或 i，四種配對中有一格 IᴬIᴬ、兩格 Iᴬi、一格 ii，比例為 1：2：1。", "逐格列出四種配子組合，再合併相同基因型的格子。"),
 ("某張家族圖只標示祖父母與孫子的 A、B、O、AB 血型，想判斷可能的親子關係，哪種做法最可靠？", ["先把每個表現型轉成可能基因型，再逐代檢查配子能否形成下一代", "只看家族中出現最多的血型就決定親子關係", "只要兩人血型不同就不可能有親子關係", "直接以血型判定唯一身分，不需考慮基因型多種可能"], "A", "A 型與 B 型各可能有兩種基因型，判讀家族關係要保留可能性並逐代檢查遺傳組合，不能以表現型數量或單一配對直接斷定。", "保留每個表現型的基因型分支，再用遺傳規則逐代排除不可能。"),
 ("下列哪個敘述能避免把 ABO 血型遺傳題與醫療輸血判斷混為一談？", ["遺傳題討論等位基因與子代機率；實際輸血還需依醫療檢驗與血庫規範", "只要知道父母血型就能自行決定輸血對象", "血型遺傳機率等於每個孩子一定會出現的結果", "ABO 血型可以取代所有輸血前檢查"], "A", "遺傳推論是機率與基因型的模型；臨床輸血須由專業人員進行血型、交叉試驗與相容性檢查，不能把課堂模型當成醫療指示。", "先確認題目是遺傳機率還是醫療決策，再標示模型可回答與不可回答的範圍。"),
]
PUBLIC_REFERENCES = [
 {"url":"https://w3.qnm.kh.edu.tw/test/%E8%87%AA%E7%84%B6%E4%B8%80%E4%B8%8B.pdf","title":"高雄市立青年國中公開補考題庫","year":"112"},
 {"url":"https://www.nhjh.tp.edu.tw/uploads/16907876075143MWxyjwe.pdf","title":"臺北市立內湖國中七年級生物公開定期評量","year":"111"},
 {"url":"https://www.klm.kh.edu.tw/upload/310/101_83606/113-2-1%E8%87%AA7A.pdf","title":"高雄市立蚵寮國民中學七年級自然科公開定期評量","year":"113"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91%28%E5%9C%B0%E7%A7%91%2B%E7%94%9F%E7%89%A9%29.pdf","title":"高雄市立國昌國中三年級自然科公開段考試題","year":"111"},
]
for ref in PUBLIC_REFERENCES:
    ref.update({"subject":"science","locator":ref["title"],"observedPattern":"研究公立學校公開試題中的 ABO 四種表現型、IA/IB/i 基因型、共顯性、複等位基因、親子配對與棋盤格判讀方向；未複製原題文字、選項、圖表或答案。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"})
for i,(prompt,options,answer,explanation,strategy) in enumerate(DATA,1):
    path=ROOT/"questions/science"/f"question-science-content-ga-iv-3-{i}.json"
    item=json.loads(path.read_text()); correct=options[ord(answer)-65]
    item.update({"prompt":prompt,"options":[{"id":chr(65+j),"text":t} for j,t in enumerate(options)],"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}：「{correct}」。"},"solutionStrategy":strategy,"solutionSteps":["先把題目中的血型轉換成可能的基因型。","列出雙親各自可提供的配子，不把表現型直接當成唯一基因型。",f"套用原理：{explanation}",f"排除混淆顯性、共顯性、複等位基因或忽略機率的選項，答案為「{correct}」。","回查棋盤格、親子推論與醫療情境是否沒有超出遺傳模型的適用範圍。"],"examPatternRefs":PUBLIC_REFERENCES,"reviewStatus":"draft"})
    path.write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n")
print(f"rewrote {len(DATA)} questions")

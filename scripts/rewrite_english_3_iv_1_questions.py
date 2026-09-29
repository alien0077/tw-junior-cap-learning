#!/usr/bin/env python3
"""Re-author English 3-IV-1 letter-recognition items with exact public exam refs."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
XIAOGANG="https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/11%E4%B8%80%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD111-1-1%E5%9C%8B%E4%B8%80%E8%8B%B1%E6%96%87%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%E5%8F%8A%E8%A7%A3%E7%AD%94%28%E6%9C%80%E7%B5%82%E5%AE%9A%E7%A8%BF%29.pdf"
YICHANG110="https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=359&cfsn=2121&fn=110-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE-%E6%9E%97%E7%8E%89%E8%93%AE.pdf&op=dlfile"
DASHE="https://www.dam.kh.edu.tw/upload/68/101_28414/%E4%B8%80%E5%B9%B4%E7%B4%9A%20%20%E5%9C%8B%E6%96%87%E3%80%81%E8%8B%B1%E8%AA%9E%E3%80%81%E6%95%B8%E5%AD%B8%E3%80%81%E8%87%AA%E7%84%B6.pdf"
YICHANG109="https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=358&cfsn=2101&name=109-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E8%A9%A6%E9%A1%8C%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile"
SOURCES={
 XIAOGANG:("高雄市立小港國中","111學年度第一學期一年級第一次段考英文科試題","只參考非選題第一大題第1至3題的大寫／小寫互換任務；未複製原題字詞或作答版面。"),
 YICHANG110:("花蓮縣立宜昌國中","110學年度第一學期七年級第一次段考英文科試題","只參考答案卷PDF第5頁寫作測驗一（一）第1至3題的字母大小寫互換任務；改用不同英文字詞與新情境。"),
 DASHE:("高雄市立大社國中","七年級第一次評量英語科試卷","只參考第一部分第1、2題字母順序填空及第二部分第2題大小寫改寫的任務形式；未複製題目字詞或表格。"),
 YICHANG109:("花蓮縣立宜昌國中","109學年度第一學期七年級第一次段考英文科試題","只參考第21題字母順序辨識及第22題字典序排列的任務形式；所有字母／字詞序列均重新設計。"),
}
ITEMS=[
 {"answer":"C","source":(XIAOGANG,1,"non-selection section I, item 1: uppercase-to-lowercase conversion"),"prompt":"A field notebook has the connected capital word “NOTEBOOK.” The index requires ordinary lowercase print. Which transcription keeps every letter in the same order?","options":[("A","notebok"),("B","NoteBook"),("C","notebook"),("D","notoebok")],"explanation":"原字母順序是 n-o-t-e-b-o-o-k，轉成小寫後應全部為 notebook。C 完整保留八個字母與排列，只改變大小寫；其他選項漏字、混用大小寫或調換字母。","strategy":"辨讀連寫字母時先逐字確認字序，再統一轉換大小寫；不可因熟悉單字而漏字、換序或保留一個大寫。","steps":["筆記索引要求把連寫的大寫字轉成一般小寫，任務是轉寫字形，不是改寫詞義。","依序核對 N-O-T-E-B-O-O-K 共八個字母，特別注意末段有連續兩個 O。","全部轉成小寫後，字母仍須照原順序排列，結果為 notebook。","C 是唯一保留完整字序且全部小寫的選項；A 漏掉一個 o，B 混入大寫，D 調換字母。","所以選 C；轉錄完成後逐字回看索引，確認沒有漏掉成對的 o 或移動相鄰字母。"]},
 {"answer":"A","source":(XIAOGANG,2,"non-selection section I, item 2: uppercase-to-lowercase conversion"),"prompt":"On a garden plan, “GARDEN” is written in connected capitals. The student must enter the same word in all lowercase. Which form is correct?","options":[("A","garden"),("B","Garden"),("C","garedn"),("D","gardne")],"explanation":"大小寫互換不改變拼字。G-A-R-D-E-N 轉為小寫仍依序是 garden，因此 A 同時符合六個字母的對應與原始次序。","strategy":"先用字母逐一對位，再一次檢查容易混淆的相鄰字母；大小寫轉換不能順便改動單字拼法。","steps":["圖面索引已把字詞內容確定為 GARDEN，現在只需要把字形改成全小寫。","逐位配對 G/g、A/a、R/r、D/d、E/e、N/n，避免把外形相近的連寫筆畫合併。","照原順序讀回 g-a-r-d-e-n，確認第4與第5位仍是 d、e。","A 完整符合小寫形式；B 留下大寫，C 對調了 e、d，D 對調了 n、e。","選 A；轉錄後把印出的 garden 與原圖逐字比對，而非只憑整字外觀判斷。"]},
 {"answer":"D","source":(XIAOGANG,3,"non-selection section I, item 3: lowercase-to-uppercase conversion"),"prompt":"A connected lowercase label reads “planet.” The filing system stores labels in uppercase. Which version preserves the same six letters?","options":[("A","PlAnet"),("B","PLANETT"),("C","planet"),("D","PLANET")],"explanation":"planet 的六個字母依序是 p-l-a-n-e-t；轉為大寫只改字母形式，結果為 PLANET。D 保留完整字序，沒有增加字母或留下小寫。","strategy":"由小寫轉大寫時先辨識每個字母，再核對字序；尤其要檢查連寫的 l、a 與詞尾 t，避免增字或交換。","steps":["這次要把已辨認的連寫小寫標籤轉成全大寫，不能因大小寫改變而增刪字母。","將單字拆成 p-l-a-n-e-t 六格，逐格確認 l 在 a 前，而 n 接在 a 後。","把六格換成 P-L-A-N-E-T，讀回仍是原單字 planet。","D 保留原字序且全大寫；A 混用大小寫，B 多出一個 T，C 沒有轉換。","因此選 D；逐格核對比整體掃讀更可靠，尤其可確認詞尾只有一個 t。"]},
 {"answer":"B","source":(YICHANG110,1,"PDF page 5, writing test I(a), item 1: MARKER case conversion"),"prompt":"A navigation slip shows the connected capitals “COMPASS.” The searchable archive uses lowercase. Which entry is an exact case conversion?","options":[("A","compas"),("B","compass"),("C","Compass"),("D","compsas")],"explanation":"逐字對應 C-O-M-P-A-S-S 的小寫是 c-o-m-p-a-s-s。B 只轉換大小寫；其他選項漏掉一個 s、保留大寫或調換字母。","strategy":"辨認連寫字時採用「先分字母、再核順序、最後轉大小寫」；不要用相似外形替換原字母。","steps":["路線卡上的 COMPASS 有七個字母，任務是轉成小寫後輸入索引。","依序拆讀 C、O、M、P、A、S、S，並特別檢查字尾有相連的兩個 s。","按位置轉寫成 c-o-m-p-a-s-s，大小寫改變不會改變詞義或字母排列。","B 是完整小寫 compass；A 漏掉一個 s，C 首字母仍大寫，D 將字母換了位置。","選 B；輸入前從左至右逐格比對，確認成對的 s 都在末尾而沒有漏寫。"]},
 {"answer":"C","source":(YICHANG110,2,"PDF page 5, writing test I(a), item 2: lowercase-to-uppercase conversion"),"prompt":"A note written in lowercase says “journey.” It begins a new line and must be copied in uppercase for a form. Which copy follows the instruction exactly?","options":[("A","journey"),("B","Journey"),("C","JOURNEY"),("D","JOURNEy")],"explanation":"題目指定全大寫，因此 j-o-u-r-n-e-y 應逐字轉成 JOURNEY。C 沒有增刪字母，也沒有留下小寫字母。","strategy":"先辨識字母與標點的邊界，再按指定格式轉換；不可把句首大寫與「全大寫」兩種要求混為一談。","steps":["表格明確要求 uppercase，表示七個字母都要轉成大寫，而不只是句首字母。","確認原字是 j-o-u-r-n-e-y，按原順序逐個映射為 J-O-U-R-N-E-Y。","檢查中段 r-n-e 的連寫筆畫分界，避免把相鄰字母誤讀或漏掉。","C 是全大寫且字詞完全相同；A 未轉換，B 只有首字母大寫，D 留下小寫 y。","所以選 C；抄到正式表格後逐格比對大小寫，確認七個位置都符合指示。"]},
 {"answer":"D","source":(YICHANG110,3,"PDF page 5, writing test I(a), item 3: uppercase-to-lowercase conversion"),"prompt":"The handwritten heading “ORCHID” is requested in all lowercase on a botanical record card. Which form preserves the letters and their order?","options":[("A","OrChid"),("B","ORCHID"),("C","orchdi"),("D","orchid")],"explanation":"O-R-C-H-I-D 轉成全小寫後是 o-r-c-h-i-d。D 保留六字母順序並完成格式轉換，其餘選項有大小寫不符或字母錯置。","strategy":"遇到連續的大寫字母時，依序確認每個字形，再逐一轉成小寫；檢查尾段 h-i-d，避免連寫造成換序。","steps":["植物資料卡指定全小寫，所以不能只把第一個字母改小寫或保留原樣。","把 ORCHID 拆為 O-R-C-H-I-D 六個位置，先確認中段是 C-H-I 而非相近的換序。","逐位轉成 o-r-c-h-i-d，且不加入空格、標點或其他字母。","D 正確保留全部字母並符合小寫格式；A 仍有大寫，B 未轉換，C 將末兩字母對調。","答案選 D；完成後將新形式與原標題逐位對照，特別複查 h、i、d 的先後。"]},
 {"answer":"A","source":(DASHE,1,"Part I, item 1: fill alphabet sequence from the given K"),"prompt":"A connected-letter strip should follow the alphabet. It shows J, K, a blank, M. Which letter belongs in the blank?","options":[("A","L"),("B","N"),("C","I"),("D","P")],"explanation":"英文字母序列中 K 之後、M 之前是 L。依前後字母定位可避免只看連寫字形而把缺格填成跳號的 N；左右兩側都支持同一答案，因此 L 是唯一能讓序列連續的字母。","strategy":"讀取連寫字母序列時，以已辨識的前後字母交叉定位缺格；不要只靠背誦其中一個字母猜答案。","steps":["先找到空格左右已確認的 J、K 與 M，這是判斷缺字的順序證據，也能確認空格的位置只有一格。","從 K 往後數一格得到 L；再從 M 往前退一格也得到 L，兩個方向各自提供一次核對。","兩個方向交叉檢查一致，表示空格只缺一個字母而不是漏掉兩格，序列前後沒有跳號。","A 的 L 同時接在 K 後並位於 M 前；B、C、D 都破壞字母連續性，不能滿足兩側線索。","因此填 L；遇到連寫筆畫不清時，前後序列能提供獨立確認，也可再對照字母表驗證。"]},
 {"answer":"B","source":(DASHE,2,"Part II, item 2: uppercase-to-lowercase conversion"),"prompt":"A handwritten badge reads “JOURNAL” in capitals. The database field accepts lowercase only. Which entry changes case without changing the word?","options":[("A","Journal"),("B","journal"),("C","JOURNAL"),("D","jounral")],"explanation":"J-O-U-R-N-A-L 的小寫形式是 journal。B 保留七個字母的原順序並全部改為小寫；D 調換了中段字母。","strategy":"轉換整個連寫字詞時，先將字母依序拆開，再檢查小寫結果；相鄰的 r、n、a 不可因連筆而錯置。","steps":["資料庫欄位要求全小寫，故七個大寫字母都必須轉換，不能只改首字母。","按順序讀出 J-O-U-R-N-A-L，留意中後段是 R-N-A-L 而非相近的換序。","轉成 j-o-u-r-n-a-l 後，單字仍保持原來的字母次序。","B 符合全小寫和原拼字；A 仍有大寫，C 完全未轉換，D 將中段字母換位。","選 B；輸入時可以逐格核對 R-N-A-L，這比只憑整字輪廓辨認更可靠。"]},
 {"answer":"C","source":(YICHANG109,21,"PDF page 2, question 21: identify correct alphabet sequence"),"prompt":"Four lines on a cursive alphabet practice card are transcribed below. Which line follows the alphabet in consecutive ascending order?","options":[("A","G H J K"),("B","B D C E"),("C","L M N O"),("D","P Q T S")],"explanation":"L、M、N、O 在字母表中連續且遞增。A 跳過 I，B 的 C 插到 D 後，D 則把 S、T 次序顛倒；只有 C 的四個位置逐格前進且沒有漏字，因此符合題目的嚴格順序條件。","strategy":"檢查字母順序時先從左到右比較相鄰兩格，再確認是否有跳號或倒置；連寫筆畫應與字母序列互相驗證。","steps":["題目不是挑選熟悉的一串，而要確認整行每一個相鄰字母都按字母表遞增，且不能略過中間字母。","逐行檢查相鄰關係：A 從 H 跳到 J、B 在 D 後退回 C、D 的尾段又從 T 退到 S。","C 的 L-M-N-O 每一步都前進一位，而且中間沒有漏掉字母，所以同時滿足遞增與連續。","只有 C 符合兩個條件；其他選項各自包含明確的跳號或倒置，無法因局部字母正確而算對。","所以選 C；看不清某個連寫字母時，可用前後字母位置反查，再回看筆形，而不是臆測字母。"]},
 {"answer":"B","source":(YICHANG109,22,"PDF page 2, question 22: arrange words in dictionary order"),"prompt":"A cursive list contains (1) cabin, (2) cable, (3) cactus, and (4) cadet. Which option gives dictionary order?","options":[("A","(2), (1), (3), (4)"),("B","(1), (2), (3), (4)"),("C","(3), (4), (1), (2)"),("D","(4), (3), (2), (1)")],"explanation":"四字都以 ca 開頭，需比較後續字母：cab… 先於 cac…，再來是 cad…。在 cab 兩字中，i 早於 l，所以 cabin 排在 cable 前；完整順序為 (1)、(2)、(3)、(4)。","strategy":"字典序遇到共同字首時，逐位向右比較第一個不同字母；先辨清連寫字母，再用該字母在字母表的位置決定先後。","steps":["先讀出四個手寫詞並標上編號，確認題目要排序的是字詞而不是照原列順序重抄。","四字共同以 ca 起頭，第三位 b、b、c、d 決定三組字詞的大致先後。","在同為 cab 的兩字中繼續比較第四位，i 早於 l，所以 cabin 排在 cable 前。","再依 c 早於 d 排入 cactus、cadet，完整次序為 cabin、cable、cactus、cadet。","對照編號得到 (1)、(2)、(3)、(4)，故選 B；若筆跡令字母不確定，先回看字形再排序。"]},
]

def make_ref(url:str,item:int,locator:str)->dict:
 school,exam,boundary=SOURCES[url]
 year={XIAOGANG:"111-1-1",YICHANG110:"110-1-1",DASHE:"undated",YICHANG109:"109-1-1"}[url]
 return {"url":url,"title":f"{school}{exam}","year":year,"subject":"english","locator":locator,"observedPattern":f"只參照第{item}題／對應子題的字母辨識、大小寫轉換或字典序任務形式；{boundary}","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"item"}

def main()->None:
 paths=[ROOT/f"questions/english/question-english-performance-3-iv-1-{n}.json" for n in range(1,11)]
 if len(ITEMS)!=10 or any(not p.is_file() for p in paths): raise FileNotFoundError("Expected ten stable question IDs; no writes performed")
 for path,item in zip(paths,ITEMS,strict=True):
  data=json.loads(path.read_text(encoding="utf-8")); url,n,locator=item["source"]
  data["prompt"]=item["prompt"]; data["options"]=[{"id":a,"text":b} for a,b in item["options"]]
  data["answer"]={"value":item["answer"],"explanation":item["explanation"]}; data["examPatternRefs"]=[make_ref(url,n,locator)]
  data["solutionStrategy"]=item["strategy"]; data["solutionSteps"]=item["steps"]
  data["provenance"]={"origin":"original","license":"All rights reserved","sourceUrl":url,"sourceLocator":f"{SOURCES[url][0]}公開試題，{locator}；只參照題型，不重製原題字詞／圖表。","authoringNote":"依官方英語課綱與 Knowledge Graph，參照公立學校公開試題之字母辨識、大小寫轉換與排序能力獨立改寫；未複製原題題幹、選項、圖表或答案。題目維持draft，尚待版本研究與完整內容發布審查。"}
  data["reviewStatus"]="draft"; data["updatedAt"]="2026-09-24"
  path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 cp=ROOT/"implementation/reports/public-exam-source-catalog.json"; catalog=json.loads(cp.read_text(encoding="utf-8"))
 for url,(school,title,boundary) in SOURCES.items():
  row={"institution":school,"url":url,"subjects":["english"],"availableMaterial":title,"researchUse":"英語3-Ⅳ-1連續體字母辨識、大小寫互換、字母序列與字典序；逐題pattern-only，不複製原卷。","licenseBoundary":boundary}
  old=next((r for r in catalog["sources"] if r.get("url")==url),None)
  if old: old.update(row)
  else: catalog["sources"].append(row)
 catalog["questionSourceUrls"]=sorted({r["url"] for r in catalog["sources"] if r.get("url")})
 cp.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"rewritten":len(ITEMS),"allRemainDraft":True,"sourceSchools":len(SOURCES)},ensure_ascii=False))

if __name__=="__main__": main()

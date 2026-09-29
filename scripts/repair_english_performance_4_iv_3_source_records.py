#!/usr/bin/env python3
"""Rebuild English 4-IV-3 questions from item-located public-school patterns."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-4-iv-3-first-pass-review.json"

SOURCES = {
    "dawan": {
        "url": "https://www.dwm.kh.edu.tw/upload/344/104_64184/112%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立大灣國中112學年度第1學期第3次段考一年級英文科試題",
        "year": "112-1",
    },
    "xiaogang": {
        "url": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/21%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/108-1-1%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立小港國中108學年度第1學期第1次段考二年級英文科試題",
        "year": "108-1",
    },
    "guangwu": {
        "url": "https://www.gwjh.hc.edu.tw/uploads/1675745677395cd8HbqqM.pdf",
        "title": "新竹市立光武國中111學年度第1學期第3次段考一年級英文科試題",
        "year": "111-1",
    },
    "guochang110": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E8%8B%B1%E8%AA%9E%E5%8D%B7.pdf",
        "title": "高雄市立國昌國中110學年度第2學期第3次段考一年級英文科試題",
        "year": "110-2",
    },
    "guochang109": {
        "url": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf",
        "title": "高雄市立國昌國中109學年度第2學期第1次定期評量一年級英文科試題",
        "year": "109-2",
    },
    "zhishan": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/61f259ce3fa2fc1d7e423fab.pdf",
        "title": "臺中市立至善國中110學年度第1學期第1次定期評量八年級英文科試題",
        "year": "110-1",
    },
    "cap111": {
        "url": "https://school.tc.edu.tw/open-message/064526/get-file/628aea9fea5f7f4dc34107c2",
        "title": "111年國中教育會考英語科閱讀試題本（臺中市教育局公開附件）",
        "year": "111",
        "institution": "國中教育會考（公辦公開試題）",
    },
}

# Each entry is newly authored; only the item skill/data mode is borrowed.
ITEMS = {
    1: {
        "prompt": "A student is writing a sentence for the school website. Which version uses capitalization correctly?",
        "options": ["our class will visit the National Palace Museum in Taipei.", "Our class will visit the national palace museum in Taipei.", "Our class will visit the National Palace Museum in Taipei.", "Our Class will visit the National Palace Museum in taipei."],
        "correct": "C",
        "explanation": "句首 Our 必須大寫；National Palace Museum 是正式機構名稱，Taipei 是地名，也都要保留專有名詞的大寫。Class 在句中是普通名詞，不應無故大寫。A 漏了句首大寫，B 把機構名稱改成小寫，D 則把普通名詞 Class 和地名 Taipei 的大小寫弄反。",
        "strategy": "先分清句首、專有名詞與一般名詞，再逐字核對大小寫；不要把「看起來重要」誤當成專有名詞。",
        "steps": ["先找出句子的第一個字，句首 Our 應以大寫字母開頭。", "圈出完整機構名稱 National Palace Museum，確認名稱內每個主要詞的指定大寫形式。", "再標出地名 Taipei；地名是專有名詞，首字母須大寫。", "檢查 class：它只是班級的普通名詞，句中不需要額外大寫。", "對照四個版本，只有 C 同時符合句首、機構名稱、地名和普通名詞的大小寫規則。"],
        "order": ["B", "D", "A", "C"],
        "refs": [
            ("guangwu", "PDF第2頁第27題；判斷含Thanksgiving、November等專有名詞大小寫的正確句。", "以完整句子辨認節慶／月份等專有名詞，並同時檢查句子其他部分是否正確。"),
            ("guochang110", "PDF第2頁第27題；選出含Thanksgiving與November等詞的正確句。", "句子正誤判斷要求在語境中核對專有名詞、節日與月份的拼寫格式。"),
            ("xiaogang", "PDF第3頁第31題；四選一判斷句子正誤，涉及句首、專名與句子形式。", "把完整句放在生活語境中比較，需同時檢查語序、句首格式及專名，而非只辨識單一字詞。"),
        ],
    },
    2: {
        "prompt": "The sign asks visitors to identify the art room. Which sentence has the correct end punctuation?",
        "options": ["Which room is the art room.", "Which room is the art room?", "Which room is the art room!", "Which room is the art room,"],
        "correct": "B",
        "explanation": "句子以 Which room 詢問地點，交際功能是直接問句，因此句尾要用問號。句點會把它標成陳述句，驚嘆號傳達強烈情緒而非一般詢問，逗號則通常不能單獨收束完整問句。判斷標點先看說話目的，不是只看句子長短。",
        "strategy": "先讀出句子的交際目的，再選句尾符號：詢問用問號、陳述用句點、強烈情緒才用驚嘆號。",
        "steps": ["讀開頭 Which room，確認句子要求對方提供房間資訊。", "把語意改述成「哪一間是美術教室？」而非告知一件事。", "一般直接問句用問號收尾，所以應選 ?。", "排除句點造成的陳述語氣，以及驚嘆號增加的非必要情緒。", "逗號不能獨自結束這個完整問句；核對後選出句尾為問號的版本。"],
        "order": ["A", "C", "D", "B"],
        "refs": [
            ("xiaogang", "PDF第3頁第31題；辨識含驚嘆句及錯誤疑問句結構的正確句。", "以完整英文句判斷句型與句尾語氣是否一致，作答須看語意和標點配合。"),
            ("dawan", "PDF第2頁第26、28題；比較直接稱呼對象的祈使句與錯誤句型。", "告示／指令型句子依功能組織，標點與稱呼位置須讓讀者辨識句界和對象。"),
            ("guangwu", "PDF第2頁第22題；辨識對特定讀者發出的禮貌指令句。", "考生需由說話目的判讀句型，並留意稱呼語和指令主句的書寫安排。"),
        ],
    },
    3: {
        "prompt": "A school notice gives the start time of a club meeting. Which line is easiest to read?",
        "options": ["The club meets at 4.15 p.m?", "The club meets at 4:15 p.m.", "The club meets at p.m. 4:15,", "The club meets at 4:15pm;"],
        "correct": "B",
        "explanation": "時間先寫小時與分鐘，再以冒號分隔；p.m. 放在數字之後，且完整陳述句以句點結尾。A 把冒號寫成句點又用問號，C 顛倒 p.m. 的位置並以逗號收尾，D 把 p.m. 黏在數字上且留下分號。這些格式差異會增加公告閱讀負擔。",
        "strategy": "時間格式分三處檢查：數字間的冒號、a.m./p.m. 的位置，以及整句的句尾標點。",
        "steps": ["先從句意確認這是陳述社團開始時間，不是在提問。", "核對時與分的分隔符號；標準易讀格式使用冒號，寫成 4:15。", "確認 p.m. 接在時間數字後，並與數字留出空格。", "最後檢查完整句以句點收尾，而不是問號、逗號或未完成的分號。", "只有 B 的時間排列、縮寫位置和句尾符號都符合清楚的公告格式。"],
        "order": ["C", "A", "B", "D"],
        "refs": [
            ("dawan", "PDF第3頁第33題；辨認活動時間四種寫法中不正確的格式。", "該題以時間表達的空格、大小寫及a.m./p.m.位置作為判讀線索。"),
            ("guangwu", "PDF第3頁第33題；比較時間的數字與p.m.多種標記方式。", "同一時間資訊以不同書寫形式呈現，需辨認縮寫、空格和大小寫是否一致。"),
            ("guochang110", "PDF第3頁第37、39題；依派對時間與上課起訖時間選出合乎格式的英文表達。", "把鐘點放進活動情境中理解，並留意at與a.m./p.m.等時間線索。"),
        ],
    },
    4: {
        "prompt": "A flyer announces a one-day science fair. Which date line is clearest?",
        "options": ["The fair is on October 12, 2026.", "The fair is on october 12 2026?", "The fair is on 12 October,. ", "The fair is on October, 12 2026!"],
        "correct": "A",
        "explanation": "這份公告採用常見的美式日期順序：月份、日期、年份；月份以大寫開頭，日期與年份之間加逗號，整句以句點結束。B 漏掉月份大寫和逗號，C 的逗號位置錯且資訊不完整，D 把逗號放在月份後並改成不合語境的驚嘆句。",
        "strategy": "先確認公告採用的日期順序，再檢查月份大小寫、日期與年份間的逗號及句尾標點。",
        "steps": ["讀出公告句子，確認這是在提供活動日期而非詢問日期。", "依本題採用的美式格式排成 Month + day + year。", "檢查月份 October 首字母大寫，日期 12 後、年份 2026 前有逗號。", "檢查逗號沒有錯放在月份之後，並確認日期資訊完整。", "最後選擇以句點結尾、四個格式條件都一致的版本。"],
        "order": ["A", "C", "D", "B"],
        "refs": [
            ("guangwu", "PDF第2頁第25題；核對日期與星期的英文表達是否相符。", "日期題需把月份日期資訊放回對話情境，辨認日期詞序及資訊一致性。"),
            ("guochang110", "PDF第2頁第31、33題；選擇生日活動日期與快閃活動日期的適當英文格式。", "活動日期題比較on、月份、日期序數詞與日期片語的排列。"),
            ("dawan", "PDF第2頁第32題；分辨詢問星期、日期與時間的不同表達。", "先辨認題目要的是日期而非星期或時間，再選擇對應的資料格式。"),
        ],
    },
    5: {
        "prompt": "You are emailing a teacher to ask about a class project. Which opening is the clearest and most appropriate?",
        "options": ["dear Ms Chen", "Dear Chen, Ms.", "DEAR, Ms. Chen!", "Dear Ms. Chen,"],
        "correct": "D",
        "explanation": "給老師的短 email 可先用 Dear 加上恰當稱謂與姓氏，再用逗號結束稱呼行，讓收件人一眼看出正文尚未開始。A 的句首及稱謂格式不完整；B 顛倒稱謂和姓氏順序；C 全大寫、在稱呼後加逗號及驚嘆號，視覺上像喊叫，也不適合一般正式詢問。",
        "strategy": "稱呼行要同時照顧收件人、稱謂順序和正文界線；先確認姓名格式，再看稱呼後的標點。",
        "steps": ["辨認寫信對象是老師，因此採用禮貌而清楚的稱呼，不使用喊叫式全大寫。", "稱謂 Ms. 放在姓氏 Chen 前面，構成 Dear Ms. Chen。", "稱呼行之後用逗號，表示稱呼結束、正文將接續。", "排除把姓氏與稱謂倒置、漏掉句首大寫或用問號／驚嘆號收尾的選項。", "選出同時符合收件人稱呼順序、大小寫和逗號慣例的一行。"],
        "order": ["C", "B", "A", "D"],
        "refs": [
            ("dawan", "PDF第2頁第26題；辨認稱呼特定讀者後，哪個句子是自然且可執行的指令。", "直接稱呼收件人／讀者時，稱呼語與後續句子需清楚分界並符合溝通目的。"),
            ("guangwu", "PDF第2頁第22題；以John為受話者的禮貌提醒句。", "評量以指定對象和說話意圖為線索，辨認禮貌稱呼和訊息安排。"),
            ("guochang110", "PDF第2頁第25題；在對話中依受話者身分選擇合宜稱謂與回應。", "對話題將稱謂放進社會情境，要求依角色與語氣判斷合宜表達。"),
        ],
    },
    6: {
        "prompt": "A lab card lists three actions students must complete before leaving. Which version is easiest to follow?",
        "options": ["1 Wear goggles 2, label the jar; 3. wash hands", "Wear goggles; label the jar; wash hands", "1. Wear goggles. 2. Label the jar. 3. Wash your hands.", "3. Wash your hands. 1. Wear goggles. 2. Label the jar."],
        "correct": "C",
        "explanation": "三項實驗室指令要讓讀者看出數量、先後與每項的界線。C 使用連續編號，每項都以祈使動詞開頭，並用句點分隔，格式平行而且順序明確。A 的編號與標點錯置，B 雖可讀但沒有呈現要求的三步順序，D 則把編號順序打亂。",
        "strategy": "清單同時檢查編號連續性、每項句型平行、項目間標點和行動順序，不能只看是否有列點。",
        "steps": ["先確認任務有三個必做動作，需要清楚區隔各項。", "檢查編號是否由 1、2、3 連續排列，代表依序完成。", "比對每一項都以行動動詞起頭：Wear、Label、Wash，句型保持平行。", "查看每個編號後有句點，句子彼此有明確分界，沒有逗號或分號混用。", "選出格式一致且順序自然的清單；離開前洗手放在第三步。"],
        "order": ["B", "C", "A", "D"],
        "refs": [
            ("dawan", "PDF第3頁第35–38題；閱讀圖書館規則清單並依規則數量與內容作答。", "規則以多項短句呈現，讀者須辨認每條界線、場所限制及可執行行動。"),
            ("guangwu", "PDF第2頁第22題；選出符合課堂規範的祈使句。", "規則題要求把動詞指令寫成清楚可理解的句子，並依讀者情境判斷。"),
            ("guochang110", "PDF第3頁第30題；從教室規範情境選出正確祈使句。", "學校規則透過簡短命令句傳達行動要求，需辨認句型和讀者能否據此行動。"),
        ],
    },
    7: {
        "prompt": "A student is recording what a teammate said. Which sentence marks the exact spoken words most clearly?",
        "options": ["Mina said; 'I will bring the map.'", "Mina said, 'I will bring the map.'", "Mina said 'I will bring the map'.", "Mina said, I will bring the map."],
        "correct": "B",
        "explanation": "直接引語要用引號標出說話者的原話；引述動詞 said 後以逗號引出引語，句尾句點放在引號內。A 用分號連接不合句構，C 把句點放到引號外且漏掉引述前逗號，D 則沒有用引號區分原話和敘述者文字。",
        "strategy": "先界定引述者的敘述和逐字引語的邊界，再核對引述前標點與引號內句尾符號。",
        "steps": ["找出敘述者的引介部分：Mina said。", "從第一個逐字說出的字 I 開始，到 map. 結束，圈出需要標示的原話。", "用成對引號框住原話，讓讀者知道哪些字是隊友親口說的。", "在 said 後用逗號引出引語，句點放在引號內收束完整引述句。", "排除缺引號、用分號引介或把句尾符號放錯位置的版本，選出符合以上位置關係者。"],
        "order": ["C", "A", "B", "D"],
        "refs": [
            ("xiaogang", "PDF第2頁第26題；在對話回應中以引號標示歌名／原話。", "題目把引號內的文字置於對話語境，要求讀者辨認引號所界定的精確內容。"),
            ("guochang109", "PDF第3頁第21題；從四句含引號的直接話語中辨認合乎對話情境的表達。", "直接引語以引號呈現，考生需把原話內容和外層敘述分開閱讀。"),
            ("dawan", "PDF第2頁第26題；辨認面向特定人物的對話句與訊息界線。", "對話題要求區分說話者、受話者及實際說出的內容，作為直接引語格式的能力參照。"),
        ],
    },
    8: {
        "prompt": "A student is preparing a contact card for a letter to a family in Taipei. Which address line is clearest?",
        "options": ["Sec. 2, Fu-shin Rd., No. 7 Taipei", "No. 7, fu-shin road section 2 taipei?", "Taipei No. 7, Sec. 2 Fu-shin Rd.!", "No. 7, Fu-shin Road, Section 2, Taipei"],
        "correct": "D",
        "explanation": "清楚的英文地址先提供門牌，再寫街道與段別，最後以逗號分隔城市；道路名稱及城市名稱首字母大寫。D 依層級排列資訊並保留清楚的逗號。A 把段別放到道路前且分隔不足，B 大小寫與句尾符號不合，C 把城市放在前面並用驚嘆號結尾，讀者較難依序定位。",
        "strategy": "地址按「門牌／街道／段別／城市」逐層排列，專名大寫；逗號用來分隔不同地理層級。",
        "steps": ["先把地址欄拆成門牌、道路、段別和城市四類資訊。", "檢查讀取順序由較細位置往外延伸：No. 7、Fu-shin Road、Section 2、Taipei。", "道路和城市是地名的一部分，確認專名首字母大寫。", "用逗號分隔門牌、街道、段別和城市，使每一層不黏成一串。", "選出不顛倒城市位置、不插入問號或驚嘆號且層級完整的地址行。"],
        "order": ["C", "D", "A", "B"],
        "refs": [
            ("zhishan", "PDF第3頁第43–45題；讀取醫院抬頭、病人住址、日期與處方等表單欄位。", "實用表單題要求依標籤辨識姓名、地址、日期與指示，並避免把不同欄位混讀。"),
            ("guochang109", "PDF第3頁第23–24題；由履歷表的Address、Telephone與E-mail欄位判斷聯絡方式。", "履歷以標籤和分欄呈現個人聯絡資料；地址文字是可被定位、轉寄或聯繫的欄位。"),
            ("cap111", "PDF第3頁第22題；判斷寄送明信片前還需要補上的聯絡資料欄位。", "郵寄情境要求辨認收件人／聯絡地址在實用書面資料中的功能，題文與選項均另行原創。"),
        ],
    },
    9: {
        "prompt": "A report explains why students used the covered walkway. Which sentence joins the two ideas correctly?",
        "options": ["The path was wet so, we walked slowly.", "The path was wet we walked slowly.", "The path was wet, so we walked slowly.", "The path, was wet; so we walked slowly!"],
        "correct": "C",
        "explanation": "The path was wet 和 we walked slowly 都能各自成為完整子句；so 連接原因與結果時，前面需用逗號標示兩個獨立子句的界線。A 把逗號放在 so 之後，B 直接拼接兩個完整句而成為 run-on sentence，D 在主詞與動詞間誤加逗號，還以分號錯誤切開 so。",
        "strategy": "先確認連接詞兩邊是否都是完整句，再判斷因果方向；so 前的逗號用來標示獨立子句界線。",
        "steps": ["把句子分成原因 The path was wet 和結果 we walked slowly 兩部分。", "分別確認兩部分各有主詞和動詞，因此都是完整獨立子句。", "so 表示前因後果：路面濕，所以走慢；方向與情境一致。", "兩個獨立子句以 so 連接時，在 so 前放逗號，逗號不能移到 so 之後。", "再排除無逗號造成黏接、主詞後多逗號或分號切錯位置的版本。"],
        "order": ["B", "A", "C", "D"],
        "refs": [
            ("xiaogang", "PDF第2頁第20題；在完整句中辨識因果連接詞與標點位置。", "因果關係題要同時讀出前因、結果和連接詞，並檢查標點是否切分句界。"),
            ("guangwu", "PDF第2頁第27題；從完整句比較連接詞與前後分句的正確形式。", "句子判斷要求檢查連接成分如何串接子句，而不是只看單一文法空格。"),
            ("guochang110", "PDF第2頁第32題；辨認因果句與because子句在完整句中的標點及語意。", "因果題需確認原因、結果及句界標點，避免兩種連接方式重疊或句子切分錯誤。"),
        ],
    },
    10: {
        "prompt": "A class is writing a short report about its garden project. Which paragraph order helps a new reader follow the report?",
        "options": ["State the goal; describe two actions the class took; report the result.", "Give the result first; leave out the actions; add unrelated facts.", "Put every idea in one sentence; remove all punctuation; repeat the title.", "List actions and results in random order; use capitals to separate ideas."],
        "correct": "A",
        "explanation": "新讀者需要先知道報告目的，再看到支持目的的行動細節，最後讀到結果；每句各自承擔一個段落功能，資訊便能沿著「為何做—做了什麼—結果如何」推進。B 缺少過程且跳到結論，C 把句界全部抹除，D 的順序和大小寫都不能代替段落組織。",
        "strategy": "用讀者的理解路徑排列段落：目的建立主題、行動提供證據、結果收束；每句只承擔清楚的功能。",
        "steps": ["先問新讀者打開報告時最需要知道什麼：這個園藝計畫想達成的目標。", "接著安排兩項具體行動，讓讀者理解班級如何推進目標。", "把觀察到的結果放在後面，結果才有前述行動作為依據。", "檢查句界是否清楚，一句承載一個相關意思，避免無標點長句或不相干資訊。", "選出依目的、行動、結果排列的段落；這個順序最能讓陌生讀者追蹤報告。"],
        "order": ["A", "D", "C", "B"],
        "refs": [
            ("zhishan", "PDF第3頁第40–45題；先讀運動資訊與醫療表單，再按題目逐層擷取所需資料。", "跨欄位閱讀要求掌握資料標籤和資訊組織，再將證據連到讀者所問的問題。"),
            ("xiaogang", "PDF第3–4頁第33–44題；依連貫短文的事件順序和段落細節回答問題。", "閱讀組織題需追蹤事件、原因和結果在篇章中的位置，不能只抓孤立字詞。"),
            ("dawan", "PDF第2–3頁第29–34題；沿對話與克漏字篇章的前後文補足語意及事件順序。", "篇章題用前後句線索建立連貫關係，讀者需辨認訊息如何逐步推進。"),
        ],
    },
}


def make_ref(item_ref: tuple[str, str, str]) -> dict:
    key, locator, pattern = item_ref
    source = SOURCES[key]
    return {
        "url": source["url"],
        "title": source["title"],
        "year": source["year"],
        "subject": "english",
        "locator": locator,
        "observedPattern": pattern,
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def apply_item(number: int, config: dict) -> list[str]:
    failures: list[str] = []
    path = QUESTION_DIR / f"question-english-performance-4-iv-3-{number}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "draft":
        return [f"{path.name}: refusing non-draft item"]
    old = {option["id"]: option["text"] for option in data.get("options", [])}
    if set(old) != {"A", "B", "C", "D"}:
        return [f"{path.name}: unexpected original option ids"]
    if len(config["options"]) != 4 or config["correct"] not in "ABCD":
        return [f"{path.name}: authored options/correct answer configuration invalid"]
    data["options"] = [{"id": label, "text": text} for label, text in zip("ABCD", config["options"])]
    data["prompt"] = config["prompt"]
    data["answer"] = {"value": config["correct"], "explanation": config["explanation"]}
    data["solutionStrategy"] = config["strategy"]
    data["solutionSteps"] = config["steps"]
    data["examPatternRefs"] = [make_ref(ref) for ref in config["refs"]]
    primary = SOURCES[config["refs"][0][0]]
    data["provenance"] = {
        "origin": "original",
        "license": "All rights reserved",
        "sourceUrl": primary["url"],
        "sourceLocator": "；".join(f"{SOURCES[key]['title']}：{locator}" for key, locator, _ in config["refs"]),
        "authoringNote": "依公立學校公開英文試題之作答能力、書面資料型態與讀者任務重新設計；只借鑑題型與推理模式，不複製原題、選項、表單、篇章或答案。仍待完整內容與授權審查。",
    }
    data["updatedAt"] = date.today().isoformat()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if len(data["options"]) != 4 or len({option["text"] for option in data["options"]}) != 4:
        failures.append(f"{path.name}: option count/text uniqueness")
    if data["answer"]["value"] not in {option["id"] for option in data["options"]}:
        failures.append(f"{path.name}: answer is not an option")
    if len(data["solutionSteps"]) != 5 or any(len(step) < 18 for step in data["solutionSteps"]):
        failures.append(f"{path.name}: five substantial solution steps required")
    if len(data["answer"]["explanation"]) < 75:
        failures.append(f"{path.name}: explanation too short")
    if len(data["examPatternRefs"]) != 3 or any("PDF第" not in ref["locator"] or "題" not in ref["locator"] for ref in data["examPatternRefs"]):
        failures.append(f"{path.name}: refs must have exact PDF page/item locators")
    if any(ref["status"] != "recorded" or ref["reuseDecision"] != "pattern-only" for ref in data["examPatternRefs"]):
        failures.append(f"{path.name}: source status/policy")
    return failures


def main() -> int:
    failures: list[str] = []
    for number, config in ITEMS.items():
        failures.extend(apply_item(number, config))
    paths = sorted(QUESTION_DIR.glob("question-english-performance-4-iv-3-*.json"))
    rows = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    strategies = {item.get("solutionStrategy") for item in rows}
    step_sets = {tuple(item.get("solutionSteps", [])) for item in rows}
    answer_counts = {choice: sum(item.get("answer", {}).get("value") == choice for item in rows) for choice in "ABCD"}
    if len(rows) != 10:
        failures.append(f"expected 10 items; found {len(rows)}")
    if len(strategies) != 10 or len(step_sets) != 10:
        failures.append("strategies/solution steps are not unique per item")
    if min(answer_counts.values(), default=0) < 2:
        failures.append(f"answer positions are not distributed: {answer_counts}")
    if any(row.get("reviewStatus") != "draft" for row in rows):
        failures.append("a question escaped draft status")
    institutions = sorted({SOURCES[ref[0]].get("institution", SOURCES[ref[0]]["title"].split("國中")[0] + "國中") for item in ITEMS.values() for ref in item["refs"]})
    report = {
        "unit": "4-Ⅳ-3：正確書寫格式",
        "checked": len(rows),
        "passed": len(rows) - min(len(rows), len(failures)),
        "failures": failures,
        "status": "pass" if len(rows) == 10 and not failures else "fail",
        "sourceInstitutions": institutions,
        "sourcePolicy": "每題3筆公校原卷的頁碼／題號定位；只改寫能力與推理模式，題文、選項、地址及答案均為原創。",
        "answerPositionCounts": answer_counts,
        "notes": "每題含唯一正解、選項辨析、專屬策略與五步詳解；題目維持draft，不代表整體內容／授權 gate已通過。",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

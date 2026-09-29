# 決策紀錄

## D-469：第三方分享之版本材料須獨立標記、不冒算出版社證據（2026-09-29）

- 使用者允許閱讀網路分享的課本／教學內容作為融合研究，但「可公開讀取」不等於出版者真實性、版次或授權已核實。
- 這類資料須在單元 `versionResearch` 記錄平台、定位、已讀範圍、內容摘要與授權界線；標為第三方分享材料，不得稱出版社官方原書或與出版社直接材料混算。
- 只概述必要教學結構與概念；不得重製原題、題幹、圖像、數值組合、解答或版面。新增來源不會自動升級稿件狀態，教材最終審查仍由使用者交 ChatGPT。
- S-9-1 僅增補一筆南一標示但來源／授權未核之自學講義證據，正文與題庫不重寫。

## D-451：補登社會社2b-Ⅳ-1融合稿並校正三版來源層級（2026-09-29）

- 名冊原為778/791，本課尚未登錄且正文是通用占位；只修此lesson與狀態紀錄，不改題庫、不重寫已登錄融合稿。
- 依官方社2b-Ⅳ-1及KG，核讀南一標示的公校選擇／機會成本計畫（p.7）、康軒標示的阿里山國中部公民計畫（pp.21–23）及翰林標示的新港國中公民計畫（pp.1–2）。逐筆限定為校方採用版本與課程定位證據，並明示非出版社原書；融合選擇成本、基本權與尊嚴、公共參與三種角度，不虛稱三家原書全文已取得。
- 原創虛構校園活動情境及資料卡，寫六段教材，以處境、自述情緒、可行選項、機會成本、證據範圍、參與設計和隱私界線為主線；content.sections與teaching.body逐段同步6/6。新增versionResearch、fusionRecord，教材維持draft供使用者交ChatGPT審查。
- 名冊刷新779/791（98.48%）：learning-content 583/583、learning-performance 196/208、剩12、長文標記609。全庫資料驗證及題源四項最新稽核記於`implementation/reports/social-performance-soc-2b-iv-1-fusion-d451.json`；題目未改，互動規格／自動化QA與commit/push仍待。

## D-446：補登社會社1b-Ⅳ-1應用領域知識解釋生活現象融合稿（2026-09-29）

- 名冊確認 `lesson-social-performance-soc-1b-iv-1` 原未登記；舊學生頁與 teaching 正文是通用占位，publisherResearch 來源錯配。只補此缺稿，不改題庫、不重寫已登記教材。
- 依官方社1b-Ⅳ-1／KG，讀南一標示的Scribd公開校本設計（生活規範與歷史／地理脈絡）、113康軒第一版標示的臺史博教案（地名、地景、族群記憶與復振；姓名標示－非商業性），以及翰林版標示的七年級地理分享課程計畫（地形、人口、土地利用與日常材料；第三方版次待核）。逐筆標出非出版社原書、上傳者／授權與讀取範圍，不冒稱三家完整課本已取得。
- 以虛構社區多地名現象為主線，原創六段：觀察提問、地理／歷史／公民解釋工具、競爭假說與所需證據、來源限制、地圖／公告／訪談資料配對、遷移至商店／招牌／公共空間。content.sections 與 teaching.body 6/6標題正文一致；新增三筆 versionResearch、fusionRecord，reviewStatus 維持 `draft`，由使用者交ChatGPT最終審查。
- 名冊刷新774/791（97.85%），learning-content 583/583、learning-performance 191/208、尚缺17；長文標記604。此為撰寫稿登錄，不等於教材審查完成。全庫結構驗證與專項結果記於 `implementation/reports/social-performance-soc-1b-iv-1-fusion-d446.json`；題庫未改，互動spec/browser QA、commit/push留待後續目標階段。

## D-445：補登社會社1a-Ⅳ-1生活經驗與社會現象融合稿（2026-09-29）

- 融合稿名冊確認 `lesson-social-performance-soc-1a-iv-1` 未登記；原學生頁與教學正文皆為通用占位，舊 publisherResearch 把學校課程計畫泛稱章節級證據。只修此缺稿，不改題庫或其他已登記稿。
- 依官方社1a-Ⅳ-1／KG，對照南一111地理教材簡介本第三方鏡像p.23、康軒標示民族實驗國中八年級公民計畫（搜尋索引級，PDF本次無法直讀）、翰林標示民生國中課程計畫索引，以及官方CPI定義。三筆版本線索的證據強度與內容範圍不同；公校計畫不是出版社章節，第三方鏡像授權與康軒原文均未核，不宣稱三版課本全文已取得或逐頁比較。
- 重寫六段原創教學，以家庭收據→CPI定義→明示假想數據的加權消費籃→經濟／地理／公民交叉解釋→漲幅／價格迷思→社會研究遷移為主線。學生頁與 teaching.body 逐段標題及正文6/6相同；新增 versionResearch／fusionRecord，lesson 維持 `draft` 供使用者交 ChatGPT 審查。
- 名冊刷新為773/791（97.72%）：learning-content 583/583、learning-performance 190/208、尚缺18；長文標記603。此數字僅為融合稿已撰寫登記，不代表來源完整或審查完成。題目未改，不重跑最近已通過之題源帳本；互動規格、browser QA及commit/push仍待目標後階段。驗證結果記於 `implementation/reports/social-performance-soc-1a-iv-1-fusion-d445.json`。

## D-421：補登社會歷史歷1b-Ⅳ-2因果分析融合稿（2026-09-29）

- 名冊確認 `lesson-social-performance-hist-1b-iv-2` 未登記融合稿；原學生頁和教學六段為泛用占位，publisherResearch錯連地理／公民計畫。只補此缺稿，不重寫已登記稿、不改題庫；相鄰歷1b-Ⅳ-1已於D-420完成且不重寫。
- 依官方歷1b-Ⅳ-2／KG，核讀南一111教材簡介本第三方鏡像p.7（章節／編輯方向，真實性與授權未核）、康軒標示淡水國中114八年級下計畫pp.1–3（保路—湖北調兵—武昌起義—省份響應）及翰林標示鹿草國中113八年級下計畫PDF p.24（革命運動、辛亥意義、資料蒐集／討論）。公校計畫不是出版社原書；只描述公開來源可見差異，不推稱課本全文逐頁融合。
- 參照臺史博戰後紀念物藏品說明、UC Press學術專書章節和學術因果史觀評論，原創六段課文聚焦長期背景、組織累積、局勢促成、直接觸發與結果擴散；練習逐條檢驗因果箭頭、必要／充分條件與反事實證據限制，與歷1b-Ⅳ-1的人物角色網絡課明確區隔。正文與學生頁6/6同步，lesson維持draft供使用者ChatGPT最後審查。
- 名冊刷新769/791（97.22%）：learning-content 583/583、learning-performance 186/208、剩22。題目未改，沿用D-438即時稽核10,566/10,566 recorded、pending 0；互動spec/browser QA後續處理。全庫資料驗證及提交仍待。報告：`implementation/reports/social-performance-hist-1b-iv-2-fusion-d439.json`。

## D-420：補登社會歷史歷1b-Ⅳ-1融合稿並校正錯置版本來源（2026-09-29）

- 最新稿件名冊未列 `lesson-social-performance-hist-1b-iv-1`；原學生頁及六階段正文是泛用占位，既有publisherResearch則誤連地理／公民計畫。只修此單元與狀態報告，不重寫已登記教材或題庫。
- 依官方歷1b-Ⅳ-1／KG，核讀南一版111教材簡介本第三方鏡像p.7（來源真實性與授權未核實，只作章節和編輯方向證據）、康軒標示淡水國中114八年級下課程計畫pp.1–3（保路、湖北調兵、武昌起義及多省響應）及翰林標示鹿草國中113八年級下計畫PDF p.24（民國建立、革命運動、史料蒐集／討論）。兩份校案非出版社課本，不能宣稱已取得三家原書逐頁材料；來源強弱與差異界線記於lesson。
- 新寫六段單元專屬課文，以孫中山、黃興、湖北革命團體與新軍參與者的不同時間／角色解釋人物—事件關係；區分背景、局勢、觸發與選擇、現場行動及政治結果。參考中山學術資料庫《國父年譜》條目與臺史博戰後紀念卷軸，分辨後編年譜、紀念敘事和事件當日記錄的證據限制。學生頁與teaching.body逐段同步，lesson維持draft供使用者ChatGPT最終審查。
- 稿件名冊刷新768/791（97.09%），learning-content 583/583、learning-performance 185/208；23篇未登錄。題庫未改，沿用D-422題源帳本10,566/10,566、pending 0。規格互動與browser QA仍待後續，未commit/push。報告：`implementation/reports/social-performance-hist-1b-iv-1-fusion-d438.json`。

## D-419：補登社會歷史歷1a-Ⅳ-2融合稿（2026-09-29）

- 融合稿名冊確認 `lesson-social-performance-hist-1a-iv-2` 未登錄；僅修改此缺稿，保留所有既有登記稿與題庫。新寫六段學生可見課文並逐段同步 `teaching.body`，教西周分封、戰國郡縣擴展、秦統一及漢初郡國並行的制度變遷，明確拆解時間順序／因果、延續／改變、群體影響與資料限制。
- 依官方歷1a-Ⅳ-2、KG及南一昇平國中、康軒竹崎高中國中部、翰林新港國中八年級歷史公校課程計畫；另核對教育部、故宮與中研院公開材料。校方計畫是版本標示與課程脈絡證據，不是出版社課本全文，因此不宣稱完整課本文本比較或出版社獨有差異；相關界線記於lesson及fusionRecord。
- 目標Schema通過、學生頁／教學正文6/6一致；融合稿名冊767/791（96.97%），learning-content 583/583、learning-performance 184/208。全庫資料驗證通過14,547 JSON／13,114 IDs／1,032 KG。題目未修改，沿用D-422已驗證題源帳本10,566/10,566、pending 0。互動規格與瀏覽器QA、commit/push仍屬整體目標待辦；教材最終審查交使用者ChatGPT，不是Codex gate。詳報 `implementation/reports/social-performance-hist-1a-iv-2-fusion-d437.json`。

## D-418：補寫名冊缺漏英文 9-Ⅳ-2、逐題中文詳解與互動驗收（2026-09-29）

- 最新融合稿名冊確認 `lesson-english-performance-9-iv-2` 缺少至少六段教學與 fusionRecord，故只處理此缺稿；既有名冊稿、課題外題目均未重寫。正文六段同步至學生頁，依官方9-Ⅳ-2／D-Ⅳ-2教比較判準、分類一致性、先篩後排、單位與同值保留。
- 來源核對：直接閱讀翰林公開閱讀教學PDF第17頁，該頁標示D-Ⅳ-2並示範生活情境閱讀、閱讀前中後策略與由基礎到深度思考；僅改寫方法、不複製原題。南一與康軒只找到官方入口，未取得本課出版社章節；公校旅行規劃課程計畫未確認出版社，不錯標版本。出版社證據維持 pending／supplement-only，不宣稱完成三版本章節融合。來源與界線見 `implementation/reports/english-performance-9-iv-2-fusion-d418.json`。
- 保留本課十題原題幹及紙本層級 pattern-only 公校考題來源，將正解位置分布為 B/C/D/A/B/C/D/A/B/C，逐題增補繁中理由、十種獨立策略及五步解題；lesson/questions 維持 draft，教材最終審查交使用者 ChatGPT，非 Codex gate。
- 新增四步 GuidedChoice，修正錯標 `LanguageTimelineBlock` 規格與測試。Node及授權環境Python Playwright通過：六段／四步可見、鍵盤錯答重試和正答回饋、Axe 0 violations／0 incomplete、320／375／768無溢位、0 page errors。規格1,027／0錯誤、24 eligible／1,003 pending；資料14,527 JSON／13,114 IDs／1,032 KG；索引1,052課／10,566題／40 mappings；稿件名冊750／791（94.82%）。本輪未重跑完整npm test／全站browser smoke，未commit/push。

## D-417：最終融合教材審查由使用者交 ChatGPT，Codex 不設審查完成 gate（2026-09-29）

- 依使用者明確指示，lesson／題庫的 ChatGPT 內容審查不屬 Codex 本輪完成條件；Codex 不執行、不等待、不要求 `content-reviewed`，也不以 Terra 或真人審查阻擋融合撰寫進度。最終教材審查由使用者自行交 ChatGPT。
- 融合撰寫百分比只按 `scripts/inventory_authored_fusion_drafts.py` 的稿件名冊條件計算；lesson 的 `draft` 保留為尚待使用者審查／發布狀態，不代表稿件未寫。出版社來源證據與技術規格 QA 仍各自獨立列示，不得混成教材審查 gate。
- 本次規格 `qaStatus: verified` 僅表示 9-Ⅳ-1 的互動及技術契約經 Node／授權 Playwright 驗證；不代表教材內容已審查。名冊 749／791（94.69%）未因改 gate 增減；下一缺稿 9-Ⅳ-2 仍待處理。

## D-416：依可核實來源界線融合英文 9-Ⅳ-1 並修正學生頁元件（2026-09-29）

- 名冊缺稿 `lesson-english-performance-9-iv-1` 原正文只有四段概括文字，無 `fusionRecord`，規格卻錯配 `LanguageTimelineBlock`。故它不屬於已登錄稿，不構成重寫既有完成稿；本次依官方 9-Ⅳ-1／D-Ⅳ-1 重新寫六段教學，加入四步 GuidedChoice，調整規格與學生頁回歸測試。
- 來源以可證範圍記錄：永慶高中九年級翰林第6冊計畫列有 9-IV-1，但沒有獨立對應章節；基隆市康軒第五冊公開教案將 9-IV-1 融入圖片／標題預測、閱讀問答、problem-solution organizer 與口頭說明；楊梅高中南一七年級計畫只作相鄰年級先備／評量參照。教育部委辦英文教學資源提供不同材料的推論教學例型，但其 CC BY-NC-ND 資源不被複製或改作。
- 正文融合的是可核實的「預測—回到線索—整理多訊息—說明」支架，新增證據範圍、不確定度及額外假設檢查；明確不宣稱完成三家九年級課本章節逐頁比較。未找到的版本章節維持 pending。
- 原有十題保留題幹與公開考題來源，答案位置調整成四種選項分布，新增逐題繁中答案理由、獨立策略與五步詳解；來源引用仍為 pattern-only，不宣稱原卷逐題定位。
- 專項 Node／Playwright（鍵盤錯答重試、正答回饋、axe、320/375/768px）通過；全庫資料與規格驗證亦通過。融合名冊刷新為 749／791，來源帳本四項當前稽核仍全數通過、pending 0。此為單元進度，不代表整案完成、真人審查或 commit/push。

## D-415：融合撰寫名冊與使用者教材審查狀態完全分離（2026-09-29）

- 重申並落實 D-395：Codex 不做、不等、不設 ChatGPT／Terra 教材審查 gate。融合撰寫進度只回答 `scripts/inventory_authored_fusion_drafts.py` 名冊中已登錄的稿件；`content-reviewed` 是使用者後續審查所用狀態，不是本任務完成條件。
- 依目前工作樹重新執行名冊：747／791（94.44%）；learning-content 583／583，learning-performance 164／208。登錄條件為至少六段 `teaching.body` 且 `fusionRecord.llmSynthesisNote` 非空。此數字是「符合名冊結構的已撰寫稿件」，不宣稱內容已由 ChatGPT 審查或可發布。
- publisher evidence、版本來源完整度、lesson `draft`、spec QA 與獨立性診斷分開呈現，不得扣除已登錄稿件、不觸發重寫，也不得將待審查誤報為融合撰寫未完成。此輪只校正規約與進度紀錄，未改寫 lesson／題庫。

## D-414：修正英語文化與習俗學習內容代碼 C-Ⅳ-4／C-Ⅳ-5 對調（2026-09-29）

- 稽核英文 8-Ⅳ-6 時發現專案 `curriculum/english/content-c-iv-4.json` 將 C-Ⅳ-4 標成「尊重欣賞文化」、`content-c-iv-5.json` 將 C-Ⅳ-5 標成「基本世界觀」；這兩個概念與官方英語課程手冊的代碼對照錯位。國教院英語課程手冊官方 PDF（2017 定稿版）第 94 頁明列 C-Ⅳ-4「基本的世界觀」、C-Ⅳ-5「國際生活禮儀」，且 8-Ⅳ-6-1／8-Ⅳ-6-2 具體展開後者；官方英語課綱另將 8-Ⅳ-6 定義為了解並遵循基本國際生活禮儀。來源：https://www.naer.edu.tw/upload/1/16/doc/2017/%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F-%E8%8B%B1%E8%AA%9E%E6%96%87%E8%AA%B2%E7%A8%8B%E6%89%8B%E5%86%8A%EF%BC%88%E5%AE%9A%E7%A8%BF%E7%89%88%EF%BC%89.pdf；https://stv.naer.edu.tw/data/course_outline/pta_18518_3555074_59836.pdf。
- 決定：穩定 ID `cur-english-content-c-iv-4/5` 與 `kg-english-content-c-iv-4/5` 不更名、不互換；依官方代碼修正標題與對應正文：C-Ⅳ-4 改為基本世界觀，C-Ⅳ-5 改為國際生活禮儀。其 lesson、題目、publisher/version research、規格與衍生索引須依正確目標逐項盤點；凡原稿／題目寫的是別的概念，不得只改標題冒充已對齊，須回到來源與 KG 重寫或降為 draft。
- 本決策同時影響後續英文 8-Ⅳ-6 融合撰寫：其直接課綱依據為 8-Ⅳ-6 與 C-Ⅳ-5；未取得的康軒目標章節保持 pending，不得從類似課名或跨年級校案推定。
- 修復驗收必須包含：官方代碼標題一致性、相關 lesson/question KG 對應、規格與 manifest、M4／站台衍生資料及單元測試；不能只以全庫 Schema 通過取代語意核對。

## D-411：8-Ⅳ-3 的來源證據不可把第三方或跨年級資料冒稱版本教材（2026-09-28）

- 來源回查發現舊稿把一份實為翰林國文校案的 PDF 標成南一英文證據；本課改列第三方未驗證 Holiday 摘要為非 publisher evidence，康軒九年級食物文化校案只作跨年級閱讀比較線索，翰林網域資源明標為非目標課本。三家當前年級課本章節證據維持 pending。
- 8-Ⅳ-3 原稿未在融合名冊，因此新增七段單元專屬正文與四步 GuidedChoice，並將十題各自改寫為含答案、解析及五步說明；題源僅借內湖與國昌公校試題的明確頁題型態，不挪用原題。lesson/questions 維持 draft，ChatGPT內容審查屬使用者後續工作。
- 題源帳本之全庫 pending 已是0；因本次替換本課題源定位，重跑來源語義、目錄覆蓋及學段相容：23,141 refs／0 flags、281／281 URLs、410／410 fit。
- 同步修正 implementation spec、manifest、Node 與瀏覽器測試。資料驗證14,522 JSON、spec 1,027／0 errors、target browser PASS、索引1,052課／10,566題／40 mappings。融合稿名冊更新為745／791（94.18%），這是登錄數而非內容審查結論。
- 本次沒有重寫其他已登記教材，沒有派子任務；全庫 `npm test` 與 smoke 未重跑，未 commit/push。

## D-404：版本證據須分清出版社教材與公校版本定位（2026-09-28）

- 每篇 lesson 的版本研究須記來源、頁碼／章節定位、查核日期及可支持主張；公校課程計畫能證明該校採用版本、冊次或列出的資源，不可冒稱出版社教材章節或教法。鄰近年級／相似標題也不可併作本課直接證據。
- 本專案的融合稿完成度以原創稿件名冊統計；publisher chapter evidence、ChatGPT內容審查與spec QA不是同一指標，不得混算或把欄位存在當成出版社實質比對。
- 英文7-Ⅳ-1案例保留來源不足界線：南一與翰林目前僅校方七上版本／字典資源脈絡，康軒只找到九年級同字詞義閱讀課次；以課綱與KG原創補足查義教學，但不宣稱三出版社章節已實質融合。

## D-403：英文 6-Ⅳ-6 既有稿與學生頁同步，校方教案不冒稱出版社版本（2026-09-28）

- 名冊確認本課先前未登記；已有六段原創 `content.sections` 與四步 GuidedChoice，不重寫這些既有內容，只修正未同步的泛用 `teaching.body` 與錯配的 LanguageTimeline 規格，並完成本課融合稿紀錄。
- 課綱定位為英語 6-Ⅳ-6（NAER PDF p.37），KG 為 `kg-english-performance-6-iv-6`。南一、康軒、翰林本輪實讀範圍限於公開數位資源入口／英語資源導覽；指定冊次章節未取得。另讀積穗國中公開教案 PDF pp.1–5 作為校本資源搜尋與成果分享活動參考，不歸因出版社。正文明確保留這些來源界線，不聲稱三家課本章節已融合。
- 學生頁正文與 `teaching.body` 對齊為六段「定義需求→搜尋詞→來源核查→整理改寫→署源卡→分享回應」；四步互動含答案、錯答提示及逐題解析。Spec 改為實際 `GuidedChoiceBlock` 並補上本課目標、迷思、遷移、fallback、鍵盤／窄螢幕測例。
- 驗證：專項 Node、完整 `npm test`（含工作台1,027／1,027）、lesson 全庫資料驗證14,514 JSON／13,114 IDs／1,032 KG、spec 1,027／0 errors（15 eligible／1,012 pending）、站台索引重建與檢查均通過。授權 Playwright 真瀏覽器：六段／四步、鍵盤錯答重試與正答解析、axe 0 violations／0 incomplete、320／375／768無水平溢位、封鎖外網仍可完成、0 page errors。題源帳本沿用 D-402 最近實測10,566／10,566、pending 0；本輪無題庫變動。稿件名冊737／791＝93.17%（只代表已有稿件登錄）。詳報 `implementation/reports/english-performance-6-iv-6-fusion-d403.json`。未派子任務、未commit/push；最終教材審查留給使用者 ChatGPT。

## D-402：英文 6-Ⅳ-5 以公開數位詞彙資源設計查詢教學，教材審查留給使用者（2026-09-28）

- 名冊確認英文 6-Ⅳ-5 原學生稿未登記融合：舊正文為泛用內容、沒有 fusionRecord／互動；本輪僅補此缺稿，不重寫已登錄 lesson、不修改本課或其他題目。
- 依官方 6-Ⅳ-5、KG `kg-english-performance-6-iv-5` 及課綱手冊 pp.101–102，原創設計「明確提問→上下文與詞性預判→查詞條欄位→例句／原句驗證→辨識來源用途→回到閱讀並留紀錄」六段教學及四步 GuidedChoice。
- 南一、康軒、翰林公開材料是數位詞彙資源／詞條功能證據，不是指定冊次章節全文或出版社教法；各家範圍限制明載於 lesson，不宣稱已完成三版指定章節比對。Lesson 維持 `draft`，教材最終審查由使用者交給 ChatGPT；審查不構成融合稿名冊 gate。
- Browser 首輪發現站台 shard 過期、仍顯示舊泛用稿；已重建並檢查索引與 lesson shards，再以真實 Chromium 確認六段新稿確實顯示。
- 驗證：專項 Node、完整 `npm test`、資料14,513 JSON／13,114 IDs／1,032 KG、spec 1,027／0 errors（14 eligible／1,013 pending）、站台索引、專項 Playwright（4步鍵盤錯答／正答、axe 0／0、320／375／768 無溢位、封鎖外網、0 page errors）通過。題源帳本唯讀重驗10,566／10,566、pending 0；融合稿名冊736／791＝93.05%（只代表稿件登錄）。詳報 `implementation/reports/english-performance-6-iv-5-fusion-d402.json`。未派子任務、未commit/push。

## D-401：英文 6-Ⅳ-4 校本跨媒材參考不得冒稱出版社課本融合（2026-09-28）

- 名冊中本課原正文未符合融合稿登記條件：四段短內容外，六段 teaching.body 是泛用占位，缺少 fusionRecord 與互動。只修此缺稿；不覆寫名冊已完成稿或題庫。
- 依官方 6-Ⅳ-4／KG `kg-english-performance-6-iv-4` 撰寫媒材探索路徑與 GuidedChoice。公開嘉義校本教案同列翰林、康軒版本，但教學流程屬校本活動，不能拆解歸因出版社；永豐校方課程計畫未標南一。出版社單元正文與三版本章節差異均未取得，來源與 fusionRecord 如實標 pending／未知，不宣稱三版出版社實質融合。
- 新增媒介專屬線索、直接觀察／推論區分、精確求助、合法分享之六段原創正文與四步互動；spec改為真實GuidedChoiceBlock。Lesson維持draft，最後內容審查留給使用者ChatGPT。
- 單元回歸、lesson schema 1,056／0、資料14,512 JSON／13,114 IDs／1,032 KG、spec 1,027／0 errors（13 eligible／1,014 pending）、站台索引及授權Playwright通過；題庫無改動，沿用D-399來源帳本。名冊735／791（92.92%，只代表有稿）。詳報 `implementation/reports/english-performance-6-iv-4-fusion-d401.json`。未commit/push、未派子任務。

## D-400：英文 6-Ⅳ-3 修復泛用稿及錯置版本依據（2026-09-28）

- 原六段正文是泛用占位，未有互動；publisherResearch 將未核實或非本單元資料記成版本依據。本輪只修正這一課。新教學以官方 6-Ⅳ-3 與課綱所列活動為範圍，獨立設計目標—作品—回饋—修訂—遷移循環及四步 GuidedChoice；不把出席當成學習成果。
- 翰林版校方文件只確認科目／冊次，未能定位 6-Ⅳ-3 教法；另兩份連結版別及單元定位未核實，保留為查找線索而不採作版本內容。沒有宣稱三版本出版社教材已實質比讀。lesson 維持 `draft`，最後教材審查交使用者 ChatGPT。
- 修正與驗證：規格由錯配 LanguageTimeline 改為實際 GuidedChoice；學生頁修正重複顯示。Schema 1,056／0、validate_data 14,511 JSON／13,114 IDs／1,032 KG、spec 1,027／0 errors（12 eligible、1,015 pending）、站台索引、單元Node、完整`npm test`（工作台1,027／1,027）及本課 Playwright 均通過；題庫來源帳本沿用 D-399，不重跑，未改題。稿件名冊 734／791（92.79%，存在統計）。詳報 `implementation/reports/english-performance-6-iv-3-fusion-d400.json`。未 commit/push、未派子任務。

## D-399：英文 6-Ⅳ-2 缺稿補寫並忠實標示版本證據（2026-09-28）

- 融合稿名冊確認本單元原稿不符合納入條件；只重寫這一個缺稿。正文依官方 6-Ⅳ-2 聚焦預覽提問、文本證據、合書提取、核對、依任務整理及間隔重訪；新增四步原創 GuidedChoice，含答案、解析、錯答提示及遷移。
- 可讀來源為南一／康軒版本標示的丹鳳國中公開英語課程計畫，僅能支持計畫列出的策略。翰林下載 PDF 未讀到。上述不是出版社課本或出版社教法，不推稱三版教材完整比較；publisher chapter evidence pending。最終教材內容審查交使用者 ChatGPT，lesson 保持 `draft`。
- 驗證：題源帳本 10,566／10,566、pending 0；語義 23,141 refs／0 flagged；來源目錄492筆、281／281 URL 覆蓋；unit-fit 410／410 compatible。專項回歸、`npm test`、全站 Playwright 1,027／1,027、本課 Playwright（axe 0 violations／0 incomplete、鍵盤、320／375／768、零 page errors）通過。Spec validator 1,027／0 errors、11 eligible／1,016 pending。詳報 `implementation/reports/english-performance-6-iv-2-fusion-d399.json`；未 commit/push、未派子任務。

## D-396：國語文學習表現總綱補齊既有名冊缺稿並驗收互動（2026-09-28）

- 名冊確認 `lesson-chinese-learning-performance` 原只有泛用占位、無 `fusionRecord`，故只補這一篇，不重寫已列名稿件或題庫。依官方課綱解讀表現指標代碼、把行動／條件／品質轉成可觀察證據、對齊任務與評量，再討論支持措施與學習目標的界線；六段學生可見正文與 teaching.body 一致，含五步 GuidedChoice 正解、解析、錯答提示與遷移題。
- 來源有官方課綱PDF定位及三份分別標示南一、康軒、翰林版本的公校課程計畫。它們是校方計畫而非出版社課本／教法；出版社章節研究仍待補，不宣稱已完成三版課本融合。lesson 維持 `draft`，最終內容審查由使用者交給 ChatGPT。
- 將本課 spec 對齊實際 GuidedChoice，並修正共用選項的 `aria-pressed` 狀態及觸控尺寸。驗證：題源帳本唯讀重驗 10,566／10,566、pending 0；融合稿名冊 730／791（92.29%，僅代表稿件存在）；資料驗證、spec 結構、單元回歸、`npm test`、學生頁 Playwright 與全站 1,027／1,027 browser smoke 均 PASS。測試與來源界線詳見 `implementation/reports/chinese-learning-performance-fusion-d396.json`。未 commit/push。

## D-394：5-Ⅳ-9 以廣播行動資訊設計原創教學與真實 GuidedChoice，出版社缺口如實保留（2026-09-28）

- 既有教材六段是泛用占位且無融合紀錄；只重寫此名冊缺稿，不碰已登錄稿件和本課題庫。以官方課綱5-Ⅳ-9及KG為教學範圍；參考公校自編火山新聞聽力課的「重聽、5W1H核對、聽後看稿」流程，但不將校本課程說成出版社教法。
- 六段正文聚焦公告目的、訊息—行動關係、否定／條件／時間詞、原安排到變更的推演、交接測試及安全公告遷移；四段音稿、選項、答案、提示與回饋原創。教材內容審查留給使用者ChatGPT，lesson維持draft。
- 原規格虛構LanguageTimeline，已對齊實際guided-choice播放器／音訊逐字稿／鍵盤重試／解析；Schema增加可選audioLabel以讓ARIA名稱正確表達廣播類別，其他對話類教材保留原預設標籤。
- 驗證：資料14,506 JSON／13,114 IDs／1,032 KG；spec 1,027／0 errors；全套npm test；授權Playwright瀏覽器6段／4步／鍵盤／逐字稿／fallback／320-768寬度；independence strict 614篇／0 failures。語音服務為mock，不代表音訊品質評估。融合稿盤點729／791，僅計稿件紀錄。
- 題源帳本本輪唯讀重驗10,566／10,566、pending 0，沒有修改題庫或重跑題目審查；完整證據見`implementation/reports/english-performance-5-iv-9-fusion-writing-d394.json`。未commit/push。

## D-444：歷1c-Ⅳ-1 撤回錯標的出版社來源並保留來源強度界線（2026-09-29）

- 發現本課舊 publisherResearch 將地理／公民校方課程資料誤標為歷史單元章節證據；撤回錯配，改列可核的歷史課程計畫和其實際支持範圍。公校版本標示不等於出版社教材正文，不得由此推稱讀完三家指定章節。
- 以官方歷1c-Ⅳ-1/KG及可追溯公開版本線索為課程邊界，使用臺灣縱貫鐵路1908年全通的博物館藏品和國史館、檔案管理局史料建立原創史實—詮釋分析課文。南一合併彙編的學校／版本／頁面對應未能核實，明確降級；康軒、翰林材料也只作校方版本／課綱配置線索。
- 原稿未列入融合稿名冊，因此僅重寫此一缺稿；六段學生正文與teaching.body逐段同步並新增versionResearch/fusionRecord。教材維持draft，最終內容審查交使用者ChatGPT，並非融合稿登記gate。
- 驗證：目前公校題源帳本10,566/10,566、pending 0；`validate_data.py` 14,552 JSON／13,114 IDs／1,032 KG通過；新融合稿名冊772/791。互動規格與browser QA未在本輪完成，未commit/push。

## D-443：融合撰寫名冊只記錄已撰寫稿，教材審查由使用者 ChatGPT 負責（2026-09-29）

- 依使用者最新指示，Codex 不做、不等待 lesson 教材內容審查，也不以 ChatGPT／Terra 審查狀態阻擋融合撰寫紀錄。名冊只回答哪些單元已有符合登記條件的融合稿；完成率以 `scripts/inventory_authored_fusion_drafts.py` 實測，不以 spec QA、publisher evidence 或 lesson `draft` 狀態替代。
- 已登記稿件不得為了重新計數而重寫。未登記項目才列為待撰寫；結構名冊本身不宣稱內容正確性、出版社來源品質或審查通過。
- 本次刷新名冊為771／791（97.47%）：learning-content 583／583，learning-performance 188／208，待補20；較長正文標記601僅供描述，不是額外 gate。題庫及 lesson 未改寫，題源帳本沿用D-438最新結果。

## D-393：5-Ⅳ-8 校方課程計畫不得冒充出版社教材，故事筆記互動與實作同規格（2026-09-28）

- 回查發現既有康軒英語來源實為國文課程計畫；撤銷其單元英語證據用途。進一步核對南一來源後，改記大豐國中南一標示計畫：PDF pp.6–7僅見相鄰5-Ⅳ-7與聽力／故事閱讀脈絡，沒有5-Ⅳ-8專屬教法；先前朴子國中計畫不再當作南一證據。翰林標示計畫只作版本／年級脈絡；康軒本課材料未取得，三家教材證據槽均明確 pending。
- 依官方5-Ⅳ-8課綱融合撰寫故事目標、障礙、行動、順序、轉折和結果的精簡筆記策略。官方課綱手冊高階5-V-8故事要素僅作教學靈感，不轉稱為5-Ⅳ-8的官方子項。所有正文、故事、選項、答案及提示原創，不抄錄教材或公開考題。
- 將虛構的 `LanguageTimelineBlock` 規格改為頁面實際 `GuidedChoiceBlock`，含4段不同故事、SpeechSynthesis本機資料路徑、收合逐字稿、錯答提示／正解解析及不可用語音時的誠實備援；規格QA只驗技術契約，lesson內容審查保留給使用者ChatGPT，lesson維持draft。
- 驗證：單元Node／正文一致性、`validate_data.py`、全庫spec 1,027／0 errors、全套`npm test`、授權Chromium本課瀏覽器回歸皆PASS；測試範圍與mock邊界見D-393報告。稿件盤點728／791只表示融合稿已記錄。題源帳本沿用D-385，未修改或重跑。
- 詳報：`implementation/reports/english-performance-5-iv-8-fusion-d393.json`。未commit/push。

## D-391：融合撰寫完成度與 ChatGPT 內容審查分開計數（2026-09-28）

- 依使用者明確指示，Codex 不執行 lesson 教材內容審查；最終內容審查由使用者交給 ChatGPT。不得把此審查設為融合撰寫完成度的 gate，也不得用實作規格 QA 的 eligible／pending 數字代表已寫融合稿數。
- 融合撰寫名冊的明確納入條件為：單元 lesson 有至少六段 `teaching.body` 且 `fusionRecord.llmSynthesisNote` 非空。名冊只回答「哪些單元有被記錄的融合稿」，不宣稱審查、來源充分性、出版社逐章融合或發布狀態通過。
- 目前 `implementation/reports/authored-fusion-writing-inventory.json` 記錄 726／791（91.78%）；learning-content 583／583，learning-performance 143／208，尚缺 65。長文標記 556 是另一個長度統計，不能替代融合稿數。不得重寫已列名稿件，只處理盤點確認缺稿的單元或使用者明確要求修正之處。
- lesson `draft`、publisher evidence 及 spec QA 可依各自資料狀態獨立保留；它們不會把已有融合正文從撰寫名冊移除，也不等於 ChatGPT 已完成審查。
- 驗證來源：稿件名冊 JSON 與 `scripts/inventory_authored_fusion_drafts.py`；本決定未重跑題源帳本、未改教材／題庫。

## D-378：Ac-Ⅳ-2 先保留既有融合，再修學生頁接線與互動規格（2026-09-28）

- 盤點確認 lesson 已有七段本課原創正文及五步 GuidedChoice；因此保留教學成果，核對 teaching.body 與學生可見 content.sections，不以 draft 或來源 gate 未過為由重寫。
- 實作是五步文字選答、三個選項、答錯 retryHint、答對 feedback；移除規格虛構的 TextEvidenceBlock、滑桿、同步圖表、外部 fallback 與預測—操作流程，改成與真實 runtime 一致的句型判讀／歧義處理規格。
- 南一目前只有目次定位，直接教學樣本 pending；康軒來源是第三方自編且標示版本的講義，翰林來源是有限官方教師用資料。不得稱完整三版融合或完整讀完任一版本；lesson 維持 draft。
- Playwright 首次看到九段舊教材，定位為被忽略的 `site/data-index.json` 過期；從目前工作樹重建索引後再跑學生頁瀏覽器測試，確認七段恰顯示一次、五步互動／錯答提示／鍵盤及320／375／768px無溢位、錯誤0。另全站browser smoke 1,027／1,027通過。詳報 `implementation/reports/chinese-content-ac-iv-2-existing-fusion-wiring-d378.json`。
- 全庫結構驗證 14,490 JSON／13,113 IDs／1,032 KG；unit spec 1,027份、0錯誤但QA 1,027 pending；publisher slots 293／3,081 verified、2,788 pending、933 blocked。題源沿用 D-377（10,566／10,566），沒有改題或重複跑題源帳本。未 commit/push，不派子任務。

## D-377：公校試題來源帳本完成重驗（2026-09-28）

- 重跑當前題源帳本：10,566／10,566 題均為 recorded，pending 0；來源語義掃描 23,141 refs、0 flagged；來源目錄 492 筆、題目引用 281 個 URL 全數覆蓋；年級適配 410／410、0 mismatch、0 unclassified。
- 此結論僅關閉公校試題 pattern-source ledger，不代表題目答案、學科品質、著作權或 `content-reviewed` 通過。詳報 `implementation/reports/public-exam-source-ledger-complete-d377.json`；不改題目、不重跑答案審查。
- 依序轉入三版本實質融合；先盤點已有正文與融合報告，保留已完成成果，不因 ledger 欄位或 1,027 規格 pending 數而整批重寫。

## D-376：先盤點既有融合，再校正 S-9-13 來源證據（2026-09-28）

- S-9-13 的六段原創教學、互動、versionResearch 與 fusionRecord 已存在；本輪保留、不重寫。D-375 已修復原稿接學生頁時重複顯示的問題。
- 南一標示第三方分享件 pp.52–63 與翰林官方角柱／圓錐概念摘要已直接閱讀並有定位，publisher slot 僅記為該有限樣本已讀；不代表版次真實性、完整章節或授權核實。康軒目前僅有公校課程計畫／索引線索，維持 pending。
- 修正證據範圍，避免把未直接觀察的活動及評量模式寫成已研究；lesson仍 draft，完整三版本融合、權利／來源與內容審查未通過。詳報 `implementation/reports/math-s-9-13-existing-fusion-evidence-inventory-d376.json`。

## D-375：S-9-13 教學原稿與學生頁重複段落對齊（2026-09-28）

- 對照 lesson、renderer 與真實學生頁後發現：完整六段單元正文已在 `content.sections`，但 `teaching.body` 還保留另一套舊六段；由於標題不同，renderer 將兩套都顯示，形成12段。這是正文重複接線，不是缺少一篇新教材。
- 保留 `content.sections` 已完成的直角柱、正角錐、圓錐、錯解診療與遷移教學；只將同檔 `teaching.body` 的 heading/body 對齊，保留既有 id/phase。加入一致性回歸與真瀏覽器 section count 斷言；不得再以重寫 lesson 解決顯示重複。
- `npm run test:math:s9-13`、全套`npm test`、`validate_data.py`（14,488 JSON／13,113 IDs／1,032 KG）、implementation spec validator（1,027／0 errors／1,027 pending）、site index build/validation（1,052 lessons／10,526 question paths／40 mappings）通過。全站授權 Python Playwright 通過1,027/1,027 traversal，且 S-9-13 實頁斷言六段恰顯示一次、互動／鍵盤／320／375／768px通過、page errors 0。第一次瀏覽器測試因舊 shard 未重建而失敗；重建後同命令通過。
- Publisher evidence ledger 當次重算為292／3,081 verified、2,789 pending、932 units blocked。單元lesson仍draft、spec QA pending；本修補不代表 publisher fusion 或全庫融合完成。公校題源帳本本輪未重跑；未commit/push、未派子任務。詳報 `implementation/reports/math-s-9-13-manuscript-render-dedup-d375.json`。

## D-374：Fc-Ⅳ-1 南一教材簡介的證據界線（2026-09-28）

- 讀取第三方上傳《111南一國中生物教材簡介本》第7頁；可直接觀察七下第二冊第4章及其小節順序，生態系組成位於交互作用之後、能量／物質循環及生態系類型之前。
- 此材料是章節簡介而非學生課本正文；上傳者、實際版次與授權均未核實。只更新可支持的章節定位與融合差異，不推論未見的概念展開、圖表或題型，不標 publisher slot verified。
- Fc-Ⅳ-1 原有六段 lesson 正文與互動已存在，全部保留；本次只補 source locator、evidence boundary 和 research report。lesson 維持 draft，完整南一正文及三版本內容審查仍 pending。
- 題源帳本本輪未重跑；全量帳本最近快照仍為 10,566/10,566 recorded、pending 0。

## D-373：既有教材先盤點並修復顯示／互動契約（2026-09-28）

- Fc-Ⅳ-1 已有六段單元專屬 lesson、三版來源研究紀錄、fusionRecord 與四步互動；本輪保留正文，不因 draft 或 evidence gate 未過而重寫。
- 真實渲染檢查發現專屬 ecosystem-scale-boundary 分支被 learningDesign 快速返回攔截；schema enum 漏登新模型；規格學生頁只渲染首個互動 block；browser smoke runner 將 component-visual-body 假設為唯一元素。逐項修正並新增 Fc-IV-1 JSDOM contract，且全庫 workbench-contract 對每一互動 block 驗證 render 數量。
- `GuidedChoiceBlock` 與 `SystemRelationshipBlock` 均由 YAML 明確列出；lesson 的實際四步選答仍以 lesson JSON 為資料來源。Spec QA 維持 untested，不把自動化契約測試誤標為 QA gate 已核准。
- 驗證：專項 JSDOM PASS；`npm test` PASS、workbench 1,027/1,027；資料驗證 14,486 JSON／13,113 IDs／1,032 KG；implementation spec 1,027／0 errors／1,027 pending；archetype registry 7／28／1,027、0 errors。第一次真實 Playwright 測試揭露 runner 單元素假設，修正後真實系統 Chrome PASS：單元 traversal 1,027/1,027、320/375/768px、鍵盤、accessibility tree、reduced-motion，Fc-IV-1 兩個互動元件均存在，頁面錯誤0（詳 `implementation/reports/browser-smoke.json`）。
- 未重跑 exam source ledger／publisher evidence 全庫工作；未升級任何 lesson；不派子任務、不 commit/push。

## D-366：先盤點既有教材，再只修證實缺口（2026-09-28）

- 本輪全庫唯讀盤點找到 1,052 篇已有 `teaching.body`、合計 6,363 段的 lesson，944 篇具有 commonCore/versionDifferences/originalAdditions 三欄融合軌跡；它們是已有產物，不可因尚未通過來源、內容或 QA gate 而說成「不存在」，亦不可只因 gate 未過就重寫。
- `implementation/reports/existing-lesson-authoring-inventory-d366.json` 是結構盤點快照；欄位存在不等於實質融合完成。後續每次編修先回讀正文、來源、互動、spec、manifest 及頁面，再把缺口分類為缺內容、缺證據、來源誤述、顯示漏接、規格／實作不一致或 QA 未跑。已存在且合格的正文須保留；只有證據不足、內容錯誤／模板化或教法不符時才重寫該單元。
- 已確認 1,037 篇的 `teaching.body` 不完全逐字鏡像 `content.sections`。採 renderer 優先顯示既有 `teaching.body`、舊 lesson 再退回 `content.sections`，以免批量複製／改寫 1,000 多份內容；逐課 browser/contract test 仍需確認學生實際可見及讀屏可用。
- Af-Ⅳ-3 既有七段正文保留原文；本次只接入學生頁、改正原本泛化選擇題與虛構 MapDataBlock 規格、補上來源層級與單元回歸。南一／康軒課文級證據仍待補，lesson 維持 draft。
- 全庫 simulation validator 另發現 155 筆數學／自然 simulation contract 與目前按 KG 推導的預期值不同。該遷移器會批改許多單元，且包含近期反覆出現的 A-7-2；不得無差別執行。須逐類核對既有單元專屬互動、schema 與模型意圖後，分批修正；不以通過 validator 為由覆蓋既有教材設計。

## D-365：Af-Ⅳ-2 翰林公開內容證據層級（2026-09-28）

- 證據：翰林雲端學院國中地理「都市擴張」公開關鍵字頁直接呈現都市範圍外擴、人口／交通／產業活動、向郊區移動及相鄰都市形成都會區的概念。該頁屬翰林出版社網站，但沒有標示特定課本版次，也不是完整學生課本章節。
- 決策：此內容可作為一筆已直接閱讀的翰林公開教學內容證據，將 Hanlin publisher slot 標記 `verified`；此狀態只表示來源內容已讀且有定位，不代表完整課本研究、版次／授權核實、內容審查或發布通過。南一、康軒現有材料僅章節／入口定位，繼續維持 pending，不得宣稱三版本實質融合完成。
- 教材融合：可以自己的話將人口集中、建成區擴張、核心—郊區移動及都會區形成放入單元專屬原創教學；不得挪用來源例圖或文字。必須區別都市人口比例、都會區空間範圍及個人遷移動機。
- 學生頁完整性：`site/app.js` 以 `content.sections` 呈現教學正文；lesson 的 `teaching.body` 六段應完整逐段同步到 `content.sections`，由單元 regression 鎖定，不得以存在未顯示的教學欄位視為已教給學生。

## D-364：地 Af-Ⅳ-1 翰林版本標示內容之證據界線與時序融合（2026-09-28）

- 讀取教育部教材資源中心「翰林國中一下地理課本重點填充(110)」資源 metadata，以及第三方上傳、標題標示翰林七下課本的印刷頁47–50可見文字。來源提供者、版次真實性、出版社認證與教材再用權均未確認；第三方頁標示 All Rights Reserved，教育部資源頁標示僅供教育使用。
- 將 Hanlin source slot 記 `verified`，其含義限定為「已取得並實讀一份版本標示教材內容來源」，不是出版社認證、正版確認、再用授權或完整章節審讀。Nani／Kang Hsuan slots仍pending，不宣稱三版本完成。
- 依讀到的教材概念序列，原創課文補入路網節點時序、運具限制、相關與因果界線；互動加入第四個節點變遷因果判讀步驟。學生教材不複製任何來源原句、圖表或題目。
- 驗證：單元 regression、`npm test`、`validate_data.py`（14,484 JSON／13,113 IDs／1,032 KG）、spec validator（1,027／0 errors，QA 1,027 pending）、strict independence（614／0風險／0失敗）、index check（1,052課／10,566題／40 mappings）、授權 Chromium traversal 1,027／1,027與單元4步鍵盤／錯答回饋／320／375／768px、axe 51 runs／0 violations／6 incomplete均通過。Lesson保持draft；內容／權利審查未通過。
- 本輪全站回歸測試照常包含 A-7-2 舊案例，沒有定向編輯該單元；沒有重跑題源帳本、派子任務、commit或push。

## D-363：Ca-Ⅳ-2 學生頁內容可見性與單元專屬鑑定互動（2026-09-28）

- 將既有六段原創教學正文實際呈現在 `content.sections`，不以非渲染欄位的 `teaching.body` 冒充學生已讀內容；回歸測試鎖定可見內容一致性。
- 互動採虛擬未知溶液鑑定：提供指示劑、虛擬產氣確認、空白及已知對照，並區分觀察與推論；不指示學生實際操作化學品。Schema 登錄專屬模型值。
- 主內容 grid 卡片增加可收縮寬度規則，修正真實瀏覽器 320px 視窗發現的 intrinsic min-width 溢位。
- 驗證：Ca-Ⅳ-2 專項 regression PASS；授權 Chromium 本課測試7個可見區段、4題步、鍵盤與320／375／768px無溢位；全站 `npm test` 列示測試全通過；資料14,483 JSON／13,113 IDs／1,032 KG，spec 1,027份0結構錯誤但QA仍pending，strict independence 614課／0失敗。lesson維持draft；來源、權利及內容QA未通過，不升級發布狀態。
- 未修改 A-7-2；全站回歸測試中執行既有 A-7-2 測例不等於定向重做該單元。未派子任務、未commit/push。

## D-362：Ca-Ⅳ-2 出版商來源重核與證據等級校正（2026-09-28）

- 本輪停止 A-7-2 專項工作。公校題源帳本重核為 10,566／10,566 recorded、pending 0；未改題，因此不重做或重跑來源題目工作。
- 翰林官方教師用《綱好在這裡合併》定位至說明頁10及課本印刷頁34–35，指出氣體製備後設計性質鑑定探究；可核實的是有限教師手冊方向，不是完整課本章節。翰林slot標為verified。
- 南一官方資源頁及康軒官方影音頁本次只核到索引，未取得 Ca-Ⅳ-2 直接內容。刪除原紀錄中無定位依據的版本特定概念、例型、迷思和評量聲稱；兩者維持pending，不以校方課程計畫取代出版社教材證據。
- 將融合說明明確限縮為「課綱／KG＋一份翰林教師手冊方向＋AI原創延伸」，不宣稱三版共識。規格以未知溶液、指示劑／產氣、空白及已知對照與替代解釋作為本課互動設計；lesson仍draft、spec QA仍untested，正式學生頁與互動QA尚待實作驗證。
- 驗證：`validate_data.py` 14,482 JSON／13,113 IDs／1,032 KG；規格1,027份、0 errors、1,027 QA pending；publisher ledger 289／3,081 verified、2,792 pending、932 blocked；目標JSON/YAML解析與`git diff --check`通過。詳`implementation/reports/science-ca-iv-2-source-correction-d362.json`。
- 未派子任務、未commit/push；不得把本輪來源校正等同 Ca-Ⅳ-2 實質融合或完整互動完成。

## D-361：Ca-Ⅳ-1 來源深度分級與一版可讀材料實質融合（2026-09-28）

- 翰林官方八上習作與112版教用《理科祕笈》提供可讀的直接出版社內容；本課以其分離技術與操作判讀重新組織原創課文。該證據足以核實翰林slot，但不等於完整課本章節審讀。
- 南一官方資源頁只列互動實驗標題；南一標示的教師分享PDF由臺師大圖書館託管，屬次級線索而非出版社教材。康軒官方實驗室／遊戲頁只核實單元及媒介標題。本課不得把三家資料寫成同深度或共同內容，Nani/Kang Hsuan slots維持pending。
- 按使用者明確允許的最低一版來源條件，以官方課綱、KG、可讀翰林材料及AI原創教學完成單元專屬融合；磁選、物料盤點和回收目標比較為本課自行設計。蒸餾只作回收水的延伸比較，Ca-Ⅳ-1課綱焦點保留結晶、過濾與簡易濾紙色層分析。
- 版本研究／正文／互動的單元回歸通過，不代表全庫獨立性、內容品質與發布審查完成；lesson仍draft、spec QA仍untested。完整本輪數據和驗證見`implementation/reports/science-ca-iv-1-substantive-fusion-d361.json`。
- 本課回饋需指出具體錯誤推理；因此沿用 Schema 已支援的可選 `retryHint`，新增四個題步的單元專屬錯答提示，並由學生頁在錯答時顯示。Chromium 實測確認鍵盤可操作四階段且320/375/768px無溢位；本輪全科`audit_lesson_independence.py --strict`為614課、0風險、0受影響引用、0失敗。

## D-359：Ba-Ⅳ-3 吸放熱一版可讀材料融合與學生正文顯示修正（2026-09-28）

- 本輪刻意不處理 A-7-2。重新核對南一與康軒原先被引用的頁面後，南一目前公開頁僅列其他冊次的圖解資源；康軒 8 下頁為化學反應、酸鹼中和、反應速率的影音／實驗索引，均不能支撐 Ba-Ⅳ-3 吸放熱正文或宣稱出版社評量重點。兩個 publisher slots 維持 pending。
- 翰林官方 2 下課本第 1 章可檢索節錄（約印刷 p.12）呈現化學反應的能量轉換，並以受熱分解與鐵粉—空氣反應分別示範吸熱／放熱；另有官方教用輔助合檔第 1 章 p.1–2。實際可讀範圍是公開索引片段／輔助頁，並非完整章節逐頁審讀。只將 Hanlin slot 標為 verified，且僅代表這筆有限直接材料已核讀。
- 依使用者允許的一版最低來源方案，融合明確採「一版有限內容＋官方 Ba-Ⅳ-3 課綱與 KG＋AI 原創補足」，不虛稱三版共同主張或已完成三版融合。把翰林例型和本課自行設計的中和對照、冷敷溫降、系統—環境邊界、能量箭頭、雙證據與熱散失限制分開標明；不複製例題、句子、圖表或答案。
- 發現原六段完整 teaching.body 並未顯示於學生實際讀取的 content.sections；學生看到的是較短摘要。已保留目標段，並將原有六段完整單元教學原文呈現於 content.sections，新增精確 parity 回歸鎖定。
- 修正規格把互動錯配為 ParticleModelBlock 的問題，改為 SystemRelationshipBlock，明列本課系統邊界、反應組／對照組溫差、兩類證據與單元專屬迷思／遷移驗收。僅修正設計規格，未改 runtime，故 spec QA 不升級。
- lesson 仍為 `draft`；南一、康軒內容證據、全單元 AI 內容／授權審查及 runtime QA 尚待完成。公校題源帳本沿用先前核對 10,566/10,566、pending 0，本輪未重跑或改題。未派子任務、未修改 A-7-2、未 commit/push。證據見 `implementation/reports/science-ba-iv-3-one-publisher-fusion-d359.json`。
- D-359 驗證補記：專項 regression、全套 `npm test`、資料驗證（14,480 JSON／13,113 IDs／1,032 KG）、規格驗證（1,027份、0 errors、287 verified／2,794 pending、1,027 QA pending）、嚴格獨立性（614／0／0）、索引建置（1,052課／10,566題／40 mappings）、授權 Python Playwright（全站1,027／1,027；本課目標＋完整六段正文均可見）與 axe（51 runs含本課三種寬度、0 violations、6 incomplete）均通過。單課互動模型與合約產生器完全一致；全庫 simulation validator 仍列出其他單元合約失配，不把該全科 gate 冒稱通過。六段正文為先前已寫內容的學生頁呈現補齊，沒有重寫題目或重跑題源帳本；結果已同步至 D-359 報告與狀態文件。

## D-358：科學 Gc-Ⅳ-2 角色—功能—穩定融合與池塘互動（2026-09-28）

- 依官方課綱 Gc-Ⅳ-2「不同生物在生態系中擔任不同角色、發揮不同功能，有助維持穩定」校正本課教學焦點。已將原有六段單元專屬正文補入學生實際讀取的 `content.sections`，並同步規格中的目標、概念、迷思與流程；正文的池塘調查與潮間帶遷移活動均為原創。
- 來源界線：翰林官方公開《理科祕笈》教用學習輔助合檔第45頁可讀到遺傳／物種／生態系多樣性、食物網穩定及威脅因素；它不是完整教科書。康軒目前僅取得官方主題索引，南一僅取得公校課程定位，皆不是出版社正文。故不把三者寫成共同教法、南一與康軒 slots 保持 pending，lesson 維持 `draft`。
- 互動修正：新建 `pond-food-web` 單元專屬模型，滑桿只切換水草擾動的概念情境，呈現可能受影響的取食／分解關係，並明示不是實測食物網、不預測族群數、不代表確定因果；加列 schema enum 與回歸測試。刪除原 learning design 中對本課不適切的相對豐度、功能冗餘、差異中的差異等高階指標，換成本課所需的角色辨識、資料／推論／限制判讀。
- 驗證：本課專項 regression 通過；`npm test` 通過，包含 1,027/1,027 workbench 遍歷；規格驗證 1,027 files／0 errors／1,027 pending；`validate_data.py` 通過 14,479 JSON／13,113 IDs／1,032 KG。Playwright 依賴為 Python 3.14、Playwright 1.58.0、Chromium 1208；正式 URL HTTP 200。隔離執行曾重現 Chrome `SIGABRT`／`EPERM`，在授權環境的同命令 browser smoke 仍執行中，完成後補記。本輪未重跑已完成的 10,566 題來源帳本。
- 完成界線：這次完成的是一課教學可見性、內容與互動模型的本質補強，不代表出版社版本證據 gate、全科獨立性審核、真人審查或 lesson 發布 gate 完成。未處理 A-7-2、未派子任務、未 commit/push。詳細來源、映射及待辦見 `implementation/reports/science-gc-iv-2-role-function-fusion-d358.json`。

### D-358 YAML／workbench manifest 同步與專屬驗收補記

- 核對後確認 `SystemRelationshipBlock` 元件名稱與本課 YAML 相同，未改名；只同步 manifest 對應 Gc-Ⅳ-2 的 Hanlin evidence 為 `verified`，Nani／康軒維持 `book-level-only`。其他 1,026 筆 manifest 未改。
- 修正本課 `initialState.variableValues` 的巢狀結構；互動操作、錯誤診斷、分層回饋和六項 test cases 改為水草擾動、模型與實測界線、潮間帶遷移的明確驗收，避免沿用泛化 placeholder。
- 專項與全套 `npm test`、spec validator（1,027／0 errors／1,027 QA pending）、data validator（14,479 JSON／13,113 IDs／1,032 KG）、strict independence（614／0／0）、manifest parity regression、全站 Playwright（1,027／1,027）及 `git diff --check` 均通過。

### D-358 publisher evidence 帳本補記

- 2026-09-28 再核讀翰林官方教用《理科祕笈》合檔第45頁，已在 versionResearch 標明「教用學習輔助資料，非完整課本」、精確定位及查核日；spec 將 Hanlin 一個 publisher source slot 標為 `verified`。這代表來源材料確實可讀並且已納入原創融合，不代表三版本融合或 lesson QA 通過。南一、康軒仍 pending，lesson draft。
- 全庫 publisher evidence ledger 隨此增加為 286／3,081 verified、2,795 pending；spec 結構驗證仍1,027／0 errors／1,027 QA pending。

### D-358 驗證補記

- 授權 Chrome 全站 browser smoke 通過 1,027/1,027；Gc-Ⅳ-2 學生頁專項測試通過六段可見、鍵盤操作擾動狀態1／2、320／375／768px 無橫向溢位、0 page errors。索引以 `--revision local` 重建並通過驗證（1,052 lessons／10,566 questions／40 mappings）。因此 D-358 驗證段所寫「browser smoke 執行中」由本補記更新為通過；隔離環境的原始 `SIGABRT`／`EPERM` 保留為執行環境差異，不是依賴缺失。

## D-357：英文 Ac-Ⅳ-2 已寫六階段教材未顯示於學生頁（2026-09-28）

- 缺口：`lesson-english-content-ac-iv-2.json` 已有六階段原創 `teaching.body`，但學生頁只讀 `content.sections`，而其中原先只有學習目標與一段導讀，主要教學內容因此不可見。
- 修正：保留既有課文，不另造模板或改寫正文；將六個階段補入 `content.sections`。專項測試逐段核對標題／正文完全一致、七節總數與 `reviewStatus=draft`。`browser_smoke_test.py` 新增正式學生頁斷言，檢查六個單元專屬標題實際呈現。
- 驗證：專項測試及 `npm test` 通過（工作台 1,027/1,027）；`validate_data.py` 14,477 JSON／13,112 IDs／1,032 KG；索引 1,052 lessons／10,526 question paths／40 mappings；授權環境 Playwright 全站 1,027/1,027、本課六段可見、320／375／768px 通過；`git diff --check` 通過。受限環境 Chrome 啟動曾回報 `EPERM`／`SIGABRT`，Playwright 1.58.0 與 Chromium 1208 均已安裝，在授權環境相同命令通過，未重裝套件。
- 完成界線：本次是已寫教材的學生頁呈現修復，不等於出版社版本全文融合；三個 publisher slots 仍 pending、lesson draft、spec QA 未升級。題源帳本唯讀核對 10,566/10,566、pending 0；當前 publisher specs 為 285/3,081 verified、2,796 pending、932/1,027 units pending。無 A-7-2 修改、子任務、commit 或 push。詳 `implementation/reports/english-ac-iv-2-visible-fusion-d357.json`。

## D-356：英文 Ac-Ⅳ-1 安全標示語用力道與來源證據分級（2026-09-28）

- 本輪重核南一官方 Quizlet 資源頁（詞彙、例句、閃卡、配對、測驗、書寫活動）、翰林官方國中英語數位網（情境 Podcast、閱讀測驗、視覺化與互動資源）；嘗試讀康軒官方英語 XML，但瀏覽工具明確回報不可存取。這些是數位服務／練習媒介證據，不是出版社課本全文，不能拿來宣稱三版概念內容已融合。
- 額外核對教育部委辦、國立臺中教育大學製作之 Warning Signs 教學資源（對應 Ac-Ⅳ-1、3-Ⅳ-3；頁面列安全標示與安全教育，授權 CC BY-NC-ND 3.0 Taiwan）。只採其可核對的教學範圍作為補充研究，不轉錄影音、標示清單或練習，也不改作原資源。
- 實質落地：在 Ac-Ⅳ-1 學生可見課文加入「提醒注意／要求具體動作／禁止進入」語用區別及反向迷思（警示語氣不等於全面封鎖；明確限制也不可弱化），同步加入 spec misconception I02 與測例、SignReadingLab regression。新段落保留學生可見內容與 lesson 教學正文一致。
- 狀態界線：本課既有來源材料已記錄，但本輪直接讀到的南一、翰林資料仍非 Ac-Ⅳ-1 版本正文，康軒 XML 未能重讀；三個 publisher slots 均維持 pending，lesson `draft`，spec `qaStatus: untested`。這是本單元來源知情的原創補強，不等於完成三版本實質融合或內容審查。完整來源→取捨→正文追溯見 `implementation/reports/english-ac-iv-1-warning-sign-fusion-d356.json`。
- 驗證：SignReadingLab 專項及全套 `npm test` 通過（工作台 1,027/1,027）；資料驗證 14,476 JSON／13,112 IDs／1,032 KG；全規格 1,027／0 errors／1,027 pending；strict independence 614篇／0 risks／0 affected references／0 failures；JSON parse 與 `git diff --check` 通過。未重跑公校題源帳本，未重開 A-7-2，未派子任務，未 commit/push。

## D-353：S-9-13 例題數值重合修正與獨立互動模型（2026-09-28）

- 更正 D-352 的敘述：當時稱「自編數值、例題均未複製」不準確。其可見直角柱例題與南一標示第三方分享件 p.52–53 的 3-4-5 底面、柱長10數值組合相同；因此不以文字重寫視為充分獨立。
- 將學生正文改為 8-15-17、柱長3的直角柱（S=240 cm²、V=180 cm³），錯解、互動預測及 7-24-25、柱長2遷移題同步重算；圓錐數據亦換為半徑4、母線7。採新模型 ID `s9-13-prism-surface-volume-v2`，舊 renderer 保留相容，模型數值由 lesson 的 `prismModel` 資料驅動。同步更新 schema、spec與來源重合回歸。
- 新例題為作者重新選擇的畢氏數組與獨立推導，避免沿用來源例題參數；但這不等於已完成出版社全文融合或授權核實。專項與全套npm tests、資料驗證（14,474 JSON／13,112 IDs／1,032 KG）、spec驗證（1,027／0 errors／1,027 pending）、strict independence（614／0風險／0失敗）、正式Chrome（1,027/1,027、三種viewport、本互動與鍵盤）及axe（48 runs／0 violations／6 incomplete）通過；站台索引1,052課／10,526題路徑／40 mappings，diff check通過。lesson維持draft、三版slots pending、spec QA未升級；已完成題源帳本不重跑，A-7-2不重開。詳報`implementation/reports/math-s-9-13-source-overlap-correction-d353.json`及更新後`implementation/reports/browser-smoke.json`。

## D-352：S-9-13 依可讀來源深化原創融合並修正互動答案鍵（2026-09-28）

- 來源核讀：南一版標示的第三方分享講義 pp.52–63 可讀到柱體、角錐、圓錐依序的展開與表面積／體積教學；分享權利及版次未獨立核實。翰林官方角柱、圓錐概念頁分別核對多邊形底面與矩形側面、面積逐項加總／柱體底面積乘高，以及圓底面加扇形側面；翰林官方影音目錄另列3-1角柱圓柱、3-2角錐圓錐及暖身／基礎／精熟索引，但本輪未播放影片。康軒官方九下影音目錄只確認第3章立體圖形，未讀影片或正文。來源強度不一，沒有冒稱三版完整章節融合，也不升級publisher slots。
- 融合落地：學生可見正文改成有來源依據但由本課作者重新組織的概念階梯：角柱「兩底＋逐片側面」表面積清單與「底面積×柱長」體積分流→正角錐底面／側面三角形加總及斜高界線→圓錐從扇形弧長等於底圓周長推導側面積。自編數值、例題、錯解診斷、遷移、圖形及互動均未複製來源內容。新增研究定位、sourceRefs及source-to-synthesis回歸。
- QA發現：lesson互動 step-1、step-4 答案鍵均與自身數值解析矛盾，原本標A但計算支持B；兩處更正為B並將回饋與鍵值一致，新增 regression。
- 驗證與界線：lesson仍`draft`；南一分享權利／版次、出版社完整章節閱讀、內容審查均未完成；三 publisher slots維持pending，spec `qaStatus`維持untested。題源帳本最近核驗10,566/10,566、pending 0，未因本次教案研究重跑。未派子任務、未commit/push。詳細報告 `implementation/reports/math-s-9-13-publisher-informed-fusion-d352.json`。

## D-352 狀態佇列校正：撤銷 S-9-1 題庫超綱舊待辦

- D-346 留下「S-9-1 十題中多題超出範圍」與需重寫的下一步；該說法已被其後 D-347 的實際逐題核答與範圍回歸取代。當前題目按目前回歸涵蓋多邊形相似範圍，不應再依舊待辦重寫；除非新增課綱證據或題目有內容變更，不重跑題庫工作。
- 狀態紀錄也曾錯稱 `currentNextAction` 已更新；實際仍保留上述過時字串。現在將佇列改為出版社實質融合及全庫規格／互動／自動化QA缺口，不再把 A-7-2 或 S-9-1 當預設回頭項目。

## D-351：S-9-13 直角三角柱專屬互動與瀏覽器驗收（2026-09-28）

- 缺口：D-350 只修正學生可見教材，尚未修互動。舊通用幾何模型操作三角形底／高，無法呈現本課直角柱表面積與體積；舊互動宣稱長方體／圓柱並超出本課設定。
- 決策：指定 `math-geometry` 專用模型 `s9-13-prism-surface-volume`。3-4-5 直角三角柱先提交柱長4增至6的預測，再解鎖立體圖、三角柱展開圖、逐面表格及鍵盤滑桿；表面積 `12+12L`、體積 `6L` 同步更新。另用5-12-13底面與柱長2作遷移，並提供錯答提示、四步導覽、重設及文字替代。正解未提交前不解鎖示範；提交後答案與依據可見。
- 範圍：本模型只教 S-9-13 所需直角柱體積；錐體／角錐內容保留於正文但不外推其體積公式。來源有限且publisher slots、內容／版權審查未完成，lesson仍`draft`，implementation spec的`qaStatus`仍待QA結果與內容審查 gate，不自動升級。
- 驗證：新增專項 Node/JSDOM regression、正式 Chromium smoke 的 S-9-13 錯答提示／重試、預測解鎖／鍵盤滑桿／遷移／重設／320、375、768px檢查均通過；全站1,027/1,027 traversal通過。axe 48 runs、0 violations，但3項color-contrast incomplete因漸層／SVG遮疊無法自動判定，尚不算完整contrast gate。全套`npm test`、資料14,473 JSON／13,112 IDs／1,032 KG、spec 1,027／0 errors／1,027 pending、strict獨立性614／0風險／0失敗、索引1,052課／10,566題／40 mappings及`git diff --check`通過。詳見 `implementation/reports/math-s-9-13-interaction-d351.json`。
- 工作流程更正：A-7-2核心內容於D-342、D-343完成後不應重開；後續依序已做地 Af-IV-1、S-9-1、Aa-IV-1、Db-IV-6、S-9-13。`currentNextAction`更新為當前真實待辦，避免舊敘述造成「仍在做A-7-2」的錯覺。未派子任務、未commit/push。
- Gate：publisher slots不變、lesson維持`draft`、spec `qaStatus`仍`untested`（全庫實施規格完成門檻仍pending，且contrast自動檢查有3項incomplete）；本次已完成該互動功能與大部分自動化驗收，但不代表出版社融合、教材內容或全庫QA完成。題源帳本沿用最近核驗10,566/10,566、pending 0，未重跑。未派子任務、未commit/push。

## D-350：S-9-13 學生可見教材與來源強度校正（2026-09-28）

- 缺口：原 lesson 的六段教學正文不在學生頁實際讀取的 `content.sections`；該欄只有三句泛化摘要。另曾把校方課程計畫／平台目錄寫成出版社教學差異，證據強度不足。
- 融合與撰寫：學生頁改為六段單元原創教學，依序分辨外殼與內部空間、直角柱列面求表面積及底面積乘高、圓錐扇形弧長回接底圓、正角錐側面與底面、單位／公式錯解診斷、無底展示罩遷移。所有算式自行設計；課綱範圍限制本課只教直角柱體積，不推廣圓錐或角錐體積。
- 來源核讀：核讀南一標示第三方分享講義 pp.58–61、均一標示「類南一版／類康軒版」課程路徑及南一／康軒／翰林採用校方課程計畫。路徑／課程計畫不是出版社正文；分享件權利及版次未核實。來源鏈支持範圍、教學排序和錐體展開概念，不構成三家現行教材完整閱讀或publisher slots通過。詳細追溯見 `implementation/reports/math-s-9-13-visible-fusion-d350.json`。
- 驗證：`npm run test:math:s9-13`通過；`validate_data.py`為14,472 JSON／13,112 IDs／1,032 KG；strict independence為614篇／0風險／0失敗；報告與`project-state.json` JSON解析及目標`git diff --check`通過。題源帳本本續作已核對10,566/10,566、pending 0，未重跑。
- Gate：publisher slots不變、lesson維持`draft`、spec QA維持`untested`；本次修復的是學生可見內容與來源主張，不代表全單元審查或互動QA完成。未改runtime，未執行瀏覽器QA；未commit/push。


## D-349：Db-Ⅳ-6來源強度校正、可見融合教材與植物運輸專屬互動（2026-09-28）

- 來源核讀：翰林官網113教用／學用 PDF 的可索引預覽定位課本4-1 pp.106–111，見維管束細胞、莖／葉脈排列、形成層／年輪與個讀—討論流程；完整PDF本輪無法直接開啟。南一111配套簡介本是第三方上傳的有限公開預覽；康軒113版ShareClass頁僅能確認分享者標示、年級與3-1構造／3-2物質運輸分節，內頁無法讀取。版次／分享權利未獨立核實；均不得冒稱三版出版社正文已逐頁讀完。另讀教育雲「發現維管束」資源頁，標示CC BY-NC-SA 4.0，作概念與教學資源旁證。
- 融合落地：把既有六段原創 Db-Ⅳ-6 教學正文全數接至學生實際讀取的 `content.sections`；教學次序聚焦維管束組成與位置、物質—組織對應、染色證據限制、來源—需求與環剝推理。修正版本差異紀錄，只主張來源實際可見的內容，明示南一／康軒材料不可讀與證據不對等。
- 互動／規格：新增 `science-life-system/plant-transport` 專屬呈現，按鈕切換有機養分來源與需求端，文字路徑同步更新；定性蒸散滑桿不產生虛構水量／速率。加入 schema、spec 與回歸測試；修正通用 learningDesign 提前返回遮蔽專屬模型的 renderer 缺陷。
- 測試校正：全站瀏覽器 smoke 的 S-9-1 斷言仍要求舊版「6.8公尺」；對照現行教材及單元回歸後，確認測試過期而非課文回歸，改為核對目前多邊形縮印資料，並加入 Db-Ⅳ-6 實際瀏覽器驗收。
- 驗證：`npm test`通過；`validate_data.py`為14,470 JSON／13,112 IDs／1,032 KG；spec validator為1,027／0 errors／1,027 pending；strict independence為614 lessons／0 risks／0 failures；授權 Chromium browser smoke遍歷1,027/1,027，本課六段、來源／需求切換、滑桿焦點與320／375／768px通過；axe代表性掃描42 runs（14單元×3視窗）、0 violations／0 incomplete；目標`git diff --check`通過。
- 未完成：本課三個publisher slots仍pending、lesson仍draft、spec QA仍pending；完整南一／康軒章節、授權真實性與AI教材複核未完成。這是有限證據上的原創來源知情融合草稿，不是已完成出版社三版全文融合或發布審定。未重跑已完成試題來源帳本；未commit/push、未派子任務。

## D-348：Aa-Ⅳ-1 教材比較證據界線與核式散射互動專屬模型（2026-09-28）

- 來源界線：周金城於《臺灣化學教育》第11期（2016）比較其引用的2013年南一、康軒、翰林八上教材；文章指出該歷史版本均直接介紹原子模型，未先說明模型作為表徵、解釋與預測工具的本質。此為二手、舊版比較，不可外推為當前版次逐頁已核讀；現有出版社欄位仍只是公校課程計畫／簡案，publisher slots 保持 pending。
- 融合決策：學生頁改顯示既有六段 Aa-Ⅳ-1 原創正文，不再只呈現三段縮寫摘要；補強模型圖與實物區別、模型預測用途、證據落差及適用限制。正文引用實驗的定性方向，不重製教材文字、題目、圖表或答案。
- 互動決策：`science-particle-lab` 增加明確標為示意、非比例數據的 `rutherford-scattering` 模型，使用最近通過距離滑桿更新定性路徑；不再讓原子模型課錯顯示溫度／固液氣粒子間距。保留其他 lesson 的既有粒子相態模型。
- 缺陷與驗證補記：原 renderer 的 generic-designed early return 曾略過專屬分支；專屬分支也未輸出四步 learningDesign。現已同時修正，回歸測試納入 `npm test`。資料驗證14,469 JSON／13,112 IDs／1,032 KG，spec 1,027／0 errors／1,027 pending，工作台完整遍歷1,027/1,027；授權 Chromium 實際學生頁驗證模型圖、四步、滑桿更新、焦點保留與320px無橫向溢出通過。全站 browser smoke 亦完成1,027單元遍歷與既有A-7-2互動檢查通過；不代表出版商融合或教材內容審查完成。
- Gate：lesson 保持 `draft`，三家 publisher evidence pending，單元 spec `qaStatus=untested`；本決策不等同完整出版社版本融合、授權核實或真人／專家審查。

## D-339：A-7-1 依可讀材料重寫融合脈絡並落實原式／化簡式互動（2026-09-27）

- 來源與證據級別：南一使用均一平台南一標示七上3-1課程資源索引（未逐一觀看影片，非出版社正文）；康軒使用第三方平台標示的六升七先修講義 pp.39–43 有限節錄；翰林使用第三方分享、標示 All Rights Reserved 的七上課本OCR約 pp.151–166，並以翰林官方1A/3-1影音索引補足章節定位。康軒／翰林分享的版次、上傳者權限與重用授權未核實；不得將材料冒稱出版社認證完整課本。
- 融合決策：將可核讀差異改寫成 A-7-1 自己的教學次序：先以單位和固定／變動量建立符號意義，再以字母部分與次方分類同類項，接著用交換／結合／分配律說明整理，最後讓多個輸入值作為錯誤檢查證據。明確指出有限代值不能替代一般化簡的運算律理由；負數代入須保留括號。可見 lesson sections 擴為六個單元專屬教學段，例題、情境、診斷與遷移均為原創，未重製來源題目或表達。
- 工程修正：原 A-7-1 說明了未實作的拖曳標籤、餐券圖示及同步圖表，且錯掛 `math-algebra-balance`。改為 `math-expression-lab`，以 x 滑桿即時比較 `3x＋2＋5x−7` 與 `8x−5`，並提供 x=−2、0、3 的靜態表格、四個單元化步驟及更新後焦點保留。lesson Schema、元件 registry、單元 spec、target regression 與正式 browser smoke 一併更新。
- 驗證：`npm run test:math:a7-1`、`npm test`、`scripts/validate_data.py`（14,462 JSON／13,112 IDs／1,032 KG）、spec validator（1,027／0 errors／1,027 pending）、strict lesson independence（614／0 risks）、授權 Chrome 完整遍歷1,027/1,027與 A-7-1 鍵盤／數值／320、375、768px檢查、axe 33 runs／0 violations／0 incomplete 均通過。完整結果見 `implementation/reports/a7-1-three-source-substantive-fusion-d339.json`。
- 未完成界線：三家完整教材正文、康軒／翰林分享材料真實性與著作權許可、出版社 evidence slot 核驗、內容審查仍未完成；維持 publisher slots pending、lesson `draft`、spec `qaStatus=untested`。本次未重跑公校題源帳本、未派子任務、未 commit/push。


## D-336：A-7-7 專用不等式數線引擎與版本標示材料融合界線（2026-09-27）

- 決策：A-7-7 的既有 `math-algebra-balance` 模擬與課程目標不符，改為專用 `math-inequality-range`，由關係詞按鈕與邊界滑桿即時同步不等式、實／空端點、左右射線及邊界／鄰值判定；lesson互動型別與learningDesign型別同步正式登記於Schema。教學本課限於不等式的意義、解的判準、數線表示及情境可行集合；求解演算法（含負數乘除反向）歸A-7-8。
- 融合證據：加入南一、康軒、翰林版本標示第三方分享的可見內容節錄／索引，分別用作語詞定義、候選值代入判解、數線端點與圖文逆讀的教學支架。原創正文和互動把三種支架重新組織為本課概念鏈，不沿用來源情境、例題、數字、答案或圖表。
- 權利／完成界線：以上分享均非出版社認證，版次與上傳者權限未核實；南一／翰林部分僅有搜尋索引節錄，康軒頁標示All Rights Reserved。僅作有限概念研究，不得稱完整官方版本比讀；三個publisher slots保持pending，lesson為`draft`，spec `qaStatus=untested`，內容審查仍待完成。
- QA需逐項驗證資料Schema、spec、互動引擎的滑桿／四種關係操作、鍵盤、窄螢幕、來源對齊與全庫測試；自動化通過不升級內容審查狀態。

## D-335：A-7-6 以第三方版本標示樣本融合「易作圖點與精確交點」的差異（2026-09-27）

- 證據：閱讀南一標示教材簡介本第三方頁面（內頁p.87）及康軒標示自學講義第三方分享（pp.52–65）；均非出版社認證，上傳者／版次及再利用權利未核實。南一樣本呈現整數解點便於定位的作圖支架；康軒標示講義呈現解點、成線、水平／鉛垂特例、代入判點到交點的學習序列。翰林仍只有官方索引／校方資料，完整教材待查。
- 融合：作圖先採容易定位的整數解點；但聯立交點（8/3，10/3）保留精確分數，逐式代回，不為配合格線取整。新增（3，3）反例，說明它雖通過x+y=6，卻不滿足2x−y=2。來源差異已落在學生可見課文、融合紀錄、來源定位與單元回歸測試；不複製樣本表達／題目／答案／圖表。
- Gate：完整出版社章節、第三方來源真實性／權利、翰林可讀教材及內容獨立性／內容審查均未完成；publisher slots維持pending，lesson維持draft，spec qaStatus=untested。
- 驗證：單元 regression及全套`npm test` PASS；規格1,027份／0 errors／1,027 pending；資料14,457 JSON／13,111 IDs／1,032 KG；正式Chrome全站遍歷1,027/1,027及320／375／768、鍵盤、accessibility tree、reduced-motion通過；axe 24 runs／0 violations／0 incomplete；diff check通過。詳見`implementation/reports/a7-6-two-version-synthesis-d335.json`。題源帳本未重跑，沒有派子任務，未commit/push。

## D-334：A-7-6 使用專屬聯立直線模型並完成瀏覽器互動驗收（2026-09-27）

- 發現：依 KG 一般數學 A 類預設的幾何引擎會呈現三角形面積，與 A-7-6 的雙直線交點不符；通用單直線函數圖也無法呈現兩式同時成立。
- 修正：新增 `math-system-graph` 引擎及 A-7-6 code-specific mapping；以 2x−y=2 與 x+y=c 顯示兩條不同線型、精確交點標示與第二式常數滑桿。互動設計步驟仍與 SVG 圖並列呈現。修正通用探索按鈕群組 ARIA role，避免以 `role=list` 包含按鈕造成 axe aria-required-children 違規。
- 驗證：`npm test`通過；A-7-6專屬 Chromium 驗證兩線、座標替代文字、鍵盤滑桿與320／375／768寬度；專屬 axe 0 violations／0 incomplete。全站 browser smoke 的單元遍歷1,027/1,027、viewport／鍵盤／reduced-motion通過；axe全站24 runs、0 violations／0 incomplete。新增 engine 已納入lesson schema；資料全庫驗證需以本次schema變更後重跑結果為準。報告`implementation/reports/a7-6-system-graph-runtime-d334.json`。

## D-333：A-7-6 單元範圍、版本證據到可見教材追溯（2026-09-27）

- 決策：lesson採單元專屬推進「由方程代入建點並連線→辨認 y=k 水平線與 x=h 鉛垂線→讀唯一交點→把候選值代回兩條原式」。保留精確共同點、近鄰錯點和新情境驗證；A-7-6 不正式擴充平行／重合解數分類。互動四步與模擬均使用同一內容邊界。
- 證據差異與限制：均一南一對齊課程頁提供任務標題／分段，非南一出版社正文；康軒官方入口僅索引，另有採康軒版校方課程計畫作流程旁證，非課本正文；翰林官方頁僅讀資源標題，未觀看影片。來源位置分別記於 lesson、spec `sourceRefs` 與 `versionResearch`；三家出版社完整正文均不得標verified，publisher slots pending。
- 修正：spec原反例將 x+y=6 與 2x−y=2 混寫；更正為 (2,4) 代第二式得0≠2，並補充 (3,3) 只滿足第一式的計算。新增單元 regression 鎖定六段可見教學、互動／例式、算術、來源限制與 draft gates。
- 驗證：`npm run test:math:a7-6`通過；`validate_implementation_specs.py`為1,027份／0錯誤／1,027 pending；YAML解析5筆sourceRefs、`validate_data.py`通過14,454 JSON／13,111 IDs／1,032 KG。題源帳本使用目前既有報告，不重跑；10,566題待補0，語義稽核23,131 refs／0 flagged。報告`implementation/reports/a7-6-scope-fusion-d333.json`。lesson draft、spec qaStatus=untested；未commit/push。

## D-322：D-8-1 限定累積相對次數主線並標清版本證據缺口（2026-09-27）

- 決策：依官方D-8-1與KG，lesson核心改為相對次數、累積相對次數、累積相對次數折線及相鄰累積值差回復單組比例；移除將直方圖作為本課主要學習目標的偏題內容。以自創步行時間資料呈現分母、上限點與差分檢核。
- 來源：南一標示講義為第三方分享索引，非出版社認證；康軒Clearnote筆記頁只見標題且未標版本，正文未能核讀；翰林官方補救GO本輪只有索引，正文不可讀。另查到國教署學習扶助材料公開分享版，可核讀概念但非出版社版本，且分享頁標All Rights Reserved，僅取概念、不複製例題、數值、表圖或表達。來源限制及細節記於`implementation/reports/math-d-8-1-scope-correction-and-source-fusion-2026-09-27.json`。
- Gate：課程範圍和原創教學已收斂，但可讀、可歸屬的三家版本證據不足；本課不計入3,081 publisher slots完成數，lesson/questions保持`draft`，spec `qaStatus=untested`。教材內容審查依使用者要求留待ChatGPT review；自動化結構驗證不替代內容審查。

## D-316：A-8-6 聚焦方程式辨認、解的意義與情境列式（2026-09-27）

- 決策：lesson以化簡後的一元、最高次二及等號條件辨識一元二次方程式，以代入同一候選值後等式兩側相等定義解／根，並從具體量關係建模。禁止在A-8-6教判別式、根數、函數圖交點、因式分解／配方法／公式解等後續內容。互動依「分類→左右代入→情境列式→範圍解讀」逐步驗收。
- 來源：南一標示八上自學講義公開分享摘錄pp.110–113；康軒第三冊標示Clearnote筆記pp.1–2；翰林官方112版補救GO索引pp.149–151與可見111版公開分享摘錄pp.60–61。南一、康軒材料非出版社認證原書；翰林PDF本次直接讀取回403，僅依搜尋可見索引與分享摘錄，不宣稱已讀完整本。課綱A-8-6另列方程式、解及具體情境列式，A-8-7才列解法與應用。
- 理由：既有lesson把課程計畫、均一與章節影音索引當作出版社教學正文，並混入後續求解、根數及圖形內容；這既不足以證明版本融合，也超出本單元學習內容。使用者允許閱讀公開分享材料後，本次依可讀的單元材料逐家比較並獨立重寫，明確保留來源權威與存取界線；未複製原教材題目或文字。
- lesson維持`draft`；spec `qaStatus=untested`。自動化測試不等於內容審查或發布；教材內容review依使用者要求保留給ChatGPT，無Terra審查。

## D-306：3-Ⅳ-5 生活用語以線索核對和情境轉接呈現（2026-09-26）

- lesson頁採資料驅動 `DailyExpressionLab`，用三個溝通任務明確區隔澄清、事故後道歉補救、婉拒邀請；學生先標記造成回應差異的上下文線索，才解鎖候選回應。不同媒介的服務簡訊作為遷移，需同時引用地點和期限證據，不能只比對單一關鍵字。
- 例句與互動資料均為原創且由 lesson JSON 提供；規格中的出版商 chapter records 仍屬章節結構線索，full-text comparison／fusion尚未完成。自動化及瀏覽器測試不代表螢幕閱讀器、完整內容／版權或發布 gate 通過，故保持 `draft`／`qaStatus=untested`。

## D-305：3-Ⅳ-4 圖表刻度互動須固定圖形高度並改變每格單位（2026-09-26）

- 使用 `DataExplorerLab` 將既有單元規格的刻度翻轉實驗接入 lesson 頁。學生先預測四格、每格5本的總量，再自行切換至每格10本；固定格數，讓讀值從20變40。解釋必須提及刻度與單位，並以不同借閱資料遷移，不能只憑答案鍵前進。
- 互動資料由 lesson JSON 提供，renderer 負責操作／狀態；回答、提示及重設可離線使用。自動化通過不等於人工瀏覽器、輔助科技、版本融合或內容／版權審查；完成發布 gates 前維持 `draft`／`qaStatus=untested`。

## D-304：3-Ⅳ-16 混合網頁閱讀需在教材頁互動核對區塊功能與證據（2026-09-26）

- 公開 lesson 頁不得以靜態體裁選擇取代單元規格的互動。學生須先預測資訊區塊，再比較說明、日期表、行動公告各自能回答的問題與推論限制；說明理由須引用日期表內容，並在不同主題中重新判斷 why 任務。
- 使用 lesson JSON 驅動來源片段、功能、問題、限制及遷移答案；renderer 只提供共用操作與狀態。資料內嵌以支援離線使用。未完成真實瀏覽器／輔助科技、出版社融合、內容版權及發布審查前，lesson 和題目維持 `draft`，spec `qaStatus=untested`。


## D-301：3-Ⅳ-13 短劇理解以預測、舞台線索、結果與新劇本遷移驗收

- 日期：2026-09-26
- 決策：以 `ShortPlayLab` 取代靜態三題測驗。學生先對 A Clear Path 標題／道具提示寫預測，通過字數門檻後才讀主劇本；六題依序檢查衝突、舞台指示、道具功能、轉折、結局主旨與人物行動變化，再於獨立原創短劇 A Softer Beginning 完成三題遷移。
- 每題錯答保留當前選項並提供對應台詞／動作回讀提示；答對才解鎖下一階。預測、步驟及完成狀態依 lesson instance 保存並可重設。課文和題庫仍維持 `draft`；出版社全文融合、內容／版權及實際可及性 QA 未完成前不升級。

## D-300：3-Ⅳ-12 閱讀策略練習採逐階段、可重試的資料驅動互動

- 日期：2026-09-26
- 決策：保留本課六項原創公告任務，但教材頁只呈現當前階段；學生答對才前進，錯答回傳該題專屬欄位提示並保留所選項。六階段完成狀態依 lesson instance 保存且可重設，植樹日公告作為不同問題欄位的遷移情境。
- 此互動只承載本課目的—策略—證據教學，不改變已獨立撰寫的題庫。單元內容仍為 `draft`；spec `qaStatus=untested`，三版本融合、內容／版權及實際瀏覽器與輔助科技 QA 未完成前，不升級狀態。

## D-296：3-Ⅳ-7 對話理解互動採先預測、逐句舉證與新情境遷移

- 日期：2026-09-26
- 決策：3-Ⅳ-7 使用 `DialogueComprehensionLab` 實作原創公車對話的主旨預測、問題／回應句證據標記、針對性錯誤回饋與設備故障新情境遷移。答案只透過互動資料渲染；題目、答案及回饋不寫死於 UI。更改已核對證據須使後續答案失效，錯誤遷移須同時指出選項與證據不匹配；互動進度按 lesson instance 保存。單元內容與題目仍維持 `draft`，本輪 DOM 測試不等同全項人工／助讀器／發布 QA。
- 理由：guide 原本配置不存在於 renderer 的 `LanguageTimelineBlock`，lesson 實際僅有一般三題選擇檢核，沒有預測保存、逐句舉證、證據變更後失效處理或跨情境遷移。專屬元件讓多輪對話的問題—回應鏈可操作並以文字標示，亦提供鍵盤、窄螢幕及 reduced-motion 基礎支援；其餘未實測項目繼續標示待驗。

## D-192：3-Ⅳ-6 來源以句型功能精確對位，不為固定筆數加弱引用

- 日期：2026-09-26
- 決策：3-Ⅳ-6 每題至少保留一筆已查閱的公立國中段考 item-level pattern-only 來源；若另有直接對應的第二份原卷，才加列第二筆。引用需明確指出所支持的句型功能，不得把紙本索引或只有相鄰但不相干的題目說成直接考點。題幹、選項、答案與詳解均原創，教材版本研究與完整內容 QA 未完成前維持 `draft`。
- 理由：原引用只有一份廣義描述、碧華／新埔未核實索引，不能證明十題各自的句型模式。公開原卷題目分別實際呈現頻率現在式、過去式、there is、位置問句、比較級、must 義務、目的不定詞、because 子句和現在進行式；逐題明載精確 locator 比維持形式上的固定來源筆數可靠。

## D-191：3-Ⅳ-5 題目只保留可核對的對話功能來源

- 日期：2026-09-26
- 決策：3-Ⅳ-5 十題均須以至少兩筆不同校方公開段考原卷的精確題號作 pattern-only 參照；若第三筆無法支持該題所需的對話功能，不為湊數加入。來源僅證明公開試卷確有相關互動命題模式，不代表原題涵蓋本題完整情境。題幹、選項、答案與解析由本專案獨立撰寫，內容 QA 完成前維持 `draft`。
- 理由：先前三筆引用含未定位的學校索引和失效附件，不能證明逐題來源；只為維持固定筆數而加入不相干題號會製造來源過度主張。新 reviewer 要求至少兩筆不同 URL、item-level 定位並逐題檢查答案說明與詳解欄位。

## D-188：依使用者指示取消 Implementation Guide 的 Terra 審查工作

- 日期：2026-09-24
- 決策：本次 Implementation Guide 執行不再排程、執行或等待 Terra 第二輪審查；其餘來源研究、原創教材／題目、答案與解析核對、互動功能、內容 QA 及發布 gate 仍依 guide 和專案規約逐項執行。未經 Terra 的項目不得假稱已完成第二輪審查，也不得因此自動升級 `reviewStatus`。
- 理由：使用者明確要求取消 Terra 審查工作；取消範圍僅限 Terra 審查，不等於放寬其他內容正確性、來源、版權或發布要求。

## D-189：3-Ⅳ-3 標示互動以線索矛盾診斷為核心，題庫來源需逐題定位

- 日期：2026-09-24
- 決策：3-Ⅳ-3 的互動採既有 `SignageReadingLab` 資料驅動元件：先記錄預測，再只翻轉箭頭，讓學生比較標示文字、方向與地圖地名；線索不一致時引導停下核對，並遷移到診所和校園場景。單元新題每題只留一筆精確 item-level 公校試題型參照，題目、選項、答案及解析保持原創；未完成版本研究、版權與全套內容 QA 前維持 `draft`，QA 狀態未經全項驗收不得升級。
- 理由：原 lesson 的通用 guided-choice 題與舊 reviewer 的三筆來源記錄沒有連接專用互動流程，十題來源皆只有未定位紙本層級引用。小港、內湖、宜昌與國昌國中公開卷提供圖像標示、路線、時刻表、安全規則、場館選擇及消費條件的具體能力線索；以逐題定位支持 pattern-only 改寫，並以標示與地圖衝突的操作支援「比對證據後採取行動」的學習目標，不把來源題目或圖像搬入教材。

## D-187：碧華校考索引僅對逐題驗證的附件定位解除 pending

- 日期：2026-09-24
- 決策：碧華114學年度第2學期第3次定期評量的校方索引 URL 預設仍須標為 `pending-item-locator`／`locatorLevel=page`。僅允許語義稽核白名單中二十四筆精確題目記錄標成 `recorded`／`locatorLevel=item`：Jf-Ⅳ-2 八年級理化第2頁第14題對應有機酸性質、第3頁第18題對應烴類完全燃燒係數推理、第3頁第23題對應酯化反應；tr-Ⅳ-1 兩題對應第5頁第33題摩擦力資料推論／控制變因；英語 B-Ⅳ-5 七年級卷第3頁第42、46題及第4頁第47、48題；英語 B-Ⅳ-6 七年級卷第3頁第45題及八年級卷第3頁第48題、第4頁第43、47題；英語 B-Ⅳ-7 八年級卷第1頁第8題；另七年級卷第1頁第13題對應存在句主謂數一致，第2頁第20、30、21、24題分別對應 `performance-3-iv-6` 的現在簡單式、過去式、because 原因子句及現在進行式；數學七年級卷第1頁第2題的比例式交叉相乘求未知數、第1頁第3題的不等式文字轉譯與嚴格／非嚴格界線、第2頁第14題的位移後變數成正比判讀、第3頁第16題的折扣後價格模式改寫為七五折求售價，以及第1頁第4題的固定存款加每週累積模式改寫為數量乘單價加一次性運費。白名單同時固定 question ID、附件名與頁／題號；其他任何同 URL 記錄未經逐題研究不得沿用例外。
- 理由：官方索引證明附件來源，但只有閱讀附件並比對能力點後才能支持題庫中的 pattern-only 改寫。六份原卷及雜湊／範圍記在 `implementation/reports/bihua-114-2-3-paper-audit.json`，精確 locator 回歸檢查在 `scripts/audit_bihua_item_mappings.py`；新增引用不包含原題文字。其餘1,124筆碧華索引引用仍 pending，不因這二十四筆例外而變更狀態；題庫全庫仍有1,129題至少一筆來源未完成。

## D-186：A-8-2 三版本教材證據降級，課程計畫不得冒稱出版社教材研究

- 日期：2026-09-24
- 決策：A-8-2 lesson 與 unit spec 先前將南一、康軒、翰林公校課程計畫／課程節次誤記為出版社教材的概念順序、例證、迷思與評量研究；另有一筆把均一標成南一並稱為出版社來源。此類主張撤回，版本融合狀態改為 pending。校方計畫只保留其實際明示的版本採用、課綱範圍、週次或評量方式；均一教材另列為免費第三方教學參考，不併入出版社版本比較。
- 理由：現有 PDF 只能直接證明課程計畫列出的單元名稱、課綱節點與評量安排，沒有足夠證據支持教材正文、概念展開次序、例題、迷思或三版本差異。專案規約要求實際閱讀可取得的三版本相關教材內容，不能用章節級課程計畫或均一仿版本課程替代。後續取得教材章節或合法出版社 sample 並逐版記錄前，A-8-2 lesson 與新題維持 `draft`；本決策也要求修正既有假融合文字。

## D-185：Implementation Guide 互動活動以受 Schema 驗證的單元資料驅動

- 日期：2026-09-24
- 決策：互動 block 可選擇提供 `guidedActivity`，由標題、引導文字、分步題目、接受答案、正誤回饋與完成訊息組成；共用 renderer 依資料呈現並逐步驗證學生輸入，不把題目答案或單元內容硬編碼在 UI。缺少該欄位的舊單元維持原 fallback 行為。
- 理由：原 workbench 只有通用狀態按鈕與規格文字展示，不能證明學生實際完成了單元運算。先以 A-8-5「提公因式—辨認平方差—完全分解」接通資料與互動，再以 jsdom 覆蓋錯答提示、重試、正答逐步解鎖及完成狀態；單元完整教學、瀏覽器視覺與助讀器 QA 仍須另行驗證。

## D-184：互動變項識別碼允許單元可讀的多字母名稱

- 日期：2026-09-23
- 決策：lesson 互動變項的 `symbol` 可使用小寫字母開頭的描述性識別碼（例如 `rain`、`slope`），不限定單一字母；變項意義仍由 `meaning` 提供。
- 理由：降雨、覆蓋、坡度與排水等地科變項用單字命名比任意單字母更可讀；現有 schema 的單字母限制與真實 lesson 資料不一致。這是資料識別欄位，不是數學符號表達式，放寬至小寫字母、數字與連字號即可維持穩定安全的結構。

## D-181：lesson schema 保留課程入口與版權界線欄位

- 日期：2026-09-23
- 決策：允許教材 `content.studyEntry` 作為單元專屬學習入口，並允許 `publisherResearch.licenseBoundary` 作為逐來源的授權／改寫界線說明；網站需呈現 studyEntry，而非只讓 schema 靜默接受。
- 理由：現存教材已填入這些有明確語意的欄位，原 schema 卻拒收；移除欄位會丟失教學入口或來源界線。新增契約並在 lesson renderer 顯示入口，可使內容資料與學生實際頁面一致。

## D-177：題目可記錄與題型來源分離的事實查證來源

- 日期：2026-09-23
- 決策：題目新增可選 `studyReferences` URI 清單，記錄答案事實所依據的權威資料；公開試題的題型改寫證據仍放在 `examPatternRefs`，兩類來源不得互相取代。
- 理由：C-2 題需修正分子定義，IUPAC Gold Book 明確定義分子為由多於一個原子組成的電中性實體；僅有公開考題 pattern 來源不能充分支持這項化學事實。新欄位可附來源而不改寫考題來源的意義。

## D-173：教材資料內的互動模擬由 lesson renderer 掛載並隔離實例狀態

- 日期：2026-09-23
- 決策：lesson 有 `simulation` 資料且 `LearningSimulations` runtime 可用時，由教材 renderer 將模擬呈現在課文內；每個顯示位置使用獨立持久化鍵，避免目錄卡片與全庫卡片的操作狀態互相覆寫。
- 理由：Ka-Ⅳ-7 已有課程專屬的光脈衝測量任務、預測提示與參數探索資料，但原 renderer 未呼叫模擬 runtime，學生無法實際操作。新增整合測試覆蓋掛載、單元步驟切換、預測狀態及雙實例隔離；真實瀏覽器與該模擬的鍵盤／螢幕閱讀器／窄螢幕 QA 仍待完成，不得因此宣告單元發布 gate 通過。

## D-172：KA-Ⅳ-7 題目採題意專屬解題步驟並維持草稿

- 日期：2026-09-23
- 決策：KA-Ⅳ-7 原創題的解題步驟必須逐題對應其題目，保持五個扁平步驟；不得沿用混合光學題型的通用步驟，也不得把結構修正視為內容審查完成。
- 理由：第 2–10 題曾把五步陣列巢狀放進步驟欄位，且內容未對應各題計算、實驗設計或資料限制。修正後仍需學科內容審查、來源定位及其他發布 gate，故全部保留 `draft`。

## D-174：題庫公開試題來源保留同值舊欄位 alias 並加一致性檢查

- 日期：2026-09-23
- 決策：`examPatternRefs[].pattern` 視為 `observedPattern` 的舊名稱相容欄位；題目 Schema 暫時接受此欄位，`validate_data.py` 強制兩者完全相等，避免把不同來源觀察混在一起。
- 理由：全庫抽查 27,383 筆來源記錄，其中 5,139 筆帶有 `pattern`，且 5,139 筆均與 `observedPattern` 完全相同。直接拒收會令其餘來源內容無法通過結構驗證；相容 alias 能保留既有資料並維持語意約束，後續可另案做可追溯的欄位遷移。

## D-166：英文標示互動採課程資料驅動的預測—操作—證據—遷移元件

- 日期：2026-09-23
- 決策：Ac-Ⅳ-1 不再用通用 guided-choice 充當互動教學；新增明確的 `language-signage-lab` 資料契約，題材、標示、位置／箭頭、選項、答案與證據均由 lesson JSON 提供，頁面元件只負責呈現與互動狀態。
- 理由：標示理解須把文字、符號／位置與讀者行動同步比對，並讓學生先預測再操作和解釋。不得把標示內容硬編碼於 UI；答案揭露前保留預測，需支援鍵盤與文字化回饋。此決策不代表其他單元已完成互動實作或 QA。

## D-165：Ac-Ⅳ-1 求助地點題以公立國中段考作跨媒介 pattern-only 參照

- 日期：2026-09-23
- 決策：第 2 題新增臺北市立內湖國中 110 學年度第二學期八年級第二次段考第 8 題定位；來源是聽力情境中判斷應前往 information desk 詢問，本題則為閱讀 HELP DESK 標示。僅參照「辨識求助地點」能力方向，不沿用原對話、選項或聽力形式。
- 理由：能力面向相近但題型媒介不同，必須明確標示類比範圍，不可宣稱是同型標示閱讀題。補足逐題來源紀錄不等於完成 Ac-Ⅳ-1 全題內容審查；單元仍維持 `draft`。

## D-160：Ac-Ⅳ-1 公開段考題型證據採逐題定位、僅作 pattern-only 改寫

- 日期：2026-09-23
- 決策：Ac-Ⅳ-1 第 1、3、6、9 題新增燕巢國中 111 學年度七年級第二次段考第 29 題的頁碼與題號定位，記錄其「讀標示判斷受限行為」能力型態；只作 pattern-only，不複製原標示、選項、圖片或答案，題庫內容維持原創與 `draft`。
- 理由：該公開題目可支持本單元四題所需的公共標示／行為限制判讀，但不能代替各題所需的不同推理，也不能證明另六題已有逐題定位。新增來源的頁碼與題號由公開卷面確認；其餘題目來源及全單元 AI／Terra 內容審查仍須獨立完成。

## D-161：Ac-Ⅳ-1 標示場所判讀題使用國教院 TASA 公開樣題作 pattern-only 來源

- 日期：2026-09-23
- 決策：Ac-Ⅳ-1 第 7 題新增國教院 TASA 英語文公開試題分析 PDF 第 16 頁的標示圖示判斷場所題；只參照「由標示及圖像線索判斷場所」能力，不複製原題圖像、選項或答案。
- 理由：來源直接呈現標示—場所判讀，與本題找候車地點的能力相符，且定位到 PDF 頁與題目提示。它是國教院公開評量分析，不冒稱公立學校段考；本題仍保留既有公立學校來源並維持原創與 `draft`。

## D-162：Ac-Ⅳ-1 回收與垃圾標示題採公立學校段考的分類指示作 pattern-only 來源

- 日期：2026-09-23
- 決策：第 8、10 題新增臺北市立景興國中 108 學年七年級第二次段考第 31–32 題的精確定位，參照分類式回收規則、標示文字與垃圾桶投放指示；題幹、標示文字、選項與答案皆由本專案獨立撰寫。
- 理由：來源直接提供接受／拒收分類與處置判斷，分別支持「辨認標示目的」與「依指示採取行動」；不複製考卷表格或原題內容，並維持題目 `draft`。

## D-163：Ac-Ⅳ-1 安靜規範題以公立國中段考題型補足情境證據

- 日期：2026-09-23
- 決策：第 4 題新增新北市立三多國中 113 學年度七年級英語段考 PDF 第 5 頁第 35 題定位，只參照依活動情境選擇安靜提醒語的能力型態；本題仍以自編圖書館標示為題幹。
- 理由：公開校方考卷直接出現安靜規範提醒語，可支援「標示目的—合宜行動」判讀，但不代表原卷本身是圖書館標示題；因此保留 pattern-only 界線。

## D-164：Ac-Ⅳ-1 濕地警示題使用教育部國教署標準化評量作 pattern-only 來源

- 日期：2026-09-23
- 決策：第 5 題新增教育部國教署 109 年八年級英語標準化評量 PDF 第 2 頁第 12 題定位，參照地面潮濕線索與小心腳步警示的語意連結；本題另創樓梯口風險情境。
- 理由：來源直接檢核 wet-floor 警告的語意理解。其性質為國教署標準化評量，不冒稱校內段考；題目仍採 pattern-only、原創與 `draft`。

## D-159：Ab 語音主題三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-ab` 的翰林、康軒、南一 publisher evidence 以三份公立國中英語課程資料與可定位公開教學資源重新核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：根層 Ab 涵蓋字詞、句子與對話的語音能力，不能只用字母拼讀或單一發音頁代表全貌。翰林資料涵蓋拼讀、例字、句子語音及歌謠／韻文；康軒資料涵蓋字母拼讀、音訊跟讀、語音辨識及口說活動；南一大吉國中課程計畫涵蓋 Starter 拼讀／查字、對話音訊／Oral Practice 與 Fun with Sounds。只採可見教學與評量方向，不複製歌詞、音檔或教材。

## D-158：Ab-Ⅳ-3 字母拼讀規則三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-ab-iv-3` 的翰林、康軒、南一 publisher evidence 改以三份明確標示版本、年級與英文領域的公立國中課程計畫核對，三個 slots 記為 `verified`；lesson、題目與互動仍為 `draft`。
- 理由：翰林資料明列 Ab-IV-3 定義、音標／子母音類別例字與規則應用；康軒東榮國中資料標示第1、2冊七年級並對應聽說讀寫及口說評量；南一大吉國中資料直接列出拼讀規則讀出／拼寫、字典與上下文查證。課程計畫不等於完整教科書，故只記錄可核對的能力順序與評量，不複製教材例字或題目。

## D-157：Ab-Ⅳ-2 歌謠韻文節奏音韻三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-ab-iv-2` 的翰林、康軒、南一 publisher evidence 以三份公立學校公開英語課程資料重新回讀，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：翰林資料直接核對歌謠／韻文、聽力預測與溝通評量，康軒資料核對音訊、跟讀、辨音與口語活動，南一資料核對聽辨、閱讀、溝通與自我檢視；歌詞及完整出版社音檔未公開，故只融合可核對的能力與教學方向，所有韻文、題目、答案、解析與互動均重新撰寫。

## D-156：Ab-Ⅳ-1 句子發音重音語調三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-ab-iv-1` 的翰林、康軒、南一 publisher evidence 以三份公立學校公開英語課程資料重新回讀，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：翰林資料核對音標／發音規則、句子發音與語調及口說評量，康軒資料核對聽音、跟讀、發音辨析、對話練習與多元評量，南一資料核對範讀、跟讀、音檔聽辨、聲音強弱與抑揚停頓；本課只融合可核對的教學方向，所有句子、題目、答案、解析、互動與活動均重新撰寫，不複製出版社或校方教材。

## D-155：Aa 字母主題三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-aa` 的翰林、康軒、南一 publisher evidence 改以嘉義縣公立學校英語課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：`Aa` 主題層級必須統整字母辨識、發音／拼讀、書寫、查字、字詞、句型與溝通入口，不能只重複 `Aa-Ⅳ-1` 的書寫技能；三份資料分別提供完整能力鏈、Get Ready 操作支架與 Starter 到對話／閱讀的遷移，本次不複製教材正文、題目、答案、圖片或影音。

## D-154：Aa-Ⅳ-1 書寫體大小寫辨識書寫三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-aa-iv-1` 的翰林、康軒、南一 publisher evidence 改以嘉義縣公立學校英語課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元不是只背字母名稱，而是要把大小寫辨識、印刷體／連續體轉換、筆畫與書寫格式、拼讀及字典查詢串成可使用的語言基礎；三份資料分別提供字形基礎、書寫支架與查詢銜接，本次不複製教材正文、題目、答案、圖片或影音。

## D-153：英語學習內容 A 語言知識三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-english-content-a` 的翰林、康軒、南一 publisher evidence 改以嘉義縣公立學校英語課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本根層單元需把字彙、拼讀、句型、查詢工具、對話理解、角色扮演與情境遷移統整成語言知識的使用鏈；三份資料分別提供形式基礎、句型操作與溝通／預測遷移的互補證據，本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-152：寫作主題單元三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：此主題單元必須統整文本理解、語句與篇章、需求書寫、仿寫改寫、自主創作、科技編輯與作品分享；三份資料在完整能力、支架化簡化與應用格式上互補，本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-151：6-Ⅳ-6 科技編輯作品及分享見解三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-6` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元不只要求「使用工具」，而是把資訊蒐集、材料組織、格式選擇、科技編輯、觀點分享與作品回饋連成完整流程；三份資料分別提供作品／觀點發表、支架化輸出與多種數位文本格式的互補證據，本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-150：6-Ⅳ-5 主動創作自訂題目表述見解發布三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-5` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元要求學習者從接受題目走向自主命題、闡述見解與發布作品；三份資料分別提供主題／百字段落創作、支架化簡化發表，以及生活經驗反思與作品編輯的證據，本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-149：6-Ⅳ-4 依需求書寫各類文本三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-4` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元的核心不是泛稱「會寫作」，而是依需求在讀者、目的、語體、文本格式與篇章組織之間做選擇；三份資料分別提供完整文本、能力簡化與學習應用格式的互補證據，本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-148：6-Ⅳ-3 仿寫改寫等技巧三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-3` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：三份資料共同指向仿寫／改寫的能力目標，但呈現了不同的支架粒度：翰林連結文句邏輯、篇章結構、文本形式與創作遷移，康軒提供能力簡化與文本型態支架，南一則把技能放入語文常識、敘事及多元文本的練習序列；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-147：6-Ⅳ-2 審題立意取材組織遣詞修訂成文三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-2` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把題意條件、寫作目的、主旨立意、材料取捨、段落組織、遣詞造句、修訂回饋與成文品質連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-146：6-Ⅳ-1 善用標點增進情感與說服三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-6-iv-1` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把標點選擇、句法停連、情感語氣、論證焦點、說服效果與讀者回應連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-145：國語文閱讀三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元統整閱讀策略、文本證據、篇章組織、作者目的、媒介差異、跨域資料、生活議題與表達輸出；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-144：5-Ⅳ-6 圖書館科技蒐集組織資訊擴展視野三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-6` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把研究問題、圖書館與數位檢索、關鍵詞選擇、來源判讀、資訊分群摘要、引用記錄與新知遷移連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-143：5-Ⅳ-5 多元閱讀理解議題與生活社會關聯三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-5` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把多元文本、公共議題、生活社會關聯、事實與觀點、資料證據及行動反思連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-142：5-Ⅳ-4 閱讀策略整合跨域知識解題三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-4` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把閱讀策略、圖表與多元文本、跨域知識、證據整合、條件推理與問題解決連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-141：5-Ⅳ-3 理解文本內容形式與寫作特色三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-3` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把內容主題、文體形式、結構安排、語言特色、修辭證據與效果解釋連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-140：5-Ⅳ-2 理解句段主要概念及寫作目的觀點三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-2` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把句段概念、訊息層次、寫作目的、作者觀點、語句證據與重述推論連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-139：5-Ⅳ-1 標點效果與流暢有感朗讀三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-5-iv-1` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把標點停連、語氣變化、句段理解、流暢朗讀、文本形式與理解驗證連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-138：國語文識字與寫字三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元統整識字、構形、語境、工具書、書體觀察、硬筆書寫、口語表達與文字輸出；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-137：4-Ⅳ-6 正確美觀硬筆字三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-6` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把筆順、姿勢、力度、結體比例、字距行距、版面功能與自我修正連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-136：4-Ⅳ-5 欣賞書法行款布局行氣風格三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-5` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把行款疏密、字距行距、行氣連貫、章法風格、局部證據與書寫比較連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-135：4-Ⅳ-4 認識書體與欣賞碑帖三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-4` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把書體辨識、碑帖觀察、筆畫結構、章法布局、賞析證據與書寫實作連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-134：4-Ⅳ-3 字辭典處理一字多音多義三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-3` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把語境辨音、義項判斷、詞語搭配、字辭典查證與不確定性處理連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-133：4-Ⅳ-2 造字原則輔助形音義理解三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-2` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把造字原則、部件與偏旁、形音義推論、語境判讀、工具書查證與證據限制連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-132：4-Ⅳ-1 識字與字詞運用三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-4-iv-1` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把識字量、字形字音字義、構形線索、語境判讀、工具書查證與正確運用連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-131：國語文口語表達三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需統整口語表達、聆聽回應、情境溝通、觀點組織、媒介運用與生活任務；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-130：2-Ⅳ-5 報告評論演說與論辯三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2-iv-5` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把資料整理、報告結構、評論推理、演說表達、聽眾回應與論辯修正連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-129：2-Ⅳ-4 運用科技資訊豐富表達三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2-iv-4` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把資訊檢索、來源判讀、媒介選擇、圖文影音整合、引用標示與數位表達連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-128：2-Ⅳ-3 明確表達與有條理論辯三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2-iv-3` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把主張、理由、證據、反例、觀點回應與論辯結構連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-127：2-Ⅳ-2 掌握聽聞邏輯提問回饋三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2-iv-2` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把聽聞邏輯、重點擷取、有效提問、證據回饋、表達修正與合作溝通連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-126：2-Ⅳ-1 情境表達與經驗分享三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-2-iv-1` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把情境與聽眾、經驗取材、細節取捨、觀點表達、回應提問與生活溝通連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-125：國語文「聆聽」三版本來源重新核對

- 日期：2026-09-23
- 決策：`cur-chinese-performance-1` 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文課程計畫、高雄市公立資源班國文課程計畫及嘉義縣永慶國中公立課程計畫公開資料核對，三個 slots 記為 `verified`；lesson、題目與互動仍維持 `draft`。
- 理由：本單元需把聆聽理解、關鍵訊息整理、語境判讀、媒介互動、口語回應與生活溝通連成可觀察的學習表現；本次只融合公開資料呈現的教學與評量方向，不複製教材正文、題目、答案、圖片或影音。

## D-124：1-Ⅳ-4 運用科技資訊增進聆聽與互動三版本來源重新核對

- 日期：2026-09-23
- 決策：1-Ⅳ-4 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要將科技資訊、聆聽理解、媒介互動、訊息整理與經驗分享連成可觀察的學習表現；本次以可回讀公立課程資料核對科技媒介、口語互動與評量方向，不複製教材正文、題目或答案。

## D-123：1-Ⅳ-3 分辨聆聽內容邏輯並找方法三版本來源重新核對

- 日期：2026-09-23
- 決策：1-Ⅳ-3 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要把聆聽邏輯、資訊判讀、方法尋找與問題解決連成可觀察的學習表現；本次以可回讀公立課程資料核對聆聽策略、媒介互動與評量方向，不複製教材正文、題目或答案。

## D-122：1-Ⅳ-2 依情境辨識聲情與表達技巧並回應三版本來源重新核對

- 日期：2026-09-23
- 決策：1-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要把情境、語氣、聲情、表達技巧與回應方式連成可觀察的學習表現；本次以可回讀公立課程資料核對聆聽判讀、口語互動與評量方向，不複製教材正文、題目或答案。

## D-121：1-Ⅳ-1 同理聆聽並記錄歸納三版本來源重新核對

- 日期：2026-09-23
- 決策：1-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要將同理聆聽、重點記錄、歸納、聲情辨識與情境回應連成可觀察的學習表現；本次以可回讀公立課程資料核對活動路徑與評量方向，不複製教材正文、題目或答案。

## D-120：國語文學習表現三版本來源重新核對

- 日期：2026-09-23
- 決策：學習表現的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元統整聆聽、口語、閱讀、寫作與任務輸出等學習表現；本次以可回讀公立課程資料核對學習表現的活動路徑、文本證據與評量方向，不複製教材正文、題目或答案。

## D-119：國語文學習內容三版本來源重新核對

- 日期：2026-09-23
- 決策：學習內容的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元統整書法／文字觀察、語詞語境、閱讀理解、文本證據與語文表達；本次以可回讀公立課程資料核對學習內容的教學結構、活動與評量方向，不複製教材正文、題目或答案。

## D-118：Cc 精神文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Cc 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結精神文化、信仰、思想、價值、社群與生活脈絡；本次以可回讀公立課程資料核對資料判讀、觀點比較、文本理解、生活反思與評量方向，不複製教材正文、題目或答案。

## D-117：Cc-Ⅳ-1 藝術信仰思想文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Cc-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結藝術、信仰、思想文化、文體、歷史與社群脈絡；本次以可回讀公立課程資料核對形式賞析、資料比較、文本理解、主題報告與評量方向，不複製教材正文、題目或答案。

## D-116：Cb 社群文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Cb 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要處理社群文化、群體生活、文化互動、公共議題與物質／精神文化的關係；本次以可回讀公立課程資料核對資料判讀、觀點比較、文本理解、生活／公共表達與評量方向，不複製教材正文、題目或答案。

## D-115：Cb-Ⅳ-2 個人家庭鄉里國族社群關係三版本來源重新核對

- 日期：2026-09-23
- 決策：Cb-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需處理個人、家庭、鄉里、國族與社群的不同關係尺度；本次以可回讀公立課程資料核對文本理解、文化差異、生活經驗、觀點解釋與評量方向，不複製教材正文、題目或答案。

## D-114：Cb-Ⅳ-1 親屬道德儀式典章制度三版本來源重新核對

- 日期：2026-09-23
- 決策：Cb-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結家庭／親屬、道德、禮俗／儀式與典章制度；本次以可回讀公立課程資料核對文本理解、資料解釋、文化差異、生活討論與評量方向，不複製教材正文、題目或答案。

## D-113：Ca 物質文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Ca 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結物質生活、器物、飲食／服飾／建築、社群文化與環境經驗；本次以可回讀公立課程資料核對文化觀察、比較、文本理解、生活連結與評量方向，不複製教材正文、題目或答案。

## D-112：Ca-Ⅳ-2 科技文明演進與生存環境文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Ca-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結科技文明、環境、社會文本、生存環境文化與資料證據；本次以可回讀公立課程資料核對檢索、統整、解釋、省思、生活連結與評量方向，不複製教材正文、題目或答案。

## D-111：Ca-Ⅳ-1 飲食服飾建築交通名勝休閒文化三版本來源重新核對

- 日期：2026-09-23
- 決策：Ca-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元橫跨飲食、服飾、建築、交通、名勝與休閒等文化生活面向；本次以可回讀公立課程資料核對文化差異、社群生活、文本理解、比較與表達方向，不複製教材正文、題目或答案。

## D-110：C 文化內涵三版本來源重新核對

- 日期：2026-09-23
- 決策：C 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要連結文化文本、公共議題、價值思辨、生活經驗與表達活動；本次以可回讀公立課程資料核對閱讀理解、觀點比較、省思及評量方向，不複製教材正文、題目或答案。

## D-109：Be 應用文本三版本來源重新核對

- 日期：2026-09-23
- 決策：Be 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元統攝多種生活應用文本，必須核對目的、對象、格式、資訊組織、溝通與評量方向；本次以可回讀公立課程資料完成交叉核對，不複製教材正文、題目或答案。

## D-108：Be-Ⅳ-3 簡報讀書報告演講稿劇本等學習應用三版本來源重新核對

- 日期：2026-09-23
- 決策：Be-Ⅳ-3 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元涵蓋簡報、讀書報告、演講稿與劇本等不同學習應用輸出；本次以可回讀公立課程資料核對資料組織、受眾、口語／書面與角色表達及評量方向，不複製教材正文、題目或答案。

## D-107：Be-Ⅳ-2 書信便條對聯等人際溝通三版本來源重新核對

- 日期：2026-09-23
- 決策：Be-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元同時涵蓋書信、便條、對聯等格式，必須核對對象、目的、語氣、格式與慣用語；本次以可回讀公立課程資料核對生活溝通與評量方向，不複製教材正文、題目或答案。

## D-106：Be-Ⅳ-1 自傳簡報新聞稿等生活應用三版本來源重新核對

- 日期：2026-09-23
- 決策：Be-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要同時處理自我介紹、簡報、新聞稿等不同生活應用格式；本次以可回讀公立課程資料核對受眾、格式、資訊組織、口語／書面溝通與評量方向，不複製教材正文、題目或答案。

## D-105：Bd 議論文本三版本來源重新核對

- 日期：2026-09-23
- 決策：Bd 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要完整區分主張、證據、理據、例證、推論與觀點表達；本次以可回讀公立課程資料核對資料統整、立場省思、論辯與評量方向，不複製教材正文、題目或答案。

## D-104：Bd-Ⅳ-2 比較比喻等論證三版本來源重新核對

- 日期：2026-09-23
- 決策：Bd-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要辨識比較、類比、比喻的對應關係及論證作用；本次以可回讀公立課程資料核對資料判讀、觀點組織、口語／書面說服與評量方向，不複製教材正文、題目或答案。

## D-103：Bd-Ⅳ-1 事實理論作為論據三版本來源重新核對

- 日期：2026-09-23
- 決策：Bd-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：本單元需要區分主張、事實、理據、例證與說服／批判表達；本次以可回讀公立課程資料核對資料統整、立場省思、論辯與評量方向，不複製教材正文、題目或答案。

## D-102：Bc 說明文本三版本來源重新核對

- 日期：2026-09-23
- 決策：Bc 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校或僅能支持廣義文體定位的來源；本次以可回讀公立課程資料核對說明文本的資料擷取、圖表／視覺證據、組織、比較、解釋、報告表達與評量方向，不複製教材正文、題目或答案。

## D-101：Bc-Ⅳ-3 數據圖表圖片工具列輔助三版本來源重新核對

- 日期：2026-09-23
- 決策：Bc-Ⅳ-3 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立資源班康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料未充分對應資料、圖表、圖片輔助與文字／視覺證據核對；本次以可回讀公立課程資料核對資訊擷取、整理、比較、表達與評量方向，不複製教材正文、圖片、題目或答案。

## D-100：Bc-Ⅳ-2 說明組織與問題解決三版本來源重新核對

- 日期：2026-09-23
- 決策：Bc-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本的說明組織定位；本次以可回讀公立課程資料核對描述、列舉、因果、問題解決、比較、分類、定義與報告表達方向，不複製教材正文、題目或答案。

## D-099：Bc-Ⅳ-1 邏輯客觀理性說明三版本來源重新核對

- 日期：2026-09-23
- 決策：Bc-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本的說明文定位；本次以可回讀公立課程資料核對資料組織、因果／定義、客觀語氣、邏輯理性表達與評量方向，不複製教材正文、題目或答案。

## D-098：Bb 抒情文本主題三版本來源重新核對

- 日期：2026-09-23
- 決策：Bb 抒情文本主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 Bb 主題來源混用出版社入口與無法直接支持國中國文的課程資料；本次以可回讀資料核對直接／間接抒情、情感語氣、自然生命主題、文本反思與表達評量方向，不複製教材正文、題目或答案。

## D-097：Bb-Ⅳ-5 事件景物間接抒情三版本來源重新核對

- 日期：2026-09-23
- 決策：Bb-Ⅳ-5 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本的間接抒情定位；本次以可回讀公立課程資料核對事件、景物、氛圍、描寫傳情與表達評量方向，不複製教材正文、題目或答案。

## D-096：Bb-Ⅳ-4 直接抒情三版本來源重新核對

- 日期：2026-09-23
- 決策：Bb-Ⅳ-4 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本的抒情定位；本次以可回讀公立課程資料核對直接抒情、情感詞、語氣、生活經驗、文本反思與表達評量方向，不複製教材正文、題目或答案。

## D-095：Bb-Ⅳ-3 物自然生命感悟三版本來源核對

- 日期：2026-09-23
- 決策：Bb-Ⅳ-3 的翰林、康軒、南一 publisher evidence 以高雄市立民族國中翰林版、臺南市公立康軒版及桃園市公立翰林版國文課程資料交叉核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：三份可回讀公立課程資料實際支持自然景物、生命經驗、環境美學、倫理／價值思辨、觀察感悟與生活連結；僅保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-094：Bb-Ⅳ-2 社會群體家國民族情感三版本來源核對

- 日期：2026-09-23
- 決策：Bb-Ⅳ-2 的翰林、康軒、南一 publisher evidence 以高雄市立民族國中翰林版、臺南市公立康軒版及桃園市公立翰林版國文課程資料交叉核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：三份可回讀公立課程資料實際支持社會群體、家國民族情感、文化／公共議題、社群關係與文本反思；僅保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-093：Bb-Ⅳ-1 自我與人際交流感受三版本來源核對

- 日期：2026-09-23
- 決策：Bb-Ⅳ-1 的翰林、康軒、南一 publisher evidence 以高雄市立民族國中翰林版、臺南市公立康軒版及桃園市公立翰林版國文課程資料交叉核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：三份可回讀公立課程資料實際支持自我感受、人際理解、生活經驗分享、文本反思與表達評量；僅保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-092：Ba 記敘文本主題三版本來源重新核對

- 日期：2026-09-23
- 決策：Ba 記敘文本主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 Ba 主題混用出版社入口與不同學校課程資料；本次以可回讀公立課程資料核對事件安排、人物／景物細節、篇章觀點、描寫表達與評量方向，不複製教材正文、題目或答案。

## D-091：Ba-Ⅳ-2 描寫作用與效果三版本來源重新核對

- 日期：2026-09-23
- 決策：Ba-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本的描寫教學定位；本次核對人物、景物、事件描寫的篇章功能、表達效果、課文理解與評量方向，不複製教材正文、題目或答案。

## D-090：Ba-Ⅳ-1 敘事順序三版本來源重新核對

- 日期：2026-09-23
- 決策：Ba-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料使用不同學校／版本的敘事定位，需統一到可回讀的國中國文課程資料；本次核對順敘、倒敘、插敘、補敘的事件理解、段落功能、篇章分析與評量方向，不複製教材正文、題目或答案。

## D-089：B 文本表述主題三版本來源重新核對

- 日期：2026-09-23
- 決策：B 文本表述主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 B 主題來源包含出版社入口與無法直接回讀的公立資料；本次以可回讀課程資料核對文本理解、篇章觀點、段落組織、證據追問與表達評量方向，不複製教材正文、題目或答案。

## D-088：Ad-Ⅳ-4 非韻文古文古典小說語錄寓言三版本來源重新核對

- 日期：2026-09-23
- 決策：Ad-Ⅳ-4 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本，且部分非韻文定位無法直接回讀；本次核對古文、古典小說、語錄、寓言的文本理解、主旨／寓意、提問與分層表達方向，不複製教材正文、題目或答案。

## D-087：Ad-Ⅳ-3 韻文古體樂府近體詞曲三版本來源重新核對

- 日期：2026-09-23
- 決策：Ad-Ⅳ-3 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有資料混用不同學校／版本與部分不一致的出版社定位；本次以可回讀公立課程資料核對韻文、古體、樂府、近體、詞曲的形式、音韻、朗誦、賞析與評量方向，不複製教材正文、題目或答案。

## D-086：Ad-Ⅳ-2 四類現代文體三版本來源重新核對

- 日期：2026-09-23
- 決策：Ad-Ⅳ-2 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有來源混用出版社索引與不同層級課程資料，無法直接形成可回讀的單元證據；本次核對新詩、現代散文、現代小說、劇本的形式／內容／寫作特色與評量方向，不複製教材正文、題目或答案。

## D-085：Ad-Ⅳ-1 篇章主旨結構寓意分析三版本來源重新核對

- 日期：2026-09-23
- 決策：Ad-Ⅳ-1 的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原有部分資料雖是公立課程計畫，但來源層級與單元定位不一致；本次統一回讀可核對的國中國文課程資料，確認篇章閱讀、主旨／結構、寓意推論與評量方向，不複製教材正文、題目或答案。

## D-084：Ab 字詞主題三版本來源以可回讀公立課程資料核對

- 日期：2026-09-23
- 決策：Ab 字詞主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 Ab 主題部分來源是出版社入口或錯誤／不足的課程資料，不能直接支持本單元；本次以可回讀資料核對字詞形音義、語境判讀、句段理解與評量方向，不複製教材正文、題目或答案。

## D-083：A 文字篇章主題三版本來源以可回讀公立課程資料核對

- 日期：2026-09-23
- 決策：A 文字篇章主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 A 主題部分來源只提供出版社首頁或錯誤科目／課程資料，不能直接支持本單元；本次以可回讀的公立課程資料核對文字篇章、文本證據、段落組織、主旨／結構與評量方向，不複製教材正文、題目或答案。

## D-082：Ad 篇章主題三版本來源以可回讀公立課程資料核對

- 日期：2026-09-23
- 決策：Ad 篇章主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中國文領域翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程資料核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先 Ad 的康軒與南一 URL 實際內容無法支持本單元國中國文篇章定位；本次改用可回讀且能支持篇章閱讀、段落組織、主旨／結構、文本理解與評量方向的公立課程資料。僅保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-081：Ac 句段主題三版本來源重新核對

- 日期：2026-09-23
- 決策：Ac 句段主題的翰林、康軒、南一 publisher evidence 改以彰化縣公立國中翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版課程計畫核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：原先部分來源只支持索引或錯誤科目，不能直接沿用；本次改以可回讀的國文課程資料支持句段、標點、句型、文句邏輯與篇章理解範圍。

## D-080：Ac-Ⅳ-3 三版本來源以文句邏輯課程計畫核對

- 日期：2026-09-23
- 決策：Ac-Ⅳ-3 的翰林、康軒、南一 publisher evidence 以彰化縣公立國中翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程計畫核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：三筆資料實際支持文句邏輯與意義、文本理解、提問和表達評量；只保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-079：Ac-Ⅳ-2 三版本來源以句型課程計畫核對

- 日期：2026-09-23
- 決策：Ac-Ⅳ-2 的翰林、康軒、南一 publisher evidence 以彰化縣公立國中翰林版、高雄市公立國中康軒版與嘉義縣永慶國中南一版公開課程計畫核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：來源實際支持敘事、有無、判斷、表態句型與句型判斷／造句／表達評量；僅保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-078：Ac-Ⅳ-1 三版本來源以公開課程計畫核對

- 日期：2026-09-23
- 決策：Ac-Ⅳ-1 的翰林、康軒、南一 publisher evidence 以彰化縣公立國中翰林版、高雄市公立國中康軒版及嘉義縣永慶國中南一版公開課程計畫核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：三筆資料均能回讀標點在文本中的作用／不同效果與相關評量方向；只保存課程定位與教學結構，不複製教材正文、題目或答案。

## D-077：Ab-Ⅳ-8 三版本來源以可回讀公立教育資料核對

- 日期：2026-09-23
- 決策：Ab-Ⅳ-8 的翰林、康軒、南一 publisher evidence 以彰化縣公立國中翰林版課程計畫、臺北市士林國中康軒版教育部資源頁及彰化縣福興國中南一版課程計畫交叉核對，三個 slots 記為 `verified`；lesson 與題目維持 `draft`。
- 理由：資料實際支持書體、名家碑帖、書法欣賞、行款布局與作品表達；僅保存來源定位與教學結構，不複製教材或題目內容，也不把來源核對誤稱為內容審查完成。

## D-076：Ab-Ⅳ-7 三版本來源改以可回讀公立課程計畫為證據

- 日期：2026-09-23
- 決策：Ab-Ⅳ-7 的翰林、康軒、南一 publisher evidence 改以彰化縣、臺中市及國立卓蘭高中附設國中部公開課程計畫核對，三個 slots 記為 `verified`；教材正文、題目與答案仍不複製，lesson 維持 `draft`。
- 理由：每個版本欄位必須能實際支持科目、版本、課綱節點與評量脈絡；公開課程計畫只能作可追溯的章節級證據，不等同完成內容審查或正式發布。

## D-071：Ab-Ⅳ-1 翰林來源需以實際內容回讀為準

- 日期：2026-09-23
- 決策：Ab-Ⅳ-1 原先登錄的嘉義縣 PDF URL 經回讀後確認主要內容為英語／綜合活動，不能作為國中國文翰林版證據；改用臺北市立北安國中 114 學年度「國文（翰林版）」公開課程計畫，定位至 PDF 第 1 頁的 Ab-Ⅳ-1 條目。
- 理由：來源 ledger 只接受能實際支持出版社、科目與課綱節點的公開證據；不能因檔名或歷史紀錄看似符合就保留錯誤 mapping。原 lesson 與題目維持 draft，直到三版本 evidence 與後續 QA 均完成。

## D-072：Ab-Ⅳ-2 沿用錯誤翰林 URL 必須替換

- 日期：2026-09-23
- 決策：Ab-Ⅳ-2 原先沿用的嘉義縣 PDF URL 與 Ab-Ⅳ-1 相同，回讀確認並非國中國文翰林課程資料；改用臺北市立北安國中 114 學年度「國文（翰林版）」公開課程計畫，定位至 PDF 第 1 頁的 Ab-Ⅳ-2 條目。
- 理由：同一來源若無法支持目前單元的科目與版本，不得因其他單元已使用而直接沿用；每一 unit 的 publisher evidence 都要能逐筆追溯。

## D-073：Ab-Ⅳ-4 翰林來源改用可回讀的國文課程計畫

- 日期：2026-09-23
- 決策：Ab-Ⅳ-4 原先登錄的嘉義縣 PDF URL 未能在回讀內容中支持國中國文語詞認念，改用臺北市立北安國中 114 學年度「國文（翰林版）」公開課程計畫，定位至 PDF 第 1 頁的 Ab-Ⅳ-4 條目。
- 理由：每個 publisher slot 必須由實際可讀的科目、版本與課綱節點證據支持；不能因同一 URL 曾被其他單元引用而推定本單元也成立。

## D-001：官方課綱優先

- 日期：2026-08-25
- 決策：課程範圍、學習表現與內容主張以教育部／國教署發布的十二年國教課綱為 source of truth。
- 理由：教材版本是對照目標，不是本專案的課程權威。

## D-002：以統一 Knowledge Graph 做為跨版本樞紐

- 日期：2026-08-25
- 決策：版本對照連至穩定 knowledge ID；不直接以出版商章節建構核心資料模型。
- 理由：降低版本改版對教材、題庫與產品的連鎖破壞。

## D-003：只收錄最小必要的版本證據

- 日期：2026-08-25
- 決策：版本對照儲存出版商、版本／年級／冊別、章節位置、證據定位與關係，不儲存教科書全文或題文。
- 理由：保留可查核性並避免侵害著作權。

## D-004：資料驅動 UI

- 日期：2026-08-25
- 決策：教材、題目、概念與 mapping 不可寫死於 UI 程式；透過已驗證的資料層提供。
- 理由：讓內容 QA 與產品迭代可獨立進行。

## D-005：M1 只登錄五科領域層官方索引

- 日期：2026-08-25
- 決策：M1 每科先建立一筆 `verified` 領域層節點，來源定位至國教署同一份官方課綱索引；不在此階段抄錄或推論細粒度課綱內容。
- 理由：先建立五科可驗證、低著作權風險的來源根節點，再以可定位的官方文件逐步拆解。

## D-006：M2 先以官方「學習重點」結構建立圖譜骨架

- 日期：2026-08-25
- 決策：五科先以官方文件明列的學習表現、學習內容及其從屬關係建立圖譜骨架；自然、社會採文件明確標示的國中階段範圍。
- 理由：建立可驗證的共同資料骨架，避免在尚未逐表核對前自行發明概念、先備關係或會考範圍。

## D-007：自然科主題 A 僅依官方表格階層建圖

- 日期：2026-08-25
- 決策：本批自然科學只收錄國民中學教育階段學習內容的主題 A、次主題 Aa／Ab 與其明列代碼；圖譜只建立官方表格直接支持的 `partOf` 關係。
- 理由：維持官方代碼與表格從屬階層，避免將未明示的先備、因果或跨概念關係視為課綱事實。

## D-008：M2 細粒度 ID 與關係只忠實表達官方表格

- 日期：2026-08-25
- 決策：五科第四學習階段官方「學習表現／學習內容」表格的正式代碼轉為穩定 ASCII ID；display label 保留官方代碼字形。羅馬數字 `Ⅳ` 在 ID 中固定轉為 `iv`。社會領域的「社／歷／地／公」分別使用 `soc／hist／geo／civ`，避免跨科代碼碰撞。
- 關係：一般表格結構只建立 `partOf`；不因表格順序、教材編排或概念直覺推論 `prerequisiteOf`、`appliesTo`、`contrastsWith`。自然科學跨科主題表明確列出的 19 個次主題關聯，以 `relatedTo` 表示，除此之外不新增推論關係。
- 內容：官方主題與次主題名稱作為結構標籤；細碼節點只保存官方代碼與本專案的最小摘要，來源欄保存官方 PDF、發布日、查核日、正文／PDF 頁碼範圍及官方代碼定位。
- 理由：將可驗證的官方表格事實與後續教材／題庫的教學推論分離，維持來源可追溯性與穩定 ID。

## D-009：M2 完成界線定義為五科第四學習階段官方學習重點表格

- 日期：2026-08-25
- 決策：M2 在五科第四學習階段「學習表現」與「學習內容」官方表格完成逐碼建模、Schema 與端點驗證後，標記為 completed。
- 完成範圍：自然科包含國中學習表現、一般學習內容及自然科學跨科主題；社會領域包含國中學習表現及國中必修歷史、地理、公民與社會表格；國文、英文、數學包含其第四學習階段官方學習表現與學習內容表格。
- 非完成範圍：不代表五科課綱所有敘述章節、國中教育會考實際命題範圍、南一／康軒／翰林版本 mapping、教材、題庫或網站產品已完成。
- 下一階段：M3 才進行出版社版本 mapping；M4 才建立自編教材與題庫。

## D-010：M3 允許國家教育研究院審定本清冊作為版本存在性證據

- 日期：2026-08-25
- 決策：`textbook-mapping.schema.json` 的 `evidence.type` 新增 `official-government-list`，用於國家教育研究院公布之教科用書審定／清冊資料。
- 限制：政府清冊只足以證實出版社、科目、冊次、年級與審定狀態；不能單獨證明課本章節如何對應細粒度 Knowledge Graph。
- 理由：M3 需要把「冊別存在性」與「章節概念 mapping」兩種證據層級分開，避免以整冊清冊過度推論章節內容。

## D-011：M3 先建立整冊存在性基線，不冒充章節級 mapping

- 日期：2026-08-25
- 決策：南一、康軒、翰林的六冊資料先以各科 `learning-content` 根節點建立 `supporting` 基線；`chapterLabel` 明確標示「整冊（冊別存在性基線）」。
- 特例：115 學年度國中英語審定本清冊列出佳音、南一、康軒，沒有以翰林為審定出版者；但翰林官方書城另公開銷售國中 `i英語` 課本。因此翰林英語 mapping 只表示翰林官方教材／書城體系的冊別存在，notes 必須保留此差異，不得把翰林說成該審定執照的出版者。
- 完成界線：此批 M3 是三版本整冊基線，不代表 90 冊都已完成章節／單元到細粒度 KG 的對照。

## D-012：M4 基線內容必須為原創並連至穩定 KG ID

- 日期：2026-08-25
- 決策：建立五科各一份原創 lesson 與三題原創 question 作為 M4 資料管線基線；全部標示 `origin=original`，不從出版社課本、習作或題庫改寫。
- 狀態：基線內容可標記 `content-reviewed`，但 M4 不因少量示例內容而宣稱完整。

## D-013：章節級 mapping 採集合檔並區分來源事實與教學判斷

- 日期：2026-08-25
- 決策：整冊存在性基線繼續使用單筆 `map-` 資料；章節級對照改用 `textbook-mapping-set.schema.json`，以出版社／科目為一個 `mapset-` 集合，內含六冊與章節條目。每個章節可連到一個以上既有 Knowledge Graph ID。
- 證據界線：章節代碼與名稱取自出版社官方公開資源；115 學年度冊別存在性仍由既有國家教育研究院清冊基線支持。兩種來源各自證明不同事實，不互相替代。
- 教學判斷：章節到 KG 的關係屬本專案依章名與官方課綱節點做的保守對照，信心等級標為 `medium`，不可解讀為出版社或主管機關背書。
- 著作權限制：只保存章節名稱、代碼、來源定位與最小必要對照，不收錄課文、題目、影音或其他受保護內容。

## D-014：M5 先採可部署的資料驅動靜態 MVP

- 日期：2026-08-25
- 決策：第一版產品使用無 build command 的靜態前端；資料由 manifest 指向 repo JSON，瀏覽器執行時載入 project state、原創 lesson/question，UI 不硬編碼教材內容。
- 理由：先驗證資料層到使用者介面的最小閉環，降低部署依賴；後續可在不改資料契約的前提下替換框架或 API。
- 限制：目前依賴 GitHub raw main 分支、沒有登入與學習進度保存，也尚未完成自動化測試與正式部署驗收。

## D-015：資料驗證改由可重複執行的 CI workflow 負責

- 日期：2026-08-25
- 決策：將 JSON 語法、對應 Schema、全域 ID、KG endpoint 與 M4 provenance 檢查集中在 `scripts/validate_data.py`，由 `.github/workflows/validate-data.yml` 於 push／pull request 執行。
- 理由：讓每次資料變更都能在遠端環境重現驗證，降低只依賴人工檢查的風險。

## D-016：M4 採課綱／KG 對照的原創內容流程

- 日期：2026-08-25
- 決策：M4 lesson／question 以官方課綱與穩定 KG ID 決定學習目標，再由本專案自行寫作；不以網路題庫、出版社題目或課文改寫成「原創」。
- 答案要求：每題必須有可檢查的 answer.value 與 answer.explanation；選擇題需檢查唯一最佳答案與 distractors。
- 來源要求：外部資料若只作事實查核，記錄 sourceUrl／sourceLocator；若直接收錄合法公開題，必須改標 official-open 或 licensed，不可標為 original。
- 審核界線：content-reviewed 表示 repo 內部檢查，不代表教師或學科專家審查。

## D-017：每個 M4 lesson 至少配置十題

- 日期：2026-08-25
- 決策：每個 lesson 以 question.lessonId 明確關聯至少 10 題；不足時 CI 失敗。
- 理由：單一教材單元若只有零星示例，無法支援理解、練習與錯誤診斷。
- 答案：每題都必須有 answer.value 與 answer.explanation，不能只提供題目或答案字母。
\n## D-018：以公開學霸筆記作重點研究，不作內容轉載\n\n- 日期：2026-08-25\n- 決策：搜尋公開學習筆記與複習策略頁，將可泛化的學習策略改寫為 lesson.studyHighlights；不複製原文或外部題庫。\n- 驗收：10 份 lesson 均有至少 3 條 highlights 與 source URL；數學／自然 4 份 lesson 各有至少 3 步互動教學。\n- 依據：docs/M4_STUDY_NOTE_HIGHLIGHTS.md。\n

## D-020：Coverage matrix 先於內容擴充

- 日期：2026-08-25
- 完成：已 materialize 1,032 份 curriculum JSON 的逐筆 coverage matrix，包含 subject、title、gradeRange、lessonId、questionCount、interactiveStatus、contentStatus。
- 現況：僅 7 筆可直接對應既有 baseline；其餘保持 not-started，避免虛報覆蓋率。
- 下一步：M4-003 逐筆完成國文 84 筆。

## D-021：M4-003 國文首批內容完成

- 日期：2026-08-25
- 完成：新增 Ab-Ⅳ-1、Ac-Ⅳ-1、Ad-Ⅳ-1 三個國文課綱節點的原創 lesson，各 10 題，均有答案與解析。
- 尚未完成：國文仍有 81 筆 coverage rows 未完成；本批不代表國文全科完成。


## D-022：M4-003 國文第二批內容完成

- 日期：2026-08-25
- 完成：新增 Ab-Ⅳ-2、Ab-Ⅳ-3、Ab-Ⅳ-4 三個國文課綱節點的原創 lesson，各 10 題。
- 尚未完成：國文仍有 78 筆 coverage rows 未完成。


## D-023：解決國文第二批題目品質 blocker

- 日期：2026-08-25
- 完成：Ab-Ⅳ-2、Ab-Ⅳ-3、Ab-Ⅳ-4 各 10 題已改為單元特定內容，並補上對應解析。
- 狀態：內容審查完成，CI 執行結果待確認。


## D-024：M4-003 國文第三批內容完成

- 日期：2026-08-25
- 完成：Ab-Ⅳ-5、Ab-Ⅳ-6、Ab-Ⅳ-7，各新增 1 份 lesson、10 題原創 question。
- 尚未完成：國文仍有 75 筆 coverage rows 未完成。


## D-025：M4-003 國文第四批內容完成

- 日期：2026-08-25
- 完成：Ab-Ⅳ-8、Ac-Ⅳ-1、Ac-Ⅳ-2，各新增 1 份 lesson、10 題原創 question。
- 尚未完成：國文仍有 72 筆 coverage rows 未完成。


## D-026：M4 改採批次流水線，不以低品質模板冒充完成

- 日期：2026-08-25
- 決策：不宣稱可在單一回合可靠產生 10,320 題正式題庫；改用 coverage matrix 驅動的批次產生、驗證與 QA。
- 狀態：已採用；後續未完成內容統一標 draft，通過內容 QA 才升級。

## D-027：題庫改採可追溯歷屆題與獨立改編規則

- 日期：2026-08-28
- 決策：題目不得因「每單元至少 10 題」而以重複模板灌數；同一 lesson 的重複題幹或完整題目由 QA 直接失敗。
- 歷屆會考題：先核對其依法令舉行考試的來源與可利用範圍，記錄年度、科目、題號、sourceUrl、sourceLocator、答案與解析。
- 公立國中考題：公開下載不自動視為授權。取得明示授權者可依授權收錄或改編，標示 `provenance.origin=licensed`；沒有授權者只作能力／題型研究，站內重新獨立命題，不把換數字或換情境的近似題標為 original。
- 來源題的 `provenance` 必須同時有 `sourceUrl` 與 `sourceLocator`；原創題仍須通過單元符合度、答案驗算與人工內容 QA。
- 狀態：已採用；現有重複題須退回修正，未完成來源核對前不得宣稱題庫 QA 通過。

## D-028：本專案採 AI 判讀審查，不設真人 reviewer

- 日期：2026-08-28
- 決策：本專案沒有真人 reviewer；題目與教材的內容判讀、答案檢查、來源界線與重複題 QA 均由 AI 執行。
- 狀態定義：`content-reviewed` 代表 AI 審查流程通過，不代表教師、真人或學科專家認證；未完成 AI 審查者維持 `draft`。
- 建議：涉及較高語意判斷時，優先升級 Terra model 進行第二輪 AI 複核；Terra 仍屬 AI，不能改標為真人審查。
- 理由：明確反映本專案實際審查流程，避免將自動驗證或 AI 判讀誤述為真人審定。

## D-031：英文與社會公開試題批次改編

- 日期：2026-08-28
- 本批來源：同一所公立國中九年級英文與社會段考；題目頁與答案頁均已下載並核對，索引保存於 `data/public-exam-sources.json`。
- 使用界線：英文只取文法題型；社會只取穩定的歷史概念，避開來源中的不穩定時事敘述；兩科均重新設計題幹、選項與解析，不保存原試卷全文。
- 本批結果：英文文法 10 題、社會歷史 10 題完成獨立改編；答案分布與唯一最佳答案已由 AI 自我檢查，均維持 `draft`，待 Terra 第二輪 AI 複核後才可升級。

## D-032：114 年會考國文詞語批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科試題本與選擇題參考答案表；題本與答案 URL、頁碼／題號定位已寫入來源索引。
- 使用界線：只採詞語使用、詞義與成語辨析的能力方向，重新設計語境、選項與解析，不保存會考原文或原選項。
- 本批結果：替換「常用語詞的正確使用」10 題；已由 AI 檢查唯一最佳答案、答案分布、單元符合度與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-033：114 年會考數學機率批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採等可能結果、卡片／球／骰子機率的能力方向，重新設計數據與情境並重算解析，不保存會考原文或圖表。
- 本批結果：替換「D-9-3：古典機率」10 題；已由 AI 檢查樣本空間、有利結果、機率化簡、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-034：114 年會考英文閱讀批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採人物、事件、原因、時間與結果的閱讀理解能力方向，重新撰寫短文與選項，不複製會考文章、圖片或原選項。
- 本批結果：替換「Ae-Ⅳ-6：故事背景人物事件結局」10 題；已由 AI 檢查題幹證據、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-035：114 年會考自然元素化合物批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採物質分類、化學式、原子序與離子判讀的能力方向，重新設計數據與情境並重算答案，不保存原題文字、圖表或選項。
- 本批結果：替換「元素與化合物」10 題；已由 AI 檢查質子／電子數、電荷、固定比例、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-036：114 年會考社會地理批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採自然災害、季風地形、水資源、碳匯、能源與人地調適的能力方向，重新設計情境、選項與解析，不保存原題文字或圖表。
- 本批結果：替換「地 Be-Ⅳ-1：自然環境」10 題；已由 AI 檢查自然條件與結論的因果關係、唯一最佳答案、選項分布與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-037：114 年會考自然全球暖化批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採二氧化碳封存、碳匯、溫室效應、節能與科學探究變因的能力方向，重新設計情境與數據，不保存原題文字、圖片或選項。
- 本批結果：替換「Me-Ⅳ-4：溫室氣體與全球暖化」10 題；已由 AI 檢查科學因果、控制變因、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-038：114 年會考國文字音字形批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採字音、字形與詞義辨析的能力方向，重新設計詞語與選項，不保存會考原文或原選項。
- 本批結果：替換「常用字的形、音、義」10 題；已由 AI 逐題檢查讀音、成語字形、唯一最佳答案、干擾項與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-039：114 年會考社會政治經濟批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採制度、國際會議、交通貿易、產業技術、勞動市場、區域整合與公共參與的能力方向，重新設計情境與選項，不保存原題文字或圖表。
- 本批結果：替換「Ea：政治經濟的變遷」10 題；已由 AI 檢查因果關係、唯一最佳答案、選項分布與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-040：114 年會考國文進階詞語批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採詞語搭配、近義語氣與成語使用限制的能力方向，重新設計語境、選項與解析，不保存會考原文或原選項。
- 本批結果：替換「常用語詞使用進階」10 題；已由 AI 檢查語意、搭配、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-041：114 年會考自然混合物批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採元素／化合物／混合物分類、分離方法與物質性質判讀的能力方向，重新設計情境與選項，不保存原題文字或圖表。
- 本批結果：替換「Ab-Ⅳ-4：純物質與混合物分類」10 題；已由 AI 檢查分類定義、分離原理、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-042：114 年會考國文閱讀寫作批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採文意、轉折、前後照應、敘述觀點、證據與主旨判讀的能力方向，重新撰寫短文與選項，不保存會考原文或原選項。
- 本批結果：替換「5-Ⅳ-3：理解文本內容形式與寫作特色」10 題；已由 AI 檢查題幹證據、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-043：114 年會考自然結構功能批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科試題本與官方選擇題參考答案表；題號與答案定位已核對。
- 使用界線：只採分子／原子、離子、化學式、物質變化與結構—性質關係的能力方向，重新設計數據與情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Cb：物質的結構與功能」10 題；已由 AI 檢查粒子數、電荷、化學式計數、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-044：公立國中英文引導討論批次改編

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中九年級英文段考試題與答案頁，題號與答案定位已核對。
- 使用界線：只採基本問答、對話理解、理由與資料情境的能力方向，重新設計討論內容與選項，不保存原題文字或對話。
- 本批結果：替換「2-Ⅳ-12：引導式討論」10 題；已由 AI 檢查語用適切性、唯一最佳答案、選項分布與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-045：會考與公立國中數學一次函數批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科試題與官方答案表，並參考高雄市立鹽埕國中公開數學段考的坐標／函數能力方向。
- 使用界線：只採代入坐標、斜率、坐標軸截距與參數判讀，重新設計數值與情境並逐題重算，不保存原題文字、圖表或選項。
- 本批結果：替換「F-8-2：一次函數的圖形」10 題；已由 AI 檢查計算、唯一最佳答案、選項分布與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-029：數學與自然科採資料驅動的自建操作模型

- 日期：2026-08-28
- 決策：數學與自然科 lesson 以穩定 KG ID 與 `lessonScope` 指派 `simulation` 資料契約；前端依 engine 呈現可調變因、即時可視化結果、預測／觀察／解釋歷程與重設控制，不再把所有型別一律降成選擇題。
- 範圍：具體學習內容採對應的數學或自然模型；主題、領域與學習表現頁使用 `concept-explorer`，不得冒充為可驗證的科學實驗。心臟血流作為生命系統模型的資料設定，不以 lesson ID 寫死在 UI。
- 隱私：學習歷程僅以版本化 localStorage 存在使用者目前裝置；不設帳號、教師監看或雲端同步。
- 來源與審查：每個 simulation 重用 lesson 的公開 `studyReferences`。資料契約和瀏覽器操作驗證不等同內容審查；模型數值、概念適用性與提示語仍須依 AI 審查規則複核。

## D-030：公開試題下載與逐題安全改編

- 日期：2026-08-28
- 決策：公開公立國中題本先下載並分開核對題目頁與答案頁；只將能確認單元、題號、答案與改編差異的題目寫入題庫。
- 本批來源：高雄市立鹽埕國中 114 學年度第 2 學期第 1 次段考九年級數學與自然試題，索引保存於 `data/public-exam-sources.json`。
- 使用界線：不把原始 PDF 提交到 repo；站內僅保存獨立改編題與 `sourceUrl`／`sourceLocator`。未取得明示授權時，不複製原題文字、圖表或答案卷。
- 本批結果：20 題數學題完成來源題號核對與獨立改編；另有 173 題重複／模板題完成單元化重寫並維持 `draft`，等待第二輪 AI 內容複核。資料 validator 已確認重複簽章為 0，但不把結構驗證當成內容完成。

## D-046：114 年會考社會法律規範批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科試題本與官方答案表；題號與答案定位已核對。
- 使用界線：只採法院、法律諮詢、權利保障及法律與習俗／道德規範差異的能力方向，重新設計情境與選項，不保存原題文字或圖表。
- 本批結果：替換「公 Bc-Ⅳ-1：社會規範及法律與其他規範差異」10 題；AI 檢查規範來源、適用範圍、制裁方式、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-047：國文成語重複題幹改為情境化問法

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本與答案表；只採成語語境判讀的能力方向。
- 本批結果：修正 4 題跨課重複題幹，改成不同的展覽、導覽、演講與校刊情境；選項、答案解析與來源標示仍保留並維持 `draft`。
- 審查界線：此批只消除可確認的重複問法，不代表已完成全庫 Terra 第二輪內容複核。

## D-048：114 年會考自然溫度與物質狀態批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採溫度變化、相變、粒子模型、熱傳與沸點判讀的能力方向。
- 使用界線：重新設計熔化、沸騰、蒸發、熱平衡與氣壓情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Ab-Ⅳ-2：溫度與物質狀態」10 題；AI 檢查單元對齊、物理概念、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-049：114 年會考自然物理與化學性質批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採物理性質、化學性質、物理變化與化學變化的判讀方向。
- 使用界線：重新設計密度、沸點、導電性、反應性與物質鑑定情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Ab-Ⅳ-3：物理與化學性質」10 題；AI 檢查分類定義、化學變化證據、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-050：114 年會考自然粒子模型與三態批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採粒子排列、三態特徵、壓縮性、擴散與物態變化的能力方向。
- 使用界線：重新設計容器、氣球、色素與相變情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Ab-Ⅳ-1：粒子模型與三態」10 題；AI 檢查粒子模型與可觀察現象的對應、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-051：114 年會考自然原子模型批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採原子模型、實驗證據、原子核與科學模型修正的能力方向。
- 使用界線：重新設計散射實驗、粒子電荷、模型限制與證據修正情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Aa-Ⅳ-1：原子模型演變」10 題；AI 檢查原子模型概念、證據支持、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-052：114 年會考自然相對質量批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採相對原子質量、相對分子／式量與化學式下標判讀的能力方向。
- 使用界線：重新設計化學式與數值計算，不保存原題文字、圖表或選項。
- 本批結果：替換「Aa-Ⅳ-2：相對原子與分子質量」10 題；AI 檢查計算、單位概念、化學式解讀、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-053：114 年會考自然元素週期性批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採週期表排列、週期與族、元素位置及性質規律的能力方向。
- 使用界線：重新設計原子序、電子層、同族比較與資料預測情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Aa-Ⅳ-4：元素性質週期性」10 題；AI 檢查週期表概念、推論限制、唯一最佳答案、選項可排除性與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-054：114 年會考自然元素與化合物符號批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題本與答案表；只採元素符號、化學式、下標／係數與原子數判讀的能力方向。
- 使用界線：重新設計 H₂O、CO₂、NaCl 等化學式情境與計算，不保存原題文字、圖表或選項。
- 本批結果：替換「Aa-Ⅳ-5：元素與化合物符號」10 題；AI 檢查符號、化學式讀法、原子數計算、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-055：114 年會考社會多元文化批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表；只採多元文化、文化交流、資料代表性與公共協商的能力方向。
- 使用界線：重新設計校園、城市、新聞資料與公共空間情境，不保存原題文字、圖表或選項。
- 本批結果：替換「地 Be-Ⅳ-2：多元文化」10 題；AI 檢查文化脈絡、刻板印象、資料推論、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-056：114 年會考社會自然資源批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表；只採自然資源分類、分布、利用、永續發展與資料判讀的能力方向。
- 使用界線：重新設計地下水、風力、礦產、能源與資源政策情境，不保存原題文字、圖表或選項。
- 本批結果：替換「地 Bf-Ⅳ-1：自然資源」10 題；AI 檢查地理因果、資源限制、資料代表性、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-057：114 年會考社會文化變遷批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表；只採社會文化變遷、科技與人口流動、跨時期資料及因果分析的能力方向。
- 使用界線：重新設計都市化、資訊傳播、文化交流、制度變化與統計資料情境，不保存原題文字、圖表或選項。
- 本批結果：替換「Eb：社會文化的變遷」10 題；AI 檢查時間順序、資料範圍、因果推論、文化脈絡、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-058：114 年會考社會商貿與文化交流批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表；只採商路、港口、商品流通、史料範圍與文化交流的能力方向。
- 使用界線：重新設計市場、航線、考古物與旅行記錄情境，不保存原題文字、圖表或選項。
- 本批結果：替換「歷 Ia-Ⅳ-2：商貿與文化交流」10 題；AI 檢查歷史因果、史料代表性、文化脈絡、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-059：公立國中英文公共場所廣播批次改編

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中九年級英文段考公開題本；只採公共場所廣播的資訊擷取、時間地點與目的判讀能力方向。
- 使用界線：重新設計圖書館、機場、車站、校園與博物館廣播，不保存原題文字或對話。
- 本批結果：替換「1-Ⅳ-11：公共場所廣播」10 題；AI 檢查語意、時間／地點資訊、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-060：公立國中英文歌謠韻文批次改編

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中九年級英文段考公開題本；只採押韻、音節、重音、頭韻與規律節奏的能力方向。
- 使用界線：全部使用本專案自編短句，不引用或重製既有歌曲歌詞。
- 本批結果：替換「1-Ⅳ-10：歌謠韻文節奏音韻」10 題；AI 檢查英文語音判讀、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-061：公立國中英文角色扮演批次改編

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中九年級英文段考公開題本；只採角色目標、日常情境語用與對話回應的能力方向。
- 使用界線：重新設計咖啡店、問路、商店、旅館、車站與面試情境，不保存原題文字或對話。
- 本批結果：替換「2-Ⅳ-9：角色扮演」10 題；AI 檢查英文語意、語用適切性、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-062：公立國中英文基本世界觀批次改編

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中九年級英文段考公開題本；只採跨文化理解、全球議題、資料來源與避免刻板印象的能力方向。
- 使用界線：重新設計交換學生、時區、環境、飲食、統計與新聞閱讀情境，不保存原題文字或圖表。
- 本批結果：替換「8-Ⅳ-5：基本世界觀」10 題；AI 檢查英文語意、跨文化適切性、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-063：114 年會考社會漢南非洲自然資源批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表，並以國教院社會領域課綱確認 `地 Bg-Ⅳ-1` 為漢南非洲自然環境與資源。
- 使用界線：重新設計乾濕季、草原、礦產、交通、水資源與保育情境，不保存原題文字、圖表或選項。
- 本批結果：替換「地 Bg-Ⅳ-1：自然環境與資源」10 題；AI 檢查區域定位、地理因果、資源利用、永續觀點、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-064：114 年會考社會歐洲與俄羅斯自然環境批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表，並以國教院社會領域課綱確認 `地 Bh-Ⅳ-1` 為歐洲與俄羅斯自然環境背景。
- 使用界線：重新設計海洋調節、地中海型氣候、山地、河流、凍土與地圖情境，不保存原題文字、圖表或選項。
- 本批結果：替換「地 Bh-Ⅳ-1：自然環境背景」10 題；AI 檢查區域定位、氣候與地形因果、資料範圍、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-065：114 年會考社會美洲自然環境批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考社會科公開試題本與答案表，並以國教院社會領域課綱確認 `地 Bi-Ⅳ-1` 為美洲自然環境背景。
- 使用界線：重新設計緯度、山脈、平原、亞馬遜水系、熱帶雨林、雨影與災害資料情境，不保存原題文字、圖表或選項。
- 本批結果：替換「地 Bi-Ⅳ-1：自然環境背景」10 題；AI 檢查區域定位、自然環境因果、地圖疊圖、資料範圍、唯一最佳答案與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-066：公立國中數學總分類模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以國教院官方數學課綱核對範圍。
- 使用界線：只研究公開題型與能力方向；重新編寫折扣、一次函數、二次方程式、幾何、統計、機率、比例、數列與座標平移情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-learning-content` 的 10 題泛用模板；AI 逐題重算答案、檢查四個選項唯一性、單元範圍、來源界線與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-067：114 年會考國文論證單元模板題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本與答案表，並以國教院語文領域課綱核對 `Bd-Ⅳ-2：比較比喻等論證`。
- 使用界線：只研究閱讀理解、論證、比較與寫作分析的能力方向；重新編寫比喻、共同比較標準、證據、資料公平性與論證漏洞情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bd-iv-2` 的 10 題固定選項題；AI 檢查論證概念、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-068：公立國中數學學習表現總分類模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以國教院官方數學課綱核對範圍。
- 使用界線：只研究公開試題的解題、表徵與推理能力方向；重新編寫方程式、比例、幾何、統計、機率、函數、因式分解、數列與不等式題，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-learning-performance` 的 10 題泛用模板；AI 逐題重算答案、檢查選項唯一性、答案位置分散、來源界線與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-070：公立國中國文經驗分享單元模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `2-Ⅳ-1`。
- 使用界線：只研究經驗分享、口語組織與聆聽回應的能力方向；重新編寫背景交代、事件順序、聽眾調整、具體證據、銜接、收束與尊重界線情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-2-iv-1` 的 10 題固定選項題；AI 檢查情境符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-071：公立國中數學學習表現總分類模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以國教院官方數學課綱核對範圍。
- 使用界線：只研究公開試題的解題、表徵與推理能力方向；重新編寫方程式、比例、幾何、統計、機率、函數、因式分解、數列與不等式題，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-learning-performance` 的 10 題泛用模板；AI 逐題重算答案、檢查選項唯一性、答案位置分散、來源界線與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-069：114 年會考國文 Bd-Ⅳ-2 論證批次改編

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本與答案表，並以國教院語文領域課綱核對 `Bd-Ⅳ-2：比較比喻等論證`。
- 使用界線：只研究閱讀理解、論證、比較與寫作分析的能力方向；重新編寫比喻、共同標準、證據、資料公平性與論證漏洞情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bd-iv-2` 的 10 題固定選項題；AI 檢查概念符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-072：公立國中國文說明方法單元模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `Bc-Ⅳ-2`。
- 使用界線：只研究列舉、因果、比較、分類、定義與問題解決的說明能力方向；重新編寫校園、環境與公共議題短文，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bc-iv-2` 的 10 題固定選項題；AI 檢查方法符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-073：公立國中國文客觀說明單元模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `Bc-Ⅳ-1：邏輯客觀理性說明`。
- 使用界線：只研究公開試題的說明與閱讀理解能力方向；重新編寫統計範圍、因果證據、客觀措辭、公平比較、研究主張與結論限制情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bc-iv-1` 的 10 題固定選項題；AI 檢查資料與課綱符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-081：114 年會考國文一字多音多義模板題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本與答案表，並以國教院語文領域課綱核對 `4-Ⅳ-3：字辭典處理一字多音多義`。
- 使用界線：只研究字音、詞義與語境判讀能力方向；重新編寫「行、長、樂、降、參、處、數、傳、薄」等詞語情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-3` 的 10 題固定選項題；AI 檢查注音、詞義、語境、字典查證步驟、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-082：公立國文書體與碑帖欣賞模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `4-Ⅳ-4：認識書體與欣賞碑帖`。
- 使用界線：只研究書體辨識、碑帖概念與書法評析能力方向；重新編寫楷書、行書、草書、隸書、章法、結構與臨寫檢核情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-4` 的 10 題固定選項題；AI 檢查書體特徵、局部與整體、評析證據、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-078：公立國中國文科技資訊表達模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `2-Ⅳ-4：運用科技資訊豐富表達`。
- 使用界線：只研究公開試題的資料判讀與表達能力方向；重新編寫來源可信度、交叉查證、圖表、引用、著作權、受眾與限制揭露情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-2-iv-4` 的 10 題固定選項題；AI 檢查資訊素養、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-079：114 年會考國文詞語使用模板題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本與答案表，並以國教院語文領域課綱核對 `4-Ⅳ-1：認識至少4500字並使用3500字`。
- 使用界線：只研究詞語理解、成語語義與語境使用能力方向；重新編寫「佇立、不約而同、絡繹不絕、相形見絀、首當其衝」等詞語的獨立語境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-1` 的 10 題固定選項題；AI 檢查詞義、搭配、語境、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-080：公立國文造字原則形音義模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `4-Ⅳ-2：造字原則輔助形音義理解`。
- 使用界線：只研究文字辨識與形音義判讀能力方向；重新編寫形聲字、會意字、形旁、聲旁與推論限制情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-2` 的 10 題固定選項題；AI 檢查造字結構、形音義推論、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-083：公立國文書法行款布局行氣模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `4-Ⅳ-5：欣賞書法行款布局行氣風格`。
- 使用界線：只研究書法作品的布局、行款、行氣與風格評析能力方向；重新編寫留白、行距、字距、重心、碑帖比較與臨寫檢核情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-5` 的 10 題固定選項題；AI 檢查書法術語、局部與整體評析、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-084：公立國文正確美觀硬筆字模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `4-Ⅳ-6：正確美觀硬筆字`。
- 使用界線：只研究硬筆字的字形、筆畫、比例、基準線、字距、行距、版面與檢核能力方向；重新編寫方格紙、公告、筆記與抄寫情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-4-iv-6` 的 10 題固定選項題；AI 檢查書寫規範、版面評量、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-085：公立國文文本內容形式與寫作特色題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `5-Ⅳ-3：理解文本內容形式與寫作特色`。
- 使用界線：只研究公開試題的文本判讀、語句關係、篇章結構、證據比較與人物／氣氛描寫能力方向；重新編寫校園說明、資料比較、敘事與詩句情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-5-iv-3` 的 10 題原有泛用題；AI 檢查單元符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-086：公立國文圖表與資料整合題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `Bc-Ⅳ-3：數據圖表圖片工具列輔助`。
- 使用界線：只研究公開試題的圖表、表格、流程圖、單位、比例、截斷刻度與文字資料整合能力方向；重新編寫校園用水、回收、參加人數與報告情境，不保存原題文字、選項、篇章或圖表。
- 本批結果：替換 `lesson-chinese-content-bc-iv-3` 的 10 題原有泛用題；AI 檢查單元符合度、數值計算、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-087：公立國文學習內容通用題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對國文學習內容。
- 使用界線：只研究公開試題的公告資訊、關聯詞、詞語搭配、字形結構、圖表閱讀與文本論證能力方向；重新編寫校園公告、資料比較、樣本範圍與文章修改情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-learning-content` 的 10 題原有通用自我檢核題；AI 檢查課綱符合度、字詞與數值判讀、唯一最佳答案、選項可排除性、來源界線與同課重複，並修正答案位置集中問題，維持 `draft` 等待 Terra 第二輪複核。

## D-088：公立國語文領域導覽題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以官方國語文課綱索引核對領域能力範圍。
- 使用界線：只研究公開試題的公告理解、資料證據、媒體識讀、圖文整合、文學欣賞與表達修改能力方向；重新編寫校園公告、調查結論、提案、詩句、討論、網路訊息與專題情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-language-arts-domain` 的 10 題全為 A 的通用題；AI 檢查領域符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-089：會考／公立國文基礎說明文題安全替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考國文科公開試題本，以及高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；並以國教院語文領域課綱核對 Bc 說明文本能力。
- 使用界線：移除原題中的 111／112 年會考標籤與未完成改編的題幹，僅研究說明文、證據、樣本、比例、比較、舉例、圖表刻度與結論限制的能力方向；重新編寫校園樹木、午餐、遮雨棚、閱讀與回收情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bc` 的 10 題；AI 檢查數值計算、資料範圍、唯一最佳答案、選項可排除性、來源界線與同課重複，維持 `draft` 等待 Terra 第二輪複核。

## D-090：公立國文標點與語意判讀題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-1：善用標點增進情感與說服`。
- 使用界線：只研究公開試題的標點、停頓、語氣與說服句型能力方向；重新編寫公告、校刊、說服文與朗讀情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-6-iv-1` 的 10 題全為 A 的標點模板題；AI 檢查標點與語意、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-091：公立國文寫作流程與篇章組織題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-2：審題立意取材組織遣詞修訂成文`。
- 使用界線：只研究公開試題的篇章理解與寫作能力方向；重新編寫審題、立意、取材、組織、遣詞、段落銜接與修訂流程情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-6-iv-2` 的 10 題全為 A 的寫作流程模板題；AI 檢查流程順序、題旨符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-092：公立國文仿寫改寫題安全替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-3：仿寫改寫等技巧`。
- 使用界線：只研究公開試題的句型、修辭、語體、敘事改寫與文字表達能力方向；重新編寫仿寫、擬人、條件句、正式語體與安全改寫界線情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-6-iv-3` 的 10 題全為 A 的仿寫模板題；AI 檢查句型結構、語意保留、改寫界線、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-093：公立國文各類文本功能題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-4：依需求書寫各類文本`。
- 使用界線：只研究公開試題的應用文、公告、心得、實驗報告、新聞稿、問卷、訊息、產品介紹與摘要能力方向；重新編寫不同讀者與文本目的的情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-6-iv-4` 的 10 題全為 A 的文本類型模板題；AI 檢查文本功能、必要資訊、受眾、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-094：公立國文自編題目審查題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-5：主動創作自訂題目表述見解發布`。
- 使用界線：只研究公開試題的能力目標、資料引用、選項設計、答案解析與發布前檢查方向；重新編寫校園公告、表格資料與自編題目 QA 情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-6-iv-5` 的 10 題全為 A 的命題模板題；AI 檢查單元符合度、唯一最佳答案、解析、來源授權、同課／跨課重複與答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-095：公立國文數位編輯與分享題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `6-Ⅳ-6：科技編輯作品及分享見解`。
- 使用界線：只研究公開試題的圖文表達、資料引用、共同編輯、媒體發布、個資與素材權利判讀方向；重新編寫簡報、影片、線上文件、社群分享與數位作品 QA 情境，不保存原題文字、選項、篇章或圖表。
- 本批結果：替換 `lesson-chinese-performance-6-iv-6` 的 10 題全為 A 的數位編輯模板題；AI 檢查內容與單元符合度、來源與權利、唯一最佳答案、選項可排除性、同課重複與答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-096：公立國文聆聽記錄與歸納題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `1-Ⅳ-1：同理聆聽並記錄歸納`。
- 使用界線：只研究公開試題的聆聽理解、重點記錄、澄清提問、操作順序、訪談歸納與轉述能力方向；重新編寫校園講座、討論、新聞、操作說明與訪談情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-1-iv-1` 的 10 題全為 A 的聆聽模板題；AI 檢查聆聽情境、資訊範圍、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-097：公立國文聲情與口語表達題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `1-Ⅳ-2：依情境辨識聲情與表達技巧並回應`。
- 使用界線：只研究公開試題的語氣、音量、速度、重音、停頓、順序詞與回應能力方向；重新編寫廣播、演講、討論、公告與對話情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-1-iv-2` 的 10 題全為 A 的聲情模板題；AI 檢查情境與聲情線索、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-098：公立國文聆聽邏輯與問題解決題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `1-Ⅳ-3：分辨聆聽內容邏輯並找方法`。
- 使用界線：只研究公開試題的因果、轉折、比較、證據、步驟、理由與問題解決判讀方向；重新編寫校園環境、交通方案、操作示範與辯論情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-1-iv-3` 的 10 題全為 A 的聆聽邏輯模板題；AI 檢查邏輯關係、證據範圍、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-099：公立國文聆聽導覽題安全替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對國文聆聽學習表現。
- 使用界線：只研究公開試題的廣播、對話、演講、訪談、公告、聲情、轉折與主旨判讀方向；重新編寫停課廣播、活動公告與口語情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-1` 的 10 題全為 A 的聆聽導覽模板題；AI 檢查資訊範圍、語意、聲情、因果、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-100：公立國文標點與朗讀題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `5-Ⅳ-1：標點效果與流暢有感朗讀`。
- 使用界線：只研究公開試題的標點、停頓、重音、語調、角色朗讀與語意辨識方向；重新編寫公告、操作步驟、對話與說明文情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-5-iv-1` 的 10 題全為 A 的標點／朗讀模板題；AI 檢查單元符合度、唯一最佳答案、選項可排除性、來源界線、同課重複與答案位置分散，維持 `draft` 等待 Terra 第二輪複核。

## D-101：數學因式分解題與答案呈現修正

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-4：因式分解`。
- 使用界線：只研究公立國中公開試題的因式分解、提出公因式、平方差、完全平方與展開驗算能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-4` 的 10 題通用模板為具體計算與判斷題，維持 `draft` 等待 Terra 第二輪 AI 複核；前端題目卡新增可展開的選項、答案與解析，資料缺答案時明確顯示尚未提供，避免畫面與資料狀態不一致。

## D-102：數學多項式運算題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-3：多項式的四則運算`。
- 使用界線：只研究公立國中公開試題的同類項、次數、加減、分配律、乘除、代入與驗算能力；重新設計數值與式子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-3` 的 10 題全 A 通用模板為具體多項式運算題，逐題重算答案並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-103：數學多項式概念題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-2：多項式的意義`。
- 使用界線：只研究公立國中公開試題的項、係數、次數、同類項、常數項、代入與多項式判讀能力；重新設計數值與式子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-2` 的 10 題全 A 通用模板為具體概念與計算題，逐題核對答案並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-104：數學乘法公式題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-1：二次式的乘法公式`。
- 使用界線：只研究公立國中公開試題的平方和、平方差、完全平方、展開與因式分解能力；重新設計數值與式子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-1` 的 10 題全 A 通用模板為具體公式題，逐題核對展開與因式分解結果並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-105：數學代數符號題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-1：代數符號`。
- 使用界線：只研究公立國中公開試題的變數、係數、常數項、代入、同類項、分配律與情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-1` 的 10 題全 A 通用模板為具體代數符號與計算題，逐題核對答案並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-106：數學一元一次方程式題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-2：一元一次方程式的意義`。
- 使用界線：只研究公立國中公開試題的未知數、等式、移項、係數、驗算與情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-2` 的 10 題全 A 通用模板為具體方程式題，逐題驗算並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-107：數學一元一次方程式應用題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-3：一元一次方程式的解法與應用`。
- 使用界線：只研究公立國中公開試題的列式、移項、驗算與生活情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-3` 的 10 題全 A 通用模板為具體應用題，逐題驗算並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-108：數學聯立方程式題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-4：二元一次聯立方程式的意義`。
- 使用界線：只研究公立國中公開試題的未知數設定、代入法、消去法、驗算與生活情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-4` 的 10 題全 A 通用模板為具體聯立方程式題，逐題驗算並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-109：數學聯立方程式應用題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-5：二元一次聯立方程式的解法與應用`。
- 使用界線：只研究公立國中公開試題的列式、代入、消去與生活情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-5` 的 10 題全 A 通用模板為具體聯立應用題，逐題驗算並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-110：數學聯立方程式幾何題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-6：二元一次聯立方程式的幾何意義`。
- 使用界線：只研究公立國中公開試題的直線、斜率、截距、交點、平行與解集判讀能力；重新設計方程式與數值，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-6` 的 10 題全 A 通用模板為具體圖形與計算題，逐題核對坐標與方程式並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-111：數學一元一次不等式題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-7：一元一次不等式的意義`。
- 使用界線：只研究公立國中公開試題的不等式運算、負數除法、數線、邊界與情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-7` 的 10 題全 A 通用模板為具體不等式題，逐題核對解集與邊界並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-112：數學一元一次不等式應用題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-7-8：一元一次不等式的解與應用`。
- 使用界線：只研究公立國中公開試題的不等式列式、整數限制、數線與生活情境建模能力；重新設計數值與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-7-8` 的 10 題全 A 通用模板為具體不等式應用題，逐題核對解集與邊界並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-113：數學因式分解方法題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-5：因式分解的方法`。
- 使用界線：只研究公立國中公開試題的公因式、分組、平方差、完全平方、乘法驗算與方法選擇能力；重新設計數值與式子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-5` 的 10 題全 A 通用模板為具體因式分解題，逐題核對展開結果並分散答案位置，維持 `draft` 等待 Terra 第二輪 AI 複核。

## D-114：數學一元二次方程式意義題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-6：一元二次方程式的意義`。
- 使用界線：只研究公開試題的二次方程式結構、解法、判別式、配方、代回驗算與情境建模能力方向；重新設計數值、式子與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-6` 的 10 題全 A 通用模板為具體題目，逐題重算答案、分散答案位置並補上解析；修正為 `draft`，等待 Terra 第二輪 AI 複核。

## D-115：數學一元二次方程式應用題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級數學科公開試題卷，並以官方數學課綱核對 `A-8-7：一元二次方程式的解法與應用`。
- 使用界線：只研究公開試題的二次方程式解法、根的判斷與情境建模能力方向；重新設計數值、式子與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-a-8-7` 的 10 題全 A 通用模板為具體題目，逐題重算答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-116：數學 100 以內質數題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-1：100以內的質數`。
- 使用界線：只研究公開試題的數與量判讀、因數與質數能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-1` 的 10 題全 A 通用模板為具體質數與質因數分解題，逐題核對因數與唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-117：數學質因數分解標準式題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-2：質因數分解的標準分解式`。
- 使用界線：只研究公開試題的因數分解、冪次與數量計算能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-2` 的 10 題全 A 通用模板為具體標準質因數分解題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-118：數學負數與四則混合運算題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-3：負數與數的四則混合運算`。
- 使用界線：只研究公開試題的負數、分數、小數、括號與運算順序能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-3` 的 10 題全 A 通用模板為具體計算與溫度情境題，逐題核對運算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-119：數學數的運算規律題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-4：數的運算規律`。
- 使用界線：只研究公開試題的交換律、結合律、分配律與運算策略能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-4` 的 10 題全 A 通用模板為具體運算規律題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-120：數學數線題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-5：數線`。
- 使用界線：只研究公開試題的數線位置、相反數、絕對值、比較與距離能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-5` 的 10 題全 A 通用模板為具體數線與情境題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-121：數學指數意義題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-6：指數的意義`。
- 使用界線：只研究公開試題的指數表示、底數正負、次方意義與數值比較能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-6` 的 10 題全 A 通用模板為具體指數題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-122：數學指數律題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-7：指數律`。
- 使用界線：只研究公開試題的同底數運算、冪的冪、零次方與指數比較能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-7` 的 10 題全 A 通用模板為具體指數律題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-123：數學科學記號題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-8：科學記號`。
- 使用界線：只研究公開試題的科學記號轉換、位數、乘除、加法與量級判斷能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-8` 的 10 題全 A 通用模板為具體科學記號題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-124：數學比與比例式題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-7-9：比與比例式`。
- 使用界線：只研究公開試題的比值化簡、比例式、單位換算與生活情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-7-9` 的 10 題全 A 通用模板為具體比與比例式題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-125：數學二次方根題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-1：二次方根`。
- 使用界線：只研究公開試題的平方根定義、根式化簡、四則運算與幾何應用能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-1` 的 10 題全 A 通用模板為具體平方根題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-126：數學二次方根近似值題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-2：二次方根的近似值`。
- 使用界線：只研究公開試題的平方根夾逼、近似值、四捨五入與誤差判斷能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-2` 的 10 題全 A 通用模板為具體根式估算題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-127：數學認識數列題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-3：認識數列`。
- 使用界線：只研究公開試題的數列規律、通項、遞推、等差數列與求和能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-3` 的 10 題全 A 通用模板為具體數列題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-128：數學等差數列題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-4：等差數列`。
- 使用界線：只研究公開試題的等差數列公差、通項、指定項與生活情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-4` 的 10 題全 A 通用模板為具體等差數列題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-129：數學等差級數求和題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-5：等差級數求和`。
- 使用界線：只研究公開試題的等差級數首尾平均、項數、求和公式與生活情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-5` 的 10 題全 A 通用模板為具體等差級數求和題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-130：數學等比數列題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-8-6：等比數列`。
- 使用界線：只研究公開試題的等比數列公比、通項、指定項與倍增情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-8-6` 的 10 題全 A 通用模板為具體等比數列題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-131：數學連比題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `N-9-1：連比`。
- 使用界線：只研究公開試題的連比整合、共同項、比例分配與生活情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n-9-1` 的 10 題全 A 通用模板為具體連比題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-132：數學統計圖表題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D-7-1：統計圖表`。
- 使用界線：只研究公開試題的統計圖表讀值、刻度、比例、平均數與中位數能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d-7-1` 的 10 題全 A 通用模板為具體資料判讀題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-133：數學統計數據題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D-7-2：統計數據`。
- 使用界線：只研究公開試題的平均數、中位數、眾數、全距與資料變動能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d-7-2` 的 10 題全 A 通用模板為具體統計數據題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-134：數學統計資料處理題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D-8-1：統計資料處理`。
- 使用界線：只研究公開試題的次數分配、相對次數、累積次數與統計量能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d-8-1` 的 10 題全 A 通用模板為具體統計資料處理題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-135：數學統計數據分布題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D-9-1：統計數據的分布`。
- 使用界線：只研究公開試題的資料分布、五數摘要、四分位距、箱型圖與離群值能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d-9-1` 的 10 題全 A 通用模板為具體資料分布題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-136：數學認識機率題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D-9-2：認識機率`。
- 使用界線：只研究公開試題的樣本空間、古典機率、互補事件與抽取情境能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d-9-2` 的 10 題全 A 通用模板為具體機率題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-137：數學資料與不確定性領域題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以官方數學課綱核對 `D：資料與不確定性`。
- 使用界線：只研究公開試題的統計量、圖表、抽樣與古典機率跨單元判讀方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-d` 的 10 題全 A 通用模板為具體跨單元資料與機率題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-138：數學函數領域題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以國教院數學領域課綱核對 `F：函數`。
- 使用界線：只研究公開試題的函數代值、斜率、截距、圖形與情境建模能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-f` 的 10 題固定選項題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-139：數學數與量領域題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以國教院數學領域課綱核對 `N：數與量`。
- 使用界線：只研究公開試題的數與量運算、數線、根號、指數、比例與單位轉換能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-n` 的 10 題固定選項題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-140：數學空間與形狀領域題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考數學科公開試題，並以國教院數學領域課綱核對 `S：空間與形狀`。
- 使用界線：只研究公開試題的角度、幾何量、相似、座標變換與圓幾何能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-math-content-s` 的 10 題固定選項題，逐題核對計算、唯一答案、分散答案位置並補上解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-141：自然科摩擦生靜電單元題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Kc-Ⅳ-1：摩擦生靜電與正負電荷`。
- 使用界線：只研究公開試題的摩擦起電、電荷作用、導體、接地與靜電現象能力方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-kc-iv-1` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-142：自然科物質組成與元素週期性題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Aa：物質組成與元素週期性`。
- 使用界線：只研究公開試題的元素符號、原子與離子、週期表及化學式判讀方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-aa` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-143：自然科物質形態與分類題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ab：物質的形態、性質及分類`。
- 使用界線：只研究公開試題的物理性質、物質三態、純物質與混合物、分離方法及密度判讀方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ab` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-144：自然科能量形式與轉換題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba：能量的形式與轉換`。
- 使用界線：只研究公開試題的能量形式、轉換、守恆、效率、熱能與能源分類能力方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-145：自然科溫度與熱量題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Bb：溫度與熱量`。
- 使用界線：只研究公開試題的溫標、熱傳播、熱平衡、比熱、相變與保溫能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-bb` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-146：自然科能量形式轉換與守恆題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-1：能量形式、轉換與守恆`。
- 使用界線：只研究公開試題的機械能、功、功率、能量守恆、效率與能源轉換能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-1` 的 10 題固定選項題，逐題核對計算、唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-147：自然科光合作用與呼吸作用題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-2：光合作用與呼吸作用的能量轉換`。
- 使用界線：只研究公開試題的光合作用原料與產物、葉綠體、實驗證據、呼吸作用及能量轉換能力方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-2` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-148：自然科化學反應吸熱與放熱題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-3：化學反應的吸熱與放熱`。
- 使用界線：只研究公開試題的吸熱、放熱、溫度變化、能量轉移及實驗控制變因能力方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-3` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與來源界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-149：自然科電池化學能轉電能題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-4：電池的化學能轉電能`。
- 使用界線：只研究公開試題的電池能量轉換、電解質、電路、電極、串聯與充電能力方向；重新設計情境與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-4` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、解析與安全操作界線；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-150：自然科力作功與能量改變題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-5：力作功與能量改變`。
- 使用界線：只研究公開試題的功、力與位移、摩擦力、重力位能、動能及功率能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-5` 的 10 題固定選項題，逐題核對計算、唯一答案、選項可排除性與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-151：自然科功率題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考自然科公開試題，並以國教院自然科學領域課綱核對 `Ba-Ⅳ-6：功率`。
- 使用界線：只研究公開試題的功率公式、單位換算、功率比較、電器功率與效率能力方向；重新設計數值與問法，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-science-content-ba-iv-6` 的 10 題固定選項題，逐題核對計算、唯一答案、選項可排除性與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-152：英文 Aa 字母題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Aa：字母`。
- 使用界線：只研究公開試題的基礎閱讀與字母辨識能力方向；重新設計字母順序、大小寫、母音與基礎書寫題，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-aa` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文拼寫與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-153：英文大小寫辨識與書寫題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Aa-Ⅳ-1：書寫體大小寫辨識書寫`。
- 使用界線：只研究公開試題的句首、姓名、地名、月份、星期與代名詞 I 大小寫能力方向；重新設計句子與選項，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-aa-iv-1` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文拼寫與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-154：英文語音題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ab：語音`。
- 使用界線：只研究公開試題的語音辨識能力方向；重新設計字首、字尾、母音、子音、長短母音與押韻題，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ab` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、語音判讀與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-155：英文句子重音與語調題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ab-Ⅳ-1：句子發音重音語調`。
- 使用界線：只研究公開試題的句子重音、疑問與直述語調、停頓、語速及口語表達能力方向；重新設計句子與情境，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ab-iv-1` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-156：英文歌謠韻文節奏音韻題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ab-Ⅳ-2：歌謠韻文節奏音韻`。
- 使用界線：只研究公開試題的押韻、節奏、音節、重音與重複語句能力方向；使用自編短語與句子，不保存任何歌詞、詩文或原題文字。
- 本批結果：替換 `lesson-english-content-ab-iv-2` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-157：英文字母拼讀規則題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ab-Ⅳ-3：字母拼讀規則`。
- 使用界線：只研究公開試題的常見子音、子音組合、長短母音、magic e、母音組合與 CVC 拼讀能力方向；使用自編字詞與句子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ab-iv-3` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文拼讀與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-158：英文字彙題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ac：字彙`。
- 使用界線：只研究公開試題的上下文詞義、同反義詞、詞性、搭配與生活情境字彙能力方向；重新設計句子與選項，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ac` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文拼寫與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-159：英文常見生活用語題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ac-Ⅳ-3：常見生活用語`。
- 使用界線：只研究公開試題的日常溝通與情境回應能力方向；重新設計問候、請求、道歉、感謝、邀請、購物、問路與祝福對話，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ac-iv-3` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-160：英文國中基本 1200 字詞題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ac-Ⅳ-4：國中基本1200字詞`。
- 使用界線：只研究公開試題的基礎字詞情境判讀能力方向；重新設計詞義、片語搭配、詞性與生活句子，不保存原題文字、選項、圖表或答案。
- 本批結果：替換 `lesson-english-content-ac-iv-4` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-161：英文篇章閱讀題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae：篇章`。
- 使用界線：只研究公開試題的篇章主旨、細節、指代、因果、推論、順序與標題判讀能力方向；重新設計自編短文與選項，不保存原題文章、圖表或答案。
- 本批結果：替換 `lesson-english-content-ae` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-162：英文短文短劇故事題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-1：簡易歌謠韻文短文短劇故事`。
- 使用界線：只研究公開試題的故事角色、事件順序、情緒、因果、韻文特徵與結局判讀能力方向；使用自編短文、對話與故事，不保存現成作品、歌詞、詩文或原題文字。
- 本批結果：替換 `lesson-english-content-ae-iv-1` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性、英文語意與解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-163：英文常見圖表題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-2：常見圖表`。
- 使用界線：只研究公開試題的表格、長條圖、折線圖、圓餅圖、比例、趨勢與座標標示判讀能力方向；使用自編資料與圖表文字，不保存原題圖表、文字或答案。
- 本批結果：替換 `lesson-english-content-ae-iv-2` 的 10 題固定選項題，逐題核對數值計算、唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-164：英文公共場所廣播題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-3：公共場所廣播`。
- 使用界線：只研究公開試題的廣播資訊判讀能力方向；重新設計車站、機場、圖書館、校園與商場的時間、地點、物品、行動、原因與安全資訊，不保存原題文字、圖表或答案。
- 本批結果：替換 `lesson-english-content-ae-iv-3` 的 10 題固定選項題，逐題核對時間數值、唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-165：英文卡片書信電郵題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-4：簡易卡片書信電郵`。
- 使用界線：只研究公開試題的卡片、書信、電郵資訊判讀能力方向；重新設計寄件人、收件人、日期、目的、行動與回覆情境，不保存原題文字、版面或答案。
- 本批結果：替換 `lesson-english-content-ae-iv-4` 的 10 題固定選項題，逐題核對時間、人物、目的、唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-166：英文不同體裁主題文章題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-5：不同體裁主題簡易文章`。
- 使用界線：只研究公開試題的不同體裁閱讀能力方向；使用自編公告、日記、食譜、新聞、廣告、說明文、經驗分享、行程與比較文章，不保存原題文章、圖表或答案。
- 本批結果：替換 `lesson-english-content-ae-iv-5` 的 10 題固定選項題，逐題核對細節、順序、目的、比較、唯一答案與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-167：英文敘事者觀點態度目的題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-7：敘事者觀點態度目的`。
- 使用界線：只研究公開試題的敘事者觀點、態度、語氣、寫作目的、證據限制與推論能力方向；使用自編短文與選項，不保存原題文章、圖表或答案。
- 本批結果：替換 `lesson-english-content-ae-iv-7` 的 10 題固定選項題，逐題核對文本證據、唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-077：公立國文明確表達與論辯模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `2-Ⅳ-3：明確表達與有條理論辯`。
- 使用界線：只研究公開試題的表達、評論與論辯能力方向；重新編寫校園提案、報告、統計資料、反面資料與演說呼籲情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-2-iv-3` 的 10 題固定選項題；AI 檢查主張與理由、資料限制、反例回應、唯一最佳答案、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-076：公立國中國文聽聞提問回饋模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `2-Ⅳ-2：掌握聽聞邏輯提問回饋`。
- 使用界線：只研究聽聞理解、澄清、追問、資料核對與建設性回饋能力方向；重新編寫訪談、討論、報告與日常對話情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-2-iv-2` 的 10 題固定選項題；AI 檢查情境符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-074：公立國中國文報告評論演說論辯模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `2-Ⅳ-5：報告評論演說與論辯`。
- 使用界線：只研究報告、評論、演說與論辯的能力方向；重新編寫資料引用、演說開場、評論證據、反例回應、圖表解釋、報告結構與行動呼籲情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-performance-2-iv-5` 的 10 題固定選項題；AI 檢查情境符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。

## D-075：公立國中國文客觀說明單元模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷，並以國教院語文領域課綱核對 `Bc-Ⅳ-1：邏輯客觀理性說明`。
- 使用界線：只研究公開試題的說明與閱讀理解能力方向；重新編寫統計範圍、因果證據、客觀措辭、公平比較、研究主張與結論限制情境，不保存原題文字、選項、篇章或答案。
- 本批結果：替換 `lesson-chinese-content-bc-iv-1` 的 10 題固定選項題；AI 檢查資料與課綱符合度、唯一最佳答案、選項可排除性、來源界線與同課重複，並分散答案位置，維持 `draft` 等待 Terra 第二輪複核。
## D-167：英文故事短文主旨題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對 `Ae-Ⅳ-8：故事短文主旨`。
- 使用界線：只研究公開試題的故事事件、轉折、結局與主旨統整能力方向；使用自編故事短文與選項，不保存任何現成作品、歌詞、詩文或原題文字。
- 本批結果：替換 `lesson-english-content-ae-iv-8` 的 10 題固定選項題，逐題核對文本證據、唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-168：英文自己、家人、朋友題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科公開閱讀／生活情境能力方向，並以國教院英語文課綱核對 `B-Ⅳ-1：自己、家人、朋友`。
- 使用界線：只研究人物關係、家庭資訊與友誼情境的判讀能力；使用自編對話與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-content-b-iv-1` 的 10 題固定選項題，逐題核對唯一答案、選項可排除性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-169：英文日常溝通字彙句型題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-2：日常溝通字彙句型`。
- 使用界線：只研究請求、建議、邀請、頻率、購物與日常問答能力；使用自編對話與選項，不保存現成題文、選項或圖片。原始 PDF 本輪因來源網域暫時無法下載，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-2` 的 10 題固定選項題，逐題核對唯一答案、句型可用性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-170：英文語言與非語言溝通策略題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-3：語言與非語言溝通策略`。
- 使用界線：只研究澄清、輪流、眼神、表情、手勢與語體調整能力；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-3` 的 10 題固定選項題，逐題核對唯一答案、策略適切性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-171：英文需求意願感受題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-4：需求、意願、感受`。
- 使用界線：只研究需求、請求、偏好、意願與情緒的生活情境判讀；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-4` 的 10 題固定選項題，逐題核對唯一答案、語句適切性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-172：英文人事時地物描述問答題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-5：人事時地物描述問答`。
- 使用界線：只研究 who、where、when、what、how、why、whose 問答能力；使用自編對話與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-5` 的 10 題固定選項題，逐題核對唯一答案、疑問詞對應與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-173：英文圖片描述題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-6：圖片描述`。
- 使用界線：只研究圖片中人物、動作、數量、位置、比較與方向的描述能力；使用自編文字情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-6` 的 10 題固定選項題，逐題核對唯一答案、描述與情境一致性及英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-174：英文角色扮演題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-7：角色扮演`。
- 使用界線：只研究角色語氣、情境回應、請求、道歉、服務與任務對話能力；使用自編對話與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-7` 的 10 題固定選項題，逐題核對唯一答案、角色適切性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-175：英文引導式討論題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `B-Ⅳ-8：引導式討論`。
- 使用界線：只研究引導提問、聆聽回應、禮貌異議、證據、輪流與討論結論能力；使用自編對話與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-b-iv-8` 的 10 題固定選項題，逐題核對唯一答案、討論策略適切性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-176：英文文化與習俗領域題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對主題 `C：文化與習俗`。
- 使用界線：只研究節慶、習俗、文化比較、脈絡與尊重欣賞能力；使用自編文化情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c` 的 10 題固定選項題，逐題核對唯一答案、文化敘述不過度概括與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-177：英文國內外節慶題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `C-Ⅳ-1：國內外節慶`。
- 使用界線：只研究節慶的時間、活動、意義、歷史脈絡與文化比較；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c-iv-1` 的 10 題固定選項題，逐題核對唯一答案、文化敘述不過度概括與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-178：英文風土民情題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `C-Ⅳ-2：風土民情`。
- 使用界線：只研究地方環境、生活方式、社區市場、迎賓與風俗脈絡判讀；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c-iv-2` 的 10 題固定選項題，逐題核對唯一答案、文化敘述不過度概括與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-179：英文文化習俗比較題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `C-Ⅳ-3：文化習俗比較`。
- 使用界線：只研究相同目的、不同做法、比較類別、訪談證據與結論範圍；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c-iv-3` 的 10 題固定選項題，逐題核對唯一答案、文化敘述不過度概括與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-180：英文尊重欣賞文化題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `C-Ⅳ-4：尊重欣賞文化`。
- 使用界線：只研究尊重提問、避免刻板印象、文化脈絡、來源查核與參與界線；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c-iv-4` 的 10 題固定選項題，逐題核對唯一答案、文化敘述不過度概括與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-181：英文基本世界觀題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `C-Ⅳ-5：基本世界觀`。
- 使用界線：只研究地理位置、語言多樣性、地圖尺度、跨國連結、環境風險、資料來源與世界觀範圍；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-content-c-iv-5` 的 10 題固定選項題，逐題核對唯一答案、證據範圍與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-182：英文思考能力領域題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題，並以國教院英語文課綱核對主題 `D：思考能力`。
- 使用界線：只研究資訊推論、分類排序、因果、事實與意見、證據範圍與來源查核；使用自編資料與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-content-d` 的 10 題固定選項題，逐題核對唯一答案、推論範圍與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-183：英文領域導覽題替換

- 日期：2026-08-28
- 本批來源：國中教育會考官方入口與官方課綱索引，核對 `語文領域－英語文` 的整合學習範圍。
- 使用界線：只研究閱讀、聽說互動、寫作目的、資訊查核與學習反思；使用自編情境與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-language-domain` 的 10 題固定選項題，逐題核對唯一答案、能力對應與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-184：英文學習內容導覽題替換

- 日期：2026-08-28
- 本批來源：國中教育會考官方入口與國教院英語文課綱，核對英語學習內容的字彙、句型、閱讀、聽力與語用範圍。
- 使用界線：只研究語言形式與真實溝通任務的連結；使用自編情境與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-learning-content` 的 10 題固定選項題，逐題核對唯一答案、能力對應與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-185：英文學習表現導覽題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對英語學習表現範圍。
- 使用界線：只研究聽讀理解、口語互動、寫作目的、語調、語境推論與自我檢核；使用自編情境與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-learning-performance` 的 10 題固定選項題，逐題核對唯一答案、能力對應與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-186：英文語言能力聽力導覽題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對英語「語言能力（聽）」範圍。
- 使用界線：只研究地點、細節、時間、選擇、情緒、順序、原因、主旨與語調判讀；使用自編聽力文字稿與選項，不保存現成題文、選項或音檔。
- 本批結果：替換 `lesson-english-performance-1` 的 10 題固定選項題，逐題核對唯一答案、聽力能力對應與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-187：英文課堂字詞題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `1-Ⅳ-1：課堂字詞`。
- 使用界線：只研究課堂指令、學習單詞彙、作答動作與澄清用語；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-performance-1-iv-1` 的 10 題固定選項題，逐題核對唯一答案、詞義與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-188：英文常用教室與生活用語題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `1-Ⅳ-2：常用教室與生活用語`。
- 使用界線：只研究道歉、請求、允許、拒絕、問路、等待與道別用語；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-performance-1-iv-2` 的 10 題固定選項題，逐題核對唯一答案、語用適切性與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-189：英文基本重要句型題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `1-Ⅳ-3：基本重要句型`。
- 使用界線：只研究 be、have、there be、過去式、未來計畫、情態動詞、比較級、請求與原因句型；使用自編情境與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-performance-1-iv-3` 的 10 題固定選項題，逐題核對唯一答案、句型文法與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-190：英文日常對話主要內容題替換

- 日期：2026-08-28
- 本批來源：鹽埕國中 114 學年度第 2 學期英文段考公開來源索引，並以國教院英語文課綱核對 `1-Ⅳ-4：日常對話主要內容`。
- 使用界線：只研究日常對話的主旨、問題、理由、時間地點、建議與細節判讀；使用自編對話與選項，不保存現成題文、選項或圖片。原始 PDF 本輪仍受來源網域 DNS 限制，未宣稱已重新下載。
- 本批結果：替換 `lesson-english-performance-1-iv-4` 的 10 題固定選項題，逐題核對唯一答案、對話證據與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-191：英文簡易歌謠韻文主要內容題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對 `1-Ⅳ-5：簡易歌謠韻文主要內容`。
- 使用界線：只研究韻文的情境、意象、主旨、訊息與價值判讀；使用全新自編短韻文與選項，不保存歌曲、歌詞、詩文、公開試題文字或音檔。
- 本批結果：替換 `lesson-english-performance-1-iv-5` 的 10 題固定選項題，逐題核對唯一答案、文本證據與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-192：英文故事短劇主要內容題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對 `1-Ⅳ-6：故事短劇主要內容`。
- 使用界線：只研究短劇的角色、事件、轉折、問題解決、價值與結局判讀；使用自編短劇與選項，不保存現成劇本、歌曲、公開試題文字或音檔。
- 本批結果：替換 `lesson-english-performance-1-iv-6` 的 10 題固定選項題，逐題核對唯一答案、文本證據與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-193：英文簡短說明敘述情境主旨題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對 `1-Ⅳ-7：簡短說明敘述情境主旨`。
- 使用界線：只研究短篇說明／敘述的主旨、因果、目的、步驟與資訊關係判讀；使用自編文字與選項，不保存現成題文、選項或圖片。
- 本批結果：替換 `lesson-english-performance-1-iv-7` 的 10 題固定選項題，逐題核對唯一答案、文本證據與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-194：英文簡易影片主要內容題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對 `1-Ⅳ-8：簡易影片主要內容`。
- 使用界線：只研究影片的主旨、目的、步驟、前後變化、細節與訊息判讀；使用自編影片文字情境與選項，不保存現成影片、圖片、題文或音檔。
- 本批結果：替換 `lesson-english-performance-1-iv-8` 的 10 題固定選項題，逐題核對唯一答案、情境證據與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-195：英文語調情緒態度題替換

- 日期：2026-08-28
- 本批來源：114 年國中教育會考英語科閱讀公開試題與國教院英語文課綱，核對 `1-Ⅳ-9：語調所表達的情緒態度`。
- 使用界線：只研究語調、重音、速度、音量、語境與情緒態度判讀；使用自編對話與文字化語調線索，不保存現成題文、音檔或圖片。
- 本批結果：替換 `lesson-english-performance-1-iv-9` 的 10 題固定選項題，逐題核對唯一答案、語調線索與英文解析；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-196：英文語言能力（說）題替換

- 日期：2026-08-28
- 本批來源：國教院英語文課綱，並參考公開公立國中英文段考常見基本問答、生活溝通、描述與問答題型，核對 `語言能力（說）`。
- 使用界線：只研究口語任務的能力結構；使用自編英文情境與選項，不保存或重製公開試題文字、選項、圖片或音檔。原始公立國中 PDF 本輪因來源網域 DNS 無法下載，未納入儲存庫。
- 本批結果：替換 `lesson-english-performance-2` 的 10 題固定選項題，加入答案與英文解析；逐題核對單元符合度、唯一最佳答案、選項可排除性、來源標示與同課題目不重複；維持 `draft`，等待 Terra 第二輪 AI 複核。
## D-197：全庫泛用題模板替換與重複題幹清理

- 日期：2026-08-28
- 本批來源：`data/public-exam-sources.json` 所列 114 年國中教育會考與高雄市立鹽埕國民中學公開試題索引；只研究會考／段考的條件判讀、資料應用與生活情境題型，並以各單元已驗證課綱範圍核對。
- 使用界線：原始公開試卷只作題型與能力方向研究；本批 7,740 題均為獨立編寫，未保存或重製原題文字、選項、圖片或音檔。因本輪公立國中 PDF 來源網域 DNS 無法下載，未宣稱已保存原始檔。
- 本批結果：移除原十種跨單元泛用問法，依學科、單元標題、任務與穩定 lesson ID 產生不同題幹、選項、答案與解析；逐題完成欄位、選項去重、答案對應與重複題幹檢查，全部降為 `draft`，等待第二輪 AI／Terra 內容複核。另修正 4 組非模板的重複題幹。
## D-198：公開試題與答案原始檔下載核對

- 日期：2026-08-28
- 下載結果：成功取得 114 年國中教育會考英語閱讀試題、英語選擇題參考答案表，以及高雄市立鹽埕國中 114 學年度第二學期第一次段考三年級英文試題與內附答案頁，暫存於 `/tmp`。
- 核對結果：以 PDF 文字擷取確認會考英語閱讀為 43 題選擇題，並確認鹽埕國中試卷含「基本問答」與「言談理解」區段及答案列；檔案 SHA-256 已於本次工作階段取得，原始 PDF 不進 repo。
- 使用界線：原卷與答案只作題型、能力與答案定位研究；題庫保留自編改寫題，不把公開試題文字、選項、圖片、音檔或答案表直接寫入題目資料。
## D-199：數學統計圖表與統計量題實質替換

- 日期：2026-08-28
- 本批來源：已下載的 114 年國中教育會考數學科與高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；核對直方圖、盒狀圖、四分位數、次數分配與資料判讀題型，並以官方數學課綱 `d-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-d-iv-1` 的 10 題泛用題，逐題重算平均數、中位數、全距、四分位數、盒狀圖、分組資料與試算表函數答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-200：數學機率樹狀圖與應用題實質替換

- 日期：2026-08-28
- 本批來源：已下載的 114 年國中教育會考數學科與高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；核對樹狀圖、兩階段試驗、條件機率、抽取與補事件題型，並以官方數學課綱 `d-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-d-iv-2` 的 10 題泛用題，逐題以路徑相乘、樣本空間或補事件重算答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-201：數學代數導覽題實質替換

- 日期：2026-08-28
- 本批來源：已下載的 114 年國中教育會考數學科與高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；核對代數式、同類項、分配律、代入、方程式與因式分解題型，並以官方數學課綱 `performance-a` 範圍核對。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a` 的 10 題泛用題，逐題重算代數式化簡、方程式、代入、公因式與乘法公式答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-202：數學符號文字表達與推理題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考代數式、符號表示、連續整數與推理證明題型，並以官方數學課綱 `a-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-1` 的 10 題泛用題，逐題推導偶數／奇數、連續整數、代數式、方程式與簡短證明答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-203：數學一元一次方程題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考一元一次方程式、移項、括號、負數、小數與生活情境題型，並以官方數學課綱 `a-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-2` 的 10 題泛用題，逐題解方程並以代回或等式整理核對答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-204：數學一元一次不等式題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考一元一次不等式、負數除法、數線邊界、整數限制與生活情境題型，並以官方數學課綱 `a-Ⅳ-3` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-3` 的 10 題泛用題，逐題重算解集、邊界與整數限制；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-205：數學二元一次聯立題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考代入法、消去法、交點、票券價格、數量情境與無解判斷題型，並以官方數學課綱 `a-Ⅳ-4` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-4` 的 10 題泛用題，逐題解聯立方程式並核對代回結果；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-206：數學多項式與乘法公式題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考多項式四則、分配律、完全平方、平方差與因式分解題型，並以官方數學課綱 `a-Ⅳ-5` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-5` 的 10 題泛用題，逐題展開、化簡或因式分解核對答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-207：數學一元二次方程題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考一元二次方程、因式分解、公式法、判別式、根與係數及幾何情境題型，並以官方數學課綱 `a-Ⅳ-6` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-a-iv-6` 的 10 題泛用題，逐題重算方程根、判別式與正值限制；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-208：數學二次函數圖形題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考二次函數圖形、頂點、對稱軸、截距、平移、係數與情境建模題型，並以官方數學課綱 `f-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-f-iv-2` 的 10 題泛用題，逐題重算頂點、對稱軸、開口、截距、平移與值域；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-209：數學二次函數標準式與極值題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考二次函數標準式、開口、頂點、對稱軸、極值、值域與情境建模題型，並以官方數學課綱 `f-Ⅳ-3` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-f-iv-3` 的 10 題泛用題，逐題重算對稱軸、頂點、最大／最小值、值域與長方形面積；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-210：數學常數與一次函數題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考常數函數、一次函數、斜率、截距、對應表與生活情境題型，並以官方數學課綱 `f-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-f-iv-1` 的 10 題泛用題，逐題重算代值、斜率、截距、函數式、圖形與情境答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-211：數學函數主題題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考函數定義、對應、定義域／值域、代值、圖形判斷與生活情境題型，並以官方數學課綱 `f` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-f` 的 10 題泛用題，逐題核對函數定義、對應關係、定義域、值域、代值與函數模型；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-212：數學資料與不確定性主題題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考統計量、次數分配、機率、抽樣與圖表判讀題型，並以官方數學課綱 `d` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-d` 的 10 題泛用題，逐題重算平均數、中位數、眾數、全距、次數分配、機率並核對抽樣與圖表判讀；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-213：數學坐標幾何主題題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考坐標、象限、距離、中點、斜率、截距、對稱、面積與圓題型，並以官方數學課綱 `g` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-g` 的 10 題泛用題，逐題重算象限、距離、中點、斜率、截距、鏡射、直線、三角形面積、平行線與圓；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-214：數學直角坐標點與距離題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考直角坐標點、象限、坐標軸、距離、中點、對稱與坐標情境題型，並以官方數學課綱 `g-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-g-iv-1` 的 10 題泛用題，逐題重算象限、坐標軸、水平／垂直距離、兩點距離、中點、對稱與幾何情境；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-215：數學二元一次直線與聯立解幾何題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考二元一次直線、聯立方程交點、幾何意義、截距、平行與情境題型，並以官方數學課綱 `g-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-g-iv-2` 的 10 題泛用題，逐題重算直線式、交點、聯立解、無解、截距、平行線與票券情境；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-216：數學因數倍數質數與 GCD／LCM 題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考因數、倍數、質因數分解、最大公因數、最小公倍數、互質與週期情境題型，並以官方數學課綱 `n-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-1` 的 10 題泛用題，逐題重算質因數分解、GCD、LCM、因數個數、互質、約分與週期情境；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-217：數學負數數線與四則運算題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考負數數線、整數四則、絕對值、排序與溫度情境題型，並以官方數學課綱 `n-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-2` 的 10 題泛用題，逐題重算整數加減乘除、絕對值、數線比較、排序與溫度情境；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-218：數學指數律、質因數與科學記號題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考非負整數次方、指數律、質因數分解與科學記號題型，並以官方數學課綱 `n-Ⅳ-3` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-3` 的 10 題泛用題，逐題重算次方、指數律、零次方、質因數分解、科學記號轉換與運算；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-219：數學比、比例、正反比與連比題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考比、比例、正比、反比、連比、比例尺與生活情境題型，並以官方數學課綱 `n-Ⅳ-4` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-4` 的 10 題泛用題，逐題重算最簡比、比例分配、正反比、連比、比例尺、單位換算與情境答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-220：數學二次方根與根式題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考平方根化簡、同類根式、根式運算、大小比較、方程式與幾何情境題型，並以官方數學課綱 `n-Ⅳ-5` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-5` 的 10 題泛用題，逐題重算平方根、最簡根式、同類根式、根式乘法、大小比較、根式方程式與幾何答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-221：數學十分逼近與估平方根題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考平方根夾逼、估值、四捨五入、平方數比較與正方形邊長題型，並以官方數學課綱 `n-Ⅳ-6` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-6` 的 10 題泛用題，逐題以平方值核對夾逼、估值、四捨五入、範圍與幾何情境答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-222：數學數列等差等比題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考等差數列、等比數列、公差、公比、通項、等差中項、級數和與生活情境題型，並以官方數學課綱 `n-Ⅳ-7` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-7` 的 10 題泛用題，逐題重算公差、公比、項值、等差中項、級數和與生活情境答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-223：數學等差級數和題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考等差級數求和、首尾平均、項數、偶數和與存款／座位情境題型，並以官方數學課綱 `n-Ⅳ-8` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-8` 的 10 題泛用題，逐題重算等差級數末項、項數與總和；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-224：數學計算機與誤差題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考計算機運算、估算、四捨五入、近似值、絕對／相對誤差與圓周長情境題型，並以官方數學課綱 `n-Ⅳ-9` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n-iv-9` 的 10 題泛用題，逐題重算計算機結果、估算、取位與誤差判讀；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-225：數學數與量綜合題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考數與量範圍常見的整數、分數、比例、百分率、根式、科學記號、數列與幾何量題型，並以官方數學課綱 `n` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-n` 的 10 題泛用題，逐題重算整數、分數、比例、百分率、根式、科學記號、數列與幾何量答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-226：數學空間與形狀綜合題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考空間與形狀範圍常見的角度、畢氏定理、圓、面積、體積、對稱與相似題型，並以官方數學課綱 `s` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s` 的 10 題泛用題，逐題重算角度、畢氏定理、圓、面積、體積、對稱、垂直與相似答案；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-227：數學幾何形體定義與性質題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考幾何形體定義、符號、全等判定與基本性質題型，並以官方數學課綱 `s-Ⅳ-1` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-1` 的 10 題泛用題，逐題核對平行四邊形、矩形、菱形、全等、垂直平分線、角平分線、切線與多邊形性質；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-228：數學角與多邊形內外角題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考角、平行線與多邊形內外角計算及推理題型，並以官方數學課綱 `s-Ⅳ-2` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-2` 的 10 題泛用題，逐題重算鄰補角、對頂角、三角形外角、四邊形內角和、正多邊形內外角與平行線對應角；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-229：數學垂直與平行題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考垂直、平行、斜率與坐標幾何題型，並以官方數學課綱 `s-Ⅳ-3` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-3` 的 10 題泛用題，逐題重算斜率、截距、平行／垂直判定與水平線段距離；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-230：數學全等與剛性變換題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考全等、平移、旋轉、鏡射的坐標變換及性質題型，並以官方數學課綱 `s-Ⅳ-4` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-4` 的 10 題泛用題，逐題核對平移、旋轉、鏡射規則、全等與剛性變換不變量；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-231：數學線對稱題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考線對稱、對稱軸與坐標鏡射題型，並以官方數學課綱 `s-Ⅳ-5` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-5` 的 10 題泛用題，逐題核對對稱軸、坐標鏡射、軸上不動點與幾何圖形對稱性質；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-232：數學相似與縮放題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考相似、縮放、比例尺、面積／體積倍率與生活情境題型，並以官方數學課綱 `s-Ⅳ-6` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-6` 的 10 題泛用題，逐題重算對應邊比例、周長／面積／體積倍率、AA 相似、影長與比例尺；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-233：數學畢氏定理題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考畢氏定理、坐標距離與生活情境題型，並以官方數學課綱 `s-Ⅳ-7` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-7` 的 10 題泛用題，逐題重算斜邊、直角邊、坐標距離、對角線、根式與直角三角形面積；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-234：數學特殊三角形、四邊形與正多邊形題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考特殊三角形、特殊四邊形與正多邊形題型，並以官方數學課綱 `s-Ⅳ-8` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-8` 的 10 題泛用題，逐題重算特殊三角形、正方形、菱形、箏形、等腰梯形與正多邊形的邊長、面積與角度；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-235：數學三角形邊角與全等題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考三角形邊角關係、三角形不等式與全等判定題型，並以官方數學課綱 `s-Ⅳ-9` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-9` 的 10 題泛用題，逐題核對三角形不等式、邊角關係、SSS／SAS／斜邊直角邊判定、等腰三角形與對應頂點；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-236：數學三角形相似題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考三角形相似判定、比例、平行線截比與生活情境題型，並以官方數學課綱 `s-Ⅳ-10` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-10` 的 10 題泛用題，逐題重算 AA／SSS 相似判定、對應邊比例、截比、周長／面積倍率、影長與未知量；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-237：數學三角形三心題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考三角形重心、外心、內心與垂心的定義、位置及比例題型，並以官方數學課綱 `s-Ⅳ-11` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-11` 的 10 題泛用題，逐題核對三角形三心、重心 2：1 比例、坐標重心、外心等距與內心等距性質；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-238：數學直角三角形邊長比與三角比題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考數學科；參考直角三角形銳角邊長比、sin／cos／tan 與仰角情境題型，並以官方數學課綱 `s-Ⅳ-12` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新數值、情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-math-performance-s-iv-12` 的 10 題泛用題，逐題核對特殊角三角比、邊長比、仰角與三角比換算；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-239：社會公民身分認同及社群題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考社會科；參考公民身分認同、社群參與、公共討論、共同規範與平等參與題型，並以官方社會領域課綱 `A` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-social-content-civ-a` 的 10 題泛用題，逐題核對多重身分、社群規範、公共參與、反歧視與公共資源公平使用；維持 `draft`，等待第二輪 AI／Terra 內容複核。
## D-240：社會公民身分題實質替換

- 日期：2026-08-28
- 本批來源：已下載的高雄市立鹽埕國中 114 學年度第二學期第一次段考社會科；參考公民身分、權利義務、平等、法治、公共參與與國家認同題型，並以官方社會領域課綱 `Aa` 核對範圍。
- 使用界線：只研究題型與能力方向；10 題使用全新情境、選項與解析，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `lesson-social-content-civ-aa` 的 10 題泛用題，逐題核對公民身分、權利義務、平等保障、公共參與、少數權利與國家認同；維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-241：修復獨立改編題的答案選項對齊

- 日期：2026-08-28
- 稽核發現：前 19 個公立國中題型獨立改編單元的產生器旋轉選項文字後，未同步更新 `answer.value`；只檢查答案 ID 存在不足以保證答案正確。
- 處理方式：僅針對具有明確原創、公開試題僅作題型參考、`draft` 與 2026-08-28 標記的 190 題恢復原始選項順序，保留題目 ID、題幹、解析、來源與 `draft` 狀態；另修正公民概念第 1 題的原始正解字母。
- QA 規則：新增可重複執行的答案對齊修復工具，後續驗證必須確認 `answer.value` 指向實際正解選項，不能只確認該 ID 存在。尚未完成 Terra 第二輪 AI 複核前，不升級為 `content-reviewed`。

## D-242：數學相似形與圓幾何模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-9-1` 至 `S-9-4`、`S-8-12` 的 50 題，以及 `S-9-5` 至 `S-9-9` 的 50 題，涵蓋相似比、平行線截比、尺規作圖、圓弧長、扇形、弦切線、點線圓關係、外心與內心；全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-243：數學重心、證明與立體幾何模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-9-10` 至 `S-9-13` 的 40 題，涵蓋重心比例與坐標、證明與反例、空間線面關係、截面、表面積與體積；全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-244：全庫完全重複題幹清除

- 日期：2026-08-28
- 稽核結果：全庫原有 8 組完全相同題幹，共 16 題，跨單元重複出現。
- 處理方式：保留穩定題目 ID 與單元連結，將每組第二題改為不同數值／情境的原創題，補上答案與解析；全部標為 `draft`，等待第二輪 AI／Terra 內容複核。
- 驗證結果：完全相同題幹組數降為 0。

## D-245：一次函數圖形與角模板題替換

- 日期：2026-08-28
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新坐標、數值、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `F-8-2` 一次函數圖形與 `S-8-1` 角的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-246：三角形全等與垂直模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、坐標、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-8-5` 三角形全等性質與 `S-7-3` 垂直的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-247：三角形基本性質與平面面積模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-8-8` 三角形基本性質與 `S-8-7` 平面圖形面積的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-248：三視圖與平行線模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新尺寸、坐標、角度、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-7-2` 三視圖與 `S-8-3` 平行的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-249：坐標距離與梯形模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新坐標、數值、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `G-8-1` 兩點距離公式與 `S-8-11` 梯形性質的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-250：全等圖形與平行四邊形模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-8-4` 全等圖形與 `S-8-9` 平行四邊形的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-251：坐標幾何導覽與基本幾何符號模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新坐標、長度、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `G` 坐標幾何與 `S-7-1` 簡單圖形／幾何符號的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-252：畢氏定理與剛性變換模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、坐標、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-8-6` 畢氏定理與 `S-7-4` 平移／旋轉／鏡射的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-253：一次函數與二次函數模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、坐標、函數式、情境、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `F-8-1` 一次函數與 `F-9-1` 二次函數意義的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-254：特殊四邊形與凸多邊形模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新數值、圖形條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-8-10` 特殊四邊形與 `S-8-2` 凸多邊形內角和的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-255：線對稱與平面坐標系模板題替換

- 日期：2026-08-29
- 本批來源：高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科公開試題，並以官方課綱 KG 核對單元範圍。
- 使用界線：只研究題型與能力方向；以全新坐標、長度、變換條件、選項與解析重寫，不重製公開試題文字、圖表或答案。
- 本批結果：替換 `S-7-5` 線對稱與 `G-7-1` 平面直角坐標系的 20 題模板，全部維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-256：修正跨課選項模板重用後完成 S-7-5／G-7-1 替換

- 日期：2026-08-29
- 驗證中發現 S-7-5 第 3 題與已替換的 S-7-4 第 3 題雖題幹不同，但整組選項與答案相同，觸發跨課模板重用檢查。
- 處理方式：改用不同鏡射坐標、選項與解析後重新執行全量 validator；相關 20 題仍為 `draft`，等待第二輪 AI／Terra 內容複核。

## D-257：社會科泛用題幹批次替換與答案直接呈現

- 日期：2026-08-29
- 問題：社會科仍有 345 個單元、3,450 題沿用同一套「分析單元相關資料／哪一項做法最合理」泛用模板；網站題目卡的答案與解析藏在折疊區，手機畫面容易誤判為沒有答案。
- 處理方式：依各單元 KG 概念與鹽埕國中公開段考的資料判讀能力方向，以全新題幹、選項與解析重寫 3,450 題；保留穩定 ID、lessonId、knowledgeIds，全部維持 `draft`。前端題目卡改為直接呈現選項、正解與解析，並避免標題與題幹重複顯示。
- 來源界線：僅研究公開段考題型／能力方向，未複製原試題文字、選項、圖片或答案；每題保留來源 URL 與原創 authoring note，待第二輪 AI／Terra 內容複核。
- 驗證：泛用分析題幹剩餘 0 題；本批題目選項唯一、答案 ID 有效、解析非空、同課題幹不重複；全量 validator 通過。

## D-258：自然科探究泛用題幹批次替換

- 日期：2026-08-29
- 問題：自然科仍有 302 個單元、3,020 題沿用「探究……哪一項做法最恰當」的泛用模板，且答案／解析不易在題目卡中直接辨識。
- 處理方式：依「測量估計、器材安全與客觀記錄、資料推論與問題察覺」等 KG 單元範圍，改寫為單元化探究題，補上唯一答案與解析；保留穩定 ID、lessonId、knowledgeIds，全部維持 `draft`。
- 來源界線：僅研究鹽埕國中公開自然科段考的題型／能力方向，未複製原題文字、選項、圖片或答案；保留來源 URL 與原創 authoring note，待第二輪 AI／Terra 內容複核。
- 驗證：舊「探究……哪一項做法」題幹剩餘 0 題；本批答案 ID、四個唯一選項與解析檢查通過；全量 validator 通過。全庫尚有 2 組歷史數學題幹重複，非本批新增，需另行內容改題。

## D-259：最後兩組數學完全重複題幹修正

- 日期：2026-08-29
- 處理方式：將正六邊形對稱軸與 5×12 長方形對角線改成不同於既有題目的數值／圖形問法，並同步修正選項、答案與解析。
- 驗證：全庫完全重複題幹組數降為 0；仍維持 `draft`，等待第二輪 AI／Terra 內容複核。

## D-260：英文元題型批次替換

- 日期：2026-08-29
- 處理方式：將英文 790 題「學習單元情境／針對學習目標」元題型改為直接英文文法、字彙、閱讀與日常對話題；保留穩定 ID、lessonId、knowledgeIds，全部維持 `draft`。
- 來源界線：僅研究鹽埕國中公開英文段考題型與能力方向，未複製原題文字、選項或答案；各題保留來源與原創 authoring note，待 Terra 第二輪 AI 複核。
- 驗證：元題型剩餘 0 題、答案與四個唯一選項檢查通過；全量 validator 通過。

## D-261：元題型與全庫重複題幹納入 validator 門檻

- 日期：2026-08-29
- 處理方式：`scripts/validate_data.py` 新增已知元題型拒絕規則，以及跨 lesson 的全庫題幹重複檢查；這些規則補足原本只檢查同課內容的缺口。
- 驗證：目前 10,380 題通過元題型與全庫題幹稽核；完全重複題幹 0 組。

## D-262：題庫狀態快照同步

- 日期：2026-08-29
- 處理方式：同步 `project-state.json`、`docs/CURRENT_STATE.md` 的實際 1,038 份 lesson／10,380 題 question、962 lesson content-reviewed／72 lesson draft、220 question content-reviewed／10,160 question draft；draft 仍不代表真人或專家審定。

## D-263：網站改用全量索引並限制單次渲染量

- 日期：2026-08-29
- 問題：`site/app.js` 仍讀舊的 95 課／950 題 manifest；改讀全量索引後若一次建立 10,000 多張卡片，又會造成瀏覽器載入失敗。
- 處理方式：部署索引加入全量題目必要欄位（題幹、選項、答案、解析），前端改讀 `data-index.json`，教材以分批請求載入，搜尋結果單次最多渲染 120 張卡片並顯示命中總數。
- 驗證：本機瀏覽器顯示 1,034 個 active lessons、10,380 題，搜尋「正六邊形有幾條對稱軸」可直接看到四個選項、答案 D 與解析；`validate_site_index.py` 與全量 validator 通過。

## D-264：公開會考題目改為獨立改寫

- 日期：2026-08-29
- 問題：40 題國文資料雖標示 `official-open`，題幹仍可辨識為公開會考原式，與本專案不得重製公開試題文字的界線不一致。
- 處理方式：以會考能力方向為研究依據，改寫為全新文化、閱讀、語文與生活應用情境，重新建立選項、答案與解析；來源僅保留作題型研究，`origin` 改為 `original`，全部維持 `draft`。
- 驗證：公開原式題目剩餘 0 題；全量 validator 通過，待 Terra 第二輪 AI 複核。

## D-265：補齊題庫 provenance authoringNote

- 日期：2026-08-29
- 處理方式：補齊 430 題缺少的 `authoringNote`；其中 30 題原先標示 `content-reviewed` 但來源界線欄位不完整，降回 `draft`。不新增未核實的授權主張。
- 驗證：10,380 題均具來源 URL、source locator 與 authoring note；目前 questions 為 190 題 `content-reviewed`、10,190 題 `draft`。
## D-266：Terra 第二輪 AI 複核後的再修正門檻

- Terra 以只讀方式複核英文、數學、社會與自然題庫，確認結構欄位大致完整，但指出「單元名稱／情境代碼」包裝的跨課模板仍可能通過原 validator；因此本次不升級任何題目為 `content-reviewed`。
- 本機交叉核對後，社會批次已是直接社會資料判讀題；另將 790 題英文移除生成代碼與 `for the ... practice` 選項標記，將單元語境與解析改為學習者可見的正常文字；將自然科 3,020 題改為含單元自然現象、測量或學科概念判讀的獨立編寫題。全部維持 `draft`，等待後續 Terra／AI 內容複核。
- validator 新增生成痕跡檢查、跨課 prompt／答案選項簽章檢查仍為硬錯誤；本次結果以「validator 通過」與「Terra 內容通過」分開記錄。

## D-267：社會與自然題改為具體資料／學科情境

- 日期：2026-08-29
- Terra 初輪指出，社會題雖已不再完全同題，但仍缺少資料、圖表、史料、地圖或案例；自然題也有把單元名稱套入探究流程的泛用題。這些內容不能升級為 `content-reviewed`。
- 處理方式：社會 3,450 題改用明確數值、比例、史料描述、地圖圖例、案例條件與制度情境；自然 3,020 題依生物、化學、物理、地科／環境及探究能力加入具體觀察、測量或實驗條件。每課十題使用不同題幹，保留穩定 ID、來源與 `draft` 狀態。
- 驗證：自然 327 個 active lessons 的題幹基礎重複為 0，社會題幹重複為 0；全量資料 validator 通過，但仍須 Terra 第二輪內容判讀。

## D-268：社會題按學科領域分流

- 日期：2026-08-29
- 問題：即使題幹含數據，若所有社會單元都使用相同的資料判讀骨架，仍可能只是跨課換皮。
- 處理方式：依 lesson 標題分流為公民、地理、歷史與一般探究能力題庫；公民加入法律位階、權利限制、民主程序與抽樣，地理加入人口密度、比例尺、土地利用、災害與區域差異，歷史加入史料作者、時間線、因果與遺址證據。保留穩定 ID、來源與 `draft`。
- 驗證：3,450 題答案欄位、選項與解析通過；每課 10 題 prompt 不重複；仍將跨課共用題型形式視為待 Terra 內容判讀風險，不升級 `content-reviewed`。

## D-269：英文題依語言能力分流

- 日期：2026-08-29
- 問題：英文 790 題雖已移除情境代碼，但若大量單元仍共用日常對話題，仍無法證明符合各 KG。
- 處理方式：依 lesson 標題將題目分流至閱讀／圖表／廣播／書信／字彙／拼字／文法／書寫／文化／對話題型；保留穩定 ID、段考題型研究來源與 `draft` 狀態。
- 驗證：全量 validator、答案欄位與題幹重複檢查通過；是否真正符合每個英文 KG，仍交由 Terra 第二輪 AI 內容複核。

## D-270：修正數學 s-Ⅳ-15 的 KG 不匹配題

- 日期：2026-08-29
- 問題：`lesson-math-performance-s-iv-15` 的 4、6、7、8 題原先分別考體積、面對角線、正方體俯視與三視圖體積，與「空間線面垂直平行」不一致。
- 處理方式：保留 question ID 與來源，改寫為直線與平面平行判定、直線與平面垂直判定、兩平面交線及平行平面的垂直關係；重新建立選項、答案與解析，維持 `draft`。
- 驗證：全量 validator 與答案選項對齊檢查通過；仍待 Terra AI 內容複核。

## D-271：替換因式分解同 KG 重複題組

- 日期：2026-08-29
- 問題：手機畫面顯示的 10 題因式分解題來自 `lesson-math-factorization-common-factor`，與另一個 `content-a-8-4` 題組共用同一 KG，造成搜尋結果出現高度重複題目；舊題雖有答案，仍不符合本專案「同課及跨課避免模板重用」的 QA 要求。
- 處理方式：保留既有 question ID，參考官方會考與公立國中段考的代數能力方向，以全新數值、情境、選項、答案與解析改寫 10 題；不複製公開試題文字、圖表、選項或答案，並將內容狀態維持 `draft`。
- 驗證：全量資料 validator、網站索引 validator、選項／答案對齊與 git diff check 通過；尚未完成 Terra 第二輪內容複核，不升級為 `content-reviewed`。

## D-272：部署索引內嵌教材資料

- 日期：2026-08-29
- 問題：公開 Pages 頁面原先由 `data-index.json` 載入題目，但再透過 `raw.githubusercontent.com` 逐課載入教材；raw 網域受限時，整頁會停留在「正在載入資料」。
- 處理方式：部署索引的 lesson 項目直接保留完整教材資料；前端優先使用索引內嵌教材，只有舊索引沒有 `content` 時才退回原本的 raw fallback。
- 驗證：本機索引包含 1,034 課、10,380 題；`validate_site_index.py`、`validate_data.py`、Python 編譯、`node --check` 與本機頁面載入均通過。公開頁面需待此次部署後重新 smoke test。
- 公開驗證補充：以唯讀下載核對 Pages `data-index.json` 的 `sourceRevision=fe163d62a`、1,034 課、內嵌教材、新數學題存在及舊題不存在；瀏覽器端因約 21 MB 索引可能逾時，故保留該工具限制註記。

## D-273：公開資料改採同網域分片載入

- 日期：2026-08-29
- 問題：D-272 的完整內嵌索引雖能避開 raw 網域依賴，但約 21 MB 的單一索引仍可能造成公開頁面首次載入逾時。
- 處理方式：保留輕量 lesson／question 索引，另外產生五個教材分片及五個題目分片；前端以同網域 `Promise.all` 載入，並保留舊索引相容路徑。
- 驗證：本機 `validate_site_index.py`、`validate_data.py`、`node --check site/app.js`、頁面 runtime 均通過；公開 `7aeb8ddbc` 的索引回報 1,034 課、10,380 題，10 個分片端點均 HTTP 200；GitHub Actions `validate-data` run `33198152630` 與 `deploy-pages` run `33198152644` 成功。

## D-274：清除跨課換名稱題型並建立語意骨架風險檢查

- 日期：2026-08-29
- 問題：完全相同題幹雖已為 0 組，但社會、自然、英文題庫仍有大量只替換 KG 名稱或數字的共用骨架，會讓學習者看到重複題，也不能證明單元符合度。
- 處理方式：保留既有 question ID，依社會的歷史／地理／公民與探究能力、自然的學科概念與探究能力、英文的閱讀／對話／文法／字彙能力，重寫題幹、條件、選項、答案與解析；公開會考及公立國中試題只作能力方向研究，未複製原文、選項、圖表或答案。
- 驗證：共重寫 7,820 題（社會 3,590、自然 3,240、英文 1,350），另重寫 24 筆數學共用技能題；`validate_data.py` 通過，答案選項對齊、provenance、每課至少 10 題及 exact duplicate 檢查通過。`audit_m4_semantic_risk.py` 的跨課骨架風險降為 0；70 個 lesson 標題草稿標記仍不升級，等待 Terra 第二輪 AI 複核。

## D-275：完成剩餘數學共用技能題的情境化替換

- 日期：2026-08-29
- 問題：上一輪語意掃描仍列出 24 筆數學題只以不同數值重複相同的質因數分解、平均數、數列、中位數與平方根練習形式。
- 處理方式：保留 question ID，改為花圃面積、分裝、測量、座位號碼、觀測值、地磚邊長等不同題幹情境，重建選項、答案與解析；仍以公開會考／公立國中試題的能力方向作研究，不複製原題。
- 驗證：24 筆均有唯一答案與解析；全量 `validate_data.py` 通過，semantic-risk scan 的跨課骨架風險降為 0，題目維持 `draft`，等待 Terra 第二輪 AI 複核。

## D-276：將跨課相同選項組合列為未完成風險

- 日期：2026-08-29
- 問題：原有 semantic scan 只移除數字後比對題幹，未檢查選項組合；因此題幹雖因日期與 KG 標籤不同而看似唯一，仍可能重用同一組選項與答案結構。
- 處理方式：`audit_m4_semantic_risk.py` 新增 `cross-lesson-identical-option-set` 報告項目；此項只作 AI 審查風險，不自動升級 reviewStatus，也不以人為流水號或無意義文字掩蓋重複。
- 驗證：目前基準資料掃描出 8,254 題跨課相同選項組合，故維持所有相關題目 `draft`；後續須按學科與 KG 語意重新命題，再由 Terra 進行第二輪 AI 複核。

## D-277：自然科依 KG 語意分流重命題

- 日期：2026-08-29
- 問題：自然科原題雖已避免完全相同題幹，仍大量共用探究流程、圖表或活動情境，無法證明題目真正對應單元概念。
- 處理方式：保留 question ID 與來源紀錄，依 KG 標籤分為電學、力學、波動、熱、運動、化學、生物、地科及探究等分支；以新數值、條件與選項重建題目，答案與解析同步重算，維持 `draft`。
- 驗證：重命題 3,240 題；`validate_data.py` 通過，答案值均對應選項。嚴格選項稽核的全庫剩餘風險為 8,242 題，故不宣稱內容審查完成，仍待後續選項模板清理與 Terra 第二輪 AI 複核。

## D-278：社會科依 KG 語意分流重命題

- 日期：2026-08-29
- 問題：社會科原題大量共用歷史史料、地理比例／密度及公民程序選項，僅替換 KG 名稱不足以證明單元符合度。
- 處理方式：保留 question ID 與來源紀錄，依 KG 標籤分為歷史、地理、公民與探究；以時間線、史料限制、人口密度、比例尺、地形資料、權利限制與公共決策等新條件重建題幹、選項、答案與解析，維持 `draft`。
- 驗證：重命題 3,590 題，`validate_data.py` 通過；嚴格選項稽核的全庫剩餘風險由 8,242 降為 4,652 題，故仍待英文／自然剩餘模板清理及 Terra 第二輪 AI 複核。

## D-279：英文先以單一 lesson 十題試點驗收

- 日期：2026-08-29
- 問題：英文全科直接套用有限句型會造成同課題幹碰撞、跨課答案／選項模板重用，以及不自然的語句。
- 處理方式：先針對 `lesson-english-content-ae-iv-1` 逐題設計短文、對話、舞台指示、文法、代名詞與事件順序題；每題重新建立自然英文選項、答案和解析，保留 `draft`。
- 驗證：該 lesson 10 題的題幹與選項組合均唯一；全庫 `validate_data.py` 通過。嚴格選項稽核的全庫剩餘風險降為 4,642 題；以此試點模式逐課擴展，未完成前不得升級 reviewStatus。

## D-280：英文逐課唯一性批次擴展

- 日期：2026-08-29
- 處理方式：依 D-279 的試點方式擴展前 10 個英文 lesson，共 100 題；每課使用十種不同短文、對話、字彙、教室用語或語音任務，重新建立選項、答案與解析，保留 `draft`。
- 驗證：10 課各自 10/10 題幹與選項組合唯一；全庫 `validate_data.py` 通過。嚴格稽核風險由 4,642 降為 4,542 題，並揭露 48 個跨課語意骨架風險，下一批仍須逐課驗證。

## D-281：英文 Ac 單元依能力分流重命題

- 日期：2026-08-29
- 問題：英文 Ac 相關題目仍有故事／舞台模板，與字彙、公共標示、教室指令及生活對話的 KG 能力不夠貼合。
- 處理方式：保留既有 question ID、來源與 `draft` 狀態，逐課重建 40 題；四課分別使用字彙語意、標示判讀、教室指令與日常對話題型，選項、答案及解析同步重寫，不複製任何公開考題原文、選項、圖表或答案。
- 驗證：四課各 10 題，題幹與選項組合均唯一；全量 `validate_data.py` 通過。嚴格稽核的跨課語意骨架風險由 48 降為 24，完全相同選項組合維持 4,542 題，仍待後續逐課重寫與 Terra 第二輪 AI 複核。

## D-282：英文剩餘草稿依 KG 能力批次重命題

- 日期：2026-08-29
- 問題：英文剩餘草稿大量共用時間、地點、文法及固定對話選項，雖題幹不同，仍會形成跨課模板重用。
- 處理方式：保留 question ID、來源與 `draft` 狀態，依 KG 標籤分流為文法、字彙、資訊判讀、閱讀、文化、溝通與學習策略題型；所有題目重新建立語境、選項、答案與解析，未複製公開會考或公立國中試題原文、選項、圖表或答案。
- 驗證：重命題 1,230 題；全量 `validate_data.py` 通過，英文跨課相同選項風險由 1,240 降為 57，跨課語意骨架風險為 0，仍待 Terra 第二輪 AI 複核。

## D-283：自然科數據案例與觀察條件擴充

- 日期：2026-08-29
- 問題：自然科依 KG 分流後，部分公式題仍因參數範圍太窄而重用選項，固定概念題也缺少具體觀察條件。
- 處理方式：保留 question ID、來源與 `draft` 狀態，擴大並獨立抽取電學、密度、反射、熱傳、速率、溶液、遺傳、板塊與月相題的實驗參數；答案與解析同步依新數據重算。
- 驗證：全量 `validate_data.py` 通過；自然科跨課相同選項風險降至 123，跨課語意骨架風險為 0，仍待後續 KG 細分與 Terra 第二輪 AI 複核。

## D-284：數學重用選項改為題目專屬干擾項

- 日期：2026-08-29
- 問題：數學不同題目的正確答案可能不同，但沿用同一組固定數字選項，無法呈現該題的計算錯誤路徑。
- 處理方式：保留 question ID、正確計算結論、來源與 `draft` 狀態；針對 84 題將錯誤選項改為依題目數據、角度、比例、機率或公式誤用設計的干擾項，並補充解析中的錯誤類型說明。
- 驗證：全量 `validate_data.py` 通過；數學跨課相同選項風險由 84 降為 16，剩餘 16 題包含概念相近的圓面積、正多邊形、比例、機率與重心題，需逐題做內容差異化，仍待 Terra 第二輪 AI 複核。

## D-285：自然科剩餘選項重用清零

- 日期：2026-08-29
- 問題：自然科依 KG 分流後仍有少量不同題目抽到完全相同的數據／概念選項組合。
- 處理方式：保留 question ID、來源與 `draft` 狀態，擴大並獨立抽取實驗數據；酸鹼、遺傳、反射、板塊、月相與氣候題的選項加入對應觀察條件，答案與解析同步更新。
- 驗證：全量 `validate_data.py` 通過；自然科跨課相同選項風險由 123 降為 0，跨課語意骨架維持 0，仍待 Terra 第二輪 AI 複核。

## D-286：英文 Ae 舊模板完整替換

- 日期：2026-08-29
- 問題：先前為保留英文試點而跳過的 Ae-Ⅳ-2～9 題目仍沿用固定閱讀、時間、標示與對話選項，造成使用者看到近似題。
- 處理方式：取消錯誤保留清單，重命題剩餘 1,300 題；依 KG 能力建立字彙、文法、資訊判讀、閱讀、文化、溝通與策略題型，保留 question ID、來源與 `draft` 狀態。
- 驗證：全量 `validate_data.py` 通過；英文跨課相同選項風險由 57 降為 0，跨課語意骨架維持 0，仍待 Terra 第二輪 AI 複核。

## D-287：全庫跨課題目重用稽核清零

- 日期：2026-08-29
- 問題：自然、英文及數學批次完成後，仍需確認沒有任何跨課相同選項、語意骨架或題幹重複。
- 處理方式：數學最後 16 題改為不同概念與數據條件；自然與英文批次保留原 question ID、來源及答案解析，所有題目維持 `draft`，不因自動驗證通過而冒充真人或專家審定。
- 驗證：全量 `validate_data.py` 通過；`audit_m4_semantic_risk.py` 回報跨課相同選項 0、跨課語意骨架 0，validator 題幹重複 0；僅保留 70 個 lesson 標題草稿標記，等待 Terra 第二輪 AI 複核。

## D-288：各科逐版本研究、單元獨立撰寫與融合門檻

- 日期：2026-08-29
- 問題：既有 M4R 主要完成資料結構、固定六階段與單一公開資源研究，不能證明每個數理、社會或語文單元都讀懂各版本後再融合；批次模板也會讓不同單元出現相同教學骨架。
- 決策：五科每一單元均須研究可取得的南一、康軒、翰林版本資料；可下載者先存本機受控快取，只能網頁閱讀者記錄 URL 與定位。LLM 必須依該單元的版本研究、官方課綱與 KG 獨立撰寫，禁止共用正文、例題、錯誤說明、互動步驟或題幹骨架。
- 狀態：採用。新增 `version-fused-v1`、`versionResearch`、`fusionRecord` 與 `audit_version_fusion.py`；歷史 `enrich_full_lessons.py` 預設拒絕執行，只能在明確指定下作舊資料遷移。
- 審查：未完成版本研究、融合或 Terra 第二輪 AI 複核者維持 `draft`；Schema、數量、建置與重複掃描通過不代表內容完成。

## D-289：數理互動教學必須逐單元獨立設計

- 日期：2026-08-29
- 問題：455 份數理／自然 lesson 雖有不同 simulation ID，但多數實際使用相同引擎、固定三步驟與泛用預測／觀察文字，互動沒有對應該單元的核心迷思與推理。
- 決策：互動渲染器可以共用程式能力，但每個單元必須獨立提供學習目標、操作物件、可改變條件、預測、步驟、錯誤回饋、證據與驗證方式；只替換標題、數字或 KG 名稱一律視為模板，不得通過內容審查。
- 試點：`lesson-math-content-a-7-3` 改為等式變形互動，使用情境建模、等量公理、逐步變形與代回驗算；新增 `simulation.learningDesign`，並修正同步工具避免覆蓋單元專屬設計。
- 驗證：455 份 simulation 契約通過；本機頁面已實際驗證 A-7-3 預測、三步驟切換與等式內容更新。其餘未完成逐單元設計者維持 `draft`。

## D-290：每篇每單元重新撰寫，禁止共用骨架

- 日期：2026-08-29
- 問題：部分 lesson 雖有六階段欄位與版本 metadata，教學段落仍可能沿用跨單元共用句型，無法達成「像寫課文一樣豐富、每篇獨立重寫」的要求。
- 決策：全科每一份 learning-content lesson 均須由 LLM 依該單元版本研究、課綱與 KG 重新撰寫完整課文；禁止共用正文、例題、迷思、引導練習、遷移、互動步驟與檢核骨架。任兩課正規化後出現相同教學段落即阻擋，不得以改名、換數字或換情境通過。
- 執行：`audit_lesson_independence.py --strict` 改為對所有 learning-content lesson 執行，且將兩課以上的重複列為風險；所有命中者維持 `draft`，須完成版本研究與獨立重寫後才能進入 Terra 第二輪 AI 複核。
- 品質判準：完成稿必須讀起來像不同作者針對不同單元各自寫成的課文；固定開場、固定轉折、固定句尾及固定互動流程均視為共用骨架，即使文字表面替換也不得通過。

## D-291：國文 Ac 目標檔名與官方課綱節點對應

- 日期：2026-08-29
- 問題：工作指示列出 `lesson-chinese-content-ac-iv-1` 至 `-5` 五個檔案；目前官方國文課綱、KG 與 coverage matrix 僅有 Ac-Ⅳ-1、Ac-Ⅳ-2、Ac-Ⅳ-3。Ac-Ⅳ-1 與 Ac-Ⅳ-2 已分別使用既有穩定 lesson ID `lesson-chinese-punctuation-effects-advanced` 與 `lesson-chinese-sentence-patterns`；Ac-Ⅳ-4、Ac-Ⅳ-5 沒有官方 curriculum／KG 節點，也沒有對應十題題庫。
- 決策：不得為配合檔名另建重複 lesson 或憑空新增 Ac-Ⅳ-4／Ac-Ⅳ-5。此次以三個既有穩定 lesson ID 重寫 Ac-Ⅳ-1～3；內容保持 `draft`，不修改題庫。後續若要處理第四、第五個單元，必須先提供正確的官方課綱代碼及其既有 KG／lesson 對應。
# D-294：3-Ⅳ-8 通用引導題不等同互動規格完成（2026-09-26）

- 衝突：lesson JSON 已有三題 `guided-choice`，但單元規格仍標 `implementationStatus=missing`，要求先預測、可操作地標記文本證據、解釋證據與結論的關係、完成新情境遷移；guide 的 `LanguageTimelineBlock` 只是類型提案，不是上述流程已驗收的證據。
- 決定：以逐單元 YAML spec 為互動發布 gate 的權威狀態；現存通用三題只算 lesson 內靜態檢核，不提升為已完成互動。本單元須補上短文／書信／訊息專屬、含 evidence 與 transfer 的操作後，才可將 implementationStatus 設為 `implemented`；瀏覽器與輔助科技 QA 未完成前 `qaStatus` 維持 `untested`。
- 狀態：本決定先澄清材料用途與驗收證據，不改 lesson 或 spec 狀態。後續實作與測試另記證據；三版本融合、內容／版權 QA 與發布 gate 仍各自獨立。

# D-296：3-Ⅳ-8 lesson互動與靜態網站資料快取驗證（2026-09-26）

- 決定：單元互動必須在實際網站由當前 lesson JSON 驅動；修改 lesson 後同步重建 `site/data-index.json` 與各科資料 shard，並用 `--check` 驗證。網站資料請求需 revalidate，避免瀏覽器持續呈現過期教材。專屬測試、網站正確互動流程通過後，只能記錄工程實作證據；全頁響應式、鍵盤、螢幕閱讀器及發布快取仍須各自驗收。
- 本次證據：`MessageReadingLab`於瀏覽器完成預測／證據／作答／新書信遷移；初測發現768px全頁溢出，修正版本單元卡為平板雙欄、內層教材單欄後，320／375／768px全頁與元件皆無溢出。JSON revalidate及資產版本更新使當前lesson shard可載入。全套`npm test`、全庫資料與規格驗證通過。真實鍵盤逐步操作、螢幕閱讀器及發布環境/CDN仍未驗；單元仍未完成全項QA、三版本融合、內容／版權審查及發布門檻；教材和題目維持`draft`。

# D-293：3-Ⅳ-8 題目來源依單題能力對位且維持原創（2026-09-26）

- 決策：公開公校試卷只作 `pattern-only` 能力模式依據；每題引用需指向實際英文評量的題號／頁次，並寫清楚觀察到的閱讀任務，不得以多個不相干 paper-level 來源堆高數量。單元題目須保留原創文本、選項、答案與解析，並維持 `draft` 直到版本融合、內容與版權 QA 等發布門檻完整通過。
- 本次對位：內湖 111-1 九年級 Q44–46（報告資訊／未提及資訊）、內湖 112-1 七年級 Q51–52（時間表與附註）、三多 112-1 七年級 Q36（海報對象／目的）、國昌 110-1 三年級 Q21–23（敘事情節順序）、國昌 112-1 三年級 Q19–21（往返信件）、鹽埕 114-2 三年級 Q39–47（日記與安全訊息）、鳳甲校方公開 113 國中閱讀素養 Q41（故事主旨）。來源頁與 PDF 於 2026-09-26 線上核對；受限 shell DNS 無法快取鹽埕 PDF，本次不聲稱已完成本機快取。
- 驗證：3-Ⅳ-8 reviewer 10/10、五個不同公校網域、50步與10種策略無重複；全庫來源目錄覆蓋212/212 URLs、來源語義0 flagged、答案欄位10,566/10,566、題目重複0；`validate_data.py` 14,431 JSON／13,111 IDs／1,032 KG。這些不等於學科正確性、三版本融合、完整版權審查或最終發布核准。

# D-292：版本融合教材與逐單元獨立撰寫列為專案內容憲法（2026-08-29）

## 決策

版本融合不是資料欄位或章節標記，而是 AI LLM 完成版本研究後的實際寫作責任。每科每單元都必須獨立重新撰寫完整教材，成品應像不同作者針對不同概念寫成的課文；禁止共用模板、固定骨架、批次套句或只替換單元名詞。數理科互動教學也必須隨單元重新設計，不得只共用選項流程。

## 執行門檻

1. LLM 必須讀取可取得的南一、康軒、翰林等版本資料，記錄來源定位、概念、表徵、例型、迷思與評量差異，再形成 `versionResearch` 與 `fusionRecord`。
2. 正文必須包含單元專屬的完整概念教學、推導或例證、常見錯誤、引導練習、遷移活動與自我檢核；語氣、入口、順序與互動任務須能與其他單元區分。
3. `scripts/audit_lesson_independence.py --strict` 對全量 learning-content lesson 通過前，不得升級 `content-reviewed` 或發布。
4. 版本融合、獨立性或 Terra 第二輪 AI 審查尚未完成時，lesson 與新增題目一律維持 `draft`。

## 影響

歷史批次教材即使通過 Schema 或舊版 QA，也必須依本決策逐單元回溯；本決策不允許為了維持舊數量而保留通用正文。實作可共用程式渲染器與資料 Schema，但不得共用內容或教法。

## D-293：內容撰寫子任務統一使用 Luna 模型（2026-08-29）

新的教材、題目、版本融合、互動教學與內容審查子任務一律指定 `gpt-5.6-luna`。既有進行中的子任務完成後，下一個續作必須切換至 Luna；此規則不改變 AI-only 審查、逐單元獨立撰寫與 `draft` 發布門檻。
# 2026-09-23 Implementation Guide 進度口徑衝突處理

- 發現 `docs/CURRENT_STATE.md` 與外部 implementation guide 的歷史段落仍保留 2026-09-12 的 `630/1,027（61.34%）` 快照；但兩份文件最上方的最新紀錄，以及 `project-state.json` 的 `implementationGuideCompletion`／`implementationGuideFirstPassProgress`，均以 2026-09-23 的 424/1,027 為目前執行序列。
- 目前不把歷史 630 快照直接當成可發布完成證據：它沒有與當前 1027 個 lesson、每題來源、版本融合、逐題 QA 重新建立一一對應的可機讀索引，而且 Dc-Ⅳ-4、Dc-Ⅳ-5 雖有舊報告，仍需在本輪重新回讀與 gate 驗證。
- 本輪暫採保守且可追溯的口徑：以最新 `project-state.json` 424 件為基線；對已存在但未納入最新序列的單元逐一重驗，只有完成回讀、來源／答案／互動契約與全套 gate 後，才遞增進度。所有單元在 Terra 第二輪、版權與正式發布前維持 `draft`。

## D-294：自然科 Jf-Ⅳ-2 公校試題來源採逐題原卷定位修復（2026-09-24）

- 不得把課程計畫或不含該考點的試卷保留為 `examPatternRefs`。每一筆來源須是可追溯公立學校原卷，定位到題號／頁碼，並說清楚本題只借用哪一項能力方向。
- Jf-Ⅳ-2 十題採內湖國中、小港國中、國昌國中公開段考；十題共 30 筆 pattern-only item-level refs。只記錄原卷能力結構，不複製原題、選項、圖表或答案。答案與五步詳解重新核對，單元題目仍為 `draft`。
- 此單元修復可降低來源語義稽核錯誤數，但不得外推為全庫來源 QA 完成；全庫未核實題目及所有其他發布 gate 持續阻擋。

# D-299：3-Ⅳ-11 封面預測須保留信心並以正文校準（2026-09-26）

- 將標題／圖片預測設計為兩段式原創閱讀實驗：封面先行預測，保存原文、引用至少兩類可見線索與初始信心後才揭露正文；讀者再標記支持證據、選擇保留未知範圍的修正版並重評信心，最後在不同封面情境遷移。
- 原始預測與信心須持續可見；更改上游線索或答案會使下游正確／完成狀態失效。互動素材使用 lesson 資料與 renderer，不將題文硬編碼在通用 UI。lesson 與題目維持 `draft`、implementation spec 維持 `qaStatus=untested`，直到出版社融合、完整內容／版權檢核及實際可及性 QA 完成。

# D-298：3-Ⅳ-10 故事要素採逐卡編輯標註與跨要素主題判讀（2026-09-26）

- 3-Ⅳ-10 不沿用 3-Ⅳ-9 的情節弧重建流程；互動採「故事編輯標註板」，六張原創線索卡依序聚焦場景、人物動機、敘事視角、伏筆、高潮與象徵，各卡以原文功能題及單卡提示診斷誤讀。
- 最終編輯註記需選出人物動機、高潮選擇及結果三項證據，選擇能由證據支持的可遷移主題並寫理由；敘事者猜測須與可觀察事實分開。保存進度；修改證據時清除依賴的主題答案／理由。
- 網站互動、lesson Schema、資料驅動 renderer、單元 implementation spec 與 component registry 同步維護。題庫沿用原創題及逐題校方公開考題 pattern-only 參照；lesson 和題目維持 `draft`。Publisher 全文融合、內容／版權與實機無障礙 QA 未完成前，不提升發布狀態。

# D-297：3-Ⅳ-9 故事情節互動以原創情節弧與證據遷移為核心（2026-09-26）

- 決定：靜態三題 guided-choice 不足以代表「故事主要內容情節」互動。此單元改以資料驅動流程驗收：先預測角色反應，再讀原創故事、標記目標／障礙／錯誤嘗試／轉折線索／結果，檢查主要情節摘要，最後在新故事重找線索、選擇推論並寫出因果理由。錯誤答案需回饋事件線索；保存互動狀態，更改上游證據須清除依賴答案。原創故事與問題不複製公校試卷；既有公開原卷僅作各題 `pattern-only` 命題能力參照。
- 狀態規則：lesson 與題目維持`draft`；三版本全文融合、內容／版權、實際鍵盤與輔助科技 QA、發布 gate各自獨立。未驗證項不得改為`verified`或`content-reviewed`。

## D-295：自然科 Aa-Ⅳ-4 公校試題來源逐題核實（2026-09-24）

- 將十題中課程計畫及泛化試題來源改為可追溯的公立學校原卷與單題／頁次定位；每題保存三份不同試卷的 pattern-only 能力引用，不複製題文、選項、圖表或答案。
- 十題正解、答案說明、解題策略及五步推理由 reviewer 固定答案與逐題 source-item pairing 驗收，10/10、30/30 通過；為補足步驟解釋，同步重寫答案說明與詳解。公開高中資優班題目僅作門得列夫預測能力模式參照，教材年級適切性仍以本單元課綱與單元內容為準。
- 此修復僅降低全庫來源語義稽核的 20 筆誤列；題目保持 `draft`，不提升單元第一輪完成計數，不代表來源目錄、publisher fusion、學科內容／版權、Terra 或全 guide gate 通過。
# D-074：Ab-Ⅳ-5 來源錯誤修正與三版本公立課程核實（2026-09-23）

- 問題：Ab-Ⅳ-5 原翰林 URL 實際回讀為英文課程計畫，原康軒 URL 也實際回讀為英文資料，不能作為國中國文常用語詞使用的章節證據。
- 處理方式：翰林改用高雄市立青年國中一年級翰林版國文課程計畫；康軒改用同校二年級第一學期康軒版國文課程計畫；南一改以嘉義縣永慶國中南一版第一冊課程計畫，逐一回讀 Ab-Ⅳ-5、文句邏輯、遣詞造句與評量定位。正文、題目、答案、解析與互動仍由本專案獨立撰寫，不複製來源內容。
- 驗證：三個 publisher evidence slots 記為 `verified`；lesson、10 題與 guided-choice 互動維持 `draft`，內容／Terra／最終 QA 尚未完成。
# D-075：Ab-Ⅳ-6 三版本公立課程證據核實（2026-09-23）

- 處理方式：翰林採嘉義縣六嘉國中八年級第二學期翰林版第四冊課程計畫；康軒採高雄市公立國中資源班康軒版第二冊課程計畫；南一採嘉義縣永慶國中南一版第一冊課程計畫。逐一回讀 Ab-Ⅳ-6 的文言詞義、語詞結構、文本理解、字典查證與評量定位。
- 驗證：三個 publisher evidence slots 記為 `verified`；lesson、10 題與 TextEvidenceBlock 互動維持 `draft`，內容／Terra／最終 QA 尚未完成。
# D-302：3-Ⅳ-14 快速閱讀互動以文本任務切換策略（2026-09-26）

- 快速閱讀不是限時逐字競速；互動依閱讀目的呈現不同原創文本，讓學生在略讀、依線索排序、格式尋讀及回讀確認間切換。錯誤提示指向該文本中的標題、路線欄、條件句或資格限制，不直接代答。
- 共用程式 renderer 與可及性表單結構可以重用，但文本、任務和診斷須由單元資料獨立撰寫。三版本全文融合、全科獨立性與內容／版權 QA 尚未完成，因此教材與題目保持 `draft`，implementation spec 保持 `qaStatus=untested`。
# D-303：3-Ⅳ-15 將敘事知識界線、語氣與證據範圍分階教學（2026-09-26）

- 互動按知識界線、作者態度、寫作目的、主張證據、樣本限制及新受眾遷移逐階呈現各自原創短文本；錯答提示必須指向本階可回讀的詞句或限制，不以共用公式替代內容分析。
- 可以共用資料驅動閱讀 renderer，但標籤、標題、文本、題目和回饋均由本單元資料提供。出版社全文融合、全科獨立性、內容／版權及真實輔助科技 QA 未完成前，維持 lesson/questions `draft` 與 spec `qaStatus=untested`。

# D-304：lesson publisher research scope 明確區分單元教學證據與版本／適性旁證（2026-09-27）

- lesson Schema 的 `publisherResearch.researchScope` 新增 `publisher-version-in-use`、`adapted-learning-objective`、`assessment-context` 與 `unit-curriculum-placement`，用來如實記錄公校課程計畫只證實採用版本、特教調整目標、評量脈絡或單元課程定位的情況；不得將其誤標成出版社單元教學順序或教材全文證據。
- 新範圍值只擴充來源描述詞彙，不會把 `publisherEvidence` 從 `pending` 升級，也不改動 lesson／question 的 `draft` 狀態或發布 gate。研究查核日期必須記錄實際回讀日期。

# D-305：依使用者指示暫停教材與題庫內容審查（2026-09-27）

- 暫停南一／康軒／翰林教材內容閱讀與融合、lesson／question 學科正確性與教學品質判讀、題目答案內容複核、內容／版權發布審查，以及任何 Terra 審查；不再為此擴大外部內容研究。
- 繼續執行不依賴教材審查的工程項目，包括互動實作、renderer／資料契約、Schema、程式測試、真實瀏覽器自動化、響應式與 axe 自動檢查、可重現性及報告一致性。
- 暫停不代表通過或永久豁免發布 gate。所有 lesson／question 維持 `draft`，implementation spec 不因工程測試通過而從 `qaStatus=untested` 升級；待使用者恢復審查後再處理相應內容 gate。

# D-306：依最新使用者指示恢復 lesson 與題庫內容審查（2026-09-27）

- 本決定取代同日 D-305 的全面暫停：lesson 與題庫的學科內容、出版社版本融合、題目答案及教學／內容品質審查均繼續執行。
- Terra 第二輪審查仍取消；不得派子任務。lesson／question 只有逐項滿足各自內容、來源、授權與發布 gate 後才可升級，既有 `draft` 狀態不因恢復審查而自動改變。

# D-307：lesson 教材內容審查暫停、題庫審查續行（2026-09-27）

- 依使用者最新指示，lesson 教材內容審查暫時取消，留待 ChatGPT 協助 review；不得把既有 lesson 初審紀錄冒充目前已完成的 ChatGPT review。lesson 仍維持 `draft`，出版社研究／融合 gate 不因暫停而通過。
- 題庫學科內容、正解、解析、解題步驟、公開試題改寫界線與品質審查繼續逐題執行；不派子任務、不執行 Terra。未完成來源逐題定位、內容／授權及其餘發布 gate 的題目保持 `draft`。
- 進度回報須分開計算「具備紀錄／局部初審」、「實質逐項完成」及「正式 `content-reviewed`／發布 gate」，不得將最後一項的 0% 說成整體工作完全沒有進度。

# D-308：公校公開試題來源帳本修復後進入版本融合（2026-09-27）

- 當前來源 ledger 有344題 pending；逐項發現全部含同一筆未核對科目／題號的碧華索引引用。其中338題另有兩筆已記錄公校試題來源，因此只移除該筆明確非證據索引並保留既有來源；另6題逐題回核公校原卷頁碼／題號後新增來源。不得把刪除無證據引用稱為新增來源證據。
- 全庫公校來源帳本 `audit_question_exam_rewrites.py` 通過10,566/10,566；來源語義稽核23,131 refs／0 flagged；公開來源目錄489 entries、278/278題目來源URL覆蓋。來源帳本通過只完成來源記錄 gate，不代表題目學科內容、答案、版權或發布QA通過；所有題目保持`draft`。
- 下一階段按使用者要求開始南一／康軒／翰林實質融合，逐課記錄實際可讀來源與概念比較，不以章節索引／欄位存在冒充全文研究；lesson內容審查依 D-307 留待 ChatGPT review，不派子任務、不執行Terra。
## D-314：A-8-4 限定因式意義，分解算法歸入後續單元

- 日期：2026-09-27
- 決策：A-8-4 教材與互動聚焦因式／倍式關係、二次多項式的乘積表示、候選因式與商式及乘回／整除驗證；不得把提公因式、平方差、和積配對、完全平方或十字交乘當成本課核心教學。公開分享材料僅作概念入口與章節編排的有限旁證：南一材料本次只取得索引可見片段、康軒為作者標示版本的學生筆記、翰林為第三方分享且標示 All Rights Reserved 的補救教材；不把它們說成已讀完三家出版社官方原書，也不抄寫正文或題目。Lesson 維持 `draft`。A-8-4 spec 中與此邊界衝突的目標／互動／題例須同步收斂至概念驗證，不可用既有 spec 推翻官方課綱範圍。
- 理由：現有 A-8-4 lesson/spec 將後續方法單元的多種演算法混入「因式分解意義」，而翰林公開分享目錄把因式與倍式辨認、提公因式／公式及十字交乘列為不同教學主題；南一與康軒可取得材料的權威與閱讀完整度亦有限。必須誠實區分概念理解、算法教學與來源權威，避免把索引或課程計畫冒充完整版本研究。
## D-315：A-8-5 以三版本公開單元材料融合因式分解方法

- 日期：2026-09-27
- 決策：A-8-5 lesson 以官方範圍「提公因式、乘法公式、十字交乘」為核心。來源採南一標示自學講義公開分享索引（相關頁91–100）、康軒第三冊標示學生筆記（共同因式與十字交乘片段、課次索引含乘法公式）、翰林官方資源站112版課本及補救GO索引（3-1公因式／公式、3-2十字交乘）；每筆都記錄其來源類型、頁次及檢索可見範圍。翰林PDF直接開啟回403，故不宣稱已下載或讀完索引未顯示部分；南一與康軒亦不宣稱官方出版商完整原本。lesson 自行重寫為係數／變數／括號三層掃描、提出後重判、公式條件、頭尾交叉和及完整乘回，排除A-8-6「因式分解解一元二次方程」內容。保留lesson `draft`、spec `qaStatus=untested`。
- 理由：舊版 A-8-5 版本研究把公校課程計畫、均一及出版社影音索引混記為出版社教學正文，不能證實各版單元教法。使用者允許參考公開分享內容後，本次取得帶頁次的三家相關教材材料，得以進行有來源界線的內容融合；但搜尋索引、學生筆記與第三方分享不能被描述成三家官方全文比讀。此證據足以支持本課概念融合作業，不代表專家審定或發布QA。
## D-317：A-8-7 三版本公開教材材料融合補記（2026-09-27）

- 決策：保留 A-8-7 既有原創應用與解題活動，新增根據本次可讀版本標示材料重新融合的方法入口與公式推導教學。融合順序為辨認平方根特例／易分解型／一般式，留下等值變形，從配方理解判別式與公式，再完整求根、代回、情境篩選。
- 來源：南一版標示公開講義Scribd索引pp.139–144；康軒第三冊標示Clearnote使用者筆記p.1；翰林官方112版補救GO搜尋索引pp.162–178、182–186，並以111版分享摘錄pp.69–79交叉查看。南一與康軒分享非出版社認證原書；康軒OCR有失真僅採清楚可讀步驟；翰林官方PDF本次直開HTTP 403，故只依官方索引與可讀分享摘錄，不宣稱讀完整本。
- 理由：既有三筆 verified slot 的核心證據是公校課程計畫，不等同出版社單元教學材料。新增研究讓可驗證的教學支架及其權威限制可追溯，並把不同版本呈現轉成原創 lesson 說明，未複製來源例題、文字、答案或圖片。
- 狀態：publisher ledger 全庫狀態不因本次研究自動調升；lesson 維持 `draft`，spec `qaStatus=untested`。依使用者先前要求，lesson 學科／教學內容審查留待 ChatGPT review；自動化驗證不等同教材審查或發布通過。
- 報告：`implementation/reports/a8-7-three-publisher-fusion.json`。
## D-318：A-8-7 選答互動與正式資料 shard 必須同步驗證（2026-09-27）

- 決策：A-8-7 lesson 的活動為網站資料驅動三選一，不描述成目前不存在的滑桿或拖曳操作；六階段需覆蓋建模、因式分解、兩側同步配方、公式與判別式、情境篩選。lesson JSON 修改後，依 D-296 重建 site index/shards 並執行 `--check`，再以真實瀏覽器對網站載入資料驗證錯答、正答回饋、鍵盤及窄螢幕。
- 問題及處理：第一次瀏覽器測試讀到舊的 `site/data-lessons-math.json`（五階段），斷言失敗。重建後 shard 套用新的六階段，1,052課網站索引及shards校驗通過，重跑瀏覽器成功；初次失敗不是程式庫或Chrome缺失。
- 驗證：A-8-7 六階段通過；320/375/768px無水平溢位；完整workbench 1,027/1,027。axe 15 runs、0 violations、0 incomplete。這些自動化不等同真人螢幕閱讀器或lesson學科內容審查；維持lesson `draft`、spec `qaStatus=untested`。
- 報告：`implementation/reports/a8-7-three-publisher-fusion.json`。

## D-319：A-8-1 三版本公開教材材料融合草稿（2026-09-27）

- 決策：A-8-1 lesson 以分配律逐項配對、面積區塊的交叉項數量、平方差中項抵消，以及公式使用條件為共同主線；原創加入 202×198 同中心等距拆解，並明確對照 202×197 不符合平方差條件。互動以實際存在的階段選答／檢視呈現，不宣稱有拖曳滑桿。
- 來源：南一標示八上自學講義第三方分享約pp.10–15及南一111教材簡介本第三方副本附件目錄；康軒D版標示 Clearnote 使用者筆記 p.2；翰林官方112補救GO學用本搜尋索引約pp.4–7及111版第三方分享pp.4–7。來源類型、定位、日期、權威與存取限制記於 lesson；翰林官方PDF直開403，南一／康軒分享非出版社認證原書，均不得宣稱完整官方原書核讀。
- 界線：僅以可讀概念、表示法及教學支架為融合研究，所有正文、例題、答案、互動均另行撰寫，不複製來源文字、題目或圖形。新增報告與單元互動資料契約測試；lesson 維持 `draft`，不將教材內容審查或發布 gate 設為通過。
- 報告：`implementation/reports/a8-1-three-publisher-fusion.json`。

## D-320：補強 A-8-4 公開版本證據並修復乘積反例（2026-09-27）

- 決策：依 A-8-4 官方課綱與 KG，保留本課只教因式／倍式方向、二次式的乘積表示與候選驗證，不提前教授提公因式、公式法或十字交乘。補讀南一標示講義索引pp.87–89、康軒第三冊標示學生筆記pp.1–2、翰林官方111補救GO搜尋索引（對應課本pp.116–117）及其第三方分享目錄，分別記錄來源可讀內容與權威限制；未讀取的官方PDF正文不當作已核讀，學生筆記OCR失真的算式不沿用。
- 發現並修正原 lesson 錯誤：`(x+3)(x+4)=x²+7x+12`，不是 `x²+7x+10`。新增以常數項不符揭露「只檢查首項／中間項」的錯誤診斷，lesson互動與單元spec同步為五階段，移除錯誤的因式樹／拖曳分解流程描述。
- 來源僅支持可追溯的版本材料融合草稿，不等於三家出版社官方原書全文比讀；publisher ledger 不因本報告自動升級。lesson 維持 `draft`，spec `qaStatus=untested`，內容審查待後續。
- 報告：`implementation/reports/a8-4-three-publisher-fusion.json`；新增 `implementation/runtime/math-a-8-4-publisher-fusion.test.mjs`。

## D-321：A-8-4 實機互動納入正式瀏覽器與 axe runner（2026-09-27）

- 決策：擴充既有 `scripts/browser_smoke_test.py`，正式點測 A-8-4 五個 activity steps 的錯答重試、正答回饋、鍵盤操作、三種 viewport，並確認第5階段選項呈現常數項12與10不等；擴充 `scripts/browser_a11y_audit.py` 將 A-8-4 加入代表單元。
- 實測環境：Python 3.14 路徑 `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`、Playwright 1.58.0、Chromium revision 1208。正式 URL `/implementation/workbench.html`，HTTP 200。全庫 smoke 1,027/1,027遍歷通過，A-8-4五階互動及320/375/768鍵盤回饋通過；axe 18 runs、0 violations、0 incomplete。
- 界線：這是自動化 DOM／瀏覽器檢查，不等於真人讀屏或教材學科內容審查；lesson維持draft、spec qaStatus仍untested。
- 詳細輸出：`implementation/reports/browser-smoke.json`、`implementation/reports/browser-a11y.json` 及 A-8-4融合報告。

## D-324：A-7-2 方程式意義範圍修正與第三方教材閱讀界線（2026-09-27）

- 決策：依 A-7-2 課綱範圍，lesson 與互動聚焦情境列式、方程式結構分類及代入候選值檢查；解方程式的等量變形方法留在 A-7-3，不以求解流程冒充本課重點。
- 來源：閱讀一份標示翰林 111 數學 1 上補救GO的 Scribd 公開分享，頁面可見 3-2 列式與解的檢驗及課本頁次 P168–169；該頁標示 All Rights Reserved，上傳者與授權未核實，非出版社認證。康軒 Clearnote 僅能確認使用者筆記標題／版本自述，頁面影像不可讀；南一均一頁僅提供課程節點與章節定位，沒有可讀出版社正文。因此不得稱已完整閱讀三版，也不得把本課計為三版本融合完成。
- 界線：只採用可確認的概念次序與表徵，lesson、例題、答案和互動均自行撰寫；保留 `draft`、spec `qaStatus=untested`。公開可讀不等於授權重製。
- 驗證：A-7-2 專屬互動測試、全套 `npm test`、全庫獨立性稽核 614 篇／0 風險通過；實機 Chromium 全站 1,027/1,027 遍歷及該課錯答重試、正答回饋、鍵盤與 320／375／768 寬度通過；axe 24 runs／0 violations／0 incomplete。規格 validator 1,027 檔／0 errors／1,027 pending；資料 validator 修正概念欄位最小長度後通過 14,446 JSON／13,111 IDs／1,032 KG。全庫互動 simulation validator 仍有其他單元失敗。自動化不等同教材內容審查、真人讀屏或發布核准。
- 報告：`implementation/reports/math-a-7-2-scope-and-source-research-2026-09-27.json`。

## D-325：A-7-2 以可讀單元材料實際融合並修正來源／互動誤述（2026-09-27）

- 決策：不再將先前只看索引的南一／康軒證據寫成版本共同概念或已融合內容。深讀一份翰林標示的第三方111補救GO分享：檔案頁81–82（對應課本P168–169）先呈現符號列式與候選值檢驗表，後續才另列等量公理／移項。將這個教學支架重新設計成「情境量定義→組成並反讀方程式→結構分類→候選值代回並列左右證據」；情境、數據、題例、診斷、回饋和互動皆為本課原創，沒有複製來源題目。
- 來源分級：南一為均一「類南一版」課程頁次映射，康軒與翰林官方頁為課次／資源索引；均未取得可與已讀材料比較的出版社正文。因此A-7-2記為「單一版本標示材料主導的實質融合草稿」，不是二版或三版融合；Publisher evidence slots不調升。第三方頁標All Rights Reserved，來源真實性與授權未核實。
- 範圍／產品一致性：同步清除lesson摘要與離堂檢核中的移項、兩側逆運算及求解步驟；修正把目前選項式互動寫成拖曳／天平操作的描述。spec融合規則容許在證據可讀性不足時據實降為一版主導，但要求逐版揭露來源類型及閱讀限制。lesson維持`draft`，spec `qaStatus=untested`。
- 驗證與紀錄：A-7-2 regression、全套`npm test`、資料驗證、spec結構驗證、strict lesson independence、網站索引重建/check、授權Chromium全站／A-7-2互動及axe均通過；全庫spec仍1,027 pending。自動化不是教師／真人內容審查或真人讀屏。細節：`implementation/reports/a7-2-substantive-fusion-d325.json`。

## D-326：A-7-2 本質融合補上來源到教學決策的逐項追溯（2026-09-27）

- 決策：D-325 已建立原創單元課文，但為了避免「有融合標籤、看不到融合如何改變教學」的落差，本次將每個可讀來源洞見明確映射到本課段落、互動與評量決策。翰林標示七上課本第三方分享 OCR 頁168–170可讀到文字關係轉方程式、定義與左右值檢驗表，後續頁另進等量公理；另有翰林標示補救GO頁81–82作相近支架佐證。南一與康軒平台樹僅作分段／頁次比較；康軒再以金山國中版本標示課程計畫校準週次和目標；學校計畫只算課程安排證據，不冒充教材正文。
- 實質融合落點：由各材料可核對的「情境表達—辨認—候選檢驗—後續求解」教學功能，獨立重排為量義與單位→建式並反讀→按等號／未知數／次數分類→候選值代入並分別比較左右→遷移與自我檢核。此順序具體落在lesson六段教學、四階互動和離堂檢核；分流錯誤回饋及同儕由式還原故事是本課新增，不歸因出版社。沒有搬用原題、數值或表述。
- Gate：這是「多來源比較後的原創融合草稿」，不是三家出版社課本均已實讀或出版社證據帳本完成。南一／康軒可讀出版社正文仍缺；翰林分享真實性、上傳權限與授權未核實；publisher evidence維持pending，lesson draft、spec qaStatus untested，內容審查等待ChatGPT。詳細逐筆定位與source-to-design trace見`implementation/reports/a7-2-substantive-fusion-d326.json`。
- 測試：本次先更新 A-7-2 regression assertions；執行結果及後續資料／套件驗證需依實測追加，不以歷史 D-325 測試冒充本次通過。

## D-327：A-7-3 本質融合以來源分級及可見正文落點驗證（2026-09-27）

- 決策：以可讀來源中的教法差異實際改變本課教學，而非把版本名稱或章節摘要並列。翰林標示第三方掃描/OCR可見頁176–177並列等量公理與移項寫法，頁178–180涵蓋括號／分數方程式，頁184–188呈現應用題由定義未知數到依情境作答的工作序列。lesson把這些洞見轉成三段網站實際呈現的原創正文：固定費與每份量建模、以新係數逐行對照兩種解法、分數式全項清分母並回原式／情境驗算。
- 來源分級：南一均一「類南一版」與康軒「類康軒版」平台只作課程樹／頁碼定位；康軒官方影音頁為索引，公校計畫只作範圍／週次旁證，兩家出版社課文正文未讀。翰林材料為Scribd第三方分享且標All Rights Reserved，版本真實性、上傳權限與授權未核實。故成果明確限為「一份版本標示分享材料主導的多來源原創融合草稿」，不稱三版本正文融合，三家publisher slots均保持pending。
- Gate：lesson維持`draft`；單元規格`qaStatus`維持`untested`；內容審查待完成。新增逐來源到lesson位置及教學決策的追溯報告 `implementation/reports/a7-3-substantive-fusion-d327.json`。題例、數值、文句與迷思診斷均自行撰寫，未複製來源。
- 驗證：本次執行結果須實測後填回報告與狀態文件；不以 A-7-2 或歷史全庫測試結果冒充本次通過。
## D-332：A-7-2 本質融合狀態與完成邊界（2026-09-27）

- 決策：A-7-2 的融合進度不得再以全庫正式發布 gate `0/1,027` 或publisher ledger verified slots推算為「融合0%」。本課已完成來源差異→教學取捨→學生可見原創段落／互動的實質融合草稿：以原式代入、比較左右值界定「解」，把天平與等式兩側同作運算留至A-7-3；此取捨分別受南一局部第三方課文摘錄、南一對齊平台課程序列、康軒官方資源索引、翰林標示教材樣本及翰林官方三版本架構表交叉支持。六段可見課文、四階互動及算式均已在D-331報告與A-7-2 regression具體追溯。
- 完成界線：本結論只表示「依目前可讀證據完成原創融合草稿及可追溯設計」，不表示南一／康軒／翰林完整正文均已實讀，也不表示第三方材料版本真實性／授權、教材內容審查或發布QA已過。使用者允許閱讀網路分享，不代表可複製受保護表達；缺讀來源不得標verified。三家publisher slots仍pending、lesson仍draft、spec仍untested。
- 本輪驗證：`npm run test:math:a7-2`通過；`scripts/validate_data.py`通過14,453 JSON、13,111 IDs、1,032 KG；`git diff --check`通過。未重寫課文、未重跑公校題源帳本、未派子任務、未commit/push。報告`implementation/reports/a7-2-fusion-resolution-d332.json`。

## D-330：A-7-2 把版本研究逐段鎖定到學習者可見教材（2026-09-27）

- 核查：A-7-2並非沒有實質教學或0%；lesson已有六段可見原創教材。D-326已記錄翰林標示課本pp.168–170及補救GO pp.81–82的候選值左右比較支架，並以均一「類南一版」、康軒索引／校方計畫確認單元順序與A-7-3邊界。本輪發現舊 regression 未逐段鎖定`content.sections`和來源設計的連結，造成完成工作難以從測試證據看出。
- 修正：為既有A-7-2測試新增六段可見正文斷言：情境列式、左右相等定義解、結構分類、表示錯位診斷、反讀情境及出口檢核；同時測試候選值算式、A-7-3範圍界線及版本融合原創設計記錄。新增source-to-visible audit report，逐條列出來源、正文位置、原創教學決策和來源限制。未重寫既有教材，避免重做。
- 狀態界線：這證明本課已完成可追溯的多來源原創教材綜整草稿，不等於三家出版社課本已讀完或三版本publisher slots完成。南一／康軒正文未讀；翰林兩份Scribd分享標All Rights Reserved，真實性、上傳權限、重用授權未核實。所有publisher slots pending，lesson draft、spec `qaStatus=untested`。
- 驗證：`npm run test:math:a7-2`通過；strict independence本次614篇／0風險／0失敗；`npm test`、資料14,452 JSON／13,111 IDs／1,032 KG、規格1,027／0錯誤／1,027 pending、報告JSON解析及`git diff --check`均通過。無需重跑公校題源帳本、不分派子任務、不commit/push。

## D-329：A-7-5 以兩份版本標示材料重建可見的解法教學（2026-09-27）

- 決策：頁面實際讀取的`content.sections`才是學生可見正文；原資料雖有較完整`teaching.body`，可見區仍僅三句摘要，不得視為完成。本次按可見內容重寫五段單元專屬教學：票券雙條件建模、代入括號逐步推導、係數相同整行消去、需倍乘之消去例、迷思與情境限制遷移。數字、情境、文句及算例均自行設計。
- 來源比較：讀取康軒標示七下講義印刷pp.18–21、28–29、31–32及翰林標示七下課本pp.22–30、41–47附近OCR；對照代入支架、係數配對／整行運算及程序後的應用脈絡。南一僅讀到均一「類南一版」課程地圖，正文未讀，不推導其教法。
- 權利與狀態：兩分享頁標All Rights Reserved；非出版社認證，上傳權限、版本真實性及重用授權未核實，僅有限研究概念支架，不複製原文、題目、數字或圖表。僅稱兩份版本標示材料主導的原創融合草稿；三家publisher slots仍pending，lesson `draft`、spec `qaStatus=untested`。詳見`implementation/reports/a7-5-two-version-substantive-fusion-d329.json`。
- 驗證：lesson/report JSON解析、單元source-to-visible regression、`npm test`（含1,027/1,027課程bundle traversal）、`validate_data.py`（14,451 JSON／13,111 IDs／1,032 KG）、implementation specs（1,027／0 errors／1,027 pending）、strict independence（614篇／0風險）及`git diff --check`均本次通過。初次資料驗證指出sourceType enum與數個證據短句不合Schema，已逐項修正後重跑全量資料驗證通過。Browser未重跑（本次僅內容、來源紀錄、規格與測試改動，未改runtime行為）。Schema通過只代表結構有效；lesson仍draft、publisher slots仍pending、spec仍untested，公校試題來源帳本未重跑；不分派子任務、不commit/push。

## D-328：A-7-4 依兩份版本標示公開材料重構共同解教學（2026-09-27）

- 決策：A-7-4課程範圍是聯立方程式的意義，不是求解算法。讀取康軒標示七下自學講義分享頁14–16中分別形成候選解集合、找出共同有序數對的活動；並讀取翰林標示七下課本分享P36–37附近的雙條件情境、同一候選對逐式代入與失敗候選辨別。把兩種支架融合重寫為「固定變數順序→分別列條件→兩欄逐式檢驗→以交集定義共同解→翻譯回情境」，並改寫學生可見的核心觀念、流程和迷思診斷，例子／係數／算式自行設計。
- 來源界線：兩份均為Scribd第三方分享並標All Rights Reserved；上傳者權限、版本真實性及重製授權未核實。南一只有「類南一版」課程地圖／公校計畫，正文未讀。故本課只稱「兩個版本標示材料主導的原創融合草稿」，不稱出版社官方二版或三版融合；三家publisher evidence都維持pending，lesson為`draft`，spec `qaStatus=untested`。
- 追溯與回歸：`implementation/reports/a7-4-two-version-substantive-fusion-d328.json`逐來源記錄可讀內容、限制及至`content.sections`／互動的教學決策；新增`implementation/runtime/math-a-7-4-substantive-fusion.test.mjs`鎖定正文、頁次、雙式算例及狀態門檻。
- 驗證：`validate_data.py`通過14,449 JSON／13,111 IDs／1,032 KG；implementation spec 1,027份／0錯誤／1,027 pending；`npm test`通過且workbench 1,027/1,027呈現；strict lesson independence 614篇／0 risks；本課source-to-design回歸、JSON/YAML parse與`git diff --check`通過。此內容變更未改runtime程式，未重跑瀏覽器；lesson仍draft，publisher slots不升級。
## D-337：A-7-2 本質融合來源決策再核驗（2026-09-27）

- 核查：確認既有六段 lesson 正文、四階互動與 D-331 source-to-visible audit 已把來源差異落成教學決策；不因發布 gate 的全庫 0/1,027 誤稱本課融合 0%，也不重寫既有內容。
- 新佐證：翰林官方教材簡介可搜尋摘錄指出，將候選值代入並檢查原式左右相等可判定方程式的解，另有後續解方程式例項；均一類南一版課程樹將「列式與解的意義」和「等量公理與移項法則」分節。兩者只作官方簡介摘錄／版本對齊課程結構佐證，並非完整出版社章節，不能升格成三版本全文讀畢。
- 狀態：A-7-2「原創、可追溯的來源知情融合草稿」完成；出版社完整正文與授權核實、獨立教材內容審查及正式QA未完成，因此三個 publisher slots 仍 pending、lesson draft、spec qaStatus untested。不得將兩層狀態合併成一個完成百分比。
- 本次驗證：`npm run test:math:a7-2`通過；`python3 scripts/validate_data.py`通過14,460 JSON／13,112 IDs／1,032 KG（lesson content-reviewed 0、draft 1,052；questions content-reviewed 0、draft 10,566）；`git diff --check`通過。未重跑題源帳本或瀏覽器套件，因資料與runtime均未變更；未派子任務、未commit/push。證據報告：`implementation/reports/a7-2-fusion-resolution-d332.json`。

## D-338：A-7-8 有限來源研究、逐段原創融合與可操作數線驗收（2026-09-27）

- 來源與差異：南一標示第三方講義僅有限搜尋OCR節錄；康軒標示校方課程計畫可讀到數線平移、負數乘除翻向、求解與應用順序，並非課本正文；翰林出版社官方4-2頁僅公開資源索引，未核讀完整影片／章節。另保留既有三家校方課程定位來源，但不把它們當出版社全文證據。真實版本與第三方權利均未核實。
- 融合決策：將有限而不同的支架重新組織成六段A-7-8專屬教學：候選值界定解集→數線反射說明負因數翻向→逐行保留同一解集→回原式檢查開端點→現實預算與整數限制取交集→出口題做完整遷移。數字、情境、解說與視覺皆原創；source-to-visible逐項對照見`implementation/reports/a7-8-three-source-substantive-fusion-d338.json`。新增四階`inequality-solution-set`互動及帶空心端點／測試值／替代文字的專用SVG數線，步驟按鍵重繪後保留焦點。
- Gate：此為有限可讀材料支撐的原創融合草稿，並非已讀完三家出版社教材。三 publisher slots維持pending、lesson `draft`、spec `qaStatus=untested`；著作權／版本真實性與獨立內容審查未完成，不升級狀態。
- 驗證：`npm run test:math:a7-8`、資料驗證14,460 JSON／13,112 IDs／1,032 KG、strict independence 614篇／0 risks／0 strict failures、spec validator 1,027／0 errors／1,027 pending均通過。授權系統Chrome Playwright全站1,027/1,027、A-7-8四步／鍵盤焦點／可存取SVG／320、375、768px通過；axe 30 runs（含A-7-8）／0 violations／0 incomplete。完整 browser smoke 需依本地教材重建被忽略的衍生site index後執行；失敗斷言已修正為SVG textContent並指向第四步，而非改動教學功能。已完成題源帳本不重跑；A-7-2與A-7-7不重做；無子任務、未commit/push。
## D-343：A-7-2 互動情境量義與規格狀態一致性修正（2026-09-27）

- 發現：四袋徽章互動實際使用`4x＋3＝27`，但lesson變數仍寫單價／材料／運費，spec初始狀態仍用重量欄位；因此學生的變數定義與題目情境不一致。YAML解析另揭露`testCases`及`definitionOfDone`清單縮排錯誤。
- 修正：將互動量義改為每袋徽章枚數、袋數4、散放枚數3、總數27；spec初始欄位改為`equalBags`、`looseBadges`、`totalBadges`，補足案例中的量義描述，並修復兩個清單的縮排。A-7-2回歸新增四欄精確比對，防止量義回退。
- 驗證：`npm run test:math:a7-2`通過；PyYAML解析成功（6個test cases、7個DoD）；`validate_implementation_specs.py`全庫1,027檔、0 errors、1,027 pending；`git diff --check`通過。未改runtime code，未重跑browser。
- 完成界線：只修互動資料與規格一致性，不代表重新完成或升級來源融合、出版社證據、lesson內容審查或規格QA。lesson維持draft、三publisher slots pending、spec QA untested。未重跑題源帳本、未派子任務、未commit/push。詳見`implementation/reports/a7-2-interaction-semantic-consistency-d343.json`。
## D-344：地 Af-Ⅳ-1 可見融合教材、來源強度與真實互動規格（2026-09-28）

- 核查：網站`lessonDetail()`僅顯示`content.sections`；此課六段原創教學只在`teaching.body`，學生端原僅見一行學習目標。既有spec也承諾未實作的MapDataBlock滑桿、同步圖表和泛用診斷。
- 來源：翰林官方113下教用統整檔PDF p.17讀到聚落形成／類型、城鄉互依、運輸方式與網絡章節架構；康軒官方頁只核實七下第五課標題，未看影音；南一採用版別的公校計畫PDF pp.101–103支持課程目標／評量安排，但非出版商正文。不得宣稱三版課文實質比較已完成或升級publisher evidence。
- 修正：六段lesson移入實際渲染的`content.sections`；以逐來源證據等級重寫fusionRecord，刪除不相干對照引用；spec改為服務功能與流向、可達性、交通建設受益／成本的單元目標，將實際三題guided-choice列作唯一互動，不再承諾不存在的地圖操作。新增`GuidedChoiceBlock` registry描述、source-to-visible regression、瀏覽器測試及axe代表課。
- 驗證：target regression、`npm test`、資料14,467 JSON／13,112 IDs／1,032 KG、strict independence 614／0風險／0失敗、spec 1,027／0 errors／1,027 pending、site index 1,052 lessons／10,566 questions／40 mappings；授權Chrome全站遍歷1,027/1,027、本課六段／四階重試／鍵盤／320、375、768px通過；axe 39 runs、0 violations／0 incomplete；`git diff --check`通過。第一次browser run暴露索引未重建，依正式流程重建後重跑成功。
- 狀態：題源帳本當前唯讀重核為10,566/10,566、pending 0；來源目錄489 entries／278 URLs全覆蓋、23,131 refs／0 flagged。全庫publisher evidence為285/3,081 verified、2,796 pending、932 units blocked，不能把題源帳本完成當作出版社融合完成。官方課綱的S-9-1與S-9-2分層，本lesson仍含部分S-9-2內容，範圍審核未完成；publisher slots pending、lesson `draft`、spec QA未升級。未派子任務、未重寫A-7-2、未commit/push。詳見`implementation/reports/math-s-9-1-visible-fusion-d345.json`。
# D-345：S-9-1 既有融合正文與學生實際可見欄位一致化（2026-09-28）

- 決策：S-9-1 的六段原創課文、例題推導、迷思、遷移與自我檢核，以及四階選擇互動早已存在於 `teaching.body` 和 `interactive.steps`；網站卻以 `content.sections` 呈現三句短綱要。保留原有教學內容，不重寫；將六段標題與正文接至網站實際讀取欄位，新增回歸測試防止教材只在後台欄位而學生看不到。
- 教學校正：把充分條件限定為三角形，避免將三角形判定條件錯誤泛化至任意多邊形；將三版本章節證據明確標成公校課程計畫，移除把均一公開課程節點寫成南一版本差異的含混說法。校方課程計畫只支撐章節／教學方向，不代表完整出版社正文已讀。
- 規格：原 spec 宣稱存在 `GeometryManipulationBlock`、滑桿及多表徵同步操作，與當前四題單選不符。修成已註冊的 `StepwiseReasoningBlock`／四階選擇流程，逐項鎖定配對、判定、面積倍率、反例、錯答回饋與實際數值驗算。三家出版社證據仍 pending，lesson 維持 draft；本次不升級內容審查或發布狀態。
- 報告：`implementation/reports/math-s-9-1-visible-fusion-d345.json`；全庫測試及瀏覽器證據各按實際範圍記錄，不將自動化測試冒充教材內容審查或出版社審定。
## D-354：英文 Ac-Ⅳ-1 六段已寫教材未顯示於學生頁（2026-09-28）

- 缺口：`site/app.js` 的 `lessonDetail()` 僅呈現 `content.sections`；lesson 已有六段單元原創教學位於 `teaching.body`，但 `content.sections` 只有目標和短導讀，故主要課文未被學生看到。
- 修正：將六段既有標題與正文逐字同步至 `content.sections`；不重寫、不增加套版文字。新增 `sign-reading-lab.test.mjs` 斷言六段逐一顯示且正文與作者稿完全一致，並鎖定 `reviewStatus=draft`，避免來源／內容 gate 未完成時越級。
- 驗證：專項 SignReadingLab regression、lesson Schema、`npm test`（含 workbench 1,027/1,027）、資料驗證14,475 JSON／13,112 IDs／1,032 KG、spec 1,027／0 errors／1,027 pending、strict independence 614／0／0、`build_site_index.py --revision local`（1,052 lessons／10,566 questions／40 mappings）、授權Chromium全站1,027/1,027及AC-IV-1六段可見回歸、axe 48 runs／0 violations／6 incomplete、`git diff --check`通過。Python Playwright 1.58.0及Chromium執行檔已核實；sandbox curl 受限但授權環境正式URL回HTTP 200，無須安裝或重debug。
- 完成界線：這是讓既有內容真正出現在學習者頁面，不等同新增出版社全文閱讀或完成版本融合。三個 publisher evidence slots 仍 pending、lesson draft、spec QA untested；題源帳本仍沿用 10,566/10,566、pending 0；未派子任務、未提交推送。
## D-355：科學 Fb-Ⅳ-4 範圍優先於版本延伸材料（2026-09-28）

- 衝突：官方自然科課綱 Fb-Ⅳ-4 的學習說明是以日、月、地相對位置解釋月相盈虧規律，且明定「不涉及月亮升落時間和方位問題」（NAER PDF 正文 p.153／PDF p.156）。現 lesson 教學目標、例子及互動把升起時刻、月曆日期和月食條件當成核心；第6題考逐夜天空位移，第9題考月食條件，與本單元焦點不一致。Nani 網域公開的 108 試題解析 PDF p.12 將月相和東升時刻連問，且出處標到另一單元「依據天體運行制訂曆法」；它是公開試題解析材料，不是 Fb-Ⅳ-4 教科書全文，不能凌駕課綱範圍。
- 決策：Fb-Ⅳ-4 僅教月球反射太陽光、恆受照半球、日月地相對位置改變、地球所見亮面比例以及月相週期規律。升落時間／方位與月食條件不得列為本單元核心目標、互動或題目；月食所需條件屬相鄰內容，不以「迷思補充」之名塞入此課。南一公開試題材料只用來標示跨單元題型邊界；康軒模擬活動與翰林四位置表徵僅按其公開資源／公校採用版本課程計畫記錄，不能冒稱已讀三家完整課本。
- 執行結果（2026-09-28）：六段 `content.sections` 學生可見正文保留四位置幾何課程，明確改正新月／滿月相對位置描述；`studyHighlights`、lesson summary、interactive 四步與 simulation 四步改為固定光源—移動月球—觀察可見亮面的推理，不再把升落時間、方位、農曆日期或月食條件當學習目標。第6題改成控制變因的模型實驗設計，第9題改成無比例尺示意圖的推論限制，兩題答案、解析、策略及五步詳解皆重寫；逐題掃讀其餘八題時又抓到第8題答案鍵 D 與解法最後一步 B 不一致，已修正末步為 D 並加入 regression；新增 `science-fb-iv-4-substantive-fusion.test.mjs` 鎖定六段正文 parity、範圍、來源誠實標示、互動及第6／8／9題答案。
- 版本證據修正：南一網域 PDF 僅記作公開命題解析／跨單元線索；康軒 XML 僅記作官方資源標題索引；翰林公開特色頁保留四錨點定位；publisherResearch 將公校課程計畫標成校方編寫，並更正康軒來源及南一九年級大有國中課程計畫。沒有取得三家完整課本章節，publisher slots 維持 pending、lesson 與題目 draft、spec `qaStatus=untested`；本次完成的是有範圍約束及可追溯來源差異的原創融合草稿，不宣稱出版社全文融合 gate 已完成。
- 驗證：專項 regression（六段 parity、四步互動、十題正解與末步相符、來源至少有指標）通過；`npm test` 通過；`validate_data.py` 通過 14,476 JSON／13,112 IDs／1,032 KG nodes；全規格 1,027／0 errors／1,027 pending；strict independence 614篇／0 risk／0 affected／0 failure；索引 1,052 lessons／10,526 question paths／40 mappings；授權 Chromium 全站 1,027/1,027、320／375／768px、鍵盤／accessibility tree／reduced-motion 通過；axe 48 runs／0 violations／6 incomplete；直接學生頁檢查六段可見、四步互動、0 page errors；YAML／JSON 解析及 scoped `git diff --check` 通過。舊 question first-pass reviewer 要求每題三筆 examPatternRefs，而本單元每題目前僅一筆，因此來源內容審查仍未通過；不是題目已完成的證據。題源 ledger 沿用 10,566/10,566、pending 0，不重跑；A-7-2 未改；未派子任務、未 commit／push。
# D-360（2026-09-28）Da-Ⅳ-1 版本材料分級與學生可見正文

- 依 `site/app.js` 的 `lessonDetail()`，學生頁只渲染 `content.sections`，不會自動顯示 `teaching.body`。Da-Ⅳ-1 已有六段獨立原創教學，故將其逐段對齊至 `content.sections`，以回歸測試鎖定標題與正文完全一致；不重寫已存在的教材。
- 本輪讀到的來源深度不一：南一111版標示第三方公開翻頁樣本可讀印刷p.31細胞形態／功能與顯微觀察流程；康軒官方資源頁只能確認1上1-2動植物細胞觀察圖卡索引；翰林官方資源索引列出1上2-2細胞觀察，另有翰林版標示公開搜尋節錄可辨習作觀察記錄欄。索引不得充作教材全文，第三方標示樣本不得推定權利已授權。
- 因尚未取得三家完整單元正文並完成來源／權利及獨立內容審查，manifest publisher slots 維持原 pending/book-level-only，lesson 維持 `draft`。本決策不構成版本融合完成或發布審定。
- 證據與回歸：`implementation/reports/science-da-iv-1-source-fusion-visibility-d360.json`、`implementation/runtime/science-da-iv-1-visible-fusion.test.mjs`。

# D-369（2026-09-28）保留既有教學原稿並修復學生頁接線與規格對實作落差

- 先盤點現有 `teaching.body`、`content.sections` 與互動，不以兩欄文字不完全相同作為重寫依據。學生頁同時保留未重複的原稿段落；同標題內容以較完整 `teaching.body` 優先，避免短摘要覆蓋正文，也不丟棄只有 `content.sections` 才有的學習目標或導讀。
- Ab-Ⅳ-1 目前實際互動是 GuidedChoiceBlock（三題單選、即時文字回饋），因此規格不可再宣稱已存在預測鎖、滑桿、同步圖表或拖放；只可按真實資料契約描述鍵盤選答、錯誤提示及正確回饋。另題幹／回饋須使用同一步實際出現的線索，不可引用不存在的「洽詢／總務處／失物」。
- 公校課程計畫的出版社標示可以支持版本章節定位、教學及評量方向，但不等同出版社課本正文樣本或完整三版本實質融合；規格需明確保留此證據界線。 lesson 未完成來源深度、內容與 Terra 審查前維持 `draft`、qaStatus `untested`。
- 回歸涵蓋原稿段落接線、實際互動題幹／回饋、鍵盤正誤操作與窄螢幕。不得因本次接線修復而批次重寫其他 lesson；後續先做 mismatch inventory，再逐項針對已證明缺口修正。
- 驗證記錄：`implementation/reports/existing-lesson-authoring-inventory-d366.json`（結構盤點，非內容通過判斷）、`scripts/browser_smoke_test.py`（授權系統 Chrome 全站及 Ab-Ⅳ-1 回歸）。

# D-370（2026-09-28）規格 bundle、renderer 與 archetype 必須同步覆蓋全部元件

- YAML 單元規格是來源；工作台讀取 `unit-specs.bundle.json`，元件必須同時存在 `component-registry.json`、runtime `renderer-registry.js`，且各自只歸屬一個 archetype。只通過 YAML Schema 不足以證明工作台能載入／呈現。
- Ab-Ⅳ-1 的學生互動是真實三步 GuidedChoiceBlock，因此同步 YAML 與 bundle；給文字化 renderer 加入 GuidedChoiceBlock。另把兩個已被規格使用、但 renderer 缺失的數學元件 AlgebraEquationMeaningBlock、EquivalentExpressionCheckBlock 加入對應的語意模型。新增 archetype 路由以涵蓋這些元件與既有英語敘事／溝通元件，且按規格實際使用學科限制適用 subject。
- 對全庫 28 種元件建立 renderer-registry 與 component-registry 的集合相等回歸；1,027 個 bundle spec 必須完整走訪。這只證明結構可渲染，不代表各課內容、出版者來源、真實互動或教學 QA 通過。
- `validate_interactive_simulations.py` 的 155 個 stale 結果經實際資料分類均有 simulation，0 個為 missing；錯誤是現有單元專屬 engine 與通用 `simulation_for()` 推導不同，故禁止批次覆蓋。逐課需以現有 interaction、simulation 設計、單元回歸及瀏覽器行為判斷，不把 validator 的 generic expected contract 當成正解。
- 驗證：archetype 7 組／28 元件／1,027 specs／0 error；workbench bundle traversal 1,027/1,027；`npm test` 通過；系統 Chrome 全站 1,027/1,027 與 Ab-Ⅳ-1 專項通過。所有 lesson 與 spec 仍維持既有 draft／QA 狀態。
# D-371：既有 lesson 學生頁接線及出版社來源交叉盤點（2026-09-28）

- 核對學生目錄是依精確 KG 配對 lesson；常用字形音義的兩篇既有 lesson 均匹配 `kg-chinese-content-ab-iv-1`，因此已接線，現況是同一單元顯示兩篇不同教材，不應誤當缺頁後再重寫或刪除。
- 修正 `lesson-chinese-common-character-form-sound-meaning` 南一 publisherResearch 與 evidence sample 中錯指嘉義永慶高中非國文課程計畫的來源；改為嘉義縣大林國中南一版國文 Ab-Ⅳ-1 公開課程計畫。核對來源：[嘉義縣大林國中九年級國文教學計畫](https://course.cyc.edu.tw/upfile/course110/sub1/14793292177358929.pdf)，PDF 第 1 頁列南一版國中國文，第 1 頁課程項目列 Ab-Ⅳ-1 常用字形音義。課程計畫只支持教材版本／課程定位，不代表讀過南一課本全文或完成三版實質融合。
- 全庫唯讀掃描發現 96 個 lesson publisherResearch URL 與 publisher chapter sample URL 有差異，另有 24 組同 KG 對應多篇 lesson。這些差異可能是樣本帳本的後續來源補充，不能僅因 URL 不同判為錯誤；需逐筆核對來源定位、時間及內容，再決定同步，禁止批量複製覆寫。KG 多篇也不等於重複，應逐篇比較正文及學生頁呈現。
- 既有 interaction materialization 報告列出 18 篇無 curriculum unit spec 的補充 lesson；抽查其欄位皆已有六段教學與三步 guided-choice。這些不在 1,027 個 curriculum-unit spec 的覆蓋集內，暫不為湊數新增 spec；如產品要把補充 lesson 納入規格驗收，需另建明確範圍與測試清單。
- 保留所有既有 lesson 正文，不動題庫及互動；未重跑已完成題源帳本，lesson 維持 draft。來源核對只完成上述單筆修正，其餘差異屬待查，不冒稱全庫來源同步完成。
# D-372：Ab-Ⅳ-1 已有教材來源重查，不重寫正文（2026-09-28）

- 先保留已存在的 3,370 字教學正文及三步原創互動，不因 versionResearch 記載較弱而重寫內容。
- 南一證據補入第三方 FlipHTML5 的 111 國文資源簡介本頁面（可見頁面印刷 p.7–8）：僅支持其形音義整理格式和詞語例證；上傳者、完整版本真實性、授權均未核實。康軒補入官方按課次「瞄準形音義」索引及 114 數位特色頁；證據只及資源類型、配對練習與即時回饋，未讀取所有遊戲或教材內文。翰林補入出版社網域國中國文四先行本 PDF p.2／p.5 的單課學習目標與形音義欄位；它是特定課次補充講義，不能代表全版本。
- 修正 versionResearch 中把專案原創活動、迷思和評量歸因出版社的表述，將可見事實、教學推論及原創擴充分開；新增 source references。正文沒有因此重寫。
- 進一步發現既有 `fusionRecord` 仍引用舊的、無法由所列來源支持的「康軒朗讀校對」「翰林閱讀表達」差異。已按實際來源重寫 commonCore/versionDifferences/originalAdditions/synthesis note，明確區分南一樣頁、康軒互動索引與翰林特定課講義，並記錄教材原有六段和三步互動已實現整合，不把完整三版書章核讀冒稱完成。
- 這是來源知情、保留原稿的 fusion research update，不等於三版完整課本內容比較、出版社授權判定、publisher evidence verified 或 AI lesson content-reviewed。lesson 維持 draft；題源帳本不重跑。
## D-379：Ac-Ⅳ-3 保留既有融合正文，修復學生頁接線並校正互動規格（2026-09-28）

- 盤點結論：lesson 原有六段完整、單元專屬教學正文；問題是 `content.sections` 只有兩段短摘要，使學生頁未呈現原稿。逐段將既有 `teaching.body` 接回學生內容欄，未重寫或丟棄原稿。
- 互動：將通用占位題修正為三題本課資料推論選答，分別檢查觀察與猜測、有限比較與因果、問卷樣本與全體推論；每題均有唯一答案、說明與 retryHint。規格同步改為實際 GuidedChoice runtime，不宣稱不存在的 TextEvidence、滑桿、同步圖表或外部 fallback。
- 證據更正：舊 publisherResearch 將公校課程計畫誤當出版社內容證據；南一／康軒／翰林三 slots 一律回到 pending。公開縣市學力檢測報告只支持其可見的教學建議，不替代出版社正文。正文是課綱、KG、公開教學建議之上的原創草稿；不得稱三版實質融合，lesson 維持 draft。此更正優先於舊帳本紀錄。
- 驗證：回歸測試、YAML parse、資料驗證 14,491 JSON／13,113 IDs／1,032 KG、unit specs 1,027／0 errors／1,027 QA pending、publisher ledger 290／3,081 verified、2,791 pending、934 blocked、`npm run pretest`、專項 Python Playwright 均通過。瀏覽器確認六段呈現、三題選答、錯答及鍵盤重試、因果／範圍回饋、320／375／768px 無溢位、page errors 0。sandbox 綁定 localhost 原始錯誤 `PermissionError: [Errno 1] Operation not permitted`；在授權執行環境既有 server 回應 200 並完成 Playwright；未安裝套件。全站 browser smoke 未重跑。題源帳本沿用 D-377 10,566／10,566，無題目修改或重複稽核；未 commit/push、未派子任務。
- 詳報：`implementation/reports/chinese-content-ac-iv-3-existing-fusion-wiring-d379.json`。
## D-395：移除 Codex lesson 內容審查 gate（2026-09-28）

- 依使用者明確指示，lesson 融合教材最終審查由使用者交 ChatGPT；Codex 不執行內容審查／Terra 複核，也不等待此審查才登記融合撰寫完成。
- 融合撰寫進度的唯一名冊依據仍為 `scripts/inventory_authored_fusion_drafts.py`：至少六段 `teaching.body` 且 `fusionRecord.llmSynthesisNote` 非空。lesson `draft`、publisher evidence、spec QA、獨立性自動診斷是獨立紀錄，不是名冊 gate；不因這些狀態重寫或扣除已登記稿件。
- 本次盤點：729／791（92.16%）；learning-content 583／583、learning-performance 146／208；長文標記559僅為另一項字數統計。未重寫既有稿件、未執行教材審查、未動題庫；本次只澄清規則。
# D-398（2026-09-28）：英文 6-Ⅳ-1 來源誤標校正、缺稿補寫與真實互動規格

- 盤點確認該 lesson 的六段是泛用占位、沒有 fusionRecord 或互動，故不屬已登記融合稿；本次只補此缺稿，不重寫既有名冊項目或題庫。
- 舊來源核查發現南一標示 PDF 為音樂課程計畫、康軒標示 PDF 為國文課程計畫、翰林標示來源無法定位英語／6-Ⅳ-1；以上錯誤歸因已撤除。以三份可直接閱讀、定位到年級／科目／頁碼的版本標示公校計畫替換，並清楚限定為校方課程計畫，不冒稱出版社章節或教法；出版社課本章節證據仍 pending。
- 依官方英語課綱 PDF p.15 將本課界定為學習興趣與態度：參與、不畏犯錯，不是文法內容或發言量評分。完成六段單元專屬正文、四步原創 GuidedChoice；以嘗試、定位卡點、使用提示／求助、依回饋再試作為教學主線。lesson 保持 draft，最終教材審查由使用者 ChatGPT 執行。
- Implementation spec 移除不存在的 LanguageTimelineBlock、預測／滑桿／同步圖表等假契約，改為頁面實際 GuidedChoice、aria-pressed／文字回饋及靜態文字循環。
- 驗證：lesson／spec 專項、資料 14,509 JSON／13,114 IDs／1,032 KG、spec 1,027／0 errors（10 eligible、1,017 pending）、完整 `npm test`、工作台 1,027／1,027、授權 Playwright（6 段、4 步、鍵盤重試、axe 0 violations、320／375／768 無溢位）通過。名冊 732／791＝92.54%，只表示稿件存在。題源帳本沿用 D-397 10,566／10,566、pending 0；本輪未修改題目。
- 詳報：`implementation/reports/english-performance-6-iv-1-fusion-d398.json`。未派子任務，未 commit/push。
# D-450：社會社2a-Ⅳ-3補登原創融合稿（2026-09-29）

- 僅補名冊缺稿 `lesson-social-performance-soc-2a-iv-3`，保留既有登錄稿及題庫。六段原創教材以校園文化展板被編輯概括引出問題，教學生辨認文化發展與交流、文化內部差異、語言／制度位階、來源代表範圍、當事人同意與可修正詮釋；全部情境自編，學生頁／教學稿6/6逐段同步。新增versionResearch與fusionRecord，維持draft供使用者ChatGPT審查，審查非名冊gate。
- 來源：南一標示第三方分享文件其實是教師自編師大公民教案，不是出版社課本；翰林標示東榮國中8下課程計畫是校方版本安排；康軒官方7下公民頁可見課次標題、跨科SEL文章可見文化脈絡分析法，但影片全片未讀。逐筆標示來源類型與範圍，未宣稱讀完未取得的三家原書。
- 名冊刷新778/791＝98.36%（learning-content 583/583；learning-performance 195/208；尚缺13；長文標記608）。目標Schema及全庫資料驗證PASS（14,558 JSON／13,114 IDs／1,032 KG）。題庫未改；沿用本目標回合已核10,566/10,566、pending 0。互動spec、非真人自動測試、commit/push尚待。詳報`implementation/reports/social-performance-soc-2a-iv-3-fusion-d450.json`。

# D-449：社會社2a-Ⅳ-2補登原創融合稿（2026-09-29）

- 只補名冊缺稿 `lesson-social-performance-soc-2a-iv-2`；不覆寫已登錄稿或題庫。原創六段教材以老市場改善議題教時間／空間／制度脈絡、權責、群體內差異、證據範圍、參與與追蹤修正；情境明示為虛構，`content.sections`與`teaching.body`逐段一致6/6。補三筆來源研究和fusionRecord，維持draft供使用者ChatGPT審查，內容審查非名冊gate。
- 來源限制逐筆註明：翰林標示之民生國中計畫提供地方政府脈絡；南一標示永慶高中歷史計畫只作地方史探究旁證；屏東跨科計畫未能核實版本，僅作弱脈絡、不歸因康軒。均非出版社原書，不宣稱已直接比讀三家完整教材。
- 名冊實測777/791＝98.23%（learning-content 583/583；learning-performance 194/208；剩14；長文標記607）。lesson schema、全庫資料驗證及正文配對通過。題源帳本本目標回合已重核10,566/10,566、pending 0，其他三項語義／目錄／學段稽核亦PASS；題目未改。規格互動QA與commit/push尚待。詳報`implementation/reports/social-performance-soc-2a-iv-2-fusion-d449.json`。

# D-448：社會社2a-Ⅳ-1補登原創融合稿（2026-09-29）

- 只處理名冊下一篇缺稿 `lesson-social-performance-soc-2a-iv-1`，不重寫既有登錄稿或題庫。以官方社2a-Ⅳ-1與KG為課程依據，寫成流域、水文、工程／制度和地方社會彼此作用的六段原創教學；學生頁及`teaching.body`逐段同步6/6，補齊版本研究與fusionRecord。維持`draft`供使用者ChatGPT最終審查；依D-395，內容審查不是融合撰寫登記gate。
- 來源分級：翰林標示的第三方水文課本分享版次／授權未核；南一標示桃園國中課程計畫、康軒標示之馬公國中教師教案均為校方材料，不冒稱出版社原書或出版社教法。只融合可讀到的概念與活動角度，不複製原文／題目。
- 名冊刷新776/791＝98.10%（learning-content 583/583；learning-performance 193/208；剩15；長文標記606）。`validate_data.py` PASS（14,556 JSON／13,114 IDs／1,032 KG）；目標正文配對與lesson diff check PASS。題庫未改，沿用D-422帳本10,566/10,566、pending 0。互動規格/browser QA、commit/push尚待。詳報`implementation/reports/social-performance-soc-2a-iv-1-fusion-d448.json`。

# D-447：社會社1c-Ⅳ-1補登原創融合稿與來源層級校正（2026-09-29）

- 最新融合名冊確認 `lesson-social-performance-soc-1c-iv-1` 尚未登錄；原正文僅泛用占位，故只修改此課，不覆寫任何已登錄lesson或題庫。依官方課綱代碼與KG，以公平貿易／可可供應鏈原創案例撰寫完整六段，區分描述、因果、價值及政策主張，教證據適配、來源限制、多方觀點及可修正結論；四筆學生資料卡明示為虛構，不偽裝成真實統計。`content.sections`與`teaching.body`標題／正文6/6一致。
- 來源層級校正：翰林版標示九上地理課本第三方公開分享可讀pp.20–31；上傳授權、版本真偽與全文完整性未核。南一版標示丹鳳高中計畫及列康軒課本為教材資源的三民國中校訂計畫均為校方安排，不是出版社原書。每筆出版社標籤僅表示分享材料所標版本／校方採用版本，不歸因出版社；定位、概念發現、授權邊界登錄於`versionResearch`及`publisherResearch`。沒有把校方課程計畫冒充出版社教學法，也不宣稱已直接核讀三家原書。
- 名冊實測775/791＝97.98%（learning-content 583/583；learning-performance 192/208；尚缺16；長文標記605）。`reviewStatus`維持`draft`，ChatGPT最終教材審查由使用者負責。題目檔未修改，沿用D-422／D-377最近題源帳本10,566/10,566、pending 0；全庫資料驗證、此課互動規格／瀏覽器測試及commit/push尚待執行。機器可讀報告：`implementation/reports/social-performance-soc-1c-iv-1-fusion-d447.json`。
## D-452：補登社會社2b-Ⅳ-2融合稿並校正三版來源層級（2026-09-29）

- 新鮮融合稿名冊確認 `lesson-social-performance-soc-2b-iv-2` 未登錄；原學生頁僅四段通用摘要，六段 teaching.body 為套版，故只處理此缺稿，不重寫已列名稿、不動題庫。
- 依官方社2b-Ⅳ-2／KG，核讀南一標示的公開第三方教師設計（文化差異、位階與不平等；上傳／授權未核）、康軒版第二冊採用之公校特教調整課程（多元族群、尊重包容、多媒材與分解目標；非出版社教法原貌）、翰林7下採用之民和國中公民課程計畫（文化定義、特徵、多樣性、主流／次文化與討論）。桃園公校跨域服飾文化設計只作補充方法線索，非三版本證據。各筆明列可支持範圍，不宣稱讀畢三家出版社原書。
- 原創重寫六段：由文化展板的過度概括切入，說明文化的動態與脈絡；區分差異描述、價值排序及制度效果；以四張虛構資料卡練代表性與證據範圍；把知情同意、署名／匿名、撤回與公開前確認落實到策展流程，再遷移至校園午餐文化週。學生頁與 teaching.body 標題／正文同步6/6，新增三家 versionResearch、publisherResearch 與 fusionRecord；`reviewStatus=draft`，最終內容審查交使用者 ChatGPT。
- 名冊更新780/791（98.61%）：learning-content 583/583、learning-performance 197/208、尚缺11；長文標記610。全 lesson schema audit 1,056/0 failures，`validate_data.py` 14,560 JSON／13,114 IDs／1,032 KG 通過。題庫未改，沿用近期公校題源帳本10,566/10,566、pending 0。互動規格、自動化QA及commit/push仍待後續階段；詳報 `implementation/reports/social-performance-soc-2b-iv-2-fusion-d452.json`。

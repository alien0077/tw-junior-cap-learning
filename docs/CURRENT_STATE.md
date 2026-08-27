# 目前狀態

> 2026-08-27：已依國家教育研究院公開五科課綱完成 915 個 batch drafts 的原創重寫與 web-source-comparison。910 個可教學 lesson／9,100 題已升級為 `content-reviewed`；5 個官方分類／根節點及其 50 題改為 `deprecated`、未刪除。每筆升級資料均記錄官方 URL、代碼定位與查核日期；全庫 validator 已通過（13,112 JSON、12,885 IDs、1,032 KG nodes）。M5 已改用完整、固定 revision 的資料索引；本機瀏覽器已驗證五科篩選、搜尋及教材連同 10 題的延遲載入。詳見 `docs/M4_WEB_SOURCE_AUDIT_2026-08-27.md` 與 `docs/M3_M4_COMPLETION_EVIDENCE_2026-08-27.md`。

- 更新日期：2026-08-27
- 目前里程碑：M5 — 靜態學習 MVP 與部署驗收
- 狀態：M3 公開可追溯對照、M4 教材／題庫與 canonical navigation、M5 固定版本資料索引與遠端 Pages 驗收均已完成

## 已完成

- M2：完成五科第四學習階段官方「學習表現／學習內容」表格逐碼建模，來源、穩定 ID 與圖譜端點均有明確驗證規則。
- M2 資料規模：1032 個 curriculum documents、1032 個 Knowledge Graph nodes、1046 條 edges；其中 1027 條 `partOf`、19 條自然科官方跨科表直接支持的 `relatedTo`。
- M3 整冊基線：建立南一、康軒、翰林六冊整冊存在性 mapping；一般冊別以國家教育研究院 115 學年度教科用書清冊為證據，翰林英語另以翰林官方書城 `i英語` 商品資料為證據並保留與審定出版者「佳音」的差異註記。
- M3 康軒章節級 mapping：完成五科各六冊，共 30 冊、310 個官方章節／單元條目對既有 KG ID 的保守對照。
- M3 翰林國文章節級 mapping：完成六冊、82 個官方課次對既有 KG ID 的保守對照；六冊課次均取自標示 115 年的翰林組織網域公開索引。
- M4 資料管線基線：五科各一份原創 lesson、各十題原創 question（共 100 題），全部連至穩定 KG ID；10 份 lesson 均含學霸筆記重點與來源，數學／自然 4 份含互動教學。

## 尚未完成

- M3／M4：目前沒有阻擋完成的項目；版本資料來源與 `content-reviewed` 的證據界線仍須依既有決策維持。
- M5：沒有阻擋完成的項目；Pages 已由 commit `14fd8a81422b` 部署，公開頁面已讀取同一固定 revision 的完整資料索引。

## 工作限制

M3 依 D-070 的公開可追溯證據門檻已完成。部分冊別的來源仍是校方課程計畫或教育平台，故章節名稱來源與 KG 對照判斷必須分層記錄，不能把本專案的 `medium` confidence 對照說成出版社背書。

2026-08-26 新增翰林數學六冊官方章節 mapping、翰林社會六冊官方目次 metadata；後者維持領域層級 KG 對照與待核驗註記。

2026-08-26 新增翰林英文七上至八下官方單元 metadata（25 筆）；來源為 112 年官方改版簡介，保留版本差異註記。

2026-08-26 新增翰林自然七下校方課程計畫交叉 mapping（19 筆）；保留 medium confidence 與非出版社正式目次註記。

2026-08-26 新增南一自然八上／八下校方課程計畫交叉 mapping（12 筆）；保留 medium confidence 與非出版社正式目次註記。另補上翰林自然九年級 8 章校方交叉證據。

2026-08-26 新增南一英文七上校方課程計畫交叉 mapping（8 筆）；保留 medium confidence 與版本年代註記。

2026-08-26 新增南一社會七下校方課程計畫交叉 mapping（地理、歷史、公民各 6 單元，共 18 筆）；來源為永豐高中國中部公開改選報告，保留 medium confidence 與 109 學年度版本註記。

2026-08-26 新增南一社會八上校方課程計畫交叉 mapping（地理、歷史、公民各 6 單元，共 18 筆）；來源為卓蘭高中附設國中部公開課程計畫，保留 medium confidence 與 111 學年度版本註記。

2026-08-26 新增南一社會九年級第 5、6 冊校方課程計畫交叉 mapping（第 5 冊 18 單元、第 6 冊 12 單元，共 30 筆）；來源為民和國中 113 學年度公開計畫，文件標示設計者為南一出版社，保留 medium confidence。

2026-08-26 新增南一社會第一、二冊校方課程計畫交叉 mapping（七上、七下各 18 單元，共 36 筆）；來源為永慶高中 114 學年度公開計畫，保留 medium confidence。

2026-08-26 新增南一版英文第三至六冊 115 學年度校方課程計畫逐課 mapping（八年級 12 課、九年級 10 課）；來源為嘉義縣大吉國中公開附件，保留 medium confidence。

2026-08-26 新增南一版數學第五、六冊 115 學年度校方課程計畫章節 mapping（6 章），以及自然第一、二冊章節 mapping（10 章）；來源為嘉義縣大吉國中公開附件，保留 medium confidence。

2026-08-26 新增南一版社會第四冊八年級下學期地理、歷史、公民各 6 單元（18 筆）；來源為卓蘭高中附設國中部 113 學年度公開課程計畫，保留 medium confidence。

2026-08-26 新增翰林版英文第五、六冊學校課程計畫逐單元 mapping（第五冊 6 單元、六冊 4 單元，共 10 筆）；來源為嘉義縣忠和國中 111 學年度公開 PDF，保留 medium confidence 與學年度差異註記。

2026-08-26 新增翰林版自然八年級下學期（第四冊）學校課程計畫章節 mapping（6 章）；來源為新北市立明志國中 11102 公開附件，保留 medium confidence 與學年度差異註記。

2026-08-26 新增翰林版自然七年級上學期（第一冊）學校課程計畫章節 mapping（6 章）；來源為嘉義縣東榮國中 110 學年度公開 PDF，保留 medium confidence 與學年度差異註記。

2026-08-26 新增翰林版自然八年級上學期（第三冊）學校課程計畫章節 mapping（4 章）；來源為嘉義縣永慶高中國中部 109 學年度公開 PDF，保留 medium confidence 與學年度差異註記。

2026-08-26 新增南一版自然九年級第五、六冊學校課程計畫章節 mapping（各 4 章，共 8 章）；來源為嘉義縣東石國中 114 學年度公開 PDF，保留 medium confidence。

2026-08-26 新增南一版英文七年級下冊（第二冊）學校課程計畫逐課 mapping（6 課）；來源為同濟高中附設國中 109 學年度公開 PDF，保留 medium confidence 與學年度差異註記。

2026-08-26 新增南一版數學第一至四冊均一「類南一版」章節結構 mapping（18 章）；來源為均一教育平台公開索引，明示依南一版章節架構編排，保留 medium confidence 與非出版社正式目次註記。

2026-08-26 新增南一版國文第一冊校方課程架構 mapping（10 課與 2 篇自學，共 12 筆）；來源為屏東縣公開課程計畫，保留 medium confidence 與 PDF 擷取限制註記。

2026-08-26 新增南一版國文第四冊校方課程計畫逐課 mapping（10 課）；來源為卓蘭高中附設國中 112 學年度公開 PDF，保留 medium confidence。

2026-08-26 新增南一版國文第六冊校方課程計畫逐課 mapping（8 課）；來源為大林國中 110 學年度公開 PDF，保留 medium confidence 與第三課標題擷取限制註記。

## 下一個工作單位

後續維護時，仍須以新的固定 commit 重跑索引、資料驗證與公開頁面 smoke test；翰林英語產品體系與國教院清冊的審定出版者資料仍須持續分開紀錄。

## Blocker 紀錄

目前未完成的官方目次來源與下一步嘗試已記錄於 `docs/BLOCKERS.md`。這些 blocker 不代表資料不存在，只代表目前尚未取得可直接核驗的公開章節定位；在解開前不把冊別存在性 baseline 升級成章節 mapping。

- M4 原創內容：目前 1,036 份 lesson、10,360 題 question，均標示 `origin=original` 並連至既有 KG ID；lesson 狀態為 1,031 `content-reviewed`、5 `deprecated`，question 狀態為 10,310 `content-reviewed`、50 `deprecated`，仍不宣稱外部教師審閱完成。

- M5 MVP：`site/` 透過 `data-manifest.json` 與 GitHub raw JSON 載入 project state、lesson、question，提供五科篩選與搜尋；`netlify.toml` 已提供靜態部署設定。
- M5 CI：新增 GitHub Actions data-validation workflow，驗證 JSON、Schema、ID uniqueness、KG endpoints 與原創內容 provenance；目前尚待取得實際 workflow run 結果。
- M5：GitHub Pages workflow run 32935192763 成功；公開 URL 與 HTTP smoke test 已驗證。

- M4 方法文件：已補上參考資料層級、原創編寫流程、答案格式、審核界線、外部資料授權規則與學霸筆記重點整合規則。

- M4 題數門檻：question 以 lessonId 歸屬單元，CI 將檢查每個 lesson 至少 10 題。
\n- M4 學霸筆記整合：docs/M4_STUDY_NOTE_HIGHLIGHTS.md；所有 lesson 已加入 highlights/references，數學與自然每單元提供互動步驟。\n

## M4 進度更新

### 目前權威快照（2026-08-26）

- coverage rows：1,032（`content-reviewed` 1,027、`deprecated` 5）。
- lessons：1,036（`content-reviewed` 1,031、`deprecated` 5）。
- questions：10,360（`content-reviewed` 10,310、`deprecated` 50）。
- canonical units：數學 7、國文 16、英文 12、自然 49、社會 77；中英文 domain 為分類節點，國文 Ab／英文 Ae 已有 child candidates。
- 最新本地 validator：13,112 JSON、12,885 IDs、1,032 KG nodes，通過。
- 上述 `content-reviewed` 僅代表 repo 內部 QA，不代表教師／學科專家審閱。

- 2026-08-26：M4 全量結構建立完成；coverage matrix 1,032/1,032 rows 均有 lesson，最新狀態為 92 `content-reviewed`、940 `draft`；最新 validator 通過 12,571 JSON files、12,558 IDs、1,032 KG nodes。此狀態不等同 `teacher-reviewed`。
- 上述全量結構行為歷史批次紀錄；目前狀態以本文件「目前權威快照」為準：coverage `content-reviewed` 117／`draft` 915，lesson `content-reviewed` 121／`draft` 915，question `content-reviewed` 1,210／`draft` 9,150。

- M4-002 已完成：已建立 [data/m4-coverage-matrix.json](../data/m4-coverage-matrix.json)，逐一列出 1,032 筆 curriculum records；目前僅 7 筆有可直接對應的既有 lesson/question baseline。
- M4 批次進度：1,032/1,032 筆 coverage rows 已 materialize，共 1,036 份 lesson、10,360 題 question；數學／自然互動狀態 0 筆 pending；18 筆為 repo 內部 `content-reviewed`、1,014 筆維持 `draft`。
- M4 題庫審查狀態：1,210 題為 `content-reviewed`、9,150 題仍為 `draft`；此欄位與 coverage row／lesson 的內部 QA 狀態分開計算，未宣稱教師審閱完成。
- 2026-08-26：新增南一版國文第三冊校方課程計畫逐課 mapping（10 課）；來源為卓蘭高中附設國中 113 學年度公開 PDF，保留 medium confidence。
- 2026-08-26：新增南一版國文第二冊校方課程計畫逐課 mapping（8 課）；來源為彰化縣福興國中 110 學年度公開 PDF，保留 medium confidence。
- 2026-08-26：新增南一版國文第五冊校方課程計畫逐課 mapping（12 課）；來源為嘉義縣永慶高中國中部 109 學年度公開 PDF，保留 medium confidence。
- 2026-08-26：南一教材 mapping 累計 126 個 mapping、36 組 mapping set、882 筆章節／單元 entries；校方來源均保留 medium confidence，未升格為出版社正式目次。
- 2026-08-26：新增南一數學第一冊 3 章與第二冊 5 章校方課程計畫 mapping；南一教材 mapping 累計 128 個 mapping、38 組 mapping set、890 筆章節／單元 entries。
- 2026-08-26：新增南一數學第三冊 5 章與第四冊 4 章校方課程計畫 mapping；南一教材 mapping 累計 130 個 mapping、40 組 mapping set、899 筆章節／單元 entries。

- 2026-08-26：為 1,031 份可對應 curriculum/KG 的 lesson 補入其官方課綱文件精確 URL；此為 provenance 強化，不改變任何 lesson 的 draft／content-reviewed 狀態。
- 2026-08-26：建立 M4 三層資料架構數學試點：126 個數學課綱節點分入 7 個 draft canonical unit（6 個 teachable、1 個分類導航），mapping 全部標示 low confidence；既有 lesson/question 保持原狀。
- 2026-08-26：建立 `migrations/math-question-migration-pilot.json`，收錄 1,270 題數學題目的可逆遷移狀態；1,220 題 pending-review、50 題分類導航來源標示 not-applicable，未刪除任何原始題目。
- 2026-08-26：以官方 `parentId`／`learning-content` 建立國文、英文、自然、社會 draft migration：分別 12／9／49／77 個候選 units，題目 manifest 分別收錄 850／1,370／3,260／3,610 題；候選結果均待逐單元核對。
- 2026-08-26：套用來源核驗修正：中英文 domain 改為 classification-only；國文 Ab 新增 4 個 child units、英文 Ae 新增 3 個 child units；相關題目 manifest 已改指 child candidate，仍維持 pending-review。
- 2026-08-26：GitHub Actions `validate-data` run 32970160723 成功；遠端 validator 通過。唯一 annotation 為 actions/checkout@v4 與 setup-python@v5 的 Node.js 20 deprecation 警告，不影響驗證結果。
- 2026-08-26：CI 已升級至 actions/checkout@v5、actions/setup-python@v6；run 32970461258 成功，validator 通過且不再出現 Node.js 20 deprecation annotation。
- 2026-08-26：最新 migration handoff push 的 CI run 32970991080 成功，遠端 validator 再次通過。
- 2026-08-26：validator 新增數學／自然每 lesson 至少 3 步互動檢查；CI run 32971196186 成功。
- 2026-08-26：目前 canonical unit 共 161 個；五科 migration manifest 合計 4,060 題尚無唯一 target unit，已列入逐題外部核驗清單。
- 2026-08-26：以國教院官方 PDF 直接核對自然全球氣候跨科主題與社會公民 Aa grouping，更新為 official-curriculum／high evidence；未改變 lesson／question 的外部審閱狀態。
- 2026-08-26：以國教院英語文課綱 PDF viewer P18 核對 Aa–Ad 項目；Aa／Ab／Ad evidence 更新為 high，Ac 維持 medium（內容跨度較大）。
- 2026-08-26：以國教院數學領域課綱 PDF viewer P80–P81（附錄三 P74–P79）核對國中六大主題；數學六個 teachable canonical unit 與 mapping 更新為 official-curriculum／high。代數單元標題保留本專案教學標籤並在 locator 註明官方主題為代數（A）；navigation 分類節點仍為 draft。
- 2026-08-26：依 migration review action plan 修正 Ab-Ⅳ-8 書法欣賞 10 題：改指唯一 child canonical unit，狀態維持 pending-review；未解 migration 題數由 4,060 降為 4,050，validator 通過。
- 2026-08-26：依 KG leaf→canonical membership 產生 migration audit，並將 90 筆唯一 teachable target 套用至原 manifest（狀態維持 pending-review）；未解 migration 題數由 4,050 降為 3,960。其餘多候選／無候選維持 null，待外部語意核對。

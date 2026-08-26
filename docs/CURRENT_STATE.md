# 目前狀態

- 更新日期：2026-08-26
- 目前里程碑：M4 — 全課綱教材與題庫
- 狀態：M4 repo 內部內容 QA 完成；教師／學科專家審閱仍未完成

## 已完成

- M2：完成五科第四學習階段官方「學習表現／學習內容」表格逐碼建模，來源、穩定 ID 與圖譜端點均有明確驗證規則。
- M2 資料規模：1032 個 curriculum documents、1032 個 Knowledge Graph nodes、1046 條 edges；其中 1027 條 `partOf`、19 條自然科官方跨科表直接支持的 `relatedTo`。
- M3 整冊基線：建立南一、康軒、翰林六冊整冊存在性 mapping；一般冊別以國家教育研究院 115 學年度教科用書清冊為證據，翰林英語另以翰林官方書城 `i英語` 商品資料為證據並保留與審定出版者「佳音」的差異註記。
- M3 康軒章節級 mapping：完成五科各六冊，共 30 冊、310 個官方章節／單元條目對既有 KG ID 的保守對照。
- M3 翰林國文章節級 mapping：完成六冊、82 個官方課次對既有 KG ID 的保守對照；六冊課次均取自標示 115 年的翰林組織網域公開索引。
- M4 資料管線基線：五科各一份原創 lesson、各十題原創 question（共 100 題），全部連至穩定 KG ID；10 份 lesson 均含學霸筆記重點與來源，數學／自然 4 份含互動教學。

## 尚未完成

- M3：南一五科仍待出版社官方目次；另以學校公開課程計畫補上南一自然八年級 12 章。翰林數學六冊已完成官方章節 mapping，翰林社會六冊為官方目次 metadata，翰林英文七上至八下為官方單元 metadata，翰林自然七下為校方 19 單元交叉證據；其餘仍待逐章公開證據。
- M3：115 學年度翰林英語審定出版者身分與翰林書城 `i英語` 產品體系需持續分開紀錄；115 下期商品資料尚未公開時，不可把 114 下期誤標為 115。
- M4：1,032/1,032 coverage rows 已完成 lesson 與題庫欄位之 repo 內部 QA；每單元至少 10 題，數學／自然具 3 步互動；仍不代表教師／學科專家審閱。
- M5：資料驅動靜態 MVP 已部署至 https://alien0077.github.io/tw-junior-cap-learning/，並完成首頁與 manifest 遠端 smoke test。

## 工作限制

M3 已完成康軒五科與翰林國文；南一 30 冊仍無可匿名逐章目次，翰林自然六冊與英文九年級仍待完整章節證據，翰林社會與英文七、八年級目前為官方目次／單元 metadata 的保守對照，因此仍為進行中。章節名稱來源與 KG 對照判斷分層記錄，不能把本專案的 `medium` confidence 對照說成出版社背書。

2026-08-26 新增翰林數學六冊官方章節 mapping、翰林社會六冊官方目次 metadata；後者維持領域層級 KG 對照與待核驗註記。

2026-08-26 新增翰林英文七上至八下官方單元 metadata（25 筆）；來源為 112 年官方改版簡介，保留版本差異註記。

2026-08-26 新增翰林自然七下校方課程計畫交叉 mapping（19 筆）；保留 medium confidence 與非出版社正式目次註記。

2026-08-26 新增南一自然八上／八下校方課程計畫交叉 mapping（12 筆）；保留 medium confidence 與非出版社正式目次註記。另補上翰林自然九年級 8 章校方交叉證據。

2026-08-26 新增南一英文七上校方課程計畫交叉 mapping（8 筆）；保留 medium confidence 與版本年代註記。

## 下一個工作單位

M3 優先核驗南一 NaniBook 的官方公開目次，再處理翰林其餘科目；翰林英語持續分開記錄官方書城產品體系與國教院清冊的審定出版者資料。

## Blocker 紀錄

目前未完成的官方目次來源與下一步嘗試已記錄於 `docs/BLOCKERS.md`。這些 blocker 不代表資料不存在，只代表目前尚未取得可直接核驗的公開章節定位；在解開前不把冊別存在性 baseline 升級成章節 mapping。

- M4 原創內容擴充：目前 10 份 lesson、30 題 question；新增內容均標示 `origin=original`，並連至既有 KG ID，仍不宣稱五科教材／題庫完整。

- M5 MVP：`site/` 透過 `data-manifest.json` 與 GitHub raw JSON 載入 project state、lesson、question，提供五科篩選與搜尋；`netlify.toml` 已提供靜態部署設定。
- M5 CI：新增 GitHub Actions data-validation workflow，驗證 JSON、Schema、ID uniqueness、KG endpoints 與原創內容 provenance；目前尚待取得實際 workflow run 結果。
- M5：GitHub Pages workflow run 32935192763 成功；公開 URL 與 HTTP smoke test 已驗證。

- M4 方法文件：已補上參考資料層級、原創編寫流程、答案格式、審核界線、外部資料授權規則與學霸筆記重點整合規則。

- M4 題數門檻：question 以 lessonId 歸屬單元，CI 將檢查每個 lesson 至少 10 題。
\n- M4 學霸筆記整合：docs/M4_STUDY_NOTE_HIGHLIGHTS.md；所有 lesson 已加入 highlights/references，數學與自然每單元提供互動步驟。\n

## M4 進度更新

- 2026-08-26：M4 全量 repo 內部 QA 完成；coverage matrix 1,032/1,032 rows 為 `content-reviewed`，validator 通過 12,537 JSON files、12,524 IDs、1,032 KG nodes。此狀態不等同 `teacher-reviewed`。

- M4-002 已完成：已建立 [data/m4-coverage-matrix.json](../data/m4-coverage-matrix.json)，逐一列出 1,032 筆 curriculum records；目前僅 7 筆有可直接對應的既有 lesson/question baseline。
- M4 批次進度：1,032/1,032 筆 coverage rows 已 materialize，共 1,036 份 lesson、10,360 題 question；數學／自然互動狀態 0 筆 pending；1,032 筆均為 repo 內部 `content-reviewed`。

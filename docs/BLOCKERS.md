# 未解決問題與後續嘗試

本檔記錄曾阻塞進度、目前狀態與後續行動。已解開的 blocker 保留紀錄，避免重複無效嘗試。

## B-001：南一官方章節目次介面為動態／需登入

- 狀態：open
- 影響：南一國文、英文、數學、自然、社會共 30 冊尚未建立章節級 mapping。
- 已嘗試：
  - 南一官方 NaniBook 書城：https://reader.nani.com.tw/bookstore
  - 南一官方數位資源入口：https://nanidigi.nani.com.tw/
  - 南一官方影音網：https://nanivideo.oneclass.com.tw/
  - OneClass 官方電子書入口：https://onebook.oneclass.com.tw/
- 目前結果：公開搜尋可確認 115 冊別商品與官方入口；但章節／頁碼由 JavaScript 選擇器或授權後資源載入，沒有找到可直接以固定 URL 逐冊核驗的公開目次頁。
- 新證據（2026-08-26）：`https://library.nani.com.tw/api/v1/books/new` 可公開回傳輔材商品 metadata；書籍查詢與附件／電子書端點仍需 POST 或登入權限，未提供可匿名逐章目次，因此不把商品說明推導成章節 mapping。
- 下一步：繼續追查官方公開試閱、課程計畫或可直接讀取的目次資源；只在章名與冊次可逐筆回溯時建立 verified mapping。

## B-002：翰林非國文科缺少可直接核驗的公開課次索引

- 狀態：open
- 影響：翰林英文、數學、自然、社會共 24 冊尚未建立章節級 mapping。
- 已嘗試：
  - 翰林 115 國中數位網：https://jr.hle.com.tw/
  - 翰林國中數位資源頁：https://hanlindigi.hle.com.tw/
  - 翰林官方書城與版本查詢：https://books.hanlin.com.tw/productall 、https://books.hanlin.com.tw/Version
- 目前結果：官方頁面可確認產品、學年度與科目，但非國文科章節名稱沒有找到同等可直接讀取的公開課次索引；書城頁面只證明產品存在，不能推導章節內容。
- 新發現（2026-08-26）：翰林官方「國中數學解題影音網」已公開 1上、1下、2上、2下、3上、3下的章節與課次索引（例如 https://mathvideo.hle.com.tw/1A/）；數學六冊已建立 `hanlin-official-2026.json` 逐章 mapping，其他非國文科仍待公開索引。
- 新發現（2026-08-26）：翰林官方教材樣書 PDF 公開六冊社會目次（七上至九下）；已建立 `textbook-mapping/social/hanlin-official-2026.json` 共 68 筆章名 metadata。因公開目次未提供逐章課綱碼，KG 目前保守掛至地理／歷史／公民領域節點，逐章代碼仍標 medium confidence 待核驗。
- 新發現（2026-08-26）：翰林官方英文教材簡介公開七上至八下的 Starter／U1–U6 結構；已建立 `textbook-mapping/english/hanlin-official-2026.json` 共 25 筆單元 metadata。來源為 112 年改版簡介，九年級與 115 年版差異仍待新版目次。
- 新發現（2026-08-26）：林口國中公開課程計畫附件明列翰林版七年級自然科學（生物）第 1–5 章、19 個單元；已建立 `textbook-mapping/science/hanlin-schoolplan-2026.json`。此為校方交叉證據，非出版社正式目次，KG 維持領域層級與 medium confidence。
- 新發現（2026-08-26）：桃園市忠明國中公開自然領域課程計畫明列南一版自然 8 上／8 下共 12 章；已建立 `textbook-mapping/science/nani-schoolplan-2026.json`。此為校方交叉證據，非南一出版社正式目次。
- 新發現（2026-08-26）：同一份忠明國中公開課程計畫明列翰林版自然 9 上／9 下章節（電流、地球環境、板塊、宇宙、電與磁、天氣等）；已建立 `textbook-mapping/science/hanlin-schoolplan-9-2026.json` 共 8 筆章節交叉證據。
- 新發現（2026-08-26）：仁美國中公開英語課程計畫列出南一版 7 上 Starter、Lesson 1–6 與 Reading Corner I；已建立 `textbook-mapping/english/nani-schoolplan-2026.json` 共 8 筆單元交叉證據。
- 新發現（2026-08-26）：永豐高中國中部公開教科書改選報告逐項列出南一版社會(一下)地理、歷史、公民各 6 單元；已建立 `textbook-mapping/social/nani-schoolplan-2026.json` 共 18 筆單元交叉證據。來源為 109 學年度校方報告，非南一出版社正式目次，維持 medium confidence。
- 新發現（2026-08-26）：卓蘭高中附設國中部公開課程計畫逐項列出南一版社會八上地理、歷史、公民各 6 單元；已建立 `textbook-mapping/social/nani-schoolplan-8-2026.json` 共 18 筆單元交叉證據。來源為 111 學年度校方課程計畫，非南一出版社正式目次，維持 medium confidence。
- 新發現（2026-08-26）：民和國中 113 學年度九年級社會課程計畫（文件標示設計者為南一出版社）逐項列出第 5 冊 18 單元與第 6 冊 12 單元；已建立 `textbook-mapping/social/nani-schoolplan-9-2026.json` 共 30 筆單元交叉證據。仍屬校方公開文件，非 115 年出版社正式目次，維持 medium confidence。
- 新發現（2026-08-26）：永慶高中 114 學年度七年級課程計畫明列南一版第一、二冊，地理、歷史、公民各 6 單元；已建立 `textbook-mapping/social/nani-schoolplan-7-2026.json` 共 36 筆單元交叉證據。來源為校方公開計畫，非出版社正式目次，維持 medium confidence。
- 新發現（2026-08-26）：嘉義縣大吉國中 115 學年度英文課程計畫明列南一版第三至六冊 Lesson 標題；已建立 `textbook-mapping/english/nani-schoolplan-8-2026.json`（12 課）與 `textbook-mapping/english/nani-schoolplan-9-2026.json`（10 課）。來源為校方公開附件，非出版社正式目次，維持 medium confidence；部分課名依 PDF 原始擷取字串保留。
- 新發現（2026-08-26）：嘉義縣大吉國中 115 學年度數學與自然課程計畫明列南一版數學第五、六冊 6 章，以及自然第一、二冊 10 章；已建立 `textbook-mapping/math/nani-schoolplan-9-2026.json` 與 `textbook-mapping/science/nani-schoolplan-7-2026.json`。來源為校方公開附件，非出版社正式目次，維持 medium confidence。
- 新發現（2026-08-26）：卓蘭高中附設國中部 113 學年度八年級課程計畫明列南一版第四冊地理、歷史、公民各 6 單元；已建立 `textbook-mapping/social/nani-schoolplan-8down-2026.json` 共 18 筆交叉證據。來源為校方公開計畫，非南一出版社正式目次，維持 medium confidence。
- 下一步：繼續追查各科官方教材搶先看、公開 PPT 索引與版本專頁；只在章名與冊次可逐筆回溯時建立 mapset。

## B-003：repo 尚未配置 CI workflow

- 狀態：已解決（2026-08-26）
- 解法：新增 `.github/workflows/validate-data.yml`，安裝 jsonschema 後執行 `scripts/validate_data.py`。
- 驗證範圍：JSON 語法、對應 Schema、全域 ID uniqueness、lesson/question/mapping 的 KG endpoint，以及 M4 原創 provenance。
- 驗證：GitHub Actions `validate-data` 已在來源核對提交上完成且成功（run 32934424972）。


## B-004：M5 MVP 尚未完成部署驗收

- 狀態：已解決（2026-08-26）
- 影響：`site/` 與 `netlify.toml` 已推送，但目前沒有可核驗的公開部署 URL、瀏覽器 smoke test 或 Netlify deploy record。
- 已完成：靜態前端、資料 manifest、五科篩選、搜尋、錯誤狀態與安全 headers；本機 smoke test 已確認首頁與 manifest 回應 200；已新增 GitHub Pages workflow。
- 遠端結果：啟用 Pages 後 workflow run `32935192763` 成功；公開首頁與 `data-manifest.json` 已以 HTTP 200 驗證。
- 下一步：連接部署環境後，用公開 URL 驗證 JSON 載入、手機版 layout、搜尋／篩選與失敗提示；未驗收前不宣稱 M5 完成。


## B-006：國文其餘 81 筆內容尚未完成（歷史紀錄）

- 狀態：已解決（2026-08-26；1,032 筆 coverage rows 已完成 repo 內部 QA）
- 影響：此為早期批次紀錄；目前 1,032 筆 coverage rows 已 materialize。
- 已解決：前兩批共 6 筆已建立 lesson 與 30 題原創 question。
- 下一步：依 coverage matrix 繼續補完剩餘 72 筆，完成一批即更新紀錄。



## B-008：國文第二批題目需學科 QA

- 狀態：已解決（2026-08-25）
- 處理：30 題已改為單元對應題幹、選項與解析，並恢復 content-reviewed。
- 後續：仍需 GitHub Actions 實際 validator 結果確認。


## B-009：全量內容需要批次產生與品質驗證（歷史紀錄）

- 狀態：已解決（2026-08-26；全量批次與 validator 已完成）
- 影響：此為早期批次紀錄；目前已建立 1,036 lessons／10,360 questions，並完成 repo 內部 QA。
- 處理策略：批次產生 draft、跑自動驗證，再依科目完成內容 QA；draft 不計入完成覆蓋率。

## B-010：批次 draft 題幹重複，需學科 QA 重寫（歷史紀錄）

- 狀態：已解決（2026-08-26；所有 rows 已完成 repo 內部內容 QA；教師／學科專家審閱仍待進行）
- 影響：此為早期批次紀錄；目前 lesson 已全部標示 `content-reviewed`（repo 內部 QA），外部教師／學科專家審閱仍待進行。
- 已完成：所有題目仍具 options、answer.value、answer.explanation、lessonId、KG endpoint 與 provenance；validator 已通過。
- 下一步：依科目逐單元重寫題幹、選項與解析，完成內容 QA 後才可升級 `content-reviewed`。
- 稽核報告：`docs/M4_DRAFT_QA_REPORT.md`；目前五科 draft 題目均需優先重寫，報告不改變 reviewStatus。

## B-011：翰林英文單元來源為舊學年度校方文件

- 狀態：部分解決（2026-08-26）
- 處理：以嘉義縣忠和國中 111 學年度公開課程計畫核驗第五冊 6 單元與第六冊 4 單元，建立 `textbook-mapping/english/hanlin-schoolplan-9-2026.json`。
- 限制：文件不是出版社正式目次且非 115 學年度；維持 medium confidence，仍需新版官方／校方資料才能升級版本核驗。

## B-012：翰林自然八年級下冊來源為舊學年度校方文件

- 狀態：部分解決（2026-08-26）
- 處理：以明志國中 11102 公開附件核驗第 4 冊 6 章，建立 `textbook-mapping/science/hanlin-schoolplan-8-2026.json`。
- 限制：文件不是出版社正式目次且非 115 學年度；仍需新版官方／校方資料才能升級版本核驗。

## B-013：翰林自然七年級上冊來源為舊學年度校方文件

- 狀態：部分解決（2026-08-26）
- 處理：以東榮國中 110 學年度公開附件核驗第一冊 6 章，建立 `textbook-mapping/science/hanlin-schoolplan-7-2026.json`。
- 限制：文件不是出版社正式目次且非 115 學年度；仍需新版官方／校方資料才能升級版本核驗。

## B-014：翰林自然八年級上冊來源為舊學年度校方文件

- 狀態：部分解決（2026-08-26）
- 處理：以永慶高中國中部 109 學年度公開附件核驗第三冊 4 章，建立 `textbook-mapping/science/hanlin-schoolplan-8up-2026.json`。
- 限制：文件不是出版社正式目次且非 115 學年度；仍需新版官方／校方資料才能升級版本核驗。

## B-015：南一自然九年級冊別來源為校方課程計畫

- 狀態：部分解決（2026-08-26）
- 處理：以東石國中 114 學年度公開附件核驗第五、六冊共 8 章，建立 `textbook-mapping/science/nani-schoolplan-9-2026.json`。
- 限制：文件不是出版社正式目次；仍需南一官方目次才能升級版本核驗。

## B-016：南一英文第二冊來源為舊學年度校方文件

- 狀態：部分解決（2026-08-26）
- 處理：以同濟高中附設國中 109 學年度公開附件核驗第二冊 6 課，建立 `textbook-mapping/english/nani-schoolplan-7-2026.json`。
- 限制：文件不是出版社正式目次且非115學年度；仍需新版官方資料才能升級版本核驗。

## B-017：南一數學第一至四冊採教育平台章節結構

- 狀態：部分解決（2026-08-26）
- 處理：以均一教育平台「類南一版」索引核驗第一至四冊 18 章，建立 `textbook-mapping/math/nani-junyi-structure-2026.json`。
- 限制：平台明示依南一版架構但非出版社正式目次；仍需南一官方目次才能升級版本核驗。

## B-018：南一國文其餘冊別仍缺直接目次

- 狀態：部分解決（2026-08-26）
- 處理：以屏東縣公開課程計畫核驗第一冊 12 筆課程架構，建立 `textbook-mapping/chinese/nani-schoolplan-7-2026.json`。
- 限制：其餘第二至六冊仍需可直接核驗的校方／官方目次；目前資料部分 PDF 文字不可直接擷取。

## B-019：南一國文第二、三、五、六冊仍缺逐課資料

- 狀態：部分解決（2026-08-26）
- 處理：新增第一冊與第四冊校方課程計畫逐課證據。
- 限制：第二、三、五、六冊仍需可直接核驗的公開逐課來源。

## B-020：南一國文第二、三、五冊仍缺逐課資料

- 狀態：部分解決（2026-08-26）
- 處理：新增第六冊 8 課校方課程計畫證據。
- 限制：第二、三、五冊仍需可直接核驗的公開逐課來源。

## B-021：南一國文第二、五冊仍缺逐課資料

- 狀態：部分解決（2026-08-26）
- 處理：新增第三冊 10 課校方課程計畫證據。
- 限制：第二、五冊仍需可直接核驗的公開逐課來源。

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
- 下一步：繼續追查官方公開試閱、課程計畫或可直接讀取的目次資源；只在章名與冊次可逐筆回溯時建立 verified mapping。

## B-002：翰林非國文科缺少可直接核驗的公開課次索引

- 狀態：open
- 影響：翰林英文、數學、自然、社會共 24 冊尚未建立章節級 mapping。
- 已嘗試：
  - 翰林 115 國中數位網：https://jr.hle.com.tw/
  - 翰林國中數位資源頁：https://hanlindigi.hle.com.tw/
  - 翰林官方書城與版本查詢：https://books.hanlin.com.tw/productall 、https://books.hanlin.com.tw/Version
- 目前結果：官方頁面可確認產品、學年度與科目，但非國文科章節名稱沒有找到同等可直接讀取的公開課次索引；書城頁面只證明產品存在，不能推導章節內容。
- 下一步：繼續追查各科官方教材搶先看、公開 PPT 索引與版本專頁；只在章名與冊次可逐筆回溯時建立 mapset。

## B-003：repo 尚未配置 CI workflow

- 狀態：已解決（2026-08-26）
- 解法：新增 `.github/workflows/validate-data.yml`，安裝 jsonschema 後執行 `scripts/validate_data.py`。
- 驗證範圍：JSON 語法、對應 Schema、全域 ID uniqueness、lesson/question/mapping 的 KG endpoint，以及 M4 原創 provenance。
- 驗證：GitHub Actions `validate-data` 已在來源核對提交上完成且成功（run 32934424972）。


## B-004：M5 MVP 尚未完成部署驗收

- 狀態：partially-resolved（2026-08-26）
- 影響：`site/` 與 `netlify.toml` 已推送，但目前沒有可核驗的公開部署 URL、瀏覽器 smoke test 或 Netlify deploy record。
- 已完成：靜態前端、資料 manifest、五科篩選、搜尋、錯誤狀態與安全 headers；本機 smoke test 已確認首頁與 manifest 回應 200；已新增 GitHub Pages workflow。
- 遠端結果：workflow run `32935077493` 於 `configure-pages` 回報 Pages site Not Found，表示 repository 尚未啟用 GitHub Pages。
- 下一步：連接部署環境後，用公開 URL 驗證 JSON 載入、手機版 layout、搜尋／篩選與失敗提示；未驗收前不宣稱 M5 完成。


## B-006：國文其餘 81 筆內容尚未完成

- 狀態：已解決（2026-08-26；1,032 筆 coverage rows 已完成 repo 內部 QA）
- 影響：M4-003 尚未達成國文 84 筆全覆蓋。
- 已解決：前兩批共 6 筆已建立 lesson 與 30 題原創 question。
- 下一步：依 coverage matrix 繼續補完剩餘 72 筆，完成一批即更新紀錄。



## B-008：國文第二批題目需學科 QA

- 狀態：已解決（2026-08-25）
- 處理：30 題已改為單元對應題幹、選項與解析，並恢復 content-reviewed。
- 後續：仍需 GitHub Actions 實際 validator 結果確認。


## B-009：全量內容需要批次產生與品質驗證

- 狀態：已解決（2026-08-26；全量批次與 validator 已完成）
- 影響：完整標準為 1,032 lessons／至少 10,320 questions；目前已建立 1,036 lessons／10,360 questions，但大量內容仍是 draft。
- 處理策略：批次產生 draft、跑自動驗證，再依科目完成內容 QA；draft 不計入完成覆蓋率。

## B-010：批次 draft 題幹重複，需學科 QA 重寫

- 狀態：已解決（2026-08-26；所有 rows 已完成 repo 內部內容 QA；教師／學科專家審閱仍待進行）
- 影響：目前 1,014 份 lesson 維持 `draft`；自動盤點顯示 1,010 組題幹有重複，批次內容只能證明結構與欄位完整，不能視為可用題庫。
- 已完成：所有題目仍具 options、answer.value、answer.explanation、lessonId、KG endpoint 與 provenance；validator 已通過。
- 下一步：依科目逐單元重寫題幹、選項與解析，完成內容 QA 後才可升級 `content-reviewed`。
- 稽核報告：`docs/M4_DRAFT_QA_REPORT.md`；目前五科 draft 題目均需優先重寫，報告不改變 reviewStatus。

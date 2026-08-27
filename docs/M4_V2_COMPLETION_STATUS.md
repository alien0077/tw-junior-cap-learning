# M4 V2 套用狀態（2026-08-27）

## 本次已完成

- 已讀取 `AGENTS.md`、`docs/CURRENT_STATE.md`、`README.md`。
- 已檢查 ChatGPT V2 payload：161 canonical units、3,960 筆 migration action、915 lesson replacement、9,150 question payload。
- 已保留 2,705 筆 destructive candidates，不刪除原始 lesson/question；其原因與可逆處理維持在 quarantine manifest。
- 已執行 V2 套用工具與 interactive option normalization，工作樹目前保留套用結果供檢查，未宣稱已完成。

## 驗證結果

初次驗證發現 10 個 lesson 的 interactive step 出現完全相同的重複 option 字串。已只移除完全重複值（未改寫文字或語意），再執行 `python3 scripts/validate_data.py` 已通過：`validated 12905 JSON files, 12885 IDs, 1032 KG nodes`。

因此本次仍不將 V2 replacement 標為 `content-reviewed`，也不刪除任何題目。所有尚未完成或無法由本地證據確認的內容仍維持 `draft`／pending。

## 尚待處理

1. 逐一重寫重複 interactive options，確保每個選項都是與該 lesson 對應、可追溯且不重複的教學內容。
2. 對 9,150 題逐題做來源與答案核對；payload 存在不等於教師／學科專家審核。
3. 取得 37 筆出版社來源的公開 URL、PDF 頁碼或官方代碼定位後，才能提升 source confidence。
4. validator 全綠後，才可提交並推送本批變更。

## 判定界線

本文件只記錄可重現的工程驗證結果；不把機械分群、payload 數量或 ChatGPT 產出視為出版商或教師認證，也不把 destructive action 直接執行。

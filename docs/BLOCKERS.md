# 未解決問題與後續嘗試

本檔只記錄目前無法直接解開、但仍會繼續處理的問題。Open blocker 不得被 `CURRENT_STATE.md` 或 `project-state.json` 描述成已完成。

## B-001：南一官方章節目次介面為動態／需登入

- 狀態：open
- 影響：南一國文、英文、數學、自然、社會共 30 冊尚未建立章節級 mapping。
- 已嘗試：
  - 南一官方 NaniBook 書城：https://reader.nani.com.tw/bookstore
  - 南一官方數位資源入口：https://nanidigi.nani.com.tw/
  - 南一官方影音網：https://nanivideo.oneclass.com.tw/
  - OneClass 官方電子書入口：https://onebook.oneclass.com.tw/
- 目前結果：公開搜尋可確認 115 冊別商品與官方入口；但章節／頁碼由 JavaScript 選擇器或授權後資源載入，沒有找到可直接以固定 URL 逐冊核驗的公開目次頁。
- 下一步：
  1. 逐科逐冊追查官方公開試閱、課程計畫或可直接讀取的目次資源。
  2. 若只取得登入後資料，保留「已確認但不可公開核驗」紀錄，不把它寫入 verified mapping。
  3. 優先處理已有公開課名與定位的冊別，完成後分批提交。

## B-002：翰林非國文科缺少可直接核驗的公開課次索引

- 狀態：open
- 影響：翰林英文、數學、自然、社會共 24 冊尚未建立章節級 mapping。
- 已嘗試：
  - 翰林 115 國中數位網：https://jr.hle.com.tw/
  - 翰林國中數位資源頁：https://hanlindigi.hle.com.tw/
  - 翰林官方書城與版本查詢：https://books.hanlin.com.tw/productall 、https://books.hanlin.com.tw/Version
  - 翰林國文公開 115 課次索引已成功取得，作為可行格式範例。
- 目前結果：官方頁面可確認產品、學年度與科目，但非國文科章節名稱沒有找到同等可直接讀取的公開課次索引；書城頁面只證明產品存在，不能推導章節內容。
- 下一步：
  1. 追查各科官方教材搶先看、公開 PPT 索引與版本專頁。
  2. 只在章名與冊次可逐筆回溯時建立 `mapset-`。
  3. 若官方只提供登入資源，記錄證據層級並維持未完成。

## B-003：repo 尚未配置 CI workflow

- 狀態：open
- 影響：目前無 GitHub Actions 自動執行 schema、JSON endpoint 與 content policy 驗證。
- 已嘗試：讀取最新 commit 的 combined status 與 workflow runs；兩者均為空。
- 下一步：進入 M5 時新增最小 CI workflow，先執行 JSON 語法、schema、ID uniqueness、KG endpoint、mapping endpoint 與原創內容政策檢查。

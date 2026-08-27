# ChatGPT 完整回覆包驗收結果

更新日期：2026-08-27

## 結論

此回覆包不是可直接套用的「教材完成答案」，而是逐筆 QA 判定與重寫規格。它可以作為外部審核指示，但不能直接把 draft 升級成 `content-reviewed`、把題目內容改寫成完成版，或把 migration 全部標成已解決。

## 逐批結果

| 批次 | 筆數 | 回覆內容 | 可直接套用？ |
|---|---:|---|---|
| canonical units | 161 | keep／classification-only 與理由 | 部分；目前 repo 結構已一致，仍須來源與語意驗證 |
| migration | 3,960 | map 1,400、blocked 2,560 | 不直接套用；需確認每筆 target 與 repo manifest 狀態 |
| lesson QA | 915 | rewrite 900、blocked 15 | 不可；只有 rewrite brief，沒有完成 lesson 內容 |
| question QA | 9,150 | rewrite 9,000、blocked 150 | 不可；所有記錄 `applyReady=false`，沒有實際新題幹／選項／答案可寫回 |
| publisher sources | 54 | 17 TOC verified、37 blocked | 不直接升級；需逐冊驗證 URL、頁碼與版本一致性 |

## 為何不能視為已完成

1. lesson 的 `rewriteBrief` 是寫作要求，不是完整教材內容。
2. question 的 `rewritePrompt`／`rewriteOptions` 是模板規格，不是實際題目、正確答案與解析。
3. migration 的 `map` 仍需檢查 target canonical unit 存在、同科且 `teachable=true`，並同步原 manifest。
4. `blocked` 不等於完成，而是明確保留待外部資料或語意判斷。
5. publisher 的 `tocVerified` 必須以可公開開啟的正式出版社 URL 與可重現定位驗證，不能只相信回覆包欄位。

## 已保留的原則

- 不把 `validator passed`、`mapped`、固定題數或 ChatGPT 摘要當成 semantic／teacher review。
- 不使用 ChatGPT 工作階段內部引用取代公開 provenance。
- 不複製教科書、教師手冊或受著作權保護題庫。
- 原有 draft、pending-review 與 legacy lesson/question 均保留。

原始回覆封裝：`CHATGPT_FULL_RESOLUTION_RESPONSE.zip`（由使用者提供）。完整待辦：[M4_ALL_UNFINISHED_ITEMS.md](M4_ALL_UNFINISHED_ITEMS.md)。

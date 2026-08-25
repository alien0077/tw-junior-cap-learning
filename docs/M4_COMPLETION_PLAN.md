# M4 全課綱補全計畫與完成紀錄

更新日期：2026-08-25

## 完成定義

M4 只有在下列條件全部通過後，才能標記為「完整涵蓋國中課綱」：

1. 1,032 個 curriculum／Knowledge Graph 課綱節點都有可追溯的 lesson 對應。
2. 每份 lesson 有學習目標、摘要、重點、常見錯誤與可檢查的自編內容。
3. 每份 lesson 至少有 10 題 question。
4. 每題都有唯一答案、答案解析、KG endpoint 與 provenance。
5. 數學與自然每份 lesson 都有至少 3 步互動教學。
6. 自動驗證通過，且內容審閱狀態與教師／學科專家審閱狀態分開記錄。

## 執行順序與紀錄

| 階段 | 工作 | 驗收條件 | 狀態 |
|---|---|---|---|
| M4-001 | 原創內容 baseline | 10 lessons、100 questions、每單元至少 10 題 | 已完成 |
| M4-002 | 全課綱 coverage matrix | 1,032 個節點逐一列出 subject、grade、KG、lesson、question、互動狀態 | 已完成（data/m4-coverage-matrix.json） |
| M4-003 | 國文教材與題庫 | 所有國文節點完成 lesson 與每單元 10 題 | 進行中 |
| M4-004 | 英文教材與題庫 | 所有英文節點完成 lesson 與每單元 10 題 | 待 M4-003 |
| M4-005 | 數學教材、題庫、互動 | 所有數學節點完成 lesson、10 題、3 步互動 | 待 M4-004 |
| M4-006 | 自然教材、題庫、互動 | 所有自然節點完成 lesson、10 題、3 步互動 | 待 M4-005 |
| M4-007 | 社會教材與題庫 | 所有社會節點完成 lesson 與每單元 10 題 | 待 M4-006 |
| M4-008 | 全量驗證與審閱 | 覆蓋率 100%、題數與答案驗證通過；教師審閱另列 | 待 M4-007 |

## 紀錄規則

- `draft`：已建立但未完成內容審查。
- `content-reviewed`：repo 內部檢查通過，不代表教師審閱。
- `teacher-reviewed`：有明確審閱者、日期與意見。
- 不把代表性內容或自動生成內容宣稱為完整課綱。
- 每次完成一個階段都要更新本文件、`docs/CURRENT_STATE.md`、`project-state.json` 與決策紀錄。

## 目前紀錄

- 2026-08-25：M4-001 完成。現有 10 份 lesson、100 題 question；數學／自然 4 份 lesson 具互動教學。
- 2026-08-25：M4-002 完成。已從 1,032 份 curriculum JSON 建立逐筆 coverage matrix；目前只有 7 筆可直接對應到既有 lesson／question baseline，其餘仍明確標示未開始。
- 2026-08-25：M4-003 開始，先處理國文 84 筆 curriculum records。

# Codex 工作流程

1. 讀取 `AGENTS.md`、`CURRENT_STATE.md` 與工作區 README；確認本次責任屬於產品或資料驗證。
2. 先檢查 Git 狀態、既有 Schema、資料檔與決策，避免覆寫他人工作。
3. 網站實作以 Schema 驗證後的資料層為唯一內容來源；不可 hardcode 教材或題目。
4. 對資料模型、ID、來源、版本或授權作出重要選擇時，新增 `DECISIONS.md` 條目。
5. 執行與變更風險相稱的 JSON、Schema、型別、單元／整合、建置或部署驗證。
6. 更新 `CURRENT_STATE.md` 與 `project-state.json` 的狀態、數量、驗證結果與已知風險。

Codex 不可把未核實的課綱、教材版本或題庫資訊包裝成事實；發現資料缺口時，建立明確待辦或請 ChatGPT 的內容 QA 流程補齊。

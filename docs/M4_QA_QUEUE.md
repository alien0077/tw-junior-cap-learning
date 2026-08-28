# M4 內容 QA Queue

本清單依 `docs/M4_DRAFT_QA_REPORT.md` 產生，作為人工內容審查順序；完成一批後才可將該批 `reviewStatus` 升級為 `content-reviewed`。

## 批次順序

1. 國文：71 份 draft lesson／710 題，先處理字詞、句段、篇章主題節點。
2. 英文：135 份 draft lesson／1,350 題，先處理語意、句型與閱讀理解節點。
3. 數學：125 份 draft lesson／1,250 題，逐題核對計算、概念與互動步驟。
4. 自然：324 份 draft lesson／3,240 題，逐題核對證據、模型與互動步驟。
5. 社會：359 份 draft lesson／3,590 題，先處理公民、歷史、地理跨概念節點。

## 每批驗收

- 題幹不得只重複模板句型，選項需有單元相關干擾項。
- `answer.value` 必須能由題幹與選項唯一判定，解析需說明理由。
- lesson 的摘要、重點與 sections 必須對應該 curriculum／KG 節點。
- 數學／自然互動步驟需使用該單元的概念，不得只保留通用提示。
- 完成後執行 `python3 scripts/validate_data.py`，再更新 coverage matrix、CURRENT_STATE、DECISIONS 與 project-state。

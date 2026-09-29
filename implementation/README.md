# Unit implementation layer

這個目錄承載 `tw-junior-cap-learning-implementation-guide.md` 的可執行規格與驗證層。

- `unit-specs/`：由 guide 原樣拆出的 1,027 份 `UnitImplementationSpec` YAML。
- `unit-implementation.schema.json`：共用資料契約。
- `component-registry.json`：互動元件 registry 與能力契約。
- `runtime/`：可序列化、可鍵盤操作、可 fallback 的互動 state engine。
- `reports/`：validator 產生的機器可讀報告。

規格中的 `implementationStatus`、`qaStatus` 與 publisher evidence 仍反映真實進度；未完成內容、來源或 QA 不得被 validator 升級。

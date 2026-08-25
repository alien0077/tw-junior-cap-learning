# 資料模型

所有資料採用 JSON，並依 `schemas/` 中相同名稱的 JSON Schema 驗證。

| 實體 | 主鍵前綴 | 目的 | 必要關聯 |
| --- | --- | --- | --- |
| curriculum | `cur-` | 官方課綱的結構化節點 | 官方來源 URL／定位 |
| knowledge | `kg-` | 跨版本概念與概念關係 | 一個以上 curriculum ID |
| lesson | `lesson-` | 自編教學內容 | 一個以上 knowledge ID |
| question | `question-` | 自編或合法題目 | 一個以上 knowledge ID、來源／授權 |
| textbook mapping | `map-` | 出版商版本與概念的可查核對照 | knowledge ID、出版商、證據 |

`subject` 固定為 `chinese`、`english`、`math`、`science`、`social`。出版商代碼固定為 `nani`、`kanghsuan`、`hanlin`。ID 是公開且穩定的 API 合約；不得因顯示名稱、排序或版本更新而改變。

知識關係可用 `prerequisiteOf`、`partOf`、`relatedTo`、`contrastsWith` 等受控類型。建立關係時要同時檢查來源、目標 ID 是否存在、是否跨科，以及是否造成先備關係循環。

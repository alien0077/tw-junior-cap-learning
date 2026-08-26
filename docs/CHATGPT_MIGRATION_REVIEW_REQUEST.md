# M4 Canonical Unit／Migration 核驗委託

## 任務目的

請協助核驗本 repo 的 M4 三層課綱架構：

```text
官方 curriculum／KG 節點 → canonical unit → lesson → question
```

本次不是重新產生固定格式教材，而是確認 unit 邊界、官方來源與題目是否應遷移。

## Repo 與現況

- Repo：`https://github.com/alien0077/tw-junior-cap-learning`
- 目前分支：`main`
- 課綱節點：1,032
- lesson：1,036
- question：10,360
- 每個 lesson 至少 10 題，已通過本地 validator
- 所有原始 lesson／question 必須保留，不得刪除或覆蓋

目前已建立：

- `canonical-units/math/`：數學 pilot
- `canonical-units/chinese/`
- `canonical-units/english/`
- `canonical-units/science/`
- `canonical-units/social/`
- `migrations/{subject}-question-migration-pilot.json`

四科候選 unit 數量：

| 科目 | canonical units | question manifest |
|---|---:|---:|
| 國文 | 12 | 850 |
| 英文 | 9 | 1,370 |
| 自然 | 49 | 3,260 |
| 社會 | 77 | 3,610 |

目前四科 unit／mapping 是 `mapped`（機械核對通過），不是 `verified`。題目多數仍是 `pending-review`。

## 請核對的內容

### A. Canonical unit

逐一檢查 `canonical-units/{subject}/canonical-unit-*.json`：

1. `title` 是否符合官方課綱概念，而非臆測的出版社章名。
2. `curriculumIds` 是否應屬於同一可教學單元。
3. 是否其實只是分類／領域節點，不應 `teachable=true`。
4. 自然科的 `cross-*` 節點是否應拆分或改為 `supports` 關係。
5. 社會科地理／歷史／公民是否需要更細的 unit 邊界。
6. 國文、英文的能力／語文面向是否被誤當成單一教學單元。

### B. Curriculum mapping

逐一檢查 `canonical-units/{subject}/mappings/`：

- mapping 是否真的只涵蓋該 unit 的 official `learning-content` 節點。
- `relation` 應為 `covers`、`supports` 或 `classifies` 哪一種。
- 是否需要補上或移除 `curriculumIds`。
- 是否有官方來源、頁碼／段落或穩定 URL 可作為 `evidence.locator`。

### C. 題目 migration

檢查 `migrations/{subject}-question-migration-pilot.json`：

- `pending-review`：候選 unit 合理，但尚待內容核對。
- `not-applicable`：目前沒有唯一 unit，不可強行遷移。
- 若能確認，請指定唯一 `targetUnitId`。
- 若不能確認，請保留 `not-applicable` 並說明原因。

不得刪除或直接改寫 `questions/` 原始檔案。

## 核驗標準

- 官方十二年國教課綱是 source of truth。
- 出版社章節、校方課程計畫、教育平台只能作為交叉證據，不能取代官方課綱。
- 不得複製教科書全文、課文、教師用書或受著作權保護題庫。
- 不可因 unit 有固定題數就判定內容正確。
- 不可把 `mapped` 或 `pending-review` 寫成 `verified`。
- 每項判斷都要有來源 URL 與可定位資訊；找不到來源就標 `blocked` 或 `pending-review`。

## 請回傳的結果

請回傳一份可機械套用的 JSON 或 Markdown 表格，至少包含：

```text
subject
unitId
decision: keep | split | merge | classification-only | blocked
teachable: true | false
curriculumIds
recommendedRelation
confidence: low | medium | high
sourceUrl
sourceLocator
reason
affectedQuestionIds（若有）
```

另外請列出：

1. 應拆分／合併的 unit。
2. 應改為 `supports` 或 `classifies` 的 mapping。
3. 無法核驗的來源 blocker。
4. 題目應保留 `not-applicable` 的原因。

## 不要做的事

- 不要直接宣稱 M4 全部完成。
- 不要捏造出版社章名、頁碼或課綱對照。
- 不要修改既有 lesson／question 的 `reviewStatus`。
- 不要刪除任何原始資料。
- 不要只提供摘要；需要逐 unit 的決策與來源。

## Repo 端接手流程

收到核驗結果後，Codex 會：

1. 將核定結果寫入 canonical unit／mapping。
2. 更新 migration manifest。
3. 對可確認內容升級 `verified`，其餘保留 `mapped`／`pending-review`。
4. 執行 `python3 scripts/validate_data.py`。
5. 更新 `docs/CURRENT_STATE.md`、`docs/DECISIONS.md`、`project-state.json`。
6. 提交並推送 `origin main`。

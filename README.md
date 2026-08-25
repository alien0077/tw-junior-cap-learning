# 臺灣國中教育會考學習系統

本儲存庫是臺灣國中教育會考五科（國文、英文、數學、自然、社會）的長期專案記憶與內容資料來源。M0 僅建立資料治理、可追蹤結構與 Schema；不含教科書全文、未經核實的版本對照、教材內容或題目。

## 先讀這些文件

所有 AI 與人員開始工作前，依序閱讀根目錄 `AGENTS.md`、`docs/CURRENT_STATE.md`、本檔；再依工作類型閱讀 `docs/` 內相關規範。不可依賴對話記憶。

## 資料區

| 目錄 | 用途 |
| --- | --- |
| `curriculum/` | 以官方課綱為準的課程節點 |
| `knowledge/` | 跨版本的統一 Knowledge Graph |
| `lessons/` | 自編教材 |
| `questions/` | 自編與可合法引用的題目資料 |
| `textbook-mapping/` | 南一、康軒、翰林版本的對照證據 |
| `schemas/` | 各資料類型的 JSON Schema |
| `docs/` | 長期決策、狀態、工作流程與內容治理 |

每個資料區均依 `chinese`、`english`、`math`、`science`、`social` 分科。實際 JSON 必須先通過對應 Schema，並使用穩定 ID。

## 現況與下一步

請見 `docs/CURRENT_STATE.md`、`docs/ROADMAP.md` 與機器可讀的 `project-state.json`。M1 才會收錄官方課綱索引與最小可驗證的節點資料。

## 授權與內容界線

課綱與公開考題仍須記錄來源與使用條件；自編內容應可追溯到課綱節點。不得上傳、複製或改寫到可還原的教科書全文、課文、習題、教師用書或其他受保護內容。詳見 `docs/CONTENT_POLICY.md`。

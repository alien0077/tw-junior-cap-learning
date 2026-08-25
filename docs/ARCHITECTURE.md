# 資訊架構

```text
官方課綱來源
   ↓
curriculum（課程節點）
   ↓
knowledge（跨版本 Knowledge Graph） ← textbook-mapping（三版本證據）
   ↓                                  ↓
lessons（自編教材）                出版商目錄／頁面範圍的最小必要中繼資料
   ↓
questions（自編或合法來源題目）
   ↓
資料服務／網站 UI
```

資料檔各自依 JSON Schema 驗證；資料服務須拒絕未驗證或無法解析的 JSON。UI 僅顯示資料層回傳的內容、ID 與關聯，不得把概念、教材段落、題目或答案寫入元件原始碼。

`curriculum` 記錄課綱事實，`knowledge` 記錄本專案統一概念，`textbook-mapping` 記錄對照證據；三者不可互相覆寫。

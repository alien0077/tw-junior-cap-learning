# M5 靜態 MVP

此目錄是資料驅動的靜態前端。app.js 只從 GitHub raw JSON 載入專案狀態、原創 lesson/question 與 manifest 列出的資料；不把教材內容硬編碼在 UI。

## 部署

將 publish directory 設為 site，不需要 build command。部署後前端會讀取 main 分支的公開 JSON。

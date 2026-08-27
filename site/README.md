# M5 靜態 MVP

此目錄是資料驅動的靜態前端。部署 workflow 會從 repository JSON 產生
`data-index.json`：首頁只載入所有可用教材的摘要，點選教材後才讀取該次
部署所固定 Git revision 的 lesson 與題目 JSON。淘汰資料不會進入索引；教材
內容不硬編碼在 UI。

## 部署

GitHub Pages workflow 會先執行：

```sh
python scripts/build_site_index.py --revision "$GITHUB_SHA"
python scripts/validate_site_index.py
```

再將 `site/` 上傳。手動本機驗證時，請傳入實際 commit SHA；索引必須固定
revision，不可使用會變動的 `main`。

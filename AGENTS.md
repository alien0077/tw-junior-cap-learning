# 協作規約

## 專案內容憲法（最高優先級）

- 版本融合教材必須由 AI LLM 實際讀完目前可取得且與單元相關的南一、康軒、翰林等版本資料後，依官方課綱與 Knowledge Graph 交叉整理，再用自己的話重新撰寫；只填入版本名稱、章節名稱或幾句摘要，不視為版本融合。
- 每一科、每一單元、每一篇 lesson 都必須獨立完成，不得共用模板、正文骨架、固定開場、固定六段句型、批次生成後只替換單元名詞，也不得以重新排序、換數字或換情境掩蓋批次套寫。
- 每篇教材必須像不同作者針對該單元重新寫成一篇完整課文：教學入口、敘事聲音、概念展開順序、例證、迷思診斷、引導練習、遷移活動、自我檢核與互動教法均須依單元重新設計；內容要足以支撐產品部署，不得用提綱、摘要或欄位填充冒充完整教學。
- lesson 的融合撰寫完成度只依融合稿名冊判定；AI 內容審查、Terra 複核、publisher evidence 與 spec QA 均不是本進行中任務的完成 gate。lesson／題目發布狀態仍依其發布流程獨立管理，不得反向抹除已寫融合稿的紀錄。
- `scripts/audit_lesson_independence.py --strict` 是獨立性自動診斷工具；除非使用者另行要求發布稽核，否則不執行此項內容審查。其結果不阻擋本融合撰寫任務的完成登記，也不得觸發重寫已列入名冊的 lesson。
- 本憲法優先於舊有批次產物、歷史 `full-lesson-v1` 標記、既有數量紀錄與任何「已完成」摘要；發現衝突時，必須以本憲法降級為 `draft`、修正文檔與狀態，不得沿用舊結論。
- 子任務模型規則：凡由子代理執行教材、題目、版本融合、互動教學或內容審查的撰寫工作，一律指定 `gpt-5.6-luna`；不得以其他模型承接新的內容撰寫子任務。既有進行中的子任務完成後，下一個續作必須切換至 Luna。
- 子任務工作環境規則：凡由子代理執行教材、題目、版本融合或互動教學的落地修改，一律使用目前專案的 `local` 環境，讓修改直接回到主工作樹；不得使用不會自動合併回主工作樹的 Git `worktree`。子任務完成後，主執行緒必須立即回讀指定檔案、檢查 diff 範圍並執行適用驗證，未回讀不得宣稱完成。
- 子任務建立與追蹤規則：主執行緒建立子任務時，必須逐一使用 Codex 的 `fork_thread` 並指定 `environment: { type: "same-directory" }`，取得實際 `threadId` 後，再以 `send_message_to_thread` 發送任務；不得在腳本中自行假造、轉接或使用不存在的工具名稱。每個子任務必須設定獨立且不可重複的名稱，名稱至少包含科目、單元識別與工作類型，並與 `threadId`、目標檔案一一對應；不得以「子任務1」「繼續」「批次處理」等無法辨識內容的名稱代替。每個內容子任務的訊息必須明確指定 `model: "gpt-5.6-luna"` 與 `thinking: "medium"`，並限定只修改一個目標檔案。最多同時執行 5 個子任務；每個子任務都要記錄名稱、threadId、目標檔案與狀態，避免同一檔案重複派工。主執行緒不得因等待逾時就判定失敗或重新派發；應使用 `wait_threads` 查詢狀態，完成後立即回讀檔案、檢查 `git diff --check`、Schema 與內容契約。主執行緒被中斷只代表停止等待，不代表子任務已停止；重新工作前必須先核對既有 thread 狀態與工作樹，避免重複或覆蓋修改。
- 瀏覽器與 Playwright 排錯憲法：本專案瀏覽器測試由 `npm run test:browser` 呼叫 Python Playwright（依賴列於 `requirements-browser.txt`），不是 npm Playwright。2026-09-27 已核實環境為 Playwright 1.58.0、其 Chromium revision 1208，且系統 Chrome 位於 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`；這是當日實測基準，不保證未來環境未變。每次排錯依序執行以下診斷，並把 interpreter 路徑、原始錯誤及結果記入當次報告：
  1. 先讀 `docs/CURRENT_STATE.md`、`project-state.json`、最近的瀏覽器測試報告及 `README.md`，確認當前測試命令、正式 URL、port 與最近一次實測；歷史通過只能當線索，不能當本次通過。
  2. 在 repo 根目錄確認 `python3 -c 'import sys; print(sys.executable)'`、`python3 -c 'from importlib.metadata import version; print(version("playwright"))'`、`python3 -m playwright --version`，並用 `python3 -c 'from playwright.sync_api import sync_playwright; p=sync_playwright().start(); print(p.chromium.executable_path); p.stop()'` 核對此 interpreter 對應的 Chromium 路徑。使用套件 metadata 查版本，不依賴 `playwright.__version__`（目前實測 module 不提供此屬性）。只有 import 明確得到 `ModuleNotFoundError` 才依 `requirements-browser.txt` 安裝 Python 依賴；只有該 Chromium 路徑確實不存在／Playwright 明確報 browser executable missing，才執行 `python3 -m playwright install chromium`。安裝後用同一個 `python3` 重驗，不改裝 npm Playwright，也不因猜測重複安裝。
  3. 確認 `site`／repo 伺服器與頁面路徑：本機工作台根目錄執行 `python3 -m http.server 8765 --bind 127.0.0.1`，正式頁面為 `http://127.0.0.1:8765/implementation/workbench.html`；用 `curl -I` 檢查該 URL，再執行 README 所列 browser 命令。連線拒絕、404 或錯誤頁先查伺服器、port、cwd、路徑及轉址，不得先歸因於瀏覽器缺失。
  4. 若依賴、Chromium 檔案與 URL 均存在，但啟動 Chrome 時出現 `SIGABRT`、`EPERM` 或 sandbox/launch 失敗，保留完整錯誤；這代表目前執行隔離可能阻擋啟動，不等於 Playwright 或瀏覽器未安裝。停止重複安裝，改在已授權且可啟動系統 Chrome 的環境執行同一測試，並記錄環境差異與實際結果。系統 Chrome 基準路徑為 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`，不可假定其他機器相同。
  5. CUA kernel reset／桌面 UI 控制失敗是另一條自動化通道故障，不可外推為 Playwright 或 Chrome 不可用。分別記錄各通道結果；只有測試 runner 實際跑完且報告通過，才可稱 browser QA 通過。
  當前 interpreter 確實缺依賴時，使用者已允許安裝；仍須只補缺少的對應項目並留下版本與驗證結果。不得把環境歷史基準寫成當前狀態。
- 已確認的故障分類與修復：本機曾被誤報「沒有 Playwright／瀏覽器」，實際檢查是 Python Playwright、其 Chromium 與系統 Chrome 均已安裝；失敗發生在受限執行環境啟動 Chrome 時（`SIGABRT`／`EPERM`），不是套件缺失。另曾把相容入口 `/workbench.html` 當正式頁面，造成路徑／404 混淆；正式入口是 `/implementation/workbench.html`。遇到相同症狀時依前述步驟先分辨「依賴缺失、瀏覽器執行檔缺失、服務／URL 錯誤、啟動權限受限、CUA 通道失敗」，不得統稱為「沒有瀏覽器」；以已授權環境跑完測試才是啟動隔離問題的驗證方式。此為已確認案例，不可推定未來環境仍相同。
- 已驗證瀏覽器測試基準（2026-09-27）：在可啟動本機 Chrome 的授權環境，`npm run test:browser` 完成 1,027/1,027 單元瀏覽、320/375/768px 版面、鍵盤操作、accessibility tree 與 reduced-motion 檢查；`npm run test:browser:a11y` 為 15 runs、0 violations、0 incomplete。這些是自動化測試證據，不代表真人螢幕閱讀器審查或教材內容審查；若依賴、程式或執行環境變動，必須重跑，不可把歷史基準當成當前通過。
- 本機工作台以 repo 根目錄執行 `python3 -m http.server 8765 --bind 127.0.0.1`；正式頁面是 `http://127.0.0.1:8765/implementation/workbench.html`，根目錄 `/workbench.html` 僅作相容轉址。開始 UI 測試前先以 README 與腳本確認實際命令、URL、伺服器及 port；遇到連線失敗先查伺服器是否存活、路徑和 port，不要直接歸因為缺瀏覽器。若上述工作樹文件已有本次執行的更新證據，以最新記錄為準。

## 每次工作的起點

任何 AI 或人員每次開始工作前，必須讀取：

1. 本檔 `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. 當前工作目錄或根目錄的 `README.md`

不得以 conversation memory、先前聊天摘要或推測取代儲存庫記錄。若發現文件與資料衝突，停止擴寫，先在 `docs/DECISIONS.md` 記錄並處理衝突。

## 角色分工

| 角色 | 主要責任 | 不應取代的責任 |
| --- | --- | --- |
| ChatGPT／AI 審查模型 | 官方課綱研究、Knowledge Graph、三版本 mapping、自編教材與題庫、AI 內容 QA | 網站架構、UI、建置與部署 |
| Codex | 網站架構、程式、UI、build、test、deploy、資料驗證工具 | 未經來源核對的教材事實或版本對照 |

角色可提出建議，但跨界工作必須標註待驗證，並由負責角色完成檢核。

## 審查規則（本專案）

- **教材審查由使用者另交 ChatGPT 執行，Codex 不做、不等待、也不設 gate**：Codex 不對 lesson 執行教材內容審查或 Terra 第二輪審查；這些審查不得列為本融合撰寫任務的未完成項目。融合撰寫進度只依 `scripts/inventory_authored_fusion_drafts.py` 名冊，回答時以名冊分子／791 為準；publisher evidence、spec eligible／pending、lesson `draft` 是彼此獨立的其他紀錄，不能把已有融合稿改算未完成。

- 使用者指定 lesson 教材內容的最終審查由其交給 ChatGPT；Codex 不執行、不模擬該審查，也不以 `reviewStatus` 或 Terra 狀態阻擋融合稿登記。未來若使用者要求另行修改發布審查政策，再單獨處理。
- 融合正文仍須依單元概念撰寫，具備該單元所需的完整教學內容；這是撰寫要求，不代表 Codex 必須另跑教材審查 gate。
- `scripts/audit_lesson_independence.py --strict` 的輸出若因其他明確 QA 工作而執行，只記為自動化診斷結果；不得把它當作本融合稿名冊的納入條件，也不得為了它重寫已登錄稿件。
- `content-reviewed` 狀態由使用者交給 ChatGPT 審查後自行決定；Codex 不設定、執行或等待此狀態，也不以它作為融合稿名冊條件。若 ChatGPT 審查需要版本資料，來源 URL、章節／頁碼定位與查核日期可作為比對材料；這是供審查者參考的證據紀錄，不是 Codex 的融合撰寫完成 gate。
- 若出版社未公開教學內容或無法取得，可閱讀網路上由學校、教師、學生或其他第三方分享且與該單元相關的課本／講義內容作為研究材料；來源須標示分享者／平台、版本標示、頁次或定位、查核日期及是否為出版社認證，未經驗證不得稱為出版社官方原書。只萃取概念順序、例型、表示法、教學支架與差異，最終教材必須依課綱與 Knowledge Graph 重新組織並以自己的話原創撰寫；不得複製受著作權保護的課本文字、題目、圖表或答案。若分享內容的授權或合法使用界線不明，僅作有限研究與來源定位，不重製其表達，並保留權利／授權待查狀態。
- 版本研究不得只停留在目次、章節名稱或單一公開影音；數理科須比較概念順序、定義、表示法、例型、迷思與應用，社會科須比較時序、史料／資料判讀、因果、尺度與觀點，語文科須比較篇目、段落重點、作者意圖、文體、修辭與注釋涵蓋範圍。
- LLM 必須以官方課綱、KG 與各版本研究紀錄融合撰寫原創正文；不得以批次模板或幾句摘要取代逐單元教學內容。研究或融合未完成時，lesson 與其新題目均維持 `draft`。
- 「每個單元獨立撰寫」是硬性規則：六階段欄位是資料結構，不得共用正文、例題、錯誤說明、互動步驟、題幹骨架或只替換單元名稱；歷史批次模板不得再用於新內容。
- 「每篇每單元重新撰寫」是內容撰寫要求：每一份 lesson 均須依本單元概念脈絡撰寫，不得以固定句型或只換名詞冒充；此要求本身不授權 Codex 進行使用者保留的最終教材審查，也不改變融合稿名冊的客觀登記條件。
- 文字成品必須達到「像不同人寫的」：不同單元要有不同的教學入口、敘事聲音、概念展開順序、例證／比喻、錯誤診斷、提問方式與活動設計；不能每課都用相同開場、相同六段轉折、相同句尾或相同「預測／觀察／解釋／檢核」流程，再填入單元名詞。這是內容獨立性要求，不是要求刻意加入錯字或不自然文風。
- `scripts/audit_lesson_independence.py --strict` 可作為明確要求的自動化診斷；其結果不構成本進行中融合撰寫任務的 gate，不得據此把已登記稿件從完成分子移除或擅自重寫。教材內容最終審查由使用者交 ChatGPT。

## 不可違反的資料規則

- 官方十二年國教課綱是課程事實的 source of truth；每一項課程主張都要有來源紀錄。
- 所有跨版本概念以 `knowledge` 的穩定 ID 為中心；不得用出版商章節名稱取代概念 ID。
- `id` 一經發佈不可任意改名、重用或重新編號。必須淘汰時保留舊 ID 與 `supersededBy` 關係。
- 內容與資料不可 hardcode 到 UI；UI 只能透過資料層/API 讀取經 Schema 驗證的資料。
- 新增或修改 JSON 必須通過對應 `schemas/` 的驗證，且不能留下無來源的事實性欄位。
- 教材與題目僅能使用自編、明確授權或合法公開且可追溯的內容；絕不複製受著作權保護的教科書內容。

## 變更紀律

- 重要決策（資料模型、ID、來源、版本策略、授權界線）要先記入 `docs/DECISIONS.md`。
- 里程碑、數量、風險或工作狀態改變時，同步更新 `docs/CURRENT_STATE.md` 與 `project-state.json`。
- 保留使用者既有內容；不做批量刪除或無關格式化。
- PR/提交應聚焦單一目的，並記錄做過的驗證與未驗證範圍。

## 開始前檢查清單

- [ ] 已閱讀必要文件與目標資料區 README。
- [ ] 已找到對應 Schema 與官方來源。
- [ ] 已確認穩定 ID，不會與既有資料衝突。
- [ ] 已判定內容不侵犯著作權且不會硬編碼到 UI。
- [ ] 已規劃狀態與決策紀錄的同步更新。

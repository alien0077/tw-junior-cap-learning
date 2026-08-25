# 來源政策與登錄

## 權威來源

1. [教育部國教署：新課綱推動相關法令規定](https://www.k12ea.gov.tw/Tw/Common/SinglePage?filter=11C2C6C1-D64E-475E-916B-D20C83896343)：十二年國教總綱與各領域課程綱要的官方索引。
2. [國中教育會考官方網站](https://cap.rcpet.edu.tw/)：會考公告、公開資料與相關說明。

來源 URL、存取日期、文件名稱、版本／發布日期、定位資訊（頁碼、段落或官方識別碼）應寫入資料的 `sources` 或 `provenance`。連結失效時，保留原 URL 並新增可驗證的替代來源，不得靜默覆寫。

## 來源優先序

1. 教育部／國教署正式發布的課綱與公告。
2. 官方教育會考資料與明示可再利用的公開資料。
3. 出版商公開目錄、版本資訊或經合法取得並僅做最小必要登錄的證據。
4. 其他來源只能作為輔助，不能推翻官方課綱。

版本 mapping 必須標示證據類型與信心等級；未核對的線索只能標為 `unverified`，不得作為學生內容或完成度依據。

## M1 官方來源登錄

| 科目 | 資料檔 | 官方索引定位 | 查核日期 |
| --- | --- | --- | --- |
| 國文 | `curriculum/chinese/official-curriculum-index.json` | 一、課程綱要第 3 項 | 2026-08-25 |
| 英文 | `curriculum/english/official-curriculum-index.json` | 一、課程綱要第 9 項 | 2026-08-25 |
| 數學 | `curriculum/math/official-curriculum-index.json` | 一、課程綱要第 12 項 | 2026-08-25 |
| 社會 | `curriculum/social/official-curriculum-index.json` | 一、課程綱要第 16 項 | 2026-08-25 |
| 自然 | `curriculum/science/official-curriculum-index.json` | 一、課程綱要第 17 項 | 2026-08-25 |

本表只證明官方索引已查核，不代表完整的課綱、教材版本或考題資料均已收錄。

## M2 官方課綱 PDF 登錄

五科的細粒度來源已鎖定為國家教育研究院的「國民中小學暨普通型高級中等學校」官方課綱 PDF；各資料檔保留直接 URL、發布日與章節定位。國教院的官方頁面同時列出各文件與發布令日期，作為 PDF 來源的登錄頁。

| 科目 | 官方發布日 | 圖譜範圍 |
| --- | --- | --- |
| 國文 | 2018-01-25 | 學習重點／學習表現、學習內容 |
| 英文 | 2018-04-16 | 學習重點／學習表現、學習內容 |
| 數學 | 2018-07-26 | 學習重點／學習表現、學習內容 |
| 社會 | 2018-10-26 | 國民中學及普通型高中範圍 |
| 自然 | 2018-11-02 | 國民中學教育階段範圍 |

## M2 自然科主題 A 細粒度登錄

- 來源：[十二年國民基本教育課程綱要國民中小學暨普通型高級中等學校－自然科學領域（PDF）](https://www.naer.edu.tw/upload/1/16/doc/820/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%87%AA%E7%84%B6%E7%A7%91%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf)，教育部發布日 2018-11-02，查核日 2026-08-25。
- 範圍：國民中學教育階段學習內容主題 A「物質的組成與特性」，含 Aa、Ab 及 Aa-Ⅳ-1～5、Ab-Ⅳ-1～4。
- 定位：正文第 22～23 頁／PDF 第 26～27 頁；各節點保留對應官方代碼與頁碼。
- 限制：本登錄是單一主題的表格階層拆解；不含其他自然科主題、教材版本 mapping、教材或題庫。

## M2 五科第四學習階段細粒度表格登錄

本批只使用教育部／國家教育研究院正式發布的課程綱要 PDF，查核日均為 2026-08-25。每個 curriculum node 另保存官方 URL、發布日期、正文／PDF 頁碼範圍及官方代碼 locator。

| 科目 | 官方發布日 | 學習表現定位 | 學習內容定位 | 細粒度節點數 |
| --- | --- | --- | --- | ---: |
| 國語文 | 2018-01-25 | 正文 6～11／PDF 8～13 | 正文 12～18／PDF 14～20 | 81 |
| 英語文 | 2018-04-16 | 正文 8～15／PDF 10～17 | 正文 16～20／PDF 18～22 | 134 |
| 數學 | 2018-07-26 | 正文 7～17／PDF 10～20 | 國中逐年級表：正文 36～45／PDF 39～48 | 123 |
| 自然科學 | 2018-11-02 | 正文 21～22／PDF 25～26 | 一般內容正文 22～30／PDF 26～34；跨科正文 30～31／PDF 34～35 | 323 |
| 社會 | 2018-10-26 | 正文 8～12／PDF 12～16 | 歷史正文 18～20／PDF 22～24；地理正文 22～24／PDF 26～28；公民正文 27～36／PDF 31～40 | 356 |

細粒度總計 1017 個 curriculum／Knowledge Graph 節點。圖譜建立 1017 條官方表格階層直接支持的 `partOf`；自然科跨科主題另依官方次主題欄建立 19 條 `relatedTo`。此處的 M2 完成只代表上述第四學習階段官方學習重點表格完成逐碼建模，不代表會考命題範圍、出版社版本 mapping、教材或題庫完成。

## M3 三版本整冊存在性基線

- 主要證據：國家教育研究院「115 學年度國民小學及國民中學教科用書」清冊：https://textbooks.naer.edu.tw/DownLoadFile.aspx?ASParam=TUZIRSs3NSUyNjglMjQlN2QlMWIlMDR1eSUwZWdocCU3ZWZ3JTExd20lMWN1JTBiJTBjJTFiZm4lMDAlMTIlN2V3ZnQlMDMlMWVwJTBiJTBjJTA2JTFkJTFldg%3D%3D
- 國文、數學、自然科學、社會之南一／康軒／翰林第一至第六冊，以及英語之南一／康軒第一至第六冊，均以該清冊作為 `official-government-list` 證據。
- 翰林英語特例：國家教育研究院 115 學年度清冊的國中英語出版者列為佳音、南一、康軒；翰林官方書城則列有 `國中課本-i英語`。因此本專案保留差異：翰林英語 mapping 的證據類型為 `official-publisher-page`，不主張其審定執照出版者為翰林。官方產品總表：https://books.hanlin.com.tw/productall
- 本批 mapping 只建立「冊別存在性 → 各科 learning-content 根節點」的 `supporting` 關係；章節／單元級 mapping 尚待後續逐冊官方目次證據。

## M4 原創 lesson / question 基線

- 五科各建立一份原創 lesson，主題分別為國文議論論據、英語 fact/opinion、數學因式分解、自然科比熱、社會機會成本。
- 每份 lesson 配三題原創單選題，全部只連至本專案穩定 KG ID；`provenance.origin=original`，未引用或改寫出版社課本、習作與題庫。

## M3 康軒章節級 mapping

- 查核日期：2026-08-25。
- 冊別證據：既有國家教育研究院 115 學年度教科用書清冊基線。
- 章節證據：康軒「國中影音高手」官方公開 XML，只取冊次、章節代碼與章節名稱等最小必要中介資料：
  - 國文：https://digitalmaster.knsh.com.tw/all/video/public/j_mandarin.xml
  - 英文：https://digitalmaster.knsh.com.tw/all/video/public/j_english.xml
  - 數學：https://digitalmaster.knsh.com.tw/all/video/public/j_math.xml
  - 自然：https://digitalmaster.knsh.com.tw/all/video/public/j_nature.xml
  - 地理：https://digitalmaster.knsh.com.tw/all/video/public/j_geography.xml
  - 歷史：https://digitalmaster.knsh.com.tw/all/video/public/j_history.xml
  - 公民：https://digitalmaster.knsh.com.tw/all/video/public/j_cs.xml
- 資料規模：五科各六冊，共 30 冊、310 個章節／單元條目；國文 82、英文 34、數學 58、自然 36、社會 100。
- 對照方法：章名先依科目與冊次正規化，再保守連至既有細粒度 KG ID；所有端點已確認存在。出版社來源只證明章節結構，KG 對照屬本專案教學判斷，統一標為 `medium` confidence。
- 限制：官方資源可能隨版本更新；因此資料同時保留查核日與版本說明。此批不含課文、題目或影音內容，也不代表南一、翰林已完成章節級對照。

## M3 翰林國文章節級 mapping

- 查核日期：2026-08-25。
- 官方章節證據：翰林組織網域的「115年翰林國文網頁版PPT」六冊索引：
  - 1上：https://sites.google.com/hanlin.com.tw/112chwebppt/1%E4%B8%8A
  - 1下：https://sites.google.com/hanlin.com.tw/112chwebppt/1%E4%B8%8B
  - 2上：https://sites.google.com/hanlin.com.tw/112chwebppt/2%E4%B8%8A
  - 2下：https://sites.google.com/hanlin.com.tw/112chwebppt/2%E4%B8%8B
  - 3上：https://sites.google.com/hanlin.com.tw/112chwebppt/3%E4%B8%8A
  - 3下：https://sites.google.com/hanlin.com.tw/112chwebppt/3%E4%B8%8B
- 資料規模：六冊共 82 個課次；只擷取課次代碼與名稱，不開啟或保存課本、習作、簡報內容。
- 對照方法：一般課文保守連至篇章主旨與閱讀理解節點；詩詞、文字結構、書法、語法、應用文、標點與資訊檢索等明確單元連至相應細粒度 KG ID。所有端點已確認存在，關係信心標為 `medium`。

## M4 原創內容擴充

- 本批新增五份原創 lesson 與每科三題原創 single-choice question，共 20 個 JSON 檔。
- 新增主題：國文資訊來源可靠性、英文 context clues、數學方程式代回、自然科探究模型、社會媒體識讀。
- 所有內容均為本專案新寫，`provenance.origin=original`，未使用出版社課文、題目或解答；每筆均連至既有 KG ID。

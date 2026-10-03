import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const lesson = JSON.parse(await readFile(new URL("../../lessons/social/lesson-social-content-geo-af-iv-1.json", import.meta.url), "utf8"));
const appSource = await readFile(new URL("../../site/app.js", import.meta.url), "utf8");
const manifest = JSON.parse(await readFile(new URL("../unit-specs.manifest.json", import.meta.url), "utf8"));

assert.equal(lesson.reviewStatus, "reviewed", "completed social content review must remain reviewed while source limitations stay explicit");
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.content.sections.length, 6, "all substantive teaching must be in the field actually shown by the website");
const normalizeParagraph = (text) => text.replace(/[。．.]/g, "");
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body: normalizeParagraph(body) })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body: normalizeParagraph(body) })),
  "learner-visible sections must expose the authored lesson rather than only a one-sentence objective"
);
assert.match(appSource, /const visibleSections = authoredBlocks\.length \? \[\.\.\.extraSections, \.\.\.authoredBlocks\] : contentSections/, "the website preserves both non-duplicate original sections and the complete authored teaching body");
assert.match(appSource, /item\.content\?\.sections \|\| \[\]/, "legacy lessons without a teaching body retain their visible sections");

const text = lesson.content.sections.map((section) => `${section.heading}\n${section.body}`).join("\n");
for (const concept of ["服務分工", "流向資料", "直線八公里", "五十二分鐘", "輪椅使用者", "農地變更", "群體公平", "資料限制", "不同年代的地圖", "交通工具也沒有脫離情境的固定排名", "載量、費用"]) {
  assert.ok(text.includes(concept), `visible lesson must teach the unit-specific idea: ${concept}`);
}
assert.match(`${lesson.content.sections[0].heading}${lesson.content.sections[0].body}`, /就醫.*服務.*往返/);
assert.match(lesson.content.sections[2].body, /甲村.*乙鎮.*丙市.*互相依賴/);
assert.match(lesson.content.sections[3].body, /八公里.*五十二分鐘.*十二公里.*三十五分鐘/);
assert.match(lesson.content.sections[2].body, /港口.*鐵路交會處.*公路轉乘點.*不能只憑新車站.*斷言地方必然繁榮/);
assert.match(lesson.content.sections[4].body, /受益者.*受損者.*客流、環境/);

const nani = lesson.versionResearch.find((entry) => entry.publisher === "nani");
const kanghsuan = lesson.versionResearch.find((entry) => entry.publisher === "kanghsuan");
const hanlin = lesson.versionResearch.find((entry) => entry.publisher === "hanlin");
assert.match(nani.sourceLocator, /pp\.101–103.*校方明列南一版/);
assert.match(nani.licenseBoundary, /不是南一出版社課文/);
assert.match(kanghsuan.sourceLocator, /七下第五課.*只讀索引/);
assert.match(kanghsuan.licenseBoundary, /未播放或複製影音/);
assert.match(hanlin.sourceLocator, /PDF p\.17.*教用架構/);
assert.match(hanlin.findings.concepts.join(" "), /聚落形成.*交通方式.*交通網絡/);
assert.match(hanlin.licenseBoundary, /不宣稱完整學生版章節已讀/);
const hanlinShare = lesson.versionResearch.find((entry) => entry.publisher === "hanlin" && entry.edition.includes("第三方版本標示分享"));
assert.ok(hanlinShare, "the additional directly read Hanlin-labeled third-party chapter must be retained as a separate source");
assert.match(hanlinShare.sourceLocator, /印刷頁47–50/);
assert.match(hanlinShare.sourceLocator, /版次真實性未核實/);
assert.match(hanlinShare.findings.concepts.join(" "), /歷史時序.*運具/);
assert.match(hanlinShare.licenseBoundary, /All Rights Reserved.*授權未由出版社確認/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /第三方翰林版本標示課本分享.*不把它稱為出版社認證原書/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /來源深度不對等.*不.*三版正文融合/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /六段不同功能的可見課文/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /時序地圖問題與運具任務均是本課原創延伸/);

assert.equal(lesson.interactive.type, "settlement-network-map");
assert.equal(lesson.interactive.steps.length, 3);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["B", "B", "A"]);
assert.match(lesson.interactive.steps[0].prompt, /快速道路|通勤時間/);
assert.match(lesson.interactive.steps[0].options.join(" "), /服務|土地|產業|人口流動/);
assert.match(lesson.interactive.steps[0].feedback, /可達性.*條件/);
assert.match(lesson.interactive.steps[1].prompt, /都市人口比例.*鄉村人口/);
assert.match(lesson.interactive.steps[1].feedback, /比例.*絕對量/);
assert.match(lesson.interactive.steps[2].options[0], /所得.*就業.*交通.*服務可近性.*人口/);
assert.match(lesson.interactive.steps[2].feedback, /多指標.*單一數字/);
const unitManifest = manifest.units.find((entry) => entry.lessonId === "cur-social-content-geo-af-iv-1");
assert.equal(unitManifest.publisherEvidence.hanlin, "verified", "directly read version-labeled textbook-content evidence should be synchronized to the unit manifest");
assert.equal(unitManifest.publisherEvidence.nani, "book-level-only");
assert.equal(unitManifest.publisherEvidence.kanghsuan, "book-level-only");

console.log("Geo Af-IV-1 Hanlin-labeled chapter evidence, original historical-node and transport-mode synthesis, six learner-visible sections, and unit-specific interaction: ok");

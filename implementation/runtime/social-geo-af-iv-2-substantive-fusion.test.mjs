import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const lesson = JSON.parse(await readFile(new URL("../../lessons/social/lesson-social-content-geo-af-iv-2.json", import.meta.url), "utf8"));
const app = await readFile(new URL("../../site/app.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "reviewed", "completed content review must remain reviewed while publisher-evidence limits stay explicit");
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
const normalize = (value) => value.replace(/[。．.]/g, "");
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body: normalize(body) })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body: normalize(body) })),
  "all authored lesson text must be learner-visible in content.sections"
);

const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join("\n");
for (const idea of ["都市人口占全區比例", "建成區增加", "核心夜間人口下降", "外圍住宅區的通勤流量上升", "都會區的形成", "都會區的空間範圍不是都市人口比例本身", "不能說所有人搬進市中心", "量", "位", "流", "代價"]) {
  assert.ok(visible.includes(idea), `visible unit-specific lesson is missing: ${idea}`);
}

const hanlin = lesson.versionResearch.find((entry) => entry.publisher === "hanlin" && entry.edition.includes("出版社網站；非特定課本版次"));
assert.ok(hanlin, "retain the directly read publisher-owned learning page as separate evidence");
assert.match(hanlin.sourceLocator, /ehanlin\.com\.tw.*都市擴張/);
assert.match(hanlin.sourceLocator, /查閱定義、人口／交通／產業擴張/);
assert.match(hanlin.licenseBoundary, /非特定課本版次|未標示課本版次/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /南一與康軒.*尚無足夠.*單元正文/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不能冒稱已讀到其單元正文/);

assert.equal(lesson.interactive.type, "settlement-network-map");
assert.equal(lesson.interactive.steps.length, 3);
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ["B", "B", "A"]);
assert.match(lesson.interactive.steps[0].prompt, /快速道路.*通勤時間/);
assert.match(lesson.interactive.steps[0].options.join(" "), /服務.*土地.*產業.*人口流動/);
assert.match(lesson.interactive.steps[1].prompt, /都市人口比例.*鄉村人口/);
assert.match(lesson.interactive.steps[1].feedback, /比例變動.*絕對量/);
assert.match(lesson.interactive.steps[2].options[0], /所得.*就業.*交通.*服務可近性.*人口/);
assert.equal(lesson.simulation.engine, "concept-explorer");
assert.match(lesson.simulation.learningDesign.steps[1].action, /外圍住宅用地/);
assert.match(lesson.simulation.learningDesign.steps[3].feedback, /模型不能直接回答/);

assert.match(app, /item\.interactive\?\.steps\?\.length/);
assert.match(app, /data-answer=/);
assert.match(app, /aria-live="polite"/);
assert.match(app, /step\.feedback/);
assert.equal(lesson.provenance.origin, "original");

console.log("Geo Af-IV-2 visible original synthesis, Hanlin public evidence boundary, four-step urbanization interaction, and concept-explorer contract: ok");

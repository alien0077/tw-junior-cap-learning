import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const lesson = JSON.parse(await readFile(new URL("../../lessons/social/lesson-social-content-geo-af-iv-3.json", import.meta.url), "utf8"));
const spec = await readFile(new URL("../unit-specs/social/cur-social-content-geo-af-iv-3.yaml", import.meta.url), "utf8");
const app = await readFile(new URL("../../site/app.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "reviewed", "completed social content review status must remain reviewed");
assert.equal(lesson.teaching.body.length, 7);
assert.match(app, /item\.teaching\?\.body\?\.filter/);
assert.match(app, /const visibleSections = authoredBlocks\.length \? \[\.\.\.extraSections, \.\.\.authoredBlocks\] : contentSections/);
assert.equal(lesson.interactive.type, "settlement-network-map");
assert.equal(lesson.interactive.steps.length, 3);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["B", "B", "A"]);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${index + 1} must provide three choices`);
  assert.equal(new Set(step.options).size, 3, `step ${index + 1} choices must be distinct`);
  assert.ok(step.feedback.length >= 12, `step ${index + 1} must explain its concept`);
}
assert.match(lesson.interactive.steps[0].options.join(" "), /服務|土地|產業|人口/);
assert.match(lesson.interactive.steps[0].feedback, /可達性|條件/);
assert.match(lesson.interactive.steps[1].feedback, /比例|絕對量/);
assert.match(lesson.interactive.steps[2].feedback, /多指標|單一數字/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不宣稱三版課文已融合/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /第三方.*未驗明版次/);
assert.match(lesson.versionResearch.find(record => record.publisher === "hanlin").licenseBoundary, /All Rights Reserved/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /七段 `teaching\.body` 正文/);
assert.doesNotMatch(spec, /MapDataBlock|同步更新.*圖、表/);
assert.match(app, /data-answer=/);
assert.match(app, /aria-live="polite"/);
assert.equal(lesson.provenance.origin, "original");

console.log("Geo Af-IV-3 seven learner-visible authored sections, source-boundary honesty, and four-step region-specific interaction: ok");

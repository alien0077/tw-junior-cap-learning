import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const lesson = JSON.parse(await readFile(new URL("../../lessons/social/lesson-social-content-geo-af-iv-3.json", import.meta.url), "utf8"));
const spec = await readFile(new URL("../unit-specs/social/cur-social-content-geo-af-iv-3.yaml", import.meta.url), "utf8");
const app = await readFile(new URL("../../site/app.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "draft", "publisher and content-review gates remain open");
assert.equal(lesson.teaching.body.length, 7);
assert.match(app, /item\.teaching\?\.body\?\.filter/);
assert.match(app, /const visibleSections = authoredBlocks\.length \? \[\.\.\.extraSections, \.\.\.authoredBlocks\] : contentSections/);
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["A", "A", "A", "A"]);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${index + 1} must provide three choices`);
  assert.equal(new Set(step.options).size, 3, `step ${index + 1} choices must be distinct`);
  assert.ok(step.feedback.length >= 25, `step ${index + 1} must explain its concept`);
  assert.ok(step.retryHint.length > 15, `step ${index + 1} must provide a useful retry hint`);
}
assert.match(lesson.interactive.steps[0].options.join(" "), /年份|分母/);
assert.match(lesson.interactive.steps[1].feedback, /聚集|互相強化/);
assert.match(lesson.interactive.steps[2].feedback, /待驗證|單一原因/);
assert.match(lesson.interactive.steps[3].feedback, /可近性|指標/);
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

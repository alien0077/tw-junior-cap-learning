import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-5-iv-6.json", import.meta.url), "utf8"));
const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-5-iv-6.yaml", import.meta.url), "utf8");
const visible = new Map(lesson.content.sections.map(({ heading, body }) => [heading, body]));

assert.equal(lesson.reviewStatus, "reviewed", "completed English lesson review status must remain reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.equal(lesson.teaching.body.length, 6);
for (const stage of lesson.teaching.body) {
  assert.equal(visible.get(stage.heading), stage.body, `student page must display complete lesson stage: ${stage.heading}`);
}
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every((item) => /未取得|pending/.test(item.outcome)), "do not claim publisher textbook pages were read");
assert.equal(lesson.versionResearch.length, 3);
assert.ok(lesson.versionResearch.every((item) => item.findings.concepts.length >= 2));
assert.equal(lesson.fusionRecord.versionDifferences.length, 2);
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 3);
assert.ok(lesson.interactive.steps.every((step) => step.options.length === 3 && step.answer && step.retryHint && step.feedback));
assert.match(lesson.teaching.body[2].body, /時間參照/);
assert.match(lesson.teaching.body[3].body, /whether／if/);
assert.match(lesson.teaching.body[5].body, /may／if/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /qaStatus: verified/);
assert.match(spec, /正文未取得/);
console.log("English 5-IV-6 visible authored lesson, provenance limits, guided-choice contract and completed review gate passed");

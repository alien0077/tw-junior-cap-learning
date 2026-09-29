import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const lesson = JSON.parse(await readFile(new URL("../../lessons/social/lesson-social-performance-soc-3d-iv-2.json", import.meta.url), "utf8"));
const shard = JSON.parse(await readFile(new URL("../../site/data-lessons-social.json", import.meta.url), "utf8"));
const spec = await readFile(new URL("../unit-specs/social/cur-social-performance-soc-3d-iv-2.yaml", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "student-visible manuscript and teaching source must match exactly",
);
assert.deepEqual(lesson.versionResearch.map((item) => item.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.fusionRecord.llmSynthesisNote.length >= 80);
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 6);
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ["A", "B", "C", "B", "A", "C"]);
assert.match(lesson.interactive.steps[5].prompt, /遷移情境.*老樹傳說/);
for (const step of lesson.interactive.steps) {
  assert.ok(step.options.length >= 3, `${step.id} needs plausible alternatives`);
  assert.ok(step.feedback.length >= 20, `${step.id} needs explanatory correct feedback`);
  assert.ok(step.retryHint.length >= 12, `${step.id} needs an actionable retry hint`);
}
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /不宣稱有未實作的變項滑桿或動態圖表/);
assert.match(spec, /六題正解序列應為A、B、C、B、A、C/);
assert.match(spec, /qaStatus: untested/, "do not promote QA before browser evidence");

const studentRecord = shard.find((item) => item.id === lesson.id);
assert.ok(studentRecord, "lesson must be present in the student-facing shard");
assert.deepEqual(studentRecord.teaching.body, lesson.teaching.body, "student shard must be rebuilt from current manuscript");
assert.deepEqual(studentRecord.interactive, lesson.interactive, "student shard must carry the current interaction");

console.log("Social Soc3d-IV-2 manuscript, fusion trace, lesson-specific guided choice and student-shard parity: PASS");

import assert from "node:assert/strict";
import fs from "node:fs";

const lesson = JSON.parse(fs.readFileSync(new URL("../../lessons/math/lesson-math-content-a-8-7.json", import.meta.url), "utf8"));
const activity = lesson.interactive;
assert.equal(activity.steps.length, 6, "A-8-7 interaction covers modeling, factoring, completing the square, formula/discriminant, and contextual filtering");
for (const [index, step] of activity.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${index + 1} has three choices`);
  assert.ok(step.options.includes(step.options["ABC".indexOf(step.answer)]), `step ${index + 1} answer key resolves to an option`);
  assert.equal(new Set(step.options).size, 3, `step ${index + 1} has distinct distractors`);
  assert.ok(step.feedback.length >= 24, `step ${index + 1} explains the math, not only correctness`);
}
assert.match(activity.steps[0].options[0], /w＋d/);
assert.match(activity.steps[1].options[0], /w（w＋d）＝a/);
assert.match(activity.steps[2].options[0], /w²＋dw−a＝0/);
assert.match(activity.steps[3].options[0], /（x＋2）²＝3/);
assert.match(activity.steps[3].feedback, /右側成3/);
assert.match(activity.steps[4].options[0], /b²−4ac＝25/);
assert.match(activity.steps[5].options[0], /代數根.*7公分/);

const sources = new Map(lesson.publisherResearch.map(item => [item.publisher, item]));
for (const publisher of ["nani", "kanghsuan", "hanlin"]) {
  assert.ok(sources.get(publisher)?.sourceUrl, `missing ${publisher} source`);
  assert.match(sources.get(publisher).outcome, /本課|材料|索引|筆記/);
}
assert.equal(lesson.reviewStatus, "draft", "fusion authoring does not imply content review");
console.log("A-8-7 publisher-informed interaction, math feedback, source records and draft gate: ok");

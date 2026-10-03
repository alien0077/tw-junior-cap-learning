import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-content-ac-iv-2.json", import.meta.url), "utf8"));
const visible = new Map(lesson.content.sections.map(({ heading, body }) => [heading, body]));

assert.equal(lesson.reviewStatus, "reviewed-content-pending-browser", "content review is complete while browser QA remains pending");
assert.equal(lesson.teaching.body.length, 6, "the authored lesson must retain all six distinct teaching stages");
for (const stage of lesson.teaching.body) {
  assert.equal(visible.get(stage.heading), stage.body, `student lesson must render the complete authored stage: ${stage.heading}`);
}
assert.equal(lesson.content.sections.length, 7, "learner-facing lesson includes its objective plus all six teaching stages");
assert.match(visible.get("讓海報活動從模糊變清楚"), /Which pictures should we use\?/);
assert.match(visible.get("角色改變，說法也要調整"), /May I borrow the scissors for a minute\?/);
assert.match(visible.get("在音訊故障時修復合作"), /The audio cut out\./);
console.log("Ac-IV-2 learner-visible original six-stage lesson and draft gate passed");

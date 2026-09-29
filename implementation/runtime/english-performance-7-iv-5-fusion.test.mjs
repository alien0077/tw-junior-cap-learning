import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-7-iv-5.json", import.meta.url), "utf8"));
assert.equal(lesson.id, "lesson-english-performance-7-iv-5");
assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-7-iv-5"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.fusionRecord.llmSynthesisNote.length >= 80);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.teaching.body.map(section => [section.heading, section.body]), lesson.content.sections.map(section => [section.heading, section.body]));
assert.equal(lesson.interactive.type, "reading-strategy-lab");
assert.equal(lesson.interactive.steps.length, 6);
for (const step of lesson.interactive.steps) {
  assert.ok(step.text && step.prompt && step.retryHint && step.feedback);
  assert.equal(step.options.length, 4);
  assert.ok("ABCD".includes(step.answer));
}
const questions = readdirSync(new URL("../../questions/english", import.meta.url))
  .filter(name => /^question-english-performance-7-iv-5-\d+\.json$/.test(name))
  .map(name => JSON.parse(readFileSync(new URL(`../../questions/english/${name}`, import.meta.url), "utf8")));
assert.equal(questions.length, 10);
for (const question of questions) {
  assert.equal(question.reviewStatus, "draft");
  assert.ok(question.answer.value);
  assert.ok(question.answer.explanation);
  assert.ok(question.solutionStrategy);
  assert.equal(question.solutionSteps.length, 5);
}
console.log("English 7-IV-5 preserved manuscript, source limits, six-stage self-monitoring lab, and ten solved items: PASS");

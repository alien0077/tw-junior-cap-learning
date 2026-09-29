import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const readJson = path => JSON.parse(readFileSync(new URL(path, import.meta.url), "utf8"));
const lesson = readJson("../../lessons/english/lesson-english-performance-8-iv-6.json");
assert.equal(lesson.id, "lesson-english-performance-8-iv-6");
assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-8-iv-6"]);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(
  lesson.teaching.body.map(({ heading, body }) => [heading, body]),
  lesson.content.sections.map(({ heading, body }) => [heading, body]),
);
assert.ok(lesson.teaching.body.every(section => section.body.length > 180));
assert.equal(lesson.versionResearch.length, 3);
assert.ok(lesson.fusionRecord.llmSynthesisNote.includes("不宣稱三版章節比較"));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.equal(step.options.length, 3);
  assert.ok(step.prompt && step.text && step.retryHint.length >= 15 && step.feedback.length >= 20);
  assert.ok(step.answer >= "A" && step.answer <= "C");
}

const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-8-iv-6.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|fusion-review-pending/);
assert.match(spec, /8-IV-6-1/);
assert.match(spec, /8-IV-6-2/);
const manifest = readJson("../unit-specs.manifest.json");
const unit = manifest.units.find(row => row.lessonId === "cur-english-performance-8-iv-6");
assert.equal(unit.component, "GuidedChoiceBlock");

const questions = Array.from({ length: 10 }, (_, index) => readJson(`../../questions/english/question-english-performance-8-iv-6-${index + 1}.json`));
for (const question of questions) {
  assert.equal(question.reviewStatus, "draft");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.equal(question.examPatternRefs.length, 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only"));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
  assert.ok(question.solutionStrategy.length >= 25);
  assert.ok(/[\u4e00-\u9fff]/.test(question.answer.explanation));
  assert.ok(question.options.some(option => option.id === question.answer.value));
}
assert.equal(new Set(questions.map(question => question.solutionStrategy)).size, 10);
console.log("English 8-IV-6 six-section original manuscript, bounded source research, four-step etiquette GuidedChoice, and ten detailed question solutions: PASS");

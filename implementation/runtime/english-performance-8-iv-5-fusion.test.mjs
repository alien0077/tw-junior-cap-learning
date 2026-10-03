import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

// Keep adjacent 8-IV-6's new authored-content contract in the same full English 8 unit test run.
await import("./english-performance-8-iv-6-fusion.test.mjs");

const readJson = path => JSON.parse(readFileSync(new URL(path, import.meta.url), "utf8"));
const lesson = readJson("../../lessons/english/lesson-english-performance-8-iv-5.json");
assert.equal(lesson.id, "lesson-english-performance-8-iv-5");
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-8-iv-5"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every(row => row.sourceLocator.length > 30 && row.findings.concepts.length >= 2));
assert.match(lesson.fusionRecord.llmSynthesisNote, /不是三家指定課本全文/);
assert.equal(lesson.content.sections.length, 7);
assert.equal(lesson.teaching.body.length, 7);
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => [heading, body]), lesson.content.sections.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.content.sections.every(section => section.body.length > 100));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.equal(step.options.length, 3);
  assert.ok(step.prompt && step.text && step.retryHint.length >= 15 && step.feedback.length >= 20);
  assert.ok(step.answer >= "A" && step.answer <= "C");
}

const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-8-iv-5.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /8-Ⅳ-5/);
assert.match(spec, /qaStatus: verified/);
assert.match(spec, /Lesson教材最後內容審查由使用者交ChatGPT處理/);
const manifest = readJson("../unit-specs.manifest.json");
const unit = manifest.units.find(row => row.lessonId === "cur-english-performance-8-iv-5");
assert.equal(unit.component, "GuidedChoiceBlock");
assert.equal(unit.status.qaStatus, "verified");
assert.deepEqual(unit.publisherEvidence, { nani: "pending", kanghsuan: "pending", hanlin: "pending" });

const questions = Array.from({ length: 10 }, (_, index) => readJson(`../../questions/english/question-english-performance-8-iv-5-${index + 1}.json`));
for (const question of questions) {
  assert.equal(question.reviewStatus, "reviewed");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.equal(question.examPatternRefs.length, 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only"));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
  assert.ok(question.solutionStrategy.length >= 20);
  assert.ok(question.answer.explanation.includes(question.answer.value));
  assert.ok(question.options.some(option => option.id === question.answer.value));
}
assert.equal(new Set(questions.map(question => question.solutionStrategy)).size, 10);

console.log("English 8-IV-5 original seven-section lesson, bounded three-publisher-plan evidence, four-step GuidedChoice, and ten solved public-exam-pattern rewrites: PASS");

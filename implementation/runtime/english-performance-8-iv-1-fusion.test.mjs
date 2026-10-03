import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-8-iv-1.json", import.meta.url), "utf8"));
assert.equal(lesson.id, "lesson-english-performance-8-iv-1");
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-8-iv-1"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.fusionRecord.llmSynthesisNote.length >= 80);
assert.equal(lesson.content.sections.length, 7);
assert.equal(lesson.teaching.body.length, 7);
assert.deepEqual(lesson.teaching.body.map(section => [section.heading, section.body]), lesson.content.sections.map(section => [section.heading, section.body]));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.ok(step.prompt && step.text && step.retryHint.length >= 12 && step.feedback);
  assert.equal(step.options.length, 3);
  assert.ok(step.answer >= "A" && step.answer <= "C");
}

const questions = Array.from({ length: 10 }, (_, index) => JSON.parse(readFileSync(
  new URL(`../../questions/english/question-english-performance-8-iv-1-${index + 1}.json`, import.meta.url), "utf8"),
));
assert.equal(new Set(questions.map(question => question.answer.value)).size, 4);
for (const question of questions) {
  assert.equal(question.reviewStatus, "reviewed");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.ok(question.studyReferences.some(url => url.includes("naer.edu.tw")));
  assert.ok(question.examPatternRefs.length >= 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only"));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionStrategy.length >= 20);
  assert.ok(question.answer.explanation.startsWith(`正確答案是${question.answer.value}`));
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
  const correctOption = question.options.find(option => option.id === question.answer.value);
  assert.ok(correctOption, `${question.id}: answer key must resolve to an option`);
}

console.log("English 8-IV-1 learner-visible fusion, three-version evidence boundaries, four-step interaction, and ten answered exam-pattern rewrites: PASS");

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const json = (path) => JSON.parse(readFileSync(new URL(path, import.meta.url), "utf8"));
const lesson = json("../../lessons/english/lesson-english-performance-9-iv-2.json");
assert.equal(lesson.id, "lesson-english-performance-9-iv-2");
assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-9-iv-2"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.match(lesson.versionResearch.find(row => row.publisher === "hanlin").sourceLocator, /PDF第17頁/);
assert.match(lesson.versionResearch.find(row => row.publisher === "kanghsuan").sourceLocator, /無免登入/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不謊稱三版章節融合/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /使用者交ChatGPT/);
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => [heading, body]), lesson.content.sections.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.content.sections.every(section => section.body.length > 100));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["A", "B", "B", "A"]);
assert.ok(lesson.interactive.steps.every(step => step.retryHint.length >= 15 && step.feedback.length >= 20));

const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-9-iv-2.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure/);
assert.match(spec, /PDF第17頁/);
assert.match(spec, /最終lesson內容審查由使用者另交ChatGPT/);
const manifest = json("../unit-specs.manifest.json");
const unit = manifest.units.find(row => row.lessonId === "cur-english-performance-9-iv-2");
assert.equal(unit.component, "GuidedChoiceBlock");
assert.equal(unit.status.qaStatus, "verified");
assert.equal(unit.publisherEvidence.nani, "pending");
assert.equal(unit.publisherEvidence.kanghsuan, "pending");

const questions = Array.from({ length: 10 }, (_, index) => json(`../../questions/english/question-english-performance-9-iv-2-${index + 1}.json`));
for (const question of questions) {
  assert.equal(question.reviewStatus, "draft");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.equal(question.examPatternRefs.length, 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only"));
  assert.ok(question.studyReferences.some(url => url.includes("naer.edu.tw")));
  assert.ok(question.options.some(option => option.id === question.answer.value));
  assert.match(question.answer.explanation, new RegExp(`正確答案是${question.answer.value}`));
  assert.ok(question.answer.explanation.length > 30);
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(/[\u4e00-\u9fff]/.test(question.solutionStrategy));
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
}
assert.equal(new Set(questions.map(question => question.answer.value)).size, 4);
assert.equal(new Set(questions.map(question => question.solutionStrategy)).size, 10);
console.log("English 9-IV-2 authored comparison/classification/ranking lesson, Hanlin evidence limits, four-step guided choice, and ten solved public-exam-pattern rewrites: PASS");

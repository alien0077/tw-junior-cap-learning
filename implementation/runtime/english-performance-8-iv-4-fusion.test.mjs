import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-8-iv-4.json", import.meta.url), "utf8"));
assert.equal(lesson.id, "lesson-english-performance-8-iv-4");
assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-8-iv-4"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every(row => row.sourceLocator.length > 30 && row.findings.concepts.length >= 2));
assert.ok(lesson.versionResearch.every(row => /公校|校方/.test(row.edition)));
assert.match(lesson.fusionRecord.llmSynthesisNote, /不是出版社課本全文/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /維持draft/);
assert.equal(lesson.content.sections.length, 7);
assert.equal(lesson.teaching.body.length, 7);
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => [heading, body]), lesson.content.sections.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.content.sections.every(section => section.body.length > 100));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.equal(new Set(lesson.interactive.steps.map(step => step.id)).size, 4);
for (const step of lesson.interactive.steps) {
  assert.ok(step.prompt && step.text && step.retryHint.length >= 15 && step.feedback.length >= 20);
  assert.equal(step.options.length, 3);
  assert.ok(step.answer >= "A" && step.answer <= "C");
  assert.ok(step.options[step.answer.charCodeAt(0) - 65]);
}

const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-8-iv-4.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /8-Ⅳ-4/);
assert.match(spec, /qaStatus: verified/);
assert.match(spec, /最終lesson教材審查由使用者交ChatGPT處理/);
const manifest = JSON.parse(readFileSync(new URL("../unit-specs.manifest.json", import.meta.url), "utf8"));
const unit = manifest.units.find(row => row.lessonId === "cur-english-performance-8-iv-4");
assert.equal(unit.component, "GuidedChoiceBlock");
assert.equal(unit.status.qaStatus, "verified");
assert.deepEqual(unit.publisherEvidence, { nani: "pending", kanghsuan: "pending", hanlin: "pending" });

const questions = Array.from({ length: 10 }, (_, index) => JSON.parse(readFileSync(
  new URL(`../../questions/english/question-english-performance-8-iv-4-${index + 1}.json`, import.meta.url), "utf8"),
));
for (const question of questions) {
  assert.equal(question.reviewStatus, "draft");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.ok(question.studyReferences.includes(lesson.studyReferences[0]));
  assert.equal(question.examPatternRefs.length, 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only" && ref.locatorLevel === "item" && /第\d+頁第\d+至\d+題/.test(ref.locator)));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
  assert.ok(question.solutionStrategy.length >= 20);
  assert.ok(question.answer.explanation.startsWith(`正確答案是${question.answer.value}`));
  assert.ok(question.options.some(option => option.id === question.answer.value));
}
assert.equal(new Set(questions.map(question => question.solutionStrategy)).size, 10);
assert.ok(new Set(questions.map(question => question.answer.value)).size >= 3);

console.log("English 8-IV-4 seven-section original manuscript, three qualified version-plan sources, four evidence-boundary guided choices, and ten solved public-exam-pattern rewrites: PASS");

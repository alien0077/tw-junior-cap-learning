import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-8-iv-3.json", import.meta.url), "utf8"));
assert.equal(lesson.id, "lesson-english-performance-8-iv-3");
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-8-iv-3"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map(row => row.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every(row => row.sourceLocator.length > 20 && row.findings.concepts.length));
assert.match(lesson.versionResearch.find(row => row.publisher === "nani").licenseBoundary, /not treated as Nan-I textbook evidence/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不宣稱逐頁三版融合/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /維持draft/);
assert.equal(lesson.content.sections.length, 7);
assert.equal(lesson.teaching.body.length, 7);
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => [heading, body]), lesson.content.sections.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.content.sections.every(section => section.body.length > 100));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.ok(step.prompt && step.text && step.retryHint.length >= 15 && step.feedback.length >= 20);
  assert.equal(step.options.length, 3);
  assert.ok(step.answer >= "A" && step.answer <= "C");
}
const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-8-iv-3.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /current-grade-publisher-chapter-evidence-pending/);
assert.match(spec, /public-school-exam-pattern-only-original-rewrite/);
assert.match(spec, /qaStatus: verified/);
const manifest = JSON.parse(readFileSync(new URL("../unit-specs.manifest.json", import.meta.url), "utf8"));
const manifestUnit = manifest.units.find(row => row.lessonId === "cur-english-performance-8-iv-3");
assert.equal(manifestUnit.component, "GuidedChoiceBlock");
assert.equal(manifestUnit.status.qaStatus, "verified");
assert.deepEqual(manifestUnit.publisherEvidence, { nani: "pending", kanghsuan: "pending", hanlin: "pending" });

const questions = Array.from({ length: 10 }, (_, index) => JSON.parse(readFileSync(
  new URL(`../../questions/english/question-english-performance-8-iv-3-${index + 1}.json`, import.meta.url), "utf8"),
));
for (const question of questions) {
  assert.equal(question.reviewStatus, "reviewed");
  assert.equal(question.lessonId, lesson.id);
  assert.deepEqual(question.knowledgeIds, lesson.knowledgeIds);
  assert.ok(question.studyReferences.some(url => url.includes("naer.edu.tw")));
  assert.equal(question.examPatternRefs.length, 2);
  assert.ok(question.examPatternRefs.every(ref => ref.status === "recorded" && ref.reuseDecision === "pattern-only" && /PDF p\./.test(ref.locator)));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionStrategy.length >= 20);
  assert.ok(question.answer.explanation.startsWith(`正確答案是${question.answer.value}`));
  assert.ok(question.solutionSteps.every(step => /[\u4e00-\u9fff]/.test(step)));
  assert.ok(question.options.find(option => option.id === question.answer.value), `${question.id}: answer key must resolve to an option`);
}
assert.equal(new Set(questions.map(question => question.solutionStrategy)).size, 10);

console.log("English 8-IV-3 original seven-section lesson, qualified source limitations, four-step guided choice, and ten solved pattern-only exam rewrites: PASS");

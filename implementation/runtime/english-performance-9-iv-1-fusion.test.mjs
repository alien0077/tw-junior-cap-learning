import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const readJson = (url) => JSON.parse(readFileSync(new URL(url, import.meta.url), "utf8"));
const lesson = readJson("../../lessons/english/lesson-english-performance-9-iv-1.json");
assert.equal(lesson.id, "lesson-english-performance-9-iv-1");
assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-9-iv-1"]);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map((x) => x.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.match(lesson.versionResearch.find((x) => x.publisher === "kanghsuan").sourceLocator, /圖片.*標題預測/);
assert.match(lesson.versionResearch.find((x) => x.publisher === "nani").sourceLocator, /未定位九年級/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /並未提供三版本各自完整/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /使用者交由ChatGPT/);
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.teaching.body.map(({ heading, body }) => [heading, body]), lesson.content.sections.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.content.sections.every((section) => section.body.length > 120));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map((x) => x.answer), ["A", "B", "A", "B"]);
assert.ok(lesson.interactive.steps.every((x) => x.retryHint.length >= 12 && x.feedback.length >= 30));

const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-9-iv-1.yaml", import.meta.url), "utf8");
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure/);
assert.match(spec, /nani-adjacent-grade-plan-only/);
assert.match(spec, /kanghsuan-public-lesson-plan-pattern-only/);
assert.match(spec, /hanlin-grade9-course-plan-only/);
const manifest = readJson("../unit-specs.manifest.json");
const manifestUnit = manifest.units.find((x) => x.lessonId === "cur-english-performance-9-iv-1");
assert.equal(manifestUnit.component, "GuidedChoiceBlock");
assert.equal(manifestUnit.publisherEvidence.kanghsuan, "public-lesson-plan-pattern-only");
assert.deepEqual(manifestUnit.status, { designStatus: "reviewed", implementationStatus: "implemented", qaStatus: "verified" });

const questions = Array.from({ length: 10 }, (_, i) => readJson(`../../questions/english/question-english-performance-9-iv-1-${i + 1}.json`));
for (const q of questions) {
  assert.equal(q.lessonId, lesson.id);
  assert.deepEqual(q.knowledgeIds, lesson.knowledgeIds);
  assert.ok(q.examPatternRefs.length >= 2);
  assert.ok(q.examPatternRefs.every((ref) => ref.status === "recorded" && ref.reuseDecision === "pattern-only"));
  assert.ok(q.options.some((option) => option.id === q.answer.value));
  assert.equal(q.solutionSteps.length, 5);
  assert.ok(/[\u4e00-\u9fff]/.test(q.solutionStrategy));
  assert.ok(q.solutionSteps.every((step) => /[\u4e00-\u9fff]/.test(step)));
}
assert.equal(new Set(questions.map((q) => q.answer.value)).size, 4);
assert.equal(new Set(questions.map((q) => q.solutionStrategy)).size, 10);

console.log("English 9-IV-1 original evidence-bound inference lesson, qualified version sources, four-step guided choice, and ten sourced answer-key items: PASS");

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-learning-performance.json", import.meta.url), "utf8"));
const specText = readFileSync(new URL("../unit-specs/english/cur-english-learning-performance.yaml", import.meta.url), "utf8");

assert.equal(lesson.id, "lesson-english-learning-performance");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.equal(lesson.reviewStatus, "reviewed");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-learning-performance"]);
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
for (const [index, section] of lesson.teaching.body.entries()) {
  assert.equal(lesson.content.sections[index].heading, section.heading);
  assert.equal(lesson.content.sections[index].body, section.body);
  assert.ok(section.body.length > 180, `short teaching section: ${section.heading}`);
}
assert.ok(lesson.fusionRecord.llmSynthesisNote.length >= 80);
assert.deepEqual(lesson.versionResearch.map((entry) => entry.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every((entry) => entry.sourceLocator.length >= 10));
assert.ok(lesson.publisherResearch.every((entry) => /公校計畫|校方計畫/.test(entry.outcome)));
assert.ok(lesson.fusionRecord.versionDifferences.some((entry) => entry.includes("不宣稱為出版社教科書")));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 5);
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ["B", "C", "A", "B", "A"]);
assert.ok(lesson.interactive.steps.every((step) => step.options.length === 3 && step.retryHint.length >= 20 && step.feedback.length >= 40));
assert.match(specText, /lessonId: cur-english-learning-performance/);
assert.match(specText, /component: GuidedChoiceBlock/);
assert.match(specText, /designStatus: reviewed/);
assert.match(specText, /implementationStatus: implemented/);
assert.match(specText, /qaStatus: verified/);
assert.match(specText, /公校計畫不是出版社課本/);
assert.doesNotMatch(specText, /LanguageTimelineBlock|language-structure|滑桿|預測—操作—觀察—解釋/);
console.log("English learning-performance authored fusion, source boundaries, manuscript parity and GuidedChoice contract: PASS");

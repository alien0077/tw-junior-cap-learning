import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const lesson = JSON.parse(fs.readFileSync(path.join(root, "lessons/chinese/lesson-chinese-learning-performance.json"), "utf8"));
const specText = fs.readFileSync(path.join(root, "implementation/unit-specs/chinese/cur-chinese-learning-performance.yaml"), "utf8");

assert.equal(lesson.id, "lesson-chinese-learning-performance");
assert.deepEqual(lesson.knowledgeIds, ["kg-chinese-learning-performance"]);
assert.equal(lesson.reviewStatus, "draft", "final content review remains with the user");
assert.equal(lesson.teaching.body.length, 6, "the umbrella lesson needs six authored teaching sections");
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "the learner-visible lesson sections must exactly match authored teaching, with no stale placeholder sections"
);
assert.ok(lesson.teaching.body.every(section => section.body.length > 100));
assert.ok(lesson.fusionRecord.llmSynthesisNote.length > 100);
assert.equal(lesson.versionResearch.length, 3);
for (const publisher of ["nani", "kanghsuan", "hanlin"]) {
  assert.ok(lesson.versionResearch.some(source => source.publisher === publisher));
}
assert.ok(lesson.versionResearch.every(source => source.licenseBoundary.includes("版本標示") && source.licenseBoundary.includes("不複製")));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 5);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${index + 1} must have three answer choices`);
  assert.ok(["A", "B", "C"].includes(step.answer), `step ${index + 1} answer key must resolve`);
  assert.ok(step.feedback.length > 20, `step ${index + 1} needs an explanation`);
  assert.ok(step.retryHint.length > 10, `step ${index + 1} needs a retry hint`);
}
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["A", "C", "B", "C", "B"]);
assert.ok(specText.includes("component: GuidedChoiceBlock"));
assert.ok(specText.includes("publisher-textbook-chapter-evidence-pending"));
assert.ok(!specText.includes("component: TextEvidenceBlock"));
assert.ok(!specText.includes("content-and-Terra-review-pending"));
console.log("PASS Chinese learning-performance fusion manuscript, evidence boundaries, learner-visible parity, and five-step answer/feedback contract");

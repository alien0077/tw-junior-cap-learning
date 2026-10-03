import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-6-iv-1.json", import.meta.url), "utf8"));
const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-6-iv-1.yaml", import.meta.url), "utf8");

assert.equal(lesson.id, "lesson-english-performance-6-iv-1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-6-iv-1"]);
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.content.sections.length, 6);
assert.deepEqual(lesson.content.sections, lesson.teaching.body.map(({ heading, body }) => ({ heading, body })));
assert.ok(lesson.teaching.body.every(({ body }) => body.length >= 100));
assert.ok(lesson.fusionRecord.llmSynthesisNote.length > 100);
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map((entry) => entry.publisher).sort(), ["hanlin", "kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every((entry) => entry.findings.concepts.length && entry.sourceLocator && entry.licenseBoundary.includes("校方")));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.ok(lesson.interactive.steps.every((step) => step.options.length === 3 && step.retryHint.length > 10 && step.feedback.length > 20));
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ["B", "B", "A", "B"]);
assert.ok(!JSON.stringify(lesson).includes("LanguageTimelineBlock"));
assert.ok(!lesson.publisherResearch.some((entry) => entry.sourceUrl.includes("15342166894673419.pdf")));
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /6-IV-1/);
assert.match(spec, /publisher-textbook-chapter-evidence-pending/);
assert.doesNotMatch(spec, /LanguageTimelineBlock/);
assert.doesNotMatch(spec, /visualizations:.*language-structure/s);

console.log("English 6-IV-1 original fusion, source boundaries, student-page parity and GuidedChoice contract: PASS");

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-6-iv-2.json", import.meta.url), "utf8"));
const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-6-iv-2.yaml", import.meta.url), "utf8");

assert.equal(lesson.id, "lesson-english-performance-6-iv-2");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-6-iv-2"]);
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections, lesson.teaching.body.map(({ heading, body }) => ({ heading, body })));
assert.ok(lesson.teaching.body.every(({ body }) => body.length >= 100));
assert.ok(lesson.fusionRecord.llmSynthesisNote.length > 100);
assert.ok(lesson.fusionRecord.commonCore.length >= 3);
assert.ok(lesson.fusionRecord.versionDifferences.length >= 1);
assert.ok(lesson.fusionRecord.originalAdditions.length >= 3);
assert.deepEqual(lesson.versionResearch.map(({ publisher }) => publisher).sort(), ["kanghsuan", "nani"]);
assert.ok(lesson.versionResearch.every((entry) => entry.findings.concepts.length >= 2 && entry.sourceLocator.includes("PDF") && entry.licenseBoundary.includes("校方")));
assert.ok(lesson.publisherResearch.some((entry) => entry.publisher === "hanlin" && entry.chapterLocator.includes("沒有讀到PDF")));
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(({ answer }) => answer), ["A", "B", "B", "B"]);
assert.ok(lesson.interactive.steps.every((step) => step.options.length === 3 && step.retryHint.length > 15 && step.feedback.length > 20));
assert.ok(!JSON.stringify(lesson).includes("LanguageTimelineBlock"));
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /LanguageTimelineBlock/);
assert.match(spec, /使用者交ChatGPT/);
assert.match(spec, /320px、375px、768px/);
assert.match(spec, /two-version-school-plan-strategy-synthesis-authored/);

console.log("English 6-IV-2 authored fusion, source boundaries, visible parity and GuidedChoice contract: PASS");

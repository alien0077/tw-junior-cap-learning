import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-5-iv-9.json", import.meta.url), "utf8"));
const spec = readFileSync(new URL("../unit-specs/english/cur-english-performance-5-iv-9.yaml", import.meta.url), "utf8");
const visible = new Map(lesson.content.sections.map(({ heading, body }) => [heading, body]));

assert.equal(lesson.id, "lesson-english-performance-5-iv-9");
assert.equal(lesson.reviewStatus, "draft", "lesson content review remains with user's ChatGPT review");
assert.equal(lesson.authoringStandard, "version-fused-v1");
assert.deepEqual(lesson.knowledgeIds, ["kg-english-performance-5-iv-9"]);
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
for (const section of lesson.teaching.body) {
  assert.equal(visible.get(section.heading), section.body);
  assert.ok(section.body.length >= 150, `short section: ${section.heading}`);
}
assert.ok(lesson.teaching.body.some(section => section.body.includes("公告目的") && section.body.includes("下一步")));
assert.ok(lesson.teaching.body.some(section => section.body.includes("may") && section.body.includes("if")));
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every(source => /pending/i.test(source.outcome)));
assert.equal(lesson.versionResearch.length, 3);
assert.ok(lesson.fusionRecord.commonCore.length >= 3);
assert.ok(lesson.fusionRecord.versionDifferences.some(text => text.includes("沒有取得")));
assert.ok(lesson.fusionRecord.originalAdditions.length >= 4);
assert.match(lesson.fusionRecord.llmSynthesisNote, /獨立撰寫/);
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.audioLabel, "英文廣播");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ["A", "B", "C", "A"]);
assert.equal(new Set(lesson.interactive.steps.map(step => step.audioScript)).size, 4);
assert.ok(lesson.interactive.steps.every(step => step.audioScript.length >= 90 && step.audioLanguage === "en-US" && step.options.length === 3 && step.retryHint.length >= 25 && step.feedback.length >= 30));
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /qaStatus: verified/);
assert.match(spec, /public-school-teaching-reference-only/);
assert.match(spec, /人工教材內容審查由使用者另以ChatGPT進行/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure|預測—操作—觀察—解釋/);
console.log("English 5-IV-9 original broadcast-note lesson, evidence limits, visible parity and guided-choice contract pass");

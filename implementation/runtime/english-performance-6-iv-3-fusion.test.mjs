import assert from 'node:assert/strict';
import fs from 'node:fs';

const lesson = JSON.parse(fs.readFileSync(new URL('../../lessons/english/lesson-english-performance-6-iv-3.json', import.meta.url), 'utf8'));
const spec = fs.readFileSync(new URL('../unit-specs/english/cur-english-performance-6-iv-3.yaml', import.meta.url), 'utf8');

assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.authoringStandard, 'version-fused-v1');
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.content.sections.length, 6);
assert.ok(lesson.teaching.body.every(section => section.body.length >= 100));
assert.ok(lesson.fusionRecord.llmSynthesisNote.length >= 80);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不冒稱|不將.*當成/);
assert.match(lesson.versionResearch.find(source => source.publisher === 'hanlin').findings.concepts.join(' '), /未知/);
assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ['A', 'B', 'A', 'B']);
for (const step of lesson.interactive.steps) {
  assert.equal(step.options.length, 3);
  assert.ok(step.feedback.length >= 25);
  assert.ok(step.retryHint.length >= 12);
}
assert.match(lesson.teaching.body[0].body, /校慶|微任務/);
assert.match(lesson.teaching.body[2].body, /圖書館|library/);
assert.match(lesson.teaching.body[4].body, /讀者劇場/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /作品證據|作品或表現痕跡/);
assert.match(spec, /qaStatus: verified/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure/);

console.log('English 6-IV-3 original participation lesson, source limits, six-section contract and GuidedChoice: PASS');

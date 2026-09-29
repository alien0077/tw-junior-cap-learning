import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/chinese/lesson-chinese-content-ac-iv-2.json', import.meta.url)));
const spec = readFileSync(new URL('../unit-specs/chinese/cur-chinese-content-ac-iv-2.yaml', import.meta.url), 'utf8');

assert.equal(lesson.reviewStatus, 'draft', 'unresolved source, rights, and content gates must keep the lesson draft');
assert.equal(lesson.content.sections.length, 7, 'all seven authored sections must be available to the learner');
assert.equal(lesson.teaching.body.length, 7);
for (let i = 0; i < lesson.content.sections.length; i += 1) {
  assert.equal(lesson.teaching.body[i].heading, lesson.content.sections[i].heading, `section ${i + 1} heading mismatch`);
  assert.equal(lesson.teaching.body[i].body, lesson.content.sections[i].body, `section ${i + 1} body is not connected to learner content`);
}
assert.match(lesson.content.sections[3].body, /兩種|歧義|敘事或表態讀法/);
assert.match(lesson.content.sections[4].body, /參考判讀/);
assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 5);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${index + 1} must expose three choices`);
  assert.match(step.answer, /^[ABC]$/);
  assert.ok(step.feedback && step.retryHint, `step ${index + 1} must explain correct and retry paths`);
}
assert.equal(lesson.interactive.steps[4].answer, 'B');
assert.match(lesson.interactive.steps[4].feedback, /兩種|歧義|敘事或表態讀法/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /status: pending[\s\S]*?required: true/);
assert.match(spec, /僅呈現 lesson JSON 的五步選擇/);
assert.match(spec, /lesson JSON 的 retryHint/);
assert.doesNotMatch(spec, /component: TextEvidenceBlock|滑桿、按鈕、鍵盤或點選方式改變|操作後所有相關表徵同步更新/);
assert.match(spec, /完整顯示 lesson 原稿七段 content\.sections/);
assert.match(spec, /南一目前只有目次定位/);

console.log('Ac-Ⅳ-2 learner manuscript parity, five-step GuidedChoice, and truthful spec contract: PASS');

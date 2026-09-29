import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/chinese/lesson-chinese-content-ac-iv-3.json', import.meta.url)));
const spec = readFileSync(new URL('../unit-specs/chinese/cur-chinese-content-ac-iv-3.yaml', import.meta.url), 'utf8');
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
for (let i = 0; i < 6; i += 1) {
  assert.equal(lesson.content.sections[i].heading, lesson.teaching.body[i].heading, `section ${i + 1} heading mismatch`);
  assert.equal(lesson.content.sections[i].body, lesson.teaching.body[i].body, `section ${i + 1} manuscript was not connected to learner content`);
}
assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 3);
for (const [i, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.options.length, 3, `step ${i + 1} must contain three options`);
  assert.match(step.answer, /^[ABC]$/);
  assert.ok(step.feedback && step.retryHint);
}
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ['B', 'A', 'C']);
assert.match(lesson.interactive.steps[0].prompt, /2\.4、2\.9、1\.8/);
assert.match(lesson.interactive.steps[1].feedback, /不等於證明因果/);
assert.match(lesson.interactive.steps[2].feedback, /全校代表性及原因/);
assert.match(lesson.interactive.scenario, /三日單班觀察、四日供湯比較/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /status: pending/);
assert.match(spec, /完整顯示 lesson teaching\.body 六段原稿/);
assert.match(spec, /三步題幹、選項、答案及回饋均由 lesson JSON 提供/);
assert.doesNotMatch(spec, /component: TextEvidenceBlock|預測—操作—觀察|變項同步更新|外部資料失效時/);
assert.match(spec, /三個 publisher slots 均維持 pending/);
assert.ok(lesson.studyReferences.some((url) => url.includes('mbct.mlc.edu.tw')));

console.log('Ac-Ⅳ-3 existing lesson visibility, original evidence reasoning, interaction contract and source boundaries: PASS');

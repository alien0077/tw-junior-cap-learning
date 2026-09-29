import assert from 'node:assert/strict';
import fs from 'node:fs';

const readJson = (path) => JSON.parse(fs.readFileSync(path, 'utf8'));
const lesson = readJson('lessons/science/lesson-science-content-fb-iv-4.json');
const excluded = /升起時刻|升落時段|地平線方位|月食條件|農曆日期/;

assert.equal(lesson.reviewStatus, 'draft', 'publisher and content-review gates are still pending');
assert.equal(lesson.content.sections.length, 6);
assert.ok(lesson.content.sections.every(({ heading, body }) => heading && body.length > 120));
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  'all six authored lesson passages must be learner-visible without drift',
);
assert.ok(lesson.content.sections.slice(0, 4).every(({ body }) => !excluded.test(body)), 'core lesson examples must stay inside Fb-IV-4 scope');
assert.match(lesson.content.sections[4].body, /不屬於本課/);
assert.match(lesson.content.summary, /相對位置/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /資料型態|來源型態/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /沒有宣稱讀完未公開/);
assert.equal(lesson.interactive.steps.length, 4);
assert.ok(lesson.interactive.steps.every((step) => !excluded.test(`${step.prompt} ${step.feedback}`)));
assert.ok(lesson.simulation.learningDesign.steps.every((step) => !excluded.test(`${step.action} ${step.equation} ${step.reason} ${step.feedback}`)));

for (let id = 1; id <= 10; id += 1) {
  const question = readJson(`questions/science/question-science-content-fb-iv-4-${id}.json`);
  assert.equal(question.reviewStatus, 'draft');
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.options.some(({ id: optionId }) => optionId === question.answer.value));
  assert.match(question.solutionSteps.at(-1), new RegExp(`選\\s*${question.answer.value}`), `Q${id} final solution step must agree with its answer key`);
  assert.ok(question.examPatternRefs.length >= 1, `Q${id} must retain a source pointer`);
}

for (const [id, expectedAnswer, requiredPhrase] of [
  [6, 'A', '固定手電筒和觀察點'],
  [8, 'D', '三天後第二張照片左側較亮'],
  [9, 'B', '不按真實比例'],
]) {
  const question = readJson(`questions/science/question-science-content-fb-iv-4-${id}.json`);
  assert.equal(question.answer.value, expectedAnswer);
  assert.ok(`${question.prompt} ${question.options.map(({ text }) => text).join(' ')}`.includes(requiredPhrase));
  assert.equal(question.solutionSteps.length, 5);
  assert.ok(question.solutionSteps.every((step) => step.length > 8));
  assert.equal(question.reviewStatus, 'draft');
}

console.log('Fb-IV-4 scope, six visible sections, source boundaries, four-step interaction, all ten answer/solution alignments, and Q6/Q8/Q9 rewrites passed.');

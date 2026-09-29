import assert from 'node:assert/strict';
import fs from 'node:fs';

const lesson = JSON.parse(fs.readFileSync('lessons/science/lesson-science-content-da-iv-1.json', 'utf8'));

assert.equal(lesson.reviewStatus, 'draft', 'source authentication, full chapter review, and independent content review remain open');
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.content.sections.length, 7, 'objective plus six original authored stages must be learner-visible');
assert.deepEqual(
  lesson.content.sections.slice(1).map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  'learner-facing sections must expose the existing unit-specific lesson, not abbreviated summaries'
);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /透明直尺/);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /官方實驗筆記圖卡/);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /官方實驗影片索引/);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /不同類型且深度不等/);
assert.equal(lesson.simulation.learningDesign.steps.length, 4);
assert.match(lesson.simulation.learningDesign.steps.map(({ action }) => action).join(' '), /低倍率/);
assert.match(lesson.simulation.learningDesign.steps.map(({ action }) => action).join(' '), /洋蔥表皮與口腔上皮/);

console.log('PASS Da-IV-1 source-qualified synthesis, six visible authored stages, microscope interaction contract, and draft gate');

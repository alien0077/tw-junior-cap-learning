import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-6-iv-5.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-6-iv-5.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-6-iv-5');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-6-iv-5']);
assert.equal(lesson.reviewStatus, "reviewed");
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections.map(section => section.heading), lesson.teaching.body.map(section => section.heading));
assert.ok(lesson.content.sections.every(section => section.body.length > 120));
assert.ok(lesson.teaching.body.every(section => section.body.length > 150));

assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.equal(step.options.length, 3);
  assert.equal(new Set(step.options).size, 3);
  assert.ok(['A', 'B', 'C'].includes(step.answer));
  assert.ok(step.retryHint.length > 20);
  assert.ok(step.feedback.length > 30);
}

assert.equal(new Set(lesson.versionResearch.map(record => record.publisher)).size, 3);
assert.deepEqual([...lesson.versionResearch.map(record => record.publisher)].sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.ok(lesson.versionResearch.every(record => record.sourceLocator.startsWith('https://') && record.reviewedAt === '2026-09-28'));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.ok(lesson.fusionRecord.versionDifferences.length >= 1);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.ok(lesson.fusionRecord.llmSynthesisNote.length > 100);
assert.match(lesson.fusionRecord.llmSynthesisNote, /原創|重新組織/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /最終教材審查由使用者ChatGPT執行，不列為Codex gate/);
assert.doesNotMatch(spec, /component: LanguageTimelineBlock/);

console.log('English 6-IV-5 authored lesson, source boundary, fusion record, and guided-choice contract: PASS');

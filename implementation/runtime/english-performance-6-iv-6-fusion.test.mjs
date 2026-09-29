import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-6-iv-6.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-6-iv-6.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-6-iv-6');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-6-iv-6']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections.map(section => section.heading), lesson.teaching.body.map(section => section.heading));
assert.ok(lesson.content.sections.every(section => section.body.length > 120));
assert.ok(lesson.teaching.body.every(section => section.body.length > 120));
assert.equal(new Set(lesson.teaching.body.map(section => section.body)).size, 6);

assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 4);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.id, `step-${index + 1}`);
  assert.equal(step.options.length, 3);
  assert.equal(new Set(step.options).size, 3);
  assert.ok(['A', 'B', 'C'].includes(step.answer));
  assert.ok(step.retryHint.length > 20);
  assert.ok(step.feedback.length > 25);
}

assert.equal(new Set(lesson.versionResearch.map(record => record.publisher)).size, 3);
assert.deepEqual([...lesson.versionResearch.map(record => record.publisher)].sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.ok(lesson.versionResearch.every(record => record.sourceLocator.startsWith('https://') && record.reviewedAt === '2026-09-28'));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.ok(lesson.fusionRecord.versionDifferences.length >= 1);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.match(lesson.fusionRecord.llmSynthesisNote, /未宣稱|不宣稱/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /component: LanguageTimelineBlock/);
assert.match(spec, /publisher-chapter-evidence-unavailable/);

console.log('English 6-IV-6 authored lesson, source boundaries, visible teaching parity, and guided-choice contract: PASS');

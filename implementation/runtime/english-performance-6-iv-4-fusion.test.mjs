import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-6-iv-4.json'), 'utf8'));
const specText = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-6-iv-4.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-6-iv-4');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-6-iv-4']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections.map(x => x.heading), lesson.teaching.body.map(x => x.heading));
assert.ok(lesson.content.sections.every(x => x.body.length >= 100));
assert.ok(lesson.teaching.body.every(x => x.body.length >= 140));
assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 4);
for (const step of lesson.interactive.steps) {
  assert.equal(step.options.length, 3);
  assert.equal(new Set(step.options).size, 3);
  assert.ok(['A', 'B', 'C'].includes(step.answer));
  assert.ok(step.retryHint.length > 20);
  assert.ok(step.feedback.length > 30);
}
assert.ok(lesson.versionResearch.some(x => x.publisher === 'hanlin'));
assert.ok(lesson.versionResearch.some(x => x.publisher === 'kanghsuan'));
assert.ok(lesson.versionResearch.some(x => x.publisher === 'nani'));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.ok(lesson.fusionRecord.llmSynthesisNote.length > 80);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /未取得|不足|待補/);
assert.match(specText, /component: GuidedChoiceBlock/);
assert.match(specText, /外網請求被封鎖時/);
assert.doesNotMatch(specText, /component: LanguageTimelineBlock/);
console.log('English 6-IV-4 lesson, provenance, fusion, and guided-choice contract: PASS');

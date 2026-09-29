import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-7-iv-1.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-7-iv-1.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-7-iv-1');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-7-iv-1']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.authoringStandard, 'version-fused-v1');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections.map(({ heading, body }) => [heading, body]), lesson.teaching.body.map(({ heading, body }) => [heading, body]));
assert.equal(new Set(lesson.teaching.body.map(({ body }) => body)).size, 6);
assert.ok(lesson.teaching.body.every(({ body }) => body.length > 150));

assert.equal(lesson.interactive.type, 'guided-choice');
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(({ answer }) => answer), ['B', 'A', 'B', 'C']);
for (const [index, step] of lesson.interactive.steps.entries()) {
  assert.equal(step.id, `step-${index + 1}`);
  assert.equal(step.options.length, 3);
  assert.equal(new Set(step.options).size, 3);
  assert.ok(step.retryHint.length > 25);
  assert.ok(step.feedback.length > 30);
}

assert.deepEqual(lesson.versionResearch.map(({ publisher }) => publisher).sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.ok(lesson.versionResearch.every(({ sourceLocator, reviewedAt }) => sourceLocator.startsWith('https://') && reviewedAt === '2026-09-28'));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不捏造|不宣稱/);
assert.match(spec, /component: GuidedChoiceBlock/);
assert.doesNotMatch(spec, /component: LanguageTimelineBlock/);
assert.match(spec, /詞性/);
assert.match(spec, /seal/);
assert.match(spec, /\b320\b/);
assert.ok(lesson.studyReferences.every((url) => /^https:\/\//.test(url)));

console.log('English 7-IV-1 fusion writing, source scope, student-page parity and dictionary-context guided-choice: PASS');

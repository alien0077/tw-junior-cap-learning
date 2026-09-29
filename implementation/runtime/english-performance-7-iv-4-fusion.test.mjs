import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-7-iv-4.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-7-iv-4.yaml'), 'utf8');
const visible = lesson.teaching.body.map(({ heading, body }) => ({ heading, body }));

assert.equal(lesson.id, 'lesson-english-performance-7-iv-4');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-7-iv-4']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.authoringStandard, 'version-fused-v1');
assert.equal(visible.length, 6);
assert.deepEqual(lesson.content.sections, visible);
assert.ok(visible.every(({ body }) => body.length > 100));
assert.deepEqual(lesson.versionResearch.map(({ publisher }) => publisher).sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不沿用|不足以作出版社內容比較/);
assert.equal(lesson.interactive.type, 'guided-choice');
assert.deepEqual(lesson.interactive.steps.map(({ answer }) => answer), ['A', 'B', 'C', 'B']);
assert.ok(lesson.interactive.steps.every(({ feedback, retryHint }) => feedback.length > 25 && retryHint.length > 15));
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /qaStatus: verified/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure/);

console.log('English 7-IV-4 discussion transfer fusion, provenance limits, visible lesson and interaction contract: PASS');

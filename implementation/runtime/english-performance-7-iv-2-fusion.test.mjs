import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-7-iv-2.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-7-iv-2.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-7-iv-2');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-7-iv-2']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.authoringStandard, 'version-fused-v1');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(lesson.content.sections.map(({ heading, body }) => [heading, body]), lesson.teaching.body.map(({ heading, body }) => [heading, body]));
assert.ok(lesson.teaching.body.every(({ body }) => body.length > 100));
assert.equal(lesson.interactive.type, 'reading-strategy-lab');
assert.equal(lesson.interactive.steps.length, 5);
assert.deepEqual(lesson.interactive.steps.map(({ answer }) => answer), ['A', 'C', 'B', 'A', 'C']);
assert.ok(lesson.interactive.steps.every(({ feedback, retryHint, text }) => feedback.length > 30 && retryHint.length > 20 && text.length > 30));
assert.deepEqual(lesson.versionResearch.map(({ publisher }) => publisher).sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.ok(lesson.versionResearch.every(({ reviewedAt, sourceLocator }) => reviewedAt === '2026-09-28' && sourceLocator.startsWith('https://')));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.equal(lesson.fusionRecord.versionDifferences.length, 3);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不宣稱|不可等同/);
assert.match(spec, /component: ReadingStrategyLab/);
assert.match(spec, /seed exchange/);
assert.match(spec, /Text says/);
assert.doesNotMatch(spec, /內容、教學法與版權審查通過/);

console.log('English 7-IV-2 existing manuscript registration, visible parity, source boundaries and five-step reading strategy contract: PASS');

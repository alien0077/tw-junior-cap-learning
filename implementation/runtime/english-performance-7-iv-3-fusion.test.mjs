import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const lesson = JSON.parse(fs.readFileSync(path.join(root, 'lessons/english/lesson-english-performance-7-iv-3.json'), 'utf8'));
const spec = fs.readFileSync(path.join(root, 'implementation/unit-specs/english/cur-english-performance-7-iv-3.yaml'), 'utf8');

assert.equal(lesson.id, 'lesson-english-performance-7-iv-3');
assert.deepEqual(lesson.knowledgeIds, ['kg-english-performance-7-iv-3']);
assert.equal(lesson.reviewStatus, 'draft');
assert.equal(lesson.authoringStandard, 'version-fused-v1');
assert.equal(lesson.content.sections.length, 6);
assert.deepEqual(lesson.content.sections, lesson.teaching.body.map(({ heading, body }) => ({ heading, body })));
assert.ok(lesson.teaching.body.every(({ body }) => body.length > 100));
assert.deepEqual(lesson.versionResearch.map(({ publisher }) => publisher).sort(), ['hanlin', 'kanghsuan', 'nani']);
assert.ok(lesson.versionResearch.every(({ reviewedAt }) => reviewedAt === '2026-09-28'));
assert.equal(lesson.fusionRecord.commonCore.length, 3);
assert.equal(lesson.fusionRecord.originalAdditions.length, 3);
assert.match(lesson.fusionRecord.llmSynthesisNote, /版別不能確認|未取得|未知/);
assert.equal(lesson.interactive.type, 'guided-choice');
assert.deepEqual(lesson.interactive.steps.map(({ answer }) => answer), ['A', 'A', 'A', 'A']);
assert.ok(lesson.interactive.steps.every(({ feedback, retryHint }) => feedback.length > 25 && retryHint.length > 15));
assert.match(spec, /component: GuidedChoiceBlock/);
assert.match(spec, /Could you repeat|漏聽/);
assert.doesNotMatch(spec, /LanguageTimelineBlock|language-structure/);
assert.match(spec, /qaStatus: verified/);

console.log('English 7-IV-3 communication repair fusion, source limits, visible lesson and guided-choice contract: PASS');

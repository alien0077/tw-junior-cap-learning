import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-a-7-5.json', import.meta.url)));
const report = JSON.parse(readFileSync(new URL('../reports/a7-5-two-version-substantive-fusion-d329.json', import.meta.url)));
const spec = readFileSync(new URL('../unit-specs/math/cur-math-content-a-7-5.yaml', import.meta.url), 'utf8');
const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join('\n');

assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.equal(lesson.content.sections.length, 5);
assert.match(visible, /x＋y＝35.*2x＋y＝50/s);
assert.match(visible, /3x＋\(2x＋1\)＝21/);
assert.match(visible, /x＝4/);
assert.match(visible, /y＝2×4＋1＝9/);
assert.match(visible, /50－35/);
assert.match(visible, /15＋20＝35/);
assert.match(visible, /2×15＋20＝50/);
assert.match(visible, /2a＋3b＝23、a－2b＝1/);
assert.match(visible, /b＝3/);
assert.match(visible, /a＝7/);
assert.match(visible, /非負整數/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /pp\.18–21/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /南一僅有類南一版索引，正文未讀/);
assert.equal(lesson.versionResearch.filter((entry) => entry.sourceLocator.includes('scribd.com')).length, 2);
for (const entry of lesson.versionResearch.filter((item) => item.sourceLocator.includes('scribd.com'))) {
  assert.match(entry.sourceLocator, /頁|印刷頁/);
  assert.match(entry.licenseBoundary, /All Rights Reserved/);
  assert.match(entry.licenseBoundary, /未核實/);
}
assert.match(spec, /two-version-labeled-third-party-material-read/);
assert.match(spec, /nani-publisher-body-unread/);
assert.match(spec, /qaStatus: (?:untested|passed|verified)/);
assert.equal(report.gates.publisherEvidenceSlots, 'all pending; no promotion');
assert.equal(report.gates.lessonReviewStatus, 'draft');
for (const trace of report.synthesisTrace) assert.ok(trace.sourceInsight && trace.lessonLocation && trace.originalDecision);

console.log('A-7-5 source-to-visible fusion, original derivations, rights limits, and content-review/evidence-boundary gates: ok');

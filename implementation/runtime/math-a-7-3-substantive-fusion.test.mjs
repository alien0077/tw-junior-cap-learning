import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-a-7-3.json', import.meta.url)));
const report = JSON.parse(readFileSync(new URL('../reports/a7-3-substantive-fusion-d327.json', import.meta.url)));
const sections = lesson.content.sections;

assert.equal(sections.length, 3, 'A-7-3 must expose its three authored teaching sections in the learner-facing content field');
assert.match(sections[0].body, /固定費|只付一次/);
assert.match(sections[1].body, /兩邊同減|移項變號/);
assert.match(sections[2].body, /同乘6|代回原式/);
assert.equal(lesson.reviewStatus, 'draft', 'publisher/content gates must not be bypassed');
assert.equal(report.lessonId, lesson.id);
assert.equal(report.gates.naniPublisherTextbookBody, 'not read');
assert.equal(report.gates.kanghsuanPublisherTextbookBody, 'not read');
assert.equal(report.gates.hanlinPublisherAuthenticityAndReuseRights, 'unverified third-party share');
assert.equal(report.gates.publisherEvidenceSlots, 'pending');
for (const locator of ['pp.176-177', 'pp.178-180', 'pp.184-188']) {
  assert.ok(report.sourceComparison[0].locator.includes(locator), `missing page-located source evidence: ${locator}`);
}
for (const trace of report.synthesisTrace) {
  assert.ok(trace.sourceInsight && trace.lessonLocation && trace.originalDecision, 'every fusion trace needs source, visible destination, and an original instructional decision');
}

console.log('A-7-3 substantive fusion trace, visible teaching, and draft gates: ok');

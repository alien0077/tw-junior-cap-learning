import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-a-7-4.json', import.meta.url)));
const report = JSON.parse(readFileSync(new URL('../reports/a7-4-two-version-substantive-fusion-d328.json', import.meta.url)));
const spec = readFileSync(new URL('../unit-specs/math/cur-math-content-a-7-4.yaml', import.meta.url), 'utf8');
const sectionText = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join('\n');

assert.equal(lesson.reviewStatus, 'draft');
assert.match(sectionText, /一道篩選條件/);
assert.match(sectionText, /同一組數/);
assert.match(sectionText, /x\+y=18/);
assert.match(sectionText, /2x\+y=30/);
assert.match(sectionText, /12\+6=18/);
assert.match(sectionText, /2×12\+6=30/);
assert.match(sectionText, /10\+8=18/);
assert.match(sectionText, /2×10\+8=28/);
assert.match(sectionText, /不等於30/);
assert.match(lesson.content.sections[1].body, /（12，6）與（6，12）/);
assert.match(lesson.content.sections[3].body, /不能通關/);

const kanghsuan = lesson.versionResearch.find((entry) => entry.edition.includes('康軒版七下基礎自學講義'));
const hanlin = lesson.versionResearch.find((entry) => entry.edition.includes('翰林國中數學七下課本'));
assert.ok(kanghsuan && hanlin, 'both source-located version-labeled readings must be retained');
assert.match(kanghsuan.sourceLocator, /頁14–16/);
assert.match(hanlin.sourceLocator, /P36–37.*598–664/);
assert.match(kanghsuan.licenseBoundary, /All Rights Reserved.*授權未核實/);
assert.match(hanlin.licenseBoundary, /All Rights Reserved.*授權未核實/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /二個版本標示材料主導/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /南一正文仍未取得/);
assert.match(spec, /kanghsuan-labeled-third-party-study-handout-read-pages-14-16/);
assert.match(spec, /publisher-evidence-pending/);
assert.match(report.fusionClassification, /two-version-labeled/);
assert.equal(report.gates.publisherEvidenceSlots, 'all pending; no promotion');
assert.equal(report.gates.naniPublisherBody, 'not read; course map/school plan only');
for (const trace of report.synthesisTrace) {
  assert.ok(trace.sourceInsight && trace.lessonLocation && trace.originalDecision);
}

console.log('A-7-4 two-source fusion trace, visible lesson, and pending gates: ok');

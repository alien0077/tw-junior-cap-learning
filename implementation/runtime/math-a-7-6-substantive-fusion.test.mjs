import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-a-7-6.json', import.meta.url), 'utf8'));
const spec = readFileSync(new URL('../unit-specs/math/cur-math-content-a-7-6.yaml', import.meta.url), 'utf8');
const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join('\n');
const research = lesson.versionResearch;

assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.match(lesson.updatedAt, /^2026-\d{2}-\d{2}$/, 'updatedAt must remain a valid review date without freezing the test to an obsolete day');
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.interactive.steps.length, 4);
assert.equal(lesson.simulation.engine, 'math-system-graph');

// Original learner-facing sequence: construct a line, prove the one common point,
// diagnose visual/coordinate errors, and transfer the reasoning to a new context.
assert.match(visible, /2x−y＝2.*（0，−2）.*（2，2）/s);
assert.match(visible, /（8\/3，10\/3）.*8\/3＋10\/3＝18\/3＝6.*2×8\/3−10\/3＝6\/3＝2/s);
assert.match(visible, /整數座標作圖.*交點.*不是整數格點.*不要.*（3，3）/s);
assert.match(visible, /（3，3）.*第一式得到6.*第二式.*3.*不成立/s);
assert.match(visible, /y＝3.*水平.*x＝−1.*鉛垂/s);
assert.match(visible, /（2.2，3.8）.*8.2.*不是共同解/s);
assert.match(visible, /校園導覽圖.*（−1，3）/s);
assert.match(visible, /x\+y=5.*x−y=1.*（3，2）/s);
assert.match(lesson.fusionRecord.llmSynthesisNote, /南一對齊課程頁.*康軒校方教學計畫.*翰林官方索引/s);
assert.match(lesson.fusionRecord.llmSynthesisNote, /版本真實性及授權未核實.*翰林可讀教材.*待完成/);
assert.ok(research.some((r) => r.publisher === 'nani'));
assert.ok(research.some((r) => r.publisher === 'kanghsuan'));
assert.ok(research.some((r) => r.publisher === 'hanlin'));
assert.ok(research.some((r) => r.publisher === 'nani' && r.sourceLocator.includes('p.87') && r.sourceLocator.includes('fliphtml5.com')));
assert.ok(research.some((r) => r.publisher === 'kanghsuan' && r.sourceLocator.includes('頁52–65') && r.sourceLocator.includes('www.scribd.com')));
assert.ok(research.filter((r) => r.sourceLocator.includes('fliphtml5.com') || r.sourceLocator.includes('www.scribd.com')).every((r) => r.licenseBoundary.includes('權利')));
assert.ok(research.some((r) => r.edition.includes('校方課程計畫')));
assert.equal(lesson.publisherResearch.filter((r) => ['nani', 'kanghsuan', 'hanlin'].includes(r.publisher) && r.status === 'verified').length, 0);

// Exact arithmetic and coordinate counterexamples used in both lesson/spec.
assert.equal(8 + 10, 18, 'the first equation evaluates to 18/3 = 6');
assert.equal(2 * 8 - 10, 6, 'the second equation evaluates to 6/3 = 2');
assert.equal(2 * 2 - 4, 0);
assert.equal(2 * 3 - 3, 3);
assert.match(spec, /第二式實得 0≠2/);
assert.match(spec, /qaStatus: untested/);
assert.match(spec, /nani:\s*\n\s*status: pending/);
assert.match(spec, /kanghsuan:\s*\n\s*status: pending/);
assert.match(spec, /hanlin:\s*\n\s*status: pending/);
assert.match(spec, /publisher-index-only-pending/);
assert.match(spec, /school-pacing-plan-cross-check-not-publisher-text/);
assert.match(spec, /public-aligned-sequence-limited-evidence/);
assert.match(spec, /third-party-version-labeled-sample-limited-research/);
assert.match(spec, /third-party-version-labeled-material-limited-research/);
assert.equal(lesson.simulation.sourceRefs.length, lesson.studyReferences.length);
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);

const simulationSource = readFileSync(new URL('../../site/simulations.js', import.meta.url), 'utf8');
const dom = new JSDOM('<!doctype html><main id="root"></main>', { url: 'https://example.test/', runScripts: 'outside-only' });
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector('#root');
root.innerHTML = dom.window.LearningSimulations.render(lesson, 'a7-6-fusion-test');
assert.match(root.textContent, /（8\/3，10\/3）/); // sum=6 => x=8/3 and y=10/3
assert.equal(root.querySelectorAll('svg .sim-line').length, 2);
assert.ok(root.querySelector('svg .sim-line-secondary'), 'the second line needs a non-color visual distinction');
assert.equal(root.querySelector('.sim-design-steps').getAttribute('role'), 'group');
assert.match(root.querySelector('svg').getAttribute('aria-label'), /交點為（8\/3，10\/3）/);
const sumSlider = root.querySelector('[data-sim-control="sum"]');
sumSlider.value = '9';
sumSlider.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
assert.match(root.textContent, /（11\/3，16\/3）/);
assert.match(root.querySelector('svg').getAttribute('aria-label'), /交點為（11\/3，16\/3）/);

console.log('A-7-6 original fusion, arithmetic, source limits, interaction, and content-review/evidence-boundary gates: ok');

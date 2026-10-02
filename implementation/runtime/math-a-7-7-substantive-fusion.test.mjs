import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { JSDOM } from 'jsdom';

const lesson = JSON.parse(readFileSync(new URL('../../lessons/math/lesson-math-content-a-7-7.json', import.meta.url), 'utf8'));
const spec = readFileSync(new URL('../unit-specs/math/cur-math-content-a-7-7.yaml', import.meta.url), 'utf8');
const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join('\n');
assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(step => step.answer), ['A', 'A', 'A', 'A']);
assert.match(lesson.interactive.steps[0].options[0], /x≥12/);
assert.match(lesson.interactive.steps[1].options[0], /x＞12.*12 不符合/);
assert.match(lesson.interactive.steps[3].options[0], /18 實心、26 空心/);
assert.equal(lesson.simulation.engine, 'math-inequality-range');
assert.equal(lesson.simulation.sourceRefs.length, lesson.studyReferences.length);
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);

// Each limited version-labeled source has a distinct teaching consequence in the visible lesson.
for (const publisher of ['nani', 'kanghsuan', 'hanlin']) {
  assert.ok(lesson.versionResearch.some(source => source.publisher === publisher && source.edition.includes('第三方分享')));
}
assert.match(visible, /至少.*高於.*T≥18.*T＞18/s);
assert.match(visible, /代入.*18.*26.*19\.5/s);
assert.match(visible, /18 畫實心、26 畫空心.*線段/s);
assert.match(visible, /座位.*整數.*溫度/s);
assert.match(visible, /下一課/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /第三方有限節錄.*權利.*draft/);
assert.match(spec, /visible-original-synthesis-traceable/);
assert.match(spec, /limited-version-labeled-teaching-evidence/);
assert.match(spec, /qaStatus: untested/);
assert.match(spec, /nani:\s*\n\s*status: pending/);
assert.match(spec, /kanghsuan:\s*\n\s*status: pending/);
assert.match(spec, /hanlin:\s*\n\s*status: pending/);
assert.doesNotMatch(visible, /除以負數|移項/);

const dom = new JSDOM('<!doctype html><main id="root"></main>', { url: 'https://example.test/', runScripts: 'outside-only' });
dom.window.eval(readFileSync(new URL('../../site/simulations.js', import.meta.url), 'utf8'));
const root = dom.window.document.querySelector('#root');
root.innerHTML = dom.window.LearningSimulations.render(lesson, 'a7-7-range-test');
assert.match(root.textContent, /x ≥ 12/);
assert.match(root.textContent, /11 不符合；12 符合；13 符合/);
assert.match(root.querySelector('svg').getAttribute('aria-label'), /端點包含/);
root.querySelector('[data-inequality-relation="greater"]').click();
assert.match(root.textContent, /x ＞ 12/);
assert.match(root.textContent, /12 不符合；13 符合/);
assert.match(root.querySelector('svg').getAttribute('aria-label'), /端點不包含/);
root.querySelector('[data-inequality-relation="at-most"]').click();
assert.match(root.textContent, /x ≤ 12/);
assert.match(root.querySelector('svg').getAttribute('aria-label'), /向左延伸/);
const slider = root.querySelector('[data-sim-control="boundary"]');
slider.value = '14';
slider.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
assert.match(root.textContent, /x ≤ 14/);
assert.equal(root.querySelector('[data-inequality-relation="at-most"]').getAttribute('aria-pressed'), 'true');
console.log('A-7-7 source-informed original fusion, scope, interactive range, and content-review/evidence-boundary gates: ok');

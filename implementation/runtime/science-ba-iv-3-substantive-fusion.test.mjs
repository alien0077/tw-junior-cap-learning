import assert from 'node:assert/strict';
import fs from 'node:fs';

const lesson = JSON.parse(fs.readFileSync('lessons/science/lesson-science-content-ba-iv-3.json', 'utf8'));
const spec = fs.readFileSync('implementation/unit-specs/science/cur-science-content-ba-iv-3.yaml', 'utf8');
const manifest = JSON.parse(fs.readFileSync('implementation/unit-specs.manifest.json', 'utf8'));
const row = manifest.units.find((item) => item.lessonId === 'cur-science-content-ba-iv-3');

assert.equal(lesson.reviewStatus, 'content-reviewed', 'content review may be complete while publisher evidence remains explicitly incomplete');
assert.equal(lesson.versionResearch.length, 3);
assert.deepEqual(lesson.versionResearch.map((source) => source.publisher).sort(), ['hanlin', 'kanghsuan', 'nani']);

const hanlin = lesson.versionResearch.find((source) => source.publisher === 'hanlin');
assert.match(hanlin.sourceLocator, /1-1約 p\.12/);
assert.match(hanlin.findings.concepts.join(' '), /吸熱/);
assert.match(hanlin.findings.concepts.join(' '), /放熱/);
assert.match(hanlin.licenseBoundary, /局部節錄/);

const nani = lesson.versionResearch.find((source) => source.publisher === 'nani');
assert.match(nani.findings.concepts.join(' '), /未提供八下 Ba-Ⅳ-3/);
const kanghsuan = lesson.versionResearch.find((source) => source.publisher === 'kanghsuan');
assert.match(kanghsuan.findings.concepts.join(' '), /未呈現 Ba-Ⅳ-3/);

assert.match(lesson.fusionRecord.commonCore.join(' '), /不能把南一資源頁或康軒章節索引當作三版共同教材證據/);
assert.match(lesson.fusionRecord.versionDifferences.join(' '), /翰林 111 版課本節錄/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /只有翰林目前提供直接內容證據/);
assert.equal(lesson.teaching.body.length, 6);
assert.equal(new Set(lesson.teaching.body.map((section) => section.heading)).size, 6);
assert.equal(lesson.content.sections.length, 7, 'objectives plus all six original teaching stages must render to learners');
assert.deepEqual(
  lesson.content.sections.slice(1).map(({ heading }) => heading),
  lesson.teaching.body.map(({ heading }) => heading),
  'all authored lesson stages must remain learner-visible in the same sequence'
);
for (const [index, section] of lesson.content.sections.slice(1).entries()) {
  assert.ok(section.body.length >= 80, `visible teaching stage ${index + 1} must retain substantive learner-facing content`);
}
assert.equal(lesson.interactive.type, 'scientific-investigation');
assert.equal(lesson.simulation.engine, 'science-energy-lab');
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);
assert.match(lesson.simulation.learningDesign.steps.map((step) => step.action).join(' '), /系統邊界/);

assert.match(spec, /component: SystemRelationshipBlock/);
assert.match(spec, /hanlin:\n        status: verified/);
assert.match(spec, /nani:\n        status: pending/);
assert.match(spec, /kanghsuan:\n        status: pending/);
assert.match(spec, /只有翰林官方課本節錄直接支持/);
assert.doesNotMatch(spec, /component: ParticleModelBlock/);
assert.equal(row.component, 'SystemRelationshipBlock');
assert.equal(row.publisherEvidence.hanlin, 'verified');
assert.equal(row.publisherEvidence.nani, 'book-level-only');
assert.equal(row.publisherEvidence.kanghsuan, 'book-level-only');
assert.equal(row.status.qaStatus, 'untested');

console.log('PASS Ba-IV-3 source-to-synthesis, learner-visible body, interaction, manifest parity, and fail-closed draft gate');

import assert from "node:assert/strict";
import fs from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(fs.readFileSync("lessons/science/lesson-science-content-ca-iv-2.json", "utf8"));
const spec = fs.readFileSync("implementation/unit-specs/science/cur-science-content-ca-iv-2.yaml", "utf8");
const manifest = JSON.parse(fs.readFileSync("implementation/unit-specs.manifest.json", "utf8"));
const row = manifest.units.find((unit) => unit.lessonId === "cur-science-content-ca-iv-2");
const simSource = fs.readFileSync("site/simulations.js", "utf8");

assert.equal(lesson.reviewStatus, "draft");
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.content.sections.length, 7, "objective plus all six authored stages must be learner-visible");
assert.deepEqual(
  lesson.content.sections.slice(1).map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "learner-visible instruction must match the authored unit lesson exactly"
);

const research = Object.fromEntries(lesson.versionResearch.map((record) => [record.publisher, record]));
assert.match(research.hanlin.sourceLocator, /material\.hle\.com\.tw.*34–36/);
assert.match(research.hanlin.findings.concepts.join(" "), /未知氣體性質/);
assert.match(research.nani.licenseBoundary, /pending/);
assert.match(research.kanghsuan.licenseBoundary, /pending/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /單一版本參照加原創補充/);
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);
assert.equal(lesson.simulation.engine, "concept-explorer");
assert.equal(lesson.simulation.model, "ca-iv-2-solution-identification");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map((step) => step.answer), ["B", "B", "A", "C"]);
assert.ok(lesson.interactive.steps.every((step) => step.retryHint && step.feedback));
assert.match(spec, /hanlin:\n        status: verified/);
assert.match(spec, /nani:\n        status: pending/);
assert.match(spec, /kanghsuan:\n        status: pending/);
assert.equal(row.component, "EvidenceLabBlock");
assert.equal(row.publisherEvidence.hanlin, "verified");
assert.equal(row.status.qaStatus, "untested");

const dom = new JSDOM("<!doctype html><html><body></body></html>", { url: "https://example.test/", runScripts: "outside-only" });
dom.window.eval(simSource);
const root = dom.window.document.body;
root.innerHTML = dom.window.LearningSimulations.render(lesson, "ca-iv-2-regression");
let simulation = root.querySelector("[data-simulation-lesson]");
assert.match(simulation.querySelector("header .tag").textContent, /概念探索工作臺/);
assert.equal(simulation.querySelectorAll("[data-design-step]").length, 4);
assert.match(simulation.textContent, /虛擬微量鑑定台/);
assert.match(simulation.textContent, /不是實驗步驟/);
assert.match(simulation.querySelector('[aria-label="未知樣品瓶"]').value, /X/);

const testSelect = () => simulation.querySelector('[data-chemical-control="test"]');
testSelect().value = "carbonateCheck";
testSelect().dispatchEvent(new dom.window.Event("change", { bubbles: true }));
simulation = root.querySelector("[data-simulation-lesson]");
simulation.querySelector('[data-chemical-action="run"]').click();
assert.match(root.textContent, /石灰水後變混濁|石灰水變混濁/);
assert.match(root.textContent, /支持生成二氧化碳/);

const sampleSelect = () => root.querySelector('[data-chemical-control="sample"]');
sampleSelect().value = "Y";
sampleSelect().dispatchEvent(new dom.window.Event("change", { bubbles: true }));
root.querySelector('[data-chemical-control="test"]').value = "litmus";
root.querySelector('[data-chemical-control="test"]').dispatchEvent(new dom.window.Event("change", { bubbles: true }));
root.querySelector('[data-chemical-action="run"]').click();
assert.match(root.textContent, /石蕊呈紅色/);
assert.match(root.textContent, /支持稀鹽酸/);

const controls = root.querySelector('[data-chemical-control="control"]');
controls.value = "blank";
controls.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
root.querySelector('[data-chemical-action="run"]').click();
assert.match(root.textContent, /空白對照沒有顯色或產氣變化/);
assert.match(root.textContent, /不能用來判定未知樣品身分/);

console.log("PASS Ca-IV-2 visible six-stage lesson, one-source fusion provenance, unique answer hints, virtual chemical identification and blank/control results; lesson remains draft");

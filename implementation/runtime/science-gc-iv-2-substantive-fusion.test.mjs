import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/science/lesson-science-content-gc-iv-2.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");
const spec = await readFile(new URL("../unit-specs/science/cur-science-content-gc-iv-2.yaml", import.meta.url), "utf8");
const manifest = JSON.parse(await readFile(new URL("../unit-specs.manifest.json", import.meta.url), "utf8"));

assert.equal(lesson.reviewStatus, "draft", "publisher and content review gates remain open");
assert.equal(lesson.content.sections.length, 6, "all six unit-authored teaching sections must be student-visible");
assert.deepEqual(
  lesson.content.sections.map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "student-visible lesson and authored teaching must remain in parity",
);
assert.equal(lesson.simulation.model, "pond-food-web");
assert(lesson.simulation.sourceRefs.some((url) => url.includes("resource.hle.com.tw")), "simulation provenance must include the read publisher study aid");
assert.match(lesson.fusionRecord.commonCore.join(" "), /南一與康軒目前可核實資料只有校方課程定位/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /證據粒度不同/);
assert.match(spec, /生產者、消費者、分解者[\s\S]*共同影響系統功能/);
assert.match(spec, /publisherEvidence:[\s\S]*?nani:[\s\S]*?status: pending/);
const manifestUnit = manifest.units.find((item) => item.lessonId === "cur-science-content-gc-iv-2");
assert.equal(manifestUnit.publisherEvidence.hanlin, "verified", "workbench manifest must match this unit's verified Hanlin source slot");
assert.equal(manifestUnit.publisherEvidence.nani, "book-level-only");
assert.equal(manifestUnit.publisherEvidence.kanghsuan, "book-level-only");

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/", runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const rootNode = dom.window.document.querySelector("#root");
rootNode.innerHTML = dom.window.LearningSimulations.render(lesson, "fusion-regression");
const simulation = rootNode.querySelector("[data-simulation-lesson]");
assert.match(simulation.textContent, /分解者/);
assert.match(simulation.textContent, /未擾動示意/);
const disturbance = simulation.querySelector('[data-sim-control="disturbance"]');
disturbance.value = "2";
disturbance.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
const updated = rootNode.querySelector("[data-simulation-lesson]");
assert.match(updated.textContent, /水草大幅減少的假設情境/);
assert.match(updated.textContent, /不能由此模型推定池塘必然崩解/);
assert.equal(updated.querySelector('[data-sim-control="disturbance"]').value, "2");

console.log("Gc-IV-2: six visible authored sections, honest publisher boundary, draft gate, and disturbance-driven food-web model verified");

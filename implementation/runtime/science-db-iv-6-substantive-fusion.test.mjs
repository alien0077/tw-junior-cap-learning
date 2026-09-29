import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/science/lesson-science-content-db-iv-6.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "draft", "incomplete publisher, rights, and content-review gates must remain draft");
assert.equal(lesson.updatedAt, "2026-09-28");
assert.equal(lesson.content.sections.length, 6);
assert.deepEqual(lesson.content.sections, lesson.teaching.body.map(({ heading, body }) => ({ heading, body })), "the full six-part original lesson must be learner-visible");
assert.equal(lesson.simulation.model, "plant-transport");
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every(({ outcome }) => /三版本融合審查尚未完成/.test(outcome)));
assert.match(lesson.fusionRecord.versionDifferences.join("\n"), /證據強度不對等.*不能聲稱已完成三版正文逐頁比較/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /原創融合草稿/);
assert.match(lesson.versionResearch.find(({ publisher }) => publisher === "hanlin").sourceLocator, /p\.106–111/);
assert.match(lesson.versionResearch.find(({ publisher }) => publisher === "kanghsuan").licenseBoundary, /內頁/);
assert.match(lesson.versionResearch.find(({ publisher }) => publisher === "nani").licenseBoundary, /權限未核實/);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "plant-transport-test");
let simulation = root.querySelector('[data-simulation-lesson$=":plant-transport-test"]');
assert.ok(simulation.querySelector(".sim-plant-transport"));
assert.match(simulation.textContent, /根 → 莖（木質部）→ 葉/);
assert.match(simulation.textContent, /成熟葉片 → 果實/);
assert.match(simulation.textContent, /不計算真實運輸速率或水量/);
assert.equal(simulation.querySelectorAll("[data-transport-choice='source']").length, 2);
assert.equal(simulation.querySelectorAll("[data-transport-choice='sink']").length, 3);

let control = simulation.querySelector('[data-transport-choice="source"][data-value="storage"]');
control.focus();
control.click();
simulation = root.querySelector('[data-simulation-lesson$=":plant-transport-test"]');
assert.match(simulation.querySelector(".sim-plant-phloem").textContent, /儲存器官（例如塊莖） → 果實/);
assert.equal(dom.window.document.activeElement.dataset.value, "storage", "choice updates must preserve keyboard focus");

control = simulation.querySelector('[data-transport-choice="sink"][data-value="shoot"]');
control.click();
simulation = root.querySelector('[data-simulation-lesson$=":plant-transport-test"]');
assert.match(simulation.querySelector(".sim-plant-phloem").textContent, /儲存器官（例如塊莖） → 生長中的芽／嫩梢/);

const transpiration = simulation.querySelector('[data-sim-control="transpiration"]');
transpiration.focus();
transpiration.value = "5";
transpiration.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
simulation = root.querySelector('[data-simulation-lesson$=":plant-transport-test"]');
assert.match(simulation.textContent, /蒸散條件目前設定為較強/);
assert.equal(simulation.querySelector('[data-sim-control="transpiration"]').value, "5");
assert.equal(dom.window.document.activeElement.dataset.simControl, "transpiration", "slider updates must preserve keyboard focus");
assert.doesNotMatch(simulation.textContent, /水量＝|每秒|流速數值/);

console.log("science Db-IV-6: visible original lesson, evidence boundaries, plant-specific model, and keyboard updates verified");

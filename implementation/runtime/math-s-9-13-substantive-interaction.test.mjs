import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-s-9-13.json", import.meta.url), "utf8"));
const source = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");
assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review may pass while unavailable publisher full bodies remain explicitly pending");
assert.equal(lesson.simulation.engine, "math-geometry");
assert.equal(lesson.simulation.model, "s9-13-prism-surface-volume-v2");
assert.equal(lesson.simulation.goal, lesson.simulation.mission && lesson.simulation.goal, "unit-specific objective is present");
assert.equal(lesson.simulation.learningDesign.steps.length, 4);
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/", runScripts: "outside-only",
});
dom.window.eval(source);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "s913-test");
const getSimulation = () => root.querySelector('[data-simulation-lesson$=":s913-test"]');
let simulation = getSimulation();
assert.ok(simulation.querySelector(".sim-prism-lab"));
assert.equal(simulation.querySelectorAll("[data-geometry-prediction]").length, 3);
assert.match(simulation.querySelector('[data-geometry-prediction="A"]').textContent, /增加 120 cm².*增加 80 cm³/);
assert.match(simulation.querySelector('[data-geometry-prediction="B"]').textContent, /增加 80 cm².*增加 120 cm³/);
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]'), null, "model stays locked before prediction submission");
assert.equal(simulation.querySelector("[data-prism-surface-area]"), null);
assert.doesNotMatch(simulation.querySelector(".sim-prism-lab").textContent, /S=2×60\+40L|表面積=320/);

simulation.querySelector('[data-geometry-action="submit-prediction"]').click();
simulation = getSimulation();
assert.match(simulation.textContent, /請先選擇一項預測/);
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]'), null);
let choice = simulation.querySelector('[data-geometry-prediction="B"]');
choice.focus();
choice.click();
simulation = getSimulation();
assert.equal(dom.window.document.activeElement.dataset.geometryPrediction, "B", "prediction selection preserves keyboard focus");
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]'), null, "selecting alone does not reveal the solution");
let submit = simulation.querySelector('[data-geometry-action="submit-prediction"]');
submit.focus();
submit.click();
simulation = getSimulation();
assert.equal(dom.window.document.activeElement.dataset.geometryAction, "submit-prediction", "submission preserves focus");
assert.equal(simulation.querySelector("[data-prism-surface-area]").textContent, "240");
assert.equal(simulation.querySelector("[data-prism-volume]").textContent, "180");
assert.equal(simulation.querySelectorAll(".sim-prism-visuals figure").length, 2, "solid and net are both rendered");
assert.match(simulation.querySelector(".sim-prism-visuals figure:nth-child(2)").textContent, /三片側面/);

const slider = simulation.querySelector('[data-sim-control="prismLength"]');
slider.focus();
slider.value = "5";
slider.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
simulation = getSimulation();
assert.equal(simulation.querySelector("[data-prism-surface-area]").textContent, "320");
assert.equal(simulation.querySelector("[data-prism-volume]").textContent, "300");
assert.match(simulation.querySelector(".sim-prism-visuals").textContent, /柱長 5 cm/);
assert.equal(dom.window.document.activeElement.dataset.simControl, "prismLength", "slider updates preserve keyboard focus");

let stepButton = simulation.querySelector('[data-design-step="1"]');
stepButton.click();
simulation = getSimulation();
assert.match(simulation.querySelector(".sim-prism-equation").textContent, /底面積=8×15÷2=60/);
stepButton = simulation.querySelector('[data-design-step="2"]');
stepButton.focus();
stepButton.click();
simulation = getSimulation();
assert.equal(dom.window.document.activeElement.dataset.designStep, "2");
assert.match(simulation.querySelector(".sim-prism-equation").textContent, /S=2×60\+40L/);

choice = simulation.querySelector('[data-geometry-transfer="B"]');
choice.click();
simulation = getSimulation();
submit = simulation.querySelector('[data-geometry-action="submit-transfer"]');
submit.click();
simulation = getSimulation();
assert.match(simulation.textContent, /280 cm²、168 cm³/);

simulation.querySelector("[data-sim-reset]").click();
simulation = getSimulation();
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]'), null, "reset returns to the locked prediction state");
assert.equal(simulation.querySelector("[data-prism-surface-area]"), null);
assert.doesNotMatch(simulation.querySelector(".sim-prism-lab").textContent, /三個側面總面積按周長/);
simulation.querySelector('[data-geometry-prediction="A"]').click();
simulation = getSimulation();
simulation.querySelector('[data-geometry-action="submit-prediction"]').click();
simulation = getSimulation();
assert.match(simulation.querySelector(".sim-prism-lab").textContent, /預測尚不正確.*周長40 cm.*底面積60 cm²/s);
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]'), null, "an incorrect prediction gets a hint without revealing the worked answer");
simulation.querySelector('[data-geometry-prediction="B"]').click();
simulation = getSimulation();
simulation.querySelector('[data-geometry-action="submit-prediction"]').click();
simulation = getSimulation();
assert.equal(simulation.querySelector('[data-sim-control="prismLength"]').value, "3", "correct retry unlocks the model");

console.log("PASS S-9-13 prediction gate, misconception hint, triangular-prism net/model, linked calculations, keyboard focus, transfer, reset, content review, and publisher evidence boundary");

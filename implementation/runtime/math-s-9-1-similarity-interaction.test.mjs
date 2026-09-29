import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-s-9-1.json", import.meta.url), "utf8"));
const runtime = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");
assert.equal(lesson.simulation.model, "s9-1-polygon-similarity-v1");
assert.equal(lesson.simulation.similarityModel.originalWidth / lesson.simulation.similarityModel.originalHeight, 3 / 4);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", { url: "https://example.test", runScripts: "outside-only" });
dom.window.eval(runtime);
const root = dom.window.document.querySelector("#root");
const render = () => { root.innerHTML = dom.window.LearningSimulations.render(lesson, "s91-test"); };
render();
const model = () => root.querySelector(".sim-similarity-lab");
assert.equal(model().querySelector('[data-sim-control="scaleX"]'), null, "hide manipulation controls until prediction submission");
model().querySelector('[data-sim-similarity="prediction"][data-value="yes"]').click();
model().querySelector('[data-sim-similarity="submit-prediction"]').click();
assert.ok(model().querySelector('[data-sim-control="scaleX"]'));
assert.ok(model().querySelector('[data-sim-control="scaleY"]'));

const scaleX = model().querySelector('[data-sim-control="scaleX"]');
scaleX.focus();
scaleX.value = "1.5";
scaleX.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
assert.equal(model().querySelector('[data-sim-control="scaleX"]').value, "1.5");
assert.equal(dom.window.document.activeElement.dataset.simControl, "scaleX", "rerender retains keyboard focus");
assert.match(model().querySelector("tbody").textContent, /1\.5/);
assert.match(model().querySelector("tbody").textContent, /90°/);
model().querySelector('[data-sim-similarity="verify"][data-value="no"]').click();
model().querySelector('[data-sim-similarity="check"]').click();
assert.match(model().querySelectorAll(".sim-status")[1].textContent, /判斷正確.*不相似/);

model().querySelector('[data-sim-similarity="transfer"][data-value="yes"]').click();
model().querySelector('[data-sim-similarity="submit-transfer"]').click();
assert.match(model().textContent, /5→2.5 與 7→3.5 的倍率相同/);
render();
assert.equal(model().querySelector('[data-sim-control="scaleX"]').value, "1.5", "local state serialization survives remount");
root.querySelector("[data-sim-reset]").click();
assert.equal(model().querySelector('[data-sim-control="scaleX"]'), null, "reset restores the locked prediction state");
console.log("PASS S-9-1 staged prediction, independent scale manipulation, live ratio evidence, verification feedback, transfer and serialized state");

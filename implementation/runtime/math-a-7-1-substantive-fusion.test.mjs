import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const readJson = async path => JSON.parse(await readFile(new URL(path, import.meta.url), "utf8"));
const lesson = await readJson("../../lessons/math/lesson-math-content-a-7-1.json");
const schema = await readJson("../../schemas/lesson.schema.json");
const specText = await readFile(new URL("../unit-specs/math/cur-math-content-a-7-1.yaml", import.meta.url), "utf8");
const registry = await readJson("../component-registry.json");
const simulations = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.equal(lesson.content.sections.length, 6);
assert.ok(lesson.content.sections.every(section => section.body.length > 80));
assert.ok(lesson.content.sections.reduce((total, section) => total + section.body.length, 0) > 600);
assert.equal(lesson.teaching.body.length, 7);
assert.equal(lesson.versionResearch.filter(item => ["nani", "kanghsuan", "hanlin"].includes(item.publisher)).length >= 7, true);
const nani = lesson.versionResearch.find(item => item.edition.includes("南一標示七上 3-1"));
const knsh = lesson.versionResearch.find(item => item.edition.includes("康軒標示之六升七"));
const hanlin = lesson.versionResearch.find(item => item.edition.includes("翰林國中數學七上課本第三方"));
assert.ok(nani && knsh && hanlin);
assert.match(nani.licenseBoundary, /不是南一出版社課本全文/);
assert.match(knsh.licenseBoundary, /真實性及使用授權均未核/);
assert.match(hanlin.licenseBoundary, /All Rights Reserved.*授權未核/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /南一.*康軒.*翰林.*真實性及權利狀態/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /均為自編/);
assert.equal(lesson.simulation.engine, "math-expression-lab");
assert.equal(lesson.simulation.learningDesign.type, "algebra-expression-investigation");
assert.match(specText, /EquivalentExpressionCheckBlock/);
assert.match(specText, /x=−2、0、3/);
assert.ok(registry.components.EquivalentExpressionCheckBlock);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulations);
const host = dom.window.document.querySelector("#root");
host.innerHTML = dom.window.LearningSimulations.render(lesson, "a7-1-fusion-test");
let root = host.querySelector("[data-simulation-lesson]");
assert.equal(root.querySelectorAll("[data-design-step]").length, 4);
assert.deepEqual(
  [...root.querySelectorAll("tbody tr")].map(row => [...row.cells].map(cell => cell.textContent)),
  [["-2", "-21", "-21"], ["0", "-5", "-5"], ["3", "19", "19"]],
);
const slider = root.querySelector('[data-sim-control="x"]');
slider.focus();
slider.value = "-2";
slider.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
root = host.querySelector("[data-simulation-lesson]");
assert.equal(root.querySelector("[data-expression-original]").textContent, "-21");
assert.equal(root.querySelector("[data-expression-reduced]").textContent, "-21");
assert.match(root.querySelector(".sim-expression-check p").textContent, /兩式同值/);
assert.equal(dom.window.document.activeElement.getAttribute("data-sim-control"), "x", "slider focus must survive live updates");
assert.match(root.querySelector('[aria-label="測試變數 x 的值"]').getAttribute("aria-label"), /測試變數/);

console.log("A-7-1 source-grounded synthesis, visible lesson, equivalent-expression runtime and keyboard focus: ok");

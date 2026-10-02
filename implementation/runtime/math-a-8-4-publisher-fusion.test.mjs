import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-a-8-4.json", import.meta.url), "utf8"));
const report = JSON.parse(await readFile(new URL("../reports/a8-4-three-publisher-fusion.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.equal(lesson.versionResearch.length, 3);
assert.equal(report.lessonId, lesson.id);
assert.match(lesson.teaching.body.find(section => section.id === "worked").body, /x²\+7x\+12.*不等於原式的 10/);
assert.equal(lesson.interactive.steps.length, 5);
assert.equal(lesson.simulation.learningDesign.steps.length, 5);
assert.match(lesson.simulation.learningDesign.steps[4].equation, /x²＋7x＋12≠x²＋7x＋10/);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "a8-4-test");
assert.equal(root.querySelectorAll("[data-design-step]").length, 5);
root.querySelector('[data-design-step="4"]').click();
assert.match(root.textContent, /x²＋7x＋12≠x²＋7x＋10/);

console.log("A-8-4 evidence provenance, corrected product check, five-stage interaction and content-review/evidence-boundary gate: ok");

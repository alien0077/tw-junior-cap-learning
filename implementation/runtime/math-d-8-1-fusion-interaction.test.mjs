import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-d-8-1.json", import.meta.url), "utf8"));
const report = JSON.parse(await readFile(new URL("../reports/math-d-8-1-scope-correction-and-source-fusion-2026-09-27.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "draft");
assert.equal(report.lessonId, lesson.id);
assert.equal(report.synthesis.fusionGate.startsWith("NOT COMPLETE"), true);
assert.equal(lesson.publisherResearch.length, 3);
assert.equal(lesson.interactive.steps.length, 4);
assert.equal(lesson.simulation.learningDesign.steps.length, 4);
assert.equal(lesson.interactive.steps.filter(step => step.answer === "A").length, 4);
assert.match(lesson.teaching.body.find(section => section.id === "explain").body, /20%、30%、35%、15%/);
assert.match(lesson.teaching.body.find(section => section.id === "worked").body, /\(4,20\).*\(16,100\)/);
assert.match(lesson.teaching.body.find(section => section.id === "worked").body, /85−50=35%/);
assert.ok(lesson.fusionRecord.versionDifferences.some(text => text.includes("康軒") && text.includes("沒有足夠證據")));

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "d81-test");
assert.equal(root.querySelectorAll("[data-design-step]").length, 4);
root.querySelector('[data-design-step="2"]').click();
assert.match(root.textContent, /85%-50%=35%/);

console.log("D-8-1 relative/cumulative frequency arithmetic, publisher evidence limits, interactive stages and draft gate: ok");

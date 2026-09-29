import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-a-8-1.json", import.meta.url), "utf8"));
const report = JSON.parse(await readFile(new URL("../reports/a8-1-three-publisher-fusion.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "draft");
assert.equal(report.status, "substantive-fusion-draft");
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every(source => source.reviewedAt === "2026-09-27"));
assert.ok(lesson.fusionRecord.versionDifferences.some(text => text.includes("南一")));
assert.ok(lesson.fusionRecord.versionDifferences.some(text => text.includes("康軒D版")));
assert.ok(lesson.fusionRecord.versionDifferences.some(text => text.includes("翰林補救GO")));
assert.equal(lesson.simulation.learningDesign.steps.length, 5);
assert.match(lesson.simulation.learningDesign.steps[4].equation, /49×51=.*2499/);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "a8-1-test");
assert.equal(root.querySelectorAll("[data-design-step]").length, 5);
assert.match(root.textContent, /先預測/);

root.querySelector('[data-design-step="4"]').click();
assert.match(root.textContent, /49×51=.*2499/);
root.querySelector('[data-sim-action="predicted"]').click();
assert.match(root.textContent, /已記錄預測/);
root.querySelector('[data-sim-action="observed"]').click();
assert.match(root.textContent, /已記錄觀察/);

console.log("A-8-1 publisher-informed lesson records, five-stage interaction and draft gate: ok");

import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/science/lesson-science-content-aa-iv-1.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");
const comparativeSource = "https://chemed.chemistry.org.tw/page/74?cat=gsmmuqdvfh";

assert.equal(lesson.reviewStatus, "reviewed", "completed lesson review remains reviewed while publisher and rights limits stay explicit");
assert.equal(lesson.content.sections.length, 6);
assert.deepEqual(
  lesson.content.sections,
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "all six original paragraphs must be visible to the learner",
);
assert.ok(lesson.studyReferences.includes(comparativeSource), "record the cross-version study used for the fusion decision");
assert.match(lesson.fusionRecord.versionDifferences.join("\n"), /2013年.*不.*現行版次/);
assert.ok(lesson.versionResearch.some(({ publisher }) => publisher === "nani"));
assert.ok(lesson.versionResearch.some(({ publisher }) => publisher === "kanghsuan"));
assert.ok(lesson.versionResearch.some(({ publisher }) => publisher === "hanlin"));
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every(({ outcome }) => /三版本融合審查尚未完成/.test(outcome)), "publisher evidence may remain limited even after the project content review is completed");
assert.match(lesson.fusionRecord.llmSynthesisNote, /ChatGPT 已完成本 lesson 的正式教材內容審查/);

const expectedCorrectOptions = [
  "原子內含帶負電電子，須修正原子不可分的想法",
  "原子大部分是空間，正電與大部分質量集中在很小的區域",
  "把為了表徵而加上的符號，誤當成直接觀察到的性質",
  "先列出模型預測，再和可重複觀察比較；指出解釋範圍與仍有限制",
];
const prompts = lesson.interactive.steps.map(({ prompt, options, feedback, answer }, index) => {
  assert.equal(answer, "A");
  assert.equal(options[0], expectedCorrectOptions[index], `step ${index + 1} must preserve its reviewed best answer`);
  return `${prompt}\n${options.join("\n")}\n${feedback}`;
}).join("\n");
assert.match(prompts, /陰極射線/);
assert.match(prompts, /金箔散射/);
assert.match(prompts, /模型.*照片|模型.*實物/);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "atom-model-test");
let simulation = root.querySelector('[data-simulation-lesson$=":atom-model-test"]');
assert.match(simulation.textContent, /集中正電區/);
assert.ok(simulation.querySelector(".sim-rutherford"));
assert.match(simulation.querySelector(".sim-rutherford svg").getAttribute("aria-label"), /路徑不按比例/);
assert.doesNotMatch(simulation.textContent, /溫度條件|粒子較緊密|可互相滑動/);
assert.equal(simulation.querySelectorAll("[data-design-step]").length, 4);
assert.ok(simulation.querySelector(".sim-rutherford"), `dedicated visualization missing for ${lesson.simulation.engine}/${lesson.simulation.model}`);

let slider = simulation.querySelector('[data-sim-control="impactProximity"]');
assert.ok(slider, "the atom lesson must render its dedicated proximity control");
assert.equal(slider.getAttribute("aria-label"), "粒子最近接近正電核程度（1＝遠，5＝近）");
const originalPath = simulation.querySelector(".sim-rutherford .sim-line").getAttribute("d");
slider.focus();
slider.value = "5";
slider.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
simulation = root.querySelector('[data-simulation-lesson$=":atom-model-test"]');
slider = simulation.querySelector('[data-sim-control="impactProximity"]');
assert.equal(slider.value, "5");
assert.notEqual(simulation.querySelector(".sim-rutherford .sim-line").getAttribute("d"), originalPath);
assert.match(simulation.textContent, /貼近.*較大的偏折/);
assert.equal(dom.window.document.activeElement, slider, "keyboard focus must remain on the control after the model updates");

slider.value = "1";
slider.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
simulation = root.querySelector('[data-simulation-lesson$=":atom-model-test"]');
assert.match(simulation.textContent, /離.*較遠.*接近直行/);
simulation.querySelector("[data-sim-reset]").click();
simulation = root.querySelector('[data-simulation-lesson$=":atom-model-test"]');
assert.equal(simulation.querySelector('[data-sim-control="impactProximity"]').value, "3");

console.log("Aa-IV-1 visible fusion, historical-source boundary, evidence-based questions, and Rutherford-specific accessible simulation: PASS");

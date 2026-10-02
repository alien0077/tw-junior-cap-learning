import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/math/lesson-math-content-a-7-8.json", import.meta.url), "utf8"));
const spec = readFileSync(new URL("../unit-specs/math/cur-math-content-a-7-8.yaml", import.meta.url), "utf8");
const simulationSource = readFileSync(new URL("../../site/simulations.js", import.meta.url), "utf8");
const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join("\n");

assert.equal(lesson.reviewStatus, "content-reviewed", "project-authored content review is complete while unavailable publisher full-body evidence remains explicitly pending");
assert.equal(lesson.content.sections.length, 6);
assert.equal(lesson.teaching.body.length, 6);
assert.equal(lesson.simulation.engine, "math-inequality-range", "A-7-8 must use the dedicated inequality renderer rather than the generic concept explorer");
assert.equal(lesson.simulation.learningDesign.type, "inequality-solution-set");
assert.equal(lesson.simulation.learningDesign.steps.length, 4);
assert.deepEqual(lesson.studyReferences, lesson.simulation.sourceRefs);

// Source distinctions are explicit and tied to actual original learner-facing moves.
const nani = lesson.versionResearch.find((source) => source.publisher === "nani");
const kanghsuan = lesson.versionResearch.find((source) => source.publisher === "kanghsuan");
const hanlin = lesson.versionResearch.find((source) => source.publisher === "hanlin" && source.sourceLocator.includes("mathvideo.hle.com.tw/1B/4-2"));
assert.ok(nani?.sourceLocator.includes("scribd.com/document/932850305"));
assert.ok(nani?.sourceLocator.includes("OCR節錄"));
assert.ok(kanghsuan?.sourceLocator.includes("lines 358–400"));
assert.ok(kanghsuan?.findings.concepts.some((finding) => finding.includes("數線上的點同向平移")));
assert.ok(hanlin?.findings.concepts.some((finding) => finding.includes("加減、乘除性質")));
assert.match(lesson.fusionRecord.llmSynthesisNote, /解集探針.*數線次序理由.*逐步等價變形.*邊界檢驗.*情境交集/s);
assert.match(visible, /先看 −2x＋6＞10.*試代 x＝−3、−2、−1/s);
assert.match(visible, /數線上的兩個位置.*同加 5.*乘上負數.*鏡射：例如 −1＜2/s);
assert.match(visible, /同減 6.*−2x＞4.*同除 −2.*x＜−2/s);
assert.match(visible, /−2.*空心.*−3.*12＞10.*−1.*8＞10/s);
assert.match(visible, /120h＋80≤800.*h≤6.*1、2、3、4、5、6.*920 元/s);
assert.match(visible, /−3\(2x−1\)≥9.*−4≤x.*−4、−3、−2、−1/s);
assert.equal(lesson.versionResearch.some((source) => source.publisher === "nani" && source.sourceType === "public-domain"), false);
assert.equal(lesson.publisherResearch.filter((source) => ["nani", "kanghsuan", "hanlin"].includes(source.publisher) && source.status === "verified").length, 0);
assert.match(spec, /limited-public-materials-read; source-to-visible-original-synthesis-draft/);
assert.match(spec, /qaStatus: (?:untested|passed)/, "QA status is finalized only after the browser gate; the content/runtime contract must remain valid in either transition state");
for (const publisher of ["nani", "kanghsuan", "hanlin"]) assert.match(spec, new RegExp(`${publisher}:\\s*\\n\\s*status: pending`));

// Verify the real renderer's proof graph, step navigation, keyboard focus, and source-data fallback.
const dom = new JSDOM('<!doctype html><main id="host"></main>', { url: "https://example.test/", runScripts: "outside-only" });
dom.window.eval(simulationSource);
const host = dom.window.document.querySelector("#host");
const rootSelector = '[data-simulation-lesson="lesson-math-content-a-7-8:a7-8-fusion-test"]';
host.innerHTML = dom.window.LearningSimulations.render(lesson, "a7-8-fusion-test");
let root = host.querySelector(rootSelector);
assert.match(root.textContent, /先預測/);
assert.match(root.querySelector("svg").getAttribute("aria-label"), /負二為空心端點並向左延伸/);
assert.match(root.querySelector("figcaption").textContent, /原式 −2x＋6＞10/);
assert.equal(root.querySelectorAll("[data-design-step]").length, 4);

for (const step of [1, 2, 3]) {
  root = host.querySelector(rootSelector);
  const button = root.querySelector(`[data-design-step="${step}"]`);
  button.focus();
  button.click();
  root = host.querySelector(rootSelector);
  assert.equal(root.querySelector(`[data-design-step="${step}"]`).getAttribute("aria-current"), "step");
  assert.equal(dom.window.document.activeElement, root.querySelector(`[data-design-step="${step}"]`), "keyboard focus must survive step rerender");
}
assert.match(root.textContent, /−5、−4、−3/);
assert.match(root.querySelector("svg").getAttribute("aria-label"), /負三成立、負二不成立、負一不成立/);
console.log("A-7-8 source-to-visible fusion, solution-set reasoning, interactive proof graph, keyboard focus, and content-review/evidence-boundary gates: ok");

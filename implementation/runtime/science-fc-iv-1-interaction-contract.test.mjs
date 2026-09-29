import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync("lessons/science/lesson-science-content-fc-iv-1.json", "utf8"));
const specText = readFileSync("implementation/unit-specs/science/cur-science-content-fc-iv-1.yaml", "utf8");
const bundle = JSON.parse(readFileSync("implementation/unit-specs.bundle.json", "utf8"));
const spec = bundle.units.find((unit) => unit.lessonId === "cur-science-content-fc-iv-1");
const simSource = readFileSync("site/simulations.js", "utf8");

assert.equal(lesson.reviewStatus, "draft", "publisher and content gates are not waived");
assert.equal(lesson.interactive.type, "scientific-investigation");
assert.match(lesson.interactive.scenario, /按鈕切換/);
assert.doesNotMatch(lesson.interactive.scenario, /拖曳/);
assert.equal(lesson.interactive.steps.length, 4);
assert.ok(lesson.interactive.steps.every((step) => step.retryHint && step.feedback));
assert.equal(lesson.simulation.model, "ecosystem-scale-boundary");
assert.doesNotMatch(lesson.simulation.mission, /拖曳/);

assert.ok(spec, "compiled implementation spec exists for Fc-IV-1");
assert.deepEqual(spec.interactiveBlocks.map((block) => block.component), ["SystemRelationshipBlock", "GuidedChoiceBlock"]);
assert.deepEqual(spec.status, { designStatus: "reviewed", implementationStatus: "implemented", qaStatus: "verified" }, "unit-specific design, runtime, browser, and accessibility checks passed; lesson content remains draft");
assert.match(specText, /以可及的按鈕切換池塘／潮間帶及五種尺度/);
assert.doesNotMatch(specText, /先提交預測，不顯示正解|改變一個變項|同步更新圖、表、句構或因果鏈|拖曳觀察鏡頭/);

const dom = new JSDOM("<!doctype html><html><body></body></html>", { url: "https://example.test/", runScripts: "outside-only" });
dom.window.eval(simSource);
const host = dom.window.document.body;
host.innerHTML = dom.window.LearningSimulations.render(lesson, "fc-iv-1-contract");
let simulation = host.querySelector("[data-simulation-lesson]");
assert.ok(simulation.querySelector('[data-eco-site="pond"]'));
assert.match(simulation.textContent, /校園池塘｜個體/);
assert.match(simulation.textContent, /一隻白腹樹蛙/);

const populationButton = simulation.querySelector('[data-eco-scale="population"]');
populationButton.focus();
populationButton.click();
simulation = host.querySelector("[data-simulation-lesson]");
assert.match(simulation.textContent, /同一時段、池塘東側的12隻同種青蛙/);
assert.equal(simulation.querySelector('[data-eco-scale="population"]').getAttribute("aria-pressed"), "true");
assert.equal(dom.window.document.activeElement.dataset.ecoScale, "population", "focus is restored after rendering updated evidence");

simulation.querySelector('[data-eco-scale="ecosystem"]').click();
simulation = host.querySelector("[data-simulation-lesson]");
assert.match(simulation.textContent, /生物群集，以及水溫26°C、光照、水質與底泥/);
simulation.querySelector('[data-eco-site="shore"]').click();
simulation = host.querySelector("[data-simulation-lesson]");
assert.match(simulation.textContent, /潮間帶｜生態系/);
assert.match(simulation.textContent, /潮汐、鹽度、岩面乾濕/);
simulation.querySelector('[data-eco-scale="biosphere"]').click();
simulation = host.querySelector("[data-simulation-lesson]");
assert.match(simulation.textContent, /單一潮間帶樣區不能代表全部/);
assert.equal(simulation.querySelectorAll("[data-eco-scale]").length, 5);
assert.equal(simulation.querySelectorAll("[data-eco-site]").length, 2);

console.log("PASS Fc-IV-1 specification matches the actual five-scale, two-site accessible model and four-step guided choice");

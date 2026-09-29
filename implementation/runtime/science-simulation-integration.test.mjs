import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/science/lesson-science-content-ka-iv-7.json", import.meta.url), "utf8"));
const appSource = await readFile(new URL("../../site/app.js", import.meta.url), "utf8");
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");
assert.match(appSource, /window\.LearningSimulations\.render\(item, instance\)/, "lesson detail must mount data-backed simulations with instance identity");

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", { url: "https://example.test/", runScripts: "outside-only" });
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = `${dom.window.LearningSimulations.render(lesson, "catalog-card")}${dom.window.LearningSimulations.render(lesson, "all-content-card")}`;
const catalogSimulation = root.querySelector('[data-simulation-lesson$=":catalog-card"]');
const contentSimulation = root.querySelector('[data-simulation-lesson$=":all-content-card"]');
assert.match(catalogSimulation.textContent, /光脈衝測量站/);
assert.match(catalogSimulation.textContent, /先預測/);
assert.match(catalogSimulation.textContent, /v＝c\/n/);
assert.equal(catalogSimulation.querySelectorAll("[data-design-step]").length, lesson.simulation.learningDesign.steps.length);

catalogSimulation.querySelector('[data-design-step="1"]').click();
const updatedCatalogSimulation = root.querySelector('[data-simulation-lesson$=":catalog-card"]');
assert.match(updatedCatalogSimulation.textContent, /t＝d\/v＝dn\/c/);
assert.doesNotMatch(contentSimulation.textContent, /t＝d\/v＝dn\/c/);

updatedCatalogSimulation.querySelector('[data-sim-action="predicted"]').click();
assert.match(root.querySelector('[data-simulation-lesson$=":catalog-card"]').textContent, /已記錄預測/);
assert.match(root.querySelector('[data-simulation-lesson$=":all-content-card"]').textContent, /尚未記錄預測/);

const appDom = new JSDOM(`<!doctype html><html><body>
  <div id="status"></div><select id="grade"></select><select id="subject"><option value="english">English</option></select><select id="publisher"></select>
  <input id="search"><div id="contentGrid"></div><div id="catalogGrid"></div><span id="catalogTitle"></span><span id="catalogCount"></span><span id="resultCount"></span>
  <span id="statNodes"></span><span id="statLessons"></span><span id="statQuestions"></span><span id="statMappings"></span>
</body></html>`, { url: "https://example.test/", runScripts: "outside-only" });
const entryLesson = { ...lesson, simulation: undefined, interactive: undefined, content: { ...lesson.content, studyEntry: "先用證據辨認光速與距離的差別。" } };
appDom.window.fetch = async () => ({ ok: true, json: async () => ({
  lessons: [entryLesson], questions: [], mappings: [], sourceRevision: "test", generatedAt: "test",
  project: { dataCounts: { knowledgeNodes: 1 }, activeLessons: 1, activeQuestions: 0 }, validation: { mappingSetCount: 0 },
}) });
appDom.window.eval(appSource);
await new Promise(resolve => setTimeout(resolve, 0));
assert.equal(appDom.window.document.querySelector(".lesson-entry")?.textContent, "先用證據辨認光速與距離的差別。");

console.log("lesson interaction integration: simulation mount/state isolation and studyEntry rendering verified");

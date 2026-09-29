import assert from "node:assert/strict";
import fs from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(fs.readFileSync("lessons/science/lesson-science-content-ca-iv-1.json", "utf8"));
const specText = fs.readFileSync("implementation/unit-specs/science/cur-science-content-ca-iv-1.yaml", "utf8");
const manifest = JSON.parse(fs.readFileSync("implementation/unit-specs.manifest.json", "utf8"));
const simSource = fs.readFileSync("site/simulations.js", "utf8");
const row = manifest.units.find((unit) => unit.lessonId === "cur-science-content-ca-iv-1");

assert.equal(lesson.reviewStatus, "draft", "global independence/content gates remain open");
assert.equal(lesson.teaching.body.length, 6);
assert.deepEqual(
  lesson.content.sections.slice(1).map(({ heading, body }) => ({ heading, body })),
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "the authored lesson must be visible to learners without replacing it with a summary"
);

const sources = Object.fromEntries(lesson.versionResearch.map((record) => [record.publisher, record]));
assert.match(sources.hanlin.sourceLocator, /p\.19–21/);
assert.match(sources.hanlin.findings.concepts.join(" "), /溶解.*過濾.*蒸發結晶/);
assert.match(sources.nani.licenseBoundary, /publisher slot 維持 pending/);
assert.match(sources.kanghsuan.licenseBoundary, /publisher slot 維持 pending/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /南一與康軒僅有單元索引/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /官方只公開互動資源標題/);
assert.deepEqual(lesson.simulation.sourceRefs, lesson.studyReferences);
assert.equal(lesson.simulation.engine, "concept-explorer");
assert.equal(lesson.simulation.model, "general");
assert.deepEqual(lesson.simulation.learningDesign.steps.map((step) => step.id), ["step-1", "step-2", "step-3", "step-4"]);
assert.match(lesson.simulation.learningDesign.steps.map((step) => step.action).join(" "), /磁鐵.*過濾.*洗液.*蒸發結晶/);
assert.equal(lesson.interactive.steps.length, 4);
assert.ok(lesson.interactive.steps.every((step) => step.options.length === 3 && step.answer === "A"));
assert.doesNotMatch(lesson.interactive.steps.flatMap((step) => step.options).join(" "), /直接猜測答案|忽略來源與限制|只寫最後結論/);

assert.match(specText, /nani:\n        status: pending/);
assert.match(specText, /kanghsuan:\n        status: pending/);
assert.match(specText, /hanlin:\n        status: verified/);
assert.match(specText, /MC-CA-IV-1-DRY-FILTER/);
assert.match(specText, /只取鹽／還要取水/);
assert.equal(row.component, "EvidenceLabBlock");
assert.equal(row.publisherEvidence.hanlin, "verified");
assert.equal(row.publisherEvidence.nani, "book-level-only");
assert.equal(row.publisherEvidence.kanghsuan, "book-level-only");
assert.equal(row.status.qaStatus, "untested");

const dom = new JSDOM("<!doctype html><html><body></body></html>", { url: "https://example.test/", runScripts: "outside-only" });
dom.window.eval(simSource);
const root = dom.window.document.body;
root.innerHTML = dom.window.LearningSimulations.render(lesson, "ca-iv-1-regression");
let simulation = root.querySelector("[data-simulation-lesson]");
assert.match(simulation.querySelector("header .tag").textContent, /概念探索工作臺/);
assert.match(simulation.textContent, /先預測/);
assert.equal(simulation.querySelectorAll("[data-design-step]").length, 4);
assert.match(simulation.textContent, /鐵屑分流/);
simulation.querySelector('[data-design-step="1"]').click();
assert.match(root.textContent, /濾渣＝主要為細砂/);
simulation = root.querySelector("[data-simulation-lesson]");
simulation.querySelector('[data-design-step="3"]').click();
assert.match(root.textContent, /表觀回收率/);

console.log("PASS Ca-IV-1 original fusion, honest source depth, student-visible lesson, stepwise interaction, and draft gates");

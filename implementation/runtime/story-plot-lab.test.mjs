import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-9.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/story-plot-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/styles.css", import.meta.url), "utf8");
const lab = lesson.interactive.storyPlotLab;
for (const stage of [lab.mainStory, lab.transfer]) {
  assert.ok(stage.requiredEvidenceIds.every(id => stage.parts.some(part => part.id === id)));
  assert.ok(stage.question.options.some(option => option.id === stage.question.answer));
}

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
mount.innerHTML = dom.window.StoryPlotLab.render(lesson, "qa-3-iv-9");
const root = () => mount.querySelector("[data-story-plot-lab]");
const click = selector => root().querySelector(selector).click();
const evidence = (kind, id) => root().querySelector(`[data-plot-evidence="${kind}"][data-part="${id}"]`).click();
const choose = (field, id) => {
  const input = root().querySelector(`input[name^="${field}-"][value="${id}"]`);
  input.checked = true;
  input.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
};
const type = (field, value) => {
  const input = root().querySelector(`[data-plot-text="${field}"]`);
  input.value = value;
  input.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
};

assert.equal(root().querySelectorAll(".story-plot-part").length, lab.mainStory.parts.length);
assert.equal(root().querySelector('[data-plot-evidence="main"]').disabled, true);
assert.match(root().querySelector('[role="status"]').textContent, /正解尚未揭露/);
click('[data-plot-action="predict"]');
assert.match(root().textContent, /至少用 8 個字/);
type("prediction", "她可能會先找出風箏飛不起來的環境原因");
click('[data-plot-action="predict"]');
assert.equal(root().querySelector('[data-plot-evidence="main"]').disabled, false);

for (const id of ["goal", "obstacle", "clue"]) evidence("main", id);
click('[data-plot-action="check-main-evidence"]');
assert.match(root().textContent, /還缺一環/);
for (const id of lab.mainStory.requiredEvidenceIds) {
  if (root().querySelector(`[data-plot-evidence="main"][data-part="${id}"]`).getAttribute("aria-pressed") !== "true") evidence("main", id);
}
click('[data-plot-action="check-main-evidence"]');
assert.match(root().textContent, /證據鏈已包含/);
choose("main", "A");
click('[data-plot-action="check-main-answer"]');
assert.equal(root().querySelector('[data-plot-evidence="transfer"]'), null);
choose("main", lab.mainStory.question.answer);
click('[data-plot-action="check-main-answer"]');
assert.ok(root().querySelector('[data-plot-evidence="transfer"]'));

for (const id of lab.transfer.requiredEvidenceIds) evidence("transfer", id);
choose("transfer", lab.transfer.question.options.find(option => option.id !== lab.transfer.question.answer).id);
type("explanation", "這樣做還不夠");
click('[data-plot-action="check-transfer"]');
assert.match(root().textContent, /至少用 18 字/);
type("explanation", "他注意到新生看不清公告，也不知道集合位置，因此改用大字並加上清楚路線圖，讓大家能找到社團教室。");
click('[data-plot-action="check-transfer"]');
assert.match(root().textContent, /選項、證據與理由尚未對齊/);
choose("transfer", lab.transfer.question.answer);
click('[data-plot-action="check-transfer"]');
assert.match(root().querySelector('[role="status"]').textContent, /互動完成/);

mount.innerHTML = dom.window.StoryPlotLab.render(lesson, "qa-3-iv-9");
assert.match(root().querySelector('[role="status"]').textContent, /互動完成/);
assert.equal(root().querySelector('[data-plot-action="check-transfer"]').disabled, true);
assert.equal(root().querySelector('[data-plot-text="explanation"]').disabled, true);
evidence("main", "obstacle");
assert.equal(root().querySelector('[data-plot-evidence="transfer"]'), null);
assert.equal(root().querySelectorAll('input[name^="main-"]:checked').length, 0);
click('[data-plot-action="reset"]');
assert.equal(root().querySelector('[data-plot-text="prediction"]').value, "");
assert.equal(dom.window.localStorage.length, 0);
assert.match(app, /StoryPlotLab\.render/);
assert.match(html, /story-plot-lab\.js/);
assert.match(css, /@media\(max-width:480px\)\{\.story-plot-part/);
assert.match(css, /prefers-reduced-motion:reduce\)\{\.story-plot-lab/);
assert.match(css, /\.story-plot-lab button\{min-height:44px/);
console.log("3-IV-9 prediction, plot evidence, answer retry, transfer rationale, persistence, and responsive hooks: ok");

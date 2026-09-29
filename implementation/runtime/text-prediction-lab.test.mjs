import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-11.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/text-prediction-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/styles.css", import.meta.url), "utf8");
const lab = lesson.interactive.textPredictionLab;
assert.equal(lesson.interactive.type, "text-prediction-lab");
assert.equal(lab.artifacts.length, 2);
for (const artifact of lab.artifacts) {
  assert.ok(artifact.sourceCues.length >= artifact.sourceCueMinimum);
  assert.ok(artifact.requiredEvidenceIds.every(id => artifact.evidence.some(part => part.id === id)));
  assert.ok(artifact.checkQuestion.options.some(option => option.id === artifact.checkQuestion.answer));
  assert.doesNotMatch(`${artifact.title} ${artifact.caption}`, /The Last Seed|Before You Hike|Three Ways to Save Water/);
}

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
mount.innerHTML = dom.window.TextPredictionLab.render(lesson, "qa-3-iv-11");
const root = () => mount.querySelector("[data-text-prediction-lab]");
const click = selector => root().querySelector(selector).click();
const type = value => {
  const input = root().querySelector('[data-tp-text="prediction"]');
  input.value = value;
  input.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
};
const choose = (field, id) => {
  const input = root().querySelector(`input[data-tp-choice="${field}"][value="${id}"]`);
  input.checked = true;
  input.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
};
const select = (kind, id) => root().querySelector(`[data-tp-${kind}="${id}"]`).click();
const message = () => [...root().querySelectorAll(".tp-feedback")].at(-1).textContent;

assert.equal(root().querySelector(".tp-reading"), null);
assert.match(root().querySelector('[role="status"]').textContent, /正文尚未揭露/);
click('[data-tp-action="reveal"]');
assert.match(message(), /至少用 10 字/);
type("這篇可能說明社區如何依圖稿修補一扇彩色玻璃窗");
select("cue", "title");
select("cue", "caption");
click('[data-tp-action="reveal"]');
assert.match(message(), /選一個把握程度/);
choose("confidence", "medium");
click('[data-tp-action="reveal"]');
assert.ok(root().querySelector(".tp-reading"));
assert.match(root().textContent, /你的原預測/);
assert.equal(root().querySelectorAll(".tp-illustration").length, 1);

const practice = lab.artifacts[0];
for (const id of practice.requiredEvidenceIds) select("evidence", id);
click('[data-tp-action="check"]');
assert.match(message(), /選擇一項修正版/);
const wrong = practice.checkQuestion.options.find(option => option.id !== practice.checkQuestion.answer).id;
choose("answer", wrong);
choose("updatedConfidence", "low");
click('[data-tp-action="check"]');
assert.match(message(), /正文實際描寫 Inez/);
choose("answer", practice.checkQuestion.answer);
click('[data-tp-action="check"]');
assert.match(message(), /重新選擇目前把握程度/);
choose("updatedConfidence", "medium");
click('[data-tp-action="check"]');
assert.ok(root().querySelector('[data-tp-action="next"]'));
assert.match(message(), /把彩色拼片與修復圖說收窄/);

select("evidence", "fitted");
assert.equal(root().querySelector('[data-tp-action="next"]'), null);
assert.equal(root().querySelectorAll('input[data-tp-choice="answer"]:checked').length, 0);
select("evidence", "fitted");
choose("answer", practice.checkQuestion.answer);
choose("updatedConfidence", "medium");
click('[data-tp-action="check"]');
click('[data-tp-action="next"]');

const transfer = lab.artifacts[1];
assert.match(root().querySelector(".tp-cover-heading h5").textContent, /A Shared Shade/);
type("我猜提案會比較戶外聚會地點並檢查行走空間");
select("cue", "title");
select("cue", "image");
choose("confidence", "high");
click('[data-tp-action="reveal"]');
for (const id of transfer.requiredEvidenceIds) select("evidence", id);
choose("answer", transfer.checkQuestion.answer);
choose("updatedConfidence", "low");
click('[data-tp-action="check"]');
assert.match(message(), /依學生實際比較和測試的條件/);
click('[data-tp-action="next"]');
assert.match(root().querySelector('[role="status"]').textContent, /預測校準完成/);
mount.innerHTML = dom.window.TextPredictionLab.render(lesson, "qa-3-iv-11");
assert.match(root().querySelector('[role="status"]').textContent, /預測校準完成/);
click('[data-tp-action="reset"]');
assert.equal(root().querySelector('[data-tp-text="prediction"]').value, "");
assert.equal(dom.window.localStorage.length, 0);

assert.match(app, /TextPredictionLab\.render/);
assert.match(html, /text-prediction-lab\.js/);
assert.match(css, /@media\(max-width:480px\)\{\.tp-evidence li/);
assert.match(css, /prefers-reduced-motion:reduce\)\{\.text-prediction-lab/);
assert.match(css, /\.text-prediction-lab button\{min-height:44px/);
console.log("3-IV-11 preview prediction, confidence calibration, evidence-based revision, distinct transfer, persistence and reset: ok");

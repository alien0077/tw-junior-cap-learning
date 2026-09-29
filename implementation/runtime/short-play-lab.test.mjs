import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-13.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/short-play-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/short-play-lab.css", import.meta.url), "utf8");
const lab = lesson.interactive.shortPlayLab;
assert.equal(lesson.interactive.type, "short-play-comprehension-lab");
assert.ok(lab.mainStages.every(stage => stage.options.length === 3 && stage.options.some((_, index) => String.fromCharCode(65 + index) === stage.answer)));
assert.ok(lab.transfer.stages.every(stage => stage.options.length === 3 && stage.options.some((_, index) => String.fromCharCode(65 + index) === stage.answer)));
assert.ok([...lab.mainScript.lines, ...lab.transfer.script.lines].every(line => ["dialogue", "direction"].includes(line.kind)));

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
const instance = "qa-short-play";
mount.innerHTML = dom.window.ShortPlayLab.render(lesson, instance);
const root = () => mount.querySelector("[data-short-play-lab]");
const click = selector => root().querySelector(selector).click();
const predict = value => {
  const input = root().querySelector("[data-spl-prediction]");
  input.value = value;
  click('[data-spl-action="reveal"]');
};
const answer = choice => {
  root().querySelector(`[data-spl-choice][value="${choice}"]`).checked = true;
  click('[data-spl-action="check"]');
};

assert.equal(root().querySelector(".spl-script"), null, "the script should stay hidden before prediction");
predict("short");
assert.equal(root().querySelector(".spl-script"), null, "short predictions must not reveal the play");
assert.match(root().querySelector('[role="status"]').textContent, /至少 12 字/);
predict("The group may need to move a stage prop so everyone can use the route.");
assert.match(root().querySelector(".spl-script").textContent, /A Clear Path/);
assert.match(root().querySelector(".spl-script").textContent, /舞台指示/);
assert.ok(root().querySelectorAll('.spl-script [data-line-kind="direction"]').length >= 1);
assert.equal(root().querySelector(".spl-progress").textContent, "排演判讀 1／9");

answer("C");
assert.equal(root().querySelector(".spl-progress").textContent, "排演判讀 1／9", "wrong interpretations must remain on the current prompt");
assert.match(root().querySelector('[role="status"]').textContent, /clash/);
assert.equal(root().querySelector('[data-spl-choice][value="C"]').checked, true, "wrong selection must remain visible for retry");
answer(lab.mainStages[0].answer);
assert.equal(root().querySelector(".spl-progress").textContent, "排演判讀 2／9");

for (const stage of lab.mainStages.slice(1)) answer(stage.answer);
assert.match(root().querySelector(".spl-script").textContent, /A Softer Beginning/);
assert.match(root().textContent, /新排演片段/);
for (const stage of lab.transfer.stages) answer(stage.answer);
assert.match(root().textContent, /兩段排演都已完成/);
mount.innerHTML = dom.window.ShortPlayLab.render(lesson, instance);
assert.match(root().textContent, /兩段排演都已完成/, "completion should restore for this lesson instance");
click('[data-spl-action="reset"]');
assert.equal(root().querySelector(".spl-progress").textContent, "讀前預測");
assert.equal(root().querySelector(".spl-script"), null);
assert.match(app, /ShortPlayLab\.render/);
assert.match(html, /short-play-lab\.js/);
assert.match(html, /short-play-lab\.css/);
assert.match(css, /prefers-reduced-motion:reduce/);
assert.match(css, /min-height:44px/);
console.log("3-IV-13 script reveal, conflict/stage-direction evidence, retry, distinct-play transfer, persistence and reset: ok");

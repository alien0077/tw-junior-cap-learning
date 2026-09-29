import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-5.json", import.meta.url), "utf8"));
const schema = JSON.parse(readFileSync(new URL("../../schemas/lesson.schema.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/daily-expression-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/daily-expression-lab.css", import.meta.url), "utf8");
const lab = lesson.interactive.dailyExpressionLab;

assert.equal(lesson.interactive.type, "daily-expression-lab");
assert.equal(lab.scenes.length, 3);
for (const scene of lab.scenes) {
  assert.ok(scene.requiredCueIds.every(id => scene.cues.some(cue => cue.id === id)));
  assert.ok(scene.question.options.some(option => option.id === scene.question.answerId));
}
assert.ok(lab.transfer.requiredCueIds.every(id => lab.transfer.cues.some(cue => cue.id === id)));
assert.ok(lab.transfer.question.options.some(option => option.id === lab.transfer.question.answerId));
assert.ok(schema.$defs.dailyExpressionLab && schema.$defs.dailyExpressionScene && schema.$defs.dailyExpressionTransfer);

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
const instance = "qa-daily-expression";
mount.innerHTML = dom.window.DailyExpressionLab.render(lesson, instance);
const root = () => mount.querySelector("[data-daily-expression-lab]");
const click = action => root().querySelector(`[data-delx-action="${action}"]`).click();
const cue = (kind, id) => root().querySelector(`[data-delx-cue="${kind}"][data-cue-id="${id}"]`).click();
const choose = (name, id) => {
  const input = root().querySelector(`[data-delx-answer="${name}"][value="${id}"]`);
  input.checked = true;
  input.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
};

assert.doesNotMatch(root().textContent, /答案：clarify/);
assert.equal(root().querySelectorAll("input[type=radio]").length, 0, "response is hidden until the context evidence is checked");
click("check-cues");
assert.match(root().textContent, /漏聽哪個細節/);
cue("scene", "missed-object"); cue("scene", "fragile-jars"); cue("scene", "morning-greeting"); click("check-cues");
assert.match(root().textContent, /漏聽哪個細節/);
cue("scene", "morning-greeting"); click("check-cues");
choose("scene", "guess"); click("answer");
assert.match(root().textContent, /clarification/);
choose("scene", "clarify"); click("answer");
assert.match(root().textContent, /道歉後接上關心與補救/);
assert.match(root().textContent, /Thanks for checking before moving them/);

cue("scene", "jay-caused-fall"); cue("scene", "classmate-concern"); click("check-cues");
choose("scene", "repair"); click("answer");
assert.match(root().textContent, /婉拒邀請時保留關係/);
cue("scene", "classmate-invites"); cue("scene", "rehearsal-conflict"); click("check-cues");
choose("scene", "polite-decline"); click("answer");
assert.match(root().textContent, /新情境遷移/);

click("check-transfer-cues");
assert.match(root().textContent, /新地點和關門時間/);
cue("transfer", "closing-time"); cue("transfer", "new-location"); click("check-transfer-cues");
choose("transfer", "assume-old"); click("transfer-answer");
assert.match(root().textContent, /時間和地點/);
choose("transfer", "confirm"); click("transfer-answer");
const explanation = root().querySelector("[data-delx-explanation]");
explanation.value = "需要確認時間和地點。";
explanation.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
click("finish-transfer");
assert.match(root().textContent, /引用 west entrance 與 4 p\.m\./);
root().querySelector("[data-delx-explanation]").value = "我要確認 west entrance 的新地點，並在 4 p.m. 前還書。";
root().querySelector("[data-delx-explanation]").dispatchEvent(new dom.window.Event("input", { bubbles: true }));
click("finish-transfer");
assert.match(root().textContent, /完成：你能依上下文選擇澄清/);
mount.innerHTML = dom.window.DailyExpressionLab.render(lesson, instance);
assert.match(root().textContent, /完成：你能依上下文選擇澄清/, "completion restores from lesson-instance storage");
click("reset");
assert.match(root().textContent, /對話 1\/3/);

assert.match(app, /DailyExpressionLab\.render/);
assert.match(html, /daily-expression-lab\.js\?v=3-iv-5-context-repair-1/);
assert.match(html, /daily-expression-lab\.css\?v=3-iv-5-context-repair-1/);
assert.match(css, /prefers-reduced-motion/);
console.log("3-IV-5 context cues, dialogue repair, apology, polite decline, service-message transfer, persistence, and reset: ok");

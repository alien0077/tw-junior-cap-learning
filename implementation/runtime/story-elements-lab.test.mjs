import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-10.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/story-elements-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/styles.css", import.meta.url), "utf8");
const lab = lesson.interactive.storyElementsLab;
assert.equal(lesson.interactive.type, "story-elements-lab");
assert.equal(lab.cards.length, 6);
for (const card of lab.cards) assert.ok(card.question.options.some(option => option.id === card.question.answer));
assert.ok(lab.synthesis.requiredEvidenceIds.every(id => lab.synthesis.evidence.some(ev => ev.id === id)));

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
mount.innerHTML = dom.window.StoryElementsLab.render(lesson, "qa-3-iv-10");
const root = () => mount.querySelector("[data-story-elements-lab]");
const click = selector => root().querySelector(selector).click();
const feedback = () => [...root().querySelectorAll(".story-elements-feedback")].at(-1).textContent;
const type = (field, value) => {
  const control = root().querySelector(`[data-se-text="${field}"]`);
  control.value = value;
  control.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
};
const choose = (field, id) => {
  const control = root().querySelector(`input[name^="${field}-"][value="${id}"]`);
  control.checked = true;
  control.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
};
const submitCard = answer => {
  choose("card", answer);
  click('[data-se-action="check-card"]');
};

assert.equal(root().querySelector(".story-elements-progress"), null);
assert.match(root().querySelector('[role="status"]').textContent, /預測尚未提交/);
click('[data-se-action="reveal"]');
assert.match(root().textContent, /至少 8 個字/);
type("prediction", "我猜黃色線結會連結某種共同守護的意義");
click('[data-se-action="reveal"]');
assert.equal(root().querySelectorAll(".story-elements-stage").length, 2);
assert.equal(root().querySelectorAll(".story-elements-choice").length, lab.cards[0].question.options.length);

const first = lab.cards[0];
const wrong = first.question.options.find(option => option.id !== first.question.answer).id;
submitCard(wrong);
assert.match(feedback(), /找出這段回答了哪些/);
submitCard(first.question.answer);
assert.match(feedback(), /共同建立時空/);
for (let index = 1; index < lab.cards.length; index += 1) {
  click('[data-se-action="next-card"]');
  const card = lab.cards[index];
  submitCard(card.question.answer);
  assert.match(feedback(), new RegExp(card.question.feedback.slice(0, 6)));
}
click('[data-se-action="next-card"]');
assert.ok(root().querySelector('[data-se-evidence="motive"]'));
assert.equal(root().querySelector('[data-se-action="check-synthesis"]').disabled, false);
click('[data-se-action="check-synthesis"]');
assert.match(feedback(), /先標出動機、關鍵選擇和結果/);

for (const id of lab.synthesis.requiredEvidenceIds) root().querySelector(`[data-se-evidence="${id}"]`).click();
choose("synthesis", lab.synthesis.question.answer);
type("explanation", "她想在霧中保護船員，危急時放下獎牌啟動信號，船隻因此轉離礁石，說明責任必須化成行動。");
click('[data-se-action="check-synthesis"]');
assert.match(root().textContent, /編輯註記完成/);
assert.equal(root().querySelector('[data-se-action="check-synthesis"]').disabled, true);
mount.innerHTML = dom.window.StoryElementsLab.render(lesson, "qa-3-iv-10");
assert.match(root().querySelector('[role="status"]').textContent, /編輯任務完成/);
root().querySelector('[data-se-evidence="choice"]').click();
assert.doesNotMatch(root().querySelector('[role="status"]').textContent, /編輯任務完成/);
assert.equal(root().querySelectorAll('input[name^="synthesis-"]:checked').length, 0);
type("explanation", "測試重置");
click('[data-se-action="reset"]');
assert.equal(root().querySelector('[data-se-text="prediction"]').value, "");
assert.equal(dom.window.localStorage.length, 0);
assert.match(app, /StoryElementsLab\.render/);
assert.match(html, /story-elements-lab\.js/);
assert.match(css, /@media\(max-width:480px\)\{\.story-elements-evidence li/);
assert.match(css, /prefers-reduced-motion:reduce\)\{\.story-elements-lab/);
assert.match(css, /\.story-elements-lab button\{min-height:44px/);
console.log("3-IV-10 prediction, six story-element annotations, retry, evidence-backed theme, persistence and invalidation: ok");

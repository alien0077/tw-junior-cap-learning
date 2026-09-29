import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(readFileSync(new URL("../../lessons/english/lesson-english-performance-3-iv-8.json", import.meta.url), "utf8"));
const source = readFileSync(new URL("../../site/message-reading-lab.js", import.meta.url), "utf8");
const app = readFileSync(new URL("../../site/app.js", import.meta.url), "utf8");
const html = readFileSync(new URL("../../site/index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("../../site/styles.css", import.meta.url), "utf8");
const lab = lesson.interactive.messageReadingLab;
assert.ok(lab.mainText.requiredEvidenceIds.every(id => lab.mainText.parts.some(part => part.id === id)));
assert.ok(lab.transfer.requiredEvidenceIds.every(id => lab.transfer.parts.some(part => part.id === id)));
assert.ok(lab.mainText.question.options.some(option => option.id === lab.mainText.question.answer));
assert.ok(lab.transfer.question.options.some(option => option.id === lab.transfer.question.answer));

const dom = new JSDOM("<main id=mount></main>", { url: "https://courseware.test/", runScripts: "outside-only" });
dom.window.eval(source);
const mount = dom.window.document.querySelector("#mount");
mount.innerHTML = dom.window.MessageReadingLab.render(lesson, "qa-3-iv-8");
const root = () => mount.querySelector("[data-message-reading-lab]");
const click = selector => root().querySelector(selector).click();
const evidence = (kind, id) => root().querySelector(`[data-message-evidence="${kind}"][data-part="${id}"]`).click();
const choose = (name, id) => {
  const input = root().querySelector(`input[name^="${name}-"][value="${id}"]`);
  input.checked = true;
  input.dispatchEvent(new dom.window.Event("change", { bubbles: true }));
};

assert.doesNotMatch(root().textContent, /答案：B/);
assert.equal(root().querySelectorAll(".message-reading-part").length, lab.mainText.parts.length);
assert.equal(root().querySelector('[data-message-evidence="main"]').disabled, true);
click('[data-message-action="predict"]');
assert.match(root().textContent, /至少 8 個字/);
const prediction = root().querySelector('[data-message-text="prediction"]');
prediction.value = "週末集會有改地點與借用設備的條件";
prediction.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
click('[data-message-action="predict"]');
assert.equal(root().querySelector('[data-message-evidence="main"]').disabled, false);
assert.match(root().querySelector(".message-reading-live").textContent, /預測已保存/);

evidence("main", "purpose");
evidence("main", "reason");
evidence("main", "decoy");
evidence("main", "entrance");
click('[data-message-action="check-evidence"]');
assert.match(root().textContent, /還漏了通知要求的行動欄位/);
for (const id of lab.mainText.requiredEvidenceIds) {
  const button = root().querySelector(`[data-message-evidence="main"][data-part="${id}"]`);
  if (button.getAttribute("aria-pressed") !== "true") evidence("main", id);
}
click('[data-message-action="check-evidence"]');
assert.match(root().textContent, /已同時保留時間／地點/);
choose("answer", "A");
click('[data-message-action="check-answer"]');
assert.match(root().textContent, /先逐欄核對/);
choose("answer", "B");
click('[data-message-action="check-answer"]');
assert.match(root().textContent, /主要內容正確/);
assert.ok(root().querySelector('[data-message-evidence="transfer"]'));

evidence("transfer", "condition");
evidence("transfer", "deadline");
choose("transferAnswer", "C");
const explanation = root().querySelector('[data-message-text="explanation"]');
explanation.value = "要早點告訴老師";
explanation.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
click('[data-message-action="check-transfer"]');
assert.match(root().textContent, /至少寫 15 字/);
const detailedExplanation = root().querySelector('[data-message-text="explanation"]');
detailedExplanation.value = "因為信中說若不能參加，要在星期二晚上前告訴老師，讓候補學生有機會補上。";
detailedExplanation.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
click('[data-message-action="check-transfer"]');
assert.match(root().textContent, /互動完成：預測、證據、文本理解與新文本遷移皆已保存/);

mount.innerHTML = dom.window.MessageReadingLab.render(lesson, "qa-3-iv-8");
assert.match(root().textContent, /互動完成：預測、證據、文本理解與新文本遷移皆已保存/);
assert.equal(root().querySelector('[data-message-evidence="main"][data-part="time-place"]').getAttribute("aria-pressed"), "true");
assert.equal(root().querySelector('[data-message-action="check-transfer"]').disabled, true);
assert.match(app, /MessageReadingLab\.render/);
assert.match(html, /message-reading-lab\.js/);
assert.match(css, /@media\(max-width:560px\)\{\.message-reading-lab/);
assert.match(css, /@media\(min-width:761px\) and \(max-width:900px\)\{\.unit-grid\{grid-template-columns:repeat\(2,minmax\(0,1fr\)\)\}\.unit-card\{min-width:0\}\.lesson-sections\{grid-template-columns:1fr\}\}/);
assert.match(css, /prefers-reduced-motion:reduce\)\{\.message-reading-lab/);
console.log("3-IV-8 prediction, evidence diagnostics, action summary, transfer, persistence, and accessibility hooks: ok");

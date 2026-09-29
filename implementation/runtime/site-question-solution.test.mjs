import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";
const component = readFileSync(new URL("../../site/question-detail.js", import.meta.url), "utf8");
const dom = new JSDOM("<main></main>", { runScripts: "outside-only" });
dom.window.eval(component);
const renderQuestionDetail = dom.window.renderQuestionDetail;

const question = JSON.parse(readFileSync(new URL("../../questions/english/question-english-performance-4-iv-1-1.json", import.meta.url), "utf8"));
dom.window.document.querySelector("main").innerHTML = renderQuestionDetail(question);
const root = dom.window.document.querySelector(".question-detail");
assert.match(root.getAttribute("aria-label"), /答案.*解析.*解題步驟/);
assert.match(root.querySelector(".answer-line").textContent, /答案：A/);
assert.match(root.querySelector(".answer-explanation").textContent, /close/);
assert.match(root.querySelector(".solution-strategy").textContent, /window/);
assert.equal(root.querySelectorAll(".solution-steps li").length, 5);
assert.match(root.querySelector(".solution-steps").textContent, /cloze/);

const unsafe = renderQuestionDetail({
  options: [{ id: "A", text: "<img src=x onerror=alert(1)>" }],
  answer: { value: "A", explanation: "<script>bad()</script>" },
  solutionStrategy: "<b>not markup</b>",
  solutionSteps: ["<svg onload=bad()>"] ,
});
const safeDom = new JSDOM(`<main>${unsafe}</main>`);
assert.equal(safeDom.window.document.querySelectorAll("img,script,svg").length, 0);
assert.match(safeDom.window.document.querySelector(".solution-strategy").textContent, /<b>not markup<\/b>/);

const missing = new JSDOM(`<main>${renderQuestionDetail({ options: [], answer: null })}</main>`);
assert.match(missing.window.document.querySelector(".solution-unavailable").textContent, /尚未提供/);
console.log("question cards render answer, explanation, strategy and detailed steps safely: ok");

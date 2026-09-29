import assert from "node:assert/strict";
import { JSDOM } from "jsdom";
import { renderStudentLesson, REQUIRED_STUDENT_SECTIONS } from "./student-lesson-shell.js";

const dom = new JSDOM("<main id='mount'></main>");
const spec = {
  lessonId: "cur-math-content-a-8-1", title: "A-8-1：二次式的乘法公式",
  status: { implementationStatus: "missing", qaStatus: "untested" },
  learningGoals: ["goal"], coreConcepts: ["concept"], contentFlow: ["flow"], misconceptions: ["misconception"],
  exitTicket: { prompt: "prompt", successCriteria: ["criterion"] }, capTransfer: { questionType: "transfer", stemConstraint: "constraint" },
  expressionExtension: { task: "student writes first" },
  interactiveBlocks: [{ id: "I01", component: "AlgebraBalanceBlock", purpose: "purpose", initialState: { mode: "predict" }, studentActions: ["action"], visualRules: ["rule"], misconceptionChecks: [{ id: "MC", trigger: "trigger", prompt: "prompt", expectedEvidence: "evidence" }], feedback: { correct: "correct", incorrect: "incorrect" } }]
};
const article = renderStudentLesson({ document: dom.window.document, mount: dom.window.document.querySelector("#mount"), spec });
assert.equal(article.querySelectorAll("section[data-section]").length, REQUIRED_STUDENT_SECTIONS.length + 1);
assert.equal(article.querySelectorAll(".interactive-block").length, 1);
assert.match(article.textContent, /容易錯在哪裡/);
console.log("student lesson shell contract: ok");

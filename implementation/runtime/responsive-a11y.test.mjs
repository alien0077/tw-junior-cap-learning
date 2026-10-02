import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";
import { renderStudentLesson } from "./student-lesson-shell.js";

const html = await readFile(new URL("../workbench.html", import.meta.url), "utf8");
const css = html.match(/<style>([\s\S]*?)<\/style>/)?.[1] ?? "";
assert.match(html, /name="viewport" content="width=device-width, initial-scale=1"/);
assert.match(css, /body\s*\{[^}]*max-width:\s*960px/);
assert.match(css, /\.interactive-controls\s*\{[^}]*flex-wrap:\s*wrap/);
assert.match(css, /button, input\s*\{[^}]*min-height:\s*44px/);
assert.match(css, /\.visualization-summary\s*\{[^}]*overflow-wrap:\s*anywhere/);
assert.match(css, /\.component-visual-body\s*\{[^}]*overflow-wrap:\s*anywhere/);
assert.match(css, /#unit\s*\{[^}]*width:\s*100%[^}]*max-width:\s*100%/);
assert.match(css, /\.math-live-canvas\s*\{[^}]*width:\s*100%[^}]*max-width:\s*100%/);
assert.match(css, /\.math-live-control input\[type="range"\]\s*\{[^}]*width:\s*100%[^}]*min-width:\s*0/);
assert.match(css, /\.math-live-table[^\{]*\{[^}]*table-layout:\s*fixed/);
assert.match(css, /prefers-reduced-motion:\s*reduce/);
assert.doesNotMatch(css, /body\s*\{[^}]*[;{]\s*width:\s*\d+px/);

const fixture = {
  lessonId: "cur-math-content-a-8-1", title: "測試單元",
  status: { implementationStatus: "missing", qaStatus: "untested" },
  learningGoals: ["goal"], coreConcepts: ["concept"], contentFlow: ["flow"], misconceptions: ["misconception"],
  exitTicket: { prompt: "prompt" }, capTransfer: { questionType: "transfer" },
  expressionExtension: { task: "task" },
  interactiveBlocks: [{
    id: "I01", component: "LanguageTimelineBlock", purpose: "purpose", initialState: { mode: "predict" },
    languageTimeline: {
      title: "語音互動測試", context: "更正寄件者。", sentence: ["I", "sent", "it."], prompt: "預測焦點。",
      choices: [{ word: "I", contrast: "寄件者", evidence: "語境" }, { word: "sent", contrast: "動作", evidence: "語境" }],
      correctWord: "I", transfer: { prompt: "更正收件人。", acceptedWord: "Mia", evidenceHint: "依角色判讀" },
    },
  }],
};

for (const width of [320, 375, 768]) {
  const dom = new JSDOM("<main id='mount'></main>", { pretendToBeVisual: true });
  Object.defineProperty(dom.window, "innerWidth", { configurable: true, value: width });
  const mount = dom.window.document.querySelector("#mount");
  const article = renderStudentLesson({ document: dom.window.document, mount, spec: fixture });
  assert.equal(dom.window.innerWidth, width);
  assert.ok(article.querySelector(".interactive-controls"), `controls at ${width}px`);
  const languageLab = article.querySelector(".language-timeline-lab");
  assert.ok(languageLab, `unit-specific language interaction at ${width}px`);
  assert.equal(languageLab.querySelector(".language-timeline-choices").hidden, true);
  languageLab.querySelector("input[aria-label='預測要承受對比重音的字']").value = "sent";
  languageLab.querySelector("button").click();
  assert.equal(languageLab.querySelector(".language-timeline-choices").hidden, false);
  assert.equal(languageLab.querySelectorAll(".language-timeline-choices button").length, 2);
  for (const button of article.querySelectorAll("button")) {
    assert.equal(button.type, "button");
    assert.ok(button.textContent.trim(), `button label at ${width}px`);
  }
  const output = article.querySelector("output");
  assert.equal(output.getAttribute("aria-live"), "polite");
  assert.equal(article.querySelector("input[name='I01-explanation']").getAttribute("aria-describedby"), output.id);
  const event = new dom.window.CustomEvent("reducedmotionchange", { detail: { enabled: true } });
  article.querySelector(".interactive-block").dispatchEvent(event);
  assert.equal(article.querySelector(".interactive-block").dataset.reducedMotion, "true");
}

console.log("responsive and accessibility contract: 320/375/768 ok");

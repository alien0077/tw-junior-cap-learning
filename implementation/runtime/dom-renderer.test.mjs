import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { JSDOM } from "jsdom";
import { renderInteractiveBlock } from "./dom-renderer.js";
import { RENDERER_COMPONENTS } from "./dom-renderer.js";

const dom = new JSDOM("<main id='mount'></main>");
const spec = { lessonId: "cur-math-content-a-8-1", coreConcepts: ["(a＋b)²＝a²＋2ab＋b²", "(a−b)²＝a²−2ab＋b²", "(a＋b)(a−b)＝a²−b²"], interactiveBlocks: [{ id: "I01", component: "AlgebraBalanceBlock", purpose: "測試", initialState: { mode: "predict" } }] };
const result = renderInteractiveBlock({ document: dom.window.document, mount: dom.window.document.querySelector("#mount"), spec });
assert.equal(result.root.querySelectorAll("button").length, 6);
result.root.querySelector("button").click();
assert.equal(result.engine.state.mode, "predict-submitted");
assert.match(result.root.querySelector("output").textContent, /已提交預測/);
assert.equal(result.root.querySelector("input").getAttribute("aria-label"), "用一句話說明觀察到的關係");
const buttons = [...result.root.querySelectorAll("button")];
buttons[1].click();
buttons[2].click();
result.root.querySelector("input").value = "因為證據支持我的觀察";
buttons[3].click();
buttons[4].click();
assert.equal(result.engine.state.mode, "verified");
assert.equal(result.root.querySelector("h3").textContent, "代數平衡");
assert.equal(result.root.querySelector(".visualization-summary").dataset.renderer, "AlgebraBalanceBlock");
assert.ok(result.root.querySelector(".visualization-summary").getAttribute("aria-label"));
assert.equal(result.root.querySelector(".component-visual-body").dataset.contentSource, "unit-spec");
assert.match(result.root.querySelector(".component-visual-prompts").textContent, /\(a＋b\)²/);
assert.equal(result.root.querySelector(".formula-model").dataset.formulaCount, "3");
assert.equal(result.root.querySelectorAll(".formula-model li").length, 3);
for (const component of RENDERER_COMPONENTS) {
  const mount = dom.window.document.createElement("div");
  const genericSpec = { lessonId: `cur-test-${component.toLowerCase()}`, interactiveBlocks: [{ id: `I-${component}`, component, purpose: "component contract", initialState: { mode: "predict" } }] };
  const rendered = renderInteractiveBlock({ document: dom.window.document, mount, spec: genericSpec });
  assert.equal(rendered.root.dataset.component, component);
  assert.equal(rendered.root.querySelectorAll("button").length, 6);
  assert.ok(rendered.root.querySelector(".interactive-fallback"));
  assert.ok(rendered.root.querySelector(".visualization-summary"));
  assert.equal(rendered.root.querySelector(".component-visual-body").dataset.component, component);
  assert.ok(rendered.root.querySelector(".component-visual-note"));
  assert.ok(rendered.root.querySelector(".component-visual-body").dataset.semanticModel);
  assert.equal(rendered.root.querySelectorAll(".component-visual-prompts li").length, 3);
}
assert.equal(RENDERER_COMPONENTS.length, 33);

const genreBundle = JSON.parse(readFileSync(new URL("../unit-specs.bundle.json", import.meta.url), "utf8"));
const genreSpec = genreBundle.units.find((unit) => unit.lessonId === "cur-english-performance-3-iv-16");
assert.equal(genreSpec.interactiveBlocks[0].component, "GenreReadingBlock");
const genreMount = dom.window.document.createElement("div");
const genre = renderInteractiveBlock({ document: dom.window.document, mount: genreMount, spec: genreSpec });
const genreLab = genre.root.querySelector(".genre-reading-lab");
assert.ok(genreLab);
const genreInputs = genreLab.querySelectorAll("input");
const genreButtons = [...genreLab.querySelectorAll("button")];
genreInputs[0].value = "公告";
genreButtons.find((button) => button.textContent === "提交預測").click();
assert.equal(genreLab.querySelector(".genre-reading-sources").hidden, true);
assert.match(genreLab.querySelector(".genre-reading-feedback").textContent, /提示/);
genreInputs[0].value = "日期表";
genreButtons.find((button) => button.textContent === "提交預測").click();
assert.equal(genre.engine.state.prediction, "日期表");
const calendar = genreButtons.find((button) => button.dataset.sourceId === "calendar");
calendar.click();
assert.match(genreLab.querySelector(".genre-reading-observation").textContent, /first and third Wednesday/);
assert.equal(calendar.getAttribute("aria-pressed"), "true");
genreInputs[1].value = "日期表把可收集的日期和時段排在一起，因此能回答何時交付。";
genreButtons.find((button) => button.textContent === "記錄證據說明").click();
assert.equal(genreLab.querySelector(".genre-reading-transfer").hidden, false);
assert.equal(genre.engine.state.explanation, genreInputs[1].value);
genreInputs[2].value = "日期表";
genreButtons.find((button) => button.textContent === "檢查遷移答案").click();
assert.match(genreLab.querySelector(".genre-reading-feedback").textContent, /分辨 why/);
genreInputs[2].value = "說明段落";
genreButtons.find((button) => button.textContent === "檢查遷移答案").click();
assert.equal(genre.engine.state.mode, "verified");
assert.equal(genre.engine.state.transferPassed, true);
assert.match(genreLab.querySelector(".genre-reading-progress").textContent, /第 4\/4 階段完成/);
const restoredGenreMount = dom.window.document.createElement("div");
const restoredGenreSpec = structuredClone(genreSpec);
restoredGenreSpec.interactiveBlocks[0].initialState = {
  mode: "verified", prediction: "日期表", selectedEvidence: ["calendar"],
  explanation: "日期表把日期和時段排在一起，因此可回答何時交付。",
  transferAnswer: "說明段落", transferPassed: true,
};
const restoredGenre = renderInteractiveBlock({ document: dom.window.document, mount: restoredGenreMount, spec: restoredGenreSpec });
assert.match(restoredGenre.root.querySelector(".interactive-status").textContent, /遷移已完成/);
assert.match(restoredGenre.root.querySelector(".genre-reading-progress").textContent, /第 4\/4 階段完成/);

const activityMount = dom.window.document.createElement("div");
const activitySpec = {
  lessonId: "cur-math-content-a-8-5",
  coreConcepts: ["最大公因式優先，再檢查平方差"],
  interactiveBlocks: [{
    id: "A85-I01", component: "StepwiseReasoningBlock", purpose: "因式分解步驟練習",
    initialState: { mode: "predict" },
    guidedActivity: {
      title: "地墊裁切單：把 6x²−24 完全分解",
      introduction: "逐步輸入並檢查。",
      stages: [
        { prompt: "最大公因式？", acceptedAnswers: ["6"], correctFeedback: "先提出 6。", hint: "比較係數。" },
        { prompt: "提出後括號？", acceptedAnswers: ["x²−4", "x^2-4"], correctFeedback: "辨認平方差。", hint: "各項除以 6。" },
        { prompt: "完全分解？", acceptedAnswers: ["6(x−2)(x+2)"], correctFeedback: "完成。", hint: "使用平方差。" },
      ],
      completionMessage: "完成三步並可展開驗算。",
    },
  }],
};
const activity = renderInteractiveBlock({ document: dom.window.document, mount: activityMount, spec: activitySpec });
const activityRoot = activity.root.querySelector(".guided-activity");
const activityInput = activityRoot.querySelector("input");
const activityButton = activityRoot.querySelector("button");
assert.equal(activityRoot.querySelector(".guided-activity-progress").textContent, "第 1/3 步");
activityInput.value = "3";
activityButton.click();
assert.equal(activityRoot.querySelector(".guided-activity-hint").hidden, false);
assert.equal(activityRoot.querySelector(".guided-activity-progress").textContent, "第 1/3 步");
activityInput.value = "6";
activityButton.click();
assert.equal(activityRoot.querySelector(".guided-activity-progress").textContent, "第 2/3 步");
activityInput.value = "x^2 - 4";
activityButton.click();
assert.equal(activityRoot.querySelector(".guided-activity-progress").textContent, "第 3/3 步");
activityInput.value = "6(x−2)(x+2)";
activityButton.click();
assert.equal(activityRoot.querySelector(".guided-activity-progress").textContent, "已完成 3/3 步");
assert.match(activityRoot.textContent, /完成三步並可展開驗算/);

const languageMount = dom.window.document.createElement("div");
const languageSpec = {
  lessonId: "cur-english-content-ab",
  interactiveBlocks: [{
    id: "CUR-ENGLISH-CONTENT-AB-I01",
    component: "LanguageTimelineBlock",
    purpose: "用語境解釋句子重音如何標記對比焦點",
    initialState: { mode: "predict", selectedEvidence: [] },
    languageTimeline: {
      title: "重音焦點工作室：把更正說清楚",
      context: "要更正寄件者是誰。",
      sentence: ["I", "sent", "the", "draft", "on", "Tuesday."],
      prompt: "先預測重音焦點。",
      choices: [
        { word: "I", contrast: "更正寄件者。", evidence: "情境指定寄件者。" },
        { word: "draft", contrast: "更正文件。", evidence: "不是寄件者。" },
      ],
      correctWord: "I",
      transfer: { prompt: "更正收件人。", acceptedWord: "Mia.", evidenceHint: "圈出收件人。" },
    },
  }],
};
const savedInteractiveStates = new Map();
const previousLocalStorage = globalThis.localStorage;
Object.defineProperty(globalThis, "localStorage", {
  configurable: true,
  value: {
    getItem: (key) => savedInteractiveStates.get(key) ?? null,
    setItem: (key, value) => savedInteractiveStates.set(key, String(value)),
  },
});
const language = renderInteractiveBlock({ document: dom.window.document, mount: languageMount, spec: languageSpec });
const lab = language.root.querySelector(".language-timeline-lab");
const labInputs = lab.querySelectorAll("input");
const labButtons = [...lab.querySelectorAll("button")];
assert.equal(lab.querySelector(".language-timeline-choices").hidden, true);
labInputs[0].value = "sent";
labButtons[0].click();
assert.equal(language.engine.state.prediction, "sent");
assert.equal(lab.querySelector(".language-timeline-choices").hidden, false);
labButtons.find((button) => button.textContent.includes("「I」")).click();
assert.equal(lab.querySelector(".language-timeline-sentence strong").textContent, "I");
assert.match(lab.querySelector(".language-timeline-observation").textContent, /一致/);
labInputs[1].value = "情境要更正寄件者，所以強調 I";
labButtons.find((button) => button.textContent.includes("記錄解釋")).click();
assert.equal(lab.querySelector(".language-timeline-progress").textContent, "階段 3/4：解釋已記錄；用新句子檢查能否遷移");
labInputs[2].value = "Mia";
labButtons.find((button) => button.textContent.includes("檢查遷移答案")).click();
assert.equal(language.engine.state.mode, "verified");
assert.equal(language.engine.state.transferPassed, true);
assert.equal(lab.querySelector(".language-timeline-progress").textContent, "階段 4/4：遷移完成");
const restoredLanguageMount = dom.window.document.createElement("div");
const restoredLanguage = renderInteractiveBlock({ document: dom.window.document, mount: restoredLanguageMount, spec: languageSpec });
assert.equal(restoredLanguage.engine.state.transferPassed, true);
assert.equal(restoredLanguage.root.querySelector(".language-timeline-progress").textContent, "階段 4/4：遷移完成");
assert.equal(restoredLanguage.root.querySelector(".language-timeline-lab input[aria-label='預測要承受對比重音的字']").value, "sent");

const compiledBundle = JSON.parse(readFileSync(new URL("../unit-specs.bundle.json", import.meta.url), "utf8"));
const readingSpec = compiledBundle.units.find((unit) => unit.lessonId === "cur-english-performance-3-iv-12");
assert.ok(readingSpec, "3-IV-12 must be present in the compiled workbench bundle");
assert.equal(readingSpec.interactiveBlocks[0].component, "TextEvidenceBlock");
assert.equal(readingSpec.interactiveBlocks[0].guidedActivity.stages.length, 6);
const readingMount = dom.window.document.createElement("div");
const reading = renderInteractiveBlock({ document: dom.window.document, mount: readingMount, spec: readingSpec });
const readingActivity = reading.root.querySelector(".guided-activity");
const readingInput = readingActivity.querySelector("input");
const readingSubmit = readingActivity.querySelector("button");
assert.equal(readingActivity.querySelector(".guided-activity-progress").textContent, "第 1/6 步");
readingInput.value = "掃描全文";
readingSubmit.click();
assert.equal(readingActivity.querySelector(".guided-activity-progress").textContent, "第 1/6 步", "incorrect prediction must not skip the current stage");
assert.equal(readingActivity.querySelector(".guided-activity-hint").hidden, false);
for (const stage of readingSpec.interactiveBlocks[0].guidedActivity.stages) {
  readingInput.value = stage.acceptedAnswers[0];
  readingSubmit.click();
}
assert.equal(readingActivity.querySelector(".guided-activity-progress").textContent, "已完成 6/6 步");
assert.match(readingActivity.textContent, /同一公告可因閱讀目的切換方法/);

const chartSpec = compiledBundle.units.find((unit) => unit.lessonId === "cur-english-performance-3-iv-4");
assert.ok(chartSpec, "3-IV-4 must be present in the compiled workbench bundle");
assert.equal(chartSpec.interactiveBlocks[0].component, "DataExplorerBlock");
assert.equal(chartSpec.interactiveBlocks[0].guidedActivity.stages.length, 5);
const chartMount = dom.window.document.createElement("div");
const chart = renderInteractiveBlock({ document: dom.window.document, mount: chartMount, spec: chartSpec });
const chartLab = chart.root.querySelector(".data-explorer-lab");
assert.ok(chartLab, "chart unit must mount its scale-manipulation lab");
const chartPrediction = chartLab.querySelector('input[type="number"]');
const chartSubmit = chartLab.querySelector("button");
const chartControls = chartLab.querySelector("fieldset");
assert.equal(chartControls.hidden, true, "answer and manipulation stay gated until prediction");
chartPrediction.value = "12";
chartSubmit.click();
assert.match(chartLab.querySelector(".data-explorer-feedback").textContent, /乘上每格/);
assert.equal(chartControls.hidden, true, "wrong prediction keeps evidence gated for retry");
chartPrediction.value = "20";
chartSubmit.click();
assert.equal(chartControls.hidden, false);
assert.match(chartLab.querySelector(".data-explorer-result").textContent, /4 格 × 每格 5 本 = 20 本/);
const chartScale = chartControls.querySelector('input[type="range"]');
chartScale.value = "10";
chartScale.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
assert.match(chartLab.querySelector(".data-explorer-result").textContent, /4 格 × 每格 10 本 = 40 本/);
const chartExplanation = chartControls.querySelector('input[type="text"]');
chartExplanation.value = "刻度單位改變，所以相同四格的總量改變";
chartControls.querySelectorAll("button")[0].click();
assert.match(chartLab.querySelector(".data-explorer-feedback").textContent, /說明通過/);

const cultureSpec = compiledBundle.units.find((unit) => unit.lessonId === "cur-english-performance-2-iv-14");
assert.ok(cultureSpec, "2-IV-14 must be present in the compiled workbench bundle");
assert.equal(cultureSpec.interactiveBlocks[0].guidedActivity.stages.length, 5);
assert.equal(cultureSpec.interactiveBlocks[0].languageTimeline.correctWord, "Some");
const cultureMount = dom.window.document.createElement("div");
const culture = renderInteractiveBlock({ document: dom.window.document, mount: cultureMount, spec: cultureSpec });
const cultureLab = culture.root.querySelector(".language-timeline-lab");
assert.equal(cultureLab.querySelector(".language-timeline-choices").hidden, true, "correct focus stays hidden until prediction");
assert.match(cultureLab.querySelector(".language-timeline-context")?.textContent ?? cultureLab.textContent, /some residents/);
const cultureLabInputs = cultureLab.querySelectorAll("input");
const cultureLabButtons = [...cultureLab.querySelectorAll("button")];
cultureLabInputs[0].value = "Some";
cultureLabButtons.find((button) => button.textContent.includes("提交預測")).click();
assert.equal(culture.engine.state.prediction, "Some");
assert.equal(cultureLab.querySelector(".language-timeline-choices").hidden, false);
cultureLabButtons.find((button) => button.textContent.includes("「paper」")).click();
assert.equal(cultureLab.querySelector(".language-timeline-sentence strong").textContent, "paper");
assert.match(cultureLab.querySelector(".language-timeline-observation").textContent, /無法證明參與者範圍/);
cultureLabButtons.find((button) => button.textContent.includes("「Some」")).click();
assert.equal(cultureLab.querySelector(".language-timeline-sentence strong").textContent, "Some");
cultureLabInputs[1].value = "Some 限定活動卡所記錄的居民，不能推成所有人。";
cultureLabButtons.find((button) => button.textContent.includes("記錄解釋")).click();
assert.equal(culture.engine.state.stressExplanation, "Some 限定活動卡所記錄的居民，不能推成所有人。");
cultureLabInputs[2].value = "this";
cultureLabButtons.find((button) => button.textContent.includes("檢查遷移答案")).click();
assert.equal(culture.engine.state.transferPassed, true);

const cultureGuided = culture.root.querySelector(".guided-activity");
const cultureGuidedInput = cultureGuided.querySelector("input");
const cultureGuidedButton = cultureGuided.querySelector("button");
assert.equal(cultureGuided.querySelector(".guided-activity-progress").textContent, "第 1/5 步");
cultureGuidedInput.value = "everyone";
cultureGuidedButton.click();
assert.equal(cultureGuided.querySelector(".guided-activity-hint").hidden, false);
for (const answer of ["some residents", "harvest walk", "no", "Some residents fold paper leaves at the harvest walk.", "this"]) {
  cultureGuidedInput.value = answer;
  cultureGuidedButton.click();
}
assert.equal(cultureGuided.querySelector(".guided-activity-progress").textContent, "已完成 5/5 步");
assert.match(cultureGuided.textContent, /你保留了來源與場合/);
if (previousLocalStorage === undefined) delete globalThis.localStorage;
else Object.defineProperty(globalThis, "localStorage", { configurable: true, value: previousLocalStorage });
console.log("DOM renderer contract: ok");

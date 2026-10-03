import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";
import { renderStudentLesson, REQUIRED_STUDENT_SECTIONS } from "./student-lesson-shell.js";
import { RENDERER_COMPONENTS } from "./dom-renderer.js";

const bundle = JSON.parse(await readFile(new URL("../unit-specs.bundle.json", import.meta.url), "utf8"));
const abIv1Lesson = JSON.parse(await readFile(new URL("../../lessons/chinese/lesson-chinese-content-ab-iv-1.json", import.meta.url), "utf8"));
const componentRegistry = JSON.parse(await readFile(new URL("../component-registry.json", import.meta.url), "utf8"));
assert.equal(bundle.units.length, 1027);
assert.equal(new Set(bundle.units.map((unit) => unit.lessonId)).size, 1027);
const abIv1Spec = bundle.units.find((unit) => unit.lessonId === "cur-chinese-content-ab-iv-1");
assert.equal(abIv1Spec.interactiveBlocks[0].component, "GuidedChoiceBlock");
assert.equal(abIv1Lesson.interactive.type, "chinese-manipulation-lab");
assert.equal(abIv1Lesson.interactive.steps.length, 3);
assert.match(abIv1Spec.fusedScope.currentEvidenceStatus, /textbook-chapter-content-and-content-review-pending/);
assert.match(abIv1Spec.fusedScope.fusionRule, /不得宣稱已讀完三版課本正文/);
assert.deepEqual([...RENDERER_COMPONENTS].sort(), Object.keys(componentRegistry.components).sort(), "every implementation-guide component must have a workbench renderer");
const subjectCounts = Object.groupBy(bundle.units, (unit) => unit.subject);
assert.deepEqual(Object.fromEntries(Object.entries(subjectCounts).map(([key, value]) => [key, value.length])), {
  chinese: 83, english: 136, math: 125, science: 325, social: 358,
});

const dom = new JSDOM("<main id='mount'></main>");
const mount = dom.window.document.querySelector("#mount");
for (const spec of bundle.units) {
  mount.replaceChildren();
  const article = renderStudentLesson({ document: dom.window.document, mount, spec });
  assert.equal(article.dataset.lessonId, spec.lessonId);
  assert.equal(article.querySelectorAll("section[data-section]").length, REQUIRED_STUDENT_SECTIONS.length + 1, spec.lessonId);
  assert.equal(article.querySelectorAll(".interactive-block").length, spec.interactiveBlocks.length, spec.lessonId);
  assert.equal(article.querySelectorAll(".component-visual-body").length, spec.interactiveBlocks.length, spec.lessonId);
  const guidedActivity = spec.interactiveBlocks[0].guidedActivity;
  const hasGuidedActivity = Boolean(guidedActivity);
  const hasLanguageTimeline = Boolean(spec.interactiveBlocks[0].languageTimeline);
  const hasDataExplorerLab = Boolean(spec.interactiveBlocks[0].dataExplorerLab);
  const genreLabSpec = spec.interactiveBlocks[0].genreReadingLab;
  const hasGenreReadingLab = Boolean(genreLabSpec);
  const expectedActivityButtons = spec.interactiveBlocks.reduce((count, block) => count + (block.guidedActivity ? 1 : 0) + (block.languageTimeline ? block.languageTimeline.choices.length + 3 : 0) + (block.dataExplorerLab ? 2 : 0) + (block.genreReadingLab ? block.genreReadingLab.sources.length + 3 : 0), 0);
  assert.ok(article.querySelectorAll("button").length >= 6 * spec.interactiveBlocks.length + expectedActivityButtons, `${spec.lessonId}: renderer must expose at least the baseline controls plus any semantic visual controls`);
  assert.equal(article.querySelectorAll(".guided-activity").length, hasGuidedActivity ? 1 : 0, spec.lessonId);
  assert.equal(article.querySelectorAll(".language-timeline-lab").length, hasLanguageTimeline ? 1 : 0, spec.lessonId);
  if (hasGuidedActivity) {
    const activity = article.querySelector(".guided-activity");
    assert.equal(activity.querySelector("h4").textContent, guidedActivity.title, spec.lessonId);
    assert.equal(activity.querySelector(".guided-activity-progress").getAttribute("aria-live"), "polite", spec.lessonId);
    const answer = activity.querySelector("input");
    const submit = activity.querySelector("button");
    if (spec.lessonId === "cur-english-performance-1-iv-6") {
      answer.value = "隨便猜一個答案";
      submit.click();
      assert.equal(activity.querySelector(".guided-activity-progress").textContent, "第 1/4 步", spec.lessonId);
      assert.equal(activity.querySelector(".guided-activity-hint").hidden, false, spec.lessonId);
      assert.match(activity.querySelector(".guided-activity-hint").textContent, /回到開頭/);
    }
    for (const stage of guidedActivity.stages) {
      answer.value = stage.acceptedAnswers[0];
      submit.click();
    }
    assert.equal(activity.querySelector(".guided-activity-progress").textContent, `已完成 ${guidedActivity.stages.length}/${guidedActivity.stages.length} 步`, spec.lessonId);
    assert.match(activity.textContent, new RegExp(guidedActivity.completionMessage.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")), spec.lessonId);
  }
  if (hasDataExplorerLab) {
    const lab = article.querySelector(".data-explorer-lab");
    assert.ok(lab, spec.lessonId);
    assert.equal(lab.querySelector('input[type="number"]').getAttribute("aria-label"), spec.interactiveBlocks[0].dataExplorerLab.predictionPrompt, spec.lessonId);
    assert.equal(lab.querySelector('input[type="range"]').getAttribute("aria-label"), spec.interactiveBlocks[0].dataExplorerLab.manipulationPrompt, spec.lessonId);
  }
  if (hasGenreReadingLab) {
    const lab = article.querySelector(".genre-reading-lab");
    assert.ok(lab, spec.lessonId);
    const inputs = lab.querySelectorAll("input");
    const buttons = [...lab.querySelectorAll("button")];
    inputs[0].value = "日期表";
    buttons.find((button) => button.textContent === "提交預測").click();
    assert.equal(spec.interactiveBlocks[0].initialState.showAnswer, false, spec.lessonId);
    buttons.find((button) => button.dataset.sourceId === "calendar").click();
    assert.match(lab.querySelector(".genre-reading-observation").textContent, /When can residents bring/);
    inputs[1].value = "日期表對齊了日期和時間，所以可回答何時交付。";
    buttons.find((button) => button.textContent === "記錄證據說明").click();
    inputs[2].value = "說明段落";
    buttons.find((button) => button.textContent === "檢查遷移答案").click();
    assert.match(lab.querySelector(".genre-reading-progress").textContent, /第 4\/4 階段完成/);
  }
  assert.ok(article.querySelector(".interactive-fallback"), spec.lessonId);
}

console.log("workbench full bundle traversal: 1027/1027 lessons rendered");

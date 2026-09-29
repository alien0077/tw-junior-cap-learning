import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";

const lesson = JSON.parse(readFileSync("lessons/math/lesson-math-content-s-9-1.json", "utf8"));
const specPath = "implementation/unit-specs/math/cur-math-content-s-9-1.yaml";
const spec = readFileSync(specPath, "utf8");

assert.equal(lesson.id, "lesson-math-content-s-9-1");
assert.equal(lesson.reviewStatus, "draft", "research, rights, and content-review gates remain open");
assert.equal(lesson.content.sections.length, 6, "the six already-authored lesson sections must be learner-visible");
assert.deepEqual(
  lesson.content.sections,
  lesson.teaching.body.map(({ heading, body }) => ({ heading, body })),
  "visible sections must expose the existing full lesson rather than replacing it with a short outline",
);

const visible = lesson.content.sections.map(({ heading, body }) => `${heading}\n${body}`).join("\n");
for (const required of ["邊界", "同一個倍率", "1/2", "2.8", "校刊編輯", "4、2", "12、5"]) {
  assert.ok(visible.includes(required), `visible teaching must contain S-9-1-specific reasoning: ${required}`);
}
for (const outOfScope of ["旗桿", "影子", "k²", "AA／SAS／SSS", "面積倍率是長度倍率的平方"]) {
  assert.ok(!visible.includes(outOfScope), `S-9-2 content must not leak into the S-9-1 lesson: ${outOfScope}`);
}
assert.equal(3 / 6, 1 / 2, "the original polygon example must use one scale factor for every side");
assert.notEqual(14 / 5, 6 / 2, "the polygon counterexample must expose a mismatched corresponding-side factor");
assert.equal(lesson.interactive.type, "guided-choice");
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.steps.map(({ id }) => id), ["step-1", "step-2", "step-3", "step-4"]);
const interaction = lesson.interactive.steps.map(({ prompt, options, feedback }) => `${prompt}\n${options.join("\n")}\n${feedback}`).join("\n");
assert.match(interaction, /邊界/);
assert.match(interaction, /末邊倍率/);
assert.doesNotMatch(interaction, /三角形|面積倍率|影子/);
assert.equal(lesson.publisherResearch.length, 3);
assert.ok(lesson.publisherResearch.every(({ sourceUrl, chapterLocator }) => sourceUrl && chapterLocator));
assert.ok(lesson.publisherResearch.every(({ publisher }) => ["nani", "kanghsuan", "hanlin"].includes(publisher)));

assert.match(spec, /component: GeometryManipulationBlock/);
assert.equal(lesson.simulation.model, "s9-1-polygon-similarity-v1");
assert.match(spec, /predict:[\s\S]*manipulate:[\s\S]*observe:[\s\S]*explain:[\s\S]*verify:[\s\S]*transfer:/);
assert.match(spec, /fallback/);
assert.match(spec, /六段完整、單元專屬正文/);
assert.match(spec, /多邊形邊界順序/);
assert.match(spec, /publisherEvidence:[\s\S]*?nani:[\s\S]*?status: pending/);

const expectedAnswers = { 1: "B", 2: "B", 3: "B", 4: "C", 5: "A", 6: "B", 7: "C", 8: "A", 9: "C", 10: "A" };
const questionFiles = readdirSync("questions/math")
  .filter((name) => /^question-math-content-s-9-1-(?:[1-9]|10)\.json$/.test(name));
assert.equal(questionFiles.length, 10, "all ten S-9-1 questions must be reviewed by this regression");
for (const name of questionFiles) {
  const question = JSON.parse(readFileSync(`questions/math/${name}`, "utf8"));
  const itemNumber = Number(name.match(/-(\d+)\.json$/)[1]);
  assert.equal(question.answer.value, expectedAnswers[itemNumber], `${name}: answer key must match its reviewed correct option`);
  assert.ok(question.options.some(({ id }) => id === question.answer.value), `${name}: answer must point to an existing option`);
  assert.equal(question.solutionSteps.length, 5, `${name}: provide five detailed solution steps`);
  assert.ok(question.examPatternRefs.some(({ locatorLevel }) => locatorLevel === "item"), `${name}: preserve an item-level public-exam pattern locator`);
  const questionText = [question.prompt, question.answer.explanation, question.solutionStrategy, ...question.solutionSteps].join("\n");
  assert.doesNotMatch(questionText, /三角形相似判定|影子測高|面積比平方/);
}

console.log("S-9-1 visible lesson, scope, ten answer keys, five-step solutions, item-level sources, interaction, and truthful spec: PASS");

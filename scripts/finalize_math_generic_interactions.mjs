import { readdir, readFile, writeFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const readText = rel => readFile(new URL(rel, ROOT), "utf8");
const readJson = async rel => JSON.parse(await readText(rel));
const writeJson = async (rel, value) => writeFile(new URL(rel, ROOT), `${JSON.stringify(value, null, 2)}\n`);
const replaceOnce = (text, before, after, label) => {
  if (!text.includes(before)) throw new Error(`missing patch anchor: ${label}`);
  return text.replace(before, after);
};

const lessonFiles = (await readdir(new URL("lessons/math/", ROOT))).filter(name => name.endsWith(".json")).sort();
let converted = 0;
for (const file of lessonFiles) {
  const path = `lessons/math/${file}`;
  const lesson = await readJson(path);
  if (lesson.reviewStatus === "deprecated" || lesson.simulation?.engine !== "concept-explorer") continue;
  const sim = lesson.simulation;
  if (lesson.id === "lesson-math-content-a-7-8") {
    lesson.simulation = { ...sim, engine: "math-inequality-range", mode: "model", model: "a-7-8-inequality-range-v1" };
  } else if (lesson.id === "lesson-math-content-a-8-2") {
    lesson.simulation = { ...sim, engine: "math-expression-lab", mode: "model", model: "a-8-2-polynomial-meaning-v1" };
  } else {
    const steps = lesson.interactive?.steps;
    if (!Array.isArray(steps) || steps.length < 3) throw new Error(`${lesson.id}: generic simulation has fewer than 3 unit-specific guided steps`);
    for (const [index, step] of steps.entries()) {
      if (!step?.prompt || !Array.isArray(step.options) || step.options.length < 2 || !step.answer || !step.feedback) {
        throw new Error(`${lesson.id}: guided step ${index + 1} is incomplete`);
      }
    }
    lesson.simulation = {
      ...sim,
      engine: "math-reasoning-lab",
      mode: "model",
      model: `${lesson.id.replace(/^lesson-math-/, "")}-reasoning-v1`,
      goal: sim.goal || lesson.interactive.goal || `操作並驗證「${lesson.title}」的數學推理。`,
      mission: sim.mission || lesson.interactive.scenario || "逐步作答、讀取即時回饋，再用證據修正推理。",
    };
  }
  lesson.updatedAt = "2026-10-01";
  await writeJson(path, lesson);
  converted += 1;
}

for (const lessonId of ["lesson-math-content-root-a", "lesson-math-content-s-9-1", "lesson-math-content-s-9-13"]) {
  const files = (await readdir(new URL("questions/math/", ROOT))).filter(name => name.endsWith(".json"));
  let count = 0;
  for (const file of files) {
    const path = `questions/math/${file}`;
    const q = await readJson(path);
    if (q.lessonId !== lessonId) continue;
    q.reviewStatus = "content-reviewed";
    q.updatedAt = "2026-10-01";
    await writeJson(path, q);
    count += 1;
  }
  if (count !== 10) throw new Error(`${lessonId}: expected 10 questions, found ${count}`);
}

let simulations = await readText("site/simulations.js");
if (!simulations.includes('if (engine === "math-reasoning-lab")')) {
  simulations = replaceOnce(
    simulations,
    '    "math-equation-meaning": { x: 5 },\n    "math-expression-lab": { x: 2 },',
    '    "math-equation-meaning": { x: 5 },\n    "math-reasoning-lab": { reasoningStep: 0, reasoningChoice: "" },\n    "math-expression-lab": { x: 2 },',
    "reasoning defaults",
  );
  simulations = replaceOnce(
    simulations,
    '"math-ticket-equation": "票券等量模型", "math-equation-meaning": "方程式意義檢驗臺", "math-function-graph": "函數圖形實驗室",',
    '"math-ticket-equation": "票券等量模型", "math-equation-meaning": "方程式意義檢驗臺", "math-reasoning-lab": "數學推理實驗室", "math-function-graph": "函數圖形實驗室",',
    "reasoning label",
  );
  const branch = `    if (engine === "math-reasoning-lab") {\n      const steps = lesson.interactive?.steps || [];\n      if (!steps.length) return \`${'${designed}'}<p role="status">本課尚缺可操作的推理步驟。</p>\`;\n      const index = clamp(Number(state.reasoningStep || 0), 0, steps.length - 1);\n      const step = steps[index];\n      const selected = state.reasoningChoice || "";\n      const correct = selected === step.answer;\n      const choices = step.options.map((option, optionIndex) => { const key = String.fromCharCode(65 + optionIndex); return \`<button type="button" data-reasoning-choice="\${key}" aria-pressed="\${selected === key}">\${key}. \${esc(option)}</button>\`; }).join("");\n      const feedback = !selected ? "先選一個答案，再依回饋修正。" : correct ? step.feedback : "這個選擇還不符合本步條件；回看題幹中的量、關係或證據後再試一次。";\n      return \`${'${designed}'}<section class="sim-reasoning-lab" aria-label="數學推理實驗室"><p>\${esc(lesson.interactive?.scenario || lesson.simulation.mission)}</p><p><b>進度：</b>第 \${index + 1}／\${steps.length} 步</p><fieldset><legend>\${esc(step.prompt)}</legend><div class="sim-actions">\${choices}</div></fieldset><p class="sim-reasoning-feedback" role="status" aria-live="polite">\${esc(feedback)}</p><div class="sim-actions"><button type="button" data-reasoning-nav="prev" \${index === 0 ? "disabled" : ""}>上一步</button><button type="button" data-reasoning-nav="next" \${!correct || index === steps.length - 1 ? "disabled" : ""}>下一步</button></div><p>每一步都必須先作答並讀取證據回饋；錯答不會直接揭露正解。</p></section>\`;\n    }\n`;
  simulations = replaceOnce(simulations, '    const evidence = ["直接觀察", "模型或資料", "可檢查的限制"][state.evidence - 1];', `${branch}    const evidence = ["直接觀察", "模型或資料", "可檢查的限制"][state.evidence - 1];`, "reasoning renderer");
  simulations = replaceOnce(
    simulations,
    'active?.matches("[data-design-step]") ? ["data-design-step", active.dataset.designStep] :',
    'active?.matches("[data-reasoning-choice]") ? ["data-reasoning-choice", active.dataset.reasoningChoice] : active?.matches("[data-reasoning-nav]") ? ["data-reasoning-nav", active.dataset.reasoningNav] : active?.matches("[data-design-step]") ? ["data-design-step", active.dataset.designStep] :',
    "reasoning focus persistence",
  );
  simulations = replaceOnce(
    simulations,
    '    const ecoSite = event.target.closest("[data-eco-site]");',
    '    const reasoningChoice = event.target.closest("[data-reasoning-choice]");\n    if (reasoningChoice) { update(root, { reasoningChoice: reasoningChoice.dataset.reasoningChoice }); return; }\n    const reasoningNav = event.target.closest("[data-reasoning-nav]");\n    if (reasoningNav) {\n      const state = read(lesson.simulation);\n      const steps = lesson.interactive?.steps || [];\n      const index = clamp(Number(state.reasoningStep || 0), 0, Math.max(0, steps.length - 1));\n      const direction = reasoningNav.dataset.reasoningNav;\n      if (direction === "prev") update(root, { reasoningStep: Math.max(0, index - 1), reasoningChoice: "" });\n      if (direction === "next" && state.reasoningChoice === steps[index]?.answer) update(root, { reasoningStep: Math.min(steps.length - 1, index + 1), reasoningChoice: "" });\n      return;\n    }\n    const ecoSite = event.target.closest("[data-eco-site]");',
    "reasoning click handlers",
  );
  await writeFile(new URL("site/simulations.js", ROOT), simulations);
}

let audit = await readText("scripts/audit_math_coverage.mjs");
if (!audit.includes('  "math-reasoning-lab",')) {
  audit = replaceOnce(audit, '  "math-equation-meaning",\n  "math-expression-lab",', '  "math-equation-meaning",\n  "math-reasoning-lab",\n  "math-expression-lab",', "audit reasoning engine registration");
  await writeFile(new URL("scripts/audit_math_coverage.mjs", ROOT), audit);
}

console.log(`converted ${converted} active generic math simulations; reviewed 30 linked questions`);

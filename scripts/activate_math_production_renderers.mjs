import { readFile, writeFile } from "node:fs/promises";

const target = new URL("../site/simulations.js", import.meta.url);
let source = await readFile(target, "utf8");

const engines = [
  "math-number-line",
  "math-inequality-range",
  "math-algebra-balance",
  "math-ticket-equation",
  "math-equation-meaning",
  "math-reasoning-lab",
  "math-expression-lab",
  "math-function-graph",
  "math-system-graph",
  "math-geometry",
  "math-data-lab",
  "math-probability-lab",
];

const oldGuard = '    if (designed && !hasDedicatedRutherfordModel && !hasDedicatedPlantTransportModel && !hasDedicatedPondFoodWebModel && lesson.simulation.model !== "fa-iv-4-atmospheric-temperature-profile" && lesson.simulation.model !== "ca-iv-2-solution-identification" && lesson.simulation.model !== "ecosystem-scale-boundary" && engine !== "math-system-graph" && engine !== "math-inequality-range" && engine !== "math-expression-lab") return designed;';
const newGuard = `    const hasDedicatedMathRenderer = ${JSON.stringify(engines)}.includes(engine);\n    if (designed && !hasDedicatedMathRenderer && !hasDedicatedRutherfordModel && !hasDedicatedPlantTransportModel && !hasDedicatedPondFoodWebModel && lesson.simulation.model !== "fa-iv-4-atmospheric-temperature-profile" && lesson.simulation.model !== "ca-iv-2-solution-identification" && lesson.simulation.model !== "ecosystem-scale-boundary") return designed;`;

if (source.includes(oldGuard)) {
  source = source.replace(oldGuard, newGuard);
} else if (!source.includes("const hasDedicatedMathRenderer =")) {
  throw new Error("site/simulations.js: expected learningDesign early-return guard was not found");
}

const prefixRepairs = [
  [
    '    if (engine === "math-number-line") {\n      const n = state.n;\n      return `<div class="sim-stage">',
    '    if (engine === "math-number-line") {\n      const n = state.n;\n      return `${designed}<div class="sim-stage">',
  ],
  [
    '    if (engine === "math-algebra-balance") {\n      const solution = state.target - state.addend;\n      return `<div class="sim-stage sim-equation">',
    '    if (engine === "math-algebra-balance") {\n      const solution = state.target - state.addend;\n      return `${designed}<div class="sim-stage sim-equation">',
  ],
  [
    '    if (engine === "math-function-graph") {\n      const y = state.m * state.x + state.b;',
    '    if (engine === "math-function-graph") {\n      const y = state.m * state.x + state.b;',
  ],
  [
    '      return `<div class="sim-stage"><svg viewBox="0 0 360 260" role="img" aria-label="y 等於 ${state.m}x 加 ${state.b} 的圖形',
    '      return `${designed}<div class="sim-stage"><svg viewBox="0 0 360 260" role="img" aria-label="y 等於 ${state.m}x 加 ${state.b} 的圖形',
  ],
  [
    '      const area = state.base * state.height / 2;\n      return `<div class="sim-stage"><svg viewBox="0 0 360 220" role="img" aria-label="底為 ${state.base}、高為 ${state.height} 的三角形">',
    '      const area = state.base * state.height / 2;\n      return `${designed}<div class="sim-stage"><svg viewBox="0 0 360 220" role="img" aria-label="底為 ${state.base}、高為 ${state.height} 的三角形">',
  ],
  [
    '    if (engine === "math-data-lab") {\n      const values = [state.a, state.b, state.c], mean = (values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1);\n      return `<div class="sim-stage">',
    '    if (engine === "math-data-lab") {\n      const values = [state.a, state.b, state.c], mean = (values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1);\n      return `${designed}<div class="sim-stage">',
  ],
  [
    '    if (engine === "math-probability-lab") {\n      const rate = state.trials ? Math.round(state.hits / state.trials * 100) : 0;\n      return `<div class="sim-stage">',
    '    if (engine === "math-probability-lab") {\n      const rate = state.trials ? Math.round(state.hits / state.trials * 100) : 0;\n      return `${designed}<div class="sim-stage">',
  ],
];

for (const [before, after] of prefixRepairs) {
  if (before === after) continue;
  if (source.includes(before)) source = source.replace(before, after);
  else if (!source.includes(after)) throw new Error(`site/simulations.js: expected production-renderer prefix not found: ${before.slice(0, 80)}`);
}

const required = [
  "const hasDedicatedMathRenderer =",
  'if (engine === "math-number-line")',
  'if (engine === "math-algebra-balance")',
  'if (engine === "math-function-graph")',
  'if (engine === "math-geometry")',
  'if (engine === "math-data-lab")',
  'if (engine === "math-probability-lab")',
  'if (engine === "math-reasoning-lab")',
];
for (const token of required) if (!source.includes(token)) throw new Error(`site/simulations.js missing ${token}`);

await writeFile(target, source, "utf8");
console.log("Math production renderers are reachable even when learningDesign is present; dedicated models retain the authored learning design where applicable.");

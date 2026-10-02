import { readdir, readFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const readText = rel => readFile(new URL(rel, ROOT), "utf8");
const readJson = async rel => JSON.parse(await readText(rel));
const list = async rel => (await readdir(new URL(rel, ROOT))).sort();

const lessonFiles = (await list("lessons/math/" )).filter(name => name.endsWith(".json"));
const questionFiles = (await list("questions/math/" )).filter(name => name.endsWith(".json"));
const specFiles = (await list("implementation/unit-specs/math/" )).filter(name => name.endsWith(".yaml"));
const reportFiles = new Set((await list("implementation/reports/" )).filter(name => /^math-.*first-pass-review\.json$/.test(name)));
const productionRendererSource = `${await readText("site/simulations.js")}\n${await readText("site/math-visual-labs.js")}\n${await readText("site/math-gold-standard.js")}\n${await readText("site/math-number-family.js")}\n${await readText("site/math-geometry-family.js")}`;
const productionMathEngines = new Set([
  "math-number-line",
  "math-inequality-range",
  "math-algebra-balance",
  "math-visual-area",
  "math-polynomial-model",
  "math-system-model",
  "math-quadratic-model",
  "math-factor-model",
  "math-ticket-equation",
  "math-equation-meaning",
  "math-reasoning-lab",
  "math-expression-lab",
  "math-function-graph",
  "math-system-graph",
  "math-geometry",
  "math-data-lab",
  "math-probability-lab",
]);
const productionRendererSignatures = new Map([
  ["math-quadratic-model", ["renderQuadraticLab", "mvl-quadratic-meaning", "quadCompleteSquare", "quadDeltaPrediction"]],
  ["math-system-model", ["renderSystemLab", "mvl-system-cards", "eliminationMethod", "systemMeaningTransfer"]],
  ["math-polynomial-model", ["renderPolynomialOps", "mvl-poly-board", "subtractPrediction", "polyTransfer"]],
  ["math-visual-area", ["renderArea", "mvl-area", "transferPrediction", 'role="img"']],
  ["math-factor-model", ["renderFactor", "mvl-factor-board", "factorTransfer", "mvl-token"]],
  ["math-number-line", ['slider("n"', 'role="img"', "sim-marker"]],
  ["math-inequality-range", ["data-inequality-relation", 'slider("boundary"', 'role="img"']],
  ["math-algebra-balance", ['class="balance"', 'slider("addend"', 'slider("target"']],
  ["math-ticket-equation", ["data-ticket-action", "sim-ticket-feedback"]],
  ["math-equation-meaning", ["sim-equation-meaning", 'slider("x"', 'class="balance"']],
  ["math-reasoning-lab", ["data-reasoning-choice", "data-reasoning-nav", "sim-reasoning-feedback"]],
  ["math-expression-lab", ["data-expression-original", "data-expression-reduced", 'slider("x"']],
  ["math-function-graph", ['slider("m"', 'slider("b"', 'role="img"']],
  ["math-system-graph", ['slider("sum"', "交點", 'role="img"']],
  ["math-geometry", ["math-geometry", 'role="img"', "sim-marker"]],
  ["math-data-lab", ["math-data-lab", 'slider("a"', 'slider("b"']],
  ["math-probability-lab", ["math-probability-lab", "trials", "role=\"status\""]],
]);
const productionModelRendererSignatures = new Map([
  ["d-9-2-relative-frequency-v1", ["renderProbability", "mgs-probability", "d92Prediction", "d92Transfer"]],
  ["d-9-1-boxplot-iqr-v1", ["renderBoxPlot", "mgs-boxplot", "d91Prediction", "d91Transfer"]],
  ["s-8-6-pythagorean-area-v1", ["renderPythagorean", "mgs-pythagorean", "s86Prediction", "s86Transfer"]],
  ["f-8-2-linear-parameter-v1", ["renderFunction", "mgs-function", "f82Mode", "f82Transfer"]],
  ["n-7-3-signed-operations-v1", ["renderSigned", "mgs-signed", "n73Prediction", "n73Transfer"]],
  ["a-7-3-linear-equation-check-v1", ["renderLinearEquationCheck", "mvl-linear-equation", "linearCandidate", "linearTransfer"]],
]);

const lessons = [];
for (const file of lessonFiles) lessons.push({ file, ...(await readJson(`lessons/math/${file}`)) });
const questions = [];
for (const file of questionFiles) questions.push({ file, ...(await readJson(`questions/math/${file}`)) });

const questionsByLesson = new Map();
for (const q of questions) {
  if (!questionsByLesson.has(q.lessonId)) questionsByLesson.set(q.lessonId, []);
  questionsByLesson.get(q.lessonId).push(q);
}

const specs = new Map();
for (const file of specFiles) {
  const text = await readText(`implementation/unit-specs/math/${file}`);
  const lessonId = text.match(/^\s*lessonId:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  const component = text.match(/^\s*component:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  const designStatus = text.match(/^\s*designStatus:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  const implementationStatus = text.match(/^\s*implementationStatus:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  const qaStatus = text.match(/^\s*qaStatus:\s*([^\n#]+)/m)?.[1]?.trim().replace(/^['"]|['"]$/g, "");
  if (lessonId) specs.set(lessonId, { file, component, designStatus, implementationStatus, qaStatus });
}

function reportCandidates(lessonFile) {
  const stem = lessonFile.replace(/^lesson-math-/, "").replace(/\.json$/, "");
  const candidates = [`math-${stem}-first-pass-review.json`];
  if (stem.startsWith("content-")) candidates.push(`math-${stem.slice("content-".length)}-first-pass-review.json`);
  return candidates;
}

function hasProductionRenderer(engine, model = null) {
  if (!engine || !productionMathEngines.has(engine)) return false;
  const modelSignatures = productionModelRendererSignatures.get(model) || [];
  if (modelSignatures.length && !modelSignatures.every(signature => productionRendererSource.includes(signature))) return false;
  const signatures = productionRendererSignatures.get(engine) || [];
  if (["math-visual-area", "math-factor-model", "math-polynomial-model", "math-system-model", "math-quadratic-model"].includes(engine)) {
    return signatures.every(signature => productionRendererSource.includes(signature));
  }
  if (modelSignatures.length) return true;
  if (!productionRendererSource.includes(`if (engine === "${engine}")`)) return false;
  return signatures.every(signature => productionRendererSource.includes(signature));
}

const rows = lessons.map(lesson => {
  const qs = questionsByLesson.get(lesson.id) || [];
  const specId = lesson.id.replace(/^lesson-math-/, "cur-math-");
  const directSpec = specs.get(specId) || null;
  const lineageSpecIds = (lesson.knowledgeIds || [])
    .filter(id => typeof id === "string" && id.startsWith("kg-math-"))
    .map(id => id.replace(/^kg-/, "cur-"));
  const resolvedSpecId = [specId, ...lineageSpecIds].find(id => specs.has(id)) || null;
  const resolvedSpec = resolvedSpecId ? specs.get(resolvedSpecId) : null;
  const reports = reportCandidates(lesson.file).filter(name => reportFiles.has(name));
  const simulationEngine = lesson.simulation?.engine || null;
  return {
    id: lesson.id,
    file: lesson.file,
    reviewStatus: lesson.reviewStatus || "missing",
    questionCount: qs.length,
    questionDrafts: qs.filter(q => q.reviewStatus !== "content-reviewed").length,
    simulationId: lesson.simulation?.id || null,
    simulationEngine,
    simulationModel: lesson.simulation?.model || null,
    simulationGoal: Boolean(lesson.simulation?.goal),
    simulationMission: Boolean(lesson.simulation?.mission),
    productionRenderer: hasProductionRenderer(simulationEngine, lesson.simulation?.model || null),
    interactiveType: lesson.interactive?.type || null,
    spec: resolvedSpec,
    directSpec,
    specResolution: directSpec ? "direct" : resolvedSpec ? "knowledge-lineage" : null,
    resolvedSpecId,
    reports,
  };
});

function rowIsActive(row) { return row.reviewStatus !== "deprecated"; }
const countBy = values => values.reduce((acc, value) => (acc[value || "missing"] = (acc[value || "missing"] || 0) + 1, acc), {});

const summary = {
  lessonCount: lessons.length,
  questionCount: questions.length,
  exactTenQuestions: rows.filter(r => r.questionCount === 10).length,
  lessonStatusCounts: countBy(rows.map(r => r.reviewStatus)),
  simulationEngineCounts: countBy(rows.map(r => r.simulationEngine)),
  interactiveTypeCounts: countBy(rows.map(r => r.interactiveType)),
  activeNonReviewedQuestionGroups: rows.filter(r => rowIsActive(r) && r.questionDrafts > 0).length,
  deprecatedNonReviewedQuestionGroups: rows.filter(r => !rowIsActive(r) && r.questionDrafts > 0).length,
  lessonsWithSimulation: rows.filter(r => r.simulationEngine).length,
  activeLessonsWithoutSimulation: rows.filter(r => !r.simulationEngine && rowIsActive(r)).length,
  activeLessonsWithProductionRenderer: rows.filter(r => rowIsActive(r) && r.productionRenderer).length,
  activeGenericSimulationCount: rows.filter(r => rowIsActive(r) && r.simulationEngine === "concept-explorer").length,
  uniqueActiveSimulationIds: new Set(rows.filter(rowIsActive).map(r => r.simulationId).filter(Boolean)).size,
  lessonsWithInteractive: rows.filter(r => r.interactiveType).length,
  lessonsWithDirectSpec: rows.filter(r => r.directSpec).length,
  lessonsWithResolvedSpec: rows.filter(r => r.spec).length,
  specs: specs.size,
  specQaStatusCounts: countBy([...specs.values()].map(s => s.qaStatus)),
  reports: reportFiles.size,
};

const activeSimulationIdGroups = new Map();
for (const row of rows.filter(rowIsActive)) {
  if (!row.simulationId) continue;
  if (!activeSimulationIdGroups.has(row.simulationId)) activeSimulationIdGroups.set(row.simulationId, []);
  activeSimulationIdGroups.get(row.simulationId).push(row);
}

const problems = {
  wrongQuestionCount: rows.filter(r => rowIsActive(r) && r.questionCount !== 10).map(r => ({ id: r.id, file: r.file, count: r.questionCount })),
  nonReviewedActiveQuestions: rows.filter(r => rowIsActive(r) && r.questionDrafts > 0).map(r => ({ id: r.id, file: r.file, count: r.questionDrafts })),
  draftLessons: rows.filter(r => r.reviewStatus === "draft").map(r => ({ id: r.id, file: r.file })),
  missingReviewStatus: rows.filter(r => r.reviewStatus === "missing").map(r => ({ id: r.id, file: r.file })),
  activeWithoutSimulation: rows.filter(r => rowIsActive(r) && !r.simulationEngine).map(r => ({ id: r.id, file: r.file })),
  duplicateActiveSimulationIds: [...activeSimulationIdGroups.entries()]
    .filter(([, group]) => group.length > 1)
    .map(([simulationId, group]) => ({ simulationId, lessons: group.map(r => r.id), files: group.map(r => r.file) })),
  activeWithGenericSimulation: rows.filter(r => rowIsActive(r) && r.simulationEngine === "concept-explorer").map(r => ({ id: r.id, file: r.file, model: r.simulationModel })),
  activeWithUnsupportedProductionSimulation: rows.filter(r => rowIsActive(r) && r.simulationEngine && !productionMathEngines.has(r.simulationEngine)).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeWithoutProductionRenderer: rows.filter(r => rowIsActive(r) && r.simulationEngine && r.simulationEngine !== "concept-explorer" && !r.productionRenderer).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeSimulationMissingModelGoalOrMission: rows.filter(r => rowIsActive(r) && r.simulationEngine && (!r.simulationModel || !r.simulationGoal || !r.simulationMission)).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeWithoutFirstPassReport: rows.filter(r => rowIsActive(r) && r.reports.length === 0).map(r => ({ id: r.id, file: r.file })),
  activeWithoutDirectSpec: rows.filter(r => rowIsActive(r) && !r.directSpec).map(r => ({ id: r.id, file: r.file, resolvedSpecId: r.resolvedSpecId, resolution: r.specResolution })),
  activeWithoutResolvedSpec: rows.filter(r => rowIsActive(r) && !r.spec).map(r => ({ id: r.id, file: r.file })),
  deprecatedWithDraftQuestions: rows.filter(r => !rowIsActive(r) && r.questionDrafts > 0).map(r => ({ id: r.id, file: r.file, count: r.questionDrafts })),
  implementedButUntestedSpecs: [...specs.entries()].filter(([, s]) => s.implementationStatus === "implemented" && s.qaStatus === "untested").map(([id, s]) => ({ id, component: s.component, file: s.file })),
  implementedButUnverifiedSpecs: [...specs.entries()].filter(([, s]) => s.implementationStatus === "implemented" && s.qaStatus !== "verified").map(([id, s]) => ({ id, component: s.component, file: s.file, qaStatus: s.qaStatus || "missing" })),
};

const output = { summary, problems };
if (process.env.MATH_AUDIT_VERBOSE === "1") output.rows = rows;
console.log(JSON.stringify(output, null, 2));

const informational = new Set(["draftLessons", "deprecatedWithDraftQuestions", "implementedButUntestedSpecs"]);
let failed = false;
for (const [name, value] of Object.entries(problems)) {
  if (informational.has(name) || !value.length) continue;
  failed = true;
  console.error(`AUDIT_FAIL ${name}: ${value.length}`);
  for (const issue of value) {
    const item = typeof issue === "string" ? { id: issue } : issue;
    const file = item.file ? `implementation/unit-specs/math/${item.file}` : "scripts/audit_math_coverage.mjs";
    const detail = item.engine ? ` engine=${item.engine}` : item.model ? ` model=${item.model}` : item.qaStatus ? ` qaStatus=${item.qaStatus}` : item.simulationId ? ` simulationId=${item.simulationId} lessons=${(item.lessons || []).join(",")}` : "";
    console.error(`::error file=${file}::${name}: ${item.id || item.simulationId || "unknown"}${detail}`);
  }
}
if (summary.lessonCount !== 129 || summary.questionCount !== 1290 || summary.specs !== 129) {
  failed = true;
  console.error(`AUDIT_FAIL expected 129 lessons / 1290 questions / 129 specs, got ${summary.lessonCount} / ${summary.questionCount} / ${summary.specs}`);
}
if (failed) process.exitCode = 1;

import { readdir, readFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const readText = rel => readFile(new URL(rel, ROOT), "utf8");
const readJson = async rel => JSON.parse(await readText(rel));
const list = async rel => (await readdir(new URL(rel, ROOT))).sort();

const lessonFiles = (await list("lessons/math/" )).filter(name => name.endsWith(".json"));
const questionFiles = (await list("questions/math/" )).filter(name => name.endsWith(".json"));
const specFiles = (await list("implementation/unit-specs/math/" )).filter(name => name.endsWith(".yaml"));
const reportFiles = new Set((await list("implementation/reports/" )).filter(name => /^math-.*first-pass-review\.json$/.test(name)));
const productionRendererSource = await readText("site/simulations.js");
const productionMathEngines = new Set([
  "math-number-line",
  "math-inequality-range",
  "math-algebra-balance",
  "math-ticket-equation",
  "math-expression-lab",
  "math-function-graph",
  "math-system-graph",
  "math-geometry",
  "math-data-lab",
  "math-probability-lab",
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
  const designStatus = text.match(/^\s*designStatus:\s*([^\n#]+)/m)?.[1]?.trim();
  const implementationStatus = text.match(/^\s*implementationStatus:\s*([^\n#]+)/m)?.[1]?.trim();
  const qaStatus = text.match(/^\s*qaStatus:\s*([^\n#]+)/m)?.[1]?.trim();
  if (lessonId) specs.set(lessonId, { file, component, designStatus, implementationStatus, qaStatus });
}

function reportCandidates(lessonFile) {
  const stem = lessonFile.replace(/^lesson-math-/, "").replace(/\.json$/, "");
  const candidates = [`math-${stem}-first-pass-review.json`];
  if (stem.startsWith("content-")) candidates.push(`math-${stem.slice("content-".length)}-first-pass-review.json`);
  return candidates;
}

function hasProductionRenderer(engine) {
  if (!engine || !productionMathEngines.has(engine)) return false;
  return productionRendererSource.includes(`if (engine === "${engine}")`);
}

const rows = lessons.map(lesson => {
  const qs = questionsByLesson.get(lesson.id) || [];
  const specId = lesson.id.replace(/^lesson-math-/, "cur-math-");
  const directSpec = specs.get(specId);
  const reports = reportCandidates(lesson.file).filter(name => reportFiles.has(name));
  const simulationEngine = lesson.simulation?.engine || null;
  return {
    id: lesson.id,
    file: lesson.file,
    reviewStatus: lesson.reviewStatus || "missing",
    questionCount: qs.length,
    questionDrafts: qs.filter(q => q.reviewStatus !== "content-reviewed").length,
    simulationEngine,
    simulationModel: lesson.simulation?.model || null,
    simulationGoal: Boolean(lesson.simulation?.goal),
    simulationMission: Boolean(lesson.simulation?.mission),
    productionRenderer: hasProductionRenderer(simulationEngine),
    interactiveType: lesson.interactive?.type || null,
    spec: directSpec || null,
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
  lessonsWithInteractive: rows.filter(r => r.interactiveType).length,
  lessonsWithDirectSpec: rows.filter(r => r.spec).length,
  specs: specs.size,
  reports: reportFiles.size,
};

const problems = {
  wrongQuestionCount: rows.filter(r => rowIsActive(r) && r.questionCount !== 10).map(r => ({ id: r.id, file: r.file, count: r.questionCount })),
  nonReviewedActiveQuestions: rows.filter(r => rowIsActive(r) && r.questionDrafts > 0).map(r => ({ id: r.id, file: r.file, count: r.questionDrafts })),
  draftLessons: rows.filter(r => r.reviewStatus === "draft").map(r => ({ id: r.id, file: r.file })),
  missingReviewStatus: rows.filter(r => r.reviewStatus === "missing").map(r => ({ id: r.id, file: r.file })),
  activeWithoutSimulation: rows.filter(r => rowIsActive(r) && !r.simulationEngine).map(r => ({ id: r.id, file: r.file })),
  activeWithGenericSimulation: rows.filter(r => rowIsActive(r) && r.simulationEngine === "concept-explorer").map(r => ({ id: r.id, file: r.file, model: r.simulationModel })),
  activeWithUnsupportedProductionSimulation: rows.filter(r => rowIsActive(r) && r.simulationEngine && !productionMathEngines.has(r.simulationEngine)).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeWithoutProductionRenderer: rows.filter(r => rowIsActive(r) && r.simulationEngine && r.simulationEngine !== "concept-explorer" && !r.productionRenderer).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeSimulationMissingModelGoalOrMission: rows.filter(r => rowIsActive(r) && r.simulationEngine && (!r.simulationModel || !r.simulationGoal || !r.simulationMission)).map(r => ({ id: r.id, file: r.file, engine: r.simulationEngine })),
  activeWithoutFirstPassReport: rows.filter(r => rowIsActive(r) && r.reports.length === 0).map(r => ({ id: r.id, file: r.file })),
  activeWithoutDirectSpec: rows.filter(r => rowIsActive(r) && !r.spec).map(r => ({ id: r.id, file: r.file })),
  deprecatedWithDraftQuestions: rows.filter(r => !rowIsActive(r) && r.questionDrafts > 0).map(r => ({ id: r.id, file: r.file, count: r.questionDrafts })),
  implementedButUntestedSpecs: [...specs.entries()].filter(([, s]) => s.implementationStatus === "implemented" && s.qaStatus === "untested").map(([id, s]) => ({ id, component: s.component, file: s.file })),
};

const output = { summary, problems };
if (process.env.MATH_AUDIT_VERBOSE === "1") output.rows = rows;
console.log(JSON.stringify(output, null, 2));

const informational = new Set(["draftLessons", "implementedButUntestedSpecs", "deprecatedWithDraftQuestions", "activeWithoutDirectSpec"]);
let failed = false;
for (const [name, value] of Object.entries(problems)) {
  if (informational.has(name) || !value.length) continue;
  failed = true;
  console.error(`AUDIT_FAIL ${name}: ${value.length}`);
  for (const issue of value) {
    const item = typeof issue === "string" ? { id: issue } : issue;
    const file = item.file ? `lessons/math/${item.file}` : "scripts/audit_math_coverage.mjs";
    const detail = item.engine ? ` engine=${item.engine}` : item.model ? ` model=${item.model}` : "";
    console.error(`::error file=${file}::${name}: ${item.id || "unknown"}${detail}`);
  }
}
if (summary.lessonCount !== 129 || summary.questionCount !== 1290) {
  failed = true;
  console.error(`AUDIT_FAIL expected 129 lessons / 1290 questions, got ${summary.lessonCount} / ${summary.questionCount}`);
}
if (failed) process.exitCode = 1;

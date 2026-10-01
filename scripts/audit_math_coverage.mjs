import { readdir, readFile } from "node:fs/promises";
import path from "node:path";

const ROOT = new URL("../", import.meta.url);
const readText = rel => readFile(new URL(rel, ROOT), "utf8");
const readJson = async rel => JSON.parse(await readText(rel));
const list = async rel => (await readdir(new URL(rel, ROOT))).sort();

const lessonFiles = (await list("lessons/math/" )).filter(name => name.endsWith(".json"));
const questionFiles = (await list("questions/math/" )).filter(name => name.endsWith(".json"));
const specFiles = (await list("implementation/unit-specs/math/" )).filter(name => name.endsWith(".yaml"));
const reportFiles = new Set((await list("implementation/reports/" )).filter(name => /^math-.*first-pass-review\.json$/.test(name)));

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

const rows = lessons.map(lesson => {
  const qs = questionsByLesson.get(lesson.id) || [];
  const specId = lesson.id.replace(/^lesson-math-/, "cur-math-content-");
  const directSpec = specs.get(specId);
  const reports = reportCandidates(lesson.file).filter(name => reportFiles.has(name));
  return {
    id: lesson.id,
    file: lesson.file,
    reviewStatus: lesson.reviewStatus || "missing",
    questionCount: qs.length,
    questionDrafts: qs.filter(q => q.reviewStatus !== "content-reviewed").length,
    simulationEngine: lesson.simulation?.engine || null,
    simulationModel: lesson.simulation?.model || null,
    simulationGoal: Boolean(lesson.simulation?.goal),
    interactiveType: lesson.interactive?.type || null,
    spec: directSpec || null,
    reports,
  };
});

const summary = {
  lessonCount: lessons.length,
  questionCount: questions.length,
  exactTenQuestions: rows.filter(r => r.questionCount === 10).length,
  lessonStatusCounts: rows.reduce((acc, row) => (acc[row.reviewStatus] = (acc[row.reviewStatus] || 0) + 1, acc), {}),
  lessonsWithSimulation: rows.filter(r => r.simulationEngine).length,
  lessonsWithoutSimulation: rows.filter(r => !r.simulationEngine && rowIsActive(r)).length,
  lessonsWithInteractive: rows.filter(r => r.interactiveType).length,
  specs: specs.size,
  reports: reportFiles.size,
};
function rowIsActive(row) { return row.reviewStatus !== "deprecated"; }

const problems = {
  wrongQuestionCount: rows.filter(r => rowIsActive(r) && r.questionCount !== 10).map(r => ({ id: r.id, count: r.questionCount })),
  nonReviewedQuestions: rows.filter(r => r.questionDrafts > 0).map(r => ({ id: r.id, count: r.questionDrafts })),
  draftLessons: rows.filter(r => r.reviewStatus === "draft").map(r => r.id),
  missingReviewStatus: rows.filter(r => r.reviewStatus === "missing").map(r => r.id),
  activeWithoutSimulation: rows.filter(r => rowIsActive(r) && !r.simulationEngine).map(r => r.id),
  activeWithoutFirstPassReport: rows.filter(r => rowIsActive(r) && r.reports.length === 0).map(r => r.id),
  implementedButUntestedSpecs: [...specs.entries()].filter(([, s]) => s.implementationStatus === "implemented" && s.qaStatus === "untested").map(([id, s]) => ({ id, component: s.component, file: s.file })),
};

console.log(JSON.stringify({ summary, problems, rows }, null, 2));

let failed = false;
for (const [name, value] of Object.entries(problems)) {
  if (["draftLessons", "activeWithoutSimulation", "implementedButUntestedSpecs"].includes(name)) continue;
  if (value.length) {
    failed = true;
    console.error(`AUDIT_FAIL ${name}: ${value.length}`);
  }
}
if (summary.lessonCount !== 129 || summary.questionCount !== 1290) {
  failed = true;
  console.error(`AUDIT_FAIL expected 129 lessons / 1290 questions, got ${summary.lessonCount} / ${summary.questionCount}`);
}
if (failed) process.exitCode = 1;

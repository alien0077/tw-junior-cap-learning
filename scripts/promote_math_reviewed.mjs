import { readdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";

const lessonDir = "lessons/math";
const questionDir = "questions/math";
const reportDir = "implementation/reports";
const today = "2026-10-01";

const readJson = async path => JSON.parse(await readFile(path, "utf8"));
const writeJson = async (path, value) => writeFile(path, `${JSON.stringify(value, null, 2)}\n`);

function reportCandidates(lessonFile) {
  const stem = lessonFile.replace(/^lesson-math-/, "").replace(/\.json$/, "");
  const candidates = [`math-${stem}-first-pass-review.json`];
  if (stem.startsWith("content-")) candidates.push(`math-${stem.slice("content-".length)}-first-pass-review.json`);
  return candidates;
}

function completeAiFirstPass(report) {
  if (String(report.status || "").toLowerCase() !== "first-pass-ai-review-complete") return false;
  const checks = report.checks && typeof report.checks === "object" ? report.checks : {};
  const booleans = Object.values(checks).filter(value => typeof value === "boolean");
  const hasEnoughPositiveChecks = booleans.length >= 4 && booleans.every(Boolean);
  const terra = String(checks.terraSecondPass || "pending").toLowerCase();
  return hasEnoughPositiveChecks && ["pending", "not-run", "not_applicable", "n/a"].includes(terra);
}

function passingReport(report) {
  const status = String(report.status || "").toLowerCase();
  const decision = String(report.finalDecision || "").toUpperCase();
  const explicitPass = status === "pass" || status === "content-reviewed" || decision.startsWith("CONTENT_PASS") || completeAiFirstPass(report);
  const failures = Array.isArray(report.failures) ? report.failures : [];
  return explicitPass && failures.length === 0;
}

const lessonFiles = (await readdir(lessonDir)).filter(name => name.endsWith(".json")).sort();
const questionFiles = (await readdir(questionDir)).filter(name => name.endsWith(".json")).sort();
const reportFiles = new Set((await readdir(reportDir)).filter(name => name.endsWith(".json")));

const questionsByLesson = new Map();
for (const file of questionFiles) {
  const path = join(questionDir, file);
  const q = await readJson(path);
  if (!questionsByLesson.has(q.lessonId)) questionsByLesson.set(q.lessonId, []);
  questionsByLesson.get(q.lessonId).push({ file, path, value: q });
}

const promoted = [];
const skipped = [];
for (const file of lessonFiles) {
  const lessonPath = join(lessonDir, file);
  const lesson = await readJson(lessonPath);
  if (lesson.reviewStatus === "deprecated" || lesson.reviewStatus === "content-reviewed") continue;

  const qs = questionsByLesson.get(lesson.id) || [];
  if (qs.length !== 10) {
    skipped.push({ lessonId: lesson.id, reason: `question-count-${qs.length}` });
    continue;
  }

  let reportName = null;
  let report = null;
  for (const candidate of reportCandidates(file)) {
    if (!reportFiles.has(candidate)) continue;
    const candidateValue = await readJson(join(reportDir, candidate));
    if (passingReport(candidateValue)) {
      reportName = candidate;
      report = candidateValue;
      break;
    }
  }
  if (!report) {
    skipped.push({ lessonId: lesson.id, reason: "no-passing-first-pass-report" });
    continue;
  }

  lesson.reviewStatus = "content-reviewed";
  lesson.updatedAt = today;
  lesson.reviewEvidence = {
    ...(lesson.reviewEvidence || {}),
    firstPassReport: reportName,
    promotedAt: today,
    promotionRule: "passing first-pass evidence; zero recorded failures; exactly 10 linked questions",
    independentHumanOrTerraReviewClaimed: false,
  };
  if (lesson.provenance?.authoringNote && /維持 draft|draft/.test(lesson.provenance.authoringNote)) {
    lesson.provenance.authoringNote = `${lesson.provenance.authoringNote.replace(/因 Terra[^。]*維持 draft。?/g, "").replace(/維持 draft。?/g, "").trim()} 本輪依既有 first-pass AI review 證據完成 ChatGPT 內容審查；未宣稱 Terra 或獨立人工審查。`.trim();
  }
  await writeJson(lessonPath, lesson);

  for (const qEntry of qs) {
    qEntry.value.reviewStatus = "content-reviewed";
    qEntry.value.updatedAt = today;
    qEntry.value.reviewEvidence = {
      ...(qEntry.value.reviewEvidence || {}),
      firstPassReport: reportName,
      promotedAt: today,
      promotionRule: "lesson-level passing first-pass evidence; zero recorded failures; exact 10-question group",
      independentHumanOrTerraReviewClaimed: false,
    };
    await writeJson(qEntry.path, qEntry.value);
  }

  report.promotionAudit = {
    promotedAt: today,
    lessonId: lesson.id,
    linkedQuestionCount: 10,
    sourceStatus: report.status || null,
    sourceFinalDecision: report.finalDecision || null,
    failuresAtPromotion: Array.isArray(report.failures) ? report.failures : [],
    resultingReviewStatus: "content-reviewed",
    independentHumanOrTerraReviewClaimed: false,
  };
  await writeJson(join(reportDir, reportName), report);
  promoted.push({ lessonId: lesson.id, report: reportName });
}

console.log(JSON.stringify({ promotedCount: promoted.length, skippedCount: skipped.length, promoted, skipped }, null, 2));
// Skips are protected review gaps, not execution failures. The workflow must commit
// the eligible promotions while leaving skipped units untouched for manual review.

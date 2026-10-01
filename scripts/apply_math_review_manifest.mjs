import { readFile, writeFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const manifestPath = process.argv[2] || "implementation/reports/math-review-repairs-2026-10-01.json";
const manifest = JSON.parse(await readFile(new URL(manifestPath, ROOT), "utf8"));

for (const unit of manifest.units || []) {
  const questionIds = unit.questionIds || [];
  for (const id of questionIds) {
    const rel = `questions/math/${id}.json`;
    const url = new URL(rel, ROOT);
    const q = JSON.parse(await readFile(url, "utf8"));
    if (q.lessonId !== unit.lessonId) throw new Error(`${id}: expected lessonId ${unit.lessonId}, got ${q.lessonId}`);
    if (unit.questionReviewStatus) q.reviewStatus = unit.questionReviewStatus;
    q.updatedAt = manifest.reviewedAt;
    const override = unit.questionOverrides?.[id];
    if (override) Object.assign(q, override);
    await writeFile(url, JSON.stringify(q, null, 2) + "\n");
  }

  if (unit.lessonPath) {
    const url = new URL(unit.lessonPath, ROOT);
    const lesson = JSON.parse(await readFile(url, "utf8"));
    if (lesson.id !== unit.lessonId) throw new Error(`${unit.lessonPath}: lesson id mismatch`);
    if (unit.lessonStatus) lesson.reviewStatus = unit.lessonStatus;
    lesson.updatedAt = manifest.reviewedAt;
    await writeFile(url, JSON.stringify(lesson, null, 2) + "\n");
  }

  if (unit.reportPath) {
    const url = new URL(unit.reportPath, ROOT);
    const report = JSON.parse(await readFile(url, "utf8"));
    report.secondPassReview = {
      reviewedAt: manifest.reviewedAt,
      decision: unit.decision,
      questionReviewStatus: unit.questionReviewStatus || null,
      lessonStatus: unit.lessonStatus || null,
      findings: unit.findings || [],
      repairs: unit.repairs || [],
      blockers: unit.blockers || []
    };
    await writeFile(url, JSON.stringify(report, null, 2) + "\n");
  }
}

import { readdir, readFile, writeFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const reportPath = new URL("implementation/reports/math-browser-qa-current.json", ROOT);
const specDir = new URL("implementation/unit-specs/math/", ROOT);
const manifestPath = new URL("implementation/reports/math-spec-qa-current.json", ROOT);

const browserReport = JSON.parse(await readFile(reportPath, "utf8"));
if (browserReport.status !== "PASS") throw new Error(`browser QA report is not PASS: ${browserReport.status}`);
if (browserReport.scope?.activeLessonsExpected !== 128 || browserReport.scope?.activeLessonsPassed !== 128) {
  throw new Error(`browser QA did not pass all 128 active math lessons: ${browserReport.scope?.activeLessonsPassed}`);
}
if (browserReport.failures?.length) throw new Error(`browser QA report contains failures: ${browserReport.failures.length}`);

const files = (await readdir(specDir)).filter(name => name.endsWith(".yaml")).sort();
if (files.length !== 129) throw new Error(`expected 129 math unit specs, got ${files.length}`);

const changed = [];
for (const file of files) {
  const url = new URL(file, specDir);
  const original = await readFile(url, "utf8");
  if (!/^\s*implementationStatus:\s*implemented\s*$/m.test(original)) {
    throw new Error(`${file}: implementationStatus is not implemented`);
  }
  const match = original.match(/^([ \t]*qaStatus:\s*)([^\n#]+)(.*)$/m);
  if (!match) throw new Error(`${file}: missing qaStatus`);
  const current = match[2].trim().replace(/^['"]|['"]$/g, "");
  if (!new Set(["untested", "verified"]).has(current)) {
    throw new Error(`${file}: unexpected qaStatus ${current}`);
  }
  if (current === "untested") {
    const updated = original.replace(/^([ \t]*qaStatus:\s*)([^\n#]+)(.*)$/m, "$1verified$3");
    await writeFile(url, updated, "utf8");
    changed.push(file);
  }
}

const manifest = {
  schemaVersion: 1,
  generatedAt: browserReport.generatedAt,
  sourceCommit: browserReport.sourceCommit,
  browserReport: "implementation/reports/math-browser-qa-current.json",
  qaStatus: "verified",
  unitSpecCount: files.length,
  changedFromUntested: changed.length,
  evidenceScope: browserReport.scope,
};
await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
console.log(JSON.stringify(manifest, null, 2));

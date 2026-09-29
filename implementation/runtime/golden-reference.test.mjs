import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const bundle = JSON.parse(await readFile(new URL("../unit-specs.bundle.json", import.meta.url), "utf8"));
const spec = bundle.units.find((unit) => unit.lessonId === "cur-math-content-a-8-1");
assert.ok(spec, "Golden Reference unit must be present in the bundle");

const formulas = [
  "(a＋b)²＝a²＋2ab＋b²",
  "(a−b)²＝a²−2ab＋b²",
  "(a＋b)(a−b)＝a²−b²",
];
for (const formula of formulas) assert.ok(spec.coreConcepts.includes(formula), formula);

const a = 3;
const b = 2;
assert.equal((a + b) ** 2, a ** 2 + 2 * a * b + b ** 2);
assert.equal((a - b) ** 2, a ** 2 - 2 * a * b + b ** 2);
assert.equal((a + b) * (a - b), a ** 2 - b ** 2);

console.log("golden reference formula runtime: 3/3 identities verified");

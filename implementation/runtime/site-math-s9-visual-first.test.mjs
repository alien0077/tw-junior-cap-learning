import assert from "node:assert/strict";
import fs from "node:fs";
const js=fs.readFileSync(new URL("../../site/math-visual-labs.js",import.meta.url),"utf8");
const css=fs.readFileSync(new URL("../../site/math-visual-labs.css",import.meta.url),"utf8");
for(let n=2;n<=8;n++){
 const lesson=JSON.parse(fs.readFileSync(new URL(`../../lessons/math/lesson-math-content-s-9-${n}.json`,import.meta.url),"utf8"));
 assert.equal(lesson.simulation.engine,"math-geometry");
 assert.ok(js.includes(lesson.simulation.model),`production visual renderer missing ${lesson.simulation.model}`);
}
for(const token of ["<svg","<figure","mvl-s9","圖像先行"]) assert.ok(js.includes(token),`missing visual-first token ${token}`);
assert.ok(css.includes("overflow-x:hidden"),"mobile horizontal overflow containment missing");
console.log("PASS production S-9-2..S-9-8 visual-first coverage");

import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import {fileURLToPath} from "node:url";
const here=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(here,"../..");
const subjects=["math","science","social","english","chinese"],counts={};
for(const subject of subjects){
 const dir=path.join(root,"lessons",subject);
 const files=fs.readdirSync(dir).filter(x=>x.endsWith(".json"));
 counts[subject]=files.length;
 for(const file of files){
  const lesson=JSON.parse(fs.readFileSync(path.join(dir,file),"utf8"));
  assert.ok(lesson.title,subject+"/"+file+" missing title");
  const isLeaf=String(lesson.id||"").toLowerCase().includes("-iv-");
  if(!isLeaf) continue;
  assert.ok(lesson.interactive,subject+"/"+file+" missing interactive contract");
  assert.ok(lesson.interactive.goal||lesson.interactive.scenario||lesson.interactive.steps,subject+"/"+file+" interactive has no teaching intent");
  const authored=(lesson.teaching?.body||lesson.content?.sections||[]).filter(x=>x?.body);
  assert.ok(authored.length,subject+"/"+file+" has no authored teaching body");
 }
}
const app=fs.readFileSync(path.join(root,"site/app.js"),"utf8"),css=fs.readFileSync(path.join(root,"site/styles.css"),"utf8");
for(const subject of subjects) assert.ok(app.includes(subject+':"')||app.includes(subject+': "'),"visual overview subject route missing: "+subject);
assert.ok(app.includes("lessonVisualOverview(item)"),"per-lesson visual overview is not mounted");\nassert.ok(app.includes("renderLessonSection(item, section, index)"),"every authored prose section must mount a visual companion");\nassert.ok(app.includes("sectionVisual(item, section, index)"),"section visual renderer missing");\nassert.ok(css.includes(".lesson-section-pair"),"prose/visual paired layout missing");\nassert.ok(css.includes(".section-visual-flow"),"section visual flow CSS missing");
assert.ok(css.includes(".lvo-flow"),"visual flow CSS missing");
assert.ok(css.includes("overflow-x:hidden"),"mobile horizontal overflow guard missing");
console.log("PASS all-subject visual-first contract",counts);

import assert from "node:assert/strict";
import { JSDOM } from "jsdom";
import { enhanceMathInteractiveBlock } from "./math-interactive-renderers.js";

const dom=new JSDOM("<main><section class='interactive-block'><div class='component-visual-body'></div></section></main>",{url:"https://example.test/"});
const root=dom.window.document.querySelector(".interactive-block");
const block={id:"S9-3-VISUAL",component:"GeometryManipulationBlock",purpose:"parallel ratio",studentActions:["pair","check"]};
const spec={subject:"math",lessonId:"cur-math-content-s-9-3",title:"S-9-3：平行線截比例線段"};
const lab=enhanceMathInteractiveBlock({document:dom.window.document,root,block,spec});
assert.ok(lab);
assert.ok(lab.querySelector("svg.math-live-canvas"),"must render the geometry before prose");
assert.match(lab.textContent,/AD \/ DB = AE \/ EC/);
assert.match(lab.textContent,/6 \/ 4 = 7\.5 \/ EC/);
const buttons=[...lab.querySelectorAll("button")];
buttons.find(b=>b.textContent==="看整段倍率").click();
assert.match(lab.textContent,/AD \/ AB = AE \/ AC/);
buttons.find(b=>b.textContent==="4 \/ 3 = 8 \/ AC").click();
assert.match(lab.textContent,/分段／分段.*分段／整段/);
console.log("PASS S-9-3 visual-first parallel proportion teaching");

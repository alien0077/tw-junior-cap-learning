import assert from "node:assert/strict";
import {JSDOM} from "jsdom";
import {enhanceMathInteractiveBlock} from "./math-interactive-renderers.js";
const ids=["s-9-1","s-9-2","s-9-3","s-9-4","s-9-5","s-9-6","s-9-7","s-9-8"];
for(const id of ids){
 const dom=new JSDOM("<div class='interactive-block'><div class='component-visual-body'></div></div>",{url:"https://example.test/"});
 const root=dom.window.document.querySelector(".interactive-block");
 const block={id:"VIS-"+id,component:"GeometryManipulationBlock",studentActions:["observe"]};
 const lab=enhanceMathInteractiveBlock({document:dom.window.document,root,block,spec:{subject:"math",lessonId:"cur-math-content-"+id,title:id}});
 assert.ok(lab,id+" must mount");
 assert.ok(lab.querySelector("svg"),id+" must teach with an actual diagram");
 assert.ok(lab.textContent.trim().length>20,id+" must include concise visual guidance");
}
console.log("PASS S-9-1..S-9-8 visual-first geometry coverage");

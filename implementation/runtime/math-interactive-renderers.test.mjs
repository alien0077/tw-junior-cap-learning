import assert from "node:assert/strict";
import { JSDOM } from "jsdom";
import { enhanceMathInteractiveBlock, MATH_LIVE_COMPONENTS } from "./math-interactive-renderers.js";

function fixture(component, extra = {}) {
  const dom = new JSDOM("<main><section class='interactive-block'><div class='component-visual-body'></div></section></main>", { url: "https://example.test/" });
  const root = dom.window.document.querySelector(".interactive-block");
  const block = {
    id: `TEST-${component}`,
    component,
    purpose: "math live renderer test",
    initialState: { mode: "predict", variableValues: {} },
    studentActions: ["先操作", "再觀察"],
    ...extra,
  };
  const spec = {
    subject: "math",
    title: extra.title || "數學互動測試",
    coreConcepts: extra.coreConcepts || ["操作後同步檢查量與表徵"],
  };
  return { dom, root, block, spec };
}

assert.deepEqual(new Set(MATH_LIVE_COMPONENTS), new Set([
  "FunctionRepresentationBlock", "GeometryManipulationBlock", "AlgebraBalanceBlock",
  "AlgebraEquationMeaningBlock", "EquivalentExpressionCheckBlock", "NumberLineBlock",
  "StepwiseReasoningBlock",
]));

{
  const { dom, root, block, spec } = fixture("FunctionRepresentationBlock", { title: "F-8-2：一次函數的圖形" });
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  assert.ok(lab);
  assert.equal(lab.dataset.liveMath, "true");
  assert.ok(lab.querySelector("svg.math-live-canvas"));
  assert.equal(lab.querySelectorAll('input[type="range"]').length, 3);
  const ranges = lab.querySelectorAll('input[type="range"]');
  ranges[0].value = "3";
  ranges[0].dispatchEvent(new dom.window.Event("input", { bubbles: true }));
  assert.match(lab.querySelector(".math-live-status").textContent, /y = 3x/);
  assert.equal(lab.querySelectorAll("tbody tr").length, 5);
}

{
  const { dom, root, block, spec } = fixture("GeometryManipulationBlock", { title: "圓與圓周長" });
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  assert.ok(lab.querySelector("circle"));
  const range = lab.querySelector('input[type="range"]');
  range.value = "5";
  range.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
  assert.match(lab.querySelector(".math-live-status").textContent, /半徑 r=5/);
  assert.match(lab.querySelector(".math-live-status").textContent, /面積/);
}

for (const component of ["AlgebraBalanceBlock", "AlgebraEquationMeaningBlock"]) {
  const { dom, root, block, spec } = fixture(component, { title: "一元一次方程式" });
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  const range = lab.querySelector('input[type="range"]');
  range.value = "4";
  range.dispatchEvent(new dom.window.Event("input", { bubbles: true }));
  assert.equal(lab.querySelector(".math-balance-visual").dataset.balanced, "true");
  assert.match(lab.querySelector(".math-live-status").textContent, /左右同為 13/);
}

{
  const { dom, root, block, spec } = fixture("EquivalentExpressionCheckBlock");
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  assert.equal(lab.querySelectorAll("tbody tr").length, 3);
  assert.match(lab.textContent, /2\(x\+3\)/);
  assert.match(lab.querySelector(".math-live-status").textContent, /完整等值理由/);
}

{
  const { dom, root, block, spec } = fixture("NumberLineBlock", { title: "數線與距離" });
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  assert.ok(lab.querySelector("svg"));
  assert.equal(lab.querySelectorAll('input[type="range"]').length, 2);
  assert.match(lab.querySelector(".math-live-status").textContent, /距離/);
}

{
  const { dom, root, block, spec } = fixture("StepwiseReasoningBlock", {
    guidedActivity: {
      stages: [
        { prompt: "第一步找共同因數" },
        { prompt: "第二步辨認平方差" },
        { prompt: "第三步展開驗算" },
      ],
    },
  });
  const lab = enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec });
  assert.equal(lab.querySelectorAll(".math-step-map li").length, 3);
  assert.match(lab.querySelector(".math-live-status").textContent, /3 個可檢核步驟/);
}

{
  const { dom, root, block } = fixture("FunctionRepresentationBlock");
  const nonMathSpec = { subject: "science", title: "not math" };
  assert.equal(enhanceMathInteractiveBlock({ document: dom.window.document, root, block, spec: nonMathSpec }), null);
}

console.log("math live interactive renderers: ok");

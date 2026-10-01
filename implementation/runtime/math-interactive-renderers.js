const SVG_NS = "http://www.w3.org/2000/svg";
const STORAGE_PREFIX = "tw-junior-cap-learning:math-lab:";

const SUPPORTED = new Set([
  "FunctionRepresentationBlock",
  "GeometryManipulationBlock",
  "AlgebraBalanceBlock",
  "AlgebraEquationMeaningBlock",
  "EquivalentExpressionCheckBlock",
  "NumberLineBlock",
  "StepwiseReasoningBlock",
]);

function svg(document, name, attrs = {}) {
  const node = document.createElementNS(SVG_NS, name);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, String(value));
  return node;
}

function number(value, fallback) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function clamp(value, min, max) { return Math.min(max, Math.max(min, value)); }

function storageFor(blockId) {
  try {
    if (!globalThis.localStorage) return null;
    const key = `${STORAGE_PREFIX}${blockId}`;
    return {
      get() {
        try { return JSON.parse(globalThis.localStorage.getItem(key) || "null"); } catch { return null; }
      },
      set(value) {
        try { globalThis.localStorage.setItem(key, JSON.stringify(value)); } catch { /* optional persistence */ }
      },
    };
  } catch { return null; }
}

function makeRange(document, { label, min, max, step = 1, value, onInput }) {
  const wrapper = document.createElement("label");
  wrapper.className = "math-live-control";
  const text = document.createElement("span");
  const output = document.createElement("output");
  const input = document.createElement("input");
  input.type = "range";
  input.min = String(min);
  input.max = String(max);
  input.step = String(step);
  input.value = String(value);
  input.setAttribute("aria-label", label);
  const sync = () => {
    output.value = input.value;
    output.textContent = input.value;
    onInput?.(Number(input.value));
  };
  text.textContent = `${label}：`;
  input.addEventListener("input", sync);
  wrapper.append(text, input, output);
  sync();
  return { wrapper, input, output };
}

function makeLab(document, block, title) {
  const lab = document.createElement("section");
  lab.className = "math-live-lab";
  lab.dataset.component = block.component;
  lab.dataset.liveMath = "true";
  lab.setAttribute("aria-labelledby", `${block.id}-math-live-title`);
  const heading = document.createElement("h4");
  heading.id = `${block.id}-math-live-title`;
  heading.textContent = title;
  const status = document.createElement("p");
  status.className = "math-live-status";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  lab.append(heading, status);
  return { lab, status };
}

function makeCanvas(document, label, width = 360, height = 240) {
  const canvas = svg(document, "svg", { viewBox: `0 0 ${width} ${height}`, role: "img", "aria-label": label, tabindex: "0" });
  canvas.classList.add("math-live-canvas");
  return canvas;
}

function mountFunctionLab({ document, root, block, spec }) {
  const saved = storageFor(block.id);
  const prior = saved?.get() || {};
  const vars = block.initialState?.variableValues || {};
  const initialA = number(prior.a ?? vars.a ?? vars.primary, 1);
  const initialB = number(prior.b ?? vars.b ?? vars.secondary, 0);
  const initialX = number(prior.x, 2);
  const state = { a: initialA, b: initialB, x: initialX };
  const { lab, status } = makeLab(document, block, "一次函數動態圖形實驗室");
  const controls = document.createElement("div");
  controls.className = "math-live-controls";
  const graph = makeCanvas(document, `${spec.title} 的動態座標圖`);
  const table = document.createElement("table");
  table.className = "math-live-table";
  table.innerHTML = "<caption>同步數值表</caption><thead><tr><th>x</th><th>y=ax+b</th></tr></thead><tbody></tbody>";
  const tbody = table.querySelector("tbody");

  const update = () => {
    graph.replaceChildren();
    const W = 360, H = 240, ox = W / 2, oy = H / 2, scale = 20;
    for (let n = -8; n <= 8; n++) {
      graph.append(svg(document, "line", { x1: ox + n * scale, y1: 10, x2: ox + n * scale, y2: H - 10, stroke: "currentColor", opacity: n === 0 ? 0.8 : 0.12 }));
    }
    for (let n = -5; n <= 5; n++) {
      graph.append(svg(document, "line", { x1: 10, y1: oy - n * scale, x2: W - 10, y2: oy - n * scale, stroke: "currentColor", opacity: n === 0 ? 0.8 : 0.12 }));
    }
    const x1 = -8, x2 = 8;
    const y1 = state.a * x1 + state.b, y2 = state.a * x2 + state.b;
    graph.append(svg(document, "line", { x1: ox + x1 * scale, y1: oy - y1 * scale, x2: ox + x2 * scale, y2: oy - y2 * scale, stroke: "currentColor", "stroke-width": 3 }));
    const y = state.a * state.x + state.b;
    graph.append(svg(document, "circle", { cx: ox + state.x * scale, cy: oy - y * scale, r: 5, fill: "currentColor" }));
    tbody.replaceChildren();
    for (const x of [-2, -1, 0, 1, 2]) {
      const row = document.createElement("tr");
      const cx = document.createElement("td");
      const cy = document.createElement("td");
      cx.textContent = String(x);
      cy.textContent = String(state.a * x + state.b);
      row.append(cx, cy); tbody.append(row);
    }
    status.textContent = `y = ${state.a}x ${state.b < 0 ? "−" : "+"} ${Math.abs(state.b)}；目前點 (${state.x}, ${y})。斜率 a 控制每增加 1 單位 x 時 y 的變化量，b 是 x=0 的截距。`;
    saved?.set(state);
  };

  const aControl = makeRange(document, { label: "斜率 a", min: -5, max: 5, step: 1, value: state.a, onInput: value => { state.a = value; update(); } });
  const bControl = makeRange(document, { label: "截距 b", min: -5, max: 5, step: 1, value: state.b, onInput: value => { state.b = value; update(); } });
  const xControl = makeRange(document, { label: "追蹤 x", min: -5, max: 5, step: 1, value: state.x, onInput: value => { state.x = value; update(); } });
  controls.append(aControl.wrapper, bControl.wrapper, xControl.wrapper);
  lab.append(controls, graph, table);
  root.querySelector(".component-visual-body")?.append(lab);
  update();
  return lab;
}

function geometryMode(spec) {
  const text = `${spec.title || ""} ${(spec.coreConcepts || []).join(" ")}`;
  if (/圓|圓周|半徑|直徑|切線/.test(text)) return "circle";
  if (/三角|勾股|相似/.test(text)) return "triangle";
  return "rectangle";
}

function mountGeometryLab({ document, root, block, spec }) {
  const store = storageFor(block.id);
  const prior = store?.get() || {};
  const mode = geometryMode(spec);
  const state = { u: number(prior.u, mode === "circle" ? 4 : 6), v: number(prior.v, 4) };
  const { lab, status } = makeLab(document, block, "動態幾何量測實驗室");
  const controls = document.createElement("div");
  const canvas = makeCanvas(document, `${spec.title} 的可操作幾何圖`);

  const update = () => {
    canvas.replaceChildren();
    if (mode === "circle") {
      const r = state.u;
      canvas.append(svg(document, "circle", { cx: 180, cy: 120, r: r * 16, fill: "none", stroke: "currentColor", "stroke-width": 3 }));
      canvas.append(svg(document, "line", { x1: 180, y1: 120, x2: 180 + r * 16, y2: 120, stroke: "currentColor", "stroke-width": 2 }));
      status.textContent = `半徑 r=${r}；直徑=${2 * r}；圓周長≈${(2 * Math.PI * r).toFixed(2)}；面積≈${(Math.PI * r * r).toFixed(2)}。拖曳半徑後，所有量同步更新。`;
    } else if (mode === "triangle") {
      const b = state.u, h = state.v;
      canvas.append(svg(document, "polygon", { points: `70,190 ${70 + b * 28},190 110,${190 - h * 28}`, fill: "none", stroke: "currentColor", "stroke-width": 3 }));
      canvas.append(svg(document, "line", { x1: 110, y1: 190, x2: 110, y2: 190 - h * 28, stroke: "currentColor", "stroke-dasharray": "5 4" }));
      status.textContent = `底=${b}、高=${h}；三角形面積=${(b * h / 2).toFixed(1)}。底或高改變時，圖形與面積立即同步。`;
    } else {
      const w = state.u, h = state.v;
      canvas.append(svg(document, "rect", { x: 70, y: 50, width: w * 30, height: h * 28, fill: "none", stroke: "currentColor", "stroke-width": 3 }));
      status.textContent = `長=${w}、寬=${h}；周長=${2 * (w + h)}；面積=${w * h}。拖曳尺寸後，周長與面積同步更新。`;
    }
    store?.set(state);
  };
  const first = makeRange(document, { label: mode === "circle" ? "半徑 r" : mode === "triangle" ? "底" : "長", min: 1, max: 8, value: state.u, onInput: value => { state.u = value; update(); } });
  controls.append(first.wrapper);
  if (mode !== "circle") {
    const second = makeRange(document, { label: mode === "triangle" ? "高" : "寬", min: 1, max: 7, value: state.v, onInput: value => { state.v = value; update(); } });
    controls.append(second.wrapper);
  }
  lab.append(controls, canvas);
  root.querySelector(".component-visual-body")?.append(lab);
  update();
  return lab;
}

function mountBalanceLab({ document, root, block, spec }) {
  const store = storageFor(block.id);
  const prior = store?.get() || {};
  const state = { x: number(prior.x, 2), leftA: 2, leftB: 5, right: 13 };
  const { lab, status } = makeLab(document, block, block.component === "AlgebraEquationMeaningBlock" ? "方程式意義與候選值實驗室" : "等式平衡實驗室");
  const scale = document.createElement("div");
  scale.className = "math-balance-visual";
  scale.setAttribute("role", "img");
  scale.setAttribute("aria-label", "等式左右兩側數值比較");
  const left = document.createElement("output");
  const sign = document.createElement("strong");
  const right = document.createElement("output");
  scale.append(left, sign, right);
  const update = () => {
    const lhs = state.leftA * state.x + state.leftB;
    left.textContent = `左：2×${state.x}+5 = ${lhs}`;
    right.textContent = `右：${state.right}`;
    sign.textContent = lhs === state.right ? "＝" : lhs < state.right ? "＜" : "＞";
    scale.dataset.balanced = String(lhs === state.right);
    status.textContent = lhs === state.right ? `x=${state.x} 代回原式後左右同為 ${state.right}，候選值通過原式檢查。` : `x=${state.x} 時左側 ${lhs}、右側 ${state.right}，尚未平衡；代回能直接看見候選值是否成立。`;
    store?.set(state);
  };
  const xControl = makeRange(document, { label: "候選 x", min: -5, max: 9, value: state.x, onInput: value => { state.x = value; update(); } });
  lab.append(xControl.wrapper, scale);
  root.querySelector(".component-visual-body")?.append(lab);
  update();
  return lab;
}

function mountEquivalentLab({ document, root, block }) {
  const store = storageFor(block.id);
  const prior = store?.get() || {};
  const state = { x: number(prior.x, 2) };
  const { lab, status } = makeLab(document, block, "等值表示多點檢查實驗室");
  const results = document.createElement("table");
  results.innerHTML = "<caption>2(x+3) 與 2x+6 的同步輸出</caption><thead><tr><th>x</th><th>2(x+3)</th><th>2x+6</th></tr></thead><tbody></tbody>";
  const tbody = results.querySelector("tbody");
  const update = () => {
    tbody.replaceChildren();
    for (const x of [state.x - 1, state.x, state.x + 1]) {
      const a = 2 * (x + 3), b = 2 * x + 6;
      const row = document.createElement("tr");
      for (const value of [x, a, b]) { const cell = document.createElement("td"); cell.textContent = String(value); row.append(cell); }
      tbody.append(row);
    }
    status.textContent = `目前以 x=${state.x - 1}, ${state.x}, ${state.x + 1} 比較輸出皆相同；數值檢查能抓出反例，但完整等值理由仍應回到分配律或代數推導。`;
    store?.set(state);
  };
  const xControl = makeRange(document, { label: "中心代入值 x", min: -6, max: 6, value: state.x, onInput: value => { state.x = value; update(); } });
  lab.append(xControl.wrapper, results);
  root.querySelector(".component-visual-body")?.append(lab);
  update();
  return lab;
}

function mountNumberLineLab({ document, root, block, spec }) {
  const store = storageFor(block.id);
  const prior = store?.get() || {};
  const state = { x: number(prior.x, 0), target: number(prior.target, 3) };
  const { lab, status } = makeLab(document, block, "數線位置與距離實驗室");
  const canvas = makeCanvas(document, `${spec.title} 的可操作數線`, 360, 120);
  const update = () => {
    canvas.replaceChildren();
    const x0 = 30, y = 60, unit = 25;
    canvas.append(svg(document, "line", { x1: x0, y1: y, x2: 330, y2: y, stroke: "currentColor", "stroke-width": 2 }));
    for (let n = -5; n <= 5; n++) {
      const px = 180 + n * unit;
      canvas.append(svg(document, "line", { x1: px, y1: y - 6, x2: px, y2: y + 6, stroke: "currentColor" }));
      const t = svg(document, "text", { x: px - 5, y: y + 24, fill: "currentColor" }); t.textContent = String(n); canvas.append(t);
    }
    canvas.append(svg(document, "circle", { cx: 180 + state.x * unit, cy: y, r: 7, fill: "currentColor" }));
    canvas.append(svg(document, "circle", { cx: 180 + state.target * unit, cy: y, r: 7, fill: "none", stroke: "currentColor", "stroke-width": 3 }));
    status.textContent = `目前位置 ${state.x}；目標 ${state.target}；距離 |${state.x}−${state.target}|=${Math.abs(state.x - state.target)}。實心點是目前位置，空心圈是目標。`;
    store?.set(state);
  };
  const xControl = makeRange(document, { label: "目前位置", min: -5, max: 5, value: state.x, onInput: value => { state.x = value; update(); } });
  const targetControl = makeRange(document, { label: "比較目標", min: -5, max: 5, value: state.target, onInput: value => { state.target = value; update(); } });
  lab.append(xControl.wrapper, targetControl.wrapper, canvas);
  root.querySelector(".component-visual-body")?.append(lab);
  update();
  return lab;
}

function mountStepwiseLab({ document, root, block }) {
  const { lab, status } = makeLab(document, block, "步驟推理可視化檢核");
  const stages = block.guidedActivity?.stages || [];
  const list = document.createElement("ol");
  list.className = "math-step-map";
  if (stages.length) {
    for (const [index, stage] of stages.entries()) {
      const item = document.createElement("li");
      item.textContent = `${index + 1}. ${stage.prompt}`;
      list.append(item);
    }
    status.textContent = `本題共有 ${stages.length} 個可檢核步驟；下方既有 guided activity 會逐步驗證輸入、錯答提示與重試，不會直接跳到答案。`;
  } else {
    for (const action of (block.studentActions || []).slice(0, 6)) {
      const item = document.createElement("li"); item.textContent = action; list.append(item);
    }
    status.textContent = "依本單元 studentActions 顯示可追溯步驟；每一步都必須留下理由或可驗證結果。";
  }
  lab.append(list);
  root.querySelector(".component-visual-body")?.append(lab);
  return lab;
}

export function enhanceMathInteractiveBlock({ document, root, spec, block }) {
  if (!document || !root || !block || spec?.subject !== "math" || !SUPPORTED.has(block.component)) return null;
  if (root.querySelector(".math-live-lab")) return root.querySelector(".math-live-lab");
  if (block.component === "FunctionRepresentationBlock") return mountFunctionLab({ document, root, block, spec });
  if (block.component === "GeometryManipulationBlock") return mountGeometryLab({ document, root, block, spec });
  if (block.component === "AlgebraBalanceBlock" || block.component === "AlgebraEquationMeaningBlock") return mountBalanceLab({ document, root, block, spec });
  if (block.component === "EquivalentExpressionCheckBlock") return mountEquivalentLab({ document, root, block, spec });
  if (block.component === "NumberLineBlock") return mountNumberLineLab({ document, root, block, spec });
  if (block.component === "StepwiseReasoningBlock") return mountStepwiseLab({ document, root, block, spec });
  return null;
}

export const MATH_LIVE_COMPONENTS = Object.freeze([...SUPPORTED]);

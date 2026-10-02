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


function mountQuadraticIdentitiesLab({ document, root, block, spec }) {
  const store = storageFor(block.id);
  const prior = store?.get() || {};
  const state = {
    a: clamp(number(prior.a, 4), 3, 8),
    b: clamp(number(prior.b, 2), 1, 7),
    mode: prior.mode || "plus",
    prediction: prior.prediction || "",
    revealed: Boolean(prior.revealed),
    transferA: clamp(number(prior.transferA, 5), 4, 9),
    transferB: clamp(number(prior.transferB, 1), 1, 8),
  };
  if (state.b >= state.a) state.b = state.a - 1;
  if (state.transferB >= state.transferA) state.transferB = state.transferA - 1;

  const { lab, status } = makeLab(document, block, "乘法公式面積探索臺");
  lab.classList.add("math-area-lab");
  const intro = document.createElement("p");
  intro.innerHTML = "<strong>先看圖，再預測。</strong> 操作 a、b，觀察面積區塊如何改變。";

  const modeBar = document.createElement("div");
  modeBar.className = "math-area-modebar";
  modeBar.setAttribute("role", "group");
  modeBar.setAttribute("aria-label", "公式模式");
  const figure = document.createElement("figure");
  figure.className = "math-area-figure";
  const canvas = makeCanvas(document, "乘法公式動態面積模型", 420, 360);
  const caption = document.createElement("figcaption");
  figure.append(canvas, caption);

  const controls = document.createElement("div");
  controls.className = "math-live-controls";
  const predict = document.createElement("fieldset");
  predict.className = "math-area-predict";
  const legend = document.createElement("legend");
  legend.textContent = "先預測，再揭示";
  predict.append(legend);
  const feedback = document.createElement("p");
  feedback.className = "math-area-feedback";
  feedback.setAttribute("aria-live", "polite");
  const evidence = document.createElement("div");
  evidence.className = "math-area-evidence";

  const modes = {
    plus: { label: "(a+b)²", correct: "two", choices: [["two","會有兩個 ab"],["none","只有 a² 與 b²"],["cancel","ab 會相消"]] },
    minus: { label: "(a−b)²", correct: "two", choices: [["two","兩個 −ab，角落補回 +b²"],["corner","最後是 −b²"],["cancel","交叉項相消"]] },
    diff: { label: "(a+b)(a−b)", correct: "cancel", choices: [["two","留下兩個 ab"],["cancel","+ab 與 −ab 相消"],["sum","變成 a²+b²"]] },
  };
  const persist = () => store?.set(state);
  const label = (text, attrs={}) => { const n=svg(document,"text",attrs); n.textContent=text; return n; };
  const rect = (x,y,w,h,textValue,fill) => {
    canvas.append(svg(document,"rect",{x,y,width:w,height:h,fill,stroke:"#334155","stroke-width":1.8}));
    if (state.revealed && textValue) canvas.append(label(textValue,{x:x+w/2,y:y+h/2+6,"text-anchor":"middle","font-size":18,"font-weight":800,fill:"#0f172a"}));
  };

  function draw() {
    canvas.replaceChildren();
    const a=state.a, b=Math.min(state.b,a-1), x=70, y=48, size=260;
    if (state.mode === "plus") {
      const ap=size*a/(a+b), bp=size-ap;
      rect(x,y,ap,ap,"a²","#dbeafe"); rect(x+ap,y,bp,ap,"ab","#fef3c7");
      rect(x,y+ap,ap,bp,"ab","#fef3c7"); rect(x+ap,y+ap,bp,bp,"b²","#ede9fe");
      canvas.append(label("a",{x:x+ap/2,y:28,"text-anchor":"middle","font-weight":700}));
      canvas.append(label("b",{x:x+ap+bp/2,y:28,"text-anchor":"middle","font-weight":700}));
      if(!state.revealed) canvas.append(label("先預測四塊面積",{x:200,y:185,"text-anchor":"middle","font-size":18,"font-weight":800}));
      caption.textContent=state.revealed ? \`整體面積 \${(a+b)**2}；四塊為 \${a*a}、\${a*b}、\${a*b}、\${b*b}。\` : "公式暫時隱藏。";
    } else if (state.mode === "minus") {
      const inner=size*(a-b)/a, cut=size-inner;
      rect(x,y,size,size,"a²","#dbeafe");
      rect(x+inner,y,cut,size,"−ab","#fee2e2"); rect(x,y+inner,size,cut,"−ab","#fee2e2");
      rect(x+inner,y+inner,cut,cut,"+b²","#dcfce7");
      canvas.append(svg(document,"rect",{x,y,width:inner,height:inner,fill:"none",stroke:"#0f172a","stroke-width":3}));
      if(!state.revealed) canvas.append(label("哪個角落被重複扣掉？",{x:200,y:185,"text-anchor":"middle","font-size":18,"font-weight":800}));
      caption.textContent=state.revealed ? "從 a² 扣兩條 ab；重疊的 b² 被扣兩次，因此要補回一次。" : "先追蹤兩條扣除區與重疊角。";
    } else {
      const scale=220/a, big=a*scale, small=b*scale, xx=82, yy=58;
      rect(xx,yy,big,big,"a²","#dbeafe"); rect(xx+big-small,yy+big-small,small,small,"−b²","#ede9fe");
      if(state.revealed) {
        canvas.append(label("+ab",{x:120,y:325,"font-size":18,"font-weight":800,fill:"#166534"}));
        canvas.append(label("−ab",{x:225,y:325,"font-size":18,"font-weight":800,fill:"#991b1b"}));
        canvas.append(label("→ 相消",{x:300,y:325,"font-size":18,"font-weight":800}));
      } else canvas.append(label("交叉項會留下嗎？",{x:200,y:185,"text-anchor":"middle","font-size":18,"font-weight":800}));
      caption.textContent=state.revealed ? "+ab 與 −ab 大小相同、符號相反，所以留下 a²−b²。" : "先預測交叉項。";
    }
    canvas.setAttribute("aria-label", \`\${modes[state.mode].label}，a=\${a}，b=\${b}，\${state.revealed?"已揭示":"尚未揭示"}\`);
  }

  function renderEvidence() {
    evidence.replaceChildren();
    evidence.hidden=!state.revealed;
    if(!state.revealed) return;
    const a=state.a,b=Math.min(state.b,a-1), p=document.createElement("p"), q=document.createElement("p");
    if(state.mode==="plus") p.textContent=\`(a+b)²=a²+ab+ab+b²=a²+2ab+b²；目前 (\${a}+\${b})²=\${(a+b)**2}。\`;
    else if(state.mode==="minus") p.textContent=\`(a−b)²=a²−ab−ab+b²=a²−2ab+b²；目前 (\${a}−\${b})²=\${(a-b)**2}。\`;
    else p.textContent=\`(a+b)(a−b)=a²−b²；目前 \${a+b}×\${a-b}=\${a*a-b*b}。\`;
    q.innerHTML="<strong>證據任務：</strong>指出圖中哪兩塊造成 2ab，或哪兩項互相抵消。";
    evidence.append(p,q);
    feedback.textContent = state.prediction===modes[state.mode].correct ? "預測吻合。請用圖中的區塊或相消位置解釋。" : "預測與觀察不同。請依圖形證據修正，不要只背公式。";
  }

  function renderChoices() {
    predict.querySelectorAll("button").forEach(n=>n.remove());
    for(const [value,textValue] of modes[state.mode].choices) {
      const b=document.createElement("button"); b.type="button"; b.textContent=textValue;
      b.setAttribute("aria-pressed",String(state.prediction===value));
      b.addEventListener("click",()=>{
        state.prediction=value; state.revealed=true; persist();
        predict.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
        draw(); renderEvidence();
      });
      predict.append(b);
    }
  }

  for(const key of Object.keys(modes)) {
    const b=document.createElement("button"); b.type="button"; b.textContent=modes[key].label;
    b.setAttribute("aria-pressed",String(state.mode===key));
    b.addEventListener("click",()=>{
      state.mode=key; state.prediction=""; state.revealed=false; persist();
      modeBar.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
      renderChoices(); draw(); renderEvidence();
      status.textContent=\`已切換到 \${modes[key].label}；先預測再揭示。\`;
    });
    modeBar.append(b);
  }

  const aControl=makeRange(document,{label:"a",min:3,max:8,value:state.a,onInput:value=>{
    state.a=value; if(state.b>=value) state.b=value-1; state.prediction=""; state.revealed=false; persist(); renderChoices(); draw(); renderEvidence();
  }});
  const bControl=makeRange(document,{label:"b",min:1,max:7,value:state.b,onInput:value=>{
    state.b=Math.min(value,state.a-1); state.prediction=""; state.revealed=false; persist(); renderChoices(); draw(); renderEvidence();
  }});
  const reset=document.createElement("button"); reset.type="button"; reset.textContent="重設並重新預測";
  reset.addEventListener("click",()=>{state.prediction="";state.revealed=false;persist();renderChoices();draw();renderEvidence();feedback.textContent="答案已隱藏。";});
  controls.append(aControl.wrapper,bControl.wrapper,reset);

  const transfer=document.createElement("section");
  transfer.className="math-area-transfer";
  const transferTitle=document.createElement("h5"); transferTitle.textContent="遷移：換數字，不換概念";
  const transferPrompt=document.createElement("p");
  const transferControls=document.createElement("div"); transferControls.className="math-live-controls";
  const ta=makeRange(document,{label:"新 a",min:4,max:9,value:state.transferA,onInput:value=>{state.transferA=value;if(state.transferB>=value)state.transferB=value-1;persist();updateTransfer();}});
  const tb=makeRange(document,{label:"新 b",min:1,max:8,value:state.transferB,onInput:value=>{state.transferB=Math.min(value,state.transferA-1);persist();updateTransfer();}});
  const answer=document.createElement("input"); answer.type="number"; answer.inputMode="numeric"; answer.setAttribute("aria-label","遷移題答案");
  const check=document.createElement("button"); check.type="button"; check.textContent="檢查遷移";
  const transferFeedback=document.createElement("p"); transferFeedback.setAttribute("aria-live","polite");
  transferControls.append(ta.wrapper,tb.wrapper);
  transfer.append(transferTitle,transferPrompt,transferControls,answer,check,transferFeedback);
  function updateTransfer(){transferPrompt.textContent=\`不看上面的數值，預測 (\${state.transferA}+\${state.transferB})² 的面積。\`;}
  check.addEventListener("click",()=>{
    const expected=(state.transferA+state.transferB)**2;
    transferFeedback.textContent=Number(answer.value)===expected ? \`正確。答案 \${expected}；你把 a²+2ab+b² 遷移到新數值。\` : "再把四塊相加：a²、ab、ab、b²。";
  });

  lab.append(intro,modeBar,figure,controls,predict,feedback,evidence,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  renderChoices(); draw(); renderEvidence(); updateTransfer();
  status.textContent="先預測，選擇後才揭示面積證據與公式。";
  persist();
  return lab;
}

function mountGeometryLab({ document, root, block, spec }) {
  if (spec?.lessonId === "cur-math-content-a-8-1") return mountQuadraticIdentitiesLab({ document, root, block, spec });
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

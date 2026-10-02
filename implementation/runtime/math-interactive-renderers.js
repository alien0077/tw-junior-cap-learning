const SVG_NS = "http://www.w3.org/2000/svg";
const STORAGE_PREFIX = "tw-junior-cap-learning:math-lab:";

const SUPPORTED = new Set([
  "FunctionRepresentationBlock",
  "GeometryManipulationBlock",
  "AlgebraBalanceBlock",
  "AlgebraEquationMeaningBlock",
  "SystemIntersectionBlock",
  "SystemEliminationBlock",
  "QuadraticMeaningBlock",
  "QuadraticSolutionBlock",
  "ProbabilityExperimentBlock",
  "DataExplorerBlock",
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


function mountLinearEquationCheckLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={candidate:number(prior.candidate,0)};
  const {lab,status}=makeLab(document,block,"一次方程式等價變形與原式驗算臺");
  lab.classList.add("math-linear-equation-check-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>解出 x 不是終點。</strong> 保留每一行等價變形，最後一定回到原方程式比較左右兩側。";

  const predict=document.createElement("fieldset");
  const pl=document.createElement("legend");pl.textContent="2(x+3)=14 的第一步？";predict.append(pl);
  const pf=document.createElement("p");pf.setAttribute("aria-live","polite");
  const chain=document.createElement("div");chain.className="math-linear-chain";chain.hidden=true;chain.setAttribute("role","img");chain.setAttribute("aria-label","兩側同除二，再兩側同減三的等價變形鏈");
  chain.innerHTML="<span>2(x+3)=14</span><b>÷2 兩側</b><span>x+3=7</span><b>−3 兩側</b><span>x=4</span>";
  [["divide","左右兩側同除以 2"],["left","只把左側 2 消掉"],["move3","先把括號內 3 移到右邊"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{
      if(value==="divide"){chain.hidden=false;pf.textContent="正確。外面的 2 乘整個括號，因此先對等號兩側同除 2。";}
      else pf.textContent="要保持等式，操作必須同步作用在左右兩側；也不能把括號內 3 當成已在括號外。";
    });predict.append(b);
  });predict.append(pf);

  const compare=document.createElement("div");compare.className="math-linear-compare";compare.setAttribute("role","img");compare.setAttribute("aria-label","候選 x 代回原式的左右值比較");
  const feedback=document.createElement("p");feedback.setAttribute("aria-live","polite");
  const update=()=>{
    const left=2*(state.candidate+3),right=14;
    compare.innerHTML="<div><span>左 2(x+3)</span><strong>"+left+"</strong></div><b>"+(left===right?"=":(left<right?"<":">"))+"</b><div><span>右</span><strong>14</strong></div>";
    feedback.textContent=left===right
      ?"x="+state.candidate+" 代回最原始方程式後左右同為 14，因此候選值通過。"
      :"x="+state.candidate+" 時左右不相等；保留這個錯誤候選，回頭定位括號、同除或移項哪一步出了問題。";
    status.textContent=left===right?"原式驗算通過；接著把同樣流程遷移到生活費用題。":"原式驗算尚未通過。";
    store?.set(state);
  };
  const candidate=makeRange(document,{label:"候選 x",min:-2,max:8,value:state.candidate,onInput:v=>{state.candidate=v;update();}});

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：15x+80=170，哪個候選人數通過原式？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["6","6"],["4","4"],["90","90"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent="x="+label;
    b.addEventListener("click",()=>{
      tf.textContent=value==="6"
        ?"正確。15×6+80=170；等式成立，而且 6 人符合非負整數的情境限制。"
        :"代回 15x+80=170 逐項計算；固定費 80 不可漏掉。";
    });transfer.append(b);
  });transfer.append(tf);

  lab.append(intro,predict,chain,candidate.wrapper,compare,feedback,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
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


function mountSystemIntersectionLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={x:clamp(number(prior.x,10),0,18),prediction:String(prior.prediction||""),transfer:String(prior.transfer||"")};
  const {lab,status}=makeLab(document,block,"雙條件共同解檢查臺");
  lab.classList.add("math-system-intersection-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>一組數要過兩關。</strong> 第一條式成立還不夠；同一個有序數對必須同時滿足兩條限制。";
  const predict=document.createElement("fieldset");
  const pl=document.createElement("legend");pl.textContent="先預測：(10,8) 能不能直接叫共同解？";predict.append(pl);
  const feedback=document.createElement("p");feedback.setAttribute("aria-live","polite");

  const candidate=document.createElement("div");candidate.className="math-system-candidate";
  candidate.setAttribute("role","img");
  candidate.setAttribute("aria-label","候選有序數對逐一通過兩條限制的模型");
  const pair=document.createElement("div");pair.className="math-system-pair";
  const cards=document.createElement("div");cards.className="math-system-cards";
  candidate.append(pair,cards);

  const choose=(value,label)=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;b.setAttribute("aria-pressed",String(state.prediction===value));
    b.addEventListener("click",()=>{
      state.prediction=value;store?.set(state);
      predict.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
      feedback.textContent=value==="no"?"正確。(10,8) 只通過 x+y=18；第二式得到 28，不是 30。":"再檢查第二張工作單。聯立方程式的解必須同時通過兩式。";
      update();
    });
    predict.append(b);
  };
  choose("yes","可以，只要通過其中一式");
  choose("no","不可以，兩式都要成立");

  const update=()=>{
    const y=18-state.x, first=state.x+y, second=2*state.x+y;
    pair.innerHTML="<span>x 果汁</span><strong>"+state.x+"</strong><span>y 茶</span><strong>"+y+"</strong>";
    cards.replaceChildren();
    const make=(title,equation,value,target)=>{
      const article=document.createElement("article");article.className="math-system-card";
      const h=document.createElement("strong");h.textContent=title;
      const eq=document.createElement("p");eq.textContent=equation;
      const result=document.createElement("p");result.className="math-system-result";
      if(!state.prediction){result.textContent="先完成預測，計算結果暫時隱藏。";}
      else{
        const pass=value===target;
        result.textContent=(pass?"✓ 通過：":"✗ 未通過：")+"左側 "+value+"，右側 "+target;
        result.dataset.pass=String(pass);
      }
      article.append(h,eq,result);return article;
    };
    cards.append(
      make("工作單 A：總杯數","x + y = 18",first,18),
      make("工作單 B：冰塊需求","2x + y = 30",second,30)
    );
    status.textContent=!state.prediction
      ?"先預測，再調整候選數對；答案保持隱藏。"
      :(first===18&&second===30
        ?"目前 ("+state.x+","+y+") 同時通過兩條限制，是共同解。"
        :"目前 ("+state.x+","+y+") 尚未同時通過兩條限制；第二式左側為 "+second+"。");
    store?.set(state);
  };
  const xControl=makeRange(document,{label:"果汁杯數 x；茶杯數 y 自動維持總杯數 18",min:0,max:18,value:state.x,onInput:value=>{state.x=value;update();}});

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：x+y=25、2x+y=46，(21,4) 是否為共同解？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["yes","同時通過兩式"],["first","只通過第一式"],["second","只通過第二式"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{
      state.transfer=value;store?.set(state);
      tf.textContent=value==="yes"?"正確。21+4=25，2×21+4=46；同一有序數對兩式都成立。":"再逐式代入。兩條式都要各自核對，而且 x、y 順序不能交換。";
    });
    transfer.append(b);
  });transfer.append(tf);

  lab.append(intro,predict,feedback,candidate,xControl.wrapper,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  update();
  return lab;
}

function mountSystemEliminationLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={method:String(prior.method||""),back:String(prior.back||""),transfer:String(prior.transfer||"")};
  const {lab,status}=makeLab(document,block,"整行消去與回代驗證臺");
  lab.classList.add("math-system-elimination-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>先看係數，再選方法。</strong> 每次消去都是整條等式一起做運算；求出一個未知數後還要回代與雙式驗算。";
  const stack=document.createElement("div");stack.className="math-system-stack";stack.setAttribute("role","img");stack.setAttribute("aria-label","兩條聯立方程式按 x、y、常數對齊");
  const renderStack=()=>{
    stack.innerHTML="<div><span>x</span><span>+</span><span>y</span><span>=</span><span>35</span></div>"+
      "<div><span>2x</span><span>+</span><span>y</span><span>=</span><span>50</span></div>"+
      (state.method==="subtract"
        ?"<div class=\"math-system-operation\"><strong>x</strong><span>+</span><strong>0y</strong><span>=</span><strong>15</strong></div>"
        :"<div class=\"math-system-operation is-pending\">先預測整行運算，再揭示消去結果</div>");
  };

  const method=document.createElement("fieldset");
  const ml=document.createElement("legend");ml.textContent="哪個操作最省步驟？";method.append(ml);
  const mf=document.createElement("p");mf.setAttribute("aria-live","polite");
  [["subtract","第二式 − 第一式，消去 y"],["left-only","只把左邊相減"],["double","兩式都先乘 2"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{
      state.method=value;store?.set(state);renderStack();
      mf.textContent=value==="subtract"?"正確。y 係數相同，整行相減：50−35 也必須一起做，得到 x=15。":value==="left-only"?"不成立。等式運算必須左右兩邊同步；只動左邊會破壞等值。":"可以繼續算，但沒有必要；本題 y 係數已經相同，直接相減更短。";
      status.textContent=value==="subtract"?"已消去 y 得 x=15；現在還不能結束，請回代求 y。":"重新看 y 欄的係數結構再選方法。";
    });method.append(b);
  });method.append(mf);

  const back=document.createElement("fieldset");
  const bl=document.createElement("legend");bl.textContent="x=15 後，回代 x+y=35 得 y=?";back.append(bl);
  const bf=document.createElement("p");bf.setAttribute("aria-live","polite");
  [["20","20"],["15","15"],["35","35"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{
      state.back=value;store?.set(state);
      if(state.method!=="subtract"){bf.textContent="先完成有效的整行消去，再回代。";return;}
      bf.textContent=value==="20"?"正確。15+y=35，所以 y=20；完整解是 (15,20)。":"把 15 代回 15+y=35，求出尚缺的量。";
      verify.hidden=value!=="20";
      status.textContent=value==="20"?"完整解 (15,20)；兩條原式都必須驗算。":"回代尚未完成。";
    });back.append(b);
  });back.append(bf);

  const verify=document.createElement("div");verify.className="math-system-cards";verify.hidden=true;
  verify.innerHTML="<article class=\"math-system-card\"><strong>原式 A</strong><p>x+y=35</p><p>15+20=35 ✓</p></article>"+
    "<article class=\"math-system-card\"><strong>原式 B</strong><p>2x+y=50</p><p>2×15+20=50 ✓</p></article>";

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：x+y=40、3x+2y=100，先怎麼消去 y？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["minus2","第一式整行乘 −2，再與第二式相加"],["subtract","兩式直接相減"],["flip-y","只把 y 改成 −y"]].forEach(([value,label])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{
      state.transfer=value;store?.set(state);
      tf.textContent=value==="minus2"?"正確。−2x−2y=−80 與 3x+2y=100 相加得 x=20，再回代 y=20。":"要讓 y 係數成為相反數，而且乘數必須作用到整條等式。";
    });transfer.append(b);
  });transfer.append(tf);

  lab.append(intro,stack,method,back,verify,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  renderStack();
  status.textContent="先觀察係數，選擇能保留等式結構的整行運算。";
  return lab;
}


function mountQuadraticMeaningLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={mode:String(prior.mode||"classify"),candidate:number(prior.candidate,1)};
  const {lab,status}=makeLab(document,block,"二次方程式意義三站實驗室");
  lab.classList.add("math-quadratic-meaning-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>先搞清楚『是什麼』，再學『怎麼解』。</strong> 本課只做化簡分類、候選值驗證與情境列式。";
  const modes=document.createElement("fieldset");
  const ml=document.createElement("legend");ml.textContent="選擇工作站";modes.append(ml);
  const stage=document.createElement("section");stage.className="math-quadratic-stage";
  const feedback=document.createElement("p");feedback.className="math-quadratic-feedback";feedback.setAttribute("aria-live","polite");

  const button=(parent,label,onClick)=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",onClick);parent.append(b);return b;
  };
  const setMode=value=>{state.mode=value;store?.set(state);modes.querySelectorAll("button").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.mode===value)));render();};
  [["classify","化簡後分類"],["root","候選根左右代入"],["context","面積情境列式"]].forEach(([value,label])=>{
    const b=button(modes,label,()=>setMode(value));b.dataset.mode=value;
  });

  const render=()=>{
    stage.replaceChildren();feedback.textContent="";
    if(state.mode==="classify"){
      stage.setAttribute("role","img");stage.setAttribute("aria-label","原方程式先化簡再判斷是否仍為一元二次方程式");
      const before=document.createElement("div");before.className="math-q-line";before.innerHTML="<span>原式</span><strong>2x²+3x=x²+7x−4</strong>";
      const arrow=document.createElement("p");arrow.textContent="先移項、合併同類項 ↓";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="化簡後是否為一元二次方程式？";prediction.append(pl);
      button(prediction,"是",()=>{after.hidden=false;trap.hidden=false;feedback.textContent="正確。化簡為 x²−4x+4=0：一個未知數、最高次2、有等號。";});
      button(prediction,"不是",()=>{feedback.textContent="再化簡一次。x² 項沒有完全消失；判斷要看化簡後的式子。";});
      const after=document.createElement("div");after.className="math-q-line is-result";after.hidden=true;after.innerHTML="<span>化簡</span><strong>x²−4x+4=0</strong>";
      const trap=document.createElement("div");trap.className="math-q-note";trap.hidden=true;trap.innerHTML="<strong>反例：</strong>3x²+2x²=5x² → 0=0，未知數消失，所以原式看見 x² 仍不足以分類。";
      stage.append(before,arrow,prediction,after,trap);
      status.textContent="分類站：一定先化簡，再看未知數種類、最高次與等號。";
    }else if(state.mode==="root"){
      const row=document.createElement("div");row.className="math-q-root-row";row.setAttribute("role","img");row.setAttribute("aria-label","候選 x 同時代入方程式左右兩側");
      const update=()=>{
        const left=state.candidate*state.candidate+3*state.candidate,right=10;
        row.innerHTML="<div><span>左側 x²+3x</span><strong>"+left+"</strong></div><b>"+(left===right?"=":(left<right?"<":">"))+"</b><div><span>右側</span><strong>"+right+"</strong></div>";
        feedback.textContent=left===right
          ?"x="+state.candidate+" 使左右同為 10，所以它是這個方程式的一個解；這仍不代表已求出全部根。"
          :"x="+state.candidate+" 時左右不相等，因此這個候選值不是解。";
        store?.set(state);
      };
      const control=makeRange(document,{label:"候選 x",min:-4,max:4,value:state.candidate,onInput:v=>{state.candidate=v;update();}});
      stage.append(control.wrapper,row);update();
      status.textContent="驗根站：同一候選值必須同時代入原等式左右兩側。";
    }else{
      const figure=document.createElement("div");figure.className="math-q-context-rect";figure.setAttribute("role","img");figure.setAttribute("aria-label","短邊 x 長邊 x 加四的長方形面積模型");
      figure.innerHTML="<div class=\"math-q-rect-box\"><span>長 x+4</span><strong>面積 45</strong><em>寬 x</em></div>";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="哪個式子保留面積量義？";prediction.append(pl);
      button(prediction,"x(x+4)=45",()=>{feedback.textContent="正確。面積是長×寬；x>0 是情境允許範圍，不是用來改寫等式。";});
      button(prediction,"x+x+4=45",()=>{feedback.textContent="這是長度相加，不是面積。回到長方形面積＝長×寬。";});
      button(prediction,"x²+4=45",()=>{feedback.textContent="少了交叉項 4x。長 x+4 與寬 x 的乘積是 x(x+4)。";});
      const check=document.createElement("p");check.innerHTML="<strong>候選 x=5：</strong>5×9=45，所以 5 通過原等式；但這一步只是驗證候選。";
      stage.append(figure,prediction,check);
      status.textContent="建模站：量義、單位、等式與情境範圍分開記錄。";
    }
  };

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：3x²+2x²=5x² 化簡後仍是二次方程式嗎？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  button(transfer,"不是，化簡為 0=0",()=>{tf.textContent="正確。未知數消失，不再是一元二次方程式。";});
  button(transfer,"是，因為原本有 x²",()=>{tf.textContent="先化簡。左右的 5x² 抵消後只剩 0=0。";});
  transfer.append(tf);

  lab.append(intro,modes,stage,feedback,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  setMode(state.mode);
  return lab;
}

function mountQuadraticSolutionLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={mode:String(prior.mode||"factor")};
  const {lab,status}=makeLab(document,block,"二次方程式解法分站工作台");
  lab.classList.add("math-quadratic-solution-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>建模、求根、驗根、情境篩選分開。</strong> 每站只處理一種認知工作，避免公式與情境條件互相干擾。";
  const modes=document.createElement("fieldset");
  const ml=document.createElement("legend");ml.textContent="選擇工作站";modes.append(ml);
  const stage=document.createElement("section");stage.className="math-quadratic-stage";
  const feedback=document.createElement("p");feedback.className="math-quadratic-feedback";feedback.setAttribute("aria-live","polite");

  const button=(parent,label,onClick)=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",onClick);parent.append(b);return b;
  };
  const setMode=value=>{state.mode=value;store?.set(state);modes.querySelectorAll("button").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.mode===value)));render();};
  [["factor","矩形建模＋完整根集"],["square","配方法"],["formula","判別式＋公式解"],["transfer","方法選擇遷移"]].forEach(([value,label])=>{
    const b=button(modes,label,()=>setMode(value));b.dataset.mode=value;
  });

  const render=()=>{
    stage.replaceChildren();feedback.textContent="";
    if(state.mode==="factor"){
      const rect=document.createElement("div");rect.className="math-q-context-rect";rect.setAttribute("role","img");rect.setAttribute("aria-label","寬 w 長 w 加五的木板面積八十四");
      rect.innerHTML="<div class=\"math-q-rect-box\"><span>長 w+5</span><strong>面積 84</strong><em>寬 w</em></div>";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="w²+5w−84=0 會得到幾個代數根？";prediction.append(pl);
      const roots=document.createElement("div");roots.className="math-q-roots";roots.hidden=true;
      roots.innerHTML="<article><strong>代數根集合</strong><p>{−12, 7}</p></article><article><strong>正寬度情境</strong><p>只允許 w=7，長=12</p></article>";
      button(prediction,"2 個",()=>{roots.hidden=false;feedback.textContent="正確。(w+12)(w−7)=0，先完整保留 −12 與 7；情境再另外排除負寬度。";});
      button(prediction,"只取正根 7",()=>{feedback.textContent="過早套用情境。代數根先完整寫成 {−12,7}，再由正長度條件保留 7。";});
      button(prediction,"沒有實根",()=>{feedback.textContent="可整數因式分解；12×(−7)=−84 且 12+(−7)=5。";});
      stage.append(rect,prediction,roots);
      status.textContent="根集站：代數根與實際可行尺寸分兩欄。";
    }else if(state.mode==="square"){
      const balance=document.createElement("div");balance.className="math-q-square-balance";balance.setAttribute("role","img");balance.setAttribute("aria-label","配方法在等式左右兩側同步加四");
      balance.innerHTML="<div><span>左側</span><strong>x²+4x</strong><em>+ ?</em></div><b>=</b><div><span>右側</span><strong>−1</strong><em>+ ?</em></div>";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="要補成平方，4 應加在哪裡？";prediction.append(pl);
      button(prediction,"左右兩側都加 4",()=>{
        balance.innerHTML="<div><span>左側</span><strong>x²+4x+4</strong></div><b>=</b><div><span>右側</span><strong>3</strong></div>";
        feedback.textContent="正確。(x+2)²=3，所以 x=−2±√3；兩側同步才能保留原解集合。";
      });
      button(prediction,"只加左側",()=>{feedback.textContent="這會改變等式。任何等價變形都必須同步維持左右兩側。";});
      stage.append(balance,prediction);
      status.textContent="配方法站：補平方不是裝飾，而是等式兩側同步的等價變形。";
    }else if(state.mode==="formula"){
      const coeff=document.createElement("div");coeff.className="math-q-coeff-cards";coeff.setAttribute("role","img");coeff.setAttribute("aria-label","a 等於二 b 等於三 c 等於負二");
      coeff.innerHTML="<span>a<strong>2</strong></span><span>b<strong>3</strong></span><span>c<strong>−2</strong></span>";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="Δ=b²−4ac 等於多少？";prediction.append(pl);
      const result=document.createElement("p");result.hidden=true;
      button(prediction,"25",()=>{result.hidden=false;result.innerHTML="<strong>Δ=25&gt;0</strong> → 兩個相異實根；x=(-3±5)/4 → 1/2、−2。";feedback.textContent="正確。c 是負數，−4ac 會變成加 16。";});
      button(prediction,"−7",()=>{feedback.textContent="重新代入 c=−2；符號不能在帶入公式時遺失。";});
      button(prediction,"7",()=>{feedback.textContent="先算 9−4×2×(−2)=9+16。";});
      stage.append(coeff,prediction,result);
      status.textContent="公式站：先鎖定 a、b、c 的原符號，再算判別式。";
    }else{
      const map=document.createElement("div");map.className="math-q-method-map";
      map.innerHTML="<article><strong>因式分解</strong><p>能快速找到整數因式時優先。</p></article><article><strong>配方法</strong><p>補 (b/2)²，兩側同步。</p></article><article><strong>公式解</strong><p>一般情況可用，先鎖定 a、b、c。</p></article>";
      const prediction=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="x²−x−12=0 最直接用哪個？";prediction.append(pl);
      button(prediction,"因式分解",()=>{feedback.textContent="正確。(x−4)(x+3)=0 → x=4 或 −3；兩根都先保留並驗算。";});
      button(prediction,"只能公式解",()=>{feedback.textContent="公式可用，但不是最省步驟。這題可直接找到乘積 −12、和 −1 的整數因式。";});
      stage.append(map,prediction);
      status.textContent="方法站：依式子結構選擇方法，不背固定順序。";
    }
  };

  lab.append(intro,modes,stage,feedback);
  root.querySelector(".component-visual-body")?.prepend(lab);
  setMode(state.mode);
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


function goldButton(document, parent, label, onClick) {
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = label;
  button.addEventListener("click", onClick);
  parent.append(button);
  return button;
}

function mountSignedOperationsGoldLab({ document, root, block }) {
  const store = storageFor(block.id), prior = store?.get() || {};
  const state = { revealed: Boolean(prior.revealed), evidence: String(prior.evidence || "") };
  const { lab, status } = makeLab(document, block, "帶號運算：運算樹 × 數線稽核");
  lab.classList.add("math-gold-signed-lab");

  const intro = document.createElement("p");
  intro.innerHTML = "<strong>先預測，不先算到底。</strong> 原式：−18.5＋4×(−1.25)−(−0.75)。先找乘法節點，再處理外層加減。";
  const predict = document.createElement("fieldset");
  const legend = document.createElement("legend"); legend.textContent = "結果大致落在哪裡？"; predict.append(legend);
  const feedback = document.createElement("p"); feedback.setAttribute("aria-live","polite");
  const canvas = makeCanvas(document, "負數混合運算數線：從負18.5加負5，再因減去負0.75向右0.75", 360, 180);
  const tree = document.createElement("div"); tree.className = "math-gold-operation-tree"; tree.hidden = !state.revealed;
  tree.innerHTML = "<article><b>先做乘法</b><span>4×(−1.25)</span><strong>−5</strong></article><article><b>外層合併</b><span>−18.5+(−5)</span><strong>−23.5</strong></article><article><b>雙負號</b><span>−(−0.75)</span><strong>+0.75 → −22.75</strong></article>";
  const evidence = document.createElement("fieldset"); evidence.hidden = !state.revealed;
  const el = document.createElement("legend"); el.textContent = "選一層證據"; evidence.append(el);
  const evidenceText = document.createElement("p"); evidenceText.setAttribute("aria-live","polite");

  const map = value => 28 + ((value + 25) / 27) * 300;
  function draw() {
    canvas.replaceChildren();
    canvas.append(svg(document,"line",{x1:28,y1:96,x2:328,y2:96,stroke:"currentColor","stroke-width":2}));
    for (const value of [-25,-20,-15,-10,-5,0]) {
      const x = map(value);
      canvas.append(svg(document,"line",{x1:x,y1:89,x2:x,y2:103,stroke:"currentColor"}));
      const t = svg(document,"text",{x,y:126,"text-anchor":"middle",fill:"currentColor"}); t.textContent = String(value); canvas.append(t);
    }
    const start = map(-18.5);
    canvas.append(svg(document,"circle",{cx:start,cy:96,r:6,fill:"currentColor"}));
    const st = svg(document,"text",{x:start,y:72,"text-anchor":"middle",fill:"currentColor"}); st.textContent="−18.5"; canvas.append(st);
    if (state.revealed) {
      const mid = map(-23.5), end = map(-22.75);
      canvas.append(svg(document,"line",{x1:start,y1:86,x2:mid,y2:86,stroke:"currentColor","stroke-width":3}));
      canvas.append(svg(document,"line",{x1:mid,y1:110,x2:end,y2:110,stroke:"currentColor","stroke-width":3,"stroke-dasharray":"5 3"}));
      canvas.append(svg(document,"circle",{cx:mid,cy:96,r:6,fill:"none",stroke:"currentColor","stroke-width":2}));
      canvas.append(svg(document,"circle",{cx:end,cy:96,r:8,fill:"currentColor"}));
      const a=svg(document,"text",{x:(start+mid)/2,y:58,"text-anchor":"middle",fill:"currentColor"});a.textContent="加 −5（向左）";canvas.append(a);
      const b=svg(document,"text",{x:(mid+end)/2,y:148,"text-anchor":"middle",fill:"currentColor"});b.textContent="−(−0.75)=+0.75（向右）";canvas.append(b);
      const f=svg(document,"text",{x:end,y:72,"text-anchor":"middle",fill:"currentColor"});f.textContent="−22.75";canvas.append(f);
    } else {
      const q=svg(document,"text",{x:180,y:48,"text-anchor":"middle",fill:"currentColor","font-weight":800});q.textContent="先預測再揭示移動";canvas.append(q);
    }
  }
  const reveal = ok => {
    state.revealed = true; store?.set(state); tree.hidden=false; evidence.hidden=false; draw();
    feedback.textContent = ok ? "預測合理。第一個必做節點是 4×(−1.25)=−5。" : "再估一次：起點已是 −18.5，又加入 −5，最後只補回 +0.75，所以仍在負二十多。";
    status.textContent = "外層數線：−18.5 → −23.5 → −22.75；雙負號只作用在最後一筆。";
  };
  goldButton(document,predict,"負二十多",()=>reveal(true));
  goldButton(document,predict,"接近 0",()=>reveal(false));
  goldButton(document,predict,"正二十多",()=>reveal(false));

  goldButton(document,evidence,"乘法先做",()=>{state.evidence="mul";store?.set(state);evidenceText.textContent="4×(−1.25)=−5；先保留完整帶號數，再交給外層加減。";});
  goldButton(document,evidence,"減去負數",()=>{state.evidence="minus";store?.set(state);evidenceText.textContent="只有 −(−0.75) 改寫成 +0.75；數線因此由 −23.5 向右。";});
  goldButton(document,evidence,"共同分母",()=>{state.evidence="fraction";store?.set(state);evidenceText.textContent="−74/4−20/4+3/4=−91/4=−22.75，與小數路徑一致。";});
  evidence.append(evidenceText);

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：−6−2×(−3)+(−4)÷2";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  goldButton(document,transfer,"−2",()=>{tf.textContent="正確。先得 −6 與 −2，再算 −6−(−6)−2=−2。";});
  goldButton(document,transfer,"2",()=>{tf.textContent="檢查最後的 (−4)÷2 仍是 −2；雙負號不會把它改正。";});
  goldButton(document,transfer,"−24",()=>{tf.textContent="這通常來自左至右直接算。先完成乘除子運算。";});
  transfer.append(tf);

  lab.append(intro,predict,feedback,canvas,tree,evidence,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  draw();
  status.textContent = state.revealed ? "已解鎖運算樹與數線證據。" : "預測前不揭示最後移動與答案。";
  return lab;
}

function mountLinearParameterGoldLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={a:clamp(number(prior.a,8),4,18),b:clamp(number(prior.b,50),20,60),x:clamp(number(prior.x,5),0,8),mode:String(prior.mode||"a")};
  const {lab,status}=makeLab(document,block,"一次函數：式 × 表 × 圖同步控制台");
  lab.classList.add("math-gold-function-lab");
  const intro=document.createElement("p");intro.innerHTML="<strong>一次只改一個參數。</strong> 比較 a 時鎖住 b；比較 b 時鎖住 a。";
  const modes=document.createElement("fieldset");const ml=document.createElement("legend");ml.textContent="探索模式";modes.append(ml);
  const canvas=makeCanvas(document,"一次函數參數同步圖",360,270);
  const table=document.createElement("table");table.className="math-live-table";
  const controls=document.createElement("div");controls.className="math-live-controls";
  const feedback=document.createElement("p");feedback.setAttribute("aria-live","polite");

  const point=(x,y)=>({x:42+x*34,y:238-y*.95});
  const drawLine=(m,b,secondary=false)=>{
    const p1=point(0,b),p2=point(8,m*8+b);
    canvas.append(svg(document,"line",{x1:p1.x,y1:p1.y,x2:p2.x,y2:p2.y,stroke:"currentColor","stroke-width":secondary?2:3,"stroke-dasharray":secondary?"6 4":"none"}));
  };
  const render=()=>{
    canvas.replaceChildren();controls.replaceChildren();table.replaceChildren();
    canvas.append(svg(document,"line",{x1:42,y1:20,x2:42,y2:238,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:42,y1:238,x2:326,y2:238,stroke:"currentColor","stroke-width":2}));
    if(state.mode==="a"){
      drawLine(18,30,true);drawLine(state.a,30,false);
      const c=makeRange(document,{label:"新的斜率 a",min:4,max:18,value:state.a,onInput:v=>{state.a=v;store?.set(state);render();}});
      controls.append(c.wrapper);
      table.innerHTML="<caption>固定 b=30</caption><thead><tr><th>x</th><th>18x+30</th><th>"+state.a+"x+30</th></tr></thead><tbody>"+[0,2,4].map(v=>"<tr><td>"+v+"</td><td>"+(18*v+30)+"</td><td>"+(state.a*v+30)+"</td></tr>").join("")+"</tbody>";
      feedback.textContent="x=0 時兩式都等於30；改變的是每單位 x 的固定變化量。";
      status.textContent="a 控制斜率；b=30 的 y 截距保持不變。";
    }else if(state.mode==="b"){
      drawLine(8,30,true);drawLine(8,state.b,false);
      const c=makeRange(document,{label:"新的截距 b",min:20,max:60,step:5,value:state.b,onInput:v=>{state.b=v;store?.set(state);render();}});
      controls.append(c.wrapper);
      table.innerHTML="<caption>固定 a=8</caption><thead><tr><th>x</th><th>8x+30</th><th>8x+"+state.b+"</th></tr></thead><tbody>"+[0,2,4].map(v=>"<tr><td>"+v+"</td><td>"+(8*v+30)+"</td><td>"+(8*v+state.b)+"</td></tr>").join("")+"</tbody>";
      feedback.textContent="兩線斜率相同；每個同一 x 的輸出都相差 "+(state.b-30)+"。";
      status.textContent="b 控制初始值／y截距；a=8 保持固定。";
    }else{
      drawLine(18,30,true);drawLine(24,0,false);
      const c=makeRange(document,{label:"比較同一個 x",min:0,max:8,value:state.x,onInput:v=>{state.x=v;store?.set(state);render();}});
      controls.append(c.wrapper);
      const y1=18*state.x+30,y2=24*state.x,p=point(state.x,y1);
      canvas.append(svg(document,"circle",{cx:p.x,cy:p.y,r:6,fill:"currentColor"}));
      table.innerHTML="<caption>同一 x 的兩方案費用</caption><tbody><tr><th>甲</th><td>"+y1+"</td></tr><tr><th>乙</th><td>"+y2+"</td></tr><tr><th>價差</th><td>"+Math.abs(y1-y2)+"</td></tr></tbody>";
      feedback.textContent=state.x===5?"x=5 時兩方案同為120；圖、表與 18x+30=24x 一致。":"目前價差 "+Math.abs(y1-y2)+"；移動 x 找價差0。";
      status.textContent="交點的定義是同一輸入下兩個輸出相等。";
    }
  };
  [["a","只改 a"],["b","只改 b"],["cross","找交點"]].forEach(([value,label])=>{
    const btn=goldButton(document,modes,label,()=>{state.mode=value;store?.set(state);modes.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===btn)));render();});
    btn.setAttribute("aria-pressed",String(state.mode===value));
  });
  const transfer=document.createElement("p");transfer.className="math-gold-transfer-note";transfer.textContent="遷移：y=−7x+100 的斜率 −7 表示每單位時間減少7；100是初始值，負水量需由情境範圍排除。";
  lab.append(intro,modes,controls,canvas,table,feedback,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  render();
  return lab;
}

function mountPythagoreanGoldLab({ document, root, block }) {
  const store=storageFor(block.id),prior=store?.get()||{};
  const state={a:clamp(number(prior.a,6),3,9),b:clamp(number(prior.b,8),3,10),revealed:Boolean(prior.revealed)};
  const {lab,status}=makeLab(document,block,"畢氏定理：平方『面積』實驗室");
  lab.classList.add("math-gold-pythagorean-lab");
  const intro=document.createElement("p");intro.innerHTML="<strong>先找直角，再找兩股與斜邊。</strong> 定理連結的是三邊的平方，不是直接把兩股相加。";
  const predict=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="兩股6、8，斜邊？";predict.append(pl);
  const pf=document.createElement("p");pf.setAttribute("aria-live","polite");
  const canvas=makeCanvas(document,"直角三角形與三邊平方關係",360,260);
  const controls=document.createElement("div");controls.className="math-live-controls";controls.hidden=!state.revealed;
  const equation=document.createElement("p");equation.className="math-gold-equation";
  function draw(){
    canvas.replaceChildren();
    const x=45,y=210,scale=16,A=[x,y-state.b*scale],B=[x,y],C=[x+state.a*scale,y];
    canvas.append(svg(document,"polygon",{points:A[0]+","+A[1]+" "+B[0]+","+B[1]+" "+C[0]+","+C[1],fill:"none",stroke:"currentColor","stroke-width":3}));
    canvas.append(svg(document,"path",{d:"M"+x+" "+(y-18)+" L"+(x+18)+" "+(y-18)+" L"+(x+18)+" "+y,fill:"none",stroke:"currentColor","stroke-width":2}));
    const ta=svg(document,"text",{x:(B[0]+C[0])/2,y:y+24,"text-anchor":"middle",fill:"currentColor"});ta.textContent="a="+state.a;canvas.append(ta);
    const tb=svg(document,"text",{x:x-12,y:(A[1]+B[1])/2,"text-anchor":"end",fill:"currentColor"});tb.textContent="b="+state.b;canvas.append(tb);
    const c2=state.a*state.a+state.b*state.b,c=Math.sqrt(c2);
    if(state.revealed){
      [["a²",state.a*state.a,220,50],["b²",state.b*state.b,220,105],["c²",c2,220,160]].forEach(([label,value,rx,ry])=>{
        canvas.append(svg(document,"rect",{x:rx,y:ry,width:100,height:42,rx:8,fill:"none",stroke:"currentColor"}));
        const t=svg(document,"text",{x:rx+50,y:ry+26,"text-anchor":"middle",fill:"currentColor","font-weight":800});t.textContent=label+" = "+value;canvas.append(t);
      });
      equation.textContent=state.a+"² + "+state.b+"² = "+c2+" = c²；c=√"+c2+" ≈ "+c.toFixed(2);
      status.textContent="兩股平方和等於斜邊平方；長度取正平方根。";
    }else{
      const q=svg(document,"text",{x:270,y:110,"text-anchor":"middle",fill:"currentColor","font-weight":800});q.textContent="先預測平方關係";canvas.append(q);
      equation.textContent="";
      status.textContent="答案隱藏；先確認直角與三邊角色。";
    }
    store?.set(state);
  }
  goldButton(document,predict,"10",()=>{state.revealed=true;controls.hidden=false;pf.textContent="正確。36+64=100，所以斜邊取正平方根10。";draw();});
  goldButton(document,predict,"14",()=>{pf.textContent="這是6+8；畢氏定理連結的是平方。";});
  goldButton(document,predict,"√14",()=>{pf.textContent="先算6²+8²，而不是6+8。";});
  predict.append(pf);
  const ca=makeRange(document,{label:"股 a",min:3,max:9,value:state.a,onInput:v=>{state.a=v;draw();}});
  const cb=makeRange(document,{label:"股 b",min:3,max:10,value:state.b,onInput:v=>{state.b=v;draw();}});
  controls.append(ca.wrapper,cb.wrapper);
  const transfer=document.createElement("p");transfer.className="math-gold-transfer-note";transfer.textContent="反向遷移：斜邊13、一股5 → h²=13²−5²=144 → h=12；再以5²+12²=13²回查。";
  lab.append(intro,predict,canvas,controls,equation,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  draw();
  return lab;
}

function mountBoxPlotGoldLab({ document, root, block }) {
  const store=storageFor(block.id),prior=store?.get()||{};
  const state={maxA:clamp(number(prior.maxA,35),30,38),q3A:clamp(number(prior.q3A,26),25,29),revealed:Boolean(prior.revealed)};
  const {lab,status}=makeLab(document,block,"盒狀圖：鬚、盒子與散布量");
  lab.classList.add("math-gold-boxplot-lab");
  const intro=document.createElement("p");intro.innerHTML="<strong>只改一個位置。</strong> 最大值是鬚端；Q3是盒子端。先預測它們各自改變哪個散布量。";
  const predict=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="最大值30→35時？";predict.append(pl);
  const pf=document.createElement("p");pf.setAttribute("aria-live","polite");
  const canvas=makeCanvas(document,"甲乙兩站同尺度盒狀圖",360,220);
  const controls=document.createElement("div");controls.className="math-live-controls";controls.hidden=!state.revealed;
  const stats=document.createElement("div");stats.className="math-gold-stat-cards";
  const x=v=>32+(v-15)/25*292;
  const addPlot=(name,min,q1,med,q3,max,y)=>{
    canvas.append(svg(document,"line",{x1:x(min),y1:y,x2:x(max),y2:y,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:x(min),y1:y-12,x2:x(min),y2:y+12,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:x(max),y1:y-12,x2:x(max),y2:y+12,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"rect",{x:x(q1),y:y-22,width:x(q3)-x(q1),height:44,fill:"none",stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:x(med),y1:y-22,x2:x(med),y2:y+22,stroke:"currentColor","stroke-width":3}));
    const t=svg(document,"text",{x:10,y:y+5,fill:"currentColor"});t.textContent=name;canvas.append(t);
  };
  function draw(){
    canvas.replaceChildren();
    canvas.append(svg(document,"line",{x1:32,y1:190,x2:324,y2:190,stroke:"currentColor","stroke-width":2}));
    for(const v of [15,20,25,30,35,40]){const t=svg(document,"text",{x:x(v),y:211,"text-anchor":"middle",fill:"currentColor"});t.textContent=String(v);canvas.append(t);}
    addPlot("甲",18,22,24,state.q3A,state.maxA,70);addPlot("乙",20,23,24,25,29,140);
    const rA=state.maxA-18,iA=state.q3A-22;
    stats.innerHTML="<article><b>甲站</b><span>中位數24</span><span>全距 "+rA+"</span><span>IQR "+iA+"</span></article><article><b>乙站</b><span>中位數24</span><span>全距9</span><span>IQR2</span></article>";
    status.textContent="最大值控制鬚與全距；Q3控制盒子右端與IQR。";
    store?.set(state);
  }
  goldButton(document,predict,"全距變、IQR不變",()=>{state.revealed=true;controls.hidden=false;pf.textContent="正確。最大值只移動鬚端；Q1、Q3不動時IQR不變。";draw();});
  goldButton(document,predict,"全距與IQR都變",()=>{pf.textContent="IQR只看Q1到Q3；最大值不是IQR端點。";});
  predict.append(pf);
  const c1=makeRange(document,{label:"甲站最大值",min:30,max:38,value:state.maxA,onInput:v=>{state.maxA=v;draw();}});
  const c2=makeRange(document,{label:"甲站 Q3",min:25,max:29,value:state.q3A,onInput:v=>{state.q3A=v;draw();}});
  controls.append(c1.wrapper,c2.wrapper);
  const note=document.createElement("p");note.className="math-gold-transfer-note";note.textContent="結論邊界：IQR較小只表示中間50%較集中，不能說每一筆資料都更接近。";
  lab.append(intro,predict,pf,canvas,controls,stats,note);
  root.querySelector(".component-visual-body")?.prepend(lab);
  draw();
  return lab;
}

function mountProbabilityFrequencyGoldLab({ document, root, block }) {
  const store=storageFor(block.id),prior=store?.get()||{};
  const state={revealed:Boolean(prior.revealed),trials:number(prior.trials,10)};
  const data={10:[7,.70],20:[12,.60],50:[27,.54],100:[51,.51],200:[101,.505]};
  const {lab,status}=makeLab(document,block,"相對頻率：短期波動 × 長期趨勢");
  lab.classList.add("math-gold-probability-lab");
  const intro=document.createElement("p");intro.innerHTML="<strong>理論機率不是這一批資料。</strong> 10次有7次正面，先判斷是否足以證明硬幣不公平。";
  const predict=document.createElement("fieldset");const pl=document.createElement("legend");pl.textContent="7/10 代表一定不公平？";predict.append(pl);
  const pf=document.createElement("p");pf.setAttribute("aria-live","polite");
  const canvas=makeCanvas(document,"累積硬幣試驗相對頻率與理論0.5基準線",360,230);
  const trials=document.createElement("fieldset");trials.hidden=!state.revealed;const tl=document.createElement("legend");tl.textContent="查看累積試驗資料";trials.append(tl);
  const card=document.createElement("div");card.className="math-gold-prob-card";
  const fx=n=>48+(Math.log10(n)-1)/(Math.log10(200)-1)*260,fy=f=>190-(f-.4)/.35*140;
  function draw(){
    canvas.replaceChildren();
    canvas.append(svg(document,"line",{x1:42,y1:196,x2:326,y2:196,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:42,y1:28,x2:42,y2:196,stroke:"currentColor","stroke-width":2}));
    canvas.append(svg(document,"line",{x1:42,y1:fy(.5),x2:326,y2:fy(.5),stroke:"currentColor","stroke-width":1.5,"stroke-dasharray":"5 4"}));
    const pts=Object.entries(data).map(([n,v])=>[Number(n),v[1]]);
    canvas.append(svg(document,"polyline",{points:pts.map(p=>fx(p[0])+","+fy(p[1])).join(" "),fill:"none",stroke:"currentColor","stroke-width":3}));
    for(const [n,f] of pts){canvas.append(svg(document,"circle",{cx:fx(n),cy:fy(f),r:n===state.trials?7:4,fill:n===state.trials?"currentColor":"white",stroke:"currentColor","stroke-width":2}));}
    const [heads,freq]=data[state.trials];
    card.innerHTML="<b>"+state.trials+" 次</b><strong>"+heads+" 次正面</strong><span>相對頻率 "+heads+"/"+state.trials+" = "+freq.toFixed(3)+"</span><p>理論公平硬幣仍是0.5；觀察值可波動。</p>";
    status.textContent="試驗次數增加時這組資料逐漸靠近0.5；接近不等於每批必須剛好一半。";
    store?.set(state);
  }
  const reveal=ok=>{state.revealed=true;trials.hidden=false;store?.set(state);pf.textContent=ok?"正確。0.70是這批10次資料的相對頻率，不足以單獨證明理論機率改變。":"短期結果可能波動；要把理論0.5與觀察0.70分開。";draw();};
  goldButton(document,predict,"不能只靠10次斷定",()=>reveal(true));
  goldButton(document,predict,"一定不公平",()=>reveal(false));
  for(const n of [10,20,50,100,200]) goldButton(document,trials,n+"次",()=>{state.trials=n;draw();});
  const transfer=document.createElement("p");transfer.className="math-gold-transfer-note";transfer.textContent="遷移：P(紅)=1/4；48/200=0.24 接近0.25但不需相等，且下一次結果不被前面試驗強迫。";
  lab.append(intro,predict,pf,trials,canvas,card,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  draw();
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



function mountFactorMeaningLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={x:clamp(number(prior.x,2),1,5),choice:String(prior.choice||"")};
  const {lab,status}=makeLab(document,block,"因式 × 商式：乘回驗證臺");
  lab.classList.add("math-factor-meaning-lab");
  const intro=document.createElement("p");
  intro.innerHTML="<strong>因式是不是靠猜？不是。</strong> 把候選因式與商式完整相乘；能逐項還原原多項式，才算成立。";

  const figure=document.createElement("figure"); figure.className="math-factor-meaning-figure";
  const canvas=makeCanvas(document,"x加2乘以x加5的面積分割",420,300);
  const caption=document.createElement("figcaption");
  figure.append(canvas,caption);
  const control=makeRange(document,{label:"觀察 x",min:1,max:5,value:state.x,onInput:v=>{state.x=v;store?.set(state);draw();}});
  const candidates=document.createElement("fieldset");
  const legend=document.createElement("legend");legend.textContent="預測：哪一組乘回會得到 x²+7x+10？";candidates.append(legend);
  const feedback=document.createElement("p"); feedback.setAttribute("aria-live","polite");
  const evidence=document.createElement("div");evidence.className="math-factor-evidence";evidence.hidden=true;
  const defs=[
    ["good","(x+2)(x+5)","x²+7x+10",true],
    ["six","(x+1)(x+6)","x²+7x+6",false],
    ["twelve","(x+3)(x+4)","x²+7x+12",false],
  ];
  for(const [value,label,expanded,ok] of defs){
    const b=document.createElement("button");b.type="button";b.textContent=label;b.setAttribute("aria-pressed",String(state.choice===value));
    b.addEventListener("click",()=>{
      state.choice=value;store?.set(state);candidates.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
      evidence.hidden=false;
      if(ok){
        feedback.textContent="成立。四個乘積都能對回原式，常數項與中間項也完全一致。";
        evidence.innerHTML="<strong>完整乘回：</strong> x·x + x·5 + 2·x + 2·5 = x²+5x+2x+10 = x²+7x+10。";
      }else{
        feedback.textContent=\`不成立。中間項雖然也是 7x，但乘回得到 \${expanded}；只對到部分項不夠。\`;
        evidence.innerHTML=\`<strong>反證：</strong>\${label} = \${expanded} ≠ x²+7x+10。請逐項核對二次項、中間項、常數項。\`;
      }
    });
    candidates.append(b);
  }

  const transfer=document.createElement("fieldset");
  const tl=document.createElement("legend");tl.textContent="遷移：x²+8x+15 應由哪兩個一次式相乘？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["a","(x+3)(x+5)",true],["b","(x+1)(x+15)",false],["c","(x+2)(x+6)",false]].forEach(([v,label,ok])=>{
    const b=document.createElement("button");b.type="button";b.textContent=label;
    b.addEventListener("click",()=>{tf.textContent=ok?"正確。3×5=15，而且3+5=8；乘回得到 x²+8x+15。":"先完整乘回。常數乘積與交叉和要同時吻合。";});
    transfer.append(b);
  }); transfer.append(tf);

  function draw(){
    canvas.replaceChildren();
    const x=state.x, unit=28, ox=62, oy=44, xp=x*unit, two=56, five=92;
    const rect=(rx,ry,w,h,fill,label)=>{
      canvas.append(svg(document,"rect",{x:rx,y:ry,width:w,height:h,fill,stroke:"#334155","stroke-width":1.7}));
      const t=svg(document,"text",{x:rx+w/2,y:ry+h/2+6,"text-anchor":"middle","font-size":17,"font-weight":800,fill:"#0f172a"});t.textContent=label;canvas.append(t);
    };
    rect(ox,oy,xp,xp,"#dbeafe","x²");
    rect(ox+xp,oy,five,xp,"#fef3c7","5x");
    rect(ox,oy+xp,xp,two,"#dcfce7","2x");
    rect(ox+xp,oy+xp,five,two,"#ede9fe","10");
    const top=svg(document,"text",{x:ox+(xp+five)/2,y:25,"text-anchor":"middle","font-weight":800});top.textContent="x + 5";canvas.append(top);
    const side=svg(document,"text",{x:22,y:oy+(xp+two)/2,"text-anchor":"middle","font-weight":800,transform:\`rotate(-90 22 \${oy+(xp+two)/2})\`});side.textContent="x + 2";canvas.append(side);
    caption.textContent=\`x=\${x} 時，長 \${x+5}、寬 \${x+2}，面積 \${(x+5)*(x+2)}；圖形仍對應 x²+7x+10。\`;
  }

  lab.append(intro,figure,control.wrapper,candidates,feedback,evidence,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  draw();
  status.textContent="先提出候選，再用四個乘積完整乘回；部分項吻合不能當證明。";
  return lab;
}

function mountFactorizationLab({ document, root, block, spec }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const broad=spec?.lessonId==="cur-math-content-a-8-5";
  if (!broad) return mountFactorMeaningLab({ document, root, block, spec });
  const state={choice:String(prior.choice||""),transfer:String(prior.transfer||"")};
  const {lab,status}=makeLab(document,block,broad?"因式分解結構探索臺":"因式與乘回驗證臺");
  lab.classList.add("math-factor-lab");
  const intro=document.createElement("p");
  intro.innerHTML="<strong>先找兩項真正共有的材料。</strong> 因式分解不是在式子外面硬加括號，而是把乘法結構找回來。";
  const board=document.createElement("div"); board.className="math-factor-board";
  const row=(title,tokens,common)=>{
    const r=document.createElement("div");r.className="math-factor-row";
    const h=document.createElement("strong");h.textContent=title;
    const ts=document.createElement("div");ts.className="math-factor-tokens";
    tokens.forEach((t,i)=>{const n=document.createElement("span");n.textContent=t;n.className="math-factor-token"+(common.includes(i)?" is-common":"");ts.append(n);});
    r.append(h,ts);return r;
  };
  board.append(row("12x²",["2","2","3","x","x"],[0,2,3]),row("18x",["2","3","3","x"],[0,1,3]));
  const common=document.createElement("p");common.className="math-factor-common";common.innerHTML="兩列共同：<strong>2 × 3 × x = 6x</strong>";board.append(common);
  const question=document.createElement("fieldset");const legend=document.createElement("legend");legend.textContent="預測：最大共同因式是什麼？";question.append(legend);
  const feedback=document.createElement("p");feedback.setAttribute("aria-live","polite");
  const evidence=document.createElement("div");evidence.className="math-factor-evidence";evidence.hidden=true;
  const choices=[["6","6"],["6x","6x"],["12x","12x"]];
  for(const [v,label] of choices){const b=document.createElement("button");b.type="button";b.textContent=label;b.setAttribute("aria-pressed",String(state.choice===v));b.addEventListener("click",()=>{
    state.choice=v;store?.set(state);question.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
    evidence.hidden=false;
    if(v==="6x"){feedback.textContent="正確。數字共同 2×3，字母共同至少一個 x，所以最大共同因式是 6x。";evidence.innerHTML="<strong>逐項相除：</strong> 12x²÷6x=2x；18x÷6x=3。<br><strong>乘回：</strong>6x(2x+3)=12x²+18x。";}
    else if(v==="6"){feedback.textContent="6 可以提出，但還漏掉兩項共同的 x。看兩列 token，x 也各至少出現一次。";evidence.textContent="候選 6 不是最大共同因式；提出後仍有共同 x。";}
    else {feedback.textContent="12x 不能整除 18x 成整式係數。候選因式必須能逐項相除。";evidence.textContent="用逐項相除檢查候選，比看外觀可靠。";}
  });question.append(b);}
  const method=document.createElement("section");method.className="math-factor-method";
  if(broad){
    const h=document.createElement("h5");h.textContent="第二層：提出共同因式後，再看剩式";
    const grid=document.createElement("div");grid.className="math-factor-method-grid";
    [["共同因式","先提出，再看括號內是否還能分解。"],["平方差","A²−B² 才能變成 (A−B)(A+B)。"],["三項式","同時檢查乘積與交叉和，最後乘回。"]].forEach(([a,b])=>{const x=document.createElement("article");x.innerHTML=\`<strong>\${a}</strong><p>\${b}</p>\`;grid.append(x);});
    method.append(h,grid);
  }
  const transfer=document.createElement("fieldset");const tl=document.createElement("legend");tl.textContent="遷移：15x²y−10xy² 的最大共同因式？";transfer.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["5","5"],["5x","5x"],["5xy","5xy"]].forEach(([v,label])=>{const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",()=>{state.transfer=v;store?.set(state);tf.textContent=v==="5xy"?"正確。係數共同 5，x、y 都取共同最低次方 1，所以 15x²y−10xy²=5xy(3x−2y)。":"再把係數、x、y 分三欄比較；每一欄都要取兩項共有的部分。";});transfer.append(b);});
  transfer.append(tf);
  lab.append(intro,board,question,feedback,evidence,method,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  status.textContent="用共同 token → 逐項相除 → 完整乘回，三層證據確認因式。";
  return lab;
}


function mountPolynomialOpsLab({ document, root, block }) {
  const store=storageFor(block.id), prior=store?.get()||{};
  const state={mode:String(prior.mode||"subtract")};
  const {lab,status}=makeLab(document,block,"多項式三站視覺工作台");
  lab.classList.add("math-poly-lab");

  const intro=document.createElement("p");
  intro.innerHTML="<strong>一次只做一件事：</strong>先預測，再看中間結構。減法看變號、乘法看完整配對、除法看重組。";

  const modes=document.createElement("fieldset");
  const modeLegend=document.createElement("legend"); modeLegend.textContent="選擇運算工作台"; modes.append(modeLegend);
  const visual=document.createElement("section"); visual.className="math-poly-visual";
  const prediction=document.createElement("fieldset"); prediction.className="math-poly-prediction";
  const feedback=document.createElement("p"); feedback.className="math-poly-feedback"; feedback.setAttribute("aria-live","polite");
  const evidence=document.createElement("div"); evidence.className="math-poly-evidence"; evidence.hidden=true;

  const setMode=value=>{
    state.mode=value; store?.set(state);
    modes.querySelectorAll("button").forEach(b=>b.setAttribute("aria-pressed",String(b.dataset.mode===value)));
    renderMode();
  };
  [["subtract","括號減法"],["multiply","多項式乘法"],["divide","多項式除法"]].forEach(([value,label])=>{
    const b=document.createElement("button"); b.type="button"; b.dataset.mode=value; b.textContent=label;
    b.addEventListener("click",()=>setMode(value)); modes.append(b);
  });

  const term=(text,kind="")=>{
    const s=document.createElement("span"); s.className="math-poly-term"+(kind?" "+kind:""); s.textContent=text; return s;
  };
  const equationLine=(parts,klass="")=>{
    const d=document.createElement("div"); d.className="math-poly-equation"+(klass?" "+klass:"");
    parts.forEach(p=>d.append(typeof p==="string"?document.createTextNode(p):p)); return d;
  };
  const addChoice=(parent,label,onPick)=>{
    const b=document.createElement("button"); b.type="button"; b.textContent=label; b.addEventListener("click",onPick); parent.append(b);
  };
  const reveal=(message,html)=>{
    feedback.textContent=message; evidence.hidden=false; evidence.innerHTML=html;
  };

  function renderMode(){
    visual.replaceChildren(); prediction.replaceChildren(); evidence.hidden=true; evidence.replaceChildren(); feedback.textContent="";
    const lg=document.createElement("legend"); prediction.append(lg);
    if(state.mode==="subtract"){
      visual.setAttribute("role","img");
      visual.setAttribute("aria-label","五 x 平方減去括號二 x 平方減三 x 加一的逐項變號模型");
      const note=document.createElement("p"); note.textContent="括號前的 − 會作用到括號內每一項。";
      visual.append(equationLine([term("5x²")," − ",term("2x² − 3x + 1","is-bracket")]),note);
      lg.textContent="預測：打開括號時，哪幾項要變號？";
      addChoice(prediction,"三項全部變號",()=>{
        visual.append(equationLine([term("5x²"),term("−2x²"),term("+3x"),term("−1")],"is-result"));
        reveal("正確。−1 分配到三項，連常數 +1 也要變成 −1。","<strong>合併：</strong>3x²+3x−1。<br><strong>x=1 驗算：</strong>原式與整理式都等於 5。");
      });
      addChoice(prediction,"只改第一項",()=>reveal("還少兩個符號變化。負號作用的是整個括號。","請逐項寫成 (−1)·2x²、(−1)·(−3x)、(−1)·(+1)。"));
      addChoice(prediction,"都不變",()=>reveal("括號前是減號，不可能直接把括號拿掉而保持三項符號。","把「−(…)」改寫成「+(−1)(…)」再看一次。"));
      status.textContent="減法站：證據是每一項的符號變化，不是只看最後答案。";
    } else if(state.mode==="multiply"){
      visual.setAttribute("role","img");
      visual.setAttribute("aria-label","二 x 減一乘 x 加三的二乘二四格乘積模型");
      const grid=document.createElement("div"); grid.className="math-poly-grid";
      ["","x","+3","2x","？","？","−1","？","？"].forEach((v,i)=>{
        const n=document.createElement(i===1||i===2||i===3||i===6?"strong":"span"); n.textContent=v; grid.append(n);
      });
      visual.append(grid);
      lg.textContent="預測：兩個二項式共有幾個項對項乘積？";
      addChoice(prediction,"4 個",()=>{
        const all=grid.children;
        ["","x","+3","2x","2x²","+6x","−1","−x","−3"].forEach((v,i)=>{all[i].textContent=v;});
        reveal("正確。2×2 共有四格，填完才能合併同類項。","<strong>(2x−1)(x+3)</strong> = 2x²+6x−x−3 = <strong>2x²+5x−3</strong>。x=2 時前後都等於 15。");
      });
      addChoice(prediction,"2 個，只乘首尾",()=>reveal("這會漏掉兩個交叉乘積。","左邊 2 項，每一項都要和右邊 2 項相乘，所以是 2×2=4 格。"));
      addChoice(prediction,"3 個",()=>reveal("仍會漏一格。","先不要合併；把四個配對 2x·x、2x·3、(−1)·x、(−1)·3 全部列出。"));
      status.textContent="乘法站：先完成四格配對，再合併同類項。";
    } else {
      visual.setAttribute("role","img");
      visual.setAttribute("aria-label","二 x 平方加三 x 減六等於 x 加三乘二 x 減三再加餘式的重組模型");
      visual.append(equationLine([term("2x²+3x−6")," = ",term("(x+3)(2x−3)")," + ",term("？","is-remainder")]));
      lg.textContent="預測：餘式是多少，才能完整重組被除式？";
      addChoice(prediction,"0",()=>reveal("少了 3。商乘除式只得到 2x²+3x−9。","把 2x²+3x−9 和原式 2x²+3x−6 比較，常數差 3。"));
      addChoice(prediction,"3",()=>{
        visual.replaceChildren(equationLine([term("2x²+3x−6")," = ",term("(x+3)(2x−3)")," + ",term("3","is-remainder")]));
        reveal("正確。除式×商＋餘式完整回到被除式。","<strong>(x+3)(2x−3)+3</strong> = 2x²+3x−9+3 = <strong>2x²+3x−6</strong>。");
      });
      addChoice(prediction,"−3",()=>reveal("方向相反；再看常數從 −9 要走到 −6。","−9 加 3 才是 −6，所以餘式應為 +3。"));
      status.textContent="除法站：商不是終點；必須用除式×商＋餘式重組原式。";
    }
  }

  const transfer=document.createElement("fieldset"); transfer.className="math-poly-transfer";
  const tl=document.createElement("legend"); tl.textContent="遷移：長 (x+5)、寬 (x−2) 的長方形面積"; transfer.append(tl);
  const tf=document.createElement("p"); tf.setAttribute("aria-live","polite");
  [["x²+3x−10",true],["x²+7x−10",false],["x²+3x+10",false]].forEach(([label,ok])=>{
    addChoice(transfer,label,()=>{tf.textContent=ok?"正確。四格是 x²、−2x、5x、−10，合併為 x²+3x−10；x=3 時兩種表示都等於 8。":"先保留四個乘積；特別檢查 x·(−2) 與 5·x 的符號，以及 5·(−2) 的常數。";});
  });
  transfer.append(tf);

  lab.append(intro,modes,visual,prediction,feedback,evidence,transfer);
  root.querySelector(".component-visual-body")?.prepend(lab);
  setMode(state.mode);
  return lab;
}

function mountStepwiseLab({ document, root, block, spec }) {
  if (spec?.lessonId === "cur-math-content-a-8-3") return mountPolynomialOpsLab({ document, root, block, spec });
  if (spec?.lessonId === "cur-math-content-a-8-4" || spec?.lessonId === "cur-math-content-a-8-5") return mountFactorizationLab({ document, root, block, spec });
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





function mountPolygonSimilarityVisualLab({document,root,block}){
 const {lab,status}=makeLab(document,block,"相似形縮放圖解臺");let k=1.5;const c=makeCanvas(document,"同形狀多邊形以統一倍率縮放",420,260);
 const draw=()=>{c.replaceChildren();const base=[[40,190],[75,70],[145,55],[180,170],[120,215]],center=[110,135];const scaled=base.map(([x,y])=>[245+(x-center[0])*k*.65,135+(y-center[1])*k*.65]);[base,scaled].forEach((pts,i)=>{c.append(svg(document,"polygon",{points:pts.map(p=>p.join(",")).join(" "),fill:"none",stroke:"currentColor","stroke-width":3}));pts.forEach((p,j)=>{const t=svg(document,"text",{x:p[0]+4,y:p[1]-5,"font-size":12});t.textContent=(i?"A′B′C′D′E′":"ABCDE")[j];c.append(t);});});status.textContent=`右圖以統一倍率約 ${k.toFixed(1)}× 縮放；角度保持、所有對應邊使用同一倍率，才是相似。`;};
 const ctl=makeRange(document,{label:"縮放倍率",min:.5,max:2,step:.25,value:k,onInput:v=>{k=v;draw();}});const p=document.createElement("p");p.innerHTML="<strong>不是「看起來像」就算相似。</strong> 逐頂點配對後，同時檢查角度保持與每一條對應邊的倍率。";lab.append(c,ctl.wrapper,p);root.querySelector(".component-visual-body")?.prepend(lab);draw();return lab;
}
function mountSectorVisualLab({document,root,block}){
 const {lab,status}=makeLab(document,block,"扇形：角度占整圓多少？");let r=5,theta=90;const c=makeCanvas(document,"圓心角、弧與扇形面積同步圖",360,270);
 const controls=document.createElement("div");controls.className="math-live-controls";
 const draw=()=>{c.replaceChildren();const cx=180,cy=140,R=r*18,a=(theta-90)*Math.PI/180,x=cx+R*Math.cos(a),y=cy+R*Math.sin(a);c.append(svg(document,"circle",{cx,cy,r:R,fill:"none",stroke:"currentColor","stroke-width":2}));c.append(svg(document,"path",{d:`M ${cx} ${cy} L ${cx} ${cy-R} A ${R} ${R} 0 ${theta>180?1:0} 1 ${x} ${y} Z`,fill:"currentColor",opacity:.14,stroke:"currentColor","stroke-width":2}));status.textContent=`θ=${theta}° = ${(theta/360).toFixed(2)} 圈；弧長≈${(2*Math.PI*r*theta/360).toFixed(2)}，扇形面積≈${(Math.PI*r*r*theta/360).toFixed(2)}。`;};
 const rr=makeRange(document,{label:"半徑 r",min:2,max:7,value:r,onInput:v=>{r=v;draw();}}),aa=makeRange(document,{label:"圓心角 θ",min:30,max:300,step:30,value:theta,onInput:v=>{theta=v;draw();}});controls.append(rr.wrapper,aa.wrapper);
 const note=document.createElement("p");note.innerHTML="<strong>同一個比例 θ/360 同時控制弧長與扇形面積。</strong> 弧是曲線，不是兩端點之間的弦。";lab.append(c,controls,note);root.querySelector(".component-visual-body")?.prepend(lab);draw();return lab;
}
function mountCirclePropertyVisualLab({document,root,block}){
 const {lab,status}=makeLab(document,block,"圓的元素辨識圖");const c=makeCanvas(document,"圓心、半徑、直徑、弦與切線",400,260),cx=190,cy=130,R=90;c.append(svg(document,"circle",{cx,cy,r:R,fill:"none",stroke:"currentColor","stroke-width":3}));
 const lines=[["半徑",cx,cy,cx+R,cy],["直徑",cx-R,cy,cx+R,cy],["弦",cx-70,cy-55,cx+55,cy-70],["切線",cx+R,30,cx+R,230]];lines.forEach(([name,x1,y1,x2,y2],i)=>{c.append(svg(document,"line",{x1,y1,x2,y2,stroke:"currentColor","stroke-width":i===3?4:2,"stroke-dasharray":i===3?"7 4":""}));const t=svg(document,"text",{x:(x1+x2)/2+6,y:(y1+y2)/2-7,"font-size":14,"font-weight":800});t.textContent=name;c.append(t);});
 const q=document.createElement("p");q.innerHTML="<strong>判讀順序：</strong>是否經圓心？端點是否都在圓上？是否只碰圓一點？三個問題就能拆開直徑、弦與切線。";lab.append(c,q);root.querySelector(".component-visual-body")?.prepend(lab);status.textContent="切線在切點與半徑垂直；直徑是通過圓心的特殊弦。";return lab;
}
function mountLineCircleRelationVisualLab({document,root,block}){
 const {lab,status}=makeLab(document,block,"直線與圓：先看圓心到直線的最短距離");let d=4,r=4;const c=makeCanvas(document,"圓與直線交點隨圓心距離變化",400,250);const draw=()=>{c.replaceChildren();const R=r*20,y=190-d*20;c.append(svg(document,"line",{x1:25,y1:190,x2:375,y2:190,stroke:"currentColor","stroke-width":3}));c.append(svg(document,"circle",{cx:200,cy:y,r:R,fill:"none",stroke:"currentColor","stroke-width":3}));c.append(svg(document,"line",{x1:200,y1:y,x2:200,y2:190,stroke:"currentColor","stroke-dasharray":"5 4"}));const rel=d<r?"相交：2 個交點":d===r?"相切：1 個交點":"相離：0 個交點";status.textContent=`OH=${d}, r=${r} → ${rel}。比較的是垂直最短距離 OH，不是任意斜線。`;};const cs=document.createElement("div");cs.className="math-live-controls";const a=makeRange(document,{label:"OH",min:1,max:7,value:d,onInput:v=>{d=v;draw();}}),b=makeRange(document,{label:"半徑 r",min:2,max:6,value:r,onInput:v=>{r=v;draw();}});cs.append(a.wrapper,b.wrapper);lab.append(c,cs);root.querySelector(".component-visual-body")?.prepend(lab);draw();return lab;
}
function mountCircumcenterVisualLab({document,root,block}){
 const {lab,status}=makeLab(document,block,"外心：三個頂點的等距中心");const c=makeCanvas(document,"三角形外接圓與兩條邊的垂直平分線",400,290);const O=[200,145],R=100,pts=[[200,45],[110,190],[290,190]];c.append(svg(document,"circle",{cx:O[0],cy:O[1],r:R,fill:"none",stroke:"currentColor","stroke-width":2}));c.append(svg(document,"polygon",{points:pts.map(p=>p.join(",")).join(" "),fill:"none",stroke:"currentColor","stroke-width":3}));[[200,20,200,270],[40,117.5,360,117.5]].forEach(v=>c.append(svg(document,"line",{x1:v[0],y1:v[1],x2:v[2],y2:v[3],stroke:"currentColor","stroke-dasharray":"6 5"})));c.append(svg(document,"circle",{cx:O[0],cy:O[1],r:5,fill:"currentColor"}));const t=svg(document,"text",{x:210,y:140,"font-weight":800});t.textContent="O 外心";c.append(t);const p=document.createElement("p");p.textContent="垂直平分線上的點到該邊兩端等距；兩條垂直平分線交於 O，因此 OA=OB=OC。";lab.append(c,p);root.querySelector(".component-visual-body")?.prepend(lab);status.textContent="外心不是靠目測找三角形中央，而是由「等距」條件找出。";return lab;
}
function mountSimilarityEvidenceVisualLab({ document, root, block }) {
  const {lab,status}=makeLab(document,block,"相似三角形證據圖解臺");
  const intro=document.createElement("p");intro.innerHTML="<strong>先看證據落在圖上的位置。</strong> 不先背 AA／SAS／SSS；先確認哪些角、哪些邊真的互相對應。";
  const figure=document.createElement("figure");const c=makeCanvas(document,"兩個相似三角形的對應頂點與邊",420,250);
  const tri=(pts,labels)=>{c.append(svg(document,"polygon",{points:pts.map(p=>p.slice(0,2).join(",")).join(" "),fill:"none",stroke:"currentColor","stroke-width":3}));pts.forEach((p,i)=>{const t=svg(document,"text",{x:p[0]+labels[i][1],y:p[1]+labels[i][2],"font-weight":800,"font-size":18});t.textContent=labels[i][0];c.append(t);});};
  tri([[35,205],[120,45],[190,205]],[["A",-20,22],["B",-5,-10],["C",6,22]]);
  tri([[235,205],[320,45],[390,205]],[["D",-20,22],["E",-5,-10],["F",6,22]]);
  const arrows=[["A ↔ D",112],["B ↔ E",137],["C ↔ F",162]];arrows.forEach(([v,y])=>{const t=svg(document,"text",{x:210,y,"text-anchor":"middle","font-size":14,"font-weight":800});t.textContent=v;c.append(t);});
  const cap=document.createElement("figcaption");cap.textContent="頂點順序一旦確定：△ABC ∼ △DEF，就固定 AB↔DE、BC↔EF、CA↔FD。";figure.append(c,cap);
  const q=document.createElement("fieldset");const l=document.createElement("legend");l.textContent="哪一張證據卡足以判定？";q.append(l);const fb=document.createElement("p");fb.setAttribute("aria-live","polite");
  [["AA：A=D、B=E",true,"兩組角相等，第三組角也隨內角和固定。"],["只有 A=D",false,"只有一組角，仍可畫出很多不同形狀。"],["兩邊同比但角不是夾角",false,"不能直接叫 SAS；相等角必須是兩組比例邊的夾角。"]].forEach(([label,ok,msg])=>{const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",()=>{fb.textContent=(ok?"成立：":"資料不足：")+msg;});q.append(b);});q.append(fb);
  const ratio=document.createElement("div");ratio.className="math-factor-evidence";ratio.innerHTML="<strong>對應一條線：</strong><br>AB / DE = BC / EF = CA / FD<br>比例方向可以反過來，但三組必須一起反。";
  lab.append(intro,figure,q,ratio);root.querySelector(".component-visual-body")?.prepend(lab);status.textContent="證據位置 → 頂點對應 → 判定法 → 同向比例。";return lab;
}

function mountRightTriangleRatioVisualLab({ document, root, block }) {
  const {lab,status}=makeLab(document,block,"同角直角三角形比值實驗");
  const intro=document.createElement("p");intro.innerHTML="<strong>固定角度、改變大小。</strong> 圖形會放大，但高／底的比值不變；改變角度後，比值才跟著改。";
  const c=makeCanvas(document,"同一銳角下兩個不同大小直角三角形",420,250);const fig=document.createElement("figure");fig.append(c);
  const controls=document.createElement("div");controls.className="math-live-controls";let scale=2.5,angle=22;
  const draw=()=>{c.replaceChildren();const rad=angle*Math.PI/180;const b1=110,h1=b1*Math.tan(rad),b2=b1*scale,h2=h1*scale;const y=210;
    [[35,b1,h1],[35,b2,h2]].forEach(([x,b,h],i)=>{const off=i?150:0;c.append(svg(document,"polygon",{points:`${x+off},${y} ${x+off+b},${y} ${x+off+b},${y-h}`,fill:"none",stroke:"currentColor","stroke-width":3}));});
    status.textContent=`角度 ${angle}°：小圖高/底=${Math.tan(rad).toFixed(3)}；大圖高/底=${(h2/b2).toFixed(3)}。倍率 ${scale.toFixed(1)} 不改變比值。`;};
  const sc=makeRange(document,{label:"整體放大倍率",min:1,max:2.5,step:.5,value:scale,onInput:v=>{scale=v;draw();}});
  const an=makeRange(document,{label:"銳角",min:15,max:40,step:1,value:angle,onInput:v=>{angle=v;draw();}});controls.append(sc.wrapper,an.wrapper);
  const note=document.createElement("p");note.textContent="觀察：只拉放大倍率時兩個比值相同；拉角度時兩個比值會一起改變。";
  lab.append(intro,fig,controls,note);root.querySelector(".component-visual-body")?.prepend(lab);draw();return lab;
}

function mountParallelProportionVisualLab({ document, root, block }) {
  const { lab, status } = makeLab(document, block, "平行線比例圖解工作台");
  lab.classList.add("math-parallel-proportion-lab");
  const intro=document.createElement("p");
  intro.innerHTML="<strong>先看圖，再列比例。</strong> 點選線段類型，圖上會直接標出哪些線段必須成對。";

  const figure=document.createElement("figure");
  const canvas=svg(document,"svg",{viewBox:"0 0 420 300",role:"img","aria-label":"三角形 ABC 中 D 在 AB、E 在 AC，DE 平行 BC；AD 6、DB 4、AE 7.5、EC 5"});
  canvas.classList.add("math-live-canvas");
  const line=(x1,y1,x2,y2,klass="")=>canvas.append(svg(document,"line",{x1,y1,x2,y2,class:klass,stroke:"currentColor","stroke-width":3}));
  line(210,25,55,265); line(210,25,365,265); line(55,265,365,265);
  line(132,145,288,145,"parallel-cut");
  const points=[["A",210,20],["B",45,282],["C",370,282],["D",120,145],["E",296,145]];
  for(const [t,x,y] of points){const n=svg(document,"text",{x,y,"font-size":18,"font-weight":800});n.textContent=t;canvas.append(n);}
  const labels=[["6",158,88,"seg-ad"],["4",88,214,"seg-db"],["7.5",255,88,"seg-ae"],["5",330,214,"seg-ec"]];
  for(const [t,x,y,k] of labels){const n=svg(document,"text",{x,y,class:k,"font-size":17,"font-weight":800});n.textContent=t;canvas.append(n);}
  const parallel=svg(document,"text",{x:210,y:135,"text-anchor":"middle","font-size":14});parallel.textContent="DE ∥ BC";canvas.append(parallel);
  const cap=document.createElement("figcaption");cap.textContent="同一側的相鄰分段要對到另一側相同位置：AD ↔ AE、DB ↔ EC。";
  figure.append(canvas,cap);

  const chooser=document.createElement("fieldset"); const lg=document.createElement("legend");lg.textContent="你現在比較哪一種線段？";chooser.append(lg);
  const evidence=document.createElement("div");evidence.className="math-factor-evidence";
  const feedback=document.createElement("p");feedback.setAttribute("aria-live","polite");
  const show=(kind)=>{
    if(kind==="parts"){
      evidence.innerHTML="<strong>相鄰分段 ↔ 相鄰分段</strong><br>AD / DB = AE / EC<br>6 / 4 = 7.5 / EC → EC = 5";
      feedback.textContent="正確配對：左右兩側都採「靠近 A 的分段／遠離 A 的分段」。";
    } else {
      evidence.innerHTML="<strong>從頂點起的整段 ↔ 從頂點起的整段</strong><br>AD / AB = AE / AC<br>6 / 10 = 7.5 / 12.5 = 0.6";
      feedback.textContent="整段必須先相加：AB=6+4，AC=7.5+5。";
    }
  };
  [["parts","看相鄰分段"],["whole","看整段倍率"]].forEach(([v,label])=>{const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",()=>show(v));chooser.append(b);});

  const trap=document.createElement("fieldset");const tl=document.createElement("legend");tl.textContent="哪個比例把分段和整段混在一起？";trap.append(tl);
  const tf=document.createElement("p");tf.setAttribute("aria-live","polite");
  [["4 / 3 = 8 / AC",true],["4 / 3 = 8 / EC",false],["4 / 7 = 8 / AC",false]].forEach(([label,bad])=>{const b=document.createElement("button");b.type="button";b.textContent=label;b.addEventListener("click",()=>{tf.textContent=bad?"抓到了：左邊是分段／分段，右邊卻是分段／整段。":"這組可以維持相同邊界；再檢查方向與平行條件。";});trap.append(b);});trap.append(tf);

  lab.append(intro,figure,chooser,evidence,feedback,trap);
  root.querySelector(".component-visual-body")?.prepend(lab);
  show("parts");
  status.textContent="圖 → 線段類型 → 對應方向 → 比例；不要先把數字塞進公式。";
  return lab;
}

export function enhanceMathInteractiveBlock({ document, root, spec, block }) {
  if (!document || !root || !block || spec?.subject !== "math" || !SUPPORTED.has(block.component)) return null;
  if (root.querySelector(".math-live-lab")) return root.querySelector(".math-live-lab");
  if (spec?.lessonId === "cur-math-content-n-7-3") return mountSignedOperationsGoldLab({ document, root, block, spec });
  if (spec?.lessonId === "cur-math-content-f-8-2") return mountLinearParameterGoldLab({ document, root, block, spec });
  if (spec?.lessonId === "cur-math-content-s-9-3") return mountParallelProportionVisualLab({ document, root, block, spec });\n  if (spec?.lessonId === "cur-math-content-s-8-6") return mountPythagoreanGoldLab({ document, root, block, spec });
  if (spec?.lessonId === "cur-math-content-d-9-1") return mountBoxPlotGoldLab({ document, root, block, spec });
  if (spec?.lessonId === "cur-math-content-d-9-2") return mountProbabilityFrequencyGoldLab({ document, root, block, spec });
  if (block.component === "FunctionRepresentationBlock") return mountFunctionLab({ document, root, block, spec });
  if (block.component === "GeometryManipulationBlock") return mountGeometryLab({ document, root, block, spec });
  if (block.component === "AlgebraBalanceBlock" && spec?.lessonId === "cur-math-linear-equation-check") return mountLinearEquationCheckLab({ document, root, block, spec });
  if (block.component === "AlgebraBalanceBlock" || block.component === "AlgebraEquationMeaningBlock") return mountBalanceLab({ document, root, block, spec });
  if (block.component === "SystemIntersectionBlock") return mountSystemIntersectionLab({ document, root, block, spec });
  if (block.component === "SystemEliminationBlock") return mountSystemEliminationLab({ document, root, block, spec });
  if (block.component === "QuadraticMeaningBlock") return mountQuadraticMeaningLab({ document, root, block, spec });
  if (block.component === "QuadraticSolutionBlock") return mountQuadraticSolutionLab({ document, root, block, spec });
  if (block.component === "EquivalentExpressionCheckBlock") return mountEquivalentLab({ document, root, block, spec });
  if (block.component === "NumberLineBlock") return mountNumberLineLab({ document, root, block, spec });
  if (block.component === "ProbabilityExperimentBlock") return mountProbabilityFrequencyGoldLab({ document, root, block, spec });
  if (block.component === "StepwiseReasoningBlock") return mountStepwiseLab({ document, root, block, spec });
  return null;
}

export const MATH_LIVE_COMPONENTS = Object.freeze([...SUPPORTED]);

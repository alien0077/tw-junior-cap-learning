/* Data-driven, dependency-free learning simulations for math and science. */
(() => {
  const storagePrefix = "tw-junior-cap-learning/simulation/v1/";
  const lessons = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
  const clamp = (value, min, max) => Math.max(min, Math.min(max, Number(value)));
  const stateKey = id => storagePrefix + id;
  const defaults = engine => ({
    "math-number-line": { n: 0 },
    "math-algebra-balance": { addend: 3, target: 11 },
    "math-function-graph": { m: 1, b: 0, x: 2 },
    "math-geometry": { base: 6, height: 4 },
    "math-data-lab": { a: 4, b: 7, c: 10 },
    "math-probability-lab": { trials: 20, hits: 0 },
    "science-motion-lab": { force: 12, mass: 3, friction: 3 },
    "science-energy-lab": { power: 12, time: 4, loss: 20 },
    "science-particle-lab": { temperature: 50, spacing: 4 },
    "science-life-system": { rate: 60, demand: 50 },
    "science-earth-space": { tilt: 23.5, position: 0 },
    "concept-explorer": { evidence: 1 },
  }[engine] || {});
  const read = simulation => {
    try { return { ...defaults(simulation.engine), ...JSON.parse(localStorage.getItem(stateKey(simulation.id)) || "{}") }; }
    catch { return defaults(simulation.engine); }
  };
  const write = (simulation, state) => localStorage.setItem(stateKey(simulation.id), JSON.stringify(state));
  const label = engine => ({
    "math-number-line": "數線操作臺", "math-algebra-balance": "代數天平", "math-function-graph": "函數圖形實驗室",
    "math-geometry": "幾何建構臺", "math-data-lab": "資料實驗室", "math-probability-lab": "機率試驗器",
    "science-motion-lab": "力與運動實驗室", "science-energy-lab": "能量實驗室", "science-particle-lab": "粒子模型實驗室",
    "science-life-system": "生命系統模型", "science-earth-space": "地球與太空模型", "concept-explorer": "概念探索工作臺",
  }[engine] || "互動模型");
  const slider = (key, text, value, min, max, step = 1, unit = "") => `<label class="sim-control"><span>${esc(text)} <output data-sim-output="${key}">${value}${unit}</output></span><input data-sim-control="${key}" type="range" min="${min}" max="${max}" step="${step}" value="${value}" aria-label="${esc(text)}"></label>`;
  const graphPoint = (x, y) => `${180 + x * 28},${130 - y * 20}`;
  const renderLearningDesign = (lesson, state) => {
    const design = lesson.simulation?.learningDesign;
    if (!design) return "";
    const current = Math.max(0, Math.min(design.steps.length - 1, Number(state.designStep || 0)));
    const step = design.steps[current];
    const visualLabel = design.type === "equation-transform" ? "目前表示" : "目前探索結果";
    return `<div class="sim-design" data-design-type="${esc(design.type)}"><p><b>先預測：</b>${esc(design.predictionPrompt)}</p><div class="sim-equation-path" aria-live="polite"><div class="sim-equation-current">${esc(step.equation)}</div><p><b>${visualLabel}：</b>${esc(step.action)}</p><p>${esc(step.reason)}</p></div><div class="sim-design-steps" role="list" aria-label="單元探索步驟">${design.steps.map((item, index) => `<button type="button" data-design-step="${index}" ${index === current ? 'aria-current="step"' : ""}>${index + 1}. ${esc(item.action)}</button>`).join("")}</div><p class="sim-design-feedback" aria-live="polite">${esc(step.feedback)}</p><p><b>用證據說明：</b>${esc(design.evidencePrompt)}</p></div>`;
  };
  const renderModel = (lesson, state) => {
    const { engine } = lesson.simulation;
    const designed = renderLearningDesign(lesson, state);
    if (designed) return designed;
    if (engine === "math-number-line") {
      const n = state.n;
      return `<div class="sim-stage"><svg viewBox="0 0 360 150" role="img" aria-label="數線上目前的值是 ${n}"><line x1="24" y1="76" x2="336" y2="76" class="sim-axis"/>${[-5,-4,-3,-2,-1,0,1,2,3,4,5].map(x => `<g><line x1="${180 + x * 28}" y1="68" x2="${180 + x * 28}" y2="84" class="sim-tick"/><text x="${180 + x * 28}" y="104" text-anchor="middle">${x}</text></g>`).join("")}<circle cx="${180 + n * 28}" cy="76" r="10" class="sim-marker"/><text x="180" y="30" text-anchor="middle">位置 ${n}</text></svg></div>${slider("n", "移動位置", n, -5, 5)}`;
    }
    if (engine === "math-algebra-balance") {
      const solution = state.target - state.addend;
      return `<div class="sim-stage sim-equation"><strong>x + ${state.addend} = ${state.target}</strong><div class="balance"><span class="balance-pan">x + ${state.addend}</span><span aria-hidden="true">⚖</span><span class="balance-pan">${state.target}</span></div><p>把常數移開後，x = <b>${solution}</b>。</p></div>${slider("addend", "左側常數", state.addend, -10, 10)}${slider("target", "右側總量", state.target, -10, 20)}`;
    }
    if (engine === "math-function-graph") {
      const y = state.m * state.x + state.b;
      const start = graphPoint(-5, state.m * -5 + state.b), end = graphPoint(5, state.m * 5 + state.b), point = graphPoint(state.x, y);
      return `<div class="sim-stage"><svg viewBox="0 0 360 260" role="img" aria-label="y 等於 ${state.m}x 加 ${state.b} 的圖形，x 等於 ${state.x} 時 y 等於 ${y}"><line x1="20" y1="130" x2="340" y2="130" class="sim-axis"/><line x1="180" y1="20" x2="180" y2="240" class="sim-axis"/><line x1="${start}" x2="${end}" class="sim-line"/><circle cx="${point.split(",")[0]}" cy="${point.split(",")[1]}" r="7" class="sim-marker"/><text x="24" y="28">y = ${state.m}x ${state.b >= 0 ? "+" : "−"} ${Math.abs(state.b)}</text><text x="24" y="50">x=${state.x}，y=${y}</text></svg></div>${slider("m", "斜率 m", state.m, -5, 5)}${slider("b", "截距 b", state.b, -8, 8)}${slider("x", "觀察 x", state.x, -5, 5)}`;
    }
    if (engine === "math-geometry") {
      const area = state.base * state.height / 2;
      return `<div class="sim-stage"><svg viewBox="0 0 360 220" role="img" aria-label="底為 ${state.base}、高為 ${state.height} 的三角形"><polygon points="70,180 ${70 + state.base * 18},180 70,${180 - state.height * 18}" class="sim-shape"/><line x1="70" y1="${180 - state.height * 18}" x2="70" y2="180" class="sim-dash"/><text x="180" y="30" text-anchor="middle">面積 = 底 × 高 ÷ 2 = ${area}</text></svg></div>${slider("base", "底", state.base, 1, 14)}${slider("height", "高", state.height, 1, 10)}`;
    }
    if (engine === "math-data-lab") {
      const values = [state.a, state.b, state.c], mean = (values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1);
      return `<div class="sim-stage"><div class="sim-bars">${values.map((value, index) => `<div><i style="height:${value * 10}px"></i><span>資料 ${index + 1}<br>${value}</span></div>`).join("")}</div><p>平均數 = <b>${mean}</b></p></div>${slider("a", "資料 1", state.a, 0, 15)}${slider("b", "資料 2", state.b, 0, 15)}${slider("c", "資料 3", state.c, 0, 15)}`;
    }
    if (engine === "math-probability-lab") {
      const rate = state.trials ? Math.round(state.hits / state.trials * 100) : 0;
      return `<div class="sim-stage"><p>試驗 ${state.trials} 次，事件出現 <b>${state.hits}</b> 次。</p><p class="sim-result">目前實驗頻率：${rate}%</p><button type="button" class="sim-button" data-sim-action="run-trials">進行一輪試驗</button></div>${slider("trials", "每輪試驗次數", state.trials, 5, 100, 5)}`;
    }
    if (engine === "science-motion-lab") {
      const net = Math.max(0, state.force - state.friction), acceleration = (net / state.mass).toFixed(2);
      return `<div class="sim-stage"><div class="sim-cart" style="--sim-speed:${Math.min(4, Number(acceleration))}s">▰</div><p>合力：${net} N；模型加速度：<b>${acceleration}</b> m/s²</p></div>${slider("force", "施力", state.force, 0, 30, 1, " N")}${slider("mass", "質量", state.mass, 1, 12, 1, " kg")}${slider("friction", "阻力", state.friction, 0, 20, 1, " N")}`;
    }
    if (engine === "science-energy-lab") {
      const input = state.power * state.time, usable = (input * (100 - state.loss) / 100).toFixed(1);
      return `<div class="sim-stage"><div class="sim-energy"><i style="width:${100 - state.loss}%"></i></div><p>輸入能量：${input} J；可用能量：<b>${usable}</b> J</p></div>${slider("power", "功率", state.power, 1, 30, 1, " W")}${slider("time", "時間", state.time, 1, 12, 1, " s")}${slider("loss", "損失", state.loss, 0, 80, 5, "%")}`;
    }
    if (engine === "science-particle-lab") {
      const phase = state.temperature < 33 ? "粒子較緊密" : state.temperature < 67 ? "粒子可互相滑動" : "粒子間距較大";
      return `<div class="sim-stage"><div class="sim-particles" style="--particle-space:${state.spacing * 2}px;--particle-motion:${Math.max(.2, 1 - state.temperature / 120)}s">${Array.from({ length: 24 }, (_, i) => `<i style="--i:${i}"></i>`).join("")}</div><p>${phase}；這是用來比較變因改變的粒子模型。</p></div>${slider("temperature", "溫度條件", state.temperature, 0, 100, 1, "%")}${slider("spacing", "初始間距", state.spacing, 1, 8)}`;
    }
    if (engine === "science-life-system") {
      if (lesson.simulation.model === "circulation" && window.heartAnatomyLab) return `${window.heartAnatomyLab()}${slider("rate", "循環速率", state.rate, 40, 120, 5, " bpm")}`;
      const balance = state.rate - state.demand;
      return `<div class="sim-stage"><div class="sim-flow"><i style="width:${Math.min(100, state.rate)}%"></i></div><p>運輸條件 ${state.rate}；需求條件 ${state.demand}；比較差：<b>${balance}</b></p><p class="sim-caption">以單一條件改變觀察系統的相對變化；實際生物系統需受更多證據限制。</p></div>${slider("rate", "運輸條件", state.rate, 0, 100)}${slider("demand", "需求條件", state.demand, 0, 100)}`;
    }
    if (engine === "science-earth-space") {
      const daylight = (12 + Math.sin(state.position * Math.PI / 180) * Math.sin(state.tilt * Math.PI / 180) * 8).toFixed(1);
      return `<div class="sim-stage"><div class="sim-orbit"><i style="transform:rotate(${state.position}deg)"></i><b style="transform:rotate(${state.tilt}deg)"></b></div><p>模型估計日照長度：<b>${daylight}</b> 小時</p></div>${slider("tilt", "傾角", state.tilt, 0, 45, .5, "°")}${slider("position", "公轉位置", state.position, 0, 360, 15, "°")}`;
    }
    const evidence = ["直接觀察", "模型或資料", "可檢查的限制"][state.evidence - 1];
    return `<div class="sim-stage"><ol class="sim-evidence"><li class="${state.evidence >= 1 ? "active" : ""}">直接觀察：寫下情境中可確認的條件</li><li class="${state.evidence >= 2 ? "active" : ""}">模型或資料：連結可重現的理由</li><li class="${state.evidence >= 3 ? "active" : ""}">限制：說明還不能推論什麼</li></ol><p>目前聚焦：<b>${evidence}</b></p></div>${slider("evidence", "推理階段", state.evidence, 1, 3)}`;
  };
  const render = lesson => {
    const simulation = lesson.simulation;
    if (!simulation) return "";
    lessons.set(lesson.id, lesson);
    const state = read(simulation);
    const reflection = esc(state.reflection || "");
    return `<section class="simulation" data-simulation-lesson="${esc(lesson.id)}" aria-label="${esc(label(simulation.engine))}"><header><span class="tag">${esc(label(simulation.engine))}</span><h4>${esc(simulation.goal)}</h4><p>${esc(simulation.mission || "先預測，再操作與解釋。")} </p></header><div class="simulation-body">${renderModel(lesson, state)}</div><footer class="sim-learning"><p><b>學習紀錄</b>：先預測，操作後再用證據解釋。</p><div class="sim-actions"><button type="button" data-sim-action="predicted">我已提出預測</button><button type="button" data-sim-action="observed">我已記錄觀察</button><button type="button" data-sim-reset>重設模型</button></div><label>我的解釋<textarea data-sim-reflection rows="3" placeholder="我改變了什麼？看見什麼？這如何支持我的解釋？">${reflection}</textarea></label><p class="sim-status" aria-live="polite">${state.status || "尚未記錄預測與觀察。"}</p><details class="sim-sources"><summary>模型依據與參考來源</summary><ul>${simulation.sourceRefs.map(url => `<li><a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(url)}</a></li>`).join("")}</ul></details></footer></section>`;
  };
  const rerender = root => { const lesson = lessons.get(root.dataset.simulationLesson); if (lesson) root.outerHTML = render(lesson); };
  const update = (root, changes) => { const lesson = lessons.get(root.dataset.simulationLesson); if (!lesson) return; const next = { ...read(lesson.simulation), ...changes }; write(lesson.simulation, next); rerender(root); };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-simulation-lesson]");
    if (!root) return;
    if (event.target.matches("[data-sim-control]")) update(root, { [event.target.dataset.simControl]: Number(event.target.value) });
    if (event.target.matches("[data-sim-reflection]")) { const lesson = lessons.get(root.dataset.simulationLesson); if (lesson) write(lesson.simulation, { ...read(lesson.simulation), reflection: event.target.value }); }
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-simulation-lesson]");
    if (!root) return;
    const lesson = lessons.get(root.dataset.simulationLesson); if (!lesson) return;
    if (event.target.closest("[data-sim-reset]")) { localStorage.removeItem(stateKey(lesson.simulation.id)); rerender(root); return; }
    const designStep = event.target.closest("[data-design-step]");
    if (designStep) { update(root, { designStep: Number(designStep.dataset.designStep) }); return; }
    const action = event.target.closest("[data-sim-action]")?.dataset.simAction; if (!action) return;
    const state = read(lesson.simulation);
    if (action === "run-trials") state.hits = Array.from({ length: state.trials }, () => Math.random() < .5).filter(Boolean).length;
    if (action === "predicted") state.status = "已記錄預測；現在只改變一項條件並觀察。";
    if (action === "observed") state.status = "已記錄觀察；請在下方用自己的話連結證據與解釋。";
    write(lesson.simulation, state); rerender(root);
  });
  window.LearningSimulations = { render };
})();

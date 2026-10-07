/* Data-driven, dependency-free learning simulations for math and science. */
(() => {
  const storagePrefix = "tw-junior-cap-learning/simulation/v1/";
  const lessons = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
  const clamp = (value, min, max) => Math.max(min, Math.min(max, Number(value)));
  const stateKey = simulation => storagePrefix + (simulation.storageId || simulation.id);
  const defaults = (engine, model) => {
    if (window.MathVisualLabs?.supports(engine, model)) return window.MathVisualLabs.defaults(engine, model);
    if (engine === "science-earth-space" && model === "fa-iv-4-atmospheric-temperature-profile") return { profileScenario: "baseline" };
    if (engine === "concept-explorer" && model === "ecosystem-scale-boundary") return { site: "pond", scale: "individual" };
    if (engine === "concept-explorer" && model === "ca-iv-2-solution-identification") return { sample: "X", test: "litmus", control: "unknown", testRun: false };
    if (engine === "science-motion-lab" && ["eb-iv-1-torque-balance","eb-iv-2-lever-balance"].includes(model)) return { leftForce: 3, leftArm: 10, rightForce: 2, rightArm: 15, torquePrediction: "", predictionSubmitted: false, torqueFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-4-friction-threshold") return { pullForce: 0, normalForce: 10, surface: "wood", frictionPrediction: "", predictionSubmitted: false, frictionFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-5-hydraulic-pressure") return { inputForce: 20, inputArea: 4, outputArea: 40, depth: 2, pressurePrediction: "", predictionSubmitted: false, pressureFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-6-buoyancy") return { objectWeight: 8, liquidDensity: 1, displacedVolume: 500, buoyancyPrediction: "", predictionSubmitted: false, buoyancyFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-8-motion-graph") return { eastDistance: 8, westDistance: 4, stopTime: 2, motionPrediction: "", predictionSubmitted: false, motionFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-9-circular-motion") return { radius: 2, speed: 4, mass: 1, circularPrediction: "", predictionSubmitted: false, circularFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-10-inertia") return { initialSpeed: 4, appliedForce: 0, friction: 0, inertiaPrediction: "", predictionSubmitted: false, inertiaFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-11-impulse") return { mass: 2, initialVelocity: 1, force: 4, duration: 2, impulsePrediction: "", predictionSubmitted: false, impulseFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "ec-iv-2-boyle") return { gasVolume: 50, boylePrediction: "", predictionSubmitted: false, boyleFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-12-mass-inertia") return { cartMass: 2, pushForce: 4, pushTime: 2, massPrediction: "", predictionSubmitted: false, massFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-13-action-reaction") return { collisionForce: 5, systemBoundary: "separate", thirdPrediction: "", predictionSubmitted: false, thirdFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-3-static-equilibrium") return { loadForce: 40, loadArm: 1, cableForce: 40, cableArm: 1, verticalSupport: 0, equilibriumPrediction: "", predictionSubmitted: false, equilibriumFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-motion-lab" && model === "eb-iv-7-simple-machines") return { machineType: "fixed", load: 120, liftHeight: .5, rampLength: 2, machinePrediction: "", predictionSubmitted: false, machineFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-earth-space" && model === "fa-iv-1-earth-spheres") return { sphereView: "all", earthPrediction: "", predictionSubmitted: false, earthFeedback: "", transferChoice: "", transferFeedback: "" };
    if (engine === "science-particle-lab" && model === "rutherford-scattering") return { impactProximity: 3 };
    if (engine === "science-life-system" && model === "plant-transport") return { transpiration: 3, source: "leaf", sink: "fruit" };
    if (engine === "science-life-system" && model === "pond-food-web") return { disturbance: 0 };
    if (engine === "math-geometry" && model === "s9-1-polygon-similarity-v1") return { scaleX: 1, scaleY: 1, predictionChoice: "", predictionSubmitted: false, similarityChoice: "", similarityFeedback: "", transferChoice: "", transferFeedback: "", transferSubmitted: false };
    if (engine === "math-geometry" && model === "s9-13-prism-surface-volume") return { prismLength: 4, predictionChoice: "", predictionSubmitted: false, designStep: 0, transferChoice: "", transferSubmitted: false };
    if (engine === "math-geometry" && model === "s9-13-prism-surface-volume-v2") return { prismLength: 3, predictionChoice: "", predictionSubmitted: false, designStep: 0, transferChoice: "", transferSubmitted: false };
    return ({
    "math-number-line": { n: 0 },
    "math-inequality-range": { boundary: 12, relation: "at-least" },
    "math-algebra-balance": { addend: 3, target: 11 },
    "math-ticket-equation": {},
    "math-equation-meaning": { x: 5 },
    "math-reasoning-lab": { reasoningStep: 0, reasoningChoice: "" },
    "math-expression-lab": { x: 2 },
    "math-function-graph": { m: 1, b: 0, x: 2 },
    "math-system-graph": { sum: 6 },
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
  };
  const read = simulation => {
    const initial = {
      ...(simulation.initialState || {}),
      ...(simulation.ticketEquation?.initialState || {}),
      ...(simulation.inequalityRange?.initialState || {}),
    };
    try { return { ...defaults(simulation.engine, simulation.model), ...initial, ...JSON.parse(localStorage.getItem(stateKey(simulation)) || "{}") }; }
    catch { return { ...defaults(simulation.engine, simulation.model), ...initial }; }
  };
  const write = (simulation, state) => localStorage.setItem(stateKey(simulation), JSON.stringify(state));
  const label = (engine, model) => window.MathVisualLabs?.supports(engine, model) ? window.MathVisualLabs.label(engine) : ({
    "math-number-line": "數線操作臺", "math-inequality-range": "不等式範圍數線", "math-algebra-balance": "代數天平", "math-ticket-equation": "票券等量模型", "math-equation-meaning": "方程式意義檢驗臺", "math-reasoning-lab": "數學推理實驗室", "math-function-graph": "函數圖形實驗室",
    "math-system-graph": "聯立直線交點探索", "math-expression-lab": "代數式同值檢核臺",
    "math-geometry": "幾何建構臺", "math-data-lab": "資料實驗室", "math-probability-lab": "機率試驗器",
    "science-motion-lab": "力與運動實驗室", "science-energy-lab": "能量實驗室", "science-particle-lab": "粒子模型實驗室",
    "science-life-system": "生命系統模型", "science-earth-space": "地球與太空模型", "concept-explorer": "概念探索工作臺",
  }[engine] || "互動模型");
  const slider = (key, text, value, min, max, step = 1, unit = "") => `<label class="sim-control"><span>${esc(text)} <output data-sim-output="${key}">${value}${unit}</output></span><input data-sim-control="${key}" type="range" min="${min}" max="${max}" step="${step}" value="${value}" aria-label="${esc(text)}"></label>`;
  const geometryChoices = (kind, options, selected) => `<fieldset class="sim-choice-group"><legend>選擇答案</legend>${options.map(([key,label]) => `<button type="button" data-geometry-${kind}="${key}" aria-pressed="${selected===key}">${key}. ${esc(label)}</button>`).join("")}</fieldset>`;
  const graphPoint = (x, y) => `${180 + x * 28},${130 - y * 20}`;
  const atmosphereProfile = scenario => {
    const shifted = scenario === "shifted";
    const firstBoundary = shifted ? 55 : 50;
    const secondBoundary = shifted ? 90 : 85;
    const points = [[0, 15], [11, -56], [firstBoundary, 0], [secondBoundary, -90]];
    const x = height => 58 + height * 3.38;
    const y = temperature => 28 + (20 - temperature) * 2.02;
    const path = points.map(([height, temperature], index) => `${index ? "L" : "M"}${x(height).toFixed(1)},${y(temperature).toFixed(1)}`).join(" ");
    const layers = ["對流層", "平流層", "中氣層", "增溫層"];
    const marks = points.map(([height, temperature]) => `<circle cx="${x(height).toFixed(1)}" cy="${y(temperature).toFixed(1)}" r="4" class="sim-marker"><title>${height} km，${temperature}°C（教學示意值）</title></circle>`).join("");
    const svg = `<svg viewBox="0 0 430 310" role="img" aria-label="${shifted ? "假設" : "典型示意"}高度溫度剖面：曲線依序下降、上升、下降，增溫層只標定性升溫方向；非實測比例圖"><defs><marker id="atmo-arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="currentColor"/></marker></defs><line x1="58" y1="28" x2="58" y2="270" class="sim-axis"/><line x1="58" y1="270" x2="396" y2="270" class="sim-axis"/><line x1="58" y1="69" x2="396" y2="69" class="sim-axis sim-grid"/><line x1="58" y1="149" x2="396" y2="149" class="sim-axis sim-grid"/><line x1="58" y1="230" x2="396" y2="230" class="sim-axis sim-grid"/><path d="${path}" class="sim-line" fill="none"/>${marks}<path d="M${x(secondBoundary).toFixed(1)},${y(-90).toFixed(1)} L${(x(secondBoundary) + 23).toFixed(1)},${(y(-90) - 28).toFixed(1)}" class="sim-line" fill="none" marker-end="url(#atmo-arrow)"/><text x="${(x(secondBoundary) + 22).toFixed(1)}" y="${(y(-90) - 31).toFixed(1)}">升溫（定性）</text><text x="4" y="20">氣溫 °C</text><text x="320" y="300">高度 km</text><text x="42" y="74">0</text><text x="32" y="154">−40</text><text x="32" y="235">−80</text><text x="55" y="290">0</text><text x="90" y="290">10</text><text x="225" y="290">50</text><text x="360" y="290">90</text><text x="73" y="45">對流層</text><text x="130" y="45">平流層</text><text x="245" y="45">中氣層</text><text x="345" y="45">增溫層</text></svg>`;
    const stateText = shifted
      ? `假設情境：把第二、三個轉折由 50／85 km 移到 55／90 km，觀察層界如何跟著資料移動。這是假設資料，不代表真實大氣已發生變化。`
      : `原創教學示意：0 km／15°C、11 km／−56°C、${firstBoundary} km／0°C、${secondBoundary} km／−90°C；其上只表示升溫方向，不外推實測數值。這不是氣象站觀測資料。`;
    return `<section class="sim-atmos-profile" aria-label="大氣高度與溫度剖面探索"><div class="sim-actions" role="group" aria-label="選擇剖面情境"><button type="button" data-atmo-scenario="baseline" aria-pressed="${!shifted}">典型示意剖面</button><button type="button" data-atmo-scenario="shifted" aria-pressed="${shifted}">假設轉折位移</button></div><figure>${svg}<figcaption>${esc(stateText)}</figcaption></figure><p class="sim-caption">使用方式：先比對趨勢轉折，再命名四層；增溫層只呈現定性箭頭。圖中直線為概念示意，不能當成等比例的真實探空曲線。</p></section>`;
  };
  const renderLearningDesign = (lesson, state) => {
    const design = lesson.simulation?.learningDesign;
    if (!design?.steps?.length) return "";
    const current = Math.max(0, Math.min(design.steps.length - 1, Number(state.designStep || 0)));
    const step = design.steps[current];
    const predicted = state.designPredictionSubmitted === true;
    const nodes = design.steps.map((item,index) => {
      const x = 70 + index * (500 / Math.max(1, design.steps.length - 1));
      const active = index === current;
      const visible = predicted || index === 0;
      return visible ? `<g class="sim-design-node ${active ? "is-active" : ""}" transform="translate(${x} 92)"><circle r="${active ? 29 : 23}"/><text y="5" text-anchor="middle">${index+1}</text><text y="48" text-anchor="middle">${esc(String(item.equation || "").slice(0,22))}</text></g>` : `<g transform="translate(${x} 92)"><circle r="23" class="sim-design-node-locked"/><text y="5" text-anchor="middle">?</text></g>`;
    }).join("");
    const links = design.steps.slice(0,-1).map((_,index) => {
      const x1=70+index*(500/Math.max(1,design.steps.length-1)),x2=70+(index+1)*(500/Math.max(1,design.steps.length-1));
      return `<line x1="${x1+28}" y1="92" x2="${x2-28}" y2="92" class="sim-design-link"/>`;
    }).join("");
    const solutionSetVisual = design.type === "inequality-solution-set" ? `<figure class="sim-inequality-proof"><svg viewBox="0 0 360 120" role="img" aria-label="數線表示 x 小於負二；負二為空心端點並向左延伸；負三成立、負二不成立、負一不成立"><line x1="24" y1="54" x2="336" y2="54" class="sim-axis"/><line x1="24" y1="54" x2="192" y2="54" class="sim-line"/><path d="M34 46 L24 54 L34 62" class="sim-line" fill="none"/><circle cx="192" cy="54" r="8" fill="white" stroke="currentColor" stroke-width="3"/><circle cx="156" cy="54" r="5" class="sim-marker"/><text x="156" y="92" text-anchor="middle">測試點</text><text x="192" y="112" text-anchor="middle">邊界</text></svg><figcaption>圖形固定對應原式 −2x＋6＞10；選不同步驟可逐行檢查推理，不是只看最後答案。</figcaption></figure>` : "";
    return `<section class="sim-design sim-design-visual-first" data-design-type="${esc(design.type)}">
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>${esc(design.predictionPrompt)}</p><button type="button" data-design-action="submit-prediction">${predicted ? "已鎖定預測" : "我已完成預測，開始操作"}</button></div>
      <figure class="sim-design-map"><svg viewBox="0 0 640 180" role="img" aria-label="本單元四步證據路徑">${links}${nodes}</svg><figcaption>${predicted ? "點選節點逐步操作；每一步都必須回到圖像或數據證據。" : "先在心中或紙上做出預測；後續證據節點暫時鎖定。"}</figcaption></figure>
      ${solutionSetVisual}
      <fieldset class="sim-design-workbench"><legend>2. 操作與證據</legend>
        <div class="sim-design-steps" role="group" aria-label="單元探索步驟">${design.steps.map((item,index) => `<button type="button" data-design-step="${index}" ${index === current ? 'aria-current="step"' : ""}>步驟 ${index+1}</button>`).join("")}</div>
        <div class="sim-design-evidence" aria-live="polite"><p class="sim-design-equation sim-equation-current">${esc(step.equation)}</p><p><b>操作：</b>${esc(step.action)}</p><p><b>為什麼：</b>${esc(step.reason)}</p><p class="sim-design-feedback">${esc(step.feedback)}</p></div>
      </fieldset>
      <div class="sim-evidence-card"><p><b>3. 用證據說明</b></p><p>${esc(design.evidencePrompt)}</p></div>
    </section>`;
  };
  const renderModel = (lesson, state) => {
    if (window.MathVisualLabs?.supports(lesson.simulation.engine, lesson.simulation.model)) return window.MathVisualLabs.render(lesson, state);
    const { engine } = lesson.simulation;
    const designed = engine === "math-geometry" && (lesson.simulation.model.startsWith("s9-13-prism-surface-volume") || lesson.simulation.model === "s9-1-polygon-similarity-v1") ? "" : renderLearningDesign(lesson, state);
    if (engine === "math-equation-meaning") {
      const config = lesson.simulation.equationMeaning;
      const x = Number(state.x);
      const left = Number(config.coefficient) * x + Number(config.constant);
      const right = Number(config.total);
      const equal = left === right;
      return `${designed}<section class="sim-equation-meaning" aria-label="一元一次方程式意義互動"><h5>候選值代回原式</h5><p>${esc(config.context)}</p><p class="sim-ticket-equation-formula" aria-live="polite">${config.coefficient} × ${esc(config.variable)} + ${config.constant} = ${config.total}</p><div class="balance" aria-label="等號兩側數值比較"><span class="balance-pan">左側 ${left}</span><span aria-hidden="true">${equal ? "＝" : "≠"}</span><span class="balance-pan">右側 ${right}</span></div>${slider("x", `候選 ${config.variable} 的值`, x, config.min, config.max, config.step)}<p class="sim-ticket-feedback" role="status" aria-live="polite">${equal ? `代入 ${config.variable}=${x} 後左右相等，因此這個候選值是解。` : `代入 ${config.variable}=${x} 後左側為 ${left}、右側為 ${right}，左右不相等，因此這個候選值不是解。`}</p><p>本互動只檢驗候選值是否符合原等式，不展示移項、同除或其他求解程序。</p></section>`;
    }
    if (engine === "math-ticket-equation") {
      const config = lesson.simulation.ticketEquation;
      const count = Number(state.ticketCount);
      const fee = Number(state.oneTimeFee);
      const total = Number(state.totalPaid);
      const candidate = Number(state.candidatePrice);
      const recalculated = count * candidate + fee;
      const validCandidate = state.candidateVerified === true && recalculated === total;
      const controls = config.controls;
      return `${designed}<section class="sim-ticket-equation" aria-label="票券價格方程式互動"><h5>先用候選票價檢查等式</h5><p>購買 <b>${count}</b> 張${esc(config.itemLabel)}，每張候選價格 <b>${candidate} ${esc(config.currencyLabel)}</b>，另付一次性費用 <b>${fee} ${esc(config.currencyLabel)}</b>；實付總額 <b>${total} ${esc(config.currencyLabel)}</b>。</p><p class="sim-ticket-equation-formula" aria-live="polite">${count} × x + ${fee} = ${total}</p><div class="balance" aria-label="等號兩側的金額比較"><span class="balance-pan">左側 ${recalculated} ${esc(config.currencyLabel)}</span><span aria-hidden="true">＝</span><span class="balance-pan">右側 ${total} ${esc(config.currencyLabel)}</span></div><table><caption>候選單價代回原式</caption><tbody><tr><th scope="row">票數</th><td>${count} 張</td></tr><tr><th scope="row">候選票價</th><td>${candidate} ${esc(config.currencyLabel)}／張</td></tr><tr><th scope="row">票券合計＋一次性費用</th><td>${count} × ${candidate} + ${fee} = ${recalculated} ${esc(config.currencyLabel)}</td></tr><tr><th scope="row">原紀錄總額</th><td>${total} ${esc(config.currencyLabel)}</td></tr></tbody></table><div class="sim-ticket-controls">${slider("ticketCount", controls.ticketCount.label, count, controls.ticketCount.min, controls.ticketCount.max, controls.ticketCount.step, " 張")}${slider("oneTimeFee", controls.oneTimeFee.label, fee, controls.oneTimeFee.min, controls.oneTimeFee.max, controls.oneTimeFee.step, ` ${config.currencyLabel}`)}${slider("totalPaid", controls.totalPaid.label, total, controls.totalPaid.min, controls.totalPaid.max, controls.totalPaid.step, ` ${config.currencyLabel}`)}${slider("candidatePrice", controls.candidatePrice.label, candidate, controls.candidatePrice.min, controls.candidatePrice.max, controls.candidatePrice.step, ` ${config.currencyLabel}`)}</div><button type="button" class="sim-button" data-ticket-action="check">代回檢查候選票價</button><p class="sim-ticket-feedback" aria-live="polite">${esc(state.candidateFeedback || "先調整票數、固定費或候選票價，再檢查左右是否相等。")}</p>${validCandidate ? `<div class="sim-ticket-solution"><p>候選值成立：${count} × ${candidate} + ${fee} = ${total}。因此每張${esc(config.itemLabel)}的價格是 <strong>${candidate} ${esc(config.currencyLabel)}／張</strong>。</p><p>等量理由：兩側同減 ${fee} 得 ${count}x = ${total - fee}；再兩側同除 ${count} 得 x = ${candidate} ${esc(config.currencyLabel)}／張。</p></div>` : ""}</section>`;
    }
    if (engine === "science-motion-lab" && ["eb-iv-1-torque-balance","eb-iv-2-lever-balance"].includes(lesson.simulation.model)) {
      const lf = clamp(Number(state.leftForce), 1, 5);
      const la = clamp(Number(state.leftArm), 5, 20);
      const rf = clamp(Number(state.rightForce), 1, 5);
      const ra = clamp(Number(state.rightArm), 5, 20);
      const lt = lf * la / 100;
      const rt = rf * ra / 100;
      const net = rt - lt;
      const direction = Math.abs(net) < 0.0001 ? "力矩平衡" : net > 0 ? "順時針" : "逆時針";
      const angle = clamp(net * 70, -18, 18);
      const predictionLocked = !state.predictionSubmitted;
      const evidence = Math.abs(net) < 0.0001
        ? `左右力矩都是 ${lt.toFixed(2)} N·m，轉動效果互相抵消；但仍要把支點支持力納入，才能判斷是否同時沒有平移。`
        : `左側 ${lt.toFixed(2)} N·m、右側 ${rt.toFixed(2)} N·m，淨力矩 ${Math.abs(net).toFixed(2)} N·m，模型因此向${direction}傾斜。`;
      const predictionChoices = [["left","逆時針"],["balance","保持水平"],["right","順時針"]].map(([value,text]) => `<button type="button" data-torque-action="predict" data-value="${value}" aria-pressed="${state.torquePrediction===value}">${text}</button>`).join("");
      return `<section class="sim-torque-lab" aria-label="力與力矩視覺實驗室">
        <div class="sim-visual-first">
          <figure class="sim-torque-stage">
            <svg viewBox="0 0 640 300" role="img" aria-label="紙尺支點模型。左側力 ${lf} 牛頓、力臂 ${la} 公分；右側力 ${rf} 牛頓、力臂 ${ra} 公分；目前${direction}">
              <defs><marker id="torque-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0,0 L0,8 L8,4 z" fill="currentColor"/></marker></defs>
              <g transform="rotate(${angle} 320 145)">
                <rect x="90" y="130" width="460" height="30" rx="10" class="sim-beam"/>
                <line x1="320" y1="112" x2="320" y2="178" class="sim-axis"/>
                <line x1="${320-la*11}" y1="75" x2="${320-la*11}" y2="126" class="sim-force-arrow" marker-end="url(#torque-arrow)"/>
                <line x1="${320+ra*11}" y1="75" x2="${320+ra*11}" y2="126" class="sim-force-arrow" marker-end="url(#torque-arrow)"/>
                <text x="${320-la*11}" y="62" text-anchor="middle">↓ ${lf} N</text>
                <text x="${320+ra*11}" y="62" text-anchor="middle">↓ ${rf} N</text>
                <line x1="${320-la*11}" y1="190" x2="320" y2="190" class="sim-measure"/>
                <line x1="320" y1="218" x2="${320+ra*11}" y2="218" class="sim-measure"/>
                <text x="${320-la*5.5}" y="208" text-anchor="middle">${la} cm</text>
                <text x="${320+ra*5.5}" y="238" text-anchor="middle">${ra} cm</text>
              </g>
              <path d="M292 260 L320 178 L348 260 Z" class="sim-fulcrum"/>
              <text x="320" y="286" text-anchor="middle">支點</text>
            </svg>
            <figcaption aria-live="polite"><strong>${direction}</strong>｜左 ${lt.toFixed(2)} N·m　右 ${rt.toFixed(2)} N·m</figcaption>
          </figure>
          <div class="sim-prediction-panel">
            <p><b>1. 先預測，不先給答案</b></p>
            <p>目前設定下，紙尺會往哪一側轉？</p>
            <div class="sim-actions" role="group" aria-label="力矩方向預測">${predictionChoices}</div>
            <button type="button" data-torque-action="submit-prediction">鎖定預測並開始實驗</button>
            <p role="status">${esc(state.torqueFeedback || "選一個方向後再開始操作。")}</p>
          </div>
        </div>
        <fieldset class="sim-torque-controls" ${predictionLocked ? "disabled" : ""}><legend class="sr-only">力與力臂控制</legend>
          <p><b>2. 一次改一個量，看尺本身怎麼變</b></p>
          ${slider("leftForce","左側力",lf,1,5,1," N")}
          ${slider("leftArm","左力臂",la,5,20,1," cm")}
          ${slider("rightForce","右側力",rf,1,5,1," N")}
          ${slider("rightArm","右力臂",ra,5,20,1," cm")}
        </fieldset>
        <div class="sim-evidence-card">
          <p><b>3. 用圖上的證據說明</b></p>
          <p aria-live="polite">${evidence}</p>
          <p>不要只說「右邊比較重」；要同時指出 <strong>力 × 垂直力臂</strong>。</p>
        </div>
        <div class="sim-transfer-card">
          <p><b>4. 遷移：同樣 2 N，怎樣比較容易轉開螺帽？</b></p>
          <div class="sim-actions" role="group" aria-label="扳手遷移題">
            <button type="button" data-torque-action="transfer" data-value="near" aria-pressed="${state.transferChoice==="near"}">手握靠近轉軸</button>
            <button type="button" data-torque-action="transfer" data-value="far" aria-pressed="${state.transferChoice==="far"}">手握遠離轉軸</button>
          </div>
          <p role="status">${esc(state.transferFeedback || "先用尺上的力臂證據判斷，再選答案。")}</p>
        </div>
      </section>`;
    }
    if (engine === "science-earth-space" && lesson.simulation.model === "fa-iv-1-earth-spheres") {
      const view=["all","atmosphere","hydrosphere","lithosphere"].includes(state.sphereView)?state.sphereView:"all",locked=!state.predictionSubmitted;
      return `<section class="sim-earth-spheres-lab" aria-label="地球圈層視覺模型"><div class="sim-visual-first"><figure class="sim-earth-spheres-stage"><svg viewBox="0 0 680 360" role="img" aria-label="大氣圈、水圈與岩石圈互動模型">
      <circle cx="300" cy="180" r="145" class="sim-atmosphere ${view==="all"||view==="atmosphere"?"is-active":""}"/><circle cx="300" cy="180" r="112" class="sim-hydrosphere ${view==="all"||view==="hydrosphere"?"is-active":""}"/><path d="M210 165 Q260 105 315 145 T395 165 Q360 210 315 205 T210 165" class="sim-lithosphere ${view==="all"||view==="lithosphere"?"is-active":""}"/><text x="490" y="100">大氣圈：包圍地球的氣體</text><text x="490" y="150">水圈：海洋、冰、地下水等</text><text x="490" y="200">岩石圈：地表岩石與地殼</text><path d="M410 245 C500 270 500 310 410 315" class="sim-cycle-arrow"/><text x="480" y="295">物質與能量跨圈層交換</text></svg><figcaption>圈層不是三個互不相干的盒子；降雨、侵蝕、蒸發等現象都跨越圈層。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>降雨落到山坡並造成侵蝕，至少涉及？</p><div class="sim-actions"><button data-earth-sphere-action="predict" data-value="multi">多個圈層交互作用</button><button data-earth-sphere-action="predict" data-value="one">只有水圈</button></div><button data-earth-sphere-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.earthFeedback||"先找出水、空氣與岩石各在哪裡。")}</p></div></div>
      <fieldset class="sim-earth-spheres-controls" ${locked?"disabled":""}><legend>2. 點選圈層</legend><div class="sim-actions"><button data-earth-sphere-action="view" data-value="all">全部</button><button data-earth-sphere-action="view" data-value="atmosphere">大氣圈</button><button data-earth-sphere-action="view" data-value="hydrosphere">水圈</button><button data-earth-sphere-action="view" data-value="lithosphere">岩石圈</button></div></fieldset>
      <div class="sim-evidence-card"><p><b>3. 從圖找證據</b></p><p>${view==="all"?"三個圈層同時顯示，箭頭表示它們會交換物質與能量。":view==="atmosphere"?"大氣圈位在地表外圍，天氣現象發生其中。":view==="hydrosphere"?"水圈不只海洋，也包含冰與地下水等地球上的水。":"岩石圈提供地表固體環境，會受到風化與侵蝕。"}</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：火山噴發把氣體與灰送入空氣，是？</b></p><div class="sim-actions"><button data-earth-sphere-action="transfer" data-value="cross">岩石圈影響大氣圈</button><button data-earth-sphere-action="transfer" data-value="none">圈層互不影響</button></div><p role="status">${esc(state.transferFeedback||"追蹤物質從哪個圈層到哪個圈層。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-7-simple-machines") {
      const type=["fixed","moving","ramp"].includes(state.machineType)?state.machineType:"fixed",load=clamp(Number(state.load),60,180),h=clamp(Number(state.liftHeight),.25,1),L=clamp(Number(state.rampLength),1,4),segments=type==="moving"?2:1,inputForce=type==="ramp"?load*h/L:load/segments,inputDistance=type==="ramp"?L:h*segments,work=inputForce*inputDistance,locked=!state.predictionSubmitted;
      const diagram=type==="ramp"?`<polygon points="150,245 430,245 430,110" class="sim-ramp"/><rect x="335" y="145" width="55" height="42" class="sim-load"/><line x1="360" y1="145" x2="260" y2="195" class="sim-force-arrow"/>`:`<circle cx="300" cy="100" r="42" class="sim-pulley"/><line x1="258" y1="100" x2="258" y2="245" class="sim-rope"/><line x1="342" y1="100" x2="342" y2="245" class="sim-rope"/><rect x="225" y="215" width="66" height="48" class="sim-load"/>`;
      return `<section class="sim-machine-lab" aria-label="簡單機械視覺實驗室"><div class="sim-visual-first"><figure class="sim-machine-stage"><svg viewBox="0 0 680 330" role="img" aria-label="${type==="fixed"?"定滑輪":type==="moving"?"動滑輪":"斜面"}搬運 ${load} 牛頓負載">${diagram}<g transform="translate(470 80)"><text y="0">輸入力 ${inputForce.toFixed(1)} N</text><text y="38">輸入距離 ${inputDistance.toFixed(2)} m</text><text y="76">理想輸入功 ${work.toFixed(1)} J</text><text y="114">負載增加位能 ${(load*h).toFixed(1)} J</text></g></svg><figcaption>簡單機械可以換「力」與「距離」，理想情況下不會免費增加功。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>承重繩段由 1 段變 2 段，理想輸入力？</p><div class="sim-actions"><button data-machine-action="predict" data-value="half">約減半</button><button data-machine-action="predict" data-value="same">不變</button></div><button data-machine-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.machineFeedback||"先想力變小時要付出什麼距離代價。")}</p></div></div>
      <fieldset class="sim-machine-controls" ${locked?"disabled":""}><legend>2. 換機械、比較力與距離</legend><div class="sim-actions"><button data-machine-action="type" data-value="fixed">定滑輪</button><button data-machine-action="type" data-value="moving">動滑輪</button><button data-machine-action="type" data-value="ramp">斜面</button></div>${slider("load","負載重量",load,60,180,20," N")}${slider("liftHeight","提升高度",h,.25,1,.25," m")}${slider("rampLength","斜面長度",L,1,4,.5," m")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>目前輸入力×輸入距離＝${work.toFixed(1)}J，負載增加的重力位能＝${(load*h).toFixed(1)}J。理想模型中兩者相等；真實機械還會有摩擦損失。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：更長的理想斜面能省力，代價是？</b></p><div class="sim-actions"><button data-machine-action="transfer" data-value="distance">需要移動更長距離</button><button data-machine-action="transfer" data-value="free">總功也自動變少</button></div><p role="status">${esc(state.transferFeedback||"比較輸入功。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-3-static-equilibrium") {
      const load=clamp(Number(state.loadForce),10,80),arm=clamp(Number(state.loadArm),.5,2),cable=clamp(Number(state.cableForce),10,80),cArm=clamp(Number(state.cableArm),.5,2),support=clamp(Number(state.verticalSupport),0,80),cw=load*arm,ccw=cable*cArm,sumT=ccw-cw,sumF=cable+support-load,locked=!state.predictionSubmitted,angle=clamp(sumT/10,-12,12);
      return `<section class="sim-equilibrium-lab" aria-label="合力與合力矩靜力平衡視覺實驗室"><div class="sim-visual-first"><figure class="sim-equilibrium-stage"><svg viewBox="0 0 700 340" role="img" aria-label="吊臂合力 ${sumF.toFixed(0)} 牛頓，合力矩 ${sumT.toFixed(0)} 牛頓公尺">
      <g transform="translate(145 190) rotate(${angle})"><circle cx="0" cy="0" r="14" class="sim-fulcrum"/><line x1="0" y1="0" x2="390" y2="0" class="sim-beam"/><line x1="${arm*170}" y1="-10" x2="${arm*170}" y2="85" class="sim-force-arrow"/><text x="${arm*170+10}" y="78">↓負載 ${load}N</text><line x1="${cArm*170}" y1="5" x2="${cArm*170}" y2="-90" class="sim-force-arrow"/><text x="${cArm*170+8}" y="-72">↑拉索 ${cable}N</text></g>
      <g transform="translate(75 55)"><text y="0">Στ = ${sumT.toFixed(0)} N·m</text><text y="34">ΣFy = ${sumF.toFixed(0)} N</text><text y="76">${Math.abs(sumT)<1?"✓ 不轉":"✗ 仍會轉"}</text><text y="108">${Math.abs(sumF)<1?"✓ 不平移":"✗ 仍會平移"}</text></g></svg><figcaption>完整靜力平衡必須同時通過兩道門：Στ=0 且 ΣF=0。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>只把負載移得更遠，負載力矩會？</p><div class="sim-actions"><button data-equilibrium-action="predict" data-value="increase">增加</button><button data-equilibrium-action="predict" data-value="same">不變</button></div><button data-equilibrium-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.equilibriumFeedback||"先用 τ=F×d 判斷。")}</p></div></div>
      <fieldset class="sim-equilibrium-controls" ${locked?"disabled":""}><legend>2. 分別調到不轉與不平移</legend>${slider("loadForce","負載",load,10,80,10," N")}${slider("loadArm","負載力臂",arm,.5,2,.25," m")}${slider("cableForce","拉索垂直分力",cable,10,80,10," N")}${slider("cableArm","拉索力臂",cArm,.5,2,.25," m")}${slider("verticalSupport","鉸接垂直支持力",support,0,80,10," N")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 雙重證據</b></p><p>目前 Στ=${sumT.toFixed(0)} N·m、ΣFy=${sumF.toFixed(0)} N。${Math.abs(sumT)<1&&Math.abs(sumF)<1?"兩者皆為 0，才是完整靜力平衡。":"只讓其中一個歸零仍不夠；看圖找出另一個未通過的條件。"}</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：物體不轉是否代表一定靜止？</b></p><div class="sim-actions"><button data-equilibrium-action="transfer" data-value="no">不一定，還要 ΣF=0</button><button data-equilibrium-action="transfer" data-value="yes">一定</button></div><p role="status">${esc(state.transferFeedback||"區分轉動和平移。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-13-action-reaction") {
      const F=clamp(Number(state.collisionForce),1,10),together=state.systemBoundary==="together",locked=!state.predictionSubmitted,L=F*18;
      return `<section class="sim-third-law-lab" aria-label="作用力反作用力視覺實驗室"><div class="sim-visual-first"><figure class="sim-third-law-stage"><svg viewBox="0 0 680 330" role="img" aria-label="兩車接觸時互相施加大小 ${F} 牛頓方向相反的力">
      <rect x="170" y="150" width="115" height="65" rx="10" class="sim-cart"/><rect x="395" y="150" width="115" height="65" rx="10" class="sim-cart"/><text x="227" y="188" text-anchor="middle">車 A</text><text x="452" y="188" text-anchor="middle">車 B</text>
      <line x1="285" y1="135" x2="${285-L}" y2="135" class="sim-force-arrow"/><text x="180" y="115">B 對 A：${F} N ←</text><line x1="395" y1="235" x2="${395+L}" y2="235" class="sim-force-arrow"/><text x="400" y="270">A 對 B：${F} N →</text>
      <rect x="${together?145:160}" y="105" width="${together?390:145}" height="155" rx="16" class="sim-system-boundary"/>${together?"":'<rect x="380" y="105" width="145" height="155" rx="16" class="sim-system-boundary"/>'}
      <text x="340" y="55" text-anchor="middle">${together?"系統＝A+B：車間力成為內力配對":"系統分開：每個力作用在不同物體上"}</text></svg><figcaption>第三定律力對：同時、等大、反向，但作用在不同物體；因此不能在「單一物體」受力圖中互相抵消。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>大車撞小車時，接觸瞬間兩車互相作用力大小？</p><div class="sim-actions"><button data-third-action="predict" data-value="equal">等大反向</button><button data-third-action="predict" data-value="big">大車施力較大</button></div><button data-third-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.thirdFeedback||"先分清楚『力』和『加速度』。")}</p></div></div>
      <fieldset class="sim-third-law-controls" ${locked?"disabled":""}><legend>2. 操作碰撞與系統邊界</legend>${slider("collisionForce","接觸力大小",F,1,10,1," N")}<div class="sim-actions"><button data-third-action="boundary" data-value="separate">分開看 A、B</button><button data-third-action="boundary" data-value="together">把 A+B 當一個系統</button></div></fieldset>
      <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>兩支箭頭都標 ${F} N，方向相反、作用對象不同。${together?"當 A+B 合併成系統時，這一對車間作用力是內力；分析整體外力時不需各自當外力相加。":"分開畫受力圖時，B 對 A 只畫在 A，A 對 B 只畫在 B。"}</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：兩車受力等大，為何加速度仍可不同？</b></p><div class="sim-actions"><button data-third-action="transfer" data-value="mass">質量不同，a=F/m</button><button data-third-action="transfer" data-value="force">因為作用力其實不等大</button></div><p role="status">${esc(state.transferFeedback||"把第三定律與第二定律分開使用。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-12-mass-inertia") {
      const mass=clamp(Number(state.cartMass),1,6),force=clamp(Number(state.pushForce),1,8),time=clamp(Number(state.pushTime),.5,4),a=force/mass,dv=a*time,locked=!state.predictionSubmitted;
      const blocks=Math.round(mass),arrow=force*18;
      return `<section class="sim-mass-inertia-lab" aria-label="質量與慣性視覺實驗室"><div class="sim-visual-first"><figure class="sim-mass-inertia-stage"><svg viewBox="0 0 680 320" role="img" aria-label="質量 ${mass} 公斤滑車受 ${force} 牛頓推力 ${time} 秒">
        <line x1="55" y1="230" x2="620" y2="230" class="sim-track"/><g transform="translate(220 170)"><rect width="120" height="48" rx="8" class="sim-cart"/>${Array.from({length:blocks},(_,i)=>`<rect x="${8+i*17}" y="-22" width="14" height="20" class="sim-mass-block"/>`).join("")}<circle cx="22" cy="58" r="10"/><circle cx="98" cy="58" r="10"/></g>
        <line x1="345" y1="190" x2="${345+arrow}" y2="190" class="sim-force-arrow"/><text x="360" y="165">F=${force} N</text><line x1="280" y1="140" x2="${280+dv*30}" y2="140" class="sim-velocity-arrow"/><text x="280" y="115">Δv=${dv.toFixed(1)} m/s</text>
        <g transform="translate(70 45)"><text y="0">a = F/m</text><text y="35">= ${force}/${mass}</text><text y="70">= ${a.toFixed(2)} m/s²</text></g></svg><figcaption>同樣推力與時間下，質量越大，速度越難改變；這就是較大的慣性。</figcaption></figure>
        <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>推力與作用時間相同，質量加倍，Δv 會？</p><div class="sim-actions"><button data-mass-inertia-action="predict" data-value="half">約變一半</button><button data-mass-inertia-action="predict" data-value="double">約變兩倍</button></div><button data-mass-inertia-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.massFeedback||"先比較 F=ma。")}</p></div></div>
        <fieldset class="sim-mass-inertia-controls" ${locked?"disabled":""}><legend>2. 做公平比較</legend>${slider("cartMass","滑車質量",mass,1,6,1," kg")}${slider("pushForce","推力",force,1,8,1," N")}${slider("pushTime","作用時間",time,.5,4,.5," s")}</fieldset>
        <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>目前 a=${a.toFixed(2)} m/s²，作用 ${time}s 後 Δv=${dv.toFixed(1)}m/s。比較質量時要固定推力與作用時間，否則不能把差異歸因於慣性。</p></div>
        <div class="sim-transfer-card"><p><b>4. 遷移：同樣推購物車，裝滿貨物後較難加速，因為？</b></p><div class="sim-actions"><button data-mass-inertia-action="transfer" data-value="mass">質量較大、慣性較大</button><button data-mass-inertia-action="transfer" data-value="gravity">重力消失</button></div><p role="status">${esc(state.transferFeedback||"把情境連回同力下的加速度。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "ec-iv-2-boyle") {
      const V=clamp(Number(state.gasVolume),20,100),k=5000,P=k/V,locked=!state.predictionSubmitted,pistonY=65+(100-V)*1.35,dots=Math.round(V/10);
      return `<section class="sim-boyle-lab" aria-label="波以耳定律注射器視覺實驗室"><div class="sim-visual-first"><figure class="sim-boyle-stage"><svg viewBox="0 0 680 350" role="img" aria-label="定溫定量氣體體積 ${V} 毫升，壓力 ${P.toFixed(0)} 相對單位">
      <g transform="translate(75 35)"><rect x="55" y="30" width="150" height="245" rx="12" class="sim-syringe"/><rect x="62" y="${pistonY}" width="136" height="${275-pistonY}" class="sim-gas"/><rect x="45" y="${pistonY-12}" width="170" height="18" class="sim-piston"/><line x1="130" y1="0" x2="130" y2="${pistonY-12}" class="sim-plunger"/><text x="235" y="90">V = ${V} mL</text><text x="235" y="130">P = ${P.toFixed(0)}</text><text x="235" y="170">PV = ${(P*V).toFixed(0)}</text></g>
      <g transform="translate(440 55)"><line x1="0" y1="220" x2="180" y2="220" class="sim-axis"/><line x1="0" y1="220" x2="0" y2="0" class="sim-axis"/><path d="M20 20 C45 75,80 130,165 195" class="sim-boyle-curve"/><circle cx="${20+(V-20)*1.8}" cy="${220-Math.min(195,(P-50)*1.25)}" r="7" class="sim-marker"/><text x="150" y="245">V</text><text x="-5" y="-8">P</text></g></svg><figcaption>定溫、定量：壓縮體積時，壓力上升；PV 在此理想模型保持固定。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>把密閉注射器體積壓成一半，壓力會？</p><div class="sim-actions"><button data-boyle-action="predict" data-value="half">變一半</button><button data-boyle-action="predict" data-value="double">約變兩倍</button></div><button data-boyle-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.boyleFeedback||"先預測，再推活塞。")}</p></div></div>
      <fieldset class="sim-boyle-controls" ${locked?"disabled":""}><legend>2. 推拉活塞</legend>${slider("gasVolume","氣體體積",V,20,100,10," mL")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 同時看注射器與 P–V 圖</b></p><p>目前 P×V＝${P.toFixed(0)}×${V}＝${(P*V).toFixed(0)}。只有在氣體量與溫度固定時，這個反比模型才適用。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：體積由 40 mL 增至 80 mL，理想壓力？</b></p><div class="sim-actions"><button data-boyle-action="transfer" data-value="half">約減半</button><button data-boyle-action="transfer" data-value="same">不變</button></div><p role="status">${esc(state.transferFeedback||"利用 PV 固定判斷。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-11-impulse") {
      const mass=clamp(Number(state.mass),1,5),v0=clamp(Number(state.initialVelocity),-4,4),force=clamp(Number(state.force),-8,8),duration=clamp(Number(state.duration),.5,4),J=force*duration,dv=J/mass,v1=v0+dv,p0=mass*v0,p1=mass*v1,locked=!state.predictionSubmitted;
      const barW=Math.abs(J)*11;
      return `<section class="sim-impulse-lab" aria-label="衝量與動量改變視覺實驗室"><div class="sim-visual-first"><figure class="sim-impulse-stage"><svg viewBox="0 0 680 330" role="img" aria-label="質量 ${mass} 公斤、平均力 ${force} 牛頓作用 ${duration} 秒">
      <g transform="translate(65 60)"><text y="0">力－時間圖</text><line x1="0" y1="180" x2="270" y2="180" class="sim-axis"/><line x1="0" y1="180" x2="0" y2="20" class="sim-axis"/><rect x="35" y="${force>=0?180-Math.abs(force)*14:180}" width="${duration*50}" height="${Math.abs(force)*14}" class="sim-impulse-area"/><text x="45" y="210">面積 J = FΔt = ${J.toFixed(1)} N·s</text></g>
      <g transform="translate(390 75)"><rect x="0" y="70" width="90" height="55" rx="8" class="sim-cart"/><line x1="45" y1="55" x2="${45+v0*14}" y2="55" class="sim-velocity-arrow"/><text x="0" y="30">初速 ${v0} m/s</text><line x1="45" y1="145" x2="${45+v1*14}" y2="145" class="sim-velocity-arrow"/><text x="0" y="180">末速 ${v1.toFixed(1)} m/s</text><text x="0" y="220">Δp = ${(p1-p0).toFixed(1)} kg·m/s</text></g>
      </svg><figcaption>力－時間圖的面積就是衝量；同一數值也等於動量改變 Δp。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>同樣平均力，作用時間加倍，速度改變量會？</p><div class="sim-actions"><button data-impulse-action="predict" data-value="same">不變</button><button data-impulse-action="predict" data-value="double">加倍</button></div><button data-impulse-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.impulseFeedback||"先從力－時間圖的面積想。")}</p></div></div>
      <fieldset class="sim-impulse-controls" ${locked?"disabled":""}><legend>2. 改變碰撞條件</legend>${slider("mass","質量",mass,1,5,1," kg")}${slider("initialVelocity","初速度",v0,-4,4,1," m/s")}${slider("force","平均力",force,-8,8,1," N")}${slider("duration","作用時間",duration,.5,4,.5," s")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>J＝${force}×${duration}＝${J.toFixed(1)} N·s；Δp＝mΔv＝${mass}×${dv.toFixed(1)}＝${J.toFixed(1)} kg·m/s。方向由正負號保留。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：安全氣囊讓人停下的動量改變相近時，延長停止時間可？</b></p><div class="sim-actions"><button data-impulse-action="transfer" data-value="less-force">降低平均力</button><button data-impulse-action="transfer" data-value="more-force">提高平均力</button></div><p role="status">${esc(state.transferFeedback||"固定 Δp，比較 F=Δp/Δt。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-10-inertia") {
      const v0=clamp(Number(state.initialSpeed),0,8),force=clamp(Number(state.appliedForce),-5,5),friction=clamp(Number(state.friction),0,5),resist=v0>0?-friction:v0<0?friction:0,net=force+resist,v1=v0+net*0.8,locked=!state.predictionSubmitted;
      const x0=105,x1=105+v0*28,x2=105+clamp(v1,0,10)*28;
      return `<section class="sim-inertia-lab" aria-label="慣性與合力視覺實驗室"><div class="sim-visual-first"><figure class="sim-inertia-stage"><svg viewBox="0 0 680 320" role="img" aria-label="初速 ${v0} 公尺每秒、合力 ${net.toFixed(1)} 牛頓的滑車">
      <line x1="60" y1="215" x2="620" y2="215" class="sim-track"/><g transform="translate(${x1} 165)"><rect width="75" height="42" rx="8" class="sim-cart"/><circle cx="15" cy="48" r="9"/><circle cx="60" cy="48" r="9"/></g>
      <line x1="${x1+38}" y1="145" x2="${x1+38+v0*15}" y2="145" class="sim-velocity-arrow"/><text x="${x1+38}" y="125">v=${v0} m/s</text>
      <line x1="${x1+38}" y1="235" x2="${x1+38+net*22}" y2="235" class="sim-force-arrow"/><text x="${x1+38}" y="265">ΣF=${net.toFixed(1)} N</text>
      <g transform="translate(60 35)"><text y="0">現在</text><circle cx="45" cy="35" r="6" class="sim-marker"/><text x="80" y="40">若 ΣF=0，速度箭頭不必變成 0</text><text x="80" y="72">而是維持原本運動狀態</text></g></svg><figcaption>${Math.abs(net)<.01?`合力為 0：模型維持原速度 ${v0} m/s`:`合力不為 0：速度會改變，下一狀態約 ${v1.toFixed(1)} m/s`}</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>已在向右滑動的車若突然合力變成 0，會？</p><div class="sim-actions"><button data-inertia-action="predict" data-value="stop">立刻停下</button><button data-inertia-action="predict" data-value="continue">維持等速直線運動</button></div><button data-inertia-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.inertiaFeedback||"不要把『沒有合力』和『沒有速度』混在一起。")}</p></div></div>
      <fieldset class="sim-inertia-controls" ${locked?"disabled":""}><legend>2. 操作合力</legend>${slider("initialSpeed","初始速度",v0,0,8,1," m/s")}${slider("appliedForce","外加水平力",force,-5,5,1," N")}${slider("friction","摩擦阻力",friction,0,5,1," N")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 視覺證據</b></p><p>ΣF=${net.toFixed(1)} N。牛頓第一運動定律說的是合力為 0 時「速度保持不變」；若原本速度不為 0，就繼續等速直線運動。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：冰面上的冰球比粗糙地面更久才停，主要因為？</b></p><div class="sim-actions"><button data-inertia-action="transfer" data-value="less-friction">阻力較小，合力更接近 0</button><button data-inertia-action="transfer" data-value="needs-force">需要持續向前力才能動</button></div><p role="status">${esc(state.transferFeedback||"用合力是否接近 0 解釋。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-9-circular-motion") {
      const radius=clamp(Number(state.radius),1,5),speed=clamp(Number(state.speed),1,8),mass=clamp(Number(state.mass),.5,3),acc=speed*speed/radius,force=mass*acc,locked=!state.predictionSubmitted;
      const R=55+radius*18,cx=250,cy=175,angle=-.65,px=cx+R*Math.cos(angle),py=cy+R*Math.sin(angle),vx=-Math.sin(angle)*55,vy=Math.cos(angle)*55;
      return `<section class="sim-circular-lab" aria-label="圓周運動與向心加速度視覺實驗室"><div class="sim-visual-first"><figure class="sim-circular-stage"><svg viewBox="0 0 650 350" role="img" aria-label="半徑 ${radius} 公尺、速率 ${speed} 公尺每秒的圓周運動">
        <circle cx="${cx}" cy="${cy}" r="${R}" class="sim-orbit"/><circle cx="${cx}" cy="${cy}" r="7" class="sim-marker"/><circle cx="${px}" cy="${py}" r="16" class="sim-cart"/>
        <line x1="${px}" y1="${py}" x2="${px+vx}" y2="${py+vy}" class="sim-velocity-arrow"/><text x="${px+vx+8}" y="${py+vy}">v 切線</text>
        <line x1="${px}" y1="${py}" x2="${px+(cx-px)*.58}" y2="${py+(cy-py)*.58}" class="sim-force-arrow"/><text x="${(px+cx)/2}" y="${(py+cy)/2-10}">a 向心</text>
        <line x1="${cx}" y1="${cy+R+30}" x2="${cx+R}" y2="${cy+R+30}" class="sim-measure"/><text x="${cx+R/2}" y="${cy+R+52}" text-anchor="middle">r=${radius} m</text>
        <g transform="translate(430 85)"><text y="0">a = v²/r</text><text y="38">${speed}² ÷ ${radius}</text><text y="76">= ${acc.toFixed(1)} m/s²</text><text y="125">F = ma = ${force.toFixed(1)} N</text></g>
      </svg><figcaption>速度沿切線；加速度與合力指向圓心。速率不是只改箭頭長度，因為 a ∝ v²。</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>半徑不變，速率加倍，向心加速度會？</p><div class="sim-actions"><button data-circular-action="predict" data-value="double">2 倍</button><button data-circular-action="predict" data-value="quad">4 倍</button></div><button data-circular-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.circularFeedback||"先看 v 在公式中是幾次方。")}</p></div></div>
      <fieldset class="sim-circular-controls" ${locked?"disabled":""}><legend>2. 操作圓周模型</legend>${slider("radius","半徑",radius,1,5,.5," m")}${slider("speed","速率",speed,1,8,.5," m/s")}${slider("mass","質量",mass,.5,3,.5," kg")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>目前 a＝v²/r＝${acc.toFixed(1)} m/s²；質量只影響所需向心力 F＝ma，不會改變同一 v、r 所要求的向心加速度。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：速率不變、半徑加倍時 a？</b></p><div class="sim-actions"><button data-circular-action="transfer" data-value="half">變成一半</button><button data-circular-action="transfer" data-value="double">變成兩倍</button></div><p role="status">${esc(state.transferFeedback||"直接比較 a=v²/r 的分母。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-8-motion-graph") {
      const east=clamp(Number(state.eastDistance),2,12),west=clamp(Number(state.westDistance),0,10),stop=clamp(Number(state.stopTime),0,6),final=east-west,distance=east+west,total=4+4+stop,avgSpeed=distance/total,avgVelocity=final/total,locked=!state.predictionSubmitted;
      const x0=70,x1=70+east*32,x2=x1-west*32,gy=250,scale=14;
      return `<section class="sim-motion-graph-lab" aria-label="路程位移與位置時間圖視覺實驗室"><div class="sim-visual-first"><figure class="sim-motion-stage"><svg viewBox="0 0 700 360" role="img" aria-label="小車先向東 ${east} 公尺，再向西 ${west} 公尺，停留 ${stop} 秒">
        <line x1="55" y1="100" x2="620" y2="100" class="sim-track"/><circle cx="${x2}" cy="100" r="20" class="sim-cart"/><text x="55" y="75">起點 0 m</text><text x="${x1}" y="75" text-anchor="middle">最東 ${east} m</text><text x="${x2}" y="145" text-anchor="middle">終點 ${final} m</text>
        <g transform="translate(55 180)"><line x1="0" y1="150" x2="590" y2="150" class="sim-axis"/><line x1="0" y1="150" x2="0" y2="0" class="sim-axis"/><text x="570" y="175">時間</text><text x="-5" y="-8">位置</text>
        <polyline points="0,150 180,${150-east*scale} 360,${150-final*scale} ${360+stop*30},${150-final*scale}" class="sim-motion-line"/>
        <circle cx="180" cy="${150-east*scale}" r="6" class="sim-marker"/><circle cx="360" cy="${150-final*scale}" r="6" class="sim-marker"/></g>
      </svg><figcaption>路程 ${distance} m｜位移 ${final} m（${final>=0?"東":"西"}）｜平均速率 ${avgSpeed.toFixed(2)} m/s｜平均速度 ${avgVelocity.toFixed(2)} m/s</figcaption></figure>
      <div class="sim-prediction-panel"><p><b>1. 先預測圖形</b></p><p>小車折返後，位置—時間圖應該？</p><div class="sim-actions"><button data-motion-action="predict" data-value="down">往下降</button><button data-motion-action="predict" data-value="flat">保持水平</button></div><button data-motion-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.motionFeedback||"先判斷折返代表位置如何改變。")}</p></div></div>
      <fieldset class="sim-motion-controls" ${locked?"disabled":""}><legend>2. 改變路線</legend>${slider("eastDistance","向東距離",east,2,12,1," m")}${slider("westDistance","折返向西",west,0,10,1," m")}${slider("stopTime","停留時間",stop,0,6,1," s")}</fieldset>
      <div class="sim-evidence-card"><p><b>3. 從路線與圖一起判讀</b></p><p>路程把走過的 ${east}+${west} 相加；位移只比較終點與起點，所以是 ${final} m。停留會讓位置—時間圖出現水平線，並增加總時間，因此會降低平均速率的數值。</p></div>
      <div class="sim-transfer-card"><p><b>4. 遷移：回到起點時</b></p><div class="sim-actions"><button data-motion-action="transfer" data-value="zero">位移為 0，但路程可不為 0</button><button data-motion-action="transfer" data-value="both">路程和位移都一定為 0</button></div><p role="status">${esc(state.transferFeedback||"把『走過多少』和『終點相對起點』分開。")}</p></div></section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-6-buoyancy") {
      const weight=clamp(Number(state.objectWeight),2,15), density=clamp(Number(state.liquidDensity),0.7,1.3), volume=clamp(Number(state.displacedVolume),100,1000);
      const buoy=density*volume/1000*9.8, net=buoy-weight, status=Math.abs(net)<.35?"接近平衡漂浮":net>0?"浮力較大，向上加速":"重量較大，向下加速";
      const waterY=105, objY=clamp(145-net*8,115,205), locked=!state.predictionSubmitted;
      return `<section class="sim-buoyancy-lab" aria-label="浮力與排液重量視覺實驗室"><div class="sim-visual-first">
        <figure class="sim-buoyancy-stage"><svg viewBox="0 0 640 330" role="img" aria-label="物體浸入液體，重量 ${weight} 牛頓，浮力 ${buoy.toFixed(1)} 牛頓，目前${status}">
          <rect x="80" y="${waterY}" width="480" height="190" rx="8" class="sim-fluid"/><line x1="80" y1="${waterY}" x2="560" y2="${waterY}" class="sim-water-line"/>
          <rect x="270" y="${objY}" width="100" height="85" rx="10" class="sim-object"/>
          <line x1="320" y1="${objY}" x2="320" y2="${objY-65}" class="sim-force-arrow"/><text x="335" y="${objY-48}">浮力 ${buoy.toFixed(1)} N ↑</text>
          <line x1="320" y1="${objY+85}" x2="320" y2="${objY+145}" class="sim-force-arrow"/><text x="335" y="${objY+130}">重量 ${weight} N ↓</text>
          <g transform="translate(455 135)"><rect width="70" height="120" class="sim-overflow-cup"/><rect y="${120-Math.min(105,volume/10)}" width="70" height="${Math.min(105,volume/10)}" class="sim-fluid"/><text x="35" y="145" text-anchor="middle">排液 ${volume} mL</text></g>
        </svg><figcaption><strong>${status}</strong>｜排開液體重量 ≈ 浮力 ${buoy.toFixed(1)} N</figcaption></figure>
        <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>同樣排開 500 mL，換成密度較大的液體，浮力會？</p><div class="sim-actions"><button data-buoyancy-action="predict" data-value="same">不變</button><button data-buoyancy-action="predict" data-value="increase">增加</button></div><button data-buoyancy-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.buoyancyFeedback||"先預測，再改液體密度。")}</p></div></div>
        <fieldset class="sim-buoyancy-controls" ${locked?"disabled":""}><legend>2. 操作浮力模型</legend>${slider("objectWeight","物體重量",weight,2,15,1," N")}${slider("liquidDensity","液體相對密度",density,.7,1.3,.1,"")}${slider("displacedVolume","排液體積",volume,100,1000,100," mL")}</fieldset>
        <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>排開液體重量＝密度 × 排液體積 × g；目前模型得到 ${buoy.toFixed(1)} N，與向上的浮力箭頭相同。判斷浮沉要再和重量 ${weight} N 比較，而不是只看物體在水中的深度。</p></div>
        <div class="sim-transfer-card"><p><b>4. 遷移：船增加貨物後仍要漂浮，必須？</b></p><div class="sim-actions"><button data-buoyancy-action="transfer" data-value="less">排開更少液體</button><button data-buoyancy-action="transfer" data-value="more">排開更多液體</button></div><p role="status">${esc(state.transferFeedback||"比較新增重量與所需浮力。")}</p></div>
      </section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-5-hydraulic-pressure") {
      const inputForce=clamp(Number(state.inputForce),10,60), inputArea=clamp(Number(state.inputArea),2,10), outputArea=clamp(Number(state.outputArea),10,80), depth=clamp(Number(state.depth),0,5);
      const p=inputForce/inputArea, out=p*outputArea, ratio=outputArea/inputArea;
      const predictionLocked=!state.predictionSubmitted;
      const smallW=50+inputArea*4, bigW=80+outputArea*2.2, fluidP=Math.min(60,10+depth*10);
      return `<section class="sim-hydraulic-lab" aria-label="壓力與帕斯卡原理視覺實驗室">
        <div class="sim-visual-first"><figure class="sim-hydraulic-stage"><svg viewBox="0 0 680 330" role="img" aria-label="液壓活塞模型，小活塞 ${inputArea} 平方公分、輸入力 ${inputForce} 牛頓，大活塞 ${outputArea} 平方公分、理想輸出力 ${out.toFixed(0)} 牛頓">
          <rect x="55" y="205" width="${smallW}" height="70" class="sim-fluid"/><rect x="${560-bigW}" y="175" width="${bigW}" height="100" class="sim-fluid"/><rect x="${55+smallW}" y="245" width="${505-smallW-bigW}" height="30" class="sim-fluid"/>
          <rect x="55" y="190" width="${smallW}" height="16" class="sim-piston"/><rect x="${560-bigW}" y="160" width="${bigW}" height="16" class="sim-piston"/>
          <line x1="${55+smallW/2}" y1="90" x2="${55+smallW/2}" y2="184" class="sim-force-arrow"/><text x="${55+smallW/2}" y="72" text-anchor="middle">↓ ${inputForce} N</text>
          <line x1="${560-bigW/2}" y1="156" x2="${560-bigW/2}" y2="72" class="sim-force-arrow"/><text x="${560-bigW/2}" y="55" text-anchor="middle">↑ ${out.toFixed(0)} N</text>
          <text x="340" y="300" text-anchor="middle">液體傳遞壓力：${p.toFixed(1)} N/cm²</text>
          <g transform="translate(290 25)"><rect width="100" height="150" rx="8" class="sim-water-tank"/><rect y="${45}" width="100" height="105" class="sim-fluid"/><circle cx="50" cy="${55+depth*17}" r="7" class="sim-marker"/><text x="112" y="${60+depth*17}">深度 ${depth} m</text></g>
        </svg><figcaption>面積比 ${ratio.toFixed(1)}×｜理想輸出力 ${out.toFixed(0)} N｜深度增加時液體壓力趨勢增加</figcaption></figure>
        <div class="sim-prediction-panel"><p><b>1. 先預測</b></p><p>輸入力不變，把輸出活塞面積變大，輸出力會？</p><div class="sim-actions"><button data-pressure-action="predict" data-value="same">不變</button><button data-pressure-action="predict" data-value="increase">增加</button></div><button data-pressure-action="submit-prediction">鎖定預測並開始</button><p role="status">${esc(state.pressureFeedback||"先預測，再操作活塞。")}</p></div></div>
        <fieldset class="sim-hydraulic-controls" ${predictionLocked?"disabled":""}><legend>2. 直接操作液壓模型</legend>${slider("inputForce","輸入力",inputForce,10,60,5," N")}${slider("inputArea","小活塞面積",inputArea,2,10,1," cm²")}${slider("outputArea","大活塞面積",outputArea,10,80,10," cm²")}${slider("depth","探針深度",depth,0,5,1," m")}</fieldset>
        <div class="sim-evidence-card"><p><b>3. 圖像證據</b></p><p>小活塞壓力＝${inputForce}÷${inputArea}＝${p.toFixed(1)} N/cm²；理想密閉液體把同一壓力傳到大活塞，所以輸出力＝${p.toFixed(1)}×${outputArea}＝${out.toFixed(0)} N。這不是能量免費增加：大活塞位移會相應縮短。</p></div>
        <div class="sim-transfer-card"><p><b>4. 遷移：想用較小輸入力舉起同一負載，應？</b></p><div class="sim-actions"><button data-pressure-action="transfer" data-value="smaller">縮小輸出活塞</button><button data-pressure-action="transfer" data-value="larger">增大輸出/輸入面積比</button></div><p role="status">${esc(state.transferFeedback||"用活塞面積比判斷。")}</p></div>
      </section>`;
    }
    if (engine === "science-motion-lab" && lesson.simulation.model === "eb-iv-4-friction-threshold") {
      const pull = clamp(Number(state.pullForce), 0, 15);
      const normal = clamp(Number(state.normalForce), 5, 20);
      const surface = state.surface === "rough" ? "rough" : "wood";
      const muS = surface === "rough" ? 0.7 : 0.5, muK = surface === "rough" ? 0.5 : 0.35;
      const maxStatic = muS * normal, kinetic = muK * normal;
      const moving = pull > maxStatic;
      const friction = moving ? kinetic : pull;
      const net = Math.max(0, pull - friction);
      const boxX = 110 + Math.min(250, net * 16);
      const predictionLocked = !state.predictionSubmitted;
      const phase = moving ? "滑動：動摩擦" : Math.abs(pull-maxStatic)<0.01 ? "臨界：最大靜摩擦" : "靜止：靜摩擦自動配合";
      return `<section class="sim-friction-lab" aria-label="靜摩擦與動摩擦視覺實驗室">
        <div class="sim-visual-first">
          <figure class="sim-friction-stage">
            <svg viewBox="0 0 640 300" role="img" aria-label="木盒摩擦模型，拉力 ${pull} 牛頓，摩擦力 ${friction.toFixed(1)} 牛頓，目前${phase}">
              <defs><marker id="friction-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0,0 L0,8 L8,4 z" fill="currentColor"/></marker></defs>
              <line x1="55" y1="220" x2="585" y2="220" class="sim-surface-line"/>
              <rect x="${boxX}" y="140" width="120" height="78" rx="8" class="sim-box"/>
              <line x1="${boxX+120}" y1="178" x2="${boxX+120+Math.max(10,pull*12)}" y2="178" class="sim-force-arrow" marker-end="url(#friction-arrow)"/>
              <text x="${boxX+155}" y="160">拉力 ${pull} N →</text>
              <line x1="${boxX}" y1="198" x2="${boxX-Math.max(10,friction*12)}" y2="198" class="sim-force-arrow" marker-end="url(#friction-arrow)"/>
              <text x="${Math.max(35,boxX-130)}" y="185">← 摩擦 ${friction.toFixed(1)} N</text>
              <line x1="${boxX+60}" y1="138" x2="${boxX+60}" y2="80" class="sim-force-arrow" marker-end="url(#friction-arrow)"/>
              <line x1="${boxX+82}" y1="82" x2="${boxX+82}" y2="138" class="sim-force-arrow" marker-end="url(#friction-arrow)"/>
              <text x="${boxX+95}" y="105">N=${normal} N</text>
              <text x="70" y="255">接觸面：${surface==="rough"?"粗糙面":"木質示意面"}</text>
            </svg>
            <figcaption><strong>${phase}</strong>｜最大靜摩擦 ${maxStatic.toFixed(1)} N｜${moving?`淨力 ${net.toFixed(1)} N`:"淨力 0 N"}</figcaption>
          </figure>
          <div class="sim-prediction-panel">
            <p><b>1. 先預測摩擦力怎麼變</b></p><p>拉力逐漸增加時，盒子還沒動之前，摩擦力會？</p>
            <div class="sim-actions"><button type="button" data-friction-action="predict" data-value="fixed" aria-pressed="${state.frictionPrediction==="fixed"}">維持固定</button><button type="button" data-friction-action="predict" data-value="follow" aria-pressed="${state.frictionPrediction==="follow"}">跟著拉力增加</button></div>
            <button type="button" data-friction-action="submit-prediction">鎖定預測並開始實驗</button><p role="status">${esc(state.frictionFeedback||"先預測，再拖動拉力。")}</p>
          </div>
        </div>
        <fieldset class="sim-friction-controls" ${predictionLocked?"disabled":""}><legend>2. 操作木盒</legend>
          ${slider("pullForce","水平拉力",pull,0,15,1," N")}${slider("normalForce","正向力",normal,5,20,1," N")}
          <div class="sim-actions"><button type="button" data-friction-action="surface" data-value="wood" aria-pressed="${surface==="wood"}">木質示意面</button><button type="button" data-friction-action="surface" data-value="rough" aria-pressed="${surface==="rough"}">較粗糙面</button></div>
        </fieldset>
        <div class="sim-evidence-card"><p><b>3. 從圖判讀證據</b></p><p>${moving?`拉力 ${pull} N 已超過最大靜摩擦 ${maxStatic.toFixed(1)} N，盒子開始滑動；此時模型改用動摩擦 ${kinetic.toFixed(1)} N。`:`盒子尚未滑動，所以靜摩擦不是固定最大值，而是配合拉力成為 ${friction.toFixed(1)} N，直到上限 ${maxStatic.toFixed(1)} N。`}</p></div>
        <div class="sim-transfer-card"><p><b>4. 遷移：增加盒上負載後，臨界滑動拉力？</b></p><div class="sim-actions"><button type="button" data-friction-action="transfer" data-value="lower">變小</button><button type="button" data-friction-action="transfer" data-value="higher">變大</button></div><p role="status">${esc(state.transferFeedback||"利用正向力與臨界值的變化判斷。")}</p></div>
      </section>`;
    }
    const hasDedicatedRutherfordModel = engine === "science-particle-lab" && lesson.simulation.model === "rutherford-scattering";
    const hasDedicatedPlantTransportModel = engine === "science-life-system" && lesson.simulation.model === "plant-transport";
    const hasDedicatedPondFoodWebModel = engine === "science-life-system" && lesson.simulation.model === "pond-food-web";
    const hasDedicatedMathRenderer = ["math-number-line","math-inequality-range","math-algebra-balance","math-ticket-equation","math-equation-meaning","math-reasoning-lab","math-expression-lab","math-function-graph","math-system-graph","math-geometry","math-data-lab","math-probability-lab"].includes(engine);
    if (designed && !hasDedicatedMathRenderer && !hasDedicatedRutherfordModel && !hasDedicatedPlantTransportModel && !hasDedicatedPondFoodWebModel && lesson.simulation.model !== "fa-iv-4-atmospheric-temperature-profile" && lesson.simulation.model !== "ca-iv-2-solution-identification" && lesson.simulation.model !== "ecosystem-scale-boundary") return designed;
    if (engine === "math-expression-lab") {
      const x = Number(state.x);
      const original = 3 * x + 2 + 5 * x - 7;
      const simplified = 8 * x - 5;
      const rows = [-2, 0, 3].map(value => `<tr><th scope="row">${value}</th><td>${3 * value + 2 + 5 * value - 7}</td><td>${8 * value - 5}</td></tr>`).join("");
      return `${designed}<div class="sim-expression-check"><h5>同值檢驗</h5><p aria-live="polite">x=${x}；原式 3x＋2＋5x−7 = <output data-expression-original>${original}</output>；整理式 8x−5 = <output data-expression-reduced>${simplified}</output>。${original === simplified ? "兩式同值。" : "兩式不同值，請檢查分組與符號。"}</p><div class="sim-table-wrap"><table><caption>固定測試值：比較原式與整理式</caption><thead><tr><th scope="col">x</th><th scope="col">原式</th><th scope="col">整理式</th></tr></thead><tbody>${rows}</tbody></table></div>${slider("x", "測試變數 x 的值", x, -5, 5)}</div>`;
    }
    if (engine === "math-inequality-range") {
      const config = lesson.simulation.inequalityRange || {};
      const min = Number.isFinite(Number(config.min)) ? Number(config.min) : 7;
      const max = Number.isFinite(Number(config.max)) ? Number(config.max) : 17;
      const step = Number.isFinite(Number(config.step)) && Number(config.step) > 0 ? Number(config.step) : 1;
      const boundary = clamp(Number(state.boundary), min, max);
      const relationKey = ["at-least", "greater", "at-most", "less"].includes(state.relation) ? state.relation : "at-least";
      const relation = ({ "at-least": ["≥", true, "向右", "至少"], greater: ["＞", false, "向右", "超過"], "at-most": ["≤", true, "向左", "至多"], less: ["＜", false, "向左", "低於"] })[relationKey];
      const [symbol, inclusive, direction, phrase] = relation;
      const span = Math.max(step, max - min);
      const x = 36 + ((boundary - min) / span) * 288;
      const start = direction === "向右" ? x : 24, end = direction === "向右" ? 336 : x;
      const offsets = Array.isArray(config.testOffsets) && config.testOffsets.length ? config.testOffsets : [-step, 0, step];
      const tests = offsets.map(offset => boundary + Number(offset)).filter(Number.isFinite);
      const qualifies = value => relationKey === "at-least" ? value >= boundary : relationKey === "greater" ? value > boundary : relationKey === "at-most" ? value <= boundary : value < boundary;
      const context = config.context ? `<p class="sim-context">${esc(config.context)}</p>` : "";
      return `<div class="sim-stage">${context}<p>語句：x ${phrase} ${boundary}　｜　符號：x ${symbol} ${boundary}　｜　端點：${inclusive ? "包含（實心）" : "不包含（空心）"}　｜　解集方向：${direction}</p><svg viewBox="0 0 360 120" role="img" aria-label="數線表示 x ${symbol} ${boundary}；${inclusive ? "端點包含" : "端點不包含"}；解集向${direction === "向右" ? "右" : "左"}延伸"><line x1="24" y1="58" x2="336" y2="58" class="sim-axis"/><line x1="${start}" y1="58" x2="${end}" y2="58" class="sim-line"/><path d="${direction === "向右" ? `M326 50 L336 58 L326 66` : `M34 50 L24 58 L34 66`}" class="sim-line" fill="none"/><circle cx="${x}" cy="58" r="9" class="sim-marker" style="fill:${inclusive ? "currentColor" : "white"};stroke:currentColor"/><text x="${x}" y="94" text-anchor="middle">${boundary}・${inclusive ? "含" : "不含"}</text></svg><p>邊界檢查：${tests.map(value => `${value} ${qualifies(value) ? "符合" : "不符合"}`).join("；")}</p></div><fieldset class="sim-relation"><legend>選擇文字條件（可用鍵盤操作）</legend>${[["at-least","至少"],["greater","超過"],["at-most","至多"],["less","低於"]].map(([value,label]) => `<button type="button" data-inequality-relation="${value}" aria-pressed="${relationKey === value}">${label}</button>`).join("")}</fieldset>${slider("boundary", "邊界值", boundary, min, max, step)}${designed || ""}`;
    }
    if (engine === "math-number-line") {
      const n = state.n;
      return `${designed}<div class="sim-stage"><svg viewBox="0 0 360 150" role="img" aria-label="數線上目前的值是 ${n}"><line x1="24" y1="76" x2="336" y2="76" class="sim-axis"/>${[-5,-4,-3,-2,-1,0,1,2,3,4,5].map(x => `<g><line x1="${180 + x * 28}" y1="68" x2="${180 + x * 28}" y2="84" class="sim-tick"/><text x="${180 + x * 28}" y="104" text-anchor="middle">${x}</text></g>`).join("")}<circle cx="${180 + n * 28}" cy="76" r="10" class="sim-marker"/><text x="180" y="30" text-anchor="middle">位置 ${n}</text></svg></div>${slider("n", "移動位置", n, -5, 5)}`;
    }
    if (engine === "math-algebra-balance") {
      const solution = state.target - state.addend;
      return `${designed}<div class="sim-stage sim-equation"><strong>x + ${state.addend} = ${state.target}</strong><div class="balance"><span class="balance-pan">x + ${state.addend}</span><span aria-hidden="true">⚖</span><span class="balance-pan">${state.target}</span></div><p>把常數移開後，x = <b>${solution}</b>。</p></div>${slider("addend", "左側常數", state.addend, -10, 10)}${slider("target", "右側總量", state.target, -10, 20)}`;
    }
    if (engine === "math-function-graph") {
      const y = state.m * state.x + state.b;
      const start = graphPoint(-5, state.m * -5 + state.b), end = graphPoint(5, state.m * 5 + state.b), point = graphPoint(state.x, y);
      return `${designed}<div class="sim-stage"><svg viewBox="0 0 360 260" role="img" aria-label="y 等於 ${state.m}x 加 ${state.b} 的圖形，x 等於 ${state.x} 時 y 等於 ${y}"><line x1="20" y1="130" x2="340" y2="130" class="sim-axis"/><line x1="180" y1="20" x2="180" y2="240" class="sim-axis"/><line x1="${start}" x2="${end}" class="sim-line"/><circle cx="${point.split(",")[0]}" cy="${point.split(",")[1]}" r="7" class="sim-marker"/><text x="24" y="28">y = ${state.m}x ${state.b >= 0 ? "+" : "−"} ${Math.abs(state.b)}</text><text x="24" y="50">x=${state.x}，y=${y}</text></svg></div>${slider("m", "斜率 m", state.m, -5, 5)}${slider("b", "截距 b", state.b, -8, 8)}${slider("x", "觀察 x", state.x, -5, 5)}`;
    }
    if (engine === "math-system-graph") {
      const sum = Number(state.sum);
      const intersectionX = (sum + 2) / 3;
      const intersectionY = (2 * sum - 2) / 3;
      const mapPoint = (x, y) => `${220 + x * 24},${140 - y * 12}`;
      const firstStart = mapPoint(-4, -10), firstEnd = mapPoint(4, 6);
      const secondStart = mapPoint(-4, sum + 4), secondEnd = mapPoint(4, sum - 4);
      const crossing = mapPoint(intersectionX, intersectionY);
      const xThird = sum + 2, yThird = 2 * sum - 2;
      return `<div class="sim-stage"><svg viewBox="0 0 440 300" role="img" aria-label="直線 2x 減 y 等於 2 與 x 加 y 等於 ${sum} 的交點為（${xThird}/3，${yThird}/3）"><line x1="40" y1="140" x2="400" y2="140" class="sim-axis"/><line x1="220" y1="20" x2="220" y2="260" class="sim-axis"/><line x1="${firstStart}" x2="${firstEnd}" class="sim-line"/><line x1="${secondStart}" x2="${secondEnd}" class="sim-line sim-line-secondary"/><circle cx="${crossing.split(",")[0]}" cy="${crossing.split(",")[1]}" r="8" class="sim-marker"/><text x="24" y="22">2x − y = 2</text><text x="24" y="44">x + y = ${sum}</text><text x="230" y="62">交點（${xThird}/3，${yThird}/3）</text></svg><p>第一條直線可由（0，−2）、（2，2）連成；交點仍要代回兩條原式確認。</p></div>${slider("sum", "第二式右側常數", sum, 3, 9, 1)}${designed}`;
    }
    if (engine === "math-geometry") {
      if (lesson.simulation.model === "s9-1-polygon-similarity-v1") {
        const config = lesson.simulation.similarityModel;
        const width = config.originalWidth, height = config.originalHeight;
        const scaleX = Number(state.scaleX), scaleY = Number(state.scaleY);
        const scaledWidth = width * scaleX, scaledHeight = height * scaleY;
        const unlocked = Boolean(state.predictionSubmitted);
        const transferWidth = config.transferWidth, transferHeight = config.transferHeight, transferScale = config.transferScale;
        const feedback = state.similarityFeedback || "先操作水平與垂直倍率，再用兩組對應邊檢查。";
        return `<section class="sim-similarity-lab" aria-label="多邊形等比例縮放探索"><h5>預測：兩個方向都乘同一倍率，矩形仍與原圖相似嗎？</h5><p>原圖為 ${width}×${height} 公分。先提交預測；解鎖後可分別調整水平與垂直倍率。</p><div class="sim-actions" role="group" aria-label="縮放預測">${[["yes","相似，因兩方向倍率一致"],["no","不相似，尺寸改變就不相似"]].map(([value,text]) => `<button type="button" data-sim-similarity="prediction" data-value="${value}" aria-pressed="${state.predictionChoice === value}">${esc(text)}</button>`).join("")}</div><button type="button" class="sim-button" data-sim-similarity="submit-prediction">提交預測並解鎖</button><p class="sim-status" aria-live="polite">${esc(state.predictionFeedback || "尚未提交預測。")}</p>${unlocked ? `<div class="sim-similarity-controls">${slider("scaleX","水平倍率",scaleX,config.scaleMin,config.scaleMax,config.scaleStep," 倍")}${slider("scaleY","垂直倍率",scaleY,config.scaleMin,config.scaleMax,config.scaleStep," 倍")}</div><figure><svg viewBox="0 0 360 190" role="img" aria-label="原圖 ${width} 乘 ${height} 公分；縮放圖水平倍率 ${scaleX}、垂直倍率 ${scaleY}，尺寸 ${scaledWidth} 乘 ${scaledHeight} 公分"><rect x="35" y="45" width="${width*28}" height="${height*28}" class="sim-shape"/><rect x="205" y="${130-scaledHeight*20}" width="${scaledWidth*20}" height="${scaledHeight*20}" fill="none" class="sim-line"/><text x="35" y="30">原圖 ${width}×${height}</text><text x="205" y="165">縮放圖 ${scaledWidth}×${scaledHeight}</text></svg><figcaption>矩形角仍為 90°；相似與否還須檢查對應邊倍率。</figcaption></figure><table><caption>沿邊界順序核對對應邊</caption><thead><tr><th>對應邊</th><th>原圖</th><th>縮放圖</th><th>倍率</th></tr></thead><tbody><tr><th>上／下邊</th><td>${width}</td><td>${scaledWidth}</td><td>${scaleX}</td></tr><tr><th>左／右邊</th><td>${height}</td><td>${scaledHeight}</td><td>${scaleY}</td></tr><tr><th>對應角</th><td colspan="3">四角仍為 90°；角相等不足以單獨證明相似</td></tr></tbody></table><fieldset><legend>驗證目前圖形是否相似</legend>${[["yes","相似"],["no","不相似"]].map(([value,text]) => `<button type="button" data-sim-similarity="verify" data-value="${value}" aria-pressed="${state.similarityChoice === value}">${text}</button>`).join("")}<button type="button" class="sim-button" data-sim-similarity="check">檢查倍率證據</button></fieldset><p class="sim-status" aria-live="polite">${esc(feedback)}</p><label>解釋你的判斷<textarea data-sim-reflection rows="3" placeholder="指出水平、垂直倍率及對應角的證據。">${esc(state.reflection || "")}</textarea></label><h6>遷移：${transferWidth}×${transferHeight} 公分新圖按 ${transferScale} 倍等比例縮印後，是否相似？</h6><p>比較 ${transferWidth*transferScale}÷${transferWidth} 與 ${transferHeight*transferScale}÷${transferHeight}。</p>${[["yes","相似；兩方向都是同倍率"],["no","不相似；尺寸縮小就不相似"]].map(([value,text]) => `<button type="button" data-sim-similarity="transfer" data-value="${value}" aria-pressed="${state.transferChoice === value}">${text}</button>`).join("")}<button type="button" class="sim-button" data-sim-similarity="submit-transfer">檢查遷移</button><p class="sim-status" aria-live="polite">${esc(state.transferFeedback || "先比較兩組對應邊的縮圖÷原圖。")}</p>` : "<p>提交預測後才顯示可操作的雙倍率模型；課文與文字題仍可閱讀。</p>"}</section>`;
      }
      if (lesson.simulation.model === "s9-13-prism-surface-volume-v2") {
        const config = lesson.simulation.prismModel;
        const base = config.baseTriangle;
        const transfer = config.transfer;
        const length = clamp(state.prismLength, config.sliderMin, config.sliderMax);
        const area = base.legA * base.legB / 2;
        const perimeter = base.legA + base.legB + base.hypotenuse;
        const surface = 2 * area + perimeter * length;
        const volume = area * length;
        const transferArea = transfer.baseTriangle.legA * transfer.baseTriangle.legB / 2;
        const transferPerimeter = transfer.baseTriangle.legA + transfer.baseTriangle.legB + transfer.baseTriangle.hypotenuse;
        const transferSurface = 2 * transferArea + transferPerimeter * transfer.length;
        const unlocked = Boolean(state.predictionSubmitted);
        const design = lesson.simulation.learningDesign;
        const step = design.steps[Math.max(0, Math.min(design.steps.length - 1, Number(state.designStep || 0)))];
        const offset = Math.max(20, Math.min(64, length * 5));
        const predictionFeedback = state.predictionFeedback || "";
        const transferFeedback = state.transferFeedback || "";
        const legScale = 8;
        return `<section class="sim-prism-lab" aria-label="直角三角柱表面積與體積互動"><h5>先預測：柱長由 ${config.initialLength} cm 增至 ${config.targetLength} cm</h5><p>底面兩股 ${base.legA}、${base.legB} cm，斜邊 ${base.hypotenuse} cm。提交前公式與數值保持隱藏。</p>${geometryChoices("prediction", [["A", `表面積增加 ${area * (config.targetLength-config.initialLength)} cm²，體積增加 ${perimeter * (config.targetLength-config.initialLength)} cm³`], ["B", `表面積增加 ${perimeter * (config.targetLength-config.initialLength)} cm²，體積增加 ${area * (config.targetLength-config.initialLength)} cm³`], ["C", "表面積與體積都不變"]], state.predictionChoice)}<button type="button" class="sim-button" data-geometry-action="submit-prediction">提交預測並解鎖模型</button><p class="sim-status" aria-live="polite">${esc(predictionFeedback)}</p>${unlocked ? `<div class="sim-prism-unlocked"><nav class="sim-design-steps" aria-label="單元探索步驟">${design.steps.map((item,index)=>`<button type="button" data-design-step="${index}" ${index===Number(state.designStep||0)?'aria-current="step"':''}>${index+1}. ${esc(item.action)}</button>`).join("")}</nav><p><b>目前推理步驟：</b>${esc(step.reason)}</p><p class="sim-prism-equation" aria-live="polite">${esc(step.equation)}</p><div class="sim-prism-visuals"><figure><svg viewBox="0 0 260 190" role="img" aria-label="${base.legA}-${base.legB}-${base.hypotenuse}直角三角柱示意，柱長${length}公分"><polygon points="35,155 35,${155-base.legB*legScale} ${35+base.legA*legScale},155" class="sim-shape"/><polygon points="${35+offset},${155-offset/3} ${35+offset},${155-base.legB*legScale-offset/3} ${35+base.legA*legScale+offset},${155-offset/3}" class="sim-shape sim-line-secondary"/><line x1="35" y1="155" x2="${35+offset}" y2="${155-offset/3}" class="sim-axis"/><text x="40" y="178">${base.legA}-${base.legB}-${base.hypotenuse}</text><text x="${55+offset/2}" y="72">柱長 ${length} cm</text></svg><figcaption>兩個全等三角端面沿柱長連接。</figcaption></figure><figure><div class="sim-net" role="img" aria-label="三片側面長方形的展開表徵">${[base.legA,base.legB,base.hypotenuse].map((side)=>`<span style="min-width:${Math.max(32,side*3)}px;height:52px">邊 ${side}<br>長 ${length}</span>`).join("")}</div><figcaption>三片側面寬分別等於底面三邊；總和由周長控制。</figcaption></figure></div><table><caption>端面、側面與容量分開計算</caption><thead><tr><th>量</th><th>幾何依據</th><th>結果</th></tr></thead><tbody><tr><th>兩個端面</th><td>2×${base.legA}×${base.legB}÷2</td><td>${2*area} cm²</td></tr><tr><th>三片側面</th><td>${perimeter}×${length}</td><td>${perimeter*length} cm²</td></tr><tr><th>表面積</th><td>兩端面＋三側面</td><td><output data-prism-surface-area>${surface}</output> cm²</td></tr><tr><th>體積</th><td>${area}×${length}</td><td><output data-prism-volume>${volume}</output> cm³</td></tr></tbody></table>${slider("prismLength","直角柱長度",length,config.sliderMin,config.sliderMax,1," cm")}<p class="sim-status" aria-live="polite">${esc(step.feedback)}</p><h6>遷移題：重新求新底面的面積與周長</h6><p>底面為 ${transfer.baseTriangle.legA}-${transfer.baseTriangle.legB}-${transfer.baseTriangle.hypotenuse} 直角三角形，柱長 ${transfer.length} cm。選出表面積與體積：</p>${geometryChoices("transfer", [["A",`${transferPerimeter*transfer.length} cm²、${transferArea*transfer.length} cm³`],["B",`${transferSurface} cm²、${transferArea*transfer.length} cm³`],["C",`${transferSurface} cm²、${transferSurface} cm³`]],state.transferChoice)}<button type="button" class="sim-button" data-geometry-action="submit-transfer">檢查遷移答案</button><p class="sim-status" aria-live="polite">${esc(transferFeedback)}</p></div>` : "<p>提交預測後才會解鎖可操作的展開表徵與逐面計算。</p>"}</section>`;
      }
      if (lesson.simulation.model === "s9-13-prism-surface-volume") {
        const length = clamp(state.prismLength, 3, 8);
        const surfaceArea = 12 + 12 * length;
        const volume = 6 * length;
        const offsetX = 105 + length * 6;
        const offsetY = -30;
        const design = lesson.simulation.learningDesign;
        const currentStep = clamp(state.designStep, 0, design.steps.length - 1);
        const step = design.steps[currentStep];
        const predictionOptions = [
          ["A", "表面積增加 12 cm²，體積增加 24 cm³"],
          ["B", "表面積增加 24 cm²，體積增加 12 cm³"],
          ["C", "表面積與體積都不變"]
        ];
        const predictionFeedback = state.predictionFeedback || (state.predictionSubmitted
          ? state.predictionChoice === "B"
            ? "預測正確。底面仍是 3-4-5 直角三角形；柱長增加 2 cm，三片側面總面積按周長 12 cm 增加 24 cm²，體積按底面積 6 cm² 增加 12 cm³。"
            : "預測不符。先看兩個量各自乘上的固定幾何量：側面增加量由底面周長 12 cm 決定；體積增加量由底面積 6 cm² 決定。"
          : "提交預測後才會顯示公式與數值；先比較「每增加 1 cm 柱長」會多出多少側面面積與內部容量。");
        const transferFeedback = state.transferFeedback || (state.transferSubmitted
          ? state.transferChoice === "B"
            ? "核算正確：底面積 (5×12÷2)=30 cm²，底面周長 5+12+13=30 cm；兩個端面共 60 cm²，側面共 30×2=60 cm²，表面積 120 cm²，體積 30×2=60 cm³。"
            : "再核對一次：先算直角三角形底面積與三邊周長；表面積＝兩個底面＋底面周長×柱長，體積＝底面積×柱長。"
          : "先獨立計算，再選一組表面積與體積。這個新截面是 5-12-13 直角三角形，柱長 2 cm。");
        const geometryChoices = (kind, options, selected) => `<div class="sim-actions" role="group" aria-label="${kind === "prediction" ? "柱長變化預測" : "遷移題答案"}">${options.map(([key, text]) => `<button type="button" data-geometry-${kind}="${key}" aria-pressed="${selected === key}">${key}. ${esc(text)}</button>`).join("")}</div>`;
        return `${designed}<section class="sim-prism-lab" aria-label="直角三角柱表面積與體積模型"><h5>先預測：柱長由 4 cm 增至 6 cm</h5><p>底面固定為兩股 3 cm、4 cm 的直角三角形。提交前先選擇變化量；公式和計算結果會暫時隱藏。</p>${geometryChoices("prediction", predictionOptions, state.predictionChoice)}<button type="button" class="sim-button" data-geometry-action="submit-prediction">提交預測並解鎖模型</button><p class="sim-status" aria-live="polite">${esc(predictionFeedback)}</p>${state.predictionSubmitted ? `<div class="sim-prism-unlocked"><nav class="sim-design-steps" aria-label="單元探索步驟">${design.steps.map((item, index) => `<button type="button" data-design-step="${index}" ${index === currentStep ? 'aria-current="step"' : ""}>${index + 1}. ${esc(item.action)}</button>`).join("")}</nav><p><b>目前推理步驟：</b>${esc(step.reason)}</p><p class="sim-prism-equation" aria-live="polite">${esc(step.equation)}</p><div class="sim-prism-visuals"><figure><svg viewBox="0 0 360 205" role="img" aria-label="直角三角柱立體示意；前後兩個 3、4、5 直角三角底面相隔 ${length} 公分"><polygon points="42,150 42,70 112,150" class="sim-shape"/><polygon points="${42 + offsetX},${150 + offsetY} ${42 + offsetX},${70 + offsetY} ${112 + offsetX},${150 + offsetY}" class="sim-shape sim-line-secondary"/><polygon points="42,150 42,70 ${42 + offsetX},${70 + offsetY} ${42 + offsetX},${150 + offsetY}" class="sim-line"/><polygon points="42,70 112,150 ${112 + offsetX},${150 + offsetY} ${42 + offsetX},${70 + offsetY}" class="sim-dash"/><polygon points="112,150 42,150 ${42 + offsetX},${150 + offsetY} ${112 + offsetX},${150 + offsetY}" class="sim-line-secondary"/><line x1="42" y1="150" x2="${42 + offsetX}" y2="${150 + offsetY}" class="sim-axis"/><text x="52" y="185">底面 3-4-5</text><text x="${60 + offsetX / 2}" y="120">柱長 ${length} cm</text></svg><figcaption>前、後兩個三角底面；三個側面沿柱長延伸。</figcaption></figure><figure><svg viewBox="0 0 360 180" role="img" aria-label="三角柱展開圖由兩個 3、4、5 直角三角形和寬 3、4、5 公分、長 ${length} 公分的三個長方形組成"><rect x="58" y="70" width="48" height="${length * 8}" class="sim-shape"/><rect x="106" y="70" width="64" height="${length * 8}" class="sim-line"/><rect x="170" y="70" width="80" height="${length * 8}" class="sim-dash"/><polygon points="106,70 170,70 106,22" class="sim-line-secondary"/><polygon points="106,${70 + length * 8} 170,${70 + length * 8} 106,${118 + length * 8}" class="sim-line-secondary"/><text x="70" y="${84 + length * 8}">3</text><text x="132" y="${84 + length * 8}">4</text><text x="204" y="${84 + length * 8}">5</text><text x="258" y="90">長方形高＝${length} cm</text><text x="107" y="16">兩個全等三角底面</text></svg><figcaption>展開圖中的三個長方形寬依序是底面三邊 3、4、5 cm。</figcaption></figure></div><div class="sim-table-wrap"><table><caption>逐面計算與內部容量同步對照</caption><thead><tr><th scope="col">量</th><th scope="col">幾何依據</th><th scope="col">代入柱長 ${length} cm</th><th scope="col">結果</th></tr></thead><tbody><tr><th scope="row">兩個三角底面</th><td>2×(3×4÷2)</td><td>12</td><td>12 cm²</td></tr><tr><th scope="row">三個側面</th><td>(3+4+5)×柱長</td><td>12×${length}</td><td>${12 * length} cm²</td></tr><tr><th scope="row">表面積</th><td>兩底面＋側面</td><td>12+12×${length}</td><td><output data-prism-surface-area>${surfaceArea}</output> cm²</td></tr><tr><th scope="row">體積</th><td>底面積×柱長</td><td>6×${length}</td><td><output data-prism-volume>${volume}</output> cm³</td></tr></tbody></table></div>${slider("prismLength", "直角柱長度", length, 3, 8, 1, " cm")}<p class="sim-caption">調整柱長後，立體示意、展開圖、側面總和、表面積和體積同步更新。這裡只呈現課綱範圍內的直角柱體積，不外推圓錐或角錐體積。</p><p class="sim-status" aria-live="polite">${esc(step.feedback)}</p><h6>遷移題：換成不同底面</h6><p>一個直角柱的底面是兩股 5 cm、12 cm、斜邊 13 cm 的直角三角形，柱長 2 cm。哪組是「表面積、體積」？</p>${geometryChoices("transfer", [["A", "90 cm²、60 cm³"], ["B", "120 cm²、60 cm³"], ["C", "120 cm²、120 cm³"]], state.transferChoice)}<button type="button" class="sim-button" data-geometry-action="submit-transfer">檢查遷移答案</button><p class="sim-status" aria-live="polite">${esc(transferFeedback)}</p></div>` : "<p>提交一項預測後，才會解鎖可操作的展開圖與數值表。</p>"}</section>`;
      }
      const area = state.base * state.height / 2;
      return `${designed}<div class="sim-stage"><svg viewBox="0 0 360 220" role="img" aria-label="底為 ${state.base}、高為 ${state.height} 的三角形"><polygon points="70,180 ${70 + state.base * 18},180 70,${180 - state.height * 18}" class="sim-shape"/><line x1="70" y1="${180 - state.height * 18}" x2="70" y2="180" class="sim-dash"/><text x="180" y="30" text-anchor="middle">面積 = 底 × 高 ÷ 2 = ${area}</text></svg></div>${slider("base", "底", state.base, 1, 14)}${slider("height", "高", state.height, 1, 10)}`;
    }
    if (engine === "math-data-lab") {
      const values = [state.a, state.b, state.c], mean = (values.reduce((sum, value) => sum + value, 0) / values.length).toFixed(1);
      return `${designed}<div class="sim-stage"><div class="sim-bars">${values.map((value, index) => `<div><i style="height:${value * 10}px"></i><span>資料 ${index + 1}<br>${value}</span></div>`).join("")}</div><p>平均數 = <b>${mean}</b></p></div>${slider("a", "資料 1", state.a, 0, 15)}${slider("b", "資料 2", state.b, 0, 15)}${slider("c", "資料 3", state.c, 0, 15)}`;
    }
    if (engine === "math-probability-lab") {
      const rate = state.trials ? Math.round(state.hits / state.trials * 100) : 0;
      return `${designed}<div class="sim-stage"><p>試驗 ${state.trials} 次，事件出現 <b>${state.hits}</b> 次。</p><p class="sim-result">目前實驗頻率：${rate}%</p><button type="button" class="sim-button" data-sim-action="run-trials">進行一輪試驗</button></div>${slider("trials", "每輪試驗次數", state.trials, 5, 100, 5)}`;
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
      if (lesson.simulation.model === "rutherford-scattering") {
        const proximity = clamp(Number(state.impactProximity || 3), 1, 5);
        const evidenceChoice = state.rutherfordEvidence || "";
        const near = proximity >= 4;
        const far = proximity <= 2;
        const pathLabel = near ? "大角度偏折較明顯" : far ? "幾乎直行" : "小角度偏折";
        const feedback = near
          ? "d 變小：α 粒子更靠近原子核，正電排斥較強，路徑彎曲更明顯。"
          : far
            ? "d 變大：α 粒子離原子核較遠，正電排斥較弱，路徑接近直行。"
            : "中等 d：α 粒子受到中等程度的排斥，路徑出現偏折。";
        const y1 = 88;
        const c1 = near ? 30 : far ? 76 : 58;
        const y2 = 145;
        const c2 = near ? 225 : far ? 154 : 188;
        const evidenceButton = (key,label) => `<button type="button" data-rutherford-action="evidence" data-value="${key}" aria-pressed="${evidenceChoice===key}">${label}</button>`;
        return `<section class="sim-rutherford sim-rutherford-lab" aria-label="拉塞福 α 粒子散射視覺實驗室">
          <header class="rutherford-hero"><div class="rutherford-breadcrumb">自然科 <span>›</span> 理化 <span>›</span> Aa-Ⅳ-1</div>
            <div><span class="sim-kicker">Aa-Ⅳ-1｜原子模型演變</span><h5>用 α 粒子散射，把看不見的原子核逼出來</h5><p>直接改變 α 粒子與原子核的距離，觀察路徑如何改變，再用真正的金箔散射證據推論原子結構。</p></div>
            <div class="rutherford-goals"><b>學習目標</b><span>能描述三類散射現象</span><span>能由證據推論核式結構</span><span>不把模型圖當成原子照片</span></div>
          </header>
          <div class="rutherford-workbench"><div class="rutherford-grid">
            <aside class="rutherford-panel prediction-panel question-panel">
              <span class="step-badge">1</span><h6>先看問題</h6>
              <p class="question-lead">α 粒子離原子核的<strong>最近通過距離 d</strong> 改變時，路徑會怎麼變？</p>
              <div class="cause-chain"><span>d 遠</span><b>→</b><span>排斥較弱</span><b>→</b><span>接近直行</span></div>
              <p class="question-hint">不用先猜答案。下一步直接拖動 d，自己看出規律。</p>
            </aside>
            <div class="rutherford-panel control-panel">
              <span class="step-badge">2</span><h6>拖動 d，觀察路徑</h6>
              <p>只改變 α 粒子與原子核的<strong>最近通過距離 d</strong>；其他條件固定。</p>
              <label class="rutherford-distance"><span>最近通過距離 d（定性等級） <output data-sim-output="impactProximity">${proximity}</output></span><input data-sim-control="impactProximity" type="range" min="1" max="5" step="1" value="${proximity}"><div><span>遠</span><span>中</span><span>近</span></div></label>
              <div class="distance-compare"><span>遠：幾乎直行</span><span>中：偏折</span><span>近：大角度偏折</span></div>
            </div>
            <figure class="rutherford-stage rutherford-panel">
              <figcaption><span class="step-badge">3</span><b>觀察同一顆 α 粒子：d 改變，路徑怎麼變？</b></figcaption>
              <svg viewBox="0 0 720 360" role="img" aria-label="單一 α 粒子最近通過距離 d 等級 ${proximity} 的路徑變化">
                <defs>
                  <radialGradient id="nucleusGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="currentColor" stop-opacity=".95"/><stop offset=".45" stop-color="currentColor" stop-opacity=".5"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></radialGradient>
                  <marker id="alphaArrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0,0 L0,8 L8,4 z" fill="currentColor"/></marker>
                </defs>
                <circle cx="470" cy="180" r="105" class="nucleus-ring"/><circle cx="470" cy="180" r="72" class="nucleus-ring"/><circle cx="470" cy="180" r="42" class="nucleus-ring"/>
                <circle cx="470" cy="180" r="72" fill="url(#nucleusGlow)" opacity=".18"/>
                <circle cx="470" cy="180" r="26" class="nucleus-core"/><text x="470" y="187" text-anchor="middle" class="nucleus-plus">＋</text>
                <text x="470" y="230" text-anchor="middle" class="nucleus-label">原子核（集中正電）</text>
                <g class="alpha-source"><circle cx="92" cy="${near ? 190 : far ? 92 : 140}" r="11"/><text x="55" y="48">追蹤同一顆 α 粒子</text></g>
                ${far
                  ? '<path d="M108 92 C280 92 450 92 660 86" class="alpha-path straight active-particle" marker-end="url(#alphaArrow)"/><text x="250" y="72" class="particle-state-label">d 遠 → 排斥弱 → 幾乎直行</text>'
                  : near
                    ? '<path d="M108 190 C290 190 400 190 430 181 C457 173 420 112 300 58" class="alpha-path rare active-particle" marker-end="url(#alphaArrow)"/><text x="175" y="235" class="particle-state-label">d 近 → 排斥強 → 大角度偏折</text>'
                    : '<path d="M108 140 C285 140 390 140 430 125 C475 108 535 74 650 62" class="alpha-path bend active-particle" marker-end="url(#alphaArrow)"/><text x="205" y="112" class="particle-state-label">d 中 → 排斥增加 → 明顯偏折</text>'}
                <line x1="470" y1="180" x2="470" y2="${near ? 190 : far ? 92 : 140}" class="distance-guide"/>
                <text x="485" y="${near ? 165 : far ? 130 : 150}" class="distance-label">d</text>
              </svg>
              <div class="rutherford-live">${esc(feedback)}</div>
              <p class="sim-caption">這裡只追蹤一顆 α 粒子，用來看清楚 d 與偏折的因果關係；下一步才看大量 α 粒子的真實金箔散射統計。</p>
            </figure>
            <aside class="rutherford-panel evidence-panel">
              <span class="step-badge">4</span><h6>對照實驗證據</h6>
              <div class="evidence-cards"><article class="evidence-straight"><span class="evidence-symbol">→</span><div><b>多數直行</b><p>大多數 α 粒子幾乎不偏折，直接通過金箔。</p></div></article><article class="evidence-bend"><span class="evidence-symbol">↗</span><div><b>少數偏折</b><p>少數 α 粒子偏折一個小角度。</p></div></article><article class="evidence-rare"><span class="evidence-symbol">↩</span><div><b>極少數大角度偏折</b><p>極少數甚至反彈回來。</p></div></article></div>
            </aside>
            <div class="rutherford-panel inference-panel">
              <span class="step-badge">5</span><h6>你能推出什麼？</h6>
              <p class="inference-callout">💡 原子大部分是空間；<br>正電與大部分質量集中在很小的區域（原子核）。</p><p>哪一個結論最符合上面的觀察？</p>
              <div class="sim-actions">
                ${evidenceButton("spread","正電均勻分散在整個原子")}
                ${evidenceButton("nucleus","原子大部分是空間；正電與大部分質量集中在很小的原子核")}
              </div>
              <p class="sim-status" role="status">${esc(state.rutherfordEvidenceFeedback || "用「多數直行＋極少數強偏折」一起判斷。")}</p>
            </div>
          </div></div>
          <section class="atomic-model-timeline" aria-label="原子模型演變時間軸">
            <div class="timeline-heading"><span class="step-badge">6</span><div><h6>原子模型的演變</h6><p>模型是基於當時證據提出的解釋，不是實際拍攝的照片。</p></div></div>
            <div class="model-cards">
              <article><div class="model-icon dalton"><i></i><span class="model-caption">實心球</span></div><b>道耳頓</b><small>實心球模型</small><p>原子是物質的基本單位。</p></article>
              <span class="model-arrow">→</span>
              <article><div class="model-icon thomson"><i></i><i></i><i></i><i></i><span class="model-caption">電子嵌在正電背景</span></div><b>湯姆森</b><small>正電背景＋電子</small><p>陰極射線顯示原子可再分。</p></article>
              <span class="model-arrow">→</span>
              <article class="is-current"><div class="model-icon rutherford"><i></i><em>＋</em><span class="model-caption">小原子核＋大片空間</span></div><b>拉塞福</b><small>核式模型</small><p>金箔散射迫使正電集中到小區域。</p></article>
              <span class="model-arrow">→</span>
              <article><div class="model-icon bohr"><i></i><i></i><em>＋</em><span class="model-caption">特定能階</span></div><b>波耳</b><small>能階模型</small><p>線光譜要求離散能量狀態。</p></article>
              <span class="model-arrow">→</span>
              <article><div class="model-icon quantum"><i></i><span class="model-caption">電子雲機率分布</span></div><b>現代量子模型</b><small>機率分布</small><p>電子以機率分布描述。</p></article>
            </div>
          </section>
        </section>`;
      }
      const phase = state.temperature < 33 ? "粒子較緊密" : state.temperature < 67 ? "粒子可互相滑動" : "粒子間距較大";
      return `<div class="sim-stage"><div class="sim-particles" style="--particle-space:${state.spacing * 2}px;--particle-motion:${Math.max(.2, 1 - state.temperature / 120)}s">${Array.from({ length: 24 }, (_, i) => `<i style="--i:${i}"></i>`).join("")}</div><p>${phase}；這是用來比較變因改變的粒子模型。</p></div>${slider("temperature", "溫度條件", state.temperature, 0, 100, 1, "%")}${slider("spacing", "初始間距", state.spacing, 1, 8)}`;
    }
    if (engine === "science-life-system") {
      if (lesson.simulation.model === "circulation" && window.heartAnatomyLab) return `${window.heartAnatomyLab()}${slider("rate", "循環速率", state.rate, 40, 120, 5, " bpm")}`;
      if (lesson.simulation.model === "pond-food-web") {
        const level = clamp(state.disturbance, 0, 2);
        const observations = [
          ["未擾動示意", "水草 → 水生昆蟲 → 小魚", "藻類 → 水生昆蟲 → 小魚", "枯葉／遺體 → 分解者 → 可再利用物質 → 水草"],
          ["局部移除部分水草", "水草路徑減少；藻類仍可作為部分水生昆蟲的食物來源", "小魚可沿未受影響的取食關係取得食物", "分解者仍處理枯葉與遺體；實際變化須觀察，模型不預測族群數"],
          ["水草大幅減少的假設情境", "水草相關取食路徑變少", "藻類路徑仍存在，但不代表能完全替代水草功能", "分解者與營養物質路徑仍需另行觀察；不能由此模型推定池塘必然崩解"]
        ][level];
        return `${designed}<section class="sim-stage sim-pond-web" aria-label="池塘生物角色與取食關係模型"><h5>池塘關係圖（概念示意，不是實測食物網）</h5><p>箭頭表示「作為食物／物質來源 → 使用者」。先看每個生物角色，再調整水草擾動情境；本模型只檢查可能受影響的關係，不計算真實族群數或保證生態結果。</p><ul class="sim-pond-roles"><li>水草、藻類：生產者，提供有機物來源</li><li>水生昆蟲、小魚：消費者，沿取食關係取得能量</li><li>分解者：分解遺體與排遺，使物質回到環境</li></ul><label class="sim-control"><span>水草擾動情境 <output data-sim-output="disturbance">${level === 0 ? "未移除" : level === 1 ? "局部移除" : "大幅減少（假設）"}</output></span><input data-sim-control="disturbance" type="range" min="0" max="2" step="1" value="${level}" aria-label="水草擾動情境"></label><h6>${esc(observations[0])}</h6><ul>${observations.slice(1).map(item => `<li>${esc(item)}</li>`).join("")}</ul><p class="sim-caption">判讀提醒：模型顯示的是待檢驗的可能關係。要判斷穩定性，還需實際記錄生物數量、環境條件、觀察時間與擾動範圍；一條替代取食路徑不等於功能完全替代。</p></section>`;
      }
      if (lesson.simulation.model === "plant-transport") {
        const sourceLabel = state.source === "storage" ? "儲存器官（例如塊莖）" : "成熟葉片";
        const sinkLabels = { root: "根", shoot: "生長中的芽／嫩梢", fruit: "果實" };
        const sinkLabel = sinkLabels[state.sink] || sinkLabels.fruit;
        const transpirationLabel = ["較弱", "偏弱", "中等", "偏強", "較強"][clamp(state.transpiration, 1, 5) - 1];
        const choices = (key, options, current, labelText) => `<div class="sim-actions" role="group" aria-label="${esc(labelText)}">${options.map(([value, label]) => `<button type="button" data-transport-choice="${key}" data-value="${value}" aria-pressed="${current === value}">${esc(label)}</button>`).join("")}</div>`;
        return `${designed}<section class="sim-plant-transport" aria-label="植物維管束運輸概念模型"><h5>分開追蹤水路與有機養分路徑</h5><p>木質部：根吸收的水與無機鹽，沿根—莖—葉方向示意；蒸散條件目前設定為<strong>${transpirationLabel}</strong>。此控制只改變概念情境標籤，不計算真實運輸速率或水量。</p><p class="sim-plant-xylem" aria-live="polite">水／無機鹽　根 → 莖（木質部）→ 葉</p><h6>選擇有機養分的來源與需求位置</h6>${choices("source", [["leaf", "成熟葉片作來源"], ["storage", "儲存器官作來源"]], state.source, "有機養分來源")}${choices("sink", [["root", "根作需求端"], ["shoot", "嫩梢作需求端"], ["fruit", "果實作需求端"]], state.sink, "有機養分需求端")}<p class="sim-plant-phloem" aria-live="polite">韌皮部概念路徑：${esc(sourceLabel)} → ${esc(sinkLabel)}。方向由來源端與需求端的情境決定，不是固定向上或向下。</p><p class="sim-caption">這是路徑概念圖，不表示流量、速率或各器官實際比例；植物狀態與季節改變時，來源／需求角色也可能改變。環剝、染色與切片只能分別支持有限推論，不能單靠單一觀察證明整個機制。</p>${slider("transpiration", "蒸散條件（1＝較弱，5＝較強；非實測量）", state.transpiration, 1, 5)}</section>`;
      }
      const balance = state.rate - state.demand;
      return `<div class="sim-stage"><div class="sim-flow"><i style="width:${Math.min(100, state.rate)}%"></i></div><p>運輸條件 ${state.rate}；需求條件 ${state.demand}；比較差：<b>${balance}</b></p><p class="sim-caption">以單一條件改變觀察系統的相對變化；實際生物系統需受更多證據限制。</p></div>${slider("rate", "運輸條件", state.rate, 0, 100)}${slider("demand", "需求條件", state.demand, 0, 100)}`;
    }
    if (engine === "science-earth-space" && lesson.simulation.model === "fa-iv-4-atmospheric-temperature-profile") {
      return `${designed}${atmosphereProfile(state.profileScenario || "baseline")}`;
    }
    if (engine === "science-earth-space") {
      const daylight = (12 + Math.sin(state.position * Math.PI / 180) * Math.sin(state.tilt * Math.PI / 180) * 8).toFixed(1);
      return `<div class="sim-stage"><div class="sim-orbit"><i style="transform:rotate(${state.position}deg)"></i><b style="transform:rotate(${state.tilt}deg)"></b></div><p>模型估計日照長度：<b>${daylight}</b> 小時</p></div>${slider("tilt", "傾角", state.tilt, 0, 45, .5, "°")}${slider("position", "公轉位置", state.position, 0, 360, 15, "°")}`;
    }
    if (engine === "concept-explorer" && lesson.simulation.model === "ecosystem-scale-boundary") {
      const scenes = {
        pond: { label: "校園池塘", individual: ["一隻白腹樹蛙"], population: ["同一時段、池塘東側的12隻同種青蛙"], community: ["青蛙、蜻蜓、睡蓮、藻類與其他微生物"], ecosystem: ["生物群集，以及水溫26°C、光照、水質與底泥等環境條件"], biosphere: ["全球各地的生物群集及其可居住環境；池塘樣本只是其中一小部分"] },
        shore: { label: "潮間帶", individual: ["岩面上的一隻藤壺"], population: ["同一潮位帶、同一觀察時段的同種藤壺"], community: ["藤壺、螃蟹、藻類及其他共同生活的物種"], ecosystem: ["海岸生物群集，以及潮汐、鹽度、岩面乾濕與溫度等環境條件"], biosphere: ["全球各地的生物群集及其可居住環境；單一潮間帶樣區不能代表全部"] }
      };
      const scales = [
        ["individual", "個體", "單一生物"], ["population", "族群", "同種個體＋地區＋時間"], ["community", "群集", "同地區多物種族群"], ["ecosystem", "生態系", "生物群集＋非生物環境"], ["biosphere", "生物圈", "全球生命及其可居住環境"]
      ];
      const site = scenes[state.site] ? state.site : "pond";
      const scale = scales.some(([key]) => key === state.scale) ? state.scale : "individual";
      const scene = scenes[site];
      const selected = scales.find(([key]) => key === scale);
      const evidence = scene[scale];
      return `${designed}<section class="sim-stage sim-ecosystem-scale" aria-label="生態層級觀察模型"><p>先選場域，再切換觀察邊界。每次切換都要問：目前納入哪些對象與條件？</p><fieldset class="sim-eco-controls"><legend>觀察場域</legend>${[["pond", "校園池塘"], ["shore", "潮間帶"]].map(([key, text]) => `<button type="button" data-eco-site="${key}" aria-pressed="${site === key}">${text}</button>`).join("")}</fieldset><fieldset class="sim-eco-controls"><legend>觀察尺度</legend>${scales.map(([key, text]) => `<button type="button" data-eco-scale="${key}" aria-pressed="${scale === key}">${text}</button>`).join("")}</fieldset><div class="sim-eco-evidence" aria-live="polite" aria-atomic="true"><h5>${esc(scene.label)}｜${esc(selected[1])}</h5><p><b>目前證據：</b>${esc(evidence[0])}</p><p><b>判讀依據：</b>${esc(selected[2])}</p>${scale === "ecosystem" ? "<p>請同時保留生物群集與非生物環境，並說明兩者在研究範圍中的關係。</p>" : ""}${scale === "biosphere" ? "<p>外推前須比較多地點與時間的證據；本地樣區不可直接代替全球資料。</p>" : ""}</div><p class="sim-eco-note">生產者／消費者／分解者是<strong>功能</strong>分類；個體／族群／群集／生態系／生物圈是<strong>尺度</strong>層級，兩者不可混為一談。</p></section>`;
    }
    if (engine === "concept-explorer" && lesson.simulation.model === "ca-iv-2-solution-identification") {
      const samples = { X: "carbonate", Y: "acid", Z: "salt" };
      const controlResults = { unknown: "未知樣品", blank: "空白對照（水）", acid: "已知酸性對照", carbonate: "已知碳酸鹽對照" };
      const results = {
        litmus: {
          carbonate: ["石蕊呈藍色，顯示此份水溶液呈鹼性。", "在本題候選範圍內，支持碳酸鈉；石蕊本身只提供酸鹼線索。"],
          acid: ["石蕊呈紅色，顯示此份水溶液呈酸性。", "在本題候選範圍內，支持稀鹽酸；不能只憑紅色推論濃度或純度。"],
          salt: ["石蕊沒有明顯轉紅或轉藍。", "在本題候選範圍內，支持接近中性的食鹽水；仍需確認控制條件。"]
        },
        carbonateCheck: {
          carbonate: ["加入虛擬稀酸後出現氣泡；氣體通入石灰水後變混濁。", "兩個相連觀察支持生成二氧化碳，符合碳酸鹽候選；仍須有空白及已知對照。"],
          acid: ["沒有觀察到持續產氣，石灰水維持澄清。", "此結果不支持碳酸鹽，但單一陰性結果不能直接證明樣品是稀鹽酸。"],
          salt: ["沒有觀察到持續產氣，石灰水維持澄清。", "此結果不支持碳酸鹽；食鹽水與其他不產氣候選仍需用另一項性質區分。"]
        }
      };
      const sample = state.control === "unknown" ? state.sample : state.control;
      const kind = state.control === "acid" ? "acid" : state.control === "carbonate" ? "carbonate" : state.control === "blank" ? "blank" : samples[sample];
      const observation = !state.testRun ? null : state.control === "blank"
        ? ["空白對照沒有顯色或產氣變化。", "空白提供背景基準，不能用來判定未知樣品身分。"]
        : results[state.test][kind];
      return `${designed}<section class="sim-stage sim-chemical-id" aria-label="未知溶液化學性質鑑定模擬"><h5>虛擬微量鑑定台</h5><p>本區只模擬已知候選的反應結果，不是實驗步驟或真實化學品操作指引。候選：食鹽水、稀鹽酸、稀碳酸鈉。</p><fieldset><legend>設定樣品與檢驗</legend><label>樣品對照 <select data-chemical-control="control" aria-label="樣品對照">${Object.entries(controlResults).map(([value,text]) => `<option value="${value}" ${state.control === value ? "selected" : ""}>${text}</option>`).join("")}</select></label>${state.control === "unknown" ? `<label>未知瓶 <select data-chemical-control="sample" aria-label="未知樣品瓶">${["X","Y","Z"].map(value => `<option value="${value}" ${state.sample === value ? "selected" : ""}>${value} 瓶</option>`).join("")}</select></label>` : ""}<label>檢驗方法 <select data-chemical-control="test" aria-label="檢驗方法"><option value="litmus" ${state.test === "litmus" ? "selected" : ""}>紫色石蕊初篩</option><option value="carbonateCheck" ${state.test === "carbonateCheck" ? "selected" : ""}>虛擬加酸與二氧化碳確認</option></select></label><button type="button" data-chemical-action="run">執行虛擬檢驗</button></fieldset><div class="sim-chemical-result" aria-live="polite"><p><b>直接觀察：</b>${esc(observation?.[0] || "先預測結果，再執行虛擬檢驗。")}</p><p><b>候選判讀：</b>${esc(observation?.[1] || "保留目前候選，不以外觀猜測身分。")}</p></div><p>推理提醒：先寫觀察，再寫推論；氣泡、顏色或陰性結果都不能單獨保證唯一身分。若控制組未如預期，應先檢查試劑／背景，不讀取未知樣本結論。</p></section>`;
    }
    if (engine === "math-reasoning-lab") {
      const steps = lesson.interactive?.steps || [];
      if (!steps.length) return `${designed}<p role="status">本課尚缺可操作的推理步驟。</p>`;
      const index = clamp(Number(state.reasoningStep || 0), 0, steps.length - 1);
      const step = steps[index];
      const selected = state.reasoningChoice || "";
      const correct = selected === step.answer;
      const choices = step.options.map((option, optionIndex) => { const key = String.fromCharCode(65 + optionIndex); return `<button type="button" data-reasoning-choice="${key}" aria-pressed="${selected === key}">${key}. ${esc(option)}</button>`; }).join("");
      const feedback = !selected ? "先選一個答案，再依回饋修正。" : correct ? step.feedback : "這個選擇還不符合本步條件；回看題幹中的量、關係或證據後再試一次。";
      return `${designed}<section class="sim-reasoning-lab" aria-label="數學推理實驗室"><p>${esc(lesson.interactive?.scenario || lesson.simulation.mission)}</p><p><b>進度：</b>第 ${index + 1}／${steps.length} 步</p><fieldset><legend>${esc(step.prompt)}</legend><div class="sim-actions">${choices}</div></fieldset><p class="sim-reasoning-feedback" role="status" aria-live="polite">${esc(feedback)}</p><div class="sim-actions"><button type="button" data-reasoning-nav="prev" ${index === 0 ? "disabled" : ""}>上一步</button><button type="button" data-reasoning-nav="next" ${!correct || index === steps.length - 1 ? "disabled" : ""}>下一步</button></div><p>每一步都必須先作答並讀取證據回饋；錯答不會直接揭露正解。</p></section>`;
    }
    const evidence = ["直接觀察", "模型或資料", "可檢查的限制"][state.evidence - 1];
    return `<div class="sim-stage"><ol class="sim-evidence"><li class="${state.evidence >= 1 ? "active" : ""}">直接觀察：寫下情境中可確認的條件</li><li class="${state.evidence >= 2 ? "active" : ""}">模型或資料：連結可重現的理由</li><li class="${state.evidence >= 3 ? "active" : ""}">限制：說明還不能推論什麼</li></ol><p>目前聚焦：<b>${evidence}</b></p></div>${slider("evidence", "推理階段", state.evidence, 1, 3)}`;
  };
  const render = (lesson, instance = "default") => {
    if (!lesson.simulation) return "";
    const resolvedInstance = lesson._simulationInstance || instance;
    const instanceKey = `${lesson.id}:${resolvedInstance}`;
    const simulation = { ...lesson.simulation, storageId: `${lesson.simulation.id}:${resolvedInstance}` };
    const runtimeLesson = { ...lesson, simulation, _simulationInstance: resolvedInstance };
    lessons.set(instanceKey, runtimeLesson);
    const state = read(simulation);
    const reflection = esc(state.reflection || "");
    const simulationLabel = simulation.model === "fa-iv-4-atmospheric-temperature-profile" ? "大氣溫度剖面模型" : label(simulation.engine, simulation.model);
    return `<section class="simulation" data-simulation-lesson="${esc(instanceKey)}" data-simulation-model="${esc(simulation.model || "")}" aria-label="${esc(simulationLabel)}"><header><span class="tag">${esc(simulationLabel)}</span><h4>${esc(simulation.goal)}</h4><p>${esc(simulation.mission || "先預測，再操作與解釋。")} </p></header><div class="simulation-body">${renderModel(runtimeLesson, state)}</div><footer class="sim-learning"><p><b>學習紀錄</b>：先預測，操作後再用證據解釋。</p><div class="sim-actions"><button type="button" data-sim-action="predicted">我已提出預測</button><button type="button" data-sim-action="observed">我已記錄觀察</button><button type="button" data-sim-reset>重設模型</button></div><label>我的解釋<textarea data-sim-reflection rows="3" placeholder="我改變了什麼？看見什麼？這如何支持我的解釋？">${reflection}</textarea></label><p class="sim-status" aria-live="polite">${state.status || "尚未記錄預測與觀察。"}</p><details class="sim-sources"><summary>模型依據與參考來源</summary><ul>${simulation.sourceRefs.map(url => `<li><a href="${esc(url)}" target="_blank" rel="noreferrer">${esc(url)}</a></li>`).join("")}</ul></details></footer></section>`;
  };
  const rerender = root => { const lesson = lessons.get(root.dataset.simulationLesson); if (lesson) root.outerHTML = render(lesson); };
  const update = (root, changes) => { const lesson = lessons.get(root.dataset.simulationLesson); if (!lesson) return; const instanceKey = root.dataset.simulationLesson; const parent = root.parentElement; const active = document.activeElement; const focusTarget = active?.matches("[data-sim-control]") ? ["data-sim-control", active.dataset.simControl] : active?.matches("[data-chemical-control]") ? ["data-chemical-control", active.dataset.chemicalControl] : active?.matches("[data-chemical-action]") ? ["data-chemical-action", active.dataset.chemicalAction] : active?.matches("[data-reasoning-choice]") ? ["data-reasoning-choice", active.dataset.reasoningChoice] : active?.matches("[data-reasoning-nav]") ? ["data-reasoning-nav", active.dataset.reasoningNav] : active?.matches("[data-design-step]") ? ["data-design-step", active.dataset.designStep] : active?.matches("[data-atmo-scenario]") ? ["data-atmo-scenario", active.dataset.atmoScenario] : active?.matches("[data-eco-site]") ? ["data-eco-site", active.dataset.ecoSite] : active?.matches("[data-eco-scale]") ? ["data-eco-scale", active.dataset.ecoScale] : active?.matches("[data-inequality-relation]") ? ["data-inequality-relation", active.dataset.inequalityRelation] : active?.matches("[data-ticket-action]") ? ["data-ticket-action", active.dataset.ticketAction] : active?.matches("[data-transport-choice]") ? ["data-transport-choice", active.dataset.transportChoice, active.dataset.value] : active?.matches("[data-geometry-prediction]") ? ["data-geometry-prediction", active.dataset.geometryPrediction] : active?.matches("[data-geometry-transfer]") ? ["data-geometry-transfer", active.dataset.geometryTransfer] : active?.matches("[data-geometry-action]") ? ["data-geometry-action", active.dataset.geometryAction] : active?.matches("[data-friction-action]") ? ["data-friction-action", active.dataset.frictionAction, active.dataset.value] : active?.matches("[data-torque-action]") ? ["data-torque-action", active.dataset.torqueAction, active.dataset.value] : active?.matches("[data-sim-similarity]") ? ["data-sim-similarity", active.dataset.simSimilarity, active.dataset.value] : null; const next = { ...read(lesson.simulation), ...changes }; write(lesson.simulation, next); rerender(root); if (focusTarget && parent) parent.querySelector(`[data-simulation-lesson="${instanceKey}"] [${focusTarget[0]}="${focusTarget[1]}"]${focusTarget[2] ? `[data-value="${focusTarget[2]}"]` : ""}`)?.focus(); };
  document.addEventListener("change", event => { const root = event.target.closest("[data-simulation-lesson]"); if (!root || !event.target.matches("[data-chemical-control]")) return; update(root, { [event.target.dataset.chemicalControl]: event.target.value, testRun: false }); });
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-simulation-lesson]");
    if (!root) return;
    const lesson = lessons.get(root.dataset.simulationLesson);
    if (!lesson) return;
    if (event.target.matches("[data-sim-control]")) update(root, { [event.target.dataset.simControl]: Number(event.target.value), ...(lesson.simulation.engine === "math-ticket-equation" ? { candidateVerified: false, candidateFeedback: "模型條件已改變，請重新檢查候選票價。" } : {}) });
    if (event.target.matches("[data-sim-reflection]")) { const lesson = lessons.get(root.dataset.simulationLesson); if (lesson) write(lesson.simulation, { ...read(lesson.simulation), reflection: event.target.value }); }
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-simulation-lesson]");
    if (!root) return;
    const lesson = lessons.get(root.dataset.simulationLesson); if (!lesson) return;
    if (event.target.closest("[data-sim-reset]")) { localStorage.removeItem(stateKey(lesson.simulation)); rerender(root); return; }
    if (event.target.closest('[data-chemical-action="run"]')) { update(root, { testRun: true }); return; }
    const reasoningChoice = event.target.closest("[data-reasoning-choice]");
    if (reasoningChoice) { update(root, { reasoningChoice: reasoningChoice.dataset.reasoningChoice }); return; }
    const reasoningNav = event.target.closest("[data-reasoning-nav]");
    if (reasoningNav) {
      const state = read(lesson.simulation);
      const steps = lesson.interactive?.steps || [];
      const index = clamp(Number(state.reasoningStep || 0), 0, Math.max(0, steps.length - 1));
      const direction = reasoningNav.dataset.reasoningNav;
      if (direction === "prev") update(root, { reasoningStep: Math.max(0, index - 1), reasoningChoice: "" });
      if (direction === "next" && state.reasoningChoice === steps[index]?.answer) update(root, { reasoningStep: Math.min(steps.length - 1, index + 1), reasoningChoice: "" });
      return;
    }
    const rutherfordAction=event.target.closest("[data-rutherford-action]");
    if(rutherfordAction && lesson.simulation.model==="rutherford-scattering"){
      const action=rutherfordAction.dataset.rutherfordAction,value=rutherfordAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{rutherfordPrediction:value,rutherfordPredictionFeedback:""});return;}
      if(action==="submit-prediction"){
        update(root,state.rutherfordPrediction
          ? {rutherfordPredictionSubmitted:true,rutherfordPredictionFeedback:state.rutherfordPrediction==="large"?"預測已記錄。現在拖動距離 d，觀察靠近原子核時路徑如何改變。":"預測已記錄。現在用距離 d 檢查你的預測，而不是直接改答案。"}
          : {rutherfordPredictionFeedback:"請先選擇一項預測。"});
        return;
      }
      if(action==="evidence"){
        update(root,value==="nucleus"
          ? {rutherfordEvidence:value,rutherfordEvidenceFeedback:"正確：多數直行表示原子大部分是空間；極少數強烈偏折表示正電與大部分質量集中在很小的原子核。"}
          : {rutherfordEvidence:value,rutherfordEvidenceFeedback:"再看極少數的大角度偏折：若正電均勻分散，就很難產生這種強烈排斥。"});
        return;
      }
    }
    const earthSphereAction=event.target.closest("[data-earth-sphere-action]");
    if(earthSphereAction && lesson.simulation.model==="fa-iv-1-earth-spheres"){const action=earthSphereAction.dataset.earthSphereAction,value=earthSphereAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{earthPrediction:value,earthFeedback:""});return;}if(action==="submit-prediction"){update(root,state.earthPrediction?{predictionSubmitted:true,earthFeedback:state.earthPrediction==="multi"?"預測已記錄。逐一切換圈層，找出降雨侵蝕跨越哪些部分。":"預測已記錄。逐一切換三圈層，追蹤雨水與岩石的交互作用。"}:{earthFeedback:"請先選擇預測。"});return;}if(action==="view"){update(root,{sphereView:value});return;}if(action==="transfer"){update(root,value==="cross"?{transferChoice:value,transferFeedback:"正確：火山物質由岩石圈進入大氣圈，是跨圈層交互作用。"}:{transferChoice:value,transferFeedback:"看箭頭：圈層之間會交換物質與能量。"});return;}}
    const machineAction=event.target.closest("[data-machine-action]");
    if(machineAction && lesson.simulation.model==="eb-iv-7-simple-machines"){const action=machineAction.dataset.machineAction,value=machineAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{machinePrediction:value,machineFeedback:""});return;}if(action==="submit-prediction"){update(root,state.machinePrediction?{predictionSubmitted:true,machineFeedback:state.machinePrediction==="half"?"預測已記錄。切換定滑輪與動滑輪，比較輸入力和距離。":"預測已記錄。切換機械，觀察承重繩段帶來的交換。"}:{machineFeedback:"請先選擇預測。"});return;}if(action==="type"){update(root,{machineType:value});return;}if(action==="transfer"){update(root,value==="distance"?{transferChoice:value,transferFeedback:"正確：理想機械省力的同時增加施力距離，輸入功不會憑空減少。"}:{transferChoice:value,transferFeedback:"看輸入力×輸入距離；理想模型仍等於負載增加的位能。"});return;}}
    const equilibriumAction=event.target.closest("[data-equilibrium-action]");
    if(equilibriumAction && lesson.simulation.model==="eb-iv-3-static-equilibrium"){const action=equilibriumAction.dataset.equilibriumAction,value=equilibriumAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{equilibriumPrediction:value,equilibriumFeedback:""});return;}if(action==="submit-prediction"){update(root,state.equilibriumPrediction?{predictionSubmitted:true,equilibriumFeedback:state.equilibriumPrediction==="increase"?"預測已記錄。只改負載力臂，觀察 Στ。":"預測已記錄。只改力臂，用 τ=Fd 檢查。"}:{equilibriumFeedback:"請先選擇預測。"});return;}if(action==="transfer"){update(root,value==="no"?{transferChoice:value,transferFeedback:"正確：Στ=0 只保證不產生角加速度；還需 ΣF=0 才能不平移。"}:{transferChoice:value,transferFeedback:"把 Στ 與 ΣF 兩個讀值分開檢查。"});return;}}
    const thirdAction=event.target.closest("[data-third-action]");
    if(thirdAction && lesson.simulation.model==="eb-iv-13-action-reaction"){const action=thirdAction.dataset.thirdAction,value=thirdAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{thirdPrediction:value,thirdFeedback:""});return;}if(action==="submit-prediction"){update(root,state.thirdPrediction?{predictionSubmitted:true,thirdFeedback:state.thirdPrediction==="equal"?"預測已記錄。調整接觸力，觀察兩支箭頭是否永遠成對。":"預測已記錄。觀察兩車箭頭數值，再分辨加速度差異。"}:{thirdFeedback:"請先選擇預測。"});return;}if(action==="boundary"){update(root,{systemBoundary:value});return;}if(action==="transfer"){update(root,value==="mass"?{transferChoice:value,transferFeedback:"正確：第三定律保證力對等大反向；第二定律說同一大小的力作用於不同質量可產生不同加速度。"}:{transferChoice:value,transferFeedback:"先看圖：兩支力箭頭的數值始終相同。"});return;}}
    const massInertiaAction=event.target.closest("[data-mass-inertia-action]");
    if(massInertiaAction && lesson.simulation.model==="eb-iv-12-mass-inertia"){const action=massInertiaAction.dataset.massInertiaAction,value=massInertiaAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{massPrediction:value,massFeedback:""});return;}if(action==="submit-prediction"){update(root,state.massPrediction?{predictionSubmitted:true,massFeedback:state.massPrediction==="half"?"預測已記錄。固定推力與時間，只改質量比較 Δv。":"預測已記錄。只改質量，用 a=F/m 檢查。"}:{massFeedback:"請先選擇預測。"});return;}if(action==="transfer"){update(root,value==="mass"?{transferChoice:value,transferFeedback:"正確：質量越大，慣性越大；同樣合力造成的加速度較小。"}:{transferChoice:value,transferFeedback:"重力仍存在；關鍵是質量與慣性。"});return;}}
    const boyleAction=event.target.closest("[data-boyle-action]");
    if(boyleAction && lesson.simulation.model==="ec-iv-2-boyle"){const action=boyleAction.dataset.boyleAction,value=boyleAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{boylePrediction:value,boyleFeedback:""});return;}if(action==="submit-prediction"){update(root,state.boylePrediction?{predictionSubmitted:true,boyleFeedback:state.boylePrediction==="double"?"預測已記錄。把體積從 100 調到 50，比較壓力。":"預測已記錄。推動活塞，用 PV 數值檢查。"}:{boyleFeedback:"請先選擇預測。"});return;}if(action==="transfer"){update(root,value==="half"?{transferChoice:value,transferFeedback:"正確：體積加倍且 PV 固定，所以壓力約減半。"}:{transferChoice:value,transferFeedback:"固定 PV 後重新比較 40 與 80 mL。"});return;}}
    const impulseAction=event.target.closest("[data-impulse-action]");
    if(impulseAction && lesson.simulation.model==="eb-iv-11-impulse"){const action=impulseAction.dataset.impulseAction,value=impulseAction.dataset.value,state=read(lesson.simulation);if(action==="predict"){update(root,{impulsePrediction:value,impulseFeedback:""});return;}if(action==="submit-prediction"){update(root,state.impulsePrediction?{predictionSubmitted:true,impulseFeedback:state.impulsePrediction==="double"?"預測已記錄。把作用時間加倍，比較圖下面積與末速。":"預測已記錄。用時間滑桿檢查力－時間面積。"}:{impulseFeedback:"請先選擇預測。"});return;}if(action==="transfer"){update(root,value==="less-force"?{transferChoice:value,transferFeedback:"正確：相同動量改變分散到較長時間，平均力可降低。"}:{transferChoice:value,transferFeedback:"固定 Δp，再看 F=Δp/Δt。"});return;}}
    const inertiaAction=event.target.closest("[data-inertia-action]");
    if(inertiaAction && lesson.simulation.model==="eb-iv-10-inertia"){
      const action=inertiaAction.dataset.inertiaAction,value=inertiaAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{inertiaPrediction:value,inertiaFeedback:""});return;}
      if(action==="submit-prediction"){update(root,state.inertiaPrediction?{predictionSubmitted:true,inertiaFeedback:state.inertiaPrediction==="continue"?"預測已記錄。把外力與摩擦都調成 0，觀察速度箭頭。":"預測已記錄。把合力調成 0，檢查速度是否必須歸零。"}:{inertiaFeedback:"請先選擇預測。"});return;}
      if(action==="transfer"){update(root,value==="less-friction"?{transferChoice:value,transferFeedback:"正確：阻力較小時，改變速度的合力較小，因此運動狀態維持更久。"}:{transferChoice:value,transferFeedback:"再把摩擦設為 0：物體不需要持續向前力才能維持等速。"});return;}
    }
    const circularAction=event.target.closest("[data-circular-action]");
    if(circularAction && lesson.simulation.model==="eb-iv-9-circular-motion"){
      const action=circularAction.dataset.circularAction,value=circularAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{circularPrediction:value,circularFeedback:""});return;}
      if(action==="submit-prediction"){update(root,state.circularPrediction?{predictionSubmitted:true,circularFeedback:state.circularPrediction==="quad"?"預測已記錄。把速率加倍，直接比較 a 的數值。":"預測已記錄。用速率滑桿檢查 v² 造成的倍率。"}:{circularFeedback:"請先選擇預測。"});return;}
      if(action==="transfer"){update(root,value==="half"?{transferChoice:value,transferFeedback:"正確：v 固定時 a 與 r 成反比，半徑加倍，向心加速度減半。"}:{transferChoice:value,transferFeedback:"看 a=v²/r：半徑在分母。"});return;}
    }
    const motionAction=event.target.closest("[data-motion-action]");
    if(motionAction && lesson.simulation.model==="eb-iv-8-motion-graph"){
      const action=motionAction.dataset.motionAction,value=motionAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{motionPrediction:value,motionFeedback:""});return;}
      if(action==="submit-prediction"){update(root,state.motionPrediction?{predictionSubmitted:true,motionFeedback:state.motionPrediction==="down"?"預測已記錄。調整折返距離，看圖線段如何下降。":"預測已記錄。改變折返距離，檢查水平線真正代表哪一段運動。"}:{motionFeedback:"請先選擇預測。"});return;}
      if(action==="transfer"){update(root,value==="zero"?{transferChoice:value,transferFeedback:"正確：位移只看起終點；繞一圈回原點位移為 0，但實際走過的路程仍大於 0。"}:{transferChoice:value,transferFeedback:"再看路線：回原點不代表途中沒有走路。"});return;}
    }
    const buoyancyAction=event.target.closest("[data-buoyancy-action]");
    if(buoyancyAction && lesson.simulation.model==="eb-iv-6-buoyancy"){
      const action=buoyancyAction.dataset.buoyancyAction,value=buoyancyAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{buoyancyPrediction:value,buoyancyFeedback:""});return;}
      if(action==="submit-prediction"){update(root,state.buoyancyPrediction?{predictionSubmitted:true,buoyancyFeedback:state.buoyancyPrediction==="increase"?"預測已記錄。調整液體密度，觀察浮力箭頭與排液重量。":"預測已記錄。用密度滑桿檢查浮力是否真的不變。"}:{buoyancyFeedback:"請先選擇預測。"});return;}
      if(action==="transfer"){update(root,value==="more"?{transferChoice:value,transferFeedback:"正確：貨物增加使總重量增加；漂浮平衡時需排開更多液體，讓浮力增加到新的重量。"}:{transferChoice:value,transferFeedback:"再增加物體重量，觀察要讓浮力追上重量時排液體積應往哪個方向改。"});return;}
    }
    const pressureAction=event.target.closest("[data-pressure-action]");
    if(pressureAction && lesson.simulation.model==="eb-iv-5-hydraulic-pressure"){
      const action=pressureAction.dataset.pressureAction,value=pressureAction.dataset.value,state=read(lesson.simulation);
      if(action==="predict"){update(root,{pressurePrediction:value,pressureFeedback:""});return;}
      if(action==="submit-prediction"){update(root,state.pressurePrediction?{predictionSubmitted:true,pressureFeedback:state.pressurePrediction==="increase"?"預測已記錄。改變兩個活塞面積，觀察輸出箭頭與數值。":"預測已記錄。請用大活塞面積滑桿實際檢查。"}:{pressureFeedback:"請先選擇預測。"});return;}
      if(action==="transfer"){update(root,value==="larger"?{transferChoice:value,transferFeedback:"正確：提高輸出/輸入面積比，在相同負載下可降低所需輸入力，但輸入端需移動更長距離。"}:{transferChoice:value,transferFeedback:"再比較面積比與輸出力；縮小輸出活塞會降低力的放大倍率。"});return;}
    }
    const frictionAction = event.target.closest("[data-friction-action]");
    if (frictionAction && lesson.simulation.model === "eb-iv-4-friction-threshold") {
      const action=frictionAction.dataset.frictionAction, value=frictionAction.dataset.value, state=read(lesson.simulation);
      if(action==="predict"){ update(root,{frictionPrediction:value,frictionFeedback:""}); return; }
      if(action==="submit-prediction"){ update(root,state.frictionPrediction?{predictionSubmitted:true,frictionFeedback:state.frictionPrediction==="follow"?"預測已記錄。現在增加拉力，找出靜摩擦上限。":"預測已記錄。用拉力滑桿檢查摩擦力是否真的固定。"}:{frictionFeedback:"請先選擇一項預測。"}); return; }
      if(action==="surface"){ update(root,{surface:value}); return; }
      if(action==="transfer"){ update(root,value==="higher"?{transferChoice:value,transferFeedback:"正確：此模型中正向力增加，最大靜摩擦上限也提高，因此需要更大的水平拉力才開始滑動。"}:{transferChoice:value,transferFeedback:"再增加正向力滑桿並比較最大靜摩擦數值。"}); return; }
    }
    const torqueAction = event.target.closest("[data-torque-action]");
    if (torqueAction && lesson.simulation.model === "eb-iv-1-torque-balance") {
      const action = torqueAction.dataset.torqueAction;
      const value = torqueAction.dataset.value;
      const state = read(lesson.simulation);
      if (action === "predict") { update(root, { torquePrediction: value, torqueFeedback: "" }); return; }
      if (action === "submit-prediction") {
        if (!state.torquePrediction) update(root, { torqueFeedback: "請先選擇逆時針、保持水平或順時針。" });
        else update(root, { predictionSubmitted: true, torqueFeedback: "預測已鎖定。現在只改一個力或力臂，直接觀察紙尺與力矩數值。" });
        return;
      }
      if (action === "transfer") {
        update(root, value === "far"
          ? { transferChoice: value, transferFeedback: "正確：施力相同時，離轉軸越遠，垂直力臂越大，力矩越大。" }
          : { transferChoice: value, transferFeedback: "再看紙尺：施力相同時，把作用位置移近支點會縮短力臂，力矩反而變小。" });
        return;
      }
    }
    const ecoSite = event.target.closest("[data-eco-site]");
    if (ecoSite) { update(root, { site: ecoSite.dataset.ecoSite }); return; }
    const ecoScale = event.target.closest("[data-eco-scale]");
    if (ecoScale) { update(root, { scale: ecoScale.dataset.ecoScale }); return; }
    const atmoScenario = event.target.closest("[data-atmo-scenario]");
    if (atmoScenario) { update(root, { profileScenario: atmoScenario.dataset.atmoScenario }); return; }
    const designAction = event.target.closest("[data-design-action]");
    if (designAction?.dataset.designAction === "submit-prediction") { update(root, { designPredictionSubmitted: true, designStep: 0 }); return; }
    const designStep = event.target.closest("[data-design-step]");
    if (designStep) { update(root, { designStep: Number(designStep.dataset.designStep) }); return; }
    const relation = event.target.closest("[data-inequality-relation]");
    if (relation) { update(root, { relation: relation.dataset.inequalityRelation }); return; }
    const transportChoice = event.target.closest("[data-transport-choice]");
    if (transportChoice) { update(root, { [transportChoice.dataset.transportChoice]: transportChoice.dataset.value }); return; }
    const geometryPrediction = event.target.closest("[data-geometry-prediction]");
    if (geometryPrediction) { update(root, { predictionChoice: geometryPrediction.dataset.geometryPrediction }); return; }
    const geometryTransfer = event.target.closest("[data-geometry-transfer]");
    if (geometryTransfer) { update(root, { transferChoice: geometryTransfer.dataset.geometryTransfer }); return; }
    const geometryAction = event.target.closest("[data-geometry-action]");
    if (geometryAction?.dataset.geometryAction === "submit-prediction") {
      const state = read(lesson.simulation);
      update(root, !state.predictionChoice
        ? { predictionFeedback: "請先選擇一項預測，再提交。" }
        : state.predictionChoice === "B"
          ? { predictionSubmitted: true, predictionFeedback: "" }
          : { predictionFeedback: (() => { const triangle = lesson.simulation.prismModel?.baseTriangle; const area = triangle ? triangle.legA * triangle.legB / 2 : 6; const perimeter = triangle ? triangle.legA + triangle.legB + triangle.hypotenuse : 12; return `預測尚不正確。先比較兩個固定量：側面面積增量由底面周長${perimeter} cm決定；體積增量由底面積${area} cm²決定。回看三片展開側面後再試一次；此時完整公式與數值仍鎖定。`; })() });
      return;
    }
    if (geometryAction?.dataset.geometryAction === "submit-transfer") {
      const state = read(lesson.simulation);
      update(root, !state.transferChoice
        ? { transferFeedback: "請先選擇一組計算結果，再檢查。" }
        : lesson.simulation.model === "s9-13-prism-surface-volume-v2" && state.transferChoice !== "B"
          ? { transferSubmitted: false, transferFeedback: "還不正確。請分別重算兩個三角端面、三片側面周長乘柱長，以及一個底面積乘柱長，再試一次。" }
          : { transferSubmitted: true, transferFeedback: "正確。兩端面與三側面合成表面積；一個底面積乘柱長才是體積。" });
      return;
    }
    const similarityControl = event.target.closest("[data-sim-similarity]");
    if (similarityControl && lesson.simulation.model === "s9-1-polygon-similarity-v1") {
      const action = similarityControl.dataset.simSimilarity;
      const value = similarityControl.dataset.value;
      const state = read(lesson.simulation);
      if (action === "prediction") update(root, { predictionChoice: value, predictionFeedback: "" });
      if (action === "submit-prediction") update(root, state.predictionChoice
        ? { predictionSubmitted: true, predictionFeedback: `預測已記錄：${state.predictionChoice === "yes" ? "相似" : "不相似"}。現在分別調整兩軸倍率並記錄觀察。` }
        : { predictionFeedback: "先選擇一項預測，才能解鎖模型。" });
      if (action === "verify") update(root, { similarityChoice: value, similarityFeedback: "" });
      if (action === "check") {
        const similar = Math.abs(Number(state.scaleX) - Number(state.scaleY)) < 1e-9;
        update(root, !state.similarityChoice
          ? { similarityFeedback: "先依兩方向倍率選擇相似或不相似。" }
          : state.similarityChoice === (similar ? "yes" : "no")
            ? { similarityFeedback: similar ? `判斷正確：兩方向倍率同為 ${state.scaleX}，對應角也保持 90°。` : `判斷正確：水平倍率 ${state.scaleX}、垂直倍率 ${state.scaleY} 不同；角雖相等，邊倍率不一致，故不相似。` }
            : { similarityFeedback: `再核對兩欄：水平倍率 ${state.scaleX}、垂直倍率 ${state.scaleY}。角相等不能取代所有對應邊倍率一致。` });
      }
      if (action === "transfer") update(root, { transferChoice: value, transferFeedback: "" });
      if (action === "submit-transfer") {
        const config = lesson.simulation.similarityModel;
        const expected = Math.abs(config.transferScale - config.transferScale) < 1e-9 ? "yes" : "no";
        update(root, !state.transferChoice
          ? { transferFeedback: "先選擇遷移判斷。" }
          : state.transferChoice === expected
            ? { transferSubmitted: true, transferFeedback: `正確：${config.transferWidth}→${config.transferWidth*config.transferScale} 與 ${config.transferHeight}→${config.transferHeight*config.transferScale} 的倍率相同。` }
            : { transferSubmitted: false, transferFeedback: "比較兩組對應邊的縮圖÷原圖；相同倍率不會因尺寸改變而失去相似。" });
      }
      return;
    }
    const ticketAction = event.target.closest("[data-ticket-action]");
    if (ticketAction?.dataset.ticketAction === "check" && lesson.simulation.engine === "math-ticket-equation") {
      const state = read(lesson.simulation);
      const count = Number(state.ticketCount), fee = Number(state.oneTimeFee), total = Number(state.totalPaid), candidate = Number(state.candidatePrice);
      const correct = count > 0 && count * candidate + fee === total;
      update(root, { candidateVerified: correct, candidateFeedback: correct ? `符合：${count} × ${candidate} + ${fee} = ${total}，左右相等。` : `不符合：${count} × ${candidate} + ${fee} = ${count * candidate + fee}，與總額 ${total} 不相等；請再檢查候選值。` });
      return;
    }
    const action = event.target.closest("[data-sim-action]")?.dataset.simAction; if (!action) return;
    const state = read(lesson.simulation);
    if (action === "run-trials") state.hits = Array.from({ length: state.trials }, () => Math.random() < .5).filter(Boolean).length;
    if (action === "predicted") state.status = "已記錄預測；現在只改變一項條件並觀察。";
    if (action === "observed") state.status = "已記錄觀察；請在下方用自己的話連結證據與解釋。";
    write(lesson.simulation, state); rerender(root);
  });
  window.LearningSimulations = { render };
})();

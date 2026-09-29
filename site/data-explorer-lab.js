(() => {
  const mounted = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `data-explorer-lab:${item.id}:${instance || "default"}`;
  const fresh = lab => ({ prediction: "", accepted: false, unit: lab.initialUnit, explanation: "", explanationPassed: false, transferAnswer: "", transferExplanation: "", completed: false, message: "" });
  const read = (item, instance) => {
    const lab = item.interactive.dataExplorerLab;
    try {
      const saved = JSON.parse(localStorage.getItem(key(item, instance)) || "{}");
      return { ...fresh(lab), ...saved, accepted: Boolean(saved.accepted), explanationPassed: Boolean(saved.explanationPassed), completed: Boolean(saved.completed) };
    } catch { return fresh(lab); }
  };
  const write = (item, instance, state) => { try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* persistence is optional */ } };
  const render = (item, instance = "default") => {
    const lab = item.interactive?.dataExplorerLab;
    if (!lab) return "";
    mounted.set(item.id, item);
    const state = read(item, instance);
    const shell = body => `<section class="data-explorer-lab" data-data-explorer-lab="${esc(item.id)}" data-del-instance="${esc(instance)}" aria-labelledby="del-title-${esc(instance)}"><header><span class="del-kicker">${esc(lab.label)}</span><h4 id="del-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p><p>${esc(lab.context)}</p></header>${body}</section>`;
    if (state.completed) return shell(`<p class="del-status" role="status" aria-live="polite">${esc(lab.transfer.completionMessage)}</p><button type="button" data-del-action="reset">重新開始</button>`);
    let body = `<p class="del-progress" role="status" aria-live="polite">${state.explanationPassed ? "第 4/4 階段：新圖表遷移" : state.accepted ? (state.unit !== lab.initialUnit ? "第 3/4 階段：說明刻度證據" : "第 2/4 階段：操作圖表刻度") : "第 1/4 階段：先提交數量預測"}</p>`;
    if (!state.accepted) {
      body += `<label class="del-field-label" for="del-prediction-${esc(instance)}">${esc(lab.predictionPrompt)}<input id="del-prediction-${esc(instance)}" data-del-field="prediction" type="number" inputmode="numeric" value="${esc(state.prediction)}"></label><button type="button" data-del-action="predict">提交預測</button>`;
    } else {
      const cells = Array.from({ length: lab.intervals }, (_, index) => `<span class="del-unit-cell" data-del-cell="${index}">${lab.unitLabel} × ${state.unit}</span>`).join("");
      body += `<section class="del-chart" aria-label="${lab.intervals} 個相同高度的單位格">${cells}</section><fieldset class="del-controls"><legend>${esc(lab.manipulationPrompt)}</legend><label class="del-field-label" for="del-scale-${esc(instance)}">每格代表的${esc(lab.unitLabel)}數<input id="del-scale-${esc(instance)}" data-del-scale type="range" min="${lab.initialUnit}" max="${lab.changedUnit}" step="${lab.changedUnit - lab.initialUnit}" value="${state.unit}"></label><output class="del-readout" data-del-readout aria-live="polite">${lab.intervals} 格 × 每格 ${state.unit} ${esc(lab.unitLabel)} = ${lab.intervals * state.unit} ${esc(lab.unitLabel)}</output></fieldset>`;
      body += `<section class="del-explanation" ${state.unit === lab.initialUnit ? "hidden" : ""}><label class="del-field-label" for="del-explanation-${esc(instance)}">${esc(lab.explanationPrompt)}<input id="del-explanation-${esc(instance)}" data-del-field="explanation" value="${esc(state.explanation)}"></label><button type="button" data-del-action="explain">檢查刻度說明</button></section>`;
      if (state.explanationPassed) {
        const options = lab.transfer.options.map((option, index) => { const value = String.fromCharCode(65 + index); return `<label class="del-option"><input type="radio" name="del-transfer-${esc(instance)}" data-del-choice value="${value}" ${state.transferAnswer === value ? "checked" : ""}><span><b>${value}.</b> ${esc(option)}</span></label>`; }).join("");
        body += `<fieldset class="del-transfer"><legend>${esc(lab.transfer.prompt)}</legend>${options}<label class="del-field-label" for="del-transfer-explanation-${esc(instance)}">${esc(lab.transfer.explanationPrompt)}<textarea id="del-transfer-explanation-${esc(instance)}" data-del-field="transferExplanation" rows="2">${esc(state.transferExplanation)}</textarea></label><button type="button" data-del-action="transfer">檢查遷移答案</button></fieldset>`;
      }
    }
    body += `<p class="del-status" role="status" aria-live="polite">${esc(state.message)}</p><button type="button" data-del-action="reset">重設本次練習</button>`;
    return shell(body);
  };
  const rerender = (root, focus) => {
    const item = mounted.get(root.dataset.dataExplorerLab);
    if (!item) return;
    const instance = root.dataset.delInstance || "default";
    const holder = document.createElement("div");
    holder.innerHTML = render(item, instance);
    const updated = holder.firstElementChild;
    root.replaceWith(updated);
    if (focus) updated.querySelector(focus)?.focus();
  };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-data-explorer-lab]");
    if (!root) return;
    const item = mounted.get(root.dataset.dataExplorerLab);
    if (!item) return;
    const instance = root.dataset.delInstance || "default";
    const state = read(item, instance);
    const field = event.target.dataset.delField;
    if (field) { state[field] = event.target.value; write(item, instance, state); }
    if (event.target.matches("[data-del-scale]")) {
      const lab = item.interactive.dataExplorerLab;
      state.unit = Number(event.target.value);
      if (state.unit === lab.initialUnit) { state.explanationPassed = false; state.transferAnswer = ""; state.transferExplanation = ""; }
      state.message = "";
      write(item, instance, state);
      root.querySelectorAll("[data-del-cell]").forEach(cell => { cell.textContent = `${lab.unitLabel} × ${state.unit}`; });
      root.querySelector("[data-del-readout]").textContent = `${lab.intervals} 格 × 每格 ${state.unit} ${lab.unitLabel} = ${lab.intervals * state.unit} ${lab.unitLabel}`;
      root.querySelector(".del-explanation").hidden = state.unit === lab.initialUnit;
      root.querySelector(".del-transfer")?.remove();
      root.querySelector(".del-progress").textContent = state.unit === lab.initialUnit ? "第 2/4 階段：操作圖表刻度" : "第 3/4 階段：說明刻度證據";
    }
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-data-explorer-lab]");
    if (!root || !event.target.matches("[data-del-choice]")) return;
    const item = mounted.get(root.dataset.dataExplorerLab);
    if (!item) return;
    const instance = root.dataset.delInstance || "default";
    const state = read(item, instance);
    state.transferAnswer = event.target.value;
    write(item, instance, state);
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-data-explorer-lab]");
    if (!root) return;
    const item = mounted.get(root.dataset.dataExplorerLab);
    if (!item) return;
    const lab = item.interactive.dataExplorerLab;
    const instance = root.dataset.delInstance || "default";
    const state = read(item, instance);
    const action = event.target.closest("[data-del-action]")?.dataset.delAction;
    if (!action) return;
    if (action === "reset") {
      try { localStorage.removeItem(key(item, instance)); } catch { /* reset remains available */ }
      rerender(root, "[data-del-field='prediction']");
    } else if (action === "predict") {
      const value = Number(state.prediction);
      if (!state.prediction || !Number.isFinite(value)) state.message = "先輸入數量預測，再提交。";
      else if (value !== lab.expectedInitialValue) state.message = lab.predictionHint;
      else { state.accepted = true; state.message = lab.predictionAccepted; }
      write(item, instance, state);
      rerender(root, state.accepted ? "[data-del-scale]" : "[data-del-field='prediction']");
    } else if (action === "explain") {
      const value = state.explanation.trim().toLocaleLowerCase();
      const accepted = Number(state.unit) !== lab.initialUnit && lab.acceptedExplanationTerms.every(term => value.includes(term.toLocaleLowerCase()));
      if (!accepted) state.message = state.unit === lab.initialUnit ? "先改變每格刻度，再比較讀值。" : lab.explanationHint;
      else { state.explanationPassed = true; state.message = lab.explanationAccepted; }
      write(item, instance, state);
      rerender(root, state.explanationPassed ? "[data-del-choice]" : "[data-del-field='explanation']");
    } else if (action === "transfer") {
      const value = state.transferExplanation.trim().toLocaleLowerCase();
      const validTerms = lab.transfer.requiredEvidenceTerms.every(term => value.includes(term.toLocaleLowerCase()));
      const validLength = value.length >= lab.transfer.minimumExplanationLength;
      if (!state.transferAnswer) state.message = "先選擇符合資料的敘述，再用資料列說明理由。";
      else if (!validLength || !validTerms) state.message = lab.transfer.retryHint;
      else if (state.transferAnswer !== lab.transfer.answer) state.message = lab.transfer.retryHint;
      else { state.completed = true; state.message = ""; }
      write(item, instance, state);
      rerender(root, state.completed ? "[data-del-action='reset']" : "[data-del-choice]");
    }
  });
  window.DataExplorerLab = { render };
})();

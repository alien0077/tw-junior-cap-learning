(() => {
  const activities = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `short-play-lab:${item.id}:${instance || "default"}`;
  const fresh = () => ({ prediction: "", revealed: false, stageIndex: 0, answers: [], message: "", complete: false });
  const read = (item, instance, total) => {
    try {
      const saved = JSON.parse(localStorage.getItem(key(item, instance)) || "{}");
      const answers = Array.isArray(saved.answers) ? saved.answers.slice(0, total) : [];
      const stageIndex = Math.min(total, Math.max(0, Number(saved.stageIndex) || 0), answers.length);
      return { ...fresh(), ...saved, stageIndex, answers, complete: Boolean(saved.complete && stageIndex === total) };
    } catch { return fresh(); }
  };
  const write = (item, instance, state) => {
    try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* lesson remains usable without storage */ }
  };
  const allStages = lab => [...lab.mainStages, ...lab.transfer.stages];
  const renderScript = script => `<article class="spl-script"><h5>${esc(script.title)}</h5><ol>${script.lines.map(line => `<li data-line-kind="${esc(line.kind)}"><b>${esc(line.speaker)}</b><span>${esc(line.text)}</span></li>`).join("")}</ol></article>`;
  const render = (item, instance = "default") => {
    const lab = item.interactive?.shortPlayLab;
    if (!lab) return "";
    activities.set(item.id, item);
    const stages = allStages(lab);
    const state = read(item, instance, stages.length);
    const shell = body => `<section class="short-play-lab" data-short-play-lab="${esc(item.id)}" data-spl-instance="${esc(instance)}" aria-labelledby="spl-title-${esc(instance)}"><header><span class="spl-kicker">短劇排演室</span><h4 id="spl-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header>${body}</section>`;
    if (state.complete) return shell(`<p class="spl-status" role="status" aria-live="polite">${esc(lab.completionMessage)}</p><button type="button" data-spl-action="reset">重新排演</button>`);
    let body = `<p class="spl-progress">${state.revealed ? `排演判讀 ${state.stageIndex + 1}／${stages.length}` : "讀前預測"}</p><progress max="${stages.length}" value="${state.stageIndex}" aria-label="短劇理解進度"></progress>`;
    if (!state.revealed) {
      body += `<article class="spl-preview"><p class="spl-label">預告：只先看標題與排演提示</p><h5>${esc(lab.preview.title)}</h5><p>${esc(lab.preview.cue)}</p><label for="spl-prediction-${esc(instance)}">你預測排演會遇到什麼問題？至少 ${lab.minimumPredictionLength} 字</label><textarea id="spl-prediction-${esc(instance)}" data-spl-prediction rows="2">${esc(state.prediction)}</textarea><button type="button" data-spl-action="reveal">保存預測並讀劇本</button><p class="spl-status" role="status" aria-live="polite">${esc(state.message)}</p></article>`;
    } else {
      const inTransfer = state.stageIndex >= lab.mainStages.length;
      const script = inTransfer ? lab.transfer.script : lab.mainScript;
      const stage = stages[state.stageIndex];
      const choice = state.answers[state.stageIndex] || "";
      body += `<p class="spl-prediction"><b>讀前預測：</b>${esc(state.prediction)}</p>${renderScript(script)}${inTransfer ? `<p class="spl-transfer-label">新劇本遷移：此處的角色、衝突與舞台線索皆不同，請重新找證據。</p>` : ""}<article class="spl-question"><h5>${esc(stage.prompt)}</h5><fieldset><legend>選出最能由台詞、動作或結果支持的解讀</legend>${stage.options.map((option, index) => { const value = String.fromCharCode(65 + index); return `<label class="spl-option"><input type="radio" name="spl-choice-${esc(instance)}" data-spl-choice value="${value}" ${choice === value ? "checked" : ""}><span><b>${value}.</b> ${esc(option)}</span></label>`; }).join("")}</fieldset><button type="button" data-spl-action="check">核對排演理解</button><p class="spl-status" role="status" aria-live="polite">${esc(state.message)}</p></article>`;
    }
    body += `<button type="button" data-spl-action="reset">重設本次排演</button>`;
    return shell(body);
  };
  const rerender = root => {
    const item = activities.get(root.dataset.shortPlayLab);
    if (!item) return;
    const next = document.createElement("div");
    next.innerHTML = render(item, root.dataset.splInstance || "default");
    root.replaceWith(next.firstElementChild);
  };
  document.addEventListener("click", event => {
    const button = event.target.closest("[data-spl-action]");
    const root = button?.closest("[data-short-play-lab]");
    if (!root) return;
    const item = activities.get(root.dataset.shortPlayLab);
    if (!item) return;
    const instance = root.dataset.splInstance || "default";
    const lab = item.interactive.shortPlayLab;
    const stages = allStages(lab);
    const state = read(item, instance, stages.length);
    if (button.dataset.splAction === "reset") {
      try { localStorage.removeItem(key(item, instance)); } catch { /* reset remains available without storage */ }
      rerender(root);
      return;
    }
    if (button.dataset.splAction === "reveal") {
      const prediction = root.querySelector("[data-spl-prediction]").value.trim();
      if (prediction.length < lab.minimumPredictionLength) state.message = `請先寫至少 ${lab.minimumPredictionLength} 字，保存一個可回頭檢查的預測。`;
      else { state.prediction = prediction; state.revealed = true; state.message = "預測已保存。讀劇本時留意角色想做什麼、什麼擋住他，以及舞台線索如何改變行動。"; }
    } else {
      const choice = root.querySelector("[data-spl-choice]:checked")?.value;
      const stage = stages[state.stageIndex];
      if (!choice) state.message = "先選一項解讀，再核對劇本證據。";
      else if (choice !== stage.answer) { state.answers[state.stageIndex] = choice; state.message = stage.retryHint; }
      else {
        state.answers[state.stageIndex] = choice;
        state.stageIndex += 1;
        state.complete = state.stageIndex === stages.length;
        state.message = state.complete ? lab.completionMessage : stage.feedback;
      }
    }
    write(item, instance, state);
    rerender(root);
  });
  window.ShortPlayLab = { render };
})();

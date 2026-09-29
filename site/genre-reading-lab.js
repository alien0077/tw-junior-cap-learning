(() => {
  const mounted = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const storageKey = (item, instance) => `genre-reading-lab:${item.id}:${instance || "default"}`;
  const blank = () => ({ predicted: false, prediction: "", selectedSource: "", explanation: "", explanationPassed: false, transferAnswer: "", completed: false, message: "" });
  const read = (item, instance) => {
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey(item, instance)) || "{}");
      return { ...blank(), ...saved, predicted: Boolean(saved.predicted), explanationPassed: Boolean(saved.explanationPassed), completed: Boolean(saved.completed) };
    } catch { return blank(); }
  };
  const write = (item, instance, state) => { try { localStorage.setItem(storageKey(item, instance), JSON.stringify(state)); } catch { /* storage is optional */ } };
  const render = (item, instance = "default") => {
    const lab = item.interactive?.genreReadingLab;
    if (!lab?.sources?.length) return "";
    mounted.set(item.id, item);
    const state = read(item, instance);
    const shell = body => `<section class="genre-reading-lab" data-genre-reading-lab="${esc(item.id)}" data-grl-instance="${esc(instance)}" aria-labelledby="grl-title-${esc(instance)}"><header><span class="grl-kicker">${esc(lab.label)}</span><h4 id="grl-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.context)}</p></header>${body}</section>`;
    if (state.completed) return shell(`<p class="grl-status" role="status" aria-live="polite">${esc(lab.transfer.completionMessage)}</p><button type="button" data-grl-action="reset">重新開始</button>`);
    let body = `<p class="grl-progress" role="status" aria-live="polite">${state.explanationPassed ? "第 3/4 階段：遷移" : state.selectedSource ? "第 2/4 階段：選取文本區塊並核對任務" : state.predicted ? "第 2/4 階段：切換文本區塊" : "第 1/4 階段：先預測"}</p>`;
    if (!state.predicted) {
      body += `<label class="grl-input-label" for="grl-prediction-${esc(instance)}">${esc(lab.predictionPrompt)}<input id="grl-prediction-${esc(instance)}" data-grl-field="prediction" value="${esc(state.prediction)}" autocomplete="off"></label><button type="button" data-grl-action="predict">提交預測</button>`;
    } else {
      const sources = lab.sources.map(source => `<button type="button" class="grl-source-button" data-grl-source="${esc(source.id)}" aria-pressed="${state.selectedSource === source.id}">查看「${esc(source.label)}」</button>`).join("");
      body += `<div class="grl-sources" role="group" aria-label="選擇要查閱的網頁區塊">${sources}</div>`;
      const selected = lab.sources.find(source => source.id === state.selectedSource);
      if (selected) body += `<article class="grl-excerpt" aria-live="polite"><p><strong>文本片段：</strong>${esc(selected.excerpt)}</p><p><strong>體裁／功能：</strong>${esc(selected.function)}</p><p><strong>適合回答：</strong>${esc(selected.question)}</p><p><strong>閱讀限制：</strong>${esc(selected.limit)}</p></article><p class="grl-hint" role="status" aria-live="polite">${state.selectedSource === lab.mainSourceId ? "這個區塊符合日期任務；請把日期線索寫進理由。" : esc(lab.sourceHint)}</p>`;
      if (!state.explanationPassed && selected) body += `<label class="grl-input-label" for="grl-explanation-${esc(instance)}">${esc(lab.explanationPrompt)}<input id="grl-explanation-${esc(instance)}" data-grl-field="explanation" value="${esc(state.explanation)}"></label><button type="button" data-grl-action="explain">檢查證據說明</button>`;
      if (state.explanationPassed) body += `<p class="grl-success" role="status" aria-live="polite">${esc(lab.evidenceFeedback)}</p><label class="grl-input-label" for="grl-transfer-${esc(instance)}">${esc(lab.transfer.prompt)}<input id="grl-transfer-${esc(instance)}" data-grl-field="transferAnswer" value="${esc(state.transferAnswer)}"></label><button type="button" data-grl-action="transfer">檢查遷移答案</button>`;
    }
    body += `<p class="grl-status" role="status" aria-live="polite">${esc(state.message)}</p><button type="button" data-grl-action="reset">重設本次練習</button>`;
    return shell(body);
  };
  const rerender = (root, selector) => {
    const item = mounted.get(root.dataset.genreReadingLab);
    if (!item) return;
    const instance = root.dataset.grlInstance || "default";
    const next = document.createElement("div");
    next.innerHTML = render(item, instance);
    const updated = next.firstElementChild;
    root.replaceWith(updated);
    if (selector) updated.querySelector(selector)?.focus();
  };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-genre-reading-lab]");
    const field = event.target.dataset.grlField;
    if (!root || !field) return;
    const item = mounted.get(root.dataset.genreReadingLab);
    if (!item) return;
    const state = read(item, root.dataset.grlInstance);
    state[field] = event.target.value;
    write(item, root.dataset.grlInstance, state);
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-genre-reading-lab]");
    if (!root) return;
    const item = mounted.get(root.dataset.genreReadingLab);
    if (!item) return;
    const lab = item.interactive.genreReadingLab;
    const instance = root.dataset.grlInstance || "default";
    const state = read(item, instance);
    const action = event.target.closest("[data-grl-action]")?.dataset.grlAction;
    const sourceId = event.target.closest("[data-grl-source]")?.dataset.grlSource;
    if (sourceId) {
      state.selectedSource = sourceId;
      state.explanationPassed = false;
      state.message = sourceId === lab.mainSourceId ? "你找到可能回答 when 的區塊；再核對日期與時段。" : lab.sourceHint;
      write(item, instance, state);
      rerender(root, `[data-grl-source="${sourceId}"]`);
      return;
    }
    if (!action) return;
    if (action === "reset") {
      try { localStorage.removeItem(storageKey(item, instance)); } catch { /* reset remains available */ }
      rerender(root, "[data-grl-field='prediction']");
    } else if (action === "predict") {
      const value = state.prediction.trim().toLocaleLowerCase();
      const accepted = lab.predictionAnswers.some(answer => answer.toLocaleLowerCase() === value);
      if (!accepted) state.message = lab.predictionHint;
      else { state.predicted = true; state.message = "預測已保存；先比較區塊功能，再決定哪一區能回答問題。"; }
      write(item, instance, state);
      rerender(root, accepted ? "[data-grl-source]" : "[data-grl-field='prediction']");
    } else if (action === "explain") {
      const value = state.explanation.trim();
      if (state.selectedSource !== lab.mainSourceId) state.message = lab.sourceHint;
      else if (value.length < lab.minimumExplanationLength) state.message = `請至少寫 ${lab.minimumExplanationLength} 個字，並指出片段中的日期或時段。`;
      else if (!lab.requiredEvidenceTerms.some(term => value.toLocaleLowerCase().includes(term.toLocaleLowerCase()))) state.message = lab.evidenceHint;
      else { state.explanationPassed = true; state.message = "理由已連結區塊與片段線索；請在新情境重新判斷 why 問題。"; }
      write(item, instance, state);
      rerender(root, state.explanationPassed ? "[data-grl-field='transferAnswer']" : "[data-grl-field='explanation']");
    } else if (action === "transfer") {
      const value = state.transferAnswer.trim().toLocaleLowerCase();
      const accepted = lab.transfer.answers.some(answer => answer.toLocaleLowerCase() === value);
      if (!accepted) state.message = lab.transfer.hint;
      else { state.completed = true; state.message = ""; }
      write(item, instance, state);
      rerender(root, state.completed ? "[data-grl-action='reset']" : "[data-grl-field='transferAnswer']");
    }
  });
  window.GenreReadingLab = { render };
})();

(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `text-prediction-lab:${item.id}:${instance || "default"}`;
  const fresh = () => ({ artifactIndex: 0, responses: {}, complete: false });
  const blank = () => ({ prediction: "", confidence: "", cues: [], revealed: false, evidence: [], answer: "", passed: false, message: "" });
  const read = (item, instance) => { try { return { ...fresh(), ...JSON.parse(localStorage.getItem(key(item, instance)) || "{}") }; } catch { return fresh(); } };
  const responseFor = (state, artifact) => ({ ...blank(), ...(state.responses[artifact.id] || {}) });
  const write = (item, instance, state) => { try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* progress persistence is optional */ } };
  const illustration = (kind, alt) => {
    if (kind === "courtyard") return `<svg class="tp-illustration" viewBox="0 0 360 190" role="img" aria-label="${esc(alt)}"><rect width="360" height="190" rx="14" fill="#e9f1ef"/><path d="M30 70 180 20 330 70" fill="#d9bd86"/><path d="M50 70h260v10H50Z" fill="#94764c"/><path d="M68 80v82m224-82v82" stroke="#94764c" stroke-width="8"/><rect x="116" y="105" width="128" height="45" rx="7" fill="#78928b"/><path d="M130 150v15m100-15v15" stroke="#485e59" stroke-width="7"/><path d="M85 174h190" stroke="#b7a27a" stroke-width="4" stroke-dasharray="7 7"/><circle cx="96" cy="102" r="8" fill="#c97e55"/><circle cx="265" cy="101" r="8" fill="#597fa0"/><path d="M98 110v24m-8 0h16m159-24v24m-8 0h16" stroke="#526b78" stroke-width="4"/></svg>`;
    return `<svg class="tp-illustration" viewBox="0 0 360 190" role="img" aria-label="${esc(alt)}"><rect width="360" height="190" rx="14" fill="#f4efdc"/><rect x="46" y="30" width="268" height="128" rx="8" fill="#ede0c5" stroke="#826b4b" stroke-width="5"/><path d="M130 32v124m88-124v124M48 92h264" stroke="#826b4b" stroke-width="5"/><path d="M52 35h75v54H52Z" fill="#89b3bd"/><path d="M135 35h79v54h-79Z" fill="#d69b69"/><path d="M223 35h87v54h-87Z" fill="#879b72"/><path d="M52 98h75v55H52Z" fill="#d2b675"/><path d="M135 98h79v55h-79Z" fill="#b88591"/><path d="M223 98h87v55h-87Z" fill="#84a4a0"/><path d="m293 26 18-13 15 12-34 42" fill="none" stroke="#665239" stroke-width="6" stroke-linecap="round"/><path d="M291 68q11 7 21 0" fill="none" stroke="#c78246" stroke-width="5"/></svg>`;
  };
  const options = (question, selected, instance, disabled = false) => question.options.map(option => `<label class="tp-option"><input type="radio" name="tp-answer-${esc(instance)}" data-tp-choice="answer" value="${esc(option.id)}" ${selected === option.id ? "checked" : ""} ${disabled ? "disabled" : ""}><span>${esc(option.text)}</span></label>`).join("");
  const render = (item, instance = "default") => {
    const lab = item.interactive?.textPredictionLab;
    if (!lab) return "";
    const state = read(item, instance);
    const artifact = lab.artifacts[state.artifactIndex];
    if (state.complete || !artifact) return `<section class="text-prediction-lab" data-text-prediction-lab="${esc(item.id)}" data-tp-instance="${esc(instance)}" aria-labelledby="tp-title-${esc(instance)}"><header><span class="tp-kicker">${esc(lab.label)}</span><h4 id="tp-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header><p class="tp-status" role="status" aria-live="polite">預測校準完成：你保留了初始線索、參照正文證據修正判斷，並指出圖片不能證明的事。</p><button type="button" data-tp-action="reset">重新開始</button></section>`;
    const response = responseFor(state, artifact);
    const cueControls = artifact.sourceCues.map(cue => `<li class="${response.cues.includes(cue.id) ? "is-selected" : ""}"><span><strong>${esc(cue.label)}</strong><br>${esc(cue.text)}</span><button type="button" data-tp-cue="${esc(cue.id)}" aria-pressed="${response.cues.includes(cue.id)}" ${response.revealed ? "disabled" : ""}>${response.cues.includes(cue.id) ? "已作為預測依據" : "用這項線索"}</button></li>`).join("");
    const confidence = artifact.confidenceOptions.map(choice => `<label class="tp-option"><input type="radio" name="tp-confidence-${esc(instance)}" data-tp-choice="confidence" value="${esc(choice.id)}" ${response.confidence === choice.id ? "checked" : ""} ${response.revealed ? "disabled" : ""}><span>${esc(choice.text)}</span></label>`).join("");
    const updatedConfidence = artifact.confidenceOptions.map(choice => `<label class="tp-option"><input type="radio" name="tp-updated-confidence-${esc(instance)}" data-tp-choice="updatedConfidence" value="${esc(choice.id)}" ${response.updatedConfidence === choice.id ? "checked" : ""} ${response.passed ? "disabled" : ""}><span>${esc(choice.text)}</span></label>`).join("");
    const evidence = artifact.evidence.map(part => `<li class="${response.evidence.includes(part.id) ? "is-selected" : ""}"><span><strong>${esc(part.label)}</strong><br>${esc(part.text)}</span><button type="button" data-tp-evidence="${esc(part.id)}" aria-pressed="${response.evidence.includes(part.id)}">${response.evidence.includes(part.id) ? "已標記" : "標記正文證據"}</button></li>`).join("");
    const preview = `<article class="tp-cover"><div class="tp-cover-heading"><span>${esc(artifact.sourceLabel)}</span><h5>${esc(artifact.title)}</h5></div>${illustration(artifact.visual, artifact.imageAlt)}<p class="tp-caption">${esc(artifact.caption)}</p></article>`;
    let stage = `<section class="tp-stage"><h5>1｜先預測，不急著猜結局</h5><p>${esc(artifact.predictionPrompt)}</p>${preview}<label for="tp-prediction-${esc(instance)}">寫下你的預測（至少 ${artifact.minimumPredictionLength} 字）</label><textarea id="tp-prediction-${esc(instance)}" data-tp-text="prediction" rows="2" ${response.revealed ? "disabled" : ""}>${esc(response.prediction)}</textarea><fieldset><legend>${esc(artifact.confidencePrompt)}</legend>${confidence}</fieldset><fieldset><legend>你用了哪些封面線索？至少選 ${artifact.sourceCueMinimum} 項</legend><ul class="tp-evidence">${cueControls}</ul></fieldset><button type="button" data-tp-action="reveal" ${response.revealed ? "disabled" : ""}>保存預測並打開正文</button><p class="tp-feedback" aria-live="polite">${esc(response.message)}</p></section>`;
    if (response.revealed) {
      stage += `<section class="tp-stage"><h5>2｜新文字出現後，校準你的預測</h5><p class="tp-original-prediction"><strong>你的原預測：</strong>${esc(response.prediction)}<br><strong>當時把握：</strong>${esc(artifact.confidenceOptions.find(choice => choice.id === response.confidence)?.text || "")}</p><article class="tp-reading"><p>${esc(artifact.readingText)}</p></article><fieldset><legend>哪幾句是判斷修正時不可漏看的正文證據？</legend><ul class="tp-evidence">${evidence}</ul></fieldset><fieldset><legend>${esc(artifact.checkQuestion.prompt)}</legend>${options(artifact.checkQuestion, response.answer, instance, response.passed)}<button type="button" data-tp-action="check" ${response.passed ? "disabled" : ""}>檢查修正判斷</button></fieldset><fieldset><legend>${esc(artifact.reassessmentPrompt)}</legend>${updatedConfidence}</fieldset><p class="tp-feedback" aria-live="polite">${esc(response.message || artifact.checkQuestion.hint)}</p>${response.passed ? `<button type="button" data-tp-action="next">${state.artifactIndex + 1 === lab.artifacts.length ? "完成預測校準" : "進入新情境遷移"}</button>` : ""}</section>`;
    }
    const status = `情境 ${state.artifactIndex + 1}/${lab.artifacts.length} · ${artifact.role === "practice" ? "引導練習" : "新情境遷移"}${response.revealed ? " · 正在依新正文校準" : " · 正文尚未揭露"}`;
    return `<section class="text-prediction-lab" data-text-prediction-lab="${esc(item.id)}" data-tp-instance="${esc(instance)}" aria-labelledby="tp-title-${esc(instance)}"><header><span class="tp-kicker">${esc(lab.label)}</span><h4 id="tp-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header>${stage}<p class="tp-status" role="status" aria-live="polite">${esc(status)}</p><button type="button" class="tp-reset" data-tp-action="reset">重新開始</button></section>`;
  };
  const activities = new Map();
  const mount = (item, instance) => { activities.set(item.id, item); return render(item, instance); };
  const rerender = (root, selector) => {
    const item = activities.get(root.dataset.textPredictionLab);
    if (!item) return;
    const instance = root.dataset.tpInstance;
    root.outerHTML = render(item, instance);
    const next = [...document.querySelectorAll("[data-text-prediction-lab]")].find(node => node.dataset.textPredictionLab === item.id && node.dataset.tpInstance === instance);
    next?.querySelector(selector)?.focus();
  };
  const current = root => {
    const item = activities.get(root.dataset.textPredictionLab);
    const state = read(item, root.dataset.tpInstance);
    const artifact = item.interactive.textPredictionLab.artifacts[state.artifactIndex];
    const response = responseFor(state, artifact);
    return { item, state, artifact, response, instance: root.dataset.tpInstance };
  };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-text-prediction-lab]");
    if (!root || event.target.dataset.tpText !== "prediction") return;
    const { item, state, artifact, response, instance } = current(root);
    response.prediction = event.target.value;
    state.responses[artifact.id] = response;
    write(item, instance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-text-prediction-lab]");
    const field = event.target.dataset.tpChoice;
    if (!root || !field) return;
    const { item, state, artifact, response, instance } = current(root);
    response[field] = event.target.value;
    response.message = "";
    if (field === "answer") { response.passed = false; response.updatedConfidence = ""; }
    state.responses[artifact.id] = response;
    write(item, instance, state);
    const button = root.querySelector(`[data-tp-action="${response.revealed ? "check" : "reveal"}"]`);
    if (button) button.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-text-prediction-lab]");
    if (!root) return;
    const { item, state, artifact, response, instance } = current(root);
    const lab = item.interactive.textPredictionLab;
    const cue = event.target.closest("[data-tp-cue]");
    const evidence = event.target.closest("[data-tp-evidence]");
    if (cue) {
      const id = cue.dataset.tpCue;
      response.cues = response.cues.includes(id) ? response.cues.filter(value => value !== id) : [...response.cues, id];
      response.message = "";
      state.responses[artifact.id] = response;
      write(item, instance, state);
      rerender(root, `[data-tp-cue="${id}"]`);
      return;
    }
    if (evidence) {
      const id = evidence.dataset.tpEvidence;
      response.evidence = response.evidence.includes(id) ? response.evidence.filter(value => value !== id) : [...response.evidence, id];
      response.answer = ""; response.passed = false; response.updatedConfidence = ""; response.message = "";
      state.responses[artifact.id] = response;
      write(item, instance, state);
      rerender(root, `[data-tp-evidence="${id}"]`);
      return;
    }
    const action = event.target.closest("[data-tp-action]")?.dataset.tpAction;
    if (!action) return;
    if (action === "reset") {
      try { localStorage.removeItem(key(item, instance)); } catch { /* progress persistence is optional */ }
      rerender(root, '[data-tp-text="prediction"]');
      return;
    }
    if (action === "reveal") {
      if (response.prediction.trim().length < artifact.minimumPredictionLength) response.message = `請至少用 ${artifact.minimumPredictionLength} 字寫下有限度的預測，再查看正文。`;
      else if (response.cues.length < artifact.sourceCueMinimum) response.message = `請至少選 ${artifact.sourceCueMinimum} 項實際可見的封面線索。`;
      else if (!response.confidence) response.message = "選一個把握程度，之後才能比較信心是否需要調整。";
      else { response.revealed = true; response.message = "原預測、信心與線索已保存；讀正文時檢查哪些內容被支持或限縮。"; }
      state.responses[artifact.id] = response;
      write(item, instance, state);
      rerender(root, response.revealed ? '[data-tp-evidence]' : '[data-tp-text="prediction"]');
      return;
    }
    if (action === "check") {
      const enoughEvidence = artifact.requiredEvidenceIds.every(id => response.evidence.includes(id));
      if (!enoughEvidence) response.message = "先標出正文中說明主題與預測界線的必要句子，再檢查修正判斷。";
      else if (!response.answer) response.message = "選擇一項修正版，並以剛標記的正文證據核對。";
      else if (!response.updatedConfidence) response.message = "比較剛才的預測和新證據，重新選擇目前把握程度。";
      else if (response.answer !== artifact.checkQuestion.answer) response.message = artifact.checkQuestion.hint;
      else { response.passed = true; response.message = artifact.checkQuestion.feedback; }
      state.responses[artifact.id] = response;
      write(item, instance, state);
      rerender(root, response.passed ? '[data-tp-action="next"]' : 'input[name^="tp-answer-"]');
      return;
    }
    if (action === "next" && response.passed) {
      if (state.artifactIndex + 1 >= lab.artifacts.length) state.complete = true;
      else state.artifactIndex += 1;
      write(item, instance, state);
      rerender(root, state.complete ? '[data-tp-action="reset"]' : '[data-tp-text="prediction"]');
    }
  });
  window.TextPredictionLab = { render: mount };
})();

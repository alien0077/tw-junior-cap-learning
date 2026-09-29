(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `message-reading-lab:${item.id}:${instance || "default"}`;
  const defaults = () => ({ prediction: "", predicted: false, evidence: [], evidenceChecked: false, answer: "", answerAttempts: 0, transferEvidence: [], transferAnswer: "", explanation: "", completed: false });
  const read = (item, instance) => { try { return { ...defaults(), ...JSON.parse(localStorage.getItem(key(item, instance)) || "{}") }; } catch { return defaults(); } };
  const write = (item, instance, state) => { try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* local progress is optional */ } };

  const render = (item, instance = "default") => {
    const lab = item.interactive?.messageReadingLab;
    if (!lab) return "";
    const state = read(item, instance);
    const parts = (list, selected, kind, disabled = false) => list.map(part => `<li class="message-reading-part${selected.includes(part.id) ? " is-selected" : ""}"><div><strong>${esc(part.label)}</strong><p>${esc(part.text)}</p></div><button type="button" data-message-evidence="${kind}" data-part="${esc(part.id)}" aria-pressed="${selected.includes(part.id)}" ${disabled ? "disabled" : ""}>${selected.includes(part.id) ? "已標記為證據" : "標記這段證據"}</button></li>`).join("");
    const options = (question, value, name) => question.options.map(option => `<label class="message-reading-option"><input type="radio" name="${esc(name)}-${esc(instance)}" value="${esc(option.id)}" data-message-value="${name}" ${value === option.id ? "checked" : ""}><span>${esc(option.text)}</span></label>`).join("");
    return `<section class="message-reading-lab" data-message-reading-lab="${esc(item.id)}" data-message-instance="${esc(instance)}" aria-labelledby="message-reading-title-${esc(instance)}">
      <header><span class="message-reading-kicker">${esc(lab.label)}</span><h4 id="message-reading-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header>
      <section class="message-reading-stage"><h5>第一步｜先預測讀者要做什麼</h5><p>${esc(lab.mainText.introduction)}</p><label for="message-reading-prediction-${esc(instance)}">先用自己的話寫下主要內容或行動</label><textarea id="message-reading-prediction-${esc(instance)}" data-message-text="prediction" rows="2" ${state.predicted ? "disabled" : ""}>${esc(state.prediction)}</textarea><button type="button" data-message-action="predict" ${state.predicted ? "disabled" : ""}>保存預測並開啟原文</button><p class="message-reading-feedback" aria-live="polite">${esc(state.predictionMessage || "")}</p></section>
      <ol class="message-reading-parts" aria-label="原創通知文本">${parts(lab.mainText.parts, state.evidence, "main", !state.predicted)}</ol>
      ${state.predicted ? `<section class="message-reading-stage"><h5>第二步｜用原文證據組成行動卡</h5><p>至少選出 ${lab.mainText.requiredEvidenceIds.length} 段；時間、地點或替代方案要回到原文核對。</p><div class="message-reading-summary" aria-label="行動卡兩種表徵"><span>文本線索 → ${esc(lab.mainText.representationLabels[0])}</span><span>證據組合 → ${esc(lab.mainText.representationLabels[1])}</span></div><button type="button" data-message-action="check-evidence" ${state.evidence.length < lab.mainText.requiredEvidenceIds.length || state.evidenceChecked ? "disabled" : ""}>檢查證據組合</button><p class="message-reading-feedback" aria-live="polite">${state.evidenceChecked ? esc(lab.mainText.evidenceAccepted) : esc(state.evidenceMessage || lab.mainText.evidenceHint)}</p></section>` : ""}
      ${state.evidenceChecked ? `<fieldset class="message-reading-stage"><legend>第三步｜選出最符合文本的理解</legend><p>${esc(lab.mainText.question.prompt)}</p>${options(lab.mainText.question, state.answer, "answer")}<button type="button" data-message-action="check-answer" ${!state.answer || state.completed ? "disabled" : ""}>檢查答案</button><p class="message-reading-feedback" aria-live="polite">${state.completed ? esc(lab.mainText.question.feedback) : state.answerAttempts ? esc(lab.mainText.question.retryHint) : ""}</p></fieldset>` : ""}
      ${state.completed ? `<section class="message-reading-stage"><h5>第四步｜換一封新訊息，遷移閱讀方法</h5><p>${esc(lab.transfer.introduction)}</p><ol class="message-reading-parts" aria-label="遷移用原創書信">${parts(lab.transfer.parts, state.transferEvidence, "transfer")}</ol><fieldset><legend>${esc(lab.transfer.question.prompt)}</legend>${options(lab.transfer.question, state.transferAnswer, "transferAnswer")}<label for="message-reading-explanation-${esc(instance)}">${esc(lab.transfer.explanationPrompt)}</label><textarea id="message-reading-explanation-${esc(instance)}" data-message-text="explanation" rows="2">${esc(state.explanation)}</textarea><button type="button" data-message-action="check-transfer" ${state.completed === "done" ? "disabled" : ""}>檢查遷移答案</button><p class="message-reading-feedback" aria-live="polite">${state.completed === "done" ? esc(lab.transfer.feedback) : esc(state.transferMessage || lab.transfer.hint)}</p></fieldset></section>` : ""}
      <p class="message-reading-live" role="status" aria-live="polite">${state.completed === "done" ? "互動完成：預測、證據、文本理解與新文本遷移皆已保存。" : state.completed ? "主要內容正確；請完成新文本遷移。" : state.predicted ? "預測已保存；請標註支持理解的文本證據。" : "答案尚未揭露；請先留下自己的預測。"}</p><button type="button" class="message-reading-reset" data-message-action="reset">重新開始</button></section>`;
  };

  const activities = new Map();
  const rerender = (root, focus) => {
    const item = activities.get(root.dataset.messageReadingLab); if (!item) return;
    const instance = root.dataset.messageInstance;
    root.outerHTML = render(item, instance);
    const next = [...document.querySelectorAll("[data-message-reading-lab]")].find(node => node.dataset.messageReadingLab === item.id && node.dataset.messageInstance === instance);
    next?.querySelector(focus)?.focus();
  };
  const mount = item => activities.set(item.id, item);
  const renderAndMount = (item, instance) => { mount(item); return render(item, instance); };

  document.addEventListener("input", event => {
    const root = event.target.closest("[data-message-reading-lab]"); if (!root) return;
    const item = activities.get(root.dataset.messageReadingLab); const field = event.target.dataset.messageText; if (!item || !field) return;
    const state = read(item, root.dataset.messageInstance); state[field] = event.target.value; write(item, root.dataset.messageInstance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-message-reading-lab]"); if (!root || !event.target.dataset.messageValue) return;
    const item = activities.get(root.dataset.messageReadingLab); if (!item) return;
    const state = read(item, root.dataset.messageInstance); state[event.target.dataset.messageValue] = event.target.value; write(item, root.dataset.messageInstance, state);
    const button = root.querySelector(`[data-message-action="${event.target.dataset.messageValue === "answer" ? "check-answer" : "check-transfer"}"]`); if (button) button.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-message-reading-lab]"); if (!root) return;
    const item = activities.get(root.dataset.messageReadingLab); if (!item) return;
    const instance = root.dataset.messageInstance; const lab = item.interactive.messageReadingLab; const state = read(item, instance);
    const evidenceButton = event.target.closest("[data-message-evidence]");
    if (evidenceButton) {
      const field = evidenceButton.dataset.messageEvidence === "main" ? "evidence" : "transferEvidence";
      const ids = state[field]; state[field] = ids.includes(evidenceButton.dataset.part) ? ids.filter(id => id !== evidenceButton.dataset.part) : [...ids, evidenceButton.dataset.part];
      if (field === "evidence") { state.evidenceChecked = false; state.evidenceMessage = ""; state.answer = ""; state.answerAttempts = 0; state.completed = false; state.transferEvidence = []; state.transferAnswer = ""; state.explanation = ""; }
      else state.transferMessage = "";
      write(item, instance, state); rerender(root, `[data-message-evidence="${field === "evidence" ? "main" : "transfer"}"][data-part="${evidenceButton.dataset.part}"]`); return;
    }
    const action = event.target.closest("[data-message-action]")?.dataset.messageAction; if (!action) return;
    if (action === "reset") { try { localStorage.removeItem(key(item, instance)); } catch {} rerender(root, '[data-message-text="prediction"]'); return; }
    if (action === "predict") {
      if (state.prediction.trim().length < 8) { state.predictionMessage = "請先用至少 8 個字描述你預測的主要內容，再開啟原文核對。"; write(item, instance, state); rerender(root, '[data-message-text="prediction"]'); return; }
      state.predicted = true; state.predictionMessage = ""; write(item, instance, state); rerender(root, '[data-message-evidence="main"]'); return;
    }
    if (action === "check-evidence") {
      const required = lab.mainText.requiredEvidenceIds; state.evidenceChecked = required.every(id => state.evidence.includes(id));
      state.evidenceMessage = state.evidenceChecked ? "" : lab.mainText.evidenceRetryHint; write(item, instance, state); rerender(root, state.evidenceChecked ? 'input[name^="answer-"]' : '[data-message-evidence="main"]'); return;
    }
    if (action === "check-answer" && state.answer) {
      if (state.answer === lab.mainText.question.answer) state.completed = true; else state.answerAttempts += 1;
      write(item, instance, state); rerender(root, state.completed ? '[data-message-evidence="transfer"]' : 'input[name^="answer-"]'); return;
    }
    if (action === "check-transfer" && state.transferAnswer && state.explanation.trim().length < lab.transfer.minimumExplanationLength) {
      state.transferMessage = `請至少寫 ${lab.transfer.minimumExplanationLength} 字，說明所選線索如何支持你的下一步。`; write(item, instance, state); rerender(root, '[data-message-text="explanation"]'); return;
    }
    if (action === "check-transfer" && state.transferAnswer) {
      const validEvidence = lab.transfer.requiredEvidenceIds.every(id => state.transferEvidence.includes(id));
      const valid = state.transferAnswer === lab.transfer.question.answer && validEvidence;
      state.completed = valid ? "done" : true; state.transferMessage = valid ? "" : lab.transfer.retryHint; write(item, instance, state); rerender(root, valid ? ".message-reading-reset" : '[data-message-evidence="transfer"]');
    }
  });
  window.MessageReadingLab = { render: renderAndMount };
})();

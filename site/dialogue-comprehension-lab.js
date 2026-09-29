(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const stateKey = (item, instance) => `dialogue-lab:${item.id}:${instance || "default"}`;
  const defaults = () => ({ prediction: "", predicted: false, evidence: [], evidenceChecked: false, answer: "", answerAttempts: 0, transferEvidence: "", transferAnswer: "", explanation: "", completed: false });
  const read = (item, instance) => {
    try { return { ...defaults(), ...JSON.parse(localStorage.getItem(stateKey(item, instance)) || "{}") }; }
    catch { return defaults(); }
  };
  const write = (item, instance, state) => localStorage.setItem(stateKey(item, instance), JSON.stringify(state));

  const render = (item, instance = "default") => {
    const activity = item.interactive.dialogueLab;
    if (!activity) return "";
    const state = read(item, instance);
    const lines = (conversation, selected, selector, disabled = false) => conversation.map(line => `<li class="dialogue-line${selected.includes(line.id) ? " is-selected" : ""}"><span class="dialogue-speaker">${esc(line.speaker)}</span><span>${esc(line.text)}</span><button type="button" data-dialogue-select="${esc(selector)}" data-line="${esc(line.id)}" aria-pressed="${selected.includes(line.id)}" ${disabled ? "disabled" : ""}>${selected.includes(line.id) ? "已選為證據" : "選作證據"}</button></li>`).join("");
    const mainOptions = activity.mainQuestion.options.map(option => `<label class="dialogue-option"><input type="radio" name="main-${esc(instance)}" value="${esc(option.id)}" data-dialogue-value="answer" ${state.answer === option.id ? "checked" : ""}><span>${esc(option.text)}</span></label>`).join("");
    const transferOptions = activity.transfer.options.map(option => `<label class="dialogue-option"><input type="radio" name="transfer-${esc(instance)}" value="${esc(option.id)}" data-dialogue-value="transferAnswer" ${state.transferAnswer === option.id ? "checked" : ""}><span>${esc(option.text)}</span></label>`).join("");
    return `<section class="dialogue-lab" data-dialogue-lab="${esc(item.id)}" data-dialogue-instance="${esc(instance)}" aria-labelledby="dialogue-title-${esc(instance)}">
      <header><span class="dialogue-kicker">${esc(activity.label)}</span><h4 id="dialogue-title-${esc(instance)}">${esc(activity.title)}</h4><p>${esc(activity.goal)}</p></header>
      <ol class="dialogue-transcript" aria-label="原創對話紀錄">${lines(activity.conversation, state.evidence, "main", !state.predicted)}</ol>
      <div class="dialogue-stage"><h5>第一步｜先預測整段對話的重點</h5><label for="dialogue-prediction-${esc(instance)}">先用自己的話寫下猜測；答案暫不揭露。</label><textarea id="dialogue-prediction-${esc(instance)}" data-dialogue-text="prediction" rows="2" ${state.predicted ? "disabled" : ""}>${esc(state.prediction)}</textarea><button type="button" data-dialogue-action="predict" ${state.predicted ? "disabled" : ""}>記錄預測並開始找證據</button></div>
      ${state.predicted ? `<div class="dialogue-stage"><h5>第二步｜標出能串起「問題」與「後續安排」的發言</h5><p>逐句閱讀；至少選出兩句關鍵證據，再核對是否能說明整段對話。</p><button type="button" data-dialogue-action="check-evidence" ${state.evidence.length < 2 || state.evidenceChecked ? "disabled" : ""}>檢查證據組合</button>${state.evidenceChecked ? `<p class="dialogue-feedback" role="status">證據已同時涵蓋事件問題與後續安排。接著回答主旨題。</p>` : `<p class="dialogue-hint" aria-live="polite">${state.evidenceMessage || (state.evidence.length < 2 ? "提示：找出造成困難的一句，以及說明如何處理的一句。" : "已選取證據；確認它們合起來能涵蓋問題與回應。")}</p>`}</div>` : ""}
      ${state.evidenceChecked ? `<fieldset class="dialogue-stage"><legend>第三步｜選出涵蓋多輪訊息的主旨</legend>${mainOptions}<button type="button" data-dialogue-action="check-answer" ${!state.answer || state.completed ? "disabled" : ""}>檢查主旨</button><p class="dialogue-hint" aria-live="polite">${state.answerAttempts === 1 ? "提示：排除只提到單一地點或人物的選項，主旨要包含問題及解決方向。" : state.answerAttempts > 1 ? "再檢查對話最初的狀況，以及最後形成的安排；不要把未提及的活動加進摘要。" : ""}</p>${state.completed ? `<p class="dialogue-feedback" role="status">${esc(activity.mainQuestion.feedback)}</p>` : ""}</fieldset>` : ""}
      ${state.completed ? `<div class="dialogue-stage"><h5>第四步｜遷移：另一段對話能推出什麼安排？</h5><ol class="dialogue-transcript" aria-label="遷移用原創對話">${lines(activity.transfer.conversation, state.transferEvidence ? [state.transferEvidence] : [], "transfer")}</ol><fieldset><legend>${esc(activity.transfer.question)}</legend>${transferOptions}<label for="dialogue-explanation-${esc(instance)}">寫出你採用的線索與推理（至少 15 字）</label><textarea id="dialogue-explanation-${esc(instance)}" data-dialogue-text="explanation" rows="2">${esc(state.explanation)}</textarea><button type="button" data-dialogue-action="check-transfer" ${state.completed === "done" ? "disabled" : ""}>檢查遷移答案</button><p class="dialogue-hint" aria-live="polite">${state.completed === "done" ? esc(activity.transfer.feedback) : state.transferMessage || (state.transferAnswer && state.explanation.length < 15 ? "請補充至少 15 字，指出對話證據及它如何支持答案。" : "正確作答需同時選對行動、標出相關發言並說明理由。")}</p></fieldset></div>` : ""}
      <p class="dialogue-live" aria-live="polite">${state.completed === "done" ? "互動完成：已保存預測、證據與遷移解釋。" : state.completed ? "主旨判斷正確；請完成新情境遷移。" : state.predicted ? "預測已保存；標記問題和後續安排的證據。" : "請先留下預測；此時尚未顯示正解。"}</p>
      <button type="button" class="dialogue-reset" data-dialogue-action="reset">重新開始</button></section>`;
  };

  const rerender = (root, focus) => {
    const item = activities.get(root.dataset.dialogueLab);
    if (!item) return;
    const instance = root.dataset.dialogueInstance;
    root.outerHTML = render(item, instance);
    const next = [...document.querySelectorAll("[data-dialogue-lab]")].find(node => node.dataset.dialogueLab === item.id && node.dataset.dialogueInstance === instance);
    next?.querySelector(focus)?.focus();
  };
  const activities = new Map();
  const mount = item => { activities.set(item.id, item); };
  const renderAndMount = (item, instance) => { mount(item); return render(item, instance); };

  document.addEventListener("input", event => {
    const root = event.target.closest("[data-dialogue-lab]");
    if (!root) return;
    const item = activities.get(root.dataset.dialogueLab); if (!item) return;
    const key = event.target.dataset.dialogueText; if (!key) return;
    const state = read(item, root.dataset.dialogueInstance); state[key] = event.target.value;
    write(item, root.dataset.dialogueInstance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-dialogue-lab]");
    if (!root || !event.target.dataset.dialogueValue) return;
    const item = activities.get(root.dataset.dialogueLab); if (!item) return;
    const state = read(item, root.dataset.dialogueInstance); state[event.target.dataset.dialogueValue] = event.target.value;
    write(item, root.dataset.dialogueInstance, state);
    const check = root.querySelector('[data-dialogue-action="check-answer"]'); if (check) check.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-dialogue-lab]"); if (!root) return;
    const item = activities.get(root.dataset.dialogueLab); if (!item) return;
    const instance = root.dataset.dialogueInstance; const activity = item.interactive.dialogueLab; const state = read(item, instance);
    const action = event.target.closest("[data-dialogue-action]")?.dataset.dialogueAction;
    const selected = event.target.closest("[data-dialogue-select]");
    if (selected) {
      const field = selected.dataset.dialogueSelect === "main" ? "evidence" : "transferEvidence";
      const current = field === "evidence" ? state.evidence : (state.transferEvidence ? [state.transferEvidence] : []);
      if (field === "evidence") {
        state.evidence = current.includes(selected.dataset.line) ? current.filter(id => id !== selected.dataset.line) : [...current, selected.dataset.line];
        state.evidenceMessage = ""; state.evidenceChecked = false; state.answer = ""; state.answerAttempts = 0;
        state.completed = false; state.transferEvidence = ""; state.transferAnswer = ""; state.explanation = "";
      } else state.transferEvidence = current.includes(selected.dataset.line) ? "" : selected.dataset.line;
      write(item, instance, state);
      const selector = `[data-dialogue-select="${selected.dataset.dialogueSelect}"][data-line="${selected.dataset.line}"]`;
      rerender(root, selector); return;
    }
    if (!action) return;
    if (action === "reset") { localStorage.removeItem(stateKey(item, instance)); rerender(root, "[data-dialogue-text='prediction']"); return; }
    if (action === "predict" && state.prediction.trim()) { state.predicted = true; write(item, instance, state); rerender(root, '[data-dialogue-select="main"]'); return; }
    if (action === "check-evidence" && state.evidence.length >= 2) {
      const required = activity.evidenceLineIds;
      state.evidenceChecked = required.every(id => state.evidence.includes(id));
      state.evidenceMessage = state.evidenceChecked ? "" : "這組證據尚未同時涵蓋問題與解決安排；回到對話再找一輪。";
      write(item, instance, state); rerender(root, state.evidenceChecked ? 'input[name^="main-"]' : '[data-dialogue-select="main"]'); return;
    }
    if (action === "check-answer" && state.answer) {
      if (state.answer === activity.mainQuestion.answer) state.completed = true;
      else state.answerAttempts += 1;
      write(item, instance, state); rerender(root, state.completed ? '[data-dialogue-select="transfer"]' : 'input[name^="main-"]'); return;
    }
    if (action === "check-transfer" && state.transferAnswer && state.transferEvidence && state.explanation.trim().length >= 15) {
      const valid = state.transferAnswer === activity.transfer.answer && activity.transfer.evidenceLineIds.includes(state.transferEvidence);
      state.completed = valid ? "done" : true;
      state.transferMessage = valid ? "" : "答案與所選證據尚未相互支持；請回到該句核對行動與時間線。";
      write(item, instance, state); rerender(root, valid ? ".dialogue-reset" : '[data-dialogue-select="transfer"]');
    }
  });
  window.DialogueComprehensionLab = { render: renderAndMount };
})();

(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const storageKey = (item, instance) => `story-plot-lab:${item.id}:${instance || "default"}`;
  const defaults = () => ({ prediction: "", predicted: false, evidence: [], evidenceChecked: false, mainAnswer: "", mainAttempts: 0, mainPassed: false, transferEvidence: [], transferAnswer: "", explanation: "", completed: false });
  const read = (item, instance) => { try { return { ...defaults(), ...JSON.parse(localStorage.getItem(storageKey(item, instance)) || "{}") }; } catch { return defaults(); } };
  const write = (item, instance, state) => { try { localStorage.setItem(storageKey(item, instance), JSON.stringify(state)); } catch { /* progress persistence is optional */ } };

  const render = (item, instance = "default") => {
    const lab = item.interactive?.storyPlotLab;
    if (!lab) return "";
    const state = read(item, instance);
    const parts = (items, selected, kind, disabled = false) => items.map(part => `<li class="story-plot-part${selected.includes(part.id) ? " is-selected" : ""}"><div><strong>${esc(part.label)}</strong><p>${esc(part.text)}</p></div><button type="button" data-plot-evidence="${kind}" data-part="${esc(part.id)}" aria-pressed="${selected.includes(part.id)}" ${disabled ? "disabled" : ""}>${selected.includes(part.id) ? "已標記為情節證據" : "標記這段情節"}</button></li>`).join("");
    const choices = (question, selected, field, disabled = false) => question.options.map(option => `<label class="story-plot-option"><input type="radio" name="${esc(field)}-${esc(instance)}" value="${esc(option.id)}" data-plot-answer="${field}" ${selected === option.id ? "checked" : ""} ${disabled ? "disabled" : ""}><span>${esc(option.text)}</span></label>`).join("");
    const evidenceSummary = (selected, required) => `情節地圖：目標 → 障礙 → 嘗試／線索 → 選擇 → 結果／改變。已標記 ${selected.length} 段；本階段要求至少 ${required.length} 段。`;
    const mainFeedback = state.evidenceChecked ? lab.mainStory.evidenceAccepted : (state.evidenceMessage || lab.mainStory.evidenceHint);
    return `<section class="story-plot-lab" data-story-plot-lab="${esc(item.id)}" data-story-plot-instance="${esc(instance)}" aria-labelledby="story-plot-title-${esc(instance)}">
      <header><span class="story-plot-kicker">${esc(lab.label)}</span><h4 id="story-plot-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header>
      <section class="story-plot-stage"><h5>第一步｜先預測，再讀故事</h5><p>${esc(lab.mainStory.introduction)}</p><label for="story-plot-prediction-${esc(instance)}">用自己的話寫下角色可能採取的改變</label><textarea id="story-plot-prediction-${esc(instance)}" data-plot-text="prediction" rows="2" ${state.predicted ? "disabled" : ""}>${esc(state.prediction)}</textarea><button type="button" data-plot-action="predict" ${state.predicted ? "disabled" : ""}>保存預測並展開故事</button><p class="story-plot-feedback" aria-live="polite">${esc(state.predictionMessage || "")}</p></section>
      <ol class="story-plot-parts" aria-label="原創故事情節">${parts(lab.mainStory.parts, state.evidence, "main", !state.predicted)}</ol>
      ${state.predicted ? `<section class="story-plot-stage"><h5>第二步｜用證據重建情節弧</h5><p>${esc(evidenceSummary(state.evidence, lab.mainStory.requiredEvidenceIds))}</p><div class="story-plot-arc" aria-label="故事情節關係"><span>目標</span><span>障礙</span><span>嘗試／線索</span><span>選擇</span><span>結果／改變</span></div><button type="button" data-plot-action="check-main-evidence" ${!state.evidence.length || state.evidenceChecked ? "disabled" : ""}>檢查情節證據</button><p class="story-plot-feedback" aria-live="polite">${esc(mainFeedback)}</p></section>` : ""}
      ${state.evidenceChecked ? `<fieldset class="story-plot-stage"><legend>第三步｜選出最忠實的主要情節</legend><p>${esc(lab.mainStory.question.prompt)}</p>${choices(lab.mainStory.question, state.mainAnswer, "main")}<button type="button" data-plot-action="check-main-answer" ${!state.mainAnswer || state.mainPassed ? "disabled" : ""}>檢查摘要</button><p class="story-plot-feedback" aria-live="polite">${state.mainPassed ? esc(lab.mainStory.question.feedback) : esc(state.mainAttempts ? lab.mainStory.question.retryHint : "")}</p></fieldset>` : ""}
      ${state.mainPassed ? `<section class="story-plot-stage"><h5>第四步｜換一個故事，重新檢驗推論</h5><p>${esc(lab.transfer.introduction)}</p><ol class="story-plot-parts" aria-label="遷移用原創故事">${parts(lab.transfer.parts, state.transferEvidence, "transfer")}</ol><p>${esc(evidenceSummary(state.transferEvidence, lab.transfer.requiredEvidenceIds))}</p><fieldset><legend>${esc(lab.transfer.question.prompt)}</legend>${choices(lab.transfer.question, state.transferAnswer, "transfer", state.completed)}<label for="story-plot-explanation-${esc(instance)}">${esc(lab.transfer.explanationPrompt)}</label><textarea id="story-plot-explanation-${esc(instance)}" data-plot-text="explanation" rows="2" ${state.completed ? "disabled" : ""}>${esc(state.explanation)}</textarea><button type="button" data-plot-action="check-transfer" ${state.completed ? "disabled" : ""}>檢查遷移推論</button><p class="story-plot-feedback" aria-live="polite">${state.completed ? esc(lab.transfer.feedback) : esc(state.transferMessage || lab.transfer.evidenceHint)}</p></fieldset></section>` : ""}
      <p class="story-plot-live" role="status" aria-live="polite">${state.completed ? "互動完成：預測、情節證據、主要內容與新故事遷移皆已保存。" : state.mainPassed ? "主要情節已核對；請在新故事重新找線索並解釋人物改變。" : state.predicted ? "預測已保存；請依事件線索重建情節，不要只看結局。" : "正解尚未揭露；先留下預測，再閱讀故事。"}</p><button type="button" class="story-plot-reset" data-plot-action="reset">重新開始</button></section>`;
  };

  const activities = new Map();
  const mount = (item, instance) => { activities.set(item.id, item); return render(item, instance); };
  const rerender = (root, focus) => {
    const item = activities.get(root.dataset.storyPlotLab);
    if (!item) return;
    const instance = root.dataset.storyPlotInstance;
    root.outerHTML = render(item, instance);
    const next = [...document.querySelectorAll("[data-story-plot-lab]")].find(node => node.dataset.storyPlotLab === item.id && node.dataset.storyPlotInstance === instance);
    next?.querySelector(focus)?.focus();
  };

  document.addEventListener("input", event => {
    const root = event.target.closest("[data-story-plot-lab]");
    const field = event.target.dataset.plotText;
    if (!root || !field) return;
    const item = activities.get(root.dataset.storyPlotLab);
    if (!item) return;
    const state = read(item, root.dataset.storyPlotInstance);
    state[field] = event.target.value;
    write(item, root.dataset.storyPlotInstance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-story-plot-lab]");
    const field = event.target.dataset.plotAnswer;
    if (!root || !field) return;
    const item = activities.get(root.dataset.storyPlotLab);
    if (!item) return;
    const state = read(item, root.dataset.storyPlotInstance);
    state[field === "main" ? "mainAnswer" : "transferAnswer"] = event.target.value;
    write(item, root.dataset.storyPlotInstance, state);
    const button = root.querySelector(`[data-plot-action="${field === "main" ? "check-main-answer" : "check-transfer"}"]`);
    if (button) button.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-story-plot-lab]");
    if (!root) return;
    const item = activities.get(root.dataset.storyPlotLab);
    if (!item) return;
    const instance = root.dataset.storyPlotInstance;
    const lab = item.interactive.storyPlotLab;
    const state = read(item, instance);
    const evidenceButton = event.target.closest("[data-plot-evidence]");
    if (evidenceButton) {
      const field = evidenceButton.dataset.plotEvidence === "main" ? "evidence" : "transferEvidence";
      const ids = state[field];
      state[field] = ids.includes(evidenceButton.dataset.part) ? ids.filter(id => id !== evidenceButton.dataset.part) : [...ids, evidenceButton.dataset.part];
      if (field === "evidence") {
        state.evidenceChecked = false; state.evidenceMessage = ""; state.mainAnswer = ""; state.mainAttempts = 0; state.mainPassed = false;
        state.transferEvidence = []; state.transferAnswer = ""; state.explanation = ""; state.completed = false;
      } else {
        state.transferMessage = ""; state.transferAnswer = ""; state.explanation = ""; state.completed = false;
      }
      write(item, instance, state);
      rerender(root, `[data-plot-evidence="${field === "evidence" ? "main" : "transfer"}"][data-part="${evidenceButton.dataset.part}"]`);
      return;
    }
    const action = event.target.closest("[data-plot-action]")?.dataset.plotAction;
    if (!action) return;
    if (action === "reset") {
      try { localStorage.removeItem(storageKey(item, instance)); } catch { /* progress storage is optional */ }
      rerender(root, '[data-plot-text="prediction"]'); return;
    }
    if (action === "predict") {
      if (state.prediction.trim().length < 8) {
        state.predictionMessage = "請至少用 8 個字預測角色可能採取的改變，再開啟故事核對。";
        write(item, instance, state); rerender(root, '[data-plot-text="prediction"]'); return;
      }
      state.predicted = true; state.predictionMessage = ""; write(item, instance, state); rerender(root, '[data-plot-evidence="main"]'); return;
    }
    if (action === "check-main-evidence") {
      state.evidenceChecked = lab.mainStory.requiredEvidenceIds.every(id => state.evidence.includes(id));
      state.evidenceMessage = state.evidenceChecked ? "" : lab.mainStory.evidenceRetryHint;
      write(item, instance, state); rerender(root, state.evidenceChecked ? 'input[name^="main-"]' : '[data-plot-evidence="main"]'); return;
    }
    if (action === "check-main-answer" && state.mainAnswer) {
      if (state.mainAnswer === lab.mainStory.question.answer) state.mainPassed = true;
      else state.mainAttempts += 1;
      write(item, instance, state); rerender(root, state.mainPassed ? '[data-plot-evidence="transfer"]' : 'input[name^="main-"]'); return;
    }
    if (action === "check-transfer") {
      const enoughEvidence = lab.transfer.requiredEvidenceIds.every(id => state.transferEvidence.includes(id));
      if (!enoughEvidence) state.transferMessage = lab.transfer.evidenceHint;
      else if (!state.transferAnswer) state.transferMessage = "先選擇推論，再用你標記的情節證據說明。";
      else if (state.explanation.trim().length < lab.transfer.minimumExplanationLength) state.transferMessage = `請至少用 ${lab.transfer.minimumExplanationLength} 字說明線索、方案與結果如何連結。`;
      else if (state.transferAnswer !== lab.transfer.question.answer) state.transferMessage = lab.transfer.retryHint;
      else { state.completed = true; state.transferMessage = ""; }
      write(item, instance, state); rerender(root, state.completed ? ".story-plot-reset" : '[data-plot-text="explanation"]');
    }
  });

  window.StoryPlotLab = { render: mount };
})();

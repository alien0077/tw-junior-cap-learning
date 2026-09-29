(() => {
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `story-elements-lab:${item.id}:${instance || "default"}`;
  const fresh = () => ({ prediction: "", revealed: false, cardIndex: 0, answers: {}, selectedAnswer: "", attempts: 0, feedback: "", evidence: [], synthesisAnswer: "", explanation: "", complete: false, synthesisMessage: "" });
  const read = (item, instance) => { try { return { ...fresh(), ...JSON.parse(localStorage.getItem(key(item, instance)) || "{}") }; } catch { return fresh(); } };
  const write = (item, instance, state) => { try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* progress persistence is optional */ } };
  const choiceMarkup = (q, value, field, instance, disabled = false) => q.options.map(option => `<label class="story-elements-choice"><input type="radio" name="${esc(field)}-${esc(instance)}" data-se-choice="${esc(field)}" value="${esc(option.id)}" ${value === option.id ? "checked" : ""} ${disabled ? "disabled" : ""}><span>${esc(option.text)}</span></label>`).join("");
  const render = (item, instance = "default") => {
    const lab = item.interactive?.storyElementsLab;
    if (!lab) return "";
    const s = read(item, instance);
    const status = s.complete ? "編輯任務完成：六項故事要素已辨認，主題判讀也已用多項證據說明。" : !s.revealed ? "預測尚未提交；故事線索和分類答案仍未展開。" : s.cardIndex < lab.cards.length ? `標註進度 ${s.cardIndex + 1}/${lab.cards.length}：根據這段原文判斷它在故事中的功能。` : "六張線索卡已完成；請用多項證據寫下主題判讀。";
    let workspace = `<section class="story-elements-stage"><h5>編輯前先預測</h5><p>${esc(lab.predictionPrompt)}</p><label for="se-prediction-${esc(instance)}">你的預測</label><textarea id="se-prediction-${esc(instance)}" data-se-text="prediction" rows="2" ${s.revealed ? "disabled" : ""}>${esc(s.prediction)}</textarea><button type="button" data-se-action="reveal" ${s.revealed ? "disabled" : ""}>保存預測，打開故事稿</button><p class="story-elements-feedback" aria-live="polite">${esc(s.feedback)}</p></section>`;
    if (s.revealed && s.cardIndex < lab.cards.length) {
      const card = lab.cards[s.cardIndex];
      workspace += `<section class="story-elements-stage"><div class="story-elements-progress" aria-label="編輯卡片進度">線索卡 ${s.cardIndex + 1}／${lab.cards.length}</div><h5>${esc(card.label)}</h5><blockquote>${esc(card.excerpt)}</blockquote><fieldset><legend>${esc(card.question.prompt)}</legend>${choiceMarkup(card.question, s.selectedAnswer, "card", instance)}<button type="button" data-se-action="check-card" ${s.selectedAnswer ? "" : "disabled"}>檢查這張標註</button></fieldset><p class="story-elements-feedback" aria-live="polite">${esc(s.feedback)}</p>${s.answers[card.id] ? `<button type="button" data-se-action="next-card">${s.cardIndex + 1 === lab.cards.length ? "整理編輯註記" : "下一張線索卡"}</button>` : ""}</section>`;
    }
    if (s.revealed && s.cardIndex >= lab.cards.length) {
      const syn = lab.synthesis;
      workspace += `<section class="story-elements-stage"><h5>編輯註記｜用要素交叉支持主題</h5><p>${esc(syn.prompt)}</p><ol class="story-elements-evidence">${syn.evidence.map(ev => `<li class="${s.evidence.includes(ev.id) ? "is-selected" : ""}"><span><strong>${esc(ev.label)}</strong><br>${esc(ev.text)}</span><button type="button" data-se-evidence="${esc(ev.id)}" aria-pressed="${s.evidence.includes(ev.id)}">${s.evidence.includes(ev.id) ? "已納入證據" : "納入這項證據"}</button></li>`).join("")}</ol><fieldset><legend>${esc(syn.question.prompt)}</legend>${choiceMarkup(syn.question, s.synthesisAnswer, "synthesis", instance, s.complete)}<label for="se-explanation-${esc(instance)}">${esc(syn.explanationPrompt)}</label><textarea id="se-explanation-${esc(instance)}" data-se-text="explanation" rows="3" ${s.complete ? "disabled" : ""}>${esc(s.explanation)}</textarea><button type="button" data-se-action="check-synthesis" ${s.complete ? "disabled" : ""}>送出編輯註記</button></fieldset><p class="story-elements-feedback" aria-live="polite">${esc(s.complete ? syn.feedback : s.synthesisMessage || syn.hint)}</p></section>`;
    }
    return `<section class="story-elements-lab" data-story-elements-lab="${esc(item.id)}" data-story-elements-instance="${esc(instance)}" aria-labelledby="se-title-${esc(instance)}"><header><span class="story-elements-kicker">${esc(lab.label)}</span><h4 id="se-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p></header><section class="story-elements-manuscript"><h5>故事稿｜${esc(lab.storyTitle)}</h5><p>你現在是校刊故事編輯。閱讀片段時，分辨「文字提到什麼」和「這項要素在故事裡做什麼」；標註不能超出敘事者實際知道的範圍。</p></section>${workspace}<p class="story-elements-status" role="status" aria-live="polite">${esc(status)}</p><button type="button" class="story-elements-reset" data-se-action="reset">重新編輯</button></section>`;
  };
  const items = new Map();
  const mount = (item, instance) => { items.set(item.id, item); return render(item, instance); };
  const rerender = (root, selector) => {
    const item = items.get(root.dataset.storyElementsLab);
    if (!item) return;
    const instance = root.dataset.storyElementsInstance;
    root.outerHTML = render(item, instance);
    const next = [...document.querySelectorAll("[data-story-elements-lab]")].find(node => node.dataset.storyElementsLab === item.id && node.dataset.storyElementsInstance === instance);
    next?.querySelector(selector)?.focus();
  };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-story-elements-lab]");
    const field = event.target.dataset.seText;
    if (!root || !field) return;
    const state = read(items.get(root.dataset.storyElementsLab), root.dataset.storyElementsInstance);
    state[field] = event.target.value;
    write(items.get(root.dataset.storyElementsLab), root.dataset.storyElementsInstance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-story-elements-lab]");
    const field = event.target.dataset.seChoice;
    if (!root || !field) return;
    const item = items.get(root.dataset.storyElementsLab);
    const state = read(item, root.dataset.storyElementsInstance);
    state[field === "card" ? "selectedAnswer" : "synthesisAnswer"] = event.target.value;
    if (field === "card") {
      state.feedback = "";
      const card = item.interactive.storyElementsLab.cards[state.cardIndex];
      if (card) delete state.answers[card.id];
    }
    write(item, root.dataset.storyElementsInstance, state);
    const button = root.querySelector(`[data-se-action="${field === "card" ? "check-card" : "check-synthesis"}"]`);
    if (button && !state.complete) button.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-story-elements-lab]");
    if (!root) return;
    const item = items.get(root.dataset.storyElementsLab);
    const instance = root.dataset.storyElementsInstance;
    const state = read(item, instance);
    const lab = item.interactive.storyElementsLab;
    const evidenceButton = event.target.closest("[data-se-evidence]");
    if (evidenceButton) {
      const id = evidenceButton.dataset.seEvidence;
      state.evidence = state.evidence.includes(id) ? state.evidence.filter(value => value !== id) : [...state.evidence, id];
      state.synthesisMessage = ""; state.synthesisAnswer = ""; state.explanation = ""; state.complete = false;
      write(item, instance, state);
      rerender(root, `[data-se-evidence="${id}"]`);
      return;
    }
    const action = event.target.closest("[data-se-action]")?.dataset.seAction;
    if (!action) return;
    if (action === "reset") {
      try { localStorage.removeItem(key(item, instance)); } catch { /* progress persistence is optional */ }
      rerender(root, '[data-se-text="prediction"]');
      return;
    }
    if (action === "reveal") {
      if (state.prediction.trim().length < 8) state.feedback = "請先寫至少 8 個字，預測讀者會從故事哪些線索理解人物與主題。";
      else { state.revealed = true; state.feedback = "預測已保留；現在逐張檢查故事線索的功能與證據範圍。"; }
      write(item, instance, state);
      rerender(root, state.revealed ? 'input[name^="card-"]' : '[data-se-text="prediction"]');
      return;
    }
    if (action === "check-card") {
      const card = lab.cards[state.cardIndex];
      if (state.selectedAnswer === card.question.answer) {
        state.answers[card.id] = state.selectedAnswer;
        state.feedback = card.question.feedback;
      } else {
        state.attempts += 1;
        state.feedback = card.question.hint;
      }
      write(item, instance, state);
      rerender(root, state.answers[card.id] ? '[data-se-action="next-card"]' : `input[name^="card-"]`);
      return;
    }
    if (action === "next-card") {
      if (state.answers[lab.cards[state.cardIndex]?.id]) {
        state.cardIndex += 1; state.selectedAnswer = ""; state.feedback = ""; state.attempts = 0;
        write(item, instance, state);
        rerender(root, state.cardIndex < lab.cards.length ? 'input[name^="card-"]' : '[data-se-evidence]');
      }
      return;
    }
    if (action === "check-synthesis") {
      const enoughEvidence = lab.synthesis.requiredEvidenceIds.every(id => state.evidence.includes(id));
      if (!enoughEvidence) state.synthesisMessage = lab.synthesis.hint;
      else if (!state.synthesisAnswer) state.synthesisMessage = "先選擇主題判讀，再說明證據如何支持它。";
      else if (state.explanation.trim().length < lab.synthesis.minimumExplanationLength) state.synthesisMessage = `請至少用 ${lab.synthesis.minimumExplanationLength} 字連結人物選擇、故事結果與主題。`;
      else if (state.synthesisAnswer !== lab.synthesis.question.answer) state.synthesisMessage = lab.synthesis.retryHint;
      else { state.complete = true; state.synthesisMessage = ""; }
      write(item, instance, state);
      rerender(root, state.complete ? ".story-elements-reset" : '[data-se-text="explanation"]');
    }
  });
  window.StoryElementsLab = { render: mount };
})();

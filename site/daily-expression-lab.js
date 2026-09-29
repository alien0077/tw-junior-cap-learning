(() => {
  const mounted = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
  const key = (item, instance) => `daily-expression-lab:${item.id}:${instance || "default"}`;
  const fresh = () => ({ sceneIndex: 0, cueIds: [], cueAccepted: false, answerId: "", answerPassed: false, transfer: false, transferCueIds: [], transferCueAccepted: false, transferAnswerId: "", transferAnswerPassed: false, explanation: "", completed: false, message: "" });
  const read = (item, instance) => {
    try { return { ...fresh(), ...JSON.parse(localStorage.getItem(key(item, instance)) || "{}") }; }
    catch { return fresh(); }
  };
  const write = (item, instance, state) => { try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* progress remains usable without storage */ } };
  const cues = (items, selected, kind) => `<ul class="delx-cues" aria-label="可供判讀的對話線索">${items.map(cue => `<li><button type="button" data-delx-cue="${kind}" data-cue-id="${esc(cue.id)}" aria-pressed="${selected.includes(cue.id)}">${esc(cue.text)}</button></li>`).join("")}</ul>`;
  const options = (question, selected, name, instance) => question.options.map(option => `<label class="delx-option"><input type="radio" name="${name}-${esc(instance)}" data-delx-answer="${name}" value="${esc(option.id)}" ${selected === option.id ? "checked" : ""}><span>${esc(option.text)}</span></label>`).join("");
  const render = (item, instance = "default") => {
    const lab = item.interactive?.dailyExpressionLab;
    if (!lab) return "";
    mounted.set(item.id, item);
    const state = read(item, instance);
    const shell = body => `<section class="daily-expression-lab" data-daily-expression-lab="${esc(item.id)}" data-delx-instance="${esc(instance)}" aria-labelledby="delx-title-${esc(instance)}"><header><span class="delx-kicker">${esc(lab.label)}</span><h4 id="delx-title-${esc(instance)}">${esc(lab.title)}</h4><p>${esc(lab.goal)}</p><p>${esc(lab.introduction)}</p></header>${body}</section>`;
    if (state.completed) return shell(`<p class="delx-status" role="status" aria-live="polite">${esc(lab.transfer.completionMessage)}</p><button type="button" data-delx-action="reset">重新開始</button>`);
    const status = `<p class="delx-status" role="status" aria-live="polite">${esc(state.message)}</p>`;
    if (!state.transfer) {
      const scene = lab.scenes[state.sceneIndex];
      let body = `<p class="delx-progress" role="status" aria-live="polite">對話 ${state.sceneIndex + 1}/${lab.scenes.length} · 先找線索，再接話</p>`;
      if (state.lastDialogue) body += `<p class="delx-next-line"><strong>對話接續：</strong>${esc(state.lastDialogue)}</p>`;
      body += `<article class="delx-scene"><span class="delx-scene-title">${esc(scene.title)}</span><pre>${esc(scene.dialogue)}</pre><p>${esc(scene.prompt)}</p></article>`;
      if (!state.cueAccepted) body += `<section class="delx-step"><h5>先標記會影響回應的線索</h5>${cues(scene.cues, state.cueIds, "scene")}<button type="button" data-delx-action="check-cues">檢查線索</button></section>`;
      else body += `<fieldset class="delx-step"><legend>${esc(scene.question.prompt)}</legend>${options(scene.question, state.answerId, "scene", instance)}<button type="button" data-delx-action="answer">送出回應</button></fieldset>`;
      body += status + `<button type="button" class="delx-reset" data-delx-action="reset">重設本次練習</button>`;
      return shell(body);
    }
    const transfer = lab.transfer;
    let body = `<p class="delx-progress" role="status" aria-live="polite">新情境遷移 · 核對時間與地點後再回覆</p><article class="delx-scene"><span class="delx-scene-title">服務訊息</span><blockquote>${esc(transfer.notice)}</blockquote><p>${esc(transfer.prompt)}</p></article>`;
    if (!state.transferCueAccepted) body += `<section class="delx-step"><h5>標出會改變下一步的訊息</h5>${cues(transfer.cues, state.transferCueIds, "transfer")}<button type="button" data-delx-action="check-transfer-cues">檢查線索</button></section>`;
    else if (!state.transferAnswerPassed) body += `<fieldset class="delx-step"><legend>${esc(transfer.question.prompt)}</legend>${options(transfer.question, state.transferAnswerId, "transfer", instance)}<button type="button" data-delx-action="transfer-answer">檢查回覆功能</button></fieldset>`;
    else body += `<section class="delx-step"><label for="delx-explanation-${esc(instance)}">${esc(transfer.explanationPrompt)}<textarea id="delx-explanation-${esc(instance)}" data-delx-explanation rows="3">${esc(state.explanation)}</textarea></label><button type="button" data-delx-action="finish-transfer">檢查證據理由</button></section>`;
    body += status + `<button type="button" class="delx-reset" data-delx-action="reset">重設本次練習</button>`;
    return shell(body);
  };
  const rerender = (root, focus) => {
    const item = mounted.get(root.dataset.dailyExpressionLab);
    if (!item) return;
    const instance = root.dataset.delxInstance || "default";
    const holder = document.createElement("div"); holder.innerHTML = render(item, instance);
    const updated = holder.firstElementChild; root.replaceWith(updated); if (focus) updated.querySelector(focus)?.focus();
  };
  const mount = item => mounted.set(item.id, item);
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-daily-expression-lab]");
    if (!root || !event.target.matches("[data-delx-explanation]")) return;
    const item = mounted.get(root.dataset.dailyExpressionLab); if (!item) return;
    const instance = root.dataset.delxInstance || "default"; const state = read(item, instance);
    state.explanation = event.target.value; write(item, instance, state);
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-daily-expression-lab]");
    if (!root || !event.target.matches("[data-delx-answer]")) return;
    const item = mounted.get(root.dataset.dailyExpressionLab); if (!item) return;
    const instance = root.dataset.delxInstance || "default"; const state = read(item, instance);
    if (event.target.dataset.delxAnswer === "scene") state.answerId = event.target.value;
    else state.transferAnswerId = event.target.value;
    write(item, instance, state);
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-daily-expression-lab]"); if (!root) return;
    const item = mounted.get(root.dataset.dailyExpressionLab); if (!item) return;
    const instance = root.dataset.delxInstance || "default"; const lab = item.interactive.dailyExpressionLab; const state = read(item, instance);
    const cueButton = event.target.closest("[data-delx-cue]");
    if (cueButton) {
      const field = cueButton.dataset.delxCue === "scene" ? "cueIds" : "transferCueIds";
      const ids = state[field]; state[field] = ids.includes(cueButton.dataset.cueId) ? ids.filter(id => id !== cueButton.dataset.cueId) : [...ids, cueButton.dataset.cueId];
      state.message = ""; write(item, instance, state); rerender(root, `[data-delx-cue="${cueButton.dataset.delxCue}"][data-cue-id="${cueButton.dataset.cueId}"]`); return;
    }
    const action = event.target.closest("[data-delx-action]")?.dataset.delxAction; if (!action) return;
    if (action === "reset") { try { localStorage.removeItem(key(item, instance)); } catch {} rerender(root, "[data-delx-cue]"); return; }
    if (action === "check-cues" || action === "check-transfer-cues") {
      const isTransfer = action === "check-transfer-cues"; const scene = isTransfer ? lab.transfer : lab.scenes[state.sceneIndex];
      const selected = isTransfer ? state.transferCueIds : state.cueIds;
      const accepted = scene.requiredCueIds.every(id => selected.includes(id)) && selected.every(id => scene.requiredCueIds.includes(id));
      if (isTransfer) state.transferCueAccepted = accepted; else state.cueAccepted = accepted;
      state.message = accepted ? "線索組合成立；現在選擇最符合功能與情境的回覆。" : (isTransfer ? lab.transfer.hint : scene.cueRetryHint);
      write(item, instance, state); rerender(root, accepted ? "input[type=radio]" : `[data-delx-cue="${isTransfer ? "transfer" : "scene"}"]`); return;
    }
    if (action === "answer") {
      const scene = lab.scenes[state.sceneIndex];
      if (!state.answerId) state.message = "先選一個回應，再送出檢查。";
      else if (state.answerId !== scene.question.answerId) state.message = scene.question.retryHint;
      else {
        state.message = scene.question.feedback; state.lastDialogue = scene.nextLine; state.sceneIndex += 1;
        state.cueIds = []; state.cueAccepted = false; state.answerId = "";
        if (state.sceneIndex >= lab.scenes.length) { state.transfer = true; state.lastDialogue = "三段對話已完成；現在用不同媒介檢查公告中的時間和地點。"; }
      }
      write(item, instance, state); rerender(root, state.transfer ? "[data-delx-cue]" : state.answerId ? "input[type=radio]" : "[data-delx-cue]"); return;
    }
    if (action === "transfer-answer") {
      const question = lab.transfer.question;
      if (!state.transferAnswerId) state.message = "先選一個回覆，再檢查它是否完成確認功能。";
      else if (state.transferAnswerId !== question.answerId) state.message = question.retryHint;
      else { state.transferAnswerPassed = true; state.message = question.feedback; }
      write(item, instance, state); rerender(root, state.transferAnswerPassed ? "[data-delx-explanation]" : "input[type=radio]"); return;
    }
    if (action === "finish-transfer") {
      const transfer = lab.transfer; const value = state.explanation.trim().toLocaleLowerCase();
      const hasEvidence = transfer.requiredEvidenceTerms.every(term => value.includes(term.toLocaleLowerCase()));
      if (value.length < transfer.minimumExplanationLength || !hasEvidence) state.message = transfer.retryHint;
      else { state.completed = true; state.message = transfer.feedback; }
      write(item, instance, state); rerender(root, state.completed ? "[data-delx-action='reset']" : "[data-delx-explanation]");
    }
  });
  window.DailyExpressionLab = { render: (item, instance = "default") => { mount(item); return render(item, instance); } };
})();

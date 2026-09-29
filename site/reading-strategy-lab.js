(() => {
  const activities = new Map();
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const key = (item, instance) => `reading-strategy-lab:${item.id}:${instance || "default"}`;
  const fresh = () => ({ index: 0, answers: [], selected: "", complete: false, message: "" });
  const read = (item, instance, count) => {
    try {
      const saved = JSON.parse(localStorage.getItem(key(item, instance)) || "{}");
      const answers = Array.isArray(saved.answers) ? saved.answers.slice(0, count) : [];
      const index = Math.min(count, Math.max(0, Number(saved.index) || 0), answers.length);
      return { index, answers, selected: String(saved.selected || ""), complete: Boolean(saved.complete && index === count), message: String(saved.message || "") };
    } catch { return fresh(); }
  };
  const write = (item, instance, state) => {
    try { localStorage.setItem(key(item, instance), JSON.stringify(state)); } catch { /* progress persistence is optional */ }
  };
  const render = (item, instance = "default") => {
    const activity = item.interactive;
    const steps = activity?.steps || [];
    if (!steps.length) return "";
    activities.set(item.id, item);
    const state = read(item, instance, steps.length);
    const shell = body => `<section class="reading-strategy-lab" data-reading-strategy-lab="${esc(item.id)}" data-rsl-instance="${esc(instance)}" aria-labelledby="rsl-title-${esc(instance)}"><header><span class="rsl-kicker">${esc(activity.labLabel || "閱讀任務實驗室")}</span><h4 id="rsl-title-${esc(instance)}">${esc(activity.labTitle || "依目的選策略，回到文本找證據")}</h4><p>${esc(activity.scenario)}</p></header>${body}</section>`;
    if (state.complete) return shell(`<p class="rsl-status" role="status" aria-live="polite">${esc(activity.completionMessage || `${steps.length} 項閱讀任務完成。你已依任務切換讀法，並回到文本確認證據。`)}</p><button type="button" data-rsl-action="reset">重新開始</button>`);
    const step = steps[state.index];
    const selected = state.answers[state.index] || state.selected;
    const options = step.options.map((option, index) => {
      const id = `rsl-${instance}-${state.index}-${index}`;
      const value = String.fromCharCode(65 + index);
      return `<label class="rsl-option" for="${esc(id)}"><input id="${esc(id)}" type="radio" name="rsl-answer-${esc(instance)}" data-rsl-answer value="${value}" ${selected === value ? "checked" : ""}><span><b>${value}.</b> ${esc(option)}</span></label>`;
    }).join("");
    const excerpt = step.text ? `<blockquote class="rsl-excerpt" aria-label="本題原創閱讀文本"><p>${esc(step.text)}</p></blockquote>` : "";
    const body = `<p class="rsl-progress">任務 ${state.index + 1}／${steps.length}</p><progress max="${steps.length}" value="${state.index}" aria-label="閱讀任務完成進度"></progress><article class="rsl-task">${excerpt}<h5>${esc(step.prompt)}</h5><fieldset><legend>選擇最符合問題目的讀法或文本證據</legend>${options}</fieldset><button type="button" data-rsl-action="check">檢查並前進</button><p class="rsl-status" role="status" aria-live="polite">${esc(state.message)}</p></article><button type="button" data-rsl-action="reset">重設本次練習</button>`;
    return shell(body);
  };
  const rerender = root => {
    const item = activities.get(root.dataset.readingStrategyLab);
    if (!item) return;
    const instance = root.dataset.rslInstance || "default";
    const next = document.createElement("div");
    next.innerHTML = render(item, instance);
    root.replaceWith(next.firstElementChild);
  };
  document.addEventListener("click", event => {
    const button = event.target.closest("[data-rsl-action]");
    const root = button?.closest("[data-reading-strategy-lab]");
    if (!root) return;
    const item = activities.get(root.dataset.readingStrategyLab);
    if (!item) return;
    const instance = root.dataset.rslInstance || "default";
    if (button.dataset.rslAction === "reset") {
      try { localStorage.removeItem(key(item, instance)); } catch { /* reset remains available without storage */ }
      rerender(root);
      return;
    }
    const steps = item.interactive.steps;
    const state = read(item, instance, steps.length);
    const choice = root.querySelector("[data-rsl-answer]:checked")?.value;
    const step = steps[state.index];
    if (!choice) state.message = "先選一個答案，再檢查你的策略。";
    else if (choice !== step.answer) {
      state.selected = choice;
      state.message = step.retryHint || "回到問題指定的資訊，核對它在文本中的位置與用途，再試一次。";
    }
    else {
      state.answers[state.index] = choice;
      state.selected = "";
      state.index += 1;
      state.complete = state.index === steps.length;
      state.message = state.complete ? "閱讀任務完成。" : step.feedback;
    }
    write(item, instance, state);
    rerender(root);
  });
  window.ReadingStrategyLab = { render };
})();

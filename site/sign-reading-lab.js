/* Data-driven English signage interaction: predict, manipulate, compare, explain, transfer. */
(() => {
  const activities = new Map();
  const keyPrefix = "tw-junior-cap-learning/sign-reading-lab/v1/";
  const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
  const defaults = () => ({ caseIndex: 0, predicted: false, direction: null, answer: "", revealed: false, attempts: 0, reflection: "" });
  const stateKey = (item, instance) => `${keyPrefix}${item.id}/${instance}`;
  const read = (item, instance) => {
    try { return { ...defaults(), ...JSON.parse(localStorage.getItem(stateKey(item, instance)) || "{}") }; }
    catch { return defaults(); }
  };
  const write = (item, instance, state) => localStorage.setItem(stateKey(item, instance), JSON.stringify(state));
  const render = (item, instance = "lab-main") => {
    const activity = item.interactive;
    if (activity?.type !== "language-signage-lab" || !activity.signageScenarios?.length) return "";
    activities.set(item.id, item);
    const state = read(item, instance);
    const scenario = activity.signageScenarios[Math.max(0, Math.min(activity.signageScenarios.length - 1, state.caseIndex))];
    const direction = state.direction || scenario.initialDirection;
    const arrow = direction === "left" ? "←" : "→";
    const correct = scenario.answerByDirection[direction];
    const cases = activity.signageScenarios.map((entry, index) => `<button type="button" data-sign-case="${index}" ${index === state.caseIndex ? 'aria-current="step"' : ""} ${!state.revealed && index !== state.caseIndex ? "disabled" : ""}>${index + 1}. ${esc(entry.place)}</button>`).join("");
    const choices = scenario.options.map((option, index) => {
      const letter = String.fromCharCode(65 + index);
      return `<label class="sign-choice"><input type="radio" name="sign-answer-${esc(instance)}" value="${letter}" data-sign-answer ${state.answer === letter ? "checked" : ""} ${!state.predicted || state.revealed ? "disabled" : ""}><span>${letter}. ${esc(option)}</span></label>`;
    }).join("");
    const outcome = state.revealed
      ? `<div class="sign-evidence" role="status" tabindex="-1"><b>答案：${correct}</b><p>${esc(scenario.evidenceByDirection[direction])}</p><p>${state.answer === correct ? "判斷正確：你有把文字與方向線索一起核對。" : `再看一次：答案 ${correct} 才同時符合標示文字和地圖位置。`}</p></div>`
      : state.attempts > 0 ? `<p class="sign-hint" role="status" tabindex="-1">先找出標示中的目的地詞，再確認箭頭指向的地圖標籤；線索衝突時不要猜。</p>` : "";
    const nextIndex = state.caseIndex + 1;
    return `<section class="activity signage-lab" data-signage-lab="${esc(item.id)}" data-signage-instance="${esc(instance)}" aria-labelledby="signage-title-${esc(instance)}">
      <h4 id="signage-title-${esc(instance)}">互動：先預測，再讓標示與地圖一起接受檢驗</h4><p>${esc(activity.goal)}</p>
      <nav class="sign-case-tabs" aria-label="練習情境">${cases}</nav>
      <p class="sign-task"><b>${esc(scenario.place)}｜任務：</b>${esc(scenario.task)}</p>
      <div class="sign-evidence-grid"><div class="sign-card"><span>標示文字</span><strong lang="en">${esc(scenario.signText)} ${state.predicted ? `<span aria-label="箭頭方向 ${direction === "left" ? "左" : "右"}">${arrow}</span>` : "?"}</strong><small>${state.predicted ? "位置線索已顯示" : "先預測後再操作"}</small></div>
      <div class="sign-map" role="img" aria-label="地圖：左側是${esc(scenario.leftDestination)}，目前位置在中間，右側是${esc(scenario.rightDestination)}；箭頭指向${direction === "left" ? "左" : "右"}"><span class="map-destination">${esc(scenario.leftDestination)}</span><span class="map-current">你在這裡</span><span class="map-destination">${esc(scenario.rightDestination)}</span><b class="map-arrow map-arrow-${direction}" aria-hidden="true">${arrow}</b></div></div>
      <div class="sign-prediction"><label for="sign-prediction-${esc(instance)}">第一步｜先寫下你的預測（答案暫不揭露）</label><textarea id="sign-prediction-${esc(instance)}" data-sign-reflection rows="2" ${state.predicted ? "disabled" : ""}>${esc(state.reflection)}</textarea><button type="button" data-sign-action="predict" ${state.predicted ? "disabled" : ""}>記錄預測並開始操作</button></div>
      <div class="sign-manipulate"><b>第二步｜只改變一項線索</b><p>翻轉箭頭方向，觀察箭頭與地圖路徑如何同步改變；標示目的地文字不變。</p><button type="button" data-sign-action="flip" ${!state.predicted || state.revealed ? "disabled" : ""}>翻轉箭頭（目前${direction === "left" ? "向左" : "向右"}）</button></div>
      <fieldset class="sign-answer"><legend>第三步｜選擇行動，並用文字和位置作證</legend>${choices}<button type="button" data-sign-action="check" ${!state.predicted || !state.answer || state.revealed ? "disabled" : ""}>檢查我的判斷</button>${outcome}</fieldset>
      <p class="sign-live" aria-live="polite">${state.revealed ? "已完成本情境；你可以進入新場所遷移練習。" : state.predicted ? "預測已保留。操作箭頭並選擇行動，再提交檢查。" : "請先寫預測；目前不顯示正解。"}</p>
      ${state.revealed && nextIndex < activity.signageScenarios.length ? `<button type="button" data-sign-case="${nextIndex}">進入新情境：${esc(activity.signageScenarios[nextIndex].place)}</button>` : ""}
      <button type="button" data-sign-action="reset">重新開始本互動</button></section>`;
  };
  const rerender = (root, focusSelector) => {
    const item = activities.get(root.dataset.signageLab);
    if (!item) return;
    const instance = root.dataset.signageInstance;
    const itemId = root.dataset.signageLab;
    root.outerHTML = render(item, instance);
    const nextRoot = [...document.querySelectorAll("[data-signage-lab]")].find(node => node.dataset.signageLab === itemId && node.dataset.signageInstance === instance);
    nextRoot?.querySelector(focusSelector)?.focus();
  };
  document.addEventListener("input", event => {
    const root = event.target.closest("[data-signage-lab]");
    if (!root || !event.target.matches("[data-sign-reflection]")) return;
    const item = activities.get(root.dataset.signageLab); if (item) write(item, root.dataset.signageInstance, { ...read(item, root.dataset.signageInstance), reflection: event.target.value });
  });
  document.addEventListener("change", event => {
    const root = event.target.closest("[data-signage-lab]");
    if (!root || !event.target.matches("[data-sign-answer]")) return;
    const item = activities.get(root.dataset.signageLab); if (item) write(item, root.dataset.signageInstance, { ...read(item, root.dataset.signageInstance), answer: event.target.value });
    const check = root.querySelector('[data-sign-action="check"]'); if (check) check.disabled = false;
  });
  document.addEventListener("click", event => {
    const root = event.target.closest("[data-signage-lab]"); if (!root) return;
    const item = activities.get(root.dataset.signageLab); if (!item) return;
    const instance = root.dataset.signageInstance; const state = read(item, instance); const scenario = item.interactive.signageScenarios[state.caseIndex]; const direction = state.direction || scenario.initialDirection; const correct = scenario.answerByDirection[direction];
    const caseButton = event.target.closest("[data-sign-case]");
    if (caseButton) {
      const index = Number(caseButton.dataset.signCase);
      if (Number.isInteger(index) && index >= 0 && index < item.interactive.signageScenarios.length && (index === state.caseIndex || state.revealed)) {
        write(item, instance, { ...defaults(), caseIndex: index }); rerender(root, "[data-sign-reflection]");
      }
      return;
    }
    const action = event.target.closest("[data-sign-action]")?.dataset.signAction; if (!action) return;
    if (action === "reset") { localStorage.removeItem(stateKey(item, instance)); rerender(root, "[data-sign-reflection]"); return; }
    if (action === "predict" && state.reflection.trim()) { state.predicted = true; state.direction = scenario.initialDirection; write(item, instance, state); rerender(root, '[data-sign-action="flip"]'); return; }
    if (action === "flip" && state.predicted && !state.revealed) { state.direction = direction === "left" ? "right" : "left"; state.answer = ""; state.attempts = 0; write(item, instance, state); rerender(root, "[data-sign-answer]"); return; }
    if (action === "check" && state.predicted && state.answer) { state.attempts += 1; state.revealed = state.answer === correct || state.attempts >= 2; write(item, instance, state); rerender(root, state.revealed ? ".sign-evidence" : ".sign-hint"); }
  });
  window.SignReadingLab = { render };
})();

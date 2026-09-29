import { InteractiveState } from "./interactive-engine.js";
import { COMPONENTS, renderComponentBody } from "./renderer-registry.js";

export const RENDERER_COMPONENTS = COMPONENTS;

const INTERACTIVE_STATE_PREFIX = "tw-junior-cap-learning:interactive:";

function stateStorage(key) {
  try {
    return globalThis.localStorage ? {
      get: () => globalThis.localStorage.getItem(key),
      set: (value) => globalThis.localStorage.setItem(key, value),
    } : null;
  } catch {
    return null;
  }
}

function hashState() {
  try {
    const value = globalThis.location?.hash?.startsWith("#state=")
      ? decodeURIComponent(globalThis.location.hash.slice("#state=".length))
      : null;
    return value || null;
  } catch {
    return null;
  }
}

function text(document, value) {
  const node = document.createElement("span");
  node.textContent = value;
  return node;
}

function normalizeAnswer(value) {
  return String(value ?? "")
    .replace(/[\s＝]/g, "")
    .replace(/[－−–]/g, "-")
    .replace(/[＋]/g, "+")
    .replace(/[＊×]/g, "*")
    .replace(/[（）]/g, (character) => character === "（" ? "(" : ")")
    .toLowerCase();
}

function renderGuidedActivity({ document, mount, activity }) {
  if (!activity || !Array.isArray(activity.stages) || activity.stages.length === 0) return null;
  const section = document.createElement("section");
  section.className = "guided-activity";
  section.setAttribute("aria-labelledby", "guided-activity-title");
  const heading = document.createElement("h4");
  heading.id = "guided-activity-title";
  heading.textContent = activity.title;
  section.append(heading);
  const introduction = document.createElement("p");
  introduction.textContent = activity.introduction;
  section.append(introduction);
  const progress = document.createElement("p");
  progress.className = "guided-activity-progress";
  progress.setAttribute("role", "status");
  progress.setAttribute("aria-live", "polite");
  section.append(progress);
  const prompt = document.createElement("label");
  const input = document.createElement("input");
  input.type = "text";
  input.autocomplete = "off";
  const submit = document.createElement("button");
  submit.type = "button";
  submit.textContent = "檢查這一步";
  const feedback = document.createElement("p");
  feedback.className = "guided-activity-feedback";
  feedback.setAttribute("aria-live", "polite");
  const hint = document.createElement("p");
  hint.className = "guided-activity-hint";
  hint.hidden = true;
  let stageIndex = 0;
  let complete = false;
  function updateStage() {
    if (complete) {
      progress.textContent = `已完成 ${activity.stages.length}/${activity.stages.length} 步`;
      prompt.textContent = activity.completionMessage;
      input.hidden = true;
      submit.hidden = true;
      return;
    }
    const current = activity.stages[stageIndex];
    progress.textContent = `第 ${stageIndex + 1}/${activity.stages.length} 步`;
    prompt.textContent = current.prompt;
    prompt.append(input);
    input.setAttribute("aria-label", current.prompt);
  }
  submit.addEventListener("click", () => {
    if (complete) return;
    const current = activity.stages[stageIndex];
    const answer = normalizeAnswer(input.value);
    if (!answer) {
      feedback.textContent = "請先輸入這一步的答案。";
      hint.hidden = true;
      return;
    }
    const accepted = current.acceptedAnswers.some((candidate) => normalizeAnswer(candidate) === answer);
    if (!accepted) {
      feedback.textContent = "這一步還不符合條件，請依提示檢查後再試。";
      hint.textContent = `提示：${current.hint}`;
      hint.hidden = false;
      input.focus();
      return;
    }
    feedback.textContent = current.correctFeedback;
    hint.hidden = true;
    input.value = "";
    stageIndex += 1;
    if (stageIndex >= activity.stages.length) {
      complete = true;
      feedback.textContent = activity.completionMessage;
    }
    updateStage();
    if (!complete) input.focus();
  });
  section.append(prompt, submit, feedback, hint);
  updateStage();
  mount.append(section);
  return section;
}

function renderLanguageTimelineActivity({ document, mount, activity, engine, storage }) {
  if (!activity?.sentence?.length || !activity.choices?.length) return null;
  const section = document.createElement("section");
  section.className = "language-timeline-lab";
  section.setAttribute("aria-labelledby", `${activity.title}-heading`);
  const heading = document.createElement("h4");
  heading.id = `${activity.title}-heading`;
  heading.textContent = activity.title;
  section.append(heading);
  const context = document.createElement("p");
  context.textContent = activity.context;
  section.append(context);
  const progress = document.createElement("p");
  progress.className = "language-timeline-progress";
  progress.setAttribute("role", "status");
  progress.setAttribute("aria-live", "polite");
  progress.textContent = "階段 1/4：先預測，再操作句子重音";
  section.append(progress);

  const predictionLabel = document.createElement("label");
  predictionLabel.textContent = "你的預測（填入句中一個字）：";
  const prediction = document.createElement("input");
  prediction.type = "text";
  prediction.autocomplete = "off";
  prediction.setAttribute("aria-label", "預測要承受對比重音的字");
  predictionLabel.append(prediction);
  const predict = document.createElement("button");
  predict.type = "button";
  predict.textContent = "提交預測並解鎖操作";
  section.append(predictionLabel, predict);

  const sentence = document.createElement("p");
  sentence.className = "language-timeline-sentence";
  sentence.setAttribute("aria-label", "可操作的英文句子");
  const renderSentence = (focus = null) => {
    sentence.replaceChildren();
    for (const [index, word] of activity.sentence.entries()) {
      if (index) sentence.append(document.createTextNode(" "));
      if (word === focus) {
        const emphasized = document.createElement("strong");
        emphasized.textContent = word;
        emphasized.setAttribute("aria-label", `${word}，目前的重音焦點`);
        sentence.append(emphasized);
      } else sentence.append(document.createTextNode(word));
    }
  };
  renderSentence();
  section.append(sentence);

  const choices = document.createElement("div");
  choices.className = "language-timeline-choices";
  choices.setAttribute("role", "group");
  choices.setAttribute("aria-label", "選擇重音焦點並觀察語意對比");
  const observation = document.createElement("p");
  observation.className = "language-timeline-observation";
  observation.setAttribute("aria-live", "polite");
  choices.hidden = true;
  for (const option of activity.choices) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `把重音放在「${option.word}」`;
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      renderSentence(option.word);
      for (const candidate of choices.querySelectorAll("button")) candidate.setAttribute("aria-pressed", String(candidate === button));
      const isCorrect = option.word === activity.correctWord;
      observation.textContent = `${option.contrast} 證據：${option.evidence}${isCorrect ? " 這與情境指定的更正焦點一致。" : " 請再比對情境指定要更正的資訊。"}`;
      progress.textContent = "階段 2/4：已操作重音焦點；比較聽者會注意到的資訊";
      engine.dispatch("manipulate", { state: { stressFocus: option.word } });
      engine.dispatch("observe", { state: { focusMatchesContext: isCorrect } });
      if (storage) { try { storage.set(engine.serialize()); } catch { /* storage is optional */ } }
      explanationLabel.hidden = false;
    });
    choices.append(button);
  }
  choices.append(observation);
  section.append(choices);

  const explanationLabel = document.createElement("label");
  explanationLabel.hidden = true;
  explanationLabel.textContent = "解釋：指出情境要更正什麼，以及重音如何幫助聽者辨認：";
  const explanation = document.createElement("input");
  explanation.type = "text";
  explanation.setAttribute("aria-label", "解釋重音焦點與情境證據的關係");
  const explain = document.createElement("button");
  explain.type = "button";
  explain.textContent = "記錄解釋並進入遷移題";
  const transfer = document.createElement("label");
  transfer.hidden = true;
  transfer.textContent = activity.transfer.prompt;
  const transferInput = document.createElement("input");
  transferInput.type = "text";
  transferInput.setAttribute("aria-label", "遷移題的重音焦點字");
  const transferButton = document.createElement("button");
  transferButton.type = "button";
  transferButton.textContent = "檢查遷移答案";
  const feedback = document.createElement("p");
  feedback.className = "language-timeline-feedback";
  feedback.setAttribute("aria-live", "polite");
  explanationLabel.append(explanation, explain);
  transfer.append(transferInput, transferButton);
  section.append(explanationLabel, transfer, feedback);

  predict.addEventListener("click", () => {
    if (!prediction.value.trim()) {
      feedback.textContent = "先提交一個預測字，再解鎖句子操作。";
      prediction.focus();
      return;
    }
    engine.dispatch("predict", { state: { prediction: prediction.value.trim() } });
    predict.disabled = true;
    prediction.readOnly = true;
    choices.hidden = false;
    progress.textContent = "階段 2/4：預測已保留；選一個字改變重音焦點";
    feedback.textContent = "預測已保留。操作不同字詞，觀察句子焦點如何改變；重音改變焦點，不會改寫句子文法。";
    if (storage) { try { storage.set(engine.serialize()); } catch { /* storage is optional */ } }
    choices.querySelector("button")?.focus();
  });
  explain.addEventListener("click", () => {
    if (!explanation.value.trim()) {
      feedback.textContent = "請用情境線索寫出一句解釋。";
      explanation.focus();
      return;
    }
    engine.dispatch("explain", { state: { stressExplanation: explanation.value.trim() } });
    explanationLabel.hidden = true;
    transfer.hidden = false;
    progress.textContent = "階段 3/4：解釋已記錄；用新句子檢查能否遷移";
    feedback.textContent = "解釋已記錄。新句改成更正收件人，請依角色線索選重音字。";
    if (storage) { try { storage.set(engine.serialize()); } catch { /* storage is optional */ } }
    transferInput.focus();
  });
  transferButton.addEventListener("click", () => {
    const answer = transferInput.value.trim().replace(/[.。!?！？]$/, "").toLowerCase();
    if (answer !== activity.transfer.acceptedWord.toLowerCase().replace(/[.。!?！？]$/, "")) {
      feedback.textContent = `再檢查一次：${activity.transfer.evidenceHint}`;
      transferInput.focus();
      return;
    }
    engine.dispatch("verify", { state: { transferAnswer: transferInput.value.trim(), transferPassed: true } });
    progress.textContent = "階段 4/4：遷移完成";
    feedback.textContent = `正確。${activity.transfer.evidenceHint}`;
    transferButton.disabled = true;
    if (storage) { try { storage.set(engine.serialize()); } catch { /* storage is optional */ } }
  });
  if (engine.state.prediction) {
    prediction.value = engine.state.prediction;
    prediction.readOnly = true;
    predict.disabled = true;
    choices.hidden = false;
    progress.textContent = "階段 2/4：預測已保留；選一個字改變重音焦點";
  }
  if (engine.state.stressFocus) {
    renderSentence(engine.state.stressFocus);
    for (const button of choices.querySelectorAll("button")) {
      button.setAttribute("aria-pressed", String(button.textContent.includes(`「${engine.state.stressFocus}」`)));
    }
    const selected = activity.choices.find((option) => option.word === engine.state.stressFocus);
    if (selected) {
      const matches = selected.word === activity.correctWord;
      observation.textContent = `${selected.contrast} 證據：${selected.evidence}${matches ? " 這與情境指定的更正焦點一致。" : " 請再比對情境指定要更正的資訊。"}`;
    }
    explanationLabel.hidden = false;
  }
  if (engine.state.stressExplanation) {
    explanation.value = engine.state.stressExplanation;
    explanationLabel.hidden = true;
    transfer.hidden = false;
    progress.textContent = "階段 3/4：解釋已記錄；用新句子檢查能否遷移";
  }
  if (engine.state.transferPassed) {
    transferInput.value = engine.state.transferAnswer || "";
    transferButton.disabled = true;
    progress.textContent = "階段 4/4：遷移完成";
    feedback.textContent = `正確。${activity.transfer.evidenceHint}`;
  }
  mount.append(section);
  return section;
}

/** Render the shared predict -> manipulate -> observe -> explain -> verify shell.
 * Subject renderers may replace the visualization body, but they must keep this
 * accessible state machine and fallback path.
 */
export function renderInteractiveBlock({ document, mount, spec, blockIndex = 0, lesson = null }) {
  const block = spec.interactiveBlocks[blockIndex];
  if (!block || !RENDERER_COMPONENTS.includes(block.component)) throw new Error("unregistered interactive block");
  const engine = new InteractiveState(block.initialState);
  const storage = stateStorage(`${INTERACTIVE_STATE_PREFIX}${block.id}`);
  if (storage) {
    try {
      const saved = storage.get();
      if (saved) engine.restore(saved);
    } catch {
      // A stale or unavailable browser record must not prevent the lesson from loading.
    }
  }
  try {
    const savedFromHash = hashState();
    if (savedFromHash) engine.restore(savedFromHash);
  } catch {
    // Ignore malformed shareable state and keep the lesson usable.
  }
  const root = document.createElement("section");
  root.className = "interactive-block";
  root.dataset.component = block.component;
  root.setAttribute("aria-labelledby", `${block.id}-title`);

  const heading = document.createElement("h3");
  heading.id = `${block.id}-title`;
  heading.append(text(document, block.component));
  root.append(heading);

  const purpose = document.createElement("p");
  purpose.className = "interactive-purpose";
  purpose.append(text(document, block.purpose));
  root.append(purpose);

  root.append(renderComponentBody({ document, spec, block, engine, storage, lesson }));
  renderLanguageTimelineActivity({ document, mount: root, activity: block.languageTimeline, engine, storage });
  renderGuidedActivity({ document, mount: root, activity: block.guidedActivity });

  const visualization = document.createElement("div");
  visualization.className = "visualization-summary";
  visualization.dataset.renderer = block.component;
  visualization.setAttribute("role", "group");
  visualization.setAttribute("aria-label", `${block.component} 視覺化與文字替代`);
  const visualizationTitle = document.createElement("strong");
  visualizationTitle.textContent = "視覺化提示";
  visualization.append(visualizationTitle);
  const visualizationList = document.createElement("ul");
  for (const rule of (spec.visualizations || []).slice(0, 4)) {
    const item = document.createElement("li");
    item.textContent = typeof rule === "string" ? rule : JSON.stringify(rule);
    visualizationList.append(item);
  }
  if (!visualizationList.children.length) {
    const item = document.createElement("li");
    item.textContent = "目前僅提供文字 fallback；視覺化內容待單元審查。";
    visualizationList.append(item);
  }
  visualization.append(visualizationList);
  root.append(visualization);

  const fallback = document.createElement("p");
  fallback.className = "interactive-fallback";
  fallback.textContent = `文字 fallback：${block.purpose}`;
  root.append(fallback);

  const output = document.createElement("output");
  output.className = "interactive-status";
  output.id = `${block.id}-status`;
  output.setAttribute("aria-live", "polite");
  output.textContent = `狀態：${engine.state.mode || "predict"}；${engine.state.transferPassed ? "遷移已完成" : "正解仍隱藏"}`;
  root.append(output);

  const controls = document.createElement("div");
  controls.className = "interactive-controls";
  function addAction(label, type, state, message) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = label;
    button.addEventListener("click", () => {
      const nextState = typeof state === "function" ? state(engine) : state;
      const snapshot = engine.dispatch(type, { state: nextState });
      if (storage) {
        try { storage.set(engine.serialize()); } catch { /* storage is optional */ }
      }
      output.textContent = snapshot.state.lastError || message(snapshot);
    });
    controls.append(button);
    return button;
  }
  addAction("提交預測", "predict", { predictionSubmitted: true }, () => "狀態：已提交預測；正解仍隱藏");
  addAction("操作一步", "manipulate", (current) => ({ step: (current.state.step || 0) + 1 }), (snapshot) => `狀態：已操作第 ${snapshot.state.step} 步；請記錄觀察`);
  addAction("記錄觀察", "observe", { observationRecorded: true }, () => "狀態：已記錄觀察；請用一句話解釋證據");
  const explanationSubmit = document.createElement("button");
  explanationSubmit.type = "button";
  explanationSubmit.textContent = "提交解釋";
  controls.append(explanationSubmit);
  explanationSubmit.dataset.requiresExplanation = "true";
  addAction("檢核並顯示局部回饋", "verify", { feedbackVisible: true }, () => "狀態：已檢核；先提供分層提示，不直接代答");
  root.append(controls);

  const explain = document.createElement("label");
  explain.append(text(document, "用一句話說明："));
  const input = document.createElement("input");
  input.type = "text";
  input.name = `${block.id}-explanation`;
  input.setAttribute("aria-label", "用一句話說明觀察到的關係");
  input.setAttribute("aria-describedby", output.id);
  explain.append(input);
  root.append(explain);
  explanationSubmit.addEventListener("click", (event) => {
    if (!input.value.trim()) {
      output.textContent = "請先輸入一句話解釋觀察到的證據";
      return;
    }
    engine.dispatch("explain", { state: { explanation: input.value.trim() } });
    if (storage) {
      try { storage.set(engine.serialize()); } catch { /* storage is optional */ }
    }
    output.textContent = "狀態：已提交解釋；可以進行檢核";
  });

  const state = document.createElement("button");
  state.type = "button";
  state.className = "state-export";
  state.textContent = "匯出操作紀錄";
  state.addEventListener("click", () => {
    root.dataset.serializedState = engine.serialize();
    try { globalThis.location.hash = `state=${encodeURIComponent(root.dataset.serializedState)}`; } catch { /* optional URL state */ }
    if (storage) {
      try { storage.set(root.dataset.serializedState); } catch { /* storage is optional */ }
    }
    output.textContent = "狀態：操作紀錄已序列化，可恢復測試";
  });
  root.append(state);
  if (engine.state.explanation) input.value = engine.state.explanation;
  root.dataset.reducedMotion = String(engine.reducedMotion);
  root.addEventListener("reducedmotionchange", (event) => {
    engine.setReducedMotion(event.detail?.enabled ?? true);
    root.dataset.reducedMotion = String(engine.reducedMotion);
  });
  mount.append(root);
  return { root, engine };
}

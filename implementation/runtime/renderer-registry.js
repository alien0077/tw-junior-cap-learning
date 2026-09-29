import { createRendererContract } from "./interactive-engine.js";

export const COMPONENTS = Object.freeze([
  "FunctionRepresentationBlock", "GeometryManipulationBlock", "DataExplorerBlock",
  "AlgebraEquationMeaningBlock", "EquivalentExpressionCheckBlock",
  "AlgebraBalanceBlock", "NumberLineBlock", "PhenomenonSimulationBlock",
  "ParticleModelBlock", "SystemRelationshipBlock", "EarthSystemBlock",
  "EvidenceLabBlock", "TextEvidenceBlock", "GuidedChoiceBlock", "LanguageTimelineBlock",
  "SignageReadingLab", "GenreReadingBlock", "TimelineCausalBlock", "MapDataBlock", "ScenarioDecisionBlock",
  "StepwiseReasoningBlock", "DialogueComprehensionLab", "StoryPlotLab",
  "StoryElementsStudio", "TextPredictionCalibrationLab", "ReadingStrategyLab", "ShortPlayLab", "DailyExpressionLab",
]);

export const RENDERER_METADATA = Object.freeze({
  FunctionRepresentationBlock: { kind: "function-representation", label: "函數表徵" },
  GeometryManipulationBlock: { kind: "geometry-manipulation", label: "幾何操作" },
  DataExplorerBlock: { kind: "data-explorer", label: "資料探索" },
  AlgebraEquationMeaningBlock: { kind: "algebra-equation-meaning", label: "等式與方程式語意" },
  EquivalentExpressionCheckBlock: { kind: "equivalent-expression-check", label: "等值表示檢查" },
  AlgebraBalanceBlock: { kind: "algebra-balance", label: "代數平衡" },
  NumberLineBlock: { kind: "number-line", label: "數線" },
  PhenomenonSimulationBlock: { kind: "phenomenon-simulation", label: "現象模擬" },
  ParticleModelBlock: { kind: "particle-model", label: "粒子模型" },
  SystemRelationshipBlock: { kind: "system-relationship", label: "系統關係" },
  EarthSystemBlock: { kind: "earth-system", label: "地球系統" },
  EvidenceLabBlock: { kind: "evidence-lab", label: "證據實驗室" },
  TextEvidenceBlock: { kind: "text-evidence", label: "文本證據" },
  GuidedChoiceBlock: { kind: "guided-choice", label: "引導選擇與即時回饋" },
  LanguageTimelineBlock: { kind: "language-timeline", label: "語言時間線" },
  SignageReadingLab: { kind: "signage-reading-lab", label: "標示閱讀實驗室" },
  GenreReadingBlock: { kind: "genre-reading", label: "體裁閱讀實驗室" },
  TimelineCausalBlock: { kind: "timeline-causal", label: "因果時間線" },
  MapDataBlock: { kind: "map-data", label: "地圖資料" },
  ScenarioDecisionBlock: { kind: "scenario-decision", label: "情境決策" },
  StepwiseReasoningBlock: { kind: "stepwise-reasoning", label: "步驟推理" },
  DialogueComprehensionLab: { kind: "dialogue-comprehension", label: "對話理解實驗室" },
  StoryPlotLab: { kind: "story-plot", label: "故事情節實驗室" },
  StoryElementsStudio: { kind: "story-elements", label: "故事編輯標註室" },
  TextPredictionCalibrationLab: { kind: "text-prediction", label: "文本預測校準實驗室" },
  ReadingStrategyLab: { kind: "reading-strategy-lab", label: "閱讀策略實驗室" },
  ShortPlayLab: { kind: "short-play-comprehension", label: "短劇理解實驗室" },
  DailyExpressionLab: { kind: "daily-expression", label: "生活對話修復工作台" },
});

const COMPONENT_MODELS = Object.freeze({
  FunctionRepresentationBlock: { model: "輸入／輸出對照", prompts: ["輸入變項", "輸出表徵", "改變後要比較的關係"] },
  GeometryManipulationBlock: { model: "形狀／量的操作", prompts: ["可調尺寸", "同步變化的幾何量", "需要檢查的不變關係"] },
  DataExplorerBlock: { model: "資料欄位與比較", prompts: ["資料欄位", "比較維度", "支持結論的資料點"] },
  AlgebraEquationMeaningBlock: { model: "情境等量與方程式意義", prompts: ["情境中的等量兩側", "未知量代表的對象", "檢查式子是否符合情境"] },
  EquivalentExpressionCheckBlock: { model: "等值式與輸出核對", prompts: ["待比較的兩個表示式", "共同代入值下的輸出", "等值或不等值的判斷依據"] },
  AlgebraBalanceBlock: { model: "等式兩側平衡", prompts: ["左側表徵", "右側表徵", "保持等值所需的操作"] },
  NumberLineBlock: { model: "數線位置與距離", prompts: ["目前位置", "移動方向／步長", "要比較的位置或距離"] },
  PhenomenonSimulationBlock: { model: "現象條件與結果", prompts: ["可改變條件", "可觀察現象", "支持解釋的觀察證據"] },
  ParticleModelBlock: { model: "粒子狀態與分布", prompts: ["粒子狀態", "分布或運動線索", "模型能支持的推論"] },
  SystemRelationshipBlock: { model: "系統元件與關係", prompts: ["系統元件", "關係或流向", "改變後受影響的元件"] },
  EarthSystemBlock: { model: "地球系統尺度", prompts: ["系統圈層／位置", "時間或空間尺度", "跨系統證據"] },
  EvidenceLabBlock: { model: "證據與主張", prompts: ["待檢驗主張", "可定位證據", "證據支持的推理步驟"] },
  TextEvidenceBlock: { model: "文本標記與推論", prompts: ["文本片段", "標記的語句功能", "由證據到結論的推論"] },
  GuidedChoiceBlock: { model: "情境線索、選項判斷與回饋", prompts: ["題目提供的語境線索", "符合線索的選項及理由", "錯答後需重新檢查的概念"] },
  LanguageTimelineBlock: { model: "語言事件時間線", prompts: ["事件／語句", "時間順序或轉折", "順序如何影響理解"] },
  SignageReadingLab: { model: "標示、方向與地圖線索", prompts: ["標示文字", "方向或位置線索", "用標示資訊選擇並說明路線"] },
  GenreReadingBlock: { model: "體裁、溝通目的與證據區塊", prompts: ["文本區塊", "讀者任務", "支持答案的格式或文字證據"] },
  TimelineCausalBlock: { model: "事件因果鏈", prompts: ["事件節點", "先後與因果連線", "支持因果判斷的資料"] },
  MapDataBlock: { model: "地圖位置與資料", prompts: ["位置或區域", "圖例／資料欄位", "空間分布支持的結論"] },
  ScenarioDecisionBlock: { model: "情境選擇與權衡", prompts: ["情境條件", "可比較選項", "支持決策的限制或證據"] },
  StepwiseReasoningBlock: { model: "步驟與理由", prompts: ["目前步驟", "下一個可驗證步驟", "每一步的理由或證據"] },
  DialogueComprehensionLab: { model: "對話語句、說話者目的與語氣", prompts: ["對話線索", "說話者意圖", "支持理解的回應或語氣"] },
  StoryPlotLab: { model: "故事事件、動機與結果", prompts: ["事件順序", "人物選擇", "選擇造成的結果"] },
  StoryElementsStudio: { model: "故事要素與主題證據", prompts: ["故事要素", "原文線索", "線索如何支持主題"] },
  TextPredictionCalibrationLab: { model: "封面線索、預測與正文校準", prompts: ["可見線索", "初步預測", "正文證據如何修正預測"] },
  ReadingStrategyLab: { model: "閱讀任務、策略選擇與證據檢核", prompts: ["本階閱讀任務", "可採取的策略", "新材料回測的證據"] },
  ShortPlayLab: { model: "短劇對白、舞台線索與衝突", prompts: ["對白或舞台指示", "角色目標／阻礙", "線索如何改變觀眾理解"] },
  DailyExpressionLab: { model: "語境線索、溝通功能與下一步回應", prompts: ["對話中可定位的線索", "說話者當下的溝通任務", "候選回應如何處理語氣與行動限制"] },
});

export function createRenderer(component, spec) {
  if (!COMPONENTS.includes(component)) throw new Error(`unregistered component: ${component}`);
  return createRendererContract(component, spec);
}

function renderDataExplorerLab({ document, mount, block }) {
  const lab = block.dataExplorerLab;
  if (!lab) return;
  const section = document.createElement("section");
  section.className = "data-explorer-lab";
  section.setAttribute("aria-labelledby", `${block.id}-data-lab-title`);
  const heading = document.createElement("h5");
  heading.id = `${block.id}-data-lab-title`;
  heading.textContent = lab.title;
  const context = document.createElement("p");
  context.textContent = lab.context;
  const predictionLabel = document.createElement("label");
  predictionLabel.textContent = lab.predictionPrompt;
  const prediction = document.createElement("input");
  prediction.type = "number";
  prediction.inputMode = "numeric";
  prediction.setAttribute("aria-label", lab.predictionPrompt);
  const submit = document.createElement("button");
  submit.type = "button";
  submit.textContent = "提交預測";
  const feedback = document.createElement("p");
  feedback.className = "data-explorer-feedback";
  feedback.setAttribute("role", "status");
  feedback.setAttribute("aria-live", "polite");
  const controls = document.createElement("fieldset");
  controls.hidden = true;
  const legend = document.createElement("legend");
  legend.textContent = lab.manipulationPrompt;
  const scaleLabel = document.createElement("label");
  const scale = document.createElement("input");
  scale.type = "range";
  scale.min = String(lab.initialUnit);
  scale.max = String(lab.changedUnit);
  scale.step = String(lab.changedUnit - lab.initialUnit);
  scale.value = String(lab.initialUnit);
  scale.setAttribute("aria-label", lab.manipulationPrompt);
  const scaleValue = document.createElement("output");
  scaleValue.textContent = `每格 ${scale.value} ${lab.unitLabel}`;
  scaleLabel.append(scale, scaleValue);
  const result = document.createElement("output");
  result.className = "data-explorer-result";
  result.setAttribute("aria-live", "polite");
  result.textContent = `${lab.intervals} 格；提交預測後才能查看讀值。`;
  const explanationLabel = document.createElement("label");
  explanationLabel.textContent = lab.explanationPrompt;
  const explanation = document.createElement("input");
  explanation.type = "text";
  explanation.setAttribute("aria-label", lab.explanationPrompt);
  const explain = document.createElement("button");
  explain.type = "button";
  explain.textContent = "檢查說明";
  const update = () => {
    const unit = Number(scale.value);
    scaleValue.textContent = `每格 ${unit} ${lab.unitLabel}`;
    result.textContent = `${lab.intervals} 格 × 每格 ${unit} ${lab.unitLabel} = ${lab.intervals * unit} ${lab.unitLabel}`;
  };
  let manipulated = false;
  submit.addEventListener("click", () => {
    const value = Number(prediction.value);
    if (!prediction.value || !Number.isFinite(value)) {
      feedback.textContent = "先輸入你的預測，再提交。";
      return;
    }
    if (value !== lab.expectedInitialValue) {
      feedback.textContent = lab.predictionHint;
      return;
    }
    feedback.textContent = lab.predictionAccepted;
    prediction.disabled = true;
    submit.disabled = true;
    controls.hidden = false;
    update();
    scale.focus();
  });
  scale.addEventListener("input", () => {
    manipulated = Number(scale.value) !== lab.initialUnit;
    update();
  });
  explain.addEventListener("click", () => {
    if (!manipulated) {
      feedback.textContent = "先操作刻度，觀察讀值改變後再說明。";
      scale.focus();
      return;
    }
    const value = explanation.value.trim().toLowerCase();
    const accepted = lab.acceptedExplanationTerms.every((term) => value.includes(term.toLowerCase()));
    feedback.textContent = accepted ? lab.explanationAccepted : lab.explanationHint;
    if (!accepted) explanation.focus();
  });
  controls.append(legend, scaleLabel, result, explanationLabel, explanation, explain);
  section.append(heading, context, predictionLabel, prediction, submit, feedback, controls);
  mount.append(section);
}

function renderGenreReadingLab({ document, mount, block, engine, storage }) {
  const lab = block.genreReadingLab;
  if (!lab?.sources?.length || !engine) return;
  const section = document.createElement("section");
  section.className = "genre-reading-lab";
  section.setAttribute("aria-labelledby", `${block.id}-genre-title`);
  const heading = document.createElement("h5");
  heading.id = `${block.id}-genre-title`;
  heading.textContent = lab.title;
  const context = document.createElement("p");
  context.textContent = lab.context;
  const progress = document.createElement("p");
  progress.className = "genre-reading-progress";
  progress.setAttribute("role", "status");
  progress.setAttribute("aria-live", "polite");
  const feedback = document.createElement("p");
  feedback.className = "genre-reading-feedback";
  feedback.setAttribute("role", "status");
  feedback.setAttribute("aria-live", "polite");

  const predictionLabel = document.createElement("label");
  predictionLabel.textContent = lab.predictionPrompt;
  const predictionInput = document.createElement("input");
  predictionInput.type = "text";
  predictionInput.autocomplete = "off";
  predictionInput.setAttribute("aria-label", lab.predictionPrompt);
  const predictButton = document.createElement("button");
  predictButton.type = "button";
  predictButton.textContent = "提交預測";
  predictionLabel.append(predictionInput);

  const sourceGroup = document.createElement("div");
  sourceGroup.className = "genre-reading-sources";
  sourceGroup.setAttribute("role", "group");
  sourceGroup.setAttribute("aria-label", "選擇要查閱的網頁區塊");
  sourceGroup.hidden = true;
  const observation = document.createElement("article");
  observation.className = "genre-reading-observation";
  observation.setAttribute("aria-live", "polite");
  const explanationLabel = document.createElement("label");
  explanationLabel.textContent = lab.explanationPrompt;
  explanationLabel.hidden = true;
  const explanationInput = document.createElement("input");
  explanationInput.type = "text";
  explanationInput.setAttribute("aria-label", lab.explanationPrompt);
  const explainButton = document.createElement("button");
  explainButton.type = "button";
  explainButton.textContent = "記錄證據說明";
  explanationLabel.append(explanationInput, explainButton);

  const transferLabel = document.createElement("label");
  transferLabel.className = "genre-reading-transfer";
  transferLabel.textContent = lab.transfer.prompt;
  transferLabel.hidden = true;
  const transferInput = document.createElement("input");
  transferInput.type = "text";
  transferInput.setAttribute("aria-label", lab.transfer.prompt);
  const transferButton = document.createElement("button");
  transferButton.type = "button";
  transferButton.textContent = "檢查遷移答案";
  transferLabel.append(transferInput, transferButton);

  const persist = () => { if (storage) { try { storage.set(engine.serialize()); } catch { /* storage is optional */ } } };
  const syncOverallStatus = () => {
    const output = mount.closest(".interactive-block")?.querySelector(".interactive-status");
    if (output) output.textContent = `狀態：${engine.state.mode || "predict"}；${engine.state.transferPassed ? "遷移已完成" : "正解仍隱藏"}`;
  };
  const renderSource = (source) => {
    observation.replaceChildren();
    for (const [label, value] of [["片段", source.excerpt], ["體裁／功能", source.function], ["適合回答", source.question], ["閱讀限制", source.limit]]) {
      const paragraph = document.createElement("p");
      const strong = document.createElement("strong");
      strong.textContent = `${label}：`;
      paragraph.append(strong, document.createTextNode(value));
      observation.append(paragraph);
    }
  };
  const setStage = (message) => { progress.textContent = message; };

  for (const source of lab.sources) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `查看「${source.label}」`;
    button.dataset.sourceId = source.id;
    button.setAttribute("aria-pressed", "false");
    button.addEventListener("click", () => {
      for (const candidate of sourceGroup.querySelectorAll("button")) candidate.setAttribute("aria-pressed", String(candidate === button));
      renderSource(source);
      engine.dispatch("manipulate", { state: { selectedEvidence: [source.id] } });
      engine.dispatch("observe", { state: { observedFunction: source.function } });
      setStage("第 2/4 階段：已切換資料區塊；比較它能回答的問題與限制");
      feedback.textContent = "區塊切換後，本文和閱讀問題已同步更新。選用相符證據再說明理由。";
      explanationLabel.hidden = false;
      syncOverallStatus();
      persist();
    });
    sourceGroup.append(button);
  }

  predictButton.addEventListener("click", () => {
    const answer = predictionInput.value.trim().toLocaleLowerCase();
    if (!answer) { feedback.textContent = "先寫下你會查哪個區塊，再提交預測。"; return; }
    const accepted = lab.predictionAnswers.some((value) => value.toLocaleLowerCase() === answer);
    if (!accepted) { feedback.textContent = `提示：${lab.predictionHint}`; predictionInput.focus(); return; }
    engine.dispatch("predict", { state: { prediction: answer } });
    predictionInput.readOnly = true;
    predictButton.disabled = true;
    sourceGroup.hidden = false;
    setStage("第 1/4 階段完成：預測已保留，現在操作不同文本區塊");
    feedback.textContent = "預測已記錄；正解仍不會先替你選來源。";
    syncOverallStatus();
    persist();
  });

  explainButton.addEventListener("click", () => {
    if (!engine.state.selectedEvidence?.length) { feedback.textContent = "先選一個區塊並讀取它的證據。"; return; }
    const answer = explanationInput.value.trim();
    if (answer.length < lab.minimumExplanationLength) { feedback.textContent = `請用完整短句說明；至少 ${lab.minimumExplanationLength} 個字，並指出區塊或證據。`; explanationInput.focus(); return; }
    engine.dispatch("explain", { state: { explanation: answer } });
    explanationLabel.hidden = true;
    transferLabel.hidden = false;
    setStage("第 3/4 階段完成：證據理由已記錄，請用新情境遷移");
    feedback.textContent = "理由已記錄。新的收集公告換了主題，請重新選擇能回答任務的區塊。";
    transferInput.focus();
    syncOverallStatus();
    persist();
  });

  transferButton.addEventListener("click", () => {
    const answer = transferInput.value.trim().toLocaleLowerCase();
    const accepted = lab.transfer.answers.some((value) => value.toLocaleLowerCase() === answer);
    if (!accepted) { feedback.textContent = `再依任務找資訊：${lab.transfer.hint}`; transferInput.focus(); return; }
    engine.dispatch("verify", { state: { transferAnswer: answer, transferPassed: true } });
    transferButton.disabled = true;
    setStage("第 4/4 階段完成：已用新情境驗證體裁與證據選擇");
    feedback.textContent = lab.transfer.completionMessage;
    syncOverallStatus();
    persist();
  });

  section.append(heading, context, progress, predictionLabel, predictButton, feedback, sourceGroup, observation, explanationLabel, transferLabel);
  if (engine.state.prediction) {
    predictionInput.value = engine.state.prediction;
    predictionInput.readOnly = true;
    predictButton.disabled = true;
    sourceGroup.hidden = false;
  }
  const selected = lab.sources.find((source) => source.id === engine.state.selectedEvidence?.[0]);
  if (selected) {
    renderSource(selected);
    for (const button of sourceGroup.querySelectorAll("button")) button.setAttribute("aria-pressed", String(button.dataset.sourceId === selected.id));
    explanationLabel.hidden = false;
  }
  if (engine.state.explanation) {
    explanationInput.value = engine.state.explanation;
    explanationLabel.hidden = true;
    transferLabel.hidden = false;
  }
  if (engine.state.transferPassed) {
    transferInput.value = engine.state.transferAnswer;
    transferButton.disabled = true;
    setStage("第 4/4 階段完成：已用新情境驗證體裁與證據選擇");
    feedback.textContent = lab.transfer.completionMessage;
  }
  syncOverallStatus();
  mount.append(section);
}

export function renderComponentBody({ document, spec, block, engine, storage, lesson = null }) {
  const metadata = RENDERER_METADATA[block.component];
  if (!metadata) throw new Error(`unregistered component: ${block.component}`);
  const model = COMPONENT_MODELS[block.component];
  const body = document.createElement("div");
  body.className = "component-visual-body";
  body.dataset.component = block.component;
  body.dataset.visualKind = metadata.kind;
  body.dataset.semanticModel = model.model;
  body.dataset.contentSource = "unit-spec";
  body.setAttribute("role", "group");
  body.setAttribute("aria-label", `${metadata.label}文字化視覺區`);

  const heading = document.createElement("h4");
  heading.textContent = metadata.label;
  body.append(heading);

  const modelHeading = document.createElement("h5");
  modelHeading.textContent = `語意模型：${model.model}`;
  body.append(modelHeading);

  const anchor = document.createElement("p");
  anchor.className = "component-visual-anchor";
  anchor.textContent = `本課觀察錨點：${spec.coreConcepts?.[0] || spec.title || "未提供單元概念"}`;
  body.append(anchor);

  const purpose = document.createElement("p");
  purpose.textContent = block.purpose;
  body.append(purpose);

  if (block.component !== "GenreReadingBlock") {
    const stateList = document.createElement("dl");
    const values = block.initialState?.variableValues || {};
    for (const [key, value] of Object.entries(values)) {
      const term = document.createElement("dt");
      term.textContent = key;
      const description = document.createElement("dd");
      description.textContent = String(value);
      stateList.append(term, description);
    }
    if (!stateList.children.length) {
      const term = document.createElement("dt");
      term.textContent = "初始狀態";
      const description = document.createElement("dd");
      description.textContent = String(block.initialState?.mode || "predict");
      stateList.append(term, description);
    }
    body.append(stateList);
  }

  const promptList = document.createElement("ul");
  promptList.className = "component-visual-prompts";
  const concepts = Array.isArray(spec.coreConcepts) ? spec.coreConcepts.filter(Boolean) : [];
  const goals = Array.isArray(spec.learningGoals) ? spec.learningGoals.filter(Boolean) : [];
  const misconceptions = Array.isArray(spec.misconceptions) ? spec.misconceptions.filter(Boolean) : [];
  const visualizations = Array.isArray(spec.visualizations) ? spec.visualizations.filter(Boolean) : [];
  const unitValues = [
    concepts[0] || spec.title || "本課核心概念",
    visualizations[0] || goals[0] || block.purpose,
    concepts[1] || misconceptions[0] || goals[1] || "本課需檢查的關係",
  ];
  for (const [index, prompt] of model.prompts.entries()) {
    const item = document.createElement("li");
    item.textContent = `${prompt}：${unitValues[index]}`;
    promptList.append(item);
  }
  body.append(promptList);

  const evidenceSection = document.createElement("section");
  evidenceSection.className = "unit-visualization-evidence";
  evidenceSection.setAttribute("aria-label", "本單元操作與證據");
  const evidenceHeading = document.createElement("h5");
  evidenceHeading.textContent = "本單元操作與證據";
  evidenceSection.append(evidenceHeading);
  const evidenceList = document.createElement("ul");
  for (const action of block.studentActions || []) {
    const item = document.createElement("li");
    item.textContent = `操作：${action}`;
    evidenceList.append(item);
  }
  for (const rule of block.visualRules || []) {
    const item = document.createElement("li");
    item.textContent = `規則：${rule}`;
    evidenceList.append(item);
  }
  if (!evidenceList.children.length) {
    const item = document.createElement("li");
    item.textContent = `${model.model} 目前讀取本課的核心概念與學習目標；操作證據待單元資料提供。`;
    evidenceList.append(item);
  }
  evidenceSection.append(evidenceList);
  body.append(evidenceSection);

  if (block.component === "GuidedChoiceBlock" && lesson?.interactive?.steps?.length) {
    const lab = document.createElement("section");
    lab.className = "guided-choice-lab";
    lab.setAttribute("aria-label", lesson.interactive.goal || "引導選擇");
    const intro = document.createElement("p");
    intro.textContent = lesson.interactive.scenario || lesson.interactive.goal || "";
    lab.append(intro);
    lesson.interactive.steps.forEach((step, index) => {
      const fieldset = document.createElement("fieldset");
      const legend = document.createElement("legend");
      legend.textContent = `第 ${index + 1} 題：${step.prompt}`;
      fieldset.append(legend);
      const feedback = document.createElement("p");
      feedback.setAttribute("role", "status");
      feedback.setAttribute("aria-live", "polite");
      let attempts = 0;
      step.options.forEach((option, optionIndex) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = `${String.fromCharCode(65 + optionIndex)}. ${option}`;
        button.addEventListener("click", () => {
          attempts += 1;
          const selected = String.fromCharCode(65 + optionIndex);
          if (selected === step.answer) {
            feedback.textContent = step.feedback;
            for (const candidate of fieldset.querySelectorAll("button")) candidate.disabled = true;
          } else {
            feedback.textContent = `再試一次：${step.retryHint}`;
            button.focus();
          }
        });
        fieldset.append(button);
      });
      fieldset.append(feedback);
      lab.append(fieldset);
    });
    body.append(lab);
  }
  if (block.component === "DataExplorerBlock") renderDataExplorerLab({ document, mount: body, block });
  if (block.component === "GenreReadingBlock") renderGenreReadingLab({ document, mount: body, block, engine, storage });

  const diagnosisSection = document.createElement("section");
  diagnosisSection.className = "unit-misconception-diagnosis";
  diagnosisSection.setAttribute("aria-label", "本單元迷思診斷");
  const diagnosisHeading = document.createElement("h5");
  diagnosisHeading.textContent = "本單元迷思診斷與回饋";
  diagnosisSection.append(diagnosisHeading);
  const diagnosisList = document.createElement("ul");
  for (const check of block.misconceptionChecks || []) {
    const item = document.createElement("li");
    item.textContent = `${check.trigger}｜${check.prompt}｜${check.expectedEvidence}`;
    diagnosisList.append(item);
  }
  if (block.feedback?.incorrect) {
    const item = document.createElement("li");
    item.textContent = `錯答回饋：${block.feedback.incorrect}`;
    diagnosisList.append(item);
  }
  if (!diagnosisList.children.length) {
    const item = document.createElement("li");
    item.textContent = `請回看「${misconceptions[0] || concepts[0] || spec.title || "本單元概念"}」並指出支持判斷的證據。`;
    diagnosisList.append(item);
  }
  diagnosisSection.append(diagnosisList);
  body.append(diagnosisSection);

  const transfer = document.createElement("p");
  transfer.className = "unit-transfer-constraint";
  transfer.textContent = `會考遷移：${spec.capTransfer?.stemConstraint || "換情境後仍須指出核心概念與證據"}；${spec.capTransfer?.requiredResponse || "回答後指出證據或推理步驟"}`;
  body.append(transfer);

  const formulas = (spec.coreConcepts || []).filter((concept) => typeof concept === "string" && concept.includes("＝") && /²|\^2/.test(concept));
  if (formulas.length) {
    const formulaModel = document.createElement("section");
    formulaModel.className = "formula-model";
    formulaModel.dataset.formulaCount = String(formulas.length);
    formulaModel.setAttribute("aria-label", `${metadata.label}公式文字模型`);
    const formulaHeading = document.createElement("h5");
    formulaHeading.textContent = "本課公式模型";
    formulaModel.append(formulaHeading);
    const formulaList = document.createElement("ol");
    for (const formula of formulas) {
      const item = document.createElement("li");
      item.dataset.formula = formula;
      item.textContent = formula;
      formulaList.append(item);
    }
    formulaModel.append(formulaList);
    body.append(formulaModel);
  }

  const note = document.createElement("p");
  note.className = "component-visual-note";
  note.textContent = `此 ${metadata.label} 已從本課 UnitImplementationSpec 讀取核心概念、操作規則、迷思診斷與遷移限制，並提供可測試的文字化替代；圖形數據仍依單元內容審查後接入。`;
  body.append(note);
  return body;
}

import { readFile, writeFile } from "node:fs/promises";

const ROOT = new URL("../", import.meta.url);
const readJson = async rel => JSON.parse(await readFile(new URL(rel, ROOT), "utf8"));
const writeJson = async (rel, value) => writeFile(new URL(rel, ROOT), `${JSON.stringify(value, null, 2)}\n`);
const replaceOnce = (text, before, after, label) => {
  if (!text.includes(before)) throw new Error(`missing patch anchor: ${label}`);
  return text.replace(before, after);
};

const lessonPath = "lessons/math/lesson-math-content-a-7-2.json";
const lesson = await readJson(lessonPath);
if (lesson.id !== "lesson-math-content-a-7-2") throw new Error("unexpected A-7-2 lesson id");

lesson.reviewStatus = "content-reviewed";
lesson.updatedAt = "2026-10-01";
if (lesson.provenance?.authoringNote) {
  lesson.provenance.authoringNote = lesson.provenance.authoringNote.replace(
    /AI／Terra 第二輪審查未完成，維持 draft。?/g,
    "已完成 2026-10-01 內容、題庫與單元邊界審查；來源維持 pattern-only／公開定位用途，不宣稱取得三版本完整正文。",
  );
}
if (lesson.fusionRecord?.llmSynthesisNote) {
  lesson.fusionRecord.llmSynthesisNote = lesson.fusionRecord.llmSynthesisNote.replace(
    /Terra[^。]*維持 draft。?/g,
    "2026-10-01 已完成本課內容與題庫邊界審查；三版本完整正文仍依各來源紀錄維持 pending，不冒充已取得。",
  );
}
const oldSimulation = lesson.simulation || {};
lesson.simulation = {
  ...oldSimulation,
  id: "sim-math-a-7-2-equation-meaning",
  engine: "math-equation-meaning",
  mode: "model",
  model: "a-7-2-equation-meaning-v1",
  goal: "從情境建立一元一次方程式，並用候選值代回原式比較左右兩側；不教授移項或求解程序。",
  mission: "操作候選 x，觀察 4x＋3 與 27 是否相等；再用等號、未知數個數與最高次數說明方程式的結構。",
  equationMeaning: {
    coefficient: 4,
    constant: 3,
    total: 27,
    variable: "x",
    min: 0,
    max: 10,
    step: 1,
    context: "四袋徽章各有 x 枚，另有 3 枚散放，共 27 枚。",
  },
};
await writeJson(lessonPath, lesson);

const patches = {
  1: {
    prompt: "候選值 x＝5 是否為方程式 3x−4＝11 的解？哪個理由完整？",
    options: [
      ["A", "代入後左邊 3×5−4＝11，與右邊 11 相等，所以 x＝5 是解"],
      ["B", "因為 5 是正數，所以一定是解"],
      ["C", "只算 3×5＝15，就可判定是解"],
      ["D", "把 11−4 算成 7，所以 x＝5 不是解"],
    ],
    value: "A",
    explanation: "把候選 x＝5 代回原式：左邊 3×5−4＝11，右邊是 11；左右相等，所以 x＝5 是解。這是在檢驗候選值，不是求解。",
    strategy: "把候選值代回原方程式，分別算出左右兩側；兩側相等才符合『解』的定義。",
    steps: ["保留原式 3x−4＝11。", "代入候選 x＝5。", "左邊算得 3×5−4＝11。", "右邊原值為 11，左右相等。", "因此 x＝5 是解，選 A。"],
  },
  4: {
    prompt: "把候選 y＝4 代入方程式 4y＋7＝23，哪個判斷正確？",
    options: [
      ["A", "左邊是 4＋4＋7＝15，所以不是解"],
      ["B", "左邊 4×4＋7＝23，和右邊 23 相等，所以 y＝4 是解"],
      ["C", "因為 23−7＝16，所以不用代入即可說 y＝4 是解"],
      ["D", "只要 y 是整數就一定是解"],
    ],
    value: "B",
    explanation: "代入 y＝4 後，左邊 4×4＋7＝23，右邊也是 23；等號成立，所以候選 y＝4 是解。",
    strategy: "不做移項；直接把給定候選值放回原式，保留左右兩側並比較。",
    steps: ["保留原式 4y＋7＝23。", "代入候選 y＝4。", "左邊得到 16＋7＝23。", "右邊仍為 23。", "左右相等，因此選 B。"],
  },
  6: {
    prompt: "要檢查 x＝7 是否為 3(x−2)＝15 的解，下列哪個代入證據正確？",
    options: [
      ["A", "3(7−2)＝15，左、右兩側相等"],
      ["B", "3×7−2＝19，所以相等"],
      ["C", "7−2＝5，因此不必比較右側"],
      ["D", "x 是正數，所以一定成立"],
    ],
    value: "A",
    explanation: "代入 x＝7 要保留括號：3(7−2)＝3×5＝15，與右側 15 相等，所以 x＝7 是解。",
    strategy: "依原式結構完整代入候選值，先算括號，再比較原式兩側是否相等。",
    steps: ["保留原式 3(x−2)＝15。", "把 x 換成 7，得 3(7−2)。", "括號先算得 5，再乘 3 得 15。", "右側為 15。", "左右相等，因此選 A。"],
  },
  7: {
    prompt: "候選 x＝4 代入方程式 5x＋2＝2x＋14，哪個比較正確？",
    options: [
      ["A", "左邊 22、右邊 22，所以 x＝4 是解"],
      ["B", "左邊 20、右邊 8，所以 x＝4 不是解"],
      ["C", "只要兩邊都有 x，就不用代入"],
      ["D", "先把 2x 移到左邊才算是在檢驗候選值"],
    ],
    value: "A",
    explanation: "代入 x＝4：左邊 5×4＋2＝22，右邊 2×4＋14＝22；左右相等，因此 x＝4 是解。",
    strategy: "未知數在等號兩側時，將同一候選值同時代入兩側並各自計算，再比較結果。",
    steps: ["保留原式 5x＋2＝2x＋14。", "左右兩側都代入 x＝4。", "左邊算得 22。", "右邊也算得 22。", "左右相等，因此選 A。"],
  },
  8: {
    prompt: "下列哪一個式子是一元一次方程式？",
    options: [["A", "2x＋6＝18"], ["B", "2x＋6"], ["C", "x²＋6＝18"], ["D", "x＋y＝18"]],
    value: "A",
    explanation: "A 有等號、只有一個未知數 x，而且 x 的最高次數是 1；B 缺等號，C 是二次，D 有兩個未知數。",
    strategy: "依序檢查三件事：是否有等號、未知數是否只有一種、未知數最高次數是否為 1。",
    steps: ["先找等號：B 淘汰。", "再數未知數種類：D 有 x、y 兩種。", "再看最高次數：C 有 x²。", "A 同時符合三項條件。", "因此選 A。"],
  },
  9: {
    prompt: "關於 4x＋1＝4x−3，下列哪個敘述最符合『一元一次方程式的意義』？",
    options: [
      ["A", "它有等號、只有未知數 x 且最高次為 1，因此是一元一次方程式；某個數是否為解仍要代入檢查"],
      ["B", "因為左右都有 4x，所以它不是方程式"],
      ["C", "只要未知數在兩側，就一定有很多解"],
      ["D", "沒有先求出 x，就不能判斷它是不是方程式"],
    ],
    value: "A",
    explanation: "是否為一元一次方程式看的是結構：有等號、一種未知數、最高次為 1。『是不是解』是另一個問題，需要把候選值代入原式比較左右。",
    strategy: "把『方程式的分類』與『候選值是否為解』分開判斷，不用求解程序決定方程式的身分。",
    steps: ["確認式子含等號。", "未知數只有 x 一種。", "x 的最高次數是 1。", "因此它符合一元一次方程式的結構。", "候選值是否成立要另行代入檢查，選 A。"],
  },
  10: {
    prompt: "長方形周長為 34 公分，寬為 6 公分，長為 x 公分。哪個方程式忠實表示題意？（本題不要求解 x）",
    options: [["A", "x＋6＝34"], ["B", "2x＋6＝34"], ["C", "x＋12＝34"], ["D", "2(x＋6)＝34"]],
    value: "D",
    explanation: "長方形周長是 2×(長＋寬)，代入長 x、寬 6，得到 2(x＋6)＝34；本題只檢查列式是否對應情境，不求 x。",
    strategy: "先把周長公式中的每個量對回題意，再以未知數 x 取代長；只列等量關係，不進入求解。",
    steps: ["周長公式為 2×(長＋寬)。", "長以 x 公分表示。", "寬為 6 公分。", "總周長為 34 公分。", "所以列 2(x＋6)＝34，選 D。"],
  },
};

for (let i = 1; i <= 10; i += 1) {
  const path = `questions/math/question-math-content-a-7-2-${i}.json`;
  const q = await readJson(path);
  const patch = patches[i];
  if (patch) {
    q.prompt = patch.prompt;
    q.options = patch.options.map(([id, text]) => ({ id, text }));
    q.answer = { value: patch.value, explanation: patch.explanation };
    q.solutionStrategy = patch.strategy;
    q.solutionSteps = patch.steps;
  }
  if (i === 2) {
    q.solutionStrategy = "把已知候選值逐項代入每個方程式的左側，並和原右側比較；左右相等的那一式才成立。";
  }
  if (i === 3) {
    q.solutionStrategy = "先說清楚等號代表兩側同值，再排除把等號誤讀成計算指令或未知數條件的選項。";
    q.solutionSteps = ["辨認等號左右各是一個數量表示。", "等號表示兩側的值相同。", "等號本身不規定 x 的正負。", "本題不需要做移項或求解。", "因此選 C。"];
  }
  if (i === 5) {
    q.solutionStrategy = "先定義未知量，再按照『原有－送出＝剩下』把故事中的三個量放進等式。";
  }
  q.reviewStatus = "content-reviewed";
  q.updatedAt = "2026-10-01";
  if (q.provenance?.authoringNote) {
    q.provenance.authoringNote = q.provenance.authoringNote.replace(
      /AI／Terra 第二輪審查未完成，維持 draft。?/g,
      "已完成 2026-10-01 內容、答案、解析與 A-7-2 單元邊界審查；公開試題僅作 pattern-only 能力模式參考。",
    );
  }
  await writeJson(path, q);
}

// Add a production interaction that tests equation meaning without teaching solving.
let simulations = await readFile(new URL("site/simulations.js", ROOT), "utf8");
simulations = replaceOnce(
  simulations,
  '"math-ticket-equation": {},\n    "math-expression-lab": { x: 2 },',
  '"math-ticket-equation": {},\n    "math-equation-meaning": { x: 5 },\n    "math-expression-lab": { x: 2 },',
  "math-equation-meaning default",
);
simulations = replaceOnce(
  simulations,
  '"math-number-line": "數線操作臺", "math-inequality-range": "不等式範圍數線", "math-algebra-balance": "代數天平", "math-ticket-equation": "票券等量模型", "math-function-graph": "函數圖形實驗室",',
  '"math-number-line": "數線操作臺", "math-inequality-range": "不等式範圍數線", "math-algebra-balance": "代數天平", "math-ticket-equation": "票券等量模型", "math-equation-meaning": "方程式意義檢驗臺", "math-function-graph": "函數圖形實驗室",',
  "math-equation-meaning label",
);
const equationMeaningBranch = `    if (engine === "math-equation-meaning") {\n      const config = lesson.simulation.equationMeaning;\n      const x = Number(state.x);\n      const left = Number(config.coefficient) * x + Number(config.constant);\n      const right = Number(config.total);\n      const equal = left === right;\n      return \`\${designed}<section class="sim-equation-meaning" aria-label="一元一次方程式意義互動"><h5>候選值代回原式</h5><p>\${esc(config.context)}</p><p class="sim-ticket-equation-formula" aria-live="polite">\${config.coefficient} × \${esc(config.variable)} + \${config.constant} = \${config.total}</p><div class="balance" aria-label="等號兩側數值比較"><span class="balance-pan">左側 \${left}</span><span aria-hidden="true">\${equal ? "＝" : "≠"}</span><span class="balance-pan">右側 \${right}</span></div>\${slider("x", \`候選 \${config.variable} 的值\`, x, config.min, config.max, config.step)}<p class="sim-ticket-feedback" role="status" aria-live="polite">\${equal ? \`代入 \${config.variable}=\${x} 後左右相等，因此這個候選值是解。\` : \`代入 \${config.variable}=\${x} 後左側為 \${left}、右側為 \${right}，左右不相等，因此這個候選值不是解。\`}</p><p>本互動只檢驗候選值是否符合原等式，不展示移項、同除或其他求解程序。</p></section>\`;\n    }\n`;
simulations = replaceOnce(simulations, '    if (engine === "math-ticket-equation") {', `${equationMeaningBranch}    if (engine === "math-ticket-equation") {`, "math-equation-meaning renderer");
await writeFile(new URL("site/simulations.js", ROOT), simulations);

let contracts = await readFile(new URL("scripts/simulation_contracts.py", ROOT), "utf8");
contracts = replaceOnce(contracts, '    "math-ticket-equation",\n    "math-expression-lab",', '    "math-ticket-equation",\n    "math-equation-meaning",\n    "math-expression-lab",', "contract engine registration");
const equationValidator = `\n\ndef _equation_meaning_errors(simulation: dict[str, Any]) -> list[str]:\n    config = simulation.get("equationMeaning")\n    if not isinstance(config, dict):\n        return ["math-equation-meaning requires equationMeaning config"]\n    errors: list[str] = []\n    for key in ("variable", "context"):\n        if not _nonempty_text(config.get(key)):\n            errors.append(f"equationMeaning.{key} must be non-empty text")\n    for key in ("coefficient", "constant", "total", "min", "max", "step"):\n        if not isinstance(config.get(key), (int, float)):\n            errors.append(f"equationMeaning.{key} must be numeric")\n    lo, hi, step = config.get("min"), config.get("max"), config.get("step")\n    if all(isinstance(value, (int, float)) for value in (lo, hi, step)) and (hi <= lo or step <= 0):\n        errors.append("equationMeaning must satisfy max > min and step > 0")\n    return errors\n`;
contracts = replaceOnce(contracts, '\n\ndef contract_errors(lesson: dict[str, Any]) -> list[str]:', `${equationValidator}\n\ndef contract_errors(lesson: dict[str, Any]) -> list[str]:`, "equation meaning validator");
contracts = replaceOnce(contracts, '    if engine == "math-ticket-equation":\n        errors.extend(_ticket_equation_errors(simulation))', '    if engine == "math-ticket-equation":\n        errors.extend(_ticket_equation_errors(simulation))\n    if engine == "math-equation-meaning":\n        errors.extend(_equation_meaning_errors(simulation))', "equation meaning validation dispatch");
await writeFile(new URL("scripts/simulation_contracts.py", ROOT), contracts);

let audit = await readFile(new URL("scripts/audit_math_coverage.mjs", ROOT), "utf8");
audit = replaceOnce(audit, '  "math-ticket-equation",\n  "math-expression-lab",', '  "math-ticket-equation",\n  "math-equation-meaning",\n  "math-expression-lab",', "audit production engine registration");
await writeFile(new URL("scripts/audit_math_coverage.mjs", ROOT), audit);

console.log("finalized A-7-2 lesson, 10 questions, and math-equation-meaning production engine");

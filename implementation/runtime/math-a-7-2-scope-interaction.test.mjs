import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { JSDOM } from "jsdom";

const lesson = JSON.parse(await readFile(new URL("../../lessons/math/lesson-math-content-a-7-2.json", import.meta.url), "utf8"));
const specText = await readFile(new URL("../unit-specs/math/cur-math-content-a-7-2.yaml", import.meta.url), "utf8");
const componentRegistry = JSON.parse(await readFile(new URL("../component-registry.json", import.meta.url), "utf8"));
const simulationSource = await readFile(new URL("../../site/simulations.js", import.meta.url), "utf8");

assert.equal(lesson.reviewStatus, "content-reviewed");
const visibleSections = lesson.content.sections;
assert.equal(visibleSections.length, 6, "the learner-visible lesson must retain its unit-specific six-part instruction");
assert.match(visibleSections[0].body, /徽章.*4x＋3＝27.*等號兩側/);
assert.match(visibleSections[1].body, /3x＋2＝11.*x＝2.*8 不等於 11.*x＝3.*11/);
assert.match(visibleSections[1].body, /不能只因測過幾個數，就斷言它是唯一解.*唯一性需要額外理由/s, "candidate substitution must not be presented as a proof of uniqueness");
assert.match(visibleSections[2].body, /5m－2＝18.*m²＋1＝10.*a＋b＝9/);
assert.match(visibleSections[3].heading, /收據分類台/);
assert.match(visibleSections[3].body, /6p＋8＝50.*6＋p＋8＝50/);
assert.match(visibleSections[4].body, /五箱.*5n＋7＝42.*不進行求解/);
assert.match(visibleSections[5].body, /代入左側得 3×5＋4＝19.*4c＋2＝30.*求解留待 A-7-3/);
assert.match(lesson.fusionRecord.versionDifferences[0], /唯一.*直接讀到.*候選值左右檢驗/);
assert.match(lesson.fusionRecord.originalAdditions.join(" "), /徽章清點、帳單與捐書/);
assert.match(lesson.fusionRecord.originalAdditions.join(" "), /原式保持不變、逐項代入、分別計算左右/);
assert.match(lesson.content.summary, /求解程序屬後續 A-7-3/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /此決策落在六段原創可見課文與四階互動/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /翰林標示課本OCR.*南一類平台.*康軒官方索引/s);
assert.match(lesson.fusionRecord.llmSynthesisNote, /不把『驗證給定候選值』誤當『有效找出未知解』/);
assert.match(lesson.fusionRecord.llmSynthesisNote, /publisher slots維持pending/);
assert.match(lesson.versionResearch.find((entry) => entry.edition.includes("補救GO學用" )).sourceLocator, /頁81–82.*P168–169/);
assert.match(lesson.versionResearch.find((entry) => entry.edition.includes("補救GO學用" )).findings.representations[0], /候選值.*左式.*右式.*並列表檢驗/);
const hanlinTextbook = lesson.versionResearch.find((entry) => entry.edition.includes("翰林國中數學七上課本"));
assert.ok(hanlinTextbook, "A-7-2 fusion must retain its page-located textbook-body evidence");
assert.match(hanlinTextbook.sourceLocator, /頁168–170.*等量公理/);
assert.match(hanlinTextbook.findings.concepts.join(" "), /文字關係列方程式.*左右相等.*等量公理/);
assert.match(hanlinTextbook.licenseBoundary, /All Rights Reserved.*授權未核實/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /翰林.*南一.*類南一版.*康軒.*金山國中.*第17–18週/);
assert.match(lesson.fusionRecord.versionDifferences.join(" "), /微課.*第17–18週.*未標出版社.*不補南一或康軒版本證據/);
assert.match(lesson.fusionRecord.originalAdditions.join(" "), /量義先行.*形式條件檢查.*證據鏈.*同儕討論/);
const naniCourseSequence = lesson.versionResearch.find((entry) => entry.edition.includes("南一七上3-2課程資源序列"));
assert.ok(naniCourseSequence, "the Nani-aligned lesson sequence must be source-located and distinguished from publisher text");
assert.match(naniCourseSequence.findings.concepts.join(" "), /列.*解的意義.*候選值檢驗.*等量公理/);
assert.match(naniCourseSequence.licenseBoundary, /非南一出版社正文.*publisher slot維持pending/);
const naniExcerpt = lesson.versionResearch.find((entry) => entry.edition.includes("公開刊物"));
assert.ok(naniExcerpt, "the partially readable Nani textbook extract must be recorded with its limits");
assert.match(naniExcerpt.findings.concepts.join(" "), /P\.183–184/);
assert.match(naniExcerpt.findings.concepts.join(" "), /天平/);
assert.match(naniExcerpt.findings.concepts.join(" "), /A-7-3/);
assert.match(naniExcerpt.licenseBoundary, /P\.183–184局部.*publisher slot維持pending/);
const kanghsuanOfficialIndex = lesson.versionResearch.find((entry) => entry.edition.includes("康軒官方國中數學影音高手"));
assert.ok(kanghsuanOfficialIndex, "the Kanghsuan official concept index must be recorded separately from school plans");
assert.match(kanghsuanOfficialIndex.findings.concepts.join(" "), /方程式的形式認識、解的意義、等量公理、移項法則/);
assert.match(kanghsuanOfficialIndex.licenseBoundary, /未播放或複製影音/);
const hanlinPublisherMatrix = lesson.versionResearch.find((entry) => entry.edition.includes("翰林官方111國中數學教材簡介本"));
assert.ok(hanlinPublisherMatrix, "the official three-publisher structure comparison must be recorded");
assert.match(hanlinPublisherMatrix.findings.concepts.join(" "), /翰林10、康軒9、南一9/);
assert.match(hanlinPublisherMatrix.licenseBoundary, /不替代三版本正文逐一研究/);
const kanghsuanPlan = lesson.versionResearch.find((entry) => entry.edition.includes("金山國中113學年度康軒版"));
assert.ok(kanghsuanPlan, "the specific Kanghsuan-aligned school-week boundary must be source-located");
assert.match(kanghsuanPlan.findings.concepts.join(" "), /第17週.*第18週.*A-7-3/);
assert.match(kanghsuanPlan.licenseBoundary, /不等於康軒課本正文.*pending/);
const guangfuKanghsuanPlan = lesson.publisherResearch.find((entry) => entry.edition.includes("光復中學107學年度康軒版"));
assert.ok(guangfuKanghsuanPlan, "A-7-2 must include the newly read Kanghsuan-aligned school-plan evidence");
assert.match(guangfuKanghsuanPlan.outcome, /代入法或枚舉法.*下一週3-3.*等量公理/);
assert.match(guangfuKanghsuanPlan.copyrightBoundary, /不是可歸屬的康軒正文.*pending/);
assert.match(lesson.versionResearch.find((entry) => entry.edition.includes("翰林國中數學七上課本")).findings.concepts.join(" "), /文字關係列方程式.*候選值比較左右式/);
assert.equal(lesson.reviewStatus, "content-reviewed", "content review may pass while unavailable publisher full bodies remain explicitly pending");
assert.match(lesson.teaching.body[0].body, /工作台實際以選項作答.*不是拖曳卡片/);
assert.doesNotMatch(lesson.teaching.summary.join(" "), /移項|同步做相反運算|天平/);
assert.doesNotMatch(lesson.teaching.exitCheck.map((item) => `${item.prompt} ${item.expectedEvidence}`).join(" "), /兩側同步|同除|移項/);
assert.equal(lesson.interactive.steps.length, 4);
assert.deepEqual(lesson.interactive.variables, [
  { symbol: "x", meaning: "每袋徽章的枚數（枚）" },
  { symbol: "bag-count", meaning: "裝有相同數量徽章的袋數（袋）" },
  { symbol: "loose-count", meaning: "袋外散放的徽章枚數（枚）" },
  { symbol: "total-count", meaning: "清點到的徽章總枚數（枚）" },
], "interactive variable meanings must match the badge-count scenario, not stale price/weight fields");
assert.match(lesson.teaching.body.find((item) => item.id === "explain").body, /驗證方法.*有效找到解|檢查某個數是不是解.*如何有效找到解/);
assert.match(lesson.interactive.steps[0].options[0], /4x＋3＝27/);
assert.match(lesson.interactive.steps[2].options[0], /4×6＋3＝27/);
assert.match(lesson.interactive.steps[3].options[0], /6s＋5＝47/);
assert.equal(lesson.simulation.engine, "math-equation-meaning", "A-7-2 must use its dedicated equation-meaning production renderer");
assert.equal(lesson.simulation.model, "a-7-2-equation-meaning-v1");
assert.ok(lesson.simulation.equationMeaning);
assert.equal(lesson.simulation.learningDesign.steps.length, 4);
assert.match(lesson.simulation.learningDesign.steps[0].equation, /4x＋3＝27/);
assert.match(lesson.simulation.learningDesign.steps[1].equation, /一種未知數.*最高次為一次/);
assert.match(lesson.simulation.learningDesign.steps[2].equation, /4×5＋3＝23.*27/);
assert.match(lesson.simulation.learningDesign.steps[3].equation, /4×6＋3＝27.*27＝27/);
assert.doesNotMatch(JSON.stringify(lesson.simulation.learningDesign), /2x＋5＝13|x＝4/);
assert.ok(lesson.simulation.sourceRefs.includes(hanlinTextbook.sourceLocator.split("；")[0]));
assert.ok(lesson.simulation.sourceRefs.includes("https://www.junyiacademy.org/topics/n-m7a-c03-2"));
assert.ok(lesson.simulation.sourceRefs.some((ref) => ref.includes("openclass.chc.edu.tw")));
assert.ok(lesson.simulation.sourceRefs.some((ref) => ref.includes("www.cshs.ntpc.edu.tw") && ref.includes("Action=downloadfile")));
assert.ok(lesson.simulation.sourceRefs.includes("https://www.kfsh.hc.edu.tw/uploads/article/1707/20180829160826.pdf"));
assert.ok(lesson.studyReferences.includes("https://teric.naer.edu.tw/wSite/DoDownload?fileName=1572591481033&format=pdf&xmlId=2046954"), "the public grade-7 instructional design must be traceable");
assert.match(lesson.fusionRecord.originalAdditions.join(" "), /解的意義／唯一解.*代入判別候選解.*不等於已證明唯一性/);
assert.doesNotMatch(specText, /兩側同時拿掉|逐步解出|移項變號|兩側同步運算後/);
assert.match(specText, /求解留至 A-7-3/);
assert.match(specText, /不呈現天平或平衡狀態/);
assert.ok(componentRegistry.components.AlgebraEquationMeaningBlock.contextModeling);
assert.ok(componentRegistry.components.AlgebraEquationMeaningBlock.candidateSubstitution);

const dom = new JSDOM("<!doctype html><html><body><main id='root'></main></body></html>", {
  url: "https://example.test/",
  runScripts: "outside-only",
});
dom.window.eval(simulationSource);
const root = dom.window.document.querySelector("#root");
root.innerHTML = dom.window.LearningSimulations.render(lesson, "a7-2-scope-test");
assert.equal(root.querySelectorAll("[data-design-step]").length, 4);
assert.match(root.textContent, /4x＋3＝27/);
root.querySelector('[data-design-step="2"]').click();
assert.match(root.querySelector(".sim-equation-current").textContent, /左側 4×5＋3＝23.*右側 27/);
root.querySelector('[data-design-step="1"]').click();
assert.match(root.querySelector(".sim-equation-current").textContent, /一種未知數 x；最高次為一次/);
assert.match(root.textContent, /候選值/);

console.log("A-7-2 scope boundary, equation modeling, candidate checking and simulation stages: ok");

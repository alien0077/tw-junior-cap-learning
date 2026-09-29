(function () {
const esc = value => String(value ?? "").replace(/[&<>"']/g, char => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));

function renderQuestionDetail(item) {
  const options = (item.options || []).map(option => `<li class="question-option${option.id === item.answer?.value ? " is-answer" : ""}"><span>${esc(option.id)}.</span> ${esc(option.text)}</li>`).join("");
  const answer = item.answer?.value
    ? `<p class="answer-line"><b>答案：${esc(item.answer.value)}</b></p><p class="answer-explanation">${esc(item.answer.explanation || "")}</p>`
    : `<p class="answer-explanation">此題尚未提供答案。</p>`;
  const solution = item.solutionStrategy || item.solutionSteps?.length
    ? `<details class="solution-detail"><summary>查看解題技巧與詳細步驟</summary>${item.solutionStrategy ? `<section class="solution-strategy"><h4>解題技巧</h4><p>${esc(item.solutionStrategy)}</p></section>` : ""}${item.solutionSteps?.length ? `<section class="solution-steps"><h4>逐步解題</h4><ol>${item.solutionSteps.map(step => `<li>${esc(step)}</li>`).join("")}</ol></section>` : ""}</details>`
    : `<p class="solution-unavailable">本題尚未提供解題技巧與步驟。</p>`;
  return `<section class="question-detail" aria-label="選項、答案、解析與解題步驟"><ol class="question-options">${options}</ol>${answer}${solution}</section>`;
}
window.renderQuestionDetail = renderQuestionDetail;
})();

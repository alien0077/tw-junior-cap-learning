import { renderInteractiveBlock } from "./dom-renderer.js?v=20260908-state-persistence-hash";

export const REQUIRED_STUDENT_SECTIONS = Object.freeze([
  ["先問你", "learningGoals"],
  ["這是重點", "coreConcepts"],
  ["為什麼", "contentFlow"],
  ["容易錯在哪裡", "misconceptions"],
  ["自己檢查", "exitTicket"],
  ["考試怎麼變形", "capTransfer"],
]);

function appendList(document, parent, values) {
  const list = document.createElement("ul");
  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = typeof value === "string" ? value : JSON.stringify(value);
    list.append(item);
  }
  parent.append(list);
}

export function renderStudentLesson({ document, mount, spec }) {
  const article = document.createElement("article");
  article.className = "student-lesson-shell";
  article.dataset.lessonId = spec.lessonId;
  const title = document.createElement("h2");
  title.textContent = spec.title;
  article.append(title);
  const status = document.createElement("p");
  status.className = "lesson-status";
  status.textContent = `實作狀態：${spec.status.implementationStatus}；QA：${spec.status.qaStatus}`;
  article.append(status);
  for (const [label, key] of REQUIRED_STUDENT_SECTIONS) {
    const section = document.createElement("section");
    section.dataset.section = label;
    const heading = document.createElement("h3");
    heading.textContent = label;
    section.append(heading);
    const value = spec[key];
    if (Array.isArray(value)) appendList(document, section, value);
    else appendList(document, section, Object.entries(value || {}).map(([k, v]) => `${k}: ${typeof v === "string" ? v : JSON.stringify(v)}`));
    article.append(section);
  }
  const interactive = document.createElement("div");
  interactive.className = "lesson-interactive-area";
  spec.interactiveBlocks.forEach((_, blockIndex) => {
    renderInteractiveBlock({ document, mount: interactive, spec, blockIndex });
  });
  article.append(interactive);
  const extension = document.createElement("section");
  extension.dataset.section = "表達延伸";
  const extensionHeading = document.createElement("h3");
  extensionHeading.textContent = "表達延伸";
  extension.append(extensionHeading);
  const extensionText = document.createElement("p");
  extensionText.textContent = spec.expressionExtension.task;
  extension.append(extensionText);
  article.append(extension);
  mount.replaceChildren(article);
  return article;
}

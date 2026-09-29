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

function renderAuthoredLessonContent(document, article, lesson) {
  if (!lesson) return;
  const authored = document.createElement("section");
  authored.dataset.section = "融合教學正文";
  authored.className = "authored-lesson-content";
  const heading = document.createElement("h3");
  heading.textContent = "融合教學正文";
  authored.append(heading);

  const teachingBody = Array.isArray(lesson.teaching?.body) ? lesson.teaching.body : [];
  const contentSections = Array.isArray(lesson.content?.sections) ? lesson.content.sections : [];
  const sections = teachingBody.length ? teachingBody : contentSections;
  for (const entry of sections) {
    const section = document.createElement("section");
    const sectionHeading = document.createElement("h4");
    sectionHeading.textContent = entry.heading || entry.phase || "教學內容";
    const body = document.createElement("p");
    body.textContent = entry.body || "";
    section.append(sectionHeading, body);
    authored.append(section);
  }

  if (!sections.length) {
    const missing = document.createElement("p");
    missing.textContent = "本課尚無可顯示的融合教學正文。";
    authored.append(missing);
  }
  article.append(authored);
}

export function renderStudentLesson({ document, mount, spec, lesson = null }) {
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
  renderAuthoredLessonContent(document, article, lesson);
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
    renderInteractiveBlock({ document, mount: interactive, spec, blockIndex, lesson });
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

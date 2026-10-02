/* Mount Phase-2 semantic family DOM renderers after LearningSimulations inserts HTML. */
(() => {
  const mounted = new WeakSet();
  const enhance = root => {
    if (!(root instanceof Element) || mounted.has(root)) return;
    const model = root.dataset.simulationModel;
    const renderer = window.MathSemanticFamilies?.[model];
    const body = root.querySelector(".simulation-body");
    if (!renderer || !body) return;
    const host = document.createElement("div");
    host.className = "math-semantic-family-host";
    host.dataset.semanticModel = model;
    body.prepend(host);
    renderer(host, { model });
    mounted.add(root);
  };
  const scan = node => {
    if (!(node instanceof Element)) return;
    if (node.matches("[data-simulation-model]")) enhance(node);
    node.querySelectorAll?.("[data-simulation-model]").forEach(enhance);
  };
  const observer = new MutationObserver(records => {
    for (const record of records) for (const node of record.addedNodes) scan(node);
  });
  const start = () => {
    document.querySelectorAll("[data-simulation-model]").forEach(enhance);
    observer.observe(document.documentElement, { childList: true, subtree: true });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start, { once: true });
  else start();
})();
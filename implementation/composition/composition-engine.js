const PHASES = Object.freeze(["student-draft", "one-problem", "first-hint", "student-revision", "re-diagnose"]);

export class CompositionAttempt {
  constructor() {
    this.phase = "student-draft";
    this.draft = "";
    this.problem = null;
    this.hint = null;
    this.revision = "";
  }

  submitDraft(text) {
    if (this.phase !== "student-draft") throw new Error("draft already submitted");
    if (!String(text).trim()) throw new Error("student draft is required");
    this.draft = String(text);
    this.phase = "one-problem";
    return this.snapshot();
  }

  diagnose(problem) {
    if (this.phase !== "one-problem") throw new Error("diagnosis is out of order");
    this.problem = String(problem);
    this.phase = "first-hint";
    return this.snapshot();
  }

  provideHint(hint) {
    if (this.phase !== "first-hint") throw new Error("hint is out of order");
    this.hint = String(hint);
    this.phase = "student-revision";
    return this.snapshot();
  }

  submitRevision(text) {
    if (this.phase !== "student-revision") throw new Error("revision is out of order");
    if (!String(text).trim()) throw new Error("student revision is required");
    this.revision = String(text);
    this.phase = "re-diagnose";
    return this.snapshot();
  }

  snapshot() { return { phase: this.phase, draft: this.draft, problem: this.problem, hint: this.hint, revision: this.revision }; }
  serialize() { return JSON.stringify(this.snapshot()); }

  restore(serialized) {
    const value = typeof serialized === "string" ? JSON.parse(serialized) : serialized;
    if (!value || typeof value !== "object" || !PHASES.includes(value.phase)) throw new TypeError("invalid composition state");
    for (const key of ["draft", "problem", "hint", "revision"]) {
      if (value[key] !== null && typeof value[key] !== "string") throw new TypeError(`invalid composition ${key}`);
    }
    this.phase = value.phase;
    this.draft = value.draft || "";
    this.problem = value.problem;
    this.hint = value.hint;
    this.revision = value.revision || "";
    return this.snapshot();
  }
}

export { PHASES };

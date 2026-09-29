/**
 * Small framework-neutral contract engine for the guide's interactive blocks.
 * Renderers can attach to this state without owning lesson data or answers.
 */
export class InteractiveState {
  constructor(initialState = {}) {
    this.state = structuredClone(initialState);
    this.state.mode ||= "predict";
    this.events = [];
    this.reducedMotion = false;
  }

  dispatch(type, payload = {}) {
    const event = { type, payload: structuredClone(payload), at: Date.now(), accepted: true };
    const mode = this.state.mode;
    const allowed = {
      predict: ["predict"],
      "predict-submitted": ["manipulate"],
      manipulate: ["manipulate", "observe"],
      observe: ["manipulate", "observe", "explain"],
      explain: ["manipulate", "observe", "explain", "verify"],
      verified: ["manipulate", "observe", "explain", "verify"],
    };
    if (type !== "reveal" && !(allowed[mode] || []).includes(type)) {
      event.accepted = false;
      event.reason = `必須先完成 ${mode} 階段，才能執行 ${type}`;
      this.state.lastError = event.reason;
      this.events.push(event);
      return this.snapshot();
    }
    this.events.push(event);
    if (type === "predict") this.state.mode = "predict-submitted";
    if (type === "manipulate") this.state.mode = "manipulate";
    if (type === "observe") this.state.mode = "observe";
    if (type === "explain") this.state.mode = "explain";
    if (type === "verify") this.state.mode = "verified";
    if (type === "reveal") this.state.showAnswer = true;
    delete this.state.lastError;
    Object.assign(this.state, payload.state || {});
    return this.snapshot();
  }

  setReducedMotion(enabled = true) {
    this.reducedMotion = Boolean(enabled);
    return this.reducedMotion;
  }

  snapshot() {
    return { state: structuredClone(this.state), events: structuredClone(this.events) };
  }

  serialize() { return JSON.stringify(this.snapshot()); }

  restore(serialized) {
    const value = typeof serialized === "string" ? JSON.parse(serialized) : serialized;
    if (!value || typeof value !== "object" || !value.state || !Array.isArray(value.events)) throw new TypeError("invalid interactive state");
    this.state = structuredClone(value.state);
    this.events = structuredClone(value.events);
    return this.snapshot();
  }
}

export function createRendererContract(component, spec) {
  return {
    component,
    lessonId: spec.lessonId,
    capabilities: ["predict", "manipulate", "observe", "explain", "verify", "keyboard", "fallback", "reduced-motion"],
    state: new InteractiveState(spec.interactiveBlocks[0].initialState),
    textFallback: spec.interactiveBlocks[0].purpose,
  };
}

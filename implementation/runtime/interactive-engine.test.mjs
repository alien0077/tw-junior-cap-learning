import assert from "node:assert/strict";
import { InteractiveState } from "./interactive-engine.js";

const engine = new InteractiveState({ mode: "predict", showAnswer: false, selectedEvidence: [] });
engine.dispatch("predict", { state: { prediction: "A" } });
engine.dispatch("manipulate", { state: { selectedEvidence: ["e1"] } });
assert.equal(engine.dispatch("verify").events.at(-1).accepted, false);
engine.dispatch("observe", { state: { observationRecorded: true } });
engine.dispatch("explain", { state: { explanation: "因為證據支持 A" } });
engine.dispatch("verify", { state: { feedbackVisible: true } });
const saved = engine.serialize();
const restored = new InteractiveState();
restored.restore(saved);
assert.deepEqual(restored.state.selectedEvidence, ["e1"]);
assert.equal(restored.events.length, 6);
assert.equal(restored.state.mode, "verified");
console.log("interactive engine contract: ok");

import assert from "node:assert/strict";
import { CompositionAttempt, PHASES } from "./composition-engine.js";

const attempt = new CompositionAttempt();
assert.deepEqual(PHASES, ["student-draft", "one-problem", "first-hint", "student-revision", "re-diagnose"]);
assert.throws(() => attempt.submitDraft(""), /draft is required/);
attempt.submitDraft("學生自己的草稿");
attempt.diagnose("證據不足");
attempt.provideHint("找一個具體細節支持主張");
attempt.submitRevision("學生修改後的版本");
assert.equal(attempt.phase, "re-diagnose");
assert.equal(attempt.snapshot().draft, "學生自己的草稿");
assert.equal(attempt.snapshot().revision, "學生修改後的版本");
const restored = new CompositionAttempt();
restored.restore(attempt.serialize());
assert.deepEqual(restored.snapshot(), attempt.snapshot());
assert.throws(() => restored.restore('{"phase":"complete"}'), /invalid composition state/);
console.log("composition attempt contract: ok");

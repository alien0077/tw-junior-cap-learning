#!/usr/bin/env python3
"""Shared validation helpers for production math/science simulation contracts.

The repository contains both generated baseline contracts and hand-authored,
more substantive contracts. Validation therefore checks runtime invariants
rather than requiring byte-for-byte equality with the baseline generator.
"""
from __future__ import annotations

from typing import Any

MATH_ENGINES = {
    "concept-explorer",
    "math-number-line",
    "math-inequality-range",
    "math-algebra-balance",
    "math-visual-area",
    "math-factor-model",
    "math-ticket-equation",
    "math-equation-meaning",
    "math-reasoning-lab",
    "math-expression-lab",
    "math-function-graph",
    "math-system-graph",
    "math-geometry",
    "math-data-lab",
    "math-probability-lab",
}

SCIENCE_ENGINES = {
    "concept-explorer",
    "science-motion-lab",
    "science-energy-lab",
    "science-particle-lab",
    "science-life-system",
    "science-earth-space",
}


def _nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _public_url(value: Any) -> bool:
    return isinstance(value, str) and value.startswith(("https://", "http://"))


def _learning_design_errors(design: Any) -> list[str]:
    if design is None:
        return []
    if not isinstance(design, dict):
        return ["learningDesign must be an object"]
    errors: list[str] = []
    for key in ("type", "objective", "predictionPrompt", "evidencePrompt"):
        if not _nonempty_text(design.get(key)):
            errors.append(f"learningDesign.{key} must be non-empty text")
    steps = design.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append("learningDesign.steps must be a non-empty list")
        return errors
    seen_ids: set[str] = set()
    for index, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            errors.append(f"learningDesign.steps[{index}] must be an object")
            continue
        for key in ("id", "action", "equation", "reason", "feedback"):
            if not _nonempty_text(step.get(key)):
                errors.append(f"learningDesign.steps[{index}].{key} must be non-empty text")
        step_id = step.get("id")
        if _nonempty_text(step_id):
            if step_id in seen_ids:
                errors.append(f"learningDesign step id is duplicated: {step_id}")
            seen_ids.add(step_id)
    return errors


def _ticket_equation_errors(simulation: dict[str, Any]) -> list[str]:
    config = simulation.get("ticketEquation")
    if not isinstance(config, dict):
        return ["math-ticket-equation requires ticketEquation config"]
    errors: list[str] = []
    for key in ("itemLabel", "priceLabel", "currencyLabel"):
        if not _nonempty_text(config.get(key)):
            errors.append(f"ticketEquation.{key} must be non-empty text")
    state = config.get("initialState")
    controls = config.get("controls")
    required_controls = ("ticketCount", "oneTimeFee", "totalPaid", "candidatePrice")
    if not isinstance(state, dict):
        errors.append("ticketEquation.initialState must be an object")
    if not isinstance(controls, dict):
        errors.append("ticketEquation.controls must be an object")
        return errors
    for key in required_controls:
        if not isinstance(state, dict) or not isinstance(state.get(key), (int, float)):
            errors.append(f"ticketEquation.initialState.{key} must be numeric")
        control = controls.get(key)
        if not isinstance(control, dict):
            errors.append(f"ticketEquation.controls.{key} must be an object")
            continue
        if not _nonempty_text(control.get("label")):
            errors.append(f"ticketEquation.controls.{key}.label must be non-empty text")
        lo, hi, step = control.get("min"), control.get("max"), control.get("step")
        if not all(isinstance(value, (int, float)) for value in (lo, hi, step)):
            errors.append(f"ticketEquation.controls.{key} min/max/step must be numeric")
        elif hi <= lo or step <= 0:
            errors.append(f"ticketEquation.controls.{key} must satisfy max > min and step > 0")
    return errors


def _equation_meaning_errors(simulation: dict[str, Any]) -> list[str]:
    config = simulation.get("equationMeaning")
    if not isinstance(config, dict):
        return ["math-equation-meaning requires equationMeaning config"]
    errors: list[str] = []
    for key in ("variable", "context"):
        if not _nonempty_text(config.get(key)):
            errors.append(f"equationMeaning.{key} must be non-empty text")
    for key in ("coefficient", "constant", "total", "min", "max", "step"):
        if not isinstance(config.get(key), (int, float)):
            errors.append(f"equationMeaning.{key} must be numeric")
    lo, hi, step = config.get("min"), config.get("max"), config.get("step")
    if all(isinstance(value, (int, float)) for value in (lo, hi, step)) and (hi <= lo or step <= 0):
        errors.append("equationMeaning must satisfy max > min and step > 0")
    return errors


def _reasoning_lab_errors(lesson: dict[str, Any]) -> list[str]:
    """Validate the lesson-level steps consumed by the reasoning-lab renderer."""
    interactive = lesson.get("interactive")
    if not isinstance(interactive, dict):
        return ["math-reasoning-lab requires lesson.interactive config"]
    steps = interactive.get("steps")
    if not isinstance(steps, list) or not steps:
        return ["math-reasoning-lab requires a non-empty lesson.interactive.steps list"]
    errors: list[str] = []
    for index, step in enumerate(steps, start=1):
        if not isinstance(step, dict):
            errors.append(f"interactive.steps[{index}] must be an object")
            continue
        for key in ("prompt", "answer", "feedback"):
            if not _nonempty_text(step.get(key)):
                errors.append(f"interactive.steps[{index}].{key} must be non-empty text")
        options = step.get("options")
        if not isinstance(options, list) or len(options) < 2 or not all(_nonempty_text(option) for option in options):
            errors.append(f"interactive.steps[{index}].options must contain at least two non-empty choices")
            continue
        answer = step.get("answer")
        valid_answers = {chr(ord("A") + offset) for offset in range(len(options))}
        if _nonempty_text(answer) and answer not in valid_answers:
            errors.append(f"interactive.steps[{index}].answer must identify one of {sorted(valid_answers)}")
    return errors


def contract_errors(lesson: dict[str, Any]) -> list[str]:
    """Return production-contract errors for one lesson without regenerating it."""
    simulation = lesson.get("simulation")
    if not isinstance(simulation, dict):
        return ["simulation must be an object"]

    errors: list[str] = []
    subject = lesson.get("subject")
    engine = simulation.get("engine")
    allowed = MATH_ENGINES if subject == "math" else SCIENCE_ENGINES if subject == "science" else set()

    for key in ("id", "engine", "mode", "model", "goal", "mission"):
        if not _nonempty_text(simulation.get(key)):
            errors.append(f"simulation.{key} must be non-empty text")
    if allowed and engine not in allowed:
        errors.append(f"unsupported {subject} simulation engine: {engine!r}")
    if simulation.get("mode") not in {"model", "explorer"}:
        errors.append("simulation.mode must be 'model' or 'explorer'")

    refs = simulation.get("sourceRefs")
    if not isinstance(refs, list) or not refs:
        errors.append("simulation.sourceRefs must be a non-empty list")
    else:
        bad_refs = [ref for ref in refs if not _public_url(ref)]
        if bad_refs:
            errors.append("simulation.sourceRefs must contain only public http(s) URLs")

    simulation_id = simulation.get("id")
    if _nonempty_text(simulation_id) and _nonempty_text(subject) and not simulation_id.startswith(f"sim-{subject}-"):
        errors.append(f"simulation.id must start with sim-{subject}-")

    errors.extend(_learning_design_errors(simulation.get("learningDesign")))
    if engine == "math-ticket-equation":
        errors.extend(_ticket_equation_errors(simulation))
    if engine == "math-equation-meaning":
        errors.extend(_equation_meaning_errors(simulation))
    if engine == "math-reasoning-lab":
        errors.extend(_reasoning_lab_errors(lesson))

    return errors

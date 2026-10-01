# CURRENT STATE

## Social Studies final review — 2026-10-01

The formal Social Studies curriculum review is complete on `main` for all 210 `content-(geo|hist|civ)-*-iv-*` units.

- Lessons: 210 / 210 pass the Social final audit; every formal lesson is `reviewed`, has at least three substantive interactive steps, and contains none of the blocked generic interaction/summary patterns checked by `scripts/audit_social_final.py`.
- Unit specs: 210 / 210 are `content-reviewed`; every formal spec has at least one non-empty source locator.
- Formal question bank: 2,100 questions across the 210 formal Social units. Every formal unit has at least 10 questions; the audit requires a non-empty answer, explanation, solution strategy, and at least three solution steps for every question.
- All Social question files: 3,610 questions. `scripts/audit_social_unit_fit.py` passes with 0 structural mismatches across subject, lesson linkage, lesson-declared Knowledge Graph linkage, and provenance source locator.
- GitHub Actions `social-final-audit` is the authoritative automated regression gate for these checks.

Legacy/compatibility lessons outside the 210 formal `content-(geo|hist|civ)-*-iv-*` units are not promoted by this review. Their publication lifecycle remains independent, per `AGENTS.md`; they must not be used to downgrade or overwrite the completed formal-unit review record.

The repository-wide `data-validation` workflow is a separate cross-subject gate. A failure caused by another subject does not change the Social-specific result; any future Social regression must be determined by the Social audit or by a Social-path error in the repository-wide validators.

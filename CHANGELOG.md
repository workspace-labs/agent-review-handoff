# Changelog

## Unreleased

Test tooling only. The skill is unchanged and stays 1.1.0.

- Added `tests/fixtures.py`: builds the nine behaviour cases as small Git projects with one prompt each,
  and afterwards reports what each reviewer changed. The requests are read from
  `tests/behavioral-cases.md`; the expected results never reach a prompt.
- One package check builds the fixtures in a temporary folder and confirms a changed file is reported.
- First run of the nine cases, 2026-11-16: one fresh Codex session per case with the installed 1.1.0.
  All nine reports met their expected result, and no reviewer changed the project it reviewed. One run
  per case, evaluated by the builder of the cases, with no run without the skill to compare against.

## 1.1.0 — 2026-11-16

- **New rule: a result that changes on unchanged work decides nothing.** When a check gives different results on repeated runs against the same candidate, or a verdict differs from an earlier review of the identical candidate with no new evidence, the reviewer reports every result and does not choose one. An unstable pass never establishes acceptance. An intermittent failure is classified by its evidence, not by whether its cause is known: a shown violation is a finding, an environmental failure is not a candidate defect, and an unestablished one blocks only the affected criterion.
- `SKILL.md` now carries its version: `Skill version: 1.1.0`.
- Removed the closing "Creation provenance" line from `SKILL.md`. It was history, not an instruction, and it is recorded under 1.0.0 below.
- Added `tests/test_skill_package.py`: offline checks of the package's wiring (name, description length, links, reference files, version against this file).
- Added `tests/behavioral-cases.md`: nine written cases for exercising a reviewing agent with the skill. They have not been run yet.
- Added the README hero picture, `media/independent-review-handoff-hero.png`.

## 1.0.0 — 2026-11-16

The first versioned copy. The skill is unchanged: these are the installed files exactly as they were.

- `skills/independent-review-handoff/`: `SKILL.md`, four reference files and `agents/openai.yaml`.
- Added the repository around it: `README.md`, `CHANGELOG.md`, `LICENSE` (MIT) and `.gitignore`.

Before this repository:

- The skill was created on 2026-09-17, as its own closing line records.
- The installed files were last changed on 2026-10-17. What changed then was not recorded.

Known gaps at 1.0.0, closed in 1.1.0 except running the behaviour cases:

- No automated tests and no written behaviour cases.
- `SKILL.md` carries no version number.
- The closing "Creation provenance" line of `SKILL.md` is history, and belongs here rather than in the instructions.

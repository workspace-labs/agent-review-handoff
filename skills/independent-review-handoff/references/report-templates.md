# Report and corrective handoff templates

Use the established project format first; embed the essential information instead of duplicating reports. Fill with verified task facts, label uncertainty, and omit irrelevant detail without hiding a material gap.

## Compact

```text
VERDICT / SCOPE: verdict, task/criterion, protected behavior, review or SELF-REVIEW
TARGET: repository/platform, baseline, candidate snapshot/dirty state, artifact if relevant
EVIDENCE: important claim → criterion → evidence → result; actual check status/provenance
FINDINGS / LIMITS: actual blockers/IDs, non-blocking notes, missing verification
INTEGRITY / GATE: what was compared, side effects, owner decision and safe next step
```

A confirmed actionable finding still needs the complete finding contract, compressed where clear. Append the corrective packet only if implementation corrections are required. No invented finding or repair packet for a passing change.

## Standard / Full

1. **VERDICT AND REVIEWED SCOPE** — answer and actual blockers first; identify independent review versus SELF-REVIEW.
2. **BASELINE / CANDIDATE IDENTITY** — commit plus working tree or reproducible manifest, platform/artifact/version, identity recheck.
3. **AUTHORIZED CONTRACT AND PROTECTED AREAS** — accepted criteria, decisions, boundaries.
4. **IMPLEMENTATION / DATA-CONTRACT REVIEW** — relevant callers, state/data paths, conclusions with basis.
5. **INDEPENDENT VERIFICATION AND REPRODUCTIONS** — claim/criterion/evidence/result, independent oracle.
6. **TEST RESULTS AND EVIDENCE PROVENANCE** — commands, environment, revision, statuses, failed/skipped runs, attribution.
7. **REGRESSION / EDGE-CASE RESULTS** — required routes/lifecycles and relevant adjacent contracts.
8. **FINDINGS AND EXISTING-FINDING STATUS** — full actionable contracts, IDs/severity/classification; unverified risks clearly separated.
9. **LIMITATIONS / UNVERIFIED ITEMS / OWNER DECISIONS** — missing proof, conflicts, proposals.
10. **REPOSITORY / ARCHIVE / DATA INTEGRITY** — compared scope, exclusions, dirty state, actual side effects.
11. **ACCEPTANCE GATE** — technical recommendation, owner's separate acceptance/release/further-work decision.
12. **CLAUDE CORRECTIVE HANDOFF — FOR OWNER AUTHORIZATION** — only when corrections are required, always last.

Full deepens the relevant evidence; it does not pad every heading. A blocked review gives the missing evidence and safe resumption point, with any confirmed defects retained.

## Corrective

Lead with per-ID **CLOSED / REOPEN / UNVERIFIED** (or required project vocabulary) and the overall review verdict. For each: original criterion/reproduction → corrective diff/candidate → original failure check → relevant siblings/regressions → evidence/status. Preserve attempts, note deviations, assign genuinely new defects new IDs. Include identity, limitations, integrity, and the owner gate. End with a corrective packet for remaining/new implementation corrections, not for already satisfied findings.

## Copy-ready repair packet

Use this exact section title and, unless a project format supersedes it, every named section below. Complete all fields from verified facts. Include a minimal per-ID reproduction with concrete inputs, observed/required results, cause certainty, and impact even if the detailed finding is elsewhere. References avoid repeating full findings only when the recipient receives the named artifact with its path, candidate identity, and relevant section. “See above” and “the earlier reproductions” are not usable references when only the packet is forwarded. Identify the repository root so relative paths resolve in a new session.

```text
CLAUDE CORRECTIVE HANDOFF — FOR OWNER AUTHORIZATION

TASK AND TARGET
Project/repository, platform, candidate commit plus changes or snapshot, exact finding IDs.
List any required attached finding/evidence artifacts with their identity and location.

AUTHORIZATION
This packet describes required corrections; it does not grant permission to begin
implementation, commit, install, upload or expand scope. Follow the owner's authorization
and repository rules.

FINDINGS TO CORRECT
For each ID: exact defect, preconditions and reproduction steps, observed versus required
behavior, root cause CONFIRMED or HYPOTHESIS with basis, and impact. Refer to a supplied
detailed finding once when helpful; include enough facts here to identify and reproduce it.

REQUIRED OUTCOME
For each ID: testable invariant, allowed outcome, explicitly forbidden outcomes.
Label any stronger/new requirement PROPOSED and awaiting owner approval.

SCOPE AND PROTECTION
Task-justified boundary, protected contracts/data/unrelated behavior, prohibited unrelated
work, real dependencies between findings, and where expansion needs approval. The builder
chooses the technical approach within approved constraints; avoid unnecessary file locks.

REQUIRED VERIFICATION
Original reproduction, semantic regression tests that expose the original defect, mandatory
failure/boundary cases, affected adjacent input routes, and applicable existing checks.
Identify independent expected values/oracles, environment, and evidence to return.

ACCEPTANCE
Exact binary closure criteria for each ID tied to evidence. Passing a test count alone
is insufficient. Independent re-review must confirm these criteria for the returned candidate.

BUILDER RETURN
Files changed, implementation summary, actual commands/tests/status/results, evidence,
candidate snapshot/commit including uncommitted changes, deviations, limitations, and status
CORRECTED / DELIVERED FOR RE-REVIEW. Attribute inherited or unexecuted checks accurately.

STOP
Return for independent re-review. Do not mark findings CLOSED yourself, start the next task,
claim owner acceptance, or treat this packet as release or additional-work authorization.
```

Before finalizing, read only the extracted packet: can the recipient identify each defect, reproduce it without guessing cases, state the invariant and protected behavior, run closure checks, and know the authorization/stop boundary? If not, complete the packet or supply an explicitly named artifact before delivery. This is a document check, not permission to launch another agent.

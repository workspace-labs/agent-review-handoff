# Findings, corrective actions, and re-review

Read for every actionable finding, corrective brief, or assigned re-review.

## Finding contract

Preserve existing IDs and project severity terms. Otherwise use F01, F02, … with Critical / High / Medium / Low, justified by concrete impact and affected cases, not dramatic wording. Finding status and overall verdict are different: OPEN or REOPEN does not itself specify severity/blocking status.

Complete every field below. Write “not applicable” or “unavailable” with the reason when appropriate; never invent a location, failure, measurement, certainty, or cause.

```text
Finding ID:
Title:
Status:
Severity:
Severity rationale:
Scope classification: A / B / C / D, with basis
Candidate commit/snapshot:
Affected file and symbol:
Relevant line range, verified against that revision: (or required project anchors)
Required behavior or invariant:
Observed behavior:
Reproduction preconditions and steps:
Evidence location and relevant result:
Root cause: CONFIRMED or HYPOTHESIS, with basis
Impact and affected cases:
Required correction outcome:
Protected behavior:
Verification needed to demonstrate closure:
```

A sound static proof can establish a confirmed defect without runtime reproduction: label it **STATIC PROOF**, identify the exact code path/inputs and consequence, and distinguish unexecuted reproduction steps. A hypothesized root cause can accompany a confirmed symptom. An unconfirmed symptom belongs under OPEN QUESTIONS / UNVERIFIED RISKS, not the confirmed defect list.

## Corrective action for each implementation correction

Define the exact defect/reproduction and invariant that must hold after repair. State allowed and forbidden outcomes, task-justified implementation scope, protected contracts/data/unrelated behavior, mandatory regression/failure cases, binary acceptance criteria tied to evidence, real dependencies on other findings, stopping point, and independent re-review requirement.

Let the engineer choose how to implement. Do not force a rewrite, dependency, backend change, or a file allowlist too narrow for a correct shared fix unless the accepted contract mandates it. Behavioral/module boundaries can be more accurate than a list of files. Explain where scope expansion needs owner authorization. Label stronger or new requirements PROPOSED; do not smuggle them into closure criteria.

Include semantic regression evidence that exposes the original defect. Do not require every new test to fail on old code: unchanged safe controls should pass both versions. Do not weaken tests or alter a correct implementation just to satisfy an incorrect historical expectation. Document the independent oracle if tests resemble complex production logic; importing production answers as expected values is circular evidence.

Use the final packet in [report-templates.md](report-templates.md). Reference one detailed finding artifact with its exact candidate identity instead of repeating pages, but keep enough task facts in the packet to use it in a fresh session. The recipient must have the referenced artifacts; temporary evidence must be marked temporary.

## Corrective re-review

For each assigned ID:

1. Recover its original accepted criterion, reproduction, status, and prior attempts/evidence.
2. Identify the exact corrective diff and candidate; check compliance with the recommended outcome and any disclosed deviation.
3. Verify the previously failing behavior and relevant sibling routes, boundaries, failure cases, and regressions.
4. Inspect whether tests prove the invariant, hide the failure, weaken assertions, or copy the production mistake.
5. Return **CLOSED**, **REOPEN**, or **UNVERIFIED** with per-criterion evidence, subject to project status/gate rules.

CLOSED requires the entire original per-finding closure contract, including any originally mandatory source regressions and evidence, to be satisfied for this candidate. Passing the repaired behavior alone is insufficient when those deliverables are still absent, even if another finding blocks the overall review. Report the behavioral criterion as passed but the finding REOPEN for a confirmed missing required deliverable, or UNVERIFIED for unavailable proof; identify the exact unmet term. Do not invent a new test requirement if the original contract did not require it. CLOSED does not mean the product has no other defects. REOPEN names the precise unmet original criterion and observed failure. UNVERIFIED names the missing evidence/access and resumption point. A missed route covered by the original invariant keeps the original ID open; a distinct new defect receives a new ID and corrective action. Group shared-root repairs operationally if helpful, while retaining separate closure evidence for each ID. Never replace an old criterion with a new architectural preference.

The builder returns **CORRECTED / DELIVERED FOR RE-REVIEW**, never closes its own finding or claims owner acceptance. Retain attempt history. Technical closure, owner acceptance, release permission, and the next task remain separate gates.

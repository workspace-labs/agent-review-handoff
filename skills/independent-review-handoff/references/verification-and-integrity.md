# Verification, evidence, and integrity

Read before executing checks, inheriting earlier results, or reviewing specialized/high-risk behavior.

## Safe execution and preservation

Inspect test/build scripts, imported setup, lifecycle hooks, profiles, caches, network/device access, and output destinations before executing. Copy only necessary synthetic/authorized material into disposable isolation outside protected trees. A symlinked dependency tree may write through to the source; a separate directory alone is not proof of isolation. Avoid real profiles/devices and external effects without explicit authorization. Do not disable sandboxing or bypass approvals; record blocked commands and the resulting missing evidence.

Capture before/after integrity proportional to risk: relevant file content hashes, inventory (including untracked files), Git status/diff, symlink targets, mode/mtime or data/archive manifests as needed. Explain exactly what was compared and excluded, including access time when appropriate. Preserve pre-existing dirty changes. Clean Git status alone does not establish filesystem immutability, archive safety, or data preservation. Do not infer that no historical upload occurred from local Git state.

Reports/examples/fixtures must not expose credentials, private keys/tokens, or real private records. Use synthetic skill-validation data. If a real review reveals a secret, redact the value, identify the affected surface, and stop unsafe activity; rotation and evidence deletion require separate permission. Record actual side effects, even unintended ones.

## Evidence ledger

For every important acceptance claim: **CLAIM → CRITERION → EVIDENCE → RESULT**. Inspect actual implementation/callers/data boundaries beyond builder-selected tests. Use direct analysis, targeted reproduction, rendered interaction, independent calculation, or failure injection as appropriate.

Each command/check entry includes:

```text
Command or static analysis method:
Target revision/snapshot and relevant artifact:
Environment/platform and disposable profile:
Execution status: PASS / FAIL / NOT RUN / ENVIRONMENT BLOCKED / INCONCLUSIVE
Relevant result, excerpt/measurement, and evidence path:
Provenance: reviewer executed / builder-reported only / inherited unchanged scope
Limitations and side effects:
```

A build is not behavioral correctness; passing tests are not complete coverage; screenshots are not data integrity. Separate skipped from passed. Do not add subset suites to full-suite counts as additional unique tests. Do not combine counts from different revisions. Retain important failed runs and classify expected fail-first, fixture mistake, product failure, or environment problem. Evidence links must exist and identify useful results; mark temporary paths as temporary.

For inherited verification, show equality of the relevant code/artifact and environment assumptions, link the earlier run/revision, and state residual limits. This can justify avoiding an expensive unchanged suite in a narrow docs review, but is not a fresh PASS.

## Adversarial checks by invariant

Select relevant normal/boundary/malformed/missing inputs, repeat/interruption/retry, first/second launch, state transitions, cancellation, stale results, identity/authorization, compatibility, and preservation. Follow the invariant through every required input route. Wheel correctness does not prove pinch correctness. Separate defect identities even when the same family of code is involved. Explain the independent oracle and numerical tolerance rather than duplicating production algorithms or taking their outputs as expected values. Do not search for a quota of defects; inspect inconvenient evidence fairly.

## Specialized emphasis

- **Data/migration:** canonical representation, validation, partial failure, retry/idempotence, old-data compatibility, recovery, first/second launch. App launch does not establish data preservation; a copied backup is not a tested restore.
- **Numerical/units:** physical meaning, conversion boundaries, independent expected values, justified tolerances. Display preferences must not alter canonical meaning when that is the contract.
- **UI/gestures:** rendered required input paths, release/cancel, lifecycle states. Distinguish math-only checks, injected events, emulator, and physical-device evidence. Do not claim an untested route works.
- **Structural refactor:** intended behavior change is NONE unless explicitly authorized. Check persistence, public contracts, imports, packaging, and runtime output. Use semantic equivalence; legitimate module relocation need not preserve bundle hashes.
- **Documentation:** commands, links, source claims, current versus future statements. Use current official primary documentation for platform claims, and separate project policy from platform requirements. Keep verification proportional.
- **Release/signing:** source-to-artifact provenance, version/package identity, signing compatibility, external secrets. Signing success does not establish migration safety. Do not install to prove an unapproved release.
- **Performance:** method, workload, sample, acceptance threshold, measurements, and limitations. Subjective smoothness is not numerical proof.

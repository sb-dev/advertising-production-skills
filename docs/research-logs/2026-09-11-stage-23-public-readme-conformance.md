# Stage 23: Public README conformance repair

Date: 11 September 2026  
Branch: `feat/bootstrap`  
Stage status: PASS before publication gate  
Predecessor: Stage 22 commit `0e4038f80a2fb5dc4f9ad487b06fee1bc45ca1d7`

## Purpose

Adopt the Production Skills public README contract through an appended conformance stage, preserving completed Advertising Stages 0–22 exactly.

The repair addresses a public-surface defect: the Stage 22 root README exposed bootstrap state and future stage numbers, reduced skills to a responsibility table, used bootstrap research logs as product navigation and omitted the full Level 1 quick-start prompt.

## Governing sources

- Production Skills public README process, commit `da7bea1d79013de584e7d53addb7f410b6521e3f`;
- Production Skills public README template at the same commit;
- Narrative Production Skills public README as a proven family reference;
- Advertising canonical Specs 01–06;
- accepted Advertising E01–E15 designs from Stage 16;
- Stage 22 production scaffold as the immutable predecessor.

No earlier Advertising stage output is rewritten.

## Acceptance checklist

| ID | Requirement | Result |
|---|---|---|
| R23-01 | Root README is product-facing rather than a bootstrap/maturity report | PASS |
| R23-02 | Advertising control model exposes commercial, audience, claim/proof and authority distinctions | PASS |
| R23-03 | Installation is direct product onboarding and contains no stage caveat | PASS |
| R23-04 | E01 complete copyable prompt is inline in the root README | PASS |
| R23-05 | Learn by Producing contains five levels × three primary examples, E01–E15 | PASS |
| R23-06 | Root example navigation uses the public `examples/` surface instead of research logs | PASS |
| R23-07 | Project structure grows with campaign complexity | PASS |
| R23-08 | All four skills have substantive explanatory sections | PASS |
| R23-09 | Packs, execution, measurement, testing, docs, boundaries, contribution and licence are public-facing | PASS |
| R23-10 | Obvious bootstrap-state leakage is rejected deterministically | PASS |
| R23-11 | Existing skill, spec, benchmark and scaffold surfaces remain preserved | PASS |
| R23-12 | Stage 23 is committed as one direct child of Stage 22 and remotely verified | pending publication |

## Public-surface changes

### Root README

The README now follows this Advertising-specific public sequence:

```text
positioning and capabilities
→ claims, proof and commercial control
→ install
→ complete E01 quick start
→ 5 × 3 Learn by Producing
→ growing campaign structure
→ four substantive skill sections
→ Extension Packs
→ execution
→ measurement / optimisation
→ testing / benchmarks
→ documentation
→ boundaries
→ contributing
→ licence
```

The root README contains no Stage-number references, branch names, completion SHAs, bootstrap-progress narration, maturity-promotion schedule, `not-run` bookkeeping or links into `docs/research-logs/`.

### Public examples index

`examples/README.md` is now a product-facing progression map with stable E01–E15 headings. Root README links resolve to those public anchors. The historical selection evidence and complete source catalogue remain preserved under research logs but are no longer the root onboarding path.

### Deterministic regression protection

`tools/validate_repo.py` now verifies:

- required public section headings;
- no obvious bootstrap-state leakage in root README;
- complete E01 prompt markers inline;
- five level headings;
- exactly E01–E15 in the Learn by Producing section;
- substantive headings for all four skills;
- canonical install route;
- public/local link resolution;
- existing skill/command/package/benchmark/scaffold integrity.

Its self-test adds deliberate mutations for README leakage, missing quick-start facts, broken progression and missing skill sections in addition to prior structural defects.

## Internal bootstrap artefacts

Stage 23 adds:

- `2026-09-11-stage-23-public-readme-contract.md`;
- `2026-09-11-stage-23-public-claims-ledger.md`;
- this conformance record.

The claims ledger remains internal and is not copied into the README.

## Future sequence

Completed Stages 0–22 retain their identifiers. The appended repair becomes Stage 23. The remaining unexecuted work is now tracked as:

```text
24  first core vertical
25  full progressive examples and Extension Packs
26  installation and repository integrity
27  optional Pactwright integration and registry treatment
28  shared-abstraction review
```

This renumbering applies only to unexecuted future work and does not rewrite any completed stage.

## Evidence boundary

This stage validates public README structure, navigation and process separation. It does not claim campaign execution, generated-media quality, pack differential results, clean installation, host compatibility, Pactwright compatibility or registry maturity.

R23-12 closes only after the branch is advanced to the Stage 23 commit, the parent/tree/diff are remotely checked and CI succeeds.

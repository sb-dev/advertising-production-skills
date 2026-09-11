# Stage 22: Production repository scaffold

Date: 11 September 2026  
Working branch: `feat/bootstrap`  
Stage acceptance: PASS before publication gate  
Approved licence: MIT

## 1. Stage purpose and authority

Stage 22 converts the accepted bootstrap workspace into the smallest useful production repository scaffold after completion of the six canonical specifications, public README design and cross-project review. The governing source remains the original bootstrap specification on `main`, especially Stage 22 / section 16 and the global rules forbidding premature runtime, campaign or maturity claims.

The accepted predecessor is Stage 21 commit `f908b947433af8fd78fa63391a72dfade9b12bb4`. Stage 21 preserved the six canonical specifications, corrected public README design, current specialist boundaries and five non-extracted abstraction candidates. No previous failed branch or alternate scaffold was used as an implementation source.

The user explicitly selected MIT for the mandatory repository `LICENSE`. No other later-stage business, creative or integration decision is made here.

## 2. Completion checklist

| ID | Requirement | Governing reference | Stage 22 implementation |
|---|---|---|---|
| S22-01 | Scaffold only after six specifications | Original §16; Spec 03 §1–2 | Six accepted specs preserved before production surfaces are added |
| S22-02 | Root README, licence, contribution and changelog surfaces | Original §16; family project contract | Public README adopted with truthful scaffold status; MIT `LICENSE`; `CONTRIBUTING.md`; `CHANGELOG.md` |
| S22-03 | Real `skills/` production surface | Original §16; Spec 03 §§2–5 | Four independently usable `SKILL.md` entry points, skill-local references and exact 33 owned intent files |
| S22-04 | Real examples surface without invented execution | Original §§11/16; Spec 04 | `examples/README.md` records E01–E15 exactly three per level and links complete accepted prompts; status `not-run` |
| S22-05 | Real benchmark surface without invented results | Original §§13/16; Spec 04 | `benchmarks/README.md` plus machine-readable frozen designed counts, all execution status `not-run` |
| S22-06 | Deterministic repository/helper checks | Spec 03 §§7–8 | `tools/validate_repo.py`, `tests/test_repository.py`, `pnpm validate`, `pnpm test` |
| S22-07 | Real CI surface | Original §16; Spec 03 §7 | GitHub Actions workflow runs deterministic validate/test only; read-only contents permission |
| S22-08 | No cosmetic empty directories | Spec 03 §2; Stage 21 build-order review | No empty Extension Pack or integration directory is created; optional directories wait for actual contents |
| S22-09 | No prohibited platform infrastructure | Original §§8/16/19 | No CRM, DSP, ad server, attribution service, account store, analytics warehouse or provider runtime added |
| S22-10 | Honest maturity/evidence boundaries | Original §18 and global maturity rules | Root README states production scaffold; Stage 23–25 execution/installation evidence remains explicitly absent |
| S22-11 | Preserve accepted work | Execution attachment §§7–9 | Existing research/specification blobs remain inherited from predecessor tree; Stage 22 only adds/updates scaffold-owned paths and progress |
| S22-12 | Verify actual scaffold and commit remotely | Execution attachment §§7–9 | Prepublication tree inspection, validator self-test, final remote ref/commit/tree/file and CI checks |

## 3. Scaffold decisions

### 3.1 Production layout

The scaffold contains actual files under every introduced directory. `extension-packs/` is deliberately not created yet because Spec 03 says to add actual implemented packs rather than an empty placeholder; implementation and comparison belong to Stage 24. `integrations/` is optional and waits for the Stage 26 Pactwright decision. No empty `assets/`, `scripts/` or `evals/` subdirectories are created inside skills.

### 3.2 Four skill packages and exact command ownership

The Stage 22 packages are:

```text
advertising-build        → 13 intents
advertising-optimise     → 10 intents
advertising-evaluate     → 9 intents
advertising-pack-author  → 1 intent
                         = 33 total
```

Every skill has YAML metadata, an activation/boundary contract, one skill-local core reference and all owned intent files. Each intent file states purpose, inputs, outputs, checks and failure routing. This makes the production surface usable as instructions without claiming Stage 23 behavioural proof or Stage 25 clean-install evidence.

The packages do not require Pactwright, an advertising account, provider API, CRM or sibling Advertising skill merely to read their own contracts. Later installation verification must still prove actual selective installation and bounded invocation from clean consumers.

### 3.3 Examples and benchmarks

Stage 22 indexes, but does not execute, the fifteen exact primary examples. The index maintains the exact 5×3 distribution and links to the complete Stage 16 prompt source. No output folder is created for a case that has not run.

The benchmark manifest preserves accepted designed counts:

```text
core vertical             1
primary examples         15
pack conditions          48
canonical cases          79
pack-authoring cases      2
supplemental regressions  4
installation combinations 8
```

All are marked `not-run`. Repository structural checks are separate from these campaign/behavioural suites.

### 3.4 Tooling and CI

The only scaffold helper is a standard-library Python repository validator. It checks required root/spec files, MIT licence, pinned development package manager, exact skill and command ownership, skill metadata/links, public README sections/evidence wording, exact E01–E15 distribution, frozen benchmark counts, required scaffold surfaces and CI commands.

The validator includes a `--self-test` fixture. Before publication the exact validator source was executed locally in self-test mode and passed six deliberate mutations:

1. missing skill;
2. wrong skill metadata;
3. missing command;
4. broken local link;
5. wrong example-level distribution;
6. false benchmark execution status.

`tests/test_repository.py` applies the same validator to the real checkout and includes four repository-copy regressions. GitHub Actions installs pinned pnpm `12.3.4`, then runs `pnpm validate` and `pnpm test`. No model/provider/live-ad secrets or paid tests are requested by this workflow.

## 4. Explicitly deferred work

The following are mandatory later-stage work, not Stage 22 substitutions:

- Stage 23: installed first core vertical and actual campaign artefacts/evaluation/correction;
- Stage 24: all fifteen primary executions, eight implemented packs, all 48 pack conditions and required canonical/authoring/regression coverage;
- Stage 25: local and pinned-remote clean installation of all four skills, actual resource use and update/removal preservation;
- Stage 26: explicit optional Pactwright integration/registry decision;
- Stage 27: evidence-based shared-abstraction review.

No generated image/video/audio, campaign performance, Legal clearance, host compatibility, release or registry promotion is claimed by the scaffold.

## 5. Verification and conformance

The original Stage 22 / Production Scaffold section was reread after implementation. Verification is against that source plus accepted Specs 01/03/04 rather than this log alone.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| Scaffold follows six specs | Original §§14/16 | inherited `docs/01`–`06` | predecessor and proposed tree inspected | PASS |
| Required root project files | Original §16 | README, MIT LICENSE, CONTRIBUTING, CHANGELOG, package.json | exact proposed-tree paths and contents inspected | PASS |
| Skills surface | Spec 03 §§2–5 | four SKILLs, four local core references, 33 commands | exact names/counts/distribution and required contract headings checked | PASS |
| Examples | Original §11; Spec 04 | E01–E15 index and source links | 15 IDs, exactly 3 each L1–L5, `not-run` state checked | PASS |
| Benchmark surface | Original §13; Spec 04 | benchmark README and suites manifest | exact accepted designed counts and `not-run` state checked | PASS |
| Deterministic validator | Spec 03 §7 | `tools/validate_repo.py` | validator source executed with six negative mutations; all detected | PASS |
| Repository regression tests | Spec 03 §7 | `tests/test_repository.py` | code inspection plus remote CI execution required at publication | PASS |
| CI | Original §16; Spec 03 §7 | `.github/workflows/validate.yml` | workflow contains pinned pnpm and actual validate/test commands; remote run checked after commit | PASS |
| Non-cosmetic layout | Spec 03 §2 | no empty optional pack/integration dirs | proposed tree inspected | PASS |
| Prohibited infrastructure absent | Original §§8/16/19 | scaffold tree | no platform/account/CRM/DSP/warehouse runtime introduced | PASS |
| Evidence/maturity truth | Original §18; global maturity | README, examples, benchmark manifest, changelog | later-stage execution remains explicitly unclaimed | PASS |
| Earlier work preserved | global verification | Stage 21 base tree plus scaffold additions | base-tree construction preserves untouched predecessor entries | PASS |

### Verification evidence limits

The validator self-test proves the validator rejects the six listed structural/evidence corruptions; it is not an agent benchmark. Repository tests and CI prove deterministic scaffold integrity only. They do not prove the advertising skills produce good campaigns, that generated media is acceptable, that clean installation works, or that any host/provider integration works.

## 6. Exit assessment and Stage 23 input

All mandatory Stage 22 scaffold requirements pass subject to the final publication gate: create the Stage-22-scoped completion commit, advance `feat/bootstrap` non-forced, verify the remote commit/tree/intended files and inspect the deterministic CI result. No user-owned decision remains for this stage after the MIT choice.

Stage 23 receives a real public scaffold, four skill entry points, exact 33-intent surface, deterministic validator/tests, accepted six specs, full synthetic E01 source and the rule that Stage 23 must prove the complete first core vertical rather than merely describe it.

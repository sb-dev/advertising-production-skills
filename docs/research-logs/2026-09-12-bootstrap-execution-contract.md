Execute the remaining bootstrap process below. Treat EACH STAGE AS A SEPARATE, COMPLETE TASK, exactly as though it were the only task I had asked you to perform.

Bootstrap specification: https://github.com/sb-dev/advertising-production-skills/blob/feat/bootstrap/docs/research-logs/2026-09-08-advertising-production-skills-new-project-bootstrap-process.md

Repository: `sb-dev/advertising-production-skills`

Working branch: `feat/bootstrap`

Starting point: commit `f877c32294de40b617c79375381b2130f0c547bd` on `feat/bootstrap` — the Stage 23 public README conformance repair. The remote branch ref was verified to point to this commit before this execution contract was created. Its parent is the accepted Stage 22 scaffold commit `0e4038f80a2fb5dc4f9ad487b06fee1bc45ca1d7`.

Accepted prior-stage state: Stages 0–22 are recorded as PASS in `docs/research-logs/README.md`. Stage 23 is the accepted public README conformance amendment defined by `2026-09-11-stage-23-public-readme-contract.md`; its content commit is the starting point above. Preserve all accepted Stages 0–23 unless a later requirement exposes a genuine contradiction or defect that requires changing accepted work. If that happens, STOP THE PROCESS AND ASK ME before modifying an accepted earlier-stage artefact.

Remaining stages authorised: Stages 24–28, executed strictly sequentially under the accepted continuation numbering:

```text
24. Implement and Prove Core Vertical
25. Expand Progressive Coverage and Extension Packs
26. Validate Installation and Repository Integrity
27. Optional Pactwright Integration + Registry Treatment
28. Review Shared-Abstraction Candidates
```

These correspond semantically to original bootstrap Stages 23–27 after the accepted Stage 23 public README conformance amendment inserted an additional stage. The original bootstrap remains authoritative for the substantive requirements of those responsibilities; the accepted progress record and Stage 23 contract govern the continuation numbering.

Do not restart Stages 1–23. Do not use another branch as an implementation source, shortcut, template or authority unless I explicitly instruct you to do so.

## 1. Non-negotiable execution rule

Authorisation to complete multiple stages means repeating the full execution and verification process for each stage. It does NOT mean batching stages, summarising their intent, reducing their depth or replacing required outputs with representative samples.

Your unit of work is ONE STAGE.

Treat the current stage exactly as if it were the ONLY task I had asked you to perform.

Do not consider later stages when deciding how much research, production, implementation or verification the current stage deserves.

Do not start the next stage until the current stage:

- has every mandatory requirement satisfied;
- has every required activity actually performed;
- has every required deliverable present and complete;
- satisfies every exact count, distribution, structure and content requirement;
- has passed every specified exit criterion;
- has its verification evidence recorded;
- has been committed to `feat/bootstrap`;
- has the remote commit verified.

A stage is not complete merely because:

- a research log exists;
- a file has the expected name;
- an implementation is described;
- a representative subset was produced;
- a validator exists but was not executed;
- CI could theoretically execute it later;
- later work could theoretically finish it;
- a commit was created.

Never substitute:

```text
representative
partial
illustrative
provisional implementation
future target
planned
designed
execution pending
```

for a requirement that the current stage says must actually exist, execute or pass.

If a stage requires an exact number of examples, packs, prompts, variants, evals, benchmark cases or installations, produce and verify that exact number.

If a stage requires execution, execute it.

If a stage requires actual generated media, inspect the actual generated artefact. A prompt, script, storyboard or production brief is not a substitute for an image, video or audio file when the requirement calls for finished media.

If a stage requires a measured comparison, do not replace it with a description of the expected result.

## 2. Authority and questions

The governing bootstrap specification, accepted Stages 0–23 and this execution contract form the acceptance boundary for the remaining stages.

Do not rewrite, weaken, reinterpret, waive or silently defer a requirement because satisfying it makes the stage larger.

If ANY question requires my input, STOP THE ENTIRE PROCESS AND ASK ME.

This includes:

- ambiguous or conflicting requirements;
- uncertainty about the accepted prior-stage boundary;
- missing required source material, campaign facts, brand constraints or reference assets;
- an unavailable tool/provider required to satisfy or verify a mandatory requirement;
- a failed prerequisite;
- an unresolved requirement from an earlier accepted stage;
- a proposed deferral, substitution, scope reduction or exception;
- a creative/business decision that belongs to me;
- any external action requiring authority I have not explicitly provided.

Do not answer such questions on my behalf.

Do not make a “reasonable assumption” and continue when my decision is required.

Do not continue with another stage while waiting for an answer.

The rule is:

```text
QUESTION REQUIRES USER INPUT
→ STOP
→ ASK
→ DO NOT CONTINUE UNTIL ANSWERED
```

Use only `feat/bootstrap` throughout the remaining bootstrap unless I explicitly change the branch strategy.

## 3. Before starting EACH stage

At the beginning of every stage:

1. Re-read the ORIGINAL bootstrap specification.
2. Read the complete substantive requirement for the current continuation stage, mapping Stage 24→original 23, 25→24, 26→25, 27→26 and 28→27.
3. Read the global principles, acceptance gates, non-goals and cross-references that constrain it.
4. Read the accepted outputs from earlier stages on `feat/bootstrap` that the stage depends on.
5. Verify that every prerequisite actually exists and passed its prior exit criteria.
6. Verify that the current branch still descends from the accepted starting point and has not silently incorporated unrelated work.

Then extract a stage-specific acceptance checklist.

The checklist must explicitly capture:

```text
stage purpose
required inputs
prerequisites
questions to resolve
required research
required production activities
required implementation
required comparisons
required candidate discovery
required analysis
required decisions
required deliverables
required contents of each deliverable
exact counts
exact distribution requirements
exact naming requirements
exact structural requirements
required prompts
required examples
required assets
required campaign variants
required Extension Packs
required evals
required tests
required execution
required measurements
required installation checks
required verification
research-log output
exit criteria
things explicitly deferred to later stages
```

For every checklist item, cite or identify the corresponding requirement in the bootstrap specification or accepted continuation amendment.

Before substantive work, state:

```text
Stage: <number and title>

Completion requires:
- ...
- ...
- ...
```

Do not begin work belonging to a later stage.

## 4. Execute the current stage fully

Give the current stage the same care, research depth, production effort, implementation effort and verification you would give it if no other bootstrap stages existed.

Do not optimise for reaching Stage 28.

Do not shorten work because several stages remain.

Do not convert exact requirements into weaker approximations.

Examples of the governing strictness:

```text
“approved offer + audience
→ campaign brief
→ message / claim / proof map
→ 2–3 cheap creative concepts
→ selection
→ representative ad variants
→ media / audience test
→ measurement contract
→ evaluation
→ bounded correction”

means the Stage 24 core vertical must actually demonstrate that complete vertical at the fidelity required by the accepted specifications.

It does NOT mean:
describe the vertical,
create empty directories,
write command stubs,
or claim the evaluator could run later.
```

```text
“expand to the selected 15 examples”
means all fifteen selected primary examples must be materially present at the required implementation level when Stage 25 owns that expansion.

It does NOT mean:
one example per level,
representative examples,
or fifteen design-only prompts when implementation is required.
```

```text
“every implemented pack must prove core works without pack, core + pack changes intended behaviour, precedence and pack evaluation”
means execute the required differential evidence for every implemented pack in scope.

It does NOT mean:
describe the intended difference.
```

```text
“validate clean external installation”
means perform the required clean external installation tests outside the source-repository assumptions and record the actual result.

It does NOT mean:
source-tree inspection,
a copy-only approximation where the contract requires the real installer,
or saying CI can run it later.
```

For advertising-production work, keep distinct wherever relevant:

```text
approved business objective
offer and price
audience hypothesis
platform targeting representation
claim
proof
creative concept
selected concept
approved creative
placement adaptation
media/test contract
publication authority
observed result
campaign learning
repair decision
```

Do not invent customer evidence, campaign outcomes, ROAS, CTR, CPA, conversions, testimonials, product capabilities, legal approvals, human approvals, benchmark executions, provider outputs, generated-media evaluations, installation results or test passes.

Synthetic fixtures must remain explicitly synthetic.

## 5. Advertising-specific production discipline

Advertising Production Skills owns campaign-production intelligence, not the upstream business model or downstream platform side effects.

Preserve this production path:

```text
approved business / offer / acquisition objective
→ campaign brief
→ audience and context evidence
→ message / claim / proof
→ creative hypotheses
→ cheapest useful representations
→ concept selection
→ cross-format production
→ media / placement test contract
→ destination continuity
→ evaluation
→ measurement
→ diagnosis
→ smallest responsible repair
```

Business Building or the consuming-project business owner retains customer, offer, price, business-wide channel choice and economics. Specialist Production Skills own final craft where appropriate. Legal owns legal conclusions. External systems own account mutation, serving, spend and data collection where specified.

Do not silently change an approved offer, price, customer or unsupported claim to make an advertising metric look better.

## 6. Claims, truthfulness and approval

Keep separate:

```text
supported fact
→ proposed claim
→ claim/proof assessment
→ creative expression
→ review / approval
→ publication authority
→ observed performance
```

And:

```text
approved business segment
→ advertising audience hypothesis
→ platform targeting representation
```

Do not allow optimisation to introduce unsupported product claims, fabricated statistics, fake testimonials, false scarcity, fake urgency, misleading before/after representations, hidden qualifications, unsupported comparisons, unsupported earnings/ROI claims, misleading price/renewal presentation or invented approvals.

If a creative path requires evidence or approval that does not exist, that path is BLOCKED. Do not manufacture the missing state.

Tool access, an earlier selection or a broad instruction to improve campaign performance is not publication/spend authority.

## 7. Verification before completion

After completing the current stage, re-read its governing requirement from the ORIGINAL bootstrap specification and accepted continuation contract.

Do not verify against your own summary of what you intended to do.

Inspect the ACTUAL repository, ACTUAL generated artefacts and ACTUAL execution results where required.

Produce a conformance table:

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| ... | ... | ... | ... | PASS / FAIL / BLOCKED |

Use only:

```text
PASS
FAIL
BLOCKED
NOT APPLICABLE
```

`NOT APPLICABLE` requires an explicit justification grounded in the governing specification.

Verification must include substance, not only filenames. Check where applicable:

- exact item counts and distributions;
- completeness and internal consistency;
- source/evidence provenance;
- required prompts and fixture classification;
- campaign briefs and claim/proof continuity;
- actual creative representations and finished media where required;
- placement/channel adaptations;
- destination consistency;
- Extension Pack activation/non-activation/precedence;
- core-vs-pack behavioural difference;
- required tests and actual results;
- actual agent/provider execution where mandated;
- actual installation commands and clean-environment evidence;
- preservation of accepted decisions;
- smallest-change repair behaviour;
- contradictions with earlier stages;
- maturity and public claims.

For media requirements: a prompt is not an image; a script/storyboard is not a finished video; an audio script is not an audio file. Inspect the representation the requirement actually asks for.

Do not weaken a validator, test, fixture, rubric or acceptance criterion to make incomplete work pass.

If anything is FAIL:

```text
repair it
→ run the same verification again
```

If anything is BLOCKED and requires my input:

```text
STOP
→ ASK ME
```

Do not begin the next stage.

## 8. Research-log requirements

Each remaining stage must leave a durable record sufficient for a future conversation to understand and verify it without relying on chat history.

Where relevant record:

```text
stage goal
accepted inputs inspected
sources actually accessed
source limitations
candidate pool
coverage/comparison analysis
production alternatives
decisions
rejected alternatives
claims/proof relationships
actual generated artefacts
provider/tool identity and configuration where material
actual tests and results
verification
conformance table
unresolved questions
explicitly deferred work
exit assessment
next-stage inputs
```

For generated work preserve enough provenance to distinguish:

```text
fixture/project input
retrieved evidence
approved decision
generation prompt
provider/model/tool
actual output
selection
approval
evaluation
repair
```

Do not mark a stage COMPLETE while using language such as “representative implementation”, “execution pending”, “future work will complete”, or “remaining examples can be added later” when the current stage owns those requirements.

## 9. Commit the completed stage

Only after every mandatory current-stage requirement is PASS:

1. Persist all complete stage outputs.
2. Persist the verification/conformance evidence.
3. Update the durable progress record accurately.
4. Review the changes for unrelated files.
5. Commit only the current stage's work to `feat/bootstrap`.
6. Verify the remote branch points to the new commit.
7. Verify the intended files exist at that immutable commit.
8. Record the stage completion receipt if that is the established branch convention.

Commit messages must remain stage-scoped.

Examples:

```text
feat: complete stage 24 core advertising vertical
feat: complete stage 25 progressive coverage and extension packs
chore: complete stage 26 installation and repository integrity
```

Do not combine several stages into one completion commit.

Do not place unfinished next-stage work in the current commit.

After remote verification, report:

```text
Stage:
Status: COMPLETE

Deliverables:
- ...

Verification:
- ...

Commit:
<full SHA>

Remaining blockers:
none
```

Only then may the next authorised stage begin.

## 10. Stage progression

Stages 24–28 are authorised, but authorisation does NOT make them one task.

The execution model is:

```text
STAGE 24 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely
→ verify the remote commit

THEN

STAGE 25 IS THE ONLY TASK
→ finish it completely
→ verify it completely
→ commit it completely
→ verify the remote commit

THEN

STAGE 26 IS THE ONLY TASK
...
```

Do not think:

```text
“I need to finish the remaining bootstrap.”
```

Think only:

```text
“I need to complete the current stage perfectly.”
```

The existence of a later stage must never justify incomplete work in the current stage.

## 11. Context and interruption safety

The repository is the authoritative bootstrap state.

At the start of every new stage, reconstruct context from:

```text
governing bootstrap specification
+
accepted Stage 0–23 outputs on feat/bootstrap
+
accepted outputs of any continuation stages already completed under this contract
```

Do not rely on long conversation memory.

If context becomes too large, STOP at the current verified stage boundary rather than compressing, batching or skipping requirements.

It is better to complete fewer stages correctly than to reach Stage 28 incorrectly.

If interrupted during a stage:

- do not claim completion;
- preserve accurate partial work only if useful;
- identify the last fully verified completion commit;
- resume the SAME stage later.

## 12. Final bootstrap audit

After Stage 28 has individually passed and been committed, perform a separate end-to-end conformance audit.

Re-read the ORIGINAL bootstrap specification, accepted Stage 23 README amendment and all accepted progress receipts.

Build a complete matrix covering Stage 0 through Stage 28 and all global acceptance gates.

For every stage verify:

```text
required durable record exists
required deliverables exist
exact counts pass
required research/production was actually performed
required executions were actually performed
exit criteria pass
completion commit exists
remote verification exists
later stages did not improperly contradict accepted work
```

Also verify globally, where applicable:

- Advertising/Business Building boundary;
- professional advertising workflow;
- claims/proof discipline;
- audience/targeting separation;
- creative concept diversity and selection;
- cross-format adaptation;
- media/test contracts;
- destination continuity;
- experiment/measurement integrity;
- optimisation/fatigue learning;
- legal/policy handoffs;
- tool/provider boundaries;
- exact 15 primary examples and prompts;
- canonical stress tests;
- six canonical specifications;
- Extension Pack contract/catalogue and implemented pack evidence;
- actual core-vertical proof;
- progressive implementation coverage;
- benchmark/evaluation evidence;
- clean external installation;
- repository integrity;
- public README consistency;
- registry/Pactwright treatment;
- maturity claims.

If the final audit reveals any unresolved mandatory failure, the bootstrap is NOT COMPLETE.

Repair the owning stage and rerun affected downstream checks.

Do not raise or mark a PR ready, publish a release or claim final bootstrap completion until the final audit has zero unresolved mandatory failures.

## 13. PR and maturity rules

Do not:

- merge to `main`;
- mark a PR ready;
- promote registry maturity;
- publish a release;
- claim `working`;
- claim `benchmarked`;
- claim `mature`;

unless the corresponding demonstrated evidence exists and I have authorised the external action where required.

A large number of files, assets, prompts, tests or commits is not evidence of maturity.

Maturity follows demonstrated acceptance criteria only.

## 14. Governing execution sequence

For EVERY remaining stage:

```text
READ THE GOVERNING STAGE REQUIREMENT
        ↓
EXTRACT EVERY REQUIREMENT
        ↓
VERIFY PREREQUISITES
        ↓
STATE THE ACCEPTANCE CHECKLIST
        ↓
PERFORM THE REQUIRED RESEARCH / DESIGN / PRODUCTION / IMPLEMENTATION
        ↓
CREATE EVERY REQUIRED DELIVERABLE
        ↓
RE-READ THE GOVERNING REQUIREMENT
        ↓
VERIFY ACTUAL OUTPUT AGAINST EVERY REQUIREMENT
        ↓
FAIL? → REPAIR
BLOCKED / USER DECISION? → STOP AND ASK
        ↓
ALL PASS
        ↓
PERSIST CONFORMANCE EVIDENCE
        ↓
COMMIT ONLY THIS STAGE
        ↓
VERIFY REMOTE COMMIT AND FILE IDENTITIES
        ↓
REPORT COMPLETION
        ↓
ONLY THEN START THE NEXT STAGE
```

The most important rule is:

# COMPLETE EACH STAGE AS IF IT WERE THE ONLY TASK I ASKED YOU TO DO.

Do not optimise for the remaining bootstrap.

Do not preserve merely the “general intent”.

Follow the actual Advertising Production Skills bootstrap requirements literally and verify that you did so.

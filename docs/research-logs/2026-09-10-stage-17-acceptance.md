# Stage 17 acceptance and fixture correction

Date: 10 September 2026  
Stage acceptance: PASS  
Scope: canonical stress-test design, not installed-skill or campaign execution  
Working branch: `feat/bootstrap`  
Completion message: `docs: complete stage 17 canonical advertising stress tests`

## Authority and recovered state

Read this record together with the [Stage 17 design](2026-09-10-stage-17-canonical-advertising-stress-tests.md), published in `430bd8bdfe5fe0b64c8fc2a292899ac40d7024ba`, blob `b5b1aab0fd2bc534a7a5bdff7d5126d3a63a6840`. This record is the authoritative acceptance decision and corrects the FDE synthetic fixture only. The design's publication-BLOCKED row describes its earlier publication state; this acceptance record supersedes that row. Its Kakeibo and ecosystem prompts, source register, nineteen obligation pairs and six cross-contract cases remain unchanged. There are still three active base prompts, not four: use the replacement FDE prompt below instead of the historical FDE prompt.

The [original bootstrap](2026-09-08-advertising-production-skills-new-project-bootstrap-process.md) was reread from `main`, unchanged blob `f72a6f167595d6f178550fb1e02c4885d875b6b2`. Stage 17 and section 12 require the three named subjects and their specific concerns. Global commercial, evidence, actual-output, external-execution and preservation rules continue to apply. The execution attachment requires complete stage-only work and a remotely verified completion commit before Stage 18.

The recovered GitHub commit is a direct child of accepted Stage 16 `f170b1f4455f1adc2e1693ace9b512597ad2f8a7`; its tree is `ab7d58c7ce1d76ee38598b7a8297607faaeb4d21`. The complete 29-file map was read and its Git-tree hash independently reconstructed. All Stage 0–16 files retain their accepted identities. Stage 17 was published as a design record, not a completion commit. No reset, replacement branch, permission change or repeated earlier stage was needed.

## Substantive corrections

The full 246-line design was inspected, including all three prompts, eight source records, nineteen pairs, six cross-contract cases, alternatives and conformance. Two ambiguities in the FDE fixture needed repair before design acceptance.

First, cohort age was measured from lead entry, while the stated horizon started at qualification. Qualification timestamps were absent. Revision FDE-17@2 explicitly uses a 45-day **lead-entry-to-signing** observation horizon. The 60- and 45-day lead cohorts have reached that horizon; the 15- and 5-day cohorts have not. This does not establish that every qualified opportunity has had 45 days since qualification, nor supply event-level signing timestamps or revenue recognition.

Second, one cohort engagement was already delivered, but the earlier capacity sentence counted both signed cohort engagements in the next delivery window. Revision FDE-17@2 separates historical outcomes from outstanding commitments. C1's delivered engagement consumes no further hours. C2's undelivered engagement and a separately identified pre-existing engagement B0 consume eight hours each in the upcoming 16-hour window. B0 is outside the four reported lead cohorts and must not inflate their contact, qualification or signing totals.

This is an explicit revision of an assistant-authored synthetic fixture, not an assumption about the user's consultancy. It preserves the intended capacity stress, all four cohort counts, commercial terms, proof limits and existing positive/adverse cases. F05 now refers to the two outstanding commitments C2/B0, not two undelivered cohort sales. F06 uses lead-entry maturity. Future implementations must consume these corrected meanings; do not concatenate contradictory fixture text or silently reschedule C1.

## Complete replacement FDE prompt

```text
Use advertising-build, advertising-optimise and advertising-evaluate to design and review the one-person FDE consultancy stress test. Write local documents under production/advertising/stress-fde/. No real consultancy offer, price, case study, prospect list, calendar, spending authority or sales history is supplied. First record the specific facts and owners needed before a real campaign could be approved. Do not convert this synthetic business into the user's actual business.

SYNTHETIC FIXTURE FDE-17@2 only: one operator offers a read-only AI workflow reliability assessment to UK B2B software teams with an already deployed AI workflow. The fictional offer is GBP 2,400 one-off for an eight-hour assessment and a written findings report. It excludes implementation, production access, 24-hour support, security certification and guaranteed business outcomes. The upcoming fictional delivery window has 16 available delivery hours and no subcontractors. Discovery and sales work have a separate four-hour allowance; those hours are not delivery capacity. A method agenda supports the described process only. No testimonial, measured ROI, certification or named-client permission exists.

Qualification requires a deployed AI workflow, an in-scope problem, an identified decision contact and willingness to discuss the stated commercial terms. A form submission is not a qualified opportunity, sale or delivery. Keep the fixture segment separate from advertising hypotheses and platform representation; do not broaden it to students or job seekers to lower lead cost.

Four synthetic lead-entry cohorts contain 10 contacts each. C1 is 60 days old: 3 qualified opportunities, 1 signed engagement, already delivered. C2 is 45 days old: 2 qualified opportunities, 1 signed engagement, not yet delivered. C3 is 15 days old: 3 qualified opportunities, no signed engagement yet. C4 is 5 days old: 1 qualified opportunity, no signed engagement yet. The observation horizon is 45 elapsed days from lead entry to signing, not from qualification. C3 and C4 have not reached it. No individual qualification or signing timestamps, revenue receipts, delivery costs or causal assignment are supplied. Do not infer qualification-to-signing rates, exact within-horizon signing rates or recognised revenue from these aggregates.

The upcoming window has two outstanding commitments: C2's signed assessment, eight hours, and a separate pre-existing signed assessment B0, eight hours. B0 belongs to an earlier intake outside these four cohorts. C1's completed assessment consumes no upcoming hours. Do not add B0 to the four-cohort sales counts or book C1 again. No remaining delivery slot is available in that window without an explicit upstream change.

Produce the synthetic brief, two exact qualification-led ad drafts, a role/concern/proof map, a destination and enquiry-to-qualified-opportunity handoff, capacity reconciliation and cohort-aware readout. Propose the smallest appropriate next test without changing the offer, promising ROI or silently extending hours. A waitlist or later date remains a proposal until the responsible authority accepts it. Do not invent a calendar or message a prospect.

Return actual Markdown outputs, independent findings, missing evidence, scoped repairs and unchanged baseline facts. Do not authenticate to ad or CRM accounts, upload contacts, run paid generation, publish, place ads or spend. This is synthetic design and analysis, not a real commercial recommendation, observed pipeline or executed campaign.
```

## Conformance review

| Requirement | Governing reference | Inspected evidence and decision | Result |
|---|---|---|---|
| Three canonical subjects | Stage 17 / section 12 | Kakeibo, FDE and ecosystem each retain a source-aware contract, active full prompt, outputs and independent findings | PASS |
| Kakeibo's seven concerns | Section 12 Kakeibo | K01–K07 cover trust, subscription/refund, financial sensitivity, acquisition, claims, privacy/targeting and retained downstream quality; source-design versus shipped behaviour remains explicit | PASS |
| FDE's six concerns | Section 12 FDE | F01–F06 cover high-ticket B2B, narrow ICP, qualification, proof, capacity and delayed outcomes; @2 resolves horizon/backlog ambiguity without inventing real facts | PASS |
| Ecosystem concerns | Section 12 ecosystem | E01–E06 separately cover adoption, developer channels, education, services, marketplace and brand/performance; proposed offers remain proposed | PASS |
| Source and fixture boundaries | Sections 2–3 / Stage 16 exit | Eight source records retain exact scopes and pinned identities; missing real FDE data and licence/brand/implementation limits remain visible | PASS |
| Constructive and adverse behaviour | Sections 3/13 | Nineteen pairs and six cross-contract cases specify expected findings, responsible repair and preservation; each alternative mutation remains an implementation subcase obligation | PASS |
| Actual-output and authority boundaries | Sections 8/13/18 | Common run contract requires actual outputs and matched comparisons; synthetic approvals grant no external authority; no universal quality score | PASS |
| Durable acceptance and preservation | Execution attachment sections 7–9 | Recovered design, this authoritative correction, reproducible oracle check and progress index; completion tree preserves every other baseline file | PASS |
| Installed agent, media production, live campaign and Legal clearance | Stage 17 Design versus Stages 18/23–25 | No such execution is required or claimed for this stage | NOT APPLICABLE |

The current review adds executed arithmetic and fixture-consistency checks to the earlier manual review; it does not retroactively claim that the original document had an executable validator. The [oracle checker](2026-09-10-stage-17-oracle-check.py) uses synthetic inputs transcribed from the inspected three prompts, with the two explicit FDE corrections above. It checks refund rates, retained costs and contributions, backlog reconciliation, cohort-unit separation, maturity boundaries and installation ratios. Three deliberate wrong conclusions are also rejected. A missing behaviour in an installed skill cannot be detected by this arithmetic check and is not claimed to be tested.

Reproduce the oracle check from a checkout:

```bash
python3 docs/research-logs/2026-09-10-stage-17-oracle-check.py
```

The executed result is 20 checks passing, including three negative checks. The expected values are Kakeibo refund proportions 1/5 and 1/10, retained costs GBP 15 and GBP 12, contribution minus media GBP -280 and GBP -200; four-cohort FDE totals 40 contacts / 9 qualified / 2 signed / 1 delivered, two outstanding commitments consuming 16 hours, zero remaining slots, and only C1/C2 reaching the lead-entry observation horizon; ecosystem ratios 3/5 per attempt and 2/3 per verified installation. These are exact synthetic arithmetic, not measured advertising efficacy.

## Publication and next-stage input

Only this acceptance record, its oracle checker and the research index are added or changed in the completion commit. The original Stage 17 source/design is preserved as the historical revision to which this correction applies; every Stage 0–16 artefact is unchanged except the index's verified Stage 16 publication entry. Stage 18 must consume this acceptance record as well as the original design. No other stage's work belongs in this commit.

Before advancing, verify the non-forced branch update, direct parent `430bd8bdfe5fe0b64c8fc2a292899ac40d7024ba`, complete expected tree and all three intended blobs. This pre-commit record cannot contain its own final SHA; the exact completion message and Git history identify it. The earlier publication-BLOCKED finding is resolved only by that actual remote read-back.

The next-stage input is three source-aware contracts with three active prompts, nineteen obligation pairs with all stated alternative mutations retained, six cross-contract cases, the corrected FDE horizon/backlog rules, and independent arithmetic oracles. Stage 18 retains all twelve evaluation dimensions, fifteen primary examples, eight selected packs and their 48 condition/case executions. None of those runtime results is claimed by this design acceptance. Project maturity remains bootstrap research.

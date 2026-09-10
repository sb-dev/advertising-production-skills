# Stage 1: Advertising domain and cross-family boundaries

Date: 10 September 2026  
Stage acceptance: PASS  
Working branch: `feat/bootstrap`  
Completion commit message: `docs: complete stage 1 advertising domain boundaries`

## 1. Goal, authority and inspected inputs

Resolve ownership of campaign briefing, objectives, creative strategy, copy direction, media planning, targeting hypotheses, testing, measurement and optimisation, and the handoffs with all nine families named by Stage 1. This is a boundary decision record, not a campaign implementation, legal opinion or claim that the neighbouring families are installed.

The acceptance contract is [the original bootstrap](2026-09-08-advertising-production-skills-new-project-bootstrap-process.md), especially sections 1–3, 5, Stage 1 in section 6, and sections 8, 13, 18–20. It was read from `main` before work and reread for conformance. Baseline commit: `4a1d98843926c4aa0d68ed29ef55d9c8044dabe2`; bootstrap blob: `f72a6f167595d6f178550fb1e02c4885d875b6b2`.

### Clean-start and Stage 0 verification

The complete, non-truncated remote tree at the baseline contains exactly three files:

1. `README.md` (blob `5051a69cfefc65f62565fb8c1f58de1c32bdf88d`).
2. `docs/research-logs/README.md` (blob `cb085c731043ec0c8cf4a62df9561458f55e3bb4`).
3. The governing bootstrap named above.

Both READMEs and the entire bootstrap were inspected. The root README explicitly says bootstrap workspace. No skills, examples, packs, integrations, CI, package metadata or production implementation exists at this baseline. Stage 0 is already satisfied by the existing initial commit, so no artificial replacement Stage 0 commit is needed.

The remote branch listing initially contained `main` and `docs/stage-01-domain-boundaries`, but no `feat/bootstrap`. The latter was created directly from the verified baseline. A subsequent complete branch listing confirmed that `main` and `feat/bootstrap` both pointed to that exact SHA. The other branch was not opened, copied, merged or used as an implementation source. There are no earlier accepted design outputs on the working branch.

### Sources actually accessed

| ID | Source and inspected revision | Use | Limitation |
|---|---|---|---|
| S1 | [Advertising bootstrap on main](https://github.com/sb-dev/advertising-production-skills/blob/4a1d98843926c4aa0d68ed29ef55d9c8044dabe2/docs/research-logs/2026-09-08-advertising-production-skills-new-project-bootstrap-process.md), blob `f72a6f167595d6f178550fb1e02c4885d875b6b2` | Governing ownership, safety, sequencing and acceptance | Describes intended capabilities; does not prove an implementation or supply campaign approvals |
| S2 | [Production Skills family README](https://github.com/sb-dev/production-skills/blob/main/README.md), blob `5b416f77c479ca6f484b91c6283237dd034f827e` | Independent domain repositories, consuming-project ownership, advertising position, planned-family distinctions | Family positioning, not evidence that every named family can execute today |
| S3 | [Cross-domain orchestration specification](https://github.com/sb-dev/production-skills/blob/main/docs/specs/04-cross-domain-orchestration-and-integration.md), version 1.1, blob `2be3cdecaf8e326d1c1076bb6044d60bbbe14616` | Handoff ownership, optional Pactwright, reproducibility and separate evaluation | Generic composition contract; does not dictate an advertising artefact schema |

All three were accessed through the GitHub connector on 10 September 2026. The supplied execution prompt is the execution-control input. No external advertising-practice finding, legal rule, platform policy or campaign result is asserted in this stage. Professional-practice research belongs to Stage 2; current legal/platform research belongs to its designated stages. The decisions below are project design decisions derived from S1, with S2/S3 used for compatibility rather than overriding S1.

## 2. Acceptance checklist extracted before production

| ID | Completion requirement | Governing reference |
|---|---|---|
| B01 | Verify clean workspace and branch provenance; preserve the original specification | Section 5; execution prompt clean-start and prerequisite rules |
| B02 | Resolve campaign briefing and objectives, keeping approved business choices upstream | Stage 1; sections 1–3 |
| B03 | Resolve creative strategy and copy direction without absorbing specialist asset craft | Stage 1; sections 2–3 and 8 |
| B04 | Resolve media planning and targeting hypotheses without autonomous spend or customer redefinition | Stage 1; sections 2–3 and 8 |
| B05 | Resolve testing, measurement and optimisation without manufacturing results or privileging vanity metrics | Stage 1; sections 3, 8 and 13 |
| B06 | Define each of the nine named cross-family handoffs, including input, returned output, authority and rejection path | Stage 1; section 2 |
| B07 | Separate campaign reasoning from administration, rendering, upload, serving, tracking, attribution computation and hosting | Section 8 |
| B08 | Preserve substantiation, approval, controlled variation, destination consistency and smallest responsible repair | Section 3; section 13 |
| B09 | Keep Pactwright optional and lifecycle authority external; keep consuming-project instances external | Section 18; S3 sections 2, 4, 8 and 14 |
| B10 | Reject the prohibited universal marketing/platform interpretations | Sections 8 and 19 |
| B11 | Persist decisions, rejected alternatives, verification, conformance and stage-only progress; no premature scaffold | Section 5; execution prompt research-log, verification and commit rules |

Required inputs are S1 and the verified Stage 0 workspace; S2/S3 are supporting compatibility evidence. There is no required candidate-pool size, asset count, campaign-variant count, prompt count, pack count, benchmark execution, installation or software test in Stage 1. Those categories are NOT APPLICABLE here because the bootstrap assigns practice research to Stage 2, domain models to Stages 3–10, skill/pack/example/eval design to Stages 14–18 and implementation to Stages 22–25. This exemption does not reduce any requirement in those stages. There is no user-owned campaign decision to resolve to complete this domain boundary stage.

## 3. Domain identity and terminology

Advertising Production owns the reusable judgement needed to turn approved commercial intent into coherent, testable campaign work. It is neither an ad-prompt catalogue nor an autonomous marketing department. The consuming project owns each real campaign, its evidence, decisions, assets and results; this repository owns reusable skills, research, examples and evaluation methods.

The business objective describes the commercial outcome and constraints; the campaign objective describes the change advertising is intended to cause within those constraints. The approved business segment, a proposed advertising audience hypothesis and a platform targeting representation are distinct objects. The first is not silently replaced by the second or third.

The offer is the approved commercial exchange. A proposition is the advertising's intended value emphasis. A claim is an assertion needing the applicable evidence and review. Proof is the supporting material with provenance and scope, not merely a persuasive way of expressing the claim. A message organises what is communicated; a concept is a creative route for communicating it. Creative direction guides execution; copy, visual and audio executions express it. A channel, placement and format constrain an execution but do not define the underlying business proposition.

A variant has identifiable changes from a parent. A production asset is an actual output, not the prompt, storyboard or promise to produce it. Approval is an attributable decision with a scope, not inferred consent. A delivery specification describes what an external executor must receive. Performance evidence records observations and their limitations. Diagnosis identifies the supported failure layer. Repair changes that layer while preserving unaffected approved work. These distinctions prevent a wording improvement from silently becoming a new offer, audience, product claim or spending decision.

## 4. Advertising responsibility matrix

| Responsibility | Advertising owns | Inputs it must preserve | Boundary and return path |
|---|---|---|---|
| Campaign briefing | Translate approved commercial intent into a coherent campaign question, constraints and required outputs | Offer, price, approved segment, business objective, economics, brand and evidence provenance | Incomplete or conflicting commercial inputs return to Business Building/project owner; Advertising does not invent approval |
| Objectives | Define what advertising should change and how its contribution will be assessed | Business outcome, capacity and downstream value constraints | Changing the business objective or declaring paid advertising justified returns upstream |
| Creative strategy | Message priorities, creative hypotheses, territories, concept alternatives and cheapest useful representations | Approved proposition boundaries, claims, proof, brand and audience evidence | Specialist craft is commissioned with a bounded brief; a concept cannot authorise a stronger claim |
| Copy direction | Advertising hierarchy, hooks, angles, CTA intent, draft copy and placement adaptation | Product truth, qualifications, commercial terms and approved claims | Narrative provides specialist storytelling/copy craft when needed; Advertising retains campaign-fit review, not unilateral legal approval |
| Media planning | Campaign-level channel/placement roles, staged budget proposals, context and allocation reasoning | Business-wide channel class, authorised ceiling, schedule and economics | New channel strategy or budget authority returns to Business Building/project owner; tools perform authorised account changes |
| Targeting hypotheses | Evidence-backed hypotheses within the approved customer boundary, plus requested platform representation | Approved segment, lawful/authorised data constraints and exclusion requirements | Unsupported identity inference or segment expansion is rejected; data access and audience upload remain external |
| Testing | Hypotheses, deliberate contrasts, comparison logic, guardrails and decision questions | Measurement feasibility, approvals and business constraints | Running spend-bearing experiments needs separate authority; external execution does not validate the design automatically |
| Measurement | Specify information needed and interpret observed platform and downstream evidence separately | Event meanings, provenance, uncertainty, timing and contribution economics | Software/analytics systems collect data and compute attribution; Advertising cannot repair missing evidence by inventing it |
| Optimisation | Diagnose delivery, audience, creative, placement, destination, policy or business failure; preserve learning and propose bounded repair | Winning/approved work, experiment validity, evidence and budget constraints | Repair outside the advertising remit is handed to its owner; clicks alone do not justify harmful scale or commercial changes |

Advertising may create text-only campaign artefacts directly. It is not required to delegate every headline to Narrative. Delegation depends on specialist craft, fidelity and delivery needs, not a rule that Advertising cannot write. Conversely, access to image/video/audio tools does not transfer their craft responsibilities or prove a generated asset was evaluated.

## 5. Nine cross-family contracts

Each handoff identifies the producer and consumer, the required inputs, the expected returned artefact/evidence, the owner of changes and the integration acceptance responsibility. Markdown is sufficient; this stage does not impose a shared runtime or universal schema. Missing execution capability does not justify pretending a handoff ran.

| Family | Inputs or request crossing the boundary | Returned output and acceptance | Decision authority and rejection route |
|---|---|---|---|
| Business Building | Approved offer, price, target customer, acquisition objective, channel class, economics, capacity and growth constraint enter Advertising. Advertising returns campaign learning and evidence of upstream problems | Campaign brief must remain traceable to those inputs; downstream evaluation must distinguish qualified response and business value from ad metrics | Business Building/project owner controls offer, price, commercial segment and business-wide acquisition choices. Advertising proposes, but does not apply, upstream changes |
| Deep Research | Bounded questions about audience/context/competition/claims, existing evidence and the decision the research must inform | Source-backed findings with provenance, limitations, contradictory evidence and unresolved questions; Advertising checks relevance to the specific campaign claim or hypothesis | Deep Research owns research method and source assessment, not commercial approval or legal conclusions. Insufficient research returns for clarification or further evidence rather than becoming customer truth |
| Legal | Exact proposed claim/execution, substantiation, product/offer facts, audience/targeting method, placement, jurisdiction and policy context | Legal findings, constraints, qualifications, escalation or unresolved issues tied to the supplied facts; Advertising checks that returned constraints are actually represented in campaign work | Legal owns legal conclusions. Advertising owns faithful implementation and can block a path pending review; it cannot grant legal clearance or treat platform acceptance as legal approval |
| Narrative | Campaign objective, message/claim/proof boundaries, audience context, selected concept or alternatives, brand voice, CTA and required representation | Story/copy/script treatment with preserved claims, rationale and source/rights information where relevant; Advertising assesses campaign and destination consistency | Narrative owns specialist narrative craft. Advertising owns campaign integration. Neither may change offer or legal constraints; requested changes crossing those boundaries return to the relevant owner |
| Video | Concept, script/message, visual direction, placement requirements, allowed claims, qualifications and fidelity/approval state | Required rough or final moving-image artefact, production provenance and craft evaluation; Advertising examines the actual output for message, claim, placement and CTA fit | Video owns motion/production craft and repair within the brief. Advertising cannot call a storyboard a finished advertisement or infer publication approval from generation |
| Audio | Message/script intent, brand/audience context, placement, voice/music/sound needs, qualifications, rights constraints and fidelity | Audio concept or actual audio asset at the requested fidelity, provenance and evaluation; Advertising assesses intelligibility of the advertising message and required disclosures in the delivered output | Audio owns sound/voice/music craft; rights/legal questions remain specialist decisions. The family README describes a combined Audio direction, not proof that a combined executor is installed |
| UIUX | Ad-to-destination message, offer, price, claims, proof, CTA, accessibility and disclosure requirements | Destination design/content/interaction and continuity evidence; Advertising reviews the ad journey against the approved promise | UIUX owns experience design; Advertising owns continuity requirements. New commercial terms return upstream. Implementation is not assumed merely because a design exists |
| Software Engineering | Approved destination design and behaviour, tracking/event requirements, integration/security constraints and required verification | Implemented destination/integration, instrumentation and technical test evidence from its owner; Advertising evaluates whether the evidence supports the campaign measurement/continuity need | Software Engineering owns implementation, hosting/instrumentation integration and technical repairs. Advertising does not build a CRM, tracking stack or attribution engine in its skills repository |
| Pactwright | Optional authorised Contract and responsibility scope enter the composed production run; Advertising returns artefacts, evaluations, blockers and bounded recommendations | Traceable evidence of the assigned advertising responsibility, identifying skill revisions and selected packs when used | Pactwright owns lifecycle, Contracts, graph semantics and orchestration acceptance. Advertising owns domain evaluation. Ordinary Advertising operation must not require Pactwright |

A real handoff instance, its approvals, third-party account credentials, private customer data and commercial results belong to the consuming project or authorised execution system. Reusable contracts and explicitly synthetic fixtures belong here. No account or campaign was accessed or changed during this stage.

## 6. External execution and approval boundaries

Advertising owns reasoning and requests; external systems own account administration, asset rendering, campaign upload, bidding/spend, ad serving, data collection, conversion tracking, attribution computation and hosting (S1 section 8). A media plan is not a live campaign. A proposed budget is not spending authority. Credentials are capability, not consent. This stage chooses no provider, vendor, account or integration implementation; those decisions belong to Stages 11–12.

Keep the following authorities separate: business-input approval; brand/creative selection; substantiation and permitted-claim review; legal/regulatory review; production acceptance at a specified fidelity; publication/spend authorisation. A decision authorises only its recorded scope. Creative selection does not legalise a claim, approve every later variant or authorise spend. A legal review does not certify creative quality, campaign effectiveness or business viability. A skill may evaluate evidence and identify a blocker without claiming to be a human approver.

Approved work is preserved by identifying which decision, artefact and scope a proposed change affects. A changed price, claim, audience boundary or material disclosure cannot inherit approval from an unrelated creative decision. A requested change is returned to its owner before commitment. The detailed state/artefact models remain for their respective later stages.

## 7. Diagnosis and smallest responsible repair boundary

| Suspected layer | Evidence question before repair | Owner and bounded response |
|---|---|---|
| Delivery | Was the approved campaign actually served as intended, and is the observation trustworthy? | External ad operations/execution repairs authorised delivery; do not rewrite creative to compensate for a broken upload |
| Audience | Is there evidence against the advertising hypothesis, or is qualification being measured incorrectly? | Advertising revises the hypothesis inside approved bounds; changes to the commercial segment return to Business Building |
| Creative | Does the observed execution communicate the supported proposition in context? | Advertising corrects message/concept or requests a specific specialist asset repair while preserving unaffected approvals |
| Placement | Is context, format or allocation mismatched to the creative/test? | Advertising proposes a placement-level change; authorised execution performs account changes |
| Destination | Does the landing experience honour the advertised promise and record the intended event? | UIUX/Software Engineering repairs the relevant experience/implementation; offer changes remain upstream |
| Policy/claims | Is a claim unsupported, context stale, or a constraint unmet? | Block the affected execution and obtain the evidence/legal/policy decision; persuasion is not a repair for missing substantiation |
| Upstream business | Does qualified response reveal an offer, economics or capacity problem? | Business Building/project owner evaluates the commercial correction; Advertising preserves the evidence and does not optimise around the constraint covertly |

These are ownership tests, not a premature statistical diagnosis engine or live-performance claim. A hypothesis of fatigue is not a verified finding. Platform-reported conversion and verified downstream value remain separate evidence categories.

## 8. Alternatives considered and rejected

| Alternative | Decision and reason |
|---|---|
| Own all marketing from customer discovery to CRM and spend | REJECT: conflicts with S1 sections 2, 8 and 19; erases commercial/execution authority |
| Limit the repository to isolated ad prompts | REJECT: cannot own coherent briefs, proof, controlled tests, diagnosis and learning required by S1 sections 1 and 3 |
| Let specialists own campaign strategy whenever they render the asset | REJECT: craft execution must preserve the advertising message/claim contract; rendering capability is not campaign authority |
| Require every piece of copy to be delegated | REJECT: unnecessary orchestration; Advertising owns copy direction and can produce bounded text while using specialist craft when needed |
| Make Advertising its own legal-compliance authority | REJECT: explicitly conflicts with Legal ownership and truthful-claim requirements |
| Treat platforms as interchangeable through a universal advertising API | REJECT: premature infrastructure and an execution-boundary violation; platform-specific capabilities will be researched separately |
| Make Pactwright mandatory or copy its lifecycle into this repository | REJECT: conflicts with optional composition and domain/lifecycle separation |
| Put live campaigns and consumer project specifications in the central family repository | REJECT: S2/S3 assign these to the consuming project |
| Adopt documented domain-native handoffs with external execution | SELECT: preserves required advertising expertise and explicit responsibility without building new infrastructure |

## 9. Verification performed

The original Stage 1 section and applicable global principles were reread, then this record was inspected against them. This was a substantive document/contract review, not an executed software benchmark. Nine advertising responsibility rows and nine named family rows were counted and inspected individually. The seven-layer repair table was checked against the governing smallest-responsible-layer principle.

Manual boundary checks actually performed:

| Review case (synthetic reasoning scenario, not a campaign execution) | Observed decision in this record | Result |
|---|---|---|
| Improve CTR by reducing the approved price | Sections 4–6 route the commercial change upstream; no silent edit | PASS |
| Invent a testimonial to strengthen a concept | Sections 3, 5 and 6 require proof/claim authority; the execution path is blocked | PASS |
| Narrow a permitted advertising hypothesis versus redefine the business segment | Sections 3–5 distinguish the objects and their owners | PASS |
| Render video from an approved script | Sections 5–6 require the actual artefact and separate production/publication authority | PASS |
| Treat a high platform-conversion count as proven business value | Sections 4 and 7 retain separate downstream evidence and business constraints | PASS |
| Repair an unrecorded conversion by rewriting the ad | Sections 5 and 7 route instrumentation repair to Software Engineering rather than creative | PASS |
| Run without Pactwright | Section 5 explicitly permits independent Advertising operation | PASS |
| Interpret a media-plan approval as live-spend authority | Section 6 explicitly prohibits that inference | PASS |
| Claim combined Audio is installed because the family direction names it | Section 5 and source limitations explicitly prohibit that maturity inference | PASS |

### Conformance table

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| Clean start, Stage 0 and original preserved | Section 5; execution prompt | Section 1; original three remote file hashes; branch listing | Inspected full tree, both READMEs, bootstrap and branch SHA; no prior branch read | PASS |
| Campaign briefing | Stage 1 | Section 4 row 1; Business Building handoff | Checked approved-input and missing-input paths | PASS |
| Objectives | Stage 1; sections 2–3 | Section 4 row 2 | Checked business/campaign distinction and upstream authority | PASS |
| Creative strategy | Stage 1; section 3 | Section 4 row 3; specialist handoffs | Checked concept/craft distinction and cheap representation | PASS |
| Copy direction | Stage 1 | Section 4 row 4; Narrative handoff | Checked direct text work, specialist craft and claim constraints | PASS |
| Media planning | Stage 1; sections 2 and 8 | Section 4 row 5; section 6 | Checked campaign/business/execution separation | PASS |
| Targeting hypotheses | Stage 1; section 3 | Sections 3–5 | Checked segment, hypothesis and platform representation remain distinct | PASS |
| Testing | Stage 1; section 3 | Section 4 row 7 | Checked controlled contrasts and separate spend authority | PASS |
| Measurement | Stage 1; sections 3 and 8 | Section 4 row 8; section 7 | Checked interpretation versus collection/computation and downstream evidence | PASS |
| Optimisation | Stage 1; section 3 | Section 4 row 9; section 7 | Inspected all seven repair ownership paths and preservation rule | PASS |
| Business Building handoff | Stage 1 | Section 5 row 1 | Checked input, output, authority and rejection route | PASS |
| Deep Research handoff | Stage 1 | Section 5 row 2 | Checked evidence provenance and no invented customer truth | PASS |
| Legal handoff | Stage 1 | Section 5 row 3 | Checked exact facts/claims, constraints and legal decision ownership | PASS |
| Narrative handoff | Stage 1 | Section 5 row 4 | Checked bounded craft request and integration acceptance | PASS |
| Video handoff | Stage 1 | Section 5 row 5 | Checked requested fidelity, actual asset and evaluation distinction | PASS |
| Audio handoff | Stage 1 | Section 5 row 6 | Checked craft, rights and capability limitations | PASS |
| UIUX handoff | Stage 1 | Section 5 row 7 | Checked destination consistency and design/implementation distinction | PASS |
| Software Engineering handoff | Stage 1 | Section 5 row 8 | Checked technical ownership and infrastructure exclusions | PASS |
| Pactwright handoff | Stage 1; section 18 | Section 5 row 9 | Checked optionality, lifecycle authority and separate domain evidence | PASS |
| Evidence, approval and truthful work | Sections 3 and 13 | Sections 3, 5–7 | Reviewed unsupported-claim, price and approval counterexamples | PASS |
| External execution and non-goals | Sections 8 and 19 | Sections 6 and 8 | Checked every listed external execution category and rejected expansion | PASS |
| Stage-only outputs and durable evidence | Section 5; execution prompt | This log and research-log index | Reviewed changed-path allowlist, internal links and conformance; no scaffold | PASS |
| Assets, prompts, packs, benchmarks and installation | Stage 1 versus Stages 14–25 | Section 2 applicability statement | Confirmed these are not Stage 1 deliverables; no execution claimed | NOT APPLICABLE |

## 10. Exit assessment and next-stage input

All mandatory Stage 1 content requirements pass. No unresolved user decision, mandatory missing source, failed prerequisite or proposed waiver remains. No business input, legal clearance, production approval, generated asset, benchmark result or campaign performance was fabricated.

The only stage changes are this complete research log and its entry/progress record in `docs/research-logs/README.md`. The original bootstrap and root README remain unchanged. Publication must be followed by remote branch-SHA and intended-file verification before Stage 2 begins. The stage completion commit is discoverable by the exact commit message above and this file's history; its own SHA is not embedded recursively in its contents.

Stage 2 consumes the ownership matrix, nine family contracts, approval separation, repair routing and rejected alternatives. It must research the full professional-practice list in the original specification. Detailed campaign models, provider decisions, skills, packs, example selection, eval architecture, six canonical specifications and production implementation remain in their explicitly assigned later stages, not unfulfilled Stage 1 work.

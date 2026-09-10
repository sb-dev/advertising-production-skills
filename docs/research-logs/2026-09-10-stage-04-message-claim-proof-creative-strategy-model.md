# Stage 4: Message, claim, proof and creative strategy model

Date: 10 September 2026  
Stage acceptance: PASS  
Working branch: `feat/bootstrap`  
Completion commit message: `docs: complete stage 4 message claim proof and creative strategy model`

## 1. Authority and accepted inputs

This stage defines how a bounded advertising brief becomes an evidence-linked message and creative strategy. It does not choose or approve a real campaign, generate final assets, run an experiment or grant legal/publication/spend authority.

The governing [original bootstrap][Bootstrap] was reread in full from `main` before work. Authority: section 6, Stage 4, together with global sections 1–3, 5, 8, 13 and 18–20. Its original blob remains `f72a6f167595d6f178550fb1e02c4885d875b6b2` on clean baseline `4a1d98843926c4aa0d68ed29ef55d9c8044dabe2`.

The immediate prerequisite is accepted [Stage 3][Stage3], commit `c7bbdf7704cfd9edf41dc419c322066fcd997bee`, parent `5efd2006ceae24aef4458575fe73f16a608e273d`, tree `8fa66b580c68720d29ee94b6b5b626ef8ae4c48c`, model blob `4f0881b53397ec1229fd882d77c2f4a5671f2aa8`. Its remote head, parent, complete tree and intended content hashes were verified before this stage began.

Relevant accepted content was reread from `feat/bootstrap`: Stage 3's header, provenance, 13 brief areas, audience distinctions, objective mapping, scoped readiness and handoffs; [Stage 1][Stage1] terminology, responsibilities, nine handoffs and separate authorities; [Stage 2][Stage2] P02–P06 on strategy, copy, art, brand and direct response. The previously inspected Stage 2 [source register][Sources] remains the provenance for its findings. Only the material actually accessed in that record is relied upon; this stage does not claim new platform/legal research or access to full reports behind its public summaries.

The definitions and checks below are original project design decisions derived from those inputs. Their semantics do not assert that any messaging technique will improve performance. Consumer behaviour, product truth, source rights and real approvals must be evidenced in the consuming project.

## 2. Acceptance checklist and applicability

| ID | Required deliverable | Original reference |
|---|---|---|
| M01 | Message hierarchy, with explicit message hypotheses and priorities | Stage 4: message hierarchy |
| M02 | Claim inventory, including intended and plausible implied meanings | Stage 4: claim inventory |
| M03 | Proof inventory, with provenance, support limits and permitted use | Stage 4: proof inventory |
| M04 | Objection map, evidence status, response and limitation handling | Stage 4: objection map |
| M05 | Creative territories, meaningful alternatives and inexpensive representations | Stage 4: creative territories; section 3 |
| M06 | Hook/angle matrix, traceable cells and controlled variation | Stage 4: hook/angle matrix; section 3 |
| M07 | CTA architecture, priority, commitment and destination continuity | Stage 4: CTA architecture; section 3 |
| M08 | Creative hypotheses, mechanism, contrast, uncertainty and evaluation handoff | Stage 4: creative hypotheses |
| R01 | Preserve all six nodes and typed links of the required evidence-to-adaptation chain | Stage 4 preserved chain |
| G01 | Preserve approved brief, commercial inputs, audience boundaries and ownership | Sections 2–3; Stage 3 |
| G02 | Separate evidence, authority, selection and execution; never manufacture proof | Sections 3/8/13/18 |
| G03 | Cheapest useful fidelity, meaningful variation, preservation and bounded repair | Sections 3/13 |
| G04 | Compare approaches and reject premature infrastructure and universal quality scoring | Sections 5/8/13/19 |
| G05 | Complete substantive/structural verification, durable evidence and stage-only publication | Execution prompt sections 7–9 |

Every model must state its meaning, minimum record content, dependencies, owner/decision and failure/repair behaviour. Verification must check the preserved chain, not just the presence of eight headings. This stage independently analyses representation choices, approval scope, evidence gaps, creative selection, cross-format semantic risks and repair ownership.

The exact mandated coverage is eight components and six chain nodes. No fixed source count, candidate pool, campaign-concept/variant count, generated asset, example prompt, pack, installed skill, software benchmark or live experiment is required in Stage 4. Those categories are NOT APPLICABLE here, not waived for later stages. Stage 5 owns the full production/adaptation model, 6 media, 7 destination handoffs, 8 test/measurement, 9 learning and 10 legal/policy context. Stages 14–18, 19 and 22–25 retain their skill/example/eval, canonical-specification and implementation requirements.

A generic definition can be complete while a particular campaign's proof, approval or destination remains unavailable. The model must identify the dependent blocked action; it must not invent the missing input or disguise it as a creative choice.

## 3. Shared semantics and ownership

Reuse Stage 3's stable identities/revisions, `real`/`synthetic` context, source/knowledge/validity, scoped use decisions and unresolved-issue records. Do not introduce a competing approval framework. A strategy can be one readable Markdown file with linked tables; eight logical components do not require eight files, agents or services. Real instance data and restricted evidence remain in the consuming project.

| Term | Meaning and boundary |
|---|---|
| Offer | The approved commercial exchange, not a creative proposition; owned upstream |
| Audience hypothesis | Stage 3's evidence-linked proposition about authorised recipients/context; not the message itself |
| Message hypothesis | A proposal about what meaning or value emphasis may matter to that audience and objective; not a discovered fact about effectiveness |
| Claim | An explicit or implied assertion that requires support appropriate to its meaning and context; rhetorical form does not erase factual implication |
| Proof | Supporting evidence with provenance, scope, limitations and appropriate assessment; not a persuasive-looking asset |
| Proof presentation | The permitted audience-facing way of showing or explaining that evidence; it can make proof understandable but cannot strengthen the underlying evidence |
| Objection | An observed or hypothesised concern, question, friction or reason not to act; it need not be something advertising should overcome |
| Territory | A strategic creative route or organising mechanism capable of yielding concepts; not a colour palette or ad size |
| Concept | A particular communicable idea within a territory; distinct from its final execution or cosmetic variant |
| Angle / hook | Angle is the selected perspective or emphasis; hook is the opening expression used to gain relevant attention |
| CTA | The intended next action and its user commitment, not merely button wording |
| Creative hypothesis | A proposition about how a particular expression/mechanism may advance a message and objective in context; not its validation result |

Advertising owns message/creative reasoning, evidence-to-claim mapping, integration and domain evaluation. Business/product owners own commercial truth and changes to offer/price/segment/economics. Research supplies attributable findings and limitations. Legal owns legal conclusions. Narrative/Video/Audio and other specialists own craft when commissioned; UIUX/Software Engineering own destination/technical work. A role may be fulfilled by the same person, but their decision authority remains explicit. [Stage1]

Claim support, permission to use evidence, permission to express a claim, creative selection, production acceptance, publication and spending are separate decisions. Record which one is being made about which revision and scope. A selected concept cannot authorise an unsupported claim, while a well-supported claim can still be unhelpful or badly expressed. Neither problem is repaired by blending all judgements into one quality score.

## 4. Required strategy models

### M01. Message hierarchy

**Definition.** Organise what the audience should understand, associate or do, in priority order, while keeping the commercial offer intact. The hierarchy distinguishes the primary message, supporting reasons, relevant proof, material qualifications and intended action. It is not a requirement to fit every possible talking point into every placement.

**Minimum record.** Message ID/revision; parent brief/objective and audience-hypothesis references; message hypothesis and rationale; primary intended takeaway; supporting messages and their priority; linked claim/proof/objection/CTA IDs; mandatory meaning/qualification dependencies; permitted omissions by scope; brand constraints; unknowns and decision status. A primary message needs a reason tied to the objective, not merely a memorable sentence.

**Dependencies and decisions.** Business/customer evidence informs the message hypothesis. Product/offer evidence supports factual assertions within it; audience interest does not prove product performance. Advertising proposes the hierarchy and the authorised campaign/brand owner accepts the relevant scope. Existing offer and audience approvals remain unchanged. Multiple audiences can require different priorities, each traceable to its own authorised hypothesis rather than a silent customer redefinition.

**Failure and repair.** Conflicting top-priority messages, unsupported promises or an action unrelated to the objective require a message-level repair. A mandatory qualification is not a low-priority message that can be removed for space. A short execution may omit a supporting topic only when the remaining meaning stays truthful and coherent; otherwise choose a narrower supported assertion or a different treatment. Preserve unaffected messages and their approvals.

### M02. Claim inventory

**Definition.** Capture the assertions a reasonable interpretation of the proposed communication could convey, including text, imagery, sequence, sound, comparisons, demonstrations, testimonials and omissions. A question, visual metaphor or subjective-sounding slogan can imply a factual assertion; treating it as “creative” does not exempt it from review. This is a project review rule, not a blanket legal classification.

**Minimum record.** Claim ID/revision; exact proposed assertion and intended meaning; plausible materially different implications to review; claim type and subject; product/offer/version, population, market, period and conditions; quantity/unit/comparator/baseline where present; linked message and source records; required proof and actual evidence IDs; support assessment and limitations; qualifications; evidence owner; use/claim review decisions and affected expressions. Split independently supportable parts of a compound assertion, then review the meaning created when they appear together.

**Dependencies and decisions.** The brief's intake inventory is the starting point, not a fresh editable product-truth store. Support assessment asks whether the evidence actually bears on the proposed scope, comparison and strength. Relevant expert/Legal review remains necessary where applicable; the Advertising skill does not grant legal clearance. The inventory retains blocked, rejected or superseded assertions with their reasons to prevent their unintentional regeneration.

**Failure and repair.** Missing evidence, stale scope, unsupported comparisons, invented endorsements or stronger implications block the dependent expression. Repair the exact assertion, obtain the required evidence/review or remove the unsupported dependency. Replacing “will” with “could” is not an automatic cure for a misleading promise. Evidence for one narrow outcome cannot be stretched to a stronger or more general benefit merely because the wording is attractive.

### M03. Proof inventory

**Definition.** Record the actual evidence available to support claims, separately from how the creative proposes to present it. Evidence can include attributable product/offer records, properly scoped research, measurements, demonstrations, certifications or genuine authorised testimonials when they exist. None is universally sufficient for every claim; adequacy is evaluated against the particular assertion.

**Minimum record.** Proof ID/revision; source location/version and retrievable passage or artefact; producer/owner; evidence type and collection/method context; subject/product/population/market/period; relevant finding or fact; uncertainty, exclusions and contradictory material; validity/review trigger; authenticity and integrity evidence available; access/rights/use restrictions; claims it supports and does not support; assessment owner/status; permitted presentation and any disclosure conditions. A proof request with no supplied material remains an explicit gap, not a proof item marked complete.

**Dependencies and decisions.** Maintain a claim-to-proof relationship with the reason each link is adequate, partial, incompatible, unverified or obsolete for its scope. One source may support several claims, and one claim may need several sources. The existence of several agreeing outputs is not independent corroboration when they all derive from the same underlying source. Source-access and confidentiality constraints may require a specialist to review private material without publishing it here.

**Failure and repair.** A generated screenshot, synthetic customer quote, mock award badge, reconstructed chart or illustrative product demonstration is not evidence of a real product result. Such material may be explicitly illustrative when permitted, but cannot be presented as independent proof. A proof presentation must not omit denominators, conditions, dates or limitations that materially change meaning. Repair the presentation or claim at its responsible layer; neither a polished render nor source-owner permission improves the evidential basis.

### M04. Objection map

**Definition.** Map reasons the intended audience might hesitate, misunderstand, question relevance or decide not to act. Distinguish a documented objection from an inferred concern and a speculative research question. The goal is a truthful, useful response, not automatic rebuttal or pressure.

**Minimum record.** Objection ID/revision; exact concern in attributable language or clearly labelled paraphrase/hypothesis; source/knowledge basis; affected audience/context and decision; evidence strength/limitations; relationship to offer, message or destination; current truthful response; supporting claim/proof; unanswered dependency; appropriate response route and owner; priority rationale and review outcome. Frequency or importance must not be invented from a single anecdote or an AI-generated persona.

**Dependencies and decisions.** Advertising can clarify a misunderstanding or make existing evidence more accessible. A real product limitation, unaffordable price, unsuitable audience or inadequate capacity may require acknowledgement, qualification or referral to Business Building rather than persuasive copy. Legal questions go to Legal; implementation friction goes to the destination owner. A business owner, not Advertising, decides whether an objection justifies changing the exchange.

**Failure and repair.** Do not create a false scarcity claim, hidden discount, testimonial or unsupported guarantee to answer a concern. Do not present an inferred vulnerability as audience truth or use it to override informed choice. If no truthful response exists, retain the limitation and affected blocked claim/action. An unanswered question can motivate research; it cannot become evidence that the proposed creative solved it.

### M05. Creative territories

**Definition.** Describe genuinely different organising routes for expressing the accepted message. Differences should concern the communication mechanism, perspective, narrative structure or role of proof, not only colour, format, headline punctuation or production polish. A territory can produce multiple concepts and each concept multiple treatments; these are linked but distinct decisions.

**Minimum record.** Territory ID/revision and plain-language thesis; parent message/audience/objective; communication mechanism; evidence and permitted-claim dependencies; candidate concept descriptions; brand fit and exclusions; context assumptions; cheapest useful representation; unresolved risks and production dependencies; alternative territory comparison; selection/rejection/defer decision with authority and rationale. State the intended takeaway and what the viewer/listener would actually encounter, rather than supplying only an evocative theme name.

**Dependencies and decisions.** Start from accepted message/proof boundaries. Explore a useful range of mechanisms appropriate to the decision; no universal territory count is imposed by this stage. Choose fidelity by uncertainty: a text description, rough sequence or layout can expose the idea before commissioning craft. Advertising owns campaign integration; specialists may help establish production feasibility without receiving authority to change the proposition.

**Failure and repair.** If a route depends on unavailable proof or a deceptive implication, block that route rather than authorise fabrication. If alternatives are merely reskins, identify the actual changed dimension and either treat them as execution variants or explore another mechanism. Selection records what must remain fixed and what is open for treatment-level change. An unresolved craft detail should not erase an accepted strategic idea unless it makes the idea infeasible.

### M06. Hook/angle matrix

**Definition.** Cross the message perspectives worth exploring with alternative opening expressions, while preserving claim/proof/CTA dependencies. An angle defines the emphasis; a hook implements the opening. Neither is automatically a new strategy, and a persuasive hook is not a result.

**Minimum record.** Angle ID and audience/message rationale; hook ID and expression/sequence description; cell/variant ID; parent territory/concept; exact claim/proof/qualification links; intended context/format; CTA reference; fixed and changed dimensions; cheapest representation; evaluation question; prohibited combinations; decision status and unresolved dependencies. Store the actual text or an actionable representation, not only labels such as “emotional hook”.

**Dependencies and decisions.** A matrix is a selection aid, not an instruction to produce every Cartesian combination. Reject cells that cannot truthfully express the message in context. When preparing a narrow test, make the changed dimension explicit and retain stable offer, audience, claim meaning and other controls as appropriate. A comparison of complete systems is permitted only when identified as such; Stage 8 owns its full experimental design.

**Failure and repair.** Do not count different prices, audiences and claims as a clean hook-only test. Do not let assembled or reordered fragments imply a stronger promise or separate an assertion from a material qualification. Repair the unsafe cell, assembly rule or claim dependency and preserve valid cells. A copy-length or attention problem is not permission to remove product truth or fabricate urgency.

### M07. CTA architecture

**Definition.** Specify the intended next action, its priority and the commitment the user makes. Button wording, spoken instructions and visual cues are expressions of this contract. An awareness execution can deliberately have no immediate transactional CTA when that matches the accepted objective; this is an explicit choice, not a missing model.

**Minimum record.** CTA ID/revision; parent objective/message and audience state; action and destination/route; primary/secondary priority or deliberate absence; user-visible wording; expected benefit and actual commitment; prerequisites, price/terms/eligibility/disclosures that apply; information or data requested; next-step expectation; measurement event reference and implementation status; owner and acceptance. Secondary actions must have an explicit role and must not disguise a different commercial commitment.

**Dependencies and decisions.** Verify that the proposed destination can deliver the promised step and preserves the approved offer. “Read details”, “request a quote”, “book” and “subscribe” are different actions with different event semantics. A planned destination can support an explicitly provisional concept, not a launch-readiness claim. Advertising owns continuity requirements; the relevant destination and commercial owners supply their decisions and technical evidence.

**Failure and repair.** A free-download CTA must not conceal an unapproved recurring payment or imply that a sales enquiry is a completed purchase. Missing terms, broken routes or contradictory action labels require a scoped destination/copy repair. More aggressive wording cannot overcome a genuine commitment mismatch. Stage 7 defines the complete cross-domain handoff; Stage 8 defines measurement use. This model supplies their necessary semantic inputs without implementing either.

### M08. Creative hypotheses

**Definition.** State why a specified creative mechanism or expression is expected to help convey a particular message to an authorised audience in context. Separate the prediction from the supporting evidence and from any later observation. A message hypothesis asks what meaning may matter; a creative hypothesis asks how a particular expression may convey it. Neither is the same as Stage 3's audience hypothesis.

**Minimum record.** Hypothesis ID/revision; parent brief/objective/audience/message; territory/concept/expression references; proposed mechanism; assumptions and supporting/contradictory evidence; contrast or alternative explanation; intended change/response and relevant measure; fixed/changed dimensions; guardrails and downstream relevance; cheapest next evidence step; potential falsifying or inconclusive observations; dependencies; review owner/status. A generic “this will perform better” is not an inspectable hypothesis.

**Dependencies and decisions.** Match the evidence step to the question. A desk review can expose incoherence, unsupported claims or missing context; it does not prove actual consumer understanding or lift. Synthetic review remains synthetic. A later live comparison requires Stage 8's complete hypothesis, variables, comparison, primary metric, guardrails, downstream metric, threshold, confounders and decision rule plus separate authority.

**Failure and repair.** A preferred concept is not a validated winner. If a comparison changes several dimensions, revise the stated treatment or the design, not the history of what changed. If available evidence cannot discriminate the alternatives, record uncertainty and choose a bounded next step rather than manufacture significance, a consumer quote or a performance forecast. Preserve rejected hypotheses and their reasons so a local refresh does not erase learning.

## 5. Preserved evidence-to-adaptation chain

Retain the original chain exactly as a traceable sequence of responsibilities:

```text
business/customer evidence
→ message hypothesis
→ claim
→ substantiation / proof
→ creative expression
→ placement adaptation
```

This is a typed traceability chain, not a claim that audience research logically proves product performance. Its links can be many-to-many and may share sources, but their meaning must remain explicit. A source about what customers care about informs message choice; the relevant product/research evidence supports the actual claim. Neither a hypothesis nor the resulting creative is its own independent evidence.

| Chain node | Required record and relationship | What cannot substitute for it |
|---|---|---|
| Business/customer evidence | Exact approved business inputs and appropriately scoped customer research, with separate knowledge/use dimensions | An invented persona, convenient assumption, unapproved offer or inaccessible source claimed as verified |
| Message hypothesis | What meaning may matter, why, to which authorised audience and objective; links back to relevant evidence | A confident claim that the message already works, or an unrelated catchy line |
| Claim | The explicit/implied assertion being conveyed, with canonical meaning, conditions and scope | The label “creative”, a question mark or an attractive image that avoids inventory review |
| Substantiation / proof | Actual evidence linked to the claim, with a reasoned support assessment, limits and use rights | A copy of the claim, repeated model outputs, a generated result, or source access without adequacy review |
| Creative expression | Exact text, sequence, layout/sound description or actual artefact, with claim/proof/qualification dependencies and requested fidelity | A prompt called a finished asset or an expression whose implications exceed the supported claim |
| Placement adaptation | Identified parent expression, context/format, changed dimensions, preserved meaning and required rechecks | A resize, crop, translation or assembly assumed safe without inspecting its resulting meaning |

Review forward from evidence to the proposed meaning and backward from every material assertion in an expression to its support and authority. Record interpretation issues at the assertion or composition level, not only at the whole-ad level. An individually supported set of components can create a new unsupported implication when assembled or juxtaposed; that combined meaning needs its own review.

The claim/proof nodes are mandatory accounting points, not an instruction to invent factual claims for a purely associative creative. Where a review finds no factual assertion in a defined expression, record that finding, rationale and scope explicitly and retain the review link. Recheck when context or expression changes; a blank inventory or “brand ad” label is not an exemption for implied claims, endorsements, identity, product depiction or CTA promises.

An approved roadmap supports an intention or plan, not automatic evidence of current capability. A source-owner statement can establish the terms of their offer within its proper authority but cannot, on that basis alone, establish independently measured effectiveness. A proof presentation must preserve this distinction. A source that cannot be made public may support a properly reviewed claim without being reproduced in the ad; permission and adequacy still require their respective owners.

### Expression and adaptation record

An expression/adaptation records its own ID/revision, parent message/concept/expression, real/synthetic context, exact content or artefact reference, intended meaning, claims and evidence depended upon, mandatory qualifications and brand elements, medium/context assumptions, changed dimensions, omissions/reordering, fidelity, owner, review status and remaining restrictions. An executable final asset additionally needs the actual output and applicable later-stage checks; this model does not manufacture one.

Meaning must survive the intended viewing/listening/reading sequence. Review the proposed result, including whether a claim is seen or heard without its conditions, whether imagery introduces additional implications, whether a truncated or reordered fragment changes meaning, and whether the CTA still requests the promised action. Translation needs meaning/term review, not just a claim that wording is fluent. Do not fill uncertain platform limits from memory; Stage 5 and the relevant execution/policy work establish current requirements.

## 6. Strategy progression and selection

This progression defines decisions for using the models, not a separate orchestrator or prescribed multi-agent staff structure.

| Decision | Evidence to inspect | Accepted output and scope |
|---|---|---|
| Is the brief sufficient for this strategy task? | Exact Stage 3 baseline, objective, audience, offer/price/brand and affected unresolved items | Explicit bounded scope; missing facts remain unresolved rather than becoming defaults |
| What message is worth expressing? | Audience/customer evidence, commercial truth, priority, objections and plausible response mechanism | Message hierarchy with supported assertions and stated hypotheses |
| Which claims are supportable for the intended use? | Claim/proof mapping, source authenticity/scope, limitations, rights and applicable specialist review | Claims permitted for their recorded scope; unsupported dependencies stay blocked |
| Which creative routes answer the question? | Meaningfully different mechanisms and decision-useful cheap representations, not unequal polish alone | Comparable territories/concepts, uncertainty and production feasibility requirements |
| What is selected or deferred? | Objective alignment, truthful meaning, relevance rationale, brand fit, clarity, context feasibility, cost of resolving uncertainty and dependencies | Attributable selection/rejection/defer rationale, fixed elements and open treatment choices |
| What may be produced or tested next? | Exact selected scope, variant changes, evidence gaps, specialist needs, destination and evaluation requirements | Bounded handoff; full production/test/legal/spend gates remain separate |

Hard failures such as unsupported material claims, unauthorised commercial changes or missing required rights cannot be offset by originality or expected attention. Among eligible alternatives, use explained qualitative trade-offs rather than a universal aggregate score. The decision can prefer a cheaper route to answer the current question without predicting that it will achieve the best commercial result.

Do not mistake fluency, novelty, a favourable AI review or concept selection for audience validation. A reviewer can identify a plausible mechanism and a clear message; actual understanding, response or incrementality requires appropriate evidence. Evidence needed to select a rough concept differs from evidence needed to approve production, publication or scaling. The chosen next step must state which uncertainty it addresses and what it cannot establish.

## 7. Invariants and bounded repair

| ID | Invariant |
|---|---|
| I01 | Strategy references the exact accepted brief, audience and commercial baseline; proposed changes remain proposals |
| I02 | Message, audience and creative hypotheses remain separately identifiable, uncertain where appropriate, and linked to the intended objective |
| I03 | Material explicit and implied assertions are inventoried, including combined visual/verbal/sequence meaning |
| I04 | Every asserted support link has actual scoped evidence and an assessment; missing, partial, stale or conflicting support is not promoted |
| I05 | Evidence quality, use rights, claim permission, creative selection and execution/spend authority remain separate |
| I06 | Claims, proof and expressions retain their conditions, units, populations, versions and applicable time/context limits |
| I07 | Creative alternatives identify genuinely changed mechanisms or are honestly labelled execution variants |
| I08 | Hook/angle cells state changed/fixed dimensions and reject unsupported combinations rather than generating all combinations blindly |
| I09 | CTA wording, user commitment, offer, destination and event meaning agree; absent transactional CTA is deliberate and objective-compatible |
| I10 | Production fidelity is chosen for the unresolved question; planned or synthetic outputs are not labelled actual assets or observations |
| I11 | Forward and reverse traceability survive adaptation; a changed implication reopens relevant claim/proof review |
| I12 | Repairs affect the smallest responsible layer while retaining unaffected approved work and historical decision evidence |

| Failure | Required response | Preserve / owner |
|---|---|---|
| Message does not answer the accepted objective | Reframe priority or hypothesis against the same approved baseline | Preserve true source facts; Advertising and brief owner |
| New offer/price/segment is smuggled into an angle | Return the proposed commercial change upstream; block affected expression | Preserve original baseline and unaffected routes; Business Building/project owner |
| Proof is absent, out of scope or contradictory | Remove/narrow the unsupported assertion or request appropriate evidence/review | Preserve supported claims; Research/product/Legal owners as applicable |
| Proof display overstates evidence | Repair chart, wording, crop, demonstration or qualifier and re-review the assertion | Preserve source evidence and valid concept; Advertising/specialist craft |
| Objection reveals real product or capacity limitation | Acknowledge/qualify or escalate instead of inventing reassurance | Preserve factual research; business/destination owner |
| Concepts differ only cosmetically | Relabel as variants or explore genuinely different mechanisms | Preserve useful executions; Advertising |
| Hook variant changes the claim or commitment | Correct the cell or explicitly redefine the treatment and its approvals | Preserve valid matrix cells and history; Advertising/appropriate owner |
| CTA and destination disagree | Repair wording, destination or authorised commercial requirement before dependent execution | Preserve unaffected claims/concept; UIUX/Software Engineering/business owner |
| Adaptation changes meaning or loses a condition | Repair only the affected treatment/combination or choose a supported narrower expression | Preserve parent meaning and other valid adaptations; specialist/Advertising |
| Performance language is unsupported | Relabel hypothesis/review accurately and obtain appropriate evidence for the decision | Preserve actual observations and uncertainty; Advertising/measurement owner |

Do not cure a presentation defect by increasing the claim or cure a commercial defect by increasing persuasive pressure. If the repair crosses an authority boundary, the relevant owner must decide it. All actual instance artefacts and evidence remain in the consuming project; Pactwright, when present, receives domain outputs and findings without surrendering its lifecycle authority. [Stage1] [Stage3]

## 8. Representation alternatives and rejected approaches

| Approach | Decision and rationale |
|---|---|
| One free-form campaign concept with no separate claim/proof records | REJECT: hides unsupported implications and makes local preservation/repair unreliable |
| Treat every message, claim and proof as the same string | REJECT: confuses hypothesis, factual assertion, evidence and audience-facing expression |
| Linked readable records with exact parents, scope and decisions | SELECT: supports both small text work and specialist production without requiring a new runtime |
| Require every theoretical angle/hook combination to be generated | REJECT: creates low-value output and unsafe combinations instead of decision-led variation |
| Select whichever polished render gets the highest AI score | REJECT: confounds idea and execution; cannot establish evidence adequacy, audience response or authority |
| Treat a general persuasion formula as the mandatory creative grammar | REJECT: ignores objective, context, evidence, brand and different legitimate creative mechanisms |
| Use generated evidence to unblock an attractive creative route | REJECT: violates truthfulness; illustration is not product or customer proof |
| Turn this model into mandatory graph infrastructure or a universal copy API | REJECT: Stage 4 needs domain semantics; tooling and shared abstractions need later independent justification |

The selected model can express a single truthful bounded message without creating unnecessary documents, and a complex cross-format campaign without erasing its dependencies. Optional packs can later influence creative grammar, but cannot override verified constraints or approved offer/audience/brand decisions. No pack or provider is selected or implemented here.

## 9. Synthetic application and semantic inspection

The following is a modelling exercise based on the explicitly synthetic `SPECIMEN-03@1` in [Stage 3][Stage3], section 11. It is not a real workshop or an approved campaign. Its invented target, offer, price, notes, owners and dates have no evidential standing outside that exercise. No final artwork, workbook, customer quote, live destination, test result or legal clearance is generated or asserted.

Retained baseline: UK adults, fictional two-hour online workshop including a workbook, GBP 40 once, one attendee per order and capacity 20; the exact booking/refund windows, budget and downstream event definitions remain those of Stage 3. `FI-BUSINESS@1` is stipulated fixture input; `FI-RESEARCH@1` is five invented non-representative notes. `FI-AUTHORITY@1` permits only inspection of synthetic conceptual framing, never real publication or spend.

### Eight-component worked mapping

| Model | Explicit fixture record and decision |
|---|---|
| M01 | MH1@1: hypothesise that explaining the format/materials helps AH1 decide whether the workshop fits. Primary meaning: two-hour online session with a workbook; supporting price/terms remain exact; CTA1 below. Bookings are not direct evidence of comprehension |
| M02 | The Stage 3 intake CL1 is decomposed without changing meaning: CL-DURATION@1 = two hours; CL-ONLINE@1 = online; CL-WORKBOOK@1 = workbook included. CL-PRICE@1 = GBP 40 once under the exact fixture terms. Each links to its original O1/PRICE1 basis; no earnings, endorsement or accreditation assertion |
| M03 | PF-OFFER@1 references the stipulated FI-BUSINESS O1/PRICE1 facts, supporting only those fixture offer/price assertions. It is not independent performance evidence. No real workbook preview is supplied; a future preview proposal stays blocked pending the actual matching artefact and permitted use |
| M04 | OB1@1 = “What is included?” is a hypothesised question, not a customer quote or a measured objection frequency. Truthful answer: the supplied session/workbook terms. No additional coaching, accreditation or financial outcome is invented |
| M05 | T1@1, make the included material concrete, proposes CONCEPT-MATERIAL@1, a preview-led idea using a genuine authorised workbook; it is conditional on unavailable material. T2@1, make the time/terms legible, proposes CONCEPT-TIME@1, a text-led arrangement of the stipulated duration and terms. These differ in mechanism, not colour; neither is a validated winner |
| M06 | The four cells below cross material/time emphasis with statement/question openings. They are candidate text for semantic inspection only, with claim/proof/CTA links and explicit fixed dimensions |
| M07 | CTA1@1 = “View workshop details”; intended action is inspection of the planned D1 details, not payment or a subscription. D1 remains unimplemented, so this can describe a concept but cannot be advertised as a verified live journey. No immediate view event is implemented or claimed; E1 is the separate downstream paid-booking measure, not a CTA click |
| M08 | CH1@1 hypothesises that stating the duration immediately may make the commitment easier to identify than placing it after a question, because the direct opening provides the duration first. Contrast HX21/HX22 within T2/CONCEPT-TIME, holding offer, claims, audience, CTA and other intended dimensions fixed. Desk review can inspect order, ambiguity and semantic parity, not actual comprehension. Response inference needs an authorised Stage 8 test; no improvement is established |

T2 can be recommended for the next low-cost conceptual inspection because its stated facts are available within the fixture; this is not a real creative approval or a claim that it would outperform T1. T1's missing material is a declared dependency, not a reason to generate a fake product preview. No required Stage 4 input is missing: defining how a blocked fixture route behaves is part of this model inspection.

### Candidate hook/angle cells

The context of every cell is `synthetic, concept-only`. They are fragments for examining meaning, not complete publication-ready ads. The exact offer/price/audience remain fixed; any expression ultimately used must undergo the full contextual qualification and destination checks.

| Cell | Parent territory / concept | Angle / opening | Candidate text | Claim and proof links | CTA and changed dimension |
|---|---|---|---|---|---|
| HX11@1 | T1@1 / CONCEPT-MATERIAL@1 | Materials / statement | “Workbook included.” | CL-WORKBOOK@1; PF-OFFER@1 | CTA1@1; material emphasis, statement form |
| HX12@1 | T1@1 / CONCEPT-MATERIAL@1 | Materials / question | “What comes with the session?” followed by “A workbook.” | CL-WORKBOOK@1; PF-OFFER@1; both parts required for this meaning | CTA1@1; opening form changes versus HX11, not inclusion |
| HX21@1 | T2@1 / CONCEPT-TIME@1 | Time / statement | “Two hours, online.” | CL-DURATION@1; CL-ONLINE@1; PF-OFFER@1 | CTA1@1; time/context emphasis, statement form |
| HX22@1 | T2@1 / CONCEPT-TIME@1 | Time / question | “How long is the online session?” followed by “Two hours.” | CL-DURATION@1; CL-ONLINE@1; PF-OFFER@1; both parts required | CTA1@1; opening form changes versus HX21, not duration or mode |

HX11/HX12 are text fragments within the conditional material-preview route; neither supplies the missing real preview or proves T1 feasible. HX21 versus HX22 is the bounded contrast proposed by CH1. HX11 versus HX21 changes emphasis/content as well as wording and therefore must not be described as the same hook-only comparison. None of these cells receives an effectiveness score or a real approval from this exercise.

### Explicit preserved chain in the fixture

| Node | Fixture instance | Typed relationship and remaining limit |
|---|---|---|
| Business/customer evidence | FI-RESEARCH@1 and FI-BUSINESS@1 | Invented notes inform MH1; stipulated offer facts, not those notes, support the factual claims |
| Message hypothesis | MH1@1 | Uses AH1 and the approved-in-fixture objective; proposes a communication effect, not a measured one |
| Claim | CL-DURATION@1 / CL-ONLINE@1 | Uses exact O1 facts; other factual components have their separate claim IDs |
| Substantiation / proof | PF-OFFER@1 | References O1/PRICE1 in FI-BUSINESS; supports fixture terms only, never real performance |
| Creative expression | HX21@1 | States the two-hour online meaning; references the exact claim/proof/CTA records |
| Placement adaptation | PA-TEXT@1, proposed hypothetical static text placement | Parent HX21; same meaning and conditions; no actual provider selected or rendering performed. Any later crop, assembly or contextual implication needs review |

The proof node does not arise from the generated wording. The source path for the offer is separate from the invented audience notes. Reverse inspection of PA-TEXT resolves HX21, its two claims, PF-OFFER and the stipulated O1 basis. Other fields of the proposed placement remain unknown and cannot support a claim of technical or legal readiness.

### Semantic review cases

Each case is a manual check of the defined model against a stated mutation of the synthetic mapping. Expected restrictions are successful model-review outcomes, not real project blockers. No external campaign or implemented production validator is run.

| Case | Mutation or question | Observed model decision and bounded repair | Review |
|---|---|---|---|
| K01 | Inspect the base mapping for conceptual analysis | Eight models and all six chain nodes are accounted for; conditional T1 and unimplemented D1 remain visible; no live authority inferred | PASS |
| K02 | Use FI-RESEARCH's invented preference notes to prove workshop effectiveness | I02/I04 reject the cross-type inference; keep notes as hypothesis input, require actual relevant outcome evidence for an outcome claim | PASS |
| K03 | Rewrite the offer as a free trial to strengthen the message | I01 rejects commercial drift; preserve approved price/offer and return the proposed change upstream | PASS |
| K04 | Add guaranteed earnings to MH1 without a proof item | I03/I04 block the assertion, even when framed as an optimistic creative hypothesis; remove it or obtain actual applicable support/review | PASS |
| K05 | Generate a happy attendee quote and list it as a testimonial | I04/I05/I10 reject fabricated customer evidence; no generation can supply an actual person's experience or permission | PASS |
| K06 | Use a mock workbook preview as proof of what attendees receive | I04/I10 reject fake product evidence; keep an explicitly illustrative placeholder only within the permitted concept scope, obtain the real artefact before reliance | PASS |
| K07 | Treat an approved future roadmap item as available now | I04/I06 reject scope/time inflation; preserve its status or obtain evidence of actual availability | PASS |
| K08 | Record OB1 as the most common concern from actual customers | I02/I04 reject invented provenance and frequency; restore the hypothetical question label | PASS |
| K09 | Answer a price objection by adding an unapproved guarantee | I01/I05 reject the new commercial commitment; clarify existing terms or refer upstream | PASS |
| K10 | Call two differently coloured versions of HX21 independent territories | I07 identifies execution variation, not mechanism diversity; relabel or explore another route | PASS |
| K11 | Compare HX11 and HX21 but report a hook-form-only effect | I08 rejects the changed emphasis/content mismatch; state the broader treatment or use HX21/HX22 with an appropriate design | PASS |
| K12 | Separate a claim from a material condition during cropping or assembly | I06/I11 reject the altered meaning; repair the affected expression/combination, not all approved claims | PASS |
| K13 | Omit a denominator or comparison basis from a proof presentation | I04/I06 require the meaning-preserving context or a narrower supported expression; a cleaner chart is not stronger evidence | PASS |
| K14 | Label CTA1 a completed booking event | I09 rejects action/event substitution; viewing details and E1 payment/retention remain distinct | PASS |
| K15 | Send “View details” to an undisclosed recurring-payment action | I01/I09 reject the mismatch and unapproved commitment; repair destination/CTA and obtain any real commercial decision | PASS |
| K16 | Declare HX21 a proven winner because an AI evaluator prefers it | I02/I10 reject validation inflation; retain synthetic review status and obtain the evidence appropriate to response/performance claims | PASS |
| K17 | Use claim approval to authorise production purchase or media spend | I05 rejects scope escalation; obtain separate actual authority and relevant later-stage gates | PASS |
| K18 | A price/claim changes, but all parent approvals are inherited unchanged | I01/I06/I12 require revision-specific dependency review; preserve unaffected work and historical decisions | PASS |
| K19 | A purely associative expression has no inventoried factual assertion | Section 5 requires an explicit interpretation review and rationale, not invented proof or automatic exemption; new implications reopen review | PASS |
| K20 | Reject a valid concept because only one crop loses clarity | I12 routes a local treatment repair; retain the concept unless evidence shows its mechanism is infeasible | PASS |

## 10. Verification and conformance

The complete governing bootstrap was reread from `main` for the exit review; blob `f72a6f167595d6f178550fb1e02c4885d875b6b2` remained unchanged. Each of the eight required models and each node/link of the original preserved chain was inspected against that original and the accepted Stage 3 boundaries, not merely against this document's own checklist. All 20 synthetic semantic cases were checked for the stated decision, evidence limit and responsible repair.

The review found that the initial hook matrix did not explicitly carry its territory/concept parents and that CH1 described a comparison without its explanatory mechanism. The corrected specimen names those parents and states the proposed mechanism without pretending it has been validated. CTA1 now also explicitly distinguishes its unimplemented immediate view action from the downstream paid-booking event. These corrections preserve the original fixture offer and authority; they do not invent customer evidence or acceptance.

Executed Python checks cover eight ordered complete model definitions; acceptance, worked mapping and conformance; the literal six-node chain and both chain tables; 12 invariants; six progression decisions; ten repair routes; eight alternatives; four uniquely identified hook cells with parent/claim/proof/CTA references; 20 completed semantic-review rows; table columns, fences and 11 local references; immutable prior-file hashes; and the two-file stage-only change set. The first structural run caught an extra table column accidentally inserted into the fixture chain when adding hook parents. That row was repaired and the same check rerun successfully, without weakening its condition.

The final run contains 26 passing documentation/reference/integrity checks. The conformance below contains 14 PASS rows and one justified NOT APPLICABLE row. These checks and manual reasoning cases are not an executed campaign, generated-asset evaluation, legal clearance, consumer study or production software benchmark. The prior Stage 2 and Stage 3 local copies retain their exact accepted remote blob hashes; original/root/Stage 1 preservation is also checked in the remote publication tree.

| Requirement | Original reference | Evidence | Verification performed | Result |
|---|---|---|---|---|
| M01 message hierarchy | Stage 4 | Section 4 M01; fixture MH1; K02/K03 | Priority, objective/audience links, mandatory meaning and scoped omissions inspected | PASS |
| M02 claim inventory | Stage 4 | Section 4 M02; canonical fixture claims; K04/K07/K12 | Explicit/implied/composite meaning, scope, evidence, authority and blocked assertions inspected | PASS |
| M03 proof inventory | Stage 4 | Section 4 M03; section 5; PF-OFFER; K02/K05/K06/K13 | Provenance, adequacy, source independence, use rights and presentation distinction inspected | PASS |
| M04 objection map | Stage 4 | Section 4 M04; OB1; K08/K09 | Observed/inferred concern, truthful response and upstream limitation handling inspected | PASS |
| M05 creative territories | Stage 4; section 3 | Section 4 M05; T1/T2; K10/K20 | Distinct mechanisms, cheap representations, dependencies, selection and preservation inspected | PASS |
| M06 hook/angle matrix | Stage 4; section 3 | Section 4 M06; four fixture cells; K11/K12 | Actual expressions, fixed/changed dimensions, linked meaning and safe combinations inspected | PASS |
| M07 CTA architecture | Stage 4; section 3 | Section 4 M07; CTA1; K14/K15 | Action, commitment, destination, optional absence and event semantics inspected | PASS |
| M08 creative hypotheses | Stage 4 | Section 4 M08; CH1; K11/K16 | Mechanism, contrast, uncertainty, evidence step and complete Stage 8 handoff inspected | PASS |
| R01 preserved chain | Stage 4 exact six-node chain | Section 5; complete fixture chain; K02/K06/K12/K19 | Forward/backward links, source distinctions, scope and no generated proof inspected | PASS |
| G01 approved inputs and boundaries | Sections 2–3; accepted Stage 3 | Sections 1/3/4/7; K03/K09/K18 | Exact prerequisite, original ownership and no silent commercial edits inspected | PASS |
| G02 separate authority and truthful evidence | Sections 3/8/13/18 | Sections 3/5/6/7; K05/K07/K16/K17 | Knowledge/support/use/selection/production/publication/spend boundaries inspected | PASS |
| G03 fidelity, variation and repair | Sections 3/13 | Sections 4/6/7/9; K10/K11/K12/K20 | Cheapest useful representations, meaningful contrasts and local repairs inspected | PASS |
| G04 choices and non-goals | Sections 5/8/13/19 | Section 8; no production files | Eight alternatives and absence of universal score/platform/scaffold inspected | PASS |
| G05 complete durable verification | Execution prompt sections 7–9 | This record and research index | Coverage, tables, reference integrity, fixture chains and intended-file checks executed | PASS |
| Generated assets, live tests, packs/examples, software benchmark and installation | Stage 4 versus later stages | Section 2 applicability statement | No such Stage 4 requirement; candidate text is explicitly a model specimen, not production proof | NOT APPLICABLE |

## 11. Exit and next-stage input

All mandatory Stage 4 requirements pass. The eight strategy components, complete evidence-to-adaptation chain, semantic/authority distinctions, creative selection and bounded-repair rules are defined and verified. No real user decision, mandatory missing source or unresolved design ambiguity remains, and no waiver of a later requirement is proposed.

Only this research record and the research-log index change. The governing bootstrap, root README and accepted earlier research remain unchanged. Publication uses the exact stage-specific commit message in the header, parented by the verified Stage 3 commit. Remote branch head, commit ancestry, complete tree and intended content hashes must match the inspected files before Stage 5 begins; the commit's own SHA is not embedded recursively in its content.

Stage 5 receives the accepted brief interface, message/claim/proof dependencies, territories/concepts, controlled hook variants, CTA semantics, creative hypotheses, selected-scope requirements and unresolved production dependencies. It must independently define campaign idea → concept → master message/script/visual direction → format variants → placement variants → production assets, and research every named static, search, social-video, CTV, display, carousel, vertical, native/sponsored and audio format. No production asset, implemented adaptation or completed later-stage model is claimed here. Maturity remains bootstrap research.

[Bootstrap]: 2026-09-08-advertising-production-skills-new-project-bootstrap-process.md
[Stage1]: 2026-09-10-stage-01-domain-boundaries.md
[Stage2]: 2026-09-10-stage-02-professional-advertising-practice.md
[Sources]: 2026-09-10-stage-02-source-register.md
[Stage3]: 2026-09-10-stage-03-campaign-brief-audience-objective-model.md

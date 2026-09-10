# Advertising Production Skills: Workflows and Artefacts Specification

Version: 1.0  
Date: 10 September 2026  
Status: Canonical design specification

## 1. Ownership and use

This document defines campaign meaning: inputs, records, production decisions, handoffs, evidence, state, diagnosis and repair. [Spec 01](01-advertising-production-skills-system-spec.md) owns the system boundary; [Spec 03](03-advertising-production-skills-repository-and-contracts-spec.md) owns installed contracts; [Spec 04](04-testing-and-benchmark-spec.md) owns evaluation execution. [Spec 05](05-advertising-production-customisation-packs-spec.md) and [Spec 06](06-advertising-production-extension-pack-catalogue.md) specialise these rules without overriding them.

A logical record can be a section, table or structured file in the consuming project. Do not create a database, graph service or separate file for every field. Reuse exact accessible upstream records rather than maintaining another editable price, customer, evidence or approval store. The local prefixes below disambiguate identifiers from the research: for example `BR.C01` is the brief's C01, not command C01. They do not introduce a new graph or runtime schema.

## 2. Production workflow and fidelity

```text
read approved business and existing campaign context
→ frame the advertising question and unresolved dependencies
→ accept a scoped brief and audience hypothesis
→ establish message / claim / proof / objection / CTA architecture
→ compare actual cheap concepts
→ record selection, fixed elements and unresolved craft questions
→ commission or produce the requested format and placement outputs
→ inspect actual returns and destination continuity
→ bind media, targeting, experiment and measurement contracts
→ evaluate the exact package and record its readiness by gate
→ receive permitted actual observations
→ reconcile and diagnose
→ correct the smallest responsible layer
→ re-evaluate, preserve learning and request authorised next action
```

A bounded task can enter at the appropriate operation without rerunning the whole chain. Its relevant prerequisites must still exist. Missing commercial truth, required source assets or an owner decision blocks the dependent step; it must not be filled by a plausible invention. When resolving a requirement needs the user, stop and ask rather than proceed on their behalf.

| Fidelity | Required work | Not implied |
|---|---|---|
| Draft | Actual requested text, rough composition, sequence, script or mockup sufficient to inspect the stated question; label hypotheses and illustrative content | Finished media, verified implementation, owner approval or audience response |
| Refine | An identified parent, evidence-led change, actual revised representation, fixed/changeable comparison and affected rechecks | Permission to rewrite the offer, valid siblings or source evidence |
| Final for scope | Every output required by the accepted request exists, is inspectable and has passed all applicable technical, craft, meaning and authority gates | Live publication, serving, legal clearance beyond its actual scope, or campaign success |

Requested and delivered fidelity are recorded separately. A prompt is not an image; a script is not audio; a storyboard is not a movie. A file can be generated but fail evaluation. Accepted-for-scope is distinct from permitted-to-publish and from actually-delivered.

<!-- resource:brief-and-evidence -->
## 3. Common identity, evidence and decisions

Every material artefact records stable ID, revision, author/responsible owner, consuming-project location, real/synthetic context, creation/update time with actual timezone/precision, requested decision and fidelity, exact parent/input revisions, fixed/changeable scope, relevant evidence and authority, actual output location, findings and unresolved dependencies. Not every small text fragment needs its own object; anything that changes commercial meaning, eligibility, claims, commitment or evaluation needs traceable provenance.

Keep the following dimensions independent:

| Dimension | Values or required content | Rule |
|---|---|---|
| Knowledge basis | `observed`, `supplied`, `derived`, `hypothesis`, `unknown`, `conflicted`, `not-applicable` | An observation may be biased; a supplied statement is not independently verified merely because it was received |
| Use decision | `pending`, `approved-for-scope`, `rejected`, `expired`, `superseded` | Approval does not strengthen evidence, and evidence does not grant rights or spending authority |
| Source | ID/location, exact version or captured-at, relevant passage/data definition, owner and accessible evidence | A title, inaccessible link or duplicated report cannot substitute for inspected support |
| Scope and validity | Product/population/market/period, effective/expiry dates, use restrictions, contradictions and recheck trigger | Preserve partial date precision and limitations; do not invent currency or temporal equivalence |
| Derivation | Exact inputs, units, method/calculation, assumptions and uncertainty | A derived projection remains a projection even when its use is approved |
| Dependency | Fields, claims, expressions, actions and findings relying on the source | A source correction reopens affected dependencies, not unrelated accepted work |

An approval identifies the actual issuer and authority, decision time, exact subject/revision, purpose, action, scope, conditions, validity period and decision evidence. A skill's favourable evaluation is not an owner decision. Synthetic approvals are valid only inside their explicitly fictional exercise and never authorise real publication, data use, spending or account changes.

Unknowns carry a question, resolution owner, evidence needed, affected action and review point. Conflicts retain both sources and the authority question. `not-applicable` needs a substantive reason. Missing, empty, zero and not-applicable are never interchangeable. Private evidence remains in controlled consumer storage; do not publish it merely to make a reference accessible.

## 4. Complete brief and audience model

A complete campaign brief has the common header, all thirteen areas below, three separate audience layers, scoped acceptance and unresolved issues. Each area is populated, explicitly unknown/conflicted with a consequence, or justifiably not applicable. A frame with unresolved inputs is not automatically an accepted launch brief.

| ID | Area | Minimum contract and acceptance boundary |
|---|---|---|
| BR.C01 | Business objective | Upstream outcome, customer/market, unit, horizon, known baseline/target, priority, capacity/other guardrails and authority. An approved learning objective may replace an unjustified numeric target; the skill must not invent that approval. Conflicting commercial priorities return upstream. |
| BR.C02 | Advertising objective | Intended change in awareness, understanding, consideration or response; parent business objective, proposed mechanism, audience/context, primary indicator, horizon and conflict rule. Platform campaign goals are later mappings, not the objective's definition. |
| BR.C03 | Approved audience evidence | Source/revision, method, observed population/market/time, finding, contradictions, limitations and permitted use. Record observed language separately from an inferred persona; unknown samples cannot be called representative. |
| BR.C04 | Offer | Exact product/service/version, beneficiary and eligibility, inclusions/exclusions, availability, capacity, fulfilment and cancellation/refund/guarantee conditions with source/approval. Advertising may emphasise supported value but cannot change the exchange. |
| BR.C05 | Price | Amount or approved quoted basis, currency, billable unit, billing period, upfront/recurring distinction, supplied fees/tax presentation, minimum commitment, introductory/renewal terms, eligibility and validity. Unknown is not free; a quote-based offer does not acquire a fabricated fixed price. |
| BR.C06 | Market | Commercial geography, language/locale, actual service/distribution availability, relevant store/platform environment and exclusions. Media geography is not fulfilment scope; translation does not authorise a new market. |
| BR.C07 | Budget | Currency, period, included media/production/measurement/other costs, total ceiling, proposed allocation/reserve, supplied commitments, excluded costs and their owner, separate planning and spending authority. No hidden production liability or double-counted subtotal. |
| BR.C08 | Economics | Approved outcome/unit, contribution basis, known acquisition/payback limits, capacity, cohort/period, cost assumptions and uncertainty. Revenue, contribution, collected cash and projected lifetime value remain distinct. Missing economics cannot support profitable scaling. |
| BR.C09 | Schedule | Intended flight, timezone/boundary conventions, production/review dependencies, offer/rights validity, deadlines and distinct measurement horizon. Requested date, confirmed readiness and actual launch are separate facts. |
| BR.C10 | Brand requirements | Identity/voice, recognisable elements, mandatory/prohibited expressions, accessibility requirements, references and actual rights/owner decisions. Inspiration is not a supplied licensed asset; preference does not override claim or legal constraints. |
| BR.C11 | Claim/proof inventory | Proposed explicit/implied assertions, exact scope, evidence references, qualifications, limitations, owner and review/use state. Retain unsupported/prohibited claims so later drafting does not regenerate them. An empty inventory needs an actual no-claim review. |
| BR.C12 | Destination | Intended route/experience, identity/revision or proposed location, owner, locale, promised action, terms/proof/disclosure and routing/tracking dependencies. Planned content, deployed endpoint and verified journey are distinct. |
| BR.C13 | Measurement events | Event identity, semantic meaning, entity counted, qualifying/disqualifying conditions, source/owner, time/window, aggregation/deduplication, value basis and implementation/verification status. A named event is a requirement until actual implementation evidence exists. |

### Three audience layers

| ID | Record | Required content | Failure boundary |
|---|---|---|---|
| AU.A01 | Approved business segment | Exact segment/revision, inclusion/exclusion, served market, actual needs/context, permitted buyer/influencer roles, offer/economics links, evidence and owner approval | New commercial customer or role scope requires its owner; not every recipient must be the end user when approved roles explicitly differ |
| AU.A02 | Advertising audience hypothesis | Parent segment, proposed context/need/response, supporting and contrary evidence, inference strength, intended observation, exclusions and decision state | Hypotheses remain uncertain; no sensitive inference or stereotype becomes researched truth because a model suggests it |
| AU.A03 | Platform targeting representation | Parent hypothesis/segment, actual selected product/profile, rule-to-control mapping, expansion behaviour, data-purpose/recipient authority, account/configuration evidence and verification state | Platform fields do not redefine the audience; hard restrictions cannot be weakened to fit the available tool |

For every mapped rule record `enforced`, `signal-only`, `unsupported` or `unverified`, plus evidence and limits. A hard restriction mapped only to a signal or an unverified control blocks execution depending on that restriction. A contextual hypothesis can be useful without personal data. Technical ability to upload does not establish authority to activate it.

Trace segment → hypothesis → representation → actual delivery evidence. Keep evidence → hypothesis and data-use authority → representation separately inspectable. A changed segment, hypothesis, representation or delivered mix is a material change to the corresponding downstream comparison, not a cosmetic rename.
<!-- /resource:brief-and-evidence -->

<!-- resource:strategy -->
## 5. Message, claim, proof and creative strategy

All strategy records inherit exact brief/audience/brand references, evidence and knowledge states, owner, decision scope, real/synthetic context and unresolved dependencies.

| ID | Model | Minimum content | Acceptance and smallest repair |
|---|---|---|---|
| ST.M01 | Message hierarchy | Primary intended takeaway; supporting messages and priority; audience/objective rationale; claim/proof/objection/CTA links; mandatory qualifications and permitted omissions | Resolve conflicting priorities or unsupported promises at the message layer. A material qualification is not optional supporting copy. |
| ST.M02 | Claim inventory | Exact assertion and plausible implied meanings; type, subject/version, population, market, period, units/comparator; evidence required and supplied; support assessment, conditions, rights, review status and affected expressions | Split independently supportable parts, then inspect their combined implication. Narrow/remove unsupported scope or obtain evidence; softening “will” to “may” is not automatic repair. |
| ST.M03 | Proof inventory | Actual source/location/version; producer and method; finding, scope, uncertainty, exclusions, contradictions, validity and authenticity limits; rights/access; claims supported and not supported; permitted presentation | Judge adequacy for the exact claim. A generated screen, testimonial, badge, reconstructed chart or repeated model output is not independent real proof. Repair presentation without strengthening the underlying evidence. |
| ST.M04 | Objection map | Exact observed concern or labelled hypothesis; source, audience/context, evidence strength, affected decision, truthful response, linked support, unanswered dependency, owner and priority | Clarify misunderstandings; acknowledge genuine limits. Price, fit, capacity or product defects may belong upstream rather than being “overcome” through urgency or pressure. |
| ST.M05 | Creative territories | Plain-language thesis and mechanism; parent message/audience; actual short treatment, evidence dependencies, possible concepts, brand fit, context, cheapest representation, risks, comparison and disposition | Alternatives must differ in communication mechanism, not only colour or punctuation. Reject proof-dependent deception; preserve a valid idea during local treatment repair. |
| ST.M06 | Hook/angle matrix | Angle perspective and rationale; actual hook expression/sequence; cell/variant identity, parents, claims/proof/qualifiers/CTA, context, fixed/changed elements, evaluation question and prohibited combinations | Do not produce the full Cartesian product by default. A hook-only comparison cannot quietly change price, audience or claim meaning. Repair the unsafe cell or assembly constraint. |
| ST.M07 | CTA architecture | Intended action and route, priority or deliberate absence, exact wording/cue, benefit and commitment, prerequisites, terms/eligibility/disclosures, required data, next-step expectation and event | Viewing, requesting, booking and subscribing are different commitments. Correct labels/routes; do not disguise payment or confirmation. An awareness task need not invent a transaction. |
| ST.M08 | Creative hypotheses | Mechanism, exact expression and contrast; audience/message/objective parents; supporting/contrary evidence, assumptions, predicted observation, fixed/changed dimensions, guardrails, falsifying/inconclusive observations and next evidence step | A preference is not validation. Match desk review, technical check, audience research or live experiment to the actual question; no invented respondent, lift or significance. |

Preserve the evidence chain in both directions:

```text
business/customer evidence
→ message hypothesis
→ claim
→ substantiation / proof
→ creative expression
→ placement adaptation
```

Audience research informs what might matter; it does not prove product performance. Source-owner permission does not establish adequacy. Proof presentation makes actual evidence understandable; it cannot improve its evidential strength. A roadmap supports an intention, not present functionality. Every material implication in text, image, sound, juxtaposition or sequence needs a reverse trace to its claim and support assessment.

A reviewed expression with no factual claim records that finding, rationale and context explicitly; “brand ad” is not an exemption. Recheck after composition, translation, crop, cutdown or context changes. Allowed components can create a new unsupported meaning when combined.

### Selection and refinement

Compare actual representations against the same accepted objective, evidence constraints, brand and intended context. Record alternatives, findings, preference or actual authorised selection, rationale, selected fixed elements, open craft choices, unresolved dependencies and the next permitted commitment. Retain rejected routes and why they failed. Honour exact requested counts; otherwise choose enough genuine alternatives to resolve the question without compulsory fan-out.

A selected concept is not a market winner, blanket production approval or permission to publish. A refinement identifies its parent, defect/question, allowed changes and required rechecks. If the mechanism or commercial proposition changes, record a new reviewed concept or upstream decision rather than concealing it as a local edit.
<!-- /resource:strategy -->

<!-- resource:production -->
## 6. Creative production and adaptation

Every production record binds identity/parents, intended meaning, actual content or output, requested/delivered fidelity, changed/fixed dimensions, format/placement/profile, source rights and dependencies, resource authority, review/selection scope and actual provenance. Six layers can share a file; their meanings cannot be merged.

| ID | Layer | Required record and decision |
|---|---|---|
| PR.P01 | Campaign idea | Organising proposition, objective/audience/message parents, communication mechanism, evidence/brand boundaries, alternative routes and cheapest representation. Selection approves only its stated scope. |
| PR.P02 | Concept | Particular opening, device, beats/composition, proof treatment, takeaway and action; parent idea/territory, actual cheap representation, alternatives, feasibility and preserved/open elements. Cosmetic variants are not automatically distinct concepts. |
| PR.P03 | Master message/script/visual direction | Canonical wording/meaning, beats, hierarchy, sound/voice/pronunciation/pacing where relevant, brand/source assets, proof/qualification and CTA, fixed and adaptable dimensions. A semantic master need not be a finished landscape video. |
| PR.P04 | Format variant | Re-expression as static, assembled text, temporal video, card sequence, audio or another defined form; parent master, exact treatment, meaning changes, specialist output, cheap check and modality risk. Resize is not semantic equivalence. |
| PR.P05 | Placement variant | Exact product/inventory/device/locale, interaction/sound context, current profile, assembly/enhancement behaviour, fields/overlays, CTA/destination, controls and inspection coverage. A preview proves only the reviewed configuration. |
| PR.P06 | Production asset | Actual required file/component/source bundle, accessible location, revision/hash where available, actual type/properties, producer/tool/settings and time, source/rights, exact parents and technical/craft/domain checks. A filename, empty manifest or prompt is not an asset. |

### Nine format responsibilities

A requirement profile records issuer/product/serving mode, market/locale, exact source and passage, publication/update and retrieved-at, version/effective context, rule class, capability/account limits and recheck trigger. Keep hard constraints, recommendations, capability descriptions and unknown conditions distinct. The numeric profiles in examples are exercise rules, not timeless live-platform limits.

| ID | Format | Required production and inspection |
|---|---|---|
| MF.F01 | Static | Actual composition, readable hierarchy, focal meaning, proof/brand/qualifications, intended scale and editable/export requirements. Physical output requires the actual printer/media-owner profile; do not invent print settings from a digital guide. |
| MF.F02 | Search | Exact component strings, mapping, destination and allowed assembly/omission rules. Inspect every finite high-risk combination or justify explicit equivalence classes and uncovered cases. Individual character fit cannot establish combined claim safety. |
| MF.F03 | Social video | Opening, beats, visual/voice/text relationship, identity, commercial disclosure, rights, CTA and interface context. Inspect actual temporal content, crop/captions, claim-bearing moments and sound-off meaning. |
| MF.F04 | CTV | Actual video, viewing/listening context, technical/delivery requirements and available response mechanism. A non-clickable placement cannot promise an interactive button; production, clearance, upload and serving remain separate. |
| MF.F05 | Display | Fixed or responsive components, inventory/device context, text-image relationship, assembly constraints and actual rendered evidence at relevant scales. A master image does not prove every responsive combination. |
| MF.F06 | Carousel | Exact cards and order/independent-view assumptions; repeated or distributed meaning, price/qualification dependencies, CTA and actual exports. A claim seen without its essential later-card condition fails. |
| MF.F07 | Vertical | Aspect/orientation, intended device, overlays/crop, safe reading and interaction context. Vertical is an orientation across formats, not a new campaign concept or proof that every platform accepts the same asset. |
| MF.F08 | Native/sponsored | Entry-point and destination meaning, actual text/media and assembly, publisher styling dependencies, source attribution, commercial identity and rights. Native appearance does not justify disguised sponsorship or fake experience. |
| MF.F09 | Audio | Audible message, voice/pronunciation, pacing, music/sound rights, qualification and usable screenless response; actual recording, properties and listening. Word count, loudness metadata or transcript alone cannot establish intelligibility or disclosure sufficiency. |

For final media inspect the actual output, not only the instruction or thumbnail. Record method and coverage: full sequence, relevant frames, reduced viewing conditions, real listening and technical probes as applicable. An unavailable inspection remains unverified. Craft acceptance, campaign integration, Legal/rights decisions and publication authority are separate.

### Adaptation invariants

| Change | Required check | Preserved boundary |
|---|---|---|
| Crop/resize | Actual focal meaning, proof, brand and readable conditions at intended viewing size | Correct dimensions do not establish correct meaning |
| Cutdown/resequence | Removed/reordered beats and changed temporal/causal implications | A shorter clip may create a new claim |
| Visual/audio/sound-off | Essential meaning in the available modality and feasible action | A companion image cannot carry a necessary screenless condition |
| Translation/transcreation | Commercial terms, quantity, nuance, comparison, qualification and action; competent review when required | Fluency does not authorise a market or price change |
| Responsive assembly | Exact permitted components, omissions, mandatory dependencies, control and coverage | Sampled safe previews do not prove every allowed combination |
| Feed/product refresh | Exact product/offer/evidence revisions, actual availability and expiry | A data refresh can change a substantive claim |
| Creator/native reuse | Particular identity/material/use rights, truthful experience and commercial identification | Access is not reuse permission or claim support |
| Automated enhancement | Actual transformation/settings and inspected result, or justified constrained behaviour | Provider automation does not decide semantic equivalence |

Reject an execution configuration when essential conditions cannot be verified or enforced. Request a compatible treatment or authorised route without weakening the source truth. Repair only the affected output, caption, mix, assembly or source dependency; preserve valid master and siblings. Record planned, requested, generated, received, evaluated, accepted and delivered as distinct facts.
<!-- /resource:production -->

<!-- resource:media -->
## 7. Media, placement, targeting and budget

A media line binds its ID/revision, parent campaign/business channel strategy, all eleven dimensions below, exact creative and journey revisions, profile, resources, authority, feasibility, findings and required executor return. A forecast, documented capability, actual configuration and observed delivery are different evidence.

| ID | Dimension | Minimum content and decisive check |
|---|---|---|
| MD.M01 | Channel role | Job within the approved channel strategy, audience/context rationale, contribution path, alternatives and success/guardrails. A channel list alone is not a plan; new business-wide channel scope returns upstream. |
| MD.M02 | Placement role | Product/buying mode, inventory/device/modality, attention/interaction, locale, format/profile, assembly/enhancement, CTA and acceptance. Reject click-dependent actions in non-clickable contexts. |
| MD.M03 | Audience hypothesis | Exact segment/hypothesis, evidence and uncertainty, inclusion/exclusion, representation and data-use authority. Expansion or signals cannot silently weaken a hard restriction. |
| MD.M04 | Geography | Served market, intended recipient geography, inclusion/exclusion, selection meaning, granularity, language, fulfilment and jurisdiction questions. Presence, residence and interest are not synonymous. |
| MD.M05 | Schedule | Flight, timezone and boundary convention, serving hours, offer/rights/approval validity, readiness, reservation/cancellation and monitoring/measurement windows. Check cross-midnight and daylight-saving boundaries when material. |
| MD.M06 | Frequency | Intended pattern, counted event/identity, cap/target/average/distribution, period, aggregation and overlap, actual control and reporting limits. No universal optimum or inferred exposure reset. |
| MD.M07 | Reach | Potential, forecast and observed/modelled reach separately; population, counting identity, period, geography, method, uncertainty and deduplication scope. Do not sum overlapping platform totals into unique people. |
| MD.M08 | Optimisation objective | Business/ad parents, exact event/action set, biddable versus observation-only mapping, value/currency, latency, attribution window and downstream guardrails. Verify what the configured goal actually rewards. |
| MD.M09 | Test allocation | Question, treatment/comparison, changed/fixed dimensions, allocation unit and denominator, money/traffic split, overlap/interference, alignment, cost/volume feasibility and stop/review conditions. Equal spend is not random assignment. |
| MD.M10 | Exclusions | Exact predicate, reason/authority, hard versus preference status, affected line, representation, freshness, update latency, evidence and review trigger. Test permitted, forbidden, stale and withdrawn states separately. |
| MD.M11 | Brand safety | Prohibited contexts and brand-specific suitability, source/authority, inventory scope, unknown-context treatment, actual controls/coverage, monitoring and authorised response. Context suitability, audience eligibility, fraud, creative truth and law remain distinct. |

A rule marked enforced still states its operational meaning and limitations. A destination eligibility check may complement permitted media controls but cannot retrospectively authorise prohibited exposure. Unknown actual controls prevent the corresponding execution claim, not all useful campaign planning.

### B01. Envelope, exposure and staging

The budget extends the brief rather than creating another financial truth. Retain upstream revision, currency/precision, period, supplied cost/fee/tax basis, included and separately funded costs, estimates, allocations, reserve, incurred costs, uncancelled liabilities, open executable authority and exact owner decisions. Estimates, commitments, served cost, billed cost, credits and cash payment are distinct.

For a planning version:

```text
sum(included allocations) + retained reserve <= declared envelope
sum(media suballocations) <= media subtotal
```

Do not add a subtotal to its children. Currency conversion needs a supplied, dated and approved basis; no exchange rate or tax conclusion is invented.

For execution use disjoint categories:

```text
I = cost already incurred, including appropriately bounded unreported accrual
L = remaining uncancelled contractual liability not already counted in I
A = maximum additional executable exposure not already counted in I or L
I + L + A <= relevant authorised ceiling
```

Retained reserve is not executable authority. Unknown liabilities or uncontrolled overdelivery prevent a claim that a hard ceiling is protected. A daily setting, schedule or alert is not assumed to be a hard total cap. Check shared budgets, automation, reporting/stop latency, cancellation terms and non-reversible commitments against the actual executor's behaviour.

A spending decision identifies issuer, exact purchase/account/campaign/phase, permitted operation, currency and cost basis, ceiling, validity, guardrails, allowed reallocation and stop owner. A production purchase and a media allocation need their respective authority. Repository-write permission and an API key grant neither.

Compare plans without committing; obtain authority before production/inventory liability; release a bounded test only with actual required assets, journey, measurement and controls; review mature evidence and residual exposure before reallocation; obtain executor evidence for actual stop or retirement. No phase or reserve is released automatically from a favourable early ratio. Preserve unaffected media lines and historical observations during repair.
<!-- /resource:media -->

<!-- resource:destination -->
## 8. Destination continuity and cross-domain handoffs

A destination is the next experience promised by the advertisement: page, form, store listing, app, marketplace, phone call or physical route. A journey names consequential transitions, not only the final URL. Include relevant redirects, locale/device/eligibility, authentication, consent, checkout, confirmation, fulfilment, post-install, already-completed, error and fallback states; omit irrelevant branches with reasons rather than invent a universal funnel.

The journey record binds ID/revision, real/synthetic context, exact brief/offer/price/audience/message/claim/proof/CTA/media/asset inputs, entry/context, route and observed/proposed content or configuration, commercial/rights validity, event/data interface, findings, coverage, authority and unresolved owners. A stable URL can serve changing content. A screenshot proves only the inspected view; a response code proves transport, not semantic or transaction correctness.

| ID | Dimension | Required comparison and evidence | Smallest repair |
|---|---|---|---|
| JT.D01 | Message | Primary/supporting meaning and intended takeaway against actual next-step content, including permitted extra explanation | Correct misleading content or route; preserve a valid proposition and other destinations |
| JT.D02 | Price | Exact amount/basis, currency, billing unit/period, fees/tax as supplied, minimum/introductory/renewal, eligibility and refund/cancellation through commitment surfaces | Restore the owning terms or obtain a real upstream change; do not adopt the newest observed page as authority |
| JT.D03 | Claim | All explicit/implied assertions added or strengthened by destination copy, visuals, demonstration or sequence | Narrow/remove or substantiate the affected claim and recheck dependent expressions |
| JT.D04 | Proof | Actual support versus audience-facing presentation and accessibility of specifically promised evidence | Repair the resource/presentation or promise; do not fabricate proof or expose confidential material |
| JT.D05 | CTA | Exact immediate action, user commitment, prerequisites, data, completion and fallback; request versus confirmation | Correct action label/route/implementation without disguising price or collecting unrelated data |
| JT.D06 | Tracking | Event meaning, counted unit, qualification, timestamp/environment, campaign mapping, permitted correlation, deduplication, value, lag and actual implementation tests | Repair technical mapping and affected interpretation, not valid creative; retain missing/delayed/modelled distinctions |
| JT.D07 | Disclosures | Applicable exact source/decision, meaning, surface, modality, timing, prominence/accessibility, language and validity | Repair the affected text/layout/mix/interaction; return unresolved sufficiency to its owner |

First compare an inexpensive ad-plus-destination representation. At implementation or release scope inspect actual relevant branches and returned technical evidence. Essential ad qualifications are not automatically cured by a destination footnote. Screenless information must be audible. Exact wording need not be identical across surfaces when the same truthful meaning and commitment are preserved.

### Handoff responsibilities

Every request includes the exact question, baseline, source restrictions, relevant continuity dimensions, fixed/changeable elements, requested output/fidelity, context, authority and acceptance evidence. Every return binds that request to an actual output or identified proposal, provenance, inspections/coverage, deviations, unresolved issues and any actual scoped decision. Use the detailed operation envelope when tools or external effects are involved.

| Owner | Requested work | Required return and boundary |
|---|---|---|
| Business Building | Exact commercial contradiction, original terms and affected journey | Retained or revised authorised commercial record; Advertising never changes the exchange itself |
| Deep Research | Bounded audience/claim/proof question with sources and standard | Attributable findings, methods, contrary evidence and limits; source relevance remains reviewed |
| Legal | Exact communication, proof, commercial/targeting facts, jurisdiction, dates and disclosure proposal | Scoped conclusion/conditions or escalation; not a generic rubber stamp |
| Narrative | Message, claim, CTA, voice and context | Actual words/script with changes identified; specialist craft and campaign integration stay separate |
| Video / Audio / visual specialist | Exact concept, rights, required disclosures/action, profile and fidelity | Actual required media/source files and craft/provenance evidence; a brief is not a produced asset |
| UI/UX | Promise, terms, proof, actions, states and accessibility | Actual content/design/interaction at requested fidelity; design is not deployed behaviour |
| Software / analytics / operator | Accepted behaviour, route/event/data contract and authorised test scope | Actual implementation/configuration and technical evidence; event transport is not qualified business value |
| Ad operations | Accepted assets/routes/settings, schedule, constraints and exact action authority | Actual configuration/resource IDs and scoped read-back; no implicit activation or spend |
| Pactwright, optional | Provided Contract and required domain evidence | Domain artefacts/findings/revisions/blockers returned to lifecycle owner; no mandatory dependency |

Reconcile all returned revisions against one accepted baseline. Different owners' positive findings cannot silently approve unreviewed changes. A partial return may support only an explicitly permitted smaller task; it cannot complete a request for final implementation. Real handoff instances remain in the consuming project.
<!-- /resource:destination -->

<!-- resource:measurement -->
## 9. Experiments, measurement and attribution

A test header records ID/revision, real/synthetic context, owner, question category, requested decision, exact brief/segment/hypothesis/claim/asset/media/destination baseline, source restrictions, planned/actual periods, analysis-plan revision, actual study/executor, approvals and unresolved dependencies. Keep design, execution, observation, analysis and decision separately identifiable.

| ID | Field | Complete required content and rejection boundary |
|---|---|---|
| EX.T01 | Hypothesis | Expected change, population/context, comparator, mechanism, outcome/direction, precisely defined estimand, support/contrary evidence, assumptions and falsifying/inconclusive observation. Assignment-policy effects differ from effects among selected viewers/clickers. |
| EX.T02 | Changed variables | Exact planned and actual differences across copy/claim/concept/format/placement/audience/destination/goal/budget/schedule/assembly/measurement; fixed revisions and deliberate interactions. Unplanned changes retain times and affected scope; do not rewrite history to preserve a hook-only label. |
| EX.T03 | Comparison | Control/treatment, eligibility, assignment mechanism/unit/probability, exposure, analysis unit/population, timing, overlap/interference and assignment-versus-exposure basis. Equal spend or competing ad sets do not establish randomisation or equal people. |
| EX.T04 | Primary metric | Exact construct/event/version, numerator/denominator, unit, qualification/exclusion, deduplication/aggregation, direction/value/currency, owner, time/cohort/window/maturity and uncertainty. Multiple co-primary outcomes need a predeclared joint/multiplicity rule. |
| EX.T05 | Guardrails | Relevant truth, rights/data/targeting, commercial, experience, capacity, delivery and validity predicates; threshold/basis, monitoring, owner, response latency, authorised stop and affected scope. Hard failures cannot be traded for CTR; no complaints is not proof of safety when observation is incomplete. |
| EX.T06 | Downstream business metric | Upstream value definition, entity/cohort, qualification, fulfilment/refund/reversal, cost basis, horizon/lag, observation availability and constrained decision. Preserve retained contribution versus revenue or speculative lifetime value. |
| EX.T07 | Evidence threshold | Required validity, practical effect, statistical framework where relevant, baseline/variance, precision/power/sample rationale, min/max duration, maturation, interval, multiple comparisons/subgroups, planned looks/stopping and feasibility. Unknown volume is not sufficient power; never weaken thresholds after seeing results. |
| EX.T08 | Confounders | Relevant alternative causes/validity threats, affected contrast, preventive controls, diagnostics, residual uncertainty and owner. Distinguish observational confounding, implementation faults, mediation and chance imbalance; outcome imbalance is not automatically assignment mismatch. |
| EX.T09 | Decision rule | Predeclared ordered invalid/harmful/supported/unsupported/inconclusive outcomes, safety/resource stops, maximum horizon/budget consequence, next evidence, action scope, owner and preservation. A better point estimate, nonsignificance or repeated fixed-horizon peeking cannot manufacture a winner or equivalence. |

Use an uncertainty method suitable for the actual assignment and dependence. Do not transfer independent-person fixed-horizon formulae blindly to clustered, adaptive or sequential settings. Bayesian reasoning states prior, likelihood, decision quantity and sensitivity. No universal sample, p-value, test duration or effect threshold is a core default. A categorical document review can require all relevant hard checks without pretending it is a statistical experiment.

### Observation and metric contracts

| Group | Required content |
|---|---|
| Identity/lineage | Export/observation ID, actual source and owner, revision/capture, integrity and exact test/arm/media/asset/destination/event/metric references |
| Population/unit | Eligibility/cohort, assignment and counting units, exclusions, aggregation, overlap, permitted linkage and deduplication basis |
| Quantity | Actual value and numerator/denominator, units/currency, cost/value basis, refunds/reversals, weighting and rounding |
| Time | Assignment/event/interaction/reporting clock, window boundaries/timezone, extraction, maturity cutoff, lag and restatements |
| Observation basis | Directly observed, provider-modelled, mixed or unavailable, method/version and exposed breakdown; independent knowledge state |
| Verification | Actual technical/qualification checks, coverage, duplicates/loss, permissions, owner and unresolved defects |
| Inference | Estimand, method/version, estimate/uncertainty, diagnostics, predeclared versus exploratory status, assumptions and decision scope |

Define what counts once, what qualifies as success, which clock applies, when follow-up matures, whether value is retained and whether units are independent. A changed event definition creates a visible comparability break unless a justified consistent reconstruction exists. A ratio with zero denominator is undefined; missing numerator or denominator is unavailable. Do not average subgroup ratios without the correct weighting and units.

Reconcile definitions before totals: entity, event, environment, period, maturity, attribution model, direct/modelled components, duplication and value/currency. Use only permitted evidenced matching or justified aggregate methods. Retain raw snapshots where permitted, version corrections, explained differences and unresolved residuals. Do not discard inconvenient rows or choose the larger report to make sources agree.

Keep platform-reported performance, business-verified outcomes and the analysis relating them separate. Add causal estimates only with their supporting design. Platform credits may overlap; the business ledger may contain organic outcomes. Neither their sum nor the full ledger is automatically caused by advertising. Distinguish not-collected, immature, privacy-limited/suppressed, lost, invalid, not-applicable and true observed zero.

### Attribution and causal scope

An attribution record identifies provider/model and version or captured methodology, eligible touchpoints, event/population, credit rules and windows, identity/aggregation, modelled composition, deduplication, value basis, cutoff/restatement, supplied uncertainty and proprietary limits. A changed model can redistribute credit without changing purchases. An attribution vendor's calculation remains external.

An incrementality claim additionally requires intervention/counterfactual, assignment or identifying assumptions, estimand, comparison population, observation coverage, estimator/uncertainty, compliance/exposure, interference, diagnostics, horizon and sensitivity. Creative A versus B is not ad versus no ad. Non-random matching, time series or geographical models must disclose their actual design, fit/placebo/sensitivity and transport limits; a “control” label is not randomisation.

Brand studies retain exact survey construct/question/scoring, comparison, response population/counts, nonresponse/weighting, horizon and absolute versus relative units. Attitudes and memory are not automatically revenue. Aggregated downstream analysis can be valid for its proper question without authorised person-level linkage; it cannot supply unsupported individual histories.

Apply validity and hard guardrails first, then maturity/threshold, then primary and downstream findings. Separate inference, creative preference, business recommendation and authority to enact it. Preserve invalid and inconclusive results with their learning; neither is automatically a losing concept. Request the smallest informative next test without releasing reserve or extending the test indefinitely.
<!-- /resource:measurement -->

<!-- resource:optimisation -->
## 10. Optimisation, fatigue, learning and preservation

A diagnosis starts with exact inputs, actual observations, evidence health and requested scope. A content defect can be established without performance data; absent data cannot establish poor market response. Triage delivery, audience, creative, placement, destination, policy/claims and upstream business alternatives before selecting a corrective layer.

| ID | Tracked record | Required content |
|---|---|---|
| LN.L01 | Parent concept | Exact territory/message/brief and commercial/audience baseline, mechanism, proof/CTA, fixed/open elements and actual selection evidence |
| LN.L02 | Variants | Exact concept/master/content or actual asset, requested/delivered fidelity, claims/qualifiers, locale/format/assembly, provenance and distinct use episodes with media/destination/configuration/time |
| LN.L03 | Changed elements | Before/proposed revisions, exact diff, reason/evidence, fixed elements, content versus configuration/data changes, dependency/approval consequences, owner and rechecks |
| LN.L04 | Audience/placement context | Three audience revisions, product/profile, inventory/device/modality, geography/timezone/window, offer/destination/goal, allocation and exclusions, actual/planned exposure units, distribution and overlap limits |
| LN.L05 | Results | Exact source-separated observation/analysis, comparison/criterion, numerator/denominator, cohort/maturity, uncertainty, attribution/causal scope, validity, guardrails and declared decision rule |
| LN.L06 | Learning | Question, observations, supported inference versus possible explanation/generalisation, contrary evidence, uncertainty, applicability, implication, action/owner and reuse/review triggers |
| LN.L07 | Lifecycle event | Exact subject/use scope, facet, prior/new value, effective and recorded time, reason, evidence and actual authority, conditions, review and downstream impact |

An asset can be used in several contexts. Identical bytes with a new platform ID are not a creative refresh; changed content under a stable ID still needs a revision. A successful parent does not transfer effectiveness, rights or approval to a child. Corrections preserve raw reports and withdrawn conclusions rather than deleting inconvenient history.

### Five independent lifecycle facets

| Facet | Values | Required evidence |
|---|---|---|
| Delivery | `proposed`, `active`, `paused`, `ended` | Actual authorised executor evidence for enabled/configured/observed serving as specifically stated; a request is not a completed action |
| Performance assessment | `untested`, `inconclusive`, `winner`, `loser`, `withdrawn` | Valid mature comparison under its declared criterion, population and horizon; preference-for-review is not a market winner |
| Evidence validity | `unreviewed`, `valid-for-scope`, `limited`, `invalid` | Exact validity findings and affected observation/analysis; invalid data cannot support new efficacy conclusions |
| Fatigue finding | `not-assessed`, `suspected`, `fatigued`, `not-supported` | Contextual exposure/outcome evidence and competing-cause review; operational diagnosis is not necessarily isolated causal wearout |
| Succession | `current`, `superseded` | Actual accepted replacement/adoption for a named scope; a planned replacement is not supersession |

Winner/loser are mutually exclusive only for the same criterion, comparison and period. A historically winning asset can later be fatigued, or remain current in one placement while superseded in another. Active does not prove an impression in every minute. A state change needs its own evidence; updated prose cannot pause a live campaign.

### Fatigue decision sequence

1. Identify the actual deterioration signal, outcome, baseline, criterion, timing and affected concept/variant/use episode.
2. Audit measurement validity, event definitions, cohort maturity, missingness and comparable cost/value basis.
3. Inspect exposure and context: population, dose/unit/window, mix, version changes, frequency distribution and overlap limits.
4. Compare plausible delivery, auction, audience, placement, destination, policy, offer and seasonal explanations using available evidence.
5. State the supported diagnosis and its strength: not-assessed, suspected, fatigued or not-supported. Do not infer a causal repetition effect from age, an average frequency, a platform rating or aggregate decline alone.
6. Choose the smallest justified investigation, treatment refresh, placement/control review or upstream referral. Define the contrast and rechecks before recommending new commitment.

A new ID does not reset memory. A declining aggregate can reflect changing mix while within-context response remains stable. Conversely, no detected decline is not proof that repetition never matters. Do not impose a universal refresh calendar or frequency threshold.

### Repair contract

Record the exact failed subject/revision and criterion, evidence, responsible layer and owner, intended correction, fixed elements and unaffected siblings, actual authority, required fidelity/output, changed dependencies and approvals, verification method and next decision. Obtain actual corrected outputs when the task requests a correction, not only a repair plan.

Compare before and after at both required byte and semantic levels. Reopen affected proof, qualification, brand, journey, policy, experiment or measurement checks. Preserve valid parents and siblings; a new offer or concept is an explicit new decision. For uncertain external effects reconcile the original request and exposure before retrying. A proposed rollback does not prove that money, messages or serving were reversed.

Keep observations, diagnosis, decision, action and generalisation separate. Reuse learning only within its evidenced context, with contrary findings and recheck triggers. “Always lead with price” cannot follow from one comparison. Respect retention and deletion constraints; preservation does not authorise indefinite retention of restricted data.
<!-- /resource:optimisation -->

<!-- resource:policy-and-actions -->
## 11. Legal, standards and platform-policy context

Policy context concerns an exact combination of facts, use and time. It does not create legal conclusions or replace the relevant specialist. A platform policy, a technical limit, a project preference and an applicable legal rule have distinct authority.

| ID | Field | Required content and acceptance boundary |
|---|---|---|
| PC.P01 | Jurisdiction | Relevant acts, parties, offered/targeted markets, medium, dates and factual basis; separate potentially relevant places from a specialist's actual applicability conclusion |
| PC.P02 | Advertising standard | Exact instrument/code/standard, issuer, edition, clause, medium/actor/scope and authority class; guidance, adjudication and law are not interchangeable |
| PC.P03 | Platform | Exact executor/product/placement/market, profile/policy revision, category/settings and review/appeal context; public documentation is not verified account capability or clearance |
| PC.P04 | Product category | Actual functionality/version, exchange, eligibility and relevant regulated-activity facts; legal and platform classifications have separate owners and uncertainty |
| PC.P05 | Claim type | Exact explicit/implied assertion, subject/population/time/comparator, proof and qualifications, rights and expressions; overall impression matters, not only literal words |
| PC.P06 | Targeting method | Actual context/query/list/retargeting/inference/expansion mechanism, source/purpose/recipient, profiling/data questions, exclusions/withdrawal and enforceability; consent and upload ability are different |
| PC.P07 | Policy source | Issuer/title/authority, canonical or controlled location, language, exact provision, version/capture, publication/update/cutoff, primary/secondary relationship, accessed scope and limitations |
| PC.P08 | Retrieved-at | Actual successful access date/time with timezone/precision, actor/method, exact source and accessed/inaccessible portions; failed access or crawl time is not a fresh verified read |
| PC.P09 | Valid-as-of/effective date | Requested assessment date, publication/update, actual application period, source coverage cutoff, retrieval, specialist valid-as-of, conditions/expiry and review trigger, all independently retained |
| PC.P10 | Campaign implication | Exact affected campaign/claim/variant/audience/placement/destination/event, required/prohibited behaviour, disclosure/control, owner, implementation evidence, decision and blocked scope |

Do not infer exemptions from labels such as B2B, education or open source, or legal classification from an app's name. Do not infer that contextual selection removes every measurement/privacy concern. Platform sensitive categories and statutory definitions need not coincide.

Before commitment verify material current assumptions against the applicable source, facts and period. A later retrieval does not make an older replaced rule effective again. A future announcement is not automatically current law; a flight crossing a verified change boundary needs an authorised transition/containment plan. Preserve partial dates, source coverage gaps and unknown transition rules. No universal “all sources expire after N days” rule is imposed.

When sources conflict: retain exact passages and dates; distinguish different scopes from true conflict; obtain the owning authoritative interpretation; map the resolution to affected outputs; inspect actual implementation and reopen only relevant decisions. Never select the most convenient, newest-looking or most numerous sources by default. Appeals must retain true facts; disguising categories, identities or destinations to evade review is not repair.

### Exact-fact Legal handoff

| Request component | Required content |
|---|---|
| H1 Identity/question | Request/revision, actual requester/recipient/remit, decision/use, deadline and exact question |
| H2 Facts/commercial baseline | Offer/product/price/renewal/refund/version, parties, markets, audience/category facts and approved source revisions |
| H3 Exact communication | Actual copy/visual/audio/sequence at required fidelity, explicit/implied claims, CTA and destination states |
| H4 Evidence/rights | Claim-proof mapping, methods/scope/contradictions, authenticity/use permissions and controlled access |
| H5 Targeting/data flow | Method, inclusions/exclusions, automation, source/purpose/recipient, storage/measurement, use/consent questions and controls |
| H6 Context/authorities | The first nine policy fields, exact provisions/versions, retrieved-at, proposed act date, conflicts and previous scoped decisions |
| H7 Proposed implementation | Disclosure/control by surface, modality, language, prominence/timing where relevant, fixed/changeable elements and sufficiency questions |
| H8 Unknowns/boundary | Missing facts, labelled assumptions, blocked actions, required return and separate resource/publication/spend scope |

The return must identify J1 actual issuer/remit; J2 exact facts/evidence inspected and not inspected; J3 assessed scope/time; J4 conclusion, issue, condition or escalation with reasons/source support; J5 required implementation and re-review triggers; J6 decision evidence, open matters and reuse/communication limits. Naming a Legal skill is not proof of availability, professional qualification, privilege or a completed legal review.

A conditional conclusion remains conditional. Review of one script does not approve a changed image, shorter disclosure, new jurisdiction or new data recipient. Advertising checks that the return answers the exact question and faithfully carries accepted constraints into the campaign; it does not promote that result into unrelated authority.

## 12. External execution request and return

Use this envelope for a concrete tool/provider/operator action. It may be part of an existing campaign record, not a new API or service.

| Field | Request contract |
|---|---|
| Q01 Identity/purpose | Request/revision, producer/recipient, consuming location, next decision and real/synthetic context |
| Q02 Exact baseline | Relevant brief/commercial/audience/claim/master/variant/media/destination/test/policy revisions and fixed/changeable scope |
| Q03 Actual operation | Actual tool/server/provider/action, version/profile, supported environment and inspected input/output schema |
| Q04 Data/recipients | Necessary fields/assets, access/rights, permitted host/model/provider recipients, retention/output access and secret references without values |
| Q05 Authority/resources | Actual scoped decision/delegation, subject/account/action, ceiling/currency/basis, attempts/concurrency, validity, constraints and stop owner |
| Q06 Preconditions | Required source/asset existence, accepted context, current profile/capability, enforced constraints, current remote state and blocking dependencies |
| Q07 Expected evidence | Required actual output/fidelity, receipts/identity, technical/craft/domain checks, coverage, read-back or observation horizon |
| Q08 Failure/change | Unknown-outcome handling, retry/idempotence evidence, cancellation/rollback or compensation limits, scoped repair and return owner |

| Field | Returned-evidence contract |
|---|---|
| U01 Binding | Exact request and actual inputs/operation, issuer and execution time with honest precision |
| U02 Outcome/receipt | Actual status, job/request/resource identity, protocol versus operation errors, partial or unknown outcome |
| U03 Output | Accessible actual file/payload/configuration, version/hash where available; generated/received/evaluated/accepted kept distinct |
| U04 Effects/cost | Known changes, actual/estimated charges and unresolved liabilities, data recipients, cancellation evidence and non-reversible effects |
| U05 Verification | Checks actually performed, method/coverage/result, relevant read-back/media/journey inspection and remaining findings |
| U06 Limits | Missing/skipped fields/files, unavailable observations, alternative explanations, unresolved rights/policy or scope changes |
| U07 Next decision | Whether the exact request is fulfilled, blocked action, smallest responsible repair and decision owner |

The nine external operation categories have these specific closure conditions:

| Category | Executor returns | Advertising must not infer |
|---|---|---|
| Account administration | Actual account/resource/permission state for the requested operation | Wider credentials, successful activation or commercial authority |
| Asset rendering | Actual files/components, provenance and technical/craft evidence | A requested job or preview is every required final asset |
| Campaign upload | Actual IDs, revision/placement mapping and activation state | Upload-only approval allows serving; coupled activation must also be authorised or the route rejected |
| Bidding/spend | Actual configuration/read-back, current liabilities and exposure | A plan or uncertain timeout is spare budget |
| Ad serving | Actual enabled/delivery observations with time, scope and limits | A proposal, pause request or selected concept changed live state |
| Data collection | Actual implemented observation and duplicate/loss/test-data checks | A specified event exists or a transport receipt is business success |
| Conversion tracking | Exact semantic/technical event tests, environment and coverage | A page visit is payment or an install is retained use |
| Attribution computation | Actual method/version, output, diagnostics, exclusions and uncertainty/limits | Allocated credit is causal incrementality |
| Hosting | Actual accessible endpoint/object/version, durability, rights and access/expiry evidence | A planned path or temporary provider URL is durable public publication |

Verify operation and side effects rather than trusting names or annotations. Unknown potentially billable/mutating outcomes are reconciled using their original identity before reissuing. A schema-valid response or checksum proves neither true meaning nor adequate control. Preserve successful siblings; correct the actual failed layer. Existing exact authority is reused within scope, while new effects or recipients need their owning decision.
<!-- /resource:policy-and-actions -->

## 13. Workflow acceptance and provenance

The work is correct only when the actual requested scope is fulfilled, the relevant models are complete, every material assertion and decision is traceable, required output and inspections exist, authority is respected, and actual repair preserves unaffected work. A completed audit may correctly reject its subject; record task fulfilment separately from subject readiness. The independent execution criteria and exact test inventory are in Spec 04.

This specification consolidates the accepted [brief model](research-logs/2026-09-10-stage-03-campaign-brief-audience-objective-model.md), [strategy model](research-logs/2026-09-10-stage-04-message-claim-proof-creative-strategy-model.md), [production model](research-logs/2026-09-10-stage-05-creative-production-cross-format-adaptation.md), [media/budget model](research-logs/2026-09-10-stage-06-media-placement-targeting-budget-model.md), [journey/handoffs](research-logs/2026-09-10-stage-07-destination-cross-domain-handoffs.md), [measurement model](research-logs/2026-09-10-stage-08-experiment-measurement-attribution-model.md), [learning model](research-logs/2026-09-10-stage-09-optimisation-fatigue-campaign-learning-model.md), [policy model](research-logs/2026-09-10-stage-10-legal-standards-platform-policy-handoffs.md) and [execution contracts](research-logs/2026-09-10-stage-12-execution-layer-tool-boundaries.md). It adopts their semantics without asserting that the researched external capabilities or actual campaigns were executed.

*Advertising Production Skills: Workflows and Artefacts Specification v1.0 · 10 September 2026*

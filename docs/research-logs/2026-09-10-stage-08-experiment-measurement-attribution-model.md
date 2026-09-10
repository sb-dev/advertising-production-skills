# Stage 8: Experiment, measurement and attribution model

Date: 10 September 2026  
Stage acceptance: PASS  
Working branch: `feat/bootstrap`  
Completion commit message: `docs: complete stage 8 experiment measurement and attribution model`

## 1. Goal, authority and verified inputs

Define a usable contract for advertising tests, the observations needed to interpret them, and the limits of attribution. The contract must distinguish a creative preference, an operational comparison, a supported causal conclusion and an authorised business decision. It does not execute an advertising campaign or implement an analytics platform.

The complete original [bootstrap][Bootstrap] was reread from `main` at entry. Authority is section 6 Stage 8, constrained by sections 1–3, 5, 8, 13 and 18–20. Original blob: `f72a6f167595d6f178550fb1e02c4885d875b6b2`; clean `main` baseline: `4a1d98843926c4aa0d68ed29ef55d9c8044dabe2`.

The resumed branch is the approved `feat/bootstrap`, not another attempt. Its head is Stage 7 commit `7b2d1d2574ac25336aef03a52c51035582e19408`, parent `6b4724fbe320873878c6505e95cbc35b90efcaa7`, tree `edca7276600404f80f56fa6769e358300d86bfdb`. Remote branch, commit metadata, complete tree, Stage 7 content and conformance were inspected. The comparison with Stage 6 is exactly one commit changing only the Stage 7 record and research index. All twelve existing file identities were recorded; earlier accepted records and the original remain unchanged. The index copy matches blob `9d5a97ffd44723d5e79a5c70a9d4c1a480644ea6`.

| Accepted input | Material consumed and preserved |
|---|---|
| [Stage 1][Stage1] | Business/Advertising/execution ownership, nine family boundaries, separate authority and smallest responsible repair |
| [Stage 2][Stage2], P07/P14–P22 | Event quality, qualified response, media operations, controlled testing, attribution, brand lift and independent QA |
| [Stage 3][Stage3], sections 3–9 | Exact baseline, source/knowledge/use distinctions, economics, event semantics, three audience layers and scoped readiness |
| [Stage 4][Stage4], M06–M08 and evidence chain | Fixed/changed dimensions, CTA commitment, message versus creative hypothesis, proof and selection limits |
| [Stage 5][Stage5], production/profile and acceptance contracts | Exact component/asset revisions, assembly controls, actual output versus proposal and contextual review coverage |
| [Stage 6][Stage6], M05–M10 and budget/acceptance model | Flight versus maturation window, exposure units, goal mapping, allocation, exclusions, liabilities and spend authority |
| [Stage 7][Stage7], all seven dimensions, handoffs and exit | Entry/destination revisions, promised action, event qualification, correlation, duplicates, technical evidence and unresolved branches |

The accepted connector-returned earlier records were reread against their unchanged current-tree identities. Stage 6's substantive media/budget model and the entire Stage 7 record were fetched again. Earlier research is not silently refreshed: the new public sources actually accessed for this stage are identified separately in [the Stage 8 source register][Sources8]. No prior failed branch is an implementation source.

## 2. Acceptance checklist and scope

| ID | Completion requirement | Governing reference |
|---|---|---|
| T01 | Define hypothesis, mechanism, population and intended effect | Stage 8: hypothesis |
| T02 | Define changed variables and preserved controls | Stage 8: changed variables; section 3 controlled variation |
| T03 | Define comparison, assignment and analysis units | Stage 8: comparison |
| T04 | Define primary metric with exact semantics and calculation | Stage 8: primary metric |
| T05 | Define guardrails, monitoring and escalation | Stage 8: guardrails; sections 3/13 |
| T06 | Define downstream business metric and observation horizon | Stage 8: downstream business metric |
| T07 | Define evidence threshold, feasibility and uncertainty | Stage 8: evidence threshold |
| T08 | Define confounders, validity checks and consequences | Stage 8: confounders |
| T09 | Define decision rule, inconclusive outcomes and authority | Stage 8: decision rule |
| M01 | Separate platform reports from verified downstream observations | Stage 8, second sentence |
| M02 | Define attribution context, interpretation and causal limits | Stage 8 title; sections 3/8/13 |
| G01 | Consume exact earlier baselines and preserve ownership/approvals | Sections 2–3/8/18; Stages 3–7 |
| G02 | Analyse professional practice, alternatives and cheap checks | Execution prompt sections 3–5/8; Stage 2 |
| G03 | Preserve truth, privacy boundaries, learning and local repair | Sections 3/13/19; execution prompt sections 5–7 |
| G04 | Verify substance, calculations, references and adverse cases | Execution prompt section 7 |
| G05 | Persist complete stage-only evidence and verify remote publication | Execution prompt sections 8–9 |

All nine test fields are mandatory for every test record. A small desk review may use categorical acceptance criteria rather than statistical thresholds, but must explain its comparison, metric, business relationship and limitations instead of leaving fields blank. A live performance experiment needs the additional operational/statistical detail appropriate to its claim.

The original requires a model definition here. It requires no fixed source count, generated advertisement, actual media experiment, minimum number of variants, primary example, Extension Pack, installed skill, benchmark run or platform integration in Stage 8. Those execution categories are NOT APPLICABLE, not waived for Stages 14–25. This record performs source research, method comparison, substantive contract design, synthetic arithmetic and documentation verification. It does not label any of those a live campaign test. Stage 9 retains campaign lifecycle/fatigue/learning design; Stage 10 retains legal/policy applicability; Stages 11–12 retain tool selection.

## 3. Professional-practice findings and approach selection

The researched practice is decision-led rather than dashboard-led. Google documents different assignment mechanisms and warns that in-flight changes complicate a campaign comparison. Its Conversion Lift and Brand Lift products answer different questions and have account-access conditions. Its data-driven attribution documentation describes account-specific credit allocation. These findings support retaining method, population, configuration and access evidence rather than assuming that anything called an experiment supplies the same inference. [R01] [R02] [R03] [R04]

Microsoft's experimentation practice checks sample-ratio mismatch before effect interpretation and diagnoses assignment, execution, logging and analysis causes. The Johari et al. abstract distinguishes fixed-sample inference from methods designed for continuous monitoring. NIST documents the large-sample two-proportion test; Penn State's retrieved teaching extracts provide power/sample-size and confidence-interval formulae. These support specific checks, not a mandatory platform, universal significance threshold or a promise that a larger sample cures biased data. [R05] [R06] [R07] [R08] [R09]

Gordon et al.'s original advertising-research abstract reports disagreement between the observational methods studied and randomised estimates. Its implication here is bounded: observational attribution must not be promoted to causal evidence without its identifying assumptions and validation. It does not establish that every observational or calibrated model is useless. Only the accessible abstract was used, not a replication of its data or full methods. [R10]

| Approach | Appropriate question and evidence | Choice and limit for this repository |
|---|---|---|
| Desk review / cheap concept comparison | Is meaning coherent, supported and feasible at the required fidelity? | USE as early uncertainty reduction; no invented consumer response or causal lift |
| Concurrent randomised A/B | What is the effect of assigning eligible units to one specified treatment rather than another? | USE when assignment, outcome collection and resources support the intended comparison |
| Randomised geographic/cluster comparison | What is the effect of the intervention at the assigned group level? | CONDITIONAL: require sufficient independent groups, interference assessment and compatible analysis, not impression-level pseudo-replication |
| Matched geography / other quasi-experiment | Can a credible counterfactual be constructed when randomisation is unavailable? | CONDITIONAL: explicit identification, pre-period/fit/sensitivity evidence and a specialist analysis contract; not automatically an RCT |
| Before/after or ordinary ad-set report | What changed during the observed periods or delivery contexts? | USE descriptively; time, mix and delivery changes prevent an automatic causal conclusion |
| Survey / brand-lift study | Did the specified awareness, association or recall construct change? | CONDITIONAL: exact instrument, sampling, comparison, non-response and study access; not a revenue result |
| Adaptive allocation / bandit | Can an authorised allocation policy improve reward while learning? | CONDITIONAL: record policy/history and use inference suitable to adaptation; allocation preference is not causal proof |
| Attribution / aggregate business modelling | How is observed value assigned or modelled across marketing activity? | REFERENCE external computation with scope/assumptions; do not build an attribution vendor or accept credit as self-validating incrementality |

These choices are original project design derived from the bootstrap and sources. They do not select a vendor or claim a head-to-head campaign was run. A multivariable or factorial experiment is permitted when its treatment, interactions and analysis are deliberate. The rule is controlled, interpretable variation, not a prohibition on testing complete creative systems.

Cheap commitment sequence: state the question; inspect the contrast and event map; check assignment and budget feasibility; freeze the analysis contract; obtain exact execution authority; inspect actual technical/assignment evidence; interpret mature observations; route the smallest justified decision. A source or platform recommendation cannot supply missing campaign approval.

## 4. Test record and nine required fields

The record may be a single readable Markdown document. It lives in the consuming project and references existing commercial, creative, media, destination and measurement records. No universal workflow engine, account store or manually maintained graph is required.

The header records test ID/revision, `real`/`synthetic` context, owner, question category, requested decision, exact brief/business/segment/hypothesis/claim/asset/media/destination revisions, source restrictions, planned and actual periods, analysis-plan version, executor/study identity if selected, approvals and unresolved dependencies. Preserve design, execution, observation, analysis and decision as separate records or clearly separated sections. Approval of one is not evidence that the next occurred.

### T01. Hypothesis

**Required content.** State the expected change, for whom, under which context, compared with what, and why the chosen advertising mechanism could produce it. Link the audience, message and creative hypotheses without merging them. Identify the outcome, direction, estimand (the precisely defined effect being estimated), supporting/contrary evidence, material assumptions and observations that would contradict or fail to resolve the hypothesis.

**Acceptance and owner.** Advertising owns campaign reasoning; the relevant study/measurement owner reviews inferential feasibility. The hypothesis must answer the accepted objective and preserve the approved offer and customer scope. For causal work, distinguish the effect of assignment to an advertising policy from the effect among people who happened to see or click an ad. The latter population can be selected by the treatment itself.

**Failure and repair.** “Variant B is better” without outcome/context/comparison is incomplete. Repair the question before producing variants or spending. A mechanism is a hypothesis, not customer evidence. A new segment, price or economic objective returns to its upstream owner.

### T02. Changed variables

**Required content.** List the exact treatment differences and fixed dimensions, with parent/revision references. Account for copy, claim meaning, proof presentation, concept, format, placement, audience representation, destination, bidding goal, budget/allocation, schedule, assembly/enhancement settings and measurement definition. Mark dimensions deliberately combined into one treatment; identify interactions when a factorial design is intended.

**Acceptance and owner.** Advertising verifies the semantic contrast; specialists and the executor confirm the actual delivered versions. A test of headline order must not also switch offer, eligibility, landing page or bidding event unnoticed. An automated optimiser or dynamic feed belongs in the treatment description when it can alter the exposure.

**Failure and repair.** Record an unplanned edit with time, affected units and scope. Restore/restart or limit the inference according to the frozen plan and technical evidence; do not silently relabel the changed intervention as the original test. Preserve both actual history and unaffected approved work. A composite-system test can remain valid for the composite effect while being insufficient to isolate a headline effect.

### T03. Comparison

**Required content.** Specify control/treatment versions; inclusion/exclusion rules; assignment mechanism and unit; intended allocation probabilities; timing; exposure rule; analysis unit; comparison population; interference/overlap handling; and whether analysis is by original assignment, actual exposure or another justified basis. Distinguish allocation of budget, auction opportunities, searches, devices, accounts and people. A 50/50 money allocation does not imply equal participant counts.

**Acceptance and owner.** The experiment/execution owner supplies assignment evidence; the analysis owner matches inference to that design. Persistent assignment can answer a different question from reassigning on every search; R01 is a provider example, not a guarantee of stable cross-device identity. The default causal question is the predeclared assignment-policy contrast. Any exposed-only, clicked-only or triggered analysis needs its own defensible eligibility and selection reasoning. [R01] [R05]

**Failure and repair.** Competing ad sets, equal spend or a favourable platform ranking are not proof of randomisation. Assignment-unit duplication, cross-arm contamination, mismatched eligibility or insufficient independent clusters blocks the claimed inference. Diagnose the relevant configuration/data/analysis layer, retain descriptive observations where trustworthy and never treat repeated impressions as independent assigned people.

### T04. Primary metric

**Required content.** Give a stable metric ID/version, purpose, exact event/construct, numerator, denominator, counting and deduplication unit, eligibility and exclusion rules, aggregation, direction, value/currency/cost basis where relevant, data owner, event-time/cohort convention, observation window, maturity rule and uncertainty method. Define a direct metric as precisely as a ratio. A survey metric also names its question/version and scoring rule.

**Acceptance and owner.** Advertising chooses a metric aligned to the objective; the technical/study owner supplies implementation and calculation evidence. Prefer one declared primary metric. Multiple co-primary metrics require a predeclared joint success and multiplicity rule, rather than selecting whichever later looks best. Keep diagnostic clicks or views separate from qualified response. Ratio metrics require uncertainty appropriate to their component dependence and assignment unit.

**Failure and repair.** Missing denominator, mixed units, changed event meaning or a proxy presented as the business outcome prevents interpretation. An unobserved denominator is not zero; a zero denominator makes the ratio undefined. Repair the definition or pipeline and keep the affected historical definition visible. No metric may be switched after results are seen and still be called the original confirmatory test.

### T05. Guardrails

**Required content.** Enumerate safety, truth/claim, targeting/data-use, commercial, customer-experience, capacity, delivery and measurement-validity conditions relevant to the test. Each has metric or exact predicate, threshold/bound and basis, monitoring cadence, observation owner, escalation/stop action, authority, response latency and affected scope. Identify hard prohibitions separately from risk preferences and statistical non-inferiority questions.

**Acceptance and owner.** Relevant business, Legal, technical and execution owners retain their decisions. Hard failures cannot be traded against CTR or a significant primary result. Safety monitoring continues even when the efficacy analysis is fixed-horizon. Automatic containment is permitted only when separately authorised and technically verified; this skill does not obtain it from a test plan.

**Failure and repair.** Stop recommending continuation when a hard condition fails, preserve the evidence and request authorised containment. A requested pause is not an observed pause. Absence of a recorded complaint is not proof of safety when observation is incomplete. A claim of statistical non-inferiority requires a justified margin and inference; a non-significant harm test does not supply it. [Bootstrap]

### T06. Downstream business metric

**Required content.** Link the primary advertising outcome to an exact business definition supplied upstream: qualified opportunity, retained/non-refunded purchase, contribution, retained usage, appropriately defined adoption or another approved outcome. Record entity/cohort, qualification, lag, completion/refund/cancellation handling, cost basis, ownership, availability, horizon and the decision it constrains. Preserve revenue, contribution, cash collection and projected lifetime value as different quantities.

**Acceptance and owner.** Business Building/project ownership defines value and trade-offs; Advertising interprets advertising evidence against them. A brand study can carry a longer-horizon business relationship without pretending each surveyed person can be linked to a sale. State when only aggregate downstream evidence is legitimately available. Lack of unit-level linkage need not invalidate a properly designed aggregate study, but does limit individual-level claims.

**Failure and repair.** More low-quality leads, cancellations or unaffordable fulfilment can defeat an apparently positive advertising result. Missing or immature downstream evidence blocks conclusions that depend on it, including profitable scaling. Return economics/capacity problems upstream; do not invent retention, match people without authority or treat all platform conversions as retained customers.

### T07. Evidence threshold

**Required content.** Predeclare the evidence sufficient for the intended decision: design-validity conditions; practical effect criterion; statistical framework if relevant; baseline/variance assumptions; target precision or power; allocation/sample rationale; minimum and maximum observation windows; maturation; uncertainty interval; multiple-comparison/subgroup handling; planned looks/stopping; and resource feasibility. State the distinction between minimum detectable effect, smallest effect worth acting on and an observed estimate.

**Acceptance and owner.** The analysis owner verifies the method and its assumptions; business ownership supplies the practical criterion and risk tolerance. A categorical desk review can require all named hard checks to pass without a p-value. A fixed-horizon experiment uses its predeclared endpoint; continuous efficacy decisions require an appropriate sequential method. Bayesian decisions identify prior, likelihood, posterior quantity, loss/decision rule and sensitivity rather than translating a frequentist p-value into a probability of success. [R06] [R07] [R08] [R09]

**Failure and repair.** More impressions, a platform learning label or an arbitrary number of days cannot substitute for the appropriate information. If feasible volume/budget cannot resolve the intended contrast, redesign the question or retain an explicitly exploratory scope; do not weaken the threshold after seeing results. An underpowered or immature result is not proof of no effect. Fixed-horizon power formulae are not reused blindly for clusters, adaptive allocation or sequential boundaries.

### T08. Confounders

**Required content.** Record each plausible alternative cause or validity threat, why it matters, which contrast/metric it affects, preventive control, observable diagnostic, residual uncertainty, owner and consequence. Cover changes in audience mix, seasonality, concurrent activity, creative/destination versions, bidding/delivery, consent or identity coverage, tracking, data joins, attribution settings, outcome lag, selection/non-response and interference where relevant. Use relevance-based coverage, not a compulsory catalogue of irrelevant risks.

**Acceptance and owner.** Distinguish a pre-existing confounder in an observational comparison, an implementation failure in a randomised design, a mediator caused by the treatment and ordinary random imbalance. Their remedies differ. Audit assignment/eligibility counts using the configured allocation; separately inspect event/observation loss. Outcome-dependent exclusions or reweighting cannot be introduced merely to erase an inconvenient sample-ratio mismatch. [R05]

**Failure and repair.** Unexplained assignment or differential logging failure blocks causal interpretation of the affected analysis. An imbalance in impressions or conversions alone is not an assignment SRM: the treatment may legitimately affect them. Preserve the raw observation provenance and diagnose before repair. A simultaneous market event limits a before/after comparison without necessarily invalidating a properly randomised concurrent comparison; document the relevant mechanism rather than declaring every concurrent activity fatal.

### T09. Decision rule

**Required content.** Write the ordered rule before execution, including invalid, harmful, supported, unsupported and inconclusive outcomes; early safety/resource stops; action scope; owner; next evidence; and preservation obligations. Define what happens at the maximum duration or budget limit when evidence remains insufficient. Separate an inferential conclusion, creative selection, a business recommendation and authority to enact it.

**Acceptance and owner.** Apply hard constraints and data/design validity first, then maturation/threshold, then primary result and downstream guardrails. A supported comparison can justify only the specified bounded next decision. Actual spend/reallocation/publication remains with the authorised executor under Stage 6; a positive result cannot release reserve automatically.

**Failure and repair.** Do not declare a winner by ranking point estimates, choose a new primary metric, keep extending an ordinary fixed-horizon test until it passes, or call “not significant” equivalence. Preserve an invalid test's findings as invalid evidence rather than as a losing concept. Record inconclusive honestly and propose the smallest additional evidence-producing step within authority. [R06] [Bootstrap]

## 5. Measurement contract and result reconciliation

### Observation record

Every imported observation retains its source, meaning and limitations. A verified downstream outcome is an observation that has passed the relevant business-definition and technical checks; it is not automatically an outcome caused by advertising.

| Group | Required content |
|---|---|
| Identity and lineage | Observation/export ID, source owner, source version or capture time, integrity reference when available, exact test/arm/media/asset/destination/event/metric revisions |
| Population and unit | Eligible population/cohort, assignment and counting units, inclusion/exclusion rules, aggregation level, known overlap, allowed correlation and deduplication basis |
| Quantity | Value, numerator/denominator where applicable, units, currency, value/cost basis, refunds/reversals and any weighting or normalisation |
| Time | Event versus interaction versus reporting time; window boundaries and timezone; extraction time; conversion lag, maturity cutoff and restatement rules |
| Observation basis | Directly observed, provider-modelled, mixed or unavailable; method/version and visible component breakdown; retain Stage 3 knowledge status separately |
| Verification | Technical checks actually performed, coverage, owner, qualification evidence, loss/duplicate diagnostics, consent/use constraints and unresolved defects |
| Inference | Estimand, estimator/method/version, effect and uncertainty, diagnostic status, planned versus exploratory analysis, assumptions and decision scope |

Provider-modelled or mixed values are not inherently unusable. Their method, provenance and intended use must be explicit. Do not reconstruct unavailable individuals, infer missing values from a rounded aggregate, or call a number independently verified because two reports reuse the same upstream event stream.

Preserve immutable source snapshots where permitted and record corrections as new versions. Personal data, account credentials and private source extracts stay with the authorised consumer/executor. Public repository examples contain only explicitly synthetic data. A deletion or data-use constraint is not bypassed to maintain an experiment; the observation loss and its analytical consequence are recorded.

### Metric and event dictionary

Stage 3's semantic event definitions and Stage 7's route/event mapping remain authoritative. Extend them with the analysis rules needed for this test, rather than renaming events to make conversion counts agree.

| Question | Rule required before interpretation |
|---|---|
| What counts once? | Stable permitted business/event identity and duplicate rules; one customer, order, request, device or survey response is not interchangeable |
| What counts as success? | Exact completion and qualification; failed requests, previews, test traffic and rejected transactions are excluded by predeclared rules |
| Which clock applies? | State assignment, event, interaction or reporting date basis; reconcile windows before comparing sources |
| Has the outcome matured? | Use the predeclared per-unit/cohort follow-up and late-arrival policy; an immature recent cohort is not a zero-performing cohort |
| Is value retained? | Preserve cancellations, refunds, chargebacks or qualification reversals under the business definition; report provisional and restated values distinctly |
| Are units independent? | Match estimator/uncertainty to assignment and dependence; repeated events and clustered units require appropriate treatment |
| Is the metric a ratio? | Retain numerator and denominator, zero/missing states and their dependence; do not silently average subgroup ratios |
| Is the definition comparable over time? | Exact version and change time; either reconstruct under a justified consistent definition or report incomparable periods separately |

A user-assignment experiment can estimate an assignment-policy effect even when not every assigned unit is served an ad. Do not replace its denominator with clicks or observed conversions after the fact. Conversely, an operational CTR report is allowed when explicitly defined as clicks per eligible counted impression; that does not make its rows independent people or its difference the same estimand as conversions per randomised unit.

### Reconciliation workflow

First compare source definitions, not totals. Check entity, qualifying event, environment, time basis, window, maturity, attribution method, modelled component, duplicate policy and value/currency basis. Match source records only through a permitted, evidenced key or a justified aggregate method. Account for known differences, retain unexplained residuals, and assign their investigation to the relevant data owner. Do not force reconciliation by deleting inconvenient rows or choosing the larger report.

Keep at least three independently labelled outputs: platform-reported performance, business-verified outcomes, and the analysis that relates them. Add a causal estimate only when supported by the study. Multiple platforms can claim overlapping credit; a downstream ledger may also contain organic outcomes. Neither the sum of platform credits nor all observed ledger activity is automatically advertising-caused. R04 describes attribution as credit allocation; the counterfactual question remains separately specified. [R04] [R10]

Missingness must distinguish not collected, not yet mature, privacy-limited/suppressed, lost, invalid, not applicable and true observed zero. For modelled/mixed reports, record what the provider exposes and what cannot be separated. An inaccessible breakdown is an evidence limitation, not a licence to invent a direct-observation fraction. Assess differential observation by arm; a common-looking reporting gap is not assumed harmless without evidence.

## 6. Attribution, incrementality and business interpretation

### Attribution record

An external attribution result records provider/model identity and revision or captured methodology; eligible channels/touchpoints; source event and population; click/view or other credit rules; lookback/conversion windows; identity/aggregation basis; direct/modelled composition; cross-source deduplication scope; value basis; data cutoff/restatements; uncertainty where supplied; and known omissions. If a proprietary method withholds details, state the limit. Do not fill it from another vendor's documentation.

Attribution output can support reporting and operational choices within its assumptions. A configured model change may redistribute credit without changing underlying purchases. Compare like-for-like definitions or explicitly label the break. Google documents account-specific allocation and bidding interaction, but that public description is not an independent audit of a particular account. [R04]

### Causal interpretation contract

For an incrementality claim, additionally retain the intervention and counterfactual; assignment/identification design; estimand; treatment/control population and observed eligibility; observation coverage; estimator and uncertainty method; compliance/exposure differences; interference assumptions; validity diagnostics; analysis horizon; and sensitivity/limitations. A randomised ad-versus-no-ad policy is not the same contrast as creative A versus creative B. Positive A-versus-B evidence does not prove either beats no advertising.

A geographic study must identify its independent assigned groups, spillover risks and pre-period information if used. A non-random matched or time-series model must state the assumptions that identify the effect, relevant fit/placebo/sensitivity evidence and limits of transport to the present decision. Do not claim randomisation because groups were labelled control and treatment. External analysts own computation; Advertising checks whether the returned conclusion matches the campaign question and available evidence. [R02] [R10]

A brand-lift record names the survey construct, question/version, comparison, response population, sample counts, response/weighting limitations and absolute versus relative units. Survey attitudes remain survey attitudes; they are not silently converted into revenue. The Google overview describes such outcome distinctions and restricted feature access; it does not establish that the consuming project can run the study. [R03]

### Quantities that must not be conflated

| Quantity | Meaning and condition |
|---|---|
| Attributed conversions/value | Credit under the identified attribution rules; can be fractional, overlapping across providers or modelled |
| Verified business outcomes | Qualified distinct business events under their definition and horizon; not necessarily caused by advertising |
| Absolute effect | Difference on the declared outcome scale, with uncertainty and the correct comparison population |
| Relative lift | Absolute effect divided by the relevant baseline; undefined at zero baseline and potentially unstable near zero |
| Attributed ROAS | Attributed value divided by the identified advertising-spend basis; neither contribution margin nor automatic causal return |
| Incremental ROAS | Estimated incremental value divided by the appropriate spend denominator for the defined intervention; report denominator and uncertainty explicitly |
| Incremental CPA | Relevant spend divided by estimated incremental conversions; zero/negative or uncertain-near-zero incrementality does not yield a reliable acquisition-cost claim |
| Contribution/payback | Upstream business-defined value/cost/horizon measure; cannot be manufactured from platform revenue alone |

For an ad-on versus ad-off intervention, the spend denominator may be intervention spend relative to the no-ad control; for changing budgets/policies it may require incremental spend or another specified comparison basis. Never silently mix definitions. Google itself distinguishes user- and geography-based lift outputs; this model requires the exact study definition rather than a universal ratio. [R02]

Do not report a negative incremental CPA as cheap acquisition when incremental conversions are negative. Record the effect and its uncertainty; mark the acquisition-cost interpretation undefined or unreliable for that scope. Ratios with uncertain denominators require a suitable analysis method, not a point-estimate division presented as a confidence interval. No one-number campaign quality or profitability score is introduced.

## 7. Validity, commitments and bounded repair

### Preflight and analysis gates

| Gate | Evidence required | Failure consequence |
|---|---|---|
| Design acceptance | Complete T01–T09; exact accepted inputs; feasible comparison and observation; chosen evidence framework | Repair missing semantics or retain explicitly exploratory/non-execution scope |
| Execution readiness | Actual accepted assets/destination; verified relevant event/assignment behaviour; current constraints; precise budget/data/publication authority | No launch or spend recommendation relying on absent implementation or permission |
| Run integrity | Actual versions/configuration and assignment history; eligibility/observation diagnostics; interventions, exposure and cost records | Investigate affected periods/units; request authorised containment where required |
| Analysis readiness | Frozen/declared analysis version; source snapshots; reconciled definitions; appropriate follow-up; resolved material validity issues | Preserve descriptive evidence but block unsupported efficacy/business inference |
| Decision acceptance | Predeclared rule applied; effect/uncertainty and guardrails; verified downstream evidence for the requested commitment | Record supported, unsupported, inconclusive or invalid conclusion with bounded action and owner |

Use PASS, FAIL, BLOCKED or justified NOT APPLICABLE for conformance findings. Inferential conclusion labels are not replacement project lifecycle states. A generic model can pass while a particular test is correctly blocked. Pactwright's lifecycle authority remains external and optional.

Sample-ratio checks compare observed counts of the eligible assignment units with the intended assignment probabilities. They do not demand that conversions, spend or impressions be exactly balanced. A flagged check is a reason to diagnose; passing it is not proof of total validity. Preserve assignment, execution, log-processing and analysis hypotheses separately, as motivated by R05. Do not rebalance the reported arms merely to make the diagnostic pass. [R05]

Maintain a change record with revision, reason, owner, timestamp, affected arms/populations, fixed elements, cost/authority consequence and required rechecks. Predeclared safety containment may interrupt the test without yielding an efficacy answer. Record the actual stop only after the executor returns evidence. An unaffordable sample cannot justify releasing reserve or extending a flight without authority.

| Failure layer | Smallest responsible action | What remains preserved |
|---|---|---|
| Unclear hypothesis or metric | Advertising/analysis owner repairs the question or definition before commitment | Accepted offer, supported claims and source evidence |
| Wrong or changing creative treatment | Advertising and specialist/executor restore or version the affected treatment | Valid parent concept and unaffected assets; actual exposure history |
| Assignment/eligibility fault | Executor investigates assignment and constraints; analyst reassesses inference | Raw evidence and earlier approved commercial boundaries |
| Missing, duplicate or misqualified event | Software/analytics repairs event pipeline and validates the affected mapping | Approved creative; original invalid/provisional observations remain labelled |
| Attribution/window mismatch | Data owner supplies compatible extracts or limits comparison | Original source reports and their definitions |
| Insufficient or immature evidence | Apply inconclusive/blocked decision; propose an authorised new evidence step | Rejected/untested hypotheses are not rewritten as proven losers |
| Positive proxy with downstream risk | Business owner evaluates economics, qualification or capacity | Accurate platform and business observations kept distinct |
| Claim, targeting or safety violation | Route for authorised containment and appropriate Legal/data/business review | Exact affected facts, scopes, decisions and unrelated valid work |

An analysis handoff asks the external owner for inputs, method/version, code or reproducible calculation reference where permitted, diagnostics, uncertainty, limitations and actual outputs. A tool's successful exit, a screenshot of a dashboard or an AI summary alone cannot prove the returned analysis matches this contract. Repository-write authority authorises these research commits, not any advertising account mutation.

## 8. Synthetic worked contract

`SYN-EXPERIMENT-08@1` is an independent, explicitly synthetic model specimen. It does not modify the Stage 7 fixture or create a real campaign. The fictitious source supplies a two-hour online workshop with a workbook for UK adults at GBP 40 one-off; it supports those stipulated terms only. No product outcome, testimonial, legal clearance, actual user data, platform access or spending authority exists. The fixture authority permits document and arithmetic inspection only.

Exact proposed control text A: **“Two-hour online workshop. Workbook included. £40 one-off. View workshop details.”**

Exact proposed treatment text B: **“Workbook included. Two-hour online workshop. £40 one-off. View workshop details.”**

These are cheap text representations, not rendered or served advertisements. Both use the same fixture details-state requirement, offer, proof limits and CTA. Only the ordering/emphasis of two supported facts changes. No financial-benefit claim or changed price is introduced.

| Required field | Filled specimen |
|---|---|
| T01 hypothesis | For the stipulated eligible audience/context, workbook-first rather than duration-first emphasis may increase qualified information requests per assigned unit by making included scope more noticeable. This mechanism is unvalidated; the estimand is the assignment-policy difference, not the effect among clickers |
| T02 changed variables | Swap the first two factual sentences. Preserve all commercial terms, claims, audience, format/placement assumptions, destination, bidding/event definitions and allocation. Unverified assembly is a blocking implementation dependency |
| T03 comparison | Proposed concurrent 1:1 persistent random assignment of eligible units to A/B; analyse by original assignment. The actual identity/assignment executor and interference controls must be verified before use; no real assignment occurred |
| T04 primary metric | Fraction of assigned eligible units making at least one valid qualified information request within seven days of assignment. One success maximum per unit; failed/test/duplicate requests do not count. A details view is diagnostic, not a request |
| T05 guardrails | No unsupported claim, forbidden delivery, unapproved data use or spend; no price/CTA discrepancy. Technical loss, capacity and customer-harm monitoring require actual owner thresholds/evidence before live readiness. No statistical no-harm assertion is made from absent complaints |
| T06 downstream metric | Retained, non-refunded paid bookings within thirty days of assignment, defined and verified by the fictitious business source. This is separate from information requests; no actual observation or profitability claim is supplied |
| T07 threshold | Proposed fixed-horizon analysis, two-sided 95% interval; primary support requires lower bound above zero and point estimate at least +0.5 percentage points. Planning assumptions are 2% versus 3%, independent binary units, 1:1 allocation, 5% two-sided size and 80% power. Approximate requirement is 3,827 units per arm; proposed collection target is 12,000 eligible units in total, with 6,000 per arm expected rather than enforced as outcome-dependent quotas. These are synthetic assumptions, not forecasts. Actual cost/volume feasibility remains unverified |
| T08 confounders | Check actual assignment/identity, eligibility, loss/duplicates, arm overlap, identical destinations/goals, attribution definition, concurrent mix changes and seven-/thirty-day maturation. A platform-impression imbalance is not itself an assignment fault |
| T09 decision rule | Hard failure requests authorised containment; invalid data blocks efficacy; insufficient/maturing evidence is inconclusive. At a predeclared resource/time stop, do not extend until significant. Primary support permits only a bounded recommendation; commercial scaling additionally requires mature acceptable downstream evidence and actual authority |

The hypothetical collection window is the half-open interval `[2026-10-01T00:00:00+01:00, 2026-10-15T00:00:00+01:00)` in Europe/London. End collection at 12,000 total eligible assignments or the fixed calendar endpoint, whichever occurs first, independently of observed efficacy. Retain actual arm counts under the proposed 1:1 randomisation; do not close one arm selectively to manufacture equal denominators. The fixture stipulates a 48-hour data-latency allowance, not a provider guarantee. Analyse the primary outcome only after the last included unit has seven elapsed days plus that allowance; thirty elapsed days plus the allowance apply to the business metric. Check actual information and maturation before applying the decision rule; reaching the calendar endpoint alone cannot establish sufficiency. Elapsed durations, not a repeated local-clock label, govern follow-up across daylight-saving changes. No flight is actually scheduled. An earlier resource/safety stop does not automatically make a fixed-horizon result confirmatory.

The specimen is complete for inspecting the model and exposes its real-execution blockers: absent approved account controls, verified event implementation, current applicable constraints, cost/volume feasibility and actual authority. It is not marked launch-ready. Missing live inputs are not missing generic Stage 8 definitions.

### Calculated evidence probes

The following aggregate counts are stipulated independently to check arithmetic and decisions, not observed from a campaign. The normal approximations assume independent binary units and sufficiently populated cells. Fractional attributed conversions, repeated impressions, clusters and missing denominators cannot be inserted into this calculation as though they satisfy those assumptions. The source basis is R07–R09, with no claim of full-method replication beyond these equations.

| Probe | Synthetic inputs | Calculated finding and model decision |
|---|---|---|
| N01 sample planning | Rates 0.02 and 0.03; two-sided alpha 0.05; power 0.80; equal independent groups | Pooled normal planning approximation gives 3,827 per arm, 7,654 total; no delivery or budget feasibility is inferred |
| N02 positive point estimate | A: 120/6,000; B: 150/6,000 | Difference +0.5 percentage points; 95% interval −0.030610 to +1.030610 percentage points; two-sided p ≈ 0.064800. INCONCLUSIVE, not a winner |
| N03 primary supported, business absent | A: 120/6,000; B: 180/6,000; downstream data unavailable | Difference +1 percentage point; 95% interval +0.441611 to +1.558389 percentage points; p ≈ 0.000451. Primary criterion met; business-scaling conclusion BLOCKED |
| N04 assignment imbalance | Proposed 1:1; observed assigned-unit counts 6,600 and 5,400 | Chi-square statistic 120 on one degree of freedom; diagnostic p is extremely small. Investigate before causal interpretation, not automatic row deletion |
| N05 undefined ratios | Relative lift with baseline zero; incremental CPA with zero/negative incremental conversions | No finite reliable acquisition/relative-lift claim; preserve absolute effect, uncertainty and explicit undefined reason |
| N06 overlapping reporting | Platform P reports 100; Q reports 80; business records 120 distinct completions and 100 retained after 20 reversals; overlap unknown | Do not call 180 unique or incremental customers, assign unexplained differences to a provider, or infer all business events were advertising-caused |

The power approximation addresses rejecting equality at a stipulated one-percentage-point effect, not proving that every accepted effect exceeds a practical margin with 80% probability. The specimen separately uses a point-estimate practical criterion. A decision requiring the interval's lower bound to exceed a non-zero margin would require its own sizing and threshold design. This distinction prevents a convenient sample-size number from silently answering a different question.

The arithmetic can be reproduced with Python's standard library:

```python
from math import ceil, erfc, isfinite, sqrt
from statistics import NormalDist

normal = NormalDist()
z95 = normal.inv_cdf(0.975)
zpower = normal.inv_cdf(0.80)
p0, p1 = 0.02, 0.03
pbar = (p0 + p1) / 2
per_arm = ceil(2 * (z95 + zpower) ** 2 * pbar * (1 - pbar) / (p1 - p0) ** 2)
assert per_arm == 3827


def compare_binary(n_a: int, x_a: int, n_b: int, x_b: int) -> tuple[float, float, float, float]:
    values = (n_a, x_a, n_b, x_b)
    if any(type(v) is not int for v in values):
        raise ValueError("Independent binary counts must be integers")
    if not (n_a > 0 and n_b > 0 and 0 <= x_a <= n_a and 0 <= x_b <= n_b):
        raise ValueError("Invalid counts or denominator")
    if min(x_a, n_a - x_a, x_b, n_b - x_b) < 10:
        raise ValueError("This probe does not support sparse-cell normal inference")
    a, b = x_a / n_a, x_b / n_b
    delta = b - a
    se = sqrt(a * (1 - a) / n_a + b * (1 - b) / n_b)
    pooled = (x_a + x_b) / (n_a + n_b)
    z = delta / sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
    return delta, delta - z95 * se, delta + z95 * se, erfc(abs(z) / sqrt(2))


weak = compare_binary(6000, 120, 6000, 150)
strong = compare_binary(6000, 120, 6000, 180)
assert weak[1] < 0 < weak[2] and weak[3] > 0.05
assert strong[1] > 0 and strong[0] >= 0.005 and strong[3] < 0.05
assert abs(weak[1] - (-0.0003060995034020993)) < 1e-12
assert abs(strong[1] - 0.004416108815413695) < 1e-12
expected = (6600 + 5400) / 2
chi2 = sum((x - expected) ** 2 / expected for x in (6600, 5400))
assert chi2 == 120 and erfc(sqrt(chi2 / 2)) < 0.001
assert 120 - 20 == 100 and 100 + 80 != 120


def positive_basis_ratio(numerator: float, denominator: float | None) -> tuple[float | None, str]:
    # Synthetic N05 probe, not a general attribution or uncertainty estimator.
    if denominator is None:
        return None, "missing denominator"
    if not isfinite(numerator) or not isfinite(denominator):
        return None, "non-finite input"
    if denominator == 0:
        return None, "zero denominator"
    if denominator < 0:
        return None, "negative denominator: no acquisition-cost interpretation"
    return numerator / denominator, "point ratio only; uncertainty not assessed"


assert positive_basis_ratio(0.01, 0)[1] == "zero denominator"
assert positive_basis_ratio(100, -5)[0] is None
assert positive_basis_ratio(100, None)[1] == "missing denominator"
assert positive_basis_ratio(100, 5)[0] == 20
print("N05 zero/negative/missing denominator distinctions: PASS")
for bad in [(0, 0, 6000, 150), (6000, 1, 6000, 2), (6000, 120.5, 6000, 180)]:
    try:
        compare_binary(*bad)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid normal-inference input was accepted")
print("Synthetic arithmetic checks passed; no campaign executed.")
```

The sparse-cell guard is a conservative applicability check for this illustration, not a universal advertising threshold or the implementation of an analysis service. A suitable exact, cluster-aware or other method remains the external analyst's responsibility where this approximation is inappropriate.

## 9. Semantic inspections

These are manual inspections of this model using explicitly synthetic challenges. Each checks a concrete contract consequence and owner. PASS means the written model handles the challenge correctly; it does not mean a live campaign, website, statistical service or installed skill was tested.

| Case | Challenge inspected | Observed model response and bounded repair | Result |
|---|---|---|---|
| Q01 | Prefer B because its rate is 2.5% rather than 2%, ignoring uncertainty | T07/T09 and N02 retain the interval and return inconclusive; no winner by rank | PASS |
| Q02 | An A-versus-B comparison is described as proof that advertising beats no advertising | Section 6 distinguishes the counterfactual; limit the conclusion or design the needed comparison | PASS |
| Q03 | Replace the approved audience restriction with a platform optimisation signal | T02/T03/T05 preserve Stage 3/6 constraints; block dependent execution and return mapping to its owner | PASS |
| Q04 | Test many metrics, then promote the best-looking one to primary | T04/T07 require predeclared joint/multiplicity rules; label post-hoc findings exploratory | PASS |
| Q05 | Compare a mature control cohort with a recent treatment cohort as if both had full follow-up | T06 and section 5 retain maturity per cohort/unit; wait for the required evidence or limit interpretation | PASS |
| Q06 | Repeatedly inspect an ordinary p-value and stop at the first success | T07/T09 require fixed or valid sequential rules; do not claim the original error guarantee | PASS |
| Q07 | A fixed-horizon rule is used to forbid stopping an unsafe test | T05/T09 allow authorised safety containment; preserve the resulting limits on efficacy inference | PASS |
| Q08 | Cheaper sign-ups are used to justify scale despite missing qualification/retention | T06/T09 block the business conclusion; obtain downstream evidence without changing the commercial baseline | PASS |
| Q09 | Negative incremental conversions produce a negative CPA called cheap acquisition | Section 6/N05 reject that interpretation; retain signed effect and uncertainty | PASS |
| Q10 | Randomising every search is described as persistent person-level assignment | T03 requires actual assignment/identity semantics and overlap limits; correct the design description | PASS |
| Q11 | Unequal impressions trigger an assignment-SRM failure despite correct eligible-unit assignment | T08/section 7 separate assignment counts from treatment-affected delivery outcomes | PASS |
| Q12 | Assignment SRM is fixed by deleting excess treatment records | T08/section 7 require root-cause diagnosis and preserve data; do not manufacture balance | PASS |
| Q13 | Fractional modelled conversions are inserted into an independent binary-count test | T04/section 5 and arithmetic validation reject incompatible input; use a suitable external method | PASS |
| Q14 | Twelve assigned regions are analysed as hundreds of thousands of independent impressions | T03/T07 require the actual cluster unit and compatible uncertainty; no pseudo-replication | PASS |
| Q15 | Outcome windows use report date for one arm and event date for the other | T04/section 5 require compatible clock/window definitions; obtain correct extracts or keep the comparison limited | PASS |
| Q16 | An attribution-model change redistributes credit and is reported as newly generated revenue | Section 6 keeps observed business events distinct; report the model break rather than inventing growth | PASS |
| Q17 | Two platforms sharing the same event feed are called independent corroboration | Section 5 records source lineage and overlap; two displays do not establish independent evidence | PASS |
| Q18 | Restrict analysis to clickers after a creative changes who clicks | T01/T03/T08 require selection/estimand reasoning; retain assignment analysis or justify a different question | PASS |
| Q19 | Change price and headline together, then claim a headline-only effect | T02 retains the actual combined treatment; reject the narrow claim or redesign with the approved price | PASS |
| Q20 | An AI panel preference is recorded as customer validation | T01/section 3 identify desk review limits; keep synthetic judgement separate from consumer evidence | PASS |
| Q21 | A persuasive result is used to average away an unsupported claim or forbidden targeting | T05/T09 put hard constraints first; request authorised containment and specialist repair | PASS |
| Q22 | A bounded claim-consistency review omits the nine test fields because it has no p-value | Section 2/T07 allow categorical thresholds, not missing comparison or business relevance | PASS |
| Q23 | A sample calculation for rejecting equality is called proof of exceeding a practical margin | T07 and section 8 explicitly separate the questions; resize/redefine the evidence contract when the decision changes | PASS |
| Q24 | A significant primary result is treated as authority to release budget reserve | T09 and section 7 preserve Stage 6 authority; a recommendation is not an executed spending decision | PASS |

## 10. Conformance and verification record

Verification is against the original Stage 8 contract and applicable global principles, not merely this document's headings. Each mandatory field was inspected for meaning, exact content, dependencies, owner, evidence and failure consequence. The review also traced platform/business/causal distinctions, source access limits, downstream maturity, independent assignment units, attribution denominators, authority and preservation.

| Requirement | Specification reference | Deliverable / evidence | Verification performed | Result |
|---|---|---|---|---|
| T01 hypothesis | Stage 8 | Section 4 T01; specimen; Q02/Q18/Q20 | Inspect mechanism, estimand, population and evidence limits | PASS |
| T02 changed variables | Stage 8; section 3 | Section 4 T02; exact A/B text; Q03/Q19 | Inspect fixed/changed scope, dynamic execution and actual-version history | PASS |
| T03 comparison | Stage 8 | Section 4 T03; approach matrix; Q10–Q14/Q18 | Inspect assignment versus delivery, analysis unit and counterfactual | PASS |
| T04 primary metric | Stage 8 | Section 4 T04; dictionary; Q04/Q13/Q15 | Inspect formula, denominator, qualification, clock and multiplicity | PASS |
| T05 guardrails | Stage 8; sections 3/13 | Section 4 T05; gates; Q07/Q21/Q24 | Inspect hard constraints, monitoring, response and authority | PASS |
| T06 downstream business metric | Stage 8 | Section 4 T06; specimen; Q05/Q08 | Inspect qualification, retention, maturity and business ownership | PASS |
| T07 evidence threshold | Stage 8 | Section 4 T07; N01–N03; Q01/Q06/Q23 | Inspect practical/statistical distinctions, sizing and stopping assumptions | PASS |
| T08 confounders | Stage 8 | Section 4 T08; validity gates; Q10–Q18 | Inspect alternative causes, assignment/logging faults and local repair | PASS |
| T09 decision rule | Stage 8 | Section 4 T09; specimen; Q01/Q06–Q08/Q24 | Inspect ordered outcomes, inconclusive handling and bounded action | PASS |
| M01 platform versus downstream | Stage 8 second sentence | Section 5; N06; Q05/Q08/Q15–Q17 | Inspect source lineage, reconciliation, missingness and causal distinction | PASS |
| M02 attribution model | Stage 8 title; sections 3/8/13 | Section 6; approach matrix; N05; Q02/Q09/Q16 | Inspect method/window/units, counterfactual and ratio limits | PASS |
| G01 prior inputs and authority | Sections 2–3/8/18 | Sections 1/4/7; exact predecessor/tree; Q03/Q19/Q24 | Inspect preserved revisions and business/domain/execution boundaries | PASS |
| G02 practice and alternatives | Execution prompt sections 3–5/8 | Section 3; ten-source register; cheap commitment sequence | Inspect actually accessed evidence, eight approaches and explicit limitations | PASS |
| G03 truth and smallest repair | Sections 3/13/19 | Sections 5–9; eight repair routes; synthetic labels | Inspect no fabricated campaign/approval and affected-scope repairs | PASS |
| G04 actual verification | Execution prompt section 7 | Semantic cases; numerical code/output; structural check record | Inspect all definitions, execute calculations and check document/reference integrity | PASS |
| G05 durable stage-only publication preparation | Execution prompt sections 8–9 | Model, source register and index | Check exact changed-path set and final acceptance consistency before commit | PASS |
| Live experiments, generated media, packs, primary examples, installed skills and benchmarks | Stage 8 definition versus Stages 14–25 | Section 2 applicability | No such execution requirement in Stage 8; none claimed here | NOT APPLICABLE |

### Executed verification

The original Stage 8 sentence, its second-sentence reporting distinction and the surrounding stage/execution boundaries were fetched again from `main` during exit review. The original blob remained `f72a6f167595d6f178550fb1e02c4885d875b6b2`. All nine definitions were compared with the literal requirements, not only this record's checklist. All twenty-four manual semantic inspections were traced through the final contract. The conformance has sixteen PASS rows and one justified NOT APPLICABLE row.

The review corrected a fixture ambiguity between expected per-arm sample size and collection stopping. The final specimen targets 12,000 total assignments under 1:1 randomisation rather than enforcing equal arm quotas. It now declares exact half-open calendar boundaries and a synthetic 48-hour latency allowance. Follow-up is measured in elapsed time so daylight-saving changes cannot silently shorten the business window. The denominator probe now executes distinct missing, zero and negative cases rather than leaving that distinction only in prose.

Executed Python verification contains 45 passing checks. It covers nine complete test definitions, sixteen acceptance requirements, eight approach comparisons, five readiness gates, eight repair routes, seven observation groups, eight event/metric questions, eight distinct quantities, nine filled fixture fields, six numerical/interpretation probes, twenty-four semantic cases and all ten source entries with provenance and limits. It checks all three intended files, Markdown tables/fences, source labels, 32 local/reference targets, baseline-index identity, final acceptance/index consistency and the exact three-file change set. Four deliberate negative mutations confirm detection of a missing definition, duplicate semantic case, nonexistent local file and unresolved source label.

The exact embedded Python block was executed, not merely inspected. It produced the N01–N04 arithmetic and N05 denominator distinctions, checked N06 reconciliation arithmetic, and rejected zero-denominator, sparse-cell and fractional-count inputs. Results were 3,827 planned units per arm; N02 difference 0.005 with interval [-0.0003060995034020993, 0.0103060995034021] and p 0.06480010307396632; N03 difference approximately 0.01 with interval [0.004416108815413695, 0.015583891184586302] and p 0.00045109534761430625; and assignment diagnostic statistic 120. Code SHA-256: `91567946f569225a39d887c75ffbf8b38ab88263ae5a185152b6234632479033`.

These are documentation, arithmetic and synthetic contract checks, not measured campaign effects, a live statistical platform, generated-ad evaluation, legal clearance or an installed-skill benchmark. The prior-file identity map comes from the complete remote tree; only the baseline index was copied locally, and its original blob matched exactly. Publication must preserve all other prior remote blobs and match the three inspected output hashes before Stage 9 begins.

## 11. Exit and next-stage input

All mandatory Stage 8 model-definition requirements pass. No unresolved model question, required missing source, failed prerequisite, user-owned decision or scope waiver remains. Only this model, its source register and the research index change. The original, root README and accepted Stage 1–7 records remain preserved. The stage-only completion commit must parent `7b2d1d2574ac25336aef03a52c51035582e19408`. Verify branch head, ancestry, complete tree and intended content identities before Stage 9.

Stage 9 receives exact experiment/variant/context identities, fixed/changed dimensions, source-separated observations, metric versions, maturation/validity findings, bounded decisions and preserved invalid/inconclusive evidence. It must independently define concept/variant lineage, changed elements, audience/placement context, results, learning and lifecycle including fatigue and supersession. This model does not claim to implement those lifecycle responsibilities or promote project maturity.

[Bootstrap]: 2026-09-08-advertising-production-skills-new-project-bootstrap-process.md
[Stage1]: 2026-09-10-stage-01-domain-boundaries.md
[Stage2]: 2026-09-10-stage-02-professional-advertising-practice.md
[Stage3]: 2026-09-10-stage-03-campaign-brief-audience-objective-model.md
[Stage4]: 2026-09-10-stage-04-message-claim-proof-creative-strategy-model.md
[Stage5]: 2026-09-10-stage-05-creative-production-cross-format-adaptation.md
[Stage6]: 2026-09-10-stage-06-media-placement-targeting-budget-model.md
[Stage7]: 2026-09-10-stage-07-destination-cross-domain-handoffs.md
[Sources8]: 2026-09-10-stage-08-source-register.md
[R01]: 2026-09-10-stage-08-source-register.md#r01
[R02]: 2026-09-10-stage-08-source-register.md#r02
[R03]: 2026-09-10-stage-08-source-register.md#r03
[R04]: 2026-09-10-stage-08-source-register.md#r04
[R05]: 2026-09-10-stage-08-source-register.md#r05
[R06]: 2026-09-10-stage-08-source-register.md#r06
[R07]: 2026-09-10-stage-08-source-register.md#r07
[R08]: 2026-09-10-stage-08-source-register.md#r08
[R09]: 2026-09-10-stage-08-source-register.md#r09
[R10]: 2026-09-10-stage-08-source-register.md#r10

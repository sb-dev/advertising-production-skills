# Advertising Production Skills — Stage 1: Domain and Cross-Family Boundaries

**Status:** Bootstrap research log  
**Stage:** 1 — Define Advertising Domain and Cross-Family Boundaries  
**Date:** 9 September 2026

## 1. Purpose

This research log defines the initial domain boundary for `advertising-production-skills` before professional-practice research, skill design, provider selection, execution architecture or production scaffolding.

The project exists to encode **reusable advertising-production intelligence** as installable Production Skills.

Its responsibility is to turn an **approved business acquisition objective, offer and target-customer decision** into a coherent advertising campaign system that can be produced, tested, measured, diagnosed and improved without silently changing upstream business truth or taking over downstream specialist production.

The Stage 1 boundary is intentionally architectural. It does not yet define a skill count, command set, provider stack, platform integrations, benchmark or final artifact schema.

---

## 2. Governing Architecture

The Production Skills family contract establishes four relevant ownership layers:

```text
production-skills
→ family-wide contracts, maturity rules and reusable cross-domain abstractions

advertising-production-skills
→ reusable advertising campaign production expertise

other Production Skills / consuming project
→ upstream business truth, research, legal authority, specialist asset craft,
  product interaction, software implementation and project-specific knowledge

Pactwright / project orchestrator, when used
→ lifecycle, responsibility, Contracts, Evidence and integration semantics
```

`advertising-production-skills` must remain independently useful without Pactwright.

The consuming project remains authoritative for its actual product, brand, customer evidence, commercial decisions, campaign approvals, project data and project-specific learning.

---

# 3. Project Charter

## 3.1 Mission

Enable AI agents to produce **strategy-led, evidence-backed, cross-format advertising campaigns** rather than isolated headlines, prompts, images or platform configuration.

A successful advertising-production process should be able to:

```text
receive an approved acquisition objective / offer / audience
→ frame the campaign
→ translate customer and product truth into messages
→ distinguish claims from proof
→ generate and compare creative hypotheses cheaply
→ select concepts deliberately
→ adapt the selected campaign across formats / placements
→ construct a media and audience test plan within authorised constraints
→ hand specialist assets and destination requirements to owning domains
→ prepare a launch-ready campaign package
→ interpret campaign evidence against downstream business outcomes
→ diagnose the responsible failure layer
→ change the smallest sufficient part
→ preserve useful campaign learning
```

## 3.2 Repository-owned outcomes

Advertising Production Skills owns reusable behaviour for producing and maintaining:

- campaign briefs derived from approved business inputs;
- advertising objectives and campaign success criteria;
- message hierarchies and message maps;
- claim / substantiation / proof architecture;
- objection and response maps where appropriate;
- creative territories, hooks, angles and campaign hypotheses;
- advertising concepts and concept-selection reasoning;
- bounded ad copy and campaign copy direction;
- creative briefs for specialist production domains;
- master campaign expression and placement adaptation rules;
- cross-format and cross-placement variant logic;
- campaign-level media plans;
- platform targeting representations derived from approved audience hypotheses;
- test allocation and authorised budget staging proposals;
- experiment design for creative, audience, placement and media variables;
- launch-package completeness and consistency checks;
- campaign measurement contracts;
- interpretation of platform-reported and downstream campaign outcomes;
- diagnosis of delivery, audience, creative, placement and destination problems;
- creative lineage, fatigue and refresh reasoning;
- campaign learning and bounded optimisation;
- advertising-domain quality criteria, failure modes and repair behaviour.

The repository owns **advertising reasoning and campaign coherence**, not every implementation or artefact involved in a campaign.

## 3.3 Intended result

The principal result is a **traceable campaign package plus campaign-learning state**.

A mature advertising handoff should make it possible to understand:

```text
what business outcome the campaign is meant to influence
which approved customer / offer / price it represents
what advertising objective is being tested
which messages, claims and proof are authorised
which creative hypotheses are active
how those hypotheses map to concepts and variants
where each variant is intended to run
which audience / placement assumptions are being tested
what spend or exposure boundary is authorised
what downstream destination must remain consistent
what will be measured
what constitutes success, failure or invalid evidence
what changed between variants
what has already been learned
```

The exact artifact model is deferred to later stages.

---

# 4. Core Boundary Rule

The central boundary is:

```text
Business Building
→ decides what business is being built and what acquisition strategy is justified

Advertising Production
→ turns the approved acquisition strategy into a campaign system

Specialist Production Skills
→ produce the specialist campaign assets / destinations required by that system

Execution systems
→ perform authorised account mutation, serving, tracking and data collection

Advertising Production
→ interprets campaign evidence and recommends the smallest responsible correction

Business Building
→ judges whether campaign outcomes improve the wider business system
```

Advertising may challenge an upstream assumption when campaign evidence makes it doubtful, but it must not silently rewrite that assumption.

When the owning layer must change, Advertising should issue a structured handoff or escalation rather than absorbing the responsibility.

---

# 5. Business Building Skills Boundary

## 5.1 Business Building owns

Business Building Skills owns the upstream commercial system, including reusable reasoning for:

- customer / problem selection;
- target segment or ICP definition;
- value proposition;
- product or service offer;
- packaging;
- price and monetisation;
- guarantees and commercial terms as business decisions;
- business-wide acquisition strategy;
- whether paid advertising is justified;
- channel-class choice in the wider acquisition mix;
- unit economics;
- acquisition-cost and payback constraints;
- delivery / fulfilment capacity;
- retention, expansion and referral economics;
- business-level experiments;
- the current business constraint;
- downstream commercial success criteria.

## 5.2 Advertising owns

Once those decisions are approved, Advertising owns their campaign-level translation:

```text
approved customer
→ campaign audience hypothesis
→ platform targeting representation

approved offer / price
→ campaign message and CTA
→ placement expression

approved acquisition objective
→ advertising objective
→ media / creative / audience experiment

approved economic ceiling
→ campaign budget staging / allocation proposal
```

Advertising owns the **campaign media plan** inside the approved business strategy. Business Building owns the **business-wide channel strategy**.

Advertising may compare campaign channel or placement options, but it must not decide that the business should abandon its approved acquisition strategy or target a different customer merely because a platform metric looks better.

## 5.3 Required Business → Advertising handoff

At minimum, later stages should support a handoff containing:

```text
business objective
approved acquisition objective
target customer / segment / ICP
customer evidence and known objections
offer
price / commercial terms
value proposition
known product truth
approved proof / evidence inventory
business constraints
economic constraints / CAC or payback expectations where relevant
delivery / sales capacity
brand requirements
geography / market
schedule constraints
business-level success metric
destination / conversion path
```

Advertising should record missing or unstable inputs rather than invent them as facts.

## 5.4 Advertising → Business feedback

Campaign evidence may reveal:

- repeated mismatch between approved audience and qualified downstream response;
- an offer that earns attention but not commercial commitment;
- economics that make the paid channel structurally unattractive;
- capacity constraints that make further acquisition harmful;
- strong response concentrated in an unapproved segment;
- repeated objections that suggest an upstream positioning or offer problem.

Advertising should report the evidence and affected assumption. Business Building owns the business-level decision to reopen the customer, offer, price, channel strategy or economics.

---

# 6. Deep Research Skills Boundary

## 6.1 Deep Research owns

Deep Research Skills owns reusable evidence-production methods such as:

- research framing;
- source strategy;
- broad discovery;
- source triage and verification;
- provenance;
- evidence extraction;
- triangulation;
- contradiction analysis;
- gap research;
- temporally valid synthesis;
- citation and material-claim verification.

## 6.2 Advertising owns

Advertising owns the **advertising question** and the **campaign interpretation** of research evidence.

Examples:

```text
Advertising asks
→ What objections appear consistently in evidence about this audience?
Deep Research produces
→ traceable evidence and synthesis
Advertising decides
→ which objection deserves a message hypothesis

Advertising asks
→ What competitor messages and ad patterns are currently visible?
Deep Research produces
→ sourced landscape / case evidence
Advertising decides
→ which territory is differentiated, credible and campaign-relevant
```

Advertising may perform small bounded lookups as part of ordinary work when no independent research workflow is justified, but general research methodology should not be reimplemented inside Advertising.

## 6.3 Boundary rule

```text
Deep Research
→ establishes evidence

Advertising
→ converts relevant evidence into campaign hypotheses, messages and tests
```

A campaign claim must not become "researched" merely because Advertising generated plausible supporting text.

---

# 7. Legal Skills Boundary

## 7.1 Legal owns

Legal Skills owns reusable legal-production expertise for:

- jurisdiction and applicability analysis;
- legal issue spotting;
- authoritative legal research;
- legal propositions and conclusions;
- legal risk communication;
- legal drafting and review;
- privacy / data-protection interpretation;
- consumer-law interpretation;
- advertising-law and regulated-sector legal interpretation;
- IP / trade mark / copyright implications;
- specialist escalation requirements.

## 7.2 Advertising owns

Advertising owns:

- identifying that a campaign element is legally or policy sensitive;
- tracking which claim, audience, placement, jurisdiction, category or disclosure creates the concern;
- maintaining claim / proof state;
- applying approved legal constraints to campaign work;
- ensuring required disclosures or restrictions survive placement adaptation;
- preventing legally unresolved material from being silently promoted to launch-ready status;
- re-evaluating campaign consistency when legal constraints change.

Advertising may track current **platform policy** as an operational campaign constraint. It does not turn platform policy into a legal conclusion.

## 7.3 Claim boundary

The claim chain should preserve distinct ownership:

```text
product / business truth
→ supplied by consuming project / Business Building

evidence / substantiation
→ supplied or verified through project evidence / Deep Research / specialist sources

legal sufficiency / required qualification
→ Legal Skills where legal judgement is required

claim hierarchy and advertising expression
→ Advertising Production Skills

final asset execution
→ specialist Production Skill where applicable
```

Advertising must never invent testimonials, objective proof, scarcity, savings, guarantees or performance evidence.

---

# 8. Narrative Production Skills Boundary

## 8.1 Advertising owns

Advertising owns the persuasive campaign intent:

- campaign message;
- message priority;
- hook / angle;
- claim and proof requirements;
- CTA;
- creative territory;
- concept hypothesis;
- placement purpose;
- mandatory content and constraints;
- bounded ad copy;
- simple performance scripts when the script is primarily an advertising expression rather than a narrative production problem.

## 8.2 Narrative owns

Narrative Production Skills owns story production when the advertising concept requires meaningful narrative craft, including:

- premise development;
- story structure;
- character motivation;
- scene progression;
- setup / payoff;
- dialogue craft beyond bounded ad copy;
- screenplay coherence;
- narrative continuity;
- narrative revision.

## 8.3 Handoff rule

```text
Advertising
→ "what this campaign needs the story to achieve"

Narrative
→ "how the story achieves it coherently"
```

Advertising may reject a narrative asset because it fails the campaign objective, message, claim or placement requirement. It should not take over narrative production to repair story structure when Narrative is the owning domain.

---

# 9. Video Production Skills Boundary

## 9.1 Advertising owns

For video advertising, Advertising owns the campaign-facing brief:

- advertising objective;
- audience hypothesis;
- message / claim / proof;
- concept;
- CTA;
- required product or brand truth;
- intended placement;
- required duration / aspect / safe-area constraints;
- attention context;
- variant purpose;
- experiment variable;
- campaign-level evaluation criteria.

## 9.2 Video owns

Video Production Skills owns specialist audiovisual production, including:

- visual direction as a video-production decision;
- visual references and manifests;
- storyboards / animatics where owned by video production;
- shot planning;
- reference frames;
- motion prototypes;
- shot generation and selection;
- continuity;
- editing;
- graphics integration;
- audio integration;
- mastering;
- delivery variants;
- technical video QC and targeted audiovisual repair.

## 9.3 Handoff rule

Advertising should specify **campaign intent and delivery constraints**, not micromanage shot-production implementation unless the shot detail is itself an approved campaign decision.

Video returns assets and production evidence. Advertising evaluates whether those assets still express the campaign hypothesis and placement role.

---

# 10. Audio Production Skills Boundary

## 10.1 Advertising owns

For audio advertising, Advertising owns:

- campaign message;
- spoken-copy intent;
- claim / proof / disclosure requirements;
- CTA;
- format and placement role;
- duration constraints;
- audience and listening context;
- concept and variant purpose;
- sonic brand requirements supplied by the project;
- campaign-level evaluation criteria.

## 10.2 Audio owns

Audio Production Skills owns specialist sound and music production, including where relevant:

- music composition / production;
- sound design;
- sonic texture;
- performance and recording choices;
- voice treatment;
- mix;
- loudness / technical delivery;
- mastering;
- audio continuity and specialist QC.

Advertising may write or direct bounded advertising copy. Audio owns how that material is realised as sound when specialist production is required.

---

# 11. UI/UX Design Skills Boundary

## 11.1 Advertising owns

Advertising owns **destination continuity requirements** between an ad and the destination it sends the user to.

It may define and audit requirements such as:

- offer consistency;
- price consistency;
- claim consistency;
- proof continuity;
- CTA continuity;
- campaign-specific information requirements;
- disclosure continuity;
- source / campaign context that must survive the handoff;
- measurement events required to evaluate the advertising hypothesis.

Advertising may diagnose a destination mismatch as the likely failure layer.

## 11.2 UI/UX owns

UI/UX Design Skills owns the actual product interaction design:

- human problem framing;
- task models;
- information architecture;
- user flows;
- interaction design;
- state behaviour;
- accessibility;
- fidelity decisions;
- product-area consistency;
- implementation-ready UX contracts;
- UX evaluation and bounded interaction repair.

## 11.3 Boundary rule

```text
Advertising
→ defines what the destination must preserve for campaign coherence

UI/UX
→ determines how the destination should work for the user
```

Advertising must not redesign a product flow solely to improve ad-platform metrics without product and UX authority.

---

# 12. Software Engineering Skills Boundary

## 12.1 Advertising owns

Advertising may define implementation requirements needed to execute or measure a campaign, such as:

- campaign identifiers;
- attribution / tracking intent;
- required conversion events;
- event semantics relevant to the campaign hypothesis;
- destination parameters;
- asset / placement delivery requirements;
- experiment assignments required by the campaign plan;
- data needed to distinguish platform-reported from verified downstream outcomes.

## 12.2 Software Engineering owns

Software Engineering Skills owns technical implementation and engineering quality for:

- landing-page or application implementation;
- tracking instrumentation;
- pixels / SDKs / server-side events;
- event pipelines;
- APIs;
- experiment infrastructure;
- data transport;
- integration code;
- reliability, security and performance;
- deployment and technical validation.

Advertising should describe **measurement meaning**, not silently implement or redefine application behaviour.

## 12.3 Analytics / attribution boundary

Advertising owns campaign interpretation and the measurement contract.

External analytics / attribution systems own collection and computation.

Software Engineering owns required implementation work.

Advertising must preserve the distinction between:

```text
platform-reported result
verified downstream event
attributed outcome
incremental business effect
```

Later stages will define how much attribution methodology belongs in core advertising reasoning versus external specialist systems.

---

# 13. Pactwright Boundary

## 13.1 Pactwright owns

When used, Pactwright may own:

- lifecycle responsibility;
- Contracts;
- authorised work;
- Project Graph / Project Intelligence semantics;
- Evidence integration;
- agent / capability composition;
- project-level dependency and delivery state.

## 13.2 Advertising owns

Advertising Production Skills retains ownership of:

- campaign-domain reasoning;
- campaign artifacts;
- advertising quality criteria;
- advertising workflow behaviour;
- campaign diagnosis and repair;
- Advertising Extension Pack semantics;
- advertising benchmark semantics.

## 13.3 Integration rule

Optional composition may look like:

```text
Pactwright Contract
→ approved advertising responsibility
→ selected Agent Pack
→ Advertising Production Skills
→ domain production
→ Advertising evaluation evidence
→ Pactwright lifecycle / integration handling
```

The Advertising repository must not define Pactwright lifecycle stages, agents, Project Graph semantics or project-wide orchestration.

Pactwright must not become a hidden dependency of core Advertising Skills.

---

# 14. External Advertising Platforms and Execution Systems

Advertising Production Skills may reason about platform capabilities, formats, placements, audiences, optimisation objectives and policy constraints.

It does **not** own the platform runtime.

External execution systems own, where applicable:

- ad-account administration;
- credentials and permissions;
- campaign upload;
- bid mutation;
- actual spend commitment;
- budget mutation;
- ad serving;
- auction execution;
- delivery optimisation performed by the platform;
- platform-side conversion tracking;
- billing;
- raw platform reporting;
- DSP / ad-server infrastructure.

A later execution layer may automate authorised operations, but the domain boundary remains:

```text
Advertising Skills
→ decide / specify / evaluate advertising work

Execution adapter / platform
→ perform authorised platform operation
```

Do not build a universal ad-platform control plane during bootstrap.

---

# 15. Brand Boundary

Advertising necessarily works with brand expression, but Stage 1 does not make it the owner of company-wide brand strategy.

The consuming project supplies approved brand decisions such as:

- brand positioning;
- identity;
- voice;
- prohibited expressions;
- visual system;
- sonic identity;
- product truth;
- reputation constraints.

Advertising owns **campaign expression within those constraints**.

Advertising may identify that the brand constraint conflicts with campaign performance or placement fit, but reopening brand strategy requires the owning project or future specialist brand capability.

---

# 16. Targeting Boundary

Targeting must preserve three distinct concepts:

```text
business segment / target customer
≠
advertising audience hypothesis
≠
platform targeting representation
```

## Business segment / target customer

Owned upstream by Business Building / the consuming project.

## Advertising audience hypothesis

Owned by Advertising. It describes which subset, state, intent, context or observable condition is expected to respond to the campaign and why.

## Platform targeting representation

Owned at campaign-planning level by Advertising, executed by the platform / authorised adapter.

Examples include:

- keyword sets;
- context / placement sets;
- broad or narrow platform audience definitions;
- first-party audience eligibility;
- retargeting cohorts where authorised;
- geographic / temporal constraints;
- exclusions.

Advertising must not infer sensitive personal attributes or use targeting mechanisms that conflict with approved legal, ethical or platform constraints.

---

# 17. Budget and Spend Boundary

Budget decisions have three layers:

```text
business economic boundary
→ Business Building / authorised owner

campaign allocation / staging proposal
→ Advertising Production Skills

actual spend / bid / account mutation
→ authorised execution system / human operator
```

Advertising may recommend:

- test budget allocation;
- channel / placement allocation inside approved scope;
- staged commitment;
- stop / continue thresholds;
- frequency or exposure limits;
- reallocation based on valid evidence.

It must not silently exceed the authorised economic boundary or commit spend merely because an optimisation loop recommends it.

---

# 18. Measurement Boundary

Advertising owns the campaign measurement question:

```text
What would demonstrate that this campaign hypothesis works?
```

It should define:

- primary campaign metric;
- guardrails;
- downstream business metric;
- observation window;
- comparison / baseline;
- evidence threshold;
- known confounders;
- invalidation conditions;
- decision rule.

Business Building owns whether the observed result is economically and strategically worthwhile for the business.

Software / analytics systems own instrumentation and computation.

Advertising should not promote vanity metrics above downstream outcomes.

---

# 19. Human and Authorised Decision Points

Not every campaign decision must be manually approved, but some commitments are outside autonomous advertising authority unless explicitly delegated.

Stage 1 treats the following as human-owned or separately authorised by default:

- changing the approved target customer;
- changing the approved offer;
- changing price or material commercial terms;
- making a new material objective claim without evidence;
- accepting unresolved legal risk;
- changing business-wide acquisition strategy;
- committing or increasing real spend beyond authorised limits;
- publishing a campaign where launch authority has not been delegated;
- materially changing brand strategy;
- using sensitive or restricted targeting methods;
- making product promises the underlying product does not support.

Within authorised boundaries, the agent may be allowed to:

- generate campaign hypotheses;
- generate low-cost concepts;
- compare variants;
- propose media allocation;
- produce placement adaptations;
- evaluate results;
- diagnose failure;
- propose the next bounded test;
- retire invalid or losing variants according to an approved rule.

Later stages should distinguish **selection**, **approval**, **authorisation** and **execution** rather than treating them as one state.

---

# 20. Cross-Family Responsibility Matrix

| Concern | Primary owner | Advertising responsibility |
|---|---|---|
| Target customer / ICP | Business Building / project | Consume; map to audience hypotheses |
| Offer / price / commercial terms | Business Building / project | Express consistently; do not rewrite silently |
| Business-wide channel strategy | Business Building | Consume; flag campaign evidence that challenges it |
| Campaign objective | Advertising | Own |
| Campaign brief | Advertising | Own |
| Message hierarchy | Advertising | Own |
| Claim / proof map | Advertising | Own structure; require real evidence |
| Evidence acquisition / verification | Deep Research / project evidence | Frame research need; interpret advertising implication |
| Legal conclusion | Legal | Track issue; apply approved constraint |
| Platform policy context | Advertising operationally | Track source/currentness; escalate legal questions |
| Creative territory / concept | Advertising | Own |
| Bounded ad copy | Advertising | Own |
| Complex story / screenplay | Narrative | Brief, constrain and evaluate against campaign intent |
| Video production | Video | Brief and campaign-evaluate |
| Music / sound production | Audio | Brief and campaign-evaluate |
| Landing / product UX | UI/UX | Define continuity requirements; diagnose mismatch |
| Software / tracking implementation | Software Engineering | Define campaign measurement semantics |
| Campaign media plan | Advertising | Own within approved business scope |
| Platform targeting representation | Advertising | Own plan; execution external |
| Campaign budget staging | Advertising | Propose within authorised ceiling |
| Actual media spend | Authorised human / execution system | Never mutate without authority |
| Campaign test design | Advertising | Own |
| Tracking / attribution computation | External analytics + Software | Specify requirements; interpret cautiously |
| Campaign diagnosis / optimisation | Advertising | Own bounded correction |
| Business viability / economics | Business Building | Feed campaign evidence back upstream |
| Lifecycle / Project Graph | Pactwright when used | Participate through optional integration only |

---

# 21. Boundary-Safe Campaign Flow

The preferred cross-family flow is:

```text
Business Building / consuming project
→ approved acquisition objective
→ approved target customer
→ approved offer / price / economics / constraints

Deep Research, when needed
→ audience / market / precedent / competitor / source evidence

Legal, when needed
→ legal / regulatory conclusions and constraints

Advertising Production
→ campaign brief
→ message / claim / proof architecture
→ creative hypotheses
→ cheap concepts
→ selected campaign concept
→ media / audience / experiment plan
→ specialist production briefs

Narrative / Video / Audio / UIUX / Software Engineering
→ specialist assets, destinations and implementation

Advertising Production
→ cross-format / destination / launch-package audit
→ campaign measurement contract

Authorised execution systems
→ launch / serve / track

Advertising Production
→ interpret evidence
→ diagnose responsible layer
→ bounded optimisation or escalation

Business Building
→ evaluate business-level effect / reopen upstream business assumptions when justified
```

This flow is not a mandatory universal lifecycle. It is a boundary map showing where responsibility changes hands.

---

# 22. Failure Routing

Advertising should diagnose failure before changing campaign work.

## Delivery failure

Examples:

- ad not serving;
- disapproval;
- tracking broken;
- budget unavailable;
- wrong geography or schedule.

Route to platform operations, policy review or Software Engineering as appropriate.

## Audience failure

Examples:

- correct delivery but low relevant response;
- qualified response concentrated elsewhere;
- targeting representation does not match intended segment.

Advertising owns audience-hypothesis and targeting-plan diagnosis. Reopening the business target customer goes upstream.

## Creative failure

Examples:

- message not noticed;
- concept unclear;
- proof weakly expressed;
- CTA not understood;
- placement adaptation damages the idea.

Advertising owns campaign diagnosis. Specialist asset craft routes to the relevant Production Skill.

## Destination failure

Examples:

- ad promise not visible after click;
- offer / price mismatch;
- UX friction;
- broken conversion path.

Advertising diagnoses continuity failure. UI/UX, Software Engineering or Business Building owns the corresponding product/business repair.

## Claim / policy / legal failure

Advertising stops promotion of the affected material and routes the issue to the appropriate evidence, legal or policy authority.

## Business-strategy failure

If advertising works at the campaign level but the resulting customers, economics, capacity or retention are poor, the correction belongs to Business Building rather than increasingly aggressive advertising.

---

# 23. Explicit Non-Goals

`advertising-production-skills` is not:

- a replacement for Business Building Skills;
- a general marketing department;
- a corporate brand-strategy system;
- a generic market-research system;
- a replacement for Deep Research Skills;
- a legal advertising-compliance authority;
- a legal-advice system;
- a universal copy generator;
- a narrative-production engine;
- a video-production engine;
- an audio-production engine;
- a UI/UX design system;
- a landing-page builder;
- a software-engineering system;
- a CRM;
- a CDP;
- a marketing-automation platform;
- an analytics warehouse;
- an attribution vendor;
- a DSP;
- an ad server;
- an autonomous media buyer;
- an ad-account credential store;
- a universal platform API;
- a universal audience graph;
- a Project Graph or lifecycle orchestrator;
- a substitute for Pactwright;
- an authority to alter product truth, commercial terms or legal constraints.

---

# 24. Stage 1 Decisions

Stage 1 accepts the following boundary decisions as the working contract for later bootstrap stages.

## Decision 1 — Advertising starts from approved business truth

The default input is not "a product that needs more growth". It is an approved business / offer / acquisition context sufficiently concrete to support campaign production.

## Decision 2 — Advertising owns campaign strategy, not business strategy

Advertising may discover evidence that challenges an upstream business assumption, but Business Building retains authority over customer, offer, pricing, monetisation, business-wide channel strategy and economics.

## Decision 3 — Advertising owns message / claim / proof architecture but not invented proof

Claims remain traceable to actual product truth and evidence. Legal sufficiency is routed to Legal where required.

## Decision 4 — Advertising owns campaign concepts; specialist domains own specialist craft

Advertising may create cheap representations and bounded ad copy. Complex narrative, video, audio, UI/UX and software work moves to the owning Production Skills family.

## Decision 5 — Advertising owns campaign media reasoning, not platform runtime

Media plan, audience hypothesis, placement logic and authorised budget staging belong to Advertising. Account mutation, serving and spend execution do not.

## Decision 6 — Advertising owns destination consistency, not destination UX

Advertising defines what must remain consistent across ad and destination. UI/UX and Software Engineering own the experience and implementation.

## Decision 7 — Advertising owns campaign measurement interpretation, not raw analytics infrastructure

It specifies what campaign evidence is needed and interprets it. Collection, computation and system implementation remain external.

## Decision 8 — Optimisation cannot silently reopen upstream authority

Campaign optimisation may change an authorised creative, audience, placement or media variable. Changes to customer, offer, price, legal position, brand strategy or business economics require the owning authority.

## Decision 9 — Pactwright integration remains optional and one-way

Pactwright may orchestrate Advertising Skills, but Advertising remains independently installable and does not encode Pactwright lifecycle semantics.

## Decision 10 — The smallest responsible layer should change

Later workflow and evaluation design should preserve valid upstream and downstream work and route defects to the owning layer rather than regenerate the whole campaign.

---

# 25. Questions Deferred to Later Stages

Stage 1 deliberately does not settle:

- the exact professional advertising workflow;
- whether copywriting is one core skill or several commands;
- the final distinction between brand advertising and direct response inside core;
- the exact artifact schema;
- creative quality dimensions;
- the final claim taxonomy;
- whether formal substantiation grades are useful;
- how platform-policy research is refreshed and cached;
- provider selection;
- Google / Meta / TikTok / LinkedIn / Reddit / Amazon integration details;
- programmatic execution architecture;
- the attribution methodology boundary;
- incrementality methods;
- exact media-planning mathematics;
- exact budget-staging rules;
- benchmark fixtures;
- Extension Packs;
- progressive examples;
- Pactwright manifest shape;
- production repository structure beyond the existing bootstrap workspace.

These belong to subsequent stages and should be resolved from evidence rather than assumptions made to complete Stage 1.

---

# 26. Stage 1 Exit Check

The Stage 1 exit criterion is satisfied if a defensible domain boundary exists before skills are proposed.

Current result:

```text
Advertising Production Skills
= reusable campaign-production reasoning

starts from
= approved business / offer / acquisition truth

owns
= campaign brief
+ advertising objective
+ message / claim / proof architecture
+ creative hypotheses and concepts
+ bounded ad copy
+ cross-format / placement adaptation
+ campaign media plan
+ audience hypotheses and targeting representation
+ experiment design
+ measurement contract and interpretation
+ fatigue / optimisation / campaign learning

hands off
= research method → Deep Research
= legal conclusions → Legal
= story craft → Narrative
= audiovisual craft → Video / Audio
= product interaction → UI/UX
= implementation / tracking systems → Software Engineering
= lifecycle / Project Graph → Pactwright
= account mutation / serving / spend → authorised execution systems

must not silently change
= target customer
+ offer
+ price
+ business-wide acquisition strategy
+ legal position
+ product truth
+ brand strategy
+ authorised spend boundary
```

No skill count or execution stack is required to make the boundary coherent.

**Stage 1 therefore passes its exit condition and Stage 2 may proceed.**

---

# 27. Governing References Used

This Stage 1 boundary was grounded primarily in the current repository and neighbouring Production Skills contracts:

- `advertising-production-skills/docs/research-logs/2026-09-08-advertising-production-skills-new-project-bootstrap-process.md`
- `production-skills/README.md`
- `production-skills/docs/specs/02-production-skills-project-contract.md`
- `production-skills/docs/specs/04-cross-domain-orchestration-and-integration.md`
- `production-skills/docs/research-logs/2026-09-08-business-building-skills-new-project-bootstrap-process.md`
- `deep-research-skills/docs/research-logs/2026-09-09-stage-01-project-goal-and-boundary.md`
- `production-skills/docs/research-logs/2026-09-08-legal-skills-new-project-bootstrap-process.md`
- `narrative-production-skills/README.md`
- `video-production-skills/README.md`
- `audio-production-skills/README.md`
- `ui-ux-design-skills/README.md`
- `software-engineering-skills/README.md`

Later stages should treat this file as the durable Stage 1 boundary record and should not rely on conversation history for these decisions.

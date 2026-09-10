# Advertising Production Skills

Evidence-led advertising, from approved offer to campaign learning.

Designed to turn an approved business objective into supported messages, meaningful creative alternatives, coherent placement variants and useful measurement. The workflow preserves accepted work and corrects the smallest responsible layer when something fails.

**Current availability: design and research only.** This revision contains six canonical specifications and complete learning prompts. Installable Advertising skills, produced learning examples and clean-consumer installation results have not yet been verified. The sections below distinguish the designed workflow from demonstrated capability.

[Quick start](#quick-start) · [Learn by Producing](#learn-by-producing) · [Skills](#skills) · [Documentation](#documentation)

## What the design covers

- **Frame the campaign:** objectives, audience hypotheses, offer continuity, messages, claims, proof and objections.
- **Develop the creative:** genuinely different concepts, cheap useful representations, exact copy and specialist production briefs; adapt meaning across formats rather than merely resizing files.
- **Plan and learn:** media roles, targeting requirements, authorised budget staging, controlled tests and downstream measurement.
- **Diagnose and repair:** separate delivery, audience, creative, placement, destination and measurement failures; preserve valid concepts and campaign learning.
- **Specialise deliberately:** select or author a reusable advertising grammar without changing the approved business facts or granting new authority.

The design covers search, static, social video, connected TV, display, carousel, vertical, native/sponsored and audio work. Actual image, video and audio requests require the corresponding produced files and inspections. A prompt, script or storyboard is not a substitute for requested final media.

## Business Building boundary

Business Building or the consuming project's business owner decides the customer, offer, price, business-wide channel choice, economics and whether paid acquisition is justified. Advertising translates those approved decisions into a campaign; it must not quietly change the exchange to improve an ad metric.

```text
approved business objective, offer and economics
→ campaign brief and audience hypothesis
→ message, claim and proof
→ concepts and placement variants
→ media, destination and test contracts
→ evaluation, measurement and bounded repair
```

[System ownership](../01-advertising-production-skills-system-spec.md) and [workflow contracts](../02-advertising-production-skills-workflows-and-artifacts-spec.md) define the complete boundary. Campaign-specific commercial records remain in the consuming project.

## Truthful and policy-aware advertising

Unsupported claims, fake testimonials, false scarcity, misleading prices and hidden material qualifications fail review even when the creative is persuasive. Evidence, permission to use it, claim approval, creative selection, publication authority and observed performance remain different facts.

Keep the approved business segment, advertising hypothesis and platform targeting representation separate. A targeting signal is not proof of an enforced exclusion. Legal conclusions belong to the appropriate Legal owner; current source and campaign facts must be checked for the actual jurisdiction, category, platform and date. A platform acceptance is not blanket legal clearance.

## Installation

**No supported installation is claimed for this design-only revision.** The intended distribution is four independently selectable Agent Skills for an existing compatible host, without Pactwright or an advertising account as a prerequisite. Host support must be established by actual clean-consumer tests, not by the installer listing a host name.

After a tested skill revision is published, use the recorded installer version, source commit and host identifier. The following is the specified consumption route, not a claim that it has run here:

```bash
: "${SKILLS_CLI_VERSION:?Use the version in the installation evidence}"
: "${REVISION:?Use the published and tested Advertising commit}"
: "${AGENT:?Use a host identifier with published installation evidence}"

SOURCE="https://github.com/sb-dev/advertising-production-skills/tree/${REVISION}"
pnpm dlx "skills@${SKILLS_CLI_VERSION}" add "$SOURCE" --list
pnpm dlx "skills@${SKILLS_CLI_VERSION}" add "$SOURCE" \
  --skill advertising-build --skill advertising-evaluate \
  --agent "$AGENT" --copy
```

The example selects the two skills used by the quick start; either can also be installed alone. It does not select every skill, every host or a global installation. Install the compatible `local-service-lead-generation` resource offered by those payloads before running E01; no separate pack installer is implied.

Use the [installation contract](../03-advertising-production-skills-repository-and-contracts-spec.md#6-installation-contract) for local-source use, exact revision binding, self-contained resources and preservation checks. The selected host/model still determines inference, data handling and any associated costs. Installing instructions does not authorise account access, uploads, media buying or paid generation.

## Quick start

Start with **E01, a bounded search unit**, rather than a full campaign. Today its complete prompt can be inspected below. Execution requires the two named skills and their compatible selected pack to be implemented, installed and verified first. This is the original E01 prompt, not a sixteenth primary example or an executed result.

```text
Use advertising-build with local-service-lead-generation, then advertising-evaluate, for E01 in production/advertising/E01.

This is a SYNTHETIC teaching exercise. Everything below is supplied fixture truth only, not a real business, testimonial, approval or campaign result. You may create the requested local artefacts. No paid generation, external upload, publication, account change, customer contact or media spend is authorised.

SYN-E01-OFFER@1: Cycle Check offers one bicycle inspection for GBP 25 total, one-off. A written assessment is included; repairs and parts are not included and require a separate quote. Service is available only to adults in fictional service zones A and B, Tuesday to Saturday, 09:00–17:00 local fixture time. Two inspection appointments can be accepted per day. A requested appointment is not confirmed until the operator replies. No speed, safety-certification, savings or repair-success claim is supported.
SYN-E01-PROOF@1 consists of those supplied offer, service and capacity facts only. Brand: plain, helpful, no pressure. Audience hypothesis: adults seeking a local bicycle assessment; no evidence establishes its prevalence. Business objective: qualified inspection requests within capacity. Advertising objective: communicate the inspection and its limits accurately. No historical results exist.
Destination fixture: cycle-check.example/details, represented locally by destination-copy.md. It must repeat the inspection price, separate repair quotation, zones, hours and request/confirmation distinction. It is not a deployed URL.
Exercise search profile: exactly 3 standalone headlines, each at most 30 characters including spaces, and exactly 2 descriptions, each at most 90 characters. All 3 x 2 headline/description combinations are possible. These are fixture constraints, not verified live platform limits.

Produce brief.md with the relevant input/unknown/approval boundaries; claim-proof.md linking every material assertion to the two supplied records; ad-copy.md with the exact five strings and character counts; destination-copy.md; and evaluation.md inspecting all six possible combinations, commercial continuity and the CTA. Choose an appropriate truthful way to retain qualifications within the profile rather than hiding them in a destination alone. Record the actual audience hypothesis separately from the business segment and any proposed platform representation.

Use a request-to-schedule CTA, not a guarantee of repair or availability. Do not broaden the zones, invent reviews or optimise to clicks. Identify the qualified-request event and capacity guardrail without claiming a tracking implementation. Prefer a compliant expression for review; do not manufacture human approval or launch readiness. Report actual local output paths and any unsatisfied requirement.
```

A fulfilled E01 run returns five actual Markdown files: the brief, claim-proof map, exact ad copy with counts, destination copy and evaluation of all six assemblies. Review the actual strings and source links. An evaluation that finds a defect must identify it and its smallest repair; a file saying PASS is not evidence by itself. A valid local search unit does not establish launch readiness or measured campaign success.

## Learn by Producing

**Five levels, three primary examples per level: fifteen complete prompts.** These are currently designed exercises, not a gallery of completed productions. Each link opens the exact original prompt and its acceptance expectations. The prices, businesses, observations and approvals in these teaching fixtures are explicitly synthetic, including the three L5 rehearsal subjects.

### L1: Bounded advertising unit

| Example and complete prompt | What the exercise produces or tests |
|---|---|
| [E01: Local inspection search unit](2026-09-10-stage-16-example-designs-and-prompts.md#e01-local-inspection-search-unit) | Exact search copy; inspection price is not repair pricing. |
| [E02: Recurring price in a static unit](2026-09-10-stage-16-example-designs-and-prompts.md#e02-recurring-price-in-a-static-unit) | SVG and PNG; recurring terms remain readable, without a false free trial. |
| [E03: A screenless B2B response](2026-09-10-stage-16-example-designs-and-prompts.md#e03-a-screenless-b2b-response) | Actual WAV and listening review; a free fit call is not free implementation. |

### L2: Coherent creative test

| Example and complete prompt | What the exercise produces or tests |
|---|---|
| [E04: A controlled search-copy comparison](2026-09-10-stage-16-example-designs-and-prompts.md#e04-a-controlled-search-copy-comparison) | Two complete search bundles; change only the opening headline. |
| [E05: Creator-native opening test](2026-09-10-stage-16-example-designs-and-prompts.md#e05-creator-native-opening-test) | Two actual vertical videos; preserve the identical shared body. |
| [E06: Brand-linked display test](2026-09-10-stage-16-example-designs-and-prompts.md#e06-brand-linked-display-test) | Two display treatments; measure the intended brand association. |

### L3: Complete campaign

| Example and complete prompt | What the exercise produces or tests |
|---|---|
| [E07: One brand idea across display, CTV and audio](2026-09-10-stage-16-example-designs-and-prompts.md#e07-one-brand-idea-across-display-ctv-and-audio) | Display, CTV and audio; preserve meaning across clickable and screenless contexts. |
| [E08: Qualification-led B2B campaign](2026-09-10-stage-16-example-designs-and-prompts.md#e08-qualification-led-b2b-campaign) | Search, sponsored editorial and display; qualify demand against scope and capacity. |
| [E09: App availability, store promise and first useful action](2026-09-10-stage-16-example-designs-and-prompts.md#e09-app-availability-store-promise-and-first-useful-action) | Carousel, video, store and first use; repair an availability delay. |

### L4: Diagnose and repair campaign performance

| Example and complete prompt | What the exercise produces or tests |
|---|---|
| [E10: Retargeting report with duplicate and ineligible outcomes](2026-09-10-stage-16-example-designs-and-prompts.md#e10-retargeting-report-with-duplicate-and-ineligible-outcomes) | Reconcile duplicate and ineligible outcomes before changing creative. |
| [E11: Apparent fatigue caused by a changed delivery mix](2026-09-10-stage-16-example-designs-and-prompts.md#e11-apparent-fatigue-caused-by-a-changed-delivery-mix) | Separate delivery-mix change from unsupported fatigue conclusions. |
| [E12: Repair a destination without changing the accepted advertisement](2026-09-10-stage-16-example-designs-and-prompts.md#e12-repair-a-destination-without-changing-the-accepted-advertisement) | Correct the offline destination while preserving the accepted advertisement. |

### L5: Full advertising-production thesis

| Example and complete prompt | What the exercise produces or tests |
|---|---|
| [E13: Kakeibo consumer subscription launch thesis](2026-09-10-stage-16-example-designs-and-prompts.md#e13-kakeibo-consumer-subscription-launch-thesis) | Full synthetic subscription campaign, retained-value readout and claim repair. |
| [E14: One-person FDE consultancy thesis](2026-09-10-stage-16-example-designs-and-prompts.md#e14-one-person-fde-consultancy-thesis) | Full synthetic B2B campaign, proof limits, qualification and sales lag. |
| [E15: Production Skills ecosystem adoption and commercial thesis](2026-09-10-stage-16-example-designs-and-prompts.md#e15-production-skills-ecosystem-adoption-and-commercial-thesis) | Separate synthetic adoption and paid-education paths, outcomes and repair. |

Required media is stated in each prompt. Where it asks for PNG, MP4 or WAV, execution must create and inspect that file; plans alone are incomplete. The eight pack showcases are a separate suite, and source-aware stress tests do not replace these fifteen learning exercises.

## Skills

All four entries are specified, not claimed as installed or benchmarked at this revision.

| Skill | Use it for | Boundary |
|---|---|---|
| `advertising-build` | New briefs, concepts, copy, adaptations, media/test plans and campaign packages | Produces the requested scope; no implicit launch or spend |
| `advertising-optimise` | Results, diagnosis, fatigue, next tests and bounded correction | Preserves commercial truth, valid assets and historical evidence |
| `advertising-evaluate` | Claims, proof, format, destination, test, measurement, policy and preservation audits | Returns independent criteria, not a universal score or Legal approval |
| `advertising-pack-author` | Reusable campaign grammar and pack revisions | Checks existing coverage, actual comparison evidence and compatibility |

The [33 intent contracts](../03-advertising-production-skills-repository-and-contracts-spec.md#5-command-registry-and-contracts) define inputs, outputs, ownership and failure handling. Intent names are workflow operations, not shell commands. A small request uses the relevant operations, not the entire campaign process.

## Extension Packs

A pack changes useful campaign reasoning, not just tone or platform vocabulary. Core remains useful without one. These eight grammars are design-complete; their runtime implementation and required comparisons are not claimed here.

| Pack and full contract | Specialisation |
|---|---|
| [P01: `direct-response-performance-campaign`](../06-advertising-production-extension-pack-catalogue.md#p01-direct-response-performance-campaign) | Qualified response, proof and downstream value |
| [P02: `brand-awareness-campaign`](../06-advertising-production-extension-pack-catalogue.md#p02-brand-awareness-campaign) | Brand-linked recognition and association |
| [P03: `b2b-demand-generation-campaign`](../06-advertising-production-extension-pack-catalogue.md#p03-b2b-demand-generation-campaign) | Organisational proof, qualification and sales lag |
| [P04: `consumer-app-acquisition-campaign`](../06-advertising-production-extension-pack-catalogue.md#p04-consumer-app-acquisition-campaign) | Store-to-first-use and retained-value continuity |
| [P05: `product-launch-campaign`](../06-advertising-production-extension-pack-catalogue.md#p05-product-launch-campaign) | Availability phases, delay and transition handling |
| [P06: `retargeting-and-reengagement-campaign`](../06-advertising-production-extension-pack-catalogue.md#p06-retargeting-and-reengagement-campaign) | Authorised prior state, recency and suppression |
| [P07: `local-service-lead-generation`](../06-advertising-production-extension-pack-catalogue.md#p07-local-service-lead-generation) | Service area, job scope, contact and capacity |
| [P08: `creator-native-social-campaign`](../06-advertising-production-extension-pack-catalogue.md#p08-creator-native-social-campaign) | Creator latitude, truthful demonstration and commercial identity |

Each catalogue entry includes a full showcase prompt, its complete core-only comparator, three behavioural observables and two adverse challenges. Both challenges must run in both conditions: six conditions per pack, forty-eight across the catalogue. Actual differences may show useful specialisation, no material difference, regression or an inconclusive comparison; superiority is not assumed.

Explicit campaign requirements and approved decisions take precedence over a selected pack. Verified legal, standards and platform constraints remain binding. A pack grants no new rights, data access or spending authority. Select one primary grammar unless a specific combination has explicit compatible scopes and a reviewed result. See [pack selection and authoring](../05-advertising-production-customisation-packs-spec.md).

## Execution layer and specialist handoffs

Use the consuming project's existing host, authorised tools and versioned campaign files. Advertising owns production reasoning and integration, while Narrative, visual, Video and Audio specialists supply craft; UI/UX and Software supply destinations and instrumentation; Legal supplies scoped legal conclusions.

External systems own account administration, rendering, campaign upload, bidding/spend, serving, data collection, tracking, attribution computation and hosting. Providers researched in the design are not installed integrations or blanket recommendations. A required tool, output or permission that is absent remains a specific unresolved dependency, not an invented successful handoff.

Pactwright composition is optional. It may supply a Contract and receive domain Evidence; it does not replace Advertising's evaluation, and ordinary use must remain standalone. No optional integration is claimed to have been tested at this revision.

## Measurement, optimisation and learning

A complete test names its hypothesis, changed variables, comparison, primary metric, guardrails, downstream business metric, evidence threshold, confounders and decision rule. Retain counting units, attribution basis, cohort windows, maturity, uncertainty and source versions.

Platform conversions are not automatically unique qualified outcomes; attribution is not incrementality; revenue is not contribution; an installation attempt is not useful adoption. Missing or immature data is not zero. High clicks do not justify downstream harm, unsupported claims or commitments beyond capacity.

Diagnose the evidence and responsible layer before refreshing creative. Keep delivery, performance assessment, evidence validity, fatigue and succession separate. A recommendation to pause is not an actual pause, and renaming an asset does not reset exposure. The [workflow specification](../02-advertising-production-skills-workflows-and-artifacts-spec.md) defines source-separated readouts and exact before/after preservation.

## Benchmarks and evidence

The [benchmark specification](../04-testing-and-benchmark-spec.md) separates twelve dimensions: deterministic validation, creative quality, campaign reasoning, business alignment, claim/legal/policy validity, experiment quality, measurement quality, optimisation/fatigue, preservation/repair, pack behaviour, end-to-end production and installation integrity. There is no universal advertising quality score.

Current evidence establishes research and specification checks only. The [bootstrap progress](README.md) links those records. It does not establish installed-skill execution, generated-media evaluation, successful clean installation or real campaign effectiveness.

The frozen execution design contains one core vertical, fifteen primary examples, forty-eight pack conditions, seventy-nine canonical cases, two authoring cases, four supplemental regression trials and eight installation combinations. These are separate coverage obligations, not a count of completed tests. They must not be combined into one advertising-quality score. Actual reports must retain exact revisions, complete prompts, outputs, inspections, failures, repairs and evidence limits.

## Canonical stress tests

The [source-aware stress contracts](2026-09-10-stage-17-canonical-advertising-stress-tests.md) deliberately distinguish actual project-source facts from fictional observations:

| Subject | What must survive campaign production |
|---|---|
| Kakeibo | Consumer trust, subscription/refund consistency, financial sensitivity, supported claims, authorised targeting and retained downstream quality |
| One-person FDE consultancy | High-ticket B2B scope, narrow ICP, qualification, genuine proof, delivery capacity and longer sales cycles |
| Production Skills ecosystem | Truthful adoption and developer messaging, separate education/services/marketplace paths, and brand/performance distinctions |

Use the [authoritative FDE-17@2 correction](2026-09-10-stage-17-acceptance.md), not the superseded historical FDE prompt. Its lead-entry clock and outstanding C2/B0 commitments are separate from delivered C1 and four-cohort totals. Missing real consultancy terms remain missing. These contracts are test designs, not evidence that a campaign launched or a product shipped.

## Documentation

| Specification | Owns |
|---|---|
| [01 System](../01-advertising-production-skills-system-spec.md) | Purpose, boundaries, architecture and commitment gates |
| [02 Workflows and artefacts](../02-advertising-production-skills-workflows-and-artifacts-spec.md) | Briefs, production, media, handoffs, measurement, state and repair |
| [03 Repository and contracts](../03-advertising-production-skills-repository-and-contracts-spec.md) | Skills, commands, self-contained resources and installation |
| [04 Testing and benchmark](../04-testing-and-benchmark-spec.md) | Independent evaluation, exact suites and actual evidence |
| [05 Customisation packs](../05-advertising-production-customisation-packs-spec.md) | Selection, precedence, composition, authoring and compatibility |
| [06 Extension Pack catalogue](../06-advertising-production-extension-pack-catalogue.md) | Eight complete grammars, prompts and behavioural criteria |

[Research and bootstrap progress](README.md) retain the source investigations and stage-level conformance. Canonical specifications own accepted operational meaning; a convenient implementation or newer-looking source does not silently change it.

## Boundaries

This project is not a CRM, ad server, DSP, customer-data platform, attribution vendor, universal audience graph, autonomous media buyer or legal compliance authority. It does not replace Business Building or own the consuming project's product truth.

Keep private campaign, customer and financial data in authorised consumer storage. Public examples use explicit synthetic fixtures or permitted source facts with their limits. Publication, recipient disclosure, provider costs, destructive changes and media spend each need their own applicable authority. No example grants real-world authority merely because it contains a fictional approval.

## Contributing and support

At this revision, contributions concern the documented design. Read the owning specification and existing research first. Propose a bounded change with its rationale, affected contracts and reproducible verification; preserve unrelated accepted work. Report a defect with the source revision, exact expected versus observed behaviour and sanitised reproduction. Never post account credentials, private audience records or confidential customer material.

Use the repository's [issue tracker](https://github.com/sb-dev/advertising-production-skills/issues) for public design questions and defect reports. The production scaffold will provide contributor guidance and executable development commands; their existence or successful execution is not claimed here. Contributing a document does not authorise a release, registry promotion or change to another project.

## Licence and third-party rights

A project licence has not yet been published in this revision. No licence badge or permissive-licence claim is made. Check the actual licence and notices before relying on a grant of rights. The fictional MIT licence in the E15 teaching input is not this repository's licence.

Repository licensing, project branding and third-party asset, font, voice and provider rights are separate. Public access, source permission, a generated output or a selected pack does not establish every required usage right.

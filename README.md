# Advertising Production Skills

**Evidence-led advertising, from approved offer to campaign learning.**

Advertising Production Skills is an open-source Production Skills project for turning an approved business objective into supported messages, meaningful creative alternatives, coherent placement variants, media/test contracts and bounded campaign learning.

**Current status: production scaffold.** The repository now exposes the four designed skill entry points, repository validation, examples/benchmark indices and CI. The Stage 23 core vertical, Stage 24 full progressive/Extension Pack execution, Stage 25 clean installation evidence and any later maturity promotion are not yet complete.

## What it covers

- campaign framing, objectives and audience hypotheses;
- message, claim, proof and objection architecture;
- genuinely different creative concepts and cheapest-useful representations;
- channel/placement adaptation without losing material meaning;
- media roles, targeting requirements, authorised budget staging and controlled tests;
- measurement interpretation, fatigue diagnosis and bounded repair;
- independent evaluation without a universal advertising-quality score;
- reusable Advertising Extension Pack grammars without changing approved business truth.

The design covers search, static, social video, connected TV, display, carousel, vertical, native/sponsored and audio work. When a task requires final media, the corresponding actual image, video or audio file and relevant inspection are required; a prompt, script or storyboard is not a substitute.

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

See [System](docs/01-advertising-production-skills-system-spec.md) and [Workflows and artefacts](docs/02-advertising-production-skills-workflows-and-artifacts-spec.md).

## Truthful and policy-aware advertising

Unsupported claims, fake testimonials, false scarcity, misleading prices and hidden material qualifications fail review even when the creative is persuasive. Evidence, permission to use it, claim approval, creative selection, publication authority and observed performance are separate facts.

Keep the approved business segment, advertising hypothesis and platform targeting representation separate. Legal conclusions remain with the appropriate Legal owner. Current campaign facts, jurisdiction, category, platform and source dates must be checked for the actual use; platform acceptance is not blanket legal clearance.

## Installation

The skill packages now exist, but clean external installation and host-compatibility evidence are Stage 25 requirements and are **not yet claimed**. The intended project-scoped route uses the open Agent Skills installer with an exact tested installer version, host identifier and repository revision:

```bash
: "${SKILLS_CLI_VERSION:?set the tested installer version}"
: "${REVISION:?set the exact Advertising commit}"
: "${AGENT:?set the tested host identifier}"

SOURCE="https://github.com/sb-dev/advertising-production-skills/tree/${REVISION}"
pnpm dlx "skills@${SKILLS_CLI_VERSION}" add "$SOURCE" --list
pnpm dlx "skills@${SKILLS_CLI_VERSION}" add "$SOURCE" \
  --skill advertising-build --skill advertising-evaluate \
  --agent "$AGENT" --copy
```

Do not infer compatibility from the installer merely listing an agent. See the [installation contract](docs/03-advertising-production-skills-repository-and-contracts-spec.md#6-installation-contract).

## Quick start

The first proving path is **E01: Local inspection search unit**. Its complete synthetic prompt is already preserved in [Stage 16](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e01-local-inspection-search-unit). Stage 23 must execute the core vertical before this README can present it as demonstrated capability.

A correct E01 execution produces five actual Markdown artefacts: a brief, claim-proof map, exact ad copy with counts, destination copy and evaluation of all permitted assemblies. A file saying PASS is not evidence by itself.

## Learn by producing

The public learning surface is fixed at **five levels × three primary examples = fifteen**. The prompts are complete; production evidence is added only when later stages actually run them.

### Level 1 — Bounded advertising unit

- [E01 Local inspection search unit](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e01-local-inspection-search-unit)
- [E02 Recurring price in a static unit](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e02-recurring-price-in-a-static-unit)
- [E03 A screenless B2B response](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e03-a-screenless-b2b-response)

### Level 2 — Coherent creative test

- [E04 A controlled search-copy comparison](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e04-a-controlled-search-copy-comparison)
- [E05 Creator-native opening test](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e05-creator-native-opening-test)
- [E06 Brand-linked display test](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e06-brand-linked-display-test)

### Level 3 — Complete campaign

- [E07 One brand idea across display, CTV and audio](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e07-one-brand-idea-across-display-ctv-and-audio)
- [E08 Qualification-led B2B campaign](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e08-qualification-led-b2b-campaign)
- [E09 App availability, store promise and first useful action](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e09-app-availability-store-promise-and-first-useful-action)

### Level 4 — Diagnose and repair campaign performance

- [E10 Retargeting report with duplicate and ineligible outcomes](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e10-retargeting-report-with-duplicate-and-ineligible-outcomes)
- [E11 Apparent fatigue caused by a changed delivery mix](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e11-apparent-fatigue-caused-by-a-changed-delivery-mix)
- [E12 Repair a destination without changing the accepted advertisement](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e12-repair-a-destination-without-changing-the-accepted-advertisement)

### Level 5 — Full advertising-production thesis

- [E13 Kakeibo consumer subscription launch thesis](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e13-kakeibo-consumer-subscription-launch-thesis)
- [E14 One-person FDE consultancy thesis](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e14-one-person-fde-consultancy-thesis)
- [E15 Production Skills ecosystem adoption and commercial thesis](docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md#e15-production-skills-ecosystem-adoption-and-commercial-thesis)

Where a prompt requests PNG, MP4, WAV or an implemented representation, execution must produce and inspect that output. The eight pack showcases are a separate suite; stress tests do not replace the fifteen learning examples.

## Project structure grows with the work

A bounded search unit should stay small:

```text
production/advertising/E01/
├── brief.md
├── claim-proof.md
├── ad-copy.md
├── destination-copy.md
└── evaluation.md
```

A complete campaign can add identifiable concepts, a semantic master, actual placement variants, media and measurement contracts, specialist return evidence and bounded repair records. Several logical records may share one file. Do not create global `draft/approved/final` trees or copy approved business truth into multiple editable locations.

## Skills

| Skill | Responsibility |
|---|---|
| [`advertising-build`](skills/advertising-build/SKILL.md) | New briefs, concepts, copy, adaptations, media/test plans and campaign packages |
| [`advertising-optimise`](skills/advertising-optimise/SKILL.md) | Results, diagnosis, fatigue, next tests and bounded correction |
| [`advertising-evaluate`](skills/advertising-evaluate/SKILL.md) | Claims, proof, format, destination, test, measurement, policy and preservation audits |
| [`advertising-pack-author`](skills/advertising-pack-author/SKILL.md) | Reusable campaign grammar and Extension Pack authoring/revision |

Intent names are bounded workflow operations, not shell commands or Pactwright lifecycle stages. The canonical 33-intent ownership remains 13 build, 10 optimise, 9 evaluate and 1 pack-author.

## Extension Packs

Eight grammars are fully specified but **not yet represented as implemented/mature runtime packs**:

1. `direct-response-performance-campaign`
2. `brand-awareness-campaign`
3. `b2b-demand-generation-campaign`
4. `consumer-app-acquisition-campaign`
5. `product-launch-campaign`
6. `retargeting-and-reengagement-campaign`
7. `local-service-lead-generation`
8. `creator-native-social-campaign`

See [Pack semantics](docs/05-advertising-production-customisation-packs-spec.md) and the [catalogue](docs/06-advertising-production-extension-pack-catalogue.md). Stage 24 must implement and execute their required comparisons before runtime maturity is claimed.

## Execution layer and specialist handoffs

Advertising owns campaign reasoning and integration. Narrative, visual, Video and Audio specialists own their craft; UI/UX and Software own destinations and implementation; Legal owns scoped legal conclusions. Account administration, rendering, campaign upload, bidding/spend, serving, data collection, tracking, attribution computation and hosting remain external operations.

Selecting a specialist also selects that specialist's actual prerequisites, approval/locking semantics and retry limits. Advertising's concept preference cannot become another domain's human approval, and remaining campaign budget cannot override a narrower specialist retry rule. See the [cross-project review](docs/research-logs/2026-09-10-stage-21-cross-project-review.md).

Pactwright is optional and is not required for standalone Advertising use.

## Measurement, optimisation and learning

A complete test names its hypothesis, changed variables, comparison, primary metric, guardrails, downstream business metric, evidence threshold, confounders and decision rule. Counting units, attribution basis, cohort windows, maturity, uncertainty and source revisions stay visible.

Platform conversions are not automatically unique qualified outcomes; attribution is not incrementality; revenue is not contribution; missing or immature data is not zero. Diagnose evidence and the responsible layer before refreshing creative.

## Benchmarks and evidence

The [benchmark specification](docs/04-testing-and-benchmark-spec.md) keeps twelve dimensions separate: deterministic validation, creative quality, campaign reasoning, business alignment, claim/legal/policy validity, experiment quality, measurement quality, optimisation/fatigue, preservation/repair, pack behaviour, end-to-end production and installation integrity.

The scaffold's deterministic repository checks are real; campaign benchmark, generated-media, pack-comparison and clean-install evidence remain unexecuted until their owning stages. See [benchmarks/README.md](benchmarks/README.md) and [bootstrap progress](docs/research-logs/README.md).

## Canonical stress tests

The [Stage 17 contracts](docs/research-logs/2026-09-10-stage-17-canonical-advertising-stress-tests.md) cover:

- Kakeibo consumer trust, subscription/refund consistency, financial sensitivity and authorised targeting;
- one-person FDE consultancy proof, qualification, capacity and longer sales cycles;
- Production Skills ecosystem adoption/commercial separation and developer-facing truthfulness.

Use the [FDE-17@2 correction](docs/research-logs/2026-09-10-stage-17-acceptance.md), not the superseded historical FDE prompt.

## Documentation

- [01 System](docs/01-advertising-production-skills-system-spec.md)
- [02 Workflows and artefacts](docs/02-advertising-production-skills-workflows-and-artifacts-spec.md)
- [03 Repository and contracts](docs/03-advertising-production-skills-repository-and-contracts-spec.md)
- [04 Testing and benchmark](docs/04-testing-and-benchmark-spec.md)
- [05 Customisation packs](docs/05-advertising-production-customisation-packs-spec.md)
- [06 Extension Pack catalogue](docs/06-advertising-production-extension-pack-catalogue.md)
- [Research logs and bootstrap progress](docs/research-logs/README.md)

## Boundaries

This project is not a CRM, ad server, DSP, customer-data platform, attribution vendor, universal audience graph, autonomous media buyer or legal compliance authority. It does not replace Business Building or own the consuming project's product truth.

Keep private campaign, customer and financial data in authorised consumer storage. Publication, recipient disclosure, provider costs, destructive changes and media spend each need their own applicable authority.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `pnpm validate` and `pnpm test` before proposing repository changes. Public issues must not contain credentials, private audience records or confidential customer material.

## Licence

MIT. See [LICENSE](LICENSE). Third-party asset, font, voice, model/provider and branding rights remain separate from the repository software/content licence.

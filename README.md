# Advertising Production Skills

**Build evidence-led advertising campaigns, not isolated ad generations.**

Advertising Production Skills gives AI coding agents a production workflow for turning an approved business objective into campaign strategy, supported claims, creative concepts, placement variants, media/test plans, measurement and bounded optimisation.

It supports the advertising-production process:

- **Campaign framing**: objectives, approved offer continuity, audience hypotheses and channel roles
- **Message and proof**: message hierarchy, explicit and implied claims, substantiation, objections and CTA meaning
- **Creative production**: genuinely different concepts, cheap useful representations, specialist production briefs and cross-format adaptation
- **Media and experimentation**: placements, targeting representations, budget staging, test design and measurement contracts
- **Optimisation**: delivery, audience, creative, placement and destination diagnosis, fatigue investigation and bounded repair
- **Evaluation**: claims, proof, format fit, destination consistency, experiment validity, measurement, policy context and preservation

The workflow is designed to preserve approved commercial truth, resolve uncertainty at the cheapest useful fidelity, separate selection from approval, evaluate the actual requested representation, and repair only the layer responsible for a failure.

## Claims, proof and commercial control

Advertising starts from approved business decisions. It does not silently change the customer, offer, price, economics or whether paid acquisition is justified.

Keep these meanings separate:

```text
approved business segment
→ advertising audience hypothesis
→ platform targeting representation
```

And keep these decisions separate:

```text
supported fact
→ proposed claim
→ claim/proof assessment
→ creative expression
→ review / approval
→ publication authority
→ observed performance
```

Unsupported claims, fake testimonials, false scarcity, misleading prices and hidden material qualifications fail review even when the creative is persuasive. Platform acceptance is not blanket legal clearance, and a targeting signal is not proof that a hard exclusion is enforced.

Business Building or the consuming project's business owner owns customer, offer, price, business-wide channel choice and economics. Advertising owns the campaign expression and learning system built from those approved inputs.

## Install

Install the full Advertising workflow for Claude Code:

```bash
npx skills add sb-dev/advertising-production-skills \
  --skill advertising-build \
  --skill advertising-optimise \
  --skill advertising-evaluate \
  --skill advertising-pack-author \
  --agent claude-code
```

For Codex, use `--agent codex` instead.

Inspect before installing:

```bash
npx skills add sb-dev/advertising-production-skills --list
```

Install only what a project needs:

```bash
npx skills add sb-dev/advertising-production-skills \
  --skill advertising-build \
  --skill advertising-evaluate \
  --agent claude-code
```

Project-local installation is the default.

## Quick start — Local inspection search unit

Start with one bounded search advertisement and learn the core campaign-production loop without generating unnecessary media.

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

A first project should stay small:

```text
production/
└── advertising/
    └── E01/
        ├── brief.md
        ├── claim-proof.md
        ├── ad-copy.md
        ├── destination-copy.md
        └── evaluation.md
```

The important behaviour is:

```text
approved commercial truth
→ bounded campaign brief
→ supported message / claim / proof
→ exact advertisement
→ destination continuity
→ evaluation
→ smallest sufficient repair
```

See [Local inspection search unit](examples/README.md#e01-local-inspection-search-unit).

## Learn by producing

Progress through increasingly demanding advertising-production problems. Each level contains three complementary examples so the workflow demonstrates reusable campaign behaviour rather than one repeated format.

### Level 1 — Bounded advertising unit

Prove precise commercial truth, claim support and destination continuity on compact units before broader campaign production.

- **[E01 Local inspection search unit](examples/README.md#e01-local-inspection-search-unit)** — local search, scope and booking truth
- **[E02 Recurring price in a static unit](examples/README.md#e02-recurring-price-in-a-static-unit)** — subscription/refund clarity in static creative
- **[E03 A screenless B2B response](examples/README.md#e03-a-screenless-b2b-response)** — audio CTA and paid-work boundary

```text
approved facts → exact unit → destination → evaluation → local repair
```

### Level 2 — Coherent creative test

Add controlled alternatives and experiment design while keeping commercial truth fixed.

- **[E04 A controlled search-copy comparison](examples/README.md#e04-a-controlled-search-copy-comparison)** — one changed opening, fixed offer
- **[E05 Creator-native opening test](examples/README.md#e05-creator-native-opening-test)** — vertical video openings with shared body
- **[E06 Brand-linked display test](examples/README.md#e06-brand-linked-display-test)** — brand association rather than generic recall

```text
fixed commercial baseline → controlled creative difference → test contract → evaluation
```

### Level 3 — Complete campaign

Take responsibility for coherent campaign production across creative, media, destination, measurement and specialist handoffs.

- **[E07 One brand idea across display, CTV and audio](examples/README.md#e07-one-brand-idea-across-display-ctv-and-audio)** — one association across three modalities
- **[E08 Qualification-led B2B campaign](examples/README.md#e08-qualification-led-b2b-campaign)** — narrow B2B fit, proof and capacity
- **[E09 App availability, store promise and first useful action](examples/README.md#e09-app-availability-store-promise-and-first-useful-action)** — launch-state and retained-use continuity

```text
brief → concepts → selection → format production → media / destination / test → evaluation
```

### Level 4 — Diagnose and repair campaign performance

Interpret evidence before changing creative, isolate the responsible layer and preserve accepted work.

- **[E10 Retargeting report with duplicate and ineligible outcomes](examples/README.md#e10-retargeting-report-with-duplicate-and-ineligible-outcomes)** — measurement and audience eligibility repair
- **[E11 Apparent fatigue caused by a changed delivery mix](examples/README.md#e11-apparent-fatigue-caused-by-a-changed-delivery-mix)** — mix effects versus unsupported fatigue claims
- **[E12 Repair a destination without changing the accepted advertisement](examples/README.md#e12-repair-a-destination-without-changing-the-accepted-advertisement)** — source authority and bounded destination correction

```text
observations → reconcile → diagnose layer → smallest repair → preserve learning
```

### Level 5 — Full advertising-production thesis

Combine business alignment, creative production, measurement, optimisation and cross-domain handoffs on complete campaign theses.

- **[E13 Kakeibo consumer subscription launch thesis](examples/README.md#e13-kakeibo-consumer-subscription-launch-thesis)** — consumer subscription, trust and retained value
- **[E14 One-person FDE consultancy thesis](examples/README.md#e14-one-person-fde-consultancy-thesis)** — high-consideration B2B qualification and capacity
- **[E15 Production Skills ecosystem adoption and commercial thesis](examples/README.md#e15-production-skills-ecosystem-adoption-and-commercial-thesis)** — open-source adoption and paid education as separate paths

```text
business objective → campaign thesis → multi-format production → measurement → diagnosis → bounded correction
```

## Project structure grows with the campaign

**One bounded advertising unit**  
Use the brief, claim/proof map, exact creative, destination copy and evaluation.

**Creative alternatives need comparison**  
Add concept treatments, fixed/changed records and test contracts.

**Several placements share one meaning**  
Add a semantic master, placement variants and specialist production returns.

**Campaign performance needs diagnosis**  
Add source-separated measurement, lifecycle state, learning and before/after repair evidence.

**Several production domains contribute**  
Use domain-specific production areas:

```text
production/
├── advertising/
├── narrative/
├── video/
├── audio/
└── product-or-destination/
```

Keep the structure lean:

- approved business truth stays authoritative rather than being copied into competing editable records;
- concepts and placement variants preserve parent meaning and provenance;
- delivery, evidence validity, fatigue and succession remain separate states;
- repair the smallest responsible layer instead of regenerating the campaign;
- actual media masters remain distinct from placement/delivery variants.

## Skills

### `advertising-build`

Build new advertising work from approved business inputs.

Use it for campaign briefs, objectives, audience models, message and claim/proof maps, creative territories, concepts, specialist creative briefs, placement adaptation, media plans, experiments and offline launch packages.

It owns advertising production decisions, not the underlying customer, offer, price or permission to spend.

### `advertising-optimise`

Interpret campaign observations and direct bounded improvement.

Use it to ingest results, diagnose delivery, audience, creative, placement and destination problems, investigate fatigue, propose the next test, refresh creative and preserve learning.

It reconciles measurement before efficacy claims and does not treat clicks, attribution or platform labels as automatic causal evidence.

### `advertising-evaluate`

Audit advertising independently of production.

Use it to inspect claims, proof, format fit, destination continuity, experiment validity, measurement, policy context and preservation. It returns criterion-level findings and smallest repair ownership rather than one universal campaign score.

Evaluation can fail a subject while completing successfully as an evaluation task.

### `advertising-pack-author`

Create or revise reusable Advertising Extension Packs.

Use it when a repeated campaign problem needs a reusable production grammar rather than a one-off prompt. It checks existing core and catalogue coverage first, defines activation and precedence, and requires differential behaviour rather than cosmetic labels or provider wrappers.

## Extension Packs

Advertising Extension Packs specialise campaign reasoning while explicit project requirements and approved work remain authoritative.

The initial catalogue covers:

- `direct-response-performance-campaign`
- `brand-awareness-campaign`
- `b2b-demand-generation-campaign`
- `consumer-app-acquisition-campaign`
- `product-launch-campaign`
- `retargeting-and-reengagement-campaign`
- `local-service-lead-generation`
- `creator-native-social-campaign`

A pack changes useful production behaviour, not merely tone or a platform name. See the [Extension Pack contract](docs/05-advertising-production-customisation-packs-spec.md) and [catalogue](docs/06-advertising-production-extension-pack-catalogue.md).

## Execution

The Advertising skills decide **what campaign-production work is needed**. Existing specialist skills, tools and authorised systems execute it.

- **Narrative Production Skills** — story/prose craft when campaign expression needs narrative structure
- **Video Production Skills** — moving-image production and temporal evaluation
- **Audio / Music Production Skills** — speech, sound and music production where required
- **UI/UX Design Skills** — destination interaction contracts and user-state design
- **Software Engineering Skills** — destination implementation, event collection and technical integration
- **Legal Skills / qualified Legal owner** — scoped legal conclusions and legal-review returns
- **Advertising platforms and operators** — account administration, upload, bidding/spend and serving
- **Analytics / measurement owners** — collection, conversion tracking and attribution computation

> **Use the least expensive representation that can resolve the current campaign uncertainty.**
>
> **Preserve approved business decisions and change only the layer that actually failed.**

## Measurement, optimisation and learning

A complete test defines the hypothesis, changed variables, comparison, primary metric, guardrails, downstream business metric, evidence threshold, confounders and decision rule before results are interpreted.

Keep platform observations, unique qualified outcomes, business verification and causal conclusions separate. Attribution is not automatically incrementality; revenue is not contribution; missing or immature data is not zero.

Optimisation preserves five distinct campaign facets:

```text
delivery
performance assessment
evidence validity
fatigue finding
succession
```

A recommendation to pause is not an actual pause, and renaming an asset does not reset audience memory.

## Testing and benchmarks

Advertising quality is evaluated across independent dimensions rather than one universal score:

- deterministic campaign validation
- creative quality
- campaign reasoning
- business alignment
- claim / legal / policy validity
- experiment quality
- measurement quality
- optimisation / fatigue
- preservation / repair
- Extension Pack behaviour
- end-to-end campaign production
- installation integrity

See the [testing and benchmark specification](docs/04-testing-and-benchmark-spec.md) and [benchmark entry point](benchmarks/README.md).

## Documentation

### Specifications

- [System specification](docs/01-advertising-production-skills-system-spec.md)
- [Workflows and artefacts](docs/02-advertising-production-skills-workflows-and-artifacts-spec.md)
- [Repository and contracts](docs/03-advertising-production-skills-repository-and-contracts-spec.md)
- [Testing and benchmark](docs/04-testing-and-benchmark-spec.md)
- [Extension Pack contract](docs/05-advertising-production-customisation-packs-spec.md)
- [Extension Pack catalogue](docs/06-advertising-production-extension-pack-catalogue.md)

## Boundaries

Advertising Production Skills is not a replacement for Business Building, a generic marketing department, CRM, email platform, DSP, ad server, autonomous media-spend agent, attribution vendor, customer-data platform, universal audience graph, legal compliance authority or one-number campaign scorer.

Campaign-specific commercial records, customer data, account state and credentials stay in authorised consuming-project systems rather than this reusable skills repository.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Preserve approved commercial and claim semantics, keep examples synthetic unless a source is genuinely public and appropriate, and add regression protection when a structural defect escapes.

## Licence

MIT. See [LICENSE](LICENSE).

Third-party provider, asset, voice, font, model and branding rights remain separate from the repository licence.

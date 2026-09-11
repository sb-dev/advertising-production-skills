# Benchmarks and evaluation evidence

The canonical evaluation architecture is defined in [`docs/04-testing-and-benchmark-spec.md`](../docs/04-testing-and-benchmark-spec.md). This scaffold establishes the public benchmark surface without pretending runtime suites have executed.

Current state:

```text
structural repository checks → implemented and executed during scaffold verification
campaign/creative benchmark cases → designed, not run
Extension Pack comparisons → designed, not run
clean installation cases → designed, not run
```

The frozen designed coverage is recorded in [`suites.json`](suites.json): one core vertical, fifteen primary examples, forty-eight pack conditions, seventy-nine canonical cases, two pack-authoring cases, four supplemental regressions and eight installation combinations.

A future report must retain exact skill/core/pack revisions, complete prompts, actual outputs, property-appropriate inspections, failures, repairs and evidence limitations. Do not collapse the twelve evaluation dimensions into one advertising-quality score.

# Stage 23: Advertising public README contract

Date: 11 September 2026  
Status: accepted Stage 23 domain contract

## Public surface

The root `README.md` is the Advertising Production Skills product surface. It is written for someone deciding whether to install and use the project.

Bootstrap execution state, stage numbering, maturity evidence, verification counts, branch names and completion SHAs belong under `docs/research-logs/` and must not appear as user-facing README content.

## Required section order

1. project positioning and production capabilities;
2. Claims, proof and commercial control;
3. Install;
4. Quick start — Local inspection search unit, with the complete E01 prompt inline;
5. Learn by producing, five levels × three primary examples;
6. Project structure grows with the campaign;
7. Skills, with substantive sections for all four core skills;
8. Extension Packs;
9. Execution;
10. Measurement, optimisation and learning;
11. Testing and benchmarks;
12. Documentation;
13. Boundaries;
14. Contributing;
15. Licence.

## Advertising-specific control model

The README must make the following distinctions understandable without requiring the specifications:

```text
approved business segment
→ advertising audience hypothesis
→ platform targeting representation
```

and:

```text
supported fact
→ proposed claim
→ claim/proof assessment
→ creative expression
→ review / approval
→ publication authority
→ observed performance
```

It must preserve the Business Building boundary: customer, offer, price, business-wide channel choice and economics remain upstream decisions.

## Quick start

E01 is the canonical Level 1 quick start. The root README contains its complete copyable synthetic prompt. A research-log link cannot substitute for that prompt.

## Progressive examples

The public progression is exactly E01–E15, three primary examples at each of five levels. Root navigation points to the public `examples/` surface rather than directly to bootstrap research logs.

## Skill sections

The README contains substantive sections for:

- `advertising-build`;
- `advertising-optimise`;
- `advertising-evaluate`;
- `advertising-pack-author`.

A responsibility table alone is insufficient.

## Prohibited root README content

The root README must not contain user-facing material such as:

```text
Stage N
feat/bootstrap
bootstrap progress
production scaffold
maturity promotion
completion commit SHA
validator check counts
not-run suite bookkeeping
this will be implemented in Stage N
```

A genuine product limitation may be stated in product language when necessary, but not as bootstrap-process narration.

## Conformance

`tools/validate_repo.py` enforces the section contract, inline E01 facts, five-level progression, E01–E15 presence, substantive skill headings, canonical installation route, local links and obvious bootstrap-state leakage.

This Stage 23 contract adopts the Production Skills public README process at commit `da7bea1d79013de584e7d53addb7f410b6521e3f` without altering completed Advertising Stages 0–22.

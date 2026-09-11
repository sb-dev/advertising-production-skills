---
name: advertising-evaluate
description: Audits advertising claims, proof, format fit, destination continuity, experiment validity, measurement, policy context and preservation. Use for independent campaign or artefact evaluation and failure triage; returns scoped evidence without a universal quality score or implied legal approval.
license: MIT
---

# Advertising Evaluate

Evaluate advertising work against the exact request, source evidence, approved constraints and actual inspected output.

## Activate when

Use for independent claim/proof review, format/placement inspection, destination continuity, experiment/measurement review, policy-context review, preservation checks or failure triage.

Do not treat evaluation as production approval, Legal clearance, launch authority or a one-number advertising score.

## Core rules

- bind criteria to the exact subject/revision and requested fidelity;
- use deterministic evidence before semantic judgement where appropriate;
- inspect actual media when the criterion concerns media;
- separate evaluator-task completion from subject acceptance;
- identify severity, evidence, method, limits and smallest repair owner;
- preserve independent dimensions rather than averaging a material failure away.

Read [references/core-contract.md](references/core-contract.md).

## Intents

- [audit-claims](commands/audit-claims.md)
- [audit-proof](commands/audit-proof.md)
- [audit-format-fit](commands/audit-format-fit.md)
- [audit-destination-consistency](commands/audit-destination-consistency.md)
- [audit-test-validity](commands/audit-test-validity.md)
- [audit-measurement](commands/audit-measurement.md)
- [audit-policy-context](commands/audit-policy-context.md)
- [verify-preservation](commands/verify-preservation.md)
- [diagnose-advertising-failure](commands/diagnose-advertising-failure.md)

## Return contract

Return criterion-level PASS/FAIL/BLOCKED/justified NOT APPLICABLE findings with evidence locations and method. A passed structural check cannot stand in for unperformed creative, media, legal or campaign-performance evaluation.

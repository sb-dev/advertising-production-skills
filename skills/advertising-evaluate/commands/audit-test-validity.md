# audit-test-validity

**Owner:** `advertising-evaluate`

## Purpose
Audit an advertising test design or executed experiment at the appropriate evidence level.

## Inputs
Full test contract, treatments, assignment/history, permitted evidence, method and planned/readout decisions.

## Outputs
Findings on nine fields, estimand, units, eligibility, maturity, confounders, stopping and decision rule.

## Checks
Do not choose a primary metric after results, rebalance outcomes to hide assignment failure or call nonsignificance equivalence.

## Failure routing
Material logging/assignment defects block causal claims while preserving valid descriptive observations.

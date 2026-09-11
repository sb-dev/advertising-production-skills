# design-test

**Owner:** `advertising-build`

## Purpose
Design a decision-relevant advertising test without pretending it has run.

## Inputs
Decision question, exact treatments/context, assignment/observation feasibility, metric definitions, horizon and resources.

## Outputs
All nine fields: hypothesis, changed variables, comparison, primary metric, guardrails, downstream metric, evidence threshold, confounders and decision rule; also units, maturity and fixed/changed dimensions.

## Checks
Review causal scope, interference, missingness, multiple changes and feasibility. Do not invent power, duration or significance.

## Failure routing
A complete design can be accepted while live execution remains blocked for authority or feasibility.

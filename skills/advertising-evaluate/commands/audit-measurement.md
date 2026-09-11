# audit-measurement

**Owner:** `advertising-evaluate`

## Purpose
Audit the meaning and validity of campaign measurement before decisions depend on it.

## Inputs
Metric/event dictionary, actual collection/qualification evidence, snapshots, attribution, reconciliation and downstream basis.

## Outputs
Findings on meaning, unit, numerator/denominator, clock/window, maturity, deduplication, currency/value and comparability.

## Checks
Missing is not zero; submission is not retained revenue; attribution is not incrementality; invalid ratios remain invalid.

## Failure routing
Request the actual data-owner correction and preserve source observations.

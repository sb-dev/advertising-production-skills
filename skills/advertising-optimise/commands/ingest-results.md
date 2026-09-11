# ingest-results

**Owner:** `advertising-optimise`

## Purpose
Turn permitted reports/exports into source-separated observations suitable for diagnosis.

## Inputs
Exact snapshots/exports or authorised reads, source owners, variant/context and event/metric/window definitions.

## Outputs
Raw-reference ledger with numerator/denominator, units, currency/value, clocks, maturity, modelled/restricted/unknown state and reconciliation.

## Checks
Check qualification, duplication, environment and comparable windows before calculating ratios. Do not sum incompatible credits.

## Failure routing
Missing or invalid reporting blocks only conclusions that depend on it; preserve the original report and unresolved residuals.

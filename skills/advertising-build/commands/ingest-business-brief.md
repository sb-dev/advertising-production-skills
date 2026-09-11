# ingest-business-brief

**Owner:** `advertising-build`

## Purpose
Map approved business truth into the advertising brief without duplicating or changing it.

## Inputs
Exact accessible objective, offer/price/segment/channel/economics, authority restrictions and existing brief.

## Outputs
Source-linked advertising intake with knowledge state, validity, approvals and explicit conflicts/dependencies.

## Checks
A newer unapproved page does not supersede an approved commercial record; unknown price is not zero.

## Failure routing
Commercial conflicts block only affected downstream work and return to the owning business authority.

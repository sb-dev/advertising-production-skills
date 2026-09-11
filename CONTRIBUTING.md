# Contributing

Advertising Production Skills is built from explicit domain contracts. Read the owning specification and relevant research log before changing a skill, command, benchmark, example or pack contract.

## Development checks

The scaffold uses only repository-local deterministic checks:

```bash
pnpm validate
pnpm test
```

`pnpm validate` checks the repository structure, skill metadata, exact 33-intent ownership, documentation links, example/benchmark indices and evidence-status rules. `pnpm test` runs validator regression tests, including deliberately broken fixtures. Neither command is a campaign benchmark or a generated-media evaluation.

## Change discipline

- preserve approved commercial, claim and audience semantics unless the change explicitly reopens them;
- make the smallest coherent change;
- add a regression case for an escaped structural defect where practical;
- keep project/customer/private campaign data out of this public repository;
- do not add a provider wrapper, account store, CRM, DSP, attribution service or universal workflow engine;
- keep Extension Pack specialisation below explicit project requirements and approved work;
- do not mark examples, packs, host support or benchmark results complete without actual evidence.

## Pull requests

Describe the owning contract, changed files, verification performed, limitations and any follow-up evidence still required. Do not use a PR description to waive a failed acceptance criterion.

## Security and sensitive data

Never commit credentials, advertising-account identifiers, customer lists, private analytics exports, confidential client material or real financial records. Use explicitly synthetic fixtures for public tests unless the source is genuinely public and its use is appropriate.

## Licence

By contributing, you agree that your contribution is licensed under the repository's MIT licence.

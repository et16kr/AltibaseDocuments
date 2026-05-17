# Full Coverage Audit Guardrail Register

- Workflow: `altibase-gpt-full-coverage-audit`
- Initialized by: `FCA-J003`
- Status: Active register for `Guardrail` and `Out-of-scope` catalog or matrix rows

## Register Contract

Add one entry for every `Guardrail` or `Out-of-scope` row. Each entry must explain the
source boundary or customer-evidence dependency and give the safest next check or
missing input pattern.

Accepted guardrail reasons include:

- exact version or patch level is required;
- customer environment, topology, object definition, log excerpt, runtime output, or
  installed tool behavior is required;
- selected sources do not support the requested compatibility, syntax, error-code, or
  operational claim;
- the item is outside the locked selected source corpus.

## Active Guardrails

No full coverage audit `Guardrail` or `Out-of-scope` rows have been cataloged yet.
Existing rebuild-era guardrails remain in `GPTs/reports/gap_register.md` until later
FCA jobs convert them into row-level dispositions here.

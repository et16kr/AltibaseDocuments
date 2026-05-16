# Scripts

This directory is reserved for benchmark tooling:

- question and manifest validation;
- attachments-only answer generation with leakage checks;
- source-backed judging;
- aggregate report generation;
- offline fixture checks.

Script jobs must keep model and provider settings configurable and include dry-run or
offline paths that do not require live model calls.

# Job PWF-J031A: LLM Developer And Test Readiness

## Goal

Validate that the attachment set supports coding-agent implementation work and
Altibase test-case generation, not only customer Q&A.

## Steps

1. Run the required first checks from `AGENTS.md`.
2. Read `GPTs/reports/full_coverage_audit/replacement_grade_reference_policy_20260518.md`,
   `GPTs/reports/full_coverage_audit/replacement_grade_gap_register_20260518.md`, residual remediation reports, and
   instruction-aware check results.
3. Create `GPTs/reports/full_coverage_audit/llm_developer_test_readiness_20260518.md`.
4. Define and run targeted readiness checks for representative coding-agent and
   test-generation scenarios, including:
   - SQL DDL/DML and data-type edge cases;
   - JDBC, CLI/ODBC, C interface, precompiler, and iSQL/iLoader usage;
   - PSM, external procedures, and package/function examples;
   - properties, data dictionary, and performance-view checks;
   - replication, backup/recovery, security/TLS, migration, and error handling;
   - generated files, script order, permissions, and rollback or stop conditions.
5. For each scenario, verify that the attachment set provides exact tokens, required
   inputs, runnable or clearly bounded examples, validation SQL/commands, and safe
   missing-input prompts.
6. If any scenario cannot be supported, update the relevant owner report or create an
   explicit not-ready section with the exact source item, attachment gap, and owner job.
7. Run repository validation, review the diff, and commit.

## Acceptance Criteria

- Developer/test readiness evidence exists for the major Altibase implementation and
  test-generation surfaces.
- Unsupported or unsafe code-generation paths are blocked by explicit missing-input
  prompts or guardrails.
- Remaining developer/test gaps are zero or explicitly not-ready with owner evidence.
- Project files are clean after the focused commit.

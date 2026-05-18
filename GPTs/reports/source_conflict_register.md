# Source Conflict And Limitation Register

Job: `S1-J003`
Created: 2026-05-18

This register is initialized for Stage 1 source selection. `S1-J003` found no open AID
conflict or recheck rows in the reviewed AID evidence. The entries below preserve AID
accepted limitations and residual label risks so downstream package work does not
turn them into unsupported customer-facing facts.

| Conflict ID | Status | Severity | Source IDs | Paths | Version Scope | Conflict Type | Finding | Authority Policy | Resolution Or Next Check | Downstream Guardrail | Owner Job | Last Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONF-000001 | accepted_limitation | Low | AID-000015; AID-000016; AID-000022; AID-000023; AID-000025 | `~/AID/source-stabilization/legacy-attachments.tsv`; `~/AID/source-stabilization/url-backed-attachments.tsv`; `~/AID/llm-reference/coverage/semantic-unit-coverage.tsv`; `~/AID/llm-reference/coverage/attachment-diagram-register.tsv`; `~/AID/llm-reference/coverage/omissions-and-risks.tsv` | aid | source_limitation | AID records accepted limitations for legacy attachment labels with no downloadable URL, unavailable diagrams, non-document-format artifacts, source variations, and accepted English-only auxiliary rows. | Preserve AID evidence labels; do not infer missing URLs, diagrams, exact values, or source-normalized variants. Korean AID sources remain authority for future cleanup checks. | Keep the limitation labels in source-pack, baseline, playbook, attachment, and upload-package work; resolve only with direct source evidence. | Do not invent unavailable source content. Ask for source or environment evidence when an answer depends on the missing artifact or exact variant. | S1-J003 | 2026-05-18 |
| CONF-000002 | accepted_residual_risk | Info | AID-000003 | `~/AID/FAQE/Home/` English-only auxiliary subset; `~/AID/source-stabilization/source-classification.tsv`; `~/AID/llm-reference/coverage/source-inventory.tsv` | aid | weak_evidence | AID classifies 126 FAQE files as `English-only source`, outside Korean-core semantic verification, but the completed LLM reference package uses them as labeled auxiliary material. | Preserve `English-only source` and `english_only_auxiliary`; do not present this material as Korean-source-verified. | Use only with explicit source-confidence labels unless later Korean-source evidence upgrades the source class. | Customer-facing answers must expose the English-only label when source confidence matters and must not override Korean-authoritative policy. | S1-J003 | 2026-05-18 |

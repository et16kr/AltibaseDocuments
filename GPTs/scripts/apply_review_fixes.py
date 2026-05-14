#!/usr/bin/env python3
"""Apply deterministic remediation fixes from review/reports to GPTs attachments.

This script intentionally fixes only customer-facing upload attachments and writes
an application report under GPTs/reports. It does not modify review reports or
source manuals.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
ATTACH_DIR = ROOT_DIR / "GPTs" / "attachments"
DEFAULT_REPORT = ROOT_DIR / "GPTs" / "reports" / "review_remediation_report.md"


@dataclass(frozen=True)
class Fix:
    label: str
    relpath: str
    old: str
    new: str


def _p(relpath: str) -> Path:
    return ROOT_DIR / relpath


def build_fixes() -> list[Fix]:
    fixes: list[Fix] = []

    def add(label: str, relpath: str, old: str, new: str) -> None:
        fixes.append(Fix(label=label, relpath=relpath, old=old, new=new))

    add(
        "R01/R15: mark 8.1 feature families as release-note-only unless sourced elsewhere",
        "GPTs/attachments/00_version_release_platform.md",
        "- External integration: Altibase Handler for MindsDB, .NET 8 support for Altibase ADO.NET and Altibase EF Core, and `node-odbc-altibase` for Node.js.\n",
        "- External integration: Altibase Handler for MindsDB, .NET 8 support for Altibase ADO.NET and Altibase EF Core, and `node-odbc-altibase` for Node.js.\n"
        "- Release-note-only feature scope: `KADA`, Kafka connectors, `abm`, MindsDB, `.NET 8`/EF Core, and `node-odbc-altibase` are summarized here for routing and version awareness. Do not generate implementation procedures for these feature families unless a dedicated attachment or source-backed block provides the procedure.\n",
    )

    add(
        "R07/R15: add AIX 7.2 to 8.1 pre-install platform baseline",
        "GPTs/attachments/01_getting_started_installation.md",
        "Item: 8.1 platform baseline\n"
        "Altibase 8.1.0.0.1 supports Linux x86-64 on Red Hat Enterprise Linux 7, 8, and 9 for server and client. Windows 2008 and Windows 10 are client-only. Altibase 8.1 requires JDK 1.8 or higher when Java components are used.\n",
        "Item: 8.1 platform baseline\n"
        "Altibase 8.1.0.0.1 supports Linux x86-64 on Red Hat Enterprise Linux 7, 8, and 9 for server and client, and AIX 7.2 for server and client. Windows 2008 and Windows 10 are client-only. Altibase 8.1 requires JDK 1.8 or higher when Java components are used.\n",
    )

    add(
        "R07/R15: add AIX 7.2 to 8.1 version differences",
        "GPTs/attachments/01_getting_started_installation.md",
        "8.1:\n"
        "Use Altibase 8.1 release notes for supported platform, package, and compatibility guidance, and Altibase 8.1 verified source for installation workflow. Altibase 8.1.0.0.1 supports Linux x86-64 server and client on Red Hat Enterprise Linux 7, 8, and 9, supports Windows 2008 and Windows 10 client-only, supports 64-bit packages only, and requires JDK 1.8 or higher for Java components.\n",
        "8.1:\n"
        "Use Altibase 8.1 release notes for supported platform, package, and compatibility guidance, and Altibase 8.1 verified source for installation workflow. Altibase 8.1.0.0.1 supports Linux x86-64 server and client on Red Hat Enterprise Linux 7, 8, and 9, supports AIX 7.2 server and client, supports Windows 2008 and Windows 10 client-only, supports 64-bit packages only, and requires JDK 1.8 or higher for Java components.\n",
    )

    add(
        "R07/R15: remove 8.1-only CHECKPOINT_SCALE from common V$LOG query",
        "GPTs/attachments/02_administration_operations.md",
        "SELECT server_status,\n"
        "       archivelog_mode,\n"
        "       checkpoint_scale,\n"
        "       begin_chkpt_file_no,\n"
        "       begin_chkpt_file_offset,\n"
        "       end_chkpt_file_no,\n"
        "       end_chkpt_file_offset,\n"
        "       oldest_logfile_no,\n"
        "       oldest_logfile_offset,\n"
        "       transaction_segment_count\n"
        "FROM V$LOG;\n"
        "\n"
        "SELECT lfg_id,\n",
        "SELECT server_status,\n"
        "       archivelog_mode,\n"
        "       begin_chkpt_file_no,\n"
        "       begin_chkpt_file_offset,\n"
        "       end_chkpt_file_no,\n"
        "       end_chkpt_file_offset,\n"
        "       oldest_logfile_no,\n"
        "       oldest_logfile_offset,\n"
        "       transaction_segment_count\n"
        "FROM V$LOG;\n"
        "```\n\n"
        "8.1-only checkpoint-scale check:\n\n"
        "```sql\n"
        "-- Use this only after confirming the target version or column availability.\n"
        "SELECT table_name, column_name\n"
        "FROM V$ALLCOLUMN\n"
        "WHERE table_name = 'V$LOG'\n"
        "  AND column_name = 'CHECKPOINT_SCALE';\n\n"
        "SELECT checkpoint_scale\n"
        "FROM V$LOG;\n"
        "```\n\n"
        "```sql\n"
        "SELECT lfg_id,\n",
    )

    add(
        "R04: make idempotent DDL exception 8.1-only",
        "GPTs/attachments/03_sql_ddl_generation.md",
        "- For broad compatibility with 7.1 and 7.3, omit `IF NOT EXISTS` and `IF EXISTS` unless the customer targets 8.1 verified source or explicitly requests idempotent DDL.\n",
        "- For broad compatibility with 7.1 and 7.3, omit `IF NOT EXISTS` and `IF EXISTS`. If a 7.1 or 7.3 customer requests idempotent DDL, use metadata pre-check SQL plus script-side conditional execution instead of SQL-level `IF EXISTS` or `IF NOT EXISTS`. Use those clauses only when the customer targets Altibase 8.1 verified source syntax.\n",
    )

    add(
        "R03/R10/R15: split ordinary replication syntax from Log Analyzer CDC syntax in attachment 03",
        "GPTs/attachments/03_sql_ddl_generation.md",
        "```text\n"
        "replication_non_ssl ::=\n"
        "  CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "  [FOR ANALYSIS | FOR ANALYSIS PROPAGATION | FOR PROPAGABLE LOGGING | FOR PROPAGATION]\n"
        "  [AS MASTER | AS SLAVE]\n"
        "  [OPTIONS option_list]\n"
        "  WITH 'remote_host_ip_or_name', remote_replication_port [USING TCP | USING IB ib_latency]\n"
        "       [...]\n"
        "  FROM [owner.]local_table [PARTITION local_partition]\n"
        "  TO   [owner.]remote_table [PARTITION remote_partition]\n"
        "  [, FROM ... TO ...]\n\n"
        "replication_ssl_8_1 ::=\n"
        "  CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "  [AS MASTER | AS SLAVE]\n"
        "  [OPTIONS option_list]\n"
        "  WITH 'remote_host_ip_or_name', remote_ssl_replication_port USING SSL\n"
        "       [...]\n"
        "  FROM [owner.]local_table [PARTITION local_partition]\n"
        "  TO   [owner.]remote_table [PARTITION remote_partition]\n"
        "  [, FROM ... TO ...]\n\n"
        "alter_replication ::=\n",
        "```text\n"
        "replication_table_non_ssl ::=\n"
        "  CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "  [AS MASTER | AS SLAVE]\n"
        "  [OPTIONS option_list]\n"
        "  WITH 'remote_host_ip_or_name', remote_replication_port [USING TCP | USING IB ib_latency]\n"
        "       [...]\n"
        "  FROM [owner.]local_table [PARTITION local_partition]\n"
        "  TO   [owner.]remote_table [PARTITION remote_partition]\n"
        "  [, FROM ... TO ...]\n\n"
        "replication_log_analyzer_cdc ::=\n"
        "  CREATE REPLICATION replication_name\n"
        "  { FOR ANALYSIS | FOR ANALYSIS PROPAGATION | FOR PROPAGABLE LOGGING | FOR PROPAGATION }\n"
        "  [OPTIONS option_list]\n"
        "  WITH 'xlog_sender_host_ip_or_name', xlog_sender_port\n"
        "       [...]\n"
        "  FROM [owner.]local_table\n"
        "  TO   [owner.]local_table\n"
        "  [, FROM ... TO ...]\n\n"
        "replication_ssl_8_1 ::=\n"
        "  CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "  [AS MASTER | AS SLAVE]\n"
        "  [OPTIONS option_list]\n"
        "  WITH 'remote_host_ip_or_name', remote_ssl_replication_port USING SSL\n"
        "       [...]\n"
        "  FROM [owner.]local_table [PARTITION local_partition]\n"
        "  TO   [owner.]remote_table [PARTITION remote_partition]\n"
        "  [, FROM ... TO ...]\n\n"
        "alter_replication ::=\n",
    )

    add(
        "R03: add EAGER restrictions for FOR ANALYSIS and RETRY in attachment 03 notes",
        "GPTs/attachments/03_sql_ddl_generation.md",
        "- Do not combine `FOR ANALYSIS` Log Analyzer replication with `USING SSL`.\n"
        "- `SYNC` copies current target data and then starts replication. `SYNC ONLY` copies current target data without creating a Sender thread. `START` resumes from the latest restart point. `QUICKSTART` starts from the current log position and can skip unsent historical changes.\n",
        "- `FOR ANALYSIS` and related Log Analyzer forms are CDC XLog Sender syntax. Do not combine them with `EAGER`, `USING SSL`, or `USING IB`.\n"
        "- `START RETRY` and `QUICKSTART RETRY` are not supported for EAGER mode. If the replication mode is unknown, verify it before adding `RETRY`.\n"
        "- `SYNC` copies current target data and then starts replication. `SYNC ONLY` copies current target data without creating a Sender thread. `START` resumes from the latest restart point. `QUICKSTART` starts from the current log position and can skip unsent historical changes.\n",
    )

    add(
        "R10/R15: move non-SSL replication SYNC after both peer objects exist",
        "GPTs/attachments/03_sql_ddl_generation.md",
        "Non-SSL TCP replication example:\n\n"
        "Local server `192.168.10.10`, remote server `192.168.10.20`:\n\n"
        "```sql\n"
        "-- Query this on 192.168.10.20 and use the result as the port below.\n"
        "SELECT name, value1\n"
        "FROM V$PROPERTY\n"
        "WHERE name = 'REPLICATION_PORT_NO';\n\n"
        "CREATE REPLICATION rep_app_user\n"
        "WITH '192.168.10.20', 35524\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "ALTER REPLICATION rep_app_user SYNC;\n"
        "```\n\n"
        "Remote server `192.168.10.20`, local server `192.168.10.10`:\n\n"
        "```sql\n"
        "-- Query this on 192.168.10.10 and use the result as the port below.\n"
        "SELECT name, value1\n"
        "FROM V$PROPERTY\n"
        "WHERE name = 'REPLICATION_PORT_NO';\n\n"
        "CREATE REPLICATION rep_app_user\n"
        "WITH '192.168.10.10', 25524\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "ALTER REPLICATION rep_app_user SYNC;\n"
        "```\n",
        "Non-SSL TCP replication example:\n\n"
        "Local server `192.168.10.10`, remote server `192.168.10.20`:\n\n"
        "```sql\n"
        "-- Query this on 192.168.10.20 and use the result as the port below.\n"
        "SELECT name, value1\n"
        "FROM V$PROPERTY\n"
        "WHERE name = 'REPLICATION_PORT_NO';\n\n"
        "CREATE REPLICATION rep_app_user\n"
        "WITH '192.168.10.20', 35524\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n"
        "```\n\n"
        "Remote server `192.168.10.20`, local server `192.168.10.10`:\n\n"
        "```sql\n"
        "-- Query this on 192.168.10.10 and use the result as the port below.\n"
        "SELECT name, value1\n"
        "FROM V$PROPERTY\n"
        "WHERE name = 'REPLICATION_PORT_NO';\n\n"
        "CREATE REPLICATION rep_app_user\n"
        "WITH '192.168.10.10', 25524\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n"
        "```\n\n"
        "After both matching replication objects exist, run synchronization or start from the chosen source direction only:\n\n"
        "```sql\n"
        "-- Choose the source node based on Active-Standby role, Active-Active ownership, and existing data.\n"
        "ALTER REPLICATION rep_app_user SYNC;\n"
        "```\n",
    )

    add(
        "R10/R15: move SSL replication SYNC after both peer objects exist",
        "GPTs/attachments/03_sql_ddl_generation.md",
        "```sql\n"
        "-- Node A: 192.168.10.10, SSL replication receiver port 45514.\n"
        "-- Node B: 192.168.10.20, SSL replication receiver port 45524.\n"
        "-- Ordinary SSL/TLS server setup must already be complete on both nodes.\n\n"
        "-- On Node A, create the object using Node B's REPLICATION_SSL_PORT_NO.\n"
        "CREATE REPLICATION rep_app_user_ssl\n"
        "WITH '192.168.10.20', 45524 USING SSL\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "ALTER REPLICATION rep_app_user_ssl SYNC;\n\n"
        "-- On Node B, create the object using Node A's REPLICATION_SSL_PORT_NO.\n"
        "CREATE REPLICATION rep_app_user_ssl\n"
        "WITH '192.168.10.10', 45514 USING SSL\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "ALTER REPLICATION rep_app_user_ssl SYNC;\n"
        "```\n",
        "```sql\n"
        "-- Node A: 192.168.10.10, SSL replication receiver port 45514.\n"
        "-- Node B: 192.168.10.20, SSL replication receiver port 45524.\n"
        "-- Ordinary SSL/TLS server setup must already be complete on both nodes.\n\n"
        "-- On Node A, create the object using Node B's REPLICATION_SSL_PORT_NO.\n"
        "CREATE REPLICATION rep_app_user_ssl\n"
        "WITH '192.168.10.20', 45524 USING SSL\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "-- On Node B, create the object using Node A's REPLICATION_SSL_PORT_NO.\n"
        "CREATE REPLICATION rep_app_user_ssl\n"
        "WITH '192.168.10.10', 45514 USING SSL\n"
        "FROM app.app_user TO app.app_user,\n"
        "FROM app.app_document TO app.app_document;\n\n"
        "-- After both matching objects exist, run from the chosen source direction only.\n"
        "ALTER REPLICATION rep_app_user_ssl SYNC;\n"
        "```\n",
    )

    add(
        "R04: split LOB IN ROW syntax by version in core type grammar",
        "GPTs/attachments/05_data_types_properties.md",
        "lob_type ::=\n"
        "  BLOB [VARIABLE (IN ROW size)]\n"
        "  | CLOB [VARIABLE (IN ROW size)]\n\n"
        "json_type_8_1 ::=\n",
        "lob_type_7_1_7_3 ::=\n"
        "  BLOB [VARIABLE (IN ROW size)]\n"
        "  | CLOB [VARIABLE (IN ROW size)]\n\n"
        "lob_type_8_1_verified ::=\n"
        "  BLOB [IN ROW size]\n"
        "  | CLOB [IN ROW size]\n\n"
        "json_type_8_1 ::=\n",
    )

    add(
        "R06/R15: remove PSM_CASE_SENSITIVE_MODE from 8.1-new property list",
        "GPTs/attachments/05_data_types_properties.md",
        "- 8.1: Adds or documents new properties including `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `PSM_CASE_SENSITIVE_MODE`, `TEMPORARY_LOB_ENABLE`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.\n",
        "- 8.1: Adds or documents new properties including `CHECKPOINT_SCALE_SINGLE_DW_BUFFER_SIZE`, `MEMORY_TEMPLOB_MAX_ALLOC_SIZE`, `MEMORY_TEMPLOB_PIECE_SIZE`, `REPLICATION_SSL_PORT_NO`, `TEMPORARY_LOB_ENABLE`, `TRCLOG_EXPLAIN_TYPE`, and `TRCLOG_JSON_PLAN_INDENT_DEPTH`.\n"
        "- Cross-version property caution: `PSM_CASE_SENSITIVE_MODE` and `REGEXP_MODE` are documented in sampled 7.x and 8.1 sources. Do not label them as 8.1-only unless the customer asks about a target build where the installed documentation proves a narrower scope.\n",
    )

    add(
        "R04: add 8.1 LOB syntax note to BLOB item",
        "GPTs/attachments/05_data_types_properties.md",
        "```sql\n"
        "BLOB [VARIABLE (IN ROW size)]\n"
        "```\n",
        "```sql\n"
        "-- 7.1 and 7.3 source syntax\n"
        "BLOB [VARIABLE (IN ROW size)]\n\n"
        "-- Altibase 8.1 verified source syntax\n"
        "BLOB [IN ROW size]\n"
        "```\n",
    )

    add(
        "R04: add 8.1 LOB syntax note to CLOB item",
        "GPTs/attachments/05_data_types_properties.md",
        "```sql\n"
        "CLOB [VARIABLE (IN ROW size)]\n"
        "```\n",
        "```sql\n"
        "-- 7.1 and 7.3 source syntax\n"
        "CLOB [VARIABLE (IN ROW size)]\n\n"
        "-- Altibase 8.1 verified source syntax\n"
        "CLOB [IN ROW size]\n"
        "```\n",
    )

    add(
        "R06/R15: reclassify PSM_CASE_SENSITIVE_MODE as cross-version",
        "GPTs/attachments/05_data_types_properties.md",
        "### Property Item: `PSM_CASE_SENSITIVE_MODE`\n\n"
        "Version: 8.1 baseline property.\n",
        "### Property Item: `PSM_CASE_SENSITIVE_MODE`\n\n"
        "Version: 7.1, 7.3, and 8.1 documented property; verify exact behavior against the installed build before treating it as newly introduced.\n",
    )

    add(
        "R06/R15: reclassify REGEXP_MODE as cross-version",
        "GPTs/attachments/05_data_types_properties.md",
        "### Property Item: `REGEXP_MODE`\n\n"
        "Version: 8.1 verified source property.\n",
        "### Property Item: `REGEXP_MODE`\n\n"
        "Version: 7.1, 7.3, and 8.1 documented property where PCRE2 regular expression processing is available; verify exact behavior against the installed build.\n",
    )

    add(
        "R08/R15: add branch-specific not-found diagnostics",
        "GPTs/attachments/07_error_messages_troubleshooting.md",
        "```sql\n"
        "SELECT user_name\n"
        "FROM SYSTEM_.SYS_USERS_\n"
        "WHERE user_name = '<OWNER_NAME>';\n\n"
        "SELECT u.user_name, t.table_name, t.table_type\n"
        "FROM SYSTEM_.SYS_TABLES_ t,\n"
        "     SYSTEM_.SYS_USERS_ u\n"
        "WHERE t.user_id = u.user_id\n"
        "  AND u.user_name = '<OWNER_NAME>'\n"
        "  AND t.table_name = '<OBJECT_NAME>';\n"
        "```\n",
        "```sql\n"
        "-- User check.\n"
        "SELECT user_name\n"
        "FROM SYSTEM_.SYS_USERS_\n"
        "WHERE user_name = '<OWNER_NAME>';\n\n"
        "-- Table, view, queue, or sequence-style object check.\n"
        "SELECT u.user_name, t.table_name, t.table_type\n"
        "FROM SYSTEM_.SYS_TABLES_ t,\n"
        "     SYSTEM_.SYS_USERS_ u\n"
        "WHERE t.user_id = u.user_id\n"
        "  AND u.user_name = '<OWNER_NAME>'\n"
        "  AND t.table_name = '<OBJECT_NAME>';\n\n"
        "-- Column check.\n"
        "SELECT u.user_name, t.table_name, c.column_name\n"
        "FROM SYSTEM_.SYS_USERS_ u,\n"
        "     SYSTEM_.SYS_TABLES_ t,\n"
        "     SYSTEM_.SYS_COLUMNS_ c\n"
        "WHERE u.user_id = t.user_id\n"
        "  AND t.table_id = c.table_id\n"
        "  AND u.user_name = '<OWNER_NAME>'\n"
        "  AND t.table_name = '<TABLE_NAME>'\n"
        "  AND c.column_name = '<COLUMN_NAME>';\n\n"
        "-- Index check.\n"
        "SELECT u.user_name, t.table_name, i.index_name\n"
        "FROM SYSTEM_.SYS_USERS_ u,\n"
        "     SYSTEM_.SYS_TABLES_ t,\n"
        "     SYSTEM_.SYS_INDICES_ i\n"
        "WHERE u.user_id = t.user_id\n"
        "  AND t.table_id = i.table_id\n"
        "  AND u.user_name = '<OWNER_NAME>'\n"
        "  AND t.table_name = '<TABLE_NAME>'\n"
        "  AND i.index_name = '<INDEX_NAME>';\n\n"
        "-- Replication definition and host checks.\n"
        "SELECT replication_name, is_started, repl_mode, role\n"
        "FROM SYSTEM_.SYS_REPLICATIONS_\n"
        "WHERE replication_name = '<REPLICATION_NAME>';\n\n"
        "SELECT replication_name, host_ip, port_no, conn_type\n"
        "FROM SYSTEM_.SYS_REPL_HOSTS_\n"
        "WHERE replication_name = '<REPLICATION_NAME>';\n"
        "```\n",
    )

    add(
        "R08/R15: split PCRE2 unsupported character set and unexpected error handling",
        "GPTs/attachments/07_error_messages_troubleshooting.md",
        "Primary Causes: `REGEXP_MODE=1` with an unsupported Altibase server character set, invalid pattern, or PCRE2 runtime error.\n\n"
        "Immediate Action: Check `REGEXP_MODE`, server character set, and pattern. If the character set is unsupported, set `REGEXP_MODE` to `0` or plan a database recreation with a supported character set.\n",
        "Primary Causes: `REGEXP_MODE=1` with an unsupported Altibase server character set, invalid pattern, or PCRE2 runtime error.\n\n"
        "Immediate Action: Branch by error code. For `0x2106B`, check `REGEXP_MODE`, server character set, and pattern; if the character set is unsupported, set `REGEXP_MODE` to `0` or plan a database recreation with a supported character set. For `0x2106C`, collect the PCRE2 detail text, Altibase version, SQL text, `REGEXP_MODE`, server character set, and trace context before escalating to Altibase Support.\n",
    )

    add(
        "R08/R15: use replication meta tables before runtime views for duplicate replication",
        "GPTs/attachments/07_error_messages_troubleshooting.md",
        "```sql\n"
        "SELECT rep_name,\n"
        "       status,\n"
        "       sender_ip,\n"
        "       sender_port,\n"
        "       peer_ip,\n"
        "       peer_port,\n"
        "       net_error_flag\n"
        "FROM V$REPSENDER\n"
        "ORDER BY rep_name;\n\n"
        "SELECT rep_name,\n"
        "       rep_gap,\n"
        "       rep_gap_size\n"
        "FROM V$REPGAP\n"
        "ORDER BY rep_name;\n"
        "```\n",
        "```sql\n"
        "-- Primary check: replication definitions, including stopped or not-yet-started objects.\n"
        "SELECT replication_name, is_started, repl_mode, role\n"
        "FROM SYSTEM_.SYS_REPLICATIONS_\n"
        "WHERE replication_name = '<REPLICATION_NAME>'\n"
        "ORDER BY replication_name;\n\n"
        "SELECT replication_name, host_ip, port_no, conn_type\n"
        "FROM SYSTEM_.SYS_REPL_HOSTS_\n"
        "WHERE replication_name = '<REPLICATION_NAME>'\n"
        "   OR (host_ip = '<PEER_HOST>' AND port_no = <PEER_PORT>)\n"
        "ORDER BY replication_name, host_ip, port_no;\n\n"
        "-- Secondary runtime check after a definition is known to exist.\n"
        "SELECT rep_name, status, sender_ip, sender_port, peer_ip, peer_port, net_error_flag\n"
        "FROM V$REPSENDER\n"
        "WHERE rep_name = '<REPLICATION_NAME>'\n"
        "ORDER BY rep_name;\n\n"
        "SELECT rep_name, rep_gap, rep_gap_size\n"
        "FROM V$REPGAP\n"
        "WHERE rep_name = '<REPLICATION_NAME>'\n"
        "ORDER BY rep_name;\n"
        "```\n",
    )

    add(
        "R00/R01/R15: remove internal Conversion TODO/JOB label from troubleshooting attachment",
        "GPTs/attachments/07_error_messages_troubleshooting.md",
        "## Conversion TODO\n\n"
        "- None for JOB-042. Future deep-dive jobs may add additional error blocks for specific utilities or connectors while preserving the standardized error format above.\n",
        "## Residual Scope\n\n"
        "- Add future error blocks only after source-backed review, and keep the standardized error format above.\n",
    )

    add(
        "R09: add DBMS_SQL_PLAN_CACHE coverage for 7.3/8.1",
        "GPTs/attachments/08_performance_tuning_monitoring.md",
        "Shared cache areas:\n\n"
        "- `Shared SQL Plan Cache`: stores SQL execution plans.\n"
        "- `Stored Procedure Cache`: stores stored procedure execution plans.\n"
        "- `Meta Cache`: stores metadata for quick access.\n\n"
        "SQL Plan Cache architecture:\n",
        "Shared cache areas:\n\n"
        "- `Shared SQL Plan Cache`: stores SQL execution plans.\n"
        "- `Stored Procedure Cache`: stores stored procedure execution plans.\n"
        "- `Meta Cache`: stores metadata for quick access.\n\n"
        "Version-aware plan pinning:\n\n"
        "- 7.3 and 8.1 sources document `DBMS_SQL_PLAN_CACHE.KEEP_PLAN(sql_text_id)` and `DBMS_SQL_PLAN_CACHE.UNKEEP_PLAN(sql_text_id)` for keeping or releasing a specific cached execution plan.\n"
        "- Do not present `DBMS_SQL_PLAN_CACHE` as common to 7.1 unless the customer confirms equivalent support in the installed source.\n"
        "- Verify pinned plan state with `V$SQL_PLAN_CACHE_SQLTEXT.PLAN_CACHE_KEEP` and `V$SQL_PLAN_CACHE_PCO.PLAN_CACHE_KEEP`.\n\n"
        "SQL Plan Cache architecture:\n",
    )

    add(
        "R09: replace Monitoring API default credentials with placeholders",
        "GPTs/attachments/08_performance_tuning_monitoring.md",
        "rc = ABISetProperty(ABI_USER, \"SYS\");\n"
        "rc = ABISetProperty(ABI_PASSWD, \"MANAGER\");\n",
        "rc = ABISetProperty(ABI_USER, \"<MONITOR_USER>\");\n"
        "rc = ABISetProperty(ABI_PASSWD, \"<MONITOR_PASSWORD>\");\n",
    )

    add(
        "R09: replace SNMP default community strings with placeholders",
        "GPTs/attachments/08_performance_tuning_monitoring.md",
        "# snmpd.conf\n"
        "rocommunity public\n"
        "rwcommunity private\n"
        "trap2sink localhost public <trap-port>\n"
        "master agentx\n",
        "# snmpd.conf\n"
        "rocommunity <readonly-community>\n"
        "rwcommunity <readwrite-community>\n"
        "trap2sink <trap-host> <trap-community> <trap-port>\n"
        "master agentx\n"
        "# Restrict SNMP ACLs and do not use default community strings in production.\n",
    )

    add(
        "R09/R15: caveat SNMP continuous session failure trap code",
        "GPTs/attachments/08_performance_tuning_monitoring.md",
        "- `10000103`: continuous session failure when the configured session failure count threshold is reached. Level `2`.\n",
        "- Continuous session failure trap code: sampled SNMP sources conflict between a `10000201` section label and `10000103` example output. Do not hard-code one value in generated alert rules until the target-version `snmptrapd` output is validated. Level `2`.\n",
    )

    add(
        "R01/R02/R03/R10/R15: replace unsafe Active-Active and sharding overview",
        "GPTs/attachments/09_replication_ha_cdc.md",
        "## Altibase Active-Active Replication & Sharding Overview\n"
        "- **Active-Active Replication**: Altibase natively supports High Availability (HA) through a proprietary in-memory Active-Active replication protocol (XLog). It guarantees sub-millisecond latency and built-in conflict resolution without requiring external clustering software.\n"
        "- **Sharding (ShardManager)**: Altibase provides scale-out capabilities via sharding. This involves configuring shard nodes, defining shard keys, and initializing shard metadata. If a user asks about scaling out, refer to Altibase's sharding capabilities. Note that specific shard routing errors are covered in the error message references.\n",
        "## Altibase Replication and Scope Overview\n"
        "- **Active-Active Replication**: Altibase supports replication topologies through XLog-based Sender and Receiver processing. Active-Active use requires explicit write ownership, conflict avoidance or conflict policy design, replication gap monitoring, and failover/failback planning. Do not promise fixed latency or automatic conflict-free behavior.\n"
        "- **Scale-out scope**: Sharding and `ShardManager` setup are outside this attachment's selected replication, HA, CDC, Log Analyzer, and replication SSL source family. Do not generate sharding configuration procedures from this file; use a dedicated sharding source audit if a user asks for scale-out setup.\n",
    )

    add(
        "R03/R10/R15: split CREATE REPLICATION syntax in attachment 09",
        "GPTs/attachments/09_replication_ha_cdc.md",
        "```text\n"
        "CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "  [FOR ANALYSIS | FOR PROPAGABLE LOGGING | FOR PROPAGATION | FOR ANALYSIS PROPAGATION]\n"
        "  [AS MASTER | AS SLAVE]\n"
        "  [OPTIONS option_name [option_name ...]]\n"
        "  WITH 'remote_host_ip_or_name', remote_host_port_no [USING conn_type [ib_latency]]\n"
        "       [...]\n"
        "  FROM user_name.table_name [PARTITION partition_name]\n"
        "  TO   user_name.table_name [PARTITION partition_name]\n"
        "  [, FROM ... TO ...];\n"
        "```\n",
        "```text\n"
        "ordinary_table_replication ::=\n"
        "  CREATE [LAZY | EAGER] REPLICATION [IF NOT EXISTS] replication_name\n"
        "    [AS MASTER | AS SLAVE]\n"
        "    [OPTIONS option_name [option_name ...]]\n"
        "    WITH 'remote_host_ip_or_name', remote_host_port_no [USING conn_type [ib_latency]]\n"
        "         [...]\n"
        "    FROM user_name.table_name [PARTITION partition_name]\n"
        "    TO   user_name.table_name [PARTITION partition_name]\n"
        "    [, FROM ... TO ...];\n\n"
        "log_analyzer_cdc_replication ::=\n"
        "  CREATE REPLICATION replication_name\n"
        "    { FOR ANALYSIS | FOR PROPAGABLE LOGGING | FOR PROPAGATION | FOR ANALYSIS PROPAGATION }\n"
        "    [OPTIONS option_name [option_name ...]]\n"
        "    WITH 'xlog_sender_host_ip_or_name', xlog_sender_port_no\n"
        "         [...]\n"
        "    FROM user_name.table_name\n"
        "    TO   user_name.table_name\n"
        "    [, FROM ... TO ...];\n"
        "```\n",
    )

    add(
        "R03/R10/R15: add LAZY-only FOR ANALYSIS note in attachment 09",
        "GPTs/attachments/09_replication_ha_cdc.md",
        "- `FOR ANALYSIS` creates an XLog Sender for Log Analyzer CDC, not ordinary table-to-table apply.\n",
        "- `FOR ANALYSIS` and related Log Analyzer CDC forms create an XLog Sender and are not ordinary table-to-table apply syntax. Do not combine them with `EAGER`, `USING SSL`, or `USING IB`; Log Analyzer CDC is LAZY/TCP or UNIX-domain-socket scoped.\n",
    )

    add(
        "R03: add EAGER restriction for START RETRY in attachment 09",
        "GPTs/attachments/09_replication_ha_cdc.md",
        "- Creates a Sender thread even when the first handshake fails.\n"
        "- iSQL can show success even when the initial handshake failed.\n"
        "- Verify with trace logs and `V$REPSENDER`.\n",
        "- Creates a Sender thread even when the first handshake fails.\n"
        "- iSQL can show success even when the initial handshake failed.\n"
        "- `RETRY` is not supported for EAGER-mode replication. Verify the replication mode before recommending `START RETRY` or `QUICKSTART RETRY`.\n"
        "- Verify with trace logs and `V$REPSENDER`.\n",
    )

    add(
        "R10/R15: replace mixed replication DDL procedure with separate standard and sync procedures",
        "GPTs/attachments/09_replication_ha_cdc.md",
        "Standard DDL procedure:\n\n"
        "```sql\n"
        "-- 1. Migrate service away from the node where required.\n"
        "SELECT COUNT(*) FROM V$SESSION WHERE ID <> SESSION_ID();\n\n"
        "-- 2. Set required properties on both nodes.\n"
        "ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1;\n"
        "ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 1;\n"
        "ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 1;\n\n"
        "-- 3. Use the replication object's default mode.\n"
        "ALTER SESSION SET REPLICATION = DEFAULT;\n\n"
        "-- 4. Clear gap, run DDL on both nodes, and clear gap again.\n"
        "ALTER REPLICATION rep1 FLUSH;\n"
        "-- Execute the same DDL on both nodes.\n"
        "ALTER REPLICATION rep1 FLUSH;\n\n"
        "-- 5. Verify SQL apply mode ended.\n"
        "SELECT rep_name, sql_apply_table_count\n"
        "FROM V$REPRECEIVER;\n\n"
        "-- 6. Restore defaults.\n"
        "ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 0;\n"
        "ALTER SYSTEM SET REPLICATION_DDL_ENABLE_LEVEL = 0;\n"
        "ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 0;\n"
        "```\n",
        "Standard DDL procedure without SQL apply mode:\n\n"
        "```sql\n"
        "-- 1. Schedule a maintenance window, stop service traffic or enter the documented admin flow.\n"
        "SELECT COUNT(*) FROM V$SESSION WHERE ID <> SESSION_ID();\n\n"
        "-- 2. Flush replication and verify no remaining gap before DDL.\n"
        "ALTER REPLICATION rep1 FLUSH ALL WAIT 60;\n"
        "SELECT rep_name, rep_gap, rep_gap_size\n"
        "FROM V$REPGAP\n"
        "WHERE rep_name = 'REP1';\n\n"
        "-- 3. Stop replication and remove the target tables from every affected replication object.\n"
        "ALTER REPLICATION rep1 STOP;\n"
        "ALTER REPLICATION rep1 DROP TABLE FROM app.t1 TO app.t1;\n\n"
        "-- 4. Execute the DDL on every node with identical object names and compatible storage choices.\n"
        "-- ALTER TABLE app.t1 ...;\n\n"
        "-- 5. Add targets back, then resynchronize or start according to the topology and data ownership.\n"
        "ALTER REPLICATION rep1 ADD TABLE FROM app.t1 TO app.t1;\n"
        "ALTER REPLICATION rep1 SYNC;\n"
        "```\n\n"
        "DDL synchronization procedure with SQL apply mode:\n\n"
        "```sql\n"
        "-- 1. Use this only for documented DDL synchronization cases, not for EAGER targets or RECOVERY-enabled objects.\n"
        "-- 2. On the local server that will execute the DDL:\n"
        "ALTER SESSION SET REPLICATION_DDL_SYNC = 1;\n\n"
        "-- 3. On the remote server, enable DDL sync and SQL apply support for the receiver side.\n"
        "ALTER SYSTEM SET REPLICATION_DDL_SYNC = 1;\n"
        "ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 1;\n\n"
        "-- 4. Flush before executing the DDL on the local server only.\n"
        "ALTER REPLICATION rep1 FLUSH ALL WAIT 60;\n"
        "-- ALTER TABLE app.t1 ...;\n\n"
        "-- 5. Verify apply completion, then restore properties.\n"
        "SELECT rep_name, sql_apply_table_count\n"
        "FROM V$REPRECEIVER\n"
        "WHERE rep_name = 'REP1';\n\n"
        "ALTER SESSION SET REPLICATION_DDL_SYNC = 0;\n"
        "ALTER SYSTEM SET REPLICATION_DDL_SYNC = 0;\n"
        "ALTER SYSTEM SET REPLICATION_SQL_APPLY_ENABLE = 0;\n"
        "```\n",
    )

    add(
        "R12/R15: state SQLGetLob 1-based fromPosition rule",
        "GPTs/attachments/12_c_cli_odbc_precompiler.md",
        "- `fromPosition`: byte-based start point for reading. The source argument text describes positions as byte positions, and the sample loop starts the first chunk with offset `0`; keep offsets consistent with the target version's sample convention.\n",
        "- `fromPosition`: byte-based start point for reading. `SQLGetLob()` `fromPosition` is documented as 1-based. If a source sample initializes a first full-read loop with offset `0`, treat that as a sample-specific convention and test against the target client patch before generating partial-read code.\n",
    )

    add(
        "R12/R15: state SQLPutLob 1-based fromPosition rule",
        "GPTs/attachments/12_c_cli_odbc_precompiler.md",
        "- Position rule: do not pass a position greater than the current target LOB length. Manual examples use `fromPosition=0` for new or whole-value locator patterns and positive positions for partial overwrite.\n",
        "- Position rule: `SQLPutLob()` `fromPosition` is documented as 1-based for partial writes. Do not pass a position greater than the current target LOB length. If a source sample uses `fromPosition=0` for new or whole-value locator patterns, label it as a sample-specific full-value convention rather than the generic partial-write rule.\n",
    )

    add(
        "R13/R15: correct AKU Kubernetes service field spelling",
        "GPTs/attachments/14_utilities_operation_tools.md",
        "- Set `publishNotReadyAddress` to true for the Kubernetes service.\n",
        "- Set `publishNotReadyAddresses: true` for the Kubernetes service.\n",
    )

    add(
        "R11: avoid promising connector-specific TLS property placement from attachment 16",
        "GPTs/attachments/16_dblink_external_connectors.md",
        "- For SSL/TLS, truststores, certificate verification, and ciphers, use this attachment for connector property names and the SSL/TLS attachment for certificate preparation.\n",
        "- For SSL/TLS, truststores, certificate verification, and ciphers, use `11_java_jdbc_spring.md` and `18_security_ssl_tls.md` for Altibase JDBC/SSL parameter names. This attachment gives connector workflow context and should not invent connector-specific TLS placement unless the connector accepts the documented Altibase JDBC URL or properties.\n",
    )

    add(
        "R13/R15: remove destructive OpenLDAP DROP USER reset",
        "GPTs/attachments/16_dblink_external_connectors.md",
        "Example user creation:\n\n"
        "```sql\n"
        "DROP USER ldap CASCADE;\n"
        "CREATE USER ldap IDENTIFIED BY ldap;\n"
        "```\n",
        "Example user creation:\n\n"
        "```sql\n"
        "CREATE USER ldap IDENTIFIED BY '<password>';\n"
        "```\n\n"
        "Do not include `DROP USER ... CASCADE` in production setup examples. If a lab reset is required, document the destructive impact, backup requirement, and explicit operator approval outside the copy-ready setup path.\n",
    )

    add(
        "R11: narrow FIPS ALTIBASE_SSL_LOAD_CONFIG wording to ODBC/CLI",
        "GPTs/attachments/18_security_ssl_tls.md",
        "6. For FIPS on 7.3 or 8.1 verified source, set `ALTIBASE_SSL_LOAD_CONFIG=1` on clients that use OpenSSL and set `SSL_LOAD_CONFIG=1` on the server.\n",
        "6. For FIPS on 7.3 or 8.1 verified source, set `ALTIBASE_SSL_LOAD_CONFIG=1` for ODBC/CLI clients and set `SSL_LOAD_CONFIG=1` on the server. For ADO.NET or other clients, use only source-documented SSL connection keys unless a matching guide explicitly documents FIPS config loading.\n",
    )

    add(
        "R11: add certificate verification caution to ADO.NET example",
        "GPTs/attachments/18_security_ssl_tls.md",
        "```text\n"
        "Server=127.0.0.1;Port=20443;User=user;Password=pwd;conn type=ssl;ssl ca=/altibase_home/sample/CERT/ca-cert.pem;ssl cert=/altibase_home/sample/CERT/client-cert.pem;ssl key=/altibase_home/sample/CERT/client-key.pem\n"
        "```\n",
        "```text\n"
        "Server=127.0.0.1;Port=20443;User=user;Password=pwd;conn type=ssl;ssl ca=/altibase_home/sample/CERT/ca-cert.pem;ssl cert=/altibase_home/sample/CERT/client-cert.pem;ssl key=/altibase_home/sample/CERT/client-key.pem\n"
        "```\n\n"
        "Production server-certificate verification requires `ssl verify=true` plus `ssl ca` or `ssl capath`; do not copy the manual-style example as a complete production verification pattern without that setting.\n",
    )

    return fixes


def apply_one(fix: Fix, *, dry_run: bool, verbose: bool) -> tuple[str, str]:
    path = _p(fix.relpath)
    text = path.read_text(encoding="utf-8")

    if fix.new in text:
        return "already_applied", fix.label

    if fix.old in text:
        new_text = text.replace(fix.old, fix.new, 1)
        if new_text == text:
            return "unchanged", fix.label
        if verbose or dry_run:
            diff = difflib.unified_diff(
                text.splitlines(),
                new_text.splitlines(),
                fromfile=str(path.relative_to(ROOT_DIR)),
                tofile=str(path.relative_to(ROOT_DIR)),
                lineterm="",
                n=3,
            )
            print("\n".join(diff))
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")
        return "would_apply" if dry_run else "applied", fix.label

    raise RuntimeError(
        f"anchor not found for fix: {fix.label}\n"
        f"file: {fix.relpath}\n"
        "The attachment may have changed. Recheck the review finding and update this script anchor."
    )


def apply_fixes(*, dry_run: bool, verbose: bool, report_path: Path | None) -> int:
    results: list[tuple[str, str]] = []
    for fix in build_fixes():
        status, label = apply_one(fix, dry_run=dry_run, verbose=verbose)
        results.append((status, label))
        print(f"{status}: {label}")

    if dry_run:
        print("dry-run: validation against modified files was skipped")
        return 0

    failures = validate(quiet=False)
    if report_path and not dry_run:
        write_report(report_path, results, failures)
        print(f"report: {report_path.relative_to(ROOT_DIR)}")

    return 1 if failures else 0


def plan() -> int:
    for index, fix in enumerate(build_fixes(), start=1):
        print(f"{index:02d}. {fix.label} -> {fix.relpath}")
    return 0


def _attachment_files() -> list[Path]:
    return sorted(p for p in ATTACH_DIR.glob("*.md") if p.name != "README.md")


def validate(*, quiet: bool) -> list[str]:
    failures: list[str] = []
    files = _attachment_files()

    def fail(message: str) -> None:
        failures.append(message)
        if not quiet:
            print(f"FAIL: {message}")

    def ok(message: str) -> None:
        if not quiet:
            print(f"PASS: {message}")

    if len(files) == 20:
        ok("20 upload attachment Markdown files are present")
    else:
        fail(f"expected 20 upload attachment Markdown files, found {len(files)}")

    combined = "\n".join(f"--- {p.name} ---\n{p.read_text(encoding='utf-8')}" for p in files)

    forbidden = [
        (r"\bJOB-[0-9]+\b", "internal job labels"),
        (r"\bIMG-[0-9]+\b", "internal image labels"),
        (r"Conversion TODO", "conversion TODO heading"),
        (r"guarantees sub-millisecond latency", "unsafe replication latency guarantee"),
        (r"built-in conflict resolution", "unsafe conflict-resolution guarantee"),
        (r"publishNotReadyAddress\b", "misspelled Kubernetes service field"),
        (r"DROP USER\s+ldap\s+CASCADE", "destructive OpenLDAP setup reset"),
        (
            r"CREATE \[LAZY \| EAGER\] REPLICATION \[IF NOT EXISTS\] replication_name\s+"
            r"\[FOR ANALYSIS",
            "combined EAGER and FOR ANALYSIS grammar",
        ),
        (r"clients that use OpenSSL", "over-broad FIPS client wording"),
    ]
    for pattern, description in forbidden:
        if re.search(pattern, combined, flags=re.IGNORECASE):
            fail(f"forbidden pattern remains: {description}")
        else:
            ok(f"forbidden pattern absent: {description}")

    positive_checks = [
        ("GPTs/attachments/01_getting_started_installation.md", "AIX 7.2", "8.1 AIX support"),
        ("GPTs/attachments/03_sql_ddl_generation.md", "replication_log_analyzer_cdc ::=", "split Log Analyzer syntax in attachment 03"),
        ("GPTs/attachments/03_sql_ddl_generation.md", "script-side conditional execution", "7.1/7.3 idempotent DDL guidance"),
        ("GPTs/attachments/05_data_types_properties.md", "lob_type_8_1_verified ::=", "8.1 LOB syntax split"),
        ("GPTs/attachments/05_data_types_properties.md", "7.1, 7.3, and 8.1 documented property", "cross-version property wording"),
        ("GPTs/attachments/07_error_messages_troubleshooting.md", "SYSTEM_.SYS_REPL_HOSTS_", "replication meta-table diagnostics"),
        ("GPTs/attachments/08_performance_tuning_monitoring.md", "sampled SNMP sources conflict between a `10000201`", "SNMP trap ambiguity caveat"),
        ("GPTs/attachments/09_replication_ha_cdc.md", "Do not promise fixed latency", "safe replication overview"),
        ("GPTs/attachments/09_replication_ha_cdc.md", "ordinary_table_replication ::=", "split CREATE REPLICATION syntax in attachment 09"),
        ("GPTs/attachments/12_c_cli_odbc_precompiler.md", "`SQLGetLob()` `fromPosition` is documented as 1-based", "SQLGetLob position rule"),
        ("GPTs/attachments/12_c_cli_odbc_precompiler.md", "`SQLPutLob()` `fromPosition` is documented as 1-based", "SQLPutLob position rule"),
        ("GPTs/attachments/14_utilities_operation_tools.md", "publishNotReadyAddresses: true", "AKU field spelling"),
        ("GPTs/attachments/16_dblink_external_connectors.md", "Do not include `DROP USER ... CASCADE`", "OpenLDAP destructive reset warning"),
        ("GPTs/attachments/18_security_ssl_tls.md", "for ODBC/CLI clients", "FIPS ODBC/CLI scope"),
    ]
    for relpath, needle, description in positive_checks:
        text = _p(relpath).read_text(encoding="utf-8")
        if needle in text:
            ok(f"expected remediation present: {description}")
        else:
            fail(f"expected remediation missing: {description}")

    admin = _p("GPTs/attachments/02_administration_operations.md").read_text(encoding="utf-8")
    if "       checkpoint_scale,\n       begin_chkpt_file_no" in admin:
        fail("checkpoint_scale still appears in the common V$LOG query")
    else:
        ok("checkpoint_scale removed from the common V$LOG query")

    return failures


def write_report(path: Path, results: list[tuple[str, str]], failures: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    today = _dt.date.today().isoformat()
    lines = [
        "# Review Remediation Application Report",
        "",
        f"Date: {today}",
        "Source: `review/reports/R00_*.md` through `review/reports/R15_multilingual_final_readiness.md`",
        "Scope: customer-facing upload attachments under `GPTs/attachments/`.",
        "",
        "## Applied Fixes",
        "",
        "| Status | Fix |",
        "| --- | --- |",
    ]
    for status, label in results:
        lines.append(f"| `{status}` | {label} |")
    lines.extend(["", "## Validation", ""])
    if failures:
        lines.append("Result: Fail")
        lines.append("")
        for failure in failures:
            lines.append(f"- {failure}")
    else:
        lines.append("Result: Pass")
        lines.append("")
        lines.append("- Script validation found no remaining targeted Blocker/High review patterns.")
        lines.append("- Re-run the detailed review reports or final readiness review before upload.")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("plan", help="List deterministic fixes without reading or writing attachments.")

    apply_parser = sub.add_parser("apply", help="Apply deterministic review remediation fixes.")
    apply_parser.add_argument("--dry-run", action="store_true", help="Print actions without writing files.")
    apply_parser.add_argument("--verbose", action="store_true", help="Show unified diffs while applying.")
    apply_parser.add_argument(
        "--report",
        default=str(DEFAULT_REPORT),
        help="Report path. Use an empty string to skip report writing.",
    )

    validate_parser = sub.add_parser("validate", help="Validate targeted review-remediation conditions.")
    validate_parser.add_argument("--quiet", action="store_true", help="Only set exit code.")

    args = parser.parse_args(argv)
    command = args.command or "plan"

    if command == "plan":
        return plan()

    if command == "apply":
        dry_run = bool(args.dry_run or os.environ.get("DRY_RUN") == "1")
        report_path = Path(args.report).resolve() if args.report else None
        return apply_fixes(dry_run=dry_run, verbose=args.verbose, report_path=report_path)

    if command == "validate":
        failures = validate(quiet=args.quiet)
        return 1 if failures else 0

    parser.error(f"unknown command: {command}")
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

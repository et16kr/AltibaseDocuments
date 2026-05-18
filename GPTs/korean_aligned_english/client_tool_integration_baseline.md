# Korean-Aligned English Baseline: Client Tool Integration Batch

- Job: `S1-J009`
- Scope: client interfaces, APIs, tools, utilities, migration, DB Link,
  connectors, Spatial, NiFi, Tableau, Kubernetes/AKU, and selected
  integration sources.
- Source-pack gate: `GPTs/source_pack/source_pack_validation.md` records
  `Status: pass`, `Verdict: Pass`, no blockers, and explicit permission to
  continue to the Korean-aligned English baseline.
- Authority rule: Korean product manuals, Korean tool manuals, Korean release
  notes, Korean third-party guides, and Korean technical documents are
  authoritative. English files are extraction aids unless explicitly classified
  otherwise. For 8.1 material, preserve the established `Altibase 8.1 verified
  source` boundary.
- Downstream boundary: this file is a working baseline for guarded first
  drafts. It does not replace exact source-pack extraction, installed header
  files, installed client-tool help, live connector tests, or customer runtime
  evidence.

## Batch Source Coverage

| Source family | Korean source IDs | English or auxiliary source IDs | Baseline manifest rows |
| --- | --- | --- | --- |
| CLI, ODBC, ACI, APRE, API | `SRC-000046`, `SRC-000050`, `SRC-000052`, `SRC-000065`, `SRC-000068`, `SRC-000110`, `SRC-000114`, `SRC-000116`, `SRC-000128`, `SRC-000130`, `SRC-000170`, `SRC-000174`, `SRC-000176`, `SRC-000188`, `SRC-000190` | `SRC-000015`, `SRC-000019`, `SRC-000021`, `SRC-000034`, `SRC-000036`, `SRC-000079`, `SRC-000083`, `SRC-000085`, `SRC-000097`, `SRC-000099`, `SRC-000140`, `SRC-000144`, `SRC-000146`, `SRC-000158`, `SRC-000160` | `KAE-BLOCK-000002` through `KAE-BLOCK-000006`, `KAE-BLOCK-000137` through `KAE-BLOCK-000141`, `KAE-BLOCK-000192` through `KAE-BLOCK-000196` |
| JDBC, Java, Spring, Hibernate, Adapter for JDBC | `SRC-000047`, `SRC-000061`, `SRC-000111`, `SRC-000125`, `SRC-000171`, `SRC-000185`, `SRC-000473`, `SRC-000012`, `SRC-000013` | `SRC-000016`, `SRC-000030`, `SRC-000080`, `SRC-000094`, `SRC-000141`, `SRC-000155`, `SRC-000005`, `SRC-000006` | `KAE-BLOCK-000016`, `KAE-BLOCK-000017`, `KAE-BLOCK-000151`, `KAE-BLOCK-000152`, `KAE-BLOCK-000207`, `KAE-BLOCK-000208`, `KAE-BLOCK-000231`, `KAE-BLOCK-000247`, `KAE-BLOCK-000248` |
| iSQL and iLoader | `SRC-000077`, `SRC-000078`, `SRC-000138`, `SRC-000139`, `SRC-000198`, `SRC-000199` | `SRC-000044`, `SRC-000045`, `SRC-000107`, `SRC-000108`, `SRC-000167`, `SRC-000168` | `KAE-BLOCK-000014`, `KAE-BLOCK-000015`, `KAE-BLOCK-000149`, `KAE-BLOCK-000150`, `KAE-BLOCK-000205`, `KAE-BLOCK-000206` |
| Utilities, operation tools, dataCompJ | `SRC-000076`, `SRC-000137`, `SRC-000197`, `SRC-000222`, `SRC-000227`, `SRC-000208`, `SRC-000213`, `SRC-000471` | `SRC-000043`, `SRC-000106`, `SRC-000166`, `SRC-000215`, `SRC-000220`, `SRC-000201`, `SRC-000206`, `SRC-000449` | `KAE-BLOCK-000038`, `KAE-BLOCK-000170`, `KAE-BLOCK-000227`, `KAE-BLOCK-000228`, `KAE-BLOCK-000229`, `KAE-BLOCK-000251`, `KAE-BLOCK-000252`, `KAE-BLOCK-000271` |
| Migration Center and Adapter for Oracle | `SRC-000048`, `SRC-000112`, `SRC-000172`, `SRC-000223`, `SRC-000209`, `SRC-000453` through `SRC-000463` | `SRC-000017`, `SRC-000081`, `SRC-000142`, `SRC-000216`, `SRC-000202`, `SRC-000430` through `SRC-000439`, `SRC-000442` | `KAE-BLOCK-000019`, `KAE-BLOCK-000154`, `KAE-BLOCK-000210`, `KAE-BLOCK-000211`, `KAE-BLOCK-000232`, `KAE-BLOCK-000254` through `KAE-BLOCK-000263`, `KAE-BLOCK-000266` |
| DB Link, Hadoop, third-party connectors | `SRC-000053`, `SRC-000059`, `SRC-000117`, `SRC-000123`, `SRC-000177`, `SRC-000183`, `SRC-000221`, `SRC-000207` | `SRC-000022`, `SRC-000028`, `SRC-000086`, `SRC-000092`, `SRC-000147`, `SRC-000153`, `SRC-000214`, `SRC-000200` | `KAE-BLOCK-000007`, `KAE-BLOCK-000008`, `KAE-BLOCK-000142`, `KAE-BLOCK-000143`, `KAE-BLOCK-000197`, `KAE-BLOCK-000198`, `KAE-BLOCK-000199`, `KAE-BLOCK-000230` |
| Kubernetes, AKU, NiFi, Tableau, Spatial, altiShapeLoader | `SRC-000008`, `SRC-000009`, `SRC-000010`, `SRC-000014`, `SRC-000074`, `SRC-000135`, `SRC-000195`, `SRC-000226`, `SRC-000212`, `SRC-000470` | `SRC-000002`, `SRC-000003`, `SRC-000004`, `SRC-000007`, `SRC-000041`, `SRC-000104`, `SRC-000164`, `SRC-000219`, `SRC-000205`, `SRC-000448` | `KAE-BLOCK-000034`, `KAE-BLOCK-000165`, `KAE-BLOCK-000221`, `KAE-BLOCK-000222`, `KAE-BLOCK-000238`, `KAE-BLOCK-000239`, `KAE-BLOCK-000244`, `KAE-BLOCK-000245`, `KAE-BLOCK-000246`, `KAE-BLOCK-000249` |

## KAE-CLIENTTOOLS-BLOCK-001: JDBC, Java, Spring, Hibernate, And Adapter For JDBC

- Source IDs: `SRC-000047`, `SRC-000016`, `SRC-000061`, `SRC-000030`,
  `SRC-000111`, `SRC-000080`, `SRC-000125`, `SRC-000094`, `SRC-000171`,
  `SRC-000141`, `SRC-000185`, `SRC-000155`, `SRC-000473`, `SRC-000012`,
  `SRC-000005`, `SRC-000013`, `SRC-000006`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, and the selected
  Spring/Hibernate third-party guide source versions.
- Source block refs: `SRC-000047/BLOCK-000552`, `SRC-000016/BLOCK-000550`,
  `SRC-000061/BLOCK-000553`, `SRC-000030/BLOCK-000551`,
  `SRC-000111/BLOCK-000556`, `SRC-000080/BLOCK-000554`,
  `SRC-000125/BLOCK-000557`, `SRC-000094/BLOCK-000555`,
  `SRC-000171/BLOCK-000560`, `SRC-000141/BLOCK-000558`,
  `SRC-000185/BLOCK-000561`, `SRC-000155/BLOCK-000559`,
  `SRC-000473/BLOCK-000562`, `SRC-000012/BLOCK-000923`,
  `SRC-000005/BLOCK-000916`, `SRC-000013/BLOCK-000924`,
  `SRC-000006/BLOCK-000917`.
- Alignment status: baseline generated from Korean JDBC, Adapter for JDBC,
  Java compatibility, Spring Data JPA, and Hibernate guide sources. No live
  Java, Spring, Hibernate, application-server, or failover test was run.

Baseline:

1. Collect the exact Altibase version and patch, JDK vendor and version,
   application framework version, selected JDBC JAR path, database host, port,
   database name, user, password handling method, TLS files, failover targets,
   and connection-pool behavior before generating code.
2. Preserve driver and JAR tokens exactly as source-backed candidates:
   `Altibase.jar`, `Altibase42.jar`, `Altibase7_1.jar`,
   `Altibase42_7_1.jar`, `Altibase_t.jar`, and
   `Altibase.jdbc.driver.AltibaseDriver`. Select the actual JAR only after
   checking the installed `$ALTIBASE_HOME/lib` directory or the delivered
   client package.
3. Use the JDBC URL shape `jdbc:Altibase://host_ip:port_no/database_name`.
   Source-backed examples include attributes with `?` and `&`, such as
   `jdbc:Altibase://localhost:20300/mydb?fetch_enough=0&time_zone=DB_TZ`.
   Do not invent non-source URL attributes.
4. Preserve connection properties and attribute names exactly when present:
   `fetch_enough`, `time_zone`, `login_timeout`, `query_timeout`,
   `lob_null_select`, `ssl_enable`, `verify_server_certificate`,
   `truststore_url`, `truststore_type`, `truststore_password`,
   `keystore_url`, `keystore_type`, `keystore_password`,
   `alternateservers`, `loadbalance`, `connectionretrycount`,
   `connectionretrydelay`, `sessionfailover`, and
   `AltibaseFailoverCallback`.
5. For failover examples, keep the source-backed property style:
   `sProps.put("alternateservers", "(database1:20300, database2:20300)")`.
   Ask for customer topology, retry policy, transaction handling expectation,
   and callback behavior before making it production code.
6. For TLS examples, require customer-provided truststore and keystore paths,
   passwords, certificate policy, and server-name verification policy before
   generating a final connection string. Do not present `ssl_enable=true` alone
   as a complete security configuration.
7. For 8.1 statement-cache material, preserve `stmt_cache_enable`,
   `stmt_cache_size`, `stmt_cache_sql_limit`, and
   `Statement.setPoolable(false/true)`. Do not combine source-backed
   driver-side statement cache advice with a duplicate DBCP cache unless the
   customer asks for a pool-specific design and provides the pool settings.
8. For Spring Data JPA and Hibernate examples, preserve Maven and property
   tokens including `com.altibase`, `altibase-jdbc`,
   `org.hibernate.orm:hibernate-community-dialects`,
   `spring.datasource.driver-class-name`, `spring.datasource.url`, and
   `spring.jpa.properties.hibernate.jdbc.lob.non_contextual_creation`.
   Source-backed Hibernate 6.4 guidance uses
   `jdbc:Altibase://127.0.0.1:20300/mydb?lob_null_select=off`.
9. Preserve the version boundary for `lob_null_select`: source guidance says
   7.1 requires `lob_null_select=off` for the referenced Hibernate path, while
   7.3 and 8.1 default to off. Do not broaden that into a general JDBC rule
   without checking the target JDBC source.
10. Treat Java compatibility tables as evidence labels. `Oracle OpenJDK`,
    `Oracle JDK`, `IBM SDK`, `x`, `●`, and `-` must not be normalized into
    unsupported prose. In particular, do not turn `-` into a tested support
    statement.

Safe first checks:

- Check `java -version`, the installed JDBC JAR name, and the exact source
  version before generating build files.
- Confirm the database accepts a basic JDBC connection before layering Spring,
  Hibernate, TLS, failover, or connection-pool behavior.
- For failover or session failover, run a controlled non-production test and
  capture connection logs before claiming behavior.

Stop conditions:

- Stop if the requested JDK, Spring, Hibernate, application server, pool, TLS,
  or failover behavior is not present in the selected sources or customer
  evidence.
- Stop if a generated example requires a password, truststore, keystore,
  callback class, or failover topology that the customer has not provided.
- Stop if the answer depends on driver implementation behavior not exposed by
  source text, installed JAR metadata, or a live test.

## KAE-CLIENTTOOLS-BLOCK-002: CLI, ODBC, Altibase C Interface, And Precompiler/APRE

- Source IDs: `SRC-000046`, `SRC-000015`, `SRC-000050`, `SRC-000019`,
  `SRC-000052`, `SRC-000021`, `SRC-000065`, `SRC-000034`, `SRC-000068`,
  `SRC-000036`, `SRC-000110`, `SRC-000079`, `SRC-000114`, `SRC-000083`,
  `SRC-000116`, `SRC-000085`, `SRC-000128`, `SRC-000097`, `SRC-000130`,
  `SRC-000099`, `SRC-000170`, `SRC-000140`, `SRC-000174`, `SRC-000144`,
  `SRC-000176`, `SRC-000146`, `SRC-000188`, `SRC-000158`, `SRC-000190`,
  `SRC-000160`.
- Version scope: 7.1, 7.3, and `Altibase 8.1 verified source`.
- Source block refs: `SRC-000046/BLOCK-000467`, `SRC-000015/BLOCK-000462`,
  `SRC-000050/BLOCK-000468`, `SRC-000019/BLOCK-000463`,
  `SRC-000052/BLOCK-000469`, `SRC-000021/BLOCK-000464`,
  `SRC-000065/BLOCK-000470`, `SRC-000034/BLOCK-000465`,
  `SRC-000068/BLOCK-000471`, `SRC-000036/BLOCK-000466`,
  `SRC-000110/BLOCK-000477`, `SRC-000079/BLOCK-000472`,
  `SRC-000114/BLOCK-000478`, `SRC-000083/BLOCK-000473`,
  `SRC-000116/BLOCK-000479`, `SRC-000085/BLOCK-000474`,
  `SRC-000128/BLOCK-000480`, `SRC-000097/BLOCK-000475`,
  `SRC-000130/BLOCK-000481`, `SRC-000099/BLOCK-000476`,
  `SRC-000170/BLOCK-000487`, `SRC-000140/BLOCK-000482`,
  `SRC-000174/BLOCK-000488`, `SRC-000144/BLOCK-000483`,
  `SRC-000176/BLOCK-000489`, `SRC-000146/BLOCK-000484`,
  `SRC-000188/BLOCK-000490`, `SRC-000158/BLOCK-000485`,
  `SRC-000190/BLOCK-000491`, `SRC-000160/BLOCK-000486`.
- Alignment status: baseline generated from paired Korean authority and
  English extraction aids. Exact structure definitions, every function
  signature, and every diagnostic code path remain source-recheck items.

Baseline:

1. Collect compiler, OS, bitness, `ALTIBASE_HOME`, include path, library path,
   driver manager use, DSN name, server host, port, NLS settings, user,
   password handling method, transaction policy, LOB/GEOMETRY/JSON use, and
   target API before writing build or connection code.
2. Preserve CLI handle-order tokens and call shapes exactly when generating
   examples: `SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &env)`,
   `SQLAllocHandle`, `SQLDriverConnect`, `SQLConnect`, and `SQLEndTran`.
   Generated code must include diagnostic collection, cleanup paths, and
   transaction handling rather than only the happy path.
3. Preserve ODBC DSN and connection-string tokens:
   `DSN=ALTIBASE;LongDataCompat=ON` and
   `DRIVER=ALTIBASE_HDB_ODBC_64bit;User=SYS;Password=<password>;Server=127.0.0.1;PORT=20300;NLS_USE=US7ASCII;LongDataCompat=ON`.
   The source-backed `LongDataCompat=ON` mapping for `SQL_BLOB` and `SQL_CLOB`
   must not be generalized beyond the ODBC source.
4. Preserve `DEFER_PREPARES=ON` only as a source-backed connection option.
   Do not apply it by default without checking the target source and customer
   workload.
5. For 8.1 JSON LOB work, preserve `SQLPutLob`, `SQLFreeLob2(stmt, locator)`,
   and `SQLEndTran`. `SQLFreeLob2()` releases the locator and is not a commit
   or rollback substitute.
6. For Altibase C Interface result handling, preserve
   `altibase_store_result()` and `altibase_use_result()` behavior boundaries.
   Avoid `altibase_store_result()` examples for large result sets, LOBs, or
   GEOMETRY values unless the customer explicitly wants full result buffering.
7. Preserve compile and link tokens: `$ALTIBASE_HOME/include/sqlcli.h`,
   `$ALTIBASE_HOME/lib/libodbccli.a`, `-I$ALTIBASE_HOME/include`,
   `-L$ALTIBASE_HOME/lib -lodbccli`, `alticapi.h`, `libalticapi.a`,
   `-lalticapi`, and `-lodbccli`.
8. Preserve APRE/Precompiler tokens: `APRE`, `apre`, `.sc`, `.c`, `-t cpp`,
   `libapre.a`, `libodbccli.a`, `-lapre`, `-lodbccli`, `WHENEVER`, `SQLCA`,
   `SQLCODE`, `SQLSTATE`, `sqlerrm.sqlerrmc`, `sqlerrm.sqlerrml`, and
   `sqlerrd[2]`. Do not generate Oracle-only `sqlwarn` handling for Altibase.
9. Selected 8.1 sources name `SQLEmptyLob()` and `SQLGetLobLength2()`, but the
   checked baseline sources do not provide complete callable signatures. Treat
   these as recheck items against installed headers or exact source blocks
   before generating compile-ready code.

Safe first checks:

- Verify `$ALTIBASE_HOME/include` and `$ALTIBASE_HOME/lib` exist and match the
  installed client version before compiling.
- Build a minimal connect, execute, fetch, diagnostics, commit, rollback, and
  cleanup program before adding LOB, JSON, or APRE logic.
- For ODBC, check the DSN or driver entry and confirm `LongDataCompat` behavior
  in a non-production test if LOB columns are involved.

Stop conditions:

- Stop if the requested API call is not present in the selected manual,
  installed header, or customer-provided header excerpt.
- Stop if code generation would require an unknown compiler, bitness, library
  path, DSN, transaction policy, LOB lifecycle, or NLS setting.
- Stop if an Oracle precompiler pattern conflicts with Altibase APRE source
  behavior.

## KAE-CLIENTTOOLS-BLOCK-003: iSQL And iLoader

- Source IDs: `SRC-000077`, `SRC-000044`, `SRC-000078`, `SRC-000045`,
  `SRC-000138`, `SRC-000107`, `SRC-000139`, `SRC-000108`, `SRC-000198`,
  `SRC-000167`, `SRC-000199`, `SRC-000168`, with release-note context from
  `SRC-000450`, `SRC-000427`, `SRC-000452`, `SRC-000429`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, and selected
  patch-level release-note context.
- Source block refs: `SRC-000077/BLOCK-000540`, `SRC-000044/BLOCK-000538`,
  `SRC-000078/BLOCK-000541`, `SRC-000045/BLOCK-000539`,
  `SRC-000138/BLOCK-000544`, `SRC-000107/BLOCK-000542`,
  `SRC-000139/BLOCK-000545`, `SRC-000108/BLOCK-000543`,
  `SRC-000198/BLOCK-000548`, `SRC-000167/BLOCK-000546`,
  `SRC-000199/BLOCK-000549`, `SRC-000168/BLOCK-000547`,
  `SRC-000450/BLOCK-000821`, `SRC-000427/BLOCK-000820`,
  `SRC-000452/BLOCK-000826`, `SRC-000429/BLOCK-000825`.
- Alignment status: baseline generated from Korean tool manuals and selected
  release notes. Full patch-by-patch option history remains a recheck item.

Baseline:

1. Collect target version and patch, `ALTIBASE_HOME`, host, port, user,
   password handling method, target schema/table, delimiter, character set,
   geometry format, partition target, replication-column handling, input/output
   file paths, error threshold, and desired file permissions before generating
   iSQL or iLoader commands.
2. Preserve iSQL connection tokens and modes:
   `isql -S server_name -PORT port_no -U user_id -P password`, `/NOLOG`,
   `-SYSDBA`, `-KEEP_SYSDBA`, `-F`, and `-O`.
3. Preserve iSQL output capture tokens: `SPOOL filename` and `SPOOL OFF`.
   Generated runbooks must name the output file and expected artifact.
4. Preserve security-sensitive file-permission variables:
   `ALTIBASE_UT_FILE_PERMISSION`, `ISQL_FILE_PERMISSION`,
   `AEXPORT_FILE_PERMISSION`, and `ILO_FILE_PERMISSION`. Source-backed default
   behavior includes `666`; use `600` in guarded examples unless a customer
   policy requires otherwise.
5. Preserve iLoader operation flow: `formout` to create a format file, `out`
   to export data, `in` to import data, and `structout` only when the source
   command is appropriate. Source-backed file examples include `employees.fmt`
   and `employees.dat`.
6. Preserve iLoader core options and files: `-T`, `-f`, `-d`,
   `-mode replace`, `-mode append`, `-mode truncate`, `-log`, `-bad`,
   and `-errors`. Generated import examples must explain where rejected rows
   and logs are written.
7. Preserve advanced iLoader tokens only with source-backed boundaries:
   `-silent`, `-nst`, `-displayquery`, `-replication true/false`,
   `-partition`, `-geom WKB`, `-verbose`, `-readsize`, `-async_prefetch`,
   `-lightmode`, and version-scoped `-stmt_prefix`.
8. Treat `-dry-run` as a recheck item. It appears in syntax/help in selected
   sources, but the checked baseline sources do not provide full production
   semantics.

Safe first checks:

- Use iSQL to confirm the target table, column order, data types, constraints,
  and permissions before generating iLoader `in` commands.
- Run iLoader on a small non-production sample and inspect `-log`, `-bad`,
  and `-errors` artifacts before full import.
- For `-geom WKB`, require source and target GEOMETRY format evidence before
  writing a production command.

Stop conditions:

- Stop if the table definition, delimiter, character set, partition name,
  replication handling, or file path is missing.
- Stop if `REPLACE`, `TRUNCATE`, or other destructive load behavior is
  requested without explicit customer approval and rollback plan.
- Stop if a patch-specific option is needed but the target patch and installed
  tool help are unavailable.

## KAE-CLIENTTOOLS-BLOCK-004: Utilities, aexport, altiComp, dataCompJ, Dump Tools, And Operation Tools

- Source IDs: `SRC-000076`, `SRC-000043`, `SRC-000137`, `SRC-000106`,
  `SRC-000197`, `SRC-000166`, `SRC-000222`, `SRC-000215`, `SRC-000227`,
  `SRC-000220`, `SRC-000208`, `SRC-000201`, `SRC-000213`, `SRC-000206`,
  `SRC-000471`, `SRC-000449`, with release-note context from `SRC-000451`,
  `SRC-000428`, `SRC-000452`, `SRC-000429`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`,
  `7.3.0.0.1`, `8.1.0.0.1`, and `dataCompJ 7.2`.
- Source block refs: `SRC-000076/BLOCK-000927`, `SRC-000043/BLOCK-000926`,
  `SRC-000137/BLOCK-000929`, `SRC-000106/BLOCK-000928`,
  `SRC-000197/BLOCK-000931`, `SRC-000166/BLOCK-000930`,
  `SRC-000222/BLOCK-000934`, `SRC-000215/BLOCK-000932`,
  `SRC-000227/BLOCK-000935`, `SRC-000220/BLOCK-000933`,
  `SRC-000208/BLOCK-000940`, `SRC-000201/BLOCK-000938`,
  `SRC-000213/BLOCK-000941`, `SRC-000206/BLOCK-000939`,
  `SRC-000471/BLOCK-000937`, `SRC-000449/BLOCK-000936`,
  `SRC-000451/BLOCK-000824`, `SRC-000428/BLOCK-000823`,
  `SRC-000452/BLOCK-000826`, `SRC-000429/BLOCK-000825`.
- Alignment status: baseline generated from Korean Utilities, Heartbeat,
  dataCompJ, and release-note sources. No live utility execution was performed.

Baseline:

1. Collect target version and patch, `ALTIBASE_HOME`, connection endpoint,
   credentials, target objects, data directory, transaction/log file paths,
   Java version for Java tools, source/target database pair, and rollback plan
   before generating utility commands.
2. For `aexport`, preserve the `DBMS_METADATA` prerequisite and the
   source-backed error token `ERR-91144 : DBMS_METADATA package does not exist`.
   If that package is missing, install or update the package according to the
   exact release/source guidance before treating `aexport` output as complete.
3. Preserve `aexport` generated-script order and output names:
   `run_il_out.sh`, `run_is.sh`, `run_il_in.sh`,
   `run_is_refresh_mview.sh`, `run_is_index.sh`, `run_is_fk.sh`,
   `run_is_alt_tbl.sh`, and `run_is_con.sh`.
4. Preserve permission guardrails for generated files:
   `AEXPORT_FILE_PERMISSION`, `ALTIBASE_UT_FILE_PERMISSION`, default `666`,
   and guarded example value `600`.
5. Preserve `altiComp` operation and comparison tokens: `DIFF`, `SYNC`,
   `MOSO`, `MOSX`, `MXSO`, `SU`, `SI`, `MI`, and `SD`. `MI` and `SD` are
   mutually exclusive in the selected source context.
6. Preserve `dataCompJ` command and configuration tokens:
   `dataCompJ`, `dataCompJCli.sh -f dataCompJ_env_file_path`,
   `Connections`, `Options`, `TablePairs`, `DIFF`, `SYNC`,
   `dataCompJ_report.txt`, `dataCompJ.log`, and `dataCompJ_data.log`.
   Source-backed package names include `dataCompJ7.2.zip` and
   `dataCompJ7.2.tar.gz`.
7. Preserve dataCompJ release-note identifiers and dependency context:
   `BUG-45222`, `BUG-46675`, `BUG-46689`, `BUG-49501`, and `Log4j 2.17.1`.
   Do not convert release-note issue text into a broad compatibility statement.
8. Preserve `altierr` examples exactly when generating diagnostic checks:
   `altierr 0x00015`, `altierr -w 00015`, `altierr 21`,
   `altierr -266286`, `altierr 266286`, `altierr 0x4102E`, and
   `altierr -w connect`.
9. Preserve dump-family tool names and intended evidence role:
   `dumpbi`, `dumpct`, `dumpdb`, `dumpddf`, `dumpla`, `dumplf`, and
   `dumptrc`. Do not generate file interpretation claims without the exact
   target file type and version.

Safe first checks:

- Verify tool version and environment with the installed binary or script help
  before using option-level commands.
- For `aexport`, confirm `DBMS_METADATA` exists before trusting generated
  schema scripts.
- For `dataCompJ`, run `DIFF` and inspect `dataCompJ_report.txt`,
  `dataCompJ.log`, and `dataCompJ_data.log` before any `SYNC`.

Stop conditions:

- Stop if a utility command writes, synchronizes, truncates, migrates, or
  rebuilds objects without explicit rollback and customer approval.
- Stop if the input file, output directory, Java runtime, object list, or
  source/target database identity is missing.
- Stop if the requested interpretation depends on a binary dump file not
  provided in the workspace.

## KAE-CLIENTTOOLS-BLOCK-005: Migration Center And Adapter For Oracle

- Source IDs: `SRC-000048`, `SRC-000017`, `SRC-000112`, `SRC-000081`,
  `SRC-000172`, `SRC-000142`, `SRC-000223`, `SRC-000216`, `SRC-000209`,
  `SRC-000202`, `SRC-000453`, `SRC-000430`, `SRC-000454`, `SRC-000431`,
  `SRC-000455`, `SRC-000432`, `SRC-000456`, `SRC-000433`, `SRC-000457`,
  `SRC-000434`, `SRC-000458`, `SRC-000435`, `SRC-000459`, `SRC-000436`,
  `SRC-000460`, `SRC-000437`, `SRC-000461`, `SRC-000438`, `SRC-000462`,
  `SRC-000439`, `SRC-000463`, `SRC-000442`.
- Version scope: Adapter for Oracle 7.1, 7.3, `Altibase 8.1 verified source`,
  Migration Center trunk/release sources, and Migration Center 7.9 through
  7.19 release notes.
- Source block refs: `SRC-000048/BLOCK-000570`, `SRC-000017/BLOCK-000569`,
  `SRC-000112/BLOCK-000572`, `SRC-000081/BLOCK-000571`,
  `SRC-000172/BLOCK-000574`, `SRC-000142/BLOCK-000573`,
  `SRC-000223/BLOCK-000576`, `SRC-000216/BLOCK-000575`,
  `SRC-000209/BLOCK-000602`, `SRC-000202/BLOCK-000601`,
  `SRC-000453/BLOCK-000578`, `SRC-000430/BLOCK-000577`,
  `SRC-000454/BLOCK-000580`, `SRC-000431/BLOCK-000579`,
  `SRC-000455/BLOCK-000582`, `SRC-000432/BLOCK-000581`,
  `SRC-000456/BLOCK-000584`, `SRC-000433/BLOCK-000583`,
  `SRC-000457/BLOCK-000586`, `SRC-000434/BLOCK-000585`,
  `SRC-000458/BLOCK-000588`, `SRC-000435/BLOCK-000587`,
  `SRC-000459/BLOCK-000590`, `SRC-000436/BLOCK-000589`,
  `SRC-000460/BLOCK-000592`, `SRC-000437/BLOCK-000591`,
  `SRC-000461/BLOCK-000594`, `SRC-000438/BLOCK-000593`,
  `SRC-000462/BLOCK-000596`, `SRC-000439/BLOCK-000595`,
  `SRC-000463/BLOCK-000600`, `SRC-000442/BLOCK-000599`.
- Alignment status: baseline generated from Korean Migration Center and
  Adapter for Oracle sources. No live Oracle, Altibase, ALA, OCI, or Migration
  Center run was performed.

Baseline:

1. Collect Migration Center version, source DBMS and version, target Altibase
   version, JDK version, OS, JDBC driver paths, project directory, object
   scope, LOB presence, primary-key coverage, character sets, migration
   downtime policy, validation policy, rollback plan, and network access before
   generating migration commands.
2. Preserve Migration Center runtime boundaries from the selected sources:
   Java 8 or later, GUI requires Swing, CLI does not require OS graphics,
   Oracle source versions are source-listed as `10gR2` through `21c`, and
   Altibase target is source-listed as `6.5.1` or later. Do not broaden these
   into support for unlisted databases or untested Java versions.
3. Preserve the CLI stage sequence and command tokens:
   `./migcenter.sh register register.xml`,
   `./migcenter.sh build project_path`,
   `./migcenter.sh reconcile project_path`,
   `./migcenter.sh run project_path`,
   `./migcenter.sh diff project_path`, and
   `./migcenter.sh filesync project_path`.
4. Preserve GUI stage names: `Prepare`, `Build`, `Reconcile`, `Run`, and
   `Data Validation`.
5. Preserve Data Validation constraints: selected sources limit validation to
   tables with `Primary Key`, exclude LOB from the checked path, and provide
   `Write to CSV` and `FILESYNC` flows. Do not promise full logical
   equivalence without customer-provided validation evidence.
6. Preserve release-note boundaries for Migration Center 7.9 through 7.19 as
   Migration Center release-note versions, not Altibase server versions. Java
   17 untested and Java 18 tested information must stay scoped to the exact
   release-note compatibility table where it appears.
7. For Adapter for Oracle, preserve `Adapter for Oracle`, ALA, OCI,
   `ALA_SENDER_IP`, `ALA_RECEIVER_PORT`, `ALA_SOCKET_TYPE`, `ALTIBASE_IP`,
   startup output `Altibase Adapter started.`, and
   `ALTER REPLICATION ala START`.
8. Preserve `oraAdapter` property-file rules and option semantics from the
   exact source. Do not infer retry, skip, or default behavior from generic
   Oracle adapter assumptions.

Safe first checks:

- Confirm source and target JDBC connectivity outside Migration Center before
  creating or running a project.
- Run `register`, `build`, and `reconcile` before `run`; inspect generated
  reports and mapping decisions before migration.
- For Adapter for Oracle, confirm ALA configuration and startup output before
  issuing `ALTER REPLICATION ala START`.

Stop conditions:

- Stop if source DBMS version, target Altibase version, JDK, JDBC driver, object
  scope, LOB policy, primary keys, character sets, or project path are missing.
- Stop if the customer asks for a destructive or cutover step without backup,
  rollback, validation, and downtime approval.
- Stop if Migration Center 7.7 or 7.8 release-note evidence is needed; the
  selected manifest rows are English-only and remain excluded until Korean
  authority or approved auxiliary use is recorded.

## KAE-CLIENTTOOLS-BLOCK-006: DB Link, Hadoop Connector, And Third-Party Connectors

- Source IDs: `SRC-000053`, `SRC-000022`, `SRC-000059`, `SRC-000028`,
  `SRC-000117`, `SRC-000086`, `SRC-000123`, `SRC-000092`, `SRC-000177`,
  `SRC-000147`, `SRC-000183`, `SRC-000153`, `SRC-000221`, `SRC-000214`,
  `SRC-000207`, `SRC-000200`.
- Version scope: DB Link and Hadoop Connector for 7.1, 7.3, and
  `Altibase 8.1 verified source`; third-party connector guide trunk and
  release sources.
- Source block refs: `SRC-000053/BLOCK-000494`, `SRC-000022/BLOCK-000492`,
  `SRC-000059/BLOCK-000495`, `SRC-000028/BLOCK-000493`,
  `SRC-000117/BLOCK-000498`, `SRC-000086/BLOCK-000496`,
  `SRC-000123/BLOCK-000499`, `SRC-000092/BLOCK-000497`,
  `SRC-000177/BLOCK-000502`, `SRC-000147/BLOCK-000500`,
  `SRC-000183/BLOCK-000503`, `SRC-000153/BLOCK-000501`,
  `SRC-000221/BLOCK-000505`, `SRC-000214/BLOCK-000504`,
  `SRC-000207/BLOCK-000507`, `SRC-000200/BLOCK-000506`.
- Alignment status: baseline generated from Korean DB Link, Hadoop Connector,
  and third-party connector guide sources. No live remote DBMS, Hadoop, Sqoop,
  DBeaver, OpenLDAP, or Oracle GoldenGate test was run.

Baseline:

1. Collect local Altibase version, remote DBMS and driver, network path,
   authentication method, character set, linker host/port, XA need, security
   policy, transaction semantics, Hadoop/Sqoop versions, and exact connector
   product version before generating integration steps.
2. Preserve DB Link properties and configuration tokens:
   `DBLINK_ENABLE`, `ALTILINKER_ENABLE`, `ALTILINKER_PORT_NO`, `AltiLinker`,
   `TARGETS`, `JDBC_DRIVER`, `CONNECTION_URL`, `USER`, `PASSWORD`,
   `XADATASOURCE_CLASS_NAME`, `XADATASOURCE_URL_SETTER_NAME`, and
   `NLS_BYTE_PER_CHAR`.
3. Preserve DB Link SQL and validation tokens:
   `CREATE PRIVATE DATABASE LINK link1 CONNECT TO ... USING ...`,
   `ALTER DATABASE LINKER START`, `V$DBLINK_ALTILINKER_STATUS`,
   `V$DBLINK_DATABASE_LINK_INFO`, `REMOTE_TABLE`, and
   `REMOTE_EXECUTE_IMMEDIATE`.
4. Preserve 8.1-only DB Link syntax boundaries for `IF NOT EXISTS`,
   `IF EXISTS`, and encrypted-password use through `altiEncrypt` in `dblink`.
   Do not apply those constructs to 7.1 or 7.3 without exact source evidence.
5. Preserve Hadoop Connector tokens and versions from the selected sources:
   Hadoop `1.0`, Sqoop `1.4.4` or later,
   `altibase_sqoop14_connector.jar`,
   `--connection-manager com.altibase.sqoop.manager.AltibaseManager`,
   `sqoop import`, and `sqoop export`. The checked source path names BLOB/CLOB
   import only; do not claim symmetric LOB export behavior without source
   evidence.
6. Preserve third-party connector guide boundaries. Source-backed examples name
   DBeaver with Altibase Server 7.1.0 or later and DBeaver 23.3.3 or later in
   the trunk connector guide; OpenLDAP `back-sql` through ODBC; and Oracle
   GoldenGate Big Data JDBC Handler with
   `gg.handler.jdbcwriter.DriverClass=Altibase.jdbc.driver.AltibaseDriver`.
7. Do not add connector-specific TLS, pooling, transaction, or LOB behavior
   unless it appears in the selected source or customer-provided product
   documentation.

Safe first checks:

- Start DB Link only after checking properties, target definitions, driver
  files, and `ALTER DATABASE LINKER START` behavior in a non-production
  environment.
- Query `V$DBLINK_ALTILINKER_STATUS` and `V$DBLINK_DATABASE_LINK_INFO` before
  using `REMOTE_TABLE` or `REMOTE_EXECUTE_IMMEDIATE`.
- Run Sqoop and third-party connector commands against a test table before
  applying to production objects.

Stop conditions:

- Stop if remote DBMS version, JDBC driver, linker configuration, credentials,
  network route, NLS setting, or transaction expectation is unknown.
- Stop if a connector claim depends on a product version not named by the
  selected source or not supplied by the customer.
- Stop if remote execution could change data and no rollback or validation
  plan is provided.

## KAE-CLIENTTOOLS-BLOCK-007: Kubernetes, AKU, And Container Deployment

- Source IDs: `SRC-000008`, `SRC-000002`, `SRC-000009`, `SRC-000003`, with
  operation-tool context from `SRC-000222`, `SRC-000215`, `SRC-000208`,
  `SRC-000201`.
- Version scope: selected AKU and Kubernetes third-party guides, tool release
  sources, and Altibase 7.1, 7.3, and `Altibase 8.1 verified source`
  boundaries where AKU server counts are source-backed.
- Source block refs: `SRC-000008/BLOCK-000919`, `SRC-000002/BLOCK-000913`,
  `SRC-000009/BLOCK-000920`, `SRC-000003/BLOCK-000914`,
  `SRC-000222/BLOCK-000934`, `SRC-000215/BLOCK-000932`,
  `SRC-000208/BLOCK-000940`, `SRC-000201/BLOCK-000938`.
- Alignment status: baseline generated from selected Korean Kubernetes/AKU
  guides and AKU/Heartbeat tool sources. No Kubernetes cluster, image pull,
  storage class, service, or failover test was run.

Baseline:

1. Collect Altibase version, AKU version, Kubernetes version, container image,
   namespace, storage class, PVC size, service type, pod count, replication
   topology, resource limits, secrets policy, startup/shutdown hooks, backup
   plan, and recovery plan before generating YAML.
2. Preserve `aku` and `AKU_SERVER_COUNT` boundaries. The selected sources give
   7.1 count range 1 through 4 and 7.3/8.1 count range 1 through 6. Do not
   broaden those ranges to other versions without source evidence.
3. Preserve Kubernetes object and field tokens from the selected guides:
   `Pod`, `Deployment`, `StatefulSet`, `Service`, `ConfigMap`,
   `PersistentVolumeClaim`, `podManagementPolicy: OrderedReady`,
   `publishNotReadyAddresses: true`, `startupProbe`,
   `/tmp/aku_start_completed`, and `terminationGracePeriodSeconds`.
4. Preserve runtime order: start Altibase server first, then run
   `aku -p start`; run `aku -p end` before stopping the server; guard
   `aku -p clean` because it is a cleanup operation.
5. Preserve sample-mode tokens: `MODE=daemon`, `MODE=replication`,
   `SLAVE_REP_PORT=20301`, `REPLICATIONS`, and
   `AKU_REPLICATION_RESET_AT_END`.
6. Preserve sample-version boundaries. The selected Kubernetes guide uses
   Kubernetes `v1.20.4` with Docker Hub `altibase/altibase`; the selected AKU
   sample uses Kubernetes `v1.24.2` with `ubuntu:18.04`. These are source
   examples, not broad compatibility guarantees.

Safe first checks:

- Validate generated YAML with the customer's Kubernetes version and namespace
  before applying it.
- Confirm PVC binding and service DNS before starting Altibase.
- Capture pod logs and AKU output for `aku -p start`, `aku -p end`, and any
  replication reset action before documenting the deployment as ready.

Stop conditions:

- Stop if image source, secret handling, PVC/storage class, backup, recovery,
  or shutdown behavior is unspecified.
- Stop if a cloud-provider-specific load balancer, storage, security, or
  operator feature is requested but not present in the selected sources.
- Stop if `aku -p clean` or replication reset would be generated without an
  explicit cleanup and rollback plan.

## KAE-CLIENTTOOLS-BLOCK-008: Spatial, altiShapeLoader, NiFi, And Tableau

- Source IDs: `SRC-000074`, `SRC-000041`, `SRC-000135`, `SRC-000104`,
  `SRC-000195`, `SRC-000164`, `SRC-000226`, `SRC-000219`, `SRC-000212`,
  `SRC-000205`, `SRC-000470`, `SRC-000448`, `SRC-000010`, `SRC-000004`,
  `SRC-000014`, `SRC-000007`.
- Version scope: Spatial SQL Reference 7.1, 7.3, `Altibase 8.1 verified
  source`, altiShapeLoader trunk/release and 1.0 release note, selected NiFi
  and Tableau third-party guides.
- Source block refs: `SRC-000074/BLOCK-000872`, `SRC-000041/BLOCK-000871`,
  `SRC-000135/BLOCK-000874`, `SRC-000104/BLOCK-000873`,
  `SRC-000195/BLOCK-000876`, `SRC-000164/BLOCK-000875`,
  `SRC-000226/BLOCK-000878`, `SRC-000219/BLOCK-000877`,
  `SRC-000212/BLOCK-000880`, `SRC-000205/BLOCK-000879`,
  `SRC-000470/BLOCK-000882`, `SRC-000448/BLOCK-000881`,
  `SRC-000010/BLOCK-000921`, `SRC-000004/BLOCK-000915`,
  `SRC-000014/BLOCK-000925`, `SRC-000007/BLOCK-000918`.
- Alignment status: baseline generated from Korean Spatial, altiShapeLoader,
  NiFi, and Tableau sources. No live Spatial query, shape load, NiFi flow, or
  Tableau connection was run.

Baseline:

1. Collect Altibase version, SRID, GEOMETRY precision, source geometry format,
   table DDL, index need, shape file encoding, Java version, NiFi version,
   Tableau version, JDBC JAR path, and validation query before generating
   integration steps.
2. Preserve Spatial DDL tokens and limits: `GEOMETRY [(precision)] [(SRID
   srid)]`, precision minimum `16`, maximum `100MBytes`, default `32,000`,
   SRID as 4-byte signed value with default `0`, and
   `CREATE INDEX ... INDEXTYPE IS RTREE`.
3. Preserve Spatial metadata and function tokens: `SPATIAL_REF_SYS`,
   `SYS_SPATIAL.ADD_SPATIAL_REF_SYS`, WKT, WKB, EWKT, EWKB,
   `SRID=<srid>;WKT`, `ASEWKB`, and `GEOMFROMEWKB`.
4. Preserve altiShapeLoader setup and property tokens: `JAVA_HOME`,
   `altiShapeLoader.properties.release`, `altiShapeLoader.properties`,
   `CREATE_TABLE`, `TABLE_TBS`, `CREATE_INDEX`, `INDEX_TBS`, `DBF_CHAR`,
   `CASE_SENSITIVE`, and `GEO_COL_SIZE`. The selected source requires a
   64-bit OS Java Runtime Environment 8 or later; Java 17 untested and Java 18
   tested information must stay scoped to the exact compatibility evidence.
5. Preserve NiFi source boundaries: NiFi `1.12.1` or earlier when `CLOB` is
   involved, `$ALTIBASE_HOME/lib/Altibase42.jar`, `Controller Service`,
   `Database Connection URL`,
   `jdbc:Altibase://host_ip:port_no/database_name`,
   `Altibase.jdbc.driver.AltibaseDriver`, and `force_clob_bind=true`.
6. Preserve Tableau source boundaries:
   `TableauDesktop-64bit-2021-4-4`, `C:\Program Files\Tableau\Drivers`,
   `$ALTIBASE_HOME/lib/Altibase42.jar`, `Other Databases (JDBC)`, and
   `jdbc:Altibase://host_ip:port_no/database_name`.

Safe first checks:

- Verify SRID and geometry precision before creating tables or RTREE indexes.
- For altiShapeLoader, test with a small shape file and inspect generated table,
  geometry column, index, and load output before production import.
- For NiFi and Tableau, confirm the exact product version and JAR location, then
  test a read-only query before generating broader workflow steps.

Stop conditions:

- Stop if SRID, precision, source geometry encoding, DBF character set, table
  naming, or index tablespace is unknown.
- Stop if NiFi, Tableau, Java, JDBC JAR, or Altibase version differs from the
  selected source examples and no customer validation is provided.
- Stop if a BI or data-flow claim requires live product behavior not captured
  by the selected guide.

## KAE-CLIENTTOOLS-BLOCK-009: Shared Missing-Input And Validation Contract

- Source IDs: all S1-J009 source IDs listed in the Batch Source Coverage table
  and aggregate manifest row `KAE-BLOCK-000274`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, selected
  patch-level release notes, Migration Center 7.9 through 7.19,
  `dataCompJ 7.2`, and selected third-party guide source versions.
- Source block refs: use `KAE-BLOCK-000274` for the complete source-pack block
  list.
- Alignment status: cross-cutting guardrail generated for downstream answer,
  playbook, attachment, and upload-package work.

Baseline:

1. Ask for missing inputs before producing final commands or code when the
   answer depends on environment, runtime state, patch level, platform, object
   definition, logs, tool output, credentials, network topology, compiler,
   Java version, Kubernetes version, connector version, or third-party product
   behavior.
2. Preserve exact command, option, SQL, API, class, method, property, file, and
   expected-output tokens from source text. Do not rename tokens to a generic
   database equivalent.
3. Separate source-backed examples from production-ready steps. Customer-ready
   scripts must include validation checks, generated artifacts, cleanup files,
   rollback notes, and stop conditions.
4. Treat destructive or state-changing actions as protected operations:
   migration `run`, `filesync`, utility `SYNC`, `REPLACE`, `TRUNCATE`,
   `REMOTE_EXECUTE_IMMEDIATE`, `aku -p clean`, replication reset, schema load,
   import, export overwrite, and adapter start/replication start steps all
   require explicit scope and rollback evidence.
5. For third-party tools, use only selected-source and customer-provided
   compatibility evidence. Do not infer support from generic JDBC, ODBC,
   Hibernate, Kubernetes, NiFi, Tableau, Sqoop, OpenLDAP, or DBeaver behavior.

Safe first checks:

- Recheck the exact source-pack block and the target installed tool help before
  item-level production output.
- Run read-only or sample-scope validation before state-changing commands.
- Record output files and logs as artifacts: iSQL spool files, iLoader logs and
  bad files, `aexport` scripts, `dataCompJ_report.txt`, DB Link status views,
  Migration Center project reports, Kubernetes pod logs, and connector test
  outputs.

Stop conditions:

- Stop if source text names a token but does not give enough detail for a
  compile-ready, executable, or production-safe artifact.
- Stop if customer evidence conflicts with selected Korean authority.
- Stop if the requested answer would add an unsupported third-party
  compatibility claim.

## KAE-CLIENTTOOLS-BLOCK-010: Scoped Not-Ready Gaps

- Source IDs: `SRC-000052`, `SRC-000021`, `SRC-000176`, `SRC-000146`,
  `SRC-000198`, `SRC-000167`, `SRC-000199`, `SRC-000168`, `SRC-000223`,
  `SRC-000216`, `SRC-000209`, `SRC-000202`, `SRC-000221`, `SRC-000214`,
  `SRC-000207`, `SRC-000200`, `SRC-000008`, `SRC-000002`, `SRC-000009`,
  `SRC-000003`, `SRC-000010`, `SRC-000004`, `SRC-000014`, `SRC-000007`,
  plus aggregate row `KAE-BLOCK-000274`.
- Version scope: 7.1, 7.3, `Altibase 8.1 verified source`, selected
  Migration Center release notes, selected third-party guide source versions,
  and `dataCompJ 7.2`.
- Source block refs: `KAE-BLOCK-000274`; gap evidence is also registered in
  `GPTs/reports/source_conflict_register.md` as `CONF-000006`.
- Alignment status: scoped recheck and limitation record. These gaps do not
  block the S1-J009 baseline, but they block exhaustive downstream claims.

Baseline gaps:

1. This batch does not exhaustively normalize every API signature, option
   table, property row, SQL grammar detail, release-note change, connector GUI
   step, Spatial function, Kubernetes YAML field, or utility output.
2. `SQLEmptyLob()` and `SQLGetLobLength2()` are named in selected 8.1 context,
   but complete callable signatures were not established by this baseline.
   Recheck installed headers or exact source blocks before generating code.
3. iLoader `-dry-run` appears in syntax/help in selected sources, but checked
   baseline sources do not establish full production semantics.
4. Migration Center 7.7 and 7.8 English-only release-note manifest rows remain
   excluded until Korean authority or approved auxiliary use is recorded.
5. Cloud-provider-specific Kubernetes storage, network, secret, load-balancer,
   and operator runbooks are outside the selected sources.
6. Live third-party compatibility for Spring/Hibernate, NiFi, Tableau,
   DBeaver, OpenLDAP, Oracle GoldenGate, Hadoop/Sqoop, and Kubernetes was not
   tested in this job.

Safe first checks:

- Use this baseline to route to the correct source group and preserve exact
  tokens; use exact source-pack blocks or installed artifacts for exhaustive
  item-level answers.
- Before upload-package or playbook work claims coverage, itemize the remaining
  source rows needed for the specific tool, API, connector, or migration path.

Stop conditions:

- Stop if downstream content would state that the attachment set contains every
  option, every API signature, or every third-party compatibility case for this
  batch.
- Stop if a customer asks for a production command or code artifact that
  depends on one of the unresolved gaps above and cannot provide target
  version, installed output, or source evidence.

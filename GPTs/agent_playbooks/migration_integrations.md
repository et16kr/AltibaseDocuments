# Migration And Integrations Playbook

- Playbook ID: `APB-000012`
- Owning job: `S2-J007`
- Status: `pass`
- Version scope: Altibase `7.1`, `7.3`, `8.1_verified`, selected tool releases, third-party guides, and guarded AID routes
- Protected topic: yes

## Source Routes

Use this playbook to draft guarded workflows for Migration Center, Adapter for Oracle, DB Link, Hadoop, Kubernetes/AKU, Spatial, altiShapeLoader, NiFi, Tableau, and classified AID integration routes. Third-party routes are compatibility-sensitive: preserve exact product versions from source and require installed-tool or customer-environment evidence before final commands.

Primary source routes:

| Route | Source IDs | Source-pack blocks | KAE blocks |
| --- | --- | --- | --- |
| Adapter for Oracle | `SRC-000017`;`SRC-000048`;`SRC-000081`;`SRC-000112`;`SRC-000142`;`SRC-000172` | `SRC-000017/BLOCK-000569`;`SRC-000048/BLOCK-000570`;`SRC-000081/BLOCK-000571`;`SRC-000112/BLOCK-000572`;`SRC-000142/BLOCK-000573`;`SRC-000172/BLOCK-000574` | `KAE-BLOCK-000019`;`KAE-BLOCK-000154`;`KAE-BLOCK-000210` |
| Migration Center manuals and release notes | `SRC-000216`;`SRC-000223`;`SRC-000202`;`SRC-000209`;`SRC-000430`;`SRC-000453`;`SRC-000431`;`SRC-000454`;`SRC-000432`;`SRC-000455`;`SRC-000433`;`SRC-000456`;`SRC-000434`;`SRC-000457`;`SRC-000435`;`SRC-000458`;`SRC-000436`;`SRC-000459`;`SRC-000437`;`SRC-000460`;`SRC-000438`;`SRC-000461`;`SRC-000439`;`SRC-000462`;`SRC-000440`;`SRC-000441`;`SRC-000442`;`SRC-000463`;`AID-SRC-000356` | `SRC-000216/BLOCK-000575`;`SRC-000223/BLOCK-000576`;`SRC-000202/BLOCK-000601`;`SRC-000209/BLOCK-000602`;`SRC-000430/BLOCK-000577`;`SRC-000453/BLOCK-000578`;`SRC-000431/BLOCK-000579`;`SRC-000454/BLOCK-000580`;`SRC-000432/BLOCK-000581`;`SRC-000455/BLOCK-000582`;`SRC-000433/BLOCK-000583`;`SRC-000456/BLOCK-000584`;`SRC-000434/BLOCK-000585`;`SRC-000457/BLOCK-000586`;`SRC-000435/BLOCK-000587`;`SRC-000458/BLOCK-000588`;`SRC-000436/BLOCK-000589`;`SRC-000459/BLOCK-000590`;`SRC-000437/BLOCK-000591`;`SRC-000460/BLOCK-000592`;`SRC-000438/BLOCK-000593`;`SRC-000461/BLOCK-000594`;`SRC-000439/BLOCK-000595`;`SRC-000462/BLOCK-000596`;`SRC-000440/BLOCK-000597`;`SRC-000441/BLOCK-000598`;`SRC-000442/BLOCK-000599`;`SRC-000463/BLOCK-000600`;`AID-SRC-000356/BLOCK-000423` | `KAE-BLOCK-000211`;`KAE-BLOCK-000232`;`KAE-BLOCK-000254`;`KAE-BLOCK-000255`;`KAE-BLOCK-000256`;`KAE-BLOCK-000257`;`KAE-BLOCK-000258`;`KAE-BLOCK-000259`;`KAE-BLOCK-000260`;`KAE-BLOCK-000261`;`KAE-BLOCK-000262`;`KAE-BLOCK-000263`;`KAE-BLOCK-000266`;`KAE-BLOCK-000276` |
| DB Link and Hadoop | `SRC-000022`;`SRC-000053`;`SRC-000086`;`SRC-000117`;`SRC-000147`;`SRC-000177`;`SRC-000028`;`SRC-000059`;`SRC-000092`;`SRC-000123`;`SRC-000153`;`SRC-000183`;`SRC-000214`;`SRC-000221`;`SRC-000200`;`SRC-000207` | `SRC-000022/BLOCK-000492`;`SRC-000053/BLOCK-000494`;`SRC-000086/BLOCK-000496`;`SRC-000117/BLOCK-000498`;`SRC-000147/BLOCK-000500`;`SRC-000177/BLOCK-000502`;`SRC-000028/BLOCK-000493`;`SRC-000059/BLOCK-000495`;`SRC-000092/BLOCK-000497`;`SRC-000123/BLOCK-000499`;`SRC-000153/BLOCK-000501`;`SRC-000183/BLOCK-000503`;`SRC-000214/BLOCK-000504`;`SRC-000221/BLOCK-000505`;`SRC-000200/BLOCK-000506`;`SRC-000207/BLOCK-000507` | `KAE-BLOCK-000007`;`KAE-BLOCK-000008`;`KAE-BLOCK-000142`;`KAE-BLOCK-000143`;`KAE-BLOCK-000197`;`KAE-BLOCK-000198`;`KAE-BLOCK-000230` |
| Spatial and altiShapeLoader | `SRC-000041`;`SRC-000074`;`SRC-000104`;`SRC-000135`;`SRC-000164`;`SRC-000195`;`SRC-000219`;`SRC-000226`;`SRC-000205`;`SRC-000212`;`SRC-000448`;`SRC-000470` | `SRC-000041/BLOCK-000871`;`SRC-000074/BLOCK-000872`;`SRC-000104/BLOCK-000873`;`SRC-000135/BLOCK-000874`;`SRC-000164/BLOCK-000875`;`SRC-000195/BLOCK-000876`;`SRC-000219/BLOCK-000877`;`SRC-000226/BLOCK-000878`;`SRC-000205/BLOCK-000879`;`SRC-000212/BLOCK-000880`;`SRC-000448/BLOCK-000881`;`SRC-000470/BLOCK-000882` | `KAE-BLOCK-000034`;`KAE-BLOCK-000165`;`KAE-BLOCK-000221`;`KAE-BLOCK-000222`;`KAE-BLOCK-000238`;`KAE-BLOCK-000239` |
| Kubernetes/AKU, NiFi, Tableau | `SRC-000002`;`SRC-000008`;`SRC-000003`;`SRC-000009`;`SRC-000004`;`SRC-000010`;`SRC-000007`;`SRC-000014` | `SRC-000002/BLOCK-000913`;`SRC-000008/BLOCK-000919`;`SRC-000003/BLOCK-000914`;`SRC-000009/BLOCK-000920`;`SRC-000004/BLOCK-000915`;`SRC-000010/BLOCK-000921`;`SRC-000007/BLOCK-000918`;`SRC-000014/BLOCK-000925` | `KAE-BLOCK-000244`;`KAE-BLOCK-000245`;`KAE-BLOCK-000246`;`KAE-BLOCK-000249` |

Cross-route baselines: `KAE-BLOCK-000274` for client/tool/integration alignment, `KAE-BLOCK-000275` for release-note/platform rechecks, and `KAE-BLOCK-000276` for AID `primary_working_source` reuse when AID content is used.

Guardrail routes: `CONF-000004` for protected administrative side effects, `CONF-000006` for client/tool exact-option recheck, `CONF-000007` for AID reuse limits, and `CONF-000009` for third-party compatibility evidence.

## Required Customer Inputs

Collect these inputs before generating runnable migration or integration artifacts:

- Target Altibase version and patch level, source product and version, destination product and version, platform, Java/JRE/JDK version, and tool release.
- Network details, hostnames, ports, user names, credential policy, schema/object scope, data volume, maintenance window, and rollback or cutover plan.
- Source and target character sets, time zone behavior, data type mapping requirements, LOB/spatial handling requirements, and unsupported-object tolerance.
- For Migration Center: source DB product, target Altibase version, JDBC drivers, project path, `register.xml`, `options.xml`, `TableCondition.properties`, Build/Reconcile/Run output directories, and whether Data Validation can require primary keys.
- For Adapter for Oracle: `$ORA_ADAPTER_HOME`, Oracle client/OCI version, `NLS_LANG`, library path, `oraAdapter.conf`, replication name, ALA sender/receiver ports, target tables, constraints, and offline SQL requirement.
- For DB Link: `$ALTIBASE_HOME/conf/dblink.conf`, `DBLINK_ENABLE`, `ALTILINKER_ENABLE`, `ALTILINKER_PORT_NO`, `TARGETS`, remote JDBC driver, remote SQL, and transaction boundary.
- For Hadoop: Hadoop and Sqoop versions, `$SQOOP_HOME`, `$ALTIBASE_HOME/lib/Altibase.jar`, `altibase_sqoop14_connector.jar`, import/export direction, staging table, and LOB requirements.
- For Kubernetes/AKU: Kubernetes version, image name, StatefulSet name, service name, replica count, storage class or volume plan, `aku.conf`, `ADMIN_MODE`, `REMOTE_SYSDBA_ENABLE`, and termination/startup probe policy.
- For Spatial/altiShapeLoader: SRID, `SPATIAL_REF_SYS` status, shapefile path, `.shp`, `.shx`, `.dbf`, `.prj`, table name, `GEOMETRY` column, `SRID`, and import/export direction.
- For NiFi and Tableau: exact tool version, JDBC driver jar, JDBC URL, driver class, CLOB requirement, `force_clob_bind=true` need, Tableau driver directory, and `TIMESTAMP_TO_DATE` decision.

If any compatibility item is unknown, generate a checklist and first checks, not a final migration script.

## Generated Artifacts

Allowed artifacts are guarded first drafts of command sequences, configuration fragments, SQL, JDBC URLs, YAML snippets, validation checklists, compatibility matrices, and cutover runbooks. Mark third-party examples as source-version specific.

### Migration Center route

```bash
./migcenter.sh register register.xml
./migcenter.sh build ./projects/project_001
./migcenter.sh reconcile ./projects/project_001
./migcenter.sh run ./projects/project_001
./migcenter.sh diff ./projects/project_001
./migcenter.sh filesync ./projects/project_001
```

Preserve these output names in generated checklists: `SrcDbObj_Create.sql`, `BuildReport4Unsupported.html`, `DbObj_Create.sql`, `DbObj_Drop.sql`, `sqlconv.html`, `sqlconv_src.sql`, `sqlconv_dest.sql`, `RunReport4Summary.html`, `RunReport4Missing.html`, `DbObj_Failed.sql`, `db2db`, `db2file`, `iLoaderIn.sh`, and `iLoaderIn.number.sh`.

Use the source process order `Prepare`, `Build`, `Reconcile`, `Run`, and `Data Validation`. For Data Validation, require primary keys and warn that LOB columns are excluded by the source route. If `TableCondition.properties` includes a `[DEST]` section, preserve that source/target SQL distinction.

### Adapter for Oracle route

```sql
CREATE REPLICATION ala FOR ANALYSIS WITH '127.0.0.1', 25090
                                            FROM sys.t1 TO scott.t2;
ALTER REPLICATION ala START;
ALTER REPLICATION ala STOP;
```

```bash
export ORA_ADAPTER_HOME=/opt/oraAdapter
export NLS_LANG=AMERICAN_AMERICA.UTF8
cd "$ORA_ADAPTER_HOME/bin"
./oraAdapter
oaUtility status
oaUtility check constraints
```

`oraAdapter.conf` drafts may include exact source property names such as `ALA_SENDER_IP`, `ALA_SENDER_REPLICATION_PORT`, `ALA_RECEIVER_PORT`, `ALA_REPLICATION_NAME`, `ALA_SOCKET_TYPE`, `ALTIBASE_USER`, `ALTIBASE_PASSWORD`, `ALTIBASE_IP`, `ALTIBASE_PORT`, `ORACLE_SERVER_ALIAS`, `ORACLE_USER`, `ORACLE_PASSWORD`, `ORACLE_GROUP_COMMIT`, `ORACLE_ARRAY_DML_MAX_SIZE`, `ORACLE_SKIP_ERROR`, `ORACLE_SKIP_INSERT`, `ORACLE_SKIP_UPDATE`, `ORACLE_SKIP_DELETE`, and `ADAPTER_LOB_TYPE_SUPPORT`.

For offline SQL, preserve source command forms: `ALTER REPLICATION ala_replication_name SET OFFLINE ENABLE WITH 'log_dir'`, `BUILD OFFLINE META`, `RESET OFFLINE META`, and `START WITH OFFLINE`.

### DB Link route

```sql
ALTER DATABASE LINKER START;
CREATE DATABASE LINK link1 CONNECT TO remote_user IDENTIFIED BY remote_password USING 'target1';
SELECT * FROM REMOTE_TABLE(link1, 'select * from t1');
SELECT REMOTE_EXECUTE_IMMEDIATE('link1', 'insert into t1 values(1)') FROM DUAL;
ALTER SESSION LINKER DUMP;
ALTER DATABASE LINKER STOP;
```

For bind workflows, preserve `REMOTE_ALLOC_STATEMENT`, `REMOTE_BIND_VARIABLE`, `REMOTE_EXECUTE_STATEMENT`, `REMOTE_NEXT_ROW`, `REMOTE_GET_COLUMN_VALUE_type`, and `REMOTE_FREE_STATEMENT`. Validate with `V$DBLINK_LINKER_SESSION_INFO`, `V$DBLINK_LINKER_CONTROL_SESSION_INFO`, `V$DBLINK_LINKER_DATA_SESSION_INFO`, `V$DBLINK_REMOTE_TRANSACTION_INFO`, `V$DBLINK_REMOTE_STATEMENT_INFO`, and `V$DBLINK_ALTILINKER_STATUS`.

### Hadoop route

```bash
cp "$ALTIBASE_HOME/lib/Altibase.jar" "$SQOOP_HOME/lib/"
cp ./altibase_sqoop14_connector.jar "$SQOOP_HOME/lib/"

sqoop list-tables \
  --connect jdbc:Altibase://127.0.0.1:20300/mydb \
  --connection-manager com.altibase.sqoop.manager.AltibaseManager
```

Preserve `Altibase.jdbc.driver.AltibaseDriver`, `com.altibase.sqoop.manager.AltibaseManager`, and the source command categories `import`, `export`, `list-databases`, and `list-tables`. For `MERGE` upsert or batch export, require the exact target Altibase/Sqoop route and staging-table evidence.

### Kubernetes and AKU route

```bash
kubectl create -f altibase-pv.yaml
kubectl create -f altibase-cm.yaml
kubectl create -f altibase-svc.yaml
kubectl create -f altibase-sts.yaml
kubectl get Pod,Service -o wide
kubectl exec -it altibase-sts-0 -- /bin/bash
aku -p start
aku -p end
```

AKU drafts must preserve `StatefulSet`, `OrderedReady`, `publishNotReadyAddress=true`, `/tmp/aku_start_completed`, `ALTIBASE_HOME`, `ADMIN_MODE=1`, `REMOTE_SYSDBA_ENABLE=1`, `AKU_STS_NAME`, `AKU_SVC_NAME`, `AKU_SERVER_COUNT`, `AKU_SYS_PASSWORD`, `AKU_PORT_NO`, `AKU_REPLICATION_PORT_NO`, `REPLICATIONS`, `REPLICATION_NAME_PREFIX`, and `SYNC_PARALLEL_COUNT`. The source has tension between option text for `stop` and examples using `aku -p end`; require installed `aku --help` before finalizing that action.

### Spatial and altiShapeLoader route

```sql
CREATE TABLE building (id INTEGER, obj GEOMETRY);
INSERT INTO building VALUES (1, GEOMETRY'POINT(10 10)');
SELECT SRID, AUTH_NAME, AUTH_SRID FROM SPATIAL_REF_SYS WHERE AUTH_SRID = '7846';
```

```bash
cp -p altiShapeLoader.properties.release altiShapeLoader.properties
./altiShapeLoader.sh -o import -f data/subway_station.shp -t SUBWAY_STATION
./altiShapeLoader.sh -o export -t POLICESTATION -f ./policestation2.shp
```

Preserve `GEOMETRY`, `WKT`, `WKB`, `EWKT`, `EWKB`, `SRID`, `SPATIAL_REF_SYS`, `SYS_SPATIAL.ADD_SPATIAL_REF_SYS`, `OPERATION`, `SHAPE_FILE`, `TABLE_NAME`, `CREATE_TABLE`, `CREATE_INDEX`, `DBF_CHAR`, `ENDIAN`, `CASE_SENSITIVE`, `CREATE_BAD`, `PARALLEL`, `COMMIT`, `ATOMIC_BATCH`, and `SRID` options. Stop if the `.prj` file is missing or if `SRID` cannot be reconciled to source/customer evidence.

### NiFi and Tableau route

```properties
nifi.web.http.host=
nifi.web.http.port=8000
```

```bash
nifi.sh start
nifi.sh status
nifi.sh stop
```

```text
Database Connection URL: jdbc:Altibase://host_ip:port_no/database_name
Database Connection URL for CLOB: jdbc:Altibase://host_ip:port_no/database_name?force_clob_bind=true
Database Driver Class Name: Altibase.jdbc.driver.AltibaseDriver
```

For Tableau, preserve `TIMESTAMP_TO_DATE = 1`, `mysql_date_function.sql`, `C:\Program Files\Tableau\Drivers`, `Altibase42.jar`, `Altibase.jar`, and `jdbc:Altibase://host_ip:port_no/database_name`. Treat the documented TableauDesktop-64bit-2021-4-4 route as a tested source route, not a guarantee for all Tableau versions.

## Guardrails

- Migration Center `Run` is irreversible in practice without a rollback plan. Require backup, project output review, and cutover approval before final run commands.
- Do not claim universal source-database support from Migration Center without checking the exact manual or release-note route for that tool release.
- Adapter for Oracle depends on Altibase ALA, Oracle OCI, replication object rules, and target-table constraints. Require primary keys, table mapping, `FOR ANALYSIS`, and OCI/library-path evidence.
- DB Link depends on server properties, AltiLinker configuration, remote JDBC driver support, and runtime transaction state. Prefer `REMOTE_TABLE` pass-through when source guidance recommends it and avoid unsupported remote DDL claims.
- Hadoop/Sqoop examples are tied to source versions such as Apache Sqoop 1.4.4 and Hadoop 1.0 routes. Require installed-tool evidence before adapting to newer clusters.
- Kubernetes examples are guide-version specific. AKU supports data synchronization among Pods, not Altibase data scale-out.
- Spatial and altiShapeLoader outputs depend on SRID, shapefile components, GeoTools constraints, geometry limitations, and supported data type conversions.
- NiFi and Tableau routes are third-party tested routes. Require exact NiFi/Tableau/JDBC driver versions, and preserve CLOB/JDBC limitations.
- AID-derived integration content may be used as `primary_working_source` only within the recorded AID classification and source-limitation route.

## Validation Checks

Run validation in layers:

1. Migration Center: verify JDBC drivers, `register.xml`, generated `options.xml`, Build reports, `BuildReport4Unsupported.html`, Reconcile reports, `DbObj_Create.sql`, `DbObj_Drop.sql`, `sqlconv.html`, Run reports, `RunReport4Summary.html`, `RunReport4Missing.html`, failed-data directories, and Data Validation reports.
2. Adapter for Oracle: verify `oraAdapter.trc` contains startup readiness, `oaUtility status`, `oaUtility check constraints`, source/target table constraints, ALA ports, Oracle connection, and `ALTER REPLICATION` state.
3. DB Link: verify `ALTER DATABASE LINKER START`, remote driver loading, `V$DBLINK_ALTILINKER_STATUS`, remote statement views, dump file `$ALTIBASE_HOME/trc/altibase_lk_dump.log`, and transaction cleanup.
4. Hadoop: verify `$SQOOP_HOME/lib/Altibase.jar`, `altibase_sqoop14_connector.jar`, `sqoop list-tables`, row counts after import/export, staging-table cleanup, and LOB restrictions.
5. Kubernetes/AKU: verify `kubectl get Pod -o wide`, `kubectl get Pod,Service -o wide`, StatefulSet replica state, headless service DNS, AKU expected output tokens such as `AKU started with START option.`, `Replication sync has ended.`, `AKU run successfully.`, and `AKU started with END option.`
6. Spatial/altiShapeLoader: verify `SPATIAL_REF_SYS`, `SYS_SPATIAL.ADD_SPATIAL_REF_SYS`, shapefile component presence, `.bad` files when `CREATE_BAD=T`, row counts, spatial indexes, and SRID consistency.
7. NiFi: verify `nifi.sh status`, UI reachability, JDBC controller service, driver path, CLOB URL when needed, and processor error queues.
8. Tableau: verify `TIMESTAMP_TO_DATE = 1` restart, `mysql_date_function.sql` execution through iSQL, driver jar placement, connection URL, and workbook query results.

## Stop Conditions

Stop and ask for evidence when:

- Tool version, third-party version, JDBC driver, JRE/JDK, or platform support is unknown.
- A Migration Center Build or Reconcile report lists unsupported objects, failed SQL conversion, data type risks, or missing drivers.
- Migration Center `Run`, DB Link remote DDL/DML, Adapter for Oracle synchronization, Hadoop export, AKU scaling, or altiShapeLoader import would change production state without approval and rollback evidence.
- Adapter for Oracle source/target tables lack required primary keys or the table/column order and constraint assumptions are not confirmed.
- DB Link properties or `dblink.conf` do not match the remote target, or active remote transactions remain.
- Hadoop/Sqoop versions differ from source routes and no live compatibility test has passed.
- AKU source examples conflict with installed `aku --help`, or StatefulSet, Pod management, service DNS, storage, startup probe, or termination settings are missing.
- Spatial SRID is missing, `.prj` cannot be parsed, `SPATIAL_REF_SYS` is not populated, or shapefile constraints are violated.
- NiFi or Tableau versions fall outside the source-tested range and no compatibility evidence exists.

## Cleanup And Rollback

Preserve cleanup as a project-specific runbook. Migration Center cleanup can include archiving project directories, reports, generated SQL, failed-data folders, and Data Validation CSV output. Adapter for Oracle cleanup can include stopping replication with `ALTER REPLICATION ... STOP`, stopping `oraAdapter`, and preserving `oraAdapter.trc`. DB Link cleanup can include `ALTER DATABASE LINKER STOP`, freeing remote statements, and preserving linker dumps. Hadoop cleanup can include staging-table cleanup and HDFS path review. Kubernetes/AKU cleanup must use the customer's StatefulSet and storage policy. altiShapeLoader cleanup must preserve generated shapefiles, `.bad` files, logs, and SRID registration evidence.

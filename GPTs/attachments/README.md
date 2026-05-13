# Altibase GPTs Attachments

이 디렉터리는 GPTs에 업로드할 고객용 Markdown 지식 파일을 담는다.

## 원칙

- 첨부 파일은 20개로 제한한다.
- 각 파일은 7.1, 7.3, 8.1 기준 답변을 지원한다.
- 8.1 문서는 내부 검증본을 기반으로 하지만, 고객용 첨부 문서에는 내부 원천명을 노출하지 않는다.
- Oracle과 겹치는 일반 SQL은 축약하고, Altibase DDL/설정/운영 차이점을 우선한다.
- 표와 이미지는 GPT 검색에 적합한 설명형 Markdown으로 바꾼다.

## 파일 목록

1. `00_version_release_platform.md`
2. `01_getting_started_installation.md`
3. `02_administration_operations.md`
4. `03_sql_ddl_generation.md`
5. `04_sql_dml_oracle_compatibility.md`
6. `05_data_types_properties.md`
7. `06_data_dictionary_performance_views.md`
8. `07_error_messages_troubleshooting.md`
9. `08_performance_tuning_monitoring.md`
10. `09_replication_ha_cdc.md`
11. `10_psm_stored_external_procedures.md`
12. `11_java_jdbc_spring.md`
13. `12_c_cli_odbc_precompiler.md`
14. `13_isql_iloader_basic_tools.md`
15. `14_utilities_operation_tools.md`
16. `15_migration_oracle_compatibility.md`
17. `16_dblink_external_connectors.md`
18. `17_kubernetes_aku_cloud.md`
19. `18_security_ssl_tls.md`
20. `19_spatial_nifi_tableau_misc.md`

## 업로드 전 검수

- `README.md`를 제외한 Markdown 파일이 정확히 20개인지 확인한다.
- 각 파일에 `적용 버전`, `원천 문서`, `이 문서로 답할 수 있는 질문`, `변환 TODO`가 있는지 확인한다.
- 고객에게 노출하지 않을 내부 원천명이 남아 있지 않은지 확인한다.

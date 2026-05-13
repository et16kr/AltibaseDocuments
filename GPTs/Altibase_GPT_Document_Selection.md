# Altibase GPTs 지식 문서 선정안

## 목표

고객이 GPTs에서 Altibase에 대해 질문할 때, 사용 중인 버전이 7.1, 7.3, 8.1 중 무엇인지에 따라 답변 기준을 달리 잡을 수 있도록 첨부용 지식 문서를 구성한다.

특히 고객 질문은 SQL 생성, DDL 작성, 서버 설정, 운영 확인 SQL, 이중화, 오류 대응에 집중될 가능성이 높다. 따라서 Oracle과 겹치는 일반 SQL 설명은 줄이고, Altibase 고유 DDL/설정/운영 차이점을 두껍게 만든다.

## 버전 정책

| 고객 버전 | 기본 원천 | 사용 방식 |
| --- | --- | --- |
| 7.1 | `Manuals/Altibase_7.1` | 7.1 고객 질문의 기준 문서로 사용한다. |
| 7.3 | `Manuals/Altibase_7.3` | 7.3 고객 질문의 기준 문서로 사용한다. |
| 8.1 | `Manuals/Altibase_trunk` + `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md` | `trunk`는 내부 원천명으로만 사용하고, 고객용 첨부 문서에는 "8.1 검증본"으로 표기한다. |

주의:

- 첨부용 결과물에는 `trunk`라는 표현을 남기지 않는다.
- 8.1 원천은 8.1 릴리스 노트와 대조하여 JSON, Temporary LOB, replication SSL, JSON plan, 신규 프로퍼티/성능 뷰 등이 반영되어 있는지 확인한다.
- `7.8`은 현재 로컬 제품 매뉴얼 세트 기준 버전이 아니므로 기본 대상에서 제외한다. 단, Migration Center 등 도구 릴리스 노트에서는 해당 버전이 나오면 보조 정보로 다룬다.

## 선정 기준

1. 고객 질문 빈도가 높은 핵심 영역
2. ChatGPT가 일반 DB 지식으로 잘못 추론하기 쉬운 Altibase 고유 정보
3. 7.1, 7.3, 8.1 버전별 차이
4. 운영 장애 대응과 실제 현장 문제 해결에 필요한 문서
5. GPTs 지식 검색에 맞게 Markdown 정리가 가능한 문서

## 최종 권장: 첨부용 20개 문서

아래 20개가 GPTs에 올릴 최종 파일 단위이다. 원본 문서를 그대로 올리지 않고, 질문 주제별로 결합한다.

| 번호 | 첨부 파일 | 고객 질문 범위 | 주요 원천 |
| --- | --- | --- | --- |
| 00 | `00_version_release_platform.md` | 7.1/7.3/8.1 릴리스, 지원 플랫폼, 업그레이드 주의사항 | Release Notes, Supported Platforms |
| 01 | `01_getting_started_installation.md` | 설치, DB 생성, 기동/종료, 기본 환경 | Getting Started, Installation |
| 02 | `02_administration_operations.md` | 운영 관리, 계정, 백업/복구, 테이블스페이스 | Administrator's Manual |
| 03 | `03_sql_ddl_generation.md` | GPT SQL 생성용 DDL/DCL/설정 SQL | SQL Reference, General Reference |
| 04 | `04_sql_dml_oracle_compatibility.md` | Oracle 호환 SQL, DML, 함수 차이 | SQL Reference |
| 05 | `05_data_types_properties.md` | 데이터 타입, 프로퍼티, JSON, Temporary LOB | General Reference 1 |
| 06 | `06_data_dictionary_performance_views.md` | 메타 테이블, 성능 뷰, 확인 SQL | General Reference 2 |
| 07 | `07_error_messages_troubleshooting.md` | 오류 코드, 원인, 조치, 확인 명령 | Error Message Reference |
| 08 | `08_performance_tuning_monitoring.md` | 실행 계획, 인덱스, 조인, 모니터링 | Performance Tuning, Monitoring API, SNMP |
| 09 | `09_replication_ha_cdc.md` | 이중화, HA, XLog/Log Analyzer, 호환성 | Replication, Log Analyzer, ReplicationCompatibility |
| 10 | `10_psm_stored_external_procedures.md` | PSM, 함수/프로시저, 외부 프로시저 | Stored Procedures, External Procedures |
| 11 | `11_java_jdbc_spring.md` | JDBC, Java 호환성, Spring/Hibernate | JDBC, Adapter for JDBC, JavaCompatibility, Spring guides |
| 12 | `12_c_cli_odbc_precompiler.md` | CLI, ODBC, C Interface, Precompiler | CLI, ODBC, C Interface, Precompiler |
| 13 | `13_isql_iloader_basic_tools.md` | iSQL, iLoader, 데이터 적재/추출 | iSQL, iLoader |
| 14 | `14_utilities_operation_tools.md` | aexport, altiComp, aku, altiMon, dataCompJ | Utilities, dataCompJ |
| 15 | `15_migration_oracle_compatibility.md` | Migration Center, Oracle Adapter, 전환 가이드 | Migration Center, Adapter for Oracle |
| 16 | `16_dblink_external_connectors.md` | DB Link, Hadoop, DBeaver, GoldenGate 등 | DB Link, Hadoop, 3rd Party Connector |
| 17 | `17_kubernetes_aku_cloud.md` | Kubernetes, AKU, 컨테이너 운영 | Kubernetes guides, AKU sample, 7.3 release AKU notes |
| 18 | `18_security_ssl_tls.md` | SSL/TLS, 인증서, 암호화 접속 | SSL/TLS User's Guide |
| 19 | `19_spatial_nifi_tableau_misc.md` | Spatial SQL, altiShapeLoader, NiFi, Tableau | Spatial SQL, altiShapeLoader, NiFi, Tableau |

## SQL 생성용 압축 전략

`03_sql_ddl_generation.md`는 고객 질문의 중심 문서다. 전체 SQL Reference를 단순 축약하지 않고, 다음 원칙으로 재작성한다.

| 구분 | 처리 방식 |
| --- | --- |
| `SELECT`, `INSERT`, `UPDATE`, `DELETE`, 기본 `JOIN`, 기본 조건식 | Oracle 호환 영역으로 간주하고 핵심 차이 또는 제한만 남긴다. 상세 문법은 "Oracle SQL과 유사"라고 표시한다. |
| `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, 제약 조건, 파티션, LOB, QUEUE | Altibase DDL 차이점이 중요하므로 상세 유지한다. 예제 SQL을 반드시 포함한다. |
| `CREATE INDEX`, 인덱스 속성, 힌트, 실행 계획 관련 SQL | 튜닝 질문과 연결되므로 상세 유지한다. |
| `CREATE/ALTER/DROP TABLESPACE`, 데이터파일, 메모리/디스크 저장 구조 | Altibase 운영 DDL의 핵심이므로 상세 유지한다. |
| `CREATE USER`, 권한, role, synonym, view, sequence | Oracle과 유사한 부분은 요약하고 Altibase 문법 차이와 예제를 우선한다. |
| Replication 관련 SQL | Altibase 고유 영역이므로 `09_replication_ha_cdc.md`와 교차 참조한다. |
| 프로퍼티/시스템 설정 관련 SQL | 대표 조회/변경 SQL을 정리하고 `05`, `06` 문서와 교차 참조한다. |
| 내장 함수, 분석 함수, 일반 표현식 | Oracle과 동일/유사한 설명은 축약하고 Altibase 특이 함수, 제한, 데이터 타입 차이만 남긴다. |

각 DDL 항목은 아래 형식으로 통일한다.

```text
질문 예시:
- 메모리 테이블을 생성하는 DDL을 만들어줘.

적용 버전:
- 공통:
- 7.1:
- 7.3:
- 8.1:

Oracle 호환성:
- Oracle과 유사한 부분:
- Altibase에서 다른 부분:

Altibase 문법 핵심:
- 필수 절:
- 선택 절:
- 주의할 제약:

예제:
- 최소 예제
- 운영 환경 예제
- 확인 SQL
```

## 변환 우선순위

1. `03_sql_ddl_generation.md`
2. `05_data_types_properties.md`
3. `06_data_dictionary_performance_views.md`
4. `02_administration_operations.md`
5. `09_replication_ha_cdc.md`
6. `08_performance_tuning_monitoring.md`
7. `07_error_messages_troubleshooting.md`
8. `01_getting_started_installation.md`

## 권장 작업 방식

- 원본 문서는 보존하고, GPT 업로드용 Markdown을 `GPTs/attachments/`에 생성한다.
- 첨부용 문서에는 `trunk`라는 표현을 남기지 않는다.
- 8.1 문서는 내부적으로 8.1 검증본 원천을 사용하되, 고객용 표기는 "8.1 검증본"으로 한다.
- 이미지 기반 구문도는 가능한 한 Mermaid flowchart 또는 텍스트 BNF로 바꾼다.
- 큰 표는 Markdown 표 그대로 두지 말고 항목 단위로 분해한다.
- 각 문서 앞부분에 "이 문서로 답할 수 있는 질문" 섹션을 둔다.

# Altibase GPTs 첨부 문서 구축 작업 문서

## 목적

GPTs에 업로드할 20개 Markdown 문서를 만들기 위한 작업 기준서다. 최종 산출물은 고객이 7.1, 7.3, 8.1 중 어떤 버전을 사용하더라도 자기 버전 기준으로 SQL, DDL, 설정, 운영, 이중화, 오류 대응 답변을 받을 수 있게 하는 것이다.

## 실행 관리

긴 작업은 job 단위로 나누어 진행한다.

- Job list: `GPTs/Altibase_GPT_Attachment_Job_List.md`
- Runner script: `GPTs/scripts/attachment_jobs.sh`

각 job은 `ToDo`, `InProgress`, `Review`, `Done`, `Fail`, `Blocked`, `Skip` 중 하나의 상태를 가진다. 각 단계는 Codex CLI에 job prompt를 전달하여 독립적으로 실행할 수 있게 구성한다.

커밋/복구 규칙:

- 각 job은 시작 시점과 종료 시점에 Git commit을 남긴다.
- 시작은 `bash GPTs/scripts/attachment_jobs.sh start JOB-ID`로 처리한다. 이 명령은 상태를 `InProgress`로 바꾸고 `GPTs/` 변경분만 commit한다.
- `run JOB-ID`는 job이 `ToDo`이면 자동으로 `start JOB-ID`를 먼저 수행한 뒤 Codex CLI를 실행한다.
- 종료는 `bash GPTs/scripts/attachment_jobs.sh finish JOB-ID Review "요약"` 또는 `Done`, `Fail`, `Blocked`, `Skip` 중 하나로 처리한다. 이 명령은 상태 변경과 산출물을 함께 commit한다.
- 긴 job에서는 중간 저장점이 필요할 때 `bash GPTs/scripts/attachment_jobs.sh commit JOB-ID "중간 요약"`을 사용한다.
- 중간에 토큰 부족, 세션 종료, CLI 실패가 발생하면 `bash GPTs/scripts/attachment_jobs.sh history JOB-ID`로 해당 job의 진행 commit을 확인하고 이어서 작업한다.
- runner의 commit 범위는 기본적으로 `GPTs/`이다. 원본 매뉴얼이나 다른 디렉터리의 수정분은 job commit에 포함하지 않는다.
- 실패한 job은 `finish JOB-ID Fail "실패 이유"`로 닫아 원인을 commit message에 남긴다. 그 job에 의존하지 않는 다른 ready job은 계속 진행한다.

전체 자동 진행:

- `bash GPTs/scripts/attachment_jobs.sh run-all`은 선행 job이 모두 `Done`인 `ToDo` 작업을 처음부터 끝까지 순차 실행한다.
- `bash GPTs/scripts/attachment_jobs.sh run-all "P3 SQL Core"`처럼 phase를 지정하면 해당 phase의 ready job만 실행한다.
- `MAX_JOBS=3`을 붙이면 긴 작업을 3개 job 단위로 끊어서 실행할 수 있다.
- `STOP_ON_FAIL=1`을 붙이면 job 하나가 실패한 즉시 전체 실행을 멈춘다. 기본값은 실패한 job을 `Fail`로 닫고 관계 없는 ready job을 계속 실행하는 것이다.
- `AUTO_ACCEPT_REVIEW=1`을 붙이면 Codex가 `Review`로 끝낸 job을 자동으로 `Done`으로 승격해 후속 dependency가 계속 진행되게 한다.
- `ALLOW_INCOMPLETE=1`을 붙이면 더 이상 ready job이 없어 멈췄지만 blocked `ToDo`가 남아 있어도 shell 성공으로 반환한다.

선행 관계 규칙:

- `next`와 `run`은 선행 job이 모두 `Done`인 작업만 실행 대상으로 삼는다.
- 어떤 job이 `Fail` 또는 `Blocked`가 되어도 관계 없는 다른 `ToDo` job은 계속 진행할 수 있다.
- 문서 변환 job은 필요한 source inventory, 언어 정책, 헤더 변환, label cleanup이 성공한 후 실행한다.
- Mermaid 변환 job은 image inventory와 관련 첨부 문서 변환이 성공한 후 실행한다.
- QA job은 자신이 검수하는 변환 job들이 성공한 후 실행한다.

## 원천 버전 매핑

| 답변 기준 버전 | 내부 원천 경로 | 고객용 표기 |
| --- | --- | --- |
| 7.1 | `Manuals/Altibase_7.1` | Altibase 7.1 |
| 7.3 | `Manuals/Altibase_7.3` | Altibase 7.3 |
| 8.1 | `Manuals/Altibase_trunk` + `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md` | Altibase 8.1 검증본 |

검수 규칙:

- 첨부용 문서에는 `trunk`를 쓰지 않는다.
- 내부 작업 문서와 선정안에는 추적성을 위해 원천 경로를 유지한다.
- 8.1 원천은 8.1 릴리스 노트와 대조해 신규 기능 반영 여부를 확인한다.

## 산출물

- `GPTs/Altibase_GPT_Document_Selection.md`
- `GPTs/Altibase_GPT_Attachment_Build_Workplan.md`
- `GPTs/attachments/README.md`
- `GPTs/attachments/00_version_release_platform.md`
- `GPTs/attachments/01_getting_started_installation.md`
- `GPTs/attachments/02_administration_operations.md`
- `GPTs/attachments/03_sql_ddl_generation.md`
- `GPTs/attachments/04_sql_dml_oracle_compatibility.md`
- `GPTs/attachments/05_data_types_properties.md`
- `GPTs/attachments/06_data_dictionary_performance_views.md`
- `GPTs/attachments/07_error_messages_troubleshooting.md`
- `GPTs/attachments/08_performance_tuning_monitoring.md`
- `GPTs/attachments/09_replication_ha_cdc.md`
- `GPTs/attachments/10_psm_stored_external_procedures.md`
- `GPTs/attachments/11_java_jdbc_spring.md`
- `GPTs/attachments/12_c_cli_odbc_precompiler.md`
- `GPTs/attachments/13_isql_iloader_basic_tools.md`
- `GPTs/attachments/14_utilities_operation_tools.md`
- `GPTs/attachments/15_migration_oracle_compatibility.md`
- `GPTs/attachments/16_dblink_external_connectors.md`
- `GPTs/attachments/17_kubernetes_aku_cloud.md`
- `GPTs/attachments/18_security_ssl_tls.md`
- `GPTs/attachments/19_spatial_nifi_tableau_misc.md`

## 작업 단계

### 1차: SQL/DDL 생성 핵심

대상:

- `03_sql_ddl_generation.md`
- `04_sql_dml_oracle_compatibility.md`
- `05_data_types_properties.md`
- `06_data_dictionary_performance_views.md`

작업:

- Oracle과 겹치는 일반 SQL은 축약한다.
- Altibase DDL, 테이블스페이스, 메모리/디스크 테이블, 인덱스, 시퀀스, 사용자/권한, 이중화 SQL, 프로퍼티 확인 SQL은 예제 중심으로 정리한다.
- 7.1/7.3/8.1 차이가 있으면 명시한다.

### 2차: 운영/성능/이중화

대상:

- `01_getting_started_installation.md`
- `02_administration_operations.md`
- `07_error_messages_troubleshooting.md`
- `08_performance_tuning_monitoring.md`
- `09_replication_ha_cdc.md`
- `18_security_ssl_tls.md`

작업:

- 운영 절차는 체크리스트로 만든다.
- 표는 항목 단위 설명으로 분해한다.
- 이미지 흐름은 Mermaid 또는 절차 텍스트로 바꾼다.

### 3차: 개발 인터페이스

대상:

- `10_psm_stored_external_procedures.md`
- `11_java_jdbc_spring.md`
- `12_c_cli_odbc_precompiler.md`
- `13_isql_iloader_basic_tools.md`

작업:

- 연결 문자열, 드라이버, API 사용 순서, LOB 처리, 오류 대응을 FAQ화한다.
- API 표는 함수별 "역할/인자/반환/주의사항"으로 분해한다.

### 4차: 도구/마이그레이션/외부 연동

대상:

- `00_version_release_platform.md`
- `14_utilities_operation_tools.md`
- `15_migration_oracle_compatibility.md`
- `16_dblink_external_connectors.md`
- `17_kubernetes_aku_cloud.md`
- `19_spatial_nifi_tableau_misc.md`

작업:

- 릴리스 노트는 버전 차이와 업그레이드 주의사항 중심으로 재구성한다.
- 스크린샷 중심 문서는 의미 있는 절차 설명으로 대체한다.
- 특정 도구별 제약사항과 문제 해결 항목을 분리한다.

## 공통 문서 템플릿

각 첨부 문서는 아래 구조를 따른다.

```markdown
# 문서 제목

## 적용 버전

- 7.1:
- 7.3:
- 8.1:

## 이 문서로 답할 수 있는 질문

- ...

## 원천 문서

- 7.1:
- 7.3:
- 8.1 검증본:

## 핵심 정리

## 버전별 차이

## 변환 TODO
```

## 검수 체크리스트

- `GPTs/attachments/*.md`가 정확히 20개인지 확인한다.
- `GPTs/attachments/README.md`는 첨부 카탈로그이며 20개 카운트에서 제외한다.
- 첨부용 문서 본문에 `trunk`가 남지 않았는지 확인한다.
- 각 첨부 문서에 적용 버전, 원천 문서, 답변 가능한 질문, 변환 TODO가 있는지 확인한다.
- `C:/`, `file://`, 깨진 이미지 링크, 원본 스크린샷만 의미하는 문장이 남지 않았는지 확인한다.
- SQL 생성 문서는 최소 20개 대표 질문으로 샘플링한다.

## 대표 SQL 생성 검수 질문

1. 8.1 기준 JSON 칼럼이 있는 테이블 DDL을 만들어줘.
2. 7.3 기준 디스크 테이블스페이스와 그 위의 테이블을 만들어줘.
3. 메모리 테이블스페이스를 생성하고 자동 확장을 켜는 SQL을 만들어줘.
4. 특정 테이블에 인덱스를 추가하고 확인하는 SQL을 만들어줘.
5. 사용자 생성과 기본 테이블스페이스 지정 SQL을 만들어줘.
6. 권한 부여와 회수 SQL을 만들어줘.
7. 시퀀스 생성 SQL을 만들어줘.
8. 테이블을 다른 테이블스페이스로 이동하는 SQL을 만들어줘.
9. LOB 칼럼을 가진 테이블 DDL을 만들어줘.
10. 파티션 테이블 생성 예제를 만들어줘.
11. 이중화 객체를 생성하는 SQL을 만들어줘.
12. 8.1 기준 SSL 이중화 생성 예제를 만들어줘.
13. 이중화 시작/중지 SQL을 만들어줘.
14. 프로퍼티 값을 확인하는 SQL을 만들어줘.
15. 성능 뷰에서 세션 상태를 확인하는 SQL을 만들어줘.
16. 실행 계획을 확인하는 절차를 알려줘.
17. iLoader로 데이터를 적재하는 명령 예제를 만들어줘.
18. JDBC 연결 문자열을 만들어줘.
19. Oracle DDL을 Altibase DDL로 바꿀 때 주의할 점을 알려줘.
20. 특정 오류 코드가 발생했을 때 원인과 조치 방법을 알려줘.

# 03. SQL DDL 생성

## 적용 버전

- 7.1: Altibase 7.1 SQL Reference 기준
- 7.3: Altibase 7.3 SQL Reference 기준
- 8.1: Altibase 8.1 검증본 SQL Reference와 8.1 릴리스 노트 기준

## 이 문서로 답할 수 있는 질문

- 메모리/디스크 테이블스페이스와 테이블 DDL을 만들어줘.
- Oracle DDL을 Altibase DDL로 바꿔줘.
- 사용자, 권한, 시퀀스, 인덱스 생성 SQL을 만들어줘.
- 이중화 객체 생성과 시작 SQL을 만들어줘.
- 설정값이나 성능 뷰를 확인하는 SQL을 만들어줘.

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/SQL Reference.md`, `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- 7.3: `Manuals/Altibase_7.3/kor/SQL Reference.md`, `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- 8.1 검증본: `SQL Reference.md`, `General_Reference-1.Data Types & Altibase Properties.md`, `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## SQL 생성 원칙

- 고객 버전이 명시되면 반드시 해당 버전 기준으로 생성한다.
- 고객 버전이 없으면 8.1 기준으로 생성하고, 7.1/7.3에서는 JSON, Temporary LOB, replication SSL 등 일부 기능이 없을 수 있음을 말한다.
- Oracle과 동일하거나 거의 같은 DML/기본 SELECT는 길게 설명하지 않는다.
- Altibase 고유 DDL, 테이블스페이스, 메모리/디스크 저장 구조, 이중화, 프로퍼티 확인 SQL을 우선한다.

## Oracle 호환성 기준

- 기본 `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `WHERE`, `GROUP BY`, `ORDER BY`는 Oracle과 유사한 영역으로 답한다.
- `CREATE TABLE`, `TABLESPACE`, `MAXROWS`, `QUEUE`, `REPLICATION`, 메모리/디스크 테이블스페이스, LOB 저장 위치는 Altibase 차이점이 중요하므로 Altibase 문법을 우선한다.
- Oracle DDL 변환 요청에는 "Oracle 문법 그대로 실행 가능"이라고 단정하지 않는다.

## DDL 작성 패턴

### 테이블스페이스

질문 예시:

- 디스크 테이블스페이스를 만들고 테이블을 생성해줘.
- 메모리 테이블스페이스를 자동 확장으로 생성해줘.

Oracle 호환성:

- Oracle의 tablespace 개념과 목적은 유사하지만, Altibase는 메모리/디스크/휘발성/임시 테이블스페이스 구분이 중요하다.

예제:

```sql
CREATE DISK TABLESPACE disk_tbs_01
DATAFILE '/data/altibase/disk_tbs_01.dbf';

CREATE MEMORY TABLESPACE mem_tbs_01
SIZE 32M
AUTOEXTEND ON;

ALTER TABLESPACE mem_tbs_01
ALTER AUTOEXTEND ON NEXT 256M MAXSIZE 1G;
```

확인 SQL:

```sql
SELECT * FROM V$TABLESPACES;
SELECT * FROM V$MEM_TABLESPACES;
```

### 테이블

질문 예시:

- 메모리 테이블을 생성하는 DDL을 만들어줘.
- LOB 칼럼이 있는 디스크 테이블을 만들어줘.

Oracle 호환성:

- 컬럼 정의, 제약 조건, 기본 DDL 구조는 Oracle과 유사하다.
- 저장 위치, 메모리/디스크 테이블스페이스, LOB 저장 위치, `MAXROWS` 같은 절은 Altibase 기준으로 확인해야 한다.

예제:

```sql
CREATE TABLE app_user (
    user_id     INTEGER NOT NULL,
    user_name   VARCHAR(80) NOT NULL,
    created_at  DATE DEFAULT SYSDATE,
    CONSTRAINT pk_app_user PRIMARY KEY (user_id)
) TABLESPACE mem_tbs_01;

CREATE TABLE app_document (
    doc_id      INTEGER NOT NULL,
    title       VARCHAR(200),
    body        CLOB,
    CONSTRAINT pk_app_document PRIMARY KEY (doc_id)
) TABLESPACE disk_tbs_01;
```

8.1 JSON 예제:

```sql
CREATE TABLE app_event (
    event_id    INTEGER NOT NULL,
    payload     JSON,
    created_at  DATE DEFAULT SYSDATE,
    CONSTRAINT pk_app_event PRIMARY KEY (event_id)
) TABLESPACE disk_tbs_01;
```

### 인덱스

질문 예시:

- 특정 컬럼에 인덱스를 추가해줘.
- 인덱스 테이블스페이스를 지정해줘.

예제:

```sql
CREATE INDEX idx_app_user_name
ON app_user (user_name)
TABLESPACE mem_tbs_01;
```

확인 SQL:

```sql
SELECT * FROM SYSTEM_.SYS_INDICES_;
```

### 사용자와 권한

질문 예시:

- 애플리케이션 사용자를 만들고 기본 테이블스페이스를 지정해줘.
- 특정 테이블에 조회/입력 권한을 부여해줘.

예제:

```sql
CREATE USER app IDENTIFIED BY app_password
DEFAULT TABLESPACE mem_tbs_01;

GRANT CREATE SESSION TO app;
GRANT SELECT, INSERT, UPDATE, DELETE ON sys.app_user TO app;
```

주의:

- 실제 운영에서는 비밀번호 정책과 권한 최소화를 적용한다.
- 객체 소유자와 스키마명을 고객 환경에 맞게 바꾼다.

### 시퀀스

질문 예시:

- PK용 시퀀스를 만들어줘.

예제:

```sql
CREATE SEQUENCE seq_app_user
START WITH 1
INCREMENT BY 1;
```

### 이중화

질문 예시:

- 두 서버 간 테이블 이중화를 생성하는 SQL을 만들어줘.
- 8.1 기준 SSL 이중화 예제를 만들어줘.

일반 예제:

```sql
CREATE REPLICATION rep_app
WITH '192.168.10.12', 35524
FROM app.app_user TO app.app_user;

ALTER REPLICATION rep_app START;
```

8.1 SSL 예제:

```sql
CREATE REPLICATION rep_app_ssl
WITH '192.168.10.12', 45524 USING SSL
FROM app.app_user TO app.app_user;
```

주의:

- 양방향 또는 Active-Standby 구성에서는 상대 서버에도 대응되는 이중화 객체를 생성해야 한다.
- SSL 이중화는 8.1 기준 기능으로 답하고, 7.1/7.3 고객에게는 사용 가능 여부를 확인하도록 안내한다.

### 설정과 확인 SQL

질문 예시:

- 현재 프로퍼티 값을 확인하는 SQL을 알려줘.
- 세션과 성능 상태를 확인하는 SQL을 알려줘.

예제:

```sql
SELECT * FROM V$PROPERTY
WHERE NAME IN ('LOG_FILE_SIZE', 'REPLICATION_SSL_PORT_NO');

SELECT * FROM V$SESSION;
SELECT * FROM V$STATEMENT;
```

주의:

- 성능 뷰 이름과 컬럼은 버전별로 달라질 수 있다.
- 정확한 컬럼 설명은 `06_data_dictionary_performance_views.md`를 함께 사용한다.

## 변환 TODO

- SQL Reference의 `CREATE/ALTER/DROP` 계열을 이 형식으로 모두 재구성한다.
- 7.1/7.3/8.1 차이를 항목별로 채운다.
- 구문 이미지나 다이어그램은 BNF형 텍스트 또는 Mermaid로 바꾼다.
- 예제 SQL은 대표 질문 20개로 샘플링 검수한다.

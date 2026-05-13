# 05. 데이터 타입과 프로퍼티

## 적용 버전

- 7.1: Altibase 7.1 General Reference 1 기준
- 7.3: Altibase 7.3 General Reference 1 기준
- 8.1: Altibase 8.1 검증본 General Reference 1과 8.1 릴리스 노트 기준

## 이 문서로 답할 수 있는 질문

- Altibase 데이터 타입과 Oracle 데이터 타입의 차이는 무엇인가?
- 서버 프로퍼티를 어디서 확인하고 어떻게 설정하는가?
- 8.1 JSON 데이터 타입과 Temporary LOB는 무엇인가?
- `LOG_FILE_SIZE`, `REPLICATION_SSL_PORT_NO` 같은 프로퍼티는 어떤 의미인가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/General Reference-1.Data Types & Altibase Properties.md`
- 7.3: `Manuals/Altibase_7.3/kor/General_Reference-1.Data Types & Altibase Properties.md`
- 8.1 검증본: `General_Reference-1.Data Types & Altibase Properties.md`, `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## 핵심 정리

- 데이터 타입 답변은 버전, 저장 대상, SQL 생성 목적을 먼저 확인한다.
- 8.1은 Native JSON 데이터 타입과 JSON 함수가 추가된 기준으로 별도 설명한다.
- 프로퍼티는 "의미", "기본값", "동적 변경 가능 여부", "관련 성능 뷰/확인 SQL"로 분해한다.

## 변환 TODO

- 데이터 타입 표를 타입별 설명 블록으로 분해한다.
- 프로퍼티 표를 항목별 설명 블록으로 분해한다.
- 8.1 신규/변경/삭제 프로퍼티를 릴리스 노트와 대조한다.

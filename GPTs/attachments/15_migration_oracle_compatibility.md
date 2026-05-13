# 15. 마이그레이션과 Oracle 호환성

## 적용 버전

- 7.1: Altibase 7.1 마이그레이션 관련 문서 기준
- 7.3: Altibase 7.3 Migration Center/Oracle Adapter 기준
- 8.1: Altibase 8.1 검증본과 최신 Migration Center 릴리스 기준

## 이 문서로 답할 수 있는 질문

- Oracle에서 Altibase로 전환할 때 DDL은 어떻게 바꾸는가?
- Migration Center 사용 절차는?
- Oracle Adapter는 어떤 경우에 사용하는가?
- 마이그레이션 전후 검증 방법은?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/Adapter for Oracle User's Manual.md`
- 7.3: `Manuals/Tools/Altibase_release/kor/Migration Center User's Manual.md`, `Manuals/Altibase_7.3/kor/Adapter for Oracle User's Manual.md`
- 8.1 검증본: `Migration Center User's Manual.md`, `Adapter for Oracle User's Manual.md`, `ReleaseNotes/kor/Altibase_Migration_Center_7_19_Release_Notes.md`

## 핵심 정리

- Oracle 호환성은 "그대로 사용 가능", "수정 필요", "대체 설계 필요"로 나눠 답한다.
- DDL 변환은 `03_sql_ddl_generation.md`를 우선 참조한다.

## 변환 TODO

- Migration Center 절차를 단계형으로 정리한다.
- Oracle 데이터 타입/DDL 차이점을 SQL 생성 문서와 연결한다.
- 도구 릴리스 노트의 7.x 버전 언급은 도구 버전으로만 표시한다.

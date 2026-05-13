# 06. 데이터 딕셔너리와 성능 뷰

## 적용 버전

- 7.1: Altibase 7.1 General Reference 2 기준
- 7.3: Altibase 7.3 General Reference 2 기준
- 8.1: Altibase 8.1 검증본 General Reference 2와 8.1 릴리스 노트 기준

## 이 문서로 답할 수 있는 질문

- 테이블, 인덱스, 사용자, 권한 정보를 조회하는 SQL을 알려줘.
- 성능 뷰에서 세션, statement, replication 상태를 확인하는 방법은?
- 특정 프로퍼티나 메타 정보를 확인하는 SQL은?
- 8.1에서 추가된 성능 뷰는 무엇인가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/General Reference-2.The Data Dictionary.md`
- 7.3: `Manuals/Altibase_7.3/kor/General_Reference-2.The Data Dictionary.md`
- 8.1 검증본: `General_Reference-2.The Data Dictionary.md`, `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## 핵심 정리

- 표 전체를 그대로 두지 말고 객체별로 "용도", "주요 컬럼", "대표 조회 SQL"을 제공한다.
- 고객이 객체명을 주면 해당 객체의 메타/성능 뷰 조회 SQL을 함께 생성한다.

## 대표 확인 SQL 패턴

```sql
SELECT * FROM SYSTEM_.SYS_TABLES_;
SELECT * FROM SYSTEM_.SYS_INDICES_;
SELECT * FROM V$SESSION;
SELECT * FROM V$STATEMENT;
SELECT * FROM V$PROPERTY;
```

## 변환 TODO

- 메타 테이블과 성능 뷰를 주제별로 재분류한다.
- 8.1 신규 성능 뷰를 릴리스 노트와 대조한다.
- 자주 쓰는 확인 SQL cookbook을 만든다.

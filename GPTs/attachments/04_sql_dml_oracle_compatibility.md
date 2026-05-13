# 04. SQL DML과 Oracle 호환성

## 적용 버전

- 7.1: Altibase 7.1 SQL Reference 기준
- 7.3: Altibase 7.3 SQL Reference 기준
- 8.1: Altibase 8.1 검증본 SQL Reference 기준

## 이 문서로 답할 수 있는 질문

- Altibase에서 Oracle SQL을 어느 정도 그대로 쓸 수 있는가?
- SELECT, INSERT, UPDATE, DELETE 작성 시 주의할 점은 무엇인가?
- Oracle 함수와 Altibase 함수의 차이를 알려줘.
- 8.1 JSON 함수는 어떻게 써야 하는가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/SQL Reference.md`
- 7.3: `Manuals/Altibase_7.3/kor/SQL Reference.md`
- 8.1 검증본: `SQL Reference.md`

## 핵심 정리

- 일반 DML은 Oracle과 유사하다고 안내하되, Altibase 데이터 타입/함수/제한사항은 반드시 확인한다.
- SQL 생성 요청에서 DML만 필요한 경우에도 테이블이 메모리인지 디스크인지, LOB/JSON 사용 여부를 확인한다.
- JSON 함수는 8.1 기준 기능으로 분리한다.

## 답변 지침

- Oracle 호환 영역: 기본 SELECT, JOIN, INSERT, UPDATE, DELETE, GROUP BY, ORDER BY.
- Altibase 확인 필요 영역: 데이터 타입 변환, 날짜/문자 함수, 정규 표현식, LOB, JSON, 힌트, 계층 질의, 분석 함수.

## 변환 TODO

- Oracle과 유사한 구문은 한 줄 설명과 예제 하나로 축약한다.
- Altibase 전용 또는 차이가 있는 함수만 상세화한다.
- 8.1 JSON 함수는 `JSON_ARRAY`, `JSON_OBJECT`, `JSON_EXISTS`, `JSON_QUERY`, `JSON_VALUE`, `JSON_VALID` 중심으로 정리한다.

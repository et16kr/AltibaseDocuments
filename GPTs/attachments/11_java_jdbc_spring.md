# 11. Java, JDBC, Spring

## 적용 버전

- 7.1: Altibase 7.1 JDBC 기준
- 7.3: Altibase 7.3 JDBC와 JDBC 4.2 개선 기준
- 8.1: Altibase 8.1 검증본 JDBC와 Java 호환성 기준

## 이 문서로 답할 수 있는 질문

- JDBC 연결 문자열을 만들어줘.
- Java 버전 호환성은 어떻게 되는가?
- Spring Data JPA/Hibernate에서 Altibase를 연결하려면?
- JDBC LOB/JSON 처리 시 주의할 점은?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/JDBC User's Manual.md`, `Manuals/Altibase_7.1/kor/Adapter for JDBC User's Manual.md`
- 7.3: `Manuals/Altibase_7.3/kor/JDBC User's Manual.md`, `Manuals/Altibase_7.3/kor/Adapter for JDBC User's Manual.md`
- 8.1 검증본: `JDBC User's Manual.md`, `Adapter for JDBC User's Manual.md`, `Technical Documents/kor/JavaCompatibility.md`
- 공통 외부 가이드: `3rd Party Guide for Altibase/kor/Spring Data JPA User's Guide for Altibase.md`, `3rd Party Guide for Altibase/kor/Spring Data JPA with Hibernate 6.4 User's Guide for Altibase.md`

## 핵심 정리

- Java 답변은 드라이버 파일, JDBC URL, 계정/권한, charset, failover 옵션을 함께 다룬다.
- Spring/Hibernate 질문은 dialect, datasource, transaction 설정을 우선한다.

## 변환 TODO

- 연결 문자열과 Spring 설정 예제를 버전별로 정리한다.
- JavaCompatibility 문서를 버전 매트릭스에서 설명형 목록으로 바꾼다.
- 8.1 JSON/LOB JDBC 주의사항을 보강한다.

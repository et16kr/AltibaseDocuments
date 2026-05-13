# 16. DB Link와 외부 커넥터

## 적용 버전

- 7.1: Altibase 7.1 DB Link/Hadoop 기준
- 7.3: Altibase 7.3 DB Link/Hadoop/3rd Party Connector 기준
- 8.1: Altibase 8.1 검증본 DB Link/Hadoop/외부 커넥터 기준

## 이 문서로 답할 수 있는 질문

- DB Link를 어떻게 구성하는가?
- Hadoop Connector는 언제 쓰는가?
- DBeaver, Hibernate, OpenLDAP, GoldenGate 연동은 어떻게 하는가?
- 외부 커넥터 문제를 어떻게 점검하는가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/DB Link User's Manual.md`, `Manuals/Altibase_7.1/kor/Hadoop Connector User's Manual.md`
- 7.3: `Manuals/Altibase_7.3/kor/DB Link User's Manual.md`, `Manuals/Altibase_7.3/kor/Hadoop Connector User's Manual.md`, `Manuals/Tools/Altibase_release/kor/Altibase 3rd Party Connector Guide.md`
- 8.1 검증본: `DB Link User's Manual.md`, `Hadoop Connector User's Manual.md`, `Altibase 3rd Party Connector Guide.md`

## 핵심 정리

- 연동 답변은 대상 제품, 연결 방식, 인증, 네트워크, 드라이버/라이브러리 버전을 함께 확인한다.
- 스크린샷 중심 절차는 설명형 단계로 변환한다.

## 변환 TODO

- 제품별 연결 절차와 제약사항을 독립 블록으로 나눈다.
- DB Link 설정과 보안 설정은 SSL/TLS 문서와 교차 참조한다.

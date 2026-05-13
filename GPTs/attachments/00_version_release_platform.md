# 00. 버전, 릴리스, 지원 플랫폼

## 적용 버전

- 7.1: Altibase 7.1 릴리스와 매뉴얼 기준
- 7.3: Altibase 7.3 릴리스와 매뉴얼 기준
- 8.1: Altibase 8.1 릴리스 노트와 8.1 검증본 기준

## 이 문서로 답할 수 있는 질문

- Altibase 7.3과 8.1의 주요 차이는 무엇인가?
- 8.1에서 추가된 JSON, Temporary LOB, replication SSL 기능은 무엇인가?
- 현재 OS가 Altibase 서버 또는 클라이언트 지원 대상인가?
- 8.1 업그레이드 시 데이터베이스/메타 호환성에서 주의할 점은 무엇인가?

## 원천 문서

- 7.1: `ReleaseNotes/kor/Altibase_7_1_0_1_2_Release_Notes.md`, `Technical Documents/kor/Supported Platforms.md`
- 7.3: `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`, `Technical Documents/kor/Supported Platforms.md`
- 8.1 검증본: `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`, `Technical Documents/kor/Supported Platforms.md`

## 핵심 정리

- 버전 질문에는 먼저 고객 버전을 확인한다.
- 고객이 버전을 말하지 않으면 8.1 기준 답변을 기본으로 하되, 7.1/7.3에서는 다를 수 있음을 명시한다.
- 플랫폼 표는 그대로 두지 말고 OS/CPU/서버 지원/클라이언트 지원/필수 소프트웨어 항목으로 풀어쓴다.

## 버전별 차이 작성 지침

- 7.1: 기존 안정 고객 기준의 기능과 제약을 유지한다.
- 7.3: AKU, JDBC 4.2, OpenSSL 3.0.8, SQL/Spatial/Replication 개선을 별도 요약한다.
- 8.1: JSON 데이터 타입, Temporary LOB, KADA, Kafka connector, ABM, replication SSL, JSON plan, 프로퍼티/성능 뷰 변경을 별도 요약한다.

## 변환 TODO

- 릴리스 노트 표를 문장형 목록으로 분해한다.
- 업그레이드 호환성 주의사항을 `위험`, `필수 작업`, `확인 SQL`로 재구성한다.
- 7.1/7.3/8.1 지원 플랫폼을 한 문서 안에서 충돌 없이 정리한다.

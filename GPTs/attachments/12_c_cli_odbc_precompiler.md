# 12. C, CLI, ODBC, Precompiler

## 적용 버전

- 7.1: Altibase 7.1 C/CLI/ODBC/Precompiler 기준
- 7.3: Altibase 7.3 C/CLI/ODBC/Precompiler 기준
- 8.1: Altibase 8.1 검증본 C/CLI/ODBC/Precompiler 기준

## 이 문서로 답할 수 있는 질문

- CLI API의 기본 호출 순서는?
- ODBC 연결 문자열은 어떻게 작성하는가?
- C Interface와 Precompiler는 어떤 차이가 있는가?
- LOB/JSON 관련 CLI 함수 사용 시 주의할 점은?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/CLI User's Manual.md`, `Manuals/Altibase_7.1/kor/ODBC User's Manual.md`, `Manuals/Altibase_7.1/kor/Altibase C Interface Manual.md`, `Manuals/Altibase_7.1/kor/Precompiler User's Manual.md`
- 7.3: `Manuals/Altibase_7.3/kor/CLI User's Manual.md`, `Manuals/Altibase_7.3/kor/ODBC User's Manual.md`, `Manuals/Altibase_7.3/kor/Altibase C Interface Manual.md`, `Manuals/Altibase_7.3/kor/Precompiler User's Manual.md`
- 8.1 검증본: `CLI User's Manual.md`, `ODBC User's Manual.md`, `Altibase C Interface Manual.md`, `Precompiler User's Manual.md`

## 핵심 정리

- API 표는 함수별 설명 블록으로 분해한다.
- 연결 문자열, 핸들 생성/해제, 트랜잭션 처리, LOB 처리 순서를 cookbook으로 만든다.

## 변환 TODO

- CLI API 목록을 "연결", "실행", "fetch", "LOB", "오류 처리"로 재분류한다.
- 8.1 JSON 관련 LOB locator 함수 설명을 보강한다.

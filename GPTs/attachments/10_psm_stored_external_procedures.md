# 10. PSM, 저장 프로시저, 외부 프로시저

## 적용 버전

- 7.1: Altibase 7.1 Stored Procedures 기준
- 7.3: Altibase 7.3 Stored Procedures 기준
- 8.1: Altibase 8.1 검증본 Stored Procedures 기준

## 이 문서로 답할 수 있는 질문

- 저장 프로시저와 함수를 어떻게 작성하는가?
- 커서, 예외, 패키지, VARRAY 사용법은?
- C/C++ 외부 프로시저는 어떻게 연결하는가?
- 8.1 Temporary LOB와 PSM의 관계는?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/Stored Procedures Manual.md`, `Manuals/Altibase_7.1/kor/External Procedures Manual.md`
- 7.3: `Manuals/Altibase_7.3/kor/Stored Procedures Manual.md`, `Manuals/Altibase_7.3/kor/External Procedures Manual.md`
- 8.1 검증본: `Stored Procedures Manual.md`, `External Procedures Manual.md`

## 핵심 정리

- Oracle PL/SQL과 유사한 부분은 짧게 설명하고, Altibase PSM 문법과 제한을 우선한다.
- 문법 이미지는 BNF형 텍스트로 변환한다.

## 변환 TODO

- procedure/function/package/cursor/exception 예제를 최소 예제와 운영 예제로 나눈다.
- 외부 프로시저는 external/internal mode 차이를 별도 설명한다.
- 8.1 Temporary LOB 관련 PSM 동작을 보강한다.

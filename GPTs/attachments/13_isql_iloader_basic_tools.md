# 13. iSQL, iLoader, 기본 도구

## 적용 버전

- 7.1: Altibase 7.1 iSQL/iLoader 기준
- 7.3: Altibase 7.3 iSQL/iLoader 기준
- 8.1: Altibase 8.1 검증본 iSQL/iLoader 기준

## 이 문서로 답할 수 있는 질문

- iSQL로 접속하고 SQL을 실행하는 방법은?
- iLoader로 데이터를 내보내고 적재하는 명령은?
- 운영자가 자주 쓰는 기본 확인 명령은?
- 비밀번호 파일이나 보안 로그인 옵션은 어떻게 쓰는가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/iSQL User's Manual.md`, `Manuals/Altibase_7.1/kor/iLoader User's Manual.md`
- 7.3: `Manuals/Altibase_7.3/kor/iSQL User's Manual.md`, `Manuals/Altibase_7.3/kor/iLoader User's Manual.md`
- 8.1 검증본: `iSQL User's Manual.md`, `iLoader User's Manual.md`

## 핵심 정리

- iSQL 답변은 접속, 스크립트 실행, 결과 확인, 오류 확인 순서로 답한다.
- iLoader 답변은 formout/out/in, 구분자, 파일 경로, replace/append 모드 같은 실무 항목을 우선한다.

## 변환 TODO

- iSQL 명령은 자주 쓰는 명령 위주로 cookbook화한다.
- iLoader 절차는 `포맷 생성 -> export -> import -> 검증`으로 정리한다.

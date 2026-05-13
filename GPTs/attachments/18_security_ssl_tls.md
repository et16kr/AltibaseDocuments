# 18. 보안과 SSL/TLS

## 적용 버전

- 7.1: Altibase 7.1 SSL/TLS 기준
- 7.3: Altibase 7.3 SSL/TLS와 OpenSSL 3.0.8 기준
- 8.1: Altibase 8.1 검증본 SSL/TLS와 replication SSL 기준

## 이 문서로 답할 수 있는 질문

- SSL/TLS 접속을 어떻게 설정하는가?
- 인증서와 서버/클라이언트 설정 흐름은?
- 7.3의 OpenSSL 3.0.8 지원 사항은?
- 8.1 replication SSL은 어떻게 구성하는가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/Altibase SSL TLS User's Guide.md`
- 7.3: `Manuals/Altibase_7.3/kor/Altibase SSL TLS User's Guide.md`, `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
- 8.1 검증본: `Altibase SSL TLS User's Guide.md`, `ReleaseNotes/kor/Altibase_8_1_0_0_1_Release_Notes.md`

## 핵심 정리

- SSL/TLS 답변은 인증서 준비, 서버 프로퍼티, 클라이언트 연결 옵션, 검증 절차로 나눈다.
- replication SSL은 이중화 문서와 함께 답한다.

## 변환 TODO

- 인증서 생성/배치/설정 절차를 체크리스트로 바꾼다.
- 프로퍼티와 연결 옵션을 항목별 설명으로 분해한다.

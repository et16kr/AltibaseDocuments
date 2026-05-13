# 07. 오류 메시지와 문제 해결

## 적용 버전

- 7.1: Altibase 7.1 Error Message Reference 기준
- 7.3: Altibase 7.3 Error Message Reference 기준
- 8.1: Altibase 8.1 검증본 Error Message Reference 기준

## 이 문서로 답할 수 있는 질문

- 특정 Altibase 오류 코드의 원인과 조치 방법은?
- SQL 실행 오류가 발생했을 때 무엇을 확인해야 하는가?
- JSON, LOB, replication, 정규 표현식 관련 오류는 어떻게 조치하는가?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/Error Message Reference.md`
- 7.3: `Manuals/Altibase_7.3/kor/Error Message Reference.md`
- 8.1 검증본: `Error Message Reference.md`

## 핵심 정리

- 오류 답변은 "증상 -> 원인 -> 조치 -> 확인 SQL/명령 -> 관련 문서" 순서로 작성한다.
- 8.1 JSON 관련 오류는 8.1 전용으로 표시한다.

## 변환 형식

```text
오류 코드:
증상:
주요 원인:
조치:
확인 SQL/명령:
버전 주의사항:
```

## 변환 TODO

- 오류 목록을 코드 순서뿐 아니라 주제별로도 재분류한다.
- 자주 묻는 SQL/DDL/이중화/접속 오류를 우선 변환한다.

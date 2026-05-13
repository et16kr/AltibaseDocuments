# 17. Kubernetes와 AKU

## 적용 버전

- 7.1: 기본 제품 매뉴얼 기준, Kubernetes 전용 가이드는 별도 확인 필요
- 7.3: AKU 지원과 Kubernetes 가이드 기준
- 8.1: Altibase 8.1 검증본과 Kubernetes/AKU 가이드 기준

## 이 문서로 답할 수 있는 질문

- Kubernetes에서 Altibase를 배포할 때 주의할 점은?
- AKU는 어떤 역할을 하는가?
- Pod 시작/종료 시 데이터 동기화 절차는?
- 컨테이너 환경에서 이중화와 스토리지를 어떻게 고려해야 하는가?

## 원천 문서

- 7.1: 기본 운영/이중화 문서
- 7.3: `3rd Party Guide for Altibase/kor/Kubernetes User's Guide for Altibase.md`, `3rd Party Guide for Altibase/kor/Altibase aku Sample Guide for Kubernetes.md`, `ReleaseNotes/kor/Altibase_7_3_0_0_1_Release_Notes.md`
- 8.1 검증본: `Kubernetes User's Guide for Altibase.md`, `Altibase aku Sample Guide for Kubernetes.md`

## 핵심 정리

- Kubernetes 답변은 StatefulSet, PV/PVC, Pod lifecycle, AKU start/end, 이중화 초기화/동기화를 함께 설명한다.
- AKU 관련 명령은 운영 유틸리티 문서와 교차 참조한다.

## 변환 TODO

- YAML/명령 예제는 목적별로 분리한다.
- Pod 시작/종료 흐름은 Mermaid flowchart로 변환한다.

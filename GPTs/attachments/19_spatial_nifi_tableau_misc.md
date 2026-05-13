# 19. Spatial, NiFi, Tableau 기타 연동

## 적용 버전

- 7.1: Spatial SQL과 기본 연동 문서 기준
- 7.3: Spatial SQL, altiShapeLoader, NiFi, Tableau 가이드 기준
- 8.1: Altibase 8.1 검증본 Spatial/연동 문서 기준

## 이 문서로 답할 수 있는 질문

- Spatial SQL과 GEOMETRY 타입은 어떻게 사용하는가?
- Shapefile을 가져오거나 내보내려면?
- NiFi에서 Altibase를 연결하는 절차는?
- Tableau에서 Altibase 데이터를 조회하려면?

## 원천 문서

- 7.1: `Manuals/Altibase_7.1/kor/Spatial SQL Reference.md`
- 7.3: `Manuals/Altibase_7.3/kor/Spatial SQL Reference.md`, `Manuals/Tools/Altibase_release/kor/altiShapeLoader User's Manual.md`, `3rd Party Guide for Altibase/kor/NiFi User's Guide for Altibase.md`, `3rd Party Guide for Altibase/kor/Tableau User's Guide for Altibase/Tableau User's Guide for Altibase.md`
- 8.1 검증본: `Spatial SQL Reference.md`, `altiShapeLoader User's Manual.md`, `NiFi User's Guide for Altibase.md`, `Tableau User's Guide for Altibase.md`

## 핵심 정리

- Spatial 답변은 GEOMETRY 타입, SRID, WKT/WKB/EWKB, 공간 함수, 적재/추출 도구를 함께 본다.
- NiFi/Tableau는 화면 캡처보다 연결 속성, 드라이버, 절차, 오류 대응을 우선한다.

## 변환 TODO

- 공간 함수는 "함수명/용도/입력/출력/예제"로 정리한다.
- altiShapeLoader 절차는 import/export cookbook으로 만든다.
- NiFi/Tableau 스크린샷은 설명형 절차로 대체한다.

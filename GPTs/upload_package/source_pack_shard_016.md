# Altibase Source Pack Shard 016

- Shard ID: `SHARD-016`
- Upload role: primary source-preserving upload candidate
- Purpose: Final source-preserving package shard for GPT Knowledge, Codex, and LLM/RAG retrieval.

## Shard Retrieval Metadata

- Topic summary: utilities manuals and tool manuals, including dataCompJ and Altibase Heartbeat, across 7.3, 8.1, and multi-version releases.
- Major source families/manuals: `utilities_datacompj`.
- Version/language span: Altibase 7.3, `8.1_verified`, multi-version release tools, and dataCompJ 7.2; English and Korean manuals.
- Representative IDs: ordered source range `SRC-000137` to `SRC-000213`; block range `BLOCK-000929` to `BLOCK-000941`.
- Retrieval aliases: Utilities Manual, dataCompJ, Altibase Heartbeat, aexport, iLoader, iloader, backup utility, export import, compare data, tool command, command option.

## SRC-000137 - Altibase 7.3

| Field | Value |
| --- | --- |
| `source_id` | SRC-000137 |
| `source_path` | Manuals/Altibase_7.3/kor/Utilities Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 7.3 |
| `language` | ko |
| `authority_label` | Korean authoritative |
| `source_sha256` | 0f6a2e0f958d3e7601dc119cee2f755e194e9e232859e7311be3fbdeb8910e14 |
| `byte_count` | 265764 |
| `line_count` | 4811 |
| `estimated_tokens` | 47129 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000137" source_path="Manuals/Altibase_7.3/kor/Utilities Manual.md" source_family="utilities_datacompj" version_scope="7.3" language="ko" authority_label="Korean authoritative" sha256="0f6a2e0f958d3e7601dc119cee2f755e194e9e232859e7311be3fbdeb8910e14" byte_count="265764" line_count="4811" estimated_tokens="47129" block_id="BLOCK-000929" -->
Utilities Manual
================

#### Altibase 7.3

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 









































<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Tools & Utilities Utilities Manual
Release 7.3
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>



<br>

# 목차

- [서문](#서문)
  - [이 매뉴얼에 대하여](#이-매뉴얼에-대하여)
- [1.aexport](#1aexport)
  - [aexport 소개](#aexport-소개)
  - [사전 설정](#사전-설정)
  - [aexport 사용방법](#aexport-사용방법)
- [2.altiComp](#2alticomp)
  - [altiComp 소개](#alticomp-소개)
  - [altiComp 사용 방법](#alticomp-사용-방법)
  - [비교(DIFF) 기능](#비교diff-기능)
  - [일치(SYNC) 기능](#일치sync-기능)
- [3.aku](#3aku)
  - [개요](#개요-2)
  - [구성 요소](#구성-요소)
  - [구문](#구문-2)
  - [파라미터](#파라미터-2)
  - [주의사항](#주의사항)
  - [제약사항](#제약사항)
  - [사용 예](#사용-예)
- [4.altiMon](#4altimon)
  - [개요](#개요-3)
  - [구문](#구문-3)
  - [파라미터](#파라미터-3)
  - [시스템 요구사항](#시스템-요구사항)
  - [altiMon 시작 및 중지](#altiMon-시작-및-중지)
  - [altiMon 설정](#altiMon-설정)
  - [altiMon 로그](#altimon-로그)
- [5.기타 Utilities](#5기타-utilities)
  - [altiAudit](#altiaudit)
  - [altibase](#altibase)
  - [altierr](#altierr)
  - [altipasswd](#altipasswd)
  - [altiProfile](#altiprofile)
  - [altiwrap](#altiwrap)
  - [awrite](#awrite)
  - [checkServer](#checkserver)
  - [dumpbi](#dumpbi)
  - [dumpct](#dumpct)
  - [dumpdb](#dumpdb)
  - [dumpddf](#dumpddf)
  - [dumpla](#dumpla)
  - [dumplf](#dumplf)
  - [dumptrc](#dumptrc)
  - [killCheckServer](#killcheckserver)
  - [server](#server)





<br>

서문
====

## 이 매뉴얼에 대하여

이 매뉴얼은 Altibase를 사용하면서 필요한 유틸리티에 대해서 설명한다.

### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

-   데이터베이스 관리자

-   성능 관리자

-   데이터베이스 사용자

-   응용 프로그램 개발자

-   기술지원부

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

-   컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

-   관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

-   컴퓨터 프로그래밍 경험

-   데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

### 소프트웨어 환경

이 매뉴얼은 데이터베이스 서버로 Altibase 버전 7.3을 사용한다는 가정 하에 작성되었다.

### 이 매뉴얼의 구성

이 매뉴얼은 다음과 같이 구성되어 있다.

- 제 1장 aexport  
  이 장은 Altibase 데이터베이스 간 자동화된 데이터 마이그레이션(migration)을 지원하기 위한 도구인 aexport에 대해서 설명한다.

- 제 2장 altiComp  
  이 장은 altiComp 유틸리티의 기능을 소개하고, 불일치하는 데이터를 비교하고 일치시키는 기능 등을 설명한다.

- 제 3장 aku

  이 장은 쿠버네티스를 이용한 파드 간 데이터 이중화를 지원하기 위한 도구인 aku에 대해서 설명한다.

- 제 4장 altiMon

  이 장은 Altibase의 서버와 Altibase 서버가 구동 된 운영체제의 자원 상태를 수집하는 모니터링 유틸리티인 altiMon에 대해서 설명한다. 

- 제 5장 기타 Utilities  
  이 장은 aexport, altiComp, aku, altiMon을 제외한 나머지 유틸리티에 대해서 설명한다.

### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이 매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

-   구문 다이어그램

-   샘플 코드 규칙

### 구문 다이어그램

이 매뉴얼에서는 다음 구성 요소로 구축된 다이어그램을 사용하여, 명령문의 구문을 설명한다.

| 구성 요소                       | 의미                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| ![](media/Utilities/image1.gif) | 명령문이 시작한다. 완전한 명령문이 아닌 구문 요소는 화살표로 시작한다. |
| ![](media/Utilities/image2.gif) | 명령문이 다음 라인에 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 종료한다. |
| ![](media/Utilities/image3.gif) | 명령문이 이전 라인으로부터 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 시작한다. |
| ![](media/Utilities/image4.gif) | 명령문이 종료한다.                                           |
| ![](media/Utilities/image5.gif) | 필수 항목                                                    |
| ![](media/Utilities/image6.gif) | 선택적 항목.                                                 |
| ![](media/Utilities/image7.gif) | 선택사항이 있는 필수 항목. 한 항목만 제공해야 한다.          |
| ![](media/Utilities/image8.gif) | 선택사항이 있는 선택적 항목                                  |
| ![](media/Utilities/image9.gif) | 선택적 항목. 여러 항목이 허용된다. 각 반복 앞부분에 콤마가 와야 한다. |

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어 설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                         | 예제                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]          | 선택 항목을 표시                                             | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시        | { ENABLE \| DISABLE \| COMPILE }                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                    | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략을 표시           | SQL\> SELECT ename FROM employee; ENAME ------------------------ SWNO HJNO HSCHOI . . . 20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이외의 기호들                             | EXEC :p1 := 1; acc NUMBER(11,2);                             |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치 지정자 | SELECT \* FROM *table_name*; CONNECT userID/password;        |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 칼럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드       | DESC SYSTEM_.SYS_INDICES_;                                   |

### 관련 자료

자세한 정보를 위하여 다음 문서 목록을 참조하기 바란다.

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   iSQL User’s Manual

-   iLoader User's Manual

### Altibase는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음 버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께 고객서비스포털(*http://support.altibase.com/kr/* )로 보내주시기 바랍니다.

-   사용 중인 매뉴얼의 이름과 버전

-   매뉴얼에 대한 의견

-   사용자의 성함, 주소, 전화번호

이 외에도 Altibase 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인 문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인 부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를 요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.



1.aexport
=======

## aexport 소개

### 개요

aexport는 Altibase 데이터베이스 간의 자동화된 데이터 마이그레이션(migration)을 지원하기 위한 도구이다. aexport는 데이터베이스의 논리적인 구조 및 데이터를 텍스트로 저장하고, 이를 다시 새로운 Altibase 데이터베이스로 로딩하기 위한 스크립트를 자동으로 생성하여 준다.

aexport가 접속한 데이터베이스로부터 추출할 수 있는 객체 및 구성 요소는 데이터베이스 사용자, 사용자 권한, 테이블, 테이블스페이스, 테이블 제약조건, 인덱스, 뷰, Materialized View, 저장 프로시저, 시퀀스, 그리고 이중화 객체이다.

aexport는 데이터베이스의 논리적인 구조를 SQL 스크립트로 변환하여 저장하고, 모든 데이터를 텍스트로 내려 받기 때문에 상이한 Altibase 버전간, 그리고 상이한 플랫폼 간의 데이터 이동 시에 유용하게 사용될 수 있다. Altibase 서버는 구동했지만 서비스는 하지 않는 상태 즉, 클라이언트 연결이 없을 때 aexport를 사용하기를 권장한다.

### aexport 기능 소개

aexport가 추출할 수 있는 데이터베이스 객체 및 구성 요소는 다음과 같다.

-   데이터베이스 사용자

-   사용자 권한

-   롤(Role)

-   테이블스페이스

-   테이블

-   테이블 제약 조건

-   인덱스

-   뷰

-   Materialized View

-   저장 프로시저

-   이중화 객체

aexport를 수행하면 위에 열거한 데이터베이스 구성 요소를 생성하기 위한 SQL 스크립트와 이를 구동하기 위한 쉘 스크립트가 생성된다.

##### aexport 모드와 SQL 스크립트 파일

aexport는 데이터베이스의 어떤 부분을 추출하는지에 따라서 다른 모드로 실행할 수 있다. 모드는 aexport실행 시 커맨드 라인에서 지정할 수 있다.

aexport 실행 모드와 각 모드 별로 생성되는 SQL 스크립트 파일은 아래의 절에서 설명한다.

##### 전체 DB 모드

이 모드는 전체 데이터베이스를 추출한다. SYS 사용자만이 이 모드로 aexport를 실행할 수 있다.

이 모드로 aexport를 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   SYS_CRT_DIR.sql: 모든 디렉토리 객체 생성

-   SYS_CRT_USER.sql: 모든 사용자와 롤(Role) 생성

-   SYS_CRT_SYNONYM.sql: 모든 시노님(Synonym) 객체 생성

-   SYS_CRT_REP.sql: 모든 이중화 객체 생성

-   ALL_CRT_VIEW_PROC.sql: 모든 뷰와 프로시저 생성

-   ALL_CRT_TBS.sql: 모든 테이블스페이스 생성

-   ALL_CRT_TBL.sql: 모든 사용자 테이블 생성

-   ALL_CRT_INDEX.sql: 모든 사용자 인덱스 생성

-   ALL_CRT_FK.sql: 모든 사용자의 외래 키 생성

-   ALL_CRT_TRIG.sql: 모든 사용자의 트리거 생성

-   ALL_CRT_SEQ.sql: 모든 사용자의 시퀀스 생성

-   ALL_CRT_LINK.sql: 모든 사용자의 데이터베이스 Link 생성

-   ALL_EXE_STATS.sql: 모든 사용자의 테이블, 칼럼, 인덱스의 통계 정보 생성

-   ALL_REFRESH_MVIEW.sql: 모든 사용자의 Materialized View를 리프레쉬

-   ALL_ALT_TBL.sql : 모든 사용자의 테이블과 파티션에 대한 접근 모드를 변경

> 주의: 롤(Role)은 비스키마 객체이므로 전체 DB 모드에서만 추출할 수 있다.
>

##### 사용자 모드

이 모드는 옵션으로 지정하는 사용자가 소유한 모든 객체를 추출한다. SYS 사용자와 옵션으로 지정하는 사용자만이 이 모드로 aexport를 실행할 수 있다. 사용자 모드로 aexport를 실행하려면, -u 커맨드라인 옵션에 사용자 이름을 지정하면 된다.

이 모드로 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   {사용자명}_CRT_TBL.sql: 지정한 사용자의 모든 테이블 생성

-   {사용자명}_CRT_INDEX.sql: 지정한 사용자의 모든 인덱스 생성

-   {사용자명}_CRT_FK.sql: 지정한 사용자의 모든 외래 키 생성

-   {사용자명}_CRT_TRIG.sql: 지정한 사용자의 모든 트리거 생성

-   {사용자명}_CRT_SEQ.sql: 지정한 사용자의 모든 시퀀스 생성

-   {사용자명}_CRT_LINK.sql: 지정한 사용자의 모든 데이터베이스 Link 생성

-   {사용자명}_EXE_STATS.sql : 지정한 사용자의 모든 테이블, 칼럼, 인덱스의 통계 정보를 설정
    
-   {사용자명}_REFRESH_MVIEW.sql: 지정한 사용자의 모든 Materialized View를 리프레쉬
    
-   {사용자명}_ALT_TBL.sql : 지정한 사용자의 테이블과 파티션에 대한 접근 모드를 변경

##### 객체 모드

이 모드는 옵션으로 지정하는 모든 객체들을 추출한다. 객체 모드로 aexport를 실행하려면, -object 커맨드라인 옵션에 추출하고자 하는 객체들을 *user.object* 의 형태로 쉼표(“,”)로 분리 하여 명시하면 된다 (공백문자가 포함되면 안됨). SYS 사용자와 지정하는 객체의 소유자만이 이 모드로 aexport를 실행할 수 있다.

지정한 모든 객체의 소유자는 같아야 한다. 그러나, SYS 사용자로 실행할 때는 지정한 객체들의 소유자가 각각 다른 사용자여도 무방하다.

이 모드로 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   {사용자명}_{객체명}_CRT.sql: 지정한 사용자 객체 생성

-   {사용자명}_{객체명}_STATS.sql: 지정한 사용자 통계 정보 생성

##### 쉘 스크립트 파일

위에서 기술한 SQL 스크립트 파일 외에, aexport 수행 시 생성되는 쉘 스크립트 파일들은 다음과 같다.

-   run_il_in.sh: 데이터 로드 스크립트

-   run_il_out.sh: 데이터 다운로드 스크립트

-   run_is.sh: 스키마 생성 스크립트

-   run_is_con.sh: constraint 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일이 생성된다. 이 파일은 인덱스, 외래 키, 트리거, 및 이중화 객체를 생성하는 SQL 스크립트를 포함한다.
    
-   run_is_fk.sh: 외래키와 트리거 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_index.sh: 인덱스 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_repl.sh: 이중화 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_refresh_mview.sh: Materialized View를 refresh하는 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_alt_tbl.sh : 테이블과 파티션에 대한 접근 모드를 변경하는 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.

aexport 수행 후 생성된 쉘 스크립트를 대상 데이터베이스에 대해 실행하면, 데이터베이스의 논리적 구조가 자동으로 생성된다. 또한 기존의 데이터가 모두 대상 데이터베이스에 로딩된다. 쉘 스크립트는 Altibase iLoader를 사용하여 데이터 다운로드 및 업로드를 수행한다. 쉘 스크립트 내에서 iLoader를 사용하는 과정은 완전히 자동화되어 있기 때문에 사용자가 iLoader의 사용법에 익숙하지 않아도 사용이 가능하다.

aexport에 의해 생성된 모든 파일은 텍스트 파일이기 때문에 사용자의 필요에 따라 변경 후 사용이 가능하므로, 좀 더 유연하게 활용할 수 있다.

##### aexport 프로퍼티와 스크립트 파일

이 절은 aexport 프로퍼티 설정에 따라서 생성되는 스크립트 파일에 대해서 설명한다.

프로퍼티에 대한 상세한 설명은 “aexport 프로퍼티” 절을 참조한다.

-   INVALID_SCRIPT = ON 일 때, INVALID.sql 파일이 생성된다. 이 파일은 유효하지 않은 모든 뷰와 저장 프로시저를 생성하는 SQL 스크립트를 포함하는데, 이 파일을 실행하는 쉘 스크립트 파일은 생성되지 않는다.
    
-   TWO_PHASE_SCRIPT = ON 일 때, ALL_OBJECT.sql 파일과 ALL_OBJECT_CONSTRAINS.sql 파일이 생성된다. ALL_OBJECT.sql 파일은 모든 객체를 생성하는 SQL 스크립트를, ALL_OBJECT_CONSTRAINS.sql 파일은 모든 인덱스, 외래키, 트리거와 이중화 객체를 생성하는 SQL 스크립트를 포함한다. 또한, ALL_OBJECT_CONSTRATINS.sql을 실행하는 run_is_con.sh 쉘 스크립트 파일이 생성된다.

## 사전 설정

### DBMS_METADATA 패키지 설치

DBMS_METADATA 패키지는 데이터베이스 딕셔너리로부터 객체 생성 DDL 구문 또는 권한 GRANT 구문을 추출하는 기능을 제공한다. 

aexport는 DBMS_METADATA 패키지에 의존성을 가지기 때문에, aexport를 사용하기 위해서는 해당 패키지를 반드시 Altibase에 설치해야 한다. DBMS_METADATA 패키지가 설치되지 않은 Altibase를 대상으로 aexport를 수행하면 다음과 같은 에러가 발생한다.

```bash
$ aexport -s localhost -u sys -p manager
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 7.3.0.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[ERR-91144 : DBMS_METADATA package does not exist.]
```

> DBMS_METADATA 패키지에 대한 자세한 설명과 예제는 *Stored Procedures Manual*의 'Altibase 저장 패키지'를 참조하기 바란다.

### aexport 설정

aexport는 서버에 접속하기 위해서 다음과 같은 정보가 필요하다.

-   ALTIBASE_HOME  
    서버 혹은 클라이언트가 설치된 경로

-   server_name  
    Altibase 서버가 구동되어 있는 컴퓨터 서버의 이름(또는 IP 주소)

-   port_no  
    TCP 또는 IPC로 접속할 때 사용할 포트 번호

-   user_id  
    데이터베이스에 등록된 사용자 ID

-   Password  
    사용자 ID와 일치하는 암호

-   NLS_USE  
    데이터 검색 시, 사용자에게 보여주는 문자 집합

ALTIBASE_HOME은 환경 변수로 설정하도록 되어 있으며, 나머지는 커맨드 라인 옵션을 통해서 설정할 수 있다.(자세한 내용은 “aexport 사용방법”을 참고한다.)

aexport를 실행하려면 ALTIBASE_HOME 환경 변수와 aexport 설정 파일(aexport.properties)이 필요하다. 실행 전에 ALTIBASE_HOME이 바르게 설정되어 있어야 하며, 샘플로 제공되는 aexport.properties.sample 파일을 이용해 aexport용 설정 파일을 생성해 두어야 한다.

ALTIBASE_HOME은 일반적으로 서버가 설치될 때 자동으로 설정되는데 클라이언트의 경우에는 사용자가 직접 설정해야 한다. 설정되지 않았을 경우에는 제대로 동작하지 않을 수 있으므로 실행 전에 바르게 설정되어 있는지 확인할 것을 권장한다.

port_no와 NLS_USE는 환경 변수 또는 서버 설정 파일(altibase.properties)을 이용해서 설정할 수도 있다. 세 가지 방법으로 모두 설정되어 있을 경우 적용 우선 순위는 다음과 같다.

1.  커맨드 라인 옵션

2.  환경 변수 (ALTIBASE_PORT_NO, ALTIBASE_NLS_USE)

3.  서버 설정 파일(altibase.properties)

그러므로 설정된 값과 다른 옵션으로 연결하고자 할 경우, 커맨드 라인 옵션을 사용하면 서버 설정 파일이나 환경 변수를 변경하지 않아도 된다.

옵션이 설정되어 있지 않을 경우에는 aexport가 처음 실행될 때 옵션 입력 프롬프트를 띄우고 사용자에게서 해당 값을 입력 받는다. 이 때 바르지 않은 형식이나 유효하지 않은 값을 입력할 경우, aexport는 제대로 동작하지 않을 수 있다.

특히 NLS_USE 옵션은 사용자가 설정하지 않았더라도 실행시에 입력 프롬프트를 띄우지 않는다. 만약 사용자가 NLS_USE 옵션을 설정하지 않았다면 현재 데이터베이스의 캐릭터 셋을 이용해 접속을 시도한다. 이 때 데이터베이스의 문자집합이 데이터베이스 캐릭터 셋이 아닐 경우에는 올바로 실행되지 않거나 사용자 데이터가 일부 깨질 수 있으므로 반드시 NLS_USE를 사용 환경에 맞는 값으로 설정해야 한다.

원활한 aexport 사용을 위해 다음 환경 변수를 설정할 것을 권장한다.

-   ALTIBASE_HOME: 서버 혹은 클라이언트가 설치된 경로

-   ALTIBASE_PORT_NO: 서버에 접속할 때 사용할 포트 번호

-   ALTIBASE_NLS_USE: 데이터 검색 시, 사용자에게 보여주는 문자집합

-   PATH: 실행파일이 있는 경로인 \$ALTIBASE_HOME/bin 추가

### 환경변수

##### ALTIBASE_HOME

패키지가 설치된 디렉토리를 설정한다. aexport 사용을 위해 반드시 설정해야 하는 환경변수이다.

##### ALTIBASE_PORT_NO

접속할 서버의 포트 번호를 설정하는 환경 변수이다. -PORT 옵션 또는 altibase.properties를 통해서 지정할 수도 있다.

포트 번호 설정의 우선순위는 -PORT 옵션, 환경 변수 ALTIBASE_PORT_NO, altibase.properties 순이며 설정되지 않았을 경우에는 포트 번호 입력 프롬프트가 출력된다.

##### ALTIBASE_SSL_PORT_NO

aexport가 SSL/TLS 통신으로 접속할 서버의 포트 번호이다.

SSL 포트 번호 설정의 우선 순위는 -PORT 옵션, 환경변수 ALTIBASE_SSL_PORT_NO, altibase.properties 파일 내의 프로퍼티 순이다. 만약 아무것도 설정되지 않았을 경우에는 포트 번호 입력 프롬프트가 출력된다.

##### ALTIBASE_NLS_USE

서버에 연결할 때 사용할 캐릭터 셋을 설정한다. -NLS_USE 옵션 또는 altibase.properties를 통해서 지정할 수도 있다.

NLS_USE 설정의 우선순위는 -NLS_USE 옵션, 환경 변수 ALTIBASE_NLS_USE, altibase.properties 순이며 설정되지 않았을 경우에는 데이터베이스 캐릭터 셋을 사용한다.

>주의: 서버 캐릭터 셋과 ALTIBASE_NLS_USE에 설정한 값이 다를 경우에는 정상적으로 동작하지 않을 수 있다. 반드시 적절한 값을 설정할 것을 권장한다.

##### ALTIBASE_UT_FILE_PERMISSION

aexport, iLoader, iSQL이 생성하는 파일들의 권한을 설정하는 공통 환경변수이다.  값을 설정하지 않으면 666 ( user:rw,  group:rw,  other: rw)로 설정된다.

예) user:rw,  group:--,  other:--로 설정하는 경우, export ALTIBASE_UT_FILE_PERMISSION=600

ISQL_FILE_PERMISSION, AEXPORT_FILE_PERMISSION, 또는 ILO_FILE_PERMISSION이 설정된 경우,  ALTIBASE_UT_FILE_PERMISSION 환경 변수 보다 우선 처리된다.

예)export ALTIBASE_UT_FILE_PERMISSION=660; export ISQL_FILE_PERMISSION=600;
iSQL에서 생성되는 파일의 권한은 ISQL_FILE_PERMISSION=600이 우선처리되어 user:rw,  group:--,  other:--으로 설정된다.  aexport, iloader가 생성하는 파일의 권한은  ALTIBASE_UT_FILE_PERMISSION=660에 따라 user:rw,  group:rw,  other:--으로 설정된다.

##### AEXPORT_FILE_PERMISSION

aexport가 생성하는 파일 권한을 설정하는 환경 변수이다. 값을 설정하지 않으면 666 ( user:rw,  group:rw,  other: rw)로 설정된다.

예) user:rw,  group:--,  other:--로 설정하는 경우,  export AEXPORT_FILE_PERMISSION=600 

## aexport 사용 방법

### 구문

![](media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04595" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="574" image_path_raw="media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif" image_class="C" format="bnf" verified="True" -->
```bnf
aexport ::=
    AEXPORT
        { -h
        | -s server_name
        | -u user_name
        | -p password
        | -port port_no
        | -tserver server_name
        | -tport port_no
        | -nls national_language_support
        | -object user_name '.' object_name { ',' user_name '.' object_name }
        | -prefer_ipv6
        | -ssl_ca CA_file_path
        | -ssl_capath CA_dir_path
        | -ssl_cert certificate_file_path
        | -ssl_key key_file_path
        | -ssl_verify
        | -ssl_cipher cipher_list }
```
<!-- IMG_RECOVERY_END ref_id="img-04595" -->


### 파라미터

| 파라미터                           | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| \-h                                | 도움말을 출력한다.                                           |
| \-s                                | 데이터를 다운로드할 서버의 호스트 명 또는 IP 주소를 설정한다. 생략시 호스트 명 입력 프롬프트가 출력된다. IP 주소의 경우, IPv4 주소 또는 IPv6 주소를 사용할 수 있다. IPv6 주소는 “[“과 “]”로 에워싸야 한다. 예를 들어, localhost 를 명시하고자 할 때, 가능한 값은 다음과 같다. localhost (호스트 이름), 127.0.0.1 (IPv4주소), [::1] (IPv6주소) Altibase에서 IPv6 주소를 사용하는 방법에 대해서는 *Administrator’s Manual*을 참고하기 바란다. |
| \-u                                | 접속할 Altibase의 사용자명을 설정한다. 생략 시 사용자명 입력 프롬프트가 출력된다. 전체 DB 모드로 실행하려면, 이 옵션에 SYS 사용자를 지정해야 한다. 사용자 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다. -u \\"user name\\" |
| \-p                                | 접속할 Altibase 사용자의 패스워드를 설정한다. 생략시 패스워드 입력 프롬프트가 출력된다. |
| \-port                             | 접속할 Altibase의 포트번호를 설정한다. 생략 시 환경 변수 ALTIBASE_PORT_NO, altibase.properties를 차례로 참조하며 설정되어 있지 않은 경우에는 포트 번호 입력 프롬프트가 출력된다. |
| \-object                           | 추출할 객체를 소유자 이름과 함께 명시한다. 추출할 객체 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다. -object \\"user name\\".\\"table name\\" |
| \-tserver                          | 추출한 데이터를 업로드할 대상 서버를 지정한다. 이 정보는 aexport가 생성하는 쉘 스크립트 파일 안에 사용된다. -s 옵션과 마찬가지로 호스트 이름, IPv4 주소 또는 IPv6 주소 모두 가능하다. |
| \-tport                            | 접속할 대상 서버의 포트번호를 설정한다. 이 정보는 aexport가 생성하는 쉘 스크립트 파일 안에 사용된다. |
| \-nls_use                          | 데이터베이스에 데이터 저장 또는 데이터 추출 시에 사용되는 클라이언트 캐릭터 셋을 지정한다 (US7ASCII, KO16KSC5601, MS949, BIG5, GB231280, MS936, UTF8, SHIFTJIS, MS932, EUCJP). 생략 시 환경 변수 ALTIBASE_NLS_USE, altibase.properties를 차례로 참조하며, 설정되지 않았을 경우에는 데이터베이스 캐릭터 셋을 사용한다. |
| \-prefer_ipv6                      | \-s 옵션으로 호스트 이름을 입력했을 때, 접속할 IP 주소의 버전을 결정하는 옵션이다. 이 옵션을 명시하면, 호스트 이름을 IPv6 주소로 바꾸어 접속한다. 이 옵션을 명시하지 않으면, isql은 IPv4 주소로 접속한다. 선호하는 버전의 IP 주소로의 접속이 실패하면, 다른 IP 버전 주소로 접속을 다시 시도한다. 예를 들어, -S 옵션에 “localhost”를 입력하고 이 옵션을 명시하면, isql 은 처음에 IPv6 주소인 [::1]로 접속하고, 이 접속이 실패하면 IPv4 주소인 127.0.0.1로 접속을 다시 시도한다. |
| \-ssl_ca *CA_file_path*            | 접속할 Altibase 서버의 공개키(public key)가 포함된 CA(인증 기관, Certification Authority) 인증서 파일의 위치를 지정한다. |
| \-ssl_capath *CA_dir_path*         | 접속할 Altibase 서버의 공개키가 포함된 CA 인증서 파일이 저장되어 있는 디렉토리를 지정한다. |
| \-ssl_cert *certificate_file_path* | 클라이언트 인증서 파일의 위치를 지정한다.                    |
| \-ssl_key *key_file_path*          | 클라이언트 개인키 파일의 위치를 지정한다.                    |
| \-ssl_verify                       | 이 옵션을 지정하면 클라이언트가 서버로부터 전달받은 인증서를 검증한다. |
| \-ssl_cipher *cipher_list*         | SSL 암호화를 위해 사용할 알고리즘의 이름 후보들을 지정한다. General Reference에서 SSL_CIPHER_LIST 프로퍼티를 참고한다. |

> SSL 접속에 대한 자세한 설명과 예제는 *iSQL User's Manual*의 '접속 연결 및 해제'를 참조하기 바란다.



### 수행 절차

aexport를 사용한 데이터베이스 마이그레이션 절차는 크게 다음과 같이 분류된다.

-   원본 데이터베이스로부터 구조 추출

-   원본 데이터베이스로부터 데이터 추출

-   대상 데이터베이스에 데이터베이스 구조 생성

-   대상 데이터베이스에 데이터 로딩

-   대상 데이터베이스에 Materialized View를 리프레쉬한 다음, 인덱스와 외래키 생성, 접근 모드 변경

##### 데이터베이스 구조 추출

aexport를 사용하여 데이터베이스 구조를 추출한다.

- aexport를 수행한다.

  ```
  $ aexport –s 127.0.0.1 –u sys –p manager
  ```


-   Altibase 데이터베이스 사용자의 암호를 입력한다. (대상 데이터베이스에서 각 사용자가 사용하게 될 암호)
    
- 원격지에 있는 Altibase의 데이터를 aexport를 이용하여 백업을 할 때에는 원격지 서버의 주소와 포트(PORT)를 명시한다.
  
  ```
  $ aexport –s 222.112.84.200 –port 20300 –u sys –p manager
  ```


##### 데이터 추출

aexport에 의하여 생성된 쉘 스크립트를 실행하여 테이블 데이터를 추출한다.

-   현재 작업중인 디스크에 충분한 공간이 있는지 확인한다. 텍스트 데이터의 경우 데이터베이스 내부 자료 형태보다 더 많은 용량을 차지할 수 있기 때문에 데이터 파일 사이즈의 두 배 가량의 여유공간 확보를 권장한다.
    
- "run_il_out.sh" 스크립트를 수행한다.

  ```
  $ sh run_il_out.sh
  ```


##### 대상 데이터베이스에 데이터베이스 구조 생성

-   aexport와 “run_il_out.sh”에 의해 생성된 모든 SQL 스크립트와 쉘 스크립트, 그리고 확장자가 “fmt”, “log”, “dat”인 파일을 대상 데이터베이스가 존재하는 시스템으로 복사한다. 대상 데이터베이스가 동일한 시스템에 존재하는 경우 이 과정은 생략한다.
    
-   대상 데이터베이스를 구동시킨다.

-   “run_is.sh” 스크립트를 수행한다.

\$ sh run_is.sh

-   iSQL로 데이터베이스에 접속하여 데이터베이스 구조가 올바르게 생성되었는지 확인한다. 만약, 데이터베이스 구조가 올바르게 생성되지 않았다면, run_is.sh 수행 당시의 화면출력을 검사하여 문제를 파악한다.

##### 대상 데이터베이스에 데이터 로딩

- “run_il_in.sh” 스크립트를 수행한다.

  ```
  $ sh run_il_in.sh
  ```


-   ‘run_il_in.sh’ 디렉토리에서 확장자가 “bad”인 파일들 중 사이즈가 0이 아닌 파일이 있는지 검사한다. 해당 파일이 있을 경우 해당 테이블에 관련된 log 파일 및 bad 파일의 내용을 검사하여 조치한다. 이에 관련된 자세한 사항은 *iLoader User’s Manual*을 참조한다.

##### 대상 데이터베이스에 Materialized View를 리프레쉬한 다음, 인덱스 및 외래키 생성, 접근 모드 변경

TWO_PHASE_SCRIPT 프로퍼티가 OFF일 때,

- “run_is_refresh_mview.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_refresh_mview.sh
  ```


- “run_is_index.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_index.sh
  ```


- “run_is_fk.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_fk.sh
  ```


- “run_is_alt_tbl.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_alt_tbl.sh
  ```


TWO_PHASE_SCRIPT 프로퍼티가 ON일 때,

- “run_is_con.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_con.sh
  ```




### 주의 사항

-   SYS 사용자가 아닌 일반 사용자로 aexport를 실행할 경우 해당 사용자가 생성한 스키마에 대해서만 스크립트를 생성한다.
    
-   SYS 사용자가 아닌 일반 사용자로 aexport를 실행할 경우 이중화 객체는 생성되지 않는다.
    
-   일반 사용자로 aexport를 실행할 경우 테이블 생성 권한이 필요하다. aexport는 객체간 의존성 분석을 위해 임시 테이블을 생성하기 때문이다.
    
-   동시에 여러 개의 aexport 프로세스를 실행하면 안 된다. aexport는 생성된 SQL 스크립트를 저장하기 위해 임시 테이블을 사용하기 때문에, 동시에 두 개 이상의 aexport 프로세스를 실행하면 예상치 못한 결과가 나올 수 있다.
    
-   EXECUTE와 TWO_PHASE_SCRIPT 프로퍼티를 ON 으로, OPERATION 프로퍼티를 IN으로 설정하고 데이터를 업로딩할 때는, INDEX 프로퍼티 값의 영향을 받지 않는다. 이는 인덱스만 생성하는 SQL 스크립트가 따로 생성되지 않기 때문이다.  
    그러므로 INDEX 프로퍼티를 ON으로 업로딩 작업 (EXECUTE=ON and OPERATION=IN)을 하려면, TWO_PHASE_SCRIPT 프로퍼티를 OFF로 해야 한다.
    
-   “run_is.sh” 스크립트 구동 시 기존에 있는 모든 사용자 및 객체를 삭제하므로, 소스 데이터베이스에서 해당 스크립트를 수행하지 않도록 주의해야 한다.
    
- 파라미터 -s, -p는 일반적으로 서버에 접속하기 위한 용도뿐 아니라 스크립트에서도 함께 사용된다. 그러나 -tserver, -tport와 함께 사용될 경우에는 –s와 –p는 데이터를 다운로드 할 서버에 접속하는 용도로만 사용되고, 대상 데이터베이스에 대해 수행할 스크립트에는 –tserver와 –tport로 명시한 값들이 사용된다.
  
  ```
  $ aexport -s 127.0.0.1 -u sys -p manager -tserver 192.168.1.10 –tport 21300
  
  $ cat run_il_in.sh
  
  iloader -s 192.168.1.10 -port 21300 -u SYS -p MANAGER in -f SYS_T1.fmt -d
  SYS_T1.dat -log SYS_T1.log -bad SYS_T1.bad
  ```


-   사용자 생성 시 PASSWORD_VERIFY_FUNCTION을 사용해서 콜백 함수를 지정했다면, 사용자를 import 하기 전에 사용자의 패스워드를 검증 함수에 부합하도록 설정해야 한다. 또한 대상 데이터베이스에 사용자를 import 하기 전에 검증 함수를 먼저 import 해야 한다.
    
-   사용자 이름 또는 추출할 객체 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다.



### aexport의 한계

-   저장 프로시저 생성 시 참조해야 할 저장 프로시저가 미리 생성되어 있지 않으면 작업이 실패하게 된다. aexport는 저장 프로시저 간의 의존성에 대한 정보에 접근할 수가 없기 때문에 저장 프로시저 생성 순서를 보장할 수 없다. 이런 경우 저장 프로시저 생성에 실패할 수 있기 때문에 대상 데이터베이스에 저장 프로시저를 수동으로 생성해야 한다.
    
-   aexport는 시퀀스의 메타 정보에 제한적인 접근만이 가능하다. 이러한 제약 때문에 SYS 사용자 이외의 계정에서 생성한 시퀀스의 경우 INCREMENT BY에 의해서 지정된 시퀀스 특성만 반영이 되고 나머지 특성은 기본 값으로 설정된다. 이러한 제약사항이 문제가 되는 경우 시퀀스를 대상 데이터베이스에 수동으로 생성해야 한다.
    
-   대상 데이터베이스에 객체를 생성하는 과정에서, Material View 생성 전에 기반 테이블이 미리 생성되어 있어야 한다. aexport는 materialized view 생성을 위한 테이블 생성 순서를 보장하지 않기 때문에, materialized view 생성에 실패할 수도 있다. 이 경우, 사용자가 수동으로 materialized view를 생성해야 한다.
    
-   aexport 가 원본 데이터베이스에서 materialized view 생성 구문을 추출할 때, 최초로 그 materialized view를 생성했던 구문을 가져온다. 즉, 원본 데이터베이스에서 materialized view에 대해서 refresh 방법 또는 refresh 변경 시기를 변경하는 DDL문을 수행하더라도 aexport가 추출하는 구문에는 해당 변경사항이 반영되지 않는다.



### SSL 접속과 스크립트 파일

-   SSL 접속으로 aexport를 실행하는 경우, 원본 데이터베이스 접속용 스크립트(run_il_out.sh) 파일에는 aexport를 실행할 때 사용한 SSL 옵션이 그대로 적용된다.
    
-   대상 데이터베이스에 SSL 접속을 원한다면 프로퍼티 파일에 SSL 관련 프로퍼티를 설정해야 한다. 자세한 설명은 aexport 프로퍼티 절의 SSL_ENABLE 프로퍼티를 참조하기 바란다.




### aexport 프로퍼티

##### aexport 프로퍼티 설정

aexport.properties 파일의 프로퍼티 값을 조정해야 한다. 이 파일은 \$ALTIBASE_HOME/conf 디렉터리에 있어야 한다 (같은 디렉터리의 altibase.properties 파일과 혼동하지 말 것). 이 파일이 없으면 aexport는 구동되지 않는다.

Altibase를 설치할 때, aexport.properties 파일은 \$ALTIBASE_HOME/conf에 존재하지 않는다. 다만, 같은 디렉터리에 aexport.properties.sample이라는 이름의 샘플 파일을 제공하는데, 이 파일을 aexport.properties이름으로 복사한 후, 수정해서 사용하면 된다.

##### aexport 프로퍼티

-   OPERATION  
    OPERATION = IN/OUT  
    OUT으로 설정할 경우, 모든 스키마와 데이터를 추출할 수 있는 스크립트가 생성된다. 데이터 추출 스크립트(iLoader 실행 명령어로 구성)를 실행하면 form 파일(.fmt)과 데이터 파일(.dat)이 만들어진다.  
    IN으로 설정할 경우, OUT에서 생성된 스키마 생성 스크립트와 데이터 로딩 스크립트를 실행하여 대상 데이터베이스에 스키마를 만들고 데이터를 입력한다. 스키마 생성 스크립트와 데이터 입력 스크립트는 aexport를 실행하지 않고 쉘 프롬프트에서 수동으로 실행할 수도 있다.
    
-   EXECUTE  
    생성한 스크립트를 자동으로 수행할 것인지 여부를 설정한다.  
    EXECUTE = ON/OFF  
    ON일 경우 OPERATION 에 지정된 작업에 맞는 적절한 스크립트 파일을 자동으로 실행한다. 스크립트 파일 이름은 ILOADER_OUT, ILOADER_IN, ISQL, ISQL_CON, ISQL_INDEX, ISQL_FOREIGN_KEY, ISQL_REPL, ISQL_REFRESH_MVIEW, 그리고 ISQL_ALT_TBL 프로퍼티로 설정된다.  
    OFF일 경우 스크립트를 생성하기만 하고 실행하지는 않는다.
    
-   INVALID_SCRIPT  
    이 프로퍼티는 유효하지 않은 객체들을 생성하는 SQL 스크립트를 하나의 스크립트 파일에 모을 것인지 여부를 결정한다.  
    INVALID_SCRIPT = ON/OFF  
    ON 일 때, INVALID.sql 파일이 생성된다. 이 파일은 유효하지 않은 뷰와 저장 프로시저를 생성하는 모든 SQL 스크립트를 포함한다.  
    OFF이면, 유효하지 않은 각 객체를 생성하는 SQL 스크립트가 따로 생성된다. 즉, 유효한 객체와 같은 방식으로 다뤄진다.
    
-   TWO_PHASE_SCRIPT  
    이 프로퍼티는 객체 생성 스크립트를 두 개의 스크립트 파일로 나눠서 생성할 것인지를 결정한다.  
    TWO_PHASE_SCRIPT = ON/OFF  
    ON 일 때, 아래와 같이 두 개의 SQL 스크립트 파일과 두 개의 쉘 스크립트 파일만이 생성된다: ALL_OBJECT.sql, ALL_OBJECT_CONSTRAINS.sql, ALL_OBJECT.sql, run_is.sh, run_is_con.sh  
    OFF이면, 각 객체를 생성하는 SQL 스크립트 파일을 따로 생성한다.
    
-   CRT_TBS_USER_MODE  
    CRT_TBS_USER_MODE = ON/OFF (기본값: OFF)  
    사용자 모드에서 테이블스페이스 생성 구문을 추출할 것인지 여부를 결정한다.  
    이 프로퍼티를 ON으로 설정하면, 사용자 모드에서 해당 사용자와 관련된 테이블스페이스를 생성하는 SQL문을 추출한다. 사용자 관련 테이블스페이스는 기본 테이블스페이스, 기본 임시 테이블스페이스, 접근 가능 여부가 설정된 테이블스페이스이다.
    
-   INDEX  
    INDEX = ON/OFF  
    대상 데이터베이스에 스키마 구성 시 인덱스 포함여부를 결정한다. 데이터 로딩 후에 인덱스를 생성하고자 할 경우 이 프로퍼티를 ON으로 설정한다. TWO_PHASE_SCRIPT프로퍼티는 OFF일 때 제대로 동작한다.
    
-   USER_PASSWORD  
    USER_PASSWORD = *password*  
    원본 데이터베이스에서 추출된 사용자를 대상 데이터베이스에 생성할 때 사용할 암호를 지정한다. (aexport는 사용자 객체 추출 시 사용자의 암호를 알 수 없기 때문에 수동 설정이 필요하다.) 이 프로퍼티가 설정되어 있지 않을 경우 각 사용자의 암호를 묻는 프롬프트가 나타난다.
    
-   VIEW_FORCE  
    VIEW_FORCE = ON/OFF  
    ON이면, 뷰의 기본 테이블 등이 존재하지 않아도 뷰를 강제로 생성한다.
    
-   DROP  
    생성 스크립트 내부에 DROP 구문을 포함할 것인지 여부를 결정한다.  
    DROP = ON/OFF  
    ON이면, 객체를 제거하는 구문이 SQL 스크립트에 포함되어 대상 데이터베이스 내에 이미 객체가 존재할 경우 기존 객체를 제거하게 된다. 기존 객체를 삭제하기 때문에 사용에 주의를 요한다.  
    
    > 주의: 객체 모드로 실행하면, 이 프로퍼티 값에 상관없이 DROP 구문이 생성되지 않는다.
    
-   ILOADER_OUT  
    ILOADER_OUT = *run_il_out.sh*  
    원본 데이터베이스에서 데이터를 추출하기 위해 생성되는 쉘 스크립트 파일명을 설정한다. OPERATION 프로퍼티를 OUT으로 설정할 경우에 사용된다.
    
-   ILOADER_IN  
    ILOADER_IN = *run_il_in.sh*  
    대상 데이터베이스에 데이터 로딩을 위해 사용될 쉘 스크립트의 파일명을 설정한다.
    
-   ISQL  
    ISQL = *run_is.sh*  
    대상 데이터베이스에 데이터베이스 스키마를 구성하기 위한 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다.
    
-   ISQL_CON  
    ISQL\_ CON = *run_is_con.sh*  
    대상 데이터베이스에 인덱스, 외래키, 트리거와 이중화 객체를 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. TWO_PHASE_SCRIPT 프로퍼티가 ON일 때 사용된다.
    
-   ISQL_INDEX  
    ISQL_INDEX = *run_is_index.sh*  
    대상 데이터베이스에 인덱스를 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   ISQL_FOREIGN_KEY  
    ISQL\_ FOREIGN_KEY = *run_is_fk.sh*  
    대상 데이터베이스에 외래키 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   ISQL_REPL  
    ISQL_REPL = *run_is_repl.sh*  
    대상 데이터베이스에 이중화를 생성하기 위한 쉘 스크립트의 파일명을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   COLLECT_DBMS_STATS  
    이 프로퍼티는 사용자의 테이블, 칼럼, 인덱스의 통계 정보를 추출할지 여부를 결정한다.  
    COLLECT_DBMS_STATS = ON/OFF  
    기본값은 OFF이며 통계 정보를 추출하지 않는다. 이 프로퍼티의 값을 ON으로 할 경우 통계 정보를 추출하도록 한다.
    
-   ISQL_REFERSH_MVIEW  
    ISQL_REFERSH_MVIEW = *run_is_refresh_mview.sh*  
    대상 데이터베이스의 Materialized View를 리프레쉬하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면, 쉘 스크립트 파일이 생성되지 않는다.
    
-   ISQL_ALT_TBL  
    ISQL_ALT_TBL = *run_is_alt_tbl.sh*  
    대상 데이터베이스의 테이블과 파티션에 대한 접근 모드를 변경하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면, 쉘 스크립트 파일이 생성되지 않는다.
    
-   ILOADER_FIELD_TERM  
    ILOADER_FIELD_TERM = *field_term*  
    테이블의 데이터를 텍스트로 다운로드 할 때 사용할 필드 구분자를 설정한다. 설정하지 않을 경우 기본값은 쉼표(,)로 구분되며, 숫자는 그대로, 문자형 칼럼은 큰 따옴표(“”)로 에워싸여서 출력된다.  
    
    > 주의: 프로퍼티 파일 내에서 \# 문자를 구분자로 사용할 경우, \# 이하를 주석으로 처리하기 때문에, \#는 구분자로 사용할 수 없다.
    
-   ILOADER_ROW_TERM  
    ILOADER\_ ROW \_TERM = *row_term*  
    테이블 데이터를 텍스트로 내릴 때 사용할 레코드 구분자를 설정한다. 설정하지 않을 경우 기본값은 \<LF\>이다.  
    
    > 주의: 프로퍼티 파일 내에서 \# 문자를 구분자로 사용할 경우, \# 이하를 주석으로 처리하기 때문에, \#는 구분자로 사용할 수 없다.
    
- ILOADER_PARTITION  

  이 프로퍼티는 원본 데이터베이스에 파티션 테이블이 있을 경우, iLoader 스크립트를 파티션 별로 생성할 것인지 결정한다.  
  ILOADER\_PARTITION = ON/OFF  

  이 값이 ON일 경우, run_il_out.sh에 각 파티션마다 form 파일과 데이터를 추출하는 스크립트가 생성된다. run_il_in.sh에도 파티션 별로 데이터를 로드하는 스크립트가 생성된다. 
  이 값이 OFF일 경우, 파티션드 테이블을 처리하는 스크립트도 넌파티션드 테이블과 동일하게 하나의 데이터 파일을 이용하여 추출·입력하도록 생성된다.
  ILOADER 관련 프로퍼티에 대한 더 자세한 설명은 *iLoader User’s Manual* 을 참고하기 바란다.

-   ILOADER_ERRORS  
    ILOADER_ERRORS = *count* (기본값: 50)  
    iLoader로 데이터를 업로드할 때 허용 가능한 최대 에러 개수를 지정한다. 이 프로퍼티의 기본값은 50이며, 0으로 설정하면 발생하는 에러 개수와 무관하게 업로드가 계속 실행된다.
    
-   ILOADER_ARRAY  
    ILOADER_ARRAY = *count* (기본값: 1)  
    iLoader로 데이터를 다운로드 또는 업로드 할 때 한 번에 처리할 row 개수를 지정한다.
    
-   ILOADER_COMMIT  
    ILOADER_COMMIT = *count* (기본값: 1000)  
    iLoader로 데이터를 업로드할 때 커밋할 단위(개수)를 지정한다. 이 프로퍼티로 -commit옵션의 값을 지정할 수 있다.
    
-   ILOADER_PARALLEL  
    ILOADER_PARALLEL = *count* (기본값: 1)  
    iLoader로 데이터를 다운로드 또는 업로드 할 때 병렬로 처리할 쓰레드 개수를 지정한다.
    
-   ILOADER_ASYNC_PREFETCH  
    ILOADER_ASYNC_PREFETCH = OFF\|ON\|AUTO (기본값 OFF)  
    iLoader로 데이터를 다운로드할 때 비동기 prefetch 동작을 설정한다. 자세한 설명은 iLoader User's Manual의  '-async_prefetch' 옵션을 참고하기 바란다.
    
-   SSL_ENABLE  
    대상 데이터베이스에 SSL 프로토콜로 접속할 것인지 여부를 지정한다.  
    SSL_ENABLE = ON/OFF  
    ON이면 대상 데이터베이스에 실행하는 쉘 스크립트(run_is.sh, run_il_in.sh) 내의 isql, iloader 명령에 SSL 관련 옵션이 지정된다.  
    SSL 관련 옵션 값은 프로퍼티(SSL_CA, SSL_CAPATH, SSL_CERT, SSL_KEY, SSL_CIPHER, SSL_VERIFY)로 명시할 수 있다. 각 프로퍼티의 역할은 aexport 접속 파라미터와 동일하므로 해당 절을 참조한다. SSL_ENABLE 프로퍼티 설정에 대한 예제는 SSL 프로퍼티 설정을 참고한다.
    
-   ILOADER_GEOM = WKB
    iLoader로 공간 데이터를 다운로드 할 때, 공간 데이터를 Well-Known Binary (WKB)  포맷으로 처리하도록 지정하는 옵션이다. run_il_out.sh 파일에 -geom WKB 옵션이 추가된다.



### 사용 예제

##### 전체 DB 모드로 실행

```
$ aexport -s 127.0.0.1 -u sys -p manager
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.3.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TBS #####
##### USER  #####
##### SYNONYM #####
##### DIRECTORY #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
##### REPLICATION #####
##### JOB #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
ALL_ALT_TBL.sql 
ALL_CRT_DIR.sql
ALL_CRT_FK.sql
ALL_CRT_INDEX.sql
ALL_CRT_JOB.sql
ALL_CRT_LIB.sql
ALL_CRT_LINK.sql
ALL_CRT_REP.sql
ALL_CRT_SEQ.sql
ALL_CRT_SYN.sql
ALL_CRT_TBL.sql
ALL_CRT_TBS.sql
ALL_CRT_TRIG.sql
ALL_CRT_USER.sql
ALL_CRT_VIEW_PROC.sql
ALL_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh
```



##### 사용자 모드로 실행

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
$ aexport -s 127.0.0.1 -u user1 -p user1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.3.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### USER #####
##### SYNONYM #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
USER1_ALT_TBL.sql
USER1_CRT_DIR.sql
USER1_CRT_FK.sql
USER1_CRT_INDEX.sql
USER1_CRT_LIB.sql
USER1_CRT_LINK.sql
USER1_CRT_SEQ.sql
USER1_CRT_SYN.sql
USER1_CRT_TBL.sql
USER1_CRT_TRIG.sql
USER1_CRT_USER.sql
USER1_CRT_VIEW_PROC.sql
USER1_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh

```



##### 객체 모드로 실행

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
iSQL> CONNECT user1/user1;
iSQL> CREATE TABLE t1(i1 INTEGER);
Create success.
iSQL> CREATE VIEW v1 AS SELECT i1 FROM t1;
Create success.
iSQL> CREATE MATERIALIZED VIEW m1 AS SELECT * FROM t1;
Create success.
iSQL> CREATE OR REPLACE PROCEDURE proc1(p1 IN INTEGER)
AS a INTEGER;
BEGIN
SELECT * INTO a FROM t1 WHERE i1 = 1;
END;
/
Create success.

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.3.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
$ ls
user1_t1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.m1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.3.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### MATERIALIZED VIEW #####
$ ls
user1_m1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1,user1.v1,user1.proc1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.3.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
##### VIEW #####
##### STORED PROCEDURE #####
$ ls
user1_proc1_CRT.sql
user1_t1_CRT.sql
user1_v1_CRT.sql

```



##### SSL 프로퍼티 설정

```
SSL_ENABLE = ON  # OFF
SSL_CA     = ${ALTIBASE_HOME}/cert/ca-cert.pem
#SSL_CAPATH = ${ALTIBASE_HOME}/cert
SSL_CERT   = ${ALTIBASE_HOME}/cert/client-cert.pem
SSL_KEY    = ${ALTIBASE_HOME}/cert/client-key.pem
SSL_CIPHER = RC4-SHA:RC4-MD5
SSL_VERIFY = ON  # OFF
```





# 2.altiComp

이 장은 altiComp 유틸리티의 기능을 소개하고, 불일치하는 데이터를 비교하고 일치시키는 기능 등을 설명한다.

## altiComp 소개

Altibase altiComp 유틸리티는 두 Altibase 간의 이중화 중에 발생한 데이터 불일치를 해결하기 위해 사용한다.

altiComp은 Altibase 데이터베이스를 또 다른 Altibase 데이터베이스와 테이블 단위로 비교, 검사하여 불일치 정보를 출력한다. 또한 불일치 데이터가 발생한 경우에는 두 데이터베이스를 일치시키는 기능도 제공한다.

### altiComp 용어

##### Master Server

두 서버 간의 불일치 레코드 발견 시 수정을 하는 기준이 되는 서버이다. altiComp 실행 시 어느 쪽 서버도 master로 지정될 수 있다.

##### Master DB

Master Server의 데이터베이스이다.

##### Slave Server

두 서버 간의 불일치 레코드 발견 시 기준 데이터베이스에 따라서 수정이 되는 쪽 서버이다. altiComp 실행 시 어느 쪽 서버도 slave로 지정될 수 있다.

##### Slave DB

Slave Server의 데이터베이스이다.

### 불일치 레코드(Different Record) 

Master DB의 지정 테이블과 Slave DB의 지정 테이블간에 주요 키(Primary Key)를 기준으로 칼럼 값이 일치하지 않는 레코드를 의미한다.

불일치 레코드가 발생하는 이유는 다음의 세 가지 경우이다.

-   MOSX 불일치: 특정 레코드가 주요 키를 기준으로 Master DB에는 있으나, Slave DB에는 없는 경우
    
-   MOSO 불일치: 특정 레코드가 주요 키를 기준으로 Master DB와 Slave DB에도 있지만, 레코드의 내용이 다른 경우
    
-   MXSO 불일치: 특정 레코드가 주요 키를 기준으로 Master DB에는 없고, Slave DB에는 있는 경우

### 일치 정책(Synchronization Policy) 

일치 정책은 불일치 레코드를 일치시키는 방법을 명시하는 정책이다. altiComp 프로그램은 기본적으로 Master DB를 기준 DB로 고정하고, Slave DB를 일치시키는 정책을 채택하고 있다.

Altibase는 일치 정책으로 다음과 같은 네 가지 방법을 제공한다.

-   SU 정책: MOSO 불일치를 해소하는 정책으로, Master DB의 레코드 내용으로 Slave DB를 변경(update)한다.
    ![](media/Utilities/su_policy.gif)
-   SI 정책: MOSX 불일치를 해소하는 정책으로, Master DB의 레코드를 Slave DB에 삽입(insert)한다.
    ![](media/Utilities/si_policy.gif)
-   MI 정책: MXSO 불일치를 해소하는 정책으로. Slave DB의 레코드를 Master DB에 삽입(insert)한다.
    ![](media/Utilities/mi_policy.gif)
-   SD 정책: MXSO 불일치를 해소하는 정책으로, Slave DB의 레코드를 삭제(delete)한다.

![](media/Utilities/sd_policy.gif)

SU정책, SI정책, MI정책, SD정책은 사용자가 altiComp 환경 파일을 사용하여 지정할 수 있다. 단, MI정책과 SD정책은 서로 배타적이므로, 동시에 지정할 수 없다는 것을 주의하라.

##### DIFF

Master DB와 Slave DB간의 이중화 작업에서 발생할 수 있는 불일치 레코드를 식별하여 실행 결과 파일로 생성하는 기능을 가진다.

##### SYNC

Master DB와 Slave DB 사이의 불일치 레코드를 식별하여 altiComp 환경 파일에 기술된 일치 정책에 따라 양방향으로 반영하여 불일치를 해소하고, 실행 요약정보와 에러 정보를 포함하는 실행 결과 파일을 생성한다.

##### altiComp 환경 파일

altiComp를 실행하기 위한 옵션을 지정하는 환경 파일이다. 이 파일은 연결정보, altiComp 기능 설정, 일치 정책 등의 내용을 포함한다.



## altiComp 사용 방법

이 절에서는 altiComp을 실행하기 위한 정보를 기술하는 altiComp 환경 파일을 먼저 설명하고, 비교(DIFF)와 일치(SYNC) 기능에 대해 설명한다.

### altiComp 실행 방법

altiComp 기능을 사용하기 위해서는 먼저 DIFF 또는 SYNC를 수행할 테이블에 대한 정보를 가지고 있는 altiComp 환경 파일을 만들어야 한다. altiComp 환경 파일은 운용 방법의 altiComp 환경 파일에서 설명한다.

altiComp 명령은 다음과 같은 형태를 갖는다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

현재 디렉토리가 /user/charlie/altibase_home/altiComp 라면

```
/user/charlie/altibase_home/altiComp> altiComp script_file_name
```

또는

```
/user/charlie/altibase_home/altiComp> altiComp  ./script_file_name
```



### altiComp 프로퍼티 설정

비교 또는 일치 작업의 내용을 기술하는 환경 파일로, 각각의 고유한 프로퍼티를 포함한다. 프로퍼티는 altiComp 유틸리티 실행에 필요한 정보를 기술한다. (\$ALTIBASE_HOME/ altiComp 디렉터리 밑에 제시된 sample.cfg 참조)

##### 설정 규칙

프로퍼티는 “**프로퍼티 이름 = 프로퍼티 값**”의 형식으로 구성되며, 대소문자 구분이 없다.

환경 파일은 다음과 같은 특별한 의미를 가지는 기호를 포함할 수 있다.

-   “ **\#** “ 기호는 주석(comment)으로 이후의 문자열은 무시된다.

-   “ **{ }** “ 기호는 프로퍼티 값을 여러 줄로 기술하기 위한 목적으로 사용된다.

-   “ **;** “ 기호는 여러 개의 값을 분리하기 위한 구분자 역할을 한다.

-   “ **“** “ 기호: 사용자 이름, 비밀번호 또는 테이블 이름, 칼럼 이름에 예약어 또는 특수 문자가 포함되어 있다면, 이 기호로 해당 문자열을 감싸준다. Altibase에서 특수 문자는 \~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \| 이다.

##### 프로퍼티 이름

공백이 없는 문자로 구성되며, 프로퍼티 그룹 내에서 식별하도록 하는 이름이다.

##### 프로퍼티 값

단일 값(single value), 다중 값(multi value) 또는 표현식(expression)을 가질 수 있다.

-   표현식은 공백이 가능하며, 대부분의 프로퍼티는 이 형태의 값을 가진다.
    예) TABLE = EMPLOYEE

-   다중 값은 “**;**” 분리자로 구분되는 여러 개의 단일 값을 가지며, 특히 여러 줄에 기술할 때는 “{ }” 기호 안에 값을 기술한다(예2). 다중 값이 허용되는 프로퍼티는 EXCLUDE 이다.
    예) EXCLUDE = ENO; DNO; ENAME 또는 EXCLUDE = {ENO; DNO; ENAME}
    
-   표현식은 공백을 포함한 문자열을 표현하기 위한 것이며, 반드시 “{ }” 기호 안에 기술되어야 한다. 표현식을 가지는 프로퍼티는 WHERE 이다.
    예) WHERE = { ENO \> ‘1000’ and ENO \< ‘2000’ }

##### 데이터 타입 지원

altiComp 대상에서 특정 칼럼을 제외시키려면 프로퍼티 EXCLUDE를 다음과 같이 사용한다.

예) EMP 테이블에 CLOB 칼럼이 존재할 때, 해당 칼럼을 altiComp 대상에서 제외한다.

TABLE = EMP
EXCLUDE = { CCC }



### 프로퍼티 옵션

altiComp 유틸리티는 아래의 프로퍼티로 Local Server와 Remote Server의 접속 정보 및 비교(DIFF) 작업, 일치(SYNC)작업, 불일치 레코드에 대한 일치 정책을 지정할 수 있다.

##### DB_MASTER

두 서버 간의 불일치 레코드 발견 시 데이터 수정의 기준으로 하려는 서버를 지정한다.

값은 사용자명, 패스워드, 서버의 IP 주소 또는 서버명, NLS_USE 를 지정한다. 각 프로퍼티의 값은 Altibase 홈 디렉터리의 프로퍼티 파일에 있는 정보와 일치하여야 한다.

- TCP 접속:

  ```
  DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=20300;NLS_USE=US7ASCII
  ```

-   SSL 접속:

    ```
    DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=${ALTIBASE_SSL_PORT_NO};NLS_USE=US7ASCII;CONNTYPE=6;SSL_CA=/home/altibase/cert/ca-cert.pem;SSL_CERT=/home/altibase/cert/client-ert.pem;SSL_KEY=/home/altibase/cert/client-key.pem
    ```


연결 문자열의 SSL 관련 속성은 SSL/TLS User's Guide를 참고하기 바란다.

##### DB_SLAVE

상대 서버를 지정한다.

값은 사용자명, 패스워드, 서버의 IP 주소 또는 서버명, NLS_USE 를 지정한다. 프로퍼티 값은 Altibase 홈 디렉터리의 프로퍼티 파일에 있는 정보와 일치하여야 한다.

##### OPERATION

비교 작업을 하는 경우에는 “DIFF”를, 일치 작업을 하는 경우에는 “SYNC”를 지정한다.

##### INSERT_TO_SLAVE

MOSX 불일치에 대한 SI정책을 지정. 해당 레코드의 Slave DB에 삽입(insert) 여부를 결정한다. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삽입하고, “OFF”이면 삽입하지 않는다.

##### INSERT_TO_MASTER

MXSO 불일치에 대한 MI정책을 지정. 해당 레코드의 Master DB에 삽입(insert) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삽입하고, “OFF”이면 삽입하지 않는다.

DELETE_IN_SLAVE 프로퍼티 값과 동시에 “ON”을 가질 수 없다.

##### DELETE_IN_SLAVE

MXSO 불일치에 대한 SD정책을 지정. 해당 레코드의 Slave DB에서 삭제(delete) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삭제하고, “OFF”이면 삭제하지 않는다.

INSERT_TO_MASTER 프로퍼티 값과 동시에 “ON”을 가질 수 없다.

##### UPDATE_TO_SLAVE

MOSO 불일치에 대한 SU정책을 지정. 해당 레코드의 Slave DB에서 수정(update) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 수정하고, “OFF”이면 수정하지 않는다.

##### CHECK_INTERVAL

테이블에 대하여 SYNC 작업을 한 후 다음 테이블의 SYNC 작업을 하기 전에 지정한 시간만큼 간격을 둔다. 단위는 MS(Millisecond)이다.

##### MAX_THREAD

운영하기 위한 쓰레드의 개수를 지정한다. 작업하려는 쓰레드의 개수를 제한 없이 사용하려면 “-1”을 명시한다.

##### COUNT_TO_COMMIT

변경된 데이터(Insert, Delete, or Update)를 몇 건 단위로 커밋할 것인가를 나타내는  단위 옵션이다. 기본값은 1000건 단위로 커밋한다.

##### FILE_MODE_MAX_ARRAY

이 값이 1보다 크면 작업 대상 테이블의 데이터를 파일에 저장한 후, 파일의 데이터에 대해서 SYNC 또는 DIFF 작업을 수행하게 된다. 이 값은 array fetch 하기 위한 array의 사이즈로 사용되고, altiComp는 지정한 값만큼의 레코드를 array fetch하여 csv 형식으로 파일에 저장한다.

이 옵션은 대용량의 테이블에 대한 altiComp 작업 성능을 향상시키기 위해 사용할 수 있으나, 대상 테이블에 LOB타입의 칼럼이 있으면 이 옵션을 사용해도 성능 향상이 미미할 수 있다.

이 옵션은 Altibase 서버간의 SYNC 또는 DIFF 작업 시에만 사용할 수 있다.

예) FILE_MODE_MAX_ARRAY = 1000

##### DIFF LOG 옵션

DIFF는 Master DB의 지정 테이블과 Slave DB의 지정 테이블간에 주요 키(Primary Key)를  기준으로 레코드 값을 비교하여 실행 결과 파일에 기록하는 작업이다. 네가지 유형의 레코드  비교 결과를 실행 결과 파일에 기록 여부를 설정할 수 있도록 각각의 프로퍼티를 제공한다.

프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 기록하고, “OFF”이면 기록 하지 않는다. 프로퍼티를 지정하지 않으면 기본값에 따라 동작한다.

1. ###### LOG_EQ_MOSO

   PK를 포함한 모든 칼럼의 값이 일치하는 레코드 (EQ_MOSO)를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "OFF"로 동작한다.
   
   이 옵션은 대용량 테이블을 비교할 때, 실행 결과 파일 용량이 커질 수 있으므로 주의해서 사용해야 한다.
   
2. ###### LOG_DF_MOSO

   PK는 동일하지만 나머지 칼럼값 중 하나라도 일치하는 않는 레코드 (DF_MOSO)를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
   
3. ###### LOG_MOSX

   Master DB에는 있으나, Slave DB에는 없는 레코드 (MOSX) 를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
   
4. ###### LOG_MXSO

   Master DB에는 없지만, Slave DB에는 있는 레코드 (MXSO) 를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   

프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
### TABLES 그룹 

실행 대상이 되는 테이블에 관련된 정보를 정의한다. 이 그룹은 실행 대상이 되는 테이블의 개수만큼 기술되어야 하며, 반드시 그룹명은 Master DB의 테이블 이름이어야 한다.

이 그룹에서 지정할 수 있는 프로퍼티는 다음과 같다.

##### WHERE

테이블의 레코드를 selection하는 조건을 지정한다. SQL 문의 WHERE 절에 기술하는 방식과 동일하게 기술한다. 다중 값을 허용하며, “;” 구분자로 여러 조건을 지정하는 것은 불가능하다. 또한 이 프로퍼티에는 주석을 달 수 없다. 비교(DIFF)와 일치(SYNC) 기능에 적용된다.

##### EXCLUDE

테이블의 레코드를 projection하는 조건을 지정한다. 프로퍼티 값은 다중 값으로 기술해야 한다. 기술된 칼럼들은 비교와 일치 작업에서 제외된다.

![](media/Utilities/e9cd168e51d8336eb99f9ba958d9688d.png)

![](media/Utilities/c8502d42132454c28fe8e7f0edd7c88b.png)

WHERE와 EXCLUDE를 적절히 조합하면, selection과 projection을 결합한 결과에 대해 altiComp 작업을 수행할 수 있다.

![](media/Utilities/3a664d250cbb847a5d4acd3acf65b5d1.png)

##### TABLE

Slave DB의 테이블 이름을 지정한다. Master DB와 Slave DB의 테이블 이름이 다른 경우에는 반드시 기술해야 하며, 비교(DIFF)와 일치(SYNC)기능에 적용된다. 생략하면 Mater DB의 테이블 이름과 동일하게 지정된다.

단, 테이블 이름은 반드시 영문 및 숫자와 해당 특수문자((공백,\~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \|)로 지정해야 하며, 한글은 사용할 수 없다.

##### SCHEMA

Slave Db의 테이블 스키마를 기술한다.

Slave의 접속하는 사용자의 스키마 이름과 대상 테이블의 스키마가 다른 경우에 반드시 기술해야 하며, 생략하면 Slave의 접속 사용자의 스키마를 사용하게 된다.



## 비교(DIFF) 기능

Master DB와 Slave DB 간의 이중화 작업에서 발생할 수 있는 불일치 레코드를 식별하여 실행 결과 파일로 생성하는 기능을 가진다.

### 환경 파일

altiComp 환경 파일의 OPERATION 프로퍼티 값을 “DIFF”로 지정한다.

실행 옵션의 모든 프로퍼티 파일을 기술해야 하며, 테이블 그룹의 WHERE, EXCLUDE, TABLE, SCHEMA 프로퍼티를 선택적으로 기술한다.

### 실행방법

비교(DIFF)기능은 다음과 같이 실행한다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

### 실행결과

실행 결과로, 실행결과에 대한 요약 정보를 포함하는 실행 로그 파일과 테이블 별로 Master Database와 Slave Database의 내용을 비교하여 불일치가 발생한 레코드의 불일치 칼럼 내용을 포함하는 실행 결과 파일이 생성된다.

예를 들어, /user/charlie/altibase_home/altiComp \> altiComp sample.cfg 과 같이 altiComp 명령을 실행했을 때, altiComp 명령이 성공적으로 실행되면 altiComp 디렉터리 하위에는 sample.log와 각각의 테이블에 대한 “마스터 테이블-사용자명.슬레이브 테이블.log” 파일이 생성된다.

##### 실행 로그 파일

“script_file_name.log” 이름으로 생성되며 실행한 환경 파일의 내용을 출력하고, 각 TABLES 그룹의 테이블에 대한 비교(DIFF)작업의 요약 정보를 출력한다.

환경 파일의 내용은 다음과 같이 출력된다.

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX = DF, Count :          1
MXSO = DF, Count :          0
MOSO = DF, Count :          1
MOSO = EQ, Count :          1

 SCAN TPS:   20547.95
     Time:       0.00 sec
```



##### 실행 결과 파일

**“마스터 테이블-사용자명.슬레이브 테이블.log”** 이름으로 생성되며, 비교 결과를 다음과 같은 형식으로 표현한다.

```
DF[m,n]-> COL_N (Vn_M, Vn_S):PK->{ PCOL_V }
```



-   DF : 불일치 원인 (MOSX, MOSO, MXSO)

-   m : Master Server의 레코드 순서

-   n : Slave Server의 레코드 순서

-   COL_N : 비교결과 다른 값을 가지는 첫 칼럼 이름

-   Vn_M : Master Server의 해당 칼럼의 값

-   Vn_S : Slave Server의 해당 칼럼의 값

단, 데이터 타입이 LOB인 칼럼이 있는 레코드의 경우 해당 칼럼의 값이 기록되지 않는다.

### 비교(DIFF) 예제

host1의 EMP 테이블과 host2의 EMPLOYEES 테이블, 그리고 host1의 DEPARTMENTS 테이블과 host2의 DEPARTMENTS 테이블에 대해 비교(DIFF) 기능을 수행하는 예제는 다음과 같다.

##### DIFF 예제 1

DB_MASTER를 host1, DB_SLAVE를 host2로 지정하고, 각각의 테이블의 모든 레코드를 비교하는 경우에 환경설정 파일은 다음과 같다

```
DB_MASTER = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
DB_SLAVE = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = DIFF
MAX_THREAD = -1
			
DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS 

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

위 예제와 같이 Master Server(host1)의 대상 테이블 이름과 Slave Server(host2)의 대상 테이블 이름이 다를 수 있다.

##### DIFF 예제 2

EMP 테이블의 ENO 칼럼을 기준으로 selection하고, JOIN_DATE, SEX 칼럼은 비교 대상에서 제외하는 경우는 다음과 같다.

CONDITION 프로퍼티 값에 따라, 비교 대상이 되는 EMP 레코드는 “ENO가 1 이상이고 20 이하”인 레코드로 제한된다.

또한 EXCLUDE 프로퍼티 값에 따라, JOIN_DATE 와 SEX는 비교 대상에서 제외된다.

즉, 다른 모든 칼럼은 같고, JOIN_DATE와 SEX만 다르다면 레코드는 동일한 것으로 처리된다.

```
[EMP]
TABLE = EMPLOYEES
WHERE = {ENO >= 1 and ENO <= 20}
EXCLUDE = {JOIN_DATE; SEX}
[DEPARTMENTS]
```



##### DIFF 예제 3

EMP 테이블의 ENO 칼럼과 JOIN_DATE를 기준으로 selection하고, SEX 칼럼은 비교 대상에서 제외하는 경우는 다음과 같다.

```
[EMP]
TABLE = EMPLOYEES
WHERE = {(ENO >= 1 and ENO <= 20) or (JOIN_DATE >= ‘20001010’)}
EXCLUDE = {SEX}

[DEPARTMENTS]
```

WHERE 프로퍼티 값에 따라, 비교 대상이 되는 EMP 레코드는 “ENO가 1 이상이고 20 이하” 또는 “JOIN_DATE가 2000년 10월 10일 이후”인 레코드로 제한된다. 또한 EXCLUDE 프로퍼티 값에 따라, SEX는 비교 대상에서 제외된다.



## 일치(SYNC) 기능

Master DB와 Slave DB 사이의 불일치 레코드를 식별하여 altiComp 환경 파일에 기술된 일치 정책에 따라 양 방향으로 반영하여 불일치를 해소하고, 실행요약정보와 에러정보를 포함하는 실행 결과 파일을 생성한다.

### 환경 파일

altiComp 환경 파일의 OPERATION 프로퍼티 값을 “SYNC”로 지정한다.

실행 옵션의 모든 프로퍼티 파일을 기술해야 하며, 테이블 그룹의 WHERE, EXCLUDE, TABLE, SCHEMA 프로퍼티는 선택적으로 기술한다

### 실행방법

일치(SYNC)기능은 다음과 같이 실행한다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

### 실행결과

실행 결과로, 실행의 요약정보를 포함하는 실행 로그 파일과 테이블 별로 Master Database와 Slave Database의 내용을 비교하여 불일치가 발생한 레코드에 대한 일치 작업의 정보를 포함하는 실행 결과 파일, 일치 작업중 발생한 에러에 관한 정보를 포함하는 에러로그 파일로 구성된다.

##### 실행 로그 파일

“script_file_name.log” 이름으로 생성되며 실행한 환경 파일의 내용을 출력하고, 각 TABLES 그룹의 테이블에 대한 일치(SYNC)작업의 요약 정보를 출력한다.

환경 파일의 내용은 다음과 같이 출력된다.

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX =  -, SI 
MXSO =  -, -
MOSO =  -, SU
MXSX =  -, -

-----------------------------------------
 Operation  Type      MASTER           SLAVE
-----------------------------------------
 INSERT     Try           0               1
             Fail           0               0

 UPDATE    Try           X               1
             Fail           X               0

 DELETE    Try           X               0
             Fail           X               0
-----------------------------------------
 UPDATE    Try           0               2
             Fail           0               0
 OOP  TPS:   13698.63
 SCAN TPS:   20547.95
     Time:       0.00 sec
```

만일 실패한 레코드가 있다면, 해당 레코드는 에러로그 파일에 원인과 레코드 내용이 출력된다.

### 일치(SYNC) 예제

불일치 레코드를 해소하기 위한 일치 정책에 관련된 OPERATION와 TABLE을 지정하는 예제를 제시한다.

##### SYNC 예제 1

MOSX 불일치레코드(Master Server에는 있지만, Slave Server에는 없는 레코드)를 Slave Server에 삽입하고, MXSO 불일치 레코드 (Slave Server에는 있지만, Master Server에는 없는 레코드)는 무시한다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

MOSX 불일치 레코드를 해소하기 위해 필요한 일치 정책은 SI 정책이므로, INSERT_TO_SLAVE 프로퍼티 값을 “ON”으로 지정하였다. 또한 MXSO 불일치 레코드는 무시하므로, 필요한 일치 정책인 MI, SD 정책에 관련된 INSERT_TO_MASTER와 DELETE_IN_SLAVE 프로퍼티는 “OFF”로 지정한다.

##### SYNC 예제 2

MOSX 불일치레코드(Master Server에는 있지만, Slave Server에는 없는 레코드)를 Slave Server에 삽입하고, MXSO 불일치 레코드(Slave Server에는 있지만, Master Server에는 없는 레코드) 는 Master Server에 삽입한다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

MOSX 불일치 레코드를 해소하기 위해 필요한 일치 정책은 SI 정책이므로, INSERT_TO_SLAVE 프로퍼티 값을 “ON”으로 지정한다. 또한 MXSO 불일치레코드는 Master Server에 삽입해야 하기 때문에, 필요한 일치 정책은 MI 정책이다. 따라서 이에 관련된 INSERT_TO_MASTER 프로퍼티를 “ON” 으로 지정하고, DELETE_IN_SLAVE 프로퍼티를 “OFF”로 지정한다.

##### SYNC 예제 3

Master Server와 동일하게 Slave Server를 일치시킨다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

Master Server와 동일하게 Slave Server를 일치시키기 위해서 필요한 일치 정책은 SI정책, SD 정책이다. 따라서, INSERT_TO_SLAVE와 DELETE_IN_SLAVE 프로퍼티 값을 “ON”으로 지정하였다.

##### SYNC 예제 4

\$ALTIBASE_HOME/sample/APRE/schema 디렉터리의 schema.sql을 참조하여 지역서버 host1의 EMPLOYEES 테이블과 원격 서버 host2의 EMPLOYEES 테이블(ENO에서 16번부터 20번까지 삭제), 그리고 host1 서버의 DEPARTMENTS 테이블과 host2 서버의 DEPARTMENTS 테이블에 대해 일치(SYNC) 기능을 수행하는 간단한 예제이다.

먼저 지역서버와 원격서버에 이중화 연결을 생성한다.

지역서버의 경우(IP: 192.168.1.11)

```
iSQL> CREATE REPLICATION rep1 WITH '127.0.0.1', 56342 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

원격서버의 경우(IP: 127.0.0.1)

```
iSQL> CREATE REPLICATION rep1 WITH '192.168.1.11', 65432 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

현재 디렉터리가 /user/charlie/altibase_home/ altiComp 이라면

```
$ vi sample.cfg
Master Server = "altibase://sys:manager@DSN=127.0.0.1;PORT_NO=20582;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=192.168.1.11;PORT_NO=20582;NLS_USE=US7ASCII"

OPERATION  = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF 
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[ EMPLOYEE S]
WHERE   = {ENO >= 1 and ENO <= 20}
TABLE   = EMPLOYEES 
SCHEMA  = SYS
[ DEPARTMENTS ]
TABLE   = DEPARTMENTS 
SCHEMA  = SYS

$ altiComp –f sample.cfg 
$ cat sample.log
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  1 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!
INFO[ MNG ] Tread #  1 start is  OK!

[DEPARTMENTS->DEPARTMENTS]
Fetch Rec In Master: 5
Fetch Rec In Slave : 5
MOSX = NO
MXSO = NO
MOSO = SU

--------------------------------------------
 Operation  Type      MASTER           SLAVE    
--------------------------------------------
 INSERT     Try            0               0 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
--------------------------------------------
 UPDATE     Try            0               0 
            Fail           0               0 
 OOP  TPS:       0.00
 SCAN TPS:   60240.96
     Time:       0.00 sec

[EMPLOYEES->EMPLOYEES]
Fetch Rec In Master: 20
Fetch Rec In Slave : 15
MOSX = NO
MXSO = NO
MOSO = SU

-------------------------------------------
 Operation  Type      MASTER           SLAVE    
-------------------------------------------
 INSERT     Try            0               5 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
-------------------------------------------
 UPDATE     Try            0               5 
            Fail           0               0 
 OOP  TPS:     576.04
 SCAN TPS:    2304.15
     Time:       0.01 sec
```



# 3.aku

## 개요

aku(Altibase Kubernetes Utility)는 쿠버네티스의 스테이트풀셋(Statefulset)에서 스케일링(scaling)할 때 파드(Pod)의 시작 및 종료에 따라 Altibase의 데이터를 동기화하거나 동기화 정보를 초기화하는 등의 작업을 수행할 수 있게 도와주는 유틸리티이다. 즉, aku는 파드들간의 데이터 이중화를 도와주는 유틸리티로, Altibase의 데이터 스케일아웃(scale-out) 기능은 지원하지 않는다.

> 스테이트풀셋은 데이터베이스처럼 상태 유지가 필요한 애플리케이션을 지원하기 위한 쿠버네티스의 워크로드 컨트롤러 중 하나이며, 스케일링은 파드를 생성하거나 종료하는 것을 의미한다. 파드는 컨테이너들을 담고 있는 쿠버네티스의 리소스이며, 이 컨테이너에 Altibase 서버가 실행된다. 

스테이트풀셋에서 스케일 업/다운할 때 아래의 조건에 해당하는 파드를 생성하거나 종료하고자 할 때 aku 유틸리티를 사용할 수 있다. 이때, aku 유틸리티가 Altibase 컨테이너에서 실행되도록 적당한 위치에 명령어를 추가해야 한다.

#### 스케일 업

기존 파드의 Altibase 서버와 동일한 데이터를 가진 파드를 생성한다.

가장 처음 생성된 파드를 aku에서는 마스터 파드(Master Pod)라고 부르며, 추가로 스케일 업하여 생성된 파드는 슬레이브 파드(Slave Pod)로 부른다.

#### 스케일 다운

파드를 종료할 때 Altibase 서버의 이중화 정보를 초기화한다. 


## 구성 요소

aku 유틸리티는 실행 파일과 설정 파일로 구성된다. 

> ⚠️ 모든 파드에서 실행하는 aku 실행 파일은 같은 버전을 사용해야 하며, aku 설정 파일 내 프로퍼티도 같은 값을 가져야 한다. 일반적으로 aku 실행 파일과 aku 설정 파일은 Altibase 컨테이너 이미지에 포함되어 있다. 
>
> Altibase 서버와 aku는 같은 컨테이너에서 실행해야 한다.

### aku 실행 파일

실행 파일의 이름은 aku이며 $ALTIBASE_HOME/bin에 위치한다. aku를 실행하려면 먼저 환경변수 ALTIBASE_HOME을 설정해야 한다.

### aku 설정 파일

aku를 실행하면 aku 설정 파일을 가장 먼저 읽어 Altibase 데이터 동기화에 필요한 정보를 얻는다. aku 설정 파일의 이름은 aku.conf이며 $ALTIBASE_HOME/conf에 위치해야 한다. Altibase 패키지에 aku.conf.sample 이름의 예제 파일을 제공하므로, aku를 실행하기 전에 이 파일을 참고하여 aku.conf를 생성해야 한다. aku 설정 파일의 내용은 아래와 같다. 

⚠️ '#' 다음에 오는 내용은 주석으로 처리한다.

~~~bash
# aku.conf.sample

#*****************************************************************
# Copyright 2022, Altibase Corporation or its subsidiaries.
# All rights reserved.
# Property File for Altibase AKU Utility
#*****************************************************************

#=================================================================
# Kubernetes setting Properties
#=================================================================
AKU_STS_NAME                  = altibase-sts    # statefulsets name
AKU_SVC_NAME                  = altibase-svc    # services name
AKU_SERVER_COUNT              = 4               # the number of Pods
#=================================================================
# Common Properties
#=================================================================
AKU_SYS_PASSWORD              = manager
AKU_PORT_NO                   = 20300
AKU_REPLICATION_PORT_NO       = 20301
AKU_QUERY_TIMEOUT             = 3600
AKU_QUERY_RETRY_COUNT         = 5
AKU_QUERY_RETRY_DELAY_MSEC    = 1000
#=================================================================
# aku start/end Properties
#=================================================================
AKU_ADDRESS_CHECK_COUNT       = 30
AKU_FLUSH_AT_START            = 1
AKU_FLUSH_TIMEOUT_AT_START    = 300
AKU_DELAY_START_COMPLETE_TIME = 0

AKU_FLUSH_AT_END              = 1
AKU_REPLICATION_RESET_AT_END  = 1
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
	REPLICATION_NAME_PREFIX = AKU_REP
	SYNC_PARALLEL_COUNT     = 1
	(
		SYS.T1, SYS.T2 PARTITION P1,
		SYS.T3
	)
)
~~~

각 프로퍼티에 대해 살펴보자.

| 카테고리                 | 프로퍼티 이름                        |  기본값   | 설명                                                         |
| ------------------------ | :----------------------------------- | :-------: | :----------------------------------------------------------- |
| 쿠버네티스 설정 프로퍼티 | AKU_STS_NAME                         |           | 쿠버네티스 오브젝트 명세에 정의한 스테이트풀셋 이름.<br/>설정할 수 있는 값의 최대 길이는 63바이트이다. |
|                          | AKU_SVC_NAME                         |           | 쿠버네티스 오브젝트 명세에 정의한 네트워크 서비스를 제공하는 서비스 이름.<br/>설정할 수 있는 값의 최대 길이는 63바이트이다. |
|                          | AKU_SERVER_COUNT                     |     4     | aku 유틸리티로 동기화할 수 있는 Altibase 서버의  최대 개수.<br/>쿠버네티스에서 스케일 업할 수 있는 파드 수를 의미하기도 한다.<br/>설정할 수 있는 값의 범위는 1 ~ 6이다. |
| 공통 프로퍼티            | AKU_SYS_PASSWORD                     |           | 데이터베이스 SYS 사용자 패스워드                             |
|                          | AKU_PORT_NO                          |   20300   | Altibase 서버의 서비스 포트.<br/>설정할 수 있는 값의 범위는 1024 ~ 65535이다. |
|                          | AKU_REPLICATION_PORT_NO              |   20301   | Altibase 이중화 포트.<br/>설정할 수 있는 값의 범위는 1024 ~ 65535이다. |
|                          | AKU_QUERY_TIMEOUT                    |   3600    | Altibase 서버 프로퍼티 QUERY_TIMEOUT를 의미한다. aku에서 수행한 쿼리의 수행 시간이 이 값을 초과하면 해당 동작은 취소된다. |
|                          | AKU_QUERY_RETRY_COUNT                |     5     | Altibase 서버에서 수행한 쿼리가 실패하면 이 값의 횟수만큼 재시도한다.<br/>0이면 재시도하지 않는다. |
|                          | AKU_QUERY_RETRY_DELAY_MSEC           | 1000 (ms) | Altibase 서버에서 수행한 쿼리가 실패하면 이 값의 시간만큼 대기한 후 재시도한다.<br/>0이면 대기하지 않고 재시도를 수행한다. |
| aku start/end 프로퍼티   | AKU_ADDRESS_CHECK_COUNT              |    30     | `aku -p start` 명령 수행 시 생성 중인 파드의 로컬 DNS가 엔드 포인트에 등록될 때까지 이 값의 횟수만큼 로컬 IP 접속을 시도한다. |
|                          | AKU_FLUSH_AT_START                   |     1     | `aku -p start` 명령 수행 시 이중화 갭을 제거할 것인지 설정한다.<br/>1이면 FLUSH 명령으로 이중화 갭을 제거하고, 0이면 제거하지 않고 시작한다. |
|                          | AKU_FLUSH_TIMEOUT_AT_START           |    300    | FLUSH WAIT 명령의 *wait_time*을 설정한다. 이 값이 0이면 FLUSH ALL을 수행하고 1 이상이면 FLUSH WAIT *wait_time*을 수행한다.<br>이 설정은 AKU_FLUSH_AT_START설정값이 1일 때만 유효하다. |
|                          | AKU_DELAY_START_COMPLETE_TIME        |  0(sec)   | 슬레이브 파드 생성 단계에서 내부적으로 데이터 동기화가 완료된 후 ADMIN_MODE 프로퍼티를 0으로 변경하기 전에 대기하는 시간을 설정한다. |
|                          | AKU_FLUSH_AT_END                     |     1     | 슬레이브 파드에서 `aku -p end` 명령 수행 시 이중화 갭을 제거할 것인지 설정한다.<br/>1이면 이중화 FLUSH ALL 명령으로 이중화 갭을 제거하고 0이면 제거하지 않는다. |
|                          | AKU_REPLICATION_RESET_AT_END         |     1     | 슬레이브 파드에서 `aku -p end` 명령 수행 시 RESET 명령으로 이중화 정보를 초기화할 것인지 설정한다.<br/>1이면 이중화 정보를 초기화하며, 0이면 초기화하지 않는다. |
| 이중화 프로퍼티          | REPLICATIONS/REPLICATION_NAME_PREFIX |           | aku가 생성하는 Altibase 이중화 객체 이름의 접두사. 설정할 수 있는 값의 최대 길이는 37바이트이다.<br/>[Altibase 이중화 객체 이름 생성 규칙](#rep_name_rules)을 참고한다. |
|                          | REPLICATIONS/SYNC_PARALLEL_COUNT     |     1     | 이중화 SYNC 수행 시 송신/수신 쓰레드의 수.<br/>1부터 100까지 설정할 수 있다. |

<a name="rep_name_rules"></a>

> [!Note] 
>
> **Altibase 이중화 객체 이름 생성 규칙**
>
> aku에서 생성하는 Altibase 이중화 객체 이름 생성 규칙은 다음과 같다.
>
> *REPLICATION_NAME_PREFIX*_\[*파드 번호*]\[*파드 번호*\]
>
> - REPLICATION_NAME_PREFIX: REPLICATIONS/REPLICATION_NAME_PREFIX 프로퍼티에서 설정한 문자열
> - 파드 번호: 쿠버네티스 스테이트풀셋이 생성하는 파드의 이름에서 *pod_name*\_ 뒤에 위치한 숫자이며 각 파드들은 순차적으로 생성된 고유한 순번을 가진다. Altibase 이중화 객체 이름에는 이중화 쌍이 되는 두 파드 번호가 포함되며, 작은 값이 앞에 위치한다.
>
> 예시) AKU_SERVER_COUNT = 4, REPLICATION_NAME_PREFIX = AKU_REP 로 설정된 경우 각 파드에서 생성되는 이중화 객체 이름
> | 파드 번호    | 이중화 객체 이름 | 설명                                      |
> | :----------- | :--------------- | :---------------------------------------- |
> | *pod_name*-0 | AKU_REP_01       | *pod_name*-0과 *pod_name*-1의 이중화 객체 |
> |              | AKU_REP_02       | *pod_name*-0과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_03       | *pod_name*-0과 *pod_name*-3의 이중화 객체 |
> | *pod_name*-1 | AKU_REP_01       | *pod_name*-0과 *pod_name*-1의 이중화 객체 |
> |              | AKU_REP_12       | *pod_name*-1과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_13       | *pod_name*-1과 *pod_name*-3의 이중화 객체 |
> | *pod_name*-2 | AKU_REP_02       | *pod_name*-0과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_12       | *pod_name*-1과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_23       | *pod_name*-2와 *pod_name*-3의 이중화 객체 |
> | *pod_name*-3 | AKU_REP_03       | *pod_name*-0과 *pod_name*-3의 이중화 객체 |
> |              | AKU_REP_13       | *pod_name*-1과 *pod_name*-3의 이중화 객체 |
> |              | AKU_REP_23       | *pod_name*-2와 *pod_name*-3의 이중화 객체 |
>
> ⚠️ aku가 생성하는 Altibase 이중화 객체의 이름을 사용자가 임의로 생성,삭제 및 수정할 경우 비정상적인 결과가 발생할 수 있다.
#### Altibase 이중화 대상 설정

사용자는 aku 설정 파일에서 aku가 생성한 Altibase 이중화 객체에서 관리할 **테이블** 또는 **파티션**을 지정할 수 있다. 이중화 대상을 지정하려면 이중화 관련 프로퍼티 설정 구문에 `[사용자 이름].[테이블 이름]` 또는 `[사용자 이름].[테이블 이름] PARTITION [파티션 이름]` 형식으로 이중화 대상의 정보를 추가해야 한다. 사용자 이름과 테이블 이름, 파티션 이름의 최대 길이는 모두 128바이트이다.

각 이중화 대상은 쉼표로 구분되며, 한 줄에 하나 이상의 이중화 대상을 입력할 수 있다.

다음은  *T1*~*T9* 테이블을 이중화 3개로 분리하여 관리하도록 설정하는 예시이다. *T2* 테이블의 경우, 파티션 *P1* 만 이중화 대상으로 설정하도록 했다.

```bash
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
    REPLICATION_NAME_PREFIX = AKU_REP1
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T1, SYS.T2 PARTITION P1,
        SYS.T3
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP2
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T4, SYS.T5, SYS.T6
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP3
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T7,
        SYS.T8,
        SYS.T9
    )
)
```



## 구문

~~~sql
aku
[-h]
[--help]
[-v]
[--version]
[-i]
[--info]
[-p [start | stop | clean] ]
[--pod [start | stop | clean] ]
~~~



## 파라미터

### -h, --help

aku 유틸리티의 사용법을 출력한다. 

### -v, --version

aku 유틸리티의 버전 정보를 출력한다. aku 유틸리티의 버전은 Altibase 서버와 같은 버전으로 사용하는 것을 권장한다. 


### -i, --info

aku 설정 파일의 내용을 출력한다. 파일에 문법(syntax) 오류가 있는 경우 에러를 출력하며 정상적일 때 아래의 정보를 출력한다.

- Altibase 서버 접속 정보(데이터베이스 사용자, 패스워드, Altibase 서비스 포트)
- Altibase 이중화 포트
- 스케일 업 최대 수(최대 파드 수)
- Altibase 이중화 객체 이름 및 이중화 대상 테이블 정보

### -p, --pod {pod_action}

스케일링으로 파드를 생성하거나 종료할 때 Altibase에서 수행할 작업을 명시한다. -p 또는 --pod 파라미터 뒤에 start, end, clean 중 하나를 반드시 입력해야 한다. 

#### **start**

Altibase 이중화 객체를 생성하고 데이터를 동기화하는 작업을 수행한다. 파드를 생성할 때 이용한다. start 명령의 상세 동작을 살펴보자.

- **마스터 파드(*pod_name*-0) 생성하기**

  Altibase 이중화 객체는 모든 파드에 생성해야 하므로 스테이트풀셋에서 *pod_name*-0을 생성할 때도 `aku -p start` 명령을 수행해야 한다.

  ![](media/Utilities/aku_p_start_master_pod.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다.
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 처음 생성된 파드이기 때문에 다른 파드와의 연결은 실패한다. 이는 정상적인 동작이니 무시해도 된다.
  
  ④ Altibase 이중화 객체를 생성한다. 만약, 같은 이름의 이중화 객체가 존재한다면 이중화 생성 단계는 생략한다. 
  
  ⑤ *pod_name*-0 에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-0과 관련된 이중화를 시작한다. 일반적인 경우 처음 생성된 파드이기 때문에 접속된 파드가 없어, 이 동작은 수행되지 않는다.
  
  ⑥ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.

- **스케일 업(Scale up)**

  마스터 파드가 생성된 상태에서 스케일 업을 하면 슬레이브 파드가 생성된다. 하나의 파드는 생성과 종료를 반복할 수 있는데, 파드가 처음 생성될 때와 종료 후 다시 시작될 때 `aku -p start` 동작이 다르다.

  > **슬레이브 파드를 처음 생성하거나, 다시 시작할 때 (AKU_REPLICATION_RESET_AT_END = 1, 기본 동작)**

  슬레이브 파드를 처음 생성하거나, 종료된 슬레이브 파드를 다시 시작하는 경우 `aku -p start` 명령이 aku에서 동작하는 과정을 설명한다.

  아래는 *pod_name*-1에서 수행한 예이다.

    ![](media/Utilities/aku_p_start_slave_pod.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다.
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공하고 *pod_name*-2, *pod_name*-3은 생성되지 않았기 때문에 접속에 실패한다.
  
  ④ Altibase 이중화 객체를 생성한다. *pod_name*-1이 다시 시작된 파드라면, 같은 이름의 이중화 객체가 존재할 수 있으며 이 단계는 생략된다.
  
  ⑤ *pod_name*-1의 이중화 대상 테이블을 대상으로 TRUNCATE를 수행한다.
  
  ⑥ *pod_name*-0에게 이중화 SYNC를 요청한다.
  
  ⑦ *pod_name*-0에서 *pod_name*-1로 이중화 SYNC를 수행하고 이중화를 시작한다.
  
  ⑧ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다. 일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다.
  
  ⑨ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다.
  
  ⑩ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.
  
    > **이중화 정보가 초기화되지 않은 슬레이브 파드를 다시 시작할 때 (AKU_FLUSH_AT_START = 1, 기본 동작)** 
  
  파드가 비정상적으로 종료되거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 종료하면 이중화 정보가 초기화 되지 않는다. 이중화 정보를 초기화 하지 않으면 Altibase에 이전의 이중화 정보가 남아 있어 파드를 다시 시작할 때 다른 노드로부터 데이터를 동기화(이중화 대상 테이블의 TRUNCATE 후 이중화 SYNC 수행)하지 않고, 자기 노드에서 다른 노드로의 데이터 동기화(FLUSH)만 수행한다. 아래는 이러한 경우, *pod_name*-1에서 `aku -p start`를 수행할 때의 aku 동작을 설명한다.
  
  참고로, 이중화 정보가 초기화 되지 않으면 이중화 관련 메타 테이블에 이중화 재시작 지점(XSN)이 -1이 아닌 값을 갖는다. 보다 자세한 내용은 [주의사항 7번](#cautions7)을 참고한다.
  
  ![](media/Utilities/aku_p_start_aku_flush_at_start_1.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다. 
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공한다. 
  
  ④ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다. 일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다.
  
  ⑤ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화에 대해 ALTER REPLICATION ~ FLUSH ALL을 수행한다. 이 명령은 *pod_name*-1에서 다른 파드로 동기화하지 못한 데이터를 전송한다. 
  
  ⑥ 접속된 다른 파드에서도 *pod_name*-1과 관련된 이중화에 대해 ALTER REPLICATION ~ FLUSH ALL을 수행하여 동기화되지 못한 데이터를 전송한다. 만약 aku 설정 파일에 AKU_FLUSH_TIMEOUT_AT_START 프로퍼티의 값이 0이 아니라면, ALTER_REPLICATION ~ FLUSH WAIT *wait_time*을 수행하여 *pod_name*-1로 동기화되지 못한 데이터를 전송한다. 
  
  ⑦ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다.
  
  ⑧ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.
  
  > **이중화 정보가 초기화되지 않은 슬레이브 파드를 다시 시작할 때 (AKU_FLUSH_AT_START = 0 일 때)**
  
  비정상적으로 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 종료한 슬레이브 파드를 다시 시작할 때, AKU_FLUSH_AT_START 프로퍼티를 0으로 설정했다면 아래와 같이 동작한다.
  
    ![](media/Utilities/aku_p_start_aku_flush_at_start_0.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다. 
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공한다.
  
  ④ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다.  일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다. 
  
  ⑤ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다. 
  
  ⑥ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.

#### **end**

Altibase 이중화를 중지하고 초기화하는 작업을 수행한다. 파드를 종료할 때 이용한다.

![](media/Utilities/aku_p_end.png)

① aku.conf 파일을 읽는다.

② 해당 파드와 이중화로 연결된 모든 파드에 접속을 시도한다. 해당 번호보다 높은 번호의 파드는 일반적인 경우 이미 삭제된 상태이기 때문에 접속이 실패할 수 있다. 이는 정상적인 동작이다.

③ 해당 파드의 이중화 객체에 ALTER REPLICATION replication_name FLUSH ALL 명령을 수행하여 변경 로그를 모두 전송한다. aku 설정 파일에서 AKU_FLUSH_AT_END 프로퍼티의 값이 0이라면 이 단계는 수행되지 않는다.

④ 해당 파드의 이중화 객체와 관련한 모든 파드에 ALTER REPLICATION replication_name STOP 수행을 요청한다.

⑤ 해당 파드의 이중화 객체와 관련한 모든 파드에 ALTER REPLICATION replication_name RESET 수행을 요청한다. aku 설정 파일에서 AKU_REPLICATION_RESET_AT_END 프로퍼티의 값이 0이라면 이 단계는 수행되지 않는다.

⑥ /tmp 디렉토리에서 aku_start_completed 파일을 삭제한다.

#### **clean**

파드에서 Altibase 이중화 객체를 모두 삭제하고, /tmp 디렉토리에서 aku_start_completed 파일을 삭제한다. 더 이상 파드 간에 동기화를 할 필요가 없을 때 사용한다.



## 주의사항

### 1) aku 설정 파일 작성 시

- aku 프로퍼티 중 기본값이 없는 프로퍼티는 반드시 명시해야 한다. 명시하지 않을 경우, "Property [*property_name*] should be specified by configuration." 에러가 발생한다.

- aku 설정 파일에 주석을 입력해야 할 경우 '#' 기호를 사용한다. 다만, '#' 뒤에 아무 내용이 없다면 구문 오류가 발생한다.

### 2) 마스터 파드의 저장소에 손상이 발생한 경우

aku는 마스터 파드의 저장소 손상으로 인한 데이터 손상을 복구할 수 없다.

### 3) aku -p start 명령 수행 시

- `aku -p start` 명령은 Altibase 서버가 정상적으로 시작된 후 수행해야 한다. 

- Altibase의 프로퍼티 중 ADMIN_MODE와 REMOTE_SYSDBA_ENABLE를 모두 1로 설정한 후 서버를 기동해야 한다.

- 하나의 파드에서 `aku -p start` 명령을 완료한 후 순차적으로 다음 파드를 생성해야 한다. 동시에 여러 파드에서 `aku -p start`를 수행하는 경우 aku가 정상적으로 동작하지 않을 수 있다. 이를 위해 startup probe를 설정해야 하며, aku_start_completed 파일의 존재 여부로 확인한다. 또한 publishNotReadyAddresses를 true로 설정해야한다. startup probe, publishNotReadyAddresses에 대한 자세한 내용은 쿠버네티스 공식 문서를 참고한다.

### 4) 마스터 파드 장애로 aku -p start 명령 수행이 실패했을 때

마스터 파드 장애란 다음과 같은 환경에서 마스터 파드에 `aku -p start` 명령이 실패하는 것을 말한다.

- 한 개 이상의 슬레이브 파드가 실행 중이다.
- 마스터 파드에 존재하는 이중화 객체 중 실행 중인 슬레이브 파드(들) 사이의 이중화 객체 정보가 일부, 또는 전부 유실되었다.

마스터 파드 장애가 발생하면 다음과 같이 마스터 파드를 복구해야 한다.

1. 복구 기준이 될 슬레이브 파드를 선택한다. 복구 기준이 되는 슬레이브 파드 외의 모든 슬레이브 파드는 `aku -p end` 명령을 수행하여 종료한다.
2. 슬레이브 파드로부터 마스터 파드로의 동기화를 수행하여 데이터 정합성을 맞춘다.
3. 마스터 파드에서 이중화를 시작한다.
4. `aku -p start` 명령을 다시 수행한다.

각 복구 단계의 자세한 내용은 아래의 마스터 파드 장애 복구 예시를 참고한다.

**마스터 파드 장애 복구 예시**

다음과 같은 환경에서 마스터 파드 *pod_name*-0에서 장애가 발생했다고 가정한다. 

- 마스터 파드의 aku 프로퍼티 설정
  - AKU_SERVER_COUNT = 4
  - REPLICATION_NAME_PREFIX = AKU_REP
- 마스터 파드의 Altibase 서버 프로퍼티 설정
  - ADMIN_MODE = 1
- 슬레이브 파드 *pod_name*-1가 실행 중이다.
- 이중화 대상 테이블은 *T1*, *T2*, 그리고 *T3*이다.
- 마스터 파드에서 슬레이브 파드 *pod_name*-1 사이의 이중화 객체 AKU_REP_01의 정보가 소실되었다.

마스터 파드 장애 상황은 아래의 로그를 통해 확인할 수 있다.

```bash
$ aku -p start
AKU started with START option.
[AKU][2024/04/19 19:21:31.012670][140276343642368] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
[AKU][2024/04/19 19:21:31.012991][140276343642368] [ERROR][akuRunStart:1030][-][-] The MASTER server is detected to have failed. Check and perform a manual recovery.
AKU failed to run.
```

이 때 마스터 파드에서 정보가 소실된 이중화 객체의 XSN을 조회하면 그 값이 -1로 출력된다.

```sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_01                      -1
1 rows selected.
```

> [!note] 
>
> XSN은 송·수신 쓰레드를 통해 원격 서버와 지역 서버에 이중화 정보를 전달하는 XLog의 식별 번호이다. 이중화 객체를 초기화 하면 이 값은 -1이 된다.
> 이 때 아래의 복구 절차를 순차적으로 수행하여 마스터 파드의 장애를 해결할 수 있다.

1. 슬레이브 파드로부터 마스터 파드로의 동기화를 수행하여 데이터 정합성을 맞춘다.

   1. 마스터 파드에서 이중화 대상 테이블 레코드를 삭제한다.

      데이터 동기화 시 충돌이 발생하는 것을 방지하기 위해 마스터 파드에서 관리하는 이중화 대상 테이블을 TRUNCATE 한다. TRUNCATE 명령을 수행하기 위해서는 Altibase 서버 프로퍼티REPLICATION_DDL_ENABLE를 1로 설정해야 한다.

      ```sql
      # REPLICATION_DDL_ENABLE 프로퍼티 설정을 1로 변경한다.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1;
      Alter success.

      # 이중화 대상 테이블의 레코드를 TRUNCATE 한다.
      iSQL> TRUNCATE TABLE T1;
      Truncate success.
      iSQL> TRUNCATE TABLE T2;
      Truncate success.
      iSQL> TRUNCATE TABLE T3;
      Truncate success.

      # REPLICATION_DDL_ENABLE 프로퍼티 설정을 0으로 원복한다.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 0;
      Alter success.
      ```

   2. 슬레이브 파드에서 데이터 동기화를 수행한다.

      데이터를 동기화하기 전에, XSN 값을 초기화하기 위해 RESET을 수행한다. 동기화가 완료되면 이중화가 자동으로 시작된다.

      ```sql
      # 슬레이브 파드에서 이중화를 중지한다.(이중화가 시작되지 않은 경우 생략할 수 있다.)
      iSQL> ALTER REPLICATION AKU_REP_01 STOP;
      Alter success.
      
      # 슬레이브 파드에서 마스터 파드와의 이중화 객체를 초기화한다.
      iSQL> ALTER REPLICATION AKU_REP_01 RESET;
      Alter success.
      
      # 이중화 SYNC를 수행하여 슬레이브 파드와 마스터 파드의 데이터 정합성을 맞춘다.
      iSQL> ALTER REPLICATION AKU_REP_01 SYNC;
      Alter success.
      ```

2. 마스터 파드에서 이중화를 시작한다.

   마스터 파드에서 이중화를 시작하여 소실되었던 이중화 객체 정보의 복구를 완료한다. 

   ```sql
   iSQL> ALTER REPLICATION AKU_REP_01 START;
   Alter success.
   ```

3. `aku -p start` 명령을 다시 수행한다.

   복구가 완료된 마스터 파드는 슬레이브 파드와 동일한 데이터를 갖고 있고, 마스터 파드와 슬레이브 파드 사이의 이중화 객체인 AKU_REP_01의 XSN 값도 갱신된다. 이제 `aku -p start` 명령을 다시 수행하면 정상적으로 처리된다.

   ```bash
   # aku.conf를 읽어 이중화 객체를 생성한다. 
   $ aku -p start
   # START option은 aku -p start 를 사용함을 의미한다. 
   AKU started with START option.
   [AKU][2024/04/19 19:21:01.011887][139922191153408] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
   
   # 마스터 파드와 슬레이브 파드의 이중화 갭을 제거한다.
   [AKU][2024/04/19 19:21:09.057372][139922191153408] [INFO][akuRunStart:891][-][-] Flush replications.
   [AKU][2024/04/19 19:21:09.086363][139922191153408] [INFO][akuRunStart:896][-][-] Replication flush has ended.
   
   # 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
   AKU run successfully.
   ```

### 5) aku -p end 명령 수행 시

- `aku -p end` 명령은 Altibase 서버를 중지하기 전에 수행해야 한다.

- `aku -p end` 명령 수행이 완료된 후 파드를 종료해야 한다. 

### 6) aku -p end 명령이 완료되기 전에 파드가 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료했다면

이중화 정보가 초기화되지 않고 남아 있을 수 있다. 이 경우 해당 파드가 다시 시작할 때 이중화 객체 생성과 이중화 대상 테이블을 TRUNCATE 하는 작업이 생략되고 이전에 생성한 이중화가 자동으로 시작된다. AKU_REPLICATION_RESET_AT_END 프로퍼티를 1으로 설정하고 `aku -p end` 명령이 정상적으로 수행될 때의 출력 결과는 [예시 4](#예시-4)를 확인해 보자.

### 7) aku -p end 명령이 완료되기 전에 파드가 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료한 상태가 장기간 지속된다면<a name="cautions7"></a>

종료된 파드뿐 아니라 다른 파드에도 이중화 정보가 초기화되지 않고 남아 있을 수 있다. 이 경우 다른 파드는 종료된 파드로 이중화 하기 위해 이중화에 필요한 온라인 로그 파일을 삭제하지 않는다. 온라인 로그 파일이 쌓이면 디스크 풀 발생으로 Altibase 서버가 정상적으로 운영되지 못할 수 있다. 따라서 이런 상황을 방지하기 위해  `aku -p end` 명령이 완전히 완료되기 전에 파드가 종료되었거나, AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료한 상태가 장기간 지속되고 있다면 이중화를 중지하고 이중화 초기화 작업을 진행해야 한다. 

~~~sql
ALTER REPLICATION replication_name STOP;
ALTER REPLICATION replication_name RESET;
~~~

*pod_name*-0과 *pod_name*-1을 운영하던 중에 *pod_name*-1에서 `aku -p end` 명령이 정상적으로 수행되지 못하고 종료되었다고 가정해 보자. 이 때 *pod_name*-0에서 SYSTEM_.SYS_REPLICATIONS\_의 XSN을 조회하면 *pod_name*-0과 *pod_name*-1의 이중화 객체인 AKU_REP_01의 XSN 값이 -1이 아닌 다른 값으로 출력된다. 이는 이중화 정보가 초기화되지 않은 것을 의미한다.

~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      859070110
3 rows selected.
~~~

*pod_name*-0에서 AKU_REP_01을 중지하고 이중화 객체를 생성한 시점으로 초기화한다. 

~~~sql
iSQL> ALTER REPLICATION AKU_REP_01 STOP;
Alter sucess.

iSQL> ALTER REPLICATION AKU_REP_01 RESET;
Alter sucess.
~~~

다시 *pod_name*-0에서 SYSTEM_.SYS_REPLICATIONS\_의 XSN을 조회해 보자. 이중화 객체 AKU_REP_01의 XSN 값이 -1으로 변경되었다.

~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      -1
3 rows selected.
~~~

<br/>

## 제약사항

aku 유틸리티를 안정적으로 사용하기 위해 쿠버네티스 환경 설정 시 반드시 지켜야 할 조건이다. 

- 쿠버네티스의 워크로드 컨트롤러 중 **스테이트풀셋에서만 사용**해야 한다.
- **Altibase 서버와 aku는 같은 컨테이너에서 실행**해야 한다.
- **파드 관리 정책은 OrderedReady** 여야 한다. OrderedReady는 스테이트풀셋의 기본 정책이다.
- 스케일 업할 수 있는 레플리카는 **최대 6개**이다.
- 파드 종료 시 aku 수행을 완료할 수 있는 시간을 확보해야 한다. 따라서, 쿠버네티스에서 파드를 강제 종료하는 대기 시간인 terminationGracePeriodSeconds를 충분히 크게 설정해야 한다.

<br/>

## 사용 예

이 장에서는 다양한 상황에서 aku를 사용하는 예제를 설명한다.

예제에서 확인할 수 있는 aku 로그의 정보는 다음과 같다.

```
[AKU][현재 날짜 시간][스레드 번호] [메시지 타입][코드 정보][대상 pod 이름][이중화 이름] 메시지
```

### 예시 1

-i 파라미터를 사용하여 aku를 실행한 결과이다. 아래 결과는 [aku 설정 파일](#aku-설정-파일)의 aku.conf.sample로 구성한 aku.conf에서 수행한 예시이다. Server ID가 0인 것은 스테이트풀셋 컨트롤러에서 처음 생성한 파드를 의미한다.

~~~bash
$ aku -i
 #########################
 [ Server ]
  Server ID        : 0
  Host             : AKUHOST-0.altibase-svc
  User             : SYS
  Password         : manager
  Port             : 20300
  Replication Port : 20301
  Max Server Count : 4
 #########################
 [ Replications ]
 #### Serve[ID:0] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_03
 #### Serve[ID:1] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_13
 #### Serve[ID:2] Replication list ####
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_23
 #### Serve[ID:3] Replication list ####
  Replication Name : AKU_REP_03
  Replication Name : AKU_REP_13
  Replication Name : AKU_REP_23
 #########################
 [ Replication Items ]
  User Name        : SYS
  Table Name       : T1
 
  User Name        : SYS
  Table Name       : T2
  Partition Name   : P1
 
  User Name        : SYS
  Table Name       : T3
 #########################
~~~

### 예시 2

마스터 파드(*pod_name-0*)에서 `aku -p start`를 수행한 예시이다.

~~~bash
$ aku -p start
AKU started with START option.
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
AKU run successfully.
~~~

출력 결과를 살펴보자. 

~~~bash
# aku.conf를 읽어 이중화 객체를 생성한다. 
# START option은 aku -p start 를 사용함을 의미한다.
AKU started with START option.

# MASTER Pod는 첫 번째 파드를 의미한다. 
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully.
~~~

### 예시 3

네 번째 파드(*pod_name-3*)에서 `aku -p start` 명령을 수행한 예시이다. Master Pod는 스테이트풀셋에서 생성한 첫 번째 파드를 의미한다.

~~~bash
$ aku -p start
AKU started with START option.
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.
AKU run successfully.
~~~

출력 결과를 살펴보자. 

~~~bash
# aku.conf를 읽어 이중화 객체를 생성한다. 
# START option은 aku -p start 를 사용함을 의미한다.
 AKU started with START option.

# SLAVE Pod는 첫 번째 파드가 아닌 다른 파드를 의미한다. 
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.

# SYNC 시 레코드 충돌 방지를 위해 대상 테이블의 레코드를 모두 삭제한다.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.

# MASTER Server는 첫 번째 파드(pod_name-0)의 Altibase 서버를 말하며 해당 서버의 데이터를 로컬 파드로 동기화한다.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully. 
~~~

### 예시 4

네 번째 파드에서 AKU_REPLICATION_RESET_AT_END 프로퍼티를 1으로 설정하고 `aku -p end` 명령을 수행할 때의 출력 결과이다. 이중화 FLUSH 및 RESET 명령이 수행된 것을 볼 수 있다

~~~bash
$ aku -p end
AKU started with END option.
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.
AKU run successfully.
~~~

출력 결과를 살펴보자.

```bash
# aku.conf를 읽어 이중화를 중지하고 초기화한다. 
# END option은 aku -p end 를 사용함을 의미한다.
AKU started with END option.

# SLAVE Pod는 첫 번째 파드가 아닌 다른 파드를 의미한다. 
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.

# 전달되지 않은 변경사항을 다른 파드로 FLUSH 한다.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.

# 로컬 파드의 AKU 에서 생성한 이중화 객체를 모두 초기화한다.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully. 
```



# 4.altiMon

## 개요

Altibase 서버 상태와 Altibase 서버가 구동 된 운영체제의 자원 상태를 수집하는 모니터링 유틸리티로, 운영체제의 자원 상태를 수집하기 위해 자체 제작한 PICL(Platform Information Collection Library) 라이브러리와 JDBC 드라이버 기반의 자바 애플리케이션이다. altiMon에서 수집한 데이터는 데이터베이스 장애 발생 시 장애 원인을 추적하는데 이용할 수 있다. 

altiMon의 모니터링 요소는 3가지로 나뉜다. 각 요소에 대한 보다 자세한 것은 [altiMon 설정 - Metrics.xml](#metricsxml)에서 설명한다.

- [OS Metric](#osmetric-요소) : Altibase의 PICL 라이브러리에서 미리 정의된 운영체제의 자원 상태
- [Command Metric](commanemetric-요소) : 사용자가 정의한 운영체제의 자원 상태
- [SQL Metric](sqlmetric-요소) : 사용자가 정의한 Altibase 서버 상태

<br/>

## 구문

~~~bash
altimon.sh {start | stop}
~~~

<div align="left">
    <img src=media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png>

<!-- IMG_RECOVERY_BEGIN ref_id="img-04608" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="2558" image_path_raw="media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png" image_class="C" format="bnf" verified="True" -->
```bnf
altimon ::=
    altimon.sh { start | stop }
```
<!-- IMG_RECOVERY_END ref_id="img-04608" -->

</div>
<br/>

## 파라미터

| 파라미터 | 설명         |
| -------- | ------------ |
| start    | altimon 시작 |
| stop     | altimon 종료 |

<br/>

## 시스템 요구사항

### 자바

- Oracle, OpenJDK 또는 IBM Java Runtime Environment 8 이상 
- 64비트 자바

### 지원 플랫폼

altiMon의 지원 플랫폼은 PICL 라이브러리를 제공하는 플랫폼에 의존한다. 

| 운영체제                                                     | CPU                     | PICL 라이브러리 |
| :----------------------------------------------------------- | :---------------------- | :-------------- |
| **AIX**                                                      |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 5.3<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 6.1<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 7.1 | PowerPC                 | aix-ppc64-5.so  |
| **HP-UX**                                                    |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HP-UX  11.31                   | Itanium (IA-64)         | hpux-ia64-11.sl |
| **Linux**                                                    |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 6.0   | x86-64                  | linux-x64.so    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 6.5   | PowerPC                 | linux-ppc64.so  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 7.2   | PowerPC (Little Endian) | linux-ppc64.so  |

AIX 7.3, RHEL 8 등 위 표에 명시되지 않은 운영체제 버전에서 PICL 라이브러리가 동작하는 지 확인하는 방법이다. 

##### PICL 라이브러리의 동작 여부를 확인하는 방법

1️⃣ $ALTIBASE_HOME/altiMon 디렉토리로 이동한다. 

  ```bash
$ cd $ALTIBASE_HOME/altiMon
  ```

2️⃣ java 명령어로 PICL 라이브러리의 동작 여부를 확인한다.

위 표에서 해당하는 운영체제의 PICL 라이브러리 파일명을 확인하고 아래 명령어를 수행한다. 반드시 $ALTIBASE_HOME/altiMon 디렉토리 아래에서 수행해야 한다. 

~~~bash
$ java -Dpicl="<picl_lib_file>" -jar lib/com.altibase.picl.jar
~~~

> 수행 예

~~~bash
$ java -Dpicl="linux-x64.so" -jar lib/com.altibase.picl.jar 
===========================================================
Platform Information Collection Library-PICL Testing Module
===========================================================

Initializing PICL(Platform Information Collection Library)...
PICL Library : linux-x64.so

----------
Process ID
----------
Altibase Process : /home/altibase/altibase_home/bin/altibase
PID : 5230
...중략... 
~~~

<br/>

## altiMon 시작 및 중지

### altiMon 시작

1️⃣ Java를 사용할 수 있게 PATH 환경 변수를 설정한다.

```bash
$ java -version
java version "1.8.0_101"
Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)
```

2️⃣ altiMon 시작 명령을 수행한다.

~~~bash
$ altimon.sh start
~~~

3️⃣ altiMon 시작이 실패하면 \$ALTIBASE_HOME/altiMon/logs/altimon.log 파일을 확인한다.



### altiMon 중지

~~~bash
$ altimon.sh stop
~~~

<br/>

## altiMon 설정

altiMon을 사용하기 위해 \$ALTIBASE_HOME/altiMon 디렉토리의 conf 디렉토리에 있는 아래의 파일들을 설정한다. 설정 파일들은 모두 XML 문서이다.

-   [config.xml](#config.xml)

-   [Metrics.xml](#metrics.xml)

-   [GroupMetrics.xml](#groupmetrics.xml)

### config.xml

altiMon 수행과 관련한 설정과 모니터링 대상인 Altibase 서버의 정보를 설정하는 파일이다. 루트 요소 \<configuration> (또는 \<config>) 태그를 시작으로 Altimon 요소와 Target 요소로 구성되어 있다. 

~~~xml
$ cat config.xml 
<?xml version="1.0" encoding="UTF-8"?>

<configuration>
    
    <!-- Altimon 요소 -->
    <Altimon Name="rnd1" monitorOsMetric="true">
        <!--<LogDir>logs</LogDir> -->
        <DateFormat>yyyy-MM-dd HH:mm:ss</DateFormat>
        <MaintenancePeriod>3<!-- days --></MaintenancePeriod>
        <Interval>60<!-- seconds --></Interval>
        <CpuSamplingInterval>3<!-- seconds --></Interval>
        <DBConnectionWatchdogCycle>60<!-- seconds --></DBConnectionWatchdogCycle>
    </Altimon>
    
    <!-- Target 요소 -->
    <Target Name="Altibase1">
        <!--<HomeDirectory>/home/altibase/altibase_home</HomeDirectory> -->
        <!--<User>sys</User> -->
        <Password Encrypted="No">manager</Password>
        <Port>20300</Port>
        <DbName>mydb</DbName>
        <NLS>KSC5601</NLS>
        <IPv6>FALSE</IPv6>
        <ConnectionProperties>login_timeout=3</ConnectionProperties>
    </Target>
    
</configuration>
~~~

> #### altiMon 실행 설정

config.xml에서 <Altimon ...> 요소는 altiMon 로그 출력 형식, 로그 파일 삭제 주기, 모니터링 주기와 같은 altiMon 실행과 관련된 설정을 정의한다. 이 요소는 두 개의 속성과 4개의 하위 요소를 가진다.

**속성**

| 속성 이름                                                    | 설명                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Name                                                         | 사용자가 임의로 설정하는 altiMon의 고유 이름이다. 현재는 별다른 용도가 없으며 추후 기능 확장 시 사용될 예정이다. |
| monitorOsMetric&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Metrics.xml 파일에서 OSMetric 요소를 사용할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 사용한다. PICL 라이브러리가 필요하다. <br />- false : 사용하지 않는다. OS 자원을 감시할 필요가 없거나 PICL C 라이브러리가 제공되지 않는 환경에서 설정한다. |

**하위 요소**

아래 표의 태그는 <Altimon ...> 요소 아래에 중첩된 하위 요소로 사용된다.

| 태그 이름                     | 설명                                                         |
| :---------------------------- | :----------------------------------------------------------- |
| \<LogDir\>                    | altiMon 로그 파일이 생성될 경로를 설정한다. 기본값은 logs 이며, 이 태그를 추가하지 않으면 $ALTIBASE_HOME/altiMon/logs로 설정된다. $ALTIBASE_HOME/altiMon 아래에 logs 디렉토리가 존재하지 않으면 altiMon을 시작할 때 생성한다. 값은 절대 경로나 $ALTIBASE_HOME/altiMon/ 아래에 생성할 디렉토리 이름을 사용할 수 있다. |
| \<DateFormat\>                | altiMon 로그의 날짜 형식을 설정한다. 기본값은 yyyy-MM-dd HH:mm:ss 이다. 설정 가능한 날짜 형식은 [자바 SimpleDateFormat 클래스의 날짜 형식](http://docs.oracle.com/javase/1.5.0/docs/api/java/text/SimpleDateFormat.html)을 참고한다. |
| \<MaintenancePeriod\>         | altiMon 로그 파일의 보관 기간을 설정한다. 기본값은 3이고 단위는 일(day)이다. |
| \<Interval\>                  | altiMon의 모니터링 데이터 수집 주기를 설정한다. 기본값은 60이고 단위는 초(second)이다. <br />Metrics.xml 파일의 \<OSMetric\> 또는 \<SQLMetric\> 요소에서 Interval 속성을 설정하지 않으면 이 값이 적용된다. GroupMetrics.xml 파일의 \<Groupetric\> 요소에서는 이 값의 영향을 받지 않는다. |
| <CpuSamplingInterval\>        | CPU 사용률(%)을 측정하는 쓰레드의 실행 주기이다. 기본값은 3이고 단위는 초(second)이다.<br/>Altibase 7.1.0.8.4 이후 부터는 CPU 사용률을 측정하기 위해 OS CPU 사용률 측정 쓰레드, Altibase CPU 사용률 측정 쓰레드가 추가되었다. 각 쓰레드는 CpuSamplingInterval 주기로 CPU 사용률을 측정하며, 모니터링 요소에서는 이 값들을 참조 한다. OS CPU 사용률 측정 쓰레드와 Altibase CPU 사용률 측정 쓰레드는 각기 별도의 쓰레드로 동작하기 때문에, CPU 과부하시 두 측정값 사이에 시간차가 발생할 수 있다. |
| \<DBConnectionWatchdogCycle\> | Altibase 서버로의 접속 시도 주기를 설정한다. Altibase 서버가 중지되었을 때 altiMon은 이 값에 따라 주기적으로 Altibase 서버에 접속을 시도하므로 Altibase 서버가 시작되면 모니터링을 지속할 수 있다. 기본값은 60이고 단위는 초(second)이다. |



> ####  Altibase 서버 설정

config.xml에서 <Target ...> 요소는 데이터베이스 사용자, 패스워드 등 altiMon으로 모니터링 할 Altibase 서버의 접속 정보를 설정한다. 이 요소는 한 개의 속성과 설정할 수 있는 속성과 8개의 하위 요소를 가진다.

**속성**

| 속성 이름                                                    | 설명                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Altibase 서버를 식별하기 위한 고유 이름으로 사용자가 임의로 설정 가능하다. 현재는 별다른 용도가 없으며 추후 기능 확장 시 사용될 예정이다. |

**하위 요소**

아래 표의 태그는 Target 요소 아래에 중첩된 하위 요소로 사용된다.

| 태그 이름                | 설명                                                         |
| :----------------------- | :----------------------------------------------------------- |
| \<HomeDirectory\>        | Altibase 서버의 홈 디렉토리를 절대 경로로 입력한다. 설정하지 않으면 환경변수 ALTIBASE_HOME 값이 적용된다. |
| \<User\>                 | Altibase 서버에 접속할 데이터베이스 사용자를 입력한다. 설정하지 않으면 기본값인 SYS 사용자로 접속한다. |
| \<Password Encrypted>    | 데이터베이스 사용자의 패스워드를 입력한다.<br />Encrypted 속성은 altiMon을 처음 시작하기 전에 "No" 값으로 설정해야 한다. 이후 altiMon을 시작하면  평문으로 입력한 패스워드가 암호화된 값으로 저장되며 Encrypted 속성의 값이 "Yes"로 변경된다. |
| \<Port\>                 | Altibase 서버의 서비스 포트를 입력한다.                      |
| \<NLS\>                  | 데이터베이스 클라이언트 캐릭터셋을 입력한다.                 |
| \<DbName\>               | 데이터베이스 이름을 입력한다. 설정하지 않으면 기본값 mydb 로 설정된다.<br />데이터베이스 이름은 아래 문장으로 확인할 수 있다.<br />`SELECT DB_NAME FROM V$DATABASE; ` |
| \<IPv6\>                 | IPv6 사용 여부를 설정한다. true 또는 false 값을 가지며 기본값은 false 이다.  <br />- true  : IPv6를 사용한다. Altibase 서버 프로퍼티 NET_CONN_IP_STACK이 1 또는 2일 때 설정할 수 있다.<br />- false : IPv6를 사용하지 않는다. |
| \<ConnectionProperties\> | Altibase 서버 접속할 때 추가적인 연결 속성이 필요한 경우 `연결속성=값;연결속성=값;...` 형식으로 입력한다. 사용할 수 있는 연결 속성은 [JDBC User's Manual](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.3/kor/JDBC%20User's%20Manual.md#%EC%97%B0%EA%B2%B0-%EC%A0%95%EB%B3%B4)을 참고한다.<br />예) `<ConnectionProperties>login_timeout=3;fetch_timeout=60</ConnectionProperties>` |



### Metrics.xml

CPU 및 메모리 사용률 등의 운영체제 자원과 Altibase 서버의 상태를 감시하기 위한 질의문을 설정하는 파일이다. 루트 요소 \<Metrics> 태그를 시작으로 CommandMetric 요소, OSMetric  요소, SQLMetric 요소로 구성되어 있다. 각 요소는 모니터링 항목에 따라 여러 번 사용할 수 있다.

~~~xml
$ cat Metrics.xml | more
<?xml version="1.0" encoding="UTF-8"?>

<Metrics>
    
    <!-- CommandMetric 요소 --> 
    <CommandMetric Name='MEM_VSZ'>
        <Command>scriptsDir/vsz.sh</Command>
        <Alert Activate='true' ComparisonType='gt'>
            <WarningThreshold Value='100000000'>
                <ActionScript>mem_act.sh</ActionScript>
            </WarningThreshold>
        </Alert>
    </CommandMetric>    
    
    <!-- OSMetric 요소 -->
    <OSMetric Name='TOTAL_CPU' Activate='true' Description='TOTAL_CPU'>
    <OSMetric Name='TOTAL_CPU_USER' Activate='false' Description='TOTAL_CPU_USER'></OSMetric>
    <OSMetric Name='TOTAL_CPU_KERNEL' Activate='false'></OSMetric>    
    <OSMetric Name='PROC_CPU' Activate='true'>
        <Alert Activate='true' ComparisonType='gt'>
            <WarningThreshold Value='80' >
                <ActionScript>cpu_act.sh</ActionScript>
            </WarningThreshold>
        </Alert>
    </OSMetric>
    
    <!-- SQLMetric 요소 --> 
    <SQLMetric Name='MEM_DATABASE_USAGE' Activate='true' Interval='30'>
        <Query>
            select
            trunc(mem_alloc_page_count*32/1024, 2) as alloc_mem_mb,
            trunc(mem_free_page_count*32/1024, 2) as free_mem_mb
            from v$database
        </Query>
        <Alert Activate='true' ComparisonColumn='ALLOC_MEM_MB' ComparisonType='GT'>
            <CriticalThreshold Value='8000' >
                <ActionScript>db_usage.sh</ActionScript>
            </CriticalThreshold>
        </Alert>
    </SQLMetric>
    <SQLMetric Name='MEMSTAT_LIST' Activate='true'>
        <Query>SELECT * FROM v$MEMSTAT ORDER BY 4 DESC LIMIT 30</Query>
    </SQLMetric>   

</Metrics>    
~~~



> #### 사용자 정의 운영체제 자원 모니터링(CommandMetric)

Metrics.xml에서 <CommandMetric ...> 요소는 사용자가 직접 감시할 운영체제 자원을 정의할 수 있게 지원하는 모니터링 요소이다. PICL 라이브러리가 필요한 OSMetric 요소를 사용할 수 없는 환경에서 사용자가 직접 운영체제 명령어로 자원을 감시할 수 있다. OSMetric 요소에서 지원하지 않는 항목을 CommandMetric 요소에 추가할 수도 있다. 

**속성**

CommandMetric 요소에서 사용할 수 있는 속성이다. 이 속성들은 OSMetric 요소, SQLMetric 요소에서도 동일하게 사용할 수 있다.

| 속성 이름   | 설명                                                         |
| :---------- | ------------------------------------------------------------ |
| Name        | CommandMetric 요소는 여러 개 사용할 수 있으며 각 요소를 식별하기 위한 고유 이름을 설정한다. 이 요소의 로그 는 *Name*.log 로 생성된다. |
| Description | 사용자가 임의의 설명을 기록하기 위한 항목이다.               |
| Activate    | 해당 CommandMetric 요소를 수집할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 해당 CommandMetric 요소를 수집한다.<br />- false : 해당 CommandMetric 요소를 수집하지 않는다. |
| Interval    | 데이터 수집 주기. 단위는 초(second)이다.<br/>설정하지 않으면 config.xml에서 Altimon 요소의 \<Interval> 에 설정한 값을 따른다. |
| Logging     | 데이터 수집 결과를 파일에 기록할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true : 데이터 수집 정보를 파일에 기록한다.<br />- false : 데이터 수집 정보를 파일에 기록하지 않는다. 단, 하위 요소로 <Alert …> 태그가 활성화되었다면, alert 정보는 이 설정과 무관하게 기록된다. |

**하위 요소**

여러 하위 요소가 있으나 여기서는 CommandMetric 요소에서만 사용할 수 있는 하위 요소를 소개하고 다른 하위 요소는 [공통 하위 요소](#공통-하위-요소) 에서 설명한다.

| 태그 이름  | 설명                                                         |
| :--------- | :----------------------------------------------------------- |
| \<Command> | 수행할 명령어 또는 스크립트 파일 경로를 절대 경로 또는 상대 경로로 입력한다. 상대 경로의 기준은 $ALTIBASE_HOME/altiMon 디렉토리이다. 예를 들어, 절대 경로 입력 방식은 $ALTIBASE_HOME/altiMon/scriptsDir/cpuUsageWithTop.sh이고 상대 경로 입력 방식은 scriptsDir/cpuUsageWithTop.sh만 입력하면 된다.<br />공통 하위 요소 중 <Alert …> 태그를 설정하려면 이 항목의 결과 값이 숫자여야 한다. |



> ####  미리 정의된 운영체제 자원 모니터링(OSMetric)

Metrics.xml에서 <OSMetric ...> 요소는 PICL 라이브러리에서 미리 정의한 운영체제 자원을 감시하도록 제공하는 모니터링 요소이다. 

감시 대상인 운영체제 자원은 아래와 같다. 

- CPU
- 메모리
- 스왑(swap)
- 디스크

**속성**

[CommandMetric 요소에서 사용하는 속성](#속성-4)과 동일하다. 다만, Name은 PICL 라이브러리에서 미리 정의한 이름을 사용해야 한다.

| Name으로 사용할 수 있는 값 | 설명                                                         |
| :------------------------- | :----------------------------------------------------------- |
| TOTAL_CPU                  | OS 전체 CPU 사용률(%)                                        |
| TOTAL_CPU_USER             | 사용자 모드(user mode)에서 CPU 사용률(%)                     |
| TOTAL_CPU_KERNEL           | 커널 모드(kernel mode)에서 CPU 사용률(%)                     |
| PROC_CPU                   | Altibase 프로세스의 CPU 사용률(%)                            |
| PROC_CPU_USER              | 사용자 모드(user mode)에서 Altibase 프로세스의 CPU 사용률(%) |
| PROC_CPU_KERNEL            | 커널 모드(kernel mode)에서 Altibase 프로세스의 CPU 사용률(%) |
| TOTAL_MEM_FREE             | 사용할 수 있는 메인 메모리(RAM)의 크기(KB)                   |
| TOTAL_MEM_FREE_PERCENTAGE  | 사용할 수 있는 메인 메모리(RAM)의 비율(%)                    |
| PROC_MEM_USED              | Altibase 프로세스가 사용중인 메인 메모리(RSS)의 크기(KB)     |
| PROC_MEM_USED_PERCENTAGE   | Altibase 프로세스가 사용중인 메인 메모리(RSS)의 비율(%)      |
| SWAP_FREE                  | 사용 가능한 SWAP의 크기(KB)                                  |
| SWAP_FREE_PERCENTAGE       | 전체 SWAP 공간에서 사용 가능한 SWAP의 비율(%)                |
| DISK_FREE                  | 지정한 디스크에서 사용되지 않은 디스크의 크기(KB). <br />이 값을 사용할 때는 <Disk Name ...> 하위 요소가 반드시 필요하다. |
| DISK_FREE_PERCENTAGE       | 지정한 디스크에서 사용되지 않은 디스크의 비율(%). <br />이 값을 사용할 때는 <Disk Name ...> 하위 요소가 반드시 필요하다. |

**하위 요소**

 [공통 하위 요소](#공통-하위-요소)를 참고한다.

> #### Altibase 서버 상태 모니터링(SQLMetric)

Metrics.xml에서 <SQLMetric ...> 요소는 Altibase 서버 상태를 수집할 수 있도록 제공하는 모니터링 요소이다.

**속성**

[CommandMetric 요소에서 사용하는 속성](#속성-4)과 동일하다. 

**하위 요소**

여러 하위 요소가 있으나 여기서는 SQLMetric 요소에서만 사용할 수 있는 하위 요소를 소개하고 다른 하위 요소는 [공통 하위 요소](#공통-하위-요소)를 참고한다.

| 태그 이름 | 설명                                                         |
| :-------- | :----------------------------------------------------------- |
| \<Query\> | 모니터링 쿼리를 입력한다. 이 쿼리는 반드시 데이터 한 건을 조회하는 SELECT 문이어야 한다. |



> #### 공통 하위 요소

CommandMetric, OSMetric, SQLMetric 요소에서 공통적으로 사용할 수 있는 하위 요소를 설명한다. 각 하위 요소는 아래와 같이 중첩적으로 사용된다. 

~~~xml
<Alert Activate='...' ComparisonColumn='...' ComparisonType='...'>
    <WarningThreshold Value='...'>
        <ActionScript>script_name</ActionScript>
    </WarningThreshold>
</Alert>
~~~

| 태그 이름                                       | 속성 이름        | 설명                                                         |
| :---------------------------------------------- | :--------------- | :----------------------------------------------------------- |
| <Alert …>                                       |                  | 이 요소는 선택 항목으로, 모니터링 요소의 출력 값이 사용자가 정의한 한계 설정을 만족할 때 별도의 로그 $ALTIBASE_HOME/altiMon/logs/alert.log에 기록하는 기능이다. |
|                                                 | Activate         | <Alert …>의 수행 여부를 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true : alert 기능을 사용한다. 하위 요소로 <WarningThreshold …> 또는 <CriticalThreshold …>가 반드시 필요하다. <br />- false : alert 기능을 사용하지 않는다. |
|                                                 | ComparisonColumn | 이 속성은 ***SQLMetric에서만*** 사용할 수 있다. SQLMetric에서 조회한 칼럼을 입력해야 한다. 칼럼의 값은 <WarningThreshold …> 또는 <CriticalThreshold …>의 Value 속성과 비교 가능한 10진수 숫자여야 한다. |
|                                                 | ComparisonType   | 모니터링 요소의 출력 값과 <WarningThreshold …> 또는 <CriticalThreshold …>의 Value 속성과 비교할 비교 연산자를 입력한다.<br />- eq : 모니터링 요소의 출력 값과 한계값이 같을 때<br/>- ne : 모니터링 요소의 출력 값이 한계값과 같지 않을 때 <br/>- gt : 모니터링 요소의 출력 값이 한계값보다 클 때<br/>- ge : 모니터링 요소의 출력 값이 한계값보다 크거나 같을 때<br/>- lt : 모니터링 요소의 출력 값이 한계값보다 작을 때<br/>- le : 모니터링 요소의 출력 값이 한계값보다 작거나 같을 때 |
| <WarningThreshold …> 또는 <CriticalThreshold …> |                  | <Alert …>의 하위 요소로 경고 종류를 선택한다. <WarningThreshold …> 일 때 alert.log의 첫 번째 열은 WARNING이고 <CriticalThreshold …>이면 CRITICAL이다. <br />Activate 속성값이 true이면 반드시 이 요소를 사용해야 한다. |
|                                                 | Value            | 모니터링 요소의 한계 값을 10진수 숫자로 설정한다.            |
| \<ActionScript\>                                |                  | <WarningThreshold …> 또는 <CriticalThreshold …>의 하위 요소로, 모니터링 요소의 출력 값이 사용자가 정의한 한계 조건에 해당할 때 수행할 스크립트 파일 이름을 입력한다. 이 파일은 미리 작성되어 있어야 하며 $ALTIBASE_HOME/altiMon/action_scripts 디렉토리에 위치해야 한다. 스크립트 수행 시 각 모니터링 요소의 Name 속성과 alert 종류, 한계 값, 모니터링 요소의 결과 값이 인자로 전달된다. <br />스크립트 수행 결과는 $ALTIBASE_HOME/altiMon/action_logs/*actionscript_name*.log에 기록된다. action_logs의 파일들은 장애 원인 분석에 꼭 필요한 정보가 될 수 있어서 altiMon이 자동으로 삭제하지 않으므로 ***사용자가 직접 관리***해야 한다. |

### GroupMetrics.xml

Metrics.xml에 정의한 Command Metric과 OS Metric 그리고 SQL Metric을 사용자가 원하는 항목 별로 조합하여 하나의 파일에 저장하는 기능을 제공한다. GroupMetrics로 수집한 데이터는 $ALTIBASE_HOME/altiMon/logs 디렉토리에 CSV 파일 형식의 *GroupMetricName*.csv 이름으로 저장된다. Metrics.xml은 루트 요소 \<GroupMetrics> 태그를 시작으로 여러 개의 GroupMetric 요소로 구성할 수 있다.

~~~xml
<?xml version="1.0" encoding="UTF-8"?>

<GroupMetrics>
    <GroupMetric Name='group1' Interval='40'>
        <Target MetricName='TOTAL_CPU'/>
        <Target MetricName='PROC_CPU'/>
        <Target MetricName='LOGFILE_COUNT'>
            <Column Name='LOG_GAP' />
        </Target>
    </GroupMetric>
    
    <GroupMetric Name='group2' Interval='80'>
        <Target MetricName='PROC_MEM_USED_PERCENTAGE'/>
        <Target MetricName='MEM_TBL_USAGE'/>
    </GroupMetric>
</GroupMetrics>
~~~

다음은 GroupMetrics.xml에 설정할 수 있는 XML 요소와 속성에 대한 설명이다.

**속성**

GroupMetric 요소에서 사용할 수 있는 속성이다. 이 속성들은 OSMetric 요소, SQLMetric 요소에서도 동일하게 사용할 수 있다.

| 속성 이름 | 설명                                                         |
| :-------- | :----------------------------------------------------------- |
| Name      | GroupMetric을 식별하는 고유한 이름으로 사용자가 임의로 설정 가능하다. 로그 파일 생성 시 이 이름이 사용된다. 예) *group1*.csv |
| Activate  | GroupMetric 요소를 수집할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 해당 CommandMetric 요소를 수집한다.<br />- false : 해당 CommandMetric 요소를 수집하지 않는다. |
| Interval  | 데이터 수집 주기. 기본값은 60이며 단위는 초(second)이다.     |

**하위 요소**

GroupMetric 요소 아래에 \<Target MetricName\>, \<Column Name\> 요소가 중첩적으로 사용된다.

| 태그 이름             | 설명                                                         |
| :-------------------- | :----------------------------------------------------------- |
| \<Target MetricName\> | Group Metric에 포함할 모니터링 요소들을 지정한다. <br /><br />MetricName 속성에 Metrics.xml에서 정의한 Command Metric과 OSMetric 그리고 SQLMetric의 이름을 입력한다. OSMetric의 DISK_FREE와 DISK_FREE_PERCENTAGE를 입력할 때 'OSMetric Name'.'Disk Name'형식으로 입력해야 한다. 예) <Target MetricName='DISK_FREE.disk1'\> |
| \<Column Name\>       | SQL Metric의 결과 중 일부 칼럼만 Group Metric에 포함하고 싶을 때 사용한다. 이 태그를 사용하지 않으면 SQL Metric에서 조회한 모든 칼럼이 Group Metric에 포함된다.<br /><br />Name 속성에 칼럼 이름을 입력한다. 칼럼 이름에 alias를 지정한 경우 alias를 입력한다. |

<br/>

## altiMon 로그

altiMon 로그는 $ALTIBASE_HOME/altiMon/logs 아래에 생성된다. 

### logs 디렉토리

logs 디렉토리에 생성되는 파일은 아래와 같다.

##### altimon.log  

altiMon 시작/중지 과정의 로그와 altiMon 수행 중 예외 상황 발생 시의 경고 또는 에러 메시지가 기록된다. 

##### alert.log  

Metrics.xml에서 \<Alert\> 설정에 해당하는 데이터를 기록하는 파일이다.

~~~bash
$ cat alert.log 
WARNING | PROC_CPU_USER | 2022-11-21 17:21:48 | PROC_CPU_USER = [90.61]
WARNING | PROC_CPU_USER | 2022-11-21 17:22:48 | PROC_CPU_USER = [90]
WARNING | PROC_CPU_USER | 2022-11-21 17:23:48 | PROC_CPU_USER = [90]
CRITICAL | DISK_FREE_PERCENTAGE.disk1 | 2022-11-21 17:24:46 | DISK_FREE_PERCENTAGE.disk1 = [5.22]
WARNING | PROC_CPU_USER | 2022-11-21 17:24:46 | PROC_CPU_USER = [90]
CRITICAL | DISK_FREE_PERCENTAGE.disk1 | 2022-11-21 17:25:46 | DISK_FREE_PERCENTAGE.disk1 = [5.22]
~~~

##### OsMetrics.log  

Metrics.xml에서 설정한 OSMetric에 의해 수집된 데이터를 기록하는 파일이다.

~~~bash
2022-11-21 20:20:25 | TOTAL_MEM_FREE_PERCENTAGE = [40.35]
2022-11-21 20:20:25 | SWAP_FREE = [94629696]
2022-11-21 20:20:25 | DISK_FREE_PERCENTAGE.disk1 = [30.21]
2022-11-21 20:20:25 | SWAP_FREE_PERCENTAGE = [96.26]
2022-11-21 20:20:25 | TOTAL_MEM_FREE = [39970752]
2022-11-21 20:20:25 | PROC_MEM_USED = [1010604]
2022-11-21 20:20:25 | PROC_MEM_USED_PERCENTAGE = [1.02]
2022-11-21 20:20:25 | PROC_CPU_KERNEL = [0]
2022-11-21 20:20:25 | PROC_CPU_USER = [0]
~~~

##### [*SQLMetric_Name*].log  

SQL Metric에 의해 수집된 데이터가 기록된 파일이다.

~~~bash
-rw-rw-rw- 1 altibase altibase   15399 Nov 21 20:21 BUFFER_STAT.log
-rw-rw-rw- 1 altibase altibase   10701 Nov 21 20:21 STATEMENT_COUNT.log
-rw-rw-rw- 1 altibase altibase  451791 Nov 21 20:21 SESSION_EVENT.log
-rw-rw-rw- 1 altibase altibase 1320921 Nov 21 20:21 MEMSTAT_LIST.log
-rw-rw-rw- 1 altibase altibase  346347 Nov 21 20:21 DB_EVENT.log
-rw-rw-rw- 1 altibase altibase   86298 Nov 21 20:21 DATAFILE_STAT.log
-rw-rw-rw- 1 altibase altibase   32364 Nov 21 20:21 MEM_GC.log
-rw-rw-rw- 1 altibase altibase   28710 Nov 21 20:21 SERVICE_THREAD_MODE.log

$ more BUFFER_STAT.log
2022-11-21 13:39:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:40:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:41:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:42:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
~~~

##### [*GroupMetric_Name*].csv  

Group Metric에 의해 수집된 데이터가 Metric별로 csv 파일에 기록된다.

~~~bash
$ cat group1.csv 
"TIMESTAMP","TOTAL_CPU_USER","PROC_CPU_USER","LOGFILE_COUNT.LOG_GAP"
"2022-11-21 13:39:42","8.01","0","0"
"2022-11-21 13:40:22","0.81","0","0"
"2022-11-21 13:41:02","0.82","0","0"
"2022-11-21 13:41:42","0.79","0","0"
"2022-11-21 13:42:22","0.69","0","0"
~~~

##### report.html  

사용자가 설정한 altiMon 설정을 웹으로 확인할 수 있도록 제공하는 html 파일이다.

<div align="left">
    <img src="media/Utilities/altiMon_report_html.png">
</div>


### logs/archive 디렉토리

logs 디렉토리의 altimon.log, \*.csv를 제외한 모든 파일이 archive/YYYY-MM-DD 디렉토리로 매일 백업된다. 이 디렉토리 중 config.xml의 altiMon 실행 설정에서 \<MaintenancePeriod\>에서 설정한 기간이 지난 디렉토리는 매일 새벽 1시 50분에 삭제된다.

### logs/csv_backup 디렉토리

Group Metric에서 Target 설정이 변경되지 않으면 계속 같은 csv 파일에 데이터가 추가된다. 하지만 Target이 변경되면 기존의 csv 파일은 logs/csv_backup 디렉토리로 백업되고 같은 이름의 파일에 새로운 데이터가 기록된다.

5.기타 Utilities
==============

## altiAudit

### 개요

감사가 Altibase 서버에서 수행 중이라면, \$ALTIBASE_HOME/trc 디렉토리에 기본적으로 감사 로그 파일이 생성되고 로그가 기록될 것이다. 감사 로그 파일의 위치는 AUDIT_LOG_DIR 프로퍼티로 변경 가능하다. 이 파일에는 사용자가 읽을 수 없는 바이너리 형태의 감사 로그가 기록되어 있다. altiAudit 유틸리티는 감사 로그 파일을 문자 형태로 변환하여 출력함으로써 사용자가 감사 로그를 분석할 수 있게 한다.

```
altiAudit [-s] {audit_log_file_name}
```



### 구문

![](media/Utilities/altiaudit.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04610" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3075" image_path_raw="media/Utilities/altiaudit.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiaudit ::=
    altiAudit [ -s ] audit_log_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-04610" -->


### 설명

서버가 남긴 감사 로그를 문자 형태로 변환하여 출력한다.

\-s 옵션을 사용해서 CSV 형태로 출력할 수도 있다.

### 사용예

아래는 감사 로그를 일반 텍스트 형태로 출력하는 명령어이다.

```
$ altiAudit $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

아래와 같은 형태의 결과가 출력된다.

```
[2015/03/05 14:59:29]
Session Info 
  User Name        = SYS
  Session ID       = 1                   
  Client IP        = 127.0.0.1
  Client Type      = CLI-64LE
  Client App Info  = isql
  Action           = INSERT
  Auto Commit      = 1                        (0:non-autocommit 1:autocommit)
 
Query Info 
  Statement ID      = 65540               
  Transaction ID    = 150657              
  Execute result    = 4                       (0:failure 1:rebuild 2:retry 3:queue empty 4:success)
  Fetch result      = 2                       (0:failure 1:success 2:no result set)
  Success count     = 1                   
  Failure count     = 0                   
  Return code       = 0x02000
  Processed row     = 1                   
  Used memory       = 0                       bytes
  XA flag           = 0                       (0:non-XA 1:XA)
 
Query Elapsed Time 
  Total time        = 0                   
  Soft prepare time = 0                   
  Parse time        = 0                   
  Validation time   = 0                   
  Optimization time = 0                   
  Execution time    = 0                   
  Fetch time        = 0                   
 
SQL 
--------------------------------------------------------------------------------
insert into t1 values ('aaaa', 1)
-------------------------------------------------------------------------------- 

```

아래는 감사 로그를 CSV 형태로 출력하는 명령어이다.

```
$ altiAudit -s $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

아래와 같이 CSV 형태의 결과가 출력된다.

```
1425535169,SYS,1,127.0.0.1,CLI-64LE,isql,INSERT,1,65540,150657,4,2,1,0,1,0,0,0,0,0,0,0,0,0,"insert
into t1 values ('aaaa', 1)"
```



### 출력 항목

출력 항목과 의미는 아래 표와 같다.

| 필드 이름              | 타입    | 설명                                                         |
| ---------------------- | ------- | ------------------------------------------------------------ |
| **Session Info**       |         |                                                              |
| User Name              | 문자열  | 세션에 접속한 사용자 이름                                    |
| Session ID             | INTEGER | 세션 ID                                                      |
| Client IP              | 문자열  | 클라이언트 IP 주소                                           |
| Client Type            | 문자열  | 접속한 클라이언트의 타입                                     |
| Client App Info        | 문자열  | 애플리케이션 정보                                            |
| Action                 | 문자열  | 실행된 구문의 종류                                           |
| Auto Commit            | INTEGER | 0: Non-auto commit mode 1: auto commit mode                  |
| **Query Info**         |         |                                                              |
| Statement ID           | INTEGER | Statement ID                                                 |
| Transaction ID         | INTEGER | 트랜잭션 ID                                                  |
| Execute result         | INTEGER | 수행 결과 0: failure 1: rebuild 2: retry 3: query empty 4: success |
| Fetch result           | INTEGER | Fetch 결과 0: failure 1: success 2: no result set            |
| Success count          | INTEGER | 감사 조건에 부합하는 구문이 성공한 횟수이다. BY SESSION 조건일 경우, 감사 조건에 부합하는 구문의 수행에 성공한 횟수의 누적 값이다. BY ACCESS 조건일 경우, 감사 조건에 부합하는 구문이 성공적으로 수행된 경우 1이 표시된다. |
| Failure count          | INTEGER | 감사 조건에 부합하는 구문이 실패한 횟수이다. BY SESSION 조건일 경우, 감사 조건에 부합하는 구문의 수행에 실패한 횟수의 누적 값이다. BY ACCESS 조건일 경우, 감사 조건에 부합하는 구문의 수행이 실패한 경우 1이 표시된다. |
| Return code            | INTEGER | 감사 조건에 부합하는 구문이 수행된 결과 코드이다. BY ACCESS 조건일 경우에만, 수행 결과가 표시된다. |
| Processed row          | INTEGER | 처리된 레코드의 개수                                         |
| Used memory            | INTEGER | 사용된 메모리 (향후 확장 예정)                               |
| XA flag                | INTEGER | 0: Non-XA 1: XA                                              |
| **Query Elapsed Time** |         |                                                              |
| Total time             | BIGINT  | 쿼리 수행에 소요된 총 시간                                   |
| Soft prepare time      | BIGINT  | Prepare 수행에 소요된 시간                                   |
| Parse time             | BIGINT  | 파싱 수행에 소요된 시간                                      |
| Validation time        | BIGINT  | 정당성 검사에 소요된 시간                                    |
| Optimization time      | BIGINT  | 최적화 수행에 소요된 시간                                    |
| Execution time         | BIGINT  | 실행에 소요된 시간                                           |
| Fetch time             | BIGINT  | Fetch 수행에 소요된 시간                                     |
| **SQL**                |         |                                                              |
|                        | 문자열  | 실행된 SQL 구문                                              |

## altibase

### 개요

‘altibase’는 Altibase의 모든 서비스를 관장하는 서버 프로세스를 실행하는 파일이다.

```
altibase {-v|n}
```



### 구문

![](media/Utilities/altibase.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04611" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3197" image_path_raw="media/Utilities/altibase.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altibase ::=
    altibase { -v | -n }
```
<!-- IMG_RECOVERY_END ref_id="img-04611" -->


### 파라미터

| 파라미터 | 설명                                                |
|----------|-----------------------------------------------------|
| \-v      | 설치되어 있는 Altibase 제품의 버전 정보를 출력한다. |
| \-n      | Altibase를 포그라운드에서 수행한다.                 |

### 설명

‘altibase’는 Altibase의 모든 서비스를 관장하는 서버 프로세스의 실행 가능(executable) 파일이다.

Altibase를 구동하거나 종료하기 위해 이 커맨드를 직접 사용하면 안 된다. 대신에 iSQL에 SYSDBA 모드로 접속한 뒤, 구동이나 종료 명령을 사용하거나 server 커맨드를 사용해야 한다. server 커맨드는 실제로 Altibase 구동과 종료에 관련된 일련의 명령을 묶어놓은 쉘 스크립트이다. 관련 내용은 본 문서의 server 항목을 참조한다.

보다 자세한 Altibase의 구동 및 종료에 관한 내용은 *iSQL User’s Manual*이나 *Getting Started Guide* 를 참조한다.

iSQL로 구동된 Altibase 서버 프로세스는 백그라운드에서 운영된다. 반면, 쉘 프롬프트에서 altibase 커맨드를 -n옵션으로 수행할 경우 Altibase는 포그라운드에서 구동된다. 이는 Altibase 디버깅을 위한 용도로만 사용되며, 실 운영 시에는 사용하지 않도록 한다.

\-v 옵션으로 altibase 커맨드를 실행하면 현재 설치된 Altibase 제품의 버전 정보를 출력한다.

### 참고사항

Getting Started Guide

Administrator’s Manual

iSQL User’s Manual





## altierr

### 개요

altierr은 Altibase 서버 에러 코드에 대한 상세한 설명을 검색하여 출력하는 유틸리티이다. 에러 번호나 에러 메시지 패턴을 이용하여 검색이 가능하다.

```
altierr {-w keyword pattern | [-n] error number}
```



### 구문

![](media/Utilities/altierr.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04612" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3244" image_path_raw="media/Utilities/altierr.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altierr ::=
    altierr { -w keyword_pattern | [ -n ] error_number }
```
<!-- IMG_RECOVERY_END ref_id="img-04612" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-w      | 지정한 검색 패턴을 포함하는 에러 메시지를 찾는다. <br />검색 패턴을 포함하는 모든 에러 메시지를 출력한다. |
| \-n      | 에러 번호를 사용하여 검색한다. 에러 번호는 16진수/양의 정수/음의 정수 형태로 입력 가능하다. <br />에러 코드와 정확히 일치하는 레코드만 검색된다. <br />에러 번호를 사용하여 검색할 경우 파라미터(“-n”)를 생략할 수 있다. |

### 설명

altierr은 Altibase 서버의 에러 코드 번호나 에러 메시지에 포함된 문자열을 이용하여 에러에 대한 상세한 설명을 검색하고 출력해 주는 유틸리티이다.

에러 상세 설명에는 에러 코드 번호, 에러 코드 문자열, 에러 설명, 에러가 발생한 원인, 그리고 에러에 대한 조치 사항이 포함된다.

Altibase 서버는 에러 상황 발생시 해당 코드를 “ERR-{에러번호}” 형태로 altibase_boot.log에 출력한다. 여기에서 에러 번호는 16진수 값으로, 해당 에러에 대한 상세 설명을 검색하기 위해 altierr을 다음과 같이 사용할 수 있다.

```
For ‘ERR-00015’
$ altierr 0x00015
$ altierr –w 00015
$ altierr 21
```

C/C++ Precompiler나 ODBC로 작성된 애플리케이션의 경우 SQL 관련 기능 수행 시 SQLCODE나 ODBC 함수의 리턴 코드에 에러 코드가 설정이 된다. 이 때 설정되는 에러 코드는 음의 정수 값이 설정되며, 해당 에러에 대한 상세 설명을 검색하기 위해 다음과 같이 altierr을 사용할 수 있다.

```
For -266286
$ altierr -266286
$ altierr 266286
$ altierr 0x4102E
```

altierr은 에러 메시지에 포함된 키워드를 이용한 검색을 지원하며, 이 경우 여러 개의 레코드가 검색될 수 있다. 키워드 패턴을 이용한 검색은 다음과 같다.

```
$ altierr –w connect
$ altierr –w “does not”
```



### 참고 사항

Error Message Reference 참조

## altipasswd

### 개요

altipasswd는 $ALTIBASE_HOME/conf/syspassword 파일을 변경한다. 데이터베이스가 서비스 상태가 아닐때는 SYSDBA 옵션으로 iSQL을 구동하여 관리자 작업을 수행하는데, 이때 syspassword 파일을 읽어 sys 계정의 패스워드를 체크한다. 따라서, 데이터베이스 상에서 ALTER USER 문으로 sys 암호를 변경하는 경우, altipasswd로 syspassword 파일의 암호도 동일하게 변경해야 한다. 데이터베이스내의 sys 암호와 syspassword 암호가 동일하게 유지되지 않으면, 데이터베이스 구동, 종료 등 SYSDBA 작업을 할 때 오류가 발생하게 된다.

```
altipasswd
```



### 구문

![](media/Utilities/altipasswd.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04613" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3304" image_path_raw="media/Utilities/altipasswd.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altipasswd ::=
    altipasswd
```
<!-- IMG_RECOVERY_END ref_id="img-04613" -->


### 설명

SYS 사용자의 암호를 변경한다.

### 사용예

SYS 사용자의 암호 “manager”를 “manager1234”로 변경한다면 쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ altipasswd
Previous Password : manager
New Password : manager1234
Retype New Password : manager1234
```



## altiProfile

### 개요

Altibase 서버 내에서 수행되는 작업과 서버의 상태 정보를 파일로 기록하여 분석할 수 있다. 서버가 남긴 상태 파일을 프로파일이라 하며 altiProfile은 이 프로파일을 문자 형태로 변환하여 출력하거나, STATEMENT 관련 데이터만 추출하여 통계 정보를 구축하여 출력한다. 이 정보를 사용하여 사용자는 시스템의 상태를 분석할 수 있다.

```
altiProfile [-stat query|session] {profile_name [profile_name2 [profile_name3] ...}
```



### 구문

![](media/Utilities/altiprofile.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04614" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3337" image_path_raw="media/Utilities/altiprofile.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiprofile ::=
    altiProfile
        [ -h
        | -stat { query | session } ]
        profile_name { profile_name }
```
<!-- IMG_RECOVERY_END ref_id="img-04614" -->


### 파라미터

| 파라미터             | 설명                                                         |
| -------------------- | ------------------------------------------------------------ |
| \-h                  | 도움말을 출력한다.                                           |
| \-stat query/session | 서버가 남긴 프로파일에서 STATEMENT의 통계 정보를 구축하여, 텍스트와 CSV 형태의 파일로 출력한다. <br />구축되는 통계 정보에 대한 자세한 설명은 아래의 "사용 방법"을 참고하기 바란다. |

### 설명

서버가 남긴 프로파일을 문자 형태로 변환하거나, STATEMENT 관련 데이터만 추출하여 통계 정보를 구축한다.

### 사용예

```
iSQL> ALTER SYSTEM SET QUERY_PROF_FLAG = 1;
Alter success.
iSQL> ALTER SYSTEM SET TIMED_STATISTICS = 1;
Alter success.
iSQL> 	 --(Execute an SQL query here.)

$ cd $ALTIBASE_HOME/trc
$ altiProfile alti-1286503704-0.prof

$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof
```



### 사용 방법

서버의 상태 및 작업 내용을 기록하려면 QUERY_PROF_FLAG 프로퍼티를 0보다 큰 값으로 설정하여야 한다. QUERY_PROF_FLAG 프로퍼티의 값에 따라 다음의 정보들이 기록된다.

| 값   | 이름           | 설명                                                         |
| ---- | -------------- | ------------------------------------------------------------ |
| 0    |                | 기록하지 않음                                                |
| 1    | [STATEMENT]    | SQL 문이 실행될 때마다 실행된 SQL문, 실행시간, 실행정보, 색인 및 디스크 접근 정보 출력. <br />단, 실행시간이 제대로 출력되게 하려면 TIMED_STATISTICS 프로퍼티를 1로 설정해야 한다. <br />TIMED_STATISTICS 프로퍼티에 대한 자세한 설명은 *General Reference*를 참조하기 바란다. |
| 2    | [BIND]         | SQL 문이 실행될 때마다 BIND 파라미터 출력                    |
| 4    | [PLAN]         | SQL 문이 실행될 때마다 실행계획 출력                         |
| 8    | [SESSION STAT] | 3초마다 세션 정보 출력(V\$SESSTAT 정보)                      |
| 16   | [SYSTEM STAT]  | 3초마다 시스템 정보 출력(V\$SYSSTAT 정보)                    |
| 32   | [MEMORY STAT]  | 3초마다 메모리 정보 출력(V\$MEMSTAT 정보)                    |

위의 값을 조합하여 원하는 정보를 기록하도록 설정한다. 예를 들어, 프로퍼티를 1+4+32=37로 설정하면 SQL 문이 실행될 때마다 SQL 문의 실행정보와 실행계획을 출력하고 3초마다 메모리 정보를 출력한다.

프로퍼티가 설정되면, 서버는 alti-\#시간-\#번호.prof 이름의 파일에 정보를 남긴다. 사용자는 altiProfile 명령어로 상태 파일을 변환하여 분석할 수 있다.

##### 통계 정보 출력

altiProfile은 -stat 옵션을 사용해서 실행된 SQL문에 대한 통계 정보를 구축하고 출력할 수 있다. 이 정보는 튜닝 대상이 되는 SQL문을 찾는데 도움이 된다.

\-stat query 옵션을 실행하여 구축되는 통계 정보는 아래와 같다.

-   COUNT: QUERY가 실행된 횟수

-   AVG: QUERY 수행에 걸린 평균 시간 (microseconds 단위)

-   TOTAL: QUERY 수행에 걸린 시간 합계 (microseconds 단위)

-   MIN: QUERY 수행에 걸린 최소 시간 (microseconds 단위)

-   MAX: QUERY 수행에 걸린 최대 시간 (microseconds 단위)

-   SUCCESS: QUERY 실행에 성공한 횟수

-   FAIL: QUERY 실행에 실패한 횟수

-   QUERY: 수행된 SQL문

\-stat session 옵션으로 수행한다면, query 옵션을 실행하여 구축되는 통계 정보에 SESSION ID가 추가된다.

아래는 \$ALTIBASE_HOME/trc 디렉토리에 생성된 모든 프로파일을 분석하여 SQL문 별로 통계 정보를 구축하는 altiProfile 실행 예제이다.

```
$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof

### Processing [/altibase_home/trc/alti-1423543095-0.prof]...
100% [====================]

### Writing CSV File [alti-prof-stat-1423543711.csv]...

### Writing TEXT File [alti-prof-stat-1423543711.txt]...

### Successfully done.

```

위에 실행 로그를 살펴보면, 통계 정보는 CSV 형식과 텍스트 형식의 파일로 저장된다. 출력된 파일의 이름은 'alti-prof-stat-\#시간.csv'과 'alti-prof-stat-\#시간.txt'로 자동 생성된다.

다음은 텍스트 파일의 내용이다. 통계 정보는 TOTAL 값으로 정렬되어 출력된다.



```
$cat alti-prof-stat-1423543711.txt
COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     5     0.003730     0.018650     0.003035     0.004640     5     0    DROP VIEW REVENUE
     5     0.003523     0.017616     0.003004     0.003745     5     0    CREATE VIEW REVENUE (
...

```

다음은 CSV 파일의 내용이다. 텍스트 파일과 동일한 내용이 CSV 형식으로 출력된다. CSV 형식의 파일은 excel 같은 스프레드시트 애플리케이션을 사용해서 사용자가 원하는 포맷으로 가공할 수 있다.

```
$ cat alti-prof-stat-1423543711.csv
COUNT,AVG,TOTAL,MIN,MAX,SUCCES,FAIL,QUERY
5,  0.003730,  0.018650,  0.003035,  0.004640,5,0,"DROP VIEW REVENUE"
5,  0.003523,  0.017616,  0.003004,  0.003745,5,0,"CREATE VIEW REVENUE (
...

```



### 주의 사항

프로파일링 기능을 동작시킬 경우, 서버 내에서 실행되는 모든 SQL 문에 대해 실행 정보를 기록하며 또한 매 3초마다 세션 및 시스템 정보 등 서버의 상태를 기록하므로 시스템에 부하를 줄 수 있다.

또한 프로파일링 기능을 설정할 때 프로파일이 커져 디스크가 꽉 찰 수 있으므로 신중해야 한다.

### 출력항목

다음과 같은 형식으로 출력된다.

```
[BIND]
..
[PLAN]
..
[STATEMENT]
..
[SESSION STAT]
..
[SYSTEM STAT]
..
[MEMORY STAT]
..

```

각 정보는 아래와 같은 형식으로 출력된다.

##### [BIND]

SQL 문에 바인드 되는 변수들에 대한 정보이다.

##### [PLAN]

실행된 SQL 문의 실행 계획이 출력된다. 실행 계획에 관한 자세한 내용은 *Performance Tuning Guide*를 참고한다.

##### [STATEMENT]

다음의 표는 실행한 STATEMENT에 대한 정보를 나타낸다.

| 필드 이름                              | 값           | 설명                                                       |
| -------------------------------------- | ------------ | ---------------------------------------------------------- |
| SQL                                    | 문자열       | 실행된 SQL 문                                              |
| **User Info**                          |              |                                                            |
| User ID                                | INTEGER      | 사용자 식별자                                              |
| Client PID                             | BIGINT       | 클라이언트 프로세스 아이디                                 |
| Client Type                            | VARCHAR(40)  | 접속한 클라이언트의 타입                                   |
| Client AppInfo                         | VARCHAR(128) | 클라이언트의 정보 문자열                                   |
| **Elapsed Time for this SQL statemen** |              |                                                            |
| Total                                  | BIGINT       | 총 쿼리 수행 시간                                          |
| Parse                                  | BIGINT       | 파싱 수행 시간                                             |
| Valid                                  | BIGINT       | 정당성 검사 수행 시간                                      |
| Optim                                  | BIGINT       | 최적화 수행 시간                                           |
| Execu                                  | BIGINT       | 실행 수행 시간                                             |
| Fetch                                  | BIGINT       | Fetch 수행 시간                                            |
| **Query Execute Info**                 |              |                                                            |
| EXECUTE Result                         | INTEGER      | 0: failure 1: rebuild 2: retry 3: queue empty 4: success   |
| Optimizer Mode                         | BIGINT       | 최적화 모드                                                |
| Cost Mode                              | BIGINT       | 최적화 비용                                                |
| Used Memory                            | BIGINT       | 향후 확장 예정                                             |
| SUCCESS SUM                            | BIGINT       | 실행 성공 횟수의 총합                                      |
| FAILURE SUM                            | BIGINT       | 실행 실패 횟수의 총합                                      |
| PROCESSED ROW                          | BIGINT       | 처리된 레코드 개수                                         |
| **Result Set Info**                    |              |                                                            |
| FETCH Result                           | INTEGER      | 0: failure 1: success 2: no results                        |
| **Index Access Info**                  |              |                                                            |
| Memory Full Scan Count                 | BIGINT       | 메모리 테이블에 대한 Full Scan이 발생한 횟수               |
| Memory Index Scan Count                | BIGINT       | 메모리 테이블에 대한 Index Scan이 발생한 횟수              |
| Disk Full Scan Count                   | BIGINT       | 디스크 테이블에 대한 Full Scan이 발생한 횟수               |
| Disk Index Scan Count                  | BIGINT       | 디스크 테이블에 대한 Iindex Scan이 발생한 횟수             |
| **Disk Access Info**                   |              |                                                            |
| READ DATA PAGE                         | BIGINT       | 질의 수행 시 디스크 페이지에 대한 읽기 연산 횟수           |
| WRITE DATA PAGE                        | BIGINT       | 사용하지 않음                                              |
| GET DATA PAGE                          | BIGINT       | 질의 수행 시 디스크 페이지에 대한 버퍼 접근 횟수           |
| CREATE DATA PAGE                       | BIGINT       | 질의 수행 시 디스크 페이지 생성 횟수                       |
| READ UNDO PAGE                         | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지에 대한 읽기 연산 횟수 |
| WRITE UNDO PAGE                        | BIGINT       | 사용하지 않음                                              |
| GET UNDO PAGE                          | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지에 대한 버퍼 접근 횟수 |
| CREATE UNDO PAGE                       | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지 생성 횟수             |

##### [SESSION STAT]

매 3초마다 V\$SESSTAT 정보가 출력된다. V\$SESSTAT의 자세한 내용은 *General Reference* 의 성능 뷰 부분을 참고한다.

##### [SYSTEM STAT]

매 3초마다 V\$SYSSTAT 정보가 출력된다. V\$SYSSTAT의 자세한 내용은 *General Reference*의 성능 뷰 부분을 참고한다.

##### [MEMORY STAT]

매 3초마다 V\$MEMSTAT 정보가 출력된다. V\$MEMSTAT의 자세한 내용은 *General Reference*의 성능 뷰 부분을 참고한다.

## altiwrap

### 개요

altiwrap은 PSM(Persistent Stored Module)으로 작성된 코드 프로그램을 암호화할 수 있는 유틸리티이다. altiwrap을 사용하여 코드를 암호화하면 다른 개발자에게 저장 프로시저 및 저장 함수 등의 PSM 코드가 노출되는 것을 방지할 수 있다.

```
altiwarp {--iname input_file} [--oname output_file]
```



### 구문

![altiwrap](media/Utilities/altiwrap.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04615" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3560" image_path_raw="media/Utilities/altiwrap.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiwrap ::=
    altiwrap
        { -h
        | --h
        | --iname input_file [ --oname output_file ] }
```
<!-- IMG_RECOVERY_END ref_id="img-04615" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-h/--h  | 도움말을 출력한다.                                           |
| \--iname | 암호화 할 파일의 이름을 지정한다. 파일의 확장자를 생략하면, '.sql'로 인식한다. |
| \--oname | 코드 프로그램이 암호화되어 저장될 파일의 이름을 지정한다. <br />파일의 확장자를 생략하면, '.plb'로 저장된다. |

### 설명

altiwrap을 실행하여 개발자가 작성한 저장 프로시저 및 저장 함수의 코드 프로그램을 암호화하여, 다른 개발자 또는 경쟁사에 노출되는 것을 방지할 수 있다.

Altibase가 암호화할 수 있는 구문은 아래와 같다.

-   CREATE [OR REPLACE] PROCEDURE

-   CREATE [OR REPLACE] FUNCTION

-   CREATE [OR REPLACE] TYPESET

-   CREATE [OR REPLACE] PACKAGE

-   CREATE [OR REPLACE] PACKAGE BODY

### 주의 사항

-   코드 프로그램이 암호화 된 후에는 프로그램을 변경할 수 없다. 프로그램을 변경할 때에는 암호화 전의 원본 프로그램에서 변경한 후 다시 암호화해야 한다.
    
-   트리거(trigger)는 암호화할 수 없다.

-   암호화된 프로그램 코드는 구문(syntax) 및 시맨틱(semantic)의 오류를 검사하지 못한다.

### 사용예제

altiwrap을 사용하여 sample1.sql 파일을 암호화한 후, 암호화된 파일을 출력한다.

아래는 sample1.sql 파일이다.

```
iSQL> create or replace procedure proc1 as
type arr1 is table of char(30) index by integer;
v1 arr1;
begin
v1[0] := 'create or replace';
v1[1] := 'typeset';
v1[2] := 'is';
v1[3] := 'success';
println( v1[0] || v1[1] || v1[2] || v1[3] || '!' );
end;
/
```

sample1.sql 파일을 암호화한다.

```
$ altiwrap --iname sample1.sql --oname --sample1.plb
```

암호화된 코드 프로그램을 isql에서 실행하면 된다.

```
iSQL> @sample1.plb
iSQL> create or replace procedure proc1 WRAPPED
'MjQz
MTk2
AAhjcmVhdGUgb3IgcmVwbGFjZSBwcm9jZWR1cqQBAAQxIGFzCnR5cGUgYXJyMSBpcyB0YWJsQAYAAWYgY2hhcigzMCkgaW5kZXggYnlAAQZ0ZWdlcjsKdjGYBQAEOwpiZWdpbgp2MVswXSA6PSAnY3JlYSu5ASdyBVsxtAN/DHNldK0CMq4CaXO5ATO4AQNzdWNjZXNsAgZwcmludGxuKCC2C3x8YAFACaABVAegAVwGDHx8ICchJyApOwplbmQ7ChEAADVBRDlBRkIzMDE0MzI1Q0U0MzY1RjYxNEI2NkYwQzRDREMzMTdDQTU=
';
/
Create success.
iSQL> exec proc1;
create or replace typeset is success!
Execute success.
```



## awrite

### 개요

로그 파일을 생성할 때 사용되는 시스템 콜의 응답 시간을 출력한다. 출력 값은 LOG_CREATE_METHOD 프로퍼티에서 시스템 콜을 결정하는데 참고된다.

### 구문

![awrite](media/Utilities/awrite.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04616" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3646" image_path_raw="media/Utilities/awrite.gif" image_class="C" format="bnf" verified="True" -->
```bnf
awrite ::=
    awrite
```
<!-- IMG_RECOVERY_END ref_id="img-04616" -->


### 설명

write()와 fallocate() 시스템 콜의 응답 시간을 출력한다.

### 사용예

아래와 같은 결과를 출력한다.

```
$ awrite
fallocate to expand file size to 1GB
 Elapsed Time ==>            2.564 seconds
write to expand file size to 1GB
 Elapsed Time ==>            4.020 seconds
```



## checkServer

### 개요

Altibase 프로세스를 감시하며, 프로세스가 비정상 종료하면 지정된 스크립트 파일을 실행한다.

```
checkServer [-n] {-f server-restart-script-file}
```



### 구문

![checkserver](media/Utilities/checkserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04617" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3680" image_path_raw="media/Utilities/checkserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
checkserver ::=
    checkServer [ -n ] -f server-restrat-script-file
```
<!-- IMG_RECOVERY_END ref_id="img-04617" -->


### 파라미터

| 파라미터 | 설명                                                                                |
|----------|-------------------------------------------------------------------------------------|
| \-n      | checkServer를 foreground에서 수행 파라미터 생략시 checkServer는 background에서 수행 |
| \-f      | Altibase 종료시 실행할 스크립트 파일의 이름                                         |

### 설명

checkServer는 주기적으로 Altibase 프로세스가 실행 중인지를 검사하여 Altibase 프로세스가 종료 되었을 경우 사용자가 지정한 스크립트를 수행한다.

Altibase가 비정상 종료 되었을 경우 Altibase 재구동 스크립트를 수행하는 것이 일반적이며, 재구동 스크립트는 다음과 같은 형식으로 작성할 수 있다.

-   Altibase 구동 스크립트 ‘restart.sh’

```
#! /bin/sh
${ALTIBASE_HOME}/bin/server start
```

checkServer는 구동시 \$ALTIBASE_HOME/trc 디렉토리에 checkServer.pid와 checkServer.log 파일을 생성한다. checkServer.pid파일은 또 다른 checkServer가 동시에 수행되지 못하도록 하는 락의 역할을 하며 checkServer.log에는 checkServer의 동작 상태가 주기적으로 기록된다.

checkServer를 ‘kill -9’등의 방법으로 강제 종료했을 경우에 checkServer.pid 파일이 디렉터리에 계속 남아있게 되어 checkServer를 다시 수행할 수 없게 된다. 이 때는 checkServer.pid파일을 삭제하면 checkServer를 정상적으로 시작할 수 있다.

checkServer를 종료하기 위해선 반드시 killCheckServer 유틸리티를 이용한다.

### 주의 사항

checkServer는 Altibase 서버가 “server stop” 커맨드를 사용하지 않고 종료된 경우에만, 지정한 재시작 스크립트를 실행한다. “server stop” 커맨드를 사용하여 Altibase 서버를 정상 종료하는 경우, checkServer 프로세스도 역시 종료되어, 재시작 스크립트를 실행하지 않게 된다. 이것은 checkServer가 “server stop” 커맨드를 사용하여 종료하는 것만 정상 종료라고 판단하기 때문이다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ checkServer –f restart.sh &
```



## dumpbi

### 개요

dumpbi는 이진 형식으로 저장된 backupinfo 파일의 백업 정보를 문자 형식으로 보여준다.

```
dumpbi  <backupinfo_file_name>
```



### 구문

![dumpbi](media/Utilities/dumpbi.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04618" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3736" image_path_raw="media/Utilities/dumpbi.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpbi ::=
    dumpbi backupinfo_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-04618" -->


### 설명

backupinfo 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpbi backupinfo
```



### 출력 항목

dumpbi는 backupinfo 의 백업 정보를 다음과 같은 섹션으로 구분하여 출력한다.

##### [BACKUO INFO FILE HDR]

| 필드 이름              | 값(단위 바이트)                 | 설명                                                         |
| ---------------------- | ------------------------------- | ------------------------------------------------------------ |
| Backup info slot count | 0 \~ unsigned int 타입의 최대값 | 저장되어 있는 backupinfo slot의 수<br />(= 현재까지 백업된 파일의 수) |
| Last backup LSN        | FileNo, Offset                  | 가장 최근에 수행된 백업 시점의 LSN<br />(유효한 backupinfo 파일인지 검증하기 위한 값) |
| Database name          | 문자열                          | 데이터베이스 이름                                            |

##### [BACKUP INFO SLOT]

| 필드 이름                     | 값(단위 바이트)                                              | 설명                                                         |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Slot index                    | 0 \~ unsigned int 타입의 최대값                              | slot의 순번                                                  |
| Begin backup time             | YYYY-MM-DD HH:MM:SS                                          | 백업 시작 일시                                               |
| End backup time               | YYYY-MM-DD HH:MM:SS                                          | 백업 완료 일시                                               |
| Incremental backup chunk cnt  | 0 \~ unsigned int 타입의 최대값                              | 데이터파일에서 변경된 페이지를 포함한 incremental chunk의 수<br />(= 백업된 incremental chunk의 수) |
| Incremental backup chunk size | 0 \~ unsigned int 타입의 최대값                              | 백업이 수행될 당시의 INCREMENTAL_BACKUP_CHUNK_SIZE의 값      |
| Backup target                 | 1: DATABASE <br />2: TABLESPACE                              | 백업 대상                                                    |
| Backup level                  | 1: level 0 <br />2: level 1                                  | 백업 레벨                                                    |
| Backup Type                   | 1: full backup <br />2: differentail backup <br />3: cumulative backup | 백업 유형                                                    |
| Tablespace ID                 | 0 \~ unsigned short 타입의 최대값                            | 백업 대상 데이터파일이 속한 테이블스페이스의 ID              |
| File ID                       | 0 \~ unsigned short 타입의 최대값                            | 백업 대상 데이터파일의 ID                                    |
| Original file size            | 0 \~ unsigned long 타입의 최대값                             | 백업된 시점의 데이터파일 크기                                |
| Backup Tag                    | 문자열                                                       | 백업 태그 이름                                               |
| Backup file name              | 문자열                                                       | 백업 파일의 경로와 이름                                      |

## dumpct

### 개요

dumpct는 이진 형식으로 저장된 changeTracking 파일의 정보를 문자 형식으로 보여준다.

```
dumpct  <changeTracking_file_name>
```



### 구문

![dumpct](media/Utilities/dumpct.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04619" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3796" image_path_raw="media/Utilities/dumpct.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpct ::=
    dumpct changeTracking_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-04619" -->


### 설명

changeTracking 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpct changeTracking
```



### 출력

dumpct는 changeTracking 파일 내의 변경 추적 정보를 다음과 같은 

[^]: 

으로 구분하여 출력한다.

##### [CHANGE TRACKING FILE HDR]

| 필드 이름                    | 값(단위 바이트)                 | 설명                                                                                                                                                  |
|------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change tracking body count   | 0 \~ unsigned int 타입의 최대값 | changeTracking 파일이 가진 body의 수 (changeTracking 파일은 header와 body로 나뉜다. body의 크기는 10Mbytes이며 공간이 부족하면 바디 단위로 확장된다.) |
| Icremental backup chunk size | 0 \~ unsigned int 타입의 최대값 | changeTracking 파일 생성시점의 INCREMENTAL_BACKUP_CHUNK_SIZE 프로퍼티 값                                                                              |
| Last flush LSN               | FileNo, Offset                  | 메모리상의 변경된 데이터가 파일로 기록된 시점의 LSN                                                                                                   |
| Database name                | 문자열                          | 데이터베이스 이름                                                                                                                                     |

##### [CHANGE TRACKING FILE BODY]

| 필드 이름                     | 값(단위 바이트)                   | 설명                                    |
| ----------------------------- | --------------------------------- | --------------------------------------- |
| Change tracking body ID       | 0 \~ unsigned int 타입의 최대값   | body의 ID                               |
| Flush LSN                     | FileNo, Offset                    | body가 flush 된 시점의 LSN(파일 검증용) |
| **Datafile descriptor slot**  |                                   |                                         |
| Slot ID                       | 0 \~ unsigned int 타입의 최대값   | slot의 ID                               |
| Tracking state                | 0: 추적 비활성화 1: 추적 활성화   | 데이터파일 변경 사항 추적 상태          |
| Tablespace type               | 0: memory TBS 1: disk TBS         | 테이블스페이스 유형                     |
| Page size                     | 0 \~ unsigned int 타입의 최대값   | 페이지 크기                             |
| Bitmap extent count           | 0 \~ unsigned short 타입의 최대값 | 할당된 비트맵 익트텐트 개수             |
| Current tracking list ID      | 0 \~ unsigned short 타입의 최대값 | 현재 추적중인 bitmap extent list의 ID   |
| **Differential0 BmpExt list** |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| **Differential1 BmpExt list** |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| **Cumulative BmpExt list**    |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| Tablespace ID                 | 0 \~ unsigned short 타입의 최대값 | 데이터파일이 속한 테이블스페이스의 ID   |
| File ID                       | 0 \~ unsigned short 타입의 최대값 | 데이터파일의 ID                         |

## dumpdb

### 개요

dumpdb는 메모리 체크포인트 이미지 파일로부터 메모리 테이블스페이스에 대한 정보를 출력하거나 또는 메모리 테이블스페이스의 증분 백업 파일의 내용을 문자 형식으로 보여주는 유틸리티이다.

```
dumpdb {-j job_number } [-i pingpong_number] [-o] [-f file_name] [-s] [-p] [-d]
```



### 구문

![dumpdb](media/Utilities/dumpdb.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04620" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="3868" image_path_raw="media/Utilities/dumpdb.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpdb ::=
    dumpdb -j job_number
        [ -i pingpong_number ]
        [ -o ]
        [ -f file_name ]
        [ -s ]
        [ -p ]
        [ -d ]
```
<!-- IMG_RECOVERY_END ref_id="img-04620" -->


### 파라미터

| 파라미터            | 설명                                                         |
| ------------------- | ------------------------------------------------------------ |
| \-j job_number      | 어떤 정보를 출력할 것인지를 지정한다. 지정 가능한 값과 각 값에 대해 추가로 지정할 수 있는 인자는 다음과 같다. <br />0: META (-s -f) <br />1: TABLESPACE (-s -f) 2: TABLESPACE-FLI (-s -d) <br />3: TABLESPACE-FREE-PAGE-LIST (-s) <br />4: TABLE (-o -d)<br />5: TABLE-ALLOC-PAGE-LIST (-o) <br />6: PAGE (-s -p -d) <br />7: INCREMENTAL_BACKUP_META (-f) |
| \-i pingpong_number | 체크포인트 이미지 파일의 핑퐁 번호이다. 생략하면 0이 사용된다. |
| \-o                 | 분석할 객체의 ID를 지정한다.                                 |
| \-f file_name       | 체크포인트 이미지 파일의 이름을 지정한다.                    |
| \-s                 | 분석할 테이블스페이스의 ID를 지정한다.                       |
| \-p                 | 분석할 페이지의 ID를 지정한다.                               |
| \-d                 | 정보를 상세히 출력한다.                                      |

### 설명

메모리 체크포인트 이미지 파일을 분석하여 메타 헤더, 페이지 등의 정보를 텍스트 형태로 출력하거나 또는 메모리 테이블스페이스의 증분 백업 파일에서 백업 정보를 텍스트 형태로 출력한다.

이 유틸리티는 디스크에 저장된 체크포인트 이미지 파일을 분석하기 때문에, Altibase 서버가 구동 중이 아니더라도 이 유틸리티를 수행하여 데이터베이스에 생성되어 있는 스키마를 확인할 수 있다.

하지만 DDL 직후 서버가 비정상 종료되어 갱신된 스키마가 디스크에 기록되지 못하면 해당 정보를 확인할 수 없다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpdb -j 1
$ dumpdb -j 1 -s 0
$ dumpdb -j 2
$ dumpdb -j 3
$ dumpdb -j 4
$ dumpdb -j 4 -d
$ dumpdb -j 4 -o 65536
$ dumpdb -j 5 -o 65536
$ dumpdb -j 6 -s 0 -p 4
```

\<예제 1\> 다음은 메모리 테이블스페이스에 관한 정보를 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수도 있다.

```
$ dumpdb -j 1
```

\<예제 2\> 다음은 메모리 테이블스페이스의 FreeListInfo(FLI) 페이지에 관한 정보를 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수 있고, -d 인자를 추가해서 FLI 페이지의 유효하지 않은 부분도 출력할 수 있다.

```
% dumpdb -j 2
```

\<예제 3\> 다음은 메모리 테이블스페이스의 FreePage들을 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수도 있다.

```
% dumpdb -j 3
```

\<예제 4\> 다음은 데이터베이스에 생성되어 있는 모든 객체 정보를 출력한다. –o 인자(아래 예제에서 SelfOID 항목)를 추가하여 특정 객체에 관한 정보만 상세히 출력할 수도 있다. –d 인자를 추가해서 객체의 칼럼 정보와 인덱스 정보 등도 출력할 수 있다.

```
% dumpdb -j 4
```

\<예제 5\> 다음은 데이터베이스에 생성되어 있는 모든 객체의 정보를 칼럼 정보와 인덱스 정보 등과 함께 출력한다.

```
% dumpdb -j 4 -d
```

\<예제 6\> 다음은 특정 테이블의 스키마와 데이터를 출력한다.

```
% dumpdb -j 4 -o 65568
```

\<예제 7\> 다음은 특정 테이블이 사용하는 페이지 목록을 출력한다.

```
% dumpdb -j 5 -o 65568
```

\<예제 8\> 다음은 메모리 데이터베이스의 특정 페이지를 출력한다.

```
% dumpdb –j 6 -s 0 -p 4
```

\<예제 9\> 다음은 증분 백업 파일에 대해 dumpdb를 수행하여 백업 정보를 출력한다.

```
% dumpdb -j 7 -f SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak
dumpdb: Release 6.3.1.0.0 - Production on Oct 31 2012 22:12:21
(c) Copyright 2001 ALTIBase Corporation.  All rights reserved.
 
[BEGIN CHECKPOINT IMAGE HEADER]
Binary DB Version             [ 6.2.1 ]
Redo LSN       [ 1, 5867599 ]
Create LSN     [0, 1385 ]
DataFileDescSlot ID           [ 1, 1 ] 
 
//백업파일에 저장된 incremental backup정보
  [BEGIN BACKUPFILE INFORMATION]
 
        Begin Backup Time             [ 2012_11_06 23:18:43 ]
        End Backup Time               [ 2012_11_06 23:18:44 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 1 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END CHECKPOINT IMAGE HEADER]
 
Dump complete.
```



### 출력 항목

다음의 표는 증분 백업 파일에 대해 dumpdb 유틸리티를 실행하여 출력되는 항목들에 한하여 설명한다.

| 필드 이름           | 설명                                                                                                                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary DB Version   | 데이터 파일의 버전                                                                                                                              |
| Redo LSN            | 미디어 복구를 위한 Redo LSN. 로그 앵커의 Redo LSN값이 데이터 파일의 Redo LSN보다 크면, 이 항목에 출력되는 Redo LSN 부터 미디어 복구가 필요하다. |
| Create LSN          | 체크포인트 이미지 생성 시점의 LSN                                                                                                               |
| DataFileDescSlot ID | 메모리 체크포인트 이미지와 묶여있는 ChangeTracking의 DataFileDescSlot ID                                                                        |

## dumpddf

### 개요

dumpddf는 데이터 파일의 헤더 정보 또는 데이터 파일 내의 특정 페이지를 출력한다. 또는 증분 백업 파일에 대해 dumpddf를 수행하면 백업 파일의 헤더 정보와 백업 정보가 출력된다.

```
dumpddf {-f datafile_name} {-m | -p pid}
```



### 구문

![dumpddf](media/Utilities/dumpddf.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04621" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4015" image_path_raw="media/Utilities/dumpddf.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpddf ::=
    dumpddf -f datafile_name { -m | -p pid }
```
<!-- IMG_RECOVERY_END ref_id="img-04621" -->


### 파라미터

| 파라미터 | 설명                                                                                                                    |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| \-f      | 정보를 얻고 싶은 데이터 파일의 이름 이 옵션은 반드시 입력해야 한다. 생략하면 dumpddf는 에러 메시지를 출력하고 종료한다. |
| \-m      | 데이터 파일의 헤더 정보를 출력한다.                                                                                     |
| \-p      | 정보를 얻고 싶은 데이터 파일내의 페이지 ID                                                                              |

### 설명

데이터 파일의 헤더의 정보 또는 데이터 파일 내의 특정 페이지를 텍스트 형태로 출력한다. 지정한 페이지가 테이블이나 인덱스의 페이지이면 논리적으로 구성하여 출력한다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpddf –f datafile –m
$ dumpddf –f datafile –p page_id
```



### 출력 항목

다음은 dumpddf의 출력 예이다.

```
[BEGIN DATABASE FILE HEADER]
Binary DB Version             [ 5.4.1 ]
Redo LSN                      [0, 734497 ]
Create LSN                    [0, 1886 ]
MustRedo LSN                  [0, 0 ]
```

출력 내용 중, 필드들은 다음과 같은 의미를 갖는다.

| 필드 이름           | 설명                                                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Binary DB Version   | 데이터 파일의 버전                                                                                                             |
| Redo LSN            | 미디어 복구를 위한 Redo LSN. 로그앵커의 Redo LSN값이 데이터 파일의 Redo LSN보다 크면, 이 Redo LSN 부터 미디어 복구가 필요하다. |
| Create LSN          | 데이터 파일 생성 시점의 LSN                                                                                                    |
| MustRedo LSN        | 미디어 복구 시 이 Redo LSN까지 수행해야 한다.                                                                                  |
| DataFileDescSlot ID | Disk datafile과 묶여있는 ChangeTracking의 DataFileDescSlot ID                                                                  |

다음은 증분 백업 파일을 dumpddf로 출력한 예이다.

```
% dumpddf -m -f system001.dbf_TAG_MONDAY.ibak
-----------------------------------------------------------------
     Altibase Client Dump Disk Database File utility.
     Release Version 6.3.1.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[BEGIN DATABASE FILE HEADER]
 
Binary DB Version             [ 6.2.1 ]
Redo LSN                      [1, 5867599 ]
Create LSN                    [0, 1914 ]
MustRedo LSN                  [0, 0 ]
DataFileDescSlot ID           [ 1, 2 ]
 
[BEGIN BACKUPFILE INFORMATION] -->백업파일에 저장된 incremental backup정보
 
        Begin Backup Time             [ 2012_11_06 23:18:44 ]
        End Backup Time               [ 2012_11_06 23:18:46 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 2 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/system001.dbf_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END DATABASE FILE HEADER]

```



## dumpla

### 개요

dumpla는 이진 형식으로 저장된 loganchor 파일의 내용을 문자 형식으로 보여준다.

loganchor는 Altibase의 물리적인 저장 정보(테이블스페이스, 데이터 파일)와 복구를 위해 필요한 정보들이 저장되는 파일이다. Altibase는 데이터베이스 생성 시(CREATE DATABASE 실행 시)에 이 파일을 생성하고 altibase.properties에 설정된 세 개의 LOGANCHOR_DIR 디렉토리에 loganchor\#(\#은 1, 2, 3)의 이름으로 저장, 관리한다. 세 개의 파일은 모두 같은 내용으로 파일이 손상될 경우를 대비해 복사본을 유지하는 것이다. 데이터베이스 생성 시에 현재 데이터베이스에 존재하는 테이블스페이스와 이에 속한 데이터 파일, 그리고 복구 관련 정보들이 저장된다. 데이터베이스 구동 시에 이 정보들을 이용하여 데이터베이스를 메모리에 적재하고 서비스를 준비한다.

```
dumpla <loganchor_file_name>
```



### 구문

![dumpla](media/Utilities/dumpla.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04622" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4117" image_path_raw="media/Utilities/dumpla.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpla ::=
    dumpla loganchor_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-04622" -->


### 설명

loganchor 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpla loganchor0
```



### 출력 항목

dumpla는 loganchor의 내용을 다음과 같은 섹션으로 구분하여 출력한다.

##### [LOGANCHOR ATTRIBUTE SIZE]

현재 Loganchor에 어떤 데이터들이 얼마만큼의 공간을 사용하고 있는지를 나타낸다. 내용은 다음과 같다.

| 필드 이름                  | 값(단위 바이트)                 | 설명                                                                                    |
|----------------------------|---------------------------------|-----------------------------------------------------------------------------------------|
| Loganchor Static Area      | 0 \~ unsigned int 타입의 최대값 | Loganchor에 고정적으로 들어가는 정보의 크기를 나타낸다. 주로 복구 시 필요한 정보들이다. |
| Tablespace Attribute       | 0 \~ unsigned int 타입의 최대값 | 저장된 Tablespace Attribute의 크기                                                      |
| Checkpoint Path Attribute  | 0 \~ unsigned int 타입의 최대값 | 저장된 Checkpoint Path의 크기                                                           |
| Checkpoint Image Attribute | 0 \~ unsigned int 타입의 최대값 | 저장된 Checkpoint Image Attribute의 크기                                                |
| Disk Datafile Attribute    | 0 \~ unsigned int 타입의 최대값 | 저장된 Disk Datafile Attribute의 크기                                                   |

##### [LOGANCHOR HEADER]

데이터베이스의 버전 및 체크포인트 Log Sequence Number (LSN) 등의 loganchor Header 정보를 나타낸다. LSN에 대한 자세한 설명은 “dumplf 의 출력”절을 참고하기 바란다.

| 필드 이름                         | 값                                   | 설명                                                                                                                                                                                                                      |
|-----------------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary DB Version                 | Major.minor.patch ex) 6.2.1          | 현재 Loganchor를 생성한 데이터베이스 실행 파일의 데이터베이스 버전이다.                                                                                                                                                   |
| Archivelog Mode                   | Archivelog \|No-Archivelog           | 데이터베이스가 아카이브 모드로 운영 중인지를 나타낸다.                                                                                                                                                                    |
| Transaction Segment Entry Count   |                                      |                                                                                                                                                                                                                           |
| Begin Checkpoint LSN              | FileNo, Offset                       | Begin Checkpoint의 LSN을 나타낸다.                                                                                                                                                                                        |
| End Checkpoint LSN                | FileNo, Offset                       | End Checkpoint의 LSN을 나타낸다.                                                                                                                                                                                          |
| Disk Redo LSN                     | FileNo, Offset                       | DRDB의 Redo 시작 위치를 나타낸다.                                                                                                                                                                                         |
| LSN for Recovery from Replication | FileNo, Offset                       | 이중화를 이용한 복구 시 이 LSN부터 시작한다.                                                                                                                                                                              |
| Server Status                     | SERVER_SHUTDOWN \|SERVER_STARTED     | 서버의 상태를 기록한다. 서버 시작 시 이 값이 SERVER_STARTED로 바뀌고 종료 시 SERVER_SHUTDOWN으로 바뀐다. 서버 시작 시에 이 값이 SERVER_STATED로 되어있다면 이전에 서버가 비정상 종료한 것이므로 재구동시 복구를 수행한다. |
| End LSN                           | FileNo, Offset                       | 서버가 정상 종료한 후 재구동시 첫 번째 기록되는 로그의 LSN                                                                                                                                                                |
| ResetLog LSN                      | FileNo, Offset                       | 불완전 복구시 설정된 Reset LSN                                                                                                                                                                                            |
| Last Created Logfile Num          | 0 \~ unsigned int 타입의 최대값      | 가장 최근에 생성된 로그 파일 번호                                                                                                                                                                                         |
| Delete Logfile(s) Range           | 삭제되는 첫 번째 \~ 마지막 파일 번호 | 가장 최근에 삭제된 로그 파일의 범위. 체크포인트 완료 후 더 이상 필요 없는 파일을 삭제하는데 이 때 지워지는 파일의 범위를 기록한다.                                                                                        |
| Update And Flush Count            | 0 \~ unsigned int 타입의 최대값      | logAnchor 파일이 변경되고 플러시된 횟수                                                                                                                                                                                   |
| New Tablespace ID                 | 0 \~ unsigned int 타입의 최대값      | 새로운 테이블스페이스 식별자. 테이블스페이스가 생성될 경우 이 값을 자신의 테이블스페이스 식별자로 사용하고 이 값을 증가시킨다.                                                                                            |

##### [TABLESPACE ATTRIBUTE]

메모리 테이블스페이스 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                   | 값                                         | 설명                                                                                                                                                                                                                                     |
|-----------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tablespace ID               | 0 \~ unsigned int 타입의 최대값            | 테이블스페이스 식별자                                                                                                                                                                                                                    |
| Tablespace Name             | 문자열 ex) SYS_TBS_MEM_DIC                 | 테이블스페이스 이름                                                                                                                                                                                                                      |
| New Database File ID        | 0 \~ unsigned int 타입의 최대값            | 테이블스페이스에서 새로 파일이 추가될 때 파일이 가지게 될 파일의 식별자                                                                                                                                                                  |
| Extent Management           | FREE EXTENT BITMAP TABLESPACE              | 디스크 테이블스페이스의 extent가 어떤 방식으로 관리되는지를 나타낸다. 현재는 FREE EXTENT BITMAP TABLESPACE만 지원한다. FREE EXTENT BITMAP TABLESPACE를 enable하면, 디스크 테이블스페이스의 free extents를 관리하는데 bitmaps을 사용한다. |
| Tablespace Status           | 아래 TABLESPACE ATTRIBUTE 설명 참조        | 테이블스페이스의 현재 상태를 나타낸다.                                                                                                                                                                                                   |
| Tablespace Type             | 0 \~ 8 아래 TABLESPACE ATTRIBUTE 설명 참조 | 테이블스페이스의 타입                                                                                                                                                                                                                    |
| Checkpoint Path Count       | Checkpoint Path 개수                       | 체크포인트 이미지 파일들의 경로. 메모리 테이블스페이스에만 적용된다.                                                                                                                                                                     |
| Autoextend Mode             | AutoExtend \|Non-AutoExtend                | 테이블스페이스가 자동으로 크기가 확장되는지 여부를 가리킨다. 메모리 테이블스페이스에만 적용된다.                                                                                                                                         |
| Shared Memory Key           | 0 \~ unsigned int 타입의 최대값            | 데이터베이스가 공유 메모리 버전이면 이 때 공유 메모리에 데이터베이스가 사용한 공유 메모리의 키                                                                                                                                           |
| Stable Checkpoint Image Num | 0\|1                                       | 체크포인트가 완료된 체크포인트 이미지의 파일 번호 메모리 테이블스페이스에만 적용된다.                                                                                                                                                    |
| Init Size                   | 0 \~ unsigned int 타입의 최대값            | 초기 크기(Mbyte)                                                                                                                                                                                                                         |
| Next Size                   | 0 \~ unsigned int 타입의 최대값            | 자동 확장되는 증가분의 크기(Mbyte)                                                                                                                                                                                                       |
| Maximum Size                | 0 \~ unsigned int 타입의 최대값            | 최대 크기                                                                                                                                                                                                                                |
| Split File Size             | 0 \~ unsigned int 타입의 최대값            | 메모리 테이블스페이스는 파일을 이 크기 단위로 생성한다. 예를 들어 테이블스페이스가 1G이고, Split file size가 100MB이면 10개의 파일이 생성된다.                                                                                           |

[TABLESPACE ATTRIBUTE] 내용 중 Tablespace Status의 의미는 다음과 같다.

| 값                   | 설명                                                       |
|----------------------|------------------------------------------------------------|
| OFFLINE              | 오프라인 상태                                              |
| ONLINE               | 온라인 상태                                                |
| INCONSISTENT         | 비일관적인 상태                                            |
| CREATING             | 생성 중                                                    |
| DROPPING             | 삭제를 수행한 트랜잭션이 아직 커밋하지 않아 삭제 중인 상태 |
| DROP_PENDING         | 삭제를 수행한 트랜잭션이 커밋 이후 Pending 연산 중인 상태  |
| DROPPED              | 삭제된 상태                                                |
| DISCARDED            | Discard된 상태                                             |
| BACKUP               | 백업 중                                                    |
| SWITCHING_TO_OFFLINE | OFFLINE으로 바뀌고 있는 중                                 |
| SWITCHING_TO_ONLINE  | ONLINE으로 바뀌고 있는 중                                  |

[TABLESPACE ATTRIBUTE] 내용 중 Tablespace Type의 의미는 다음과 같다.

| 값 | 설명                     |
|----|--------------------------|
| 0  | MEMORY SYSTEM DICTIONARY |
| 1  | MEMORY SYSETM DATA       |
| 2  | MEMORY USER DATA         |
| 3  | DISK SYSTEM DATA         |
| 4  | DISK USER DATA           |
| 5  | DISK SYSTEM TEMP         |
| 6  | DISK USER TEMP           |
| 7  | DISK SYSTEM UNDO         |
| 8  | VOLATILE USER DATA       |

##### [MEMORY CHECKPOINT PATH ATTRIBUTE]

메모리 테이블스페이스의 체크포인트 저장 경로를 나타낸다. 내용은 다음과 같다.

| 필드 이름       | 값                              | 설명                          |
|-----------------|---------------------------------|-------------------------------|
| Tablespace ID   | 0 \~ unsigned int 타입의 최대값 | 테이블스페이스 식별자         |
| Checkpoint Path | 문자열                          | 체크포인트 이미지 파일의 경로 |

##### [MEMORY CHECKPOINT IMAGE ATTRIBUTE]

메모리 테이블스페이스의 체크포인트 이미지 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                          | 값                              | 설명                                                                    |
|------------------------------------|---------------------------------|-------------------------------------------------------------------------|
| Tablespace ID                      | 0 \~ unsigned int 타입의 최대값 | 테이블스페이스 식별자                                                   |
| File Number                        | 0 \~ unsigned int 타입의 최대값 | 파일 번호                                                               |
| Create LSN                         | \< FileNo, Offset\>             | 데이터 파일 생성 시점의 LSN                                             |
| Create On Disk (PingPong 0)        | Created\|None                   | 0번 체크포인트 이미지 파일 생성 유무                                    |
| Create On Disk (PingPong 1)        | Created\|None                   | 1번 체크포인트 이미지 파일 생성 유무                                    |
| ChangeTracking DataFileDescSlot ID | 0 \~ unsigned int 타입의 최대값 | Memory checkpoint image와 묶여있는 ChangeTracking의 DataFileDescSlot ID |

##### [DISK DATABASE FILE ATTRIBUTE]

디스크 테이블스페이스의 데이터 파일 저장 경로를 나타낸다. 내용은 다음과 같다.

| 필드 이름                          | 값                                          | 설명                                                          |
|------------------------------------|---------------------------------------------|---------------------------------------------------------------|
| Tablespace ID                      | 0 \~ unsigned int 타입의 최대값             | 테이블스페이스 식별자                                         |
| Database File ID                   | 0 \~ unsigned int 타입의 최대값             | 데이터 파일 식별자                                            |
| Database File Path                 | 문자열                                      | 데이터 파일의 경로                                            |
| Create LSN                         | \< FileNo, Offset\>                         | 데이터 파일이 생성된 시점의 시스템 로그의 마지막 LSN          |
| Database File Status               | 아래 DISK_DATABASE_FILE_ATTRIBUTE 설명 참조 | 파일의 상태                                                   |
| Autoextend Mode                    | AutoExtend\| Non-AutoExtend                 | 자동 확장 설정 여부                                           |
| Create Mode                        | 0\|1                                        | 0: 재사용 1: 새로 생성한 파일                                 |
| Initialize Size                    | 0 \~ unsigned int 타입의 최대값             | 초기 크기(MByte)                                              |
| Current Size                       | 0 \~ unsigned int 타입의 최대값             | 현재 크기(MByte)                                              |
| Next Size                          | 0 \~ unsigned int 타입의 최대값             | 확장 단위 크기(MByte)                                         |
| Maximum Size                       | 0 \~ unsigned int 타입의 최대값             | 최대 크기(MByte)                                              |
| ChangeTracking DataFileDescSlot ID | 0 \~ unsigned int 타입의 최대값             | Disk datafile과 묶여있는 ChangeTracking의 DataFileDescSlot ID |

[DISK DATABASE FILE ATTRIBUTE] 내용 중 Database File Status의 의미는 다음과
같다.

| 값           | 설명                    |
|--------------|-------------------------|
| OFFLINE      | 오프라인 상태           |
| ONLINE       | 온라인 상태             |
| CREATING     | 생성 중                 |
| BACKUP_BEGIN | 백업을 시작한 상태      |
| BACKUP_END   | 백업을 종료 중인 상태   |
| DROPPING     | 삭제 중인 상태          |
| RESIZING     | 크기를 바꾸고 있는 상태 |
| DROPPED      | 삭제된 상태             |

다음은 dumpla의 출력 결과 중 일부분을 예로 보인 것이다.

```
[ DISK DATABASE FILE ATTRIBUTE ]
Tablespace ID                  [ 2 ]
Database File ID               [ 0 ]
Database File Path C:\altibase_home\dbs\system001.dbf]
Create LSN                     [0, 4443 ]
Database File Status           [ ONLINE ]
Autoextend Mode                [ Non-Autoextend ]
Create Mode                    [ 0 ]
Initialize Size                [10 MBytes(1280 Pages)]
Current Size                   [10 MBytes(1280 Pages)]
Next Size                      [0 MBytes(0 Pages)]
Maximum Size                   [0 MBytes(0 Pages)]
```



##### [Change Tracking ATTRIBUTE]

changeTracking 파일에 대한 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                     | 값                                     | 설명                                                |
|-------------------------------|----------------------------------------|-----------------------------------------------------|
| Last Flush LSN                | FileNo, Offset                         | 메모리상의 변경된 데이터가 파일로 기록된 시점의 LSN |
| Change Tracking Manager State | 문자열 ex) CHANGE TRACKING MGR ENABLED | 페이지 변경 추적 기능의 상태                        |
| Change Tracking File Name     | 문자열                                 | 변경 추적 파일의 경로                               |

##### [Backup Info ATTRIBUTE]

backupinfo 파일에 대한 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                    | 값                                     | 설명                                                  |
|------------------------------|----------------------------------------|-------------------------------------------------------|
| Delete Archivelog File Range | FileNo, Offset                         | 삭제해도 완전 복구가 가능한 아카이브 로그 파일의 번호 |
| Last Backup LSN              | FileNo, Offset                         | 최근에 수행된 백업 시점의 LSN                         |
| Before Backup LSN            | FileNo, Offset                         | 최근에 수행된 백업이전에 수행된 LSN                   |
| Backup Info Manager State    | 문자열 예) BACKUP INFO MGR INITIALIZED | 백업 정보 파일 관리자의 상태                          |
| Backup Directory Path        | 문자열 예) /backup_dir/                | 백업 경로                                             |
| Backup Info File Name        | 문자열                                 | 백업 정보 파일 이름                                   |

## dumplf

### 개요

Altibase는 복구를 위해서 트랜잭션이 변경 연산(INSERT, DELETE, UPDATE 등)을 수행할 때, 데이터베이스 영역(DB File)외의 별도 파일에 로그를 남긴다. 이 로그는 IO 최소화를 위해서 이진(binary) 형식으로 기록되어 있다. 이 로그가 기록되는 로그 파일은 altibase.properties의 LOG_DIR 프로퍼티에 설정되는 디렉토리에 logfile\#(\#은 로그파일 번호로 계속 증가한다) 형태로 저장된다.

dumplf는 이 로그 파일의 내용을 텍스트 형식으로 변환해서 보여주는 유틸리티이다. 이 로그를 통해서 데이터베이스에 수행된 연산의 종류 및 변경 연산을 수행하는 트랜잭션의 빈도를 측정할 수 있다.

```
dumplf {-f log_file_name} [-t transaction_id][-s] [-l][-S lsn [-F path] [-g]]
```



### 구문

![](media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04623" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4334" image_path_raw="media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumplf ::=
    dumplf -f log_file
        [ -t transaction_id ]
        [ -s ]
        [ -l ]
        [ -S lsn [ -F path ] [ -g ] ]
```
<!-- IMG_RECOVERY_END ref_id="img-04623" -->


### 파라미터

| 파라미터 | 설명                                                                                                                                                         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \-f      | 출력할 로그 파일의 이름                                                                                                                                      |
| \-t      | 출력할 로그에 해당하는 트랜잭션 ID                                                                                                                           |
| \-s      | 로그 파일의 헤더만 출력하고자 할 때 명시                                                                                                                     |
| \-l      | 로그의 유형 (LT 필드) 또는 서브로그유형 (OPTYPE 과 UTYPE 필드)과 관련된 정보만 출력                                                                          |
| \-S      | MMDB에서 INSERT, UPDATE, DELETE, COMMIT, ROLLBACK의 로그 개수를 출력한다. 특정 lsn을 입력하면 해당 lsn 이후의 로그만, '0,0'을 입력하면 전체 로그를 보여준다. |
| \-F      | 로그를 분석할 대상 경로를 지정할 수 있으며, 생략할 경우 \$ALTIBASE_HOME/logs 의 경로를 분석한다.                                                             |
| \-g      | 테이블의 오브젝트 ID별 통계가 전체 통계 정보와 함께 출력된다. 생략하면 전체 통계 정보만 출력된다.                                                            |

### 설명

로그 파일의 내용을 텍스트 형식으로 변환해서 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumplf -f logfile0
```



### 출력 항목

다음은 dumplf의 출력 예이다.

```
LSN=<0,820>, COMP:N, MAGIC:820, TID: 6400,BE: N, REP: Y, ISVP: N, ISVP_DEPTH: 0 PLSN=<0,739>, LT: SMR_LT_MEMTRANS_COMMIT, SZ: 45
```

로그 파일의 내용 중, 필드들은 다음과 같은 의미를 갖는다.

| 필드 이름               | 값                                                                             | 설명                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LSN                     | 형식: ( FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값 ,         | 로그의 sequence number로 로그의 물리적인 위치를 표시한다. LSN은 파일 번호, 오프셋으로 구성된다.                                                                                           |
| COMP                    | Y\|N                                                                           | Y: 로그가 압축(compress)되었음 N: 압축되지 않음                                                                                                                                           |
| MAGIC                   | 0 - unsigned short 타입의 최대값                                               | 로그 레코드가 유효하다는 것을 나타내기 위해서 로그 LSN의 로그 파일 번호와 오프셋으로 이 값을 만들고 Redo, Undo시 로그를 읽었을 때 이 값이 현재 로그의 LSN과 동일한지 검사한다.            |
| TID                     | 0 - unsigned int 타입의 최대값                                                 | 트랜잭션 식별자                                                                                                                                                                           |
| BE                      | Y\|N                                                                           | Y : Begin Transaction Log                                                                                                                                                                 |
| REP                     | Y\|N                                                                           | Y: 이중화가 걸려있는 경우 Sender가 Standby로 보내거나 참조하는 로그이다. N: Sender는 이 로그를 무시한다                                                                                   |
| ISVP                    | Y\|N                                                                           | Y: 묵시적 저장점 (Implicit Savepoint) 로그. 문장(Statement) 시작 후 처음으로 찍힌 로그이다. 트랜잭션이 문장을 수행했을 때 오류가 발생하면 이 로그까지 부분 철회(Partial Rollback)을 한다. |
| ISVP_DEPTH              | 0 - 255                                                                        | 어떤 SQL 구문이 다른 구문 내에 중첩되었을 때 묵시적 저장점의 중첩 깊이                                                                                                                    |
| PLSN                    | 형식: (FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값            | Previous Log LSN으로 이 값을 이용하여 같은 트랜잭션이 기록한 로그들끼리 체인(Chain)으로 연결되어 있다.                                                                                    |
| LT                      | 문자열                                                                         | 로그의 유형을 나타낸다. 자세한 내용은 아래 로그 유형에 대한 표를 참고한다.                                                                                                                |
| SZ                      | 0 - unsigned int 타입의 최대값                                                 | 로그 크기 (단위: bytes)                                                                                                                                                                   |
| RdSz                    | 0 - unsigned int 타입의 최대값                                                 | 로그 레코드의 크기 (단위: bytes)                                                                                                                                                          |
| DMIOff                  | 0 - unsigned int 타입의 최대값                                                 | 논리적 로그의 위치. 트랜잭션 언두 또는 이중화에서 사용한다.                                                                                                                               |
| TableOID                | 0 - unsigned int 타입의 최대값                                                 | 테이블의 오브젝트 ID                                                                                                                                                                      |
| OID                     | 0 - unsigned int 타입의 최대값                                                 | 테이블을 제외한 모든 오브젝트의 ID. 레코드 오브젝트도 포함한다.                                                                                                                           |
| ContType                | 0, 1                                                                           | 이중화를 위해 사용하는 내부 값                                                                                                                                                            |
| OPTYPE                  | LogTypeName\<LogTypeNumber\>                                                   | Nested Top Action (NTA) 로그의 작업 유형                                                                                                                                                  |
| AFTER                   | SZ: \<size\>, Value: \<value\>                                                 | 로그 레코드의 변경 후 이미지 (after image)                                                                                                                                                |
| BEFORE                  | SZ: \<size\>, Value: \<value\>                                                 | 로그 레코드의 변경 전 이미지 (before image)                                                                                                                                               |
| UTYPE                   | LogTypeName\<LogTypeNumber\>                                                   | UPDATE 로그의 작업 유형                                                                                                                                                                   |
| UPOS                    | 형식: (SPACEID:\<SpaceID\>, PID:\<PageID\>, OFFSET:\<Offset\> =\> OID:\<OID\>) | 변경된 객체의 주소. 또한 변경 작업 동안 발생한 정보도 포함한다.                                                                                                                           |
| SPACEID                 | 0 - unsigned short 타입의 최대값                                               | 변경된 객체를 포함하고 있는 테이블스페이스의 ID                                                                                                                                           |
| PID                     | 0 - unsigned int 타입의 최대값                                                 | 변경된 객체를 포함하고 있는 페이지의 ID                                                                                                                                                   |
| Offset                  | 0 - unsigned int 타입의 최대값                                                 | 변경된 객체를 포함하고 있는 페이지 내에서의 offset                                                                                                                                        |
| FLISlot PrevPID NextPID | 형식: (\<BeforePID\> =\> \<AfterPID\>)                                         | 메모리 테이블스페이스를 관리하기 위해 사용하는 내부 값                                                                                                                                    |
| ESLSN                   | 형식: (FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값            | 복구 수행 시 시작할 LSN                                                                                                                                                                   |
| Lob Locator             | 0 - unsigned long 타입의 최대값                                                | 이중화에서 LOB타입과 관련해서 내부적으로 사용하는 값                                                                                                                                      |

dumplf의 결과 중 LT (Log Type: 로그 유형)의 의미는 다음과 같다.

| 값                        | 설명                                        |
|---------------------------|---------------------------------------------|
| SMR_LT_DUMMY              | Dummy 로그                                  |
| SMR_LT_CHKPT_BEGIN        | Checkpoint Begin 로그                       |
| SMR_LT_DIRTY_PAGE         | Dirty Page 로그                             |
| SMR_LT_CHKPT_END          | Checkpoint End 로그                         |
| SMR_LT_MEMTRANS_COMMIT    | Memory Transaction Commit 로그              |
| SMR_LT_MEMTRANS_ABORT     | Memory Transaction Abort 로그               |
| SMR_LT_DSKTRANS_COMMIT    | Disk Transaction Commit 로그                |
| SMR_LT_DSKTRANS_ABORT     | Disk Transaction Abort 로그                 |
| SMR_LT_SAVEPOINT_SET      | Savepoint Set 로그                          |
| SMR_LT_SAVEPOINT_ABORT    | Savepoint Abort Begin 로그                  |
| SMR_LT_XA_PREPARE         | XA Prepare 로그                             |
| SMR_LT_TRANS_PREABORT     | Abort Begin 로그                            |
| SMR_LT_DDL                | DDL (Data Definition Language) 로그         |
| SMR_LT_XA_SEGS            | XA Prepare Transaction Segment Information  |
| SMR_LT_LOB_FOR_REPL       | 이중화를 위한 LOB 로그                      |
| SMR_LT_UPDATE             | MMDB(Main Memory Database) Update 로그      |
| SMR_LT_NTA                | MMDB NTA(Nested Top Action) 로그            |
| SMR_LT_COMPENSATION       | Compensation 로그                           |
| SMR_LT_DUMMY_COMPENSATION | Dummy Compensation 로그                     |
| SMR_LT_FILE_BEGIN         | File Begin 로그                             |
| SMR_LT_FILE_TBS_UPDATE    | Tablespace Update 로그                      |
| SMR_LT_FILE_END           | File End 로그                               |
| SMR_DLT_READONLY          | DRDB(Disk Resident Database) Redo Only 로그 |
| SMR_DLT_UNDOABLE          | DRDB Undo 로그                              |
| SMR_DLT_NTA               | DRDB NTA 로그                               |
| SMR_DLT_COMPENSATION      | DRDB Compensation 로그                      |
| SMR_DLT_REF_NTA           | DRDB Reference NTA 로그                     |
| SMR_LT_TABLE_META         | 이중화를 위한 테이블 메타 로그              |

OPTYPE 과 UTYPE 에 가능한 로그 타입 이름

| 값                                                           | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| SMR_OP_SMM_PERS_LIST_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_ALLOC <br />SMR_OP_SMC_VAR_SLOT_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_FREE <br />SMR_OP_SMC_VAR_SLOT_FREE | MMDB의 페이지와 슬롯에 관련된 로그                           |
| SMR_OP_CREATE_TABLE <br />SMR_OP_CREATE_INDEX <br />SMR_OP_DROP_INDEX <br />SMR_OP_ALTER_TABLE <br />SMR_OP_SMM_CREATE_TBS <br />SMR_OP_INSTANT_AGING_AT_ALTER_TABLE <br />SMR_OP_SMC_TABLEHEADER_ALLOC | MMDB에서 DDL 구문 수행과 관련된 로그                         |
| SMR_MEM_LOB_CURSOR_OPEN <br />SMR_DISK_LOB_CURSOR_OPEN <br />SMR_LOB_CURSOR_CLOSE <br />SMR_PREPARE4WRITE <br />SMR_FINISH2WRITE | MMDB에서 LOB 데이터 제어와 관련된 로그                       |
| SDR_OP_SDP_CREATE_TABLE_SEGMENT <br />SDR_OP_SDP_CREATE_LOB_SEGMENT <br />SDR_OP_SDP_CREATE_INDEX_SEGMENT <br />SDR_OP_SDP_ADD_LOB_PAGE_TO_AGINGLIST <br />SDR_OP_SDC_ALLOC_UNDO_PAGE <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTENT_FROM_TBS <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTDIR_FROM_LIST <br />SDR_OP_SDPTB_RESIZE_GG <br />SDR_OP_SDPST_ALLOC_PAGE <br />SDR_OP_SDPSF_ALLOC_PAGE <br />SCT_UPDATE_MRDB_CREATE_TBS <br />SCT_UPDATE_MRDB_CREATE_CIMAGE_FILE <br />SCT_UPDATE_MRDB_DROP_TBS <br />SCT_UPDATE_MRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_MRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_MRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_TBS <br />SCT_UPDATE_DRDB_DROP_TBS <br />SCT_UPDATE_DRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_DRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_DBF <br />SCT_UPDATE_DRDB_DROP_DBF <br />SCT_UPDATE_DRDB_EXTEND_DBF <br />SCT_UPDATE_DRDB_SHRINK_DBF <br />SCT_UPDATE_DRDB_AUTOEXTEND_DBF <br />SCT_UPDATE_DRDB_ALTER_DBF_ONLINE <br />SCT_UPDATE_DRDB_ALTER_DBF_OFFLINE <br />SCT_UPDATE_VRDB_CREATE_TBS <br />SCT_UPDATE_VRDB_DROP_TBS <br />SCT_UPDATE_VRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_COMMON_ALTER_ATTR_FLAG | 테이블스페이스와 세그먼트에 관련된 로그                      |
| SDR_OP_SDPST_UPDATE_WMINFO_4DPATH <br />SDR_OP_SDPST_UPDATE_MFNL_4DPATH <br />SDR_OP_SDPST_UPDATE_BMP_4DPATH <br />SDR_OP_SDPSF_ADD_PIDLIST_PVTFREEPIDLIST_4DPATH <br />SDR_OP_SDPSF_MERGE_SEG_4DPATH <br />SDR_OP_SDPSF_UPDATE_HWMINFO_4DPATH <br />SDR_OP_SDP_DPATH_ADD_SEGINFOSET | DRDB에서 Direct Page Insert를 위한 페이지 관리와 관련된 로그 |
| SDR_OP_SDN_INSERT_KEY_WITH_NTA <br />SDR_OP_SDN_DELETE_KEY_WITH_NTA | DRDB에서 B-tree 인덱스를 위한 NTA 로그                       |
| SDR_OP_STNDR_INSERT_KEY_WITH_NTA <br />SDR_OP_STNDR_DELETE_KEY_WITH_NTA | DRDB에서 R-tree 인덱스를 위한 NTA 로그                       |
| SDR_SDP_1BYTE <br />SDR_SDP_2BYTE <br />SDR_SDP_4BYTE <br />SDR_SDP_8BYTE <br />SDR_SDP_BINARY | 물리적 DRDB 로그                                             |
| SDR_SDP_PAGE_CONSISTENT <br />SDR_SDP_INIT_PHYSICAL_PAGE <br />SDR_SDP_INIT_LOGICAL_HDR <br />SDR_SDP_INIT_SLOT_DIRECTORY <br />SDR_SDP_FREE_SLOT <br />SDR_SDP_FREE_SLOT_FOR_SID <br />SDR_SDP_RESTORE_FREESPACE_CREDIT <br />SDR_SDP_RESET_PAGE <br />SDR_SDP_WRITE_PAGEIMG <br />SDR_SDP_WRITE_DPATH_INS_PAGE | DRDB의 페이지와 슬롯에 관련된 로그                           |
| SDR_SDPST_INIT_SEGHDR <br />SDR_SDPST_INIT_BMP <br />SDR_SDPST_INIT_LFBMP <br />SDR_SDPST_INIT_EXTDIR <br />SDR_SDPST_ADD_RANGESLOT <br />SDR_SDPST_ADD_SLOTS <br />SDR_SDPST_ADD_EXTDESC <br />SDR_SDPST_ADD_EXT_TO_SEGHDR <br />SDR_SDPST_UPDATE_WM <br />SDR_SDPST_UPDATE_MFNL <br />SDR_SDPST_UPDATE_PBS <br />SDR_SDPST_UPDATE_LFBMP_4DPATH <br />SDR_SDPSC_INIT_SEGHDR <br />SDR_SDPSC_INIT_EXTDIR <br />SDR_SDPSC_ADD_EXTDESC_TO_EXTDIR <br />SDR_SDPTB_INIT_LGHDR_PAGE <br />SDR_SDPTB_ALLOC_IN_LG <br />SDR_SDPTB_FREE_IN_LG | DRDB를 위한 세그먼트와 테이블스페이스에 관련된 로그          |
| SDR_SDC_INSERT_ROW_PIECE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_DELETEUNDO <br />SDR_SDC_UPDATE_ROW_PIECE <br />SDR_SDC_OVERWRITE_ROW_PIECE <br />SDR_SDC_CHANGE_ROW_PIECE_LINK <br />SDR_SDC_DELETE_FIRST_COLUMN_PIECE <br />SDR_SDC_ADD_FIRST_COLUMN_PIECE <br />SDR_SDC_DELETE_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_DELETE_ROW_PIECE SDR_SDC_LOCK_ROW | DRDB의 테이블 레코드 관리에 관련된 로그                      |
| SDR_SDC_UPDATE_LOBDESC <br />SDR_SDC_UPDATE_LOBDESC_KEY <br />SDR_SDC_LOB_WRITE_PIECE <br />SDR_SDC_LOB_WRITE_PIECE4DML <br />SDR_SDC_INIT_LOBPAGE <br />SDR_SDC_LOB_PAGE_TO_AGING_LIST | DRDB에서 LOB 타입 사용에 관련된 로그                         |
| SDR_SDC_PK_LOG                                               | DRDB에서 이중화를 위한 프라이머리 키 사용에 관련된 로그      |
| SDR_SDC_INIT_CTL <br />SDR_SDC_EXTEND_CTL <br />SDR_SDC_BIND_CTS <br />SDR_SDC_UNBIND_CTS <br />SDR_SDC_BIND_ROW <br />SDR_SDC_UNBIND_ROW <br />SDR_SDC_ROW_TIMESTAMPING <br />SDR_SDC_DATA_SELFAGING | DRDB에서 레코드를 위한 MVCC 관련된 로그                      |
| SDR_SDC_BIND_TSS <br />SDR_SDC_UNBIND_TSS <br />SDR_SDC_SET_INITSCN_TO_TSS <br />SDR_SDC_INIT_TSS_PAGE <br />SDR_SDC_INIT_UNDO_PAGE <br />SDR_SDC_INSERT_UNDO_REC<br /> | DRDB에서 Trasaction Status Slots (TSS)과 언두 레코드에 관련된 로그 |
| SDR_SDN_INSERT_INDEX_KEY <br />SDR_SDN_FREE_INDEX_KEY <br />SDR_SDN_INSERT_UNIQUE_KEY <br />SDR_SDN_INSERT_DUP_KEY <br />SDR_SDN_DELETE_KEY_WITH_NTA <br />SDR_SDN_FREE_KEYS <br />SDR_SDN_COMPACT_INDEX_PAGE | DRDB에서 B-tree 인덱스 관련된 로그                           |
| SDR_SDN_MAKE_CHAINED_KEYS <br />SDR_SDN_MAKE_UNCHAINED_KEYS <br />SDR_SDN_KEY_STAMPING <br />SDR_SDN_INIT_CTL <br />SDR_SDN_EXTEND_CTL <br />SDR_SDN_FREE_CTS | DRDB에서 B-tree 인덱스 키를 위한 MVCC에 관련된 로그          |
| SDR_STNDR_MAKE_CHAINED_KEYS <br />SDR_STNDR_MAKE_UNCHAINED_KEYS <br />SDR_STNDR_KEY_STAMPING | DRDB에서 R-tree 인덱스 관련된 로그                           |
| SMR_PHYSICAL                                                 | MMDB에서 물리적 로그                                         |
| SMR_SMM_MEMBASE_SET_SYSTEM_SCN <br />SMR_SMM_MEMBASE_ALLOC_PERS_LIST <br />SMR_SMM_MEMBASE_ALLOC_EXPAND_CHUNK <br />SMR_SMM_PERS_UPDATE_LINK <br />SMR_SMM_PERS_UPDATE_NEXT_FREE_PAGE_LINK <br />SMR_SMM_MEMBASE_INFO | MMDB에서 기본 정보와 관련된 로그                             |
| SMR_SMC_TABLEHEADER_INIT <br />SMR_SMC_TABLEHEADER_UPDATE_INDEX <br />SMR_SMC_TABLEHEADER_UPDATE_COLUMNS <br />SMR_SMC_TABLEHEADER_UPDATE_INFO <br />SMR_SMC_TABLEHEADER_SET_NULLROW <br />SMR_SMC_TABLEHEADER_UPDATE_ALL <br />SMR_SMC_TABLEHEADER_UPDATE_ALLOCINFO <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG <br />SMR_SMC_TABLEHEADER_SET_SEQUENCE <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_COLUMN_COUNT <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_SEGMENT <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG_FOR_MEDIA_RECV <br />SMR_SMC_TABLEHEADER_SET_SEGSTOATTR <br />SMR_SMC_TABLEHEADER_SET_INSERTLIMIT <br />SMR_SMC_INDEX_SET_FLAG <br />SMR_SMC_INDEX_SET_SEGATTR <br />SMR_SMC_INDEX_SET_SEGSTOATTR <br />SMR_SMC_INDEX_SET_DROP_FLAG | MMDB에서 테이블 헤더와 인덱스 헤더에 관련된 로그             |
| SMR_SMC_PERS_INIT_FIXED_PAGE <br />SMR_SMC_PERS_INIT_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_FREE<br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_VERSION <br />SMR_SMC_PERS_SET_FIX_ROW_DROP_FLAG <br />SMR_SMC_PERS_SET_FIX_ROW_DELETE_BIT <br />SMR_SMC_PERS_INIT_VAR_PAGE <br />SMR_SMC_PERS_UPDATE_VAR_ROW_HEAD <br />SMR_SMC_PERS_UPDATE_VAR_ROW <br />SMR_SMC_PERS_SET_VAR_ROW_FLAG <br />SMR_SMC_PERS_SET_VAR_ROW_NXT_OID <br />SMR_SMC_PERS_WRITE_LOB_PIECE <br />SMR_SMC_PERS_INSERT_ROW <br />SMR_SMC_PERS_UPDATE_INPLACE_ROW <br />SMR_SMC_PERS_UPDATE_VERSION_ROW<br /> SMR_SMC_PERS_DELETE_VERSION_ROW | MMDB에서 테이블 레코드와 관련된 로그                         |

MVCC와 관련된 자세한 설명은 *Administrator’s Manual* 을 참고하기 바란다.

## dumptrc 

### 개요

Altibase 서버가 비정상 종료될 때 \$ALTIBASE_HOME/trc 디렉토리에 기록되는 트레이스 로그 파일을 사용자가 식별할 수 있는 형태로 변환하여 출력한다.

```
dumptrc [-h |[-p file_path][-c [-s]]
[-a|-i file_name [-i file_name]..|-e file_name [-e file_name]..] [-n file_count] [-x] |-f |-v]
```



### 구문

![](media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04624" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4479" image_path_raw="media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumptrc ::=
    dumptrc
        [ -h
        | -p file_path [ -c [ -s ] ]
          { -a | -i file_name { -i file_name } | -e file_name { -e file_name } }
          [ -n line_count ]
          [ x ]
        | -f
        | -v ]
```
<!-- IMG_RECOVERY_END ref_id="img-04624" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-h      | 도움말을 출력한다. 파라미터를 생략하거나 다른 파라미터와 중복하여 사용할 경우 도움말이 우선한다. |
| \-p      | 트레이스 로그 파일을 가져오는 경로를 지정한다. 경로를 지정하지 않으면 기본적으로 \$ALTIBASE_HOME/trc 디렉토리의 로그 파일을 가져온다. |
| \-c      | altibase_error.log에 기록된 ALTIBASE 프로세스 콜 스택을 사용자가 식별할 수 있는 함수명으로 변환하여 출력한다. 콜 스택의 주소를 함수명으로 변경하지 않으려면 -s 옵션를 사용한다. 파라미터 -a, -i, -e, -n과 함께 사용하지 않으면 콜 스택만 기록된다. |
| \-s      | 트레이스 로그에 기록된 콜 스택만을 출력하고 함수명으로 변경하지 않는다. |
| \-a      | 트레이스 로그 파일의 전부를 정렬하여 출력한다.               |
| \-i      | 지정하는 트레이스 로그 파일을 출력한다. 복수의 로그 파일이 출력 가능하다. '-e' 파라미터와 함께 사용할 수 없다. |
| \-e      | 지정한 트레이스 로그 파일을 제외한 모든 파일을 출력한다. 반복하여 복수의 로그 파일을 제거할 수 있으며, '-i' 파라미터와 함께 사용할 수 없다. |
| \-n      | 한 번에 출력할 로그의 개수를 지정한다. 1\~127개의 로그를 출력할 수 있으며, 지정하지 않으면 10개의 로그가 출력된다. |
| \-f      | 트레이스 로그 파일이 기록될 때마다 추가되는 로그 메세지를 출력한다. |
| -x       | altibase버전과 dumptrc버전이 틀린 경우도 콜 스택을 출력한다. |
| \-v      | dumptrc의 버전을 출력한다.                                   |

### 설명

프로세스 콜 스택에는 Altibase 종료 당시 수행되던 Altibase 내부 모듈에 대한 정보가 기록된다. dumptrc를 이용하여 가져올 수 있는 트레이스 로그 파일은 \$ALTIBASE_HOME/trc 디렉터리에 기록되는 아래의 파일들을 사용할 수 있다.

-   ERROR : altibase_error.log
-   SERVER : altibase_boot.log
-   SM : altibase_sm.log
-   RP : altibase_rp.log
-   QP : altibase_qp.log
-   JOB : altibase_job.log
-   DK : altibase_dk.log
-   DR : altibase_dr.log
-   XA : altibase_xa.log
-   MM : altibase_mm.log
-   RP_CONFLICT : altibase_rp_conflict.log
-   DUMP : altibase_dump.log
-   TRC : altibase_trace.log
-   SNMP : altibase_snmp.log
-   CM : altibase_cm.log
-   MISC : altibase_misc.log
-   SD : altibase_sd.log

만약 \$ALTIBASE_HOME/trc가 아닌 다른 경로에 있는 트레이스 로그 파일을 출력할 때에는 '-p'를 사용하여 경로를 변경할 수 있다.

Altibase 서버가 비정상 종료할 경우, 프로세스 콜 스택을 dumptrc로 변환하여 Altibase 기술서비스 팀에 송부하면, 보다 빨리 문제를 해결할 수 있을 것이다.

### 주의 사항

 Altibase의 실행 파일의 버전과 dumptrc의 버전이 동일해야 정확한 콜 스택 정보를 확인할 수 있다.버전이 틀릴 경우는 잘못된 값이 나올 수 있기 때문에 기본적으로 경고메시지를 보여주고 콜 스택을 출력하지 않는다. 버전이 틀릴때도 강제로 콜스택을 출력하기 위해서는 -x옵션을 사용하면 된다.

### 사용예

altibase_error.log와 altibase_boot.log를 묶어서 출력한다.

```
$ dumptrc -i server -i error
[2015/10/21 17:29:42 55C][PID:32702][Thread-2]
  ==> Initialize Disaster Recovery Manager  
[2015/10/21 17:29:42 55D][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 55E][PID:32702][Thread-2]
  ==> Initialize MMX Service  
[2015/10/21 17:29:42 55F][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 560][PID:32702][Thread-2]
  ==> Initialize Audit Service  
[2015/10/21 17:29:42 561][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 562][PID:32702][Thread-2]
  ==> Initialize Job Manager  
[2015/10/21 17:29:42 563][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 7.3.0.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF
Caller[1] 0000000000426CFE
Caller[2] 00007FD306FD4CB0
Caller[3] 00007FD30609F763
Caller[4] 000000000042F66F
Caller[5] 00000000004213CE
Caller[6] 000000000041D1E0
Caller[7] 00007FD305FD376D
Caller[8] 00000000004206BD
END-STACK =======================================
10 logs printed.
```

error.log만 제외하고 출력한다.

```
$ dumptrc -e error
[2015/10/21 17:29:48 571][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:48 572][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 573][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:49 574][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 575][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:49 576][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 577][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:53 578][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 579][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:53 57A][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
10 logs printed.
```

콜 스택과 altibase_boot.log, altibase_sm.log을 함께 출력하되 상위 20개 로그
출력한다.

```
$ dumptrc -c -i error -i server -i sm -n 20
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:42 551][PID:32702][Thread-2]
  ==> Initialize Security Module  
[2015/10/21 17:29:42 552][PID:32702][Thread-2]
  ... [SUCCESS] 
...
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 7.3.0.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
Caller[3] 00007FD30609F763  => not found
Caller[4] 000000000042F66F  => mmtSessionManager::run()
Caller[5] 00000000004213CE  => mmi::serverStart(int, int)
Caller[6] 000000000041D1E0  => main
Caller[7] 00007FD305FD376D  => not found
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```

다른 디렉토리의 trc 로그에서 콜 스택을 가져와서 출력한다.

```
$ dumptrc -p ./altibase_home/trc -c -n 20

Path : ./altibase_home/trc
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:45 568][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:45 569][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
...
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 7.3.0.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
...
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```



## killCheckServer

### 개요

killCheckServer는 실행 중인 checkServer를 종료한다.

```
killCheckServer
```



### 구문

![killcheckserver](media/Utilities/killcheckserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04625" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4705" image_path_raw="media/Utilities/killcheckserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
killcheckserver ::=
    killCheckServer
```
<!-- IMG_RECOVERY_END ref_id="img-04625" -->


### 설명

killCheckServer는 실행 중인 checkServer를 종료한다.

server stop 또는 server kill 명령을 사용해서 Altibase 서버를 종료할 경우, checkServer가 동작 중이라면 서버 종료 전에 먼저 server 스크립트 내에서 killCheckServer가 checkServer의 동작을 동작을 멈추도록 되어 있다. 그리고, \$ALTIBASE_HOME/trc 디렉토리의 killCheckServer.log 파일에 killCheckServer 수행 결과가 아래와 같이 기록된다.

- checkServer가 동작 중일 때:

  ```
  checkServer killed.
  ```


- checkServer가 동작 중이 아닐 때:

  ```
  ERROR CODE : -27
  ```


그러나, 사용자가 직접 killCheckServer 명령어를 실행할 경우에는 killCheckServer.log에 수행 결과가 기록되지 않는다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ killCheckServer
```



## server

### 개요

Altibase 데이터베이스의 생성, 구동 및 종료시키기 위한 쉘 스크립트이다.

```
server { start | stop | restart | kill | status | create db_charset national_charset | startRoleManager | stopRoleManager } 
```



### 구문

![server](media/Utilities/server.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-04626" source_md="Manuals/Altibase_7.3/kor/Utilities Manual.md" line_no="4753" image_path_raw="media/Utilities/server.gif" image_class="C" format="bnf" verified="True" -->
```bnf
server ::=
    'server' { 'start'
             | 'stop'
             | 'restart'
             | 'kill'
             | 'status'
             | 'create' db_charset national_charset
             | 'startRoleManager'
             | 'stopRoleManager' }
```
<!-- IMG_RECOVERY_END ref_id="img-04626" -->


### 파라미터

| 파라미터         | 설명                                                                      |
|------------------|---------------------------------------------------------------------------|
| start            | Altibase 프로세스를 구동한다.                                             |
| stop             | Altibase 프로세스를 종료한다.                                             |
| restart          | Altibase 프로세스를 재구동한다.                                           |
| kill             | Altibase 프로세스를 강제 종료한다.                                        |
| status           | 데이터베이스 내의 테이블 목록을 출력한다.                                 |
| create           | 크기 10M, 노아카이브 로그로 입력된 캐릭터 셋으로 데이터베이스를 생성한다. |
| startRoleManager | Altibase 프로세스를 Disaster Recovery의 역할 관리자로서 구동한다.         |
| stopRoleManager  | 역할 관리자를 종료한다.                                                   |

### 설명

Altibase의 구동 및 종료, 데이터베이스 생성은 iSQL상에서 SQL 구문으로 수행해야 한다. Altibase는 사용자 편의를 위해 관리자가 자주 사용하는 이러한 구문들을 묶어서 쉘 스크립트 파일 형태로 제공한다.

server 스크립트가 제공하는 기능은 다음과 같다.

-   Altibase 프로세스의 구동

-   Altibase 프로세스의 종료

-   Altibase 프로세스의 재구동

-   Altibase 프로세스의 강제 종료

-   “SELECT \* FROM TAB;” 결과 출력

-   Altibase 데이터베이스 생성

-   Altibase 프로세스를 역할 관리자로 구동

-   역할 관리자 종료

Altibase 관리를 위한 SQL 구문에 대한 자세한 내용은 *SQL Reference*를 참조한다.

### 사용예

사용 방법은 다음과 같다.

```
$ server start
$ server restart
$ server stop
$ server status
$ server kill
$ server create ksc5601 utf16
$ server startRoleManager
$ server stopRoleManager
```



### 참고사항

*Administrator’s Manual*, *SQL Reference*를 참고하기 바란다.
<!-- SOURCE_BLOCK_END source_id="SRC-000137" block_id="BLOCK-000929" -->

## SRC-000166 - Trunk

| Field | Value |
| --- | --- |
| `source_id` | SRC-000166 |
| `source_path` | Manuals/Altibase_trunk/eng/Utilities Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | en |
| `authority_label` | English extraction aid; Altibase 8.1 verified source |
| `source_sha256` | a7a85b69a217a813389c870d5252f2b3c313fc0a021ed6a4f6481bdc9f86ea1b |
| `byte_count` | 231417 |
| `line_count` | 4477 |
| `estimated_tokens` | 57722 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000166" source_path="Manuals/Altibase_trunk/eng/Utilities Manual.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="en" authority_label="English extraction aid; Altibase 8.1 verified source" sha256="a7a85b69a217a813389c870d5252f2b3c313fc0a021ed6a4f6481bdc9f86ea1b" byte_count="231417" line_count="4477" estimated_tokens="57722" block_id="BLOCK-000930" -->
Utilities Manual
================

#### Trunk

Altibase® Tools & Utilities

<br><br><br><br><br><br>
<!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>

<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Tools & Utilities Manual
Trunk
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the
software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>

<br>

# Table of Contents

- [Preface](#preface)
  - [About This Manual](#about-this-manual)
- [1. aexport](#1-aexport)
  - [Introducing aexport](#introducing-aexport)
  - [Prerequisite](#prerequisite)
  - [How to Use aexport](#how-to-use-aexport)
- [2. altiComp](#2-alticomp)
  - [Introducing altiComp](#introducing-alticomp)
  - [How to Use altiComp](#how-to-use-alticomp)
  - [Comparison (DIFF) Function](#comparison-diff-function)
  - [Synchronization (SYNC) Function](#synchronization-sync-function)
- [3. aku](#3-aku)
  - [Introducing aku](#introducing-aku)
  - [Setup to run aku](#setup-to-run-aku)
  - [Usage of aku](#usage-of-aku)
  - [Cautions](#cautions)
  - [Examples](#examples)
- [4. Other Utilities](#4-other-utilities)
  - [altiAudit](#altiaudit)
  - [altibase](#altibase)
  - [altiMon](#altimon)
  - [altierr](#altierr)
  - [altipasswd](#altipasswd)
  - [altiProfile](#altiprofile)
  - [altiwrap](#altiwrap)
  - [awrite](#awrite)
  - [checkServer](#checkserver)
  - [dumpbi](#dumpbi)
  - [dumpct](#dumpct)
  - [dumpdb](#dumpdb)
  - [dumpddf](#dumpddf)
  - [dumpla](#dumpla)
  - [dumplf](#dumplf)
  - [dumptrc](#dumptrc)
  - [killCheckServer](#killcheckserver)
  - [server](#server)



Preface
====

### About This Manual

This manual describes how to use Altibase utilities.

#### Audience

This manual has been prepared for the following Altibase users:

-   Database administrators
-   Performance administrators
-   Database users
-   Application developers
-   Technical Supporters

It is recommended for those reading this manual possess the following background knowledge:

-   Basic knowledge in the use of computers, operating systems, and operating system utilities
-   Experience in using relational database and an understanding of database concepts
-   Computer programming experience
-   Experience in database server management, operating system management, or network administration

#### Organization

This manual is organized as follows:

-   Chapter 1: aexport  
    This chapter describes aexport, a tool for supporting automated data migration between Altibase databases.

-   Chapter 2: altiComp  
    This chapter describes the altiComp utility's features and explains the capabilities of comparing and matching inconsistent data.

-   Chapter 3: aku  
    This chapter describes aku, the utility to support the data replication between pods using Kubernetes.

-   Chapter 4: Utilities  
    This chapter describes the rest of the utilities except aexport, altiComp, and aku.

#### Documentation Conventions

This section describes the conventions used in this manual. Understanding these conventions will make it easier to find information in this manual and in the other manuals in the series. 

There are two sets of conventions:

-   Syntax diagram conventions
-   Sample code conventions

##### Syntax Diagram Conventions

This manual describes command syntax using diagrams composed of the following elements:

| Elements                                                     | Meaning                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [![image1](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image1.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image1.gif) | Indicates the start of a command. If a syntactic element starts with an arrow, it is not a complete command. |
| [![image2](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image2.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image2.gif) | Indicates that the command continues to the next line. If a syntactic element ends with this symbol, it is not a complete command. |
| [![image3](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image3.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image3.gif) | Indicates that the command continues from the previous line. If a syntactic element starts with this symbol, it is not a complete command. |
| [![image4](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image4.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image4.gif) | Indicates the end of a statement.                            |
| [![image5](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image5.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image5.gif) | Indicates a mandatory element.                               |
| [![image6](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image6.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image6.gif) | Indicates an optional element.                               |
| [![image7](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image7.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image7.gif) | Indicates a mandatory element comprised of options. One, and only one, option must be specified. |
| [![image8](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image8.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image8.gif) | Indicates an optional element comprised of options.          |
| [![image9](https://github.com/ALTIBASE/Documents/raw/master/Manuals/Altibase_7.1/eng/media/SQL/image9.gif)](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/media/SQL/image9.gif) | Indicates an optional element in which multiple elements may be specified. A comma must precede all but the first element. |

##### Sample Code Conventions

The code examples explain SQL statements, stored procedures, iSQL statements, and other command line syntax.

The following table describes the printing conventions used in the code examples.

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL\> SELECT ename FROM employee;<br/> ENAME<br/>  -----------------------<br/> SWNO<br/>  HJNO<br/>  HSCHOI<br/>  .<br/> .<br/> .<br/> 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code. | EXEC :p1 := 1; acc NUMBER(11,2)                              |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT \* FROM *table_name*; <br/>CONNECT *userID*/*password*; |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### Related Documentations

For more detailed information, please refer to the following documents.

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   iSQL User’s Manual

-   iLoader User's Manual

#### Altibase Welcomes Your Comments and Feedbacks

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there is any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](http://support.altibase.com/en/).

Thank you. We always welcome your feedbacks and suggestions.



# 1. aexport

### Introducing aexport

#### Overview

aexport supports automated data migration between Altibases. This utility stores logical structures and data in text format, and automatically creates a script to load the stored text data into a new database. 

The objects and components that aexport can extract from a database to which it is connected are database users, user privileges, tables, tablespaces, table constraints, indexes, views, materialized views, stored procedures, sequences, and replication objects. 

Because aexport creates SQL scripts corresponding to logical structures in the database and downloads all data in text form, it can migrate data between databases of different versions or platforms. This utility should be used when the database is running, but not actively providing service (when clients are not connected).

#### aexport Features

aexport can extract the following database objects and structural elements:

-   Database users
-   User privileges 
-   Roles 
-   Tablespaces 
-   Tables 
-   Table constraints 
-   Indexes 
-   Views 
-   Materialized views 
-   Stored procedures 
-   Replication objects

In order to execute, aexport generates the SQL scripts to create the database components listed above and the shell scripts to run them.

##### aexport Modes and Script Files

aexport can be executed in different modes to extract different portions of the database. The desired mode can be specified on the command-line.

The aexport execution mode and the SQL script files generated for each mode are described in the section below.

##### Full DB Mode

Full DB mode extracts the entire database and is only available for the SYS user.

The following SQL script files are generated for this mode:

-   SYS_CRT_DIR.sql: Creates all directory objects.

-   SYS_CRT_USER.sql: Creates all users and roles.

-   SYS_CRT_SYNONYM.sql: Create all synonym objects.

-   SYS_CRT_REP.sql: Create all replicaiton objects.

-   ALL_CRT_VIEW_PROC.sql: Creates all views and stored procedures.

-   ALL_CRT_TBS.sql: Creates all tablespaces.

-   ALL_CRT_TBL.sql: Creates all user tables.

-   ALL_CRT_INDEX.sql: Creates all user indexes.

-   ALL_CRT_FK.sql:  Creates all user-defined foreign keys.

-   ALL_CRT_TRIG.sql: Creates all user-defined triggers.

-   ALL_CRT_SEQ.sql: Creates all user-defined sequences.

-   ALL_CRT_LINK.sql: Creates all user-defined database link objects.

-   ALL_EXE_STATS.sql: Creates statistics for all user-defined tables, columns, and indexes.

-   ALL_REFRESH_MVIEW.sql: Refreshes all user materialized views.

-   ALL_ALT_TBL.sql :  Switches the data access mode for tables and partitions of all users.

> Note: 
>
> A role can only be extracted in full DB mode, because it is a non-schema object.

##### User Mode

This mode exports all objects owned by a specified user and is available only for the SYS user or the user whose objects are to be exported. Set the -u command-line option to the desired user for this mode.

The following SQL script files are generated for this mode:

-   {User name}_CRT_TBL.sql: Creates all tables of the specified user.

-   {User name}_CRT_INDEX.sql: Creates all indexes of the specified user.

-   {User name}_CRT_FK.sql: Creates all foreign keys of the specified user.

-   {User name}_CRT_TRIG.sql: Creates all triggers of the specified user.

-   {User name}_CRT_SEQ.sql: Creates all sequences of the specified user.

-   {User name}_CRT_LINK.sql: Creates all database link objects of the specified user

-   {User name}_EXE_STATS.sql: Creates statistics for all tables, columns and indexes of specified user

-   {User name}_REFRESH_MVIEW.sql: Refreshes all materialized views of the specified user.

-   {User name}_ALT_TBL.sql : Switches the data access mode for tables and partitions of the specified user.

##### Object Mode

Object mode exports a specified set of objects (user.object) and is available only for the SYS user or the user whose objects are to be exported. Use the -object command-line option for this mode.

All specified objects must belong to the same user; however, the SYS user can export any user object. 

The following SQL script files are generated for this mode

-   {User name}_{Object name}_CRT.sql: Creates the specified user object.

-   {User name}_{Object name}_STATS.sql: Creates the specified user statistics.

#####  Shell Script Files

In addition to the above SQL scripts, the following shell script files are also created when aexport is executed:

-   run_il_in.sh: Loads data.

-   run_il_out.sh: Downloads data.

-   run_is.sh: Creates schema.

-   run_is_con.sh: Creates constraints. This script includes SQL scripts for creating indexes, foreign keys, triggers, and replication objects. This script is created if the TWO_PHASE_SCRIPT property is set to ON.

-   run_is_fk.sh: Creates foreign keys and triggers. This script is not created if the TWO_PHASE_SCRIPT property is set to ON.

-   run_is_index.sh: Creates indexes. This script is not created if the TWO_PHASE_SCRIPT property is set to ON.

-   run_is_repl.sh: Creates replication objects. This script is not created if the TWO_PHASE_SCRIPT property is set to ON.

-   run_is_refresh_mview.sh:  Refreshes materialized views. This script is not created if the TWO_PHASE_SCRIPT property is set to ON.

-   run_is_alt_tbl.sh : Switches the data access mode of tables and partitions. This script is not created if the TWO_PHASE_SCRIPT property is set to ON.

When one of the above shell script files is executed on the destination database, the logical structure of the source database is created on the destination database. Additionally, all data that exists on the source database is loaded into the destination database. These shell script files use iLoader to download and upload data; the iLoader process is automated within the shell script.

All files generated by aexport are text files, so the user can modify them as desired.

-   ##### aexport Properties and Script Files
  
    This section discusses script files generated by aexport properties.
    
    Please refer to aexport Properties for more information.
    
    -   INVALID_SCRIPT = ON,INVALID.sql is generated. This script file contains SQL scripts for all invalid views and stored procedures. A shell script file for executing INVALID.sql is not generated.
    
    -   TWO_PHASE_SCRIPT = OON, ALL_OBJECT.sql is generated for all objects and ALL_OBJECT_CONSTRAINTS.sql for all indexes, foreign keys, triggers, and replication objects. The run_is_con.sh shell script file for executing ALL_OBJECT_CONSTRAINTS.sql is also generated.

### Prerequisite

#### Install DBMS_METADATA Package

The DBMS_METADATA package provides functionality to extract object creation DDL statements or GRANT statements from the database dictionary.

To use aexport, it is necessary to have the DBMS_METADATA package installed in Altibase, as aexport has a dependency on this package. If not, the following error occurs:

```bash
$ aexport -s localhost -u sys -p manager
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 7.3.0.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[ERR-91144 : DBMS_METADATA package does not exist.]
```

> For more detailed information about DBMS_METADATA package, please refer to [***Stored Procedures Manual*** - DBMS_METADATA](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_trunk/eng/Stored%20Procedures%20Manual.md#dbms_metadata).


#### Setting aexport

aexport requires the following information to connect to a server:

-   ALTIBASE_HOME  
    The path where the server or client is installed.

-   server_name  
    The name or IP address of the computer hosting the database from which data is to be downloaded.

-   port_no  
    The port number to be used to connect over TCP or IPC.

-   user_id  
    The database user identifier used by aexport to connect to the database.

-   Password  
    The password for the database user identifier.

-   NLS_USE  
    The character set in which to display data.

The path where the server or client is installed can only be set with the ALTIBASE_HOME environment variable. The rest can be set with command-line options. For more detailed information about command-line options, please refer to "How to Use aexport". 

The ALTIBASE_HOME environment variable must be correctly set, and the aexport property settings file (aexport.properties) must exist and be properly configured for aexport to run successfully. For more detailed information about the aexport.properties file, please refer to "aexport Properties".

ALTIBASE_HOME is usually set automatically when the server is installed. For the client, the user must set it manually. If it is not set, it may not work properly, so it is recommended to check whether it is set correctly before executing.

port_no and NLS_USE can be set with environment variables or the altibase.properties file. If set in more than one way, the following methods take precedence in descending order.

1.  Command-line options

2.  Environment variables (ALTIBASE_PORT_NO, ALTIBASE_NLS_USE)

3.  The altibase.properties file

On omission, the user is prompted to enter a value immediately after aexporthas been executed. aexport may not work normally if the value is invalid.

If the option is not set, the first time aexport is run, it prompts for an option and prompts the user for a value.If incorrect format or an invalid value is entered, aexport may not work properly.

One exception is the NLS_USE option. On omission, the user is not prompted to enter a value, but the database character set is used by default. If the user omits the NLS_USE option in an environment that does not use the US7ASCII character set, aexport will run abnormally with the risk of data loss. Therefore, the user should set the NLS_USE option to a value that is compatible with his or her operating environment.

The user is recommended to set the following environment variables for aexport to run normally:

-   ALTIBASE_HOME: The path where the server or client is installed.

-   ALTIBASE_PORT_NO: The port number used to connect to the server.

-   ALTIBASE_NLS_USE: The character set used to export and import data.

-   PATH: The path to the aexport executable file. It is normally $ALTIBASE_HOME/bin.

#### Environment Variables

##### ALTIBASE_HOME

Sets the directory in which the package was installed. This must be set to use aexport.

##### ALTIBASE_PORT_NO

Sets the port number used to connect to the server. This can also be set with the -port command-line option, or set in advance in the altibase.properties file.

If different values are set for the ALTIBASE_PORT_NO environment variable and the altibase.properties file, the environment variable takes precedence. However, the value set with the -port command-line option overrides both. On omission, the user will be prompted to enter a value after aexport has started.

##### ALTIBASE_SSL_PORT_NO

Sets the server port number that aexport is to connect to over SSL/TLS. 

For the port number in SSL, the -PORT option, environment variables, ALTIBASE_SSL_PORT_NO, and the properties in the altibase.properties file take precedence over each other (in consecutive order). On omission, the user is prompted to enter the port number.

##### ALTIBASE_NLS_USE

Sets the character set use when connecting to the server. This can also be set with the - nls_use command-line option, or be set in advance in the altibase.properties file.

If different values are set for the ALTIBASE_NLS_USE environment variable and the altibase.properties file, the environment variable takes precedence. However, the value set with the -nls_use command-line option overrides both.

Note: If the server character set and the value set in ALTIBASE_NLS_USE are different, it may not work properly. It is recommended to set the appropriate value.



### How to Use aexport

#### Syntax

![](media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05721" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="511" image_path_raw="media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif" image_class="C" format="bnf" verified="True" -->
```bnf
aexport ::=
    AEXPORT
        { -h
        | -s server_name
        | -u user_name
        | -p password
        | -port port_no
        | -tserver server_name
        | -tport port_no
        | -nls national_language_support
        | -object user_name '.' object_name { ',' user_name '.' object_name }
        | -prefer_ipv6
        | -ssl_ca CA_file_path
        | -ssl_capath CA_dir_path
        | -ssl_cert certificate_file_path
        | -ssl_key key_file_path
        | -ssl_verify
        | -ssl_cipher cipher_list }
```
<!-- IMG_RECOVERY_END ref_id="img-05721" -->


#### Parameters

| Parameter                          | Description                                                  |
| ---------------------------------- | ------------------------------------------------------------ |
| \-h                                | Displays the Help menu                                       |
| \-s                                | Sets the host name or IP of the server from which to download data. On omission, the user is prompted for the host name. This can be a host name, an IPv4 address, or an IPv6 address. If it is an IPv6 address, it must be enclosed in square brackets (“[ ]“). The localhost (the same computer on which aexport is executed) can be set as the computer's host name, the localhost’s IPv4 address (usually 127.0.0.1), or the localhost IPv6 address (usually [::1]). For more information about Altibase and IPv6 address notation, please refer to the *Administrator's Manual.* |
| \-u                                | This sents the name of the Altibase user to access the server from whichd data is to be downloaded. On omission, the user is prompted for the user name.This option must be set to the SYS user to perform a full DB mode export. <br/>Use double quotation marks if there are lower case letters, special characters or spaces in the username. -u \"user name\" |
| \-p                                | Sets the password for the user. On omission, the user is prompted for a password. |
| \-port                             | Sets the server port number to access for data download. On omission, the ALTIBASE_PORT_NO environment variable and the altibase.properties setting are checked in turn to determine the port number. If neither is set, the user is prompted for a port number. |
| \-object                           | This option specifies an object which will be extracted along with the owner name. Use double quotation marks if there are lower case letters, special characters or space in the object name. -object \"user name\".\"table name\" |
| \-tserver                          | Sets the destination server (the server to which the exported data is to be uploaded). This information is written to the script files that are created when aexport is executed, and used when those scripts are subsequently executed. As with the -s option, this can be a host name, an IPv4 address or an IPv6 address. |
| \-tport                            | Sets the destination server port number. This information is written to the script files that are created when aexport is executed, and used when those scripts are subsequently executed. |
| \-nls_use                          | Sets the character set to export (download) data from the source database and import (upload) data to the destination database. At present, the supported character sets are US7ASCII, KO16KSC5601, MS949, BIG5, GB231280, MS936, UTF8, SHIFTJIS, MS932 and EUCJP. |
| \-prefer_ipv6                      | This option determines whether to first attempt to resolve a host name to an IPv4 address or an IPv6 address. If a host name is specified for the -s option and this option is used, aexport will first attempt to resolve the host name to an IPv6 address. In contrast, if a host name is specified for the -s option and this option is omitted, aexport will first attempt to resolve the host name to an IPv4 address. That is, the default behavior is to attempt to resolve the host name to an IPv4 address. If aexport fails to connect using the preferred IP address type, it attempts to connect using the other IP address type. For example, when localhost is specified for the -s option and this option is used, aexport first tries to connect to the [::1] IPv6 address. If this attempt fails, aexport then attempts to connect to the 127.0.0.1 IPv4 address. |
| \-ssl_ca *CA_file_path*            | Specifies the location of the certification authority (CA) certificate in which the public key of the Altibase server to be connected to is incorporated. |
| \-ssl_capath *CA_dir_path*         | Specifies the directory under which the certification authority (CA) certificate in which the public key of the Altibase server to be connected is incorporated. |
| \-ssl_cert *certificate_file_path* | Specifies the location of the client authentication file.    |
| \-ssl_key *key_file_path*          | Specifies the location of the client private key file.       |
| \-ssl_verify                       | Verifies the certificate the client receives from the server. |
| \-ssl_cipher *cipher_list*         | Specifies a cipher list for SSL encryption. Please refer to the SSL_CIPHER_LIST property in the *General Reference.* |

> For more detailed information about SSL connection, please refer to Chapter 2. Connecting and Disconnecting in the *iSQL User’s Manual.* 

#### The Data Migration Process

The process of using aexport to migrate data can be roughly divided into the following steps:

-   Generate SQL script files for creating the structure of the objects to be exported from the source database and shell script files for executing the SQL script files
-   Export (download) the data from the source database
-   Create the required database structures in the destination database
-   Import (upload) the data to the destination database
-   Refresh the materialized view in the destination database, and create indexes and foreign keys in the destination database, and then switch the data access mode

##### Exporting the Source Database Structure

aexport is first used to generate SQL script files that contain information about the structure of the source database and shell script files for executing the SQL script files.

- Execute aexport

```
$ aexport –s 127.0.0.1 –u sys –p manager
```


-   Enter the passwords of the Altibase users at the prompts. This sets the password for each user that is created in the destination database. 
-   When using aexport to back up the data on a remote server, indicate the address of the remote server and the port through which to connect to the remote server.

```
$ aexport –s 222.112.84.200 –port 20300 –u sys –p manager
```


##### Exporting Data from the Source Database

Export (download) the data from the source database by executing the shell script that was created by aexport in the previous step.

-   Check the disk to which the data are to be downloaded to ensure that it has enough free space to hold the data. Because data in text form can occupy more space than the data in internally used data files, it is recommended that the amount of available free space be twice the size of the original data files.
-   Execute the "run_il_out.sh" script.

```
$ sh run_il_out.sh
```


##### Creating the Destination Database Structure

-   Copy all SQL scripts and shell scripts and all 'fmt', 'log', and 'dat' format files created by the “run_il_out.sh” shell script to the system on which the destination database is located. Skip this step if the destination database is on the same system as the source database.

-   Start up the destination database.

-   Execute the “run_is.sh” script.

```
$ sh run_is.sh
```

-   Use iSQL to access the database and check whether all of the required database objects were properly created. If the required database structure was not properly created, inspect the output that was displayed on the screen while run_is.sh was executing to determine the cause of the problem.

##### Importing Data into the Destination Database

- Execute the “run_il_in.sh” script.

```
$ sh run_il_in.sh
```


-   Check the directory containing the “run_il_in.sh” shell script file to see whether it contains any files that have the “*.bad” filename extension and are greater than 0 bytes in size. If such a file exists, inspect the contents of the “*.bad” file and the log files related to the table having the same name as the “*.bad” file and take suitable steps to resolve the problem. For more information on how to resolve such problems, please refer to the *iLoader User's Manual.*

##### Refresh the materialized view in the destination database, and create indexes and foreign keys in the destination database, and then switch the data access mode

When the TWO_PHASE_SCRIPT property is set to "Off":

- Execute the "run_is_refresh_mview.sh" script.

```
$ sh run_is_refresh_mview.sh
```


- Execute the “run_is_index.sh” script.

```
$ sh run_is_index.sh
```


- Execute the “run_is_fk.sh” script.

```
$ sh run_is_fk.sh
```


- Execute the “run_is_alt_tbl.sh” script.

```
$ sh run_is_alt_tbl.sh
```


When TWO_PHASE_SCRIPT = ON:

- Execute the “run_is_con.sh” script.

```
$ sh run_is_con.sh
```




#### Notes

-   If a normal user who is not the SYS user executes aexport, scripts are created only for the user's schema.
-   If a normal user who is not the SYS user executes aexport, scripts are created for replication objects.
-   If a normal user who is not the SYS user executes aexport, CREATE TABLE privileges are required. This is because aexport creates temporary tables to analyze object interdependencies.
-   Do not run two or more aexport processes at the same time. Because aexport uses a temporary table to store created SQL scripts, running two or more aexport processes at the same time will yield unpredictable results.
-   If the EXECUTE and TWO_PHASE_SCRIPT aexport properties are both set to ON and the OPERATION property is set to IN when uploading data, this uploading operation will not be affected by the value of the INDEX property, because no SQL script file dedicated to creating the index is generated.  
    Therefore, when it is desired to perform the uploading operation (EXECUTE = ON and OPERATION = IN) with ON for the INDEX property, the TWO_PHASE_SCRIPT property must be set to OFF.
-   When the “run_is.sh” script is executed, all existing users and objects will be deleted from the database. Therefore, care must be taken to avoid executing this script on the source database.
-   If the -tserver and -tport options are not specified, then the -s and -p parameters are used not only to identify the source server from which data are downloaded, but are also used in all created scripts to identify the destination server to which data will be uploaded. To specify a destination server and port that are different from the source server and port,  use the -tserver and -tport options. In this case, the -s and -p options will only identify the source server from which data are downloaded, whereas the values specified for the -tserver and -tport options will be written into the created scripts.

```
$ aexport -s 127.0.0.1 -u sys -p manager -tserver 192.168.1.10 –tport 21300

$ cat run_il_in.sh

iloader -s 192.168.1.10 -port 21300 -u SYS -p MANAGER in -f SYS_T1.fmt -d
SYS_T1.dat -log SYS_T1.log -bad SYS_T1.bad
```


-   If CALLBACK functions are specified using PASSWORD_VERIFY_FUNCTION at user creation, the user’s password must be set to correspond to validity functions before user importation. Validity functions must also be imported before importing the user to the database.
-   Double quotation marks should be used if there are lower case letters, special characters or spaces in the user name or the name of objects which will be extracted.



#### Limitations

-   If a stored procedure needs to refer to when creating a stored procedure is not created in advance, the operation will fail. aexport cannot guarantee the order in which stored procedures are created because they cannot access information about dependencies between stored procedures. In this case, the stored procedure creation can fail, so the stored procedure must be created in the destination  database.
-   aexport only has limited access to the meta information of the sequence. Because of this restriction, only the sequence characteristics specified by the INCINMENT BY of a sequence created in an account other than the SYS user are reflected, and the remaining attributes are set to the default values. If these constraints are a problem, the sequence must be created in the destination database.
-   In creating an object in the destination database, the base table must be created before creating the Material View. Because aexport does not guarantee the table creation order for creating materialized views, it may fail to create a materialized view. In this case, the user must manually create a materialized view
-   When aexport extracts the materialized view creation statement from the source database, it imports the statement that originally created the materialized view. That is, even if the DDL statement that changes the refresh method or refresh change time is executed for the materialized view in the source database, the change is not reflected in the statement extracted by aexport.



#### SSL Connection and Script Files

-   If aexport is executed on SSL, the SSL option that was specified to execute aexport is used with the source database connection script (run_il_out.sh).
  
-   In to connect an SSL to the target databe, the SSL related properties must be set in the property file.  Refer to ILOADER_ARRAY in the aexport property section for a detailed description.  
    ILOADER_ARRAY = *count* (Default: 1)  
    Speifcies the number of rows to process at once when downloading or uploading data to iLoader.
    
-   ILOADER**\_**COMMIT  
    ILOADER**\_**COMMIT = *count* (Default: 1000)  
    Specifies the unit (number) to commit when uploading data to iLoader. The value of the -commit option can be specified with this property.
    
-   ILOADER_PARALLEL  
    ILOADER_PARALLEL = *count* (Default: 1)  
    Specifies the number of threads to process in parallel when downloading or uploading to iLoader.
    
-   ILOADER_ASYNC_PREFETCH  
    ILOADER_ASYNC_PREFETCH = OFF\|ON\|AUTO (Default: OFF)  
    Sets asynchronous prefetch behavior when downloading data to iLoader. For more informaiton please refer to the '-async_prefetch' option in the *iLoader User's Manual.*
    
-   Refer to the SSL_ENABLE property.



#### aexport Properties

##### Setting the aexport Properties

Some of the settings that govern the use of aexport are made in the aexport.properties file. The aexport.properties file must be located in the $ALTIBASE_HOME/conf directory. (This file is not to be confused with the altibase.properties file, which by default is located in the same directory.)

When Altibase is installed, the \$ALTIBASE_HOME/conf directory does not actually contain a file called aexport.properties, but it does contain a sample properties file called aexport.properties.sample. It is thus necessary to copy the aexport.properties.sample, paste it into the same directory, and rename it as aexport.properties before executing aexport. If aexport cannot find the aexport.properties file in \$ALTIBASE_HOME/conf, it will raise an error and terminate.

##### List of aexport Properties

-   OPERATION  
    OPERATION = IN/OUT  
    If this property is set to OUT, scripts for exporting all schemas and data will be created. When the data export script, which consists of iLoader commands, is executed, form files (.fmt) and data files (.dat) will be created.  
    If this property is set to IN, the schema creation script and the data loading script, which were created by previously executing aexport with this property set to OUT, will be executed, the schema will be created in the destination database, and the data will be loaded into the destination database. The schema creation script and the data loading script can be executed manually at a shell prompt without executing aexport.
    
-   EXECUTE  
    This property determines whether to automatically execute the scripts that were created.  
    EXECUTE = ON/OFF  
    If it is set to ON, the scripts that are appropriate for the current operation (set using the OPERATION property) will be executed automatically. The file names of these scripts are set using the ILOADER_OUT, ILOADER_IN, ISQL, ISQL_CON, ISQL_INDEX, ISQL_FOREIGN_KEY, ISQL_ALT_TBL, and ISQL_REPL properties.  
    If it is set to OFF, the scripts will be created, but not executed.
    
-   INVALID_SCRIPT  
    This property determines whether to group all of the object creation scripts for invalid objects in a single script file.  
    INVALID_SCRIPT = ON/OFF  
    If this property is set to OFF, a SQL script file will be generated for each of the invalid objects in the database; that is, they will be treated just like the valid database objects.
    
-   TWO_PHASE_SCRIPT  
    This property determines whether to group all of the object creation scripts in two script files.  
    TWO_PHASE_SCRIPT = ON/OFF  
    If this property is set to ON, aexport will create only two SQL script files and two shell script files: ALL_OBJECT.sql, ALL_OBJECT_CONSTRAINS.sql, ALL_OBJECT.sql, run_is.sh, run_is_con.sh  
    If this property is set to OFF, aexport will generate different SQL script files for each of the objects in a database.
    
-   CRT_TBS_USER_MODE  
    CRT_TBS_USER_MODE = ON/OFF (Default: OFF)  
    This property determines whether or not to extract a statement for creating tablespace in user mode.  
    If this property is set to ON, the SQL statement creating tablespace related to the user in the user mode is extracted. The user related tablespaces are default tablespace, default temporary tablespace, and the tablespace specified whether or not to available to be accessed.
    
-   INDEX  
    INDEX = ON/OFF  
    This property determines whether or not to create the indexes when creating the rest of the schema in the destination database. If it is desired to create the indexes after the data have been located into the destination database, set this property to ON. It is used when the TWO_PHASE_SCRIPT property is set to OFF.
    
-   USER_PASSWORD  
    USER_PASSWORD = *password*  
    This property is used to set the password when the users exported from the source database are created in the destination database. (Because aexport does not know the passwords of users exported from the source database, the passwords must be manually set.) If this property is not set, a prompt for setting each user's password will appear.
    
-   VIEW_FORCE  
    VIEW_FORCE = ON/OFF  
    If this property is set to ON, views will be forcibly created, even if the underlying tables or other objects don't exist.
    
-   DROP  
    This property determines whether to include DROP statements in created scripts.  
    DROP = ON/OFF  
    If this property is set to ON, and if the destination database already contains objects corresponding to those that are to be created, the existing objects will be dropped. Because this option specifies that existing objects are to be dropped, it should be used with caution.  
    Note) If aexport is executed in Object Mode, DROP statements are not generated, regardless of the setting of this property.
    
-   ILOADER_OUT  
    ILOADER_OUT = *run_il_out.sh*  
    This property determines the name of the shell script file that is created to export (download) the data from the source database. It is used when the OPERATION property is set to OUT.
    
-   ILOADER_IN  
    ILOADER_IN = *run_il_in.sh*  
    This property determines the name of the shell script file that will be used to import (upload) the data into the destination database.
    
-   ISQL  
    ISQL = *run_is.sh*  
    This property determines the name of the script file that will be used to create the database schema in the destination database.
    
-   ISQL_CON  
    ISQL\_ CON = *run_is_con.sh*  
    This property determines the name of the shell script file that is used to execute the SQL script files for creating indexes, foreign keys, triggers and replication objects. It is used when the TWO_PHASE_SCRIPT property is set to ON.
    
-   ISQL_INDEX  
    ISQL_INDEX = *run_is_index.sh*  
    This property determines the name of the shell script that will be used to create indexes in the destination database. If no value is specified for this property in the aexport.properties file, this shell script file will not be generated.
    
-   ISQL_FOREIGN_KEY  
    ISQL\_ FOREIGN_KEY = *run_is_fk.sh*  
    This property determines the name of the shell script file that is used to execute the SQL script files for creating foreign keys. If no value is specified for this property in the aexport.properties file, this shell script file will not be generated.
    
-   ISQL_REPL  
    ISQL_REPL = *run_is_repl.sh*  
    This property determines the name of the shell script that will be used to create replication objects in the destination database. If no value is specified for this property in the aexport.properties file, this shell script file will not be generated.
    
-   COLLECT_DBMS_STATS  
    This property determines whether to display the statistics for tables, columns and indexes of specified user.  
    COLLECT_DBMS_STATS = ON/OFF  
    The default value is OFF and no statistical information is exported. When this property's value is ON, statistics information is exported.
    
-   ISQL_REFERSH_MVIEW  
    ISQL_REFERSH_MVIEW = *run_is_refresh_mview.sh*  
    This property determines the name of the shell script that will be used to execute the SQL script files for refreshing the materialized view in the destination database. If no value is specified for this property in the aexport.properties file, this shell script file will not be generated.
    
-   ISQL_ALT_TBL  
    ISQL_ALT_TBL = *run_is_alt_tbl.sh*  
    This property sets the name of the shell script file executing the SQL script which switches the data access mode for the tables and partitions of the target database. On omission, aexport does not generate this shell script file.
    
-   ILOADER_FIELD_TERM  
    ILOADER_FIELD_TERM = *field_term*  
    This property is used to set the field delimiters that are used when the data in tables are saved as text. If this property is not set, the default delimiter between values is the comma (“,”), no block delimiters are used for numeric values, and double quotation marks (“ “ “) are used as block delimiters around strings.  
    Note) The pound (i.e. hash or number sign) character “#” cannot be specified as a delimiter, because it is used to denote comments in the properties file (The remainder of the line after the “#” will be ignored).
    
-   ILOADER_ROW_TERM  
    ILOADER\_ ROW \_TERM = *row_term*  
    This property sets the record delimiter to use when texting table data. If not set, the default is <LF\>.  
    Note) The pound (i.e. hash or number sign) character “#” cannot be specified as the record delimiter, because it is used to denote comments in the properties file (The remainder of the line after the “#” will be ignored).
    
- ILOADER_PARTITION  

  This property determines whether the iLoader scripts are generated for each partition when there is a partitioned table in the source database. 
  ILOADER\_ PARTITION = ON/OFF  

  When this property is set to ON, scripts for extracting form files and data for each partition are generated in run_il_out.sh. Similarly, scripts for loading data for each partition are generated in run_il_in.sh.

  When this property is set to OFF, scripts for handling partitioned tables are generated to use a single data file for extraction and loading, similar to non-partitioned tables.

  For more detailed information, please refer to the *iLoader User's Manual.*  

-   ILOADER_ERRORS  
    ILOADER_ERRORS = *count* (Default: 50)  
    This property specifies the number of allowable maximum errors when uploading data with iLoader. The default value of this property is set to 50, and the upload is continuously executed regardless of the number of incurring errors if the default value is set to 0.
    
-   ILOADER_ARRAY  
    ILOADER_ARRAY = *count* (Default: 1)  
    This property specifies the number of rows to be processed at once when downloading or uploading data with iLoader.
    
-   ILOADER**\_**COMMIT  
    ILOADER**\_**COMMIT = *count* (Default: 1000)  
    This property specifies the unit(number) to commit when uploading the data with iLoader. The value of -commit option can be specified as well.
    
-   ILOADER_PARALLEL  
    ILOADER_PARALLEL = *count* (Default: 1)  
    This property specifies the number of threads which will be executed with parallel processing when uploading or downloading with iLoader.
    
-   ILOADER_ASYNC_PREFETCH  
    ILOADER_ASYNC_PREFETCH = OFF\|ON\|AUTO (Default: OFF)  
    This property sets asynchronous prefect behavior when downloading data to iLoader. For more information, please refer to the '-async_prefetch' option in the *iLoader User's Manual.*
    
-   SSL_ENABLE  
    This property specifies whether to connect to the target database using the SSL protocol.  
    SSL_ENABLE = ON/OFF  
    If this property is set to ON, SSL-related options are enabled for iSQL and iLoader commands in the shell scripts (run_is.sh and run_il_in.sh) to be executed on the target database.  
    SSL-related options can be enabled with the SSL_CA, SSL_CAPATH, SSL_CERT, SSL_KEY, SSL_CIPHER, SSL_VERIFY properties. For further information about these properties, please refer to Parameters.



#### Example

##### Execution in Full DB Mode

```
$ aexport -s 127.0.0.1 -u sys -p manager
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TBS #####
##### USER  #####
##### SYNONYM #####
##### DIRECTORY #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
##### REPLICATION #####
##### JOB #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
ALL_ALT_TBL.sql 
ALL_CRT_DIR.sql
ALL_CRT_FK.sql
ALL_CRT_INDEX.sql
ALL_CRT_JOB.sql
ALL_CRT_LIB.sql
ALL_CRT_LINK.sql
ALL_CRT_REP.sql
ALL_CRT_SEQ.sql
ALL_CRT_SYN.sql
ALL_CRT_TBL.sql
ALL_CRT_TBS.sql
ALL_CRT_TRIG.sql
ALL_CRT_USER.sql
ALL_CRT_VIEW_PROC.sql
ALL_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh
```



##### Execution in User Mode

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
$ aexport -s 127.0.0.1 -u user1 -p user1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### USER #####
##### SYNONYM #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
USER1_ALT_TBL.sql
USER1_CRT_DIR.sql
USER1_CRT_FK.sql
USER1_CRT_INDEX.sql
USER1_CRT_LIB.sql
USER1_CRT_LINK.sql
USER1_CRT_SEQ.sql
USER1_CRT_SYN.sql
USER1_CRT_TBL.sql
USER1_CRT_TRIG.sql
USER1_CRT_USER.sql
USER1_CRT_VIEW_PROC.sql
USER1_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh

```



##### Execution in Object Mode

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
iSQL> CONNECT user1/user1;
iSQL> CREATE TABLE t1(i1 INTEGER);
Create success.
iSQL> CREATE VIEW v1 AS SELECT i1 FROM t1;
Create success.
iSQL> CREATE MATERIALIZED VIEW m1 AS SELECT * FROM t1;
Create success.
iSQL> CREATE OR REPLACE PROCEDURE proc1(p1 IN INTEGER)
AS a INTEGER;
BEGIN
SELECT * INTO a FROM t1 WHERE i1 = 1;
END;
/
Create success.

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
$ ls
user1_t1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.m1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### MATERIALIZED VIEW #####
$ ls
user1_m1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1,user1.v1,user1.proc1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
##### VIEW #####
##### STORED PROCEDURE #####
$ ls
user1_proc1_CRT.sql
user1_t1_CRT.sql
user1_v1_CRT.sql

```



##### SSL Property Setting

```
SSL_ENABLE = ON  # OFF
SSL_CA     = ${ALTIBASE_HOME}/cert/ca-cert.pem
#SSL_CAPATH = ${ALTIBASE_HOME}/cert
SSL_CERT   = ${ALTIBASE_HOME}/cert/client-cert.pem
SSL_KEY    = ${ALTIBASE_HOME}/cert/client-key.pem
SSL_CIPHER = RC4-SHA:RC4-MD5
SSL_VERIFY = ON  # OFF
```





# 2. altiComp

This chapter describes the altiComp utility and its features such as consistency control. 

### Introducing altiComp

The altiComp utility monitors the progress of replication between two Altibase databases and resolves data inconsistencies that arise during the course of replication.

altiComp compares Altibase with another HDB on a table-by-table basis, and outputs information about any inconsistencies it finds. It also has a feature for synchronizing two databases in the event of data inconsistencies.

#### altiComp Terms

##### Master Server

Master Server is a server to be corrected when a discrepancy record is found between two servers. When running altiComp, either server can be designated as master.

##### Master DB

The database on the master server.

##### Slave Server

When the discrepancy record between two servers is found, Slave Server is the server to be corrected according to the reference database. When running altiComp, either server can be designated as a slave.

##### Slave DB

The database on the slave server.

#### Different Records

Different records are records whose column values do not match based on the primary key between the Master DB and Slave DB.

There are three types of differences:

-   MOSX difference: When a record based on a primary key can be found in the Master DB but not in the Slave DB.
-   MOSO difference: When a record based on a primary key can be found in both the master and slave tables but the record contents are different.
-   MXSO difference: When a record based on a primary key can be found in the Slave DB but not in the Master DB.

#### Synchronization Policy

A synchronization policy is a policy that specifies how to synchronize different records. alticomp usually treats the Master DB as the reference DB and synchronizes the Slave DB with it.

Altibase provides four synchronization policies: 

-   SU Policy: This policy resolves MOSO differences by updating the Slave DB with the contents of the Master DB.
    ![](media/Utilities/su_policy_eng.png)
-   SI Policy: This policy resolves MOSX differences by inserting records from the Master DB into the Slave DB.
    ![](media/Utilities/si_policy_eng.png)
-   MI Policy: This policy resolves MXSO differences by inserting records from the Slave DB into the Master DB.
    ![](media/Utilities/mi_policy_eng.png)
-   SD Policy: This policy resolves MXSO differences by deleting records from the Slave DB. 

![](media/Utilities/sd_policy_eng.png)

The SU policy, SI policy, MI policy, and SD policy are set in the altiComp environment file. Note that the MI policy and the SD policy are mutually exclusive, meaning that they cannot both be enabled at the same time.

##### DIFF

Creates an execution result file that identifies inconsistent records found during replication between the Master DB and the Slave DB.

##### SYNC

Identifies inconsistent records between the Master DB and the Slave DB, bidirectionally resolves inconsistencies according to the synchronization policy set in the altiComp environment file, and creates an execution result file including execution summary information and error information.

##### altiComp Environment File

An environment file is for setting options for altiComp. This file includes conneciton information, altiComp function settings, synchronization policies, etc.



### How to Use altiComp

This chapter describes the altiComp environment file that contains information for running altiComp, and explains the DIFF and SYNC features.

#### How to Execute altiComp

To use altiComp, an altiComp environment file, which contains information about the table(s) on which DIFF or SYNC is to be executed, must first be created. The altiComp environment file will be explained in the How to Use altiComp section.

altiComp commands have the following form: 

```
$ altiComp -f script_file_name
```

script_file_name : File name including the path of the environment file

If the current directory is: /user/charlie/altibase_home/altiComp:

```
/user/charlie/altibase_home/altiComp> altiComp script_file_name
```

Or

```
/user/charlie/altibase_home/altiComp> altiComp  ./script_file_name
```



#### How to Set altiComp Properties

Each comparison and synchronization task that is described in the environment file, has its own unique properties. The properties provide information necessary for running altiComp (Please refer to the sample.cfg file in the ALTIBASE_HOME/altiComp directory).

##### Rules for Setting Properties

Properties follow the format “**property name = property value**” and are case-insensitive. 

The following symbols have special meanings when used in the environment file:

-   “ **\#** “ (sharp) indicates a comment and causes the remainder of the line to be ignored. 
-   “ **{ }** “ (curly braces) used to indicate that a property value spans multiple lines.
-   “ **;** “ (semicolon) serves as a delimiter to separate multiple values.
-   “ **“** “ (double quotation marks) are used to enclose a string (such as a user name, password, table name, or column name) that includes one or more reserved words or special characters.
-   In Altibase, the following are special characters: \~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \|

##### Property Names

A property name consists of characters other than spaces, and identifies a property within a group.

##### Property Values

A property can take a single value, multiple values, or an expression. 

-   An expression may include blanks. Most properties follow this format:
    Ex) TABLE = EMPLOYEE

-   Multiple values consist of several values separated by the “**;**” delimiter, and must be contained within “{}” if they occupy more than one line (see Example 2). The “EXCLUDE” group allows multiple values.
    Ex) EXCLUDE = ENO; DNO; ENAME
    Or EXCLUDE = {ENO; DNO; ENAME}
-   Expressions are character strings, can include spaces, and must be enclosed within “{}”. The “WHERE” property is an expression.
    Ex) WHERE = { ENO \> ‘1000’ and ENO \< ‘2000’ }

##### Data Type Support

The EXCLUDE property is used as follows to exclude a particular column or columns from altiComp targets.

Example 4) Exclude a certain column from altiComp targets, if a CLOB column exists in the EMP table. 

TABLE = EMP
EXCLUDE = { CCC }

#### Property Options

Use the following properties to specify information for accessing the local and remote servers, comparison (DIFF) and synchronization (SYNC) tasks, and synchronization policies for inconsistent records. 

##### DB_MASTER

This is used to set the server whose contents are to be accepted as correct if inconsistent records are found between two servers.

Sets the user name and password, the name or IP address of the server, and NLS_USE. The property values must match the information in the property file in the home directory of Altibase.

- TCP Connection:

```
DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=20300;NLS_USE=US7ASCII
```

- SSL Connection:

```
DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=${ALTIBASE_SSL_PORT_NO};NLS_USE=US7ASCII;CONNTYPE=6;SSL_CA=/home/altibase/cert/ca-cert.pem;SSL_CERT=/home/altibase/cert/client-ert.pem;SSL_KEY=/home/altibase/cert/client-key.pem
```


For more detailed  information about connection string attributes for SSL, please refer to the *SSL/TLS User’s Guide.* 

##### DB_SLAVE

This is used to set the other server. 

This sets the user name and password, the name or IP address of the server, and NLS_USE. The property values must match the information in the property file in the home directory of Altibase. 

##### OPERATION

This is set to “DIFF” for a comparison task, or to “SYNC” for a synchronization task.

##### INSERT_TO_SLAVE

This sets the SI policy used to resolve MOSX inconsistencies. Specifies whether to insert the record in question into the Slave DB. The property value is set to “ON” to specify that the record is to be inserted, and “OFF” to specify that it is not to be inserted.

##### INSERT_TO_MASTER

This sets the MI policy used to resolve MXSO inconsistencies. Specifies whether to insert the  52 Utilities Manual record in question into the Master DB. The property value is set to “ON” to specify that the record is to be inserted, and “OFF” to specify that it is not to be inserted. 

This property and DELETE_IN_SLAVE cannot both be set to “ON” simultaneously.

##### DELETE_IN_SLAVE

Sets the SD policy used to resolve MXSO inconsistencies. Specifies whether to delete the record in question from the Slave DB. The property value is set to “ON” to specify that the record is to be deleted, and “OFF” to specify that it is not to be deleted. 

This property and INSERT_TO_MASTER cannot both be set to “ON” simultaneously.

##### UPDATE_TO_SLAVE

This sets the SU policy used to resolve MOSO inconsistencies. Specifies whether to update the record in question in the Slave DB. The property value is set to “ON” to specify that the record is to be changed, and “OFF” to specify that it is not to be changed. 

##### CHECK_INTERVAL

This sets the interval between the completion of a SYNC operation on a table and the start of a SYNC operation on the next table. Expressed in units of ms (milliseconds).

##### MAX_THREAD

This specifies the maximum number of threads that can run concurrently. Set to -1 to specify an unlimited number of threads.

##### COUNT_TO_COMMIT

This specifies the number of changed data(INSERT, DELETE or UPDATE) to be committed at once. The default value is 1000.

##### FILE_MODE_MAX_ARRAY

If its value is greater than 1, altiComp writes the fetched data to a file and then starts a SYNC or DIFF operation on the file. This value is used to set the maximum size of array(s) for fetching data. altiComp fetches a number of records equal to this value and writes them to a csv file. 

This option can be used to realize better performance. However, when a target table has many LOB type columns, this option may not improve performance. 

This option can only be used between Altibases.

Ex) FILE_MODE_MAX_ARRAY = 1000

#### TABLES Group

This defines information related to target table(s). The number of descriptions in the group must equal the number of target tables, and the name of each group must correspond to the name of a table in the Master DB. 

The following properties can be set:

##### WHERE

Sets conditions for selecting table records. This property is described in the same way as a WHERE clause of a SQL statement. Multiple values are permitted, but the “;” delimiter cannot be used to specify multiple values. Moreover, this property cannot be commented. 

This applies to the comparison (DIFF) and synchronization (SYNC) functions. 

##### EXCLUDE

This sets conditions for the projection of table records. The property may have multiple values. The specified columns are excluded from comparison and synchronization operations. 

![](media/Utilities/e9cd168e51d8336eb99f9ba958d9688d.png)

![](media/Utilities/c8502d42132454c28fe8e7f0edd7c88b.png)

With the proper combination of WHERE and EXCLUDE, the result of combining selection and projection altiComp can be used.

![](media/Utilities/3a664d250cbb847a5d4acd3acf65b5d1.png)

##### TABLE

This sets the Slave DB table name. In cases where the table names on the Master DB and the Slave DB differ from each other, this must be explicitly described in order to use the comparison (DIFF) and synchronization (SYNC) functions. if omitted, it is assumed that the table name on the Slave DB is the same as that on the Master DB. 

The table name can contain Roman alphabetic characters, numbers, and the following special characters: ((space,\~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \|)

However, it cannot contain Korean characters.

##### SCHEMA

This specifies the table schema in the Slave database

If the schema name of the connecting user of Slave is different from the schema of the target table, it must be described. If omitted, the schema of the connecting user of Slave is used.

### Comparison (DIFF) Function

This function identifies different records that are found during replication between the Master and Slave databases, and creates an execution result file.

#### Environment File

In the altiComp environment file, set the OPERATION property to “DIFF”. 

All execution option properties must be specified, and the table group properties WHERE, EXCLUDE, TABLE, and SCHEMA can be optionally specified.

#### Execution

The comparison (DIFF) function is executed as follows:

```
$ altiComp -f script_file_name
```

script_file_name: File name including the path of the environment file

#### Execution Results

This function compares the contents of the Master and Slave Databases with each execution log file and table, and creates an execution result file that includes the contents of inconsistent columns of inconsistent records.


For example, if the following altiComp command is running successfully, /user/charlie/altibase_home/altiComp> altiComp sample.cfg a “mastertable-username.slavetable.log” file is created for each table in the altiComp directory, alongside sample.log. 

##### Execution Log File

This file is created as “script_file_name.log” and displays the contents of the executed environment file with a summary of the comparison (DIFF) task for each table in the TABLES group. 

The contents of the environment file are displayed as follows:

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX = DF, Count :          1
MXSO = DF, Count :          0
MOSO = DF, Count :          1

 SCAN TPS:   20547.95
     Time:       0.00 sec
```



##### Execution Result File

This file is created as “mastertable username.slavetable.log” and displays the comparison results in the following format. 

```
DF[m,n]-> COL_N (Vn_M, Vn_S):PK->{ PCOL_V }
```



-   DF : The type of inconsistency (MOSX, MOSO, MXSO) 
-   m : The record number on the Master server 
-   n : The record number on the Slave server 
-   COL_N : The name of the first column that has different values after comparison
-   Vn_M : The value in the corresponding column on the Master server 
-   Vn_S : The value in the corresponding column on the Slave Server

However, for records that have LOB type columns, the LOB column value is not output.

#### Comparison (DIFF) Examples

The following examples compare the EMP table of host1 with the EMPLOYEES table of host2, and the DEPARTMENTS table of host1 and the DEPARTMENTS table of host2. 

##### DIFF Example 1

Specify DB_MASTER as host1 and DB_SLAVE as host2. The environment file for comparing all the records in each table should look like this:

```
DB_MASTER = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
DB_SLAVE = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = DIFF
MAX_THREAD = -1
			
DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS 

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

The name of the target table for the Master Server (host1) and Slave Server (host2) may differ, as shown in the above example. 

##### DIFF Example 2

From the EMP table, select the values to be compared according to the ENO column, and exclude the JOIN_DATE and GENDER columns as below. 

The CONDITION property specifies that the EMP records to be compared as limited to “ENO >= 1 and ENO <= 20". 

The EXCLUDE property specifies that the JOIN_DATE and GENDER columns are not to be compared. 

In other words, if all columns (other than the JOIN_DATE and GENDER columns) are identical, it is assumed that the record is the same. 

```
[EMP]
TABLE = EMPLOYEES
WHERE = {ENO >= 1 and ENO <= 20}
EXCLUDE = {JOIN_DATE; SEX}
[DEPARTMENTS]
```



##### DIFF Example 3

From the EMP table, select the values to be compared according to the ENO and JOIN_DATE columns, and exclude the GENDER column as below.

```
[EMP]
TABLE = EMPLOYEES
WHERE = {(ENO >= 1 and ENO <= 20) or (JOIN_DATE >= ‘20001010’)}
EXCLUDE = {SEX}

[DEPARTMENTS]
```

The WHERE property determines whether the EMP records for comparison are to be limited by “ENO >= 1 and ENO <= 20" or “JOIN_DATE >= 20001010”. The EXCLUDE property specifies that the GENDER column is not to be compared.



### Synchronization (SYNC) Function

This function identifies records that are inconsistent between the Master and Slave databases, bidirectionally resolves the differences according to the synchronization policy in the altiComp configuration file, and creates an execution result file including execution summary information and error information.

#### Environment File

In the altiComp environment file, set the OPERATION property to “SYNC”. 

All execution option properties must be described, and the table group properties WHERE, EXCLUDE, TABLE, and SCHEMA can be optionally specified.

#### Execution

The synchronization (SYNC) function is executed as follows:

```
$ altiComp -f script_file_name
```

script_file_name: File name including the path of the environment file

#### Execution Results

This function compares the contents of the Master and Slave databases with each execution log file and table, and creates an execution result file that consists of information about synchronization tasks conducted on different records and an error log that includes information about errors which occurred during synchronization.

##### Execution Log File

This file is created as “script_file_name.log” and displays the contents of the executed environment file as well as the summary of the synchronization (SYNC) task for the table(s) in each TABLES group. 

The contents of the environment file are written to the log file as follows:

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX =  -, SI 
MXSO =  -, -
MOSO =  -, SU
MXSX =  -, -

-----------------------------------------
 Operation  Type      MASTER           SLAVE
-----------------------------------------
 INSERT     Try           0               1
             Fail           0               0

 UPDATE    Try           X               1
             Fail           X               0

 DELETE    Try           X               0
             Fail           X               0
-----------------------------------------
 UPDATE    Try           0               2
             Fail           0               0
 OOP  TPS:   13698.63
 SCAN TPS:   20547.95
     Time:       0.00 sec
```

If a failure occurs for any record, the cause of the error and the record contents are written to the log file.

#### Synchronization (SYNC) Examples

The following examples show how to specify OPERATION and TABLE for the synchronization policy to resolve data inconsistency. 

##### SYNC Example 1

Insert an MOSX inconsistent record (a record that exists in the Master server, but not in the Slave server) into the Slave server, and ignore an MXSO inconsistent record ( a record that exists in the Slave server, but not in the Master server). 

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

The INSERT_TO_SLAVE property has been set to “ON” because the SI policy is required to resolve MOSX inconsistency. Likewise, the INSERT_TO_MASTER and DELETE_IN_SLAVE properties have been set to “OFF” because the MI and SD policies required to resolve MSXO inconsistency have been ignored. 

##### SYNC Example 2

Insert an MOSX inconsistent record (a record that exists in the Master Server, but not in the Slave server) into the Slave server, and an MSXO inconsistent record (a record that exists in the Slave server, but not in the Master server) into the Master server. 

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

The INSERT_TO_SLAVE property has been set to “ON” because the SI policy is required to resolve MOSX inconsistency. Likewise, the INSERT_TO_MASTER property has been set to “ON” because the MI policy is required to resolve MXSO inconsistency. However, the DELETE_IN_SLAVE property has been set to “OFF” because the SD policy is unnecessary. 

##### SYNC Example 3

Synchronize the Master and Slave servers. 

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

The SI and SD policies are necessary to synchronize the Master and Slave servers. Therefore, the INSERT_TO_SLAVE and DELETE_IN_SLAVE properties have been set to “ON”. 

##### SYNC Example 4

Please refer to schema.sql in the $ALTIBASE_HOME/sample/APRE/schema directory.

Synchronize the EMPLOYEES table of the local server host1 with the EMPLOYEES table of the remote server host2 (delete 16 to 20 from the ENO column), and the DEPARTMENTS table of host1 with the DEPARTMENTS table of host2. 

First, set up replication between the local and remote servers. 

For the local server (IP: 192.168.1.11)

```
iSQL> CREATE REPLICATION rep1 WITH '127.0.0.1', 56342 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

For the remote server (IP: 127.0.0.1)

```
iSQL> CREATE REPLICATION rep1 WITH '192.168.1.11', 65432 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

If the current directory is /user/charlie/altibase_home/ altiComp:

```
$ vi sample.cfg
Master Server = "altibase://sys:manager@DSN=127.0.0.1;PORT_NO=20582;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=192.168.1.11;PORT_NO=20582;NLS_USE=US7ASCII"

OPERATION  = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF 
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[ EMPLOYEE S]
WHERE   = {ENO >= 1 and ENO <= 20}
TABLE   = EMPLOYEES 
SCHEMA  = SYS
[ DEPARTMENTS ]
TABLE   = DEPARTMENTS 
SCHEMA  = SYS

$ altiComp –f sample.cfg 
$ cat sample.log
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  1 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!
INFO[ MNG ] Tread #  1 start is  OK!

[DEPARTMENTS->DEPARTMENTS]
Fetch Rec In Master: 5
Fetch Rec In Slave : 5
MOSX = NO
MXSO = NO
MOSO = SU

--------------------------------------------
 Operation  Type      MASTER           SLAVE    
--------------------------------------------
 INSERT     Try            0               0 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
--------------------------------------------
 UPDATE     Try            0               0 
            Fail           0               0 
 OOP  TPS:       0.00
 SCAN TPS:   60240.96
     Time:       0.00 sec

[EMPLOYEES->EMPLOYEES]
Fetch Rec In Master: 20
Fetch Rec In Slave : 15
MOSX = NO
MXSO = NO
MOSO = SU

-------------------------------------------
 Operation  Type      MASTER           SLAVE    
-------------------------------------------
 INSERT     Try            0               5 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
-------------------------------------------
 UPDATE     Try            0               5 
            Fail           0               0 
 OOP  TPS:     576.04
 SCAN TPS:    2304.15
     Time:       0.01 sec
```



# 3. aku

## Introducing aku

### Overview

Altibase Kubernetes Utility (AKU) is a utility that helps you perform tasks such as synchronizing data in Altibase with the start and termination of Pods or resetting synchronization information when scaling in a Statefulset in Kubernetes. Aku supports data replication among Pods but does not support Altibase's data scale-out feature.

> StatefulSets are one of Kubernetes' workloads for supporting stateful applications like databases, and scaling means creating or terminating pods. A Pod is a resource in Kubernetes that contains containers, and Altibase server runs on these containers.

When scaling up or down on a StatefulSet, you can use aku to start or terminate pods that meet the following conditions. You should add the command in the appropriate location so that aku runs on the Altibase container.

#### When scaling up

You can use aku, if you want to create a Pods with the same data as Altibase server in an existing Pod.

The pod generated at first is called a "Master pod", and the pod generated by further scaling up is called a "Slave pod".

#### When scaling down

You can use aku, if you want to initialize the replication information of Altibase server when Pods are terminated.

### Component

> ⚠️ Aku should be running with a same version in all Pods, and the aku configuration files should have same values. Basically, aku and aku configuration file are included in the Altibase container image.
>
> Altibase Server and aku should be executed within the same container.

#### aku

Aku is located in $ALTIBASE_HOME/bin. To execute aku, you need to set $ALTIBASE_HOME and add $ALTIBASE_HOME/bin to $PATH.

#### aku.conf

aku.conf is the configuration file for aku. When executing aku, it reads aku.conf file to obtain the information needed for Altibase data synchronization. Altibase provides aku.conf.sample in $ALTIBASE_HOME/conf directory. Before running aku, generate the aku.conf file in the same directory using aku.conf.sample.

The aku.conf.sample file is as follows:

⚠️ Line after # symbol is commented out.

```bash
# aku.conf.sample

#***************************************************************** 
# Copyright 2022, Altibase Corporation or its subsidiaries.
# All rights reserved.
# Property File for Altibase AKU Utility
#*****************************************************************

#=================================================================
# Kubernetes setting Properties
#=================================================================
AKU_STS_NAME                  = altibase-sts    # statefulsets name
AKU_SVC_NAME                  = altibase-svc    # services name
AKU_SERVER_COUNT              = 4               # the number of Pods
#=================================================================
# Common Properties
#=================================================================
AKU_SYS_PASSWORD              = manager
AKU_PORT_NO                   = 20300
AKU_REPLICATION_PORT_NO       = 20301
AKU_QUERY_TIMEOUT             = 3600
AKU_QUERY_RETRY_COUNT         = 5
AKU_QUERY_RETRY_DELAY_MSEC    = 1000
#=================================================================
# aku start/end Properties
#=================================================================
AKU_ADDRESS_CHECK_COUNT       = 30
AKU_FLUSH_AT_START            = 1
AKU_FLUSH_TIMEOUT_AT_START    = 300
AKU_DELAY_START_COMPLETE_TIME = 0

AKU_FLUSH_AT_END              = 1
AKU_REPLICATION_RESET_AT_END  = 1
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
	REPLICATION_NAME_PREFIX = AKU_REP
	SYNC_PARALLEL_COUNT     = 1
	(
		SYS.T1, SYS.T2 PARTITION P1,
		SYS.T3
	)
)
```

For details of each properties, refer to [aku-properties](#aku-properties).

## Setup to run aku

### Prerequisite

To ensure stable usage of aku in a Kubernetes environment, the following conditions must be met:

* It should be used only in **StatefulSets** among Kubernetes workload.
* The **Pod management policy should be OrderedReady**. OrderedReady is the default policy for StatefulSets.
* The maximum number of scalable replicas is **up to 6.**
* **Altibase server and aku** should be executed within the same container.
* `aku -p start` command should be performed after Altibase server has started successfully.
* aku may not work normally when you execute `aku -p start` on multiple pods at the same time. To prevent this, it is required to configure the **Startup Probe** in Kubernetes.
* **Startup Probe** configuration is needed to verify if `aku -p start` command has been successfully executed. You can use the presence of the aku_start_completed file in the /tmp directory as an indicator for verification.
* Set **publishNotReadyAddress** to true.
* `aku -p end` command should be performed before stopping the Altibase server.
* A Pod should be terminated after `aku -p end` command completes successfully.
* Kubernetes's **terminationGracePeriodSeconds** should be set to a large value to allow aku to complete its tasks successfully before Pod is terminated.

### Altibase Environment Variable and Properties

* Altibase Environment 
  * $ALTIBASE_HOME
    * Sets the directory in which Altibase server was installed. This must be set to use aku.

* Altibase Properties
  * set ADMIN_MODE to 1.
  * set REMOTE_SYSDBA_ENABLE to 1.

### aku Properties

| Category                      | Property name                        | Default value | Description                                                  |
| ----------------------------- | :----------------------------------- | :-----------: | :----------------------------------------------------------- |
| Kubernetes Setting Properties | AKU_STS_NAME                         |               | The name of the StatefulSet defined in the Kubernetes object specification.<br/>It can be set up to 63 bytes. |
|                               | AKU_SVC_NAME                         |               | The service name that provides the Network Service defined in the Kubernetes object specification.<br/>It can be set up to 63 bytes. |
|                               | AKU_SERVER_COUNT                     |       4       | The maximum number of Altibase servers that can be synchronized using aku. It also refers to the number of Pods that can be scaled up in Kubernetes. </br>It can be set from 1 to 6. |
| Common Properties             | AKU_SYS_PASSWORD                     |               | Database SYS user password                                   |
|                               | AKU_PORT_NO                          |     20300     | Altibase Server Port number.<br />It can be set from 1024 to 65535. |
|                               | AKU_REPLICATION_PORT_NO              |     20301     | Altibase Replication Port number.<br />It can be set from 1024 to 65535. |
|                               | AKU_QUERY_TIMEOUT                    |     3600      | It refers to the Altibase server property QUERY_TIMEOUT. If the execution time of SQL statements executed by aku exceeds AKU_QUERY_TIMEOUT value, the statement is canceled. |
|                               | AKU_QUERY_RETRY_COUNT                |       5       | If a query executed on the Altibase server fails, it retries the specified number of times with this value.<br/> If this value is set to 0, it does not retry. |
|                               | AKU_QUERY_RETRY_DELAY_MSEC           |   1000 (ms)   | If a query executed on the Altibase server fails, it retries after waiting the specified time with this value. .<br/>If this value is set to 0, it does not wait and retries. |
| aku start/end Properties      | AKU_ADDRESS_CHECK_COUNT              |      30       | The number of attempts to connect to the local IP for checking if the DNS address of the currently created Pods is registered in the Kubernetes service (indicating whether communication between internal Pods is possible) when running `aku -p start`. |
|                               | AKU_FLUSH_AT_START                   |       1       | This property determines whether replication gaps should be removed or not, during the execution of the `aku -p start` command.<br/>If this value is set to 1, replication gaps are removed by using FLUSH command. </br>If this value is set to 0, replication gaps will not be removed. |
|                               | AKU_FLUSH_TIMEOUT_AT_START           |      300      | This property sets the *wait_time* for the FLUSH WAIT command. <br/>If this value is set to 0, it performs FLUSH.<br/>If this value is set to 1 or greater, it performs FLUSH WAIT  with the specified *wait_time*. </br>This setting is valid only if AKU_FLUSH_AT_START is set to 1. |
|                               | AKU_DELAY_START_COMPLETE_TIME        |    0(sec)     | This property specifies a waiting time (in seconds) during `aku -p start` process on the slave pod, specifically after the data synchronization is completed internally and before changing the Altibase property ADMIN_MODE to 0. |
|                               | AKU_FLUSH_AT_END                     |       1       | This property determines whether replication gaps should be removed or not, during the execution of the `aku -p end` command on the Slave Pod.<br/>If this value is set to 1, replication gaps are removed by using FLUSH ALL command.<br />If this value is set to 0, replication gaps will not be removed. |
|                               | AKU_REPLICATION_RESET_AT_END         |       1       | This property determines whether to perform a reset of the replication information or not by using RESET command.<br/>If this value is set to 1, the replication information is reset.<br/>If this value is set to 0, the replication information is not reset. |
| Replication Properties        | REPLICATIONS/REPLICATION_NAME_PREFIX |               | This property specifies the prefix of the replication object's name that is created by aku. The maximum value is 37 bytes. Please refer to the [Naming rule of the replication object in aku](#rep_name_rules). |
|                               | REPLICATIONS/SYNC_PARALLEL_COUNT     |       1       | The number of threads for sending/receiving during replication sync.<br/>It can be set from 1 to 100. |

<a name="rep_name_rules"> </a>

> [!NOTE]  
>
> **Naming rule of the replication object in aku**
>
> The naming rule of the replication object in aku is as follow:
>
> *REPLICATION_NAME_PREFIX*_\[*Pod Number*]\[*Pod Number*\]
>
> - REPLICATION_NAME_PREFIX: The strings specified as REPLICATIONS/REPLICATION_NAME_PREFIX property.
> - Pod number: The number located after *pod_name*_ in the names of pods created by the Kubernetes StatefulSet. Each pod has a unique sequential number assigned to it. In the names of Altibase replication objects, the numbers of the two pods that form the replication pair are included, and the smaller number appears first.
>
> Example)  The names of the replication objects created in each Pod when AKU_SERVER_COUNT = 4 and REPLICATION_NAME_PREFIX = "AKU_REP"
> | Pod Number   | Replication object name | Description                                                  |
> | :----------- | :---------------------- | :----------------------------------------------------------- |
> | *pod_name*-0 | AKU_REP_01              | Replication object name between *pod_name*-0 and *pod_name*-1 |
> |              | AKU_REP_02              | Replication object name between  *pod_name*-0 and *pod_name*-2 |
> |              | AKU_REP_03              | Replication object name between  *pod_name*-0 and *pod_name*-3 |
> | *pod_name*-1 | AKU_REP_01              | Replication object name between  *pod_name*-0 and *pod_name*-1 |
> |              | AKU_REP_12              | Replication object name between  *pod_name*-1 and *pod_name*-2 |
> |              | AKU_REP_13              | Replication object name between  *pod_name*-1 and *pod_name*-3 |
> | *pod_name*-2 | AKU_REP_02              | Replication object name between  *pod_name*-0 and *pod_name*-2 |
> |              | AKU_REP_12              | Replication object name between  *pod_name*-1 and *pod_name*-2 |
> |              | AKU_REP_23              | Replication object name between  *pod_name*-2 and *pod_name*-3 |
> | *pod_name*-3 | AKU_REP_03              | Replication object name between  *pod_name*-0 and *pod_name*-3 |
> |              | AKU_REP_13              | Replication object name between  *pod_name*-1 and *pod_name*-3 |
> |              | AKU_REP_23              | Replication object name between  *pod_name*-2 and *pod_name*-3 |
>
> ⚠️ Do not create/drop/modify the Altibase replication objects created by aku.

#### How to configure Altibase Replication Targets

Users can specify **tables** or **partitions** to be managed by the Altibase replication objects created by aku in the aku configuration file. To specify a replication target, add the target information in the format `[user name].[table name]` or `[user name].[table name] PARTITION [partition name]` to the replication property section. The maximum length for the user name, table name, and partition name is 128 bytes. 

Each replication target is separated by commas, and one or more replication target can be written on a single line.

Here's an example of configuring tables *T1* to *T9* to be split and managed across three replications. For table *T2*, only partition *P1* is set as the replication target.

```bash
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
    REPLICATION_NAME_PREFIX = AKU_REP1
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T1, SYS.T2 PARTITION P1,
        SYS.T3
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP2
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T4, SYS.T5, SYS.T6
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP3
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T7,
        SYS.T8,
        SYS.T9
    )
)
```

## Usage of aku

### Syntax

```
aku
[-h]
[--help]
[-v]
[--version]
[-i]
[--info]
[-p [start | stop | clean] ]
[--pod [start | stop | clean] ]
```

### Parameters

#### -h, --help

Displays the usage of aku

#### -v, --version

Displays the version information of aku. It is recommended to use the same version of aku as Altibase server.


#### -i, --info

Displays the following informations defined in aku.conf file.

- Altibase Server Information
  - Server ID
  - Host
  - User
  - Password
  - Port
  - Replication Port
  - Max Server Count : Maximum number of scalable Pods

- Replication Information
  - Replication object's name

- Replication Items
  - Replication Target table and User Name

#### -p, --pod {*pod_action*}

Specify the action to be performed with aku. *pod_action* options are "start", "end", and "clean".

### pod_action with aku

The followings introduce the action performed during execution of aku.

#### aku -p start

It creates Altibase replication objects and synchronizes data. You can use the command when starting Pods.

The following shows the detailed behavior of  `aku -p start` command.

>  ⚠️ `aku -p start` command should be performed after Altibase server has started successfully.

##### Creation of Master Pod (*pod_name*-0)

Since Altibase replication objects need to be created on all Pods, you should execute `aku -p start` command even if creating *pod_name*-0 in a StatefulSet.

The following explains the detailed behavior of `aku -p start` command while creating *pod_name*-0 in a StatefulSet.

![](media/Utilities/aku_p_start_master_pod.png)

① Read "aku.conf" file.

② Verify if the aku_started_completed file exists in /tmp directory. In the usual case, if the `aku -p start` command has not been executed previously, this file does not exist. If it exists, an error message is displayed and aku terminates the process because it is considered a duplicate execution of the `aku -p start` command.

③ Connect to all pods that are the target servers for replication. Typically, as this is an initially created pod, connection attempts to other pods fail. This is the expected behavior.

④ Create the Altibase replication objects. If a replication object with the same name already exists, the replication creation step will be skipped.

⑤ Start replication associated with all pods that successfully connect from *pod_name*-0, and start replication associated with *pod_name*-0 from other connected pods. Typically, as this is the initially created pod, there are no connected pods, so this action is not performed.

⑥ Create a file named "aku_start_completed" in /tmp directory.

##### **Scale up**

When scaling up in a StatefulSet, a Slave Pod is created. A Pod can be created and terminated repeatedly. The process of `aku -p start` execution is a little different when a Pod is first created and when it is restarted after being terminated.

> **When creating a Slave Pod for the first time, or restart (Default behavior, AKU_REPLICATION_RESET_AT_END =1)**

The following explains the detailed behavior of `aku -p start` command on *pod_name*-1 when the Slave Pod is created for the first time and is restarted normally.

![](media/Utilities/aku_p_start_slave_pod.png)

① Read "aku.conf" file.

② Verify if the aku_started_completed file exists in /tmp directory. In the usual case, if the `aku -p start` command has not been executed previously, this file does not exist. If it exists, an error message is displayed and aku terminates the process because it is considered a duplicate execution of the `aku -p start` command.

③ Connect to all pods that are the target servers for replication. Typically, only the connection with *pod_name*-0 succeeds, and the connection to *pod_name*-2 or *pod_name*-3 fails because those pods are not created yet. 

④ Create the Altibase replication objects. If *pod_name*-1 is restarted pod, the replication object with the same name may exist and this step will be skipped.

⑤ Execute 'TRUNCATE table' on the replication target table in *pod_name*-1. 

⑥ Request *pod_name*-0(Master Pod) to perform replication synchronization. 

⑦ Perform replication synchronization from *pod_name*-0 to *pod_name*-1 and start the replication.

⑧ Start replication associated with all pods that successfully connect from *pod_name*-1, and start replication associated with *pod_name*-1 from other connected pods. Typically, only AKU_REP_01, the replication related to *pod_name*-0, starts on *pod_name*-0 and *pod_name*-1. 

⑨ Set the Altibase server property ADMIN_MODE to 0 on *pod_name*-1 to allow to access for database user. 

⑩ Create a file named "aku_start_completed" in /tmp directory.

##### Restarting Slave Pods that Haven't Reset the Replication Information

>  **Case of restarting a Slave Pod that has not reset the replication information (Default behavior, AKU_FLUSH_AT_START = 1)**

The following explanation describes the basic behavior of aku when executing `aku -p start` on a Slave Pod that has not reset the replication information.

If a Pod is abnormally terminated or terminated with the AKU_REPLICATION_RESET_AT_END property sets to 0, the replication information is not initialized. If the replication information were not initialized, when restarting Pods the previous replication information would exist, so the below data synchronization actions from other nodes are skipped.

* Executes 'TRUNCATE table' on the replication target table.
* Requests for performing replication synchronization.

In this case, if the AKU_FLUSH_AT_START property sets to 1, data synchronization from itself to other nodes will be performed.

Note that if the replication information is not reset and remains, the XSN of the replication object has a value other than -1. Refer to the [Cautions 4](#cautions4).

![](media/Utilities/aku_p_start_aku_flush_at_start_1.png)

① Read "aku.conf" file.

② Verify if the aku_started_completed file exists in /tmp directory. In the usual case, if the `aku -p start` command has not been executed previously, this file does not exist. If it exists, an error message is displayed and aku terminates the process because it is considered a duplicate execution of the `aku -p start` command.

③ Connect to all pods that are the target servers for replication. Typically, only the connection with *pod_name*-0 succeeds.

④ Start replication associated with all pods that successfully connect from *pod_name*-1, and start replication associated with *pod_name*-1 from other connected pods. Typically, only AKU_REP_01, the replication related to *pod_name*-0, starts on *pod_name*-0 and *pod_name*-1.

⑤ Execute ALTER REPLICATION ~ FLUSH ALL command to the replications associated with all pods that successfully connect from *pod_name*-1. This command sends all unsynchronized data to other pods from *pod_name*-1.

⑥ On other connected pods, execute ALTER REPLICATION ~ FLUSH ALL command to replications related to *pod_name*-1 to send unsynchronized data. If AKU_FLUSH_TIMEOUT_AT_START is not set to 0, execute ALTER_REPLICATION ~ FLUSH WAIT *wait_time*. 

⑦ Set the Altibase server property ADMIN_MODE to 0 on *pod_name*-1 to allow to access for database user. 

⑧ Create a file named "aku_start_completed" in /tmp directory.

> **Case of restarting  a Slave Pod that hasn't reset the replication information (AKU_FLUSH_AT_START = 0)** 

The following explanation describes the behavior of aku when executing `aku -p start` on a Slave Pod that has not reset the replication information, with the property AKU_FLUSH_AT_START set to 0.

![](media/Utilities/aku_p_start_aku_flush_at_start_0.png)

① Read "aku.conf" file.

② Verify if the aku_started_completed file exists in /tmp directory. In the usual case, if the `aku -p start` command has not been executed previously, this file does not exist. If it exists, an error message is displayed and aku terminates the process because it is considered a duplicate execution of the `aku -p start` command.

③ Connect to all pods that are the target servers for replication. Typically, only the connection with *pod_name*-0 succeeds.

④ Start replication associated with all pods that successfully connect from *pod_name*-1, and start replication associated with *pod_name*-1 from other connected pods. Typically, only AKU_REP_01, the replication related to *pod_name*-0, starts on *pod_name*-0 and *pod_name*-1.

⑤ Set the Altibase server property ADMIN_MODE to 0 on *pod_name*-1 to allow to access for database user. 

⑥ Create a file named "aku_start_completed" in /tmp directory.

#### **aku -p end**

The command should be used when terminating Pods. It performs to stop Altibase replication and reset the replication information. 

![](media/Utilities/aku_p_end.png)

① Read "aku.conf" file.

② Connect to all Pods, which are connected with the current Pod. Since Pods are terminated sequentially, connection errors can occur when attempting to connect to already deleted Pods. This is the expected behavior.

③ Send the replication change logs to the replication objects of current Pod by executing 'ALTER REPLICATION *replication_name* FLUSH ALL'. If the AKU_FLUSH_TIMEOUT_AT_START property is set to 0, this step is skipped.

④ Request to perform "ALTER REPLICATION *replication_name* STOP" on all Pods related to current Pod.

⑤ Request to perform "ALTER REPLICATION *replication_name* RESET" on all Pods related to current Pod. If the AKU_REPLICATION_RESET_AT_END property is set to 0, this step is skipped.

   > ⚠️ `aku -p end` command should be performed before stopping the Altibase server.

⑥ Delete the "aku_start_completed" file in the /tmp directory.

#### **aku -p clean**

This command deletes all Altibase replication objects on the pods and the "aku_start_completed" file in the /tmp directory. Users can use this command when synchronization between pods is no longer needed.



## Cautions

### 1) aku.conf

* Every aku property which does not have its default value must be specified. If not, the "Property [*property_name*] should be specified by configuration." error occurs.
* Use # symbol to write a comment in the "aku.conf" file. Note that if there is no letter after # symbol, it causes the syntax error.

### 2) Storage corruption in Master Pod

aku does not recover data corruption due to storage corruption in Master Pod.

### 3) In case `aku -p start` command fails due to a master pod failure

Master pod failure refers to a scenario where the `aku -p start` command fails on the master pod under the following circumstances:

- One or more slave pods are running.
- In the master pod, some or all of the replication object information between the running slave pod(s) and the master pod is lost.

When a master pod failure occurs, the following steps should be taken to recover the master pod:

1. Select the slave pod that will serve as the basis for recovery. Execute the `aku -p end` command to terminate all slave pods except for the one chosen as the recovery basis.
2. Synchronize data from the slave pod to the master pod to ensure data consistency.
3. Start replication on the master pod.
4. Retry the command `aku -p start`.

Refer to the example below for detailed steps of master pod failure recovery.

**Example of Master Pod Failure Recovery**

Assuming a failure occurs in the master pod named *pod_name*-0 in the following environment:

- Configuration of the aku property in the master pod:
  - AKU_SERVER_COUNT = 4
  - REPLICATION_NAME_PREFIX = AKU_REP
- Configuration of Altibase server properties in the master pod:
  - ADMIN_MODE = 1
- Slave pod *pod_name*-1 is running.
- Replication targets tables are *T1*, *T2*, and *T3*.
- Information of replication object AKU_REP_01 (the replication between the master pod and slave pod *pod_name*-1) in the master pod is lost.

The master pod failure situation can be identified through the following log:

```bash
$ aku -p start
AKU started with START option.
[AKU][2024/04/19 19:21:31.012670][140276343642368] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
[AKU][2024/04/19 19:21:31.012991][140276343642368] [ERROR][akuRunStart:1030][-][-] The MASTER server is detected to have failed. Check and perform a manual recovery.
AKU failed to run.
```

At this point, when querying the XSN of the replication is lost in the master pod, the value is output as -1:

```sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_01                      -1
1 rows selected.
```

> [!note]
>
> XSN is the identification number of XLog, which delivers replication information between remote servers and local servers through sender and receiver threads. When initializing replication objects, this value becomes -1.
> The following recovery procedures can be sequentially performed to resolve the failure of the master pod:

1. Synchronize data from slave pods to the master pod to ensure data consistency.

   1. Delete records of replication target tables on the master pod.

      To prevent conflicts during data synchronization, TRUNCATE the replication target tables managed by the master pod. To execute the TRUNCATE command, the Altibase server property REPLICATION_DDL_ENABLE must be set to 1.

      ```sql
      # Change the REPLICATION_DDL_ENABLE property to 1.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1;
      Alter success.

      # TRUNCATE records of replication target tables.
      iSQL> TRUNCATE TABLE T1;
      Truncate success.
      iSQL> TRUNCATE TABLE T2;
      Truncate success.
      iSQL> TRUNCATE TABLE T3;
      Truncate success.

      # Restore the REPLICATION_DDL_ENABLE property to 0.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 0;
      Alter success.
      ```

   2. Perform data synchronization on the slave pod.

      Before synchronizing data, RESET the XSN value to initialize it. Once synchronization is complete, replication will automatically start.

      ```sql
      # Stop replication on the slave pod (can be omitted if replication has not started).
      iSQL> ALTER REPLICATION AKU_REP_01 STOP;
      Alter success.
      
      # Reset the replication object between the master pod and the slave pod.
      iSQL> ALTER REPLICATION AKU_REP_01 RESET;
      Alter success.
      
      # Perform replication SYNC to synchronize data consistency between the slave pod and the master pod.
      iSQL> ALTER REPLICATION AKU_REP_01 SYNC;
      Alter success.
      ```

2. Start replication on the master pod.

   Start replication on the master pod to complete the recovery of lost replication object information.

   ```sql
   iSQL> ALTER REPLICATION AKU_REP_01 START;
   Alter success.
   ```

3. Retry the `aku -p start` command.

   Once recovery is completed, the master pod will have the same data as the slave pod, and the XSN value of the replication object AKU_REP_01 will be updated. Now, when the `aku -p start` command is retried, it will be processed successfully.

   ```bash
   # Read aku.conf and create replication objects. 
   $ aku -p start
   # START option means that aku -p start is executed.
   AKU started with START option.
   [AKU][2024/04/19 19:21:01.011887][139922191153408] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
   
   # Remove replication gap between the master pod and the slave pod.
   [AKU][2024/04/19 19:21:09.057372][139922191153408] [INFO][akuRunStart:891][-][-] Flush replications.
   [AKU][2024/04/19 19:21:09.086363][139922191153408] [INFO][akuRunStart:896][-][-] Replication flush has ended.
   
   # After all procedures are successfully completed, aku is terminated. 
   AKU run successfully.
   ```

### 4) If the situation in which Pod was force terminated before `aku -p end` command completed or terminated with the property AKU_REPLICATION_RESET_AT_END set to 0, continues for a long time<a name="cautions4"></a>

If the situation in which a Pod was force-terminated before the `aku -p end` command completed or terminated with the property AKU_REPLICATION_RESET_AT_END set to 0 continues for a long time, there is a possibility of uninitialized replication information remaining in the terminated Pod as well as in other Pods. When this happens, the other Pods do not delete the online log files that are required for replication to the terminated Pod. If the online log file accumulates a lot, it can lead to disk space exhaustion and result in Altibase server not being able to operate normally. To prevent this situation, if you notice that there are long periods of time in which a Pod was terminated before the `aku -p end` command completed, you should stop replication and initialize the replication information. Refer to the commands below.

~~~sql
ALTER REPLICATION replication_name STOP;
ALTER REPLICATION replication_name RESET;
~~~
Suppose *pod_name*-1 failed to complete `aku -p end` and and terminated abnormally while *pod_name*-0 and *pod_name*-1 are both operational. Let's check the XSN of SYSTEM_.SYS_REPLICATIONS_ on *pod_name*-0. You can see that the XSN value of the replication object AKU_REP_01 is not -1. It means that the replication information is not initialized. AKU_REP_01 is the replication object between *pod_name*-0 and *pod_name*-1.
~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      859070110
3 rows selected.
~~~
Execute the statements for stopping and resetting replication of the object(AKU_REP_01) on *pod_name*-0.
~~~sql
iSQL> ALTER REPLICATION AKU_REP_01 STOP;
Alter sucess.
iSQL> ALTER REPLICATION AKU_REP_01 RESET;
Alter sucess.
~~~
And then, let's check the XSN of SYSTEM_.SYS_REPLICATIONS_ on *pod_name*-0. The XSN value of the replication object AKU_REP_01 was changed to -1.
~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      -1
3 rows selected.
~~~

## Examples

This section introduces various examples of aku usage.

The aku log in the example codes includes the following information:

```
[AKU][Date and time][Thread number] [Message type][Code information][Target pod name][Replication name] Message
```

### aku -i

This is the result of running `aku -i` and displays the information set in aku.conf. A server with Server ID 0 is that of the first Pod created by the StatefulSet.

~~~bash
$ aku -i
  #########################
 [ Server ]
  Server ID        : 0
  Host             : AKUHOST-0.altibase-svc
  User             : SYS
  Password         : manager
  Port             : 20300
  Replication Port : 20301
  Max Server Count : 4
 #########################
 [ Replications ]
 #### Serve[ID:0] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_03
 #### Serve[ID:1] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_13
 #### Serve[ID:2] Replication list ####
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_23
 #### Serve[ID:3] Replication list ####
  Replication Name : AKU_REP_03
  Replication Name : AKU_REP_13
  Replication Name : AKU_REP_23
 #########################
 [ Replication Items ]
  #### Replication [Prefix:AKU_REP] item list ####
  User Name        : SYS
  Table Name       : T1
 
  User Name        : SYS
  Table Name       : T2
  Partition Name   : P1
 
  User Name        : SYS
  Table Name       : T3
 #########################
~~~

### aku -p start on a Master Pod

This is an output of running `aku -p start` on a Master Pod (*pod_name*-0).

~~~bash
$ aku -p start
AKU started with START option.
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
AKU run successfully.
~~~

The Description of the output is as below.

~~~bash
# Read aku.conf and create replication objects. 
# START option means that aku -p start is executed.
AKU started with START option.

# MASTER Pod indicates the first pod. 
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.

# After all procedures are successfully completed, aku is terminated. 
AKU run successfully.
~~~

### aku -p start on the 4th Pod

This is an output of `aku -p start` command on the 4th Pod (*pod_name*-3).

~~~bash
AKU started with START option.
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.
AKU run successfully.
~~~

The Description of the output is as below.

~~~bash
# Read aku.conf and create replication objects. 
# START option means that aku -p start is executed.
 AKU started with START option.

# SLAVE Pod indicates other pods but the first pod. 
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.

# To prvent record conflict during SYNC processing, deletes all records on the target table.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.

# MASTER Server indicates the Altibase server of the Master Pod. The data has been synchronized from the server to the local pod.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.

# After all procedures are successfully completed, aku is terminated. 
AKU run successfully.
~~~

### aku -p end on the 4th Pod

This is an output of `aku -p end` command with the property AKU_REPLICATION_RESET_AT_END set to 1 on the 4th Pod (*pod_name*-3). You can see that replication FLUSH and RESET commands are executed.

~~~bash
$ aku -p end
AKU started with END option.
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.
AKU run successfully.
~~~

The Description of the output is as below.

```bash
# Read aku.conf, stop the replication and reset the replication. 
# END option means that aku -p end is executed.
AKU started with END option.

# SLAVE Pod indicates other pods but the first pod. 
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.

# FLUSH unsent changes to other pods.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.

# Reset all replication objects created on the aku of the local pod.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.

# After all procedures are successfully completed, aku is terminated. 
AKU run successfully.
```


# 4. Other Utilities

### altiAudit

#### About altiAudit

When auditing is performed on the Altibase server, the $ALTIBASE_HOME/trc directory is the default location for where the audit log file is created and audit logs are written; this location can be changed with the AUDIT_LOG_DIR property. Audit logs in the audit log file are written in binary format and are therefore, illegible by the user. The altiAudit utility converts and prints the audit log file in text format to enable the user to analyze them.

```
altiAudit [-s] {audit_log_file_name}
```



#### Syntax

![](media/Utilities/altiaudit.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05734" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="2463" image_path_raw="media/Utilities/altiaudit.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiaudit ::=
    altiAudit [ -s ] audit_log_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-05734" -->


#### Descriptions

This converts and outputs audit logs written by the server in text format.

With the -s option, audit logs can also be printed in CSV format.

#### Examples

The following command prints audit logs in plain text format.

```
$ altiAudit $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

The results are printed as below:

```
[2015/03/05 14:59:29]
Session Info 
  User Name        = SYS
  Session ID       = 1                   
  Client IP        = 127.0.0.1
  Client Type      = CLI-64LE
  Client App Info  = isql
  Action           = INSERT
  Auto Commit      = 1                        (0:non-autocommit 1:autocommit)
 
Query Info 
  Statement ID      = 65540               
  Transaction ID    = 150657              
  Execute result    = 4                       (0:failure 1:rebuild 2:retry 3:queue empty 4:success)
  Fetch result      = 2                       (0:failure 1:success 2:no result set)
  Success count     = 1                   
  Failure count     = 0                   
  Return code       = 0x02000
  Processed row     = 1                   
  Used memory       = 0                       bytes
  XA flag           = 0                       (0:non-XA 1:XA)
 
Query Elapsed Time 
  Total time        = 0                   
  Soft prepare time = 0                   
  Parse time        = 0                   
  Validation time   = 0                   
  Optimization time = 0                   
  Execution time    = 0                   
  Fetch time        = 0                   
 
SQL 
--------------------------------------------------------------------------------
insert into t1 values ('aaaa', 1)
-------------------------------------------------------------------------------- 

```

The following command prints audit logs in CSV format:

```
$ altiAudit -s $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

The results are printed as below:

```
1425535169,SYS,1,127.0.0.1,CLI-64LE,isql,INSERT,1,65540,150657,4,2,1,0,1,0,0,0,0,0,0,0,0,0,"insert
into t1 values ('aaaa', 1)"
```



#### Output

In the output, each field has the following meaning:

| Field Nam              | Type    | Description                                                  |
| ---------------------- | ------- | ------------------------------------------------------------ |
| **Session Info**       |         |                                                              |
| User Name              | String  | The name of the user connected to the session                |
| Session ID             | INTEGER | The session ID                                               |
| Client IP              | String  | The client IP address                                        |
| Client Type            | String  | The connected client type                                    |
| Client App Info        | String  | The application information                                  |
| Action                 | String  | The executed statement type                                  |
| Auto Commit            | INTEGER | 0: Non-auto commit mode 1: auto commit mode                  |
| **Query Info**         |         |                                                              |
| Statement ID           | INTEGER | The statement ID                                             |
| Transaction ID         | INTEGER | The transaction ID                                           |
| Execute result         | INTEGER | The execution result: 0: failure 1: rebuild 2: retry 3: query empty 4: success |
| Fetch result           | INTEGER | The fetch result: 0: failure 1: success 2: no result set     |
| Success count          | INTEGER | The number of times the statements conforming to the auditing condition succeeds. For the BY SESSION condition: the accumulated number of times the statements conforming to the auditing condition succeeds. For the BY ACCESS condition: if the statement conforming to the auditing condition succeeds, 1 is output. |
| Failure count          | INTEGER | The number of times the statement conforming to the auditing condition fails. For the BY SESSION condition: the accumulated number of times the statements conforming to the auditing condition fails. For the BY ACCESS condition: if the statement conforming to the auditing condition fails, 1 is output. |
| Return code            | INTEGER | The result code of the executed statement conforming to the auditing condition. The execution result is only output for the BY ACCESS condition. |
| Processed row          | INTEGER | The number of processed records                              |
| Used memory            | INTEGER | The memory usage (to be extended in the future)              |
| XA flag                | INTEGER | 0: Non-XA 1: XA                                              |
| **Query Elapsed Time** |         |                                                              |
| Total time             | BIGINT  | The total time consumed in query execution                   |
| Soft prepare time      | BIGINT  | The time consumed in preparing                               |
| Parse time             | BIGINT  | The time consumed in parsing                                 |
| Validation time        | BIGINT  | The time consumed in validation                              |
| Optimization time      | BIGINT  | The time consumed in optimization                            |
| Execution time         | BIGINT  | The time consumed in execution                               |
| Fetch time             | BIGINT  | The time consumed in fetching                                |
| **SQL**                |         |                                                              |
|                        | INTEGER | The executed SQL statement                                   |

### altibase

#### About altibase

altibase is the executable server file that controls all Altibase services.

```
altibase {-v|n}
```



#### Syntax

![](media/Utilities/altibase.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05735" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="2585" image_path_raw="media/Utilities/altibase.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altibase ::=
    altibase { -v | -n }
```
<!-- IMG_RECOVERY_END ref_id="img-05735" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-v       | Displays the version of Altibase that is currently installed |
| \-n       | Executes Altibase in the foreground                          |

#### Description 

altibase is the executable server file that controls all Altibase services.

To start up or shut down Altibase normally in a production environment, do not use this command. Instead, log into iSQL in SYSDBA mode and use the startup or shutdown command, or use the server command. The server command is actually a shell comprising several commands related to starting up and shutting down the server. For more information about the server utility, please refer to server in this document. 

For a complete explanation of how to start up and shut down Altibase, please refer to the *iSQL User's Manual* or the *Altibase Getting Started Manual*.

When the Altibase server process is started using iSQL, it runs in the background. In contrast, when the altibase command is executed at the shell prompt with the -n option, Altibase is executed in the foreground. This is used only for Altibase debugging purposes, and is not intended or recommended for live deployment, that is, for use in a production environment. 

Running the altibase executable file with the -v option does not start up the server, but merely outputs information about the currently installed version of Altibase.

#### References

Please refer to the *Altibase Getting Started*, the *Altibase Administrator’s Manual*, and the *Altibase iSQL User’s Manual* 

### altiMon

#### About altiMon

altimon.sh monitors the status of the Altibase server process and the related host system.

altimon.sh {start \| stop}

#### Syntax

![](media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05736" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="2620" image_path_raw="media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png" image_class="C" format="bnf" verified="True" -->
```bnf
altimon ::=
    altimon.sh { start | stop }
```
<!-- IMG_RECOVERY_END ref_id="img-05736" -->


#### Parameters

| Parameter | Description        |
| --------- | ------------------ |
| start     | Run altimon        |
| stop      | Terminates altimon |

#### Description

altiMon consistently monitors Altibase server and the related host system in order to record the collected data into the log files.

altiMon mainly monitors information on operating system and database, and refer to the Setting altiMon Configuration for in-depth information. 

##### start

1. Set the JAVE_HOME environment variables.

2. Run the command. 

- Unix Platforms

```
$ altimon.sh start
```


3. If operation fails, verify the file $ALTIBASE_HOME/altiMon/logs/altimon.log.

##### stop

- Unix Platforms

```
$ altimon.sh stop
```

#### Operating System

altiMon uses PICL library written in C language in order to collect information on operating system. The PICL library is available on the operation systems describe in the chart below. 

| OS                           | CPU                     | PICL Library    |
| :--------------------------- | :---------------------- | :-------------- |
| **AIX**                      |                         |                 |
| AIX 5.3   AIX 6.1   AIX 7.1  | PowerPC                 | aix-ppc64-5.so  |
| **HP-UX**                    |                         |                 |
| HP-UX  11.31                 | Itanium (IA-64)         | hpux-ia64-11.sl |
| **Linux**                    |                         |                 |
| Red Hat Enterprise Linux 6.0 | x86-64                  | linux-x64.so    |
| Red Hat Enterprise Linux 6.5 | PowerPC                 | linux-ppc64.so  |
| Red Hat Enterprise Linux 7.2 | PowerPC (Little Endian) | linux-ppc64.so  |

it can also be used after checking whether the PICL for the lower version works on the OS version that is not supported.

  ```
  $ cd $ALTIBASE_HOME/altiMon # java -Dpicl="<picl_lib_file>" -jar lib/com.altibase.picl.jar
  ```

Example)

This procedures verifies that the "aix-ppc64-5.so" PICL library is available on the unsupported version of the AIX operating system and runs altimon

1. Verify that PICL for lower versions works.

```
$ cd $ALTIBASE_HOME/altiMon 
$ java -Dpicl="aix-ppc64-5.so" -jar lib/com.altibase.picl.jar
```

2. After the general operation is verified, open the $ALTIBASE_HOME/bin/altimon.sh file and set the PICL file in the PICL_LIB variable.

```
PICL_LIB=-Dpicl="aix-ppc64-5.so"
```

3. Run altimon

```
$ altimon.sh start
```

##### Notes

altiMon requires Java 8 version or later to operate.

The user should select the Java version equivalent to the number of bits of the PICL C library. For example, if the PICL C library is linux x64, 64bit Java should be used.

#### Setting altiMon Configuration 

It is required that the following files located in the $ALTIBASE_HOME/altiMon/conf directory should be configured in order to properly use altiMon

-   [config.xml](#config.xml)

-   [Metrics.xml](#metrics.xml)

-   [GroupMetrics.xml](#groupmetrics.xml)

##### config.xml

This file configures Altibase access and altiMon control information.

| Tag Name                                                | Status    | Description                                                  |
| ------------------------------------------------------- | --------- | ------------------------------------------------------------ |
| \<Altimon Name='String' monitorOsMetric="true\|false"\> | Mandatory | The monitorOsMetric attribute specifies whether or not to measure the OsMetrics. Default Value: TRUE It should be set to false when there is no PICL C library that can be compatible to the user environment. |
| \<DateFormat\>                                          | Optional  | tag. Date and time format when recording logs. Default Value : yyyy-MM-dd HH:mm:ss Refer to the Java Document for the date format which is available to select. |
| \<Interval\>                                            | Optional  | Data collection cycle. Default Value : 60(sec) The specified values are applied unless intervals are specified in the  settings, or .However, the  is not affected. |
| <CpuSamplingInterval\>                                  | Optional  | This is the execution cycle of the thread that measures CPU utilization (%). The default value is 3, and the unit is second.<br/>Since Altibase 7.1.0.8.4, OS CPU utilization measurement thread and ALTIBASE HDB CPU utilization measurement thread have been added to measure CPU utilization. Each thread measures the CPU usage rate at the CpuSamplingInterval cycle, and these values are referred to in the monitoring element. Since the OS CPU utilization measurement thread and the ALTIBASE HDB CPU utilization measurement thread operate as separate threads, a time difference may occur between the two measurement values when the CPU is overloaded. |
| \<LogDir\>                                              | Optional  | tag should be specified when using an extra disk;otherwise, the following directory would be set to default as following: $ALTIBASE_HOME/altiMon/logs |
| \<MaintenancePeriod\>                                   | Optional  | Log file maintenance period Default Value : 3 days           |
| \<Target Name='String'\>                                | Mandatory | This tag indicates the monitoring target database. Name: name |
| \<HomeDirectory\>                                       | Optional  | tag sets ALTIBASE_Home directory as an absolute path. If it is not specified, the ALTIBASE_HOME environment variable will be used. |
| \<DBConnectionWatchdogCycle\>                           | Optional  | This tag indicates the execution cycle of DB connection watchdog.DB connection watchdog enables monitoring target database to continue monitoring by periodically attempting to access to the database even after shutting down. Default Value : 60(sec) |
| \<User\>                                                | Optional  | Connected user. If this file is not specified, altiMon will connect via SYS user. |
| \<Password Encrypted="Yes \| No"\>                      | Mandatory | When the encrypted attributes is "No", and even if the user registered the password, altiMon alters the encrypted attributes to "YES", and thus, the password is also encrypted. |
| \<Port\>                                                | Mandatory | Port number                                                  |
| \<NLS\>                                                 | Mandatory | NLS_USE                                                      |
| \<DbName\>                                              | Optional  | Database Name <br/>Default Value : mydb                      |
| \<IPv6\>                                                | Optional  | IPv6 status of use <br/>Default Value: false                 |

##### Metrics.xml

The following categories provide information on the Metrics.xml file which can configure the predefined OS Metrics, and SQL Metrics, as well as user-defined OS Metrics(Command Metric).

| Tag Name                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| \<OSMetric Name='PROC_CPU_USER' Activate='true' Interval='30' Logging='true'\> | This tag configures the predefined OS Metric and uses predefined OS Metrics as in the following. TOTAL_CPU TOTAL_CPU_USER TOTAL_CPU_KERNEL PROC_CPU PROC_CPU_USER PROC_CPU_KERNEL TOTAL_MEM_FREE TOTAL_MEM_FREE_PERCENTAGE PROC_MEM_USED (=> RSS) PROC_MEM_USED_PERCENTAGE SWAP_FREE SWAP_FREE_PERCENTAGE DISK_FREE DISK_FREE_PERCENTAGE DISK_FREE or DISK_FREE_PERCENTAGE must have the  tag as belows, and the 'Disk Name' should be uniquely named. <br /><OSMetric Name='DISK_FREE' Activate='true'\> <br /><Disk Name='disk1'\>/home\</Disk\> \</OSMetric\> \<OSMetric Name='DISK_FREE' Activate='true'\> \<Disk Name='disk2'\>/home2\</Disk\> \</OSMetric\> |
| \<SQLMetric Name='MEM_DATABASE_USAGE' Activate='true' Interval='60' Logging='true'\> | This configures the SQL Metric, and it is required to define a Name. <br />Name: Metric name (Required) <br />Activate: Status of operation(Data Collection)<br />The specifiable value is either true or false, and default value is true.<br/>Interval: If the cycle of data collection is not specified, the specified values in the config.xml file is used.<br />Logging: It sets whether or not to log the result of data collection into the log file. The default value is set to true. Set to false if you want to record only the alert info. |
| \<CommandMetric Name='MEM_VSZ' Activate='true' Interval='60' Logging='true'\> | This tag configures the user-defined OS Metric. The altiMon executes a command or script specified in the tag, and the value output as stdout is used as measured value. |
| \<Query\>                                                    | This  tag configures a query, and it is necessary in case of SQL Metric. |
| \<Command\>                                                  | The tag configures command or script file, and it is required for CommandMetric. The script file can be set up by an absolute or relative path. The relative path is based up on the following directory: $ALTIBASE_HOME/altiMon |
| \<Alert Activate='true' ComparisonColumn='ALLOC_MEM_MB' ComparisonType='gt'\> | Warning setup optional. <br />The measured values which are compared with the threshold values should be numbers.<br />Activate: Operation status, optional. (Default value: True)<br />Comparison: Column the target column which will be compared with threshold value. (Optional)<br />ComparisonType: comparison operator. (Required) <br />-eq: is equal to the threshold value <br />-ne: is not equal to the threshold value <br />-gt: is greater than the threshold value <br />-ge: is greater than or equal to the threshold value <br />-lt: is less than the threshold value <br />-le: is less than or equal to the threshold value |
| \<WarningThreshold Value='500'\> or \<CriticalThreshold Value='800'\> | This tag can specify the threshold values.(Possible to set 'Critical’ and 'Warning' level) <br/>In case of , it is required.<br />Value: threshold values |
| \<ActionScript\>db_usage.sh\</ActionScript\>                 | This tag configures the script file name to be executed when the threshold value is out of the specified range. <br />The script file should be existing in the following directory : $ALTIBASE_HOME/altiMon/action_scripts |

##### GroupMetrics.xml

The GroupMetrics.xml is a file defining the Group Metrics, which is comprised of OS Metric, Command Metric, and SQL Metric. The GroupMetric can be defined by using metrics specified in Metrics.xml. 

Unlike the common Metric measured values are stored to the *.log file, the data collected by group metric are stored to CSV files. 

| Tag Name                                    | Description                                                  |
| ------------------------------------------- | ------------------------------------------------------------ |
| \<GroupMetric Name='group1' Interval='30'\> | Configure Group Metric.<br />Name: metric name (Required) <br />Activate: Data collecttion status (Optional). Available value is either true or false. The default value is true.<br /> Interval: Data collection cycle (Necessary) |
| \<Target MetricName='PROC_CPU_USER'/\>      | This specifies the base metric which will be included in the group metric. <br />MetricName: The name of OSMetric, Command Metric or SQLMetric whick is defined in Metrics.xml.<br />A SQL Metric should necessarily retrieve one row of a SELECT query. When specifying DISK_FREE, or DISK_FREE_PERCENTAGE, a character string which is linked with 'Metric Name' and 'Disk Name' with ‘.’ should be specified as a MetricName. <br />\<Target MetricName='DISK_FREE.disk1'/\> |
| \<Column Name='LOG_GAP' /\>                 | In the case of the SQL Metric, the columns which will be included in the group metric are specified by this tag. <br />If this tag is not specified, every select target will be included in the Group Metric.<br />Name: The target column used in a SELECT query. If you specify an alias, the alias should be used. |

##### Others

-   action_scripts directory  
     In order to normally execute a script file specifying the tag, the script file should be located in the directory $ALTIBASE_HOME/altiMon/action_scripts.  
    For example, 'db_usage.sh' file in db_usage.sh should be located under the action_scripts directory in order for a script file to normally executes.

#### Example

The followings are examples of the altiMon configuration files.

##### config.xml

```
<?xml version="1.0" encoding="UTF-8"?>
 
<config>
    <Altimon Name='rnd1'>
        <!-- <LogDir>/home/bethy/arugs/logs</LogDir> -->
        <DateFormat>yyyy-MM-dd HH:mm:ss</DateFormat>
        <MaintenancePeriod>3</MaintenancePeriod>
        <Interval>60</Interval>
    </Altimon>
    <Target Name='Altibase1'>
        <HomeDirectory>/home/bethy/work/altibase_trunk/altibase_home</HomeDirectory>
        <User>sys</User>
        <Password Encrypted="NO">manager</Password>
        <Port>20020</Port>
        <DbName>mydb</DbName>
        <NLS>KSC5601</NLS>
        <IPv6>FALSE</IPv6>
    </Target>
 
</config>
```



##### OSMetrics.xml

```
<?xml version="1.0" encoding="UTF-8"?>
 
<Metrics>
  <OSMetric Name='TOTAL_CPU' Activate='true' Description='TOTAL_CPU'>
  <OSMetric Name='PROC_CPU' Activate='true' Interval='60'>
    <Alert Activate='true' ComparisonType='gt'>
        <WarningThreshold Value='80'>
            <ActionScript>cpu_act.sh</ActionScript>
        </WarningThreshold>
    </Alert>
  </OSMetric>
 
  <SQLMetric Name='MEM_DATABASE_USAGE' Activate='true' Interval='30'>
    <Query>select
            trunc(mem_alloc_page_count*32/1024, 2) as alloc_mem_mb,
            trunc(mem_free_page_count*32/1024, 2) as free_mem_mb
            from v$database</Query>
    <Alert Activate='true' ComparisonColumn='ALLOC_MEM_MB' ComparisonType='GT'>
        <CriticalThreshold Value='8000' >
            <ActionScript>db_usage.sh</ActionScript>
        </CriticalThreshold>
    </Alert>
  </SQLMetric>
 
  <CommandMetric Name='MEM_VSZ'>
    <Command>scriptsDir/vsz.sh</Command>
    <Alert Activate='true' ComparisonType='gt'>
        <WarningThreshold Value='100000000'> <!-- in kB -->
            <ActionScript>mem_act.sh</ActionScript>
        </WarningThreshold>
    </Alert>  
</CommandMetric>
</Metrics>

```



##### GroupMetrics.xml

```
<GroupMetrics>
    <GroupMetric Name='group1' Interval='30'>
        <Target MetricName='TOTAL_CPU'/>
        <Target MetricName='PROC_CPU'/>
        <Target MetricName='LOGFILE_COUNT'>
            <Column Name='LOG_GAP' />
        </Target>
    </GroupMetric>
    <GroupMetric Name='group2' Interval='60'>
        <Target MetricName='PROC_MEM_USED_PERCENTAGE'/>
        <Target MetricName='MEM_VSZ'/>
        <Target MetricName='LOGFILE_COUNT'/>
    </GroupMetric>
</GroupMetrics>

```



#### Output Items

The items are outptted with the folllowing format in the directories below. 

##### logs directory

-   altimon.log  
    This is the file recording all sorts of logs(info, warn, error) by altiMon daemon.

-   alert.log  
    This file records the data relevant to the  setting.

-   OsMetrics.log  
    This file records all the collected data by all the OS Metric.

-   [SQLMetric_Name].log  
    The collected data by SQL Metric are recorded into a different log file for each Metric.

-   [GroupMetric_Name].csv  
    The collected data by Group Metric are recorded into a different csv file for each Metric.

-   report.html  
    This file reports user configuration setting with a HTML format .

##### logs/archive directory

All the files in the logs directory except altimon.log, and *.csv are backed up into a archive/YYYY-MM-DD directory every day. 

Among above directories, the directories with expired maintenance period specified in are removed at 1:50am every day. 

##### logs/csv_backup directory

For Group Metrics, collected data(metric values) are constantly added to the same csv file unless the settings are modified. 

However, in case of the changed metric settings meaning that when the target objects in the group metric are changed, the existing csv file is backed up into the logs/csv_backup directory, and data are recorded in a new file with the identical name.

### altierr

#### About altierr

altierr searches for and displays detailed descriptions of Altibase server errors. Errors can be looked up using the error number, or a character string can be used as a search term and sought for within the error messages.

```
altierr {-w keyword pattern | [-n] error number}
```



#### Syntax

![](media/Utilities/altierr.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05737" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="2917" image_path_raw="media/Utilities/altierr.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altierr ::=
    altierr { -w keyword_pattern | [ -n ] error_number }
```
<!-- IMG_RECOVERY_END ref_id="img-05737" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-w       | Searches for error messages containing the specified search term. All error messages that contain the search term will be displayed. |
| \-n       | Searches for an error corresponding to the specified error code number. The error code number can be a hexadecimal number, a positive integer, or a negative integer. <br />Only the record that matches the error code number, if any, will be displayed. <br />When searching for an error using the error code number, the numeric parameter indicator (-n) can be safely omitted. |

#### Description

altierr searches the Altibase errors for strings that contain the specified error message or that match the specified error code number and displays the detailed description of any error that is found. The detailed description of the error includes the error code number, the error code string, the description, the cause of the error, and the action that the user must take in order  to remedy the error. When an error occurs, the Altibase server writes the corresponding error code to altibase_boot.log in the following format:

ERR-error code 

altierr can be used to search for the detailed description using either a hexadecimal or decimal error code, as shown below:

```
For ‘ERR-00015’
$ altierr 0x00015
$ altierr –w 00015
$ altierr 21
```

When SQL-related errors occur in applications written using the C/C++ precompiler or applications that use ODBC, the error code will be set in the SQLCODE variable, or will be returned by the ODBC function. In these cases, the error code will be a negative integer. To search for the description of the corresponding error, use altierr as follows:

```
For -266286
$ altierr -266286
$ altierr 266286
$ altierr 0x4102E
```

altierr can be used to search the text of error messages for a search term. In this case, multiple records may be returned. Use a character string as a search term for searching the text of error message descriptions as follows:

```
$ altierr –w connect
$ altierr –w “does not”
```



#### References

Please refer to the *Altibase Error Message Reference.*

### altipasswd

#### About altipasswd

altipasswd modifies the $ALTIBASE_HOME/conf/syspassword file. When database is not in service status, administrative job is executed by running iSQL with SYSDBA option. In this case, the password of SYS user is verified by reading the syspasswd file. Therefore, when SYS user's password is modified by using ALTER USER SQL statement, password of syspassword file should be equally modified by using altipasswd. If the password of the SYS user and syspassword are not identical, error will occur when SYSDBA tasks, such as starting up and shutting down the database, are performed.

```
altipasswd
```



#### Syntax

![](media/Utilities/altipasswd.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05738" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="2977" image_path_raw="media/Utilities/altipasswd.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altipasswd ::=
    altipasswd
```
<!-- IMG_RECOVERY_END ref_id="img-05738" -->


#### Description

Changes the password of the SYS user.

#### Example

To change the password of the SYS user from “manager” to “manager1234”, type the following at a shell prompt:

```
$ altipasswd
Previous Password : manager
New Password : manager1234
Retype New Password : manager1234
```



### altiProfile

#### About altiProfile

Altibase can write information about tasks that are executed on the server and server status to files for analysis. A file that contains information about server status is called a profile. altiProfile can convert a profile to character format or print STATEMENT statistics. The user can analyze the system status with this information.

```
altiProfile [-stat query|session] {profile_name [profile_name2 [profile_name3] ...}
```



#### Syntax

![](media/Utilities/altiprofile.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05739" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3010" image_path_raw="media/Utilities/altiprofile.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiprofile ::=
    altiProfile
        [ -h
        | -stat { query | session } ]
        profile_name { profile_name }
```
<!-- IMG_RECOVERY_END ref_id="img-05739" -->


#### Parameters

| Parameter            | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| \-h                  | Displays help.                                               |
| \-stat query/session | Builds statistics from profile STATEMENTs and prints them in text and CSV formats.<br />For more detailed information about statistics, please refer to How to use altiProfile. |

#### Description

altiProfile converts a server profile to character format or prints STATEMENT statistics.

#### Example

```
iSQL> ALTER SYSTEM SET QUERY_PROF_FLAG = 1;
Alter success.
iSQL> ALTER SYSTEM SET TIMED_STATISTICS = 1;
Alter success.
iSQL> 	 --(Execute an SQL query here.)

$ cd $ALTIBASE_HOME/trc
$ altiProfile alti-1286503704-0.prof

$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof
```



#### How to use altiProfile

The QUERY_PROF_FLAG property must be set to a value larger than 0 to write information about server status and tasks. The following information is logged for the QUERY_PROF_FLAG property: 

| Value | Name           | Description                                                  |
| ----- | -------------- | ------------------------------------------------------------ |
| 0     |                | No logging.                                                  |
| 1     | [STATEMENT]    | Whenever a SQL statement is executed, the executed SQL statement, execution time, execution information, and information about index and disk access are output. The value for the TIMED_STATISTICS property must be set to 1 to print the proper execution time. For further information about the TIMED_STATISTICS property, please refer to the *General Reference.* |
| 2     | [BIND]         | Whenever a SQL statement is executed, BIND parameter(s) is/are output. |
| 4     | [PLAN]         | Whenever a SQL statement is executed, the execution plan is output |
| 8     | [SESSION STAT] | Every 3 seconds, session information (i.e. the data in V$SESSTAT) is output. |
| 16    | [SYSTEM STAT]  | Every 3 seconds, system information (i.e. the data in V$SYSSTAT) is output. |
| 32    | [MEMORY STAT]  | Every 3 seconds, information about memory (i.e. the data in V$MEMSTAT) is output. |

The above values can be combined to log the desired information. For example, if the property is set to 1+4+32=37, then whenever a SQL statement is executed, the execution information and execution plan for the SQL statement are output, and additionally, information about memory is output every 3 seconds. 

If the QUERY_PROF_FLAG property is set to a nonzero value, the server will create and write to a profile file having a name that follows this convention:

##### Outputing Statistics

altiProfile can use the -stat option to build and out statistical information about executed SQL statements. This information helps you find the SQL statement to tune.

The -stat query option builds statistics on the following: 

-   COUNT: The number of times the query was executed.

-   AVG: The amount of time (in microseconds) the query took to execute, on average.

-   TOTAL: The amount of time (in microseconds) the query took to execute, in sum.

-   MIN: The minimum amount of time (in microseconds) the query took to execute.

-   MAX: The maximum amount of time (in microseconds) the query took to execute.

-   SUCCESS: The number of times the query succeeded.

-   FAIL: The number of times the query failed.

-   QUERY: The SQL statement that was executed.

When the -stat session option is used, SESSION ID is added to the statistics built using the query option.

The following is an example of altiProfile building statistics on SQL statements by analyzing profiles in the $ALTIBASE_HOME/trc directory.

```
$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof

### Processing [/altibase_home/trc/alti-1423543095-0.prof]...
100% [====================]

### Writing CSV File [alti-prof-stat-1423543711.csv]...

### Writing TEXT File [alti-prof-stat-1423543711.txt]...

### Successfully done.

```

In the example above, statistics are saved in text and CSV formats. The names of the files are automatically generated as 'alti-prof-stat-#time.csv' and 'alti-prof-stat-#time.txt'. 

The following is an example of a text file. Statistics are displayed in order under the column TOTAL. 

```
$cat alti-prof-stat-1423543711.txt
COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     5     0.003730     0.018650     0.003035     0.004640     5     0    DROP VIEW REVENUE
     5     0.003523     0.017616     0.003004     0.003745     5     0    CREATE VIEW REVENUE (
...

```

The following is an example of a CSV file. The content displayed is the same as that of a text file, except that it is in CSV format. CSV format allows the user to move data between programs.

```
$ cat alti-prof-stat-1423543711.csv
COUNT,AVG,TOTAL,MIN,MAX,SUCCES,FAIL,QUERY
5,  0.003730,  0.018650,  0.003035,  0.004640,5,0,"DROP VIEW REVENUE"
5,  0.003523,  0.017616,  0.003004,  0.003745,5,0,"CREATE VIEW REVENUE (
...

```



#### Precaution

When the profiling function is activated, execution information is recorded for all SQL statements executed in the server, and the state of the server, such as session and system information, is recorded every 3 seconds. Therefore, the size of the profile file will increase rapidly, which could cause the disk to become full, consequently causing problems. So, care should be taken when considering whether to perform profiling. 

#### Output

Files are output in the follwing format.

```
[BIND]
..
[PLAN]
..
[STATEMENT]
..
[SESSION STAT]
..
[SYSTEM STAT]
..
[MEMORY STAT]
..

```

Each item is output as follows. 

##### [BIND]

Outputs information on variables that are bound to the SQL statement.

##### [PLAN]

Outputs the execution plan for the executed SQL statement. For more information on execution plans, please refer to the *Performance Tuning Guide.*

##### [STATEMENT]

The following table shows the statement-related information that is logged.

| Field Name                             | Value        | Description                                                  |
| -------------------------------------- | ------------ | ------------------------------------------------------------ |
| SQL                                    | String       | The SQL statement that was executed                          |
| **User Info**                          |              |                                                              |
| User ID                                | INTEGER      | The user identifier                                          |
| Client PID                             | BIGINT       | The identifier of the client process                         |
| Client Type                            | VARCHAR(40)  | The type of the connected client                             |
| Client AppInfo                         | VARCHAR(128) | A string containing information about the client applicaiton |
| **Elapsed Time for this SQL statemen** |              |                                                              |
| Total                                  | BIGINT       | The total query execution time                               |
| Parse                                  | BIGINT       | The time taken to parse the query                            |
| Valid                                  | BIGINT       | The time taken to validate the query                         |
| Optim                                  | BIGINT       | The time taken to optimize the query                         |
| Execu                                  | BIGINT       | The time taken to execute the query                          |
| Fetch                                  | BIGINT       | The time taken to fetch query results                        |
| **Query Execute Info**                 |              |                                                              |
| EXECUTE Result                         | INTEGER      | 0: failure 1: rebuild 2: retry 3: queue empty 4: success     |
| Optimizer Mode                         | BIGINT       | The optimization mode                                        |
| Cost Mode                              | BIGINT       | The optimization cost                                        |
| Used Memory                            | BIGINT       | Reserved for future use                                      |
| SUCCESS SUM                            | BIGINT       | The total number of successful executions                    |
| FAILURE SUM                            | BIGINT       | The total number of failed executions                        |
| PROCESSED ROW                          | BIGINT       | The number of processed records for this SQL statement       |
| **Result Set Info**                    |              |                                                              |
| FETCH Result                           | INTEGER      | 0: failure 1: success 2: no results                          |
| **Index Access Info**                  |              |                                                              |
| Memory Full Scan Count                 | BIGINT       | The number of full scans that were performed on memory tables |
| Memory Index Scan Count                | BIGINT       | The number of index scans that were performed on memory tables |
| Disk Full Scan Count                   | BIGINT       | The number of full scans that were performed on disk tables  |
| Disk Index Scan Count                  | BIGINT       | The number of index scans that were performed on disk tables |
| **Disk Access Info**                   |              |                                                              |
| READ DATA PAGE                         | BIGINT       | The number of disk pages that were read from disk for the query |
| WRITE DATA PAGE                        | BIGINT       | not used                                                     |
| GET DATA PAGE                          | BIGINT       | The number of buffers that were accessed for a disk page during query execution |
| CREATE DATA PAGE                       | BIGINT       | The number of disk pages that were created during query execution |
| READ UNDO PAGE                         | BIGINT       | The number of disk pages in UNDO tablespace that were read from disk during query execution |
| WRITE UNDO PAGE                        | BIGINT       | not used                                                     |
| GET UNDO PAGE                          | BIGINT       | The number of buffers in UNDO tablespace that were accessed for a disk page during query execution |
| CREATE UNDO PAGE                       | BIGINT       | The number of disk pages in UNDO tablespace that were created during query execution |

##### [SESSION STAT]

Outputs the data in the V\$SESSTAT performance view every 3 seconds. For more information  on the V$SESSTAT performance view, please refer to the chapter in the *General Reference*.

##### [SYSTEM STAT]

Outputs the data in the V\$SYSSTAT performance view every 3 seconds. For more information on the V$SYSSTAT performance view, please refer to the chapter in the *General Reference*.

##### [MEMORY STAT]

Outputs the data in the V\$MEMSTAT performance view every 3 seconds. For more information on the V$MEMSTAT performance view, please refer to the chapter in the *General Reference*.

### altiwrap

#### About altiwrap

altiwrap encrypts code programs written as persistent stored modules (PSMs). This utility prevents PSM code (e.g., stored procedures and stored functions) from being exposed. 

```
altiwarp {--iname input_file} [--oname output_file]
```



#### Syntax

![altiwrap](media/Utilities/altiwrap.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05740" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3229" image_path_raw="media/Utilities/altiwrap.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiwrap ::=
    altiwrap
        { -h
        | --h
        | --iname input_file [ --oname output_file ] }
```
<!-- IMG_RECOVERY_END ref_id="img-05740" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-h/--h   | Outputs help                                                  |
| \--iname  | Specifies the name of the file to encrypt. On omission of the extension, .sql is assumed. |
| \--oname  | Specifies the file name under which an encrypted code program is to be saved. On omission of the extension, it is saved as a .plb file. |

#### Description

altiwrap encrypts the code programs of stored procedures and stored functions to prevent them from being exposed. 

Altibase can encrypt the following statements. 

-   CREATE [OR REPLACE] PROCEDURE

-   CREATE [OR REPLACE] FUNCTION

-   CREATE [OR REPLACE] TYPESET

-   CREATE [OR REPLACE] PACKAGE

-   CREATE [OR REPLACE] PACKAGE BODY

####  Considerations

-   Code programs cannot be modified after encryption. Changes must be made to the original code program, and then re-encrypted. 
-   Triggers cannot be encrypted. 
-   Encrypted code programs cannot be checked for syntax and semantic errors.

#### Example

Use altiwrap to encrypt the sample1.sql file, and then output it.

Create the sample1. sql file. 

```
iSQL> create or replace procedure proc1 as
type arr1 is table of char(30) index by integer;
v1 arr1;
begin
v1[0] := 'create or replace';
v1[1] := 'typeset';
v1[2] := 'is';
v1[3] := 'success';
println( v1[0] || v1[1] || v1[2] || v1[3] || '!' );
end;
/
```

Encrypt the file

```
$ altiwrap --iname sample1.sql --oname --sample1.plb
```

Run the encrypted file in iSQL.

```
iSQL> @sample1.plb
iSQL> create or replace procedure proc1 WRAPPED
'MjQz
MTk2
AAhjcmVhdGUgb3IgcmVwbGFjZSBwcm9jZWR1cqQBAAQxIGFzCnR5cGUgYXJyMSBpcyB0YWJsQAYAAWYgY2hhcigzMCkgaW5kZXggYnlAAQZ0ZWdlcjsKdjGYBQAEOwpiZWdpbgp2MVswXSA6PSAnY3JlYSu5ASdyBVsxtAN/DHNldK0CMq4CaXO5ATO4AQNzdWNjZXNsAgZwcmludGxuKCC2C3x8YAFACaABVAegAVwGDHx8ICchJyApOwplbmQ7ChEAADVBRDlBRkIzMDE0MzI1Q0U0MzY1RjYxNEI2NkYwQzRDREMzMTdDQTU=
';
/
Create success.
iSQL> exec proc1;
create or replace typeset is success!
Execute success.
```



### awrite

#### About awrite

Outputs the response time of the system call used to create the log file. The output value is used to determine the system call in the LOG_CREATE_METHOD property.

#### Syntax

![awrite](media/Utilities/awrite.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05741" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3313" image_path_raw="media/Utilities/awrite.gif" image_class="C" format="bnf" verified="True" -->
```bnf
awrite ::=
    awrite
```
<!-- IMG_RECOVERY_END ref_id="img-05741" -->


#### Description

Outputs the response time of write () and fallocate () system calls.

#### Example

awrite outputs the following:

```
$ awrite
fallocate to expand file size to 1GB
 Elapsed Time ==>            2.564 seconds
write to expand file size to 1GB
 Elapsed Time ==>            4.020 seconds
```



### checkServer

#### About checkServer

Monitors the Altibase process and, if Altibase terminates, executes a script specified by a user.

```
checkServer [-n] {-f server-restart-script-file}
```



#### Syntax

![checkserver](media/Utilities/checkserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05742" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3347" image_path_raw="media/Utilities/checkserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
checkserver ::=
    checkServer [ -n ] -f server-restrat-script-file
```
<!-- IMG_RECOVERY_END ref_id="img-05742" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-n       | Specifies that checkServer is to be executed in the foreground. If this parameter is omitted, checkServer will be executed in the background |
| \-f       | The name of the script file to be executed when Altibase terminates |

#### Description

checkServer periodically checks whether the Altibase process is running. If checkServer detects that Altibase has terminated, it executes the script specified by a user. It is common to set an Altibase restart script to be executed in the event of termination. Such a restart script can be written as follows:

-   The Altibase starup script 'restart.sh'

```
#! /bin/sh
${ALTIBASE_HOME}/bin/server start
```

When checkServer is executed, it creates the files checkServer.pid and checkServer.log in the $ALTIBASE_HOME/trc directory. checkServer.pid is a kind of lock that prevents another instance of checkServer from being started while the current instance is running. checkServer.log is used to regularly record the status of checkServer.

If checkServer is terminated abnormally, for example by using the command kill -9, the checkServer.pid file will not be deleted from the $ALTIBASE_HOME/trc directory. As long as this file remains in that directory, it will prevent checkServer from being executed again.

To terminate checkServer normally, use the killcheckServer utility

#### Note

checkServer executes the specified restart script only when the Altibase server is shut down without using the server stop command. When the Altibase server is shut down normally using server stop, checkServer is also terminated, and thus does not execute the restart script. That is, checkServer only considers shutdown using the server stop command to be a normal shutdown.

#### Example

checkServer is executed from a shell prompt as follows:

```
$ checkServer –f restart.sh &
```



### dumpbi

#### About dumpbi

dumpbi outputs backup information of the backupInfo file which is recorded in binary format as text format. 

```
dumpbi  <backupinfo_file_name>
```



#### Syntax

![dumpbi](media/Utilities/dumpbi.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05743" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3401" image_path_raw="media/Utilities/dumpbi.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpbi ::=
    dumpbi backupinfo_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-05743" -->


#### Description

Outputs contents of the backupInfo file in text format.

#### Example

At a shell prompt, type the following:

```
$ dumpbi backupinfo
```



#### Output

dumpbi outputs backup information of the backupInfo file in the following format:

##### [BACKUO INFO FILE HDR]

| Field Name             | Value (bytes)                                              | Description                                                  |
| ---------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Backup info slot count | From 0(zero) to the maximum value of the unsigned int type | The number of stored backupinfo slots <br/>(=the number of files backed up until now) |
| Last backup LSN        | FileNo, Offset                                             | The LSN of the point in time at which the most recent backup was performed<br/>(the value necessary for determining the validity of the backupInfo file) |
| Database name          | String                                                     | The database name                                            |

##### [BACKUP INFO SLOT]

| Field Name                    | Value (bytes)                                                | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Slot index                    | From 0(zero) to the maximum value of the unsigned int type   | The slot order                                               |
| Begin backup time             | YYYY-MM-DD HH:MM:SS                                          | The start time of backup                                     |
| End backup time               | YYYY-MM-DD HH:MM:SS                                          | The completion time of backup                                |
| Incremental backup chunk cnt  | From 0(zero) to the maximum value of the unsigned int type   | The number of incremental chunks, including the pages changed from the datafile<br/>(=the number of backed up incremental chunks) |
| Incremental backup chunk size | From 0(zero) to the maximum value of the unsigned int type   | The INCREMENTAL_BACKUP_CHUNK_SI ZE value during backup       |
| Backup target                 | 1: DATABASE <br />2: TABLESPACE                              | The backup target                                            |
| Backup level                  | 1: level 0 <br />2: level 1                                  | The backup level                                             |
| Backup Type                   | 1: full backup <br />2: differentail backup <br />3: cumulative backup | The backup type                                              |
| Tablespace ID                 | From 0(zero) to the maximum value of the unsigned short type | The ID of the tablespace to which the backup target datafile belongs |
| File ID                       | From 0(zero) to the maximum value of the unsigned short type | The backup target datafile ID                                |
| Original file size            | From 0(zero) to the maximum value of the unsigned long type  | The size of the datafile when it was backed up               |
| Backup Tag                    | String                                                       | The backup tag name                                          |
| Backup file name              | String                                                       | The path and name of the backup file                         |

### dumpct

#### About dumpct

Outputs information of the changeTracking file which is recorded in binary format as text format.

```
dumpct  <changeTracking_file_name>
```



#### Syntax

![dumpct](media/Utilities/dumpct.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05744" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3461" image_path_raw="media/Utilities/dumpct.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpct ::=
    dumpct changeTracking_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-05744" -->


#### Description

Outputs contents of the changeTracking file in text format.

#### Example

At a shell prompt, type the following:

```
$ dumpct changeTracking
```



#### Output

dumpct outputs backup information of the changeTracking file in the following format:

The output is separated by [^]:

##### [CHANGE TRACKING FILE HDR]

| Field Name                   | Value (bytes)                                              | Description                                                  |
| ---------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Change tracking body count   | From 0(zero) to the maximum value of the unsigned int type | The number of bodies of the changeTracking file. (The changeTracking file is composed of headers and bodies. The size of the body is 10Mbytes and enlarges in body units if space is insufficient) |
| Icremental backup chunk size | From 0(zero) to the maximum value of the unsigned int type | The value of the INCREMENTAL_BACKUP_CHUNK_SI ZE property at the time of the creation of the changeTracking file. |
| Last flush LSN               | FileNo, Offset                                             | The LSN at the time data changed in memory were written to files. |
| Database name                | String                                                     | The database name                                            |

##### [CHANGE TRACKING FILE BODY]

| Field Name                    | Value (bytes)                                                | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Change tracking body ID       | From 0(zero) to the maximum value of the unsigned int type   | The body ID                                                  |
| Flush LSN                     | FileNo, Offset                                               | The LSN at the time that the body was flushed (for file validation) |
| **Datafile descriptor slot**  |                                                              |                                                              |
| Slot ID                       | The LSN at the time that the body was flushed (for file validation) | The slot ID                                                  |
| Tracking state                | 0: Disables tracking <br/>1: Enables tracking                | The datafile change tracking state                           |
| Tablespace type               | 0: memory TBS <br/>1: disk TBS                               | The tablespace type                                          |
| Page size                     | From 0(zero) to the maximum value of the unsigned int type   | The page size                                                |
| Bitmap extent count           | From 0(zero) to the maximum value of the unsigned short type | The number of allocated bitmap extents                       |
| Current tracking list ID      | From 0(zero) to the maximum value of the unsigned short type | The ID of the bitmap extent list currently being tracked     |
| **Differential0 BmpExt list** |                                                              |                                                              |
| List                          | From 0(zero) to the maximum value of the unsigned int type   | The block ID of the bitmap extent list                       |
| Hint                          | From 0(zero) to the maximum value of the unsigned int type   |                                                              |
| **Differential1 BmpExt list** |                                                              |                                                              |
| List                          | From 0(zero) to the maximum value of the unsigned int type   | The block ID of the bitmap extent list                       |
| Hint                          | From 0(zero) to the maximum value of the unsigned int type   |                                                              |
| **Cumulative BmpExt list**    |                                                              |                                                              |
| List                          | From 0(zero) to the maximum value of the unsigned int type   | The block ID of the bitmap extent list                       |
| Hint                          | From 0(zero) to the maximum value of the unsigned int type   |                                                              |
| Tablespace ID                 | From 0(zero) to the maximum value of the unsigned short type | The ID of the tablespace to which the datafile belongs       |
| File ID                       | From 0(zero) to the maximum value of the unsigned short type | The datafile ID                                              |

### dumpdb

#### About dumpdb

dumpdb outputs memory tablespace information from memory checkpoint image files, or the contents of incremental backup files of the memory tablespace in character format.

```
dumpdb {-j job_number } [-i pingpong_number] [-o] [-f file_name] [-s] [-p] [-d]
```



#### Syntax

![dumpdb](media/Utilities/dumpdb.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05745" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3531" image_path_raw="media/Utilities/dumpdb.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpdb ::=
    dumpdb -j job_number
        [ -i pingpong_number ]
        [ -o ]
        [ -f file_name ]
        [ -s ]
        [ -p ]
        [ -d ]
```
<!-- IMG_RECOVERY_END ref_id="img-05745" -->


#### Parameters

| Parameters          | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| \-j job_number      | Specifies which information to output. Values available for specification and suboptions available for additional specification for each value are as below: <br />0: META (-s -f) <br />1: TABLESPACE (-s -f) 2: TABLESPACE-FLI (-s -d) <br />3: TABLESPACE-FREE-PAGE-LIST (-s) <br />4: TABLE (-o -d)<br />5: TABLE-ALLOC-PAGE-LIST (-o) <br />6: PAGE (-s -p -d) <br />7: INCREMENTAL_BACKUP_META (-f) |
| \-i pingpong_number | Specifies the ping pong number of the checkpoint image file. On omission, 0 is used. |
| \-o                 | Specifies the ID of the object to be analyzed.               |
| \-f file_name       | Specifies the name of the checkpoint image file.             |
| \-s                 | Specifies the ID of the tablespace to be analyzed.           |
| \-p                 | Specifies the ID of the page to be analyzed.                 |
| \-d                 | Outputs detailed information.                                |

#### Description

dumpdb analyzes memory checkpoint image files and outputs information of the meta header, page, etc. in text format, or outputs backup information from incremental backup files of the memory tablespace in text format.

Since this utility analyzes checkpoint image files stored on the disk, the user can view schemas created in the database, regardless of the status of the Altibase server. However, if the server is abnormally terminated after a DDL operation and this leads to the updated schema not being recorded on the disk, such information cannot be given.

#### Examples

At a shell prompt, type the following:

```
$ dumpdb -j 1
$ dumpdb -j 1 -s 0
$ dumpdb -j 2
$ dumpdb -j 3
$ dumpdb -j 4
$ dumpdb -j 4 -d
$ dumpdb -j 4 -o 65536
$ dumpdb -j 5 -o 65536
$ dumpdb -j 6 -s 0 -p 4
```

\<Example 1\> This example outputs information on the memory tablespace. By adding the -s suboption, information only regarding a certain tablespace can be output.

```
$ dumpdb -j 1
```

\<Example 2\> This example outputs information on the FreeListInfo(FLI) page of the memory tablespace. By adding the -s suboption, information only regarding a certain tablespace can be output; by adding the -d suboption, invalid contents of the FLI page can also be output.

```
% dumpdb -j 2
```

<Example 3> This example outputs the free pages of the memory tablespace. By adding the - s suboption, information only regarding a certain tablespace can be output.

```
% dumpdb -j 3
```

<Example 4> This example outputs information on all of the objects created in the database. By adding the -o suboption(the SelfOID in the example below), detailed information only regarding a certain object can be output; by adding the -d suboption, information on columns and indexes of the object can also be output.

```
% dumpdb -j 4
```

<Example 5> This example outputs information on all of the objects created in the database, along with information on columns and indexes.

```
% dumpdb -j 4 -d
```

<Example 6> This example outputs the schema and data of a certain table.

```
% dumpdb -j 4 -o 65568
```

\<Example 7\> This example outputs the list of pages that a certain table uses.

```
% dumpdb -j 5 -o 65568
```

\<Example 8\> This example outputs a certain page from the memory database.

```
% dumpdb –j 6 -s 0 -p 4
```

\<Example 9\> This example executes dumpdb on incremental backup files and outputs backup information.

```
% dumpdb -j 7 -f SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak
dumpdb: Release 6.3.1.0.0 - Production on Oct 31 2012 22:12:21
(c) Copyright 2001 ALTIBase Corporation.  All rights reserved.
 
[BEGIN CHECKPOINT IMAGE HEADER]
Binary DB Version             [ 6.2.1 ]
Redo LSN       [ 1, 5867599 ]
Create LSN     [0, 1385 ]
DataFileDescSlot ID           [ 1, 1 ] 
 
//Incremental backup information stored in the backup file. 
  [BEGIN BACKUPFILE INFORMATION]
 
        Begin Backup Time             [ 2012_11_06 23:18:43 ]
        End Backup Time               [ 2012_11_06 23:18:44 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 1 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END CHECKPOINT IMAGE HEADER]
 
Dump complete.
```



#### Output

The following table describes only the items that are output by executing the dumpdb utility on incremental backup files.

| Field Name          | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Binary DB Version   | The version of the data file.                                |
| Redo LSN            | The Redo LSN for media recovery.<br/> If the value of the Redo LSN of the log anchor is larger than the Redo LSN of the datafile, starting from the Redo LSN output of this item, media recovery is required. |
| Create LSN          | The LSN at the time point of the checkpoint image creation   |
| DataFileDescSlot ID | The DataFileDescSlot ID of the ChangeTracking bound to the memory checkpoint image. |

### dumpddf

#### About dumpddf

dumpddf outputs header information of data files or specific pages in data files. Also, if dumpddf is executed on incremental backup files, header information of the backup file and backup information are output.

```
dumpddf {-f datafile_name} {-m | -p pid}
```



#### Syntax

![dumpddf](media/Utilities/dumpddf.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05746" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3676" image_path_raw="media/Utilities/dumpddf.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpddf ::=
    dumpddf -f datafile_name { -m | -p pid }
```
<!-- IMG_RECOVERY_END ref_id="img-05746" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-f       | Specifies the name of the data file for which it is desired to obtain information. This option must be given. If it is omitted, dumpddf will terminate and output an error message. |
| \-m       | Outputs the data file header information.                    |
| \-p       | Specifies the ID of the page in the data file for which it is desired to obtain information. |

#### Description

Outputs space and information in the data file. The menue page outputs a page from a table or socket.

#### Example

At a shell prompt, type the following:

```
$ dumpddf –f datafile –m
$ dumpddf –f datafile –p page_id
```



#### Output

The following is an example of dumpddf output:

```
[BEGIN DATABASE FILE HEADER]
Binary DB Version             [ 5.4.1 ]
Redo LSN                      [0, 734497 ]
Create LSN                    [0, 1886 ]
MustRedo LSN                  [0, 0 ]
```

In the output, each field has the following meaning:

| Filed Name          | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Binary DB Version   | The version of the data file                                 |
| Redo LSN            | The redo LSN for media recovery. If the loganchor SN is higher than the Redo LSN of the data file, it will be necessary to perform media recovery, starting from this redo LSN. |
| Create LSN          | The LSN at the time when the specified datafile was created. |
| MustRedo LSN        | Indicates that recovery must be performed up to this redo LSN |
| DataFileDescSlot ID | The ID of the DataFileDescSlot of the changeTracking file bound to the disk datafile. |

The following is an example of outputting an incremental backup file by dumpddf.

```
% dumpddf -m -f system001.dbf_TAG_MONDAY.ibak
-----------------------------------------------------------------
     Altibase Client Dump Disk Database File utility.
     Release Version 6.3.1.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[BEGIN DATABASE FILE HEADER]
 
Binary DB Version             [ 6.2.1 ]
Redo LSN                      [1, 5867599 ]
Create LSN                    [0, 1914 ]
MustRedo LSN                  [0, 0 ]
DataFileDescSlot ID           [ 1, 2 ]
 
[BEGIN BACKUPFILE INFORMATION] -->incremental backup information stored in the backup file
 
        Begin Backup Time             [ 2012_11_06 23:18:44 ]
        End Backup Time               [ 2012_11_06 23:18:46 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 2 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/system001.dbf_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END DATABASE FILE HEADER]

```



### dumpla

#### About dumpla

ddumpla outputs the contents of loganchor files, which are saved in binary form, in the form of text. 

Loganchor files contain information that is necessary in order to recover physically stored information (i.e. data files).When a database is created using the CREATE DATABASE statement, Altibase creates these files and stores them with the sequential names loganchor# (where “#” = 1, 2, or 3). Altibase stores these three files, which have the same contents, in the three respective directories specified using the LOGANCHOR_DIR property in altibase.properties. The reason that three files are maintained is to be prepared in the event that some of the files become lost or corrupt. These files contain information about all of the database's tablespaces and the data files stored in them, as well as recovery-related information. When the database is started, this information is used to load the database into memory and prepare to provide service.

```
dumpla <loganchor_file_name>
```



#### Syntax

![dumpla](media/Utilities/dumpla.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05747" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3778" image_path_raw="media/Utilities/dumpla.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpla ::=
    dumpla loganchor_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-05747" -->


#### Description

Outputs the content of a loganchor file in the form of text.

#### Example

At a shell prompt, type the following:

```
$ dumpla loganchor0
```



#### Output

dumpla displays the contents of a loganchor file in the following format:

##### [LOGANCHOR ATTRIBUTE SIZE]

This section indicates the amount of space that is occupied by each kind of data in the loganchor file. The contents of this section are as follows:

| Field Name                 | Value (bytes)                                               | Description                                                  |
| -------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| Loganchor Static Area      | From 0 (zero) to the maximum value of the unsigned int type | The size of the static information in the loganchor file. Most of this information is information that is required for recovery. |
| Tablespace Attribute       | From 0 (zero) to the maximum value of the unsigned int type | The size of the stored tablespace attributes                 |
| Checkpoint Path Attribute  | From 0 (zero) to the maximum value of the unsigned int type | The size of the stored checkpoint path attributes            |
| Checkpoint Image Attribute | From 0 (zero) to the maximum value of the unsigned int type | The size of the stored checkpoint image attributes           |
| Disk Datafile Attribute    | From 0 (zero) to the maximum value of the unsigned int type | The size of the stored disk datafile attributes              |

##### [LOGANCHOR HEADER]

This is loganchor header information, such as the version of the database and the checkpoint Log Sequence Number (LSN). For more information about Log Sequence Numbers, please refer to "dumplf Output Items".

| Field Name                        | Value                                                        | Description                                                  |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Binary DB Version                 | Major.minor.patch ex) 6.2.1                                  | The version of the database executable file with which the loganchor file was created |
| Archivelog Mode                   | Archivelog \|No-Archivelog                                   | Indicates whether the database is running in archive mode    |
| Transaction Segment Entry Count   |                                                              |                                                              |
| Begin Checkpoint LSN              | FileNo, Offset                                               | The LSN that was current when checkpointing most recently began. |
| End Checkpoint LSN                | FileNo, Offset                                               | The LSN that was current when checkpointing was most recently completed. |
| Disk Redo LSN                     | FileNo, Offset                                               | The redo start point for a DRDB.                             |
| LSN for Recovery from Replication | FileNo, Offset                                               | Recovers from replicaiton starts with this LSN.              |
| Server Status                     | SERVER_SHUTDOWN \|SERVER_STARTED                             | Logs the server state. This value is changed to SERVER_STARTED when the server is started and to SERVER_SHUTDOWN when the server is shut down normally. If this value is already set to SERVER_STARTED when the server starts, this indicates that the server was shut down abnormally, so the server will perform restart recovery. |
| End LSN                           | FileNo, Offset                                               | The LSN of the first log that is written to when the server is started up after having shut down normally |
| ResetLog LSN                      | FileNo, Offset                                               | The Reset LSN that was set during incomplete recovery        |
| Last Created Logfile Num          | From 0 (zero) to the maximum value of the unsigned int type  | The number of the most recently created log file             |
| Delete Logfile(s) Range           | Format: [first logfile no. ~ last logfile no.] The numbers of the first and last log files that were deleted. | The range of the most recently deleted log files. When checkpointing is completed, log files that are no longer necessary are deleted. These numbers indicate the range of log files that were deleted. |
| Update And Flush Count            | From 0 (zero) to the maximum value of the unsigned int type  | The number of times that loganchor files were changed and flushed |
| New Tablespace ID                 | From 0 (zero) to the maximum value of the unsigned int type  | The identifier for the next new tablespace. When a tablespace is created, this value will be used as its identifier, and will then be incremented. |
| Checkpoint Scale                  | PAIR\|SINGLE                                                 | The setting of checkpoint scale for the current database.    |

##### [TABLESPACE ATTRIBUTE]

This section provides information about the tablespace. The contents of this section are as follows:

| Field Name                   | Value                                                        | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Tablespace ID                | From 0 (zero) to the maximum value of the unsigned int type  | The identifier of the tablespace                             |
| Tablespace Name              | String Ex.) SYS_TBS_MEM_DIC                                  | The name of the tablespace                                   |
| New Database File ID         | From 0 (zero) to the maximum value of the unsigned int type  | The identifier that will be given to the next file to be added to the tablespace |
| Extent Management            | FREE EXTENT BITMAP TABLESPACE                                | This indicates how extents are managed when a disk tablespace is created. At present, only FREE EXTENT BITMAP TABLESPACE is supported. If FREE EXTENT BITMAP TABLESPACE is enabled, bitmaps can be used to manage the free extents in a disk tablespace. |
| Tablespace Status            | Refer to Possible Tablespace Status Values in [TABLESPACE ATTRIBUTE]. | Indicates the current status of the tablespace               |
| Tablespace Type              | 0 - 8 (Refer to Possible Tablespace Type Values in [TABLESPACE ATTRIBUTE]) | Indicates the type of the tablespace                         |
| Checkpoint Path Count        | The number of checkpoint paths                               | The number of checkpoint image file paths. This applies only to memory tablespaces. |
| Autoextend Mode              | AutoExtend \|Non-AutoExtend                                  | Indicates whether the tablespace extends in size automatically. This applies only to memory tablespaces |
| Shared Memory Key            | From 0 (zero) to the maximum value of the unsigned int type  | The shared memory key for a database that resides in shared memory. This applies only to memory tablespaces |
| Stable Checkpoint Image Num. | 0\|1                                                         | The ping pong number corresponding to the set of checkpoint image files that is stable after checkpointing. This applies only to memory tablespaces. |
| Init Size                    | From 0 (zero) to the maximum value of the unsigned int type  | The initial size (MB) of the tablespace                      |
| Next Size                    | From 0 (zero) to the maximum value of the unsigned int type  | The increment by which the tablespace automatically increases in size (MB) |
| Maximum Size                 | From 0 (zero) to the maximum value of the unsigned int type  | The maximum size of the tablespace.                          |
| Split File Size              | From 0 (zero) to the maximum value of the unsigned int type  | When a memory tablespace is created, it consists of multiple files of this size. For example, if a tablespace 1 GB in size is to be created and the split file size is 100 MB, then 10 files will be created. |

In [TABLESPACE ATTRIBUTE], Tablespace Status can have the following values:

| Value                | Description                                                  |
| -------------------- | ------------------------------------------------------------ |
| OFFLINE              | Currently offline                                            |
| ONLINE               | Currently online                                             |
| INCONSISTENT         | In an inconsistent state                                     |
| CREATING             | Being created                                                |
| DROPPING             | Waiting to be dropped, because the transaction that will drop the database has not been committed yet |
| DROP_PENDING         | The transaction that will drop the database has been committed but the tablespace is still waiting to be dropped because one or more operations are still pending. |
| DROPPED              | Deleted (dropped)                                            |
| DISCARDED            | Discarded                                                    |
| BACKUP               | Being backed up                                              |
| SWITCHING_TO_OFFLINE | Being brough online                                          |
| SWITCHING_TO_ONLINE  | Being taken offline                                          |

The possible values of Tablespace Type in [TABLESPACE ATTRIBUTE] are as follows:

| Value | Description              |
| ----- | ------------------------ |
| 0     | MEMORY SYSTEM DICTIONARY |
| 1     | MEMORY SYSETM DATA       |
| 2     | MEMORY USER DATA         |
| 3     | DISK SYSTEM DATA         |
| 4     | DISK USER DATA           |
| 5     | DISK SYSTEM TEMP         |
| 6     | DISK USER TEMP           |
| 7     | DISK SYSTEM UNDO         |
| 8     | VOLATILE USER DATA       |

##### [MEMORY CHECKPOINT PATH ATTRIBUTE]

This section indicates the path in which checkpoint image files are saved for a memory tablespace. The contents of this section are as follows:

| Field Name      | Value                                                       | Description                      |
| --------------- | ----------------------------------------------------------- | -------------------------------- |
| Tablespace ID   | From 0 (zero) to the maximum value of the unsigned int type | The identifier of the tablespace |
| Checkpoint Path | String                                                      | The checkpoint impage file path  |

##### [MEMORY CHECKPOINT IMAGE ATTRIBUTE]

This section indicates the checkpoint image information for a memory tablespace. The contents of this section are as follows:

| Field Name                          | Value                                                       | Description                                                  |
| ----------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| Tablespace ID                       | From 0 (zero) to the maximum value of the unsigned int type | The identifier of the tablespace                             |
| File Number                         | From 0 (zero) to the maximum value of the unsigned int type | The file number                                              |
| Stable Single Checkpoint Image Num. | 0\|1                                                        | The ping pong number for stable checkpoint image files after checkpointing. This applies only when the checkpoint scale is set to SINGLE. |
| Create LSN                          | \< FileNo, Offset\>                                         | The LSN that was current at the time at which the data file was created |
| Create On Disk (PingPong 0)         | Created\|None                                               | Whether the set of checkpointing files identified by #0 has been created |
| Create On Disk (PingPong 1)         | Created\|None                                               | Whether the set of checkpointing files identified by #1 has been created |
| ChangeTracking DataFileDescSlot ID  | From 0(zero) to the maximum value of the unsigned int type  | The DataFileDescSlot ID of the changeTracking file bound to the memory checkpoint image |

##### [DISK DATABASE FILE ATTRIBUTE]

This information indicates the path in which the data file or files for a disk tablespace are saved. The contents of this section are as follows:

| Field Name                         | Value                                                        | Description                                                  |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Tablespace ID                      | From 0(zero) to the maximum value of the unsigned int type   | The identifier of the tablespace                             |
| Database File ID                   | From 0(zero) to the maximum value of the unsigned int type   | The identifier of the data file                              |
| Database File Path                 | String                                                       | The data file path                                           |
| Create LSN                         | \< FileNo, Offset\>                                          | The LSN that was current at the time that the dat file was created |
| Database File Status               | Refer to Database File Status Values for [DISK DATABASE FILE ATTRIBUTE] | The file state                                               |
| Autoextend Mode                    | AutoExtend\| Non-AutoExtend                                  | Whether auto extension mode has been set                     |
| Create Mode                        | 0\|1                                                         | 0: The file was reused <br/>1: The file is a newly created file |
| Initialize Size                    | From 0 (zero) to the maximum value of the unsigned int type  | The initial size (MB) of the data file                       |
| Current Size                       | From 0 (zero) to the maximum value of the unsigned int type  | The initial size (MB) of the data file                       |
| Next Size                          | From 0 (zero) to the maximum value of the unsigned int type  | The increment by which the data file automatically increases in size (MB) |
| Maximum Size                       | From 0 (zero) to the maximum value of the unsigned int type  | The maximum size (MB) of the data file                       |
| ChangeTracking DataFileDescSlot ID | From 0(zero) to the maximum value of the unsigned int type   | The ID of the DataFileDescSlot of the changeTracking file bound to the disk datafile |

In [DISK DATABASE FILE ATTRIBUTE], Database File Status means the following: 	

| Value        | Description               |
| ------------ | ------------------------- |
| OFFLINE      | Offline                   |
| ONLINE       | Online                    |
| CREATING     | Being created             |
| BACKUP_BEGIN | Backup has started        |
| BACKUP_END   | Backup is being completed |
| DROPPING     | Being dropped (deleted)   |
| RESIZING     | Being resized             |
| DROPPED      | Has been dropped          |

The following is an example of some of the information output by dumpla:

```
[ DISK DATABASE FILE ATTRIBUTE ]
Tablespace ID                  [ 2 ]
Database File ID               [ 0 ]
Database File Path C:\altibase_home\dbs\system001.dbf]
Create LSN                     [0, 4443 ]
Database File Status           [ ONLINE ]
Autoextend Mode                [ Non-Autoextend ]
Create Mode                    [ 0 ]
Initialize Size                [10 MBytes(1280 Pages)]
Current Size                   [10 MBytes(1280 Pages)]
Next Size                      [0 MBytes(0 Pages)]
Maximum Size                   [0 MBytes(0 Pages)]
```



##### [Change Tracking ATTRIBUTE]

This section provides information about the changeTracking file. The contents of this section are as follows:

| Field Name                    | Value                                  | Description                                                  |
| ----------------------------- | -------------------------------------- | ------------------------------------------------------------ |
| Last Flush LSN                | FileNo, Offset                         | The LSN at the time data changed in memory were written to files |
| Change Tracking Manager State | String ex) CHANGE TRACKING MGR ENABLED | The page change tracking state                               |
| Change Tracking File Name     | String                                 | The changeTracking file path                                 |

##### [Backup Info ATTRIBUTE]

This section provides information about the backupInfo file. The contents of this section are as follows:

| Field Name                   | Value                                    | Description                                                  |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------------------ |
| Delete Archivelog File Range | FileNo, Offset                           | The number of the archive log file which can be completely recovered, even after deletion |
| Last Backup LSN              | FileNo, Offset                           | The LSN at the time of the most recently performed backup    |
| Before Backup LSN            | FileNo, Offset                           | The LSN prior to the time of the most recently performed backup |
| Backup Info Manager State    | String e.g.) BACKUP INFO MGR INITIALIZED | The backup information file manager state                    |
| Backup Directory Path        | String e.g.) /backup_dir/                | The backup path                                              |
| Backup Info File Name        | String                                   | The backup information file name                             |

### dumplf

#### ABout dumplf

When a transaction performs an operation that changes the contents of the database, such as an INSERT, DELETE or UPDATE operation, changes are made not only to the database's data buffers, but also to log files. These files are maintained for use in performing recovery if it becomes necessary. To minimize I/O, these logs are recorded in binary format. These log files are stored with the name logfile# (where “#” is the number of the log file, which continuously increments) in the directory specified in the LOG_DIR property in the altibase.properties file.

dumplf is a utility that converts and outputs the contents of these log files in text form. These logs can be used to check the types of operations that are performed on the database and determine the frequency of transactions that change the contents of the database.

```
dumplf {-f log_file_name} [-t transaction_id][-s] [-l][-S lsn [-F path] [-g]]
```



#### Syntax

![](media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05748" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="3996" image_path_raw="media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumplf ::=
    dumplf -f log_file
        [ -t transaction_id ]
        [ -s ]
        [ -l ]
        [ -S lsn [ -F path ] [ -g ] ]
```
<!-- IMG_RECOVERY_END ref_id="img-05748" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-f       | Specifies the name of the file which is to be output.        |
| \-t       | Specifies the ID of the transaciton for which the logs are to be output. |
| \-s       | Specifies that only the header of the logs is to be output. <br/>If this option is omitted, both the header and the body will be output. |
| \-l       | Displays only information corresponding to log types (LT field) and sub-logtypes (OPTYPE and UTYPE fields) in the specified log file. |
| \-S       | Outputs the number of logs of INSERT, UPDATE, DELETE, COMMIT, and ROLLBACK in MMDB. If specified lsn is inserted, only the log after sn is displayed. If ‘0, 0’ is inserted, the entire logs are displayed. |
| \-F       | Specifies the object target path, and it analyzes $ALTIBASE_HOME/logs if omitted. |
| \-g       | Outputs ID statistic of table object along with the entire statistics information. The entire statistic information is output if omitted. |

#### Description

Converts the contents of a log file to text form and outputs it.

#### Example

The following is executed at a shell prompt:

```
$ dumplf -f logfile0
```



#### Output

The following is an example of dumplf output:

```
LSN=<0,820>, COMP:N, MAGIC:820, TID: 6400,BE: N, REP: Y, ISVP: N, ISVP_DEPTH: 0 PLSN=<0,739>, LT: SMR_LT_MEMTRANS_COMMIT, SZ: 45
```

Each field in a log file has the following meaning:다음과 같은 의미를 갖는다.

| Field Name              | Value                                                        | Description                                                  |
| ----------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LSN                     | Format: (FileNo, Offset) Offset range: From 0 (zero) to the maximum value of the unsigned int type | This is the log sequence number, which contains information about the physical location of the current log in a log file. The LSN consists of the identifier of the file number and an offset value. |
| COMP                    | Y\|N                                                         | Indicates whether logs are compressed. <br/>Y: Compressed N: Not compressed |
| MAGIC                   | From 0 (zero) to the maximum value of the unsigned short type | This value is generated using the log file number and offset portions of the LSN to determine whether a log record is valid. When a Redo or Undo action is performed, even if a log record having garbage data is in a log file, it is possible to determine whether the log record is valid. |
| TID                     | From 0 (zero) to the maximum value of the unsigned int type  | The identifier of the transaction                            |
| BE                      | Y\|N                                                         | Y: Indicates that the Sender must check whether to send this log to the Receiver. N: This log is not used by the replication Sender. |
| REP                     | Y\|N                                                         | Y: Indicates that the Sender must check whether to send this log to the Receiver. <br/>N: This log is not used by the replication Sender. |
| ISVP                    | Y\|N                                                         | Y: Indicates that this log is an Implicit Savepoint Log, that is, the first log that is recorded after the start of execution of a statement. If an error occurs while the statement is executing, the transaction is partially rolled back; that is, it is rolled back only as far as this log. |
| ISVP_DEPTH              | 0 - 255                                                      | Implicit Savepoint Depth, that is, the nesting depth when a statement is nested within one or more other statements |
| PLSN                    | Format: (FileNo, Offset) Offset range: From 0 (zero) to the maximum value of the unsigned int type | This value is used to connect all of the logs recorded by the same transaction in a chain. |
| LT                      | String                                                       | Indicates the Log Type (LT).                                 |
| SZ                      | From 0 (zero) to the maximum value of the unsigned int type  | Indicates the size of the log, in bytes                      |
| RdSz                    | From 0 (zero) to the maximum value of the unsigned int type  | indicates the size of the redo log record, in bytes          |
| DMIOff                  | From 0 (zero) to the maximum value of the unsigned int type  | Indicates the location of the logical log that is used to undo a transaction, or is used for replication |
| TableOID                | From 0 (zero) to the maximum value of the unsigned int type  | The object identifier of the table                           |
| OID                     | From 0 (zero) to the maximum value of the unsigned int type  | The object identifier of all objects other than tables. This includes record objects |
| ContType                | 0, 1                                                         | An itnernal vlaue that is used for replicaiton               |
| OPTYPE                  | LogTypeName\<LogTypeNumber\>                                 | The operation type of a Nested Top Action (NTA) log          |
| AFTER                   | SZ: \<size\>, Value: \<value\>                               | The after name image of the log record                       |
| BEFORE                  | SZ: \<size\>, Value: \<value\>                               | The before image of the log record                           |
| UTYPE                   | LogTypeName\<LogTypeNumber\>                                 | The operation type of an UPDATE log                          |
| UPOS                    | Format: (SPACEID:\<SpaceID\>, PID:\<PageID\>, OFFSET:\<Offset\> =\> OID:\<OID\>) | The address of the object that was updated. Additionally contains information about what happened during an update operation. |
| SPACEID                 | From 0 (zero) to the maximum value of the unsigned short type | The identifier of the tablespace containing the object that was updated |
| PID                     | From 0 (zero) to the maximum value of the unsigned int type  | The identifier of the page containing the object that was updated |
| Offset                  | From 0 (zero) to the maximum value of the unsigned short type | The offset from the beginning of the page containing the object that was updated |
| FLISlot PrevPID NextPID | Format: (\<BeforePID\> =\> \<AfterPID\>)                     | An internal value used for managing MMDB tablespaces         |
| ESLSN                   | Format: (FileNo, Offset) Offset range: From 0 (zero) to the maximum value of the unsigned int type | This is the LSN from which recovery would be performed, if necessary |
| Lob Locator             | From 0 (zero) to the maximum value of the unsigned long type | An interally used value related to the use of replication with the LOB type |

The possible values of LT (Log Type) in the dumplf output are as follows:

| Value                     | Description                                |
| ------------------------- | ------------------------------------------ |
| SMR_LT_DUMMY              | Dummy Log                                  |
| SMR_LT_CHKPT_BEGIN        | Checkpoint Being Log                       |
| SMR_LT_DIRTY_PAGE         | Dirty Page Log                             |
| SMR_LT_CHKPT_END          | Checkpoint End Log                         |
| SMR_LT_MEMTRANS_COMMIT    | Memory Transaction Commit Log              |
| SMR_LT_MEMTRANS_ABORT     | Memory Transaction Abort Log               |
| SMR_LT_DSKTRANS_COMMIT    | Disk Transaction Commit Log                |
| SMR_LT_DSKTRANS_ABORT     | Disk Transaction Abort Log                 |
| SMR_LT_SAVEPOINT_SET      | Savepoint Set Log                          |
| SMR_LT_SAVEPOINT_ABORT    | Savepoint Abort Begin Log                  |
| SMR_LT_XA_PREPARE         | XA Prepare Log                             |
| SMR_LT_TRANS_PREABORT     | Abort Begin Log                            |
| SMR_LT_DDL                | DDL (Data Definition Language) Log         |
| SMR_LT_XA_SEGS            | XA Prepare Transaction Segment Information |
| SMR_LT_LOB_FOR_REPL       | LOB Log for Replication                    |
| SMR_LT_UPDATE             | MMDB(Main Memory Database) Update Log      |
| SMR_LT_NTA                | MMDB NTA(Nested Top Action) Log            |
| SMR_LT_COMPENSATION       | Compensation Log                           |
| SMR_LT_DUMMY_COMPENSATION | Dummy Compensation Log                     |
| SMR_LT_FILE_BEGIN         | File Begin Log                             |
| SMR_LT_FILE_TBS_UPDATE    | Tablespace Update Log                      |
| SMR_LT_FILE_END           | File End Log                               |
| SMR_DLT_READONLY          | DRDB(Disk Resident Database) Redo Only Log |
| SMR_DLT_UNDOABLE          | DRDB Undo Log                              |
| SMR_DLT_NTA               | DRDB NTA Log                               |
| SMR_DLT_COMPENSATION      | DRDB Compensation Log                      |
| SMR_DLT_REF_NTA           | DRDB Reference NTA Log                     |
| SMR_LT_TABLE_META         | Table Meta Log for Replication             |

Possible LogTypeName Values for OPTYPE and UTYPE

| Value                                                        | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| SMR_OP_SMM_PERS_LIST_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_ALLOC <br />SMR_OP_SMC_VAR_SLOT_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_FREE <br />SMR_OP_SMC_VAR_SLOT_FREE | Logs related to pages and slots in an MMDB                   |
| SMR_OP_CREATE_TABLE <br />SMR_OP_CREATE_INDEX <br />SMR_OP_DROP_INDEX <br />SMR_OP_ALTER_TABLE <br />SMR_OP_SMM_CREATE_TBS <br />SMR_OP_INSTANT_AGING_AT_ALTER_TABLE <br />SMR_OP_SMC_TABLEHEADER_ALLOC | Logs related to the execution of DDL statements in an MMDB   |
| SMR_MEM_LOB_CURSOR_OPEN <br />SMR_DISK_LOB_CURSOR_OPEN <br />SMR_LOB_CURSOR_CLOSE <br />SMR_PREPARE4WRITE <br />SMR_FINISH2WRITE | Logs related to controlling LOB values in an MMDB            |
| SDR_OP_SDP_CREATE_TABLE_SEGMENT <br />SDR_OP_SDP_CREATE_LOB_SEGMENT <br />SDR_OP_SDP_CREATE_INDEX_SEGMENT <br />SDR_OP_SDP_ADD_LOB_PAGE_TO_AGINGLIST <br />SDR_OP_SDC_ALLOC_UNDO_PAGE <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTENT_FROM_TBS <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTDIR_FROM_LIST <br />SDR_OP_SDPTB_RESIZE_GG <br />SDR_OP_SDPST_ALLOC_PAGE <br />SDR_OP_SDPSF_ALLOC_PAGE <br />SCT_UPDATE_MRDB_CREATE_TBS <br />SCT_UPDATE_MRDB_CREATE_CIMAGE_FILE <br />SCT_UPDATE_MRDB_DROP_TBS <br />SCT_UPDATE_MRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_MRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_MRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_TBS <br />SCT_UPDATE_DRDB_DROP_TBS <br />SCT_UPDATE_DRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_DRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_DBF <br />SCT_UPDATE_DRDB_DROP_DBF <br />SCT_UPDATE_DRDB_EXTEND_DBF <br />SCT_UPDATE_DRDB_SHRINK_DBF <br />SCT_UPDATE_DRDB_AUTOEXTEND_DBF <br />SCT_UPDATE_DRDB_ALTER_DBF_ONLINE <br />SCT_UPDATE_DRDB_ALTER_DBF_OFFLINE <br />SCT_UPDATE_VRDB_CREATE_TBS <br />SCT_UPDATE_VRDB_DROP_TBS <br />SCT_UPDATE_VRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_COMMON_ALTER_ATTR_FLAG | Logs related to tablespaces and segments                     |
| SDR_OP_SDPST_UPDATE_WMINFO_4DPATH <br />SDR_OP_SDPST_UPDATE_MFNL_4DPATH <br />SDR_OP_SDPST_UPDATE_BMP_4DPATH <br />SDR_OP_SDPSF_ADD_PIDLIST_PVTFREEPIDLIST_4DPATH <br />SDR_OP_SDPSF_MERGE_SEG_4DPATH <br />SDR_OP_SDPSF_UPDATE_HWMINFO_4DPATH <br />SDR_OP_SDP_DPATH_ADD_SEGINFOSET | Logs related to page management for Direct Page Insert in a DRDB |
| SDR_OP_SDN_INSERT_KEY_WITH_NTA <br />SDR_OP_SDN_DELETE_KEY_WITH_NTA | NTA Logs for DRDB B-tree Indexes                             |
| SDR_OP_STNDR_INSERT_KEY_WITH_NTA <br />SDR_OP_STNDR_DELETE_KEY_WITH_NTA | NTA Logs for DRDB R-tree Indexes                             |
| SDR_SDP_1BYTE <br />SDR_SDP_2BYTE <br />SDR_SDP_4BYTE <br />SDR_SDP_8BYTE <br />SDR_SDP_BINARY | Physical DRDB logs                                           |
| SDR_SDP_PAGE_CONSISTENT <br />SDR_SDP_INIT_PHYSICAL_PAGE <br />SDR_SDP_INIT_LOGICAL_HDR <br />SDR_SDP_INIT_SLOT_DIRECTORY <br />SDR_SDP_FREE_SLOT <br />SDR_SDP_FREE_SLOT_FOR_SID <br />SDR_SDP_RESTORE_FREESPACE_CREDIT <br />SDR_SDP_RESET_PAGE <br />SDR_SDP_WRITE_PAGEIMG <br />SDR_SDP_WRITE_DPATH_INS_PAGE | Logs related to page and slot management in a DRDB           |
| SDR_SDPST_INIT_SEGHDR <br />SDR_SDPST_INIT_BMP <br />SDR_SDPST_INIT_LFBMP <br />SDR_SDPST_INIT_EXTDIR <br />SDR_SDPST_ADD_RANGESLOT <br />SDR_SDPST_ADD_SLOTS <br />SDR_SDPST_ADD_EXTDESC <br />SDR_SDPST_ADD_EXT_TO_SEGHDR <br />SDR_SDPST_UPDATE_WM <br />SDR_SDPST_UPDATE_MFNL <br />SDR_SDPST_UPDATE_PBS <br />SDR_SDPST_UPDATE_LFBMP_4DPATH <br />SDR_SDPSC_INIT_SEGHDR <br />SDR_SDPSC_INIT_EXTDIR <br />SDR_SDPSC_ADD_EXTDESC_TO_EXTDIR <br />SDR_SDPTB_INIT_LGHDR_PAGE <br />SDR_SDPTB_ALLOC_IN_LG <br />SDR_SDPTB_FREE_IN_LG | The log related to segment and tablespace management for DRDB |
| SDR_SDC_INSERT_ROW_PIECE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_DELETEUNDO <br />SDR_SDC_UPDATE_ROW_PIECE <br />SDR_SDC_OVERWRITE_ROW_PIECE <br />SDR_SDC_CHANGE_ROW_PIECE_LINK <br />SDR_SDC_DELETE_FIRST_COLUMN_PIECE <br />SDR_SDC_ADD_FIRST_COLUMN_PIECE <br />SDR_SDC_DELETE_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_DELETE_ROW_PIECE SDR_SDC_LOCK_ROW | Logs related to the management of rows in tables in a DRDB   |
| SDR_SDC_UPDATE_LOBDESC <br />SDR_SDC_UPDATE_LOBDESC_KEY <br />SDR_SDC_LOB_WRITE_PIECE <br />SDR_SDC_LOB_WRITE_PIECE4DML <br />SDR_SDC_INIT_LOBPAGE <br />SDR_SDC_LOB_PAGE_TO_AGING_LIST | Logs related to the use of the LOB type in a DRDB            |
| SDR_SDC_PK_LOG                                               | Logs related to the use of primary keys for replication in a DRDB |
| SDR_SDC_INIT_CTL <br />SDR_SDC_EXTEND_CTL <br />SDR_SDC_BIND_CTS <br />SDR_SDC_UNBIND_CTS <br />SDR_SDC_BIND_ROW <br />SDR_SDC_UNBIND_ROW <br />SDR_SDC_ROW_TIMESTAMPING <br />SDR_SDC_DATA_SELFAGING | Logs related to MVCC for records in a DRDB                   |
| SDR_SDC_BIND_TSS <br />SDR_SDC_UNBIND_TSS <br />SDR_SDC_SET_INITSCN_TO_TSS <br />SDR_SDC_INIT_TSS_PAGE <br />SDR_SDC_INIT_UNDO_PAGE <br />SDR_SDC_INSERT_UNDO_REC<br /> | Logs related to Transaction Status Slots (TSS) and undo records in a DRDB |
| SDR_SDN_INSERT_INDEX_KEY <br />SDR_SDN_FREE_INDEX_KEY <br />SDR_SDN_INSERT_UNIQUE_KEY <br />SDR_SDN_INSERT_DUP_KEY <br />SDR_SDN_DELETE_KEY_WITH_NTA <br />SDR_SDN_FREE_KEYS <br />SDR_SDN_COMPACT_INDEX_PAGE | Logs related to B-tree indexes in a DRDB                     |
| SDR_SDN_MAKE_CHAINED_KEYS <br />SDR_SDN_MAKE_UNCHAINED_KEYS <br />SDR_SDN_KEY_STAMPING <br />SDR_SDN_INIT_CTL <br />SDR_SDN_EXTEND_CTL <br />SDR_SDN_FREE_CTS | Logs related to MVCC for B-tree index keys in a DRDB         |
| SDR_STNDR_MAKE_CHAINED_KEYS <br />SDR_STNDR_MAKE_UNCHAINED_KEYS <br />SDR_STNDR_KEY_STAMPING | Logs related to MVCC for R-tree index keys in a DRDB         |
| SMR_PHYSICAL                                                 | Physical logs in an MMDB                                     |
| SMR_SMM_MEMBASE_SET_SYSTEM_SCN <br />SMR_SMM_MEMBASE_ALLOC_PERS_LIST <br />SMR_SMM_MEMBASE_ALLOC_EXPAND_CHUNK <br />SMR_SMM_PERS_UPDATE_LINK <br />SMR_SMM_PERS_UPDATE_NEXT_FREE_PAGE_LINK <br />SMR_SMM_MEMBASE_INFO | Logs related to base information in an MMDB                  |
| SMR_SMC_TABLEHEADER_INIT <br />SMR_SMC_TABLEHEADER_UPDATE_INDEX <br />SMR_SMC_TABLEHEADER_UPDATE_COLUMNS <br />SMR_SMC_TABLEHEADER_UPDATE_INFO <br />SMR_SMC_TABLEHEADER_SET_NULLROW <br />SMR_SMC_TABLEHEADER_UPDATE_ALL <br />SMR_SMC_TABLEHEADER_UPDATE_ALLOCINFO <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG <br />SMR_SMC_TABLEHEADER_SET_SEQUENCE <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_COLUMN_COUNT <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_SEGMENT <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG_FOR_MEDIA_RECV <br />SMR_SMC_TABLEHEADER_SET_SEGSTOATTR <br />SMR_SMC_TABLEHEADER_SET_INSERTLIMIT <br />SMR_SMC_INDEX_SET_FLAG <br />SMR_SMC_INDEX_SET_SEGATTR <br />SMR_SMC_INDEX_SET_SEGSTOATTR <br />SMR_SMC_INDEX_SET_DROP_FLAG | Logs related to table headers and index headers in an MMDB   |
| SMR_SMC_PERS_INIT_FIXED_PAGE <br />SMR_SMC_PERS_INIT_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_FREE<br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_VERSION <br />SMR_SMC_PERS_SET_FIX_ROW_DROP_FLAG <br />SMR_SMC_PERS_SET_FIX_ROW_DELETE_BIT <br />SMR_SMC_PERS_INIT_VAR_PAGE <br />SMR_SMC_PERS_UPDATE_VAR_ROW_HEAD <br />SMR_SMC_PERS_UPDATE_VAR_ROW <br />SMR_SMC_PERS_SET_VAR_ROW_FLAG <br />SMR_SMC_PERS_SET_VAR_ROW_NXT_OID <br />SMR_SMC_PERS_WRITE_LOB_PIECE <br />SMR_SMC_PERS_INSERT_ROW <br />SMR_SMC_PERS_UPDATE_INPLACE_ROW <br />SMR_SMC_PERS_UPDATE_VERSION_ROW<br /> SMR_SMC_PERS_DELETE_VERSION_ROW | Logs related to rows in tables in an MMDB                    |

Please refer to the *Atibase Administrator’s Manual* for more information about MVCC.

### dumptrc 

#### About dumptrc

dumptrc outputs a trace log file recorded in $ALTIBASE_HOME/trc directory by converting into a format that a user can identify when the ALTIBASE HDB server is abnormally shut down.

```
dumptrc [-h |[-p file_path][-c [-s]]
[-a|-i file_name [-i file_name]..|-e file_name [-e file_name]..] [-n file_count] |-f |-v]
```



#### Syntax

![](media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05749" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="4141" image_path_raw="media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumptrc ::=
    dumptrc
        [ -h
        | -p file_path [ -c [ -s ] ]
          { -a | -i file_name { -i file_name } | -e file_name { -e file_name } }
          [ -n line_count ]
          [ x ]
        | -f
        | -v ]
```
<!-- IMG_RECOVERY_END ref_id="img-05749" -->


#### Parameters

| Parameter | Description                                                  |
| --------- | ------------------------------------------------------------ |
| \-h       | This outputs help. If the parameter is omitted or used as a duplicate with other parameter, the help would be preceding. |
| \-p       | This parameter specify the path brining a trace log file. Basically, if the path is not specified, a log file in $ALTIBASE_HOME/trc is retrieved. |
| \-c       | This parameter converts ALTIBASE process call stack recorded in altibase_error.log into a function name which a user can identify and return. Use -s option if the user does not wish to convert the call stack address into a function name. Only the call stack is recorded if the parameter is used with -a, -i, -e, -n. |
| \-s       | This parameter outputs only the call stack recorded in a trace log and does not modify a function name. |
| \-a       | This parameter sorts and outputs all the trace log files.    |
| \-i       | This parameter outputs specific trace log files. Multiple log files can be output. However, this parameter cannot be used with -e parameter. |
| \-e       | This parameter outputs all files except a specified trace log file. Multiple log files cannot be repeatedly removed, and this parameter cannot be used with -i parameter. |
| \-n       | This parameter specifies the number of logs which will be output at once. 1 to 127 logs can be output and 10 logs are output unless otherwise specified. |
| \-f       | This parameter outputs a log message which is added whenever a trace log file is recorded. |
| \-v       | This parameter outputs dumptc version                        |

#### Description

The information of Altibase internal modules executed during Altibase termination is recorded in the process call stack. The module informaiton can be retrieved with dumptrc and retrievable trace log files can use the following files that are recorded into $ALTIBASE_HOME/trc.

-   ERROR : altibase_error.log

-   SERVER : altibase_boot.log

-   SM : altibase_sm.log

-   RP : altibase_rp.log

-   QP : altibase_qp.log

-   DK : altibase_dk.log

-   DR : altibase_dr.log

-   XA : altibase_xa.log

-   MM : altibase_mm.log

-   RP_CONFLICT : altibase_rp_conflict.log

-   DUMP : altibase_dump.log

-   TRC : altibase_trace.log

-   SNMP : altibase_snmp.log

-   CM : altibase_cm.log

-   MISC : altibase_misc.log

-   SD : altibase_sd.log

If outputting a trace log file located from a different path other than $ALTIBASE_HOME/trc, the path can be modified by using -p parameter. 

If experiencing abnormal termination of Altibase server, convert the process call stack into dumptrc and send it to Altibase technical service team so that the problem can be quickly solved.

#### Precaution

The version of Altibase executable file and that of the dumptrc should be identical to confirm the call stack information in order to normally operate the dumptrc.

#### Examples

<Example 1>  altibase_error.log and altibase_boot.log are bound to output

```
$ dumptrc -i server -i error
[2015/10/21 17:29:42 55C][PID:32702][Thread-2]
  ==> Initialize Disaster Recovery Manager  
[2015/10/21 17:29:42 55D][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 55E][PID:32702][Thread-2]
  ==> Initialize MMX Service  
[2015/10/21 17:29:42 55F][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 560][PID:32702][Thread-2]
  ==> Initialize Audit Service  
[2015/10/21 17:29:42 561][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 562][PID:32702][Thread-2]
  ==> Initialize Job Manager  
[2015/10/21 17:29:42 563][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF
Caller[1] 0000000000426CFE
Caller[2] 00007FD306FD4CB0
Caller[3] 00007FD30609F763
Caller[4] 000000000042F66F
Caller[5] 00000000004213CE
Caller[6] 000000000041D1E0
Caller[7] 00007FD305FD376D
Caller[8] 00000000004206BD
END-STACK =======================================
10 logs printed.
```

<Example 2> Output except error.log.

```
$ dumptrc -e error
[2015/10/21 17:29:48 571][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:48 572][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 573][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:49 574][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 575][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:49 576][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 577][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:53 578][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 579][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:53 57A][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
10 logs printed.
```

<Example 3> Output a call stack, altibase_boot.log, and altiabse_sm.log together, but output the top 20 logs.

```
$ dumptrc -c -i error -i server -i sm -n 20
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:42 551][PID:32702][Thread-2]
  ==> Initialize Security Module  
[2015/10/21 17:29:42 552][PID:32702][Thread-2]
  ... [SUCCESS] 
...
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
Caller[3] 00007FD30609F763  => not found
Caller[4] 000000000042F66F  => mmtSessionManager::run()
Caller[5] 00000000004213CE  => mmi::serverStart(int, int)
Caller[6] 000000000041D1E0  => main
Caller[7] 00007FD305FD376D  => not found
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```

<Example 4>  Output a call stack from trc log of a different directory

```
$ dumptrc -p /home/djin/work/altidev4/trunk/altibase_home/trc -c -n 20

Path : /home/djin/work/altidev4/trunk/altibase_home/trc
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:45 568][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:45 569][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
...
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
...
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```



### killCheckServer

#### About killCheckServer

killCheckServer terminates the checkServer utility if it is currently running.

```
killCheckServer
```



#### Syntax

![killcheckserver](media/Utilities/killcheckserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05750" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="4379" image_path_raw="media/Utilities/killcheckserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
killcheckserver ::=
    killCheckServer
```
<!-- IMG_RECOVERY_END ref_id="img-05750" -->


#### Description

killCheckServer terminates the checkServer utility if it is currently running.

If the server stop or server kill command was issued to stop the Altibase server, the server script terminates checkServer process by executing this utility before terminating the Altibase instance. In that case, the following results of killCheckServer execution will be recorded in the killCheckServer.log file under the $ALTIBASE_HOME/trc directory:

- When checkServer is running:

```
checkServer killed.
```


- When checkServer is not running: 

```
ERROR CODE : -27
```


If the user executes the killCheckServer command directly, then the result will not be recorded in the file.

#### Example

At a shell prompt, enter the following:

```
$ killCheckServer
```



### server

#### About server

server is a shell script that is used to create, start up, shut down and check the status of Altibase.

```
server { start | stop | restart | kill | status | create db_charset national_charset | startRoleManager | stopRoleManager } 
```



#### Syntax

![server](media/Utilities/server.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-05751" source_md="Manuals/Altibase_trunk/eng/Utilities Manual.md" line_no="4427" image_path_raw="media/Utilities/server.gif" image_class="C" format="bnf" verified="True" -->
```bnf
server ::=
    'server' { 'start'
             | 'stop'
             | 'restart'
             | 'kill'
             | 'status'
             | 'create' db_charset national_charset
             | 'startRoleManager'
             | 'stopRoleManager' }
```
<!-- IMG_RECOVERY_END ref_id="img-05751" -->


#### Parameters

| Parameter        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| start            | Starts up the Altibase process                               |
| stop             | Shuts down the Altibase process                              |
| restart          | Restarts the Altibase process                                |
| kill             | Forcibly termincates the Altibase process                    |
| status           | Displays the status of the Altibase process                  |
| create           | Creates a database that is 10MB in size, runs in noarchivelog mode, and uses the specified character sets |
| startRoleManager | Starts the Altibase process as the role manager for Disaster Recovery |
| stopRoleManager  | Terminates the role manager                                  |

#### Description

iSQL is used to execute SQL statements for creating, starting up and shutting down Altibase. These frequently used commands have been combined and provided in the form of the server shell script for the convenience of DBAs.

The server script includes the following functionalities:

-   Starting up the Altibase process 
-   Shutting down the Altibase process 
-   Restarting the Altibase process 
-   Forcibly terminating the Altibase process 
-   Displaying the result of querying “SELECT * from TAB;” 
-   Creating an Altibase 
-   Starting the Altibase process as the role manager

For more information about using SQL to manage Altibase databases, please refer to the *SQL Reference*.

#### Examples

The server shell command is used as follows:

```
$ server start
$ server restart
$ server stop
$ server status
$ server kill
$ server create ksc5601 utf16
$ server startRoleManager
$ server stopRoleManager
```



#### References

Please refer to the *Administrator’s Manual* and *SQL Reference*.
<!-- SOURCE_BLOCK_END source_id="SRC-000166" block_id="BLOCK-000930" -->

## SRC-000197 - Trunk

| Field | Value |
| --- | --- |
| `source_id` | SRC-000197 |
| `source_path` | Manuals/Altibase_trunk/kor/Utilities Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | ko |
| `authority_label` | Korean authoritative; Altibase 8.1 verified source |
| `source_sha256` | 7122c896093fd9f20f1d6057fdc5a71c1f53ba787ec671ceda22081eb8799250 |
| `byte_count` | 261522 |
| `line_count` | 4814 |
| `estimated_tokens` | 46040 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000197" source_path="Manuals/Altibase_trunk/kor/Utilities Manual.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="ko" authority_label="Korean authoritative; Altibase 8.1 verified source" sha256="7122c896093fd9f20f1d6057fdc5a71c1f53ba787ec671ceda22081eb8799250" byte_count="261522" line_count="4814" estimated_tokens="46040" block_id="BLOCK-000931" -->
Utilities Manual
================

#### Trunk

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 









































<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Tools & Utilities Utilities Manual
Trunk
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>


<br>

# 목차

- [서문](#서문)
  - [이 매뉴얼에 대하여](#이-매뉴얼에-대하여)
- [1.aexport](#1aexport)
  - [aexport 소개](#aexport-소개)
  - [사전 설정](#사전-설정)
  - [aexport사용방법](#aexport-사용방법)
- [2.altiComp](#2alticomp)
  - [altiComp 소개](#alticomp-소개)
  - [altiComp 사용 방법](#alticomp-사용-방법)
  - [비교(DIFF) 기능](#비교diff-기능)
  - [일치(SYNC) 기능](#일치sync-기능)
- [3.aku](#3aku)
  - [개요](#개요-2)
  - [구성 요소](#구성-요소)
  - [구문](#구문-2)
  - [파라미터](#파라미터-2)
  - [주의사항](#주의사항)
  - [제약사항](#제약사항)
  - [사용 예](#사용-예)
- [4.altiMon](#4altimon)
  - [개요](#개요-3)
  - [구문](#구문-3)
  - [파라미터](#파라미터-3)
  - [시스템 요구사항](#시스템-요구사항)
  - [altiMon 시작 및 중지](#altiMon-시작-및-중지)
  - [altiMon 설정](#altiMon-설정)
  - [altiMon 로그](#altimon-로그)
- [5.기타 Utilities](#5기타-utilities)
  - [altiAudit](#altiaudit)
  - [altibase](#altibase)
  - [altierr](#altierr)
  - [altipasswd](#altipasswd)
  - [altiProfile](#altiprofile)
  - [altiwrap](#altiwrap)
  - [awrite](#awrite)
  - [checkServer](#checkserver)
  - [dumpbi](#dumpbi)
  - [dumpct](#dumpct)
  - [dumpdb](#dumpdb)
  - [dumpddf](#dumpddf)
  - [dumpla](#dumpla)
  - [dumplf](#dumplf)
  - [dumptrc](#dumptrc)
  - [killCheckServer](#killcheckserver)
  - [server](#server)





<br>

서문
====

## 이 매뉴얼에 대하여

이 매뉴얼은 Altibase를 사용하면서 필요한 유틸리티에 대해서 설명한다.

### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

-   데이터베이스 관리자

-   성능 관리자

-   데이터베이스 사용자

-   응용 프로그램 개발자

-   기술지원부

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

-   컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

-   관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

-   컴퓨터 프로그래밍 경험

-   데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

### 소프트웨어 환경

이 매뉴얼은 데이터베이스 서버로 Altibase 버전 7.1을 사용한다는 가정 하에 작성되었다.

### 이 매뉴얼의 구성

이 매뉴얼은 다음과 같이 구성되어 있다.

- 제 1장 aexport  
  이 장은 Altibase 데이터베이스 간 자동화된 데이터 마이그레이션(migration)을 지원하기 위한 도구인 aexport에 대해서 설명한다.

- 제 2장 altiComp  
  이 장은 altiComp 유틸리티의 기능을 소개하고, 불일치하는 데이터를 비교하고 일치시키는 기능 등을 설명한다.

- 제 3장 aku

  이 장은 쿠버네티스를 이용한 파드 간 데이터 이중화를 지원하기 위한 도구인 aku에 대해서 설명한다.

- 제 4장 altiMon

  이 장은 Altibase의 서버와 Altibase 서버가 구동 된 운영체제의 자원 상태를 수집하는 모니터링 유틸리티인 altiMon에 대해서 설명한다. 

- 제 5장 기타 Utilities  
  이 장은 aexport, altiComp, aku, altiMon을 제외한 나머지 유틸리티에 대해서 설명한다.

### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이 매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

-   구문 다이어그램

-   샘플 코드 규칙

### 구문 다이어그램

이 매뉴얼에서는 다음 구성 요소로 구축된 다이어그램을 사용하여, 명령문의 구문을 설명한다.

| 구성 요소                       | 의미                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| ![](media/Utilities/image1.gif) | 명령문이 시작한다. 완전한 명령문이 아닌 구문 요소는 화살표로 시작한다. |
| ![](media/Utilities/image2.gif) | 명령문이 다음 라인에 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 종료한다. |
| ![](media/Utilities/image3.gif) | 명령문이 이전 라인으로부터 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 시작한다. |
| ![](media/Utilities/image4.gif) | 명령문이 종료한다.                                           |
| ![](media/Utilities/image5.gif) | 필수 항목                                                    |
| ![](media/Utilities/image6.gif) | 선택적 항목.                                                 |
| ![](media/Utilities/image7.gif) | 선택사항이 있는 필수 항목. 한 항목만 제공해야 한다.          |
| ![](media/Utilities/image8.gif) | 선택사항이 있는 선택적 항목                                  |
| ![](media/Utilities/image9.gif) | 선택적 항목. 여러 항목이 허용된다. 각 반복 앞부분에 콤마가 와야 한다. |

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어 설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                         | 예제                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]          | 선택 항목을 표시                                             | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시        | { ENABLE \| DISABLE \| COMPILE }                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                    | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략을 표시           | SQL\> SELECT ename FROM employee; ENAME ------------------------ SWNO HJNO HSCHOI . . . 20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이외의 기호들                             | EXEC :p1 := 1; acc NUMBER(11,2);                             |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치 지정자 | SELECT \* FROM *table_name*; CONNECT userID/password;        |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 칼럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드       | DESC SYSTEM_.SYS_INDICES_;                                   |

### 관련 자료

자세한 정보를 위하여 다음 문서 목록을 참조하기 바란다.

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   iSQL User’s Manual

-   iLoader User's Manual

### Altibase는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음 버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께 고객서비스포털(*http://support.altibase.com/kr/* )로 보내주시기 바랍니다.

-   사용 중인 매뉴얼의 이름과 버전

-   매뉴얼에 대한 의견

-   사용자의 성함, 주소, 전화번호

이 외에도 Altibase 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인 문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인 부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를 요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.



1.aexport
=======

## aexport 소개

### 개요

aexport는 Altibase 데이터베이스 간의 자동화된 데이터 마이그레이션(migration)을 지원하기 위한 도구이다. aexport는 데이터베이스의 논리적인 구조 및 데이터를 텍스트로 저장하고, 이를 다시 새로운 Altibase 데이터베이스로 로딩하기 위한 스크립트를 자동으로 생성하여 준다.

aexport가 접속한 데이터베이스로부터 추출할 수 있는 객체 및 구성 요소는 데이터베이스 사용자, 사용자 권한, 테이블, 테이블스페이스, 테이블 제약조건, 인덱스, 뷰, Materialized View, 저장 프로시저, 시퀀스, 그리고 이중화 객체이다.

aexport는 데이터베이스의 논리적인 구조를 SQL 스크립트로 변환하여 저장하고, 모든 데이터를 텍스트로 내려 받기 때문에 상이한 Altibase 버전간, 그리고 상이한 플랫폼 간의 데이터 이동 시에 유용하게 사용될 수 있다. Altibase 서버는 구동했지만 서비스는 하지 않는 상태 즉, 클라이언트 연결이 없을 때 aexport를 사용하기를 권장한다.

### aexport 기능 소개

aexport가 추출할 수 있는 데이터베이스 객체 및 구성 요소는 다음과 같다.

-   데이터베이스 사용자

-   사용자 권한

-   롤(Role)

-   테이블스페이스

-   테이블

-   테이블 제약 조건

-   인덱스

-   뷰

-   Materialized View

-   저장 프로시저

-   이중화 객체

aexport를 수행하면 위에 열거한 데이터베이스 구성 요소를 생성하기 위한 SQL 스크립트와 이를 구동하기 위한 쉘 스크립트가 생성된다.

##### aexport 모드와 SQL 스크립트 파일

aexport는 데이터베이스의 어떤 부분을 추출하는지에 따라서 다른 모드로 실행할 수 있다. 모드는 aexport 실행 시 커맨드 라인에서 지정할 수 있다.

aexport 실행 모드와 각 모드 별로 생성되는 SQL 스크립트 파일은 아래의 절에서 설명한다.

##### 전체 DB 모드

이 모드는 전체 데이터베이스를 추출한다. SYS 사용자만이 이 모드로 aexport를 실행할 수 있다.

이 모드로 aexport를 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   SYS_CRT_DIR.sql: 모든 디렉토리 객체 생성

-   SYS_CRT_USER.sql: 모든 사용자와 롤(Role) 생성

-   SYS_CRT_SYNONYM.sql: 모든 시노님(Synonym) 객체 생성

-   SYS_CRT_REP.sql: 모든 이중화 객체 생성

-   ALL_CRT_VIEW_PROC.sql: 모든 뷰와 프로시저 생성

-   ALL_CRT_TBS.sql: 모든 테이블스페이스 생성

-   ALL_CRT_TBL.sql: 모든 사용자 테이블 생성

-   ALL_CRT_INDEX.sql: 모든 사용자 인덱스 생성

-   ALL_CRT_FK.sql: 모든 사용자의 외래 키 생성

-   ALL_CRT_TRIG.sql: 모든 사용자의 트리거 생성

-   ALL_CRT_SEQ.sql: 모든 사용자의 시퀀스 생성

-   ALL_CRT_LINK.sql: 모든 사용자의 데이터베이스 Link 생성

-   ALL_EXE_STATS.sql: 모든 사용자의 테이블, 칼럼, 인덱스의 통계 정보 생성

-   ALL_REFRESH_MVIEW.sql: 모든 사용자의 Materialized View를 리프레쉬

-   ALL_ALT_TBL.sql : 모든 사용자의 테이블과 파티션에 대한 접근 모드를 변경

> 주의: 롤(Role)은 비스키마 객체이므로 전체 DB 모드에서만 추출할 수 있다.
>

##### 사용자 모드

이 모드는 옵션으로 지정하는 사용자가 소유한 모든 객체를 추출한다. SYS 사용자와 옵션으로 지정하는 사용자만이 이 모드로 aexport를 실행할 수 있다. 사용자 모드로 aexport를 실행하려면, -u 커맨드라인 옵션에 사용자 이름을 지정하면 된다.

이 모드로 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   {사용자명}_CRT_TBL.sql: 지정한 사용자의 모든 테이블 생성

-   {사용자명}_CRT_INDEX.sql: 지정한 사용자의 모든 인덱스 생성

-   {사용자명}_CRT_FK.sql: 지정한 사용자의 모든 외래 키 생성

-   {사용자명}_CRT_TRIG.sql: 지정한 사용자의 모든 트리거 생성

-   {사용자명}_CRT_SEQ.sql: 지정한 사용자의 모든 시퀀스 생성

-   {사용자명}_CRT_LINK.sql: 지정한 사용자의 모든 데이터베이스 Link 생성

-   {사용자명}_EXE_STATS.sql : 지정한 사용자의 모든 테이블, 칼럼, 인덱스의 통계 정보를 설정
    
-   {사용자명}_REFRESH_MVIEW.sql: 지정한 사용자의 모든 Materialized View를 리프레쉬
    
-   {사용자명}_ALT_TBL.sql : 지정한 사용자의 테이블과 파티션에 대한 접근 모드를 변경

##### 객체 모드

이 모드는 옵션으로 지정하는 모든 객체들을 추출한다. 객체 모드로 aexport를 실행하려면, -object 커맨드라인 옵션에 추출하고자 하는 객체들을 *user.object* 의 형태로 쉼표(“,”)로 분리 하여 명시하면 된다 (공백문자가 포함되면 안됨). SYS 사용자와 지정하는 객체의 소유자만이 이 모드로 aexport를 실행할 수 있다.

지정한 모든 객체의 소유자는 같아야 한다. 그러나, SYS 사용자로 실행할 때는 지정한 객체들의 소유자가 각각 다른 사용자여도 무방하다.

이 모드로 실행할 때 생성되는 SQL 스크립트 파일은 아래와 같다.

-   {사용자명}_{객체명}_CRT.sql: 지정한 사용자 객체 생성

-   {사용자명}_{객체명}_STATS.sql: 지정한 사용자 통계 정보 생성

##### 쉘 스크립트 파일

위에서 기술한 SQL 스크립트 파일 외에, aexport 수행 시 생성되는 쉘 스크립트 파일들은 다음과 같다.

-   run_il_in.sh: 데이터 로드 스크립트

-   run_il_out.sh: 데이터 다운로드 스크립트

-   run_is.sh: 스키마 생성 스크립트

-   run_is_con.sh: constraint 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일이 생성된다. 이 파일은 인덱스, 외래 키, 트리거, 및 이중화 객체를 생성하는 SQL 스크립트를 포함한다.
    
-   run_is_fk.sh: 외래키와 트리거 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_index.sh: 인덱스 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_repl.sh: 이중화 생성 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_refresh_mview.sh: Materialized View를 refresh하는 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.
    
-   run_is_alt_tbl.sh : 테이블과 파티션에 대한 접근 모드를 변경하는 스크립트. TWO_PHASE_SCRIPT 프로퍼티를 ON으로 설정하면, 이 쉘 스크립트 파일은 생성되지 않는다.

aexport 수행 후 생성된 쉘 스크립트를 대상 데이터베이스에 대해 실행하면, 데이터베이스의 논리적 구조가 자동으로 생성된다. 또한 기존의 데이터가 모두 대상 데이터베이스에 로딩된다. 쉘 스크립트는 Altibase iLoader를 사용하여 데이터 다운로드 및 업로드를 수행한다. 쉘 스크립트 내에서 iLoader를 사용하는 과정은 완전히 자동화되어 있기 때문에 사용자가 iLoader의 사용법에 익숙하지 않아도 사용이 가능하다.

aexport에 의해 생성된 모든 파일은 텍스트 파일이기 때문에 사용자의 필요에 따라 변경 후 사용이 가능하므로, 좀 더 유연하게 활용할 수 있다.

##### aexport 프로퍼티와 스크립트 파일

이 절은 aexport 프로퍼티 설정에 따라서 생성되는 스크립트 파일에 대해서 설명한다.

프로퍼티에 대한 상세한 설명은 “aexport 프로퍼티” 절을 참조한다.

-   INVALID_SCRIPT = ON 일 때, INVALID.sql 파일이 생성된다. 이 파일은 유효하지 않은 모든 뷰와 저장 프로시저를 생성하는 SQL 스크립트를 포함하는데, 이 파일을 실행하는 쉘 스크립트 파일은 생성되지 않는다.
    
-   TWO_PHASE_SCRIPT = ON 일 때, ALL_OBJECT.sql 파일과 ALL_OBJECT_CONSTRAINS.sql 파일이 생성된다. ALL_OBJECT.sql 파일은 모든 객체를 생성하는 SQL 스크립트를, ALL_OBJECT_CONSTRAINS.sql 파일은 모든 인덱스, 외래키, 트리거와 이중화 객체를 생성하는 SQL 스크립트를 포함한다. 또한, ALL_OBJECT_CONSTRATINS.sql을 실행하는 run_is_con.sh 쉘 스크립트 파일이 생성된다.

## 사전 설정

### DBMS_METADATA 패키지 설치

DBMS_METADATA 패키지는 데이터베이스 딕셔너리로부터 객체 생성 DDL 구문 또는 권한 GRANT 구문을 추출하는 기능을 제공한다. 

aexport는 DBMS_METADATA 패키지에 의존성을 가지기 때문에, aexport를 사용하기 위해서는 해당 패키지를 반드시 Altibase에 설치해야 한다. DBMS_METADATA 패키지가 설치되지 않은 Altibase를 대상으로 aexport를 수행하면 다음과 같은 에러가 발생한다.

```bash
$ aexport -s localhost -u sys -p manager
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 7.3.0.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[ERR-91144 : DBMS_METADATA package does not exist.]
```

> DBMS_METADATA 패키지에 대한 자세한 설명과 예제는 *Stored Procedures Manual*의 'Altibase 저장 패키지'를 참조하기 바란다.

### aexport 설정

aexport는 서버에 접속하기 위해서 다음과 같은 정보가 필요하다.

-   ALTIBASE_HOME  
    서버 혹은 클라이언트가 설치된 경로

-   server_name  
    Altibase 서버가 구동되어 있는 컴퓨터 서버의 이름(또는 IP 주소)

-   port_no  
    TCP 또는 IPC로 접속할 때 사용할 포트 번호

-   user_id  
    데이터베이스에 등록된 사용자 ID

-   Password  
    사용자 ID와 일치하는 암호

-   NLS_USE  
    데이터 검색 시, 사용자에게 보여주는 문자 집합

ALTIBASE_HOME은 환경 변수로 설정하도록 되어 있으며, 나머지는 커맨드 라인 옵션을 통해서 설정할 수 있다.(자세한 내용은 “aexport 사용방법”을 참고한다.)

aexport를 실행하려면 ALTIBASE_HOME 환경 변수와 aexport 설정 파일(aexport.properties)이 필요하다. 실행 전에 ALTIBASE_HOME이 바르게 설정되어 있어야 하며, 샘플로 제공되는 aexport.properties.sample 파일을 이용해 aexport용 설정 파일을 생성해 두어야 한다.

ALTIBASE_HOME은 일반적으로 서버가 설치될 때 자동으로 설정되는데 클라이언트의 경우에는 사용자가 직접 설정해야 한다. 설정되지 않았을 경우에는 제대로 동작하지 않을 수 있으므로 실행 전에 바르게 설정되어 있는지 확인할 것을 권장한다.

port_no와 NLS_USE는 환경 변수 또는 서버 설정 파일(altibase.properties)을 이용해서 설정할 수도 있다. 세 가지 방법으로 모두 설정되어 있을 경우 적용 우선 순위는 다음과 같다.

1.  커맨드 라인 옵션

2.  환경 변수 (ALTIBASE_PORT_NO, ALTIBASE_NLS_USE)

3.  서버 설정 파일(altibase.properties)

그러므로 설정된 값과 다른 옵션으로 연결하고자 할 경우, 커맨드 라인 옵션을 사용하면 서버 설정 파일이나 환경 변수를 변경하지 않아도 된다.

옵션이 설정되어 있지 않을 경우에는 aexport가 처음 실행될 때 옵션 입력 프롬프트를 띄우고 사용자에게서 해당 값을 입력 받는다. 이 때 바르지 않은 형식이나 유효하지 않은 값을 입력할 경우, aexport는 제대로 동작하지 않을 수 있다.

특히 NLS_USE 옵션은 사용자가 설정하지 않았더라도 실행시에 입력 프롬프트를 띄우지 않는다. 만약 사용자가 NLS_USE 옵션을 설정하지 않았다면 현재 데이터베이스의 캐릭터 셋을 이용해 접속을 시도한다. 이 때 데이터베이스의 문자집합이 데이터베이스 캐릭터 셋이 아닐 경우에는 올바로 실행되지 않거나 사용자 데이터가 일부 깨질 수 있으므로 반드시 NLS_USE를 사용 환경에 맞는 값으로 설정해야 한다.

원활한 aexport 사용을 위해 다음 환경 변수를 설정할 것을 권장한다.

-   ALTIBASE_HOME: 서버 혹은 클라이언트가 설치된 경로

-   ALTIBASE_PORT_NO: 서버에 접속할 때 사용할 포트 번호

-   ALTIBASE_NLS_USE: 데이터 검색 시, 사용자에게 보여주는 문자집합

-   PATH: 실행파일이 있는 경로인 \$ALTIBASE_HOME/bin 추가

### 환경변수

##### ALTIBASE_HOME

패키지가 설치된 디렉토리를 설정한다. aexport 사용을 위해 반드시 설정해야 하는 환경변수이다.

##### ALTIBASE_PORT_NO

접속할 서버의 포트 번호를 설정하는 환경 변수이다. -PORT 옵션 또는 altibase.properties를 통해서 지정할 수도 있다.

포트 번호 설정의 우선순위는 -PORT 옵션, 환경 변수 ALTIBASE_PORT_NO, altibase.properties 순이며 설정되지 않았을 경우에는 포트 번호 입력 프롬프트가 출력된다.

##### ALTIBASE_SSL_PORT_NO

aexport가 SSL/TLS 통신으로 접속할 서버의 포트 번호이다.

SSL 포트 번호 설정의 우선 순위는 -PORT 옵션, 환경변수 ALTIBASE_SSL_PORT_NO, altibase.properties 파일 내의 프로퍼티 순이다. 만약 아무것도 설정되지 않았을 경우에는 포트 번호 입력 프롬프트가 출력된다.

##### ALTIBASE_NLS_USE

서버에 연결할 때 사용할 캐릭터 셋을 설정한다. -NLS_USE 옵션 또는 altibase.properties를 통해서 지정할 수도 있다.

NLS_USE 설정의 우선순위는 -NLS_USE 옵션, 환경 변수 ALTIBASE_NLS_USE, altibase.properties 순이며 설정되지 않았을 경우에는 데이터베이스 캐릭터 셋을 사용한다.

> 주의: 서버 캐릭터 셋과 ALTIBASE_NLS_USE에 설정한 값이 다를 경우에는 정상적으로 동작하지 않을 수 있다. 반드시 적절한 값을 설정할 것을 권장한다.

##### ALTIBASE_UT_FILE_PERMISSION

aexport, iLoader, iSQL이 생성하는 파일들의 권한을 설정하는 공통 환경변수이다.  값을 설정하지 않으면 666 ( user:rw,  group:rw,  other: rw)로 설정된다.

예) user:rw,  group:--,  other:--로 설정하는 경우, export ALTIBASE_UT_FILE_PERMISSION=600

ISQL_FILE_PERMISSION, AEXPORT_FILE_PERMISSION, 또는 ILO_FILE_PERMISSION이 설정된 경우, ALTIBASE_UT_FILE_PERMISSION 환경 변수 보다 우선 처리된다.

예)export ALTIBASE_UT_FILE_PERMISSION=660; export ISQL_FILE_PERMISSION=600;

iSQL에서 생성되는 파일의 권한은 ISQL_FILE_PERMISSION=600이 우선처리되어 user:rw,  group:--,  other:--으로 설정된다.  aexport, iloader가 생성하는 파일의 권한은  ALTIBASE_UT_FILE_PERMISSION=660에 따라 user:rw,  group:rw,  other:--으로 설정된다.

##### AEXPORT_FILE_PERMISSION

aexport가 생성하는 파일 권한을 설정하는 환경 변수이다. 값을 설정하지 않으면 666 ( user:rw,  group:rw,  other: rw)로 설정된다.

예) user:rw,  group:--,  other:--로 설정하는 경우, export AEXPORT_FILE_PERMISSION=600 

## aexport 사용 방법

### 구문

![](media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06951" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="574" image_path_raw="media/Utilities/83e5d3722e9a7c575270c6a6bb5206c2.gif" image_class="C" format="bnf" verified="True" -->
```bnf
aexport ::=
    AEXPORT
        { -h
        | -s server_name
        | -u user_name
        | -p password
        | -port port_no
        | -tserver server_name
        | -tport port_no
        | -nls national_language_support
        | -object user_name '.' object_name { ',' user_name '.' object_name }
        | -prefer_ipv6
        | -ssl_ca CA_file_path
        | -ssl_capath CA_dir_path
        | -ssl_cert certificate_file_path
        | -ssl_key key_file_path
        | -ssl_verify
        | -ssl_cipher cipher_list }
```
<!-- IMG_RECOVERY_END ref_id="img-06951" -->


### 파라미터

| 파라미터                           | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| \-h                                | 도움말을 출력한다.                                           |
| \-s                                | 데이터를 다운로드할 서버의 호스트 명 또는 IP 주소를 설정한다. 생략시 호스트 명 입력 프롬프트가 출력된다. IP 주소의 경우, IPv4 주소 또는 IPv6 주소를 사용할 수 있다. IPv6 주소는 “[“과 “]”로 에워싸야 한다. 예를 들어, localhost 를 명시하고자 할 때, 가능한 값은 다음과 같다. localhost (호스트 이름), 127.0.0.1 (IPv4주소), [::1] (IPv6주소) Altibase에서 IPv6 주소를 사용하는 방법에 대해서는 *Administrator’s Manual*을 참고하기 바란다. |
| \-u                                | 접속할 Altibase의 사용자명을 설정한다. 생략 시 사용자명 입력 프롬프트가 출력된다. 전체 DB 모드로 실행하려면, 이 옵션에 SYS 사용자를 지정해야 한다. 사용자 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다. -u \\"user name\\" |
| \-p                                | 접속할 Altibase 사용자의 패스워드를 설정한다. 생략시 패스워드 입력 프롬프트가 출력된다. |
| \-port                             | 접속할 Altibase의 포트번호를 설정한다. 생략 시 환경 변수 ALTIBASE_PORT_NO, altibase.properties를 차례로 참조하며 설정되어 있지 않은 경우에는 포트 번호 입력 프롬프트가 출력된다. |
| \-object                           | 추출할 객체를 소유자 이름과 함께 명시한다. 추출할 객체 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다. -object \\"user name\\".\\"table name\\" |
| \-tserver                          | 추출한 데이터를 업로드할 대상 서버를 지정한다. 이 정보는 aexport가 생성하는 쉘 스크립트 파일 안에 사용된다. -s 옵션과 마찬가지로 호스트 이름, IPv4 주소 또는 IPv6 주소 모두 가능하다. |
| \-tport                            | 접속할 대상 서버의 포트번호를 설정한다. 이 정보는 aexport가 생성하는 쉘 스크립트 파일 안에 사용된다. |
| \-nls_use                          | 데이터베이스에 데이터 저장 또는 데이터 추출 시에 사용되는 클라이언트 캐릭터 셋을 지정한다 (US7ASCII, KO16KSC5601, MS949, BIG5, GB231280, MS936, UTF8, SHIFTJIS, MS932, EUCJP). 생략 시 환경 변수 ALTIBASE_NLS_USE, altibase.properties를 차례로 참조하며, 설정되지 않았을 경우에는 데이터베이스 캐릭터 셋을 사용한다. |
| \-prefer_ipv6                      | \-s 옵션으로 호스트 이름을 입력했을 때, 접속할 IP 주소의 버전을 결정하는 옵션이다. 이 옵션을 명시하면, 호스트 이름을 IPv6 주소로 바꾸어 접속한다. 이 옵션을 명시하지 않으면, isql은 IPv4 주소로 접속한다. 선호하는 버전의 IP 주소로의 접속이 실패하면, 다른 IP 버전 주소로 접속을 다시 시도한다. 예를 들어, -S 옵션에 “localhost”를 입력하고 이 옵션을 명시하면, isql 은 처음에 IPv6 주소인 [::1]로 접속하고, 이 접속이 실패하면 IPv4 주소인 127.0.0.1로 접속을 다시 시도한다. |
| \-ssl_ca *CA_file_path*            | 접속할 Altibase 서버의 공개키(public key)가 포함된 CA(인증 기관, Certification Authority) 인증서 파일의 위치를 지정한다. |
| \-ssl_capath *CA_dir_path*         | 접속할 Altibase 서버의 공개키가 포함된 CA 인증서 파일이 저장되어 있는 디렉토리를 지정한다. |
| \-ssl_cert *certificate_file_path* | 클라이언트 인증서 파일의 위치를 지정한다.                    |
| \-ssl_key *key_file_path*          | 클라이언트 개인키 파일의 위치를 지정한다.                    |
| \-ssl_verify                       | 이 옵션을 지정하면 클라이언트가 서버로부터 전달받은 인증서를 검증한다. |
| \-ssl_cipher *cipher_list*         | SSL 암호화를 위해 사용할 알고리즘의 이름 후보들을 지정한다. General Reference에서 SSL_CIPHER_LIST 프로퍼티를 참고한다. |

> SSL 접속에 대한 자세한 설명과 예제는 *iSQL User's Manual*의 '접속 연결 및 해제'를 참조하기 바란다.



### 수행 절차

aexport를 사용한 데이터베이스 마이그레이션 절차는 크게 다음과 같이 분류된다.

-   원본 데이터베이스로부터 구조 추출

-   원본 데이터베이스로부터 데이터 추출

-   대상 데이터베이스에 데이터베이스 구조 생성

-   대상 데이터베이스에 데이터 로딩

-   대상 데이터베이스에 Materialized View를 리프레쉬한 다음, 인덱스와 외래키 생성, 접근 모드 변경

##### 데이터베이스 구조 추출

aexport를 사용하여 데이터베이스 구조를 추출한다.

- aexport를 수행한다.

  ```
  $ aexport –s 127.0.0.1 –u sys –p manager
  ```


-   Altibase 데이터베이스 사용자의 암호를 입력한다. (대상 데이터베이스에서 각 사용자가 사용하게 될 암호)
    
- 원격지에 있는 Altibase의 데이터를 aexport를 이용하여 백업을 할 때에는 원격지 서버의 주소와 포트(PORT)를 명시한다.
  
  ```
  $ aexport –s 222.112.84.200 –port 20300 –u sys –p manager
  ```


##### 데이터 추출

aexport에 의하여 생성된 쉘 스크립트를 실행하여 테이블 데이터를 추출한다.

-   현재 작업중인 디스크에 충분한 공간이 있는지 확인한다. 텍스트 데이터의 경우 데이터베이스 내부 자료 형태보다 더 많은 용량을 차지할 수 있기 때문에 데이터 파일 사이즈의 두 배 가량의 여유공간 확보를 권장한다.
    
- "run_il_out.sh" 스크립트를 수행한다.

  ```
  $ sh run_il_out.sh
  ```


##### 대상 데이터베이스에 데이터베이스 구조 생성

-   aexport와 “run_il_out.sh”에 의해 생성된 모든 SQL 스크립트와 쉘 스크립트, 그리고 확장자가 “fmt”, “log”, “dat”인 파일을 대상 데이터베이스가 존재하는 시스템으로 복사한다. 대상 데이터베이스가 동일한 시스템에 존재하는 경우 이 과정은 생략한다.
    
-   대상 데이터베이스를 구동시킨다.

-   “run_is.sh” 스크립트를 수행한다.

\$ sh run_is.sh

-   iSQL로 데이터베이스에 접속하여 데이터베이스 구조가 올바르게 생성되었는지 확인한다. 만약, 데이터베이스 구조가 올바르게 생성되지 않았다면, run_is.sh 수행 당시의 화면출력을 검사하여 문제를 파악한다.

##### 대상 데이터베이스에 데이터 로딩

- “run_il_in.sh” 스크립트를 수행한다.

  ```
  $ sh run_il_in.sh
  ```


-   ‘run_il_in.sh’ 디렉토리에서 확장자가 “bad”인 파일들 중 사이즈가 0이 아닌 파일이 있는지 검사한다. 해당 파일이 있을 경우 해당 테이블에 관련된 log 파일 및 bad 파일의 내용을 검사하여 조치한다. 이에 관련된 자세한 사항은 *iLoader User’s Manual*을 참조한다.

##### 대상 데이터베이스에 Materialized View를 리프레쉬한 다음, 인덱스 및 외래키 생성, 접근 모드 변경

TWO_PHASE_SCRIPT 프로퍼티가 OFF일 때,

- “run_is_refresh_mview.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_refresh_mview.sh
  ```


- “run_is_index.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_index.sh
  ```


- “run_is_fk.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_fk.sh
  ```


- “run_is_alt_tbl.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_alt_tbl.sh
  ```


TWO_PHASE_SCRIPT 프로퍼티가 ON일 때,

- “run_is_con.sh” 스크립트를 수행한다.

  ```
  $ sh run_is_con.sh
  ```




### 주의 사항

-   SYS 사용자가 아닌 일반 사용자로 aexport를 실행할 경우 해당 사용자가 생성한 스키마에 대해서만 스크립트를 생성한다.
    
-   SYS 사용자가 아닌 일반 사용자로 aexport를 실행할 경우 이중화 객체는 생성되지 않는다.
    
-   일반 사용자로 aexport를 실행할 경우 테이블 생성 권한이 필요하다. aexport는 객체간 의존성 분석을 위해 임시 테이블을 생성하기 때문이다.
    
-   동시에 여러 개의 aexport 프로세스를 실행하면 안 된다. aexport는 생성된 SQL 스크립트를 저장하기 위해 임시 테이블을 사용하기 때문에, 동시에 두 개 이상의 aexport 프로세스를 실행하면 예상치 못한 결과가 나올 수 있다.
    
-   EXECUTE와 TWO_PHASE_SCRIPT 프로퍼티를 ON 으로, OPERATION 프로퍼티를 IN으로 설정하고 데이터를 업로딩할 때는, INDEX 프로퍼티 값의 영향을 받지 않는다. 이는 인덱스만 생성하는 SQL 스크립트가 따로 생성되지 않기 때문이다.  
    그러므로 INDEX 프로퍼티를 ON으로 업로딩 작업 (EXECUTE=ON and OPERATION=IN)을 하려면, TWO_PHASE_SCRIPT 프로퍼티를 OFF로 해야 한다.
    
-   “run_is.sh” 스크립트 구동 시 기존에 있는 모든 사용자 및 객체를 삭제하므로, 소스 데이터베이스에서 해당 스크립트를 수행하지 않도록 주의해야 한다.
    
- 파라미터 -s, -p는 일반적으로 서버에 접속하기 위한 용도뿐 아니라 스크립트에서도 함께 사용된다. 그러나 -tserver, -tport와 함께 사용될 경우에는 –s와 –p는  데이터를 다운로드 할 서버에 접속하는 용도로만 사용되고, 대상 데이터베이스에 대해 수행할 스크립트에는 –tserver와 –tport로 명시한 값들이 사용된다.
  
  ```
  $ aexport -s 127.0.0.1 -u sys -p manager -tserver 192.168.1.10 –tport 21300
  
  $ cat run_il_in.sh
  
  iloader -s 192.168.1.10 -port 21300 -u SYS -p MANAGER in -f SYS_T1.fmt -d
  SYS_T1.dat -log SYS_T1.log -bad SYS_T1.bad
  ```


-   사용자 생성 시 PASSWORD_VERIFY_FUNCTION을 사용해서 콜백 함수를 지정했다면, 사용자를 import 하기 전에 사용자의 패스워드를 검증 함수에 부합하도록 설정해야 한다. 또한 대상 데이터베이스에 사용자를 import 하기 전에 검증 함수를 먼저 import 해야 한다.
    
-   사용자 이름 또는 추출할 객체 이름에 소문자, 특수 문자 또는 공백이 포함된 경우 큰 따옴표를 사용해야 한다.



### aexport의 한계

-   저장 프로시저 생성 시 참조해야 할 저장 프로시저가 미리 생성되어 있지 않으면 작업이 실패하게 된다. aexport는 저장 프로시저 간의 의존성에 대한 정보에 접근할 수가 없기 때문에 저장 프로시저 생성 순서를 보장할 수 없다. 이런 경우 저장 프로시저 생성에 실패할 수 있기 때문에 대상 데이터베이스에 저장 프로시저를 수동으로 생성해야 한다.
    
-   aexport는 시퀀스의 메타 정보에 제한적인 접근만이 가능하다. 이러한 제약 때문에 SYS 사용자 이외의 계정에서 생성한 시퀀스의 경우 INCREMENT BY에 의해서 지정된 시퀀스 특성만 반영이 되고 나머지 특성은 기본 값으로 설정된다. 이러한 제약사항이 문제가 되는 경우 시퀀스를 대상 데이터베이스에 수동으로 생성해야 한다.
    
-   대상 데이터베이스에 객체를 생성하는 과정에서, Material View 생성 전에 기반 테이블이 미리 생성되어 있어야 한다. aexport는 materialized view 생성을 위한 테이블 생성 순서를 보장하지 않기 때문에, materialized view 생성에 실패할 수도 있다. 이 경우, 사용자가 수동으로 materialized view를 생성해야 한다.
    
-   aexport 가 원본 데이터베이스에서 materialized view 생성 구문을 추출할 때, 최초로 그 materialized view를 생성했던 구문을 가져온다. 즉, 원본 데이터베이스에서 materialized view에 대해서 refresh 방법 또는 refresh 변경 시기를 변경하는 DDL문을 수행하더라도 aexport가 추출하는 구문에는 해당 변경사항이 반영되지 않는다.



### SSL 접속과 스크립트 파일

-   SSL 접속으로 aexport를 실행하는 경우, 원본 데이터베이스 접속용 스크립트(run_il_out.sh) 파일에는 aexport를 실행할 때 사용한 SSL 옵션이 그대로 적용된다.
    
-   대상 데이터베이스에 SSL 접속을 원한다면 프로퍼티 파일에 SSL 관련 프로퍼티를 설정해야 한다. 자세한 설명은 aexport 프로퍼티 절의 SSL_ENABLE 프로퍼티를 참조하기 바란다.




### aexport 프로퍼티

##### aexport 프로퍼티 설정

aexport.properties 파일의 프로퍼티 값을 조정해야 한다. 이 파일은 \$ALTIBASE_HOME/conf 디렉터리에 있어야 한다 (같은 디렉터리의 altibase.properties 파일과 혼동하지 말 것). 이 파일이 없으면 aexport는 구동되지 않는다.

Altibase를 설치할 때, aexport.properties 파일은 \$ALTIBASE_HOME/conf에 존재하지 않는다. 다만, 같은 디렉터리에 aexport.properties.sample이라는 이름의 샘플 파일을 제공하는데, 이 파일을 aexport.properties이름으로 복사한 후, 수정해서 사용하면 된다.

##### aexport 프로퍼티

-   OPERATION  
    OPERATION = IN/OUT  
    OUT으로 설정할 경우, 모든 스키마와 데이터를 추출할 수 있는 스크립트가 생성된다. 데이터 추출 스크립트(iLoader 실행 명령어로 구성)를 실행하면 form
    파일(.fmt)과 데이터 파일(.dat)이 만들어진다.  
    IN으로 설정할 경우, OUT에서 생성된 스키마 생성 스크립트와 데이터 로딩 스크립트를 실행하여 대상 데이터베이스에 스키마를 만들고 데이터를 입력한다. 스키마 생성 스크립트와 데이터 입력 스크립트는 aexport를 실행하지 않고 쉘 프롬프트에서 수동으로 실행할 수도 있다.
    
-   EXECUTE  
    생성한 스크립트를 자동으로 수행할 것인지 여부를 설정한다.  
    EXECUTE = ON/OFF  
    ON일 경우 OPERATION 에 지정된 작업에 맞는 적절한 스크립트 파일을 자동으로 실행한다. 스크립트 파일 이름은 ILOADER_OUT, ILOADER_IN, ISQL, ISQL_CON, ISQL_INDEX, ISQL_FOREIGN_KEY, ISQL_REPL, ISQL_REFRESH_MVIEW, 그리고 ISQL_ALT_TBL 프로퍼티로 설정된다.  
    OFF일 경우 스크립트를 생성하기만 하고 실행하지는 않는다.
    
-   INVALID_SCRIPT  
    이 프로퍼티는 유효하지 않은 객체들을 생성하는 SQL 스크립트를 하나의 스크립트 파일에 모을 것인지 여부를 결정한다.  
    INVALID_SCRIPT = ON/OFF  
    ON 일 때, INVALID.sql 파일이 생성된다. 이 파일은 유효하지 않은 뷰와 저장 프로시저를 생성하는 모든 SQL 스크립트를 포함한다.  
    OFF이면, 유효하지 않은 각 객체를 생성하는 SQL 스크립트가 따로 생성된다. 즉, 유효한 객체와 같은 방식으로 다뤄진다.
    
-   TWO_PHASE_SCRIPT  
    이 프로퍼티는 객체 생성 스크립트를 두 개의 스크립트 파일로 나눠서 생성할 것인지를 결정한다.  
    TWO_PHASE_SCRIPT = ON/OFF  
    ON 일 때, 아래와 같이 두 개의 SQL 스크립트 파일과 두 개의 쉘 스크립트 파일만이 생성된다: ALL_OBJECT.sql, ALL_OBJECT_CONSTRAINS.sql, ALL_OBJECT.sql, run_is.sh, run_is_con.sh  
    OFF이면, 각 객체를 생성하는 SQL 스크립트 파일을 따로 생성한다.
    
-   CRT_TBS_USER_MODE  
    CRT_TBS_USER_MODE = ON/OFF (기본값: OFF)  
    사용자 모드에서 테이블스페이스 생성 구문을 추출할 것인지 여부를 결정한다.  
    이 프로퍼티를 ON으로 설정하면, 사용자 모드에서 해당 사용자와 관련된 테이블스페이스를 생성하는 SQL문을 추출한다. 사용자 관련 테이블스페이스는 기본 테이블스페이스, 기본 임시 테이블스페이스, 접근 가능 여부가 설정된 테이블스페이스이다.
    
-   INDEX  
    INDEX = ON/OFF  
    대상 데이터베이스에 스키마 구성 시 인덱스 포함여부를 결정한다. 데이터 로딩 후에 인덱스를 생성하고자 할 경우 이 프로퍼티를 ON으로 설정한다. TWO_PHASE_SCRIPT프로퍼티는 OFF일 때 제대로 동작한다.
    
-   USER_PASSWORD  
    USER_PASSWORD = *password*  
    원본 데이터베이스에서 추출된 사용자를 대상 데이터베이스에 생성할 때 사용할 암호를 지정한다. (aexport는 사용자 객체 추출 시 사용자의 암호를 알 수 없기 때문에 수동 설정이 필요하다.) 이 프로퍼티가 설정되어 있지 않을 경우 각 사용자의 암호를 묻는 프롬프트가 나타난다.
    
-   VIEW_FORCE  
    VIEW_FORCE = ON/OFF  
    ON이면, 뷰의 기본 테이블 등이 존재하지 않아도 뷰를 강제로 생성한다.
    
-   DROP  
    생성 스크립트 내부에 DROP 구문을 포함할 것인지 여부를 결정한다.  
    DROP = ON/OFF  
    ON이면, 객체를 제거하는 구문이 SQL 스크립트에 포함되어 대상 데이터베이스 내에 이미 객체가 존재할 경우 기존 객체를 제거하게 된다. 기존 객체를 삭제하기 때문에 사용에 주의를 요한다.  
    
    > 주의: 객체 모드로 실행하면, 이 프로퍼티 값에 상관없이 DROP 구문이 생성되지 않는다.
    
-   ILOADER_OUT  
    ILOADER_OUT = *run_il_out.sh*  
    원본 데이터베이스에서 데이터를 추출하기 위해 생성되는 쉘 스크립트 파일명을 설정한다. OPERATION 프로퍼티를 OUT으로 설정할 경우에 사용된다.
    
-   ILOADER_IN  
    ILOADER_IN = *run_il_in.sh*  
    대상 데이터베이스에 데이터 로딩을 위해 사용될 쉘 스크립트의 파일명을 설정한다.
    
-   ISQL  
    ISQL = *run_is.sh*  
    대상 데이터베이스에 데이터베이스 스키마를 구성하기 위한 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다.
    
-   ISQL_CON  
    ISQL\_ CON = *run_is_con.sh*  
    대상 데이터베이스에 인덱스, 외래키, 트리거와 이중화 객체를 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. TWO_PHASE_SCRIPT 프로퍼티가 ON일 때 사용된다.
    
-   ISQL_INDEX  
    ISQL_INDEX = *run_is_index.sh*  
    대상 데이터베이스에 인덱스를 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   ISQL_FOREIGN_KEY  
    ISQL\_ FOREIGN_KEY = *run_is_fk.sh*  
    대상 데이터베이스에 외래키 생성하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   ISQL_REPL  
    ISQL_REPL = *run_is_repl.sh*  
    대상 데이터베이스에 이중화를 생성하기 위한 쉘 스크립트의 파일명을 설정한다. 이 프로퍼티를 설정하지 않으면 쉘 스크립트 파일은 생성되지 않는다.
    
-   COLLECT_DBMS_STATS  
    이 프로퍼티는 사용자의 테이블, 칼럼, 인덱스의 통계 정보를 추출할지 여부를 결정한다.  
    COLLECT_DBMS_STATS = ON/OFF  
    기본값은 OFF이며 통계 정보를 추출하지 않는다. 이 프로퍼티의 값을 ON으로 할 경우 통계 정보를 추출하도록 한다.
    
-   ISQL_REFERSH_MVIEW  
    ISQL_REFERSH_MVIEW = *run_is_refresh_mview.sh*  
    대상 데이터베이스의 Materialized View를 리프레쉬하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면, 쉘 스크립트 파일이 생성되지 않는다.
    
-   ISQL_ALT_TBL  
    ISQL_ALT_TBL = *run_is_alt_tbl.sh*  
    대상 데이터베이스의 테이블과 파티션에 대한 접근 모드를 변경하는 SQL 스크립트를 실행하는 쉘 스크립트 파일의 이름을 설정한다. 이 프로퍼티를 설정하지 않으면, 쉘 스크립트 파일이 생성되지 않는다.
    
-   ILOADER_FIELD_TERM  
    ILOADER_FIELD_TERM = *field_term*  
    테이블의 데이터를 텍스트로 다운로드 할 때 사용할 필드 구분자를 설정한다. 설정하지 않을 경우 기본값은 쉼표(,)로 구분되며, 숫자는 그대로, 문자형 칼럼은 큰 따옴표(“”)로 에워싸여서 출력된다.  
    
    > 주의: 프로퍼티 파일 내에서 \# 문자를 구분자로 사용할 경우, \# 이하를 주석으로 처리하기 때문에, \#는 구분자로 사용할 수 없다.
    
-   ILOADER_ROW_TERM  
    ILOADER\_ ROW \_TERM = *row_term*  
    테이블 데이터를 텍스트로 내릴 때 사용할 레코드 구분자를 설정한다. 설정하지 않을 경우 기본값은 \<LF\>이다.  
    
    > 주의: 프로퍼티 파일 내에서 \# 문자를 구분자로 사용할 경우, \# 이하를 주석으로 처리하기 때문에, \#는 구분자로 사용할 수 없다.
    
- ILOADER_PARTITION  

  이 프로퍼티는 원본 데이터베이스에 파티션 테이블이 있을 경우, iLoader 스크립트를 파티션 별로 생성할 것인지 결정한다.  
  ILOADER\_PARTITION = ON/OFF  

  이 값이 ON일 경우, run_il_out.sh에 각 파티션마다 form 파일과 데이터를 추출하는 스크립트가 생성된다. run_il_in.sh에도 파티션 별로 데이터를 로드하는 스크립트가 생성된다. 
  이 값이 OFF일 경우, 파티션드 테이블을 처리하는 스크립트도 넌파티션드 테이블과 동일하게 하나의 데이터 파일을 이용하여 추출·입력하도록 생성된다.
  ILOADER 관련 프로퍼티에 대한 더 자세한 설명은 *iLoader User’s Manual* 을 참고하기 바란다.

-   ILOADER_ERRORS  
    ILOADER_ERRORS = *count* (기본값: 50)  
    iLoader로 데이터를 업로드할 때 허용 가능한 최대 에러 개수를 지정한다. 이 프로퍼티의 기본값은 50이며, 0으로 설정하면 발생하는 에러 개수와 무관하게 업로드가 계속 실행된다.
    
-   ILOADER_ARRAY  
    ILOADER_ARRAY = *count* (기본값: 1)  
    iLoader로 데이터를 다운로드 또는 업로드 할 때 한 번에 처리할 row 개수를 지정한다.
    
-   ILOADER_COMMIT  
    ILOADER_COMMIT = *count* (기본값: 1000)  
    iLoader로 데이터를 업로드할 때 커밋할 단위(개수)를 지정한다. 이 프로퍼티로 -commit옵션의 값을 지정할 수 있다.
    
-   ILOADER_PARALLEL  
    ILOADER_PARALLEL = *count* (기본값: 1)  
    iLoader로 데이터를 다운로드 또는 업로드 할 때 병렬로 처리할 쓰레드 개수를 지정한다.
    
-   ILOADER_ASYNC_PREFETCH  
    ILOADER_ASYNC_PREFETCH = OFF\|ON\|AUTO (기본값 OFF)  
    iLoader로 데이터를 다운로드할 때 비동기 prefetch 동작을 설정한다. 자세한 설명은 iLoader User's Manual의 '-async_prefetch' 옵션을 참고하기 바란다.
    
-   SSL_ENABLE  
    대상 데이터베이스에 SSL 프로토콜로 접속할 것인지 여부를 지정한다.  
    SSL_ENABLE = ON/OFF  
    ON이면 대상 데이터베이스에 실행하는 쉘 스크립트(run_is.sh, run_il_in.sh) 내의 isql, iloader 명령에 SSL 관련 옵션이 지정된다.  
    SSL 관련 옵션 값은 프로퍼티(SSL_CA, SSL_CAPATH, SSL_CERT, SSL_KEY, SSL_CIPHER, SSL_VERIFY)로 명시할 수 있다. 각 프로퍼티의 역할은 aexport 접속 파라미터와 동일하므로 해당 절을 참조한다. SSL_ENABLE 프로퍼티 설정에 대한 예제는 SSL 프로퍼티 설정을 참고한다.
    
-   ILOADER_GEOM = WKB
    iLoader로 공간 데이터를 다운로드 할 때, 공간 데이터를 Well-Known Binary (WKB)  포맷으로 처리하도록 지정하는 옵션이다. run_il_out.sh 파일에 -geom WKB 옵션이 추가된다.



### 사용 예제

##### 전체 DB 모드로 실행

```
$ aexport -s 127.0.0.1 -u sys -p manager
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TBS #####
##### USER  #####
##### SYNONYM #####
##### DIRECTORY #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
##### REPLICATION #####
##### JOB #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
ALL_ALT_TBL.sql 
ALL_CRT_DIR.sql
ALL_CRT_FK.sql
ALL_CRT_INDEX.sql
ALL_CRT_JOB.sql
ALL_CRT_LIB.sql
ALL_CRT_LINK.sql
ALL_CRT_REP.sql
ALL_CRT_SEQ.sql
ALL_CRT_SYN.sql
ALL_CRT_TBL.sql
ALL_CRT_TBS.sql
ALL_CRT_TRIG.sql
ALL_CRT_USER.sql
ALL_CRT_VIEW_PROC.sql
ALL_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh
```



##### 사용자 모드로 실행

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
$ aexport -s 127.0.0.1 -u user1 -p user1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### USER #####
##### SYNONYM #####
##### TABLE #####
##### QUEUE #####
##### SEQUENCE #####
##### DATABASE LINK #####
##### VIEW #####
##### MATERIALIZED VIEW #####
##### STORED PROCEDURE #####
##### STORED PACKAGE #####
##### TRIGGER #####
##### LIBRARY #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------

$ ls -l
USER1_ALT_TBL.sql
USER1_CRT_DIR.sql
USER1_CRT_FK.sql
USER1_CRT_INDEX.sql
USER1_CRT_LIB.sql
USER1_CRT_LINK.sql
USER1_CRT_SEQ.sql
USER1_CRT_SYN.sql
USER1_CRT_TBL.sql
USER1_CRT_TRIG.sql
USER1_CRT_USER.sql
USER1_CRT_VIEW_PROC.sql
USER1_REFRESH_MVIEW.sql
run_il_in.sh
run_il_out.sh
run_is.sh
run_is_alt_tbl.sh
run_is_fk.sh
run_is_index.sh
run_is_job.sh
run_is_refresh_mview.sh
run_is_repl.sh

```



##### 객체 모드로 실행

```
iSQL> CREATE USER user1 IDENTIFIED BY user1;
Create success.
iSQL> CONNECT user1/user1;
iSQL> CREATE TABLE t1(i1 INTEGER);
Create success.
iSQL> CREATE VIEW v1 AS SELECT i1 FROM t1;
Create success.
iSQL> CREATE MATERIALIZED VIEW m1 AS SELECT * FROM t1;
Create success.
iSQL> CREATE OR REPLACE PROCEDURE proc1(p1 IN INTEGER)
AS a INTEGER;
BEGIN
SELECT * INTO a FROM t1 WHERE i1 = 1;
END;
/
Create success.

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
$ ls
user1_t1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.m1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### MATERIALIZED VIEW #####
$ ls
user1_m1_CRT.sql

$ aexport -s 127.0.0.1 -u user1 -p user1 -object user1.t1,user1.v1,user1.proc1
-----------------------------------------------------------------
    Altibase Export Script Utility.
    Release Version 7.1.0.0.0
    Copyright 2000, ALTIBASE Corporation or its subsidiaries.
    All Rights Reserved.
-----------------------------------------------------------------
##### TABLE #####
##### VIEW #####
##### STORED PROCEDURE #####
$ ls
user1_proc1_CRT.sql
user1_t1_CRT.sql
user1_v1_CRT.sql

```



##### SSL 프로퍼티 설정

```
SSL_ENABLE = ON  # OFF
SSL_CA     = ${ALTIBASE_HOME}/cert/ca-cert.pem
#SSL_CAPATH = ${ALTIBASE_HOME}/cert
SSL_CERT   = ${ALTIBASE_HOME}/cert/client-cert.pem
SSL_KEY    = ${ALTIBASE_HOME}/cert/client-key.pem
SSL_CIPHER = RC4-SHA:RC4-MD5
SSL_VERIFY = ON  # OFF
```





# 2.altiComp

이 장은 altiComp 유틸리티의 기능을 소개하고, 불일치하는 데이터를 비교하고 일치시키는 기능 등을 설명한다.

## altiComp 소개

Altibase altiComp 유틸리티는 두 Altibase 간의 이중화 중에 발생한 데이터 불일치를 해결하기 위해 사용한다.

altiComp은 Altibase 데이터베이스를 또 다른 Altibase 데이터베이스와 테이블 단위로 비교, 검사하여 불일치 정보를 출력한다. 또한 불일치 데이터가 발생한 경우에는 두 데이터베이스를 일치시키는 기능도 제공한다.

### altiComp 용어

##### Master Server

두 서버 간의 불일치 레코드 발견 시 수정을 하는 기준이 되는 서버이다. altiComp 실행 시 어느 쪽 서버도 master로 지정될 수 있다.

##### Master DB

Master Server의 데이터베이스이다.

##### Slave Server

두 서버 간의 불일치 레코드 발견 시 기준 데이터베이스에 따라서 수정이 되는 쪽 서버이다. altiComp 실행 시 어느 쪽 서버도 slave로 지정될 수 있다.

##### Slave DB

Slave Server의 데이터베이스이다.

### 불일치 레코드(Different Record) 

Master DB의 지정 테이블과 Slave DB의 지정 테이블간에 주요 키(Primary Key)를 기준으로 칼럼 값이 일치하지 않는 레코드를 의미한다.

불일치 레코드가 발생하는 이유는 다음의 세 가지 경우이다.

-   MOSX 불일치: 특정 레코드가 주요 키를 기준으로 Master DB에는 있으나, Slave DB에는 없는 경우
    
-   MOSO 불일치: 특정 레코드가 주요 키를 기준으로 Master DB와 Slave DB에도 있지만, 레코드의 내용이 다른 경우
    
-   MXSO 불일치: 특정 레코드가 주요 키를 기준으로 Master DB에는 없고, Slave DB에는 있는 경우

### 일치 정책(Synchronization Policy) 

일치 정책은 불일치 레코드를 일치시키는 방법을 명시하는 정책이다. altiComp 프로그램은 기본적으로 Master DB를 기준 DB로 고정하고, Slave DB를 일치시키는 정책을 채택하고 있다.

Altibase는 일치 정책으로 다음과 같은 네 가지 방법을 제공한다.

-   SU 정책: MOSO 불일치를 해소하는 정책으로, Master DB의 레코드 내용으로 Slave DB를 변경(update)한다.
    ![](media/Utilities/su_policy.gif)
-   SI 정책: MOSX 불일치를 해소하는 정책으로, Master DB의 레코드를 Slave DB에 삽입(insert)한다.
    ![](media/Utilities/si_policy.gif)
-   MI 정책: MXSO 불일치를 해소하는 정책으로. Slave DB의 레코드를 Master DB에 삽입(insert)한다.
    ![](media/Utilities/mi_policy.gif)
-   SD 정책: MXSO 불일치를 해소하는 정책으로, Slave DB의 레코드를 삭제(delete)한다.
    ![](media/Utilities/sd_policy.gif)

SU정책, SI정책, MI정책, SD정책은 사용자가 altiComp 환경 파일을 사용하여 지정할 수 있다. 단, MI정책과 SD정책은 서로 배타적이므로, 동시에 지정할 수 없다는 것을 주의하라.

##### DIFF

Master DB와 Slave DB간의 이중화 작업에서 발생할 수 있는 불일치 레코드를 식별하여 실행 결과 파일로 생성하는 기능을 가진다.

##### SYNC

Master DB와 Slave DB 사이의 불일치 레코드를 식별하여 altiComp 환경 파일에 기술된 일치 정책에 따라 양방향으로 반영하여 불일치를 해소하고, 실행 요약정보와 에러 정보를 포함하는 실행 결과 파일을 생성한다.

##### altiComp 환경 파일

altiComp를 실행하기 위한 옵션을 지정하는 환경 파일이다. 이 파일은 연결정보, altiComp 기능 설정, 일치 정책 등의 내용을 포함한다.



## altiComp 사용 방법

이 절에서는 altiComp을 실행하기 위한 정보를 기술하는 altiComp 환경 파일을 먼저 설명하고, 비교(DIFF)와 일치(SYNC) 기능에 대해 설명한다.

### altiComp 실행 방법

altiComp 기능을 사용하기 위해서는 먼저 DIFF 또는 SYNC를 수행할 테이블에 대한 정보를 가지고 있는 altiComp 환경 파일을 만들어야 한다. altiComp 환경 파일은 운용 방법의 altiComp 환경 파일에서 설명한다.

altiComp 명령은 다음과 같은 형태를 갖는다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

현재 디렉토리가 /user/charlie/altibase_home/altiComp 라면

```
/user/charlie/altibase_home/altiComp> altiComp script_file_name
```

또는

```
/user/charlie/altibase_home/altiComp> altiComp  ./script_file_name
```



### altiComp 프로퍼티 설정

비교 또는 일치 작업의 내용을 기술하는 환경 파일로, 각각의 고유한 프로퍼티를 포함한다. 프로퍼티는 altiComp 유틸리티 실행에 필요한 정보를 기술한다. (\$ALTIBASE_HOME/ altiComp 디렉터리 밑에 제시된 sample.cfg 참조)

##### 설정 규칙

프로퍼티는 “**프로퍼티 이름 = 프로퍼티 값**”의 형식으로 구성되며, 대소문자 구분이 없다.

환경 파일은 다음과 같은 특별한 의미를 가지는 기호를 포함할 수 있다.

-   “ **\#** “ 기호는 주석(comment)으로 이후의 문자열은 무시된다.

-   “ **{ }** “ 기호는 프로퍼티 값을 여러 줄로 기술하기 위한 목적으로 사용된다.

-   “ **;** “ 기호는 여러 개의 값을 분리하기 위한 구분자 역할을 한다.

-   “ **“** “ 기호: 사용자 이름, 비밀번호 또는 테이블 이름, 칼럼 이름에 예약어 또는 특수 문자가 포함되어 있다면, 이 기호로 해당 문자열을 감싸준다. Altibase에서 특수 문자는 \~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \| 이다.

##### 프로퍼티 이름

공백이 없는 문자로 구성되며, 프로퍼티 그룹 내에서 식별하도록 하는 이름이다.

##### 프로퍼티 값

단일 값(single value), 다중 값(multi value) 또는 표현식(expression)을 가질 수 있다.

-   표현식은 공백이 가능하며, 대부분의 프로퍼티는 이 형태의 값을 가진다.
    예) TABLE = EMPLOYEE

-   다중 값은 “**;**” 분리자로 구분되는 여러 개의 단일 값을 가지며, 특히 여러 줄에 기술할 때는 “{ }” 기호 안에 값을 기술한다(예2). 다중 값이 허용되는 프로퍼티는 EXCLUDE 이다.
    예) EXCLUDE = ENO; DNO; ENAME 또는 EXCLUDE = {ENO; DNO; ENAME}
    
-   표현식은 공백을 포함한 문자열을 표현하기 위한 것이며, 반드시 “{ }” 기호 안에 기술되어야 한다. 표현식을 가지는 프로퍼티는 WHERE 이다.
    예) WHERE = { ENO \> ‘1000’ and ENO \< ‘2000’ }

##### 데이터 타입 지원

altiComp 대상에서 특정 칼럼을 제외시키려면 프로퍼티 EXCLUDE를 다음과 같이 사용한다.

예) EMP 테이블에 CLOB 칼럼이 존재할 때, 해당 칼럼을 altiComp 대상에서 제외한다.

TABLE = EMP
EXCLUDE = { CCC }



### 프로퍼티 옵션

altiComp 유틸리티는 아래의 프로퍼티로 Local Server와 Remote Server의 접속 정보 및 비교(DIFF) 작업, 일치(SYNC)작업, 불일치 레코드에 대한 일치 정책을 지정할 수 있다.

##### DB_MASTER

두 서버 간의 불일치 레코드 발견 시 데이터 수정의 기준으로 하려는 서버를 지정한다.

값은 사용자명, 패스워드, 서버의 IP 주소 또는 서버명, NLS_USE 를 지정한다. 각 프로퍼티의 값은 Altibase 홈 디렉터리의 프로퍼티 파일에 있는 정보와 일치하여야 한다.

- TCP 접속:

  ```
  DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=20300;NLS_USE=US7ASCII
  ```

-   SSL 접속:

    ```
    DB_MASTER = altibase://sys:manager@DSN=192.188.1.1;PORT_NO=${ALTIBASE_SSL_PORT_NO};NLS_USE=US7ASCII;CONNTYPE=6;SSL_CA=/home/altibase/cert/ca-cert.pem;SSL_CERT=/home/altibase/cert/client-ert.pem;SSL_KEY=/home/altibase/cert/client-key.pem
    ```


연결 문자열의 SSL 관련 속성은 SSL/TLS User's Guide를 참고하기 바란다.

##### DB_SLAVE

상대 서버를 지정한다.

값은 사용자명, 패스워드, 서버의 IP 주소 또는 서버명, NLS_USE 를 지정한다. 프로퍼티 값은 Altibase 홈 디렉터리의 프로퍼티 파일에 있는 정보와 일치하여야 한다.

##### OPERATION

비교 작업을 하는 경우에는 “DIFF”를, 일치 작업을 하는 경우에는 “SYNC”를 지정한다.

##### INSERT_TO_SLAVE

MOSX 불일치에 대한 SI정책을 지정. 해당 레코드의 Slave DB에 삽입(insert) 여부를 결정한다. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삽입하고, “OFF”이면 삽입하지 않는다.

##### INSERT_TO_MASTER

MXSO 불일치에 대한 MI정책을 지정. 해당 레코드의 Master DB에 삽입(insert) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삽입하고, “OFF”이면 삽입하지 않는다.

DELETE_IN_SLAVE 프로퍼티 값과 동시에 “ON”을 가질 수 없다.

##### DELTE_IN_SLAVE

MXSO 불일치에 대한 SD정책을 지정. 해당 레코드의 Slave DB에서 삭제(delete) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 삭제하고, “OFF”이면 삭제하지 않는다.

INSERT_TO_MASTER 프로퍼티 값과 동시에 “ON”을 가질 수 없다.

##### UPDATE_TO_SLAVE

MOSO 불일치에 대한 SU정책을 지정. 해당 레코드의 Slave DB에서 수정(update) 여부를 결정. 프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 수정하고, “OFF”이면 수정하지 않는다.

##### CHECK_INTERVAL

테이블에 대하여 SYNC 작업을 한 후 다음 테이블의 SYNC 작업을 하기 전에 지정한 시간만큼 간격을 둔다. 단위는 MS(Millisecond)이다.

##### MAX_THREAD

운영하기 위한 쓰레드의 개수를 지정한다. 작업하려는 쓰레드의 개수를 제한 없이 사용하려면 “-1”을 명시한다.

##### COUNT_TO_COMMIT

변경된 데이터(Insert, Delete, or Update)를 몇 건 단위로 커밋할 것인가를 나타내는  단위 옵션이다. 기본값은 1000건 단위로 커밋한다.

##### FILE_MODE_MAX_ARRAY

이 값이 1보다 크면 작업 대상 테이블의 데이터를 파일에 저장한 후, 파일의 데이터에 대해서 SYNC 또는 DIFF 작업을 수행하게 된다. 이 값은 array fetch 하기 위한 array의 사이즈로 사용되고, altiComp는 지정한 값만큼의 레코드를 array fetch하여 csv 형식으로 파일에 저장한다.

이 옵션은 대용량의 테이블에 대한 altiComp 작업 성능을 향상시키기 위해 사용할 수 있으나, 대상 테이블에 LOB타입의 칼럼이 있으면 이 옵션을 사용해도 성능 향상이 미미할 수 있다.

이 옵션은 Altibase 서버간의 SYNC 또는 DIFF 작업 시에만 사용할 수 있다.

예) FILE_MODE_MAX_ARRAY = 1000

##### DIFF LOG 옵션

DIFF는 Master DB의 지정 테이블과 Slave DB의 지정 테이블간에 주요 키(Primary Key)를  기준으로 레코드 값을 비교하여 실행 결과 파일에 기록하는 작업이다. 네가지 유형의 레코드  비교 결과를 실행 결과 파일에 기록 여부를 설정할 수 있도록 각각의 프로퍼티를 제공한다.

프로퍼티 값은 “ON”, “OFF”를 가질 수 있으며, “ON”이면 기록하고, “OFF”이면 기록 하지 않는다. 프로퍼티를 지정하지 않으면 기본값에 따라 동작한다.

1. ###### LOG_EQ_MOSO

   PK를 포함한 모든 칼럼의 값이 일치하는 레코드 (EQ_MOSO)를 실행 결과 파일에  기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "OFF"로 동작한다.
   
   이 옵션은 대용량 테이블을 비교할 때, 실행 결과 파일 용량이 커질 수 있으므로 주의해서  사용해야 한다.
   
2. ###### LOG_DF_MOSO

   PK는 동일하지만 나머지 칼럼값 중 하나라도 일치하는 않는 레코드 (DF_MOSO)를  실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
   
3. ###### LOG_MOSX

   Master DB에는 있으나, Slave DB에는 없는 레코드 (MOSX) 를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   
   프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
   
4. ###### LOG_MXSO

   Master DB에는 없지만, Slave DB에는 있는 레코드 (MXSO) 를 실행 결과 파일에 기록할지 결정하는 프로퍼티이다. 
   

프로퍼티를 지정하지 않으면 "ON"으로 동작한다.
### TABLES 그룹 

실행 대상이 되는 테이블에 관련된 정보를 정의한다. 이 그룹은 실행 대상이 되는 테이블의 개수만큼 기술되어야 하며, 반드시 그룹명은 Master DB의 테이블 이름이어야 한다.

이 그룹에서 지정할 수 있는 프로퍼티는 다음과 같다.

##### WHERE

테이블의 레코드를 selection하는 조건을 지정한다. SQL 문의 WHERE 절에 기술하는 방식과 동일하게 기술한다. 다중 값을 허용하며, “;” 구분자로 여러 조건을 지정하는 것은 불가능하다. 또한 이 프로퍼티에는 주석을 달 수 없다. 비교(DIFF)와 일치(SYNC) 기능에 적용된다.

##### EXCLUDE

테이블의 레코드를 projection하는 조건을 지정한다. 프로퍼티 값은 다중 값으로 기술해야 한다. 기술된 칼럼들은 비교와 일치 작업에서 제외된다.

![](media/Utilities/e9cd168e51d8336eb99f9ba958d9688d.png)

![](media/Utilities/c8502d42132454c28fe8e7f0edd7c88b.png)

WHERE와 EXCLUDE를 적절히 조합하면, selection과 projection을 결합한 결과에 대해 altiComp 작업을 수행할 수 있다.

![](media/Utilities/3a664d250cbb847a5d4acd3acf65b5d1.png)

##### TABLE

Slave DB의 테이블 이름을 지정한다. Master DB와 Slave DB의 테이블 이름이 다른 경우에는 반드시 기술해야 하며, 비교(DIFF)와 일치(SYNC)기능에 적용된다. 생략하면 Mater DB의 테이블 이름과 동일하게 지정된다.

단, 테이블 이름은 반드시 영문 및 숫자와 해당 특수문자((공백,\~, !, \@, \#, \$, %, \^, &, \*, (, ), \_, +, \|)로 지정해야 하며, 한글은 사용할 수 없다.

##### SCHEMA

Slave Db의 테이블 스키마를 기술한다.

Slave의 접속하는 사용자의 스키마 이름과 대상 테이블의 스키마가 다른 경우에 반드시 기술해야 하며, 생략하면 Slave의 접속 사용자의 스키마를 사용하게 된다.



## 비교(DIFF) 기능

Master DB와 Slave DB 간의 이중화 작업에서 발생할 수 있는 불일치 레코드를 식별하여 실행 결과 파일로 생성하는 기능을 가진다.

### 환경 파일

altiComp 환경 파일의 OPERATION 프로퍼티 값을 “DIFF”로 지정한다.

실행 옵션의 모든 프로퍼티 파일을 기술해야 하며, 테이블 그룹의 WHERE, EXCLUDE, TABLE, SCHEMA 프로퍼티를 선택적으로 기술한다.

### 실행방법

비교(DIFF)기능은 다음과 같이 실행한다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

### 실행결과

실행 결과로, 실행결과에 대한 요약 정보를 포함하는 실행 로그 파일과 테이블 별로 Master Database와 Slave Database의 내용을 비교하여 불일치가 발생한 레코드의 불일치 칼럼 내용을 포함하는 실행 결과 파일이 생성된다.

예를 들어, /user/charlie/altibase_home/altiComp \> altiComp sample.cfg 과 같이 altiComp 명령을 실행했을 때, altiComp 명령이 성공적으로 실행되면 altiComp 디렉터리 하위에는 sample.log와 각각의 테이블에 대한 “마스터 테이블-사용자명.슬레이브 테이블.log” 파일이 생성된다.

##### 실행 로그 파일

“script_file_name.log” 이름으로 생성되며 실행한 환경 파일의 내용을 출력하고, 각 TABLES 그룹의 테이블에 대한 비교(DIFF)작업의 요약 정보를 출력한다.

환경 파일의 내용은 다음과 같이 출력된다.

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX = DF, Count :          1
MXSO = DF, Count :          0
MOSO = DF, Count :          1
MOSO = EQ, Count :          1

 SCAN TPS:   20547.95
     Time:       0.00 sec
```



##### 실행 결과 파일

**“마스터 테이블-사용자명.슬레이브 테이블.log”** 이름으로 생성되며, 비교 결과를 다음과 같은 형식으로 표현한다.

```
DF[m,n]-> COL_N (Vn_M, Vn_S):PK->{ PCOL_V }
```



-   DF : 불일치 원인 (MOSX, MOSO, MXSO)

-   m : Master Server의 레코드 순서

-   n : Slave Server의 레코드 순서

-   COL_N : 비교결과 다른 값을 가지는 첫 칼럼 이름

-   Vn_M : Master Server의 해당 칼럼의 값

-   Vn_S : Slave Server의 해당 칼럼의 값

단, 데이터 타입이 LOB인 칼럼이 있는 레코드의 경우 해당 칼럼의 값이 기록되지 않는다.

### 비교(DIFF) 예제

host1의 EMP 테이블과 host2의 EMPLOYEES 테이블, 그리고 host1의 DEPARTMENTS 테이블과 host2의 DEPARTMENTS 테이블에 대해 비교(DIFF) 기능을 수행하는 예제는 다음과 같다.

##### DIFF 예제 1

DB_MASTER를 host1, DB_SLAVE를 host2로 지정하고, 각각의 테이블의 모든 레코드를 비교하는 경우에 환경설정 파일은 다음과 같다

```
DB_MASTER = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
DB_SLAVE = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = DIFF
MAX_THREAD = -1
			
DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS 

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

위 예제와 같이 Master Server(host1)의 대상 테이블 이름과 Slave Server(host2)의 대상 테이블 이름이 다를 수 있다.

##### DIFF 예제 2

EMP 테이블의 ENO 칼럼을 기준으로 selection하고, JOIN_DATE, SEX 칼럼은 비교 대상에서 제외하는 경우는 다음과 같다.

CONDITION 프로퍼티 값에 따라, 비교 대상이 되는 EMP 레코드는 “ENO가 1 이상이고 20 이하”인 레코드로 제한된다.

또한 EXCLUDE 프로퍼티 값에 따라, JOIN_DATE 와 SEX는 비교 대상에서 제외된다.

즉, 다른 모든 칼럼은 같고, JOIN_DATE와 SEX만 다르다면 레코드는 동일한 것으로 처리된다.

```
[EMP]
TABLE = EMPLOYEES
WHERE = {ENO >= 1 and ENO <= 20}
EXCLUDE = {JOIN_DATE; SEX}
[DEPARTMENTS]
```



##### DIFF 예제 3

EMP 테이블의 ENO 칼럼과 JOIN_DATE를 기준으로 selection하고, SEX 칼럼은 비교 대상에서 제외하는 경우는 다음과 같다.

```
[EMP]
TABLE = EMPLOYEES
WHERE = {(ENO >= 1 and ENO <= 20) or (JOIN_DATE >= ‘20001010’)}
EXCLUDE = {SEX}

[DEPARTMENTS]
```

WHERE 프로퍼티 값에 따라, 비교 대상이 되는 EMP 레코드는 “ENO가 1 이상이고 20 이하” 또는 “JOIN_DATE가 2000년 10월 10일 이후”인 레코드로 제한된다.

또한 EXCLUDE 프로퍼티 값에 따라, SEX는 비교 대상에서 제외된다.



## 일치(SYNC) 기능

Master DB와 Slave DB 사이의 불일치 레코드를 식별하여 altiComp 환경 파일에 기술된 일치 정책에 따라 양 방향으로 반영하여 불일치를 해소하고, 실행요약정보와 에러정보를 포함하는 실행 결과 파일을 생성한다.

### 환경 파일

altiComp 환경 파일의 OPERATION 프로퍼티 값을 “SYNC”로 지정한다.

실행 옵션의 모든 프로퍼티 파일을 기술해야 하며, 테이블 그룹의 WHERE, EXCLUDE, TABLE, SCHEMA 프로퍼티는 선택적으로 기술한다

### 실행방법

일치(SYNC)기능은 다음과 같이 실행한다.

```
$ altiComp -f script_file_name
```

script_file_name : 환경 파일의 경로명을 포함한 파일 이름

### 실행결과

실행 결과로, 실행의 요약정보를 포함하는 실행 로그 파일과 테이블 별로 Master Database와 Slave Database의 내용을 비교하여 불일치가 발생한 레코드에 대한 일치 작업의 정보를 포함하는 실행 결과 파일, 일치 작업중 발생한 에러에 관한 정보를 포함하는 에러로그 파일로 구성된다.

##### 실행 로그 파일

“script_file_name.log” 이름으로 생성되며 실행한 환경 파일의 내용을 출력하고, 각 TABLES 그룹의 테이블에 대한 일치(SYNC) 작업의 요약 정보를 출력한다.

환경 파일의 내용은 다음과 같이 출력된다.

```
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!

[TAB_2->TAB_2]
Fetch Rec In Master: 3
Fetch Rec In Slave : 2
MOSX =  -, SI 
MXSO =  -, -
MOSO =  -, SU
MXSX =  -, -

-----------------------------------------
 Operation  Type      MASTER           SLAVE
-----------------------------------------
 INSERT     Try           0               1
             Fail           0               0

 UPDATE    Try           X               1
             Fail           X               0

 DELETE    Try           X               0
             Fail           X               0
-----------------------------------------
 UPDATE    Try           0               2
             Fail           0               0
 OOP  TPS:   13698.63
 SCAN TPS:   20547.95
     Time:       0.00 sec
```

만일 실패한 레코드가 있다면, 해당 레코드는 에러로그 파일에 원인과 레코드 내용이 출력된다.

### 일치(SYNC) 예제

불일치 레코드를 해소하기 위한 일치 정책에 관련된 OPERATION와 TABLE을 지정하는 예제를 제시한다.

##### SYNC 예제 1

MOSX 불일치레코드(Master Server에는 있지만, Slave Server에는 없는 레코드)를 Slave Server에 삽입하고, MXSO 불일치 레코드 (Slave Server에는 있지만, Master Server에는 없는 레코드)는 무시한다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

MOSX 불일치 레코드를 해소하기 위해 필요한 일치 정책은 SI 정책이므로, INSERT_TO_SLAVE 프로퍼티 값을 “ON”으로 지정하였다. 또한 MXSO 불일치 레코드는 무시하므로, 필요한 일치 정책인 MI, SD 정책에 관련된 INSERT_TO_MASTER와 DELETE_IN_SLAVE 프로퍼티는 “OFF”로 지정한다.

##### SYNC 예제 2

MOSX 불일치레코드(Master Server에는 있지만, Slave Server에는 없는 레코드)를 Slave Server에 삽입하고, MXSO 불일치 레코드(Slave Server에는 있지만, Master Server에는 없는 레코드) 는 Master Server에 삽입한다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = OFF
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = ON
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

MOSX 불일치 레코드를 해소하기 위해 필요한 일치 정책은 SI 정책이므로, INSERT_TO_SLAVE 프로퍼티 값을 “ON”으로 지정한다. 또한 MXSO 불일치레코드는 Master Server에 삽입해야 하기 때문에, 필요한 일치 정책은 MI 정책이다. 따라서 이에 관련된 INSERT_TO_MASTER 프로퍼티를 “ON” 으로 지정하고, DELETE_IN_SLAVE 프로퍼티를 “OFF”로 지정한다.

##### SYNC 예제 3

Master Server와 동일하게 Slave Server를 일치시킨다고 가정하자.

```
Master Server = "altibase://sys:manager@DSN=host1;PORT_NO=10111;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=host2;PORT_NO=20111;NLS_USE=US7ASCII"
OPERATION = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[EMP]
TABLE = EMPLOYEES
SCHEMA = SYS

[DEPARTMENTS]
TABLE = DEPARTMENTS
SCHEMA = SYS
```

Master Server와 동일하게 Slave Server를 일치시키기 위해서 필요한 일치 정책은 SI정책, SD 정책이다. 따라서, INSERT_TO_SLAVE와 DELETE_IN_SLAVE 프로퍼티 값을 “ON”으로 지정하였다.

##### SYNC 예제 4

\$ALTIBASE_HOME/sample/APRE/schema 디렉터리의 schema.sql을 참조하여 지역서버 host1의 EMPLOYEES 테이블과 원격 서버 host2의 EMPLOYEES 테이블(ENO에서 16번부터 20번까지 삭제), 그리고 host1 서버의 DEPARTMENTS 테이블과 host2 서버의 DEPARTMENTS 테이블에 대해 일치(SYNC) 기능을 수행하는 간단한 예제이다.

먼저 지역서버와 원격서버에 이중화 연결을 생성한다.

지역서버의 경우(IP: 192.168.1.11)

```
iSQL> CREATE REPLICATION rep1 WITH '127.0.0.1', 56342 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

원격서버의 경우(IP: 127.0.0.1)

```
iSQL> CREATE REPLICATION rep1 WITH '192.168.1.11', 65432 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
Create Success
iSQL>
```

현재 디렉터리가 /user/charlie/altibase_home/ altiComp 이라면

```
$ vi sample.cfg
Master Server = "altibase://sys:manager@DSN=127.0.0.1;PORT_NO=20582;NLS_USE=US7ASCII"
Slave Server  = "altibase://sys:manager@DSN=192.168.1.11;PORT_NO=20582;NLS_USE=US7ASCII"

OPERATION  = SYNC
MAX_THREAD = -1

DELETE_IN_SLAVE = ON
INSERT_TO_SLAVE = ON
INSERT_TO_MASTER = OFF 
UPDATE_TO_SLAVE = ON

LOG_DIR = "./"
LOG_FILE = "sample.log"

[ EMPLOYEE S]
WHERE   = {ENO >= 1 and ENO <= 20}
TABLE   = EMPLOYEES 
SCHEMA  = SYS
[ DEPARTMENTS ]
TABLE   = DEPARTMENTS 
SCHEMA  = SYS

$ altiComp –f sample.cfg 
$ cat sample.log
INFO[ MNG ] Tread #  0 init is   OK!
INFO[ MNG ] Tread #  1 init is   OK!
INFO[ MNG ] Tread #  0 start is  OK!
INFO[ MNG ] Tread #  1 start is  OK!

[DEPARTMENTS->DEPARTMENTS]
Fetch Rec In Master: 5
Fetch Rec In Slave : 5
MOSX = NO
MXSO = NO
MOSO = SU

--------------------------------------------
 Operation  Type      MASTER           SLAVE    
--------------------------------------------
 INSERT     Try            0               0 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
--------------------------------------------
 UPDATE     Try            0               0 
            Fail           0               0 
 OOP  TPS:       0.00
 SCAN TPS:   60240.96
     Time:       0.00 sec

[EMPLOYEES->EMPLOYEES]
Fetch Rec In Master: 20
Fetch Rec In Slave : 15
MOSX = NO
MXSO = NO
MOSO = SU

-------------------------------------------
 Operation  Type      MASTER           SLAVE    
-------------------------------------------
 INSERT     Try            0               5 
            Fail           0               0 

 UPDATE     Try            X               0 
            Fail           X               0 

 DELETE     Try            X               0 
            Fail           X               0
-------------------------------------------
 UPDATE     Try            0               5 
            Fail           0               0 
 OOP  TPS:     576.04
 SCAN TPS:    2304.15
     Time:       0.01 sec
```

# 3.aku

## 개요

aku(Altibase Kubernetes Utility)는 쿠버네티스의 스테이트풀셋(Statefulset)에서 스케일링(scaling)할 때 파드(Pod)의 시작 및 종료에 따라 Altibase의 데이터를 동기화하거나 동기화 정보를 초기화하는 등의 작업을 수행할 수 있게 도와주는 유틸리티이다. 즉, aku는 파드들간의 데이터 이중화를 도와주는 유틸리티로, Altibase의 데이터 스케일아웃(scale-out) 기능은 지원하지 않는다.

> 스테이트풀셋은 데이터베이스처럼 상태 유지가 필요한 애플리케이션을 지원하기 위한 쿠버네티스의 워크로드 컨트롤러 중 하나이며, 스케일링은 파드를 생성하거나 종료하는 것을 의미한다. 파드는 컨테이너들을 담고 있는 쿠버네티스의 리소스이며, 이 컨테이너에 Altibase 서버가 실행된다. 

스테이트풀셋에서 스케일 업/다운할 때 아래의 조건에 해당하는 파드를 생성하거나 종료하고자 할 때 aku 유틸리티를 사용할 수 있다. 이때, aku 유틸리티가 Altibase 컨테이너에서 실행되도록 적당한 위치에 명령어를 추가해야 한다.

#### 스케일 업

기존 파드의 Altibase 서버와 동일한 데이터를 가진 파드를 생성한다.

가장 처음 생성된 파드를 aku에서는 마스터 파드(Master Pod)라고 부르며, 추가로 스케일 업하여 생성된 파드는 슬레이브 파드(Slave Pod)로 부른다.

#### 스케일 다운

파드를 종료할 때 Altibase 서버의 이중화 정보를 초기화한다. 


## 구성 요소

aku 유틸리티는 실행 파일과 설정 파일로 구성된다. 

> ⚠️ 모든 파드에서 실행하는 aku 실행 파일은 같은 버전을 사용해야 하며, aku 설정 파일 내 프로퍼티도 같은 값을 가져야 한다. 일반적으로 aku 실행 파일과 aku 설정 파일은 Altibase 컨테이너 이미지에 포함되어 있다. 
>
> Altibase 서버와 aku는 같은 컨테이너에서 실행해야 한다.

### aku 실행 파일

실행 파일의 이름은 aku이며 $ALTIBASE_HOME/bin에 위치한다. aku를 실행하려면 먼저 환경변수 ALTIBASE_HOME을 설정해야 한다.

### aku 설정 파일

aku를 실행하면 aku 설정 파일을 가장 먼저 읽어 Altibase 데이터 동기화에 필요한 정보를 얻는다. aku 설정 파일의 이름은 aku.conf이며 $ALTIBASE_HOME/conf에 위치해야 한다. Altibase 패키지에 aku.conf.sample 이름의 예제 파일을 제공하므로, aku를 실행하기 전에 이 파일을 참고하여 aku.conf를 생성해야 한다. aku 설정 파일의 내용은 아래와 같다. 

⚠️ '#' 다음에 오는 내용은 주석으로 처리한다.

~~~bash
# aku.conf.sample

#*****************************************************************
# Copyright 2022, Altibase Corporation or its subsidiaries.
# All rights reserved.
# Property File for Altibase AKU Utility
#*****************************************************************

#=================================================================
# Kubernetes setting Properties
#=================================================================
AKU_STS_NAME                  = altibase-sts    # statefulsets name
AKU_SVC_NAME                  = altibase-svc    # services name
AKU_SERVER_COUNT              = 4               # the number of Pods
#=================================================================
# Common Properties
#=================================================================
AKU_SYS_PASSWORD              = manager
AKU_PORT_NO                   = 20300
AKU_REPLICATION_PORT_NO       = 20301
AKU_QUERY_TIMEOUT             = 3600
AKU_QUERY_RETRY_COUNT         = 5
AKU_QUERY_RETRY_DELAY_MSEC    = 1000
#=================================================================
# aku start/end Properties
#=================================================================
AKU_ADDRESS_CHECK_COUNT       = 30
AKU_FLUSH_AT_START            = 1
AKU_FLUSH_TIMEOUT_AT_START    = 300
AKU_DELAY_START_COMPLETE_TIME = 0

AKU_FLUSH_AT_END              = 1
AKU_REPLICATION_RESET_AT_END  = 1
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
	REPLICATION_NAME_PREFIX = AKU_REP
	SYNC_PARALLEL_COUNT     = 1
	(
		SYS.T1, SYS.T2 PARTITION P1,
		SYS.T3
	)
)
~~~

각 프로퍼티에 대해 살펴보자.

| 카테고리                 | 프로퍼티 이름                        |  기본값   | 설명                                                         |
| ------------------------ | :----------------------------------- | :-------: | :----------------------------------------------------------- |
| 쿠버네티스 설정 프로퍼티 | AKU_STS_NAME                         |           | 쿠버네티스 오브젝트 명세에 정의한 스테이트풀셋 이름.<br/>설정할 수 있는 값의 최대 길이는 63바이트이다. |
|                          | AKU_SVC_NAME                         |           | 쿠버네티스 오브젝트 명세에 정의한 네트워크 서비스를 제공하는 서비스 이름.<br/>설정할 수 있는 값의 최대 길이는 63바이트이다. |
|                          | AKU_SERVER_COUNT                     |     4     | aku 유틸리티로 동기화할 수 있는 Altibase 서버의  최대 개수.<br/>쿠버네티스에서 스케일 업할 수 있는 파드 수를 의미하기도 한다.<br/>설정할 수 있는 값의 범위는 1 ~ 6이다. |
| 공통 프로퍼티            | AKU_SYS_PASSWORD                     |           | 데이터베이스 SYS 사용자 패스워드                             |
|                          | AKU_PORT_NO                          |   20300   | Altibase 서버의 서비스 포트.<br/>설정할 수 있는 값의 범위는 1024 ~ 65535이다. |
|                          | AKU_REPLICATION_PORT_NO              |   20301   | Altibase 이중화 포트.<br/>설정할 수 있는 값의 범위는 1024 ~ 65535이다. |
|                          | AKU_QUERY_TIMEOUT                    |   3600    | Altibase 서버 프로퍼티 QUERY_TIMEOUT를 의미한다. aku에서 수행한 쿼리의 수행 시간이 이 값을 초과하면 해당 동작은 취소된다. |
|                          | AKU_QUERY_RETRY_COUNT                |     5     | Altibase 서버에서 수행한 쿼리가 실패하면 이 값의 횟수만큼 재시도한다.<br/>0이면 재시도하지 않는다. |
|                          | AKU_QUERY_RETRY_DELAY_MSEC           | 1000 (ms) | Altibase 서버에서 수행한 쿼리가 실패하면 이 값의 시간만큼 대기한 후 재시도한다.<br/>0이면 대기하지 않고 재시도를 수행한다. |
| aku start/end 프로퍼티   | AKU_ADDRESS_CHECK_COUNT              |    30     | `aku -p start` 명령 수행 시 생성 중인 파드의 로컬 DNS가 엔드 포인트에 등록될 때까지 이 값의 횟수만큼 로컬 IP 접속을 시도한다. |
|                          | AKU_FLUSH_AT_START                   |     1     | `aku -p start` 명령 수행 시 이중화 갭을 제거할 것인지 설정한다.<br/>1이면 FLUSH 명령으로 이중화 갭을 제거하고, 0이면 제거하지 않고 시작한다. |
|                          | AKU_FLUSH_TIMEOUT_AT_START           |    300    | FLUSH WAIT 명령의 *wait_time*을 설정한다. 이 값이 0이면 FLUSH ALL을 수행하고 1 이상이면 FLUSH WAIT *wait_time*을 수행한다.<br>이 설정은 AKU_FLUSH_AT_START설정값이 1일 때만 유효하다. |
|                          | AKU_DELAY_START_COMPLETE_TIME        |  0(sec)   | 슬레이브 파드 생성 단계에서 내부적으로 데이터 동기화가 완료된 후 ADMIN_MODE 프로퍼티를 0으로 변경하기 전에 대기하는 시간을 설정한다. |
|                          | AKU_FLUSH_AT_END                     |     1     | 슬레이브 파드에서 `aku -p end` 명령 수행 시 이중화 갭을 제거할 것인지 설정한다.<br/>1이면 이중화 FLUSH ALL 명령으로 이중화 갭을 제거하고 0이면 제거하지 않는다. |
|                          | AKU_REPLICATION_RESET_AT_END         |     1     | 슬레이브 파드에서 `aku -p end` 명령 수행 시 RESET 명령으로 이중화 정보를 초기화할 것인지 설정한다.<br/>1이면 이중화 정보를 초기화하며, 0이면 초기화하지 않는다. |
| 이중화 프로퍼티          | REPLICATIONS/REPLICATION_NAME_PREFIX |           | aku가 생성하는 Altibase 이중화 객체 이름의 접두사로, 최대 길이는 37바이트이다.<br/>[Altibase 이중화 객체 이름 생성 규칙](#rep_name_rules)을 참고한다. |
|                          | REPLICATIONS/SYNC_PARALLEL_COUNT     |     1     | 이중화 SYNC 수행 시 송신/수신 쓰레드의 수.<br/>1부터 100까지 설정할 수 있다. |

<a name="rep_name_rules"></a>

> [!Note] 
>
> **Altibase 이중화 객체 이름 생성 규칙**
>
> aku에서 생성하는 Altibase 이중화 객체 이름 생성 규칙은 다음과 같다.
>
> *REPLICATION_NAME_PREFIX*_\[*파드 번호*]\[*파드 번호*\]
>
> - REPLICATION_NAME_PREFIX: REPLICATIONS/REPLICATION_NAME_PREFIX 프로퍼티에서 설정한 문자열
> - 파드 번호: 쿠버네티스 스테이트풀셋이 생성하는 파드의 이름에서 *pod_name*\_ 뒤에 위치한 숫자이며 각 파드들은 순차적으로 생성된 고유한 순번을 가진다. Altibase 이중화 객체 이름에는 이중화 쌍이 되는 두 파드 번호가 포함되며, 작은 값이 앞에 위치한다.
>
> 예시) AKU_SERVER_COUNT = 4, REPLICATION_NAME_PREFIX = AKU_REP 로 설정된 경우 각 파드에서 생성되는 이중화 객체 이름
> | 파드 번호    | 이중화 객체 이름 | 설명                                      |
> | :----------- | :--------------- | :---------------------------------------- |
> | *pod_name*-0 | AKU_REP_01       | *pod_name*-0과 *pod_name*-1의 이중화 객체 |
> |              | AKU_REP_02       | *pod_name*-0과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_03       | *pod_name*-0과 *pod_name*-3의 이중화 객체 |
> | *pod_name*-1 | AKU_REP_01       | *pod_name*-0과 *pod_name*-1의 이중화 객체 |
> |              | AKU_REP_12       | *pod_name*-1과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_13       | *pod_name*-1과 *pod_name*-3의 이중화 객체 |
> | *pod_name*-2 | AKU_REP_02       | *pod_name*-0과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_12       | *pod_name*-1과 *pod_name*-2의 이중화 객체 |
> |              | AKU_REP_23       | *pod_name*-2와 *pod_name*-3의 이중화 객체 |
> | *pod_name*-3 | AKU_REP_03       | *pod_name*-0과 *pod_name*-3의 이중화 객체 |
> |              | AKU_REP_13       | *pod_name*-1과 *pod_name*-3의 이중화 객체 |
> |              | AKU_REP_23       | *pod_name*-2와 *pod_name*-3의 이중화 객체 |
>
> ⚠️ aku가 생성하는 Altibase 이중화 객체의 이름을 사용자가 임의로 생성,삭제 및 수정할 경우 비정상적인 결과가 발생할 수 있다.
#### Altibase 이중화 대상 설정

사용자는 aku 설정 파일에서 aku가 생성한 Altibase 이중화 객체에서 관리할 **테이블** 또는 **파티션**을 지정할 수 있다. 이중화 대상을 지정하려면 이중화 관련 프로퍼티 설정 구문에 `[사용자 이름].[테이블 이름]` 또는 `[사용자 이름].[테이블 이름] PARTITION [파티션 이름]` 형식으로 이중화 대상의 정보를 추가해야 한다. 사용자 이름과 테이블 이름, 파티션 이름의 최대 길이는 모두 128바이트이다.

각 이중화 대상은 쉼표로 구분되며, 한 줄에 하나 이상의 이중화 대상을 입력할 수 있다.

다음은  *T1*~*T9* 테이블을 이중화 3개로 분리하여 관리하도록 설정하는 예시이다. *T2* 테이블의 경우, 파티션 *P1* 만 이중화 대상으로 설정하도록 했다.

```bash
#=================================================================
# Replication Properties
#=================================================================
REPLICATIONS = (
    REPLICATION_NAME_PREFIX = AKU_REP1
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T1, SYS.T2 PARTITION P1,
        SYS.T3
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP2
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T4, SYS.T5, SYS.T6
    )
),
(
    REPLICATION_NAME_PREFIX = AKU_REP3
    SYNC_PARALLEL_COUNT     = 1
    (
        SYS.T7,
        SYS.T8,
        SYS.T9
    )
)
```



## 구문

~~~sql
aku
[-h]
[--help]
[-v]
[--version]
[-i]
[--info]
[-p [start | stop | clean] ]
[--pod [start | stop | clean] ]
~~~



## 파라미터

### -h, --help

aku 유틸리티의 사용법을 출력한다. 

### -v, --version

aku 유틸리티의 버전 정보를 출력한다. aku 유틸리티의 버전은 Altibase 서버와 같은 버전으로 사용하는 것을 권장한다. 


### -i, --info

aku 설정 파일의 내용을 출력한다. 파일에 문법(syntax) 오류가 있는 경우 에러를 출력하며 정상적일 때 아래의 정보를 출력한다.

- Altibase 서버 접속 정보(데이터베이스 사용자, 패스워드, Altibase 서비스 포트)
- Altibase 이중화 포트
- 스케일 업 최대 수(최대 파드 수)
- Altibase 이중화 객체 이름 및 이중화 대상 테이블 정보

### -p, --pod {pod_action}

스케일링으로 파드를 생성하거나 종료할 때 Altibase에서 수행할 작업을 명시한다. -p 또는 --pod 파라미터 뒤에 start, end, clean 중 하나를 반드시 입력해야 한다. 

#### **start**

Altibase 이중화 객체를 생성하고 데이터를 동기화하는 작업을 수행한다. 파드를 생성할 때 이용한다. start 명령의 상세 동작을 살펴보자.

- **마스터 파드(*pod_name*-0) 생성하기**

  Altibase 이중화 객체는 모든 파드에 생성해야 하므로 스테이트풀셋에서 *pod_name*-0을 생성할 때도 `aku -p start` 명령을 수행해야 한다.

  ![](media/Utilities/aku_p_start_master_pod.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다.
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 처음 생성된 파드이기 때문에 다른 파드와의 연결은 실패한다. 이는 정상적인 동작이니 무시해도 된다.
  
  ④ Altibase 이중화 객체를 생성한다. 만약, 같은 이름의 이중화 객체가 존재한다면 이중화 생성 단계는 생략한다. 
  
  ⑤ *pod_name*-0 에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-0과 관련된 이중화를 시작한다. 일반적인 경우 처음 생성된 파드이기 때문에 접속된 파드가 없어, 이 동작은 수행되지 않는다.
  
  ⑥ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.

- **스케일 업(Scale up)**

  마스터 파드가 생성된 상태에서 스케일 업을 하면 슬레이브 파드가 생성된다. 하나의 파드는 생성과 종료를 반복할 수 있는데, 파드가 처음 생성될 때와 종료 후 다시 시작될 때 `aku -p start` 동작이 다르다.

  > **슬레이브 파드를 처음 생성하거나, 다시 시작할 때 (AKU_REPLICATION_RESET_AT_END = 1, 기본 동작)**

  슬레이브 파드를 처음 생성하거나, 종료된 슬레이브 파드를 다시 시작하는 경우 `aku -p start` 명령이 aku에서 동작하는 과정을 설명한다.

  아래는 *pod_name*-1에서 수행한 예이다.

    ![](media/Utilities/aku_p_start_slave_pod.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다.
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공하고 *pod_name*-2, *pod_name*-3은 생성되지 않았기 때문에 접속에 실패한다.
  
  ④ Altibase 이중화 객체를 생성한다. *pod_name*-1이 다시 시작된 파드라면, 같은 이름의 이중화 객체가 존재할 수 있으며 이 단계는 생략된다.
  
  ⑤ *pod_name*-1의 이중화 대상 테이블을 대상으로 TRUNCATE를 수행한다.
  
  ⑥ *pod_name*-0에게 이중화 SYNC를 요청한다.
  
  ⑦ *pod_name*-0에서 *pod_name*-1로 이중화 SYNC를 수행하고 이중화를 시작한다.
  
  ⑧ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다. 일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다.
  
  ⑨ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다.
  
  ⑩ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.
  
    > **이중화 정보가 초기화되지 않은 슬레이브 파드를 다시 시작할 때 (AKU_FLUSH_AT_START = 1, 기본 동작)** 
  
  파드가 비정상적으로 종료되거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 종료하면 이중화 정보가 초기화 되지 않는다. 이중화 정보를 초기화 하지 않으면 Altibase에 이전의 이중화 정보가 남아 있어 파드를 다시 시작할 때 다른 노드로부터 데이터를 동기화(이중화 대상 테이블의 TRUNCATE 후 이중화 SYNC 수행)하지 않고, 자기 노드에서 다른 노드로의 데이터 동기화(FLUSH)만 수행한다. 아래는 이러한 경우, *pod_name*-1에서 `aku -p start`를 수행할 때의 aku 동작을 설명한다.
  
  참고로, 이중화 정보가 초기화 되지 않으면 이중화 관련 메타 테이블에 이중화 재시작 지점(XSN)이 -1이 아닌 값을 갖는다. 보다 자세한 내용은 [주의사항 7번](#cautions7)을 참고한다.
  
  ![](media/Utilities/aku_p_start_aku_flush_at_start_1.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다. 
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공한다. 
  
  ④ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다. 일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다.
  
  ⑤ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화에 대해 ALTER REPLICATION ~ FLUSH ALL을 수행한다. 이 명령은 *pod_name*-1에서 다른 파드로 동기화하지 못한 데이터를 전송한다. 
  
  ⑥ 접속된 다른 파드에서도 *pod_name*-1과 관련된 이중화에 대해 ALTER REPLICATION ~ FLUSH ALL을 수행하여 동기화되지 못한 데이터를 전송한다. 만약 aku 설정 파일에 AKU_FLUSH_TIMEOUT_AT_START 프로퍼티의 값이 0이 아니라면, ALTER_REPLICATION ~ FLUSH WAIT *wait_time*을 수행하여 *pod_name*-1로 동기화되지 못한 데이터를 전송한다. 
  
  ⑦ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다.
  
  ⑧ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.
  
  > **이중화 정보가 초기화되지 않은 슬레이브 파드를 다시 시작할 때 (AKU_FLUSH_AT_START = 0 일 때)**
  
  비정상적으로 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 종료한 슬레이브 파드를 다시 시작할 때, AKU_FLUSH_AT_START 프로퍼티를 0으로 설정했다면 아래와 같이 동작한다.
  
    ![](media/Utilities/aku_p_start_aku_flush_at_start_0.png)
  
  ① aku.conf 파일을 읽는다.
  
  ② /tmp 디렉토리에 aku_start_completed 파일이 있는지 확인한다. 일반적인 경우 기존에 `aku -p start` 명령이 실행되지 않았으므로 이 파일은 존재하지 않는다. 만약 존재할 경우, `aku -p start` 명령을 중복으로 실행한 것으로 판단하여 오류 메시지를 출력하고 종료한다. 
  
  ③ 이중화 대상 서버인 모든 파드에 접속을 시도한다. 일반적인 경우 *pod_name*-0과의 접속만 성공한다.
  
  ④ *pod_name*-1에서 접속에 성공한 모든 파드와 관련된 이중화를 시작하고, 접속된 다른 파드에서 *pod_name*-1과 관련된 이중화를 시작한다.  일반적인 경우 *pod_name*-0과 관련한 이중화(AKU_REP_01)만 *pod_name*-0 및 *pod_name*-1 파드에서 시작된다. 
  
  ⑤ *pod_name*-1의 Altibase 서버 프로퍼티 ADMIN_MODE를 0으로 설정하여 데이터베이스 사용자의 접속을 허용한다. 
  
  ⑥ /tmp 디렉토리에 aku_start_completed 파일을 생성한다.

#### **end**

Altibase 이중화를 중지하고 초기화하는 작업을 수행한다. 파드를 종료할 때 이용한다.

![](media/Utilities/aku_p_end.png)

① aku.conf 파일을 읽는다.

② 해당 파드와 이중화로 연결된 모든 파드에 접속을 시도한다. 해당 번호보다 높은 번호의 파드는 일반적인 경우 이미 삭제된 상태이기 때문에 접속이 실패할 수 있다. 이는 정상적인 동작이다.

③ 해당 파드의 이중화 객체에 ALTER REPLICATION replication_name FLUSH ALL 명령을 수행하여 변경 로그를 모두 전송한다. aku 설정 파일에서 AKU_FLUSH_AT_END 프로퍼티의 값이 0이라면 이 단계는 수행되지 않는다.

④ 해당 파드의 이중화 객체와 관련한 모든 파드에 ALTER REPLICATION replication_name STOP 수행을 요청한다.

⑤ 해당 파드의 이중화 객체와 관련한 모든 파드에 ALTER REPLICATION replication_name RESET 수행을 요청한다. aku 설정 파일에서 AKU_REPLICATION_RESET_AT_END 프로퍼티의 값이 0이라면 이 단계는 수행되지 않는다.

⑥ /tmp 디렉토리에서 aku_start_completed 파일을 삭제한다.

#### **clean**

파드에서 Altibase 이중화 객체를 모두 삭제하고, /tmp 디렉토리에서 aku_start_completed 파일을 삭제한다. 더 이상 파드 간에 동기화를 할 필요가 없을 때 사용한다.



## 주의사항

### 1) aku 설정 파일 작성 시

- aku 프로퍼티 중 기본값이 없는 프로퍼티는 반드시 명시해야 한다. 명시하지 않을 경우, "Property [*property_name*] should be specified by configuration." 에러가 발생한다.

- aku 설정 파일에 주석을 입력해야 할 경우 '#' 기호를 사용한다. 다만, '#' 뒤에 아무 내용이 없다면 구문 오류가 발생한다.

### 2) 마스터 파드의 저장소에 손상이 발생한 경우

aku는 마스터 파드의 저장소 손상으로 인한 데이터 손상을 복구할 수 없다.

### 3) aku -p start 명령 수행 시

- `aku -p start` 명령은 Altibase 서버가 정상적으로 시작된 후 수행해야 한다. 

- Altibase의 프로퍼티 중 ADMIN_MODE와 REMOTE_SYSDBA_ENABLE를 모두 1로 설정한 후 서버를 기동해야 한다.

- 하나의 파드에서 `aku -p start` 명령을 완료한 후 순차적으로 다음 파드를 생성해야 한다. 동시에 여러 파드에서 `aku -p start`를 수행하는 경우 aku가 정상적으로 동작하지 않을 수 있다. 이를 위해 startup probe를 설정해야 하며, aku_start_completed 파일의 존재 여부로 확인한다. 또한 publishNotReadyAddresses를 true로 설정해야한다. startup probe, publishNotReadyAddresses에 대한 자세한 내용은 쿠버네티스 공식 문서를 참고한다.

### 4) 마스터 파드 장애로 aku -p start 명령 수행이 실패했을 때

마스터 파드 장애란 다음과 같은 환경에서 마스터 파드에 `aku -p start` 명령이 실패하는 것을 말한다.

- 한 개 이상의 슬레이브 파드가 실행 중이다.
- 마스터 파드에 존재하는 이중화 객체 중 실행 중인 슬레이브 파드(들) 사이의 이중화 객체 정보가 일부, 또는 전부 유실되었다.

마스터 파드 장애가 발생하면 다음과 같이 마스터 파드를 복구해야 한다.

1. 복구 기준이 될 슬레이브 파드를 선택한다. 복구 기준이 되는 슬레이브 파드 외의 모든 슬레이브 파드는 `aku -p end` 명령을 수행하여 종료한다.
2. 슬레이브 파드로부터 마스터 파드로의 동기화를 수행하여 데이터 정합성을 맞춘다.
3. 마스터 파드에서 이중화를 시작한다.
4. `aku -p start` 명령을 다시 수행한다.

각 복구 단계의 자세한 내용은 아래의 마스터 파드 장애 복구 예시를 참고한다.

**마스터 파드 장애 복구 예시**

다음과 같은 환경에서 마스터 파드 *pod_name*-0에서 장애가 발생했다고 가정한다. 

- 마스터 파드의 aku 프로퍼티 설정
  - AKU_SERVER_COUNT = 4
  - REPLICATION_NAME_PREFIX = AKU_REP
- 마스터 파드의 Altibase 서버 프로퍼티 설정
  - ADMIN_MODE = 1
- 슬레이브 파드 *pod_name*-1가 실행 중이다.
- 이중화 대상 테이블은 *T1*, *T2*, 그리고 *T3*이다.
- 마스터 파드에서 슬레이브 파드 *pod_name*-1 사이의 이중화 객체 AKU_REP_01의 정보가 소실되었다.

마스터 파드 장애 상황은 아래의 로그를 통해 확인할 수 있다.

```bash
$ aku -p start
AKU started with START option.
[AKU][2024/04/19 19:21:31.012670][140276343642368] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
[AKU][2024/04/19 19:21:31.012991][140276343642368] [ERROR][akuRunStart:1030][-][-] The MASTER server is detected to have failed. Check and perform a manual recovery.
AKU failed to run.
```

이 때 마스터 파드에서 정보가 소실된 이중화 객체의 XSN을 조회하면 그 값이 -1로 출력된다.

```sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_01                      -1
1 rows selected.
```

> [!note] 
>
> XSN은 송·수신 쓰레드를 통해 원격 서버와 지역 서버에 이중화 정보를 전달하는 XLog의 식별 번호이다. 이중화 객체를 초기화 하면 이 값은 -1이 된다.
> 이 때 아래의 복구 절차를 순차적으로 수행하여 마스터 파드의 장애를 해결할 수 있다.

1. 슬레이브 파드로부터 마스터 파드로의 동기화를 수행하여 데이터 정합성을 맞춘다.

   1. 마스터 파드에서 이중화 대상 테이블 레코드를 삭제한다.

      데이터 동기화 시 충돌이 발생하는 것을 방지하기 위해 마스터 파드에서 관리하는 이중화 대상 테이블을 TRUNCATE 한다. TRUNCATE 명령을 수행하기 위해서는 Altibase 서버 프로퍼티REPLICATION_DDL_ENABLE를 1로 설정해야 한다.

      ```sql
      # REPLICATION_DDL_ENABLE 프로퍼티 설정을 1로 변경한다.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 1;
      Alter success.

      # 이중화 대상 테이블의 레코드를 TRUNCATE 한다.
      iSQL> TRUNCATE TABLE T1;
      Truncate success.
      iSQL> TRUNCATE TABLE T2;
      Truncate success.
      iSQL> TRUNCATE TABLE T3;
      Truncate success.

      # REPLICATION_DDL_ENABLE 프로퍼티 설정을 0으로 원복한다.
      iSQL> ALTER SYSTEM SET REPLICATION_DDL_ENABLE = 0;
      Alter success.
      ```

   2. 슬레이브 파드에서 데이터 동기화를 수행한다.

      데이터를 동기화하기 전에, XSN 값을 초기화하기 위해 RESET을 수행한다. 동기화가 완료되면 이중화가 자동으로 시작된다.

      ```sql
      # 슬레이브 파드에서 이중화를 중지한다.(이중화가 시작되지 않은 경우 생략할 수 있다.)
      iSQL> ALTER REPLICATION AKU_REP_01 STOP;
      Alter success.
      
      # 슬레이브 파드에서 마스터 파드와의 이중화 객체를 초기화한다.
      iSQL> ALTER REPLICATION AKU_REP_01 RESET;
      Alter success.
      
      # 이중화 SYNC를 수행하여 슬레이브 파드와 마스터 파드의 데이터 정합성을 맞춘다.
      iSQL> ALTER REPLICATION AKU_REP_01 SYNC;
      Alter success.
      ```

2. 마스터 파드에서 이중화를 시작한다.

   마스터 파드에서 이중화를 시작하여 소실되었던 이중화 객체 정보의 복구를 완료한다. 

   ```sql
   iSQL> ALTER REPLICATION AKU_REP_01 START;
   Alter success.
   ```

3. `aku -p start` 명령을 다시 수행한다.

   복구가 완료된 마스터 파드는 슬레이브 파드와 동일한 데이터를 갖고 있고, 마스터 파드와 슬레이브 파드 사이의 이중화 객체인 AKU_REP_01의 XSN 값도 갱신된다. 이제 `aku -p start` 명령을 다시 수행하면 정상적으로 처리된다.

   ```bash
   # aku.conf를 읽어 이중화 객체를 생성한다. 
   $ aku -p start
   # START option은 aku -p start 를 사용함을 의미한다. 
   AKU started with START option.
   [AKU][2024/04/19 19:21:01.011887][139922191153408] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
   
   # 마스터 파드와 슬레이브 파드의 이중화 갭을 제거한다.
   [AKU][2024/04/19 19:21:09.057372][139922191153408] [INFO][akuRunStart:891][-][-] Flush replications.
   [AKU][2024/04/19 19:21:09.086363][139922191153408] [INFO][akuRunStart:896][-][-] Replication flush has ended.
   
   # 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
   AKU run successfully.
   ```

### 5) aku -p end 명령 수행 시

- `aku -p end` 명령은 Altibase 서버를 중지하기 전에 수행해야 한다.

- `aku -p end` 명령 수행이 완료된 후 파드를 종료해야 한다. 

### 6) aku -p end 명령이 완료되기 전에 파드가 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료했다면

이중화 정보가 초기화되지 않고 남아 있을 수 있다. 이 경우 해당 파드가 다시 시작할 때 이중화 객체 생성과 이중화 대상 테이블을 TRUNCATE 하는 작업이 생략되고 이전에 생성한 이중화가 자동으로 시작된다. AKU_REPLICATION_RESET_AT_END 프로퍼티를 1으로 설정하고 `aku -p end` 명령이 정상적으로 수행될 때의 출력 결과는 [예시 4](#예시-4)를 확인해 보자.

### 7) aku -p end 명령이 완료되기 전에 파드가 종료되었거나 AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료한 상태가 장기간 지속된다면<a name="cautions7"></a>

종료된 파드뿐 아니라 다른 파드에도 이중화 정보가 초기화되지 않고 남아 있을 수 있다. 이 경우 다른 파드는 종료된 파드로 이중화 하기 위해 이중화에 필요한 온라인 로그 파일을 삭제하지 않는다. 온라인 로그 파일이 쌓이면 디스크 풀 발생으로 Altibase 서버가 정상적으로 운영되지 못할 수 있다. 따라서 이런 상황을 방지하기 위해  `aku -p end` 명령이 완전히 완료되기 전에 파드가 종료되었거나, AKU_REPLICATION_RESET_AT_END 프로퍼티를 0으로 설정하고 파드를 종료한 상태가 장기간 지속되고 있다면 이중화를 중지하고 이중화 초기화 작업을 진행해야 한다. 

~~~sql
ALTER REPLICATION replication_name STOP;
ALTER REPLICATION replication_name RESET;
~~~

*pod_name*-0과 *pod_name*-1을 운영하던 중에 *pod_name*-1에서 `aku -p end` 명령이 정상적으로 수행되지 못하고 종료되었다고 가정해 보자. 이 때 *pod_name*-0에서 SYSTEM_.SYS_REPLICATIONS\_의 XSN을 조회하면 *pod_name*-0과 *pod_name*-1의 이중화 객체인 AKU_REP_01의 XSN 값이 -1이 아닌 다른 값으로 출력된다. 이는 이중화 정보가 초기화되지 않은 것을 의미한다.

~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      859070110
3 rows selected.
~~~

*pod_name*-0에서 AKU_REP_01을 중지하고 이중화 객체를 생성한 시점으로 초기화한다. 

~~~sql
iSQL> ALTER REPLICATION AKU_REP_01 STOP;
Alter sucess.

iSQL> ALTER REPLICATION AKU_REP_01 RESET;
Alter sucess.
~~~

다시 *pod_name*-0에서 SYSTEM_.SYS_REPLICATIONS\_의 XSN을 조회해 보자. 이중화 객체 AKU_REP_01의 XSN 값이 -1으로 변경되었다.

~~~sql
iSQL> SELECT REPLICATION_NAME, XSN FROM SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME                XSN                  
--------------------------------------------------------
AKU_REP_03                      -1
AKU_REP_02                      -1
AKU_REP_01                      -1
3 rows selected.
~~~

<br/>

## 제약사항

aku 유틸리티를 안정적으로 사용하기 위해 쿠버네티스 환경 설정 시 반드시 지켜야 할 조건이다. 

- 쿠버네티스의 워크로드 컨트롤러 중 **스테이트풀셋에서만 사용**해야 한다.
- **Altibase 서버와 aku는 같은 컨테이너에서 실행**해야 한다.
- **파드 관리 정책은 OrderedReady** 여야 한다. OrderedReady는 스테이트풀셋의 기본 정책이다.
- 스케일 업할 수 있는 레플리카는 **최대 6개**이다.
- 파드 종료 시 aku 수행을 완료할 수 있는 시간을 확보해야 한다. 따라서, 쿠버네티스에서 파드를 강제 종료하는 대기 시간인 terminationGracePeriodSeconds를 충분히 크게 설정해야 한다.

<br/>

## 사용 예

이 장에서는 다양한 상황에서 aku를 사용하는 예제를 설명한다.

예제에서 확인할 수 있는 aku 로그의 정보는 다음과 같다.

```
[AKU][현재 날짜 시간][스레드 번호] [메시지 타입][코드 정보][대상 pod 이름][이중화 이름] 메시지
```

### 예시 1

-i 파라미터를 사용하여 aku를 실행한 결과이다. 아래 결과는 [aku 설정 파일](#aku-설정-파일)의 aku.conf.sample로 구성한 aku.conf에서 수행한 예시이다. Server ID가 0인 것은 스테이트풀셋 컨트롤러에서 처음 생성한 파드를 의미한다.

~~~bash
$ aku -i
 #########################
 [ Server ]
  Server ID        : 0
  Host             : AKUHOST-0.altibase-svc
  User             : SYS
  Password         : manager
  Port             : 20300
  Replication Port : 20301
  Max Server Count : 4
 #########################
 [ Replications ]
 #### Serve[ID:0] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_03
 #### Serve[ID:1] Replication list ####
  Replication Name : AKU_REP_01
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_13
 #### Serve[ID:2] Replication list ####
  Replication Name : AKU_REP_02
  Replication Name : AKU_REP_12
  Replication Name : AKU_REP_23
 #### Serve[ID:3] Replication list ####
  Replication Name : AKU_REP_03
  Replication Name : AKU_REP_13
  Replication Name : AKU_REP_23
 #########################
 [ Replication Items ]
  User Name        : SYS
  Table Name       : T1
 
  User Name        : SYS
  Table Name       : T2
  Partition Name   : P1
 
  User Name        : SYS
  Table Name       : T3
 #########################
~~~

### 예시 2

마스터 파드(*pod_name-0*)에서 `aku -p start`를 수행한 예시이다.

~~~bash
$ aku -p start
AKU started with START option.
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.
AKU run successfully.
~~~

출력 결과를 살펴보자. 

~~~bash
# aku.conf를 읽어 이중화 객체를 생성한다. 
# START option은 aku -p start 를 사용함을 의미한다.
AKU started with START option.

# MASTER Pod는 첫 번째 파드를 의미한다. 
[AKU][2024/03/18 12:34:58.136944][140708807235840] [INFO][akuRunStart:828][-][-] Start as MASTER Pod.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully.
~~~

### 예시 3

네 번째 파드(*pod_name-3*)에서 `aku -p start` 명령을 수행한 예시이다. Master Pod는 스테이트풀셋에서 생성한 첫 번째 파드를 의미한다.

~~~bash
$ aku -p start
AKU started with START option.
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.
AKU run successfully.
~~~

출력 결과를 살펴보자. 

~~~bash
# aku.conf를 읽어 이중화 객체를 생성한다. 
# START option은 aku -p start 를 사용함을 의미한다.
 AKU started with START option.

# SLAVE Pod는 첫 번째 파드가 아닌 다른 파드를 의미한다. 
[AKU][2024/03/18 14:01:59.604647][140678415444224] [INFO][akuRunStart:903][-][-] Start as SLAVE Pod.

# SYNC 시 레코드 충돌 방지를 위해 대상 테이블의 레코드를 모두 삭제한다.
[AKU][2024/03/18 14:02:01.005068][140678415444224] [INFO][akuRunStart:959][-][-] Truncate tables for replications.
[AKU][2024/03/18 14:02:01.025100][140678415444224] [INFO][akuRunStart:964][-][-] Table truncation has ended.

# MASTER Server는 첫 번째 파드(pod_name-0)의 Altibase 서버를 말하며 해당 서버의 데이터를 로컬 파드로 동기화한다.
[AKU][2024/03/18 14:02:01.025877][140678415444224] [INFO][akuRunStart:975][-][-] Sync tables from MASTER Server.
[AKU][2024/03/18 14:02:05.045135][140678415444224] [INFO][akuRunStart:980][-][-] Replication sync has ended.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully. 
~~~

### 예시 4

네 번째 파드에서 AKU_REPLICATION_RESET_AT_END 프로퍼티를 1으로 설정하고 `aku -p end` 명령을 수행할 때의 출력 결과이다. 이중화 FLUSH 및 RESET 명령이 수행된 것을 볼 수 있다

~~~bash
$ aku -p end
AKU started with END option.
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.
AKU run successfully.
~~~

출력 결과를 살펴보자.

```bash
# aku.conf를 읽어 이중화를 중지하고 초기화한다. 
# END option은 aku -p end 를 사용함을 의미한다.
AKU started with END option.

# SLAVE Pod는 첫 번째 파드가 아닌 다른 파드를 의미한다. 
[AKU][2024/03/18 14:02:49.246961][139626938108160] [INFO][akuRunEnd:1090][-][-] Start as SLAVE Pod.

# 전달되지 않은 변경사항을 다른 파드로 FLUSH 한다.
[AKU][2024/03/18 14:02:49.247094][139626938108160] [INFO][akuRunEnd:1095][-][-] Flush replications.
[AKU][2024/03/18 14:02:49.247731][139626938108160] [INFO][akuRunEnd:1100][-][-] Replication flush has ended.

# 로컬 파드의 AKU 에서 생성한 이중화 객체를 모두 초기화한다.
[AKU][2024/03/18 14:02:52.001848][139626938108160] [INFO][akuRunEnd:1114][-][-] Reset replications.
[AKU][2024/03/18 14:02:52.014300][139626938108160] [INFO][akuRunEnd:1119][-][-] Replication reset has ended.

# 정상적으로 모든 절차가 수행된 뒤 aku가 종료된다. 
AKU run successfully. 
```





# 4.altiMon

## 개요

Altibase 서버 상태와 Altibase 서버가 구동 된 운영체제의 자원 상태를 수집하는 모니터링 유틸리티로, 운영체제의 자원 상태를 수집하기 위해 자체 제작한 PICL(Platform Information Collection Library) 라이브러리와 JDBC 드라이버 기반의 자바 애플리케이션이다. altiMon에서 수집한 데이터는 데이터베이스 장애 발생 시 장애 원인을 추적하는데 이용할 수 있다. 

altiMon의 모니터링 요소는 3가지로 나뉜다. 각 요소에 대한 보다 자세한 것은 [altiMon 설정 - Metrics.xml](#metricsxml)에서 설명한다.

- [OS Metric](#osmetric-요소) : Altibase의 PICL 라이브러리에서 미리 정의된 운영체제의 자원 상태
- [Command Metric](commanemetric-요소) : 사용자가 정의한 운영체제의 자원 상태
- [SQL Metric](sqlmetric-요소) : 사용자가 정의한 Altibase 서버 상태

<br/>

## 구문

~~~bash
altimon.sh {start | stop}
~~~

<div align="left">
    <img src=media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png>

<!-- IMG_RECOVERY_BEGIN ref_id="img-06964" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="2560" image_path_raw="media/Utilities/9f7b2fa1105d33ea554edb062ca8b96f.png" image_class="C" format="bnf" verified="True" -->
```bnf
altimon ::=
    altimon.sh { start | stop }
```
<!-- IMG_RECOVERY_END ref_id="img-06964" -->

</div>
<br/>

## 파라미터

| 파라미터 | 설명         |
| -------- | ------------ |
| start    | altimon 시작 |
| stop     | altimon 종료 |

<br/>

## 시스템 요구사항

### 자바

- Oracle, OpenJDK 또는 IBM Java Runtime Environment 8 이상 
- 64비트 자바

### 지원 플랫폼

altiMon의 지원 플랫폼은 PICL 라이브러리를 제공하는 플랫폼에 의존한다. 

| 운영체제                                                     | CPU                     | PICL 라이브러리 |
| :----------------------------------------------------------- | :---------------------- | :-------------- |
| **AIX**                                                      |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 5.3<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 6.1<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AIX 7.1 | PowerPC                 | aix-ppc64-5.so  |
| **HP-UX**                                                    |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HP-UX  11.31                   | Itanium (IA-64)         | hpux-ia64-11.sl |
| **Linux**                                                    |                         |                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 6.0   | x86-64                  | linux-x64.so    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 6.5   | PowerPC                 | linux-ppc64.so  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Red Hat Enterprise Linux 7.2   | PowerPC (Little Endian) | linux-ppc64.so  |

AIX 7.3, RHEL 8 등 위 표에 명시되지 않은 운영체제 버전에서 PICL 라이브러리가 동작하는 지 확인하는 방법이다. 

##### PICL 라이브러리의 동작 여부를 확인하는 방법

1️⃣ $ALTIBASE_HOME/altiMon 디렉토리로 이동한다. 

  ```bash
$ cd $ALTIBASE_HOME/altiMon
  ```

2️⃣ java 명령어로 PICL 라이브러리의 동작 여부를 확인한다.

위 표에서 해당하는 운영체제의 PICL 라이브러리 파일명을 확인하고 아래 명령어를 수행한다. 반드시 $ALTIBASE_HOME/altiMon 디렉토리 아래에서 수행해야 한다. 

~~~bash
$ java -Dpicl="<picl_lib_file>" -jar lib/com.altibase.picl.jar
~~~

> 수행 예

~~~bash
$ java -Dpicl="linux-x64.so" -jar lib/com.altibase.picl.jar 
===========================================================
Platform Information Collection Library-PICL Testing Module
===========================================================

Initializing PICL(Platform Information Collection Library)...
PICL Library : linux-x64.so

----------
Process ID
----------
Altibase Process : /home/altibase/altibase_home/bin/altibase
PID : 5230
...중략... 
~~~

<br/>

## altiMon 시작 및 중지

### altiMon 시작

1️⃣ Java를 사용할 수 있게 PATH 환경 변수를 설정한다.

```bash
$ java -version
java version "1.8.0_101"
Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)
```

2️⃣ altiMon 시작 명령을 수행한다.

~~~bash
$ altimon.sh start
~~~

3️⃣ altiMon 시작이 실패하면 \$ALTIBASE_HOME/altiMon/logs/altimon.log 파일을 확인한다.



### altiMon 중지

~~~bash
$ altimon.sh stop
~~~

<br/>

## altiMon 설정

altiMon을 사용하기 위해 \$ALTIBASE_HOME/altiMon 디렉토리의 conf 디렉토리에 있는 아래의 파일들을 설정한다. 설정 파일들은 모두 XML 문서이다.

-   [config.xml](#config.xml)

-   [Metrics.xml](#metrics.xml)

-   [GroupMetrics.xml](#groupmetrics.xml)

### config.xml

altiMon 수행과 관련한 설정과 모니터링 대상인 Altibase 서버의 정보를 설정하는 파일이다. 루트 요소 \<configuration> (또는 \<config>) 태그를 시작으로 Altimon 요소와 Target 요소로 구성되어 있다. 

~~~xml
$ cat config.xml 
<?xml version="1.0" encoding="UTF-8"?>

<configuration>
    
    <!-- Altimon 요소 -->
    <Altimon Name="rnd1" monitorOsMetric="true">
        <!--<LogDir>logs</LogDir> -->
        <DateFormat>yyyy-MM-dd HH:mm:ss</DateFormat>
        <MaintenancePeriod>3<!-- days --></MaintenancePeriod>
        <Interval>60<!-- seconds --></Interval>
        <CpuSamplingInterval>3<!-- seconds --></Interval>
        <DBConnectionWatchdogCycle>60<!-- seconds --></DBConnectionWatchdogCycle>
    </Altimon>
    
    <!-- Target 요소 -->
    <Target Name="Altibase1">
        <!--<HomeDirectory>/home/altibase/altibase_home</HomeDirectory> -->
        <!--<User>sys</User> -->
        <Password Encrypted="No">manager</Password>
        <Port>20300</Port>
        <DbName>mydb</DbName>
        <NLS>KSC5601</NLS>
        <IPv6>FALSE</IPv6>
        <ConnectionProperties>login_timeout=3</ConnectionProperties>
    </Target>
    
</configuration>
~~~

> #### altiMon 실행 설정

config.xml에서 <Altimon ...> 요소는 altiMon 로그 출력 형식, 로그 파일 삭제 주기, 모니터링 주기와 같은 altiMon 실행과 관련된 설정을 정의한다. 이 요소는 두 개의 속성과 4개의 하위 요소를 가진다.

**속성**

| 속성 이름                                                    | 설명                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Name                                                         | 사용자가 임의로 설정하는 altiMon의 고유 이름이다. 현재는 별다른 용도가 없으며 추후 기능 확장 시 사용될 예정이다. |
| monitorOsMetric&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Metrics.xml 파일에서 OSMetric 요소를 사용할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 사용한다. PICL 라이브러리가 필요하다. <br />- false : 사용하지 않는다. OS 자원을 감시할 필요가 없거나 PICL C 라이브러리가 제공되지 않는 환경에서 설정한다. |

**하위 요소**

아래 표의 태그는 <Altimon ...> 요소 아래에 중첩된 하위 요소로 사용된다.

| 태그 이름                     | 설명                                                         |
| :---------------------------- | :----------------------------------------------------------- |
| \<LogDir\>                    | altiMon 로그 파일이 생성될 경로를 설정한다. 기본값은 logs 이며, 이 태그를 추가하지 않으면 $ALTIBASE_HOME/altiMon/logs로 설정된다. $ALTIBASE_HOME/altiMon 아래에 logs 디렉토리가 존재하지 않으면 altiMon을 시작할 때 생성한다. 값은 절대 경로나 $ALTIBASE_HOME/altiMon/ 아래에 생성할 디렉토리 이름을 사용할 수 있다. |
| \<DateFormat\>                | altiMon 로그의 날짜 형식을 설정한다. 기본값은 yyyy-MM-dd HH:mm:ss 이다. 설정 가능한 날짜 형식은 [자바 SimpleDateFormat 클래스의 날짜 형식](http://docs.oracle.com/javase/1.5.0/docs/api/java/text/SimpleDateFormat.html)을 참고한다. |
| \<MaintenancePeriod\>         | altiMon 로그 파일의 보관 기간을 설정한다. 기본값은 3이고 단위는 일(day)이다. |
| \<Interval\>                  | altiMon의 모니터링 데이터 수집 주기를 설정한다. 기본값은 60이고 단위는 초(second)이다. <br />Metrics.xml 파일의 \<OSMetric\> 또는 \<SQLMetric\> 요소에서 Interval 속성을 설정하지 않으면 이 값이 적용된다. GroupMetrics.xml 파일의 \<Groupetric\> 요소에서는 이 값의 영향을 받지 않는다. |
| <CpuSamplingInterval\>        | CPU 사용률(%)을 측정하는 쓰레드의 실행 주기이다. 기본값은 3이고 단위는 초(second)이다.<br/>Altibase 7.1.0.8.4 이후 부터는 CPU 사용률을 측정하기 위해 OS CPU 사용률 측정 쓰레드, Altibase CPU 사용률 측정 쓰레드가 추가되었다. 각 쓰레드는 CpuSamplingInterval 주기로 CPU 사용률을 측정하며, 모니터링 요소에서는 이 값들을 참조 한다. OS CPU 사용률 측정 쓰레드와 Altibase CPU 사용률 측정 쓰레드는 각기 별도의 쓰레드로 동작하기 때문에, CPU 과부하시 두 측정값 사이에 시간차가 발생할 수 있다. |
| \<DBConnectionWatchdogCycle\> | Altibase 서버로의 접속 시도 주기를 설정한다. Altibase 서버가 중지되었을 때 altiMon은 이 값에 따라 주기적으로 Altibase 서버에 접속을 시도하므로 Altibase 서버가 시작되면 모니터링을 지속할 수 있다. 기본값은 60이고 단위는 초(second)이다. |



> ####  Altibase 서버 설정

config.xml에서 <Target ...> 요소는 데이터베이스 사용자, 패스워드 등 altiMon으로 모니터링 할 Altibase 서버의 접속 정보를 설정한다. 이 요소는 한 개의 속성과 설정할 수 있는 속성과 8개의 하위 요소를 가진다.

**속성**

| 속성 이름                                                    | 설명                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Altibase 서버를 식별하기 위한 고유 이름으로 사용자가 임의로 설정 가능하다. 현재는 별다른 용도가 없으며 추후 기능 확장 시 사용될 예정이다. |

**하위 요소**

아래 표의 태그는 Target 요소 아래에 중첩된 하위 요소로 사용된다.

| 태그 이름                | 설명                                                         |
| :----------------------- | :----------------------------------------------------------- |
| \<HomeDirectory\>        | Altibase 서버의 홈 디렉토리를 절대 경로로 입력한다. 설정하지 않으면 환경변수 ALTIBASE_HOME 값이 적용된다. |
| \<User\>                 | Altibase 서버에 접속할 데이터베이스 사용자를 입력한다. 설정하지 않으면 기본값인 SYS 사용자로 접속한다. |
| \<Password Encrypted>    | 데이터베이스 사용자의 패스워드를 입력한다.<br />Encrypted 속성은 altiMon을 처음 시작하기 전에 "No" 값으로 설정해야 한다. 이후 altiMon을 시작하면  평문으로 입력한 패스워드가 암호화된 값으로 저장되며 Encrypted 속성의 값이 "Yes"로 변경된다. |
| \<Port\>                 | Altibase 서버의 서비스 포트를 입력한다.                      |
| \<NLS\>                  | 데이터베이스 클라이언트 캐릭터셋을 입력한다.                 |
| \<DbName\>               | 데이터베이스 이름을 입력한다. 설정하지 않으면 기본값 mydb 로 설정된다.<br />데이터베이스 이름은 아래 문장으로 확인할 수 있다.<br />`SELECT DB_NAME FROM V$DATABASE; ` |
| \<IPv6\>                 | IPv6 사용 여부를 설정한다. true 또는 false 값을 가지며 기본값은 false 이다.  <br />- true  : IPv6를 사용한다. Altibase 서버 프로퍼티 NET_CONN_IP_STACK이 1 또는 2일 때 설정할 수 있다.<br />- false : IPv6를 사용하지 않는다. |
| \<ConnectionProperties\> | Altibase 서버 접속할 때 추가적인 연결 속성이 필요한 경우 `연결속성=값;연결속성=값;...` 형식으로 입력한다. 사용할 수 있는 연결 속성은 [JDBC User's Manual](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_trunk/kor/JDBC%20User's%20Manual.md#%EC%97%B0%EA%B2%B0-%EC%A0%95%EB%B3%B4)을 참고한다.<br />예) `<ConnectionProperties>login_timeout=3;fetch_timeout=60</ConnectionProperties>` |



### Metrics.xml

CPU 및 메모리 사용률 등의 운영체제 자원과 Altibase 서버의 상태를 감시하기 위한 질의문을 설정하는 파일이다. 루트 요소 \<Metrics> 태그를 시작으로 CommandMetric 요소, OSMetric  요소, SQLMetric 요소로 구성되어 있다. 각 요소는 모니터링 항목에 따라 여러 번 사용할 수 있다.

~~~xml
$ cat Metrics.xml | more
<?xml version="1.0" encoding="UTF-8"?>

<Metrics>
    
    <!-- CommandMetric 요소 --> 
    <CommandMetric Name='MEM_VSZ'>
        <Command>scriptsDir/vsz.sh</Command>
        <Alert Activate='true' ComparisonType='gt'>
            <WarningThreshold Value='100000000'>
                <ActionScript>mem_act.sh</ActionScript>
            </WarningThreshold>
        </Alert>
    </CommandMetric>    
    
    <!-- OSMetric 요소 -->
    <OSMetric Name='TOTAL_CPU' Activate='true' Description='TOTAL_CPU'>
    <OSMetric Name='TOTAL_CPU_USER' Activate='false' Description='TOTAL_CPU_USER'></OSMetric>
    <OSMetric Name='TOTAL_CPU_KERNEL' Activate='false'></OSMetric>    
    <OSMetric Name='PROC_CPU' Activate='true'>
        <Alert Activate='true' ComparisonType='gt'>
            <WarningThreshold Value='80' >
                <ActionScript>cpu_act.sh</ActionScript>
            </WarningThreshold>
        </Alert>
    </OSMetric>
    
    <!-- SQLMetric 요소 --> 
    <SQLMetric Name='MEM_DATABASE_USAGE' Activate='true' Interval='30'>
        <Query>
            select
            trunc(mem_alloc_page_count*32/1024, 2) as alloc_mem_mb,
            trunc(mem_free_page_count*32/1024, 2) as free_mem_mb
            from v$database
        </Query>
        <Alert Activate='true' ComparisonColumn='ALLOC_MEM_MB' ComparisonType='GT'>
            <CriticalThreshold Value='8000' >
                <ActionScript>db_usage.sh</ActionScript>
            </CriticalThreshold>
        </Alert>
    </SQLMetric>
    <SQLMetric Name='MEMSTAT_LIST' Activate='true'>
        <Query>SELECT * FROM v$MEMSTAT ORDER BY 4 DESC LIMIT 30</Query>
    </SQLMetric>   

</Metrics>    
~~~



> #### 사용자 정의 운영체제 자원 모니터링(CommandMetric)

Metrics.xml에서 <CommandMetric ...> 요소는 사용자가 직접 감시할 운영체제 자원을 정의할 수 있게 지원하는 모니터링 요소이다. PICL 라이브러리가 필요한 OSMetric 요소를 사용할 수 없는 환경에서 사용자가 직접 운영체제 명령어로 자원을 감시할 수 있다. OSMetric 요소에서 지원하지 않는 항목을 CommandMetric 요소에 추가할 수도 있다. 

**속성**

CommandMetric 요소에서 사용할 수 있는 속성이다. 이 속성들은 OSMetric 요소, SQLMetric 요소에서도 동일하게 사용할 수 있다.

| 속성 이름   | 설명                                                         |
| :---------- | ------------------------------------------------------------ |
| Name        | CommandMetric 요소는 여러 개 사용할 수 있으며 각 요소를 식별하기 위한 고유 이름을 설정한다. 이 요소의 로그 는 *Name*.log 로 생성된다. |
| Description | 사용자가 임의의 설명을 기록하기 위한 항목이다.               |
| Activate    | 해당 CommandMetric 요소를 수집할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 해당 CommandMetric 요소를 수집한다.<br />- false : 해당 CommandMetric 요소를 수집하지 않는다. |
| Interval    | 데이터 수집 주기. 단위는 초(second)이다.<br/>설정하지 않으면 config.xml에서 Altimon 요소의 \<Interval> 에 설정한 값을 따른다. |
| Logging     | 데이터 수집 결과를 파일에 기록할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true : 데이터 수집 정보를 파일에 기록한다.<br />- false : 데이터 수집 정보를 파일에 기록하지 않는다. 단, 하위 요소로 <Alert …> 태그가 활성화되었다면, alert 정보는 이 설정과 무관하게 기록된다. |

**하위 요소**

여러 하위 요소가 있으나 여기서는 CommandMetric 요소에서만 사용할 수 있는 하위 요소를 소개하고 다른 하위 요소는 [공통 하위 요소](#공통-하위-요소) 에서 설명한다.

| 태그 이름  | 설명                                                         |
| :--------- | :----------------------------------------------------------- |
| \<Command> | 수행할 명령어 또는 스크립트 파일 경로를 절대 경로 또는 상대 경로로 입력한다. 상대 경로의 기준은 $ALTIBASE_HOME/altiMon 디렉토리이다. 예를 들어, 절대 경로 입력 방식은 $ALTIBASE_HOME/altiMon/scriptsDir/cpuUsageWithTop.sh이고 상대 경로 입력 방식은 scriptsDir/cpuUsageWithTop.sh만 입력하면 된다.<br />공통 하위 요소 중 <Alert …> 태그를 설정하려면 이 항목의 결과 값이 숫자여야 한다. |



> ####  미리 정의된 운영체제 자원 모니터링(OSMetric)

Metrics.xml에서 <OSMetric ...> 요소는 PICL 라이브러리에서 미리 정의한 운영체제 자원을 감시하도록 제공하는 모니터링 요소이다. 

감시 대상인 운영체제 자원은 아래와 같다. 

- CPU
- 메모리
- 스왑(swap)
- 디스크

**속성**

[CommandMetric 요소에서 사용하는 속성](#속성-4)과 동일하다. 다만, Name은 PICL 라이브러리에서 미리 정의한 이름을 사용해야 한다.

| Name으로 사용할 수 있는 값 | 설명                                                         |
| :------------------------- | :----------------------------------------------------------- |
| TOTAL_CPU                  | OS 전체 CPU 사용률(%)                                        |
| TOTAL_CPU_USER             | 사용자 모드(user mode)에서 CPU 사용률(%)                     |
| TOTAL_CPU_KERNEL           | 커널 모드(kernel mode)에서 CPU 사용률(%)                     |
| PROC_CPU                   | Altibase 프로세스의 CPU 사용률(%)                            |
| PROC_CPU_USER              | 사용자 모드(user mode)에서 Altibase 프로세스의 CPU 사용률(%) |
| PROC_CPU_KERNEL            | 커널 모드(kernel mode)에서 Altibase 프로세스의 CPU 사용률(%) |
| TOTAL_MEM_FREE             | 사용할 수 있는 메인 메모리(RAM)의 크기(KB)                   |
| TOTAL_MEM_FREE_PERCENTAGE  | 사용할 수 있는 메인 메모리(RAM)의 비율(%)                    |
| PROC_MEM_USED              | Altibase 프로세스가 사용중인 메인 메모리(RSS)의 크기(KB)     |
| PROC_MEM_USED_PERCENTAGE   | Altibase 프로세스가 사용중인 메인 메모리(RSS)의 비율(%)      |
| SWAP_FREE                  | 사용 가능한 SWAP의 크기(KB)                                  |
| SWAP_FREE_PERCENTAGE       | 전체 SWAP 공간에서 사용 가능한 SWAP의 비율(%)                |
| DISK_FREE                  | 지정한 디스크에서 사용되지 않은 디스크의 크기(KB). <br />이 값을 사용할 때는 <Disk Name ...> 하위 요소가 반드시 필요하다. |
| DISK_FREE_PERCENTAGE       | 지정한 디스크에서 사용되지 않은 디스크의 비율(%). <br />이 값을 사용할 때는 <Disk Name ...> 하위 요소가 반드시 필요하다. |

**하위 요소**

 [공통 하위 요소](#공통-하위-요소)를 참고한다.

> #### Altibase 서버 상태 모니터링(SQLMetric)

Metrics.xml에서 <SQLMetric ...> 요소는 Altibase 서버 상태를 수집할 수 있도록 제공하는 모니터링 요소이다.

**속성**

[CommandMetric 요소에서 사용하는 속성](#속성-4)과 동일하다. 

**하위 요소**

여러 하위 요소가 있으나 여기서는 SQLMetric 요소에서만 사용할 수 있는 하위 요소를 소개하고 다른 하위 요소는 [공통 하위 요소](#공통-하위-요소)를 참고한다.

| 태그 이름 | 설명                                                         |
| :-------- | :----------------------------------------------------------- |
| \<Query\> | 모니터링 쿼리를 입력한다. 이 쿼리는 반드시 데이터 한 건을 조회하는 SELECT 문이어야 한다. |



> #### 공통 하위 요소

CommandMetric, OSMetric, SQLMetric 요소에서 공통적으로 사용할 수 있는 하위 요소를 설명한다. 각 하위 요소는 아래와 같이 중첩적으로 사용된다. 

~~~xml
<Alert Activate='...' ComparisonColumn='...' ComparisonType='...'>
    <WarningThreshold Value='...'>
        <ActionScript>script_name</ActionScript>
    </WarningThreshold>
</Alert>
~~~

| 태그 이름                                       | 속성 이름        | 설명                                                         |
| :---------------------------------------------- | :--------------- | :----------------------------------------------------------- |
| <Alert …>                                       |                  | 이 요소는 선택 항목으로, 모니터링 요소의 출력 값이 사용자가 정의한 한계 설정을 만족할 때 별도의 로그 $ALTIBASE_HOME/altiMon/logs/alert.log에 기록하는 기능이다. |
|                                                 | Activate         | <Alert …>의 수행 여부를 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true : alert 기능을 사용한다. 하위 요소로 <WarningThreshold …> 또는 <CriticalThreshold …>가 반드시 필요하다. <br />- false : alert 기능을 사용하지 않는다. |
|                                                 | ComparisonColumn | 이 속성은 ***SQLMetric에서만*** 사용할 수 있다. SQLMetric에서 조회한 칼럼을 입력해야 한다. 칼럼의 값은 <WarningThreshold …> 또는 <CriticalThreshold …>의 Value 속성과 비교 가능한 10진수 숫자여야 한다. |
|                                                 | ComparisonType   | 모니터링 요소의 출력 값과 <WarningThreshold …> 또는 <CriticalThreshold …>의 Value 속성과 비교할 비교 연산자를 입력한다.<br />- eq : 모니터링 요소의 출력 값과 한계값이 같을 때<br/>- ne : 모니터링 요소의 출력 값이 한계값과 같지 않을 때 <br/>- gt : 모니터링 요소의 출력 값이 한계값보다 클 때<br/>- ge : 모니터링 요소의 출력 값이 한계값보다 크거나 같을 때<br/>- lt : 모니터링 요소의 출력 값이 한계값보다 작을 때<br/>- le : 모니터링 요소의 출력 값이 한계값보다 작거나 같을 때 |
| <WarningThreshold …> 또는 <CriticalThreshold …> |                  | <Alert …>의 하위 요소로 경고 종류를 선택한다. <WarningThreshold …> 일 때 alert.log의 첫 번째 열은 WARNING이고 <CriticalThreshold …>이면 CRITICAL이다. <br />Activate 속성값이 true이면 반드시 이 요소를 사용해야 한다. |
|                                                 | Value            | 모니터링 요소의 한계 값을 10진수 숫자로 설정한다.            |
| \<ActionScript\>                                |                  | <WarningThreshold …> 또는 <CriticalThreshold …>의 하위 요소로, 모니터링 요소의 출력 값이 사용자가 정의한 한계 조건에 해당할 때 수행할 스크립트 파일 이름을 입력한다. 이 파일은 미리 작성되어 있어야 하며 $ALTIBASE_HOME/altiMon/action_scripts 디렉토리에 위치해야 한다. 스크립트 수행 시 각 모니터링 요소의 Name 속성과 alert 종류, 한계 값, 모니터링 요소의 결과 값이 인자로 전달된다. <br />스크립트 수행 결과는 $ALTIBASE_HOME/altiMon/action_logs/*actionscript_name*.log에 기록된다. action_logs의 파일들은 장애 원인 분석에 꼭 필요한 정보가 될 수 있어서 altiMon이 자동으로 삭제하지 않으므로 ***사용자가 직접 관리***해야 한다. |

### GroupMetrics.xml

Metrics.xml에 정의한 Command Metric과 OS Metric 그리고 SQL Metric을 사용자가 원하는 항목 별로 조합하여 하나의 파일에 저장하는 기능을 제공한다. GroupMetrics로 수집한 데이터는 $ALTIBASE_HOME/altiMon/logs 디렉토리에 CSV 파일 형식의 *GroupMetricName*.csv 이름으로 저장된다. Metrics.xml은 루트 요소 \<GroupMetrics> 태그를 시작으로 여러 개의 GroupMetric 요소로 구성할 수 있다.

~~~xml
<?xml version="1.0" encoding="UTF-8"?>

<GroupMetrics>
    <GroupMetric Name='group1' Interval='40'>
        <Target MetricName='TOTAL_CPU'/>
        <Target MetricName='PROC_CPU'/>
        <Target MetricName='LOGFILE_COUNT'>
            <Column Name='LOG_GAP' />
        </Target>
    </GroupMetric>
    
    <GroupMetric Name='group2' Interval='80'>
        <Target MetricName='PROC_MEM_USED_PERCENTAGE'/>
        <Target MetricName='MEM_TBL_USAGE'/>
    </GroupMetric>
</GroupMetrics>
~~~

다음은 GroupMetrics.xml에 설정할 수 있는 XML 요소와 속성에 대한 설명이다.

**속성**

GroupMetric 요소에서 사용할 수 있는 속성이다. 이 속성들은 OSMetric 요소, SQLMetric 요소에서도 동일하게 사용할 수 있다.

| 속성 이름 | 설명                                                         |
| :-------- | :----------------------------------------------------------- |
| Name      | GroupMetric을 식별하는 고유한 이름으로 사용자가 임의로 설정 가능하다. 로그 파일 생성 시 이 이름이 사용된다. 예) *group1*.csv |
| Activate  | GroupMetric 요소를 수집할 것인지 설정한다. true 또는 false 값을 가지며 기본값은 true이다.<br />- true  : 해당 CommandMetric 요소를 수집한다.<br />- false : 해당 CommandMetric 요소를 수집하지 않는다. |
| Interval  | 데이터 수집 주기. 기본값은 60이며 단위는 초(second)이다.     |

**하위 요소**

GroupMetric 요소 아래에 \<Target MetricName\>, \<Column Name\> 요소가 중첩적으로 사용된다.

| 태그 이름             | 설명                                                         |
| :-------------------- | :----------------------------------------------------------- |
| \<Target MetricName\> | Group Metric에 포함할 모니터링 요소들을 지정한다. <br /><br />MetricName 속성에 Metrics.xml에서 정의한 Command Metric과 OSMetric 그리고 SQLMetric의 이름을 입력한다. OSMetric의 DISK_FREE와 DISK_FREE_PERCENTAGE를 입력할 때 'OSMetric Name'.'Disk Name'형식으로 입력해야 한다. 예) <Target MetricName='DISK_FREE.disk1'\> |
| \<Column Name\>       | SQL Metric의 결과 중 일부 칼럼만 Group Metric에 포함하고 싶을 때 사용한다. 이 태그를 사용하지 않으면 SQL Metric에서 조회한 모든 칼럼이 Group Metric에 포함된다.<br /><br />Name 속성에 칼럼 이름을 입력한다. 칼럼 이름에 alias를 지정한 경우 alias를 입력한다. |

<br/>

## altiMon 로그

altiMon 로그는 $ALTIBASE_HOME/altiMon/logs 아래에 생성된다. 

### logs 디렉토리

logs 디렉토리에 생성되는 파일은 아래와 같다.

##### altimon.log  

altiMon 시작/중지 과정의 로그와 altiMon 수행 중 예외 상황 발생 시의 경고 또는 에러 메시지가 기록된다. 

##### alert.log  

Metrics.xml에서 \<Alert\> 설정에 해당하는 데이터를 기록하는 파일이다.

~~~bash
$ cat alert.log 
WARNING | PROC_CPU_USER | 2022-11-21 17:21:48 | PROC_CPU_USER = [90.61]
WARNING | PROC_CPU_USER | 2022-11-21 17:22:48 | PROC_CPU_USER = [90]
WARNING | PROC_CPU_USER | 2022-11-21 17:23:48 | PROC_CPU_USER = [90]
CRITICAL | DISK_FREE_PERCENTAGE.disk1 | 2022-11-21 17:24:46 | DISK_FREE_PERCENTAGE.disk1 = [5.22]
WARNING | PROC_CPU_USER | 2022-11-21 17:24:46 | PROC_CPU_USER = [90]
CRITICAL | DISK_FREE_PERCENTAGE.disk1 | 2022-11-21 17:25:46 | DISK_FREE_PERCENTAGE.disk1 = [5.22]
~~~

##### OsMetrics.log  

Metrics.xml에서 설정한 OSMetric에 의해 수집된 데이터를 기록하는 파일이다.

~~~bash
2022-11-21 20:20:25 | TOTAL_MEM_FREE_PERCENTAGE = [40.35]
2022-11-21 20:20:25 | SWAP_FREE = [94629696]
2022-11-21 20:20:25 | DISK_FREE_PERCENTAGE.disk1 = [30.21]
2022-11-21 20:20:25 | SWAP_FREE_PERCENTAGE = [96.26]
2022-11-21 20:20:25 | TOTAL_MEM_FREE = [39970752]
2022-11-21 20:20:25 | PROC_MEM_USED = [1010604]
2022-11-21 20:20:25 | PROC_MEM_USED_PERCENTAGE = [1.02]
2022-11-21 20:20:25 | PROC_CPU_KERNEL = [0]
2022-11-21 20:20:25 | PROC_CPU_USER = [0]
~~~

##### [*SQLMetric_Name*].log  

SQL Metric에 의해 수집된 데이터가 기록된 파일이다.

~~~bash
-rw-rw-rw- 1 altibase altibase   15399 Nov 21 20:21 BUFFER_STAT.log
-rw-rw-rw- 1 altibase altibase   10701 Nov 21 20:21 STATEMENT_COUNT.log
-rw-rw-rw- 1 altibase altibase  451791 Nov 21 20:21 SESSION_EVENT.log
-rw-rw-rw- 1 altibase altibase 1320921 Nov 21 20:21 MEMSTAT_LIST.log
-rw-rw-rw- 1 altibase altibase  346347 Nov 21 20:21 DB_EVENT.log
-rw-rw-rw- 1 altibase altibase   86298 Nov 21 20:21 DATAFILE_STAT.log
-rw-rw-rw- 1 altibase altibase   32364 Nov 21 20:21 MEM_GC.log
-rw-rw-rw- 1 altibase altibase   28710 Nov 21 20:21 SERVICE_THREAD_MODE.log

$ more BUFFER_STAT.log
2022-11-21 13:39:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:40:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:41:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
2022-11-21 13:42:42 |  VICTIM_FAILS = [0] READ_PAGES = [2]
~~~

##### [*GroupMetric_Name*].csv  

Group Metric에 의해 수집된 데이터가 Metric별로 csv 파일에 기록된다.

~~~bash
$ cat group1.csv 
"TIMESTAMP","TOTAL_CPU_USER","PROC_CPU_USER","LOGFILE_COUNT.LOG_GAP"
"2022-11-21 13:39:42","8.01","0","0"
"2022-11-21 13:40:22","0.81","0","0"
"2022-11-21 13:41:02","0.82","0","0"
"2022-11-21 13:41:42","0.79","0","0"
"2022-11-21 13:42:22","0.69","0","0"
~~~

##### report.html  

사용자가 설정한 altiMon 설정을 웹으로 확인할 수 있도록 제공하는 html 파일이다.

<div align="left">
    <img src="media/Utilities/altiMon_report_html.png">
</div>


### logs/archive 디렉토리

logs 디렉토리의 altimon.log, \*.csv를 제외한 모든 파일이 archive/YYYY-MM-DD 디렉토리로 매일 백업된다. 이 디렉토리 중 config.xml의 altiMon 실행 설정에서 \<MaintenancePeriod\>에서 설정한 기간이 지난 디렉토리는 매일 새벽 1시 50분에 삭제된다.

### logs/csv_backup 디렉토리

Group Metric에서 Target 설정이 변경되지 않으면 계속 같은 csv 파일에 데이터가 추가된다. 하지만 Target이 변경되면 기존의 csv 파일은 logs/csv_backup 디렉토리로 백업되고 같은 이름의 파일에 새로운 데이터가 기록된다.

5.기타 Utilities
==============

## altiAudit

### 개요

감사가 Altibase 서버에서 수행 중이라면, \$ALTIBASE_HOME/trc 디렉토리에 기본적으로 감사 로그 파일이 생성되고 로그가 기록될 것이다. 감사 로그 파일의 위치는 AUDIT_LOG_DIR 프로퍼티로 변경 가능하다. 이 파일에는 사용자가 읽을 수 없는 바이너리 형태의 감사 로그가 기록되어 있다. altiAudit 유틸리티는 감사 로그 파일을 문자 형태로 변환하여 출력함으로써 사용자가 감사 로그를 분석할 수 있게 한다.

```
altiAudit [-s] {audit_log_file_name}
```



### 구문

![](media/Utilities/altiaudit.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06966" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3077" image_path_raw="media/Utilities/altiaudit.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiaudit ::=
    altiAudit [ -s ] audit_log_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-06966" -->


### 설명

서버가 남긴 감사 로그를 문자 형태로 변환하여 출력한다.

\-s 옵션을 사용해서 CSV 형태로 출력할 수도 있다.

### 사용예

아래는 감사 로그를 일반 텍스트 형태로 출력하는 명령어이다.

```
$ altiAudit $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

아래와 같은 형태의 결과가 출력된다.

```
[2015/03/05 14:59:29]
Session Info 
  User Name        = SYS
  Session ID       = 1                   
  Client IP        = 127.0.0.1
  Client Type      = CLI-64LE
  Client App Info  = isql
  Action           = INSERT
  Auto Commit      = 1                        (0:non-autocommit 1:autocommit)
 
Query Info 
  Statement ID      = 65540               
  Transaction ID    = 150657              
  Execute result    = 4                       (0:failure 1:rebuild 2:retry 3:queue empty 4:success)
  Fetch result      = 2                       (0:failure 1:success 2:no result set)
  Success count     = 1                   
  Failure count     = 0                   
  Return code       = 0x02000
  Processed row     = 1                   
  Used memory       = 0                       bytes
  XA flag           = 0                       (0:non-XA 1:XA)
 
Query Elapsed Time 
  Total time        = 0                   
  Soft prepare time = 0                   
  Parse time        = 0                   
  Validation time   = 0                   
  Optimization time = 0                   
  Execution time    = 0                   
  Fetch time        = 0                   
 
SQL 
--------------------------------------------------------------------------------
insert into t1 values ('aaaa', 1)
-------------------------------------------------------------------------------- 

```

아래는 감사 로그를 CSV 형태로 출력하는 명령어이다.

```
$ altiAudit -s $ALTIBASE_HOME/trc/alti-1366989680-0.aud
```

아래와 같이 CSV 형태의 결과가 출력된다.

```
1425535169,SYS,1,127.0.0.1,CLI-64LE,isql,INSERT,1,65540,150657,4,2,1,0,1,0,0,0,0,0,0,0,0,0,"insert
into t1 values ('aaaa', 1)"
```



### 출력 항목

출력 항목과 의미는 아래 표와 같다.

| 필드 이름              | 타입    | 설명                                                         |
| ---------------------- | ------- | ------------------------------------------------------------ |
| **Session Info**       |         |                                                              |
| User Name              | 문자열  | 세션에 접속한 사용자 이름                                    |
| Session ID             | INTEGER | 세션 ID                                                      |
| Client IP              | 문자열  | 클라이언트 IP 주소                                           |
| Client Type            | 문자열  | 접속한 클라이언트의 타입                                     |
| Client App Info        | 문자열  | 애플리케이션 정보                                            |
| Action                 | 문자열  | 실행된 구문의 종류                                           |
| Auto Commit            | INTEGER | 0: Non-auto commit mode 1: auto commit mode                  |
| **Query Info**         |         |                                                              |
| Statement ID           | INTEGER | Statement ID                                                 |
| Transaction ID         | INTEGER | 트랜잭션 ID                                                  |
| Execute result         | INTEGER | 수행 결과 0: failure 1: rebuild 2: retry 3: query empty 4: success |
| Fetch result           | INTEGER | Fetch 결과 0: failure 1: success 2: no result set            |
| Success count          | INTEGER | 감사 조건에 부합하는 구문이 성공한 횟수이다. BY SESSION 조건일 경우, 감사 조건에 부합하는 구문의 수행에 성공한 횟수의 누적 값이다. BY ACCESS 조건일 경우, 감사 조건에 부합하는 구문이 성공적으로 수행된 경우 1이 표시된다. |
| Failure count          | INTEGER | 감사 조건에 부합하는 구문이 실패한 횟수이다. BY SESSION 조건일 경우, 감사 조건에 부합하는 구문의 수행에 실패한 횟수의 누적 값이다. BY ACCESS 조건일 경우, 감사 조건에 부합하는 구문의 수행이 실패한 경우 1이 표시된다. |
| Return code            | INTEGER | 감사 조건에 부합하는 구문이 수행된 결과 코드이다. BY ACCESS 조건일 경우에만, 수행 결과가 표시된다. |
| Processed row          | INTEGER | 처리된 레코드의 개수                                         |
| Used memory            | INTEGER | 사용된 메모리 (향후 확장 예정)                               |
| XA flag                | INTEGER | 0: Non-XA 1: XA                                              |
| **Query Elapsed Time** |         |                                                              |
| Total time             | BIGINT  | 쿼리 수행에 소요된 총 시간                                   |
| Soft prepare time      | BIGINT  | Prepare 수행에 소요된 시간                                   |
| Parse time             | BIGINT  | 파싱 수행에 소요된 시간                                      |
| Validation time        | BIGINT  | 정당성 검사에 소요된 시간                                    |
| Optimization time      | BIGINT  | 최적화 수행에 소요된 시간                                    |
| Execution time         | BIGINT  | 실행에 소요된 시간                                           |
| Fetch time             | BIGINT  | Fetch 수행에 소요된 시간                                     |
| **SQL**                |         |                                                              |
|                        | 문자열  | 실행된 SQL 구문                                              |

## altibase

### 개요

‘altibase’는 Altibase의 모든 서비스를 관장하는 서버 프로세스를 실행하는 파일이다.

```
altibase {-v|n}
```



### 구문

![](media/Utilities/altibase.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06967" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3199" image_path_raw="media/Utilities/altibase.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altibase ::=
    altibase { -v | -n }
```
<!-- IMG_RECOVERY_END ref_id="img-06967" -->


### 파라미터

| 파라미터 | 설명                                                |
|----------|-----------------------------------------------------|
| \-v      | 설치되어 있는 Altibase 제품의 버전 정보를 출력한다. |
| \-n      | Altibase를 포그라운드에서 수행한다.                 |

### 설명

‘altibase’는 Altibase의 모든 서비스를 관장하는 서버 프로세스의 실행 가능(executable) 파일이다.

Altibase를 구동하거나 종료하기 위해 이 커맨드를 직접 사용하면 안 된다. 대신에 iSQL에 SYSDBA 모드로 접속한 뒤, 구동이나 종료 명령을 사용하거나 server 커맨드를 사용해야 한다. server 커맨드는 실제로 Altibase 구동과 종료에 관련된 일련의 명령을 묶어놓은 쉘 스크립트이다. 관련 내용은 본 문서의 server 항목을 참조한다.

보다 자세한 Altibase의 구동 및 종료에 관한 내용은 *iSQL User’s Manual*이나 *Getting Started Guide* 를 참조한다.

iSQL로 구동된 Altibase 서버 프로세스는 백그라운드에서 운영된다. 반면, 쉘 프롬프트에서 altibase 커맨드를 -n옵션으로 수행할 경우 Altibase는 포그라운드에서 구동된다. 이는 Altibase 디버깅을 위한 용도로만 사용되며, 실 운영 시에는 사용하지 않도록 한다.

\-v 옵션으로 altibase 커맨드를 실행하면 현재 설치된 Altibase 제품의 버전 정보를 출력한다.

### 참고사항

Getting Started Guide

Administrator’s Manual

iSQL User’s Manual





## altierr

### 개요

altierr은 Altibase 서버 에러 코드에 대한 상세한 설명을 검색하여 출력하는 유틸리티이다. 에러 번호나 에러 메시지 패턴을 이용하여 검색이 가능하다.

```
altierr {-w keyword pattern | [-n] error number}
```



### 구문

![](media/Utilities/altierr.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06968" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3246" image_path_raw="media/Utilities/altierr.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altierr ::=
    altierr { -w keyword_pattern | [ -n ] error_number }
```
<!-- IMG_RECOVERY_END ref_id="img-06968" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-w      | 지정한 검색 패턴을 포함하는 에러 메시지를 찾는다. <br />검색 패턴을 포함하는 모든 에러 메시지를 출력한다. |
| \-n      | 에러 번호를 사용하여 검색한다. 에러 번호는 16진수/양의 정수/음의 정수 형태로 입력 가능하다. <br />에러 코드와 정확히 일치하는 레코드만 검색된다. <br />에러 번호를 사용하여 검색할 경우 파라미터(“-n”)를 생략할 수 있다. |

### 설명

altierr은 Altibase 서버의 에러 코드 번호나 에러 메시지에 포함된 문자열을 이용하여 에러에 대한 상세한 설명을 검색하고 출력해 주는 유틸리티이다.

에러 상세 설명에는 에러 코드 번호, 에러 코드 문자열, 에러 설명, 에러가 발생한 원인, 그리고 에러에 대한 조치 사항이 포함된다.

Altibase 서버는 에러 상황 발생시 해당 코드를 “ERR-{에러번호}” 형태로 altibase_boot.log에 출력한다. 여기에서 에러 번호는 16진수 값으로, 해당 에러에 대한 상세 설명을 검색하기 위해 altierr을 다음과 같이 사용할 수 있다.

```
For ‘ERR-00015’
$ altierr 0x00015
$ altierr –w 00015
$ altierr 21
```

C/C++ Precompiler나 ODBC로 작성된 애플리케이션의 경우 SQL 관련 기능 수행 시 SQLCODE나 ODBC 함수의 리턴 코드에 에러 코드가 설정이 된다. 이 때 설정되는 에러 코드는 음의 정수 값이 설정되며, 해당 에러에 대한 상세 설명을 검색하기 위해 다음과 같이 altierr을 사용할 수 있다.

```
For -266286
$ altierr -266286
$ altierr 266286
$ altierr 0x4102E
```

altierr은 에러 메시지에 포함된 키워드를 이용한 검색을 지원하며, 이 경우 여러 개의 레코드가 검색될 수 있다. 키워드 패턴을 이용한 검색은 다음과 같다.

```
$ altierr –w connect
$ altierr –w “does not”
```



### 참고 사항

Error Message Reference 참조

## altipasswd

### 개요

altipasswd는 $ALTIBASE_HOME/conf/syspassword 파일을 변경한다. 데이터베이스가 서비스 상태가 아닐때는 SYSDBA 옵션으로 iSQL을 구동하여 관리자 작업을 수행하는데, 이때 syspassword 파일을 읽어 sys 계정의 패스워드를 체크한다. 따라서, 데이터베이스 상에서 ALTER USER 문으로 sys 암호를 변경하는 경우, altipasswd로 syspassword 파일의 암호도 동일하게 변경해야 한다. 데이터베이스내의 sys 암호와 syspassword 암호가 동일하게 유지되지 않으면, 데이터베이스 구동, 종료 등 SYSDBA 작업을 할 때 오류가 발생하게 된다.

```
altipasswd
```



### 구문

![](media/Utilities/altipasswd.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06969" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3306" image_path_raw="media/Utilities/altipasswd.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altipasswd ::=
    altipasswd
```
<!-- IMG_RECOVERY_END ref_id="img-06969" -->


### 설명

SYS 사용자의 암호를 변경한다.

### 사용예

SYS 사용자의 암호 “manager”를 “manager1234”로 변경한다면 쉘 프롬프트 상에서
다음과 같이 수행한다.

```
$ altipasswd
Previous Password : manager
New Password : manager1234
Retype New Password : manager1234
```



## altiProfile

### 개요

Altibase 서버 내에서 수행되는 작업과 서버의 상태 정보를 파일로 기록하여 분석할 수 있다. 서버가 남긴 상태 파일을 프로파일이라 하며 altiProfile은 이 프로파일을 문자 형태로 변환하여 출력하거나, STATEMENT 관련 데이터만 추출하여 통계 정보를 구축하여 출력한다. 이 정보를 사용하여 사용자는 시스템의 상태를 분석할 수 있다.

```
altiProfile [-stat query|session] {profile_name [profile_name2 [profile_name3] ...}
```



### 구문

![](media/Utilities/altiprofile.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06970" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3340" image_path_raw="media/Utilities/altiprofile.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiprofile ::=
    altiProfile
        [ -h
        | -stat { query | session } ]
        profile_name { profile_name }
```
<!-- IMG_RECOVERY_END ref_id="img-06970" -->


### 파라미터

| 파라미터             | 설명                                                         |
| -------------------- | ------------------------------------------------------------ |
| \-h                  | 도움말을 출력한다.                                           |
| \-stat query/session | 서버가 남긴 프로파일에서 STATEMENT의 통계 정보를 구축하여, 텍스트와 CSV 형태의 파일로 출력한다. <br />구축되는 통계 정보에 대한 자세한 설명은 아래의 "사용 방법"을 참고하기 바란다. |

### 설명

서버가 남긴 프로파일을 문자 형태로 변환하거나, STATEMENT 관련 데이터만 추출하여 통계 정보를 구축한다.

### 사용예

```
iSQL> ALTER SYSTEM SET QUERY_PROF_FLAG = 1;
Alter success.
iSQL> ALTER SYSTEM SET TIMED_STATISTICS = 1;
Alter success.
iSQL> 	 --(Execute an SQL query here.)

$ cd $ALTIBASE_HOME/trc
$ altiProfile alti-1286503704-0.prof

$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof
```



### 사용 방법

서버의 상태 및 작업 내용을 기록하려면 QUERY_PROF_FLAG 프로퍼티를 0보다 큰 값으로 설정하여야 한다. QUERY_PROF_FLAG 프로퍼티의 값에 따라 다음의 정보들이 기록된다.

| 값   | 이름           | 설명                                                         |
| ---- | -------------- | ------------------------------------------------------------ |
| 0    |                | 기록하지 않음                                                |
| 1    | [STATEMENT]    | SQL 문이 실행될 때마다 실행된 SQL문, 실행시간, 실행정보, 색인 및 디스크 접근 정보 출력. <br />단, 실행시간이 제대로 출력되게 하려면 TIMED_STATISTICS 프로퍼티를 1로 설정해야 한다. <br />TIMED_STATISTICS 프로퍼티에 대한 자세한 설명은 *General Reference*를 참조하기 바란다. |
| 2    | [BIND]         | SQL 문이 실행될 때마다 BIND 파라미터 출력                    |
| 4    | [PLAN]         | SQL 문이 실행될 때마다 실행계획 출력                         |
| 8    | [SESSION STAT] | 3초마다 세션 정보 출력(V\$SESSTAT 정보)                      |
| 16   | [SYSTEM STAT]  | 3초마다 시스템 정보 출력(V\$SYSSTAT 정보)                    |
| 32   | [MEMORY STAT]  | 3초마다 메모리 정보 출력(V\$MEMSTAT 정보)                    |

위의 값을 조합하여 원하는 정보를 기록하도록 설정한다. 예를 들어, 프로퍼티를 1+4+32=37로 설정하면 SQL 문이 실행될 때마다 SQL 문의 실행정보와 실행계획을 출력하고 3초마다 메모리 정보를 출력한다.

프로퍼티가 설정되면, 서버는 alti-\#시간-\#번호.prof 이름의 파일에 정보를 남긴다. 사용자는 altiProfile 명령어로 상태 파일을 변환하여 분석할 수 있다.

##### 통계 정보 출력

altiProfile은 -stat 옵션을 사용해서 실행된 SQL문에 대한 통계 정보를 구축하고 출력할 수 있다. 이 정보는 튜닝 대상이 되는 SQL문을 찾는데 도움이 된다.

\-stat query 옵션을 실행하여 구축되는 통계 정보는 아래와 같다.

-   COUNT: QUERY가 실행된 횟수

-   AVG: QUERY 수행에 걸린 평균 시간 (microseconds 단위)

-   TOTAL: QUERY 수행에 걸린 시간 합계 (microseconds 단위)

-   MIN: QUERY 수행에 걸린 최소 시간 (microseconds 단위)

-   MAX: QUERY 수행에 걸린 최대 시간 (microseconds 단위)

-   SUCCESS: QUERY 실행에 성공한 횟수

-   FAIL: QUERY 실행에 실패한 횟수

-   QUERY: 수행된 SQL문

\-stat session 옵션으로 수행한다면, query 옵션을 실행하여 구축되는 통계 정보에 SESSION ID가 추가된다.

아래는 \$ALTIBASE_HOME/trc 디렉토리에 생성된 모든 프로파일을 분석하여 SQL문 별로 통계 정보를 구축하는 altiProfile 실행 예제이다.

```
$ altiProfile -stat query $ALTIBASE_HOME/trc/*.prof

### Processing [/altibase_home/trc/alti-1423543095-0.prof]...
100% [====================]

### Writing CSV File [alti-prof-stat-1423543711.csv]...

### Writing TEXT File [alti-prof-stat-1423543711.txt]...

### Successfully done.

```

위에 실행 로그를 살펴보면, 통계 정보는 CSV 형식과 텍스트 형식의 파일로 저장된다. 출력된 파일의 이름은 'alti-prof-stat-\#시간.csv'과 'alti-prof-stat-\#시간.txt'로 자동 생성된다.

다음은 텍스트 파일의 내용이다. 통계 정보는 TOTAL 값으로 정렬되어 출력된다.



```
$cat alti-prof-stat-1423543711.txt
COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     5     0.003730     0.018650     0.003035     0.004640     5     0    DROP VIEW REVENUE
     5     0.003523     0.017616     0.003004     0.003745     5     0    CREATE VIEW REVENUE (
...

```

다음은 CSV 파일의 내용이다. 텍스트 파일과 동일한 내용이 CSV 형식으로 출력된다. CSV 형식의 파일은 excel 같은 스프레드시트 애플리케이션을 사용해서 사용자가 원하는 포맷으로 가공할 수 있다.

```
$ cat alti-prof-stat-1423543711.csv
COUNT,AVG,TOTAL,MIN,MAX,SUCCES,FAIL,QUERY
5,  0.003730,  0.018650,  0.003035,  0.004640,5,0,"DROP VIEW REVENUE"
5,  0.003523,  0.017616,  0.003004,  0.003745,5,0,"CREATE VIEW REVENUE (
...

```



### 주의 사항

프로파일링 기능을 동작시킬 경우, 서버 내에서 실행되는 모든 SQL 문에 대해 실행 정보를 기록하며 또한 매 3초마다 세션 및 시스템 정보 등 서버의 상태를 기록하므로 시스템에 부하를 줄 수 있다.

또한 프로파일링 기능을 설정할 때 프로파일이 커져 디스크가 꽉 찰 수 있으므로 신중해야 한다.

### 출력항목

다음과 같은 형식으로 출력된다.

```
[BIND]
..
[PLAN]
..
[STATEMENT]
..
[SESSION STAT]
..
[SYSTEM STAT]
..
[MEMORY STAT]
..

```

각 정보는 아래와 같은 형식으로 출력된다.

##### [BIND]

SQL 문에 바인드 되는 변수들에 대한 정보이다.

##### [PLAN]

실행된 SQL 문의 실행 계획이 출력된다. 실행 계획에 관한 자세한 내용은 *Performance Tuning Guide*를 참고한다.

##### [STATEMENT]

다음의 표는 실행한 STATEMENT에 대한 정보를 나타낸다.

| 필드 이름                              | 값           | 설명                                                       |
| -------------------------------------- | ------------ | ---------------------------------------------------------- |
| SQL                                    | 문자열       | 실행된 SQL 문                                              |
| **User Info**                          |              |                                                            |
| User ID                                | INTEGER      | 사용자 식별자                                              |
| Client PID                             | BIGINT       | 클라이언트 프로세스 아이디                                 |
| Client Type                            | VARCHAR(40)  | 접속한 클라이언트의 타입                                   |
| Client AppInfo                         | VARCHAR(128) | 클라이언트의 정보 문자열                                   |
| **Elapsed Time for this SQL statemen** |              |                                                            |
| Total                                  | BIGINT       | 총 쿼리 수행 시간                                          |
| Parse                                  | BIGINT       | 파싱 수행 시간                                             |
| Valid                                  | BIGINT       | 정당성 검사 수행 시간                                      |
| Optim                                  | BIGINT       | 최적화 수행 시간                                           |
| Execu                                  | BIGINT       | 실행 수행 시간                                             |
| Fetch                                  | BIGINT       | Fetch 수행 시간                                            |
| **Query Execute Info**                 |              |                                                            |
| EXECUTE Result                         | INTEGER      | 0: failure 1: rebuild 2: retry 3: queue empty 4: success   |
| Optimizer Mode                         | BIGINT       | 최적화 모드                                                |
| Cost Mode                              | BIGINT       | 최적화 비용                                                |
| Used Memory                            | BIGINT       | 향후 확장 예정                                             |
| SUCCESS SUM                            | BIGINT       | 실행 성공 횟수의 총합                                      |
| FAILURE SUM                            | BIGINT       | 실행 실패 횟수의 총합                                      |
| PROCESSED ROW                          | BIGINT       | 처리된 레코드 개수                                         |
| **Result Set Info**                    |              |                                                            |
| FETCH Result                           | INTEGER      | 0: failure 1: success 2: no results                        |
| **Index Access Info**                  |              |                                                            |
| Memory Full Scan Count                 | BIGINT       | 메모리 테이블에 대한 Full Scan이 발생한 횟수               |
| Memory Index Scan Count                | BIGINT       | 메모리 테이블에 대한 Index Scan이 발생한 횟수              |
| Disk Full Scan Count                   | BIGINT       | 디스크 테이블에 대한 Full Scan이 발생한 횟수               |
| Disk Index Scan Count                  | BIGINT       | 디스크 테이블에 대한 Iindex Scan이 발생한 횟수             |
| **Disk Access Info**                   |              |                                                            |
| READ DATA PAGE                         | BIGINT       | 질의 수행 시 디스크 페이지에 대한 읽기 연산 횟수           |
| WRITE DATA PAGE                        | BIGINT       | 사용하지 않음                                              |
| GET DATA PAGE                          | BIGINT       | 질의 수행 시 디스크 페이지에 대한 버퍼 접근 횟수           |
| CREATE DATA PAGE                       | BIGINT       | 질의 수행 시 디스크 페이지 생성 횟수                       |
| READ UNDO PAGE                         | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지에 대한 읽기 연산 횟수 |
| WRITE UNDO PAGE                        | BIGINT       | 사용하지 않음                                              |
| GET UNDO PAGE                          | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지에 대한 버퍼 접근 횟수 |
| CREATE UNDO PAGE                       | BIGINT       | 질의 수행 시 UNDO 영역 디스크 페이지 생성 횟수             |

##### [SESSION STAT]

매 3초마다 V\$SESSTAT 정보가 출력된다. V\$SESSTAT의 자세한 내용은 *General Reference* 의 성능 뷰 부분을 참고한다.

##### [SYSTEM STAT]

매 3초마다 V\$SYSSTAT 정보가 출력된다. V\$SYSSTAT의 자세한 내용은 *General Reference*의 성능 뷰 부분을 참고한다.

##### [MEMORY STAT]

매 3초마다 V\$MEMSTAT 정보가 출력된다. V\$MEMSTAT의 자세한 내용은 *General Reference*의 성능 뷰 부분을 참고한다.

## altiwrap

### 개요

altiwrap은 PSM(Persistent Stored Module)으로 작성된 코드 프로그램을 암호화할 수 있는 유틸리티이다. altiwrap을 사용하여 코드를 암호화하면 다른 개발자에게 저장 프로시저 및 저장 함수 등의 PSM 코드가 노출되는 것을 방지할 수 있다.

```
altiwarp {--iname input_file} [--oname output_file]
```



### 구문

![altiwrap](media/Utilities/altiwrap.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06971" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3563" image_path_raw="media/Utilities/altiwrap.gif" image_class="C" format="bnf" verified="True" -->
```bnf
altiwrap ::=
    altiwrap
        { -h
        | --h
        | --iname input_file [ --oname output_file ] }
```
<!-- IMG_RECOVERY_END ref_id="img-06971" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-h/--h  | 도움말을 출력한다.                                           |
| \--iname | 암호화 할 파일의 이름을 지정한다. 파일의 확장자를 생략하면, '.sql'로 인식한다. |
| \--oname | 코드 프로그램이 암호화되어 저장될 파일의 이름을 지정한다. <br />파일의 확장자를 생략하면, '.plb'로 저장된다. |

### 설명

altiwrap을 실행하여 개발자가 작성한 저장 프로시저 및 저장 함수의 코드 프로그램을 암호화하여, 다른 개발자 또는 경쟁사에 노출되는 것을 방지할 수 있다.

Altibase가 암호화할 수 있는 구문은 아래와 같다.

-   CREATE [OR REPLACE] PROCEDURE

-   CREATE [OR REPLACE] FUNCTION

-   CREATE [OR REPLACE] TYPESET

-   CREATE [OR REPLACE] PACKAGE

-   CREATE [OR REPLACE] PACKAGE BODY

### 주의 사항

-   코드 프로그램이 암호화 된 후에는 프로그램을 변경할 수 없다. 프로그램을 변경할 때에는 암호화 전의 원본 프로그램에서 변경한 후 다시 암호화해야 한다.
    
-   트리거(trigger)는 암호화할 수 없다.

-   암호화된 프로그램 코드는 구문(syntax) 및 시맨틱(semantic)의 오류를 검사하지 못한다.

### 사용예제

altiwrap을 사용하여 sample1.sql 파일을 암호화한 후, 암호화된 파일을 출력한다.

아래는 sample1.sql 파일이다.

```
iSQL> create or replace procedure proc1 as
type arr1 is table of char(30) index by integer;
v1 arr1;
begin
v1[0] := 'create or replace';
v1[1] := 'typeset';
v1[2] := 'is';
v1[3] := 'success';
println( v1[0] || v1[1] || v1[2] || v1[3] || '!' );
end;
/
```

sample1.sql 파일을 암호화한다.

```
$ altiwrap --iname sample1.sql --oname --sample1.plb
```

암호화된 코드 프로그램을 isql에서 실행하면 된다.

```
iSQL> @sample1.plb
iSQL> create or replace procedure proc1 WRAPPED
'MjQz
MTk2
AAhjcmVhdGUgb3IgcmVwbGFjZSBwcm9jZWR1cqQBAAQxIGFzCnR5cGUgYXJyMSBpcyB0YWJsQAYAAWYgY2hhcigzMCkgaW5kZXggYnlAAQZ0ZWdlcjsKdjGYBQAEOwpiZWdpbgp2MVswXSA6PSAnY3JlYSu5ASdyBVsxtAN/DHNldK0CMq4CaXO5ATO4AQNzdWNjZXNsAgZwcmludGxuKCC2C3x8YAFACaABVAegAVwGDHx8ICchJyApOwplbmQ7ChEAADVBRDlBRkIzMDE0MzI1Q0U0MzY1RjYxNEI2NkYwQzRDREMzMTdDQTU=
';
/
Create success.
iSQL> exec proc1;
create or replace typeset is success!
Execute success.
```



## awrite

### 개요

로그 파일을 생성할 때 사용되는 시스템 콜의 응답 시간을 출력한다. 출력 값은 LOG_CREATE_METHOD 프로퍼티에서 시스템 콜을 결정하는데 참고된다.

### 구문

![awrite](media/Utilities/awrite.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06972" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3649" image_path_raw="media/Utilities/awrite.gif" image_class="C" format="bnf" verified="True" -->
```bnf
awrite ::=
    awrite
```
<!-- IMG_RECOVERY_END ref_id="img-06972" -->


### 설명

write()와 fallocate() 시스템 콜의 응답 시간을 출력한다.

### 사용예

아래와 같은 결과를 출력한다.

```
$ awrite
fallocate to expand file size to 1GB
 Elapsed Time ==>            2.564 seconds
write to expand file size to 1GB
 Elapsed Time ==>            4.020 seconds
```



## checkServer

### 개요

Altibase 프로세스를 감시하며, 프로세스가 비정상 종료하면 지정된 스크립트 파일을 실행한다.

```
checkServer [-n] {-f server-restart-script-file}
```



### 구문

![checkserver](media/Utilities/checkserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06973" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3683" image_path_raw="media/Utilities/checkserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
checkserver ::=
    checkServer [ -n ] -f server-restrat-script-file
```
<!-- IMG_RECOVERY_END ref_id="img-06973" -->


### 파라미터

| 파라미터 | 설명                                                                                |
|----------|-------------------------------------------------------------------------------------|
| \-n      | checkServer를 foreground에서 수행 파라미터 생략시 checkServer는 background에서 수행 |
| \-f      | Altibase 종료시 실행할 스크립트 파일의 이름                                         |

### 설명

checkServer는 주기적으로 Altibase 프로세스가 실행 중인지를 검사하여 Altibase 프로세스가 종료 되었을 경우 사용자가 지정한 스크립트를 수행한다.

Altibase가 비정상 종료 되었을 경우 Altibase 재구동 스크립트를 수행하는 것이 일반적이며, 재구동 스크립트는 다음과 같은 형식으로 작성할 수 있다.

-   Altibase 구동 스크립트 ‘restart.sh’

```
#! /bin/sh
${ALTIBASE_HOME}/bin/server start
```

checkServer는 구동시 \$ALTIBASE_HOME/trc 디렉토리에 checkServer.pid와 checkServer.log 파일을 생성한다. checkServer.pid파일은 또 다른 checkServer가 동시에 수행되지 못하도록 하는 락의 역할을 하며 checkServer.log에는 checkServer의 동작 상태가 주기적으로 기록된다.

checkServer를 ‘kill -9’등의 방법으로 강제 종료했을 경우에 checkServer.pid 파일이 디렉터리에 계속 남아있게 되어 checkServer를 다시 수행할 수 없게 된다. 이 때는 checkServer.pid파일을 삭제하면 checkServer를 정상적으로 시작할 수 있다.

checkServer를 종료하기 위해선 반드시 killCheckServer 유틸리티를 이용한다.

### 주의 사항

checkServer는 Altibase 서버가 “server stop” 커맨드를 사용하지 않고 종료된 경우에만, 지정한 재시작 스크립트를 실행한다. “server stop” 커맨드를 사용하여 Altibase 서버를 정상 종료하는 경우, checkServer 프로세스도 역시 종료되어, 재시작 스크립트를 실행하지 않게 된다. 이것은 checkServer가 “server stop” 커맨드를 사용하여 종료하는 것만 정상 종료라고 판단하기 때문이다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ checkServer –f restart.sh &
```



## dumpbi

### 개요

dumpbi는 이진 형식으로 저장된 backupinfo 파일의 백업 정보를 문자 형식으로 보여준다.

```
dumpbi  <backupinfo_file_name>
```



### 구문

![dumpbi](media/Utilities/dumpbi.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06974" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3739" image_path_raw="media/Utilities/dumpbi.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpbi ::=
    dumpbi backupinfo_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-06974" -->


### 설명

backupinfo 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpbi backupinfo
```



### 출력 항목

dumpbi는 backupinfo 의 백업 정보를 다음과 같은 섹션으로 구분하여 출력한다.

##### [BACKUO INFO FILE HDR]

| 필드 이름              | 값(단위 바이트)                 | 설명                                                         |
| ---------------------- | ------------------------------- | ------------------------------------------------------------ |
| Backup info slot count | 0 \~ unsigned int 타입의 최대값 | 저장되어 있는 backupinfo slot의 수<br />(= 현재까지 백업된 파일의 수) |
| Last backup LSN        | FileNo, Offset                  | 가장 최근에 수행된 백업 시점의 LSN<br />(유효한 backupinfo 파일인지 검증하기 위한 값) |
| Database name          | 문자열                          | 데이터베이스 이름                                            |

##### [BACKUP INFO SLOT]

| 필드 이름                     | 값(단위 바이트)                                              | 설명                                                         |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Slot index                    | 0 \~ unsigned int 타입의 최대값                              | slot의 순번                                                  |
| Begin backup time             | YYYY-MM-DD HH:MM:SS                                          | 백업 시작 일시                                               |
| End backup time               | YYYY-MM-DD HH:MM:SS                                          | 백업 완료 일시                                               |
| Incremental backup chunk cnt  | 0 \~ unsigned int 타입의 최대값                              | 데이터파일에서 변경된 페이지를 포함한 incremental chunk의 수<br />(= 백업된 incremental chunk의 수) |
| Incremental backup chunk size | 0 \~ unsigned int 타입의 최대값                              | 백업이 수행될 당시의 INCREMENTAL_BACKUP_CHUNK_SIZE의 값      |
| Backup target                 | 1: DATABASE <br />2: TABLESPACE                              | 백업 대상                                                    |
| Backup level                  | 1: level 0 <br />2: level 1                                  | 백업 레벨                                                    |
| Backup Type                   | 1: full backup <br />2: differentail backup <br />3: cumulative backup | 백업 유형                                                    |
| Tablespace ID                 | 0 \~ unsigned short 타입의 최대값                            | 백업 대상 데이터파일이 속한 테이블스페이스의 ID              |
| File ID                       | 0 \~ unsigned short 타입의 최대값                            | 백업 대상 데이터파일의 ID                                    |
| Original file size            | 0 \~ unsigned long 타입의 최대값                             | 백업된 시점의 데이터파일 크기                                |
| Backup Tag                    | 문자열                                                       | 백업 태그 이름                                               |
| Backup file name              | 문자열                                                       | 백업 파일의 경로와 이름                                      |

## dumpct

### 개요

dumpct는 이진 형식으로 저장된 changeTracking 파일의 정보를 문자 형식으로 보여준다.

```
dumpct  <changeTracking_file_name>
```



### 구문

![dumpct](media/Utilities/dumpct.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06975" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3799" image_path_raw="media/Utilities/dumpct.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpct ::=
    dumpct changeTracking_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-06975" -->


### 설명

changeTracking 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpct changeTracking
```



### 출력

dumpct는 changeTracking 파일 내의 변경 추적 정보를 다음과 같은 

[^]: 

으로 구분하여 출력한다.

##### [CHANGE TRACKING FILE HDR]

| 필드 이름                    | 값(단위 바이트)                 | 설명                                                                                                                                                  |
|------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change tracking body count   | 0 \~ unsigned int 타입의 최대값 | changeTracking 파일이 가진 body의 수 (changeTracking 파일은 header와 body로 나뉜다. body의 크기는 10Mbytes이며 공간이 부족하면 바디 단위로 확장된다.) |
| Icremental backup chunk size | 0 \~ unsigned int 타입의 최대값 | changeTracking 파일 생성시점의 INCREMENTAL_BACKUP_CHUNK_SIZE 프로퍼티 값                                                                              |
| Last flush LSN               | FileNo, Offset                  | 메모리상의 변경된 데이터가 파일로 기록된 시점의 LSN                                                                                                   |
| Database name                | 문자열                          | 데이터베이스 이름                                                                                                                                     |

##### [CHANGE TRACKING FILE BODY]

| 필드 이름                     | 값(단위 바이트)                   | 설명                                    |
| ----------------------------- | --------------------------------- | --------------------------------------- |
| Change tracking body ID       | 0 \~ unsigned int 타입의 최대값   | body의 ID                               |
| Flush LSN                     | FileNo, Offset                    | body가 flush 된 시점의 LSN(파일 검증용) |
| **Datafile descriptor slot**  |                                   |                                         |
| Slot ID                       | 0 \~ unsigned int 타입의 최대값   | slot의 ID                               |
| Tracking state                | 0: 추적 비활성화 1: 추적 활성화   | 데이터파일 변경 사항 추적 상태          |
| Tablespace type               | 0: memory TBS 1: disk TBS         | 테이블스페이스 유형                     |
| Page size                     | 0 \~ unsigned int 타입의 최대값   | 페이지 크기                             |
| Bitmap extent count           | 0 \~ unsigned short 타입의 최대값 | 할당된 비트맵 익트텐트 개수             |
| Current tracking list ID      | 0 \~ unsigned short 타입의 최대값 | 현재 추적중인 bitmap extent list의 ID   |
| **Differential0 BmpExt list** |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| **Differential1 BmpExt list** |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| **Cumulative BmpExt list**    |                                   |                                         |
| List                          | 0 \~ unsigned int 타입의 최대값   | bitmap extent list에 매달린 block ID    |
| Hint                          | 0 \~ unsigned int 타입의 최대값   |                                         |
| Tablespace ID                 | 0 \~ unsigned short 타입의 최대값 | 데이터파일이 속한 테이블스페이스의 ID   |
| File ID                       | 0 \~ unsigned short 타입의 최대값 | 데이터파일의 ID                         |

## dumpdb

### 개요

dumpdb는 메모리 체크포인트 이미지 파일로부터 메모리 테이블스페이스에 대한 정보를 출력하거나 또는 메모리 테이블스페이스의 증분 백업 파일의 내용을 문자 형식으로 보여주는 유틸리티이다.

```
dumpdb {-j job_number } [-i pingpong_number] [-o] [-f file_name] [-s] [-p] [-d]
```



### 구문

![dumpdb](media/Utilities/dumpdb.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06976" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="3871" image_path_raw="media/Utilities/dumpdb.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpdb ::=
    dumpdb -j job_number
        [ -i pingpong_number ]
        [ -o ]
        [ -f file_name ]
        [ -s ]
        [ -p ]
        [ -d ]
```
<!-- IMG_RECOVERY_END ref_id="img-06976" -->


### 파라미터

| 파라미터            | 설명                                                         |
| ------------------- | ------------------------------------------------------------ |
| \-j job_number      | 어떤 정보를 출력할 것인지를 지정한다. 지정 가능한 값과 각 값에 대해 추가로 지정할 수 있는 인자는 다음과 같다. <br />0: META (-s -f) <br />1: TABLESPACE (-s -f) 2: TABLESPACE-FLI (-s -d) <br />3: TABLESPACE-FREE-PAGE-LIST (-s) <br />4: TABLE (-o -d)<br />5: TABLE-ALLOC-PAGE-LIST (-o) <br />6: PAGE (-s -p -d) <br />7: INCREMENTAL_BACKUP_META (-f) |
| \-i pingpong_number | 체크포인트 이미지 파일의 핑퐁 번호이다. 생략하면 0이 사용된다. |
| \-o                 | 분석할 객체의 ID를 지정한다.                                 |
| \-f file_name       | 체크포인트 이미지 파일의 이름을 지정한다.                    |
| \-s                 | 분석할 테이블스페이스의 ID를 지정한다.                       |
| \-p                 | 분석할 페이지의 ID를 지정한다.                               |
| \-d                 | 정보를 상세히 출력한다.                                      |

### 설명

메모리 체크포인트 이미지 파일을 분석하여 메타 헤더, 페이지 등의 정보를 텍스트 형태로 출력하거나 또는 메모리 테이블스페이스의 증분 백업 파일에서 백업 정보를 텍스트 형태로 출력한다.

이 유틸리티는 디스크에 저장된 체크포인트 이미지 파일을 분석하기 때문에, Altibase 서버가 구동 중이 아니더라도 이 유틸리티를 수행하여 데이터베이스에 생성되어 있는 스키마를 확인할 수 있다.

하지만 DDL 직후 서버가 비정상 종료되어 갱신된 스키마가 디스크에 기록되지 못하면 해당 정보를 확인할 수 없다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpdb -j 1
$ dumpdb -j 1 -s 0
$ dumpdb -j 2
$ dumpdb -j 3
$ dumpdb -j 4
$ dumpdb -j 4 -d
$ dumpdb -j 4 -o 65536
$ dumpdb -j 5 -o 65536
$ dumpdb -j 6 -s 0 -p 4
```

\<예제 1\> 다음은 메모리 테이블스페이스에 관한 정보를 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수도 있다.

```
$ dumpdb -j 1
```

\<예제 2\> 다음은 메모리 테이블스페이스의 FreeListInfo(FLI) 페이지에 관한 정보를 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수 있고, -d 인자를 추가해서 FLI 페이지의 유효하지 않은 부분도 출력할 수 있다.

```
% dumpdb -j 2
```

\<예제 3\> 다음은 메모리 테이블스페이스의 FreePage들을 출력한다. –s 인자를 추가하여 특정 테이블스페이스에 관한 정보만 출력할 수도 있다.

```
% dumpdb -j 3
```

\<예제 4\> 다음은 데이터베이스에 생성되어 있는 모든 객체 정보를 출력한다. –o 인자(아래 예제에서 SelfOID 항목)를 추가하여 특정 객체에 관한 정보만 상세히 출력할 수도 있다. –d 인자를 추가해서 객체의 칼럼 정보와 인덱스 정보 등도 출력할 수 있다.

```
% dumpdb -j 4
```

\<예제 5\> 다음은 데이터베이스에 생성되어 있는 모든 객체의 정보를 칼럼 정보와 인덱스 정보 등과 함께 출력한다.

```
% dumpdb -j 4 -d
```

\<예제 6\> 다음은 특정 테이블의 스키마와 데이터를 출력한다.

```
% dumpdb -j 4 -o 65568
```

\<예제 7\> 다음은 특정 테이블이 사용하는 페이지 목록을 출력한다.

```
% dumpdb -j 5 -o 65568
```

\<예제 8\> 다음은 메모리 데이터베이스의 특정 페이지를 출력한다.

```
% dumpdb –j 6 -s 0 -p 4
```

\<예제 9\> 다음은 증분 백업 파일에 대해 dumpdb를 수행하여 백업 정보를 출력한다.

```
% dumpdb -j 7 -f SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak
dumpdb: Release 6.3.1.0.0 - Production on Oct 31 2012 22:12:21
(c) Copyright 2001 ALTIBase Corporation.  All rights reserved.
 
[BEGIN CHECKPOINT IMAGE HEADER]
Binary DB Version             [ 6.2.1 ]
Redo LSN       [ 1, 5867599 ]
Create LSN     [0, 1385 ]
DataFileDescSlot ID           [ 1, 1 ] 
 
//백업파일에 저장된 incremental backup정보
  [BEGIN BACKUPFILE INFORMATION]
 
        Begin Backup Time             [ 2012_11_06 23:18:43 ]
        End Backup Time               [ 2012_11_06 23:18:44 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 1 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/SYS_TBS_MEM_DATA-0-0_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END CHECKPOINT IMAGE HEADER]
 
Dump complete.
```



### 출력 항목

다음의 표는 증분 백업 파일에 대해 dumpdb 유틸리티를 실행하여 출력되는 항목들에 한하여 설명한다.

| 필드 이름           | 설명                                                                                                                                            |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary DB Version   | 데이터 파일의 버전                                                                                                                              |
| Redo LSN            | 미디어 복구를 위한 Redo LSN. 로그 앵커의 Redo LSN값이 데이터 파일의 Redo LSN보다 크면, 이 항목에 출력되는 Redo LSN 부터 미디어 복구가 필요하다. |
| Create LSN          | 체크포인트 이미지 생성 시점의 LSN                                                                                                               |
| DataFileDescSlot ID | 메모리 체크포인트 이미지와 묶여있는 ChangeTracking의 DataFileDescSlot ID                                                                        |

## dumpddf

### 개요

dumpddf는 데이터 파일의 헤더 정보 또는 데이터 파일 내의 특정 페이지를 출력한다. 또는 증분 백업 파일에 대해 dumpddf를 수행하면 백업 파일의 헤더 정보와 백업 정보가 출력된다.

```
dumpddf {-f datafile_name} {-m | -p pid}
```



### 구문

![dumpddf](media/Utilities/dumpddf.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06977" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4018" image_path_raw="media/Utilities/dumpddf.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpddf ::=
    dumpddf -f datafile_name { -m | -p pid }
```
<!-- IMG_RECOVERY_END ref_id="img-06977" -->


### 파라미터

| 파라미터 | 설명                                                                                                                    |
|----------|-------------------------------------------------------------------------------------------------------------------------|
| \-f      | 정보를 얻고 싶은 데이터 파일의 이름 이 옵션은 반드시 입력해야 한다. 생략하면 dumpddf는 에러 메시지를 출력하고 종료한다. |
| \-m      | 데이터 파일의 헤더 정보를 출력한다.                                                                                     |
| \-p      | 정보를 얻고 싶은 데이터 파일내의 페이지 ID                                                                              |

### 설명

데이터 파일의 헤더의 정보 또는 데이터 파일 내의 특정 페이지를 텍스트 형태로 출력한다. 지정한 페이지가 테이블이나 인덱스의 페이지이면 논리적으로 구성하여 출력한다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpddf –f datafile –m
$ dumpddf –f datafile –p page_id
```



### 출력 항목

다음은 dumpddf의 출력 예이다.

```
[BEGIN DATABASE FILE HEADER]
Binary DB Version             [ 5.4.1 ]
Redo LSN                      [0, 734497 ]
Create LSN                    [0, 1886 ]
MustRedo LSN                  [0, 0 ]
```

출력 내용 중, 필드들은 다음과 같은 의미를 갖는다.

| 필드 이름           | 설명                                                                                                                           |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Binary DB Version   | 데이터 파일의 버전                                                                                                             |
| Redo LSN            | 미디어 복구를 위한 Redo LSN. 로그앵커의 Redo LSN값이 데이터 파일의 Redo LSN보다 크면, 이 Redo LSN 부터 미디어 복구가 필요하다. |
| Create LSN          | 데이터 파일 생성 시점의 LSN                                                                                                    |
| MustRedo LSN        | 미디어 복구 시 이 Redo LSN까지 수행해야 한다.                                                                                  |
| DataFileDescSlot ID | Disk datafile과 묶여있는 ChangeTracking의 DataFileDescSlot ID                                                                  |

다음은 증분 백업 파일을 dumpddf로 출력한 예이다.

```
% dumpddf -m -f system001.dbf_TAG_MONDAY.ibak
-----------------------------------------------------------------
     Altibase Client Dump Disk Database File utility.
     Release Version 6.3.1.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
[BEGIN DATABASE FILE HEADER]
 
Binary DB Version             [ 6.2.1 ]
Redo LSN                      [1, 5867599 ]
Create LSN                    [0, 1914 ]
MustRedo LSN                  [0, 0 ]
DataFileDescSlot ID           [ 1, 2 ]
 
[BEGIN BACKUPFILE INFORMATION] -->백업파일에 저장된 incremental backup정보
 
        Begin Backup Time             [ 2012_11_06 23:18:44 ]
        End Backup Time               [ 2012_11_06 23:18:46 ]
        IBChunk Count                 [ 0 ]
        Backup Target                 [ DATABASE ]
        Backup Level                  [ LEVEL0 ]
        Backup Type                   [ FULL ]
        TableSpace ID                 [ 2 ]
        File ID                       [ 0 ]
        Backup Tag Name               [ MONDAY ]
        Backup File Name              [ /backup_dir/TAG_MONDAY/system001.dbf_TAG_MONDAY.ibak ]
 
  [END BACKUPFILE INFORMATION]
 
[END DATABASE FILE HEADER]

```



## dumpla

### 개요

dumpla는 이진 형식으로 저장된 loganchor 파일의 내용을 문자 형식으로 보여준다.

loganchor는 Altibase의 물리적인 저장 정보(테이블스페이스, 데이터 파일)와 복구를 위해 필요한 정보들이 저장되는 파일이다. Altibase는 데이터베이스 생성 시(CREATE DATABASE 실행 시)에 이 파일을 생성하고 altibase.properties에 설정된 세 개의 LOGANCHOR_DIR 디렉토리에 loganchor\#(\#은 1, 2, 3)의 이름으로 저장, 관리한다. 세 개의 파일은 모두 같은 내용으로 파일이 손상될 경우를 대비해 복사본을 유지하는 것이다. 데이터베이스 생성 시에 현재 데이터베이스에 존재하는 테이블스페이스와 이에 속한 데이터 파일, 그리고 복구 관련 정보들이 저장된다. 데이터베이스 구동 시에 이 정보들을 이용하여 데이터베이스를 메모리에 적재하고 서비스를 준비한다.

```
dumpla <loganchor_file_name>
```



### 구문

![dumpla](media/Utilities/dumpla.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06978" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4120" image_path_raw="media/Utilities/dumpla.gif" image_class="C" format="bnf" verified="True" -->
```bnf
dumpla ::=
    dumpla loganchor_file_name
```
<!-- IMG_RECOVERY_END ref_id="img-06978" -->


### 설명

loganchor 파일의 내용을 텍스트 형식으로 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumpla loganchor0
```



### 출력 항목

dumpla는 loganchor의 내용을 다음과 같은 섹션으로 구분하여 출력한다.

##### [LOGANCHOR ATTRIBUTE SIZE]

현재 Loganchor에 어떤 데이터들이 얼마만큼의 공간을 사용하고 있는지를 나타낸다. 내용은 다음과 같다.

| 필드 이름                  | 값(단위 바이트)                 | 설명                                                                                    |
|----------------------------|---------------------------------|-----------------------------------------------------------------------------------------|
| Loganchor Static Area      | 0 \~ unsigned int 타입의 최대값 | Loganchor에 고정적으로 들어가는 정보의 크기를 나타낸다. 주로 복구 시 필요한 정보들이다. |
| Tablespace Attribute       | 0 \~ unsigned int 타입의 최대값 | 저장된 Tablespace Attribute의 크기                                                      |
| Checkpoint Path Attribute  | 0 \~ unsigned int 타입의 최대값 | 저장된 Checkpoint Path의 크기                                                           |
| Checkpoint Image Attribute | 0 \~ unsigned int 타입의 최대값 | 저장된 Checkpoint Image Attribute의 크기                                                |
| Disk Datafile Attribute    | 0 \~ unsigned int 타입의 최대값 | 저장된 Disk Datafile Attribute의 크기                                                   |

##### [LOGANCHOR HEADER]

데이터베이스의 버전 및 체크포인트 Log Sequence Number (LSN) 등의 loganchor Header 정보를 나타낸다. LSN에 대한 자세한 설명은 “dumplf 의 출력”절을 참고하기 바란다.

| 필드 이름                         | 값                                   | 설명                                                         |
| --------------------------------- | ------------------------------------ | ------------------------------------------------------------ |
| Binary DB Version                 | Major.minor.patch ex) 6.2.1          | 현재 Loganchor를 생성한 데이터베이스 실행 파일의 데이터베이스 버전이다. |
| Archivelog Mode                   | Archivelog \|No-Archivelog           | 데이터베이스가 아카이브 모드로 운영 중인지를 나타낸다.       |
| Transaction Segment Entry Count   |                                      |                                                              |
| Begin Checkpoint LSN              | FileNo, Offset                       | Begin Checkpoint의 LSN을 나타낸다.                           |
| End Checkpoint LSN                | FileNo, Offset                       | End Checkpoint의 LSN을 나타낸다.                             |
| Disk Redo LSN                     | FileNo, Offset                       | DRDB의 Redo 시작 위치를 나타낸다.                            |
| LSN for Recovery from Replication | FileNo, Offset                       | 이중화를 이용한 복구 시 이 LSN부터 시작한다.                 |
| Server Status                     | SERVER_SHUTDOWN \|SERVER_STARTED     | 서버의 상태를 기록한다. 서버 시작 시 이 값이 SERVER_STARTED로 바뀌고 종료 시 SERVER_SHUTDOWN으로 바뀐다. 서버 시작 시에 이 값이 SERVER_STATED로 되어있다면 이전에 서버가 비정상 종료한 것이므로 재구동시 복구를 수행한다. |
| End LSN                           | FileNo, Offset                       | 서버가 정상 종료한 후 재구동시 첫 번째 기록되는 로그의 LSN   |
| ResetLog LSN                      | FileNo, Offset                       | 불완전 복구시 설정된 Reset LSN                               |
| Last Created Logfile Num          | 0 \~ unsigned int 타입의 최대값      | 가장 최근에 생성된 로그 파일 번호                            |
| Delete Logfile(s) Range           | 삭제되는 첫 번째 \~ 마지막 파일 번호 | 가장 최근에 삭제된 로그 파일의 범위. 체크포인트 완료 후 더 이상 필요 없는 파일을 삭제하는데 이 때 지워지는 파일의 범위를 기록한다. |
| Update And Flush Count            | 0 \~ unsigned int 타입의 최대값      | logAnchor 파일이 변경되고 플러시된 횟수                      |
| New Tablespace ID                 | 0 \~ unsigned int 타입의 최대값      | 새로운 테이블스페이스 식별자. 테이블스페이스가 생성될 경우 이 값을 자신의 테이블스페이스 식별자로 사용하고 이 값을 증가시킨다. |
| Checkpoint Scale                  | PAIR\|SINGLE                         | 현재 데이터베이스의 체크포인트 스케일 설정                   |

##### [TABLESPACE ATTRIBUTE]

메모리 테이블스페이스 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                   | 값                                         | 설명                                                         |
| --------------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| Tablespace ID               | 0 \~ unsigned int 타입의 최대값            | 테이블스페이스 식별자                                        |
| Tablespace Name             | 문자열 ex) SYS_TBS_MEM_DIC                 | 테이블스페이스 이름                                          |
| New Database File ID        | 0 \~ unsigned int 타입의 최대값            | 테이블스페이스에 새로운 파일이 추가될 때 파일이 가지게 될 파일의 식별자 |
| Extent Management           | FREE EXTENT BITMAP TABLESPACE              | 디스크 테이블스페이스의 extent가 어떤 방식으로 관리되는지를 나타낸다. 현재는 FREE EXTENT BITMAP TABLESPACE만 지원한다. FREE EXTENT BITMAP TABLESPACE를 enable하면, 디스크 테이블스페이스의 free extents를 관리하는데 bitmaps을 사용한다. |
| Tablespace Status           | 아래 TABLESPACE ATTRIBUTE 설명 참조        | 테이블스페이스의 현재 상태를 나타낸다.                       |
| Tablespace Type             | 0 \~ 8 아래 TABLESPACE ATTRIBUTE 설명 참조 | 테이블스페이스의 타입                                        |
| Checkpoint Path Count       | Checkpoint Path 개수                       | 체크포인트 이미지 파일들의 경로. 메모리 테이블스페이스에만 적용된다. |
| Autoextend Mode             | AutoExtend \|Non-AutoExtend                | 테이블스페이스가 자동으로 크기가 확장되는지 여부를 가리킨다. 메모리 테이블스페이스에만 적용된다. |
| Shared Memory Key           | 0 \~ unsigned int 타입의 최대값            | 데이터베이스가 공유 메모리 버전이면 이 때 공유 메모리에 데이터베이스가 사용한 공유 메모리의 키 |
| Stable Checkpoint Image Num. | 0\|1                                       | 체크포인트가 완료된 체크포인트 이미지 파일의 핑퐁 번호. 메모리 테이블스페이스에만 적용된다. |
| Init Size                   | 0 \~ unsigned int 타입의 최대값            | 초기 크기(Mbyte)                                             |
| Next Size                   | 0 \~ unsigned int 타입의 최대값            | 자동 확장되는 증가분의 크기(Mbyte)                           |
| Maximum Size                | 0 \~ unsigned int 타입의 최대값            | 최대 크기                                                    |
| Split File Size             | 0 \~ unsigned int 타입의 최대값            | 메모리 테이블스페이스는 파일을 이 크기 단위로 생성한다. 예를 들어 테이블스페이스가 1G이고, Split file size가 100MB이면 10개의 파일이 생성된다. |

[TABLESPACE ATTRIBUTE] 내용 중 Tablespace Status의 의미는 다음과 같다.

| 값                   | 설명                                                       |
|----------------------|------------------------------------------------------------|
| OFFLINE              | 오프라인 상태                                              |
| ONLINE               | 온라인 상태                                                |
| INCONSISTENT         | 비일관적인 상태                                            |
| CREATING             | 생성 중                                                    |
| DROPPING             | 삭제를 수행한 트랜잭션이 아직 커밋하지 않아 삭제 중인 상태 |
| DROP_PENDING         | 삭제를 수행한 트랜잭션이 커밋 이후 Pending 연산 중인 상태  |
| DROPPED              | 삭제된 상태                                                |
| DISCARDED            | Discard된 상태                                             |
| BACKUP               | 백업 중                                                    |
| SWITCHING_TO_OFFLINE | OFFLINE으로 바뀌고 있는 중                                 |
| SWITCHING_TO_ONLINE  | ONLINE으로 바뀌고 있는 중                                  |

[TABLESPACE ATTRIBUTE] 내용 중 Tablespace Type의 의미는 다음과 같다.

| 값 | 설명                     |
|----|--------------------------|
| 0  | MEMORY SYSTEM DICTIONARY |
| 1  | MEMORY SYSETM DATA       |
| 2  | MEMORY USER DATA         |
| 3  | DISK SYSTEM DATA         |
| 4  | DISK USER DATA           |
| 5  | DISK SYSTEM TEMP         |
| 6  | DISK USER TEMP           |
| 7  | DISK SYSTEM UNDO         |
| 8  | VOLATILE USER DATA       |

##### [MEMORY CHECKPOINT PATH ATTRIBUTE]

메모리 테이블스페이스의 체크포인트 저장 경로를 나타낸다. 내용은 다음과 같다.

| 필드 이름       | 값                              | 설명                          |
|-----------------|---------------------------------|-------------------------------|
| Tablespace ID   | 0 \~ unsigned int 타입의 최대값 | 테이블스페이스 식별자         |
| Checkpoint Path | 문자열                          | 체크포인트 이미지 파일의 경로 |

##### [MEMORY CHECKPOINT IMAGE ATTRIBUTE]

메모리 테이블스페이스의 체크포인트 이미지 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                           | 값                              | 설명                                                         |
| ----------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| Tablespace ID                       | 0 \~ unsigned int 타입의 최대값 | 테이블스페이스 식별자                                        |
| File Number                         | 0 \~ unsigned int 타입의 최대값 | 파일 번호                                                    |
| Stable Single Checkpoint Image Num. | 0\|1                            | 체크포인트가 완료된 체크포인트 이미지 파일의 핑퐁 번호. 체크포인트 스케일이 싱글일 때만 적용된다. |
| Create LSN                          | \< FileNo, Offset\>             | 데이터 파일 생성 시점의 LSN                                  |
| Create On Disk (PingPong 0)         | Created\|None                   | 0번 체크포인트 이미지 파일 생성 유무                         |
| Create On Disk (PingPong 1)         | Created\|None                   | 1번 체크포인트 이미지 파일 생성 유무                         |
| ChangeTracking DataFileDescSlot ID  | 0 \~ unsigned int 타입의 최대값 | Memory checkpoint image와 묶여있는 ChangeTracking의 DataFileDescSlot ID |

##### [DISK DATABASE FILE ATTRIBUTE]

디스크 테이블스페이스의 데이터 파일 저장 경로를 나타낸다. 내용은 다음과 같다.

| 필드 이름                          | 값                                          | 설명                                                          |
|------------------------------------|---------------------------------------------|---------------------------------------------------------------|
| Tablespace ID                      | 0 \~ unsigned int 타입의 최대값             | 테이블스페이스 식별자                                         |
| Database File ID                   | 0 \~ unsigned int 타입의 최대값             | 데이터 파일 식별자                                            |
| Database File Path                 | 문자열                                      | 데이터 파일의 경로                                            |
| Create LSN                         | \< FileNo, Offset\>                         | 데이터 파일이 생성된 시점의 시스템 로그의 마지막 LSN          |
| Database File Status               | 아래 DISK_DATABASE_FILE_ATTRIBUTE 설명 참조 | 파일의 상태                                                   |
| Autoextend Mode                    | AutoExtend\| Non-AutoExtend                 | 자동 확장 설정 여부                                           |
| Create Mode                        | 0\|1                                        | 0: 재사용 1: 새로 생성한 파일                                 |
| Initialize Size                    | 0 \~ unsigned int 타입의 최대값             | 초기 크기(MByte)                                              |
| Current Size                       | 0 \~ unsigned int 타입의 최대값             | 현재 크기(MByte)                                              |
| Next Size                          | 0 \~ unsigned int 타입의 최대값             | 확장 단위 크기(MByte)                                         |
| Maximum Size                       | 0 \~ unsigned int 타입의 최대값             | 최대 크기(MByte)                                              |
| ChangeTracking DataFileDescSlot ID | 0 \~ unsigned int 타입의 최대값             | Disk datafile과 묶여있는 ChangeTracking의 DataFileDescSlot ID |

[DISK DATABASE FILE ATTRIBUTE] 내용 중 Database File Status의 의미는 다음과 같다.

| 값           | 설명                    |
|--------------|-------------------------|
| OFFLINE      | 오프라인 상태           |
| ONLINE       | 온라인 상태             |
| CREATING     | 생성 중                 |
| BACKUP_BEGIN | 백업을 시작한 상태      |
| BACKUP_END   | 백업을 종료 중인 상태   |
| DROPPING     | 삭제 중인 상태          |
| RESIZING     | 크기를 바꾸고 있는 상태 |
| DROPPED      | 삭제된 상태             |

다음은 dumpla의 출력 결과 중 일부분을 예로 보인 것이다.

```
[ DISK DATABASE FILE ATTRIBUTE ]
Tablespace ID                  [ 2 ]
Database File ID               [ 0 ]
Database File Path C:\altibase_home\dbs\system001.dbf]
Create LSN                     [0, 4443 ]
Database File Status           [ ONLINE ]
Autoextend Mode                [ Non-Autoextend ]
Create Mode                    [ 0 ]
Initialize Size                [10 MBytes(1280 Pages)]
Current Size                   [10 MBytes(1280 Pages)]
Next Size                      [0 MBytes(0 Pages)]
Maximum Size                   [0 MBytes(0 Pages)]
```



##### [Change Tracking ATTRIBUTE]

changeTracking 파일에 대한 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                     | 값                                     | 설명                                                |
|-------------------------------|----------------------------------------|-----------------------------------------------------|
| Last Flush LSN                | FileNo, Offset                         | 메모리상의 변경된 데이터가 파일로 기록된 시점의 LSN |
| Change Tracking Manager State | 문자열 ex) CHANGE TRACKING MGR ENABLED | 페이지 변경 추적 기능의 상태                        |
| Change Tracking File Name     | 문자열                                 | 변경 추적 파일의 경로                               |

##### [Backup Info ATTRIBUTE]

backupinfo 파일에 대한 정보를 나타낸다. 내용은 다음과 같다.

| 필드 이름                    | 값                                     | 설명                                                  |
|------------------------------|----------------------------------------|-------------------------------------------------------|
| Delete Archivelog File Range | FileNo, Offset                         | 삭제해도 완전 복구가 가능한 아카이브 로그 파일의 번호 |
| Last Backup LSN              | FileNo, Offset                         | 최근에 수행된 백업 시점의 LSN                         |
| Before Backup LSN            | FileNo, Offset                         | 최근에 수행된 백업이전에 수행된 LSN                   |
| Backup Info Manager State    | 문자열 예) BACKUP INFO MGR INITIALIZED | 백업 정보 파일 관리자의 상태                          |
| Backup Directory Path        | 문자열 예) /backup_dir/                | 백업 경로                                             |
| Backup Info File Name        | 문자열                                 | 백업 정보 파일 이름                                   |

## dumplf

### 개요

Altibase는 복구를 위해서 트랜잭션이 변경 연산(INSERT, DELETE, UPDATE 등)을 수행할 때, 데이터베이스 영역(DB File)외의 별도 파일에 로그를 남긴다. 이 로그는 IO 최소화를 위해서 이진(binary) 형식으로 기록되어 있다. 이 로그가 기록되는 로그 파일은 altibase.properties의 LOG_DIR 프로퍼티에 설정되는 디렉토리에 logfile\#(\#은 로그파일 번호로 계속 증가한다) 형태로 저장된다.

dumplf는 이 로그 파일의 내용을 텍스트 형식으로 변환해서 보여주는 유틸리티이다. 이 로그를 통해서 데이터베이스에 수행된 연산의 종류 및 변경 연산을 수행하는 트랜잭션의 빈도를 측정할 수 있다.

```
dumplf {-f log_file_name} [-t transaction_id][-s] [-l][-S lsn [-F path] [-g]]
```



### 구문

![](media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06979" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4338" image_path_raw="media/Utilities/cf929d8b05f4569ae6f63eab0d68f8bc.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumplf ::=
    dumplf -f log_file
        [ -t transaction_id ]
        [ -s ]
        [ -l ]
        [ -S lsn [ -F path ] [ -g ] ]
```
<!-- IMG_RECOVERY_END ref_id="img-06979" -->


### 파라미터

| 파라미터 | 설명                                                                                                                                                         |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \-f      | 출력할 로그 파일의 이름                                                                                                                                      |
| \-t      | 출력할 로그에 해당하는 트랜잭션 ID                                                                                                                           |
| \-s      | 로그 파일의 헤더만 출력하고자 할 때 명시                                                                                                                     |
| \-l      | 로그의 유형 (LT 필드) 또는 서브로그유형 (OPTYPE 과 UTYPE 필드)과 관련된 정보만 출력                                                                          |
| \-S      | MMDB에서 INSERT, UPDATE, DELETE, COMMIT, ROLLBACK의 로그 개수를 출력한다. 특정 lsn을 입력하면 해당 lsn 이후의 로그만, '0,0'을 입력하면 전체 로그를 보여준다. |
| \-F      | 로그를 분석할 대상 경로를 지정할 수 있으며, 생략할 경우 \$ALTIBASE_HOME/logs 의 경로를 분석한다.                                                             |
| \-g      | 테이블의 오브젝트 ID별 통계가 전체 통계 정보와 함께 출력된다. 생략하면 전체 통계 정보만 출력된다.                                                            |

### 설명

로그 파일의 내용을 텍스트 형식으로 변환해서 보여준다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ dumplf -f logfile0
```



### 출력 항목

다음은 dumplf의 출력 예이다.

```
LSN=<0,820>, COMP:N, MAGIC:820, TID: 6400,BE: N, REP: Y, ISVP: N, ISVP_DEPTH: 0 PLSN=<0,739>, LT: SMR_LT_MEMTRANS_COMMIT, SZ: 45
```

로그 파일의 내용 중, 필드들은 다음과 같은 의미를 갖는다.

| 필드 이름               | 값                                                                             | 설명                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LSN                     | 형식: ( FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값 ,         | 로그의 sequence number로 로그의 물리적인 위치를 표시한다. LSN은 파일 번호, 오프셋으로 구성된다.                                                                                           |
| COMP                    | Y\|N                                                                           | Y: 로그가 압축(compress)되었음 N: 압축되지 않음                                                                                                                                           |
| MAGIC                   | 0 - unsigned short 타입의 최대값                                               | 로그 레코드가 유효하다는 것을 나타내기 위해서 로그 LSN의 로그 파일 번호와 오프셋으로 이 값을 만들고 Redo, Undo시 로그를 읽었을 때 이 값이 현재 로그의 LSN과 동일한지 검사한다.            |
| TID                     | 0 - unsigned int 타입의 최대값                                                 | 트랜잭션 식별자                                                                                                                                                                           |
| BE                      | Y\|N                                                                           | Y : Begin Transaction Log                                                                                                                                                                 |
| REP                     | Y\|N                                                                           | Y: 이중화가 걸려있는 경우 Sender가 Standby로 보내거나 참조하는 로그이다. N: Sender는 이 로그를 무시한다                                                                                   |
| ISVP                    | Y\|N                                                                           | Y: 묵시적 저장점 (Implicit Savepoint) 로그. 문장(Statement) 시작 후 처음으로 찍힌 로그이다. 트랜잭션이 문장을 수행했을 때 오류가 발생하면 이 로그까지 부분 철회(Partial Rollback)을 한다. |
| ISVP_DEPTH              | 0 - 255                                                                        | 어떤 SQL 구문이 다른 구문 내에 중첩되었을 때 묵시적 저장점의 중첩 깊이                                                                                                                    |
| PLSN                    | 형식: (FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값            | Previous Log LSN으로 이 값을 이용하여 같은 트랜잭션이 기록한 로그들끼리 체인(Chain)으로 연결되어 있다.                                                                                    |
| LT                      | 문자열                                                                         | 로그의 유형을 나타낸다. 자세한 내용은 아래 로그 유형에 대한 표를 참고한다.                                                                                                                |
| SZ                      | 0 - unsigned int 타입의 최대값                                                 | 로그 크기 (단위: bytes)                                                                                                                                                                   |
| RdSz                    | 0 - unsigned int 타입의 최대값                                                 | 로그 레코드의 크기 (단위: bytes)                                                                                                                                                          |
| DMIOff                  | 0 - unsigned int 타입의 최대값                                                 | 논리적 로그의 위치. 트랜잭션 언두 또는 이중화에서 사용한다.                                                                                                                               |
| TableOID                | 0 - unsigned int 타입의 최대값                                                 | 테이블의 오브젝트 ID                                                                                                                                                                      |
| OID                     | 0 - unsigned int 타입의 최대값                                                 | 테이블을 제외한 모든 오브젝트의 ID. 레코드 오브젝트도 포함한다.                                                                                                                           |
| ContType                | 0, 1                                                                           | 이중화를 위해 사용하는 내부 값                                                                                                                                                            |
| OPTYPE                  | LogTypeName\<LogTypeNumber\>                                                   | Nested Top Action (NTA) 로그의 작업 유형                                                                                                                                                  |
| AFTER                   | SZ: \<size\>, Value: \<value\>                                                 | 로그 레코드의 변경 후 이미지 (after image)                                                                                                                                                |
| BEFORE                  | SZ: \<size\>, Value: \<value\>                                                 | 로그 레코드의 변경 전 이미지 (before image)                                                                                                                                               |
| UTYPE                   | LogTypeName\<LogTypeNumber\>                                                   | UPDATE 로그의 작업 유형                                                                                                                                                                   |
| UPOS                    | 형식: (SPACEID:\<SpaceID\>, PID:\<PageID\>, OFFSET:\<Offset\> =\> OID:\<OID\>) | 변경된 객체의 주소. 또한 변경 작업 동안 발생한 정보도 포함한다.                                                                                                                           |
| SPACEID                 | 0 - unsigned short 타입의 최대값                                               | 변경된 객체를 포함하고 있는 테이블스페이스의 ID                                                                                                                                           |
| PID                     | 0 - unsigned int 타입의 최대값                                                 | 변경된 객체를 포함하고 있는 페이지의 ID                                                                                                                                                   |
| Offset                  | 0 - unsigned int 타입의 최대값                                                 | 변경된 객체를 포함하고 있는 페이지 내에서의 offset                                                                                                                                        |
| FLISlot PrevPID NextPID | 형식: (\<BeforePID\> =\> \<AfterPID\>)                                         | 메모리 테이블스페이스를 관리하기 위해 사용하는 내부 값                                                                                                                                    |
| ESLSN                   | 형식: (FileNo, Offset) 각 값의 범위: 0 - unsigned int 타입의 최대값            | 복구 수행 시 시작할 LSN                                                                                                                                                                   |
| Lob Locator             | 0 - unsigned long 타입의 최대값                                                | 이중화에서 LOB타입과 관련해서 내부적으로 사용하는 값                                                                                                                                      |

dumplf의 결과 중 LT (Log Type: 로그 유형)의 의미는 다음과 같다.

| 값                        | 설명                                        |
|---------------------------|---------------------------------------------|
| SMR_LT_DUMMY              | Dummy 로그                                  |
| SMR_LT_CHKPT_BEGIN        | Checkpoint Begin 로그                       |
| SMR_LT_DIRTY_PAGE         | Dirty Page 로그                             |
| SMR_LT_CHKPT_END          | Checkpoint End 로그                         |
| SMR_LT_MEMTRANS_COMMIT    | Memory Transaction Commit 로그              |
| SMR_LT_MEMTRANS_ABORT     | Memory Transaction Abort 로그               |
| SMR_LT_DSKTRANS_COMMIT    | Disk Transaction Commit 로그                |
| SMR_LT_DSKTRANS_ABORT     | Disk Transaction Abort 로그                 |
| SMR_LT_SAVEPOINT_SET      | Savepoint Set 로그                          |
| SMR_LT_SAVEPOINT_ABORT    | Savepoint Abort Begin 로그                  |
| SMR_LT_XA_PREPARE         | XA Prepare 로그                             |
| SMR_LT_TRANS_PREABORT     | Abort Begin 로그                            |
| SMR_LT_DDL                | DDL (Data Definition Language) 로그         |
| SMR_LT_XA_SEGS            | XA Prepare Transaction Segment Information  |
| SMR_LT_LOB_FOR_REPL       | 이중화를 위한 LOB 로그                      |
| SMR_LT_UPDATE             | MMDB(Main Memory Database) Update 로그      |
| SMR_LT_NTA                | MMDB NTA(Nested Top Action) 로그            |
| SMR_LT_COMPENSATION       | Compensation 로그                           |
| SMR_LT_DUMMY_COMPENSATION | Dummy Compensation 로그                     |
| SMR_LT_FILE_BEGIN         | File Begin 로그                             |
| SMR_LT_FILE_TBS_UPDATE    | Tablespace Update 로그                      |
| SMR_LT_FILE_END           | File End 로그                               |
| SMR_DLT_READONLY          | DRDB(Disk Resident Database) Redo Only 로그 |
| SMR_DLT_UNDOABLE          | DRDB Undo 로그                              |
| SMR_DLT_NTA               | DRDB NTA 로그                               |
| SMR_DLT_COMPENSATION      | DRDB Compensation 로그                      |
| SMR_DLT_REF_NTA           | DRDB Reference NTA 로그                     |
| SMR_LT_TABLE_META         | 이중화를 위한 테이블 메타 로그              |

OPTYPE 과 UTYPE 에 가능한 로그 타입 이름

| 값                                                           | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| SMR_OP_SMM_PERS_LIST_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_ALLOC <br />SMR_OP_SMC_VAR_SLOT_ALLOC <br />SMR_OP_SMC_FIXED_SLOT_FREE <br />SMR_OP_SMC_VAR_SLOT_FREE | MMDB의 페이지와 슬롯에 관련된 로그                           |
| SMR_OP_CREATE_TABLE <br />SMR_OP_CREATE_INDEX <br />SMR_OP_DROP_INDEX <br />SMR_OP_ALTER_TABLE <br />SMR_OP_SMM_CREATE_TBS <br />SMR_OP_INSTANT_AGING_AT_ALTER_TABLE <br />SMR_OP_SMC_TABLEHEADER_ALLOC | MMDB에서 DDL 구문 수행과 관련된 로그                         |
| SMR_MEM_LOB_CURSOR_OPEN <br />SMR_DISK_LOB_CURSOR_OPEN <br />SMR_LOB_CURSOR_CLOSE <br />SMR_PREPARE4WRITE <br />SMR_FINISH2WRITE | MMDB에서 LOB 데이터 제어와 관련된 로그                       |
| SDR_OP_SDP_CREATE_TABLE_SEGMENT <br />SDR_OP_SDP_CREATE_LOB_SEGMENT <br />SDR_OP_SDP_CREATE_INDEX_SEGMENT <br />SDR_OP_SDP_ADD_LOB_PAGE_TO_AGINGLIST <br />SDR_OP_SDC_ALLOC_UNDO_PAGE <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTENT_FROM_TBS <br />SDR_OP_SDPTB_ALLOCATE_AN_EXTDIR_FROM_LIST <br />SDR_OP_SDPTB_RESIZE_GG <br />SDR_OP_SDPST_ALLOC_PAGE <br />SDR_OP_SDPSF_ALLOC_PAGE <br />SCT_UPDATE_MRDB_CREATE_TBS <br />SCT_UPDATE_MRDB_CREATE_CIMAGE_FILE <br />SCT_UPDATE_MRDB_DROP_TBS <br />SCT_UPDATE_MRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_MRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_MRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_TBS <br />SCT_UPDATE_DRDB_DROP_TBS <br />SCT_UPDATE_DRDB_ALTER_TBS_ONLINE <br />SCT_UPDATE_DRDB_ALTER_TBS_OFFLINE <br />SCT_UPDATE_DRDB_CREATE_DBF <br />SCT_UPDATE_DRDB_DROP_DBF <br />SCT_UPDATE_DRDB_EXTEND_DBF <br />SCT_UPDATE_DRDB_SHRINK_DBF <br />SCT_UPDATE_DRDB_AUTOEXTEND_DBF <br />SCT_UPDATE_DRDB_ALTER_DBF_ONLINE <br />SCT_UPDATE_DRDB_ALTER_DBF_OFFLINE <br />SCT_UPDATE_VRDB_CREATE_TBS <br />SCT_UPDATE_VRDB_DROP_TBS <br />SCT_UPDATE_VRDB_ALTER_AUTOEXTEND <br />SCT_UPDATE_COMMON_ALTER_ATTR_FLAG | 테이블스페이스와 세그먼트에 관련된 로그                      |
| SDR_OP_SDPST_UPDATE_WMINFO_4DPATH <br />SDR_OP_SDPST_UPDATE_MFNL_4DPATH <br />SDR_OP_SDPST_UPDATE_BMP_4DPATH <br />SDR_OP_SDPSF_ADD_PIDLIST_PVTFREEPIDLIST_4DPATH <br />SDR_OP_SDPSF_MERGE_SEG_4DPATH <br />SDR_OP_SDPSF_UPDATE_HWMINFO_4DPATH <br />SDR_OP_SDP_DPATH_ADD_SEGINFOSET | DRDB에서 Direct Page Insert를 위한 페이지 관리와 관련된 로그 |
| SDR_OP_SDN_INSERT_KEY_WITH_NTA <br />SDR_OP_SDN_DELETE_KEY_WITH_NTA | DRDB에서 B-tree 인덱스를 위한 NTA 로그                       |
| SDR_OP_STNDR_INSERT_KEY_WITH_NTA <br />SDR_OP_STNDR_DELETE_KEY_WITH_NTA | DRDB에서 R-tree 인덱스를 위한 NTA 로그                       |
| SDR_SDP_1BYTE <br />SDR_SDP_2BYTE <br />SDR_SDP_4BYTE <br />SDR_SDP_8BYTE <br />SDR_SDP_BINARY | 물리적 DRDB 로그                                             |
| SDR_SDP_PAGE_CONSISTENT <br />SDR_SDP_INIT_PHYSICAL_PAGE <br />SDR_SDP_INIT_LOGICAL_HDR <br />SDR_SDP_INIT_SLOT_DIRECTORY <br />SDR_SDP_FREE_SLOT <br />SDR_SDP_FREE_SLOT_FOR_SID <br />SDR_SDP_RESTORE_FREESPACE_CREDIT <br />SDR_SDP_RESET_PAGE <br />SDR_SDP_WRITE_PAGEIMG <br />SDR_SDP_WRITE_DPATH_INS_PAGE | DRDB의 페이지와 슬롯에 관련된 로그                           |
| SDR_SDPST_INIT_SEGHDR <br />SDR_SDPST_INIT_BMP <br />SDR_SDPST_INIT_LFBMP <br />SDR_SDPST_INIT_EXTDIR <br />SDR_SDPST_ADD_RANGESLOT <br />SDR_SDPST_ADD_SLOTS <br />SDR_SDPST_ADD_EXTDESC <br />SDR_SDPST_ADD_EXT_TO_SEGHDR <br />SDR_SDPST_UPDATE_WM <br />SDR_SDPST_UPDATE_MFNL <br />SDR_SDPST_UPDATE_PBS <br />SDR_SDPST_UPDATE_LFBMP_4DPATH <br />SDR_SDPSC_INIT_SEGHDR <br />SDR_SDPSC_INIT_EXTDIR <br />SDR_SDPSC_ADD_EXTDESC_TO_EXTDIR <br />SDR_SDPTB_INIT_LGHDR_PAGE <br />SDR_SDPTB_ALLOC_IN_LG <br />SDR_SDPTB_FREE_IN_LG | DRDB를 위한 세그먼트와 테이블스페이스에 관련된 로그          |
| SDR_SDC_INSERT_ROW_PIECE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_INSERT_ROW_PIECE_FOR_DELETEUNDO <br />SDR_SDC_UPDATE_ROW_PIECE <br />SDR_SDC_OVERWRITE_ROW_PIECE <br />SDR_SDC_CHANGE_ROW_PIECE_LINK <br />SDR_SDC_DELETE_FIRST_COLUMN_PIECE <br />SDR_SDC_ADD_FIRST_COLUMN_PIECE <br />SDR_SDC_DELETE_ROW_PIECE_FOR_UPDATE <br />SDR_SDC_DELETE_ROW_PIECE SDR_SDC_LOCK_ROW | DRDB의 테이블 레코드 관리에 관련된 로그                      |
| SDR_SDC_UPDATE_LOBDESC <br />SDR_SDC_UPDATE_LOBDESC_KEY <br />SDR_SDC_LOB_WRITE_PIECE <br />SDR_SDC_LOB_WRITE_PIECE4DML <br />SDR_SDC_INIT_LOBPAGE <br />SDR_SDC_LOB_PAGE_TO_AGING_LIST | DRDB에서 LOB 타입 사용에 관련된 로그                         |
| SDR_SDC_PK_LOG                                               | DRDB에서 이중화를 위한 프라이머리 키 사용에 관련된 로그      |
| SDR_SDC_INIT_CTL <br />SDR_SDC_EXTEND_CTL <br />SDR_SDC_BIND_CTS <br />SDR_SDC_UNBIND_CTS <br />SDR_SDC_BIND_ROW <br />SDR_SDC_UNBIND_ROW <br />SDR_SDC_ROW_TIMESTAMPING <br />SDR_SDC_DATA_SELFAGING | DRDB에서 레코드를 위한 MVCC 관련된 로그                      |
| SDR_SDC_BIND_TSS <br />SDR_SDC_UNBIND_TSS <br />SDR_SDC_SET_INITSCN_TO_TSS <br />SDR_SDC_INIT_TSS_PAGE <br />SDR_SDC_INIT_UNDO_PAGE <br />SDR_SDC_INSERT_UNDO_REC<br /> | DRDB에서 Trasaction Status Slots (TSS)과 언두 레코드에 관련된 로그 |
| SDR_SDN_INSERT_INDEX_KEY <br />SDR_SDN_FREE_INDEX_KEY <br />SDR_SDN_INSERT_UNIQUE_KEY <br />SDR_SDN_INSERT_DUP_KEY <br />SDR_SDN_DELETE_KEY_WITH_NTA <br />SDR_SDN_FREE_KEYS <br />SDR_SDN_COMPACT_INDEX_PAGE | DRDB에서 B-tree 인덱스 관련된 로그                           |
| SDR_SDN_MAKE_CHAINED_KEYS <br />SDR_SDN_MAKE_UNCHAINED_KEYS <br />SDR_SDN_KEY_STAMPING <br />SDR_SDN_INIT_CTL <br />SDR_SDN_EXTEND_CTL <br />SDR_SDN_FREE_CTS | DRDB에서 B-tree 인덱스 키를 위한 MVCC에 관련된 로그          |
| SDR_STNDR_MAKE_CHAINED_KEYS <br />SDR_STNDR_MAKE_UNCHAINED_KEYS <br />SDR_STNDR_KEY_STAMPING | DRDB에서 R-tree 인덱스 관련된 로그                           |
| SMR_PHYSICAL                                                 | MMDB에서 물리적 로그                                         |
| SMR_SMM_MEMBASE_SET_SYSTEM_SCN <br />SMR_SMM_MEMBASE_ALLOC_PERS_LIST <br />SMR_SMM_MEMBASE_ALLOC_EXPAND_CHUNK <br />SMR_SMM_PERS_UPDATE_LINK <br />SMR_SMM_PERS_UPDATE_NEXT_FREE_PAGE_LINK <br />SMR_SMM_MEMBASE_INFO | MMDB에서 기본 정보와 관련된 로그                             |
| SMR_SMC_TABLEHEADER_INIT <br />SMR_SMC_TABLEHEADER_UPDATE_INDEX <br />SMR_SMC_TABLEHEADER_UPDATE_COLUMNS <br />SMR_SMC_TABLEHEADER_UPDATE_INFO <br />SMR_SMC_TABLEHEADER_SET_NULLROW <br />SMR_SMC_TABLEHEADER_UPDATE_ALL <br />SMR_SMC_TABLEHEADER_UPDATE_ALLOCINFO <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG <br />SMR_SMC_TABLEHEADER_SET_SEQUENCE <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_COLUMN_COUNT <br />SMR_SMC_TABLEHEADER_UPDATE_TABLE_SEGMENT <br />SMR_SMC_TABLEHEADER_UPDATE_FLAG_FOR_MEDIA_RECV <br />SMR_SMC_TABLEHEADER_SET_SEGSTOATTR <br />SMR_SMC_TABLEHEADER_SET_INSERTLIMIT <br />SMR_SMC_INDEX_SET_FLAG <br />SMR_SMC_INDEX_SET_SEGATTR <br />SMR_SMC_INDEX_SET_SEGSTOATTR <br />SMR_SMC_INDEX_SET_DROP_FLAG | MMDB에서 테이블 헤더와 인덱스 헤더에 관련된 로그             |
| SMR_SMC_PERS_INIT_FIXED_PAGE <br />SMR_SMC_PERS_INIT_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW <br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_FREE<br />SMR_SMC_PERS_UPDATE_FIXED_ROW_NEXT_VERSION <br />SMR_SMC_PERS_SET_FIX_ROW_DROP_FLAG <br />SMR_SMC_PERS_SET_FIX_ROW_DELETE_BIT <br />SMR_SMC_PERS_INIT_VAR_PAGE <br />SMR_SMC_PERS_UPDATE_VAR_ROW_HEAD <br />SMR_SMC_PERS_UPDATE_VAR_ROW <br />SMR_SMC_PERS_SET_VAR_ROW_FLAG <br />SMR_SMC_PERS_SET_VAR_ROW_NXT_OID <br />SMR_SMC_PERS_WRITE_LOB_PIECE <br />SMR_SMC_PERS_INSERT_ROW <br />SMR_SMC_PERS_UPDATE_INPLACE_ROW <br />SMR_SMC_PERS_UPDATE_VERSION_ROW<br /> SMR_SMC_PERS_DELETE_VERSION_ROW | MMDB에서 테이블 레코드와 관련된 로그                         |

MVCC와 관련된 자세한 설명은 *Administrator’s Manual* 을 참고하기 바란다.

## dumptrc 

### 개요

Altibase 서버가 비정상 종료될 때 \$ALTIBASE_HOME/trc 디렉토리에 기록되는 트레이스 로그 파일을 사용자가 식별할 수 있는 형태로 변환하여 출력한다.

```
dumptrc [-h |[-p file_path][-c [-s]]
[-a|-i file_name [-i file_name]..|-e file_name [-e file_name]..] [-n file_count] [-x] |-f |-v]
```



### 구문

![](media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06980" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4483" image_path_raw="media/Utilities/8d31776c2bc3e1d547efa1715f6899f7.png" image_class="C" format="bnf" verified="True" -->
```bnf
dumptrc ::=
    dumptrc
        [ -h
        | -p file_path [ -c [ -s ] ]
          { -a | -i file_name { -i file_name } | -e file_name { -e file_name } }
          [ -n line_count ]
          [ x ]
        | -f
        | -v ]
```
<!-- IMG_RECOVERY_END ref_id="img-06980" -->


### 파라미터

| 파라미터 | 설명                                                         |
| -------- | ------------------------------------------------------------ |
| \-h      | 도움말을 출력한다. 파라미터를 생략하거나 다른 파라미터와 중복하여 사용할 경우 도움말이 우선한다. |
| \-p      | 트레이스 로그 파일을 가져오는 경로를 지정한다. 경로를 지정하지 않으면 기본적으로 \$ALTIBASE_HOME/trc 디렉토리의 로그 파일을 가져온다. |
| \-c      | altibase_error.log에 기록된 ALTIBASE 프로세스 콜 스택을 사용자가 식별할 수 있는 함수명으로 변환하여 출력한다. 콜 스택의 주소를 함수명으로 변경하지 않으려면 -s 옵션를 사용한다. 파라미터 -a, -i, -e, -n과 함께 사용하지 않으면 콜 스택만 기록된다. |
| \-s      | 트레이스 로그에 기록된 콜 스택만을 출력하고 함수명으로 변경하지 않는다. |
| \-a      | 트레이스 로그 파일의 전부를 정렬하여 출력한다.               |
| \-i      | 지정하는 트레이스 로그 파일을 출력한다. 복수의 로그 파일이 출력 가능하다. '-e' 파라미터와 함께 사용할 수 없다. |
| \-e      | 지정한 트레이스 로그 파일을 제외한 모든 파일을 출력한다. 반복하여 복수의 로그 파일을 제거할 수 있으며, '-i' 파라미터와 함께 사용할 수 없다. |
| \-n      | 한 번에 출력할 로그의 개수를 지정한다. 1\~127개의 로그를 출력할 수 있으며, 지정하지 않으면 10개의 로그가 출력된다. |
| \-f      | 트레이스 로그 파일이 기록될 때마다 추가되는 로그 메세지를 출력한다. |
| -x       | altibase버전과 dumptrc버전이 틀린 경우도 콜 스택을 출력한다. |
| \-v      | dumptrc의 버전을 출력한다.                                   |

### 설명

프로세스 콜 스택에는 Altibase 종료 당시 수행되던 Altibase 내부 모듈에 대한 정보가 기록된다. dumptrc를 이용하여 가져올 수 있는 트레이스 로그 파일은 \$ALTIBASE_HOME/trc 디렉터리에 기록되는 아래의 파일들을 사용할 수 있다.

-   ERROR : altibase_error.log
-   SERVER : altibase_boot.log
-   SM : altibase_sm.log
-   RP : altibase_rp.log
-   QP : altibase_qp.log
-   JOB : altibase_job.log
-   DK : altibase_dk.log
-   DR : altibase_dr.log
-   XA : altibase_xa.log
-   MM : altibase_mm.log
-   RP_CONFLICT : altibase_rp_conflict.log
-   DUMP : altibase_dump.log
-   TRC : altibase_trace.log
-   SNMP : altibase_snmp.log
-   CM : altibase_cm.log
-   MISC : altibase_misc.log
-   SD : altibase_sd.log

만약 \$ALTIBASE_HOME/trc가 아닌 다른 경로에 있는 트레이스 로그 파일을 출력할 때에는 '-p'를 사용하여 경로를 변경할 수 있다.

Altibase 서버가 비정상 종료할 경우, 프로세스 콜 스택을 dumptrc로 변환하여 Altibase 기술서비스 팀에 송부하면, 보다 빨리 문제를 해결할 수 있을 것이다.

### 주의 사항

 Altibase의 실행 파일의 버전과 dumptrc의 버전이 동일해야 정확한 콜 스택 정보를 확인할 수 있다.버전이 틀릴 경우는 잘못된 값이 나올 수 있기 때문에 기본적으로 경고메시지를 보여주고 콜 스택을 출력하지 않는다. 버전이 틀릴때도 강제로 콜스택을 출력하기 위해서는 -x옵션을 사용하면 된다.

### 사용예

altibase_error.log와 altibase_boot.log를 묶어서 출력한다.

```
$ dumptrc -i server -i error
[2015/10/21 17:29:42 55C][PID:32702][Thread-2]
  ==> Initialize Disaster Recovery Manager  
[2015/10/21 17:29:42 55D][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 55E][PID:32702][Thread-2]
  ==> Initialize MMX Service  
[2015/10/21 17:29:42 55F][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 560][PID:32702][Thread-2]
  ==> Initialize Audit Service  
[2015/10/21 17:29:42 561][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 562][PID:32702][Thread-2]
  ==> Initialize Job Manager  
[2015/10/21 17:29:42 563][PID:32702][Thread-2]
  ... [SUCCESS] 
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF
Caller[1] 0000000000426CFE
Caller[2] 00007FD306FD4CB0
Caller[3] 00007FD30609F763
Caller[4] 000000000042F66F
Caller[5] 00000000004213CE
Caller[6] 000000000041D1E0
Caller[7] 00007FD305FD376D
Caller[8] 00000000004206BD
END-STACK =======================================
10 logs printed.
```

error.log만 제외하고 출력한다.

```
$ dumptrc -e error
[2015/10/21 17:29:48 571][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:48 572][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 573][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:49 574][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:49 575][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:49 576][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 577][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : CREATE TABLE T1 ( I1 INTEGER )]
[2015/10/21 17:29:53 578][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:53 579][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
[2015/10/21 17:29:53 57A][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
10 logs printed.
```

콜 스택과 altibase_boot.log, altibase_sm.log을 함께 출력하되 상위 20개 로그를 출력한다.

```
$ dumptrc -c -i error -i server -i sm -n 20
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:42 551][PID:32702][Thread-2]
  ==> Initialize Security Module  
[2015/10/21 17:29:42 552][PID:32702][Thread-2]
  ... [SUCCESS] 
...
[2015/10/21 17:29:42 564][PID:32702][Thread-2]
--- STARTUP Process SUCCESS ---
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
Caller[3] 00007FD30609F763  => not found
Caller[4] 000000000042F66F  => mmtSessionManager::run()
Caller[5] 00000000004213CE  => mmi::serverStart(int, int)
Caller[6] 000000000041D1E0  => main
Caller[7] 00007FD305FD376D  => not found
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```

다른 디렉토리의 trc 로그에서 콜 스택을 가져와서 출력한다.

```
$ dumptrc -p /home/djin/work/altidev4/trunk/altibase_home/trc -c -n 20

Path : /home/djin/work/altidev4/trunk/altibase_home/trc
=================================================
= Callstack Information 0
=================================================
[2015/10/21 17:29:45 568][PID:32702][Thread-2]
[EXEC_DDL_END : SUCCESS]
[2015/10/21 17:29:45 569][PID:32702][Thread-2]
[EXEC_DDL_BEGIN : DROP TABLE T1]
...
[2015/10/21 17:30:51 57B] Dump of Stack
SIGNAL INFORMATION ==============================
Signal 6(SIGABRT) caught.
    Sent by process : 2331
    Sent by user    : 1000
BEGIN-DUMP ======================================
===== SERVER =====
ALTIBASE hdb
    Product version  : 6.7.1.0.0
    CPU              : X86
    Operating System : x86_64-unknown-linux-gnu
    Process ID       : 32698
    Thread No        : 0
END-DUMP ========================================
BEGIN-STACK [CRASH] =============================
Caller[0] 00000000011E0EBF  => iduStack::dumpStack(iduSignalDef const*, siginfo*, ucontext*)
Caller[1] 0000000000426CFE  => mmmSignalHandler
Caller[2] 00007FD306FD4CB0  => not found
...
Caller[8] 00000000004206BD  => _start
END-STACK =======================================
20 logs printed.

```



## killCheckServer

### 개요

killCheckServer는 실행 중인 checkServer를 종료한다.

```
killCheckServer
```



### 구문

![killcheckserver](media/Utilities/killcheckserver.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06981" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4708" image_path_raw="media/Utilities/killcheckserver.gif" image_class="C" format="bnf" verified="True" -->
```bnf
killcheckserver ::=
    killCheckServer
```
<!-- IMG_RECOVERY_END ref_id="img-06981" -->


### 설명

killCheckServer는 실행 중인 checkServer를 종료한다.

server stop 또는 server kill 명령을 사용해서 Altibase 서버를 종료할 경우, checkServer가 동작 중이라면 서버 종료 전에 먼저 server 스크립트 내에서 killCheckServer가 checkServer의 동작을 동작을 멈추도록 되어 있다. 그리고, \$ALTIBASE_HOME/trc 디렉토리의 killCheckServer.log 파일에 killCheckServer 수행 결과가 아래와 같이 기록된다.

- checkServer가 동작 중일 때:

  ```
  checkServer killed.
  ```


- checkServer가 동작 중이 아닐 때:

  ```
  ERROR CODE : -27
  ```


그러나, 사용자가 직접 killCheckServer 명령어를 실행할 경우에는 killCheckServer.log에 수행 결과가 기록되지 않는다.

### 사용예

쉘 프롬프트 상에서 다음과 같이 수행한다.

```
$ killCheckServer
```



## server

### 개요

Altibase 데이터베이스의 생성, 구동 및 종료시키기 위한 쉘 스크립트이다.

```
server { start | stop | restart | kill | status | create db_charset national_charset | startRoleManager | stopRoleManager } 
```



### 구문

![server](media/Utilities/server.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-06982" source_md="Manuals/Altibase_trunk/kor/Utilities Manual.md" line_no="4756" image_path_raw="media/Utilities/server.gif" image_class="C" format="bnf" verified="True" -->
```bnf
server ::=
    'server' { 'start'
             | 'stop'
             | 'restart'
             | 'kill'
             | 'status'
             | 'create' db_charset national_charset
             | 'startRoleManager'
             | 'stopRoleManager' }
```
<!-- IMG_RECOVERY_END ref_id="img-06982" -->


### 파라미터

| 파라미터         | 설명                                                                      |
|------------------|---------------------------------------------------------------------------|
| start            | Altibase 프로세스를 구동한다.                                             |
| stop             | Altibase 프로세스를 종료한다.                                             |
| restart          | Altibase 프로세스를 재구동한다.                                           |
| kill             | Altibase 프로세스를 강제 종료한다.                                        |
| status           | 데이터베이스 내의 테이블 목록을 출력한다.                                 |
| create           | 크기 10M, 노아카이브 로그로 입력된 캐릭터 셋으로 데이터베이스를 생성한다. |
| startRoleManager | Altibase 프로세스를 Disaster Recovery의 역할 관리자로서 구동한다.         |
| stopRoleManager  | 역할 관리자를 종료한다.                                                   |

### 설명

Altibase의 구동 및 종료, 데이터베이스 생성은 iSQL상에서 SQL 구문으로 수행해야 한다. Altibase는 사용자 편의를 위해 관리자가 자주 사용하는 이러한 구문들을 묶어서 쉘 스크립트 파일 형태로 제공한다.

server 스크립트가 제공하는 기능은 다음과 같다.

-   Altibase 프로세스의 구동

-   Altibase 프로세스의 종료

-   Altibase 프로세스의 재구동

-   Altibase 프로세스의 강제 종료

-   “SELECT \* FROM TAB;” 결과 출력

-   Altibase 데이터베이스 생성

-   Altibase 프로세스를 역할 관리자로 구동

-   역할 관리자 종료

Altibase 관리를 위한 SQL 구문에 대한 자세한 내용은 *SQL Reference*를 참조한다.

### 사용예

사용 방법은 다음과 같다.

```
$ server start
$ server restart
$ server stop
$ server status
$ server kill
$ server create ksc5601 utf16
$ server startRoleManager
$ server stopRoleManager
```



### 참고사항

*Administrator’s Manual*, *SQL Reference*를 참고하기 바란다.
<!-- SOURCE_BLOCK_END source_id="SRC-000197" block_id="BLOCK-000931" -->

## SRC-000215 - Release 7.1

| Field | Value |
| --- | --- |
| `source_id` | SRC-000215 |
| `source_path` | Manuals/Tools/Altibase_trunk/eng/Altibase Heartbeat User's Guide.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | en |
| `authority_label` | English extraction aid; Altibase 8.1 verified source |
| `source_sha256` | 20d8a0d460577531367d960f4a6cd1413090483890d9511b7d87dcd7f5c161b3 |
| `byte_count` | 28334 |
| `line_count` | 694 |
| `estimated_tokens` | 7048 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000215" source_path="Manuals/Tools/Altibase_trunk/eng/Altibase Heartbeat User&#x27;s Guide.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="en" authority_label="English extraction aid; Altibase 8.1 verified source" sha256="20d8a0d460577531367d960f4a6cd1413090483890d9511b7d87dcd7f5c161b3" byte_count="28334" line_count="694" estimated_tokens="7048" block_id="BLOCK-000932" -->
Altibase Heartbeat User's Guide
================

#### Release 7.1

Altibase® Tool & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>



<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. -->  

<pre>
Altibase Tool & Utilities Altibase HeartBeat User's Guide
Release 7.1
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the
software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>


<br>

# Table Of Contents

- [Preface](#preface)
  - [About This Manual](#about-this-manual)
- [1. Introduction to Altibase Heartbeat](#1-introduction-to-altibase-heartbeat)
  - [Overview of Altibase Heartbeat](#overview-of-altibase-heartbeat)
  - [Altibase Heartbeat Procedure](#altibase-heartbeat-procedure)
- [2. Commands](#2-commands)
  - [aheartbeat](#aheartbeat)
- [3. Configuring Altibase Heartbeat](#3-configuring-altibase-heartbeat)
  - [Configuration](#configuration)
  - [Configuring an Altibase Heartbeat System : A Practice Example](#configuring-an-altibase-heartbeat-system--a-practice-example)
- [4. Altibase Heartbeat Process](#4-altibase-heartbeat-process)
  - [aheartbeat Status](#aheartbeat-status)
  - [Determing Failure](#determing-failure)
  - [Role of aheartbeat 0](#role-of-aheartbeat-0)
  - [Failover and Failback](#failover-and-failback)
  - [Logging](#logging)

<br>

Preface
====

### About This Manual

This guide describes how to use the Altibase Heartbeat utility in a distributed database environment.

#### Audience

This manual has been prepared for the following Altibase users:

-   Database administrators
-   Performance administrators
-   Database users
-   Application developers
-   Technical Supporters

It is recommended for those reading this manual possess the following background knowledge:

-   Basic knowledge in the use of computers, operating systems, and operating system utilities
-   Experience in using relational database and an understanding of database concepts
-   Computer programming experience
-   Experience in database server management, operating system management, or network administration

#### Organization

The manual is organized as follows:

-   Chapter 1: Introduction to Altibase heartbeat  
    This chapter introduces Altibase Heartbeat and describes its basic procedure.

-   Chapter 2: Commands  
    This chapter explains Altibase Heartbeat commands

-   Chapter 3: Configuring Altibase Heartbeat  
    This chapter describes how to configure Altibase Heartbeat, and how to configure a distributed database environment with Altibase Heartbeats.
    
-   Chapter 4: Altibase Heartbeat Process  
    This chapter explains the Altibase Heartbeat process in details. On which criteria Altibase Heartbeat determines failure, and once failure is detected, how Failover is performed are examined.

#### Documentation Convention

This section describes the convention used in this manual. Understanding this convention will make it easier to find information in this manual and in the other manuals in the series. 

This convention described here is as follow: 

- Sample Code Convention

##### Sample Code Conventions

The code examples explain SQL statements, stored procedures, iSQL statements, and other command line syntax.

The following table describes the printing conventions used in the code examples.

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL\> SELECT ename FROM employee;<br/> ENAME<br/>  -----------------------<br/> SWNO<br/>  HJNO<br/>  HSCHOI<br/>  .<br/> .<br/> .<br/> 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code. | EXEC :p1 := 1; acc NUMBER(11,2)                              |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT \* FROM *table_name*; <br/>CONNECT *userID*/*password*; |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### Related Documentations

For more detailed information, please refer to the following documents.

-   Getting Started Guide

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   Stored Procedures Manual

-   Error Message Reference

#### Altibase Welcomes Your Comments and Feedbacks

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there is any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](http://support.altibase.com/en/).

Thank you. We always welcome your feedbacks and suggestions.

<br>

# 1. Introduction to Altibase Heartbeat

This chapter introduces the Altibase Heartbeat and describes its basic procedure.

### Overview of Altibase Heartbeat

The Altibase Heartbeat utility detects node failures in a distributed database environment and enables the DBA to counter failures. aheartbeat[^1]  can be utilized in an environment where Altibase servers are connected through replication. 

[^1]: aheartbeat has detected failure on the other node, this file is executed for remote node Failover. This file can be either an executable binary or script file.


Therefore, Altibase Heardbeat and aheartbeat are used interchageably in this document. 

#### Altibase Heartbeat Components

Altibase Heartbeat mainly consists of the following:

-   aheartbeat process

-   Execution file to perform Failover to the local node

-   Execution file for remote node Failover

##### aheartbeat Process

aheartbeat is a background process and detects two types of failures; it either detects database failure by periodically connecting to the Altibase server on the same node, or detects network failure by periodically connecting to aheartbeats on other nodes.

##### Execution File to Perform Failover to the Local Node

After database server failure on the same node as aheartbeat has been detected, this file is executed to perform Failover to the local node. This file can be either an executable binary or script file.

##### Execution File to Perform Failover to the Local Node

After aheartbeat has detected failure on the other node, this file is executed for remote node Failover. This file can be either an executable binary or script file.

### Altibase Heartbeat Procedure

This section explains the basic Altibase Heartbeat procedure in a distributed database environment. The following figure is a diagram of a simple distributed database environment consisting of multiple Altibase databases with Altibase Heartbeats.

![heartbeat](media/Heartbeat/heartbeat.gif)

[Figure 1-1] Altibase Heartbeat Procedure

As shown above, aheartbeat detects database failure by monitoring the Altibase server process of the node it resides on(1. check in the figure). It also detects node failure(3. check) or external network failure(2. check) by monitoring aheartbeat processes on other nodes. 

If the Altibase server on Node A fails, let's look at how aheartbeats will run:

1.  Node A’s aheartbeat detects an Altibase server failure.

2.  Node A’s aheartbeat executes the execution file to perform Failover to the local node and terminates itself.
  
3.  By detecting the termination of Node A’s aheartbeat, Node B’s aheartbeat registers an Altibase server failure on Node A and executes the execution file for remote node Failover. 

<br>

# 2. Commands

This chapter explains Altibase Heartbeat commands.

### aheartbeat

aheartbeat is used to start up or terminate Altibase Heartbeat, or retrieve information about nodes. 

#### Syntax

```
aheartbeat {-r|-s|-i}
```

#### Options

| Option        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| \-r or --run  | Starts aheartbeat                                            |
| \-s or --stop | Terminates aheartbeat                                        |
| \-i or --info | Outputs information on all nodes consisting the distributed environment in which aheartbeats are running |

#### Example

Starts Altibase Heartbeat.

```
$ aheartbeat -r
```

Terminates Altibase Heartbeat.

```
$ aheartbeat -s
```

Outputs information on all nodes consisting the distributed environment in which aheartbeats are running,

```
$ aheartbeat -i
#ID     IP                 PORT      STATUS
0      192.168.1.31        55778     RUN
0      172.168.221.32      55778     RUN
1      192.168.2.33        55444     RUN
1      168.768.1.1         55444     READY
2      192.168.2.33        54321     ERROR
2      ::2:1               54321     RUN
```

<br>

# 3. Configuring Altibase Heartbeat

This chapter explains how to configure Altibase Heartbeat, and how to configure a distributed database environment with Altibase Heartbeats.

### Configuration

This section explains the necessary configuration for using Altibase Heartbeats in a distributed database environment.

#### Environment Variables

##### Mandatory Environment Variables

The following environment variables must be set to use Altibase Heartbeats:

- ALTI_HBP_HOME  
  Sets the Altibase Heartbeat home directory. And sets the ALTI_HBP_HOME/bin on the environment variables PATH as follows.

```
export PATH=$ALTI_HBP_HOME/bin:$PATH : PATH
```


-   ALTI_HBP_ID  
    Sets an ID to identify the node on which Altibase Heartbeats reside. The value must be an integer between 1 and 99, and each node must have a unique ID. Since the ID 0 indicates that aheartbeat exists in an external network, an internal network node cannot take 0 as its ID. 
    
-   ALTI_HBP_ALTIBASE_PORT_NO  
    Sets Altibase server’s listening port number which the Altibase Heartbeat is to monitor; this is the listening port number of the Altibase server that exists on the same node as the aheartbeat. 
    
-   ALTI_HBP_DETECT_INTERVAL  
    Sets the interval (in seconds) after which the Altibase Heartbeat monitors Altibase server failure. 
    
-   ALTI_HBP_DETECT_HIGHWATER_MARK  
    Sets the number of failed connections to tolerate before determining a failure when the aheartbeat receives no response from the Altibase server it is monitoring or aheartbeats on other nodes. 

##### Optional Environment Variables

If necessary, the following environment variables can be set additionally.

-   ALTI_HBP_ALTIBASE_FAILURE_EVENT  
    The name of an executable script or binary file which the Altibase Heartbeat executes when it detects an Altibase server failure on the same node. On omission, $ALTI_HBP_HOME/bin/altibaseFailureEvent.sh is executed by default.
    
-   ALTI_HBP_REMOTE_NODE_FAILURE_EVENT  
    The name of an executable script or binary file which the Altibase Heartbeat executes when it detects an Altibase server failure on another node. On omission, $ALTI_HBP_HOME/bin/remoteNodeFailureEvent.sh is executed by default. 

#### Setting aheartbeat Nodes

The purpose of the aheartbeat.settings file is to configure a distributed environment which uses Altibase Heartbeats. This file stores information on all nodes consisting the distributed environment, and exists in the $ALTI_HBP_HOME/conf directory. To execute Altibase Heartbeat, it is imperative that this file exists. 

The information stored in the aheartbeat.settings file consists of the ID, IP address and aheartbeat‘s listening port number on each node. This information is necessary for aheartbeats to connect to aheartbeats on other nodes. 

If one server has many IP addresses, you can specify up to four sets of different IP addresses for the same ID. Also, IPs of different versions can be set for the same ID.

\<An example of the aheartbeat.settings file>

```
# ID   IP                  PORT
0      169.215.114.23    55778     # public domain
0      222.112.231.234   55778     # public domain
1      192.168.2.33       55444
1      222.112.181.231   55444     # public domain
2      192.168.2.33       54321
2      ::ffff:c0a8:221   54321     # IPv6
```

In the above example, Node 0 has two IP addresses (169.215.114.23, 222.112.231.234) and aheartbeat’s listening port number is 55778. Node 1 has two IP addresses (192.168.2.33, 222.112.181.231) and aheartbeat’s listening port number is 55444. 

Two IP addresses of different versions are set to the same ID for Node 2 (IPv4: 192.168.2.33, IPv6: ::ffff:c0a8:221) and aheartbeat’s listening port number is 55321. Comments can be left with a #.

##### Note

The settings in the aheartbeat.settings file must be identical for all of the nodes comprising a distributed environment. Otherwise, Altibase Heartbeat can malfunction.

#### Failover Execution File

When aheartbeat fails to connect to an Altibase server on its node or aheartbeats on other nodes (or simply put, detects a failure), it executes the failover execution file. The failover execution file must be in the $ALTI_HBT_HOME/bin directory and the file name can be set with the ALTI_HBP_ALTIBASE_FAILURE_EVENT, ALTI_HBP_REMOTE_NODE_FAILURE_EVENT environment variables described above.

The default script file for failover is as follows.

-   altibaseFailureEvent.sh  
    This script file is executed when Altibase Heartbeat detects an Altibase server failure on the same node. Tasks, such as notifying DBAs of failures or restarting the failed Altibase server, can be included.
    
-   remoteNodeFailureEvent.sh  
    This script file is executed when Altibase Heartbeat detects a failure on another node. Tasks, such as performing Failover to the services of a failed database, can be included.

Database administrators can override failure by modifying the default script file or writing application programs which execute Failover operations.

#### aheartbeat 0

In a system where databases in an internal network provide services to clients in an external network, aheartbeat can exist in the external network to detect network failure from the internal to external network. The ID of a node which has aheartbeat in the external network must be 0. Therefore, aheartbeat in the external network is called aheartbeat 0.

The user can decide whether or not to add aheartbeat 0.

### Configuring an Altibase Heartbeat System : A Practice Example

A practice example is provided in this section to show how to configure a distributed environment with Altibase databases and the Altibase Heartbeat utility.

It is possible to provide enforced and continuous database services by incorporating the Altibase Heartbeat utility in a distributed environment consisted of Altibase databases.

#### Distributed Environment Diagram and Conditions 

Three nodes(A, B, C) exist in the internal network and each node has an Altibase server and aheartbeat.

![heartbeat_sample](media/Heartbeat/heartbeat_sample.gif)

[Figure 3-1] Distributed Environment Diagram and Conditions

-   Each node’s Altibase database has a client requesting services.

-   aheartbeat 0 runs in a public network with the IP address 169.215.114.23, and the listening port number 44000.
  
-   Each node’s IP address, aheartbeat and Altibase server’s listening port number are as follows.

| Node | IP Address     | Altibase Server Listerning Port Number | aheartbeat Listening Port Number |
| ---- | -------------- | -------------------------------------- | -------------------------------- |
| A    | 192.168.100.30 | 20000                                  | 21000                            |
| B    | 192.168.100.31 | 30000                                  | 31000                            |
| C    | 192.168.100.32 | 40000                                  | 41000                            |

#### Setting Environment Variables 

Under the above conditions, the environment variables for each node can be set as follows.

- aheartbeat 0’s Node (external network):

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=0

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node A:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=1

  ALTI_HBP_ALTIBASE_PORT_NO=20000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node B:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=2

  ALTI_HBP_ALTIBASE_PORT_NO=30000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node C:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=3

  ALTI_HBP_ALTIBASE_PORT_NO=40000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

> Note: the ALTI_HBP_ALTIBASE_PORT_NO environment variable is ignored in the 0 Node.
>

#### aheartbeat.settings

The contents of the $ALTI_HBP_HOME/conf/aheartbeat.settings file are identical over all nodes and are as follows.

\# ID     IP PORT

0      169.215.114.23        44000    #External Network

1      192.168.100.30        21000    #NODE A

2      192.168.100.31        31000    #NODE B

3      192.168.100.32        41000    #NODE C

####  Failover Execution File

Make the necessary changes to the contents of the altibaseFailureEvent.sh and remoteNodeFailureEvent.sh files in the \$ALTI_HBP_HOME/bin directory. You can also write an application program for Failover, put the execution binary into the $ALTI_HBP_HOME/bin directory and then set the environment variables.

#### Starting aheartbeat 

Start Altibase Heartbeat on each node with the following command.

```
$ aheartbeat -r
```

The startup order of the nodes is irrelevant. Once aheartbeats are running, the status of each node can be checked with the following command.

```
$ aheartbeat -i
```

<br>

# 4. Altibase Heartbeat Process

This chapter explains the Altibase Heartbeat process in details. On which criteria Altibase Heartbeat determines failure, and once failure is detected, how Failover is performed are examined.

### aheartbeat Status

aheartbeat defines the status of itself and other aheartbeats.

aheartbeat is in one of the following three statuses, depending on its execution state.

-   Ready: aheartbeat is not yet running

-   Run: aheartbeat has been executed and is in the state of running normally.

-   Error: The node is in a state of failure

aHeartbeat also defines aheartbeats on other nodes to be in one of the following three statuses.

-   Ready: aheartbeat has not yet performed an initial handshake with the corresponding node’s aheartbeat. 
-   Run: aheartbeat has successfully performed a handshake with the corresponding node’s aheartbeat and is in the state of being connected normally. 
-   Error: aheartbeat cannot connect to the corresponding node’s aheartbeat whose status was previously detected to be 'Run'.

The following figure shows how status transition occurs and the table lists the situations under which each status transition occurs.

![heartbeat_transition](media/Heartbeat/heartbeat_transition.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-07265" source_md="Manuals/Tools/Altibase_trunk/eng/Altibase Heartbeat User&#x27;s Guide.md" line_no="559" image_path_raw="media/Heartbeat/heartbeat_transition.gif" image_class="E" format="mermaid" verified="True" -->
```mermaid
flowchart LR
    Ready([Ready])
    Run([Run])
    Error([Error])
    Ready -->|"(1)"| Run
    Run -->|"(2)"| Error
    Error -->|"(3)"| Run
    Run -->|"(4)"| Ready
```
<!-- IMG_RECOVERY_END ref_id="img-07265" -->


[Figure 4-1] Status Transition

Each status transition occurs in the following table.

| Status Transition | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| (1)               | After starting up, aheartbeat has successfully performed a handshake |
| (2)               | aheartbeat has terminated due to failure                     |
| (3)               | After failure, aheartbeat has restarted and successfully re-performed a handshake |
| (4)               | aheartbeat has terminated normally                           |

[Table 4-1] Status Transition

### Determing Failure

This section examines the criteria on which Altibase Heartbeat determines failure.

Altibase Heartbeat monitors in the following order and detects failure by connecting to three objects. The table below depicts the node (local or remote) which aheartbeat registers to have failed for each monitoring target object when connection fails.

| Order | Monitoring Target                          | Registered Node Failure |
| ----- | ------------------------------------------ | ----------------------- |
| 1     | aheartbeat 0                               | Local node failure      |
| 2     | Altibase database server on the local node | Local node failure      |
| 3     | aheartbeat on the remote server            | Remote node failure     |

[Table 4-2] Determing Failure

#### Local Node Failure

When aheartbeats of each node detect failure at #1 or #2 in the above table, they register a local node failure.

aheartbeats of each node initially monitor aheartbeat 0 which resides in the external public network; when connection fails, they register a local node failure. In this case, aheartbeat determines that database services cannot be provided due to network failure between the Altibase server and clients.

If connection to aheartbeat 0 is normal or aheartbeat 0 is nonexistent, aheartbeats of each node monitor the Altibase database server on the local node; when connection fails, they register a database failure. In this case, aheartbeat determines that database services cannot be provided due to database failure. 

If aheartbeat acknowledges that a failure has occurred in the above two monitoring targets, it executes the execution file to perform Failover to the local node and terminates itself.

#### Remote Node Failure

If aheartbeats of each node detect failure at #3 in the above table, they register a remote node failure. That is, when connection to another node’s aheartbeat which has been identified to be in the RUN status fails, they determine that the node has failed and execute the execution file for remote node Failover.

> Note: When a local node fails, the aheartbeat of the node shuts itself down, so the aheartbeats of other nodes cannot access the aheartbeats of the node. Therefore, it is determined that a failure has occurred in the Altibase server of the remote node.
> 

### Role of aheartbeat 0

aheartbeat 0’s role and features in a distributed database environment are as follows.

-   aheartbeat 0 does not monitor the Altibase server on its node.

-   aheartbeats on nodes other than aheartbeat 0, can verify disconnection with the external network by connecting to aheartbeat 0. Disconnection with the external network indicates disconnection with the clients.

How failure detection results differ in relation to whether or not aheartbeat 0 exists in a distributed database environment is explained below.

#### When aheartbeat 0 is Nonexistent

Let’s suppose the network has failed in a distributed database environment where aheartbeats reside in the internal network.

![heartbeat_fail_0_noexistence](media/Heartbeat/heartbeat_fail_0_noexistence.gif)

[Figure 4-2] Network Failure Between an Internal and External Network

If a network failure occurs between Node A and the external network as shown above, Node A’s aheartbeat is not capable of providing services to the client. However, it overlooks the network failure and continues to run. By doing so, Node B’s aheartbeat also overlooks the failure that has occurred on Node A and does not perform Failover to Node A.

#### When aheartbeat 0 is Existent

Next, let’s suppose the network has failed in a distributed database environment where aheartbeat resides in the external network.

![heartbeat_fail_0_existence](media/Heartbeat/heartbeat_fail_0_existence.gif)

[Figure 4-2] Network Failure Between an Internal and External Network

If a network failure occurs between Node A and the external network as shown above, it is impossible for Node A’s aheartbeat to connect to aheartbeat 0. Therefore, Node A’s aheartbeat registers a local node failure, terminates itself and by doing so, allows other nodes to detect its failure. Since Node B’s aheartbeat can’t connect Node A’s aheartbeat, it executes the remote node failover execution file to perform Failover to Node A. 

As seen in the examples above, since aheartbeat 0 can detect network failure between the internal and external networks, the provision of continuous database services can be enforced by using aheartbeat 0.

### Failover and Failback

#### Failover

When aheartbeat detects a failure, it executes the failover execution file with the following two arguments to enable the DBA to efficiently perform Failover.

| Argument        | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| First Argument  | The number of failed nodes                                   |
| Second Argument | The IDs of the failed nodes. These are differentiated by blaks and are specified in ascending order. |

For example, let’s assume that there is a distributed environment where five nodes with the respective IDs 1, 2, 3, 4, 5, which each have Altibase servers and aheartbeats running, and that the Altibase server has failed on the node with the ID 3. Once aheartbeat on the node ID 3 detects that its Altibase server has failed, it executes the following local node failover script and terminates itself.

```
altibaseFailureEvent.sh 1 3
```

Once aheartbeats of other nodes detect that aheartbeat of the node ID 3 has terminated, they execute the following remote node failover script.

```
remoteNodeFailureEvent.sh 1 3
```

If the Altibase server on the node ID 1 fails while Node ID 3 is down, the failover script is executed with the following arguments.

```
altibaseFailureEvent.sh 2 1 3
remoteNodeFailureEvent.sh 2 1 3
```

This means that two servers have failed and their IDs are 1 and 3.

#### Failback

Failback after a node has recovered from failure must be manually performed by the user.

### Logging

Altibase Heartbeat writes the following information to the log file while it is processing.

-   Information of aheartbeat startup

-   Information of connection failure of the Altibase Server

-   Information of the start of an connection to another node

-   Information of aheartbeat failure situation of Altibase server and other nodes

-   Information of each node's aheartbeat status transition

Log files are fixed to $ALTI_HBP_HOME/log/aheartbeat.log.

The output format of log information is as follows.

```
[YYYY-MM-DD HH:MM:SS T-<threadID>] Log Body
```

<!-- SOURCE_BLOCK_END source_id="SRC-000215" block_id="BLOCK-000932" -->

## SRC-000220 - Release 7.2

| Field | Value |
| --- | --- |
| `source_id` | SRC-000220 |
| `source_path` | Manuals/Tools/Altibase_trunk/eng/dataCompJ User's Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | en |
| `authority_label` | English extraction aid; Altibase 8.1 verified source |
| `source_sha256` | 2db7dee4d8722ce5cd91a8dfd02318bdb0f10fd6bfa9ce00cf8245116f349b08 |
| `byte_count` | 49861 |
| `line_count` | 1165 |
| `estimated_tokens` | 12443 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000220" source_path="Manuals/Tools/Altibase_trunk/eng/dataCompJ User&#x27;s Manual.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="en" authority_label="English extraction aid; Altibase 8.1 verified source" sha256="2db7dee4d8722ce5cd91a8dfd02318bdb0f10fd6bfa9ce00cf8245116f349b08" byte_count="49861" line_count="1165" estimated_tokens="12443" block_id="BLOCK-000933" -->
dataCompJ User's Manual
================

#### Release 7.2

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>



<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Tools & Utilities dataCompJ User's Manual
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the
software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>


<br>

# Table Of Contents

- [Preface](#preface)

- [1. Introducing dataCompJ](#1-introducing-datacompj)
  - [Overview](#overview)
  - [System Requirements](#system-requirements)
- [2. Getting Started](#2-getting-started)
  - [Terms for dataCompJ](#terms-for-datacompj)
  - [Inconsistent Records and Synchronization Policy](#inconsistent-records-and-synchronization-policy)
  - [Synchronization Policy](#synchronization-policy)
- [3. How to Use dataCompJ](#3-how-to-use-datacompj)
  - [How to run dataCompJ](#how-to-run-datacompj)
  - [Executing dataCompJ](#executing-datacompj)
  - [Configuration File Setup](#configuration-file-setup)
- [4. Functions](#4-functions)
  - [Comparison (DIFF) Function](#comparison-diff-function)
  - [Synchronization(SYNC) Function](#synchronizationsync-function)
- [Appendix A: Data Type compatibility table between Other Databases](#appendix-a-data-type-compatibility-table-between-other-databases)

<br>

Preface
----

This manual describes the ability of dataCompJ to compare and match the discrepant data efficiently and how to use it.

#### Audience

This manual has been prepared for the following Altibase users:

- Database administrators
- Performance administrators
- Database users
- Application developers
- Technical Supporters

It is recommended for those reading this manual possess the following background knowledge:

- Basic knowledge in the use of computers, operating systems, and operating system utilities
- Experience in using relational database and an understanding of database concepts
- Computer programming experience
- Experience in database server management, operating system management, or network administration

#### Organization

This manual is organized as follows:

- Chapter 1: Introducing dataCompJ  
  This chapter introduces dataCompJ and explains how to install it.

- Chapter 2: Getting Started  
  This chapter describes the key concepts that helps running dataCompJ more effectively.

- Chapter 3: How to use dataCompJ  
  This chapter provides a step by step guide to operate dataCompJ and set up the configuration file.

- Chapter 4: Functions

  This chapter explains DIFF function and SYNC function in detail.

- Appendix A: Data Type compatibility table between Other Databases

#### Documentation Conventions

This section describes the conventions used in this manual. Understanding these conventions will make it easier to find information in this manual and in the other manuals in the series. 

There are two sets of conventions:

- Syntax diagram convetions
- Sample code conventions

##### Syntax Diagram Conventions

This manual describes command syntax using diagrams composed of the following elements:

| Elements                              | Meaning                                                      |
| ------------------------------------- | ------------------------------------------------------------ |
| ![image1](media/dataCompJ/image1.gif) | Indicates the start of a command. If a syntactic element starts with an arrow, it is not a complete command. |
| ![image2](media/dataCompJ/image2.gif) | Indicates that the command continues to the next line. If a syntactic element ends with this symbol, it is not a complete command. |
| ![image3](media/dataCompJ/image3.gif) | Indicates taht the command continues from the previous line. If a syntactic element starts witht his symbol, it is not a complete command. |
| ![image4](media/dataCompJ/image4.gif) | Indicates the end of a statement.                            |
| ![image5](media/dataCompJ/image5.gif) | Indicates a manatory element.                                |
| ![image6](media/dataCompJ/image6.gif) | Indicates an optional element.                               |
| ![image7](media/dataCompJ/image7.gif) | Indicates a mandatory element comprised of options. One, and only one, option must be specified. |
| ![image8](media/dataCompJ/image8.gif) | Indicates an optional element comprised of options.          |
| ![image9](media/dataCompJ/image9.gif) | Indicates an optional element in which multiple elements may be specified. A comman must precede all but the first element. |

##### Sample Code Conventions

The code examples explain SQL statements, stored procedures, iSQL statements, and other command line syntax.

The following table describes the printing conventions used in the code examples.

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)][[FIXED \|] VARIABLE]                      |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL> SELECT ename FROM employee; ENAME ----------------------- SWNO HJNO HSCHOI . . . 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code.Other Symbols | EXEC :p1 := 1; acc NUMBER(11,2);Symbols other than those shown above are part of the actual code. |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT * FROM *table_name*; CONNECT *userID*/*password*;     |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### Related Documentations

For more detailed information, please refer to the following documents.

- Installation Guide

- Getting Started Guide

- Administrator’s Manual

- Replication Manual

- Precompiler User’s Manual

- API User’s Manual

- Altibase C Interface Manual

- iSQL User’s Manual

- Utilities Manual

- General Reference

- Error Message Reference

#### Altibase Welcomes Your Comments and Feedbacks

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there is any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](#http://altibase.com/support-center/en/).

Thank you. We always welcome your feedbacks and suggestions.

<br>

# 1. Introducing dataCompJ

This chapter introduces dataCompJ and explains how to install it. This chapter consists of the following sections:

- Overview

- System Requirements

- Installation and Uninstallation

### Overview

Altibase dataCompJ is a utility designed to guarantee data consistency between two heterogeneous databases and resolve data inconsistency if any. dataCompJ compares Altibase with another heterogeneous database on a table-by-table basis, and outputs information on any inconsistency it detects. Also, it offers an efficient feature for synchronizing two databases by applying the inconsistent data to slave database in the event of data inconsistency.

Data managed by dataCompJ are replicated by Adapter for Oracle or Adapter for JDBC provided by Altibase.

A proper use of Altibase dataCompJ would be a cornerstone of effective data management with advantageous usability along with its advanced technical performance.

### System Requirements

This section discusses the system requirements for dataCompJ and compatible database management systems.

#### Hardware Requirements

- CPU: Pentium III 800MHz or better
- Main memory: Minimum 512MB,  4GB or more recommended
- Disk: 50MB or more free space

#### Software Requirements

- Oracle, OpenJDK or IBM Java Runtime Environment 8 or higher

dataCompJ is a pure Java-based client application relying on the JAVA Runtime Environment (JRE) instead of the client's hardware or an operating system.

#### Compatible Database Systems

##### Master DB

- Altibase: Altibase 5.3.3 or later

##### Slave DB

- Oracle: Oracle 9i or later
- MariaDB: MariaDB 5.5.x or later

Refer to [Terms for dataCompJ](#terms-for-datacompj) section for more detailed definitions of Master/Slave DB.

dataCompJ can be used with Altibase and various other databases. Since this tool uses JDBC driver to connect to database, the JDBC driver compatible with original and target database is required. Currently JDBC driver for Oracle, ojdbc5.jar, is provided along with dataCompJ for your convenience.

#### Intallation and Uninstallation

dataCompJ can be downloaded from the official [Altibase Customer Support portal](#http://altibase.com/support-center/en/). It is provided as a zip or tar.gz file in the name of dataCompJCli which includes executable files and JDBC drivers.

dataCompJ is installed once dataCompJCli is decompressed. Subdirectory of JDBC including dataCompJCli.sh and XML file exist in the directory created as a result of the decompression.

In order to uninstall dataCompJ, delete the directory in which dataCompJ is installed.

<br>

# 2. Getting Started

This chapter describes the key concepts that helps running dataCompJ more effectively.

This chapter consists of the following sections:

- Terms for dataCompJ
- Inconsistent Records
- Synchronization Policy

### Terms for dataCompJ

##### Master DB

Master DB indicates Altibase database containing original data between two heterogeneous databases to be compared.

##### Slave DB

Slave DB indicates the other database to which the replicated data is applied between the two heterogeneous databases to be compared.

##### TablePair

TablePair means the comparison target of dataComJ specified by the user, and it is in table unit. TablePair represents a pair comprised of a table (Master table) in Master DB and a table (Slave table) in Slave DB.

##### Master Table

Master table is a orginal table in the Master DB specified by the user in TablePair.

##### Slave Table

Slave table is a comparison target table in the Slave DB specified by the user in TablePair.

### Inconsistent Records and Synchronization Policy

Inconsistent records signify records whose column values are inconsistent based on the primary key of the master and slave tables. The inconsistent record can be divided into three types as in the following.

##### MOSO inconsistent

This is a case in which particular records with the same value of primary key columns can be found in both Master and Slave DB, but the value of non primary key columns are different from each other.

##### MOSX inconsistent

This is a case in which records with values of primary key columns can be found in Master DB, but not in Slave DB.

##### MXSO inconsistent

This is a case when there exists particular records with values of primary key columns only in Slave DB, not in Master DB.

##### Resolving Inconsistent Record

When dataCompJ discovers inconsistent records, the two following functions are provided depending on the user's choice as delineated in dataCompJ configuration file.

1.  DIFF: This function distinguishes inconsistent records between Master tables and Slave tables and records them to a CSV format file.
2.  SYNC: This function distinguishes inconsistent records between Master tables and Slave tables and resolves the inconsistency based on the synchronization policy delineated in the dataCompJ configuration file.

### Synchronization Policy

Synchronization policy defines how to match up the records in slave tables in accordance with the records in master tables when dataCompJ discovers any inconsistent records. The synchronization policy provides the following three methods. 

##### MOSO Inconsistency

This method updates records with the same primary key in slave tables based on the master table records with UPDATE_TO_SLAVE policy.

##### MOSX Inconsistency

This method is used to insert a record, which exists in the master table but not in the slave table, into the slave table with INSERT_TO_SLAVE policy.

##### MXSO Inconsistency

This method deletes records, which exists only in the slave table, but not in the master table, from the slave table with DELETE_FROM_SLAVE policy.

<br>

# 3. How to Use dataCompJ

This section provides a step by step guide to operate dataCompJ and set up configuration file. 

This chapter consists of the following sections:

- How to run dataCompJ
- Executing dataCompJ
- Configuration File Setup

### How to run dataCompJ

The followings are the command to execute dataCompJ in the Command Line Interface (CLI).

- Linux

```
$ dataCompJCli.sh -f dataCompJ_env_file_path
```


- Windows

```
C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path
```


##### dataCompJ_env_file_path

This indicates the file path of dataCompJ configuration file and in a required option. dataCompJ.xml is provided as an configuration file when dataCompJ is installed but user can choose to create another file to use an as configuration file.

### Executing dataCompJ

dataCompJ operates based on the configuration file set up by the user, and it is largely divided into two phases which are build and run.

##### Build Phase

Build phase is an initial investigation step to determine whether the run phase can be performed based on the configuration file. If any issue is discovered, it is output in the report file(dataCompJ_report.txt) and dataCompJ is terminated.

1.  Read the configuration file set up by the user.
2.  Verify whether the connection information described in the configuration file is valid.
3.  Connect to both databases to validate the target tables described in the configuration file and verify the meta information. If an issue is detected in either of the tables, it is recorded in the report file and dataCompJ is terminated.

##### Run Phase

In run phase, data in the target tables are compared then either comparing(DIFF) or synchronizing(SYNC) is executed according to the user's choice.

The execution result of each TablePair is output in the report file(dataCompJ_report.txt).

##### Output Files

When dataCompJ is executed, one report file and two log files are generated.

The output files generated by the comparison function(DIFF) is thoroughly delineated in the section 'Comparison (DIFF) Function'.

-   dataCompJ_report.txt: This is a report file in a text form to inform the execution results to a user.
-   dataCompJ.log: This is a log file recording events that occurs during the program operation. Also, this file is used to trace execution history of the program.
-   dataCompJ_data.log: This is a log file generated in the run phase, and this file records details of inconsistent records processed during the execution of comparison(Diff)/synchronization(Sync) in case \<TraceInconsistentRecord\> in the configuration file is set to true. It is suggested to use this file only when report of inconsistent records is required in detail since large capacity file is created if there are a lot of inconsistent data and this degrades the program performance.

### Configuration File Setup

Configuration file is essential in order to execute dataCompJ. dataCompJ.xml file is provided by default when dataCompJ is installed, and it is also available to use any other file user has created as an configuration file.  The configuration file should be written based on the XML rules delineated in dataCompJ.xml, and it should be encoded with UTF-8 if multiple languages are included.

The dataCompJ configuration file can be divided into three sections, such as Connections, Options, and TablePairs.

##### Connections

The Connections section is the part in which information required for connecting to the Master DB and Slave DB is recorded.

###### \<MasterDB\> 

The connection information of Master DB is recorded. The Master DB should be Altibase database. The following XML elements are the sub-elements of the Master DB.

\<JdbcUrl\>  
This is a character string used to record information of JDBC connection except user ID and password.

\<JdbcFilePath\>  
This is used to specify the path in which the JDBC jar file exist in order to connect to Master DB.

\<UserId\>  
This is used to specify the user ID in order to connect to the database.

\<Password\>  
This is used to specify the user password in order to connect to the database.

\<FetchSize\>  
This is used to specify the number of records that are fetched at once when importing data from the database. It is optional to fill this in and the default value is set to 1,000.

\<BatchSize\>  
This is used to specify the number of records that are executed at once when updating the database by using INSERT/DELETE/UPDATE statement. For instance, if 10 is specified in this entry, ten INSERT/DELETE/UPDATE are executed at once. It is optional to fill this in and the default value is set to 1,000.

###### \<SlaveDB\> 

This is used to record the connection information of Slave DB. The sub-elements of Slave DB is identical to that of the Master DB. 

##### Options

User inserts property values to execute dataCompJ in this section.

###### \<Operation\> 

This is used to specify which function should be executed between comparison(DIFF) and synchronization(SYNC) function to process inconsistent data.

###### \<FileEncoding\> 

This is used to specify the type of encoding for files generated when dataCompJ is executed.

###### \<Diff\>

\<DirPath\>  
This is used to specify the directory path in which a CSV file is created as a result of comparing each target table when the comparison(DIFF) is executed. 

###### \<Sync\> 

The followings are options for executing the synchronization(SYNC) function.

\<MOSO UPDATE_TO_SLAVE="true"/\>  
This option specifies whether or not to update records in the slave table based on records in the master table if MOSO inconsistent data is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

\<MOSX INSERT_TO_SLAVE="true"/\>  
This option specifies whether or not to insert the records which exist only in the master table into the slave table if MOSX inconsistent data is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

\<MXSO DELETE_FROM_SLAVE="true"/\>  
This option specifies whether or not to delete the records in slave table which does not exist in the master table if MXSO inconsistent is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

###### \<Log\>

The following XML elements are the sub-elements of a log.

\<DirPath\>  
This element specifies the directory path of log files created when dataCompJ is executed.

\<TraceInconsistentRecord\>  
This element specifies whether or not to record details of all the inconsistent records detected while DIFF/SYNC function is executed.

###### \<MaxThread\> 

This element indicates the maximum number of allocable threads. If it is specified to 0, the number of CPU core of the machine dataCompJ is running is allocated as MaxThread.

##### TablePairs

TablePairs is the part in which target tables for comparison are recorded. There are two methods for recording the comparison target tables, such as recording each individual information on the target tables and specifying the path of the text file in which all the table names are listed. Such methods can be used either one at a time or simultaneously. 

The methods for providing information on each individual table is as follows, and it has an advantage that it can control the data comparison method precisely. For instance, it is also possible to exclude specific columns or compare only target data satisfying certain conditions.

The target table's name should be one that is allowed by both Master DB and Slave DB. The user must use double quotation marks (") in XML file if the table name contains any space, special character or it is case-sensitive. For instance, when a comparision target table's name is Employee 01 of SYS schema, user must write the table name with double quotation marks as SYS."Employee 01" because it contains a space in its name.

###### \<TablePair\> 

This is a unit of target data for comparison comprised of one master table and one slave table. The following XML elements are the sub-elements of TablePair.

\<MasterTable\>  
This element is the name of target data and it can be specified as *[SchemaName].TableName* format. Unless it is specified, the UserId of Master DB is the default schema name. This is a required entry; thus, an error is occurred when it is not written.

\<SlaveTable\>  
This element is the name of target data and it can be specified as *[SchemaName].TableName* format. Unless it is specified, the UserId of Slave DB is used as the default schema name. This is a required entry; thus, an error is occurred when it is not written.

\<Exclude\>  
This element specifies a condition for projecting table records. This element can also specify multiple columns by using a comma(,). This is an optional entry and if this is not written, all the columns with data types supported by dataCompJ would be selected as comparison targets.

\<Where\>  
This elements specifies a condition for selecting table records. It has the same formay as WHERE clause of SQL statement, and multiple conditions are allowed. This is an optional entry, and all the records would be comparison targets if it is not written.

\<TableNameFilePath\>  
Providing the path of the text file enumerating all the table names is as below, and this gives an advantage in inputting tables easily in case it is required to compare multiple tables at once.

```
<TableNameFilePath>table_name_file_path</TableNameFilePath>
```

table_name_file_path is the path of the text file enumerating table names. The name of comparison target can be specified with *[SchemaName].TableName* format, and each table is distinguished with a new-line character. The name of comparison target in Master DB should be identical to the name of comparison target in Slave DB.

###### Restrictions

The following restrictions should be considered when selecting comparison target tables. If any constraint is infringed, dataCompJ outputs the issue occurred during the build phase to the report file(dataCompJ_report.txt) and does not proceed to the run phase.

1. A comparison target table should be identically(the column name, column order, data type, and primary key) composed. However, the data type should be compatible to that of the other database.

2. The unsupported data type is automatically excluded from the comparison targets. (e.g., binary type such as LOB)

3. There should be at least more than one column which can compare values other than a primary key.

   (Example 1) table1 (c1 int, c2 int, c3 CLOB, primary key (c1, c2))  
   (Example 2) table1 (c1 int, c2 int, c3 varchar(100), primary key (c1, c2))

   In the example 1, c3 is the only column satisfying the 'Constraint 3'. However, it infringes 'Constraint 2' since the data type CLOB is not supported by dataCompJ. Therefore, comparison for table 1 is not allowed.

   In the enxt example, c3 is the only column satisfying 'Constraint 3' and it is varchar type which is supported by dataCompJ. Thus, the table 1 can be compared.

<br>

# 4. Functions

This chapter explains DIFF function and SYNC function in detail with examples.

This chapter consists of the following sections:

- Comparison (Diff) funtion
- Synchronization (SYNC) function

### Comparison (DIFF) Function

The comparison(DIFF) function verifies inconsistent records between Master DB and Slave DB by identifying the inconsistent records occurred during the replication execution between the two database system and recording them to a file.

#### Configuration File

Set the \<Options\> - \<Operation\> value in dataCompJ configuration file to "DIFF".

<Connections\> and <Options\> are required entries and target table should be described in <TablePairs\>.

##### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
        <JdbcFilePath>./jdbc/Altibase710.jar</JdbcFilePath>
        <UserId>sys</UserId>
        <Password>manager</Password>
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
        <JdbcFilePath>./jdbc/ojdbc5.jar</JdbcFilePath>
        <UserId>altibase</UserId>
        <Password>altibase</Password>
    </SlaveDB>
</Connections>
  
<Options>
    <Operation>DIFF</Operation> 
    <FileEncoding>UTF-8</FileEncoding>
    <Diff>
        <DirPath>./diff/</DirPath>
    </Diff>
    <Sync>
        <MOSO UPDATE_TO_SLAVE="true"/>
        <MOSX INSERT_TO_SLAVE="true"/>
        <MXSO DELETE_FROM_SLAVE="true"/>
    </Sync>
    <Log>
        <DirPath>./</DirPath>
        <TraceInconsistentRecord>false</TraceInconsistentRecord>
    </Log>
    <MaxThread>0</MaxThread>
</Options>
  
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### How to Execute Comparison(DIFF)

The comparison(DIFF) is executed with the following command.

```
$ dataCompJCli.sh -f dataCompJ.xml
```

#### Execution Result

As a result of the execution, a report file(dataCompJ_report.txt) in which the execution result is summarized and log files(dataCompJ.log, dataCompJ_data.log) in which the event is recorded during the execution are created. Such files are delineated in the "Output Files" in detail. 

The table structure used in the example is as follows.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int);
```

##### DIFF Execution

```
$ dataCompJCli.sh -f dataCompJ.xml
----------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
----------------------------------------------------------
* Build started  at 2016-12-14 16:30:03.673
* Build finished at 2016-12-14 16:30:04.357 (Elapsed: 0:00:00.691)
* Run   started  at 2016-12-14 16:30:04.374
* Run   finished at 2016-12-14 16:30:04.905 (Elapsed: 0:00:00.531)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
```

###### Verifying the Report File

```
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 16:30:03.673
     - Finished : 2016-12-14 16:30:04.357
     - Elapsed  : 0:00:00.691
--------------------------------------------------------
 
[ User input information ]
...
 
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: C3(CLOB)
==========================================================
    Run
     - Started  : 2016-12-14 17:19:42.731
     - Finished : 2016-12-14 17:19:42.822
     - Elapsed  : 0:00:00.091
----------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------

```

##### Executable Data File

Four following comma-separated values(CSV) format data files are created in a TablePair unit as a result of selecting the comparison(DIFF).

-   *SchemaName.TableName*\_MASTER_diff.csv:  
    If MOSO is detected, this file stores the value of inconsistent record founds in the master table in CSV form.

-   *SchemaName.TableName*\_SLAVE_diff.csv:  
    This file stores the value of inconsistent records found in the slave table due to MOSO inconsistency in CSV form.

-   *SchemaName.TableName*\_MASTER_only.csv:  
    This file stores the value of records which only exist in the master table due to MOSX inconsistency in CSV form.

-   *SchemaName.TableName*\_SLAVE_only.csv:  
    This file stores the value of records which only exist in the slave table due to MXSO inconsistency in CSV form.

Since the inconsistent data due to MOSO inconsistency are recorded in the same order in in SchemaName.TableName_MASTER_diff.csv and SchemaName.TableName_SLAVE_diff.csv, when DIFF function is used to compare these files, user can intuitively compare the part MOSO inconsistency occurred.

#### Example

The table structure used for the examples is as follows.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int); /* Unsupported data in C3 CLOB dataCompJ */
CREATE TABLE ex2 (C1 int primary key, C2 varchar(20), C3 int);
```

##### DIFF Example 1

This example demonstrates specifying or omitting the schema name for two target tables. 

In case of EX1 in the example below, <MasterTable\> entry describes only the table name without schema and <SlaveTable\> entry is omitted. The <MasterTable\> describing the table name only uses the value inserted in <MasterDB\>-\<UserId\> as its schema name. The omitted <SlaveTable\> is processed assuming that it has the same value with <MasterTable\>.

C3 column in EX1 table is automatically excluded from the comparison target since it is a CLOB type which is unsupported data type by dataCompJ, and this is recorded in candidate tables entry in the report. 

In EX2 table, the schema name and table name are specified by a user, and it is processed based on the inserted schema and table names.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>DIFF</Operation> 
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 2 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: 
===========================================================================
    Run
     - Started  : 2016-12-14 17:56:04.516
     - Finished : 2016-12-14 17:56:04.593
     - Elapsed  : 0:00:00.076
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
```

##### DIFF Example 2

The following example shows that a user can specify certain columns in tables to exclude, and conduct comparison(Diff) on records meeting specified conditions (Where). 

User specifies to exclude C4 in non-primary key columns on EX1 table from the comparison targets in dataCompJ.xml, and execute comparison only for the records whose C1 column value is greater than 5.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
...
<Options>
    <Operation>DIFF</Operation> 
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
        <Exclude>C4</Exclude>
        <Where>C1 > 5</Where>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 2 ]
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2 FROM SYS.EX1 WHERE C1 > 5 ORDER BY C1 ASC
    * Excluded columns     : C4
    * Where condition      : C1 > 5
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: 
===========================================================================
    Run
     - Started  : 2016-12-14 17:57:09.895
     - Finished : 2016-12-14 17:57:09.974
     - Elapsed  : 0:00:00.080
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:            5
 Fetched record count from SLAVE :            5
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               5
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

### Synchronization(SYNC) Function

The Synchronization(SYNC) function identifies the inconsistent records occurred during the replication between the master DB and slave DB and applies them to the slave DB. This feature allows effective synchronization between the two database system.

#### Configuration Files

Set the \<Options\> - \<Operation\> value in dataCompJ configruration file to "SYNC".

<Connections\> and <Options\> are required entries and target table should be described in <TablePairs\>.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>SYNC</Operation> 
...
</Options>
  
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### How to Execyte Synchronization(SYNC)

The Synchronization(SYNC) function is executed as in the following manner.

```
$ dataCompJCli.sh -f dataCompJ.xml
$ dataCompJCli.sh -f ./dataCompJ.xml
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:08:40.407
* Build finished at 2016-12-14 18:08:41.076 (Elapsed: 0:00:00.676)
* Run   started  at 2016-12-14 18:08:41.090
* Run   finished at 2016-12-14 18:08:41.654 (Elapsed: 0:00:00.564)
---------------------------------------------------------------------------
Refer to the following output files for details.
---------------------------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record

```

#### Execution Results

As a result of the execution, a report file(dataCompJ_report.txt) in which the execution result is summarized and log files(dataCompJ.log, dataCompJ_data.log) in which the event is recorded during the execution are created. Such files are delineated in the "Output Files" in detail. 

###### dataCompJ_report.txt

```
$ cat dataCompJ_report.txt
===========================================================================
    Build
     - Started  : 2016-12-14 18:08:40.407
     - Finished : 2016-12-14 18:08:41.076
     - Elapsed  : 0:00:00.676
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
 
===========================================================================
    Run
     - Started  : 2016-12-14 18:08:41.090
     - Finished : 2016-12-14 18:08:41.654
     - Elapsed  : 0:00:00.564
---------------------------------------------------------------------------
 
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type    Resolution                Try         Fail
------------------------------------------------------
MOSO    UPDATE TO SLAVE                  2           0
MOSX    INSERT TO SLAVE                  1           0
MXSO    DELETE FROM SLAVE                1           0
------------------------------------------------------
```

When SYNC is correctly performed on all of the target tables and records, result fetched by executing DIFF on the same target table shows that all the records are identical.

```
$ dataCompJCli.sh -f ./dataCompJ.xml
-----------------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:11:54.924
* Build finished at 2016-12-14 18:11:55.561 (Elapsed: 0:00:00.645)
* Run   started  at 2016-12-14 18:11:55.580
* Run   finished at 2016-12-14 18:11:56.190 (Elapsed: 0:00:00.610)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
 
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 18:11:54.924
     - Finished : 2016-12-14 18:11:55.561
     - Elapsed  : 0:00:00.645
---------------------------------------------------------
 
[ User input information ]
...
 
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
 
==========================================================
    Run
     - Started  : 2016-12-14 18:11:55.580
     - Finished : 2016-12-14 18:11:56.190
     - Elapsed  : 0:00:00.610
---------------------------------------------------------------------------
 
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

<br>

# Appendix A: Data Type compatibility table between Other Databases

This section displays data type mapping table between other databases supported by dataCompJ. 

If comparison is executed on tables with unsupported data types by dataCompJ, it is processed in the following manners:

-   If both master table and slave table are in data types unsupported by dataCompJ: An error stating that the data type is unsupported is displayed in the build phase and it does not proceed to run phase.

-   If either the master table or the slave table is unsupported data type: In the build step, an error is reported to the report file (dataCompJ_report.txt) that the number of columns to be compared in the table is different, and does not proceed to run phase.

If the column data type of the table to be compared is a data type supported by dataCompJ, but the column data type of the target table for comparison is using different combination of data types to the one in data type compatibility table between other databases, it is processed in the following manners:

-   If the data comparison is impossible (e.g., comparison between integer type and character type data type): An error stating that the data type is incompatible is reported to the report file (dataCompJ_report.txt) in the build phase and it does not proceed to run phase.

-   For data types that is comparable but different to each other (e.g., integer and floating-point types): The run phase is executed since it cannot be processed in the build phase. However, in the execution result all records are treated as inconsistent records.

#### Altibase to Oracle

| Altibase | Oracle         | Description                                                  |
| -------- | -------------- | ------------------------------------------------------------ |
| SMALLINT | NUMBER         |                                                              |
| INTEGER  | NUMBER         |                                                              |
| BIGINT   | NUMBER         |                                                              |
| NUMERIC  | NUMBER         |                                                              |
| REAL     | NUMBER         |                                                              |
| DOUBLE   | NUMBER         |                                                              |
| FLOAT    | FLOAT          |                                                              |
| DATE     | DATE TIMESTAMP | - DATE - TIMESTAMP: Compared based on the smaller precision. For example, Altibase DATE supports up to microsecond, and Oracle TIMESTAMP supports up to nano second. In this case, the comparison of records is performed until nanosecond. <br>- DATE-DATE: Since Oracle DATE supports up to YYYY-MM-DD HH: MM: SS, only the according part is extracted from Altibase DATE and compared. |
| CHAR     | CHAR           |                                                              |
| VARCHAR  | VARCHAR2       |                                                              |
| NCHAR    | NCHAR          |                                                              |
| NVARCHAR | NVARCHAR2      |                                                              |

#### Altibase to MariaDB

| Altibase | MariaDB                                       | Description                                                  |
| -------- | --------------------------------------------- | ------------------------------------------------------------ |
| SMALLINT | SMALLINT                                      |                                                              |
| INTEGER  | INT                                           |                                                              |
| BIGINT   | BIGINT                                        |                                                              |
| NUMERIC  | DECIMAL                                       |                                                              |
| REAL     | FLOAT                                         |                                                              |
| DOUBLE   | DOUBLE                                        |                                                              |
| FLOAT    | N/A                                           | Data type corresponding to Altibase FLOAT does not exist in MariaDB. |
| DATE     | DATE, DATETIME, TIMESTAMP                     | - DATE-DATE: Since MariaDB DATE supports up to YYYY-MM-DD, only the according part is extracted from Altibase DATE and compared.<br>- DATE-DATETIME: Since MariaDB DATETIME supports up to YYYY-MM-DD HH: MM: SS, only the according part is extracted from Altibase DATE and compared.<br>- DATE-TIMESTAMP: Since MariaDB TIMESTAMP supports up to YYYY-MM-DD HH: MM: Microseconds 0-6 (default: 0), only the according part is extracted from Altibase DATE and compared. |
| CHAR     | CHAR                                          |                                                              |
| VARCHAR  | VARCHAR, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT |                                                              |
| NCHAR    | CHAR with Character set                       |                                                              |
| NVARCHAR | VARCHAR with Character set                    |                                                              |

<!-- SOURCE_BLOCK_END source_id="SRC-000220" block_id="BLOCK-000933" -->

## SRC-000222 - Release 7.1

| Field | Value |
| --- | --- |
| `source_id` | SRC-000222 |
| `source_path` | Manuals/Tools/Altibase_trunk/kor/Altibase Heartbeat User's Guide.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | ko |
| `authority_label` | Korean authoritative; Altibase 8.1 verified source |
| `source_sha256` | 92952fabc102408401feb73d1f032f78afaa6a1f9607316d4d0908440a7fc2ae |
| `byte_count` | 31811 |
| `line_count` | 850 |
| `estimated_tokens` | 5016 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000222" source_path="Manuals/Tools/Altibase_trunk/kor/Altibase Heartbeat User&#x27;s Guide.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="ko" authority_label="Korean authoritative; Altibase 8.1 verified source" sha256="92952fabc102408401feb73d1f032f78afaa6a1f9607316d4d0908440a7fc2ae" byte_count="31811" line_count="850" estimated_tokens="5016" block_id="BLOCK-000934" -->
Altibase Heartbeat User's Guide
================

#### Release 7.1

Altibase® Tool & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 











































<!-- PDF 변환을 위한 여백입니다. -->

<pre>
Altibase Tool & Utilities Altibase HeartBeat User's Guide
Release 7.1
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>

<br>

# 목차

- [서문](#%EC%84%9C%EB%AC%B8)
  - [이 매뉴얼에 대하여](#%EC%9D%B4-%EB%A7%A4%EB%89%B4%EC%96%BC%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
- [1.Altibase Heartbeat 소개](#1altibase-heartbeat-%EC%86%8C%EA%B0%9C)
  - [Altibase Heartbeat 개요](#altibase-heartbeat-%EA%B0%9C%EC%9A%94)
  - [Altibase Heartbeat의 기본 동작](#altibase-heartbeat%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EB%8F%99%EC%9E%91)
- [2.명령어](#2%EB%AA%85%EB%A0%B9%EC%96%B4)
  - [aheartbeat](#aheartbeat)
- [3.Altibase Heartbeat 구성하기](#3altibase-heartbeat-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
  - [환경 설정](#%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95)
  - [Altibase Heartbeat 시스템 구성 연습](#altibase-heartbeat-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%84%B1-%EC%97%B0%EC%8A%B5)
- [4.Altibase Heartbeat 동작](#4altibase-heartbeat-%EB%8F%99%EC%9E%91)
  - [aheartbeat의 상태](#aheartbeat%EC%9D%98-%EC%83%81%ED%83%9C)
  - [장애 판단](#%EC%9E%A5%EC%95%A0-%ED%8C%90%EB%8B%A8)
  - [0번 aheartbeat의 역할](#0%EB%B2%88-aheartbeat%EC%9D%98-%EC%97%AD%ED%95%A0)
  - [Failover와 Failback](#failover%EC%99%80-failback)
  - [로깅](#%EB%A1%9C%EA%B9%85)

<br>

서문
====

### 이 매뉴얼에 대하여

이 매뉴얼은 Altibase로 구성된 분산 데이터베이스 환경에서 사용할 수 있는 Altibase
Heartbeat 유틸리티에 대해 설명한다.

#### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

-   데이터베이스 사용자

-   데이터베이스 관리자

-   응용 프로그램 개발자

-   성능 관리자

-   기술지원부서

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

-   컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

-   관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

-   컴퓨터 프로그래밍과 관련된 경험이나 지식

-   데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

-   분산 환경에서의 데이터의 저장, 관리 및 처리와 관련된 지식

#### 소프트웨어 환경

이 매뉴얼은 Altibase 7.1 이상의 버전을 데이터베이스 서버로 사용한다는 가정 하에
작성되었다.

#### 이 매뉴얼의 구성

이 매뉴얼은 다음과 같이 구성되어 있다.

-   제 1장 Altibase Heartbeat 소개  
    이 장은 Altibase Heartbeat의 개요와 기본적인 동작을 설명한다.

-   제 2 장 명령어  
    이 장은 Altibase Heartbeat 명령어에 대해 설명한다.

-   제 3장 Altibase Heartbeat 구성하기  
    이 장에서는 Altibase Heartbeat를 설정하는 방법을 설명한다. 또한 Altibase
    Heartbeat와 함께 분산 데이터베이스 환경을 어떻게 구성할 수 있는지 살펴본다.

-   제 4 장 Altibase Heartbeat 동작  
    이 장은 Altibase Heartbeat의 동작을 상세히 설명한다. Altibase Heartbeat가
    장애를 판단하는 기준은 무엇인지, 장애를 감지한 후의 Failover는 어떻게
    이루어지는지 살펴본다.

#### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이
매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

-   샘플 코드 규칙

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어
설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                                                | 예제                                                                                                         |
|--------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [ ]          | 선택 항목을 표시                                                                    | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                                                                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시                               | { ENABLE \| DISABLE \| COMPILE }                                                                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                                           | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ]                                            |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략되는 것을 표시                           | SQL\> SELECT ename FROM employee; ENAME  ----------------------- SWNO  HJNO  HSCHOI  . . . 20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이 외에 기호들                                                   | EXEC :p1 := 1; acc NUMBER(11,2);                                                                             |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치         | SELECT \* FROM *table_name*; CONNECT *userID*/*password*;                                                    |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 칼럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                                                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드                              | DESC SYSTEM_.SYS_INDICES_;                                                                                   |

#### 관련 자료

자세한 정보를 위하여 다음 문서 목록을 참조하기 바란다.

-   Getting Started Guide

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   Stored Procedures Manual

-   Error Message Reference

#### 알티베이스는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음
버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께
고객서비스포털(*http://support.altibase.com/kr/* )로 보내주시기 바랍니다.

-   사용 중인 매뉴얼의 이름과 버전

-   매뉴얼에 대한 의견

-   사용자의 성함, 주소, 전화번호

이 외에도 알티베이스 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인
문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인
부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를
요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.

<br>

1.Altibase Heartbeat 소개
=======================

이 장은 Altibase Heartbeat의 개요와 기본적인 동작을 설명한다.

### Altibase Heartbeat 개요

Altibase Heartbeat는 분산 데이터베이스 환경에서 각 데이터베이스 노드의 장애를
감지하고, DBA가 장애에 대한 조치를 할 수 있도록 제공되는 유틸리티이다.
aheartbeat[^1]는 Altibase 서버들이 이중화로 연결되어 구성된 환경에서 사용할 수
있다.

[^1]: aheartbeat: Altibase Heartbeat 유틸리티의 실행 바이너리 파일 이름이다.


따라서 본 문서에서는 Altibase Heartbeat과 aheartbeat가 혼용되어 사용된다.

#### Altibase Heartbeat 구성요소

Altibase Heartbeat는 아래의 세가지 주요 요소로 구성된다.

-   aheartbeat 프로세스

-   로컬 노드 failover 수행 파일

-   리모트 노드 failover 수행 파일

##### aheartbeat 프로세스

aheartbeat는 백그라운드에 수행되면서 총 2종류의 장애를 감지한다. 하나는 자기
노드의 Altibase 서버에 주기적으로 접속을 시도하여 데이터베이스의 장애를
감지한다. 그리고 다른 노드의 aheartbeat과 주기적으로 접속을 시도하여 네트워크
장애를 감지한다.

##### 로컬 노드 failover 수행 파일

로컬 노드 failover 수행 파일은 aheartbeat가 같은 노드의 데이터베이스 서버의
장애를 감지한 후에 failover를 위해 실행하는 파일이다. 이 파일은 실행이 가능한
바이너리 또는 스크립트 파일일 수 있다.

##### 리모트 노드 failover 수행 파일

리모트 노드 failover 수행 파일은 aheartbeat가 다른 노드의 장애를 감지한 후에
failover를 위해 실행하는 파일이다. 이 파일은 실행이 가능한 바이너리 또는
스크립트 파일일 수 있다.

### Altibase Heartbeat의 기본 동작

이 절에서는 Altibase Heartbeat가 분산 데이터베이스 환경에서 동작하는 기본 과정을
설명한다. 아래 그림은 다수의 Altibase를 Altibase Heartbeat와 함께 구성한
기본적인 분산 데이터베이스 환경을 도식화한 그림이다.

![heartbeat](media/Heartbeat/heartbeat.gif)

그림 1-1 Altibase Heartbeat의 동작

그림에서 보듯이 aheartbeat는 자신이 속한 노드의 Altibase 서버 프로세스를
감시해서 데이터베이스 장애를 감지(그림에서 1번 check)한다. 그리고 다른 노드의
aheartbeat 프로세스를 감시해서 노드 장애(그림에서 3번 check) 또는 외부 네트워크
장애(그림에서 2번 check)를 감지한다.

만약 노드 A에 있는 Altibase 서버에 장애가 발생한 경우 aheartbeat들이 어떻게
동작할 것인지 살펴본다.

1.  노드 A의 aheartbeat가 Altibase 서버의 장애 감지

2.  노드 A의 aheartbeat가 로컬 노드 failover 수행 파일을 실행하고, aheartbeat는
    스스로 종료

3.  노드 B의 aheartbeat는 노드 A의 aheartbeat가 없어졌음을 감지하고 노드 A의
    Altibase 서버에 장애가 발생했음을 인지하여, 리모트 노드 failover 수행 파일을
    실행.


<br>

2.명령어
======

이 장은 Altibase Heartbeat 명령어에 대해 설명한다.

### aheartbeat

aheartbeat는 Altibase Heartbeat를 구동 또는 종료하거나, 노드들의 정보를 얻기
위해 사용된다.

#### 구문

```
aheartbeat {-r|-s|-i}
```



#### 옵션

| 옵션            | 설명                                                    |
|-----------------|---------------------------------------------------------|
| \-r 또는 --run  | aheartbeat 시작                                         |
| \-s 또는 --stop | aheartbeat 종료                                         |
| \-i 또는 --info | aheartbeat가 동작하는 분산 환경의 모든 노드 정보를 출력 |

#### 예제

Altibase Heartbeat를 시작한다.

```
$ aheartbeat -r
```

Altibase Heartbeat를 종료한다.

```
$ aheartbeat -s
```

aheartbeat가 동작하는 분산 환경을 구성하는 모든 노드에 대한 정보를 출력한다.

```
$ aheartbeat -i
#ID     IP                 PORT      STATUS
0      192.168.1.31        55778     RUN
0      172.168.221.32      55778     RUN
1      192.168.2.33        55444     RUN
1      168.768.1.1         55444     READY
2      192.168.2.33        54321     ERROR
2      ::2:1               54321     RUN
```

<br>

3.Altibase Heartbeat 구성하기
===========================

이 장에서는 Altibase Heartbeat를 설정하는 방법을 설명한다. 또한 Altibase
Heartbeat를 분산 데이터베이스 환경에서 어떻게 이용할 수 있는지 살펴본다.

### 환경 설정

이 절은 Altibase Heartbeat를 분산 데이터베이스 환경에 사용하기 위해 필요한 환경
설정에 대해 설명한다.

#### 환경 변수

##### 필수 환경 변수

아래는 Altibase Heartbeat를 사용하기 위해 반드시 설정해야 하는 환경변수의
목록이다.

- ALTI_HBP_HOME  
  Altibase Heartbeat의 홈 디렉토리를 설정한다. 아래 예제와 같이 환경 변수
  PATH에 ALTI_HBP_HOME/bin을 추가해야 한다.

  ```
  export PATH=$ALTI_HBP_HOME/bin:$PATH : PATH
  ```


-   ALTI_HBP_ID  
    Altibase Heartbeat가 위치하는 노드를 식별하기 위한 ID를 설정한다. 1에서 99
    사이의 정수로 설정해야 하며, 각 노드는 유일한 ID를 가져야 한다. 특히 ID 0은
    해당 노드의 aheartbeat가 외부 네트워크에 존재함을 나타내기 때문에, 내부망에
    존재하는 노드의 ID로는 사용할 수 없다.

-   ALTI_HBP_ALTIBASE_PORT_NO  
    Altibase Heartbeat가 감시할 Altibase 서버의 리스닝 포트 번호(listening port
    number)를 설정한다. 즉, aheartbeat와 동일한 노드에 존재하는 Altibase 서버의
    리스닝 포트 번호이다.

-   ALTI_HBP_DETECT_INTERVAL  
    Altibase Heartbeat가 Altibase 서버의 장애를 검사하는 주기를 초 단위로
    설정한다.

-   ALTI_HBP_DETECT_HIGHWATER_MARK  
    Altibase Heartbeat가 감시하는 Altibase 서버 또는 다른 노드의 aheartbeat로의
    접속 시도에 대해 응답이 없는 경우, 몇 회 접속 시도 이후에 장애로 판단할
    것인지 설정한다.

##### 선택 환경 변수

아래의 환경변수는 필요에 따라 추가적으로 설정할 수 있다.

-   ALTI_HBP_ALTIBASE_FAILURE_EVENT  
    Altibase Heartbeat가 같은 노드의 Altibase 서버의 장애를 감지할 때 실행하는
    실행 가능한 바이너리 파일 또는 스크립트 파일의 이름이다. 설정하지 않으면
    기본으로 \$ALTI_HBP_HOME/bin/altibaseFailureEvent.sh가 실행된다.

-   ALTI_HBP_REMOTE_NODE_FAILURE_EVENT  
    Altibase Heartbeat가 다른 노드의 장애를 감지한 경우 실행하는 실행 가능한
    바이너리 파일 또는 스크립트 파일의 이름이다. 설정하지 않으면 기본으로
    \$ALTI_HBP_HOME/bin/remoteNodeFailureEvent.sh가 실행된다.

#### aheartbeat 노드 설정

Altibase Heartbeat을 이용한 분산 환경 구성을 위하여 aheartbeat.settings 파일이
존재한다. aheartbeat.settings 파일은 분산 환경을 구성하는 모든 노드에 대한
정보를 저장하는 파일로써, \$ALTI_HBP_HOME/conf 디렉터리에 존재한다. 이 파일은
Altibase Heartbeat를 실행하기 위해 반드시 필요하다.

aheartbeat.settings에 저장되는 각 노드에 대한 정보는 노드 ID, IP 주소,
aheartbeat의 리스닝 포트 번호(listening port number)로 구성된다. 각 요소는
aheartbeat가 다른 노드의 aheartbeat에 접속하기 위해 필요한 항목이다.

만약 한 장비가 여러 개의 IP 주소를 가지는 경우, 동일한 ID에 대해 서로 다른 IP
주소로 구성된 세트를 4개까지 설정할 수 있다. 그리고 동일한 ID에 대해 IP 버전별
설정도 가능하다.

\<aheartbeat.settings 파일의 예시\>

```
# ID   IP                  PORT
0      169.215.114.23    55778     # public domain
0      222.112.231.234   55778     # public domain
1      192.168.2.33       55444
1      222.112.181.231   55444     # public domain
2      192.168.2.33       54321
2      ::ffff:c0a8:221   54321     # IPv6
```

위의 예시에서 노드 0은 두 개의 IP 주소 169.215.114.23과 222.112.231.234를 가지며
aheartbeat의 리스닝 포트 번호는 55778이다. 노드 1은 192.168.2.33과
222.112.181.231 두 개의 IP 주소를 가지며 aheartbeat의 리스닝 포트 번호는
55444이다.

노드 2의 경우 동일한 ID에 대해 IP 버전별로 설정한 것으로써, IPv4 주소
192.168.2.33과 IPv6 주소 ::ffff:c0a8:221을 따로 설정한 것이다. aheartbeat의
리스닝 포트 번호는 55321이다. 그리고 \#을 이용하여 주석을 남길 수 있다.

##### 주의 사항

한 분산 환경을 구성하는 모든 노드는 aheartbeat.settings 파일의 설정 내용이
동일해야 한다. 그렇지 않으면 Altibase Heartbeat가 오동작을 일으킬 수 있다.

#### failover 수행 파일

aheartbeat가 자기 노드의 Altibase 서버 혹은 다른 노드의 aheartbeat에 접속이
불가능하면, 즉 장애를 감지하면 failover용 실행 파일을 실행한다. failover용 실행
파일은 \$ALTI_HBT_HOME/bin 디렉토리에 있어야 하며, 파일명은 위의 절에서 설명한
ALTI_HBP_ALTIBASE_FAILURE_EVENT, ALTI_HBP_REMOTE_NODE_FAILURE_EVENT 환경변수로
설정할 수 있다.

기본으로 제공하는 failover용 스크립트 파일은 아래와 같다.

-   altibaseFailureEvent.sh  
    Altibase Heartbeat가 같은 노드의 Altibase 서버의 장애를 감지한 경우 실행하는
    스크립트 파일이다. DBA에게 장애 발생을 알려주거나 해당 노드의 Altibase
    서버를 재구동하는 등의 작업을 포함시킬 수 있다.

-   remoteNodeFailureEvent.sh  
    Altibase Heartbeat가 다른 노드의 장애를 감지한 경우 실행하는 스크립트
    파일이다. 장애가 발생한 데이터베이스의 서비스를 failover하는 등의 작업을
    포함시킬 수 있다.

데이터베이스 관리자는 기본으로 제공되는 스크립트 파일을 상황에 맞게 수정하거나,
failover 작업을 수행하는 응용프로그램을 작성하여 장애에 능동적으로 대처할 수
있다.

#### 0번 aheartbeat

내부망의 데이터베이스가 외부망의 클라이언트에 서비스를 제공하는 시스템 구성에서,
내부망에서 외부망으로의 네트워크 장애를 감지하기 위해 외부망에 Altibase
Heartbeat를 둘 수 있다. 외부망에 aheartbeat를 두는 노드의 ID는 반드시 0이어야
한다. 이런 연유로 외부망에 두는 aheartbeat를 0번 aheartbeat라고 부른다.

0번 aheartbeat의 추가는 사용자 선택사항이다.

### Altibase Heartbeat 시스템 구성 연습

이 절은 Altibase와 Altibase Heartbeat 유틸리티로 분산 환경을 구성하는 방법을
예시와 함께 살펴본다.

Altibase로 이루어진 분산 환경에 Altibase Heartbeat 유틸리티를 포함시켜서 더욱
강화된 무정지 데이터베이스 서비스를 제공할 수 있다.

#### 분산환경 구성도 및 조건

내부망에 A, B, C 세 노드가 있고 각 노드에 Altibase 서버와 aheartbeat가 존재한다.

![heartbeat_sample](media/Heartbeat/heartbeat_sample.gif)

그림 3-1 분산환경 구성도

-   각 노드의 Altibase에 서비스를 요청하는 클라이언트가 존재한다.

-   0번 aheartbeat가 공용망인 169.215.114.23에서 리스닝 포트 번호 44000으로
    동작한다.

-   각 노드의 IP 주소와 aheartbeat, Altibase 서버의 리스닝 포트 번호는 아래와
    같다.

| 노드 | IP 주소        | Altibase 서버 리스닝 포트 번호 | aheartbeat 리스닝 포트 번호 |
|------|----------------|--------------------------------|-----------------------------|
| A    | 192.168.100.30 | 20000                          | 21000                       |
| B    | 192.168.100.31 | 30000                          | 31000                       |
| C    | 192.168.100.32 | 40000                          | 41000                       |

#### 환경변수 설정

위와 같은 조건하에서 각 노드의 환경변수는 아래와 같이 설정할 수 있을 것이다.

- 0 번 aheartbeat의 노드(외부망):

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=0

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 A:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=1

  ALTI_HBP_ALTIBASE_PORT_NO=20000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 B:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=2

  ALTI_HBP_ALTIBASE_PORT_NO=30000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 C:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=3

  ALTI_HBP_ALTIBASE_PORT_NO=40000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

> 참고: 0번 노드에서는 ALTI_HBP_ALTIBASE_PORT_NO 환경변수가 무시된다.
>

#### aheartbeat.settings

\$ALTI_HBP_HOME/conf/aheartbeat.settings 파일의 내용은 모든 노드에서 동일하며
아래와 같다.

\# ID     IP PORT

0      169.215.114.23        44000    #External Network

1      192.168.100.30        21000    #NODE A

2      192.168.100.31        31000    #NODE B

3      192.168.100.32        41000    #NODE C

#### failover 수행 파일

\$ALTI_HBP_HOME/bin 디렉토리의 altibaseFailureEvent.sh 파일과
remoteNodeFailureEvent.sh의 내용을 상황에 맞게 수정한다. 또는 failover를 위한
응용프로그램을 작성한 후 실행 바이너리를 \$ALTI_HBP_HOME/bin 디렉토리에 두고
해당 환경변수를 설정한다.

#### aheartbeat 구동

각 노드에서 Altibase Heartbeat를 아래의 명령어로 실행한다.

```
$ aheartbeat -r
```

노드별 구동 순서는 상관없다. 실행 후 시간이 조금 경과하면 아래의 명령어로 각
노드의 상태를 확인할 수 있다.

```
$ aheartbeat -i
```

<br>

4.Altibase Heartbeat 동작
=======================

이장은 Altibase Heartbeat의 동작을 상세히 설명한다. Altibase Heartbeat가 장애를
판단하는 기준이 무엇인지, 장애를 감지한 후의 Failover는 어떻게 이루어지는지
살펴본다.

### aheartbeat의 상태

aheartbeat는 자신의 상태와 다른 aheartbeat의 상태를 각각 정의한다.

우선 aheartbeat 자신은 실행 상태에 따라 아래의 세가지 중 하나의 상태를 가진다.

-   Ready: aheartbeat 실행 전 상태

-   Run: aheartbeat가 실행되어 정상적으로 동작중인 상태

-   Error: 해당 노드에 장애가 발생한 상태

또한 aheartbeat는 다른 노드에 존재하는 aheartbeat의 상태를 아래 세가지 상태 중
하나로 정의한다.

-   Ready: 상대 노드의 aheartbeat와 최초 handshake를 하기 전

-   Run: 상대 노드의 aheartbeat와 성공적으로 handshake한 후 정상적으로 연결되는
    상태

-   Error: 이전까지 Run 상태로 감지되던 상대 노드 aheartbeat에 접속이 불가능한
    경우

한 상태에서 다른 상태로 전이되는 과정은 아래 그림과 같이 이루어진다. 

![heartbeat_transition](media/Heartbeat/heartbeat_transition.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-07367" source_md="Manuals/Tools/Altibase_trunk/kor/Altibase Heartbeat User&#x27;s Guide.md" line_no="676" image_path_raw="media/Heartbeat/heartbeat_transition.gif" image_class="E" format="mermaid" verified="True" -->
```mermaid
flowchart LR
    Ready([Ready])
    Run([Run])
    Error([Error])
    Ready -->|"(1)"| Run
    Run -->|"(2)"| Error
    Error -->|"(3)"| Run
    Run -->|"(4)"| Ready
```
<!-- IMG_RECOVERY_END ref_id="img-07367" -->


그림 4-1 aheartbeat 상태 전이

각각의 상태 전이는 아래 표와 같은 상황에서 발생한다.

| 상태 전이 | 설명                                         |
|-----------|----------------------------------------------|
| (1)       | aheartbeat 시작후 handshake 성공             |
| (2)       | 장애로 인해 aheartbeat 종료                  |
| (3)       | 장애 후 aheartbeat 재시작후 handshake 재성공 |
| (4)       | aheartbeat 정상 종료                         |

표 4-1 상태 전이

### 장애 판단

이 절은 Altibase Heartbeat가 장애를 감지하기 위해 취하는 동작과 장애를 판단하는
기준은 무엇인지 살펴본다.

Altibase Heartbeat는 아래의 순서대로 감시를 진행하며, 세 가지 대상에 접속해서
장애를 감지한다. 또한 아래 표는 각 감시 대상 별로 접속이 불가능할 때 어떤
노드(로컬 또는 리모트 노드)에 장애가 발생한 것으로 판단하는지도 보여준다.

| 순서 | 감시 대상                 | 노드 장애 판단          |
|------|---------------------------|-------------------------|
| 1    | 0번 aheartbeat            | 로컬 노드에 장애 발생   |
| 2    | 로컬 노드의 Altibase 서버 | 로컬 노드에 장애 발생   |
| 3    | 리모트 노드의 aheartbeat  | 리모트 노드에 장애 발생 |

표 4-2 장애 판단

#### 로컬 노드의 장애

각 노드의 aheartbeat들이 위 표의 1번 또는 2번에서 장애를 감지하는 경우 로컬
노드에 장애가 발생한 것으로 판단한다.

각 노드의 aheartbeat들은 가장 먼저 외부 공용망에 존재하는 0번 aheartbeat를
감시하며 접속이 불가능할 때 로컬 노드에 장애가 발생한 것으로 판단하다. 이 경우
로컬 노드에 존재하는 Altibase 서버 자체의 장애 여부와는 상관없으며, Altibase
서버와 클라이언트간의 네트워크 장애로 인해 서비스가 불가능하다고 판단한다.

0 번 aheartbeat로의 접속이 정상이거나, 0번 aheartbeat가 없을 때에는 각 노드의
aheartbeat들은 로컬 노드에 존재하는 Altibase 서버를 감시하며 이에 접속이
불가능할 때 데이터베이스 장애로 판단한다. 이 경우 데이터베이스 자체 장애로 인해
서비스가 불가능하다고 판단한다.

위의 두 감시 대상에서 장애가 발생한 것을 인지하면, aheartbeat는 로컬 노드
failover 수행 파일을 시작하고 스스로 종료한다.

#### 리모트 노드의 장애

각 노드의 aheartbeat들이 위 표의 3번에서 장애를 감지하는 경우 리모트 노드에
장애가 발생한 것으로 판단한다. 즉, RUN 상태로 파악된 다른 노드의 aheartbeat에
접속이 불가능하다면 그 노드에 장애가 발생한 것으로 판단하고 리모트 노드 failover
수행 파일을 시작한다.

> 참고: 로컬 노드에 장애가 발생하면 그 노드의 aheartbeat는 스스로 종료하기
> 때문에, 다른 노드의 aheartbeat들은 그 노드의 aheartbeat에 접속할 수 없다. 따라서
> 리모트 노드의 Altibase 서버에 장애가 발생한 것으로 판단한다.
>

### 0번 aheartbeat의 역할

0번 aheartbeat가 분산 데이터베이스 환경에서 하는 역할과 특징은 아래와 같다.

-   0번 aheartbeat는 자기 노드의 Altibase 서버를 감시하지 않는다.

-   ID가 0이 아닌 노드의 aheartbeat가 0번 aheartbeat에 접속하는 것으로 외부망과
    단절되었는지 여부를 파악할 수 있다. 외부망과 단절되었다는 것은 클라이언트와
    접속이 끊어졌다는 것을 의미한다.

아래는 분산 데이터베이스 환경에서 0번 aheartbeat가 구축되었는지 여부에 따라 장애
감지 결과가 어떻게 달라지는지 살펴본다.

#### 0번 aheartbeat가 없을 때

aheartbeat가 내부망 안에서만 구축된 분산 데이터베이스 환경에서 네트워크 연결에
장애가 발생한 경우를 가정해 보자.

![heartbeat_fail_0_noexistence](media/Heartbeat/heartbeat_fail_0_noexistence.gif)

그림 4-2 내부망과 외부망 사이의 네트워크 장애 발생

위 그림에서처럼 노드 A와 외부망 사이에서 네트워크에 장애가 발생하는 경우, 노드
A의 aheartbeat는 클라이언트에 서비스를 할 수 없는 상황이다. 하지만 네트워크
장애를 감지하지 못하여 aheartbeat가 계속 동작한다. 이로 인해 노드 B의 aheartbeat
역시 노드 A의 데이터베이스 서비스에 문제가 발생한 것을 감지할 수 없고, 노드 A를
failover 하지 않는다.

#### 0번 aheartbeat가 있을 때

aheartbeat가 외부망에 존재하는 분산 데이터베이스 환경에서 네트워크 연결에 장애가
발생한 경우를 가정해 보자.

![heartbeat_fail_0_existence](media/Heartbeat/heartbeat_fail_0_existence.gif)

그림 4- 3 내부망과 외부망 사이의 네트워크 장애 발생

위 그림에서처럼 노드 A와 외부망 사이에 네트워크에 장애가 발생하는 경우, 노드 A의
aheartbeat는 0번 aheartbeat에 접속이 불가능하다. 따라서 노드 A의 aheartbeat는
로컬 노드에 장애가 발생한 것으로 판단하여, 스스로 종료하고 다른 노드에서 본인의
장애를 감지할 수 있도록 한다. 결국 노드 B의 aheartbeat는 노드 A의 aheartbeat에
접속을 할 수 없으므로 노드 A를 failover하기 위해 리모트 노드 failover 수행
파일을 실행한다.

위의 두 예시에서 보듯이 0번 aheartbeat가 있다면 내부망과 외부망 사이에 발생하는
네트워크 장애까지 감지할 수 있으므로 무정지 데이터베이스 서비스를 더욱 강화할 수
있다.

### Failover와 Failback

#### Failover

DBA가 좀 더 효율적으로 failover를 수행하기 위하여, aheartbeat는 장애를 감지하면
다음 2개의 인자와 함께 failover 수행 파일을 실행한다.

| 인자         | 설명                                                            |
|--------------|-----------------------------------------------------------------|
| 첫 번째 인자 | 장애가 일어난 노드의 개수                                       |
| 두 번째 인자 | 장애가 일어난 노드의 ID들. 공백으로 구분하여 오름차순으로 지정. |

예를 들어 ID가 각각 1, 2, 3, 4, 5인 다섯 개의 노드에 Altibase 서버와
aheartbeat가 실행 중인 분산 환경에서, ID가 3인 노드의 Altibase 서버에 장애가
발생했다고 가정하자. ID가 3인 노드의 aheartbeat가 자기 노드의 Altibase 서버에
장애를 감지하면, 아래와 같이 로컬 노드 failover 스크립트를 실행하고 자신은
종료한다.

```
altibaseFailureEvent.sh 1 3
```

그리고 나머지 노드의 aheartbeat들은 ID가 3인 노드의 aheartbeat가 종료된 것을
감지한 후 아래와 같이 리모트 노드 failover 스크립트를 실행한다.

```
remoteNodeFailureEvent.sh 1 3
```

ID 3 노드의 장애 상황에서 또다시 ID 1인 노드의 Altibase 서버에 장애가 발생하면
아래와 같은 인자와 함께 failover 스크립트를 실행한다.

```
altibaseFailureEvent.sh 2 1 3
remoteNodeFailureEvent.sh 2 1 3
```

즉, 두 개의 서버에 장애가 발생했으며 그 ID는 1과 3이라는 것을 의미한다.

#### Failback

장애가 발생한 노드가 복구된 후의 failback은 사용자가 수동으로 수행해야 한다.

### 로깅

Altibase Heartbeat는 동작 중에 아래와 같은 정보를 로그 파일에 기록한다.

-   aheartbeat 시작 정보

-   Altibase 서버로의 접속 실패 정보

-   다른 노드로 접속 시작 정보

-   Altibase 서버 및 다른 노드의 aheartbeat 장애 상황 정보

-   각 노드의 aheartbeat 상태 변화 정보

로그 파일은 \$ALTI_HBP_HOME/log/aheartbeat.log로 고정되어 있다.

로그 정보의 출력 형식은 다음과 같다.

```
[YYYY-MM-DD HH:MM:SS T-<threadID>] Log Body
```

<!-- SOURCE_BLOCK_END source_id="SRC-000222" block_id="BLOCK-000934" -->

## SRC-000227 - Release 7.2

| Field | Value |
| --- | --- |
| `source_id` | SRC-000227 |
| `source_path` | Manuals/Tools/Altibase_trunk/kor/dataCompJ User's Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | 8.1_verified |
| `language` | ko |
| `authority_label` | Korean authoritative; Altibase 8.1 verified source |
| `source_sha256` | c520527c7fb7f9d83411b059eb6b42e43cc844eda6316c9867ce255132d1cbd7 |
| `byte_count` | 53442 |
| `line_count` | 1174 |
| `estimated_tokens` | 9531 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000227" source_path="Manuals/Tools/Altibase_trunk/kor/dataCompJ User&#x27;s Manual.md" source_family="utilities_datacompj" version_scope="8.1_verified" language="ko" authority_label="Korean authoritative; Altibase 8.1 verified source" sha256="c520527c7fb7f9d83411b059eb6b42e43cc844eda6316c9867ce255132d1cbd7" byte_count="53442" line_count="1174" estimated_tokens="9531" block_id="BLOCK-000935" -->
dataCompJ User's Manual
================

#### Release 7.2

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 











































<!-- PDF 변환을 위한 여백입니다. -->

<pre>
Altibase Tool & Utilities dataCompJ User's Manual
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>


<br>

# 목차

- [dataCompJ User's Manual](#datacompj-users-manual)
  - [서문](#%EC%84%9C%EB%AC%B8)
    - [이 매뉴얼에 대하여](#%EC%9D%B4-%EB%A7%A4%EB%89%B4%EC%96%BC%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
  - [1.dataCompJ 소개](#1datacompj-%EC%86%8C%EA%B0%9C)
    - [개요](#%EA%B0%9C%EC%9A%94)
    - [시스템 요구 사항](#%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%9A%94%EA%B5%AC-%EC%82%AC%ED%95%AD)
  - [2.dataCompJ 시작하기](#2datacompj-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
    - [용어](#%EC%9A%A9%EC%96%B4)
    - [불일치 레코드(Inconsistent record)](#%EB%B6%88%EC%9D%BC%EC%B9%98-%EB%A0%88%EC%BD%94%EB%93%9Cinconsistent-record)
    - [일치 정책 (Synchronization policy)](#%EC%9D%BC%EC%B9%98-%EC%A0%95%EC%B1%85-synchronization-policy)
  - [3.dataCompJ 사용 방법](#3datacompj-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)
    - [dataCompJ 실행 방법](#datacompj-%EC%8B%A4%ED%96%89-%EB%B0%A9%EB%B2%95)
    - [dataCompJ 수행 단계](#datacompj-%EC%88%98%ED%96%89-%EB%8B%A8%EA%B3%84)
    - [dataCompJ 설정 파일 구성](#dataCompJ-설정-파일-구성)
  - [4.dataCompJ 기능](#4datacompj-%EA%B8%B0%EB%8A%A5)
    - [비교(DIFF) 기능](#%EB%B9%84%EA%B5%90diff-%EA%B8%B0%EB%8A%A5)
    - [일치(SYNC) 기능](#%EC%9D%BC%EC%B9%98sync-%EA%B8%B0%EB%8A%A5)
  - [A. 부록: 이기종간 데이터 타입 호환 테이블](#a-%EB%B6%80%EB%A1%9D-%EC%9D%B4%EA%B8%B0%EC%A2%85%EA%B0%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85-%ED%98%B8%ED%99%98-%ED%85%8C%EC%9D%B4%EB%B8%94)

<br>

서문
====

### 이 매뉴얼에 대하여

이 매뉴얼은 Altibase 데이터베이스에서 이기종 데이터베이스로 데이터를 복제한 이후의 데이터 정합성 확인과 데이터 불일치를 해소하기 위한 도구인 dataCompJ를 사용하는 방법을 기술한다.

#### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

- 데이터베이스 관리자

- 성능 관리자

- 데이터베이스 사용자

- 응용 프로그램 개발자

- 기술지원부

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

- 컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

- 관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

- 컴퓨터 프로그래밍 경험

- 데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

#### 이 매뉴얼의 구성

- 제 1장 dataCompJ 소개  
  이 장은 dataCompJ의 특징을 이해하고자 하는 사용자에게 이 도구를 소개하고 설치하는 방법을 설명한다.

- 제 2장 dataCompJ 시작하기  
  이 장은 사용자들이 dataCompJ를 좀 더 능률적이고 효율적으로 실행하는 데 도움이 되는 기본 개념을 소개한다.

- 제 3장 dataCompJ 사용 방법
  이 장은 dataCompJ를 원활하게 실행하기 위한 방법과 dataCompJ 설정 파일 구성, 설정 시 고려할 점들을 설명한다.

- 제 4장 dataCompJ 기능

  이 장은 dataCompJ의 비교(DIFF) 기능과 일치(SYNC) 기능을 예제와 함께 보다 자세히 설명한다.

- A. 부록: 이기종간 데이터 타입 호환 테이블

#### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이 매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

- 구문 다이어그램

- 샘플 코드 규칙

##### 구문 다이어그램

이 매뉴얼에서는 다음 구성 요소로 구축된 다이어그램을 사용하여, 명령문의 구문을 설명한다.

| 구성 요소                             | 의미                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| ![image1](media/dataCompJ/image1.gif) | 명령문이 시작한다. 완전한 명령문이 아닌 구문 요소는 화살표로 시작한다. |
| ![image2](media/dataCompJ/image2.gif) | 명령문이 다음 라인에 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 종료한다. |
| ![image3](media/dataCompJ/image3.gif) | 명령문이 이전 라인으로부터 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 시작한다. |
| ![image4](media/dataCompJ/image4.gif) | 명령문이 종료한다.                                           |
| ![](media/dataCompJ/image5.gif)       | 필수 항목                                                    |
| ![](media/dataCompJ/image6.gif)       | 선택적 항목                                                  |
| ![](media/dataCompJ/image7.gif)       | 선택사항이 있는 필수 항목. 한 항목만 제공해야 한다.          |
| ![](media/dataCompJ/image8.gif)       | 선택사항이 있는 선택적 항목                                  |
| ![](media/dataCompJ/image9.gif)       | 선택적 항목. 여러 항목이 허용된다. 각 반복 앞부분에 콤마가 와야 한다. |

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어 설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                         | 예제                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]          | 선택 항목을 표시                                             | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시        | { ENABLE \| DISABLE \| COMPILE }                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                    | { ENABLE \| DISABLE \| COMPILE } <br />[ ENABLE \| DISABLE \| COMPILE ] |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략을 표시           | SQL\> SELECT ename FROM employee; <br />ENAME  <br />----------------------- <br />SWNO  <br />HJNO  <br />HSCHOI  <br />. . . <br />20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이외의 기호들                             | EXEC :p1 := 1; <br />acc NUMBER(11,2);                       |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치 | SELECT \* FROM *table_name*; <br />CONNECT *userID*/*password*; |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 컬럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드       | DESC SYSTEM_.SYS_INDICES_;                                   |

#### 관련 자료

자세한 정보를 위하여 Altibase의 다음 문서 목록을 참조한다.

- Installation Guide
- Getting Started Guide

- Administrator’s Manual

- Replication Manual

- Precompiler User’s Manual

- API User’s Manual

- Altibase C Interface Manual

- iSQL User’s Manual

- Utilities Manual

- General Reference

- Error Message Reference

#### Altibase는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음 버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께 고객서비스포털(http://support.altibase.com/kr/ )로 보내주시기 바랍니다.

- 사용 중인 매뉴얼의 이름과 버전

- 매뉴얼에 대한 의견

- 사용자의 성함, 주소, 전화번호

이 외에도 Altibase 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인 문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인 부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를 요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.

<br>

1.dataCompJ 소개
=====================

이 장은 dataCompJ의 특징을 이해하고자 하는 사용자에게 이 도구를 소개하고 설치하는 방법을 설명한다. 이 장은 다음의 절로 구성된다.

- 개요
- 시스템 요구 사항
- 설치 및 제거

### 개요

dataCompJ는 Altibase에서 이기종 데이터베이스로 복제한 데이터를 대상으로 데이터 정합성 확인과 데이터 불일치를 해소하기 위한 도구이다. 테이블 단위로 데이터를 비교하고 데이터 불일치가 있는 경우 이에 관한 정보를 파일로 출력한다. 불일치 데이터를 Slave 데이터베이스에 직접 적용하여 데이터를 일치시키는 기능도 제공한다.

dataCompJ 작업 대상 데이터는 Altibase에서 제공하는 데이터 복제 도구인 Adapter for Oracle 또는 Adapter for JDBC를 사용하여 복제한 데이터를 대상으로 한다.

dataCompJ는 편리한 사용성과 빠른 성능으로, 효율적인 이기종 데이터베이스 간 데이터 관리 방법을 제공한다.

### 시스템 요구 사항

이 절은 dataCompJ를 설치하고 실행하기 위해 필요한 시스템 사양에 대해 설명하고, dataCompJ와 호환되는 데이터베이스 관리 시스템을 열거한다.

#### 하드웨어 요구 사항

- CPU: 800MHz 펜티엄 III 이상
- 메인 메모리: 최소 512MB, 4GB 이상 권장
- 디스크: 50MB 이상의 여유 공간

#### 소프트웨어 요구 사항

- Oracle, OpenJDK 또는 IBM Java 8 이상의 JRE

dataCompJ는 순수 Java 기반 클라이언트 애플리케이션으로 하드웨어 및 운영체제에 상관없이 독립적으로 실행되나, 자바 런타임 환경(JRE)에 의존적이므로 환경에 맞는 JRE를 설치해야 한다. 또한 설치된 Java의 경로를 가리키는 JAVA_HOME 환경변수가 설정되어 있어야 한다.

#### 호환되는 데이터베이스 관리 시스템

##### Master DB

- Altibase: Altibase 5.3.3 이상

##### Slave DB

- Oracle: Oracle 9i 이상
- MariaDB: MariaDB 5.5.x 이상

Master/Slave DB의 의미는 ['용어](#용어)'절을 참조한다.

dataCompJ는 Altibase 및 이기종 데이터베이스들과 함께 사용할 수 있다. 데이터베이스 접속을 위해 JDBC 드라이버를 사용하므로, 원본 데이터베이스와 대상 데이터베이스에 호환되는 JDBC 드라이버를 준비하는 것이 중요하다. 현재 오라클용 JDBC 드라이버인 ojdbc5.jar를 제공한다.

#### 설치 및 제거

dataCompJ는 [Altibase 고객 서비스 포털](#http://support.altibase.com)에서 내려받을 수 있다. dataCompJCli라는 이름의 zip 또는 tar.gz 파일 형식으로 제공된다. 다운로드받은 압축 파일을 원하는 위치에 해제하면 dataCompJ 설치가 완료된다. 생성된 디렉토리 안에는 실행파일인 dataCompJCli.sh, JDBC 드라이버를 포함한 JDBC 하위 디렉토리 및 XML 기본 설정 파일이 존재한다.
dataCompJ를 제거하기 위해서는 dataCompJ가 설치되어 있는 디렉토리를 삭제한다.

<br>

2.dataCompJ 시작하기
=====================

이 장은 사용자들이 dataCompJ를 좀 더 능률적이고 효율적으로 실행하는 데 도움이 되는 기본 개념을 소개한다. 이 장은 다음의 절로 구성된다.

- 용어

- 불일치 레코드
- 일치 정책

### 용어

##### Master DB

비교 대상인 두 이기종 데이터베이스 중 원본 데이터를 가진 Altibase 데이터베이스이다.

##### Slave DB

비교 대상인 두 이기종 데이터베이스 중 복제된 데이터가 적용되는 다른 벤더의 데이터베이스이다.

##### TablePair

사용자가 지정하는 dataCompJ의 비교 대상을 의미하며 테이블 단위이다. Master DB에 있는 하나의 테이블(Master table)과 Slave DB에 있는 하나의 테이블(Slave table)이 쌍을 이룬다.

##### Master 테이블

TablePair 중 사용자가 지정한 Master DB의 비교 대상 테이블이다.

##### Slave 테이블

TablePair 중 사용자가 지정한 Slave DB의 비교 대상 테이블이다.

### 불일치 레코드(Inconsistent record)

불일치 레코드는 Master 테이블과 Slave 테이블의 주요 키(Primary Key)를 기준으로 컬럼 값이 일치하지 않는 레코드들을 의미한다. 불일치 레코드 종류는 다음과 같이 세 가지 타입이 있다.

##### MOSO 불일치

동일한 주요 키 컬럼들(Primary key columns) 값을 가진 특정 레코드가 Master 테이블과 Slave 테이블에 모두 존재하지만, 주요 키가 아닌 컬럼들(Non primary key columns)의 값이 서로 다른 경우

##### MOSX 불일치

특정 주요 키 컬럼들(Primary key columns) 값을 가진 레코드가 Master 테이블에만 존재하고 Slave 테이블에는 존재하지 않는 경우

##### MXSO 불일치

특정 주요 키 컬럼들(Primary key columns) 값을 가진 레코드가 Master 테이블에는 존재하지 않고 Slave 테이블에만 존재하는 경우

##### 불일치 레코드 처리

1.  DIFF: Master 테이블과 Slave 테이블 간의 불일치 레코드를 식별하여 CSV 형식의 파일에 기록한다.
2.  SYNC: Master 테이블과 Slave 테이블 간의 불일치 레코드를 식별하여 dataCompJ 설정 파일에 기술된 일치 정책에 따라 불일치를 해소한다.

### 일치 정책 (Synchronization policy)

일치 정책은 dataCompJ가 불일치 레코드를 발견하였을 때, Master 테이블의 레코드를 기준으로 Slave 테이블의 레코드를 어떻게 일치시킬지 명시하는 정책이다. 일치 정책으로 다음과 같은 세 가지 방법을 제공한다.

##### MOSO 불일치

UPDATE_TO_SLAVE 정책이다. Master 테이블의 레코드를 기준으로 동일한 주요 키를 가진 Slave 테이블의 레코드를 변경(update)한다.

##### MOSX 불일치

INSERT_TO_SLAVE 정책이다. Master 테이블에만 존재하고 Slave 테이블에는 존재하지 않는 레코드를 Slave 테이블에 삽입(insert)한다.

##### MXSO 불일치

DELETE_FROM_SLAVE 정책이다. Master 테이블에는 존재하지 않고 Slave 테이블에만 존재하는 레코드를 Slave 테이블에서 삭제(delete)한다.

<br>

3.dataCompJ 사용 방법
=====================

이 장은 dataCompJ를 원활하게 실행하는 방법과 dataCompJ의 설정 파일 구성, 설정 시 고려할 점들을 설명한다. 이 장은 다음의 절로 구성된다.

- 실행 방법
- 수행 단계
- 설정 파일 구성

### dataCompJ 실행 방법

dataCompJ를 Command Line Interface (CLI)에서 수행하는 명령어는 다음과 같다.

- Linux

  ```
  $ dataCompJCli.sh -f dataCompJ_env_file_path
  ```


- Windows

  ```
  C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path
  ```

**dataCompJ_env_file_path**

dataCompJ 설정 파일의 경로를 의미하며 필수 옵션이다. dataCompJ 설치 시 dataCompJ.xml 이라는 설정 파일을 제공한다. 사용자는 이 파일을 이용하거나 새로운 이름의 설정 파일을 사용할 수 있다.

### dataCompJ 수행 단계

dataCompJ는 사용자가 설정한 설정 파일을 기반으로 동작하며, 크게 구축(Build)과 실행(Run)이라는 두 단계를 수행한다.

##### 구축(Build) 단계

구축 단계는 주어진 설정 파일을 기반으로 실행(Run) 단계가 수행 가능한지 판단하기 위한 초기 조사 단계이다. 하나의 문제라도 발견되면 이를 리포트 파일(dataCompJ_report.txt)에 출력하며 dataCompJ를 종료한다.

구축 단계는 아래의 순서대로 진행된다.

1.  사용자가 지정한 설정 파일을 읽는다.

2.  설정 파일에 기술된 접속정보가 유효한지 확인한다.

3.  설정 파일에 기술된 대상 테이블들의 유효성을 검증하기 위해 양쪽 데이터베이스에 접속하여 메타 정보를 확인한다. 테이블 중 어느 한쪽에서라도 문제를 발견하면 리포트 파일에 출력하고 dataCompJ를 종료한다.

##### 실행(Run) 단계

실행 단계는 대상 테이블들의 데이터를 비교하여, 사용자의 선택에 따라 비교(DIFF) 또는 일치(SYNC) 기능을 수행하는 단계이다.

각 TablePair의 수행 결과는 출력 파일 (dataCompJ_report.txt)에 출력된다.

##### 출력 파일

dataCompJ를 수행하면 텍스트 형식의 리포트 파일 1개, 로그 파일 2개가 생성된다.

비교(DIFF) 기능에 의해 생성되는 출력 파일에 대한 상세한 설명은 '[비교(DIFF) 기능](#비교diff-기능)'을 참고한다.

-   dataCompJ_report.txt: 수행 결과를 정리하여 사용자에게 전달하기 위한 텍스트 형태의 리포트 파일이다.
-   dataCompJ.log: 프로그램 수행 시 발생하는 이벤트를 기록하는 로그 파일이다. 프로그램의 상세 수행 이력을 추적하기 위해 사용한다.
-   dataCompJ_data.log: 실행(Run) 단계에서 생성되는 로그 파일로, 사용자가 설정 파일의 \<TraceInconsistentRecord\>를 true로 설정한 경우 비교(DIFF)/일치(SYNC) 수행 시 처리되는 불일치 레코드의 상세 내용을 기록한다.
    불일치 레코드가 많은 경우 대용량의 파일이 생성되고 프로그램의 처리 성능이 저하되기 때문에, 불일치 레코드 처리 내역에 대한 상세 내용이 필요한 경우에만 사용을 권장한다.


### dataCompJ 설정 파일 구성

dataCompJ를 수행하기 위해서는 설정 파일 입력이 필수이다. dataCompJ 설치 시 dataCompJ.xml 라는 파일을 기본 설정 파일로 제공하며, 사용자가 임의의 파일을 작성하여 사용할 수도 있다. 단, dataCompJ.xml에 기술된 XML 규칙에 따라 작성해야 하며 다국어가 포함된 경우 반드시 UTF-8로 인코딩해야 한다.

dataCompJ 설정 파일은 크게 [Connections](#connections), [Options](#options), [TablePairs](#tablepairs) 3개 부분으로 구성된다.

##### Connections

Connections는 Master DB 및 Slave DB에 접속하기 위한 정보를 기록하는 부분이다.

###### \<MasterDB\>

Master DB의 접속 정보를 기록한다. Master DB의 종류는 반드시 Altibase 데이터베이스여야 한다. 아래 XML Element는 Master DB의 하위 요소들이다.

\<JdbcUrl\>  
JDBC 접속에 사용되는 정보로 데이터베이스 사용자 아이디와 암호를 제외한 나머지 정보를 기록하는 문자열이다.

\<JdbcFilePath\>  
Master DB 접속에 사용할 JDBC jar file이 존재하는 경로를 지정한다.

\<UserId\>  
데이터베이스 접속을 위한 사용자 아이디를 지정한다.

\<Password\>  
데이터베이스 접속을 위한 사용자 아이디의 암호를 지정한다.

\<FetchSize\>  
데이터베이스에서 데이터를 가져오는 작업을 할 때, 한번에 가져오는 레코드의 개수를 지정한다. 이 항목은 선택 항목이며, 기본값은 1,000이다.

\<BatchSize\>  
데이터베이스에 INSERT/DELETE/UPDATE와 같은 변경 작업을 수행할 때, 한 번에 수행되는 레코드 개수를 지정한다. 예를 들어 이 항목에 10을 지정하면, 10개 레코드 단위로 INSERT/DELETE/UPDATE를 수행한다. 이 항목은 선택 항목이며, 기본값은 1,000이다.

###### \<SlaveDB\>

Slave DB의 접속 정보를 기록한다. Slave DB의 하위 요소들은 위에서 기술한 [Master DB](#masterdb)의 하위 요소들과 동일하다.

##### Options

Options는 dataCompJ의 수행에 필요한 사용자 설정값을 입력하는 부분이다.

###### \<Operation\>

불일치 데이터 처리를 위한 기능을 지정하는 항목으로 비교(DIFF)나 일치(SYNC) 둘 중 하나의 기능을 선택한다.

###### \<FileEncoding\>

dataCompJ 수행 시 생성되는 파일들의 encoding 타입을 지정한다.

###### \<Diff\>

\<DirPath\>  
비교(DIFF)를 수행하였을 때 비교 대상 테이블별 결과 CSV 파일이 생성되는 디렉토리 경로를 지정한다.

###### \<Sync\>

일치(SYNC) 기능 수행 시 옵션들

\<MOSO UPDATE_TO_SLAVE="true"/\>  
MOSO 불일치 데이터 발견 시 Master 테이블 레코드 기준으로 Slave 테이블의 레코드를 업데이트(Update)할지 여부이다. False를 선택하면 MOSO 불일치 데이터를 처리하지 않는다.

\<MOSX INSERT_TO_SLAVE="true"/\>  
MOSX 불일치 데이터 발견 시 Master 테이블에만 존재하는 레코드를 Slave 테이블에 삽입(Insert)할지 여부이다. False를 선택하면 MOSX 불일치 데이터를 처리하지 않는다.

\<MXSO DELETE_FROM_SLAVE="true"/\>  
MXSO 불일치 데이터 발견 시 Master 테이블에 존재하지 않는 Slave 테이블의 레코드를 삭제(Delete)할지 여부이다. False를 선택하면 MXSO 불일치 데이터를 처리하지 않는다.

###### \<Log\>

아래 XML Element는 Log의 하위 요소들이다.

\<DirPath\>  
dataCompJ 수행 시 생성되는 로그 파일들의 디렉토리 경로를 지정한다.

\<TraceInconsistentRecord\>  
DIFF/SYNC 수행 시 발견되는 모든 불일치 레코드의 상세 내역을 dataCompJ_data.log 파일에 기록할지 여부를 True/False 값으로 결정한다.

###### \<MaxThread\>

dataCompJ에 할당 가능한 최대 쓰레드 개수이다. 0으로 지정하는 경우, dataCompJ가 수행되는 장비의 CPU core 갯수를 MaxThread 값으로 할당한다.

##### TablePairs

TablePairs는 비교 대상 테이블들을 기록하는 부분이다. 비교 대상 테이블에 대한 개별 정보를 기록하는 방법과 일괄적으로 테이블 이름들이 나열되어 있는 텍스트 파일 경로를 지정하는 방법 두 가지를 제공한다. 이 두 가지 방법은 개별로도 사용 가능하며 동시에 사용도 가능하다.

개별 테이블에 대한 정보를 제공하는 방법은 아래와 같으며, 데이터 비교 방법을 상세히 제어할 수 있다는 장점이 있다. 예를 들어, 데이터 비교 시 특정 컬럼을 제외시키거나 특정 조건을 만족하는 데이터들만 비교 대상으로 할 수도 있다.

비교 대상인 테이블 이름은 Master DB와 Slave DB 모두에서 허용하는 이름이어야 한다. XML 파일에 있는 테이블 이름에 공백, 특수문자 등이 있거나 대소문자를 구분해야 하는 경우 큰따옴표(")를 사용한다. 예를 들어, 비교 대상 테이블 이름이 SYS schema의 Employee 01이면, 테이블 이름이 공백을 포함하기 때문에 SYS."Employee 01"처럼 테이블 이름에 큰 따옴표를 사용한다.

###### \<TablePair\>

데이터 비교 대상 단위로 하나의 Master 테이블과 하나의 Slave 테이블로 구성된다. 아래의 XML element는 TablePair의 하위 요소들이다.

\<MasterTable\>  
Master DB에 존재하는 비교 대상 테이블의 이름으로 [*SchemaName*].*TableName* 형식으로 지정한다. 스키마 이름을 별도로 지정하지 않으면 Master DB의 UserId를 기본 스키마 이름으로 사용한다. 이 항목은 필수 항목으로, 기술되지 않으면 프로그램 수행 시 에러가 발생한다.

\<SlaveTable\>  
Slave DB에 존재하는 비교 대상 테이블의 이름으로 [*SchemaName*].*TableName* 형식으로 지정한다. 스키마 이름을 별도로 지정하지 않으면 Slave DB의 UserId를 기본 스키마 이름으로 사용한다. 이 항목은 선택 항목으로, 기술되지 않으면 \<MasterTable\>과 같은 이름으로 간주한다.

\<Exclude\>  
테이블의 레코드를 Projection하는 조건을 지정한다. 쉼표(,)를 구분자로 사용하여 여러 개의 컬럼을 지정할 수 있다. 이 항목은 선택 항목으로, 기술되지 않으면 dataCompJ가 지원하는 데이터 타입을 가진 모든 컬럼들을 비교대상으로 선택한다.

\<Where\>  
테이블의 레코드를 Selection하는 조건을 지정한다. SQL 문의 WHERE 절에 기술하는 방식과 동일하게 기술하며 다중 조건을 허용한다. 단, 양쪽 데이터베이스에 동일하게 적용되므로 양쪽 데이터베이스 문법에 모두 적합해야 한다. 이 항목은 선택 항목으로, 기술되지 않으면 모든 레코드들을 비교 대상으로 한다.

\<TableNameFilePath\>  
일괄적으로 테이블 이름들을 나열한 텍스트 파일 경로를 제공하는 방법은 아래와 같으며, 다수의 테이블들을 일괄적으로 비교해야 하는 경우 테이블 입력을 손쉽게 할 수 있다는 장점이 있다.

```
<TableNameFilePath>table_name_file_path</TableNameFilePath>
```

table_name_file_path는 테이블 이름들을 나열한 텍스트 파일의 경로이다. 비교 대상 테이블의 이름은 [SchemaName].TableName 형식으로 지정할 수 있으며, 각각의 테이블 이름은 개행 문자로 구분한다. MasterDB의 비교 대상 테이블 이름과 SlaveDB의 비교 대상 테이블 이름은 반드시 일치해야 한다.

###### 제약 사항

비교 대상의 테이블을 선택할 때 다음의 제약 사항을 반드시 고려해야 한다. 하나의 제약 사항이라도 위반한 경우, dataCompJ는 구축 단계에서 발생한 문제점을 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행 단계를 수행하지 않는다.

1.  하나의 비교대상 테이블은 Master DB와 Slave DB에 반드시 동일하게 (컬럼 이름, 컬럼 순서, 데이터 타입, 주요 키) 구성되어야 한다. 단, 데이터 타입은 이기종 데이터베이스간 서로 비교 가능한 타입이면 가능하다.

2.  지원하지 않는 데이터 타입의 컬럼은 비교 대상에서 자동으로 제외된다. (예, LOB과 같은 Binary Type)

3.  주요 키(primary key) 외에 값을 비교할 수 있는 컬럼이 적어도 한 개 이상이어야 한다.

    (예제 1) table1 (c1 int, c2 int, c3 CLOB, primary key (c1, c2))  
    (예제 2) table1 (c1 int, c2 int, c3 varchar(100), primary key (c1, c2))  
    예제 1에서 '제약조건 3'을 만족하는 컬럼은 c3 뿐이다. 단, c3 컬럼의 데이터 타입인 CLOB은 dataCompJ가 지원하지 않기 때문에, '제약 사항 2'를 위반한다. 따라서, table1에 대한 비교는 허용되지 않는다.  
    예제 2에서 '제약 사항 3'을 만족하는 컬럼은 c3 뿐이다. 또한, c3의 데이터 타입이 dataCompJ가 지원하는 varchar 타입이기 때문에 table1에 대한 비교가 가능하다.

<br>

4.dataCompJ 기능
=====================

이 장은 dataCompJ의 비교(DIFF) 기능과 일치(SYNC) 기능을 보다 자세히 예제와 함께 설명한다.

- 비교 (DIFF) 기능
- 일치 (SYNC) 기능

### 비교(DIFF) 기능

비교(DIFF) 기능은 Master DB와 Slave DB 간의 이기종 복제 작업에서 발생할 수 있는 불일치 레코드들을 식별하고 이들을 파일에 기록하여, 두 데이터베이스 시스템간의 불일치 레코드들을 확인한다.

#### 설정 파일

dataCompJ 설정파일의 \<Options\> - \<Operation\> 값을 “DIFF”로 지정한다.

\<Connections\>와 \<Options\>의 항목들은 모두 필수로 기입해야 하며, 대상 테이블에 대해 \<TablePairs\>에 기술해야 한다.

##### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
        <JdbcFilePath>./jdbc/Altibase710.jar</JdbcFilePath>
        <UserId>sys</UserId>
        <Password>manager</Password>
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
        <JdbcFilePath>./jdbc/ojdbc5.jar</JdbcFilePath>
        <UserId>altibase</UserId>
        <Password>altibase</Password>
    </SlaveDB>
</Connections>

<Options>
    <Operation>DIFF</Operation>
    <FileEncoding>UTF-8</FileEncoding>
    <Diff>
        <DirPath>./diff/</DirPath>
    </Diff>
    <Sync>
        <MOSO UPDATE_TO_SLAVE="true"/>
        <MOSX INSERT_TO_SLAVE="true"/>
        <MXSO DELETE_FROM_SLAVE="true"/>
    </Sync>
    <Log>
        <DirPath>./</DirPath>
        <TraceInconsistentRecord>false</TraceInconsistentRecord>
    </Log>
    <MaxThread>0</MaxThread>
</Options>

<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### 실행 방법

비교(DIFF)는 다음과 같이 실행한다.

```
$ dataCompJCli.sh -f dataCompJ.xml
```

#### 실행 결과

실행 결과로 수행 결과가 요약된 리포트 파일( dataCompJ_report.txt)과 수행 중 이벤트가 기록되는 로그파일들(dataCompJ.log, dataCompJ_data.log)이 생성된다. 보다 상세한 설명은 [출력 파일](#출력-파일)을 참고한다.

예제에 사용되는 테이블의 구조는 아래와 같다.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int);
```

##### DIFF 수행

```
$ dataCompJCli.sh -f dataCompJ.xml
----------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
----------------------------------------------------------
* Build started  at 2016-12-14 16:30:03.673
* Build finished at 2016-12-14 16:30:04.357 (Elapsed: 0:00:00.691)
* Run   started  at 2016-12-14 16:30:04.374
* Run   finished at 2016-12-14 16:30:04.905 (Elapsed: 0:00:00.531)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
```

###### 리포트 파일 내용 확인

```
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 16:30:03.673
     - Finished : 2016-12-14 16:30:04.357
     - Elapsed  : 0:00:00.691
--------------------------------------------------------

[ User input information ]
...

[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
==========================================================
    Run
     - Started  : 2016-12-14 17:19:42.731
     - Finished : 2016-12-14 17:19:42.822
     - Elapsed  : 0:00:00.091
----------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------

```

##### 실행 데이터 파일

비교(DIFF) 기능을 선택하였을 때 TablePair 단위로 다음 4개의 CSV 형식의 데이터 파일들이 생성된다.

-   *SchemaName.TableName*\_MASTER_diff.csv:  
    MOSO 불일치 발생 시 Master 테이블의 해당 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_SLAVE_diff.csv:  
    MOSO 불일치 발생 시 Slave 테이블의 해당 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_MASTER_only.csv:  
    MOSX 불일치 발생 시 Master 테이블에만 존재하는 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_SLAVE_only.csv:  
    MXSO 불일치 발생 시 Slave 테이블에만 존재하는 레코드 값을 CSV 형태로 저장하는 파일.

*SchemaName.TableName*\_MASTER_diff.csv 파일과 *SchemaName.TableName*\_SLAVE_diff.csv 파일에는 MOSO 불일치 데이터가 같은 순서로 기록되기 때문에, DIFF 프로그램으로 두 개의 파일을 비교하면 MOSO 불일치가 발생한 부분을 직관적으로 비교할 수 있다.

#### 예제

예제에 사용되는 테이블의 구조는 아래와 같다.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int); /* C3 CLOB dataCompJ에서 지원하지 않는 데이터 타입 */
CREATE TABLE ex2 (C1 int primary key, C2 varchar(20), C3 int);
```

##### DIFF 예제 1

두 개의 테이블을 대상으로 스키마 이름을 생략 또는 명시하는 예제이다.

아래의 예제에서 EX1 테이블의 경우 \<MasterTable\>항목은 스키마 이름 없이 테이블 이름만 기술하고, \<SlaveTable\> 항목은 생략했다. 스키마 이름 없이 테이블 이름만 기술한 \<MasterTable\>은 \<MasterDB\>-\<UserId\>에 입력된 값을 스키마 이름으로 사용한다. 생략된 \<SlaveTable\>은 \<MasterTable\>과 같은 값으로 가정하여 처리된다.

EX1 테이블의 C3 컬럼은 dataCompJ가 지원하지 않는 데이터 타입인 CLOB으로 비교 대상에서 자동으로 제외되며, 리포트의 Candidate tables 항목에 이 내용이 기록된다.

EX2 테이블은 스키마 이름과 테이블 이름을 사용자가 명시적으로 입력하였고, 입력받은 스키마 이름과 테이블 이름을 기반으로 처리된다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>DIFF</Operation>
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 2 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns:
===========================================================================
    Run
     - Started  : 2016-12-14 17:56:04.516
     - Finished : 2016-12-14 17:56:04.593
     - Elapsed  : 0:00:00.076
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
```

##### DIFF 예제 2

대상 테이블의 특정 컬럼을 사용자가 명시적으로 제외하고(Exclude), 특정 조건을 만족하는 레코드(Where)만을 대상으로 비교(Diff) 수행하는 예제이다.
dataCompJ.xml의 EX1 테이블에 대해 주요 키가 아닌 컬럼들 중 C4 컬럼을 비교 대상에서 제외하고 C1 컬럼값이 5보다 큰 레코드만 비교 작업을 수행하도록 사용자가 명시적으로 입력한다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
...
<Options>
    <Operation>DIFF</Operation>
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
        <Exclude>C4</Exclude>
        <Where>C1 > 5</Where>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 2 ]
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2 FROM SYS.EX1 WHERE C1 > 5 ORDER BY C1 ASC
    * Excluded columns     : C4
    * Where condition      : C1 > 5
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns:
===========================================================================
    Run
     - Started  : 2016-12-14 17:57:09.895
     - Finished : 2016-12-14 17:57:09.974
     - Elapsed  : 0:00:00.080
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:            5
 Fetched record count from SLAVE :            5
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               5
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

### 일치(SYNC) 기능

일치(SYNC)기능은 Master DB와 Slave DB 간의 이기종 복제 작업에서 발생할 수 있는 불일치 레코드들을 식별하여 이를 Slave DB에 적용한다. 두 데이터베이스 시스템의 데이터 동기화(Synchronization)를 손쉽게 할 수 있다.

#### 설정 파일

dataCompJ 설정 파일의 \<Options\> - \<Operation\> 값을 “SYNC”로 지정한다.

\<Connections\>와 \<Options\> 항목들은 모두 필수로 기입해야 하며, 대상 테이블에 대해 \<TablePairs\>에 기술해야 한다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>SYNC</Operation>
...
</Options>

<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### 실행 방법

일치(SYNC) 기능은 다음과 같이 실행한다.

```
$ dataCompJCli.sh -f dataCompJ.xml
$ dataCompJCli.sh -f ./dataCompJ.xml
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:08:40.407
* Build finished at 2016-12-14 18:08:41.076 (Elapsed: 0:00:00.676)
* Run   started  at 2016-12-14 18:08:41.090
* Run   finished at 2016-12-14 18:08:41.654 (Elapsed: 0:00:00.564)
---------------------------------------------------------------------------
Refer to the following output files for details.
---------------------------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record

```

#### 실행 결과

실행 결과로 수행 결과가 요약된 리포트 파일(dataCompJ_report.txt)과 수행 중 이벤트가 기록되는 로그 파일들(dataCompJ.log, dataCompJ_data.log)이 생성된다. 보다 상세한 설명은 [출력 파일](#출력-파일)을 참고한다.

###### dataCompJ_report.txt

```
$ cat dataCompJ_report.txt
===========================================================================
    Build
     - Started  : 2016-12-14 18:08:40.407
     - Finished : 2016-12-14 18:08:41.076
     - Elapsed  : 0:00:00.676
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)

===========================================================================
    Run
     - Started  : 2016-12-14 18:08:41.090
     - Finished : 2016-12-14 18:08:41.654
     - Elapsed  : 0:00:00.564
---------------------------------------------------------------------------

1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type    Resolution                Try         Fail
------------------------------------------------------
MOSO    UPDATE TO SLAVE                  2           0
MOSX    INSERT TO SLAVE                  1           0
MXSO    DELETE FROM SLAVE                1           0
------------------------------------------------------
```

모든 대상 테이블과 레코드들에 대해 SYNC가 정확히 수행된 경우, 동일한 대상 테이블에 대해 DIFF 기능을 재수행하면 모든 레코드가 동일하다는 비교 결과를 얻게 된다.

```
$ dataCompJCli.sh -f ./dataCompJ.xml
-----------------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:11:54.924
* Build finished at 2016-12-14 18:11:55.561 (Elapsed: 0:00:00.645)
* Run   started  at 2016-12-14 18:11:55.580
* Run   finished at 2016-12-14 18:11:56.190 (Elapsed: 0:00:00.610)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.

$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 18:11:54.924
     - Finished : 2016-12-14 18:11:55.561
     - Elapsed  : 0:00:00.645
---------------------------------------------------------

[ User input information ]
...

[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)

==========================================================
    Run
     - Started  : 2016-12-14 18:11:55.580
     - Finished : 2016-12-14 18:11:56.190
     - Elapsed  : 0:00:00.610
---------------------------------------------------------------------------

1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

<br>

# A. 부록: 이기종간 데이터 타입 호환 테이블

dataCompJ가 지원하는 이기종 데이터베이스 간의 데이터 타입 매핑 테이블이다.

dataCompJ가 지원하지 않는 데이터 타입을 가진 테이블을 대상으로 데이터 비교를 수행하면 다음과 같이 처리된다.

-   Master 테이블과 Slave 테이블 모두 dataCompJ가 지원하지 않는 데이터 타입인 경우: 구축(Build) 단계에서 지원하지 않는 데이터 타입이라는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(Run) 단계를 수행하지 않는다.

-   Master 테이블과 Slave 테이블 둘 중 하나만 지원하는 데이터 타입인 경우: 구축(Build) 단계에서 테이블의 비교 대상 컬럼의 개수가 다르다는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(run) 단계를 수행하지 않는다.

dataCompJ가 지원하는 데이터 타입이지만, 비교 대상 테이블의 컬럼 데이터 타입이 이기종간 데이터 타입 호환 테이블과 다른 데이터 타입 조합을 사용하는 경우 다음과 같이 처리된다.

-   데이터 비교 자체가 아예 불가능한 타입의 경우 (예를 들어, 정수형과 문자형 데이터 타입간의 비교): 구축(build) 단계에서 호환되지 않는 타입이라는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(run) 단계를 수행하지 않는다.

-   비교는 가능하지만 상이한 데이터 타입의 경우 (예를 들어, 정수형과 부동 소수점 형): 구축(build) 단계에서 처리할 수 없으므로, 그대로 실행(run) 단계를 수행한다. 단, 수행 결과에 모든 레코드가 불일치 레코드로 처리된다.

#### Altibase to Oracle

| Altibase | Oracle         | 설명                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| SMALLINT | NUMBER         |                                                              |
| INTEGER  | NUMBER         |                                                              |
| BIGINT   | NUMBER         |                                                              |
| NUMERIC  | NUMBER         |                                                              |
| REAL     | NUMBER         |                                                              |
| DOUBLE   | NUMBER         |                                                              |
| FLOAT    | FLOAT          |                                                              |
| DATE     | DATE TIMESTAMP | - DATE-TIMESTAMP의 경우 소수점의 자릿수가 짧은 쪽을 기준으로 하여 비교한다. 예를 들어 Altibase DATE는 마이크로 초까지 지원하고, Oracle의 TIMESTAMP는 나노 초까지 지원 한다. 이 경우, 레코드의 동일 여부 비교는 나노 초를 기준으로 한다.<br />- DATE-DATE의 경우 Oracle DATE 타입은 YYYY-MM-DD HH:MM:SS까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 소수점 이하의 초는 무시하고 동일한 YYYY-MM-DD HH:MM:SS 형식으로 비교한다. |
| CHAR     | CHAR           |                                                              |
| VARCHAR  | VARCHAR2       |                                                              |
| NCHAR    | NCHAR          |                                                              |
| NVARCHAR | NVARCHAR2      |                                                              |

#### Altibase to MariaDB

| Altibase | MariaDB                                       | 설명                                                         |
| -------- | --------------------------------------------- | ------------------------------------------------------------ |
| SMALLINT | SMALLINT                                      |                                                              |
| INTEGER  | INT                                           |                                                              |
| BIGINT   | BIGINT                                        |                                                              |
| NUMERIC  | DECIMAL                                       |                                                              |
| REAL     | FLOAT                                         |                                                              |
| DOUBLE   | DOUBLE                                        |                                                              |
| FLOAT    | N/A                                           | Altibase Float 타입에 해당하는 MariaDB의 데이터 타입은 없다. |
| DATE     | DATE, DATETIME, TIMESTAMP                     | - DATE-DATE: MariaDB의 DATE는 YYYY-MM-DD까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 날짜 이하는 무시하고 동일한 YYYY-MM-DD 형식으로 비교한다. <br />- DATE-DATETIME: MariaDB의 DATE는 YYYY-MM-DD HH:MM:SS까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 소수점 이하의 초는 무시하고 동일한 YYYY-MM-DD HH:MM:SS 형식으로 비교한다.<br />- DATE-TIMESTAMP: MariaDB의 DATE는 YYYY-MM-DD HH:MM:DD Microseconds 0 \~ 6 (default: 0)까지 지원한다. 따라서, Altibase DATE 데이터에서 동일한 부분을 추출하여 비교한다. |
| CHAR     | CHAR                                          |                                                              |
| VARCHAR  | VARCHAR, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT |                                                              |
| NCHAR    | CHAR with Character set                       |                                                              |
| NVARCHAR | VARCHAR with Character set                    |                                                              |
<!-- SOURCE_BLOCK_END source_id="SRC-000227" block_id="BLOCK-000935" -->

## SRC-000449 - Release 7.2 (Feb. 17, 2022)

| Field | Value |
| --- | --- |
| `source_id` | SRC-000449 |
| `source_path` | ReleaseNotes/eng/Altibase_dataCompJ_7_2_Release_Notes.md |
| `source_family` | utilities_datacompj |
| `version_scope` | dataCompJ 7.2 |
| `language` | en |
| `authority_label` | English extraction aid |
| `source_sha256` | 178f574a01368353b7a381274a6ef7658c5e5670c0031c4d9b051141c510ab29 |
| `byte_count` | 5733 |
| `line_count` | 209 |
| `estimated_tokens` | 1413 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000449" source_path="ReleaseNotes/eng/Altibase_dataCompJ_7_2_Release_Notes.md" source_family="utilities_datacompj" version_scope="dataCompJ 7.2" language="en" authority_label="English extraction aid" sha256="178f574a01368353b7a381274a6ef7658c5e5670c0031c4d9b051141c510ab29" byte_count="5733" line_count="209" estimated_tokens="1413" block_id="BLOCK-000936" -->
dataCompJ Release Notes
================

#### Release 7.2 (Feb. 17, 2022)

Altibase® Tools & Utilities

<br><br><br><br><br><br>
<!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>


<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Release Notes dataCompJ
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>


<br>

# Table Of Contents

- [1. Overview](#1-overview)
  - [1.1 Hardware Requirements](#11-hardware-requirements)
  - [1.2 Supported Operating Systems and Platforms](#12-supported-operating-systems-and-platforms)
- [2. Release Information](#2-release-information)
  - [2.1 Version](#21-version)
  - [2.2 New Features](#22-new-features)
  - [2.3 Bug Fixed](#23-bug-fixed)
  - [2.4 Database Compatibility](#24-database-compatibility)
  - [2.5 Properties](#25-properties)
  - [2.6 Error Messages](#26-error-messages)
- [3. Open Source Libraries Used](#3-open-source-libraries-used)
- [4. Packages](#4-packages)
- [5. Downloads](#5-downloads)
  - [5.1 Packages](#51-packages)

<br>

# 1. Overview

 Altibase dataCompJ is a utility designed to guarantee data consistency between two heterogeneous databases and resolve data inconsistency if any. The main target data for comparing in dataCompJ is replicated data from Altibase to another heterogeneous database using Altibase Adapter for Oracle (oraAdapter) or JDBC Adapter provided by Altibase. dataCompJ compares Altibase with another heterogeneous database on a table-by-table basis, and outputs information on any inconsistency it detects.
Also, it offers an efficient feature for synchronizing two databases in the event of data inconsistency. A proper use of Altibase dataCompJ would be a cornerstone of effective data management with advantageous usability along with its advanced technical performance.  

### 1.1 Hardware Requirements

- CPU: 800 MHz Pentium III or better
- Main memory: Minimum 512MB, 4GB or more recommended
- Disk: More than 50MB of free space for installation

### 1.2 Supported Operating Systems and Platforms

| Mode | JRE                                                         |
| ---- | ----------------------------------------------------------- |
| CLI  | Oracle, OpenJDK or IBM Java Runtime Environment 8 or higher |

dataCompJ is a pure Java-based client application relying on the JAVA Runtime Environment (JRE) instead of the client's hardware or an operating system.

<br>

# 2. Release Information

### 2.1 Version

- 7.2

### 2.2 New Features

- N/A

### 2.3 Bug Fixed

| PK        | Synopsis                                                     |
| --------- | ------------------------------------------------------------ |
| BUG-45222 | Requires handling of user-entered object names enclosed in double quotation marks. |
| BUG-46675 | Error message for the unsupported DB JDBC URL should be provided more clearly. |
| BUG-46689 | Need to modify the DB type check routine using the JDBC URL string. |
| BUG-49501 | dataCompJ log4j upgraded to version 2.17.1 due to security issues. |

### 2.4 Database Compatibility

#### Master Database

- Altibase: Altibase 5.3.3 or higher

#### Slave Database

- Oracle: Oracle 9i or higher
- MariaDB: MariaDB 5.5.x or higher

### 2.5 Properties

### 2.6 Error Messages

<br>

# 3. Open Source Libraries Used

dataCompJ is based on the following open-source libraries. The licenses are distributed in a text file format
along with dataCompJ.

| Library             | Open Source License                                          |
| ------------------- | ------------------------------------------------------------ |
| Apache Commons CLI  | http://commons.apache.org/proper/commons-cli/<br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Apache Commons Lang | http://commons.apache.org/proper/commons-lang/ <br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Apache Commons IO   | http://commons.apache.org/proper/commons-io/ <br>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| JDOM                | http://www.jdom.org/ <br/>License: Apache-style Open Source License (http://www.jdom.org/docs/faq.html#a0030) |
| Log4j               | http://logging.apache.org/index.html <br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Oracle JDBC Driver  | http://www.oracle.com <br>License: Oracle Free Use Terms and Conditions (https://www.oracle.com/downloads/licenses/oracle-free-license.html) |

<br>

# 4. Packages

| Archive Name                             |
| ---------------------------------------- |
| dataCompJ7.2.zip<br/>dataCompJ7.2.tar.gz |

<br>

# 5. Downloads

### 5.1 Packages

http://support.altibase.com/kr/product
<!-- SOURCE_BLOCK_END source_id="SRC-000449" block_id="BLOCK-000936" -->

## SRC-000471 - Release 7.2 (Feb. 17, 2022)

| Field | Value |
| --- | --- |
| `source_id` | SRC-000471 |
| `source_path` | ReleaseNotes/kor/Altibase_dataCompJ_7_2_Release_Notes.md |
| `source_family` | utilities_datacompj |
| `version_scope` | dataCompJ 7.2 |
| `language` | ko |
| `authority_label` | Korean authoritative |
| `source_sha256` | 8b7146563c00fe4efbcaf22b3114d30fd8a916ad59fa6088809506806fdfae8a |
| `byte_count` | 5577 |
| `line_count` | 213 |
| `estimated_tokens` | 996 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000471" source_path="ReleaseNotes/kor/Altibase_dataCompJ_7_2_Release_Notes.md" source_family="utilities_datacompj" version_scope="dataCompJ 7.2" language="ko" authority_label="Korean authoritative" sha256="8b7146563c00fe4efbcaf22b3114d30fd8a916ad59fa6088809506806fdfae8a" byte_count="5577" line_count="213" estimated_tokens="996" block_id="BLOCK-000937" -->
dataCompJ Release Notes
================

#### Release 7.2 (Feb. 17, 2022)

Altibase® Tools & Utilities

<br><br><br><br><br><br>
<!-- PDF 변환을 위한 여백입니다. --> 





































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 









































<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Release Notes dataCompJ
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>



<br>

# 목차

- [1. 개요](#1-개요)
  - [1.1 하드웨어 요구사항](#11-하드웨어-요구사항)
  - [1.2 지원하는 OS 및 플랫폼](#12-지원하는-os-및-플랫폼)
- [2. 릴리즈 정보](#2-릴리즈-정보)
  - [2.1 버전](#21-버전)
  - [2.2 새로운 기능](#22-새로운-기능)
  - [2.3 수정된 버그](#23-수정된-버그)
  - [2.4 데이터베이스 호환성](#24-데이터베이스-호환성)
  - [2.5 프로퍼티](#25-프로퍼티)
  - [2.6 에러 메시지](#26-에러-메시지)
- [3. 사용된 오픈소스 라이브러리](#3-사용된-오픈소스-라이브러리)
- [4. 패키지](#4-패키지)
- [5. 다운로드](#5-다운로드)
  - [5.1 패키지](#51-패키지)

<br>

# 1. 개요

dataCompJ는 Altibase에서 이기종 데이터베이스로 복제한 데이터를 대상으로 데이터 정합성 확인과 데이터 불일치를 해소하기 위한 도구이다. 테이블 단위로 데이터를 비교하고 데이터 불일치가 있는 경우 이에 관한 정보를 파일로 출력한다. 불일치 데이터를 Slave 데이터베이스에 직접 적용하여 데이터를 일치시키는 기능도 제공한다.<br>
dataCompJ가 관리하는 데이터는 데이터 복제 도구로 Altibase에서 제공하는 Adapter for Oracle 또는 Adapter for JDBC를 사용하여 복제한 데이터를 전제로 한다. <br>
dataCompJ는 편리한 사용성과 빠른 성능으로, 효율적인 이기종 데이터베이스 간 데이터 관리 방법을 제공한다.

### 1.1 하드웨어 요구사항

- 메인 메모리: 최소 512MB, 4GB 이상 권장
- 디스크: 최소 500MB 이상의 여유 공간 필요

### 1.2 지원하는 OS 및 플랫폼

| Mode | JRE                                                      |
| ---- | -------------------------------------------------------- |
| CLI  | Oracle, OpenJDK 또는 IBM Java Runtime Environment 8 이상 |

dataCompJ는 순수 Java 기반 클라이언트 애플리케이션으로, 하드웨어나 OS보다 JAVA Runtime Environment (JRE)에 의존한다.

<br>

# 2. 릴리즈 정보

### 2.1 버전

- 7.2

### 2.2 새로운 기능

### 2.3 수정된 버그

| 버그 번호 | 제목                                                         |
| --------- | ------------------------------------------------------------ |
| BUG-45222 | 따옴표로 묶인 사용자 입력 개체 이름을 처리해야 한다.         |
| BUG-46675 | 미지원 DB JDBC URL에 대한 에러메시지를 더욱 명확하게 제공해야 한다. |
| BUG-46689 | JDBC URL 문자열을 이용한 DB 타입 검사 루틴을 수정해야 한다.  |
| BUG-49501 | dataCompJ log4j 보안 문제로 2.17.1 버전으로 업그레이드 한다. |

### 2.4 데이터베이스 호환성

#### Master 데이터베이스

- Altibase: Altibase 5.3.3 이상

#### Slave 데이터베이스

- Oracle: Oracle 9i 이상
- MariaDB: MariaDB 5.5.x 이상

### 2.5 프로퍼티

### 2.6 에러 메시지

<br>

# 3. 사용된 오픈소스 라이브러리

dataCompJ는 아래의 오픈소스 라이브러리에 기반한다. 라이선스는 텍스트 파일 형식으로 dataCompJ와 함께 제공된다.

| 라이브러리          | 오픈소스 라이선스                                            |
| ------------------- | ------------------------------------------------------------ |
| Apache Commons CLI  | http://commons.apache.org/proper/commons-cli/<br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Apache Commons Lang | http://commons.apache.org/proper/commons-lang/ <br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Apache Commons IO   | http://commons.apache.org/proper/commons-io/ <br>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| JDOM                | http://www.jdom.org/ <br/>License: Apache-style Open Source License (http://www.jdom.org/docs/faq.html#a0030) |
| Log4j               | http://logging.apache.org/index.html <br/>License: Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0.txt) |
| Oracle JDBC Driver  | http://www.oracle.com <br>License: Oracle Free Use Terms and Conditions (https://www.oracle.com/downloads/licenses/oracle-free-license.html) |

<br>

# 4. 패키지

2가지 종류의 압축 파일을 제공한다. 
- dataCompJ7.2.zip
- dataCompJ7.2.tar.gz 

<br>

# 5. 다운로드

### 5.1 패키지

http://support.altibase.com/kr/product
<!-- SOURCE_BLOCK_END source_id="SRC-000471" block_id="BLOCK-000937" -->

## SRC-000201 - Release 7.1

| Field | Value |
| --- | --- |
| `source_id` | SRC-000201 |
| `source_path` | Manuals/Tools/Altibase_release/eng/Altibase Heartbeat User's Guide.md |
| `source_family` | utilities_datacompj |
| `version_scope` | multi |
| `language` | en |
| `authority_label` | English extraction aid |
| `source_sha256` | a405854c16bd862249a6c17f414bd283c93ae296101c8393621ba1f0e367c79c |
| `byte_count` | 28332 |
| `line_count` | 692 |
| `estimated_tokens` | 7048 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000201" source_path="Manuals/Tools/Altibase_release/eng/Altibase Heartbeat User&#x27;s Guide.md" source_family="utilities_datacompj" version_scope="multi" language="en" authority_label="English extraction aid" sha256="a405854c16bd862249a6c17f414bd283c93ae296101c8393621ba1f0e367c79c" byte_count="28332" line_count="692" estimated_tokens="7048" block_id="BLOCK-000938" -->
Altibase Heartbeat User's Guide
================

#### Release 7.1

Altibase® Tool & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>


<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. -->  

<pre>
Altibase Tool & Utilities Altibase HeartBeat User's Guide
Release 7.1
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the
software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>

<br>

# Table Of Contents

- [Preface](#preface)
  - [About This Manual](#about-this-manual)
- [1. Introduction to Altibase Heartbeat](#1-introduction-to-altibase-heartbeat)
  - [Overview of Altibase Heartbeat](#overview-of-altibase-heartbeat)
  - [Altibase Heartbeat Procedure](#altibase-heartbeat-procedure)
- [2. Commands](#2-commands)
  - [aheartbeat](#aheartbeat)
- [3. Configuring Altibase Heartbeat](#3-configuring-altibase-heartbeat)
  - [Configuration](#configuration)
  - [Configuring an Altibase Heartbeat System : A Practice Example](#configuring-an-altibase-heartbeat-system--a-practice-example)
- [4. Altibase Heartbeat Process](#4-altibase-heartbeat-process)
  - [aheartbeat Status](#aheartbeat-status)
  - [Determing Failure](#determing-failure)
  - [Role of aheartbeat 0](#role-of-aheartbeat-0)
  - [Failover and Failback](#failover-and-failback)
  - [Logging](#logging)

<br>

Preface
====

### About This Manual

This guide describes how to use the Altibase Heartbeat utility in a distributed database environment.

#### Audience

This manual has been prepared for the following Altibase users:

-   Database administrators
-   Performance administrators
-   Database users
-   Application developers
-   Technical Supporters

It is recommended for those reading this manual possess the following background knowledge:

-   Basic knowledge in the use of computers, operating systems, and operating system utilities
-   Experience in using relational database and an understanding of database concepts
-   Computer programming experience
-   Experience in database server management, operating system management, or network administration

#### Organization

The manual is organized as follows:

-   Chapter 1: Introduction to Altibase heartbeat  
    This chapter introduces Altibase Heartbeat and describes its basic procedure.

-   Chapter 2: Commands  
    This chapter explains Altibase Heartbeat commands

-   Chapter 3: Configuring Altibase Heartbeat  
    This chapter describes how to configure Altibase Heartbeat, and how to configure a distributed database environment with Altibase Heartbeats.
    
-   Chapter 4: Altibase Heartbeat Process  
    This chapter explains the Altibase Heartbeat process in details. On which criteria Altibase Heartbeat determines failure, and once failure is detected, how Failover is performed are examined.

#### Documentation Convention

This section describes the convention used in this manual. Understanding this convention will make it easier to find information in this manual and in the other manuals in the series. 

This convention described here is as follow: 

- Sample Code Convention

##### Sample Code Conventions

The code examples explain SQL statements, stored procedures, iSQL statements, and other command line syntax.

The following table describes the printing conventions used in the code examples.

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL\> SELECT ename FROM employee;<br/> ENAME<br/>  -----------------------<br/> SWNO<br/>  HJNO<br/>  HSCHOI<br/>  .<br/> .<br/> .<br/> 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code. | EXEC :p1 := 1; acc NUMBER(11,2)                              |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT \* FROM *table_name*; <br/>CONNECT *userID*/*password*; |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### Related Documentations

For more detailed information, please refer to the following documents.

-   Getting Started Guide

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   Stored Procedures Manual

-   Error Message Reference

#### Altibase Welcomes Your Comments and Feedbacks

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there is any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](http://support.altibase.com/en/).

Thank you. We always welcome your feedbacks and suggestions.

<br>

# 1. Introduction to Altibase Heartbeat

This chapter introduces the Altibase Heartbeat and describes its basic procedure.

### Overview of Altibase Heartbeat

The Altibase Heartbeat utility detects node failures in a distributed database environment and enables the DBA to counter failures. aheartbeat[^1]  can be utilized in an environment where Altibase servers are connected through replication. 

[^1]: aheartbeat has detected failure on the other node, this file is executed for remote node Failover. This file can be either an executable binary or script file.


Therefore, Altibase Heardbeat and aheartbeat are used interchageably in this document. 

#### Altibase Heartbeat Components

Altibase Heartbeat mainly consists of the following:

-   aheartbeat process

-   Execution file to perform Failover to the local node

-   Execution file for remote node Failover

##### aheartbeat Process

aheartbeat is a background process and detects two types of failures; it either detects database failure by periodically connecting to the Altibase server on the same node, or detects network failure by periodically connecting to aheartbeats on other nodes.

##### Execution File to Perform Failover to the Local Node

After database server failure on the same node as aheartbeat has been detected, this file is executed to perform Failover to the local node. This file can be either an executable binary or script file.

##### Execution File to Perform Failover to the Local Node

After aheartbeat has detected failure on the other node, this file is executed for remote node Failover. This file can be either an executable binary or script file.

### Altibase Heartbeat Procedure

This section explains the basic Altibase Heartbeat procedure in a distributed database environment. The following figure is a diagram of a simple distributed database environment consisting of multiple Altibase databases with Altibase Heartbeats.

![heartbeat](media/Heartbeat/heartbeat.gif)

[Figure 1-1] Altibase Heartbeat Procedure

As shown above, aheartbeat detects database failure by monitoring the Altibase server process of the node it resides on(1. check in the figure). It also detects node failure(3. check) or external network failure(2. check) by monitoring aheartbeat processes on other nodes. 

If the Altibase server on Node A fails, let's look at how aheartbeats will run:

1.  Node A’s aheartbeat detects an Altibase server failure.

2.  Node A’s aheartbeat executes the execution file to perform Failover to the local node and terminates itself.
  
3.  By detecting the termination of Node A’s aheartbeat, Node B’s aheartbeat registers an Altibase server failure on Node A and executes the execution file for remote node Failover. 

<br>

# 2. Commands

This chapter explains Altibase Heartbeat commands.

### aheartbeat

aheartbeat is used to start up or terminate Altibase Heartbeat, or retrieve information about nodes. 

#### Syntax

```
aheartbeat {-r|-s|-i}
```

#### Options

| Option        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| \-r or --run  | Starts aheartbeat                                            |
| \-s or --stop | Terminates aheartbeat                                        |
| \-i or --info | Outputs information on all nodes consisting the distributed environment in which aheartbeats are running |

#### Example

Starts Altibase Heartbeat.

```
$ aheartbeat -r
```

Terminates Altibase Heartbeat.

```
$ aheartbeat -s
```

Outputs information on all nodes consisting the distributed environment in which aheartbeats are running,

```
$ aheartbeat -i
#ID     IP                 PORT      STATUS
0      192.168.1.31        55778     RUN
0      172.168.221.32      55778     RUN
1      192.168.2.33        55444     RUN
1      168.768.1.1         55444     READY
2      192.168.2.33        54321     ERROR
2      ::2:1               54321     RUN
```

<br>

# 3. Configuring Altibase Heartbeat

This chapter explains how to configure Altibase Heartbeat, and how to configure a distributed database environment with Altibase Heartbeats.

### Configuration

This section explains the necessary configuration for using Altibase Heartbeats in a distributed database environment.

#### Environment Variables

##### Mandatory Environment Variables

The following environment variables must be set to use Altibase Heartbeats:

- ALTI_HBP_HOME  
  Sets the Altibase Heartbeat home directory. And sets the ALTI_HBP_HOME/bin on the environment variables PATH as follows.

```
export PATH=$ALTI_HBP_HOME/bin:$PATH : PATH
```


-   ALTI_HBP_ID  
    Sets an ID to identify the node on which Altibase Heartbeats reside. The value must be an integer between 1 and 99, and each node must have a unique ID. Since the ID 0 indicates that aheartbeat exists in an external network, an internal network node cannot take 0 as its ID. 
    
-   ALTI_HBP_ALTIBASE_PORT_NO  
    Sets Altibase server’s listening port number which the Altibase Heartbeat is to monitor; this is the listening port number of the Altibase server that exists on the same node as the aheartbeat. 
    
-   ALTI_HBP_DETECT_INTERVAL  
    Sets the interval (in seconds) after which the Altibase Heartbeat monitors Altibase server failure. 
    
-   ALTI_HBP_DETECT_HIGHWATER_MARK  
    Sets the number of failed connections to tolerate before determining a failure when the aheartbeat receives no response from the Altibase server it is monitoring or aheartbeats on other nodes. 

##### Optional Environment Variables

If necessary, the following environment variables can be set additionally.

-   ALTI_HBP_ALTIBASE_FAILURE_EVENT  
    The name of an executable script or binary file which the Altibase Heartbeat executes when it detects an Altibase server failure on the same node. On omission, $ALTI_HBP_HOME/bin/altibaseFailureEvent.sh is executed by default.
    
-   ALTI_HBP_REMOTE_NODE_FAILURE_EVENT  
    The name of an executable script or binary file which the Altibase Heartbeat executes when it detects an Altibase server failure on another node. On omission, $ALTI_HBP_HOME/bin/remoteNodeFailureEvent.sh is executed by default. 

#### Setting aheartbeat Nodes

The purpose of the aheartbeat.settings file is to configure a distributed environment which uses Altibase Heartbeats. This file stores information on all nodes consisting the distributed environment, and exists in the $ALTI_HBP_HOME/conf directory. To execute Altibase Heartbeat, it is imperative that this file exists. 

The information stored in the aheartbeat.settings file consists of the ID, IP address and aheartbeat‘s listening port number on each node. This information is necessary for aheartbeats to connect to aheartbeats on other nodes. 

If one server has many IP addresses, you can specify up to four sets of different IP addresses for the same ID. Also, IPs of different versions can be set for the same ID.

\<An example of the aheartbeat.settings file>

```
# ID   IP                  PORT
0      169.215.114.23    55778     # public domain
0      222.112.231.234   55778     # public domain
1      192.168.2.33       55444
1      222.112.181.231   55444     # public domain
2      192.168.2.33       54321
2      ::ffff:c0a8:221   54321     # IPv6
```

In the above example, Node 0 has two IP addresses (169.215.114.23, 222.112.231.234) and aheartbeat’s listening port number is 55778. Node 1 has two IP addresses (192.168.2.33, 222.112.181.231) and aheartbeat’s listening port number is 55444. 

Two IP addresses of different versions are set to the same ID for Node 2 (IPv4: 192.168.2.33, IPv6: ::ffff:c0a8:221) and aheartbeat’s listening port number is 55321. Comments can be left with a #.

##### Note

The settings in the aheartbeat.settings file must be identical for all of the nodes comprising a distributed environment. Otherwise, Altibase Heartbeat can malfunction.

#### Failover Execution File

When aheartbeat fails to connect to an Altibase server on its node or aheartbeats on other nodes (or simply put, detects a failure), it executes the failover execution file. The failover execution file must be in the $ALTI_HBT_HOME/bin directory and the file name can be set with the ALTI_HBP_ALTIBASE_FAILURE_EVENT, ALTI_HBP_REMOTE_NODE_FAILURE_EVENT environment variables described above.

The default script file for failover is as follows.

-   altibaseFailureEvent.sh  
    This script file is executed when Altibase Heartbeat detects an Altibase server failure on the same node. Tasks, such as notifying DBAs of failures or restarting the failed Altibase server, can be included.
    
-   remoteNodeFailureEvent.sh  
    This script file is executed when Altibase Heartbeat detects a failure on another node. Tasks, such as performing Failover to the services of a failed database, can be included.

Database administrators can override failure by modifying the default script file or writing application programs which execute Failover operations.

#### aheartbeat 0

In a system where databases in an internal network provide services to clients in an external network, aheartbeat can exist in the external network to detect network failure from the internal to external network. The ID of a node which has aheartbeat in the external network must be 0. Therefore, aheartbeat in the external network is called aheartbeat 0.

The user can decide whether or not to add aheartbeat 0.

### Configuring an Altibase Heartbeat System : A Practice Example

A practice example is provided in this section to show how to configure a distributed environment with Altibase databases and the Altibase Heartbeat utility.

It is possible to provide enforced and continuous database services by incorporating the Altibase Heartbeat utility in a distributed environment consisted of Altibase databases.

#### Distributed Environment Diagram and Conditions 

Three nodes(A, B, C) exist in the internal network and each node has an Altibase server and aheartbeat.

![heartbeat_sample](media/Heartbeat/heartbeat_sample.gif)

[Figure 3-1] Distributed Environment Diagram and Conditions

-   Each node’s Altibase database has a client requesting services.

-   aheartbeat 0 runs in a public network with the IP address 169.215.114.23, and the listening port number 44000.
  
-   Each node’s IP address, aheartbeat and Altibase server’s listening port number are as follows.

| Node | IP Address     | Altibase Server Listerning Port Number | aheartbeat Listening Port Number |
| ---- | -------------- | -------------------------------------- | -------------------------------- |
| A    | 192.168.100.30 | 20000                                  | 21000                            |
| B    | 192.168.100.31 | 30000                                  | 31000                            |
| C    | 192.168.100.32 | 40000                                  | 41000                            |

#### Setting Environment Variables 

Under the above conditions, the environment variables for each node can be set as follows.

- aheartbeat 0’s Node (external network):

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=0

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node A:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=1

  ALTI_HBP_ALTIBASE_PORT_NO=20000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node B:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=2

  ALTI_HBP_ALTIBASE_PORT_NO=30000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- Node C:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=3

  ALTI_HBP_ALTIBASE_PORT_NO=40000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

> Note: the ALTI_HBP_ALTIBASE_PORT_NO environment variable is ignored in the 0 Node.
>

#### aheartbeat.settings

The contents of the $ALTI_HBP_HOME/conf/aheartbeat.settings file are identical over all nodes and are as follows.

\# ID     IP PORT

0      169.215.114.23        44000    #External Network

1      192.168.100.30        21000    #NODE A

2      192.168.100.31        31000    #NODE B

3      192.168.100.32        41000    #NODE C

####  Failover Execution File

Make the necessary changes to the contents of the altibaseFailureEvent.sh and remoteNodeFailureEvent.sh files in the \$ALTI_HBP_HOME/bin directory. You can also write an application program for Failover, put the execution binary into the $ALTI_HBP_HOME/bin directory and then set the environment variables.

#### Starting aheartbeat 

Start Altibase Heartbeat on each node with the following command.

```
$ aheartbeat -r
```

The startup order of the nodes is irrelevant. Once aheartbeats are running, the status of each node can be checked with the following command.

```
$ aheartbeat -i
```

<br>

# 4. Altibase Heartbeat Process

This chapter explains the Altibase Heartbeat process in details. On which criteria Altibase Heartbeat determines failure, and once failure is detected, how Failover is performed are examined.

### aheartbeat Status

aheartbeat defines the status of itself and other aheartbeats.

aheartbeat is in one of the following three statuses, depending on its execution state.

-   Ready: aheartbeat is not yet running

-   Run: aheartbeat has been executed and is in the state of running normally.

-   Error: The node is in a state of failure

aHeartbeat also defines aheartbeats on other nodes to be in one of the following three statuses.

-   Ready: aheartbeat has not yet performed an initial handshake with the corresponding node’s aheartbeat. 
-   Run: aheartbeat has successfully performed a handshake with the corresponding node’s aheartbeat and is in the state of being connected normally. 
-   Error: aheartbeat cannot connect to the corresponding node’s aheartbeat whose status was previously detected to be 'Run'.

The following figure shows how status transition occurs and the table lists the situations under which each status transition occurs.

![heartbeat_transition](media/Heartbeat/heartbeat_transition.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-07061" source_md="Manuals/Tools/Altibase_release/eng/Altibase Heartbeat User&#x27;s Guide.md" line_no="557" image_path_raw="media/Heartbeat/heartbeat_transition.gif" image_class="E" format="mermaid" verified="True" -->
```mermaid
flowchart LR
    Ready([Ready])
    Run([Run])
    Error([Error])
    Ready -->|"(1)"| Run
    Run -->|"(2)"| Error
    Error -->|"(3)"| Run
    Run -->|"(4)"| Ready
```
<!-- IMG_RECOVERY_END ref_id="img-07061" -->


[Figure 4-1] Status Transition

Each status transition occurs in the following table.

| Status Transition | Description                                                  |
| ----------------- | ------------------------------------------------------------ |
| (1)               | After starting up, aheartbeat has successfully performed a handshake |
| (2)               | aheartbeat has terminated due to failure                     |
| (3)               | After failure, aheartbeat has restarted and successfully re-performed a handshake |
| (4)               | aheartbeat has terminated normally                           |

[Table 4-1] Status Transition

### Determing Failure

This section examines the criteria on which Altibase Heartbeat determines failure.

Altibase Heartbeat monitors in the following order and detects failure by connecting to three objects. The table below depicts the node (local or remote) which aheartbeat registers to have failed for each monitoring target object when connection fails.

| Order | Monitoring Target                          | Registered Node Failure |
| ----- | ------------------------------------------ | ----------------------- |
| 1     | aheartbeat 0                               | Local node failure      |
| 2     | Altibase database server on the local node | Local node failure      |
| 3     | aheartbeat on the remote server            | Remote node failure     |

[Table 4-2] Determing Failure

#### Local Node Failure

When aheartbeats of each node detect failure at #1 or #2 in the above table, they register a local node failure.

aheartbeats of each node initially monitor aheartbeat 0 which resides in the external public network; when connection fails, they register a local node failure. In this case, aheartbeat determines that database services cannot be provided due to network failure between the Altibase server and clients.

If connection to aheartbeat 0 is normal or aheartbeat 0 is nonexistent, aheartbeats of each node monitor the Altibase database server on the local node; when connection fails, they register a database failure. In this case, aheartbeat determines that database services cannot be provided due to database failure. 

If aheartbeat acknowledges that a failure has occurred in the above two monitoring targets, it executes the execution file to perform Failover to the local node and terminates itself.

#### Remote Node Failure

If aheartbeats of each node detect failure at #3 in the above table, they register a remote node failure. That is, when connection to another node’s aheartbeat which has been identified to be in the RUN status fails, they determine that the node has failed and execute the execution file for remote node Failover.

> Note: When a local node fails, the aheartbeat of the node shuts itself down, so the aheartbeats of other nodes cannot access the aheartbeats of the node. Therefore, it is determined that a failure has occurred in the Altibase server of the remote node.
> 

### Role of aheartbeat 0

aheartbeat 0’s role and features in a distributed database environment are as follows.

-   aheartbeat 0 does not monitor the Altibase server on its node.

-   aheartbeats on nodes other than aheartbeat 0, can verify disconnection with the external network by connecting to aheartbeat 0. Disconnection with the external network indicates disconnection with the clients.

How failure detection results differ in relation to whether or not aheartbeat 0 exists in a distributed database environment is explained below.

#### When aheartbeat 0 is Nonexistent

Let’s suppose the network has failed in a distributed database environment where aheartbeats reside in the internal network.

![heartbeat_fail_0_noexistence](media/Heartbeat/heartbeat_fail_0_noexistence.gif)

[Figure 4-2] Network Failure Between an Internal and External Network

If a network failure occurs between Node A and the external network as shown above, Node A’s aheartbeat is not capable of providing services to the client. However, it overlooks the network failure and continues to run. By doing so, Node B’s aheartbeat also overlooks the failure that has occurred on Node A and does not perform Failover to Node A.

#### When aheartbeat 0 is Existent

Next, let’s suppose the network has failed in a distributed database environment where aheartbeat resides in the external network.

![heartbeat_fail_0_existence](media/Heartbeat/heartbeat_fail_0_existence.gif)

[Figure 4-2] Network Failure Between an Internal and External Network

If a network failure occurs between Node A and the external network as shown above, it is impossible for Node A’s aheartbeat to connect to aheartbeat 0. Therefore, Node A’s aheartbeat registers a local node failure, terminates itself and by doing so, allows other nodes to detect its failure. Since Node B’s aheartbeat can’t connect Node A’s aheartbeat, it executes the remote node failover execution file to perform Failover to Node A. 

As seen in the examples above, since aheartbeat 0 can detect network failure between the internal and external networks, the provision of continuous database services can be enforced by using aheartbeat 0.

### Failover and Failback

#### Failover

When aheartbeat detects a failure, it executes the failover execution file with the following two arguments to enable the DBA to efficiently perform Failover.

| Argument        | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| First Argument  | The number of failed nodes                                   |
| Second Argument | The IDs of the failed nodes. These are differentiated by blaks and are specified in ascending order. |

For example, let’s assume that there is a distributed environment where five nodes with the respective IDs 1, 2, 3, 4, 5, which each have Altibase servers and aheartbeats running, and that the Altibase server has failed on the node with the ID 3. Once aheartbeat on the node ID 3 detects that its Altibase server has failed, it executes the following local node failover script and terminates itself.

```
altibaseFailureEvent.sh 1 3
```

Once aheartbeats of other nodes detect that aheartbeat of the node ID 3 has terminated, they execute the following remote node failover script.

```
remoteNodeFailureEvent.sh 1 3
```

If the Altibase server on the node ID 1 fails while Node ID 3 is down, the failover script is executed with the following arguments.

```
altibaseFailureEvent.sh 2 1 3
remoteNodeFailureEvent.sh 2 1 3
```

This means that two servers have failed and their IDs are 1 and 3.

#### Failback

Failback after a node has recovered from failure must be manually performed by the user.

### Logging

Altibase Heartbeat writes the following information to the log file while it is processing.

-   Information of aheartbeat startup

-   Information of connection failure of the Altibase Server

-   Information of the start of an connection to another node

-   Information of aheartbeat failure situation of Altibase server and other nodes

-   Information of each node's aheartbeat status transition

Log files are fixed to $ALTI_HBP_HOME/log/aheartbeat.log.

The output format of log information is as follows.

```
[YYYY-MM-DD HH:MM:SS T-<threadID>] Log Body
```

<!-- SOURCE_BLOCK_END source_id="SRC-000201" block_id="BLOCK-000938" -->

## SRC-000206 - Release 7.2

| Field | Value |
| --- | --- |
| `source_id` | SRC-000206 |
| `source_path` | Manuals/Tools/Altibase_release/eng/dataCompJ User's Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | multi |
| `language` | en |
| `authority_label` | English extraction aid |
| `source_sha256` | 1ebf9ef932f1e37c09cc4929ec5e60aefed3c8af6030b2cfcc173f0fbc5b9fb0 |
| `byte_count` | 49859 |
| `line_count` | 1163 |
| `estimated_tokens` | 12442 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000206" source_path="Manuals/Tools/Altibase_release/eng/dataCompJ User&#x27;s Manual.md" source_family="utilities_datacompj" version_scope="multi" language="en" authority_label="English extraction aid" sha256="1ebf9ef932f1e37c09cc4929ec5e60aefed3c8af6030b2cfcc173f0fbc5b9fb0" byte_count="49859" line_count="1163" estimated_tokens="12442" block_id="BLOCK-000939" -->
dataCompJ User's Manual
================

#### Release 7.2

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>


<br><br><!-- PDF 변환을 위한 여백입니다. --> 





























<!-- PDF 변환을 위한 여백입니다. --> 

<pre>
Altibase Tools & Utilities dataCompJ User's Manual
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
This manual contains proprietary information of Altibase® Corporation; it is provided under a license agreement containing restrictions on use and disclosure and is also protected by copyright patent and other intellectual property law. Reverse engineering of the
software is prohibited.<br>
All trademarks, registered or otherwise, are the property of their respective owners.<br>
<b>Altibase Corp</b>
10F, Daerung PostTower II,
306, Digital-ro, Guro-gu, Seoul 08378, Korea
Telephone : +82-2-2082-1000 
Fax       : +82-2-2082-1099
Customer Service Portal : <a href='http://support.altibase.com/en/'>http://support.altibase.com/en/</a>
Homepage                : <a href='http://www.altibase.com'>http://www.altibase.com</a></pre>

<br>

# Table Of Contents

- [Preface](#preface)

- [1. Introducing dataCompJ](#1-introducing-datacompj)
  - [Overview](#overview)
  - [System Requirements](#system-requirements)
- [2. Getting Started](#2-getting-started)
  - [Terms for dataCompJ](#terms-for-datacompj)
  - [Inconsistent Records and Synchronization Policy](#inconsistent-records-and-synchronization-policy)
  - [Synchronization Policy](#synchronization-policy)
- [3. How to Use dataCompJ](#3-how-to-use-datacompj)
  - [How to run dataCompJ](#how-to-run-datacompj)
  - [Executing dataCompJ](#executing-datacompj)
  - [Configuration File Setup](#configuration-file-setup)
- [4. Functions](#4-functions)
  - [Comparison (DIFF) Function](#comparison-diff-function)
  - [Synchronization(SYNC) Function](#synchronizationsync-function)
- [Appendix A: Data Type compatibility table between Other Databases](#appendix-a-data-type-compatibility-table-between-other-databases)

<br>

Preface
====

This manual describes the ability of dataCompJ to compare and match the discrepant data efficiently and how to use it.

#### Audience

This manual has been prepared for the following Altibase users:

- Database administrators
- Performance administrators
- Database users
- Application developers
- Technical Supporters

It is recommended for those reading this manual possess the following background knowledge:

- Basic knowledge in the use of computers, operating systems, and operating system utilities
- Experience in using relational database and an understanding of database concepts
- Computer programming experience
- Experience in database server management, operating system management, or network administration

#### Organization

This manual is organized as follows:

- Chapter 1: Introducing dataCompJ  
  This chapter introduces dataCompJ and explains how to install it.

- Chapter 2: Getting Started  
  This chapter describes the key concepts that helps running dataCompJ more effectively.

- Chapter 3: How to use dataCompJ  
  This chapter provides a step by step guide to operate dataCompJ and set up the configuration file.

- Chapter 4: Functions

  This chapter explains DIFF function and SYNC function in detail.

- Appendix A: Data Type compatibility table between Other Databases

#### Documentation Conventions

This section describes the conventions used in this manual. Understanding these conventions will make it easier to find information in this manual and in the other manuals in the series. 

There are two sets of conventions:

- Syntax diagram convetions
- Sample code conventions

##### Syntax Diagram Conventions

This manual describes command syntax using diagrams composed of the following elements:

| Elements                              | Meaning                                                      |
| ------------------------------------- | ------------------------------------------------------------ |
| ![image1](media/dataCompJ/image1.gif) | Indicates the start of a command. If a syntactic element starts with an arrow, it is not a complete command. |
| ![image2](media/dataCompJ/image2.gif) | Indicates that the command continues to the next line. If a syntactic element ends with this symbol, it is not a complete command. |
| ![image3](media/dataCompJ/image3.gif) | Indicates taht the command continues from the previous line. If a syntactic element starts witht his symbol, it is not a complete command. |
| ![image4](media/dataCompJ/image4.gif) | Indicates the end of a statement.                            |
| ![image5](media/dataCompJ/image5.gif) | Indicates a manatory element.                                |
| ![image6](media/dataCompJ/image6.gif) | Indicates an optional element.                               |
| ![image7](media/dataCompJ/image7.gif) | Indicates a mandatory element comprised of options. One, and only one, option must be specified. |
| ![image8](media/dataCompJ/image8.gif) | Indicates an optional element comprised of options.          |
| ![image9](media/dataCompJ/image9.gif) | Indicates an optional element in which multiple elements may be specified. A comman must precede all but the first element. |

##### Sample Code Conventions

The code examples explain SQL statements, stored procedures, iSQL statements, and other command line syntax.

The following table describes the printing conventions used in the code examples.

| Rules            | Meaning                                                      | Example                                                      |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]              | Indicates an optional item                                   | VARCHAR [(*size*)][[FIXED \|] VARIABLE]                      |
| { }              | Indicates a mandatory field for which one or more items must be selected. | { ENABLE \| DISABLE \| COMPILE }                             |
| \|               | A delimiter between optional or mandatory arguments.         | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ] |
| . . .            | Indicates that the previous argument is repeated, or that sample code has been omitted. | SQL> SELECT ename FROM employee; ENAME ----------------------- SWNO HJNO HSCHOI . . . 20 rows selected. |
| Other Symbols    | Symbols other than those shown above are part of the actual code.Other Symbols | EXEC :p1 := 1; acc NUMBER(11,2);Symbols other than those shown above are part of the actual code. |
| Italics          | Statement elements in italics indicate variables and special values specified by the user. | SELECT * FROM *table_name*; CONNECT *userID*/*password*;     |
| Lower case words | Indicate program elements set by the user, such as table names, column names, file names, etc. | SELECT ename FROM employee;                                  |
| Upper case words | Keywords and all elements provided by the system appear in upper case. | DESC SYSTEM_.SYS_INDICES_;                                   |

#### Related Documentations

For more detailed information, please refer to the following documents.

- Installation Guide

- Getting Started Guide

- Administrator’s Manual

- Replication Manual

- Precompiler User’s Manual

- API User’s Manual

- Altibase C Interface Manual

- iSQL User’s Manual

- Utilities Manual

- General Reference

- Error Message Reference

#### Altibase Welcomes Your Comments and Feedbacks

Please let us know what you like or dislike about our manuals. To help us with better future versions of our manuals, please tell us if there is any corrections or classifications that you would find useful.

Include the following information:

- The name and version of the manual that you are using
- Any comments about the manual
- Your name, address, and phone number

If you need immediate assistance regarding any errors, omissions, and other technical issues, please contact [Altibase's Support Portal](#http://altibase.com/support-center/en/).

Thank you. We always welcome your feedbacks and suggestions.

<br>

# 1. Introducing dataCompJ

This chapter introduces dataCompJ and explains how to install it. This chapter consists of the following sections:

- Overview

- System Requirements

- Installation and Uninstallation

### Overview

Altibase dataCompJ is a utility designed to guarantee data consistency between two heterogeneous databases and resolve data inconsistency if any. dataCompJ compares Altibase with another heterogeneous database on a table-by-table basis, and outputs information on any inconsistency it detects. Also, it offers an efficient feature for synchronizing two databases by applying the inconsistent data to slave database in the event of data inconsistency.

Data managed by dataCompJ are replicated by Adapter for Oracle or Adapter for JDBC provided by Altibase.

A proper use of Altibase dataCompJ would be a cornerstone of effective data management with advantageous usability along with its advanced technical performance.

### System Requirements

This section discusses the system requirements for dataCompJ and compatible database management systems.

#### Hardware Requirements

- CPU: Pentium III 800MHz or better
- Main memory: Minimum 512MB,  4GB or more recommended
- Disk: 50MB or more free space

#### Software Requirements

- Oracle, OpenJDK or IBM Java Runtime Environment 8 or higher

dataCompJ is a pure Java-based client application relying on the JAVA Runtime Environment (JRE) instead of the client's hardware or an operating system.

#### Compatible Database Systems

##### Master DB

- Altibase: Altibase 5.3.3 or later

##### Slave DB

- Oracle: Oracle 9i or later
- MariaDB: MariaDB 5.5.x or later

Refer to [Terms for dataCompJ](#terms-for-datacompj) section for more detailed definitions of Master/Slave DB.

dataCompJ can be used with Altibase and various other databases. Since this tool uses JDBC driver to connect to database, the JDBC driver compatible with original and target database is required. Currently JDBC driver for Oracle, ojdbc5.jar, is provided along with dataCompJ for your convenience.

#### Intallation and Uninstallation

dataCompJ can be downloaded from the official [Altibase Customer Support portal](#http://altibase.com/support-center/en/). It is provided as a zip or tar.gz file in the name of dataCompJCli which includes executable files and JDBC drivers.

dataCompJ is installed once dataCompJCli is decompressed. Subdirectory of JDBC including dataCompJCli.sh and XML file exist in the directory created as a result of the decompression.

In order to uninstall dataCompJ, delete the directory in which dataCompJ is installed.

<br>

# 2. Getting Started

This chapter describes the key concepts that helps running dataCompJ more effectively.

This chapter consists of the following sections:

- Terms for dataCompJ
- Inconsistent Records
- Synchronization Policy

### Terms for dataCompJ

##### Master DB

Master DB indicates Altibase database containing original data between two heterogeneous databases to be compared.

##### Slave DB

Slave DB indicates the other database to which the replicated data is applied between the two heterogeneous databases to be compared.

##### TablePair

TablePair means the comparison target of dataComJ specified by the user, and it is in table unit. TablePair represents a pair comprised of a table (Master table) in Master DB and a table (Slave table) in Slave DB.

##### Master Table

Master table is a orginal table in the Master DB specified by the user in TablePair.

##### Slave Table

Slave table is a comparison target table in the Slave DB specified by the user in TablePair.

### Inconsistent Records and Synchronization Policy

Inconsistent records signify records whose column values are inconsistent based on the primary key of the master and slave tables. The inconsistent record can be divided into three types as in the following.

##### MOSO inconsistent

This is a case in which particular records with the same value of primary key columns can be found in both Master and Slave DB, but the value of non primary key columns are different from each other.

##### MOSX inconsistent

This is a case in which records with values of primary key columns can be found in Master DB, but not in Slave DB.

##### MXSO inconsistent

This is a case when there exists particular records with values of primary key columns only in Slave DB, not in Master DB.

##### Resolving Inconsistent Record

When dataCompJ discovers inconsistent records, the two following functions are provided depending on the user's choice as delineated in dataCompJ configuration file.

1.  DIFF: This function distinguishes inconsistent records between Master tables and Slave tables and records them to a CSV format file.
2.  SYNC: This function distinguishes inconsistent records between Master tables and Slave tables and resolves the inconsistency based on the synchronization policy delineated in the dataCompJ configuration file.

### Synchronization Policy

Synchronization policy defines how to match up the records in slave tables in accordance with the records in master tables when dataCompJ discovers any inconsistent records. The synchronization policy provides the following three methods. 

##### MOSO Inconsistency

This method updates records with the same primary key in slave tables based on the master table records with UPDATE_TO_SLAVE policy.

##### MOSX Inconsistency

This method is used to insert a record, which exists in the master table but not in the slave table, into the slave table with INSERT_TO_SLAVE policy.

##### MXSO Inconsistency

This method deletes records, which exists only in the slave table, but not in the master table, from the slave table with DELETE_FROM_SLAVE policy.

<br>

# 3. How to Use dataCompJ

This section provides a step by step guide to operate dataCompJ and set up configuration file. 

This chapter consists of the following sections:

- How to run dataCompJ
- Executing dataCompJ
- Configuration File Setup

### How to run dataCompJ

The followings are the command to execute dataCompJ in the Command Line Interface (CLI).

- Linux

```
$ dataCompJCli.sh -f dataCompJ_env_file_path
```


- Windows

```
C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path
```


##### dataCompJ_env_file_path

This indicates the file path of dataCompJ configuration file and in a required option. dataCompJ.xml is provided as an configuration file when dataCompJ is installed but user can choose to create another file to use an as configuration file.

### Executing dataCompJ

dataCompJ operates based on the configuration file set up by the user, and it is largely divided into two phases which are build and run.

##### Build Phase

Build phase is an initial investigation step to determine whether the run phase can be performed based on the configuration file. If any issue is discovered, it is output in the report file(dataCompJ_report.txt) and dataCompJ is terminated.

1.  Read the configuration file set up by the user.
2.  Verify whether the connection information described in the configuration file is valid.
3.  Connect to both databases to validate the target tables described in the configuration file and verify the meta information. If an issue is detected in either of the tables, it is recorded in the report file and dataCompJ is terminated.

##### Run Phase

In run phase, data in the target tables are compared then either comparing(DIFF) or synchronizing(SYNC) is executed according to the user's choice.

The execution result of each TablePair is output in the report file(dataCompJ_report.txt).

##### Output Files

When dataCompJ is executed, one report file and two log files are generated.

The output files generated by the comparison function(DIFF) is thoroughly delineated in the section 'Comparison (DIFF) Function'.

-   dataCompJ_report.txt: This is a report file in a text form to inform the execution results to a user.
-   dataCompJ.log: This is a log file recording events that occurs during the program operation. Also, this file is used to trace execution history of the program.
-   dataCompJ_data.log: This is a log file generated in the run phase, and this file records details of inconsistent records processed during the execution of comparison(Diff)/synchronization(Sync) in case \<TraceInconsistentRecord\> in the configuration file is set to true. It is suggested to use this file only when report of inconsistent records is required in detail since large capacity file is created if there are a lot of inconsistent data and this degrades the program performance.

### Configuration File Setup

Configuration file is essential in order to execute dataCompJ. dataCompJ.xml file is provided by default when dataCompJ is installed, and it is also available to use any other file user has created as an configuration file.  The configuration file should be written based on the XML rules delineated in dataCompJ.xml, and it should be encoded with UTF-8 if multiple languages are included.

The dataCompJ configuration file can be divided into three sections, such as Connections, Options, and TablePairs.

##### Connections

The Connections section is the part in which information required for connecting to the Master DB and Slave DB is recorded.

###### \<MasterDB\> 

The connection information of Master DB is recorded. The Master DB should be Altibase database. The following XML elements are the sub-elements of the Master DB.

\<JdbcUrl\>  
This is a character string used to record information of JDBC connection except user ID and password.

\<JdbcFilePath\>  
This is used to specify the path in which the JDBC jar file exist in order to connect to Master DB.

\<UserId\>  
This is used to specify the user ID in order to connect to the database.

\<Password\>  
This is used to specify the user password in order to connect to the database.

\<FetchSize\>  
This is used to specify the number of records that are fetched at once when importing data from the database. It is optional to fill this in and the default value is set to 1,000.

\<BatchSize\>  
This is used to specify the number of records that are executed at once when updating the database by using INSERT/DELETE/UPDATE statement. For instance, if 10 is specified in this entry, ten INSERT/DELETE/UPDATE are executed at once. It is optional to fill this in and the default value is set to 1,000.

###### \<SlaveDB\> 

This is used to record the connection information of Slave DB. The sub-elements of Slave DB is identical to that of the Master DB. 

##### Options

User inserts property values to execute dataCompJ in this section.

###### \<Operation\> 

This is used to specify which function should be executed between comparison(DIFF) and synchronization(SYNC) function to process inconsistent data.

###### \<FileEncoding\> 

This is used to specify the type of encoding for files generated when dataCompJ is executed.

###### \<Diff\>

\<DirPath\>  
This is used to specify the directory path in which a CSV file is created as a result of comparing each target table when the comparison(DIFF) is executed. 

###### \<Sync\> 

The followings are options for executing the synchronization(SYNC) function.

\<MOSO UPDATE_TO_SLAVE="true"/\>  
This option specifies whether or not to update records in the slave table based on records in the master table if MOSO inconsistent data is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

\<MOSX INSERT_TO_SLAVE="true"/\>  
This option specifies whether or not to insert the records which exist only in the master table into the slave table if MOSX inconsistent data is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

\<MXSO DELETE_FROM_SLAVE="true"/\>  
This option specifies whether or not to delete the records in slave table which does not exist in the master table if MXSO inconsistent is detected. If it is set to 'false', the MOSO inconsistent data will not be processed.

###### \<Log\>

The following XML elements are the sub-elements of a log.

\<DirPath\>  
This element specifies the directory path of log files created when dataCompJ is executed.

\<TraceInconsistentRecord\>  
This element specifies whether or not to record details of all the inconsistent records detected while DIFF/SYNC function is executed.

###### \<MaxThread\> 

This element indicates the maximum number of allocable threads. If it is specified to 0, the number of CPU core of the machine dataCompJ is running is allocated as MaxThread.

##### TablePairs

TablePairs is the part in which target tables for comparison are recorded. There are two methods for recording the comparison target tables, such as recording each individual information on the target tables and specifying the path of the text file in which all the table names are listed. Such methods can be used either one at a time or simultaneously. 

The methods for providing information on each individual table is as follows, and it has an advantage that it can control the data comparison method precisely. For instance, it is also possible to exclude specific columns or compare only target data satisfying certain conditions.

The target table's name should be one that is allowed by both Master DB and Slave DB. The user must use double quotation marks (") in XML file if the table name contains any space, special character or it is case-sensitive. For instance, when a comparision target table's name is Employee 01 of SYS schema, user must write the table name with double quotation marks as SYS."Employee 01" because it contains a space in its name.

###### \<TablePair\> 

This is a unit of target data for comparison comprised of one master table and one slave table. The following XML elements are the sub-elements of TablePair.

\<MasterTable\>  
This element is the name of target data and it can be specified as *[SchemaName].TableName* format. Unless it is specified, the UserId of Master DB is the default schema name. This is a required entry; thus, an error is occurred when it is not written.

\<SlaveTable\>  
This element is the name of target data and it can be specified as *[SchemaName].TableName* format. Unless it is specified, the UserId of Slave DB is used as the default schema name. This is a required entry; thus, an error is occurred when it is not written.

\<Exclude\>  
This element specifies a condition for projecting table records. This element can also specify multiple columns by using a comma(,). This is an optional entry and if this is not written, all the columns with data types supported by dataCompJ would be selected as comparison targets.

\<Where\>  
This elements specifies a condition for selecting table records. It has the same formay as WHERE clause of SQL statement, and multiple conditions are allowed. This is an optional entry, and all the records would be comparison targets if it is not written.

\<TableNameFilePath\>  
Providing the path of the text file enumerating all the table names is as below, and this gives an advantage in inputting tables easily in case it is required to compare multiple tables at once.

```
<TableNameFilePath>table_name_file_path</TableNameFilePath>
```

table_name_file_path is the path of the text file enumerating table names. The name of comparison target can be specified with *[SchemaName].TableName* format, and each table is distinguished with a new-line character. The name of comparison target in Master DB should be identical to the name of comparison target in Slave DB.

###### Restrictions

The following restrictions should be considered when selecting comparison target tables. If any constraint is infringed, dataCompJ outputs the issue occurred during the build phase to the report file(dataCompJ_report.txt) and does not proceed to the run phase.

1. A comparison target table should be identically(the column name, column order, data type, and primary key) composed. However, the data type should be compatible to that of the other database.

2. The unsupported data type is automatically excluded from the comparison targets. (e.g., binary type such as LOB)

3. There should be at least more than one column which can compare values other than a primary key.

   (Example 1) table1 (c1 int, c2 int, c3 CLOB, primary key (c1, c2))  
   (Example 2) table1 (c1 int, c2 int, c3 varchar(100), primary key (c1, c2))

   In the example 1, c3 is the only column satisfying the 'Constraint 3'. However, it infringes 'Constraint 2' since the data type CLOB is not supported by dataCompJ. Therefore, comparison for table 1 is not allowed.

   In the enxt example, c3 is the only column satisfying 'Constraint 3' and it is varchar type which is supported by dataCompJ. Thus, the table 1 can be compared.

<br>

# 4. Functions

This chapter explains DIFF function and SYNC function in detail with examples.

This chapter consists of the following sections:

- Comparison (Diff) funtion
- Synchronization (SYNC) function

### Comparison (DIFF) Function

The comparison(DIFF) function verifies inconsistent records between Master DB and Slave DB by identifying the inconsistent records occurred during the replication execution between the two database system and recording them to a file.

#### Configuration File

Set the \<Options\> - \<Operation\> value in dataCompJ configuration file to "DIFF".

<Connections\> and <Options\> are required entries and target table should be described in <TablePairs\>.

##### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
        <JdbcFilePath>./jdbc/Altibase710.jar</JdbcFilePath>
        <UserId>sys</UserId>
        <Password>manager</Password>
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
        <JdbcFilePath>./jdbc/ojdbc5.jar</JdbcFilePath>
        <UserId>altibase</UserId>
        <Password>altibase</Password>
    </SlaveDB>
</Connections>
  
<Options>
    <Operation>DIFF</Operation> 
    <FileEncoding>UTF-8</FileEncoding>
    <Diff>
        <DirPath>./diff/</DirPath>
    </Diff>
    <Sync>
        <MOSO UPDATE_TO_SLAVE="true"/>
        <MOSX INSERT_TO_SLAVE="true"/>
        <MXSO DELETE_FROM_SLAVE="true"/>
    </Sync>
    <Log>
        <DirPath>./</DirPath>
        <TraceInconsistentRecord>false</TraceInconsistentRecord>
    </Log>
    <MaxThread>0</MaxThread>
</Options>
  
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### How to Execute Comparison(DIFF)

The comparison(DIFF) is executed with the following command.

```
$ dataCompJCli.sh -f dataCompJ.xml
```

#### Execution Result

As a result of the execution, a report file(dataCompJ_report.txt) in which the execution result is summarized and log files(dataCompJ.log, dataCompJ_data.log) in which the event is recorded during the execution are created. Such files are delineated in the "Output Files" in detail. 

The table structure used in the example is as follows.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int);
```

##### DIFF Execution

```
$ dataCompJCli.sh -f dataCompJ.xml
----------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
----------------------------------------------------------
* Build started  at 2016-12-14 16:30:03.673
* Build finished at 2016-12-14 16:30:04.357 (Elapsed: 0:00:00.691)
* Run   started  at 2016-12-14 16:30:04.374
* Run   finished at 2016-12-14 16:30:04.905 (Elapsed: 0:00:00.531)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
```

###### Verifying the Report File

```
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 16:30:03.673
     - Finished : 2016-12-14 16:30:04.357
     - Elapsed  : 0:00:00.691
--------------------------------------------------------
 
[ User input information ]
...
 
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: C3(CLOB)
==========================================================
    Run
     - Started  : 2016-12-14 17:19:42.731
     - Finished : 2016-12-14 17:19:42.822
     - Elapsed  : 0:00:00.091
----------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------

```

##### Executable Data File

Four following comma-separated values(CSV) format data files are created in a TablePair unit as a result of selecting the comparison(DIFF).

-   *SchemaName.TableName*\_MASTER_diff.csv:  
    If MOSO is detected, this file stores the value of inconsistent record founds in the master table in CSV form.

-   *SchemaName.TableName*\_SLAVE_diff.csv:  
    This file stores the value of inconsistent records found in the slave table due to MOSO inconsistency in CSV form.

-   *SchemaName.TableName*\_MASTER_only.csv:  
    This file stores the value of records which only exist in the master table due to MOSX inconsistency in CSV form.

-   *SchemaName.TableName*\_SLAVE_only.csv:  
    This file stores the value of records which only exist in the slave table due to MXSO inconsistency in CSV form.

Since the inconsistent data due to MOSO inconsistency are recorded in the same order in in SchemaName.TableName_MASTER_diff.csv and SchemaName.TableName_SLAVE_diff.csv, when DIFF function is used to compare these files, user can intuitively compare the part MOSO inconsistency occurred.

#### Example

The table structure used for the examples is as follows.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int); /* Unsupported data in C3 CLOB dataCompJ */
CREATE TABLE ex2 (C1 int primary key, C2 varchar(20), C3 int);
```

##### DIFF Example 1

This example demonstrates specifying or omitting the schema name for two target tables. 

In case of EX1 in the example below, <MasterTable\> entry describes only the table name without schema and <SlaveTable\> entry is omitted. The <MasterTable\> describing the table name only uses the value inserted in <MasterDB\>-\<UserId\> as its schema name. The omitted <SlaveTable\> is processed assuming that it has the same value with <MasterTable\>.

C3 column in EX1 table is automatically excluded from the comparison target since it is a CLOB type which is unsupported data type by dataCompJ, and this is recorded in candidate tables entry in the report. 

In EX2 table, the schema name and table name are specified by a user, and it is processed based on the inserted schema and table names.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>DIFF</Operation> 
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 2 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: 
===========================================================================
    Run
     - Started  : 2016-12-14 17:56:04.516
     - Finished : 2016-12-14 17:56:04.593
     - Elapsed  : 0:00:00.076
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
```

##### DIFF Example 2

The following example shows that a user can specify certain columns in tables to exclude, and conduct comparison(Diff) on records meeting specified conditions (Where). 

User specifies to exclude C4 in non-primary key columns on EX1 table from the comparison targets in dataCompJ.xml, and execute comparison only for the records whose C1 column value is greater than 5.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
...
<Options>
    <Operation>DIFF</Operation> 
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
        <Exclude>C4</Exclude>
        <Where>C1 > 5</Where>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 2 ]
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2 FROM SYS.EX1 WHERE C1 > 5 ORDER BY C1 ASC
    * Excluded columns     : C4
    * Where condition      : C1 > 5
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     : 
    * Where condition      : 
    * N/A data type columns: 
===========================================================================
    Run
     - Started  : 2016-12-14 17:57:09.895
     - Finished : 2016-12-14 17:57:09.974
     - Elapsed  : 0:00:00.080
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:            5
 Fetched record count from SLAVE :            5
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               5
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

### Synchronization(SYNC) Function

The Synchronization(SYNC) function identifies the inconsistent records occurred during the replication between the master DB and slave DB and applies them to the slave DB. This feature allows effective synchronization between the two database system.

#### Configuration Files

Set the \<Options\> - \<Operation\> value in dataCompJ configruration file to "SYNC".

<Connections\> and <Options\> are required entries and target table should be described in <TablePairs\>.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>SYNC</Operation> 
...
</Options>
  
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### How to Execyte Synchronization(SYNC)

The Synchronization(SYNC) function is executed as in the following manner.

```
$ dataCompJCli.sh -f dataCompJ.xml
$ dataCompJCli.sh -f ./dataCompJ.xml
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:08:40.407
* Build finished at 2016-12-14 18:08:41.076 (Elapsed: 0:00:00.676)
* Run   started  at 2016-12-14 18:08:41.090
* Run   finished at 2016-12-14 18:08:41.654 (Elapsed: 0:00:00.564)
---------------------------------------------------------------------------
Refer to the following output files for details.
---------------------------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record

```

#### Execution Results

As a result of the execution, a report file(dataCompJ_report.txt) in which the execution result is summarized and log files(dataCompJ.log, dataCompJ_data.log) in which the event is recorded during the execution are created. Such files are delineated in the "Output Files" in detail. 

###### dataCompJ_report.txt

```
$ cat dataCompJ_report.txt
===========================================================================
    Build
     - Started  : 2016-12-14 18:08:40.407
     - Finished : 2016-12-14 18:08:41.076
     - Elapsed  : 0:00:00.676
---------------------------------------------------------------------------
 
[ User input information ]
...
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
 
===========================================================================
    Run
     - Started  : 2016-12-14 18:08:41.090
     - Finished : 2016-12-14 18:08:41.654
     - Elapsed  : 0:00:00.564
---------------------------------------------------------------------------
 
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type    Resolution                Try         Fail
------------------------------------------------------
MOSO    UPDATE TO SLAVE                  2           0
MOSX    INSERT TO SLAVE                  1           0
MXSO    DELETE FROM SLAVE                1           0
------------------------------------------------------
```

When SYNC is correctly performed on all of the target tables and records, result fetched by executing DIFF on the same target table shows that all the records are identical.

```
$ dataCompJCli.sh -f ./dataCompJ.xml
-----------------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:11:54.924
* Build finished at 2016-12-14 18:11:55.561 (Elapsed: 0:00:00.645)
* Run   started  at 2016-12-14 18:11:55.580
* Run   finished at 2016-12-14 18:11:56.190 (Elapsed: 0:00:00.610)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
 
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 18:11:54.924
     - Finished : 2016-12-14 18:11:55.561
     - Elapsed  : 0:00:00.645
---------------------------------------------------------
 
[ User input information ]
...
 
[ Problematic table(s): 0 ]
 
[ Candidate table(s) for data comparison: 1 ]
 
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
 
==========================================================
    Run
     - Started  : 2016-12-14 18:11:55.580
     - Finished : 2016-12-14 18:11:56.190
     - Elapsed  : 0:00:00.610
---------------------------------------------------------------------------
 
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

<br>

# Appendix A: Data Type compatibility table between Other Databases

This section displays data type mapping table between other databases supported by dataCompJ. 

If comparison is executed on tables with unsupported data types by dataCompJ, it is processed in the following manners:

-   If both master table and slave table are in data types unsupported by dataCompJ: An error stating that the data type is unsupported is displayed in the build phase and it does not proceed to run phase.

-   If either the master table or the slave table is unsupported data type: In the build step, an error is reported to the report file (dataCompJ_report.txt) that the number of columns to be compared in the table is different, and does not proceed to run phase.

If the column data type of the table to be compared is a data type supported by dataCompJ, but the column data type of the target table for comparison is using different combination of data types to the one in data type compatibility table between other databases, it is processed in the following manners:

-   If the data comparison is impossible (e.g., comparison between integer type and character type data type): An error stating that the data type is incompatible is reported to the report file (dataCompJ_report.txt) in the build phase and it does not proceed to run phase.

-   For data types that is comparable but different to each other (e.g., integer and floating-point types): The run phase is executed since it cannot be processed in the build phase. However, in the execution result all records are treated as inconsistent records.

#### Altibase to Oracle

| Altibase | Oracle         | Description                                                  |
| -------- | -------------- | ------------------------------------------------------------ |
| SMALLINT | NUMBER         |                                                              |
| INTEGER  | NUMBER         |                                                              |
| BIGINT   | NUMBER         |                                                              |
| NUMERIC  | NUMBER         |                                                              |
| REAL     | NUMBER         |                                                              |
| DOUBLE   | NUMBER         |                                                              |
| FLOAT    | FLOAT          |                                                              |
| DATE     | DATE TIMESTAMP | - DATE - TIMESTAMP: Compared based on the smaller precision. For example, Altibase DATE supports up to microsecond, and Oracle TIMESTAMP supports up to nano second. In this case, the comparison of records is performed until nanosecond. <br>- DATE-DATE: Since Oracle DATE supports up to YYYY-MM-DD HH: MM: SS, only the according part is extracted from Altibase DATE and compared. |
| CHAR     | CHAR           |                                                              |
| VARCHAR  | VARCHAR2       |                                                              |
| NCHAR    | NCHAR          |                                                              |
| NVARCHAR | NVARCHAR2      |                                                              |

#### Altibase to MariaDB

| Altibase | MariaDB                                       | Description                                                  |
| -------- | --------------------------------------------- | ------------------------------------------------------------ |
| SMALLINT | SMALLINT                                      |                                                              |
| INTEGER  | INT                                           |                                                              |
| BIGINT   | BIGINT                                        |                                                              |
| NUMERIC  | DECIMAL                                       |                                                              |
| REAL     | FLOAT                                         |                                                              |
| DOUBLE   | DOUBLE                                        |                                                              |
| FLOAT    | N/A                                           | Data type corresponding to Altibase FLOAT does not exist in MariaDB. |
| DATE     | DATE, DATETIME, TIMESTAMP                     | - DATE-DATE: Since MariaDB DATE supports up to YYYY-MM-DD, only the according part is extracted from Altibase DATE and compared.<br>- DATE-DATETIME: Since MariaDB DATETIME supports up to YYYY-MM-DD HH: MM: SS, only the according part is extracted from Altibase DATE and compared.<br>- DATE-TIMESTAMP: Since MariaDB TIMESTAMP supports up to YYYY-MM-DD HH: MM: Microseconds 0-6 (default: 0), only the according part is extracted from Altibase DATE and compared. |
| CHAR     | CHAR                                          |                                                              |
| VARCHAR  | VARCHAR, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT |                                                              |
| NCHAR    | CHAR with Character set                       |                                                              |
| NVARCHAR | VARCHAR with Character set                    |                                                              |

<!-- SOURCE_BLOCK_END source_id="SRC-000206" block_id="BLOCK-000939" -->

## SRC-000208 - Release 7.1

| Field | Value |
| --- | --- |
| `source_id` | SRC-000208 |
| `source_path` | Manuals/Tools/Altibase_release/kor/Altibase Heartbeat User's Guide.md |
| `source_family` | utilities_datacompj |
| `version_scope` | multi |
| `language` | ko |
| `authority_label` | Korean authoritative |
| `source_sha256` | 8beb2b7fc2ffc7ea8f5a80716b754146689c5f8e306940ffbce4083d07d497b3 |
| `byte_count` | 31791 |
| `line_count` | 846 |
| `estimated_tokens` | 5011 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000208" source_path="Manuals/Tools/Altibase_release/kor/Altibase Heartbeat User&#x27;s Guide.md" source_family="utilities_datacompj" version_scope="multi" language="ko" authority_label="Korean authoritative" sha256="8beb2b7fc2ffc7ea8f5a80716b754146689c5f8e306940ffbce4083d07d497b3" byte_count="31791" line_count="846" estimated_tokens="5011" block_id="BLOCK-000940" -->
Altibase Heartbeat User's Guide
================

#### Release 7.1

Altibase® Tool & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 











































<!-- PDF 변환을 위한 여백입니다. -->

<pre>
Altibase Tool & Utilities Altibase HeartBeat User's Guide
Release 7.1
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>
<br>

# 목차

- [서문](#%EC%84%9C%EB%AC%B8)
  - [이 매뉴얼에 대하여](#%EC%9D%B4-%EB%A7%A4%EB%89%B4%EC%96%BC%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
- [1.Altibase Heartbeat 소개](#1altibase-heartbeat-%EC%86%8C%EA%B0%9C)
  - [Altibase Heartbeat 개요](#altibase-heartbeat-%EA%B0%9C%EC%9A%94)
  - [Altibase Heartbeat의 기본 동작](#altibase-heartbeat%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EB%8F%99%EC%9E%91)
- [2.명령어](#2%EB%AA%85%EB%A0%B9%EC%96%B4)
  - [aheartbeat](#aheartbeat)
- [3.Altibase Heartbeat 구성하기](#3altibase-heartbeat-%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0)
  - [환경 설정](#%ED%99%98%EA%B2%BD-%EC%84%A4%EC%A0%95)
  - [Altibase Heartbeat 시스템 구성 연습](#altibase-heartbeat-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%84%B1-%EC%97%B0%EC%8A%B5)
- [4.Altibase Heartbeat 동작](#4altibase-heartbeat-%EB%8F%99%EC%9E%91)
  - [aheartbeat의 상태](#aheartbeat%EC%9D%98-%EC%83%81%ED%83%9C)
  - [장애 판단](#%EC%9E%A5%EC%95%A0-%ED%8C%90%EB%8B%A8)
  - [0번 aheartbeat의 역할](#0%EB%B2%88-aheartbeat%EC%9D%98-%EC%97%AD%ED%95%A0)
  - [Failover와 Failback](#failover%EC%99%80-failback)
  - [로깅](#%EB%A1%9C%EA%B9%85)

<br>

서문
====

### 이 매뉴얼에 대하여

이 매뉴얼은 Altibase로 구성된 분산 데이터베이스 환경에서 사용할 수 있는 Altibase
Heartbeat 유틸리티에 대해 설명한다.

#### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

-   데이터베이스 사용자

-   데이터베이스 관리자

-   응용 프로그램 개발자

-   성능 관리자

-   기술지원부서

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

-   컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

-   관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

-   컴퓨터 프로그래밍과 관련된 경험이나 지식

-   데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

-   분산 환경에서의 데이터의 저장, 관리 및 처리와 관련된 지식

#### 소프트웨어 환경

이 매뉴얼은 Altibase 7.1 이상의 버전을 데이터베이스 서버로 사용한다는 가정 하에
작성되었다.

#### 이 매뉴얼의 구성

이 매뉴얼은 다음과 같이 구성되어 있다.

-   제 1장 Altibase Heartbeat 소개  
    이 장은 Altibase Heartbeat의 개요와 기본적인 동작을 설명한다.

-   제 2 장 명령어  
    이 장은 Altibase Heartbeat 명령어에 대해 설명한다.

-   제 3장 Altibase Heartbeat 구성하기  
    이 장에서는 Altibase Heartbeat를 설정하는 방법을 설명한다. 또한 Altibase
    Heartbeat와 함께 분산 데이터베이스 환경을 어떻게 구성할 수 있는지 살펴본다.

-   제 4 장 Altibase Heartbeat 동작  
    이 장은 Altibase Heartbeat의 동작을 상세히 설명한다. Altibase Heartbeat가
    장애를 판단하는 기준은 무엇인지, 장애를 감지한 후의 Failover는 어떻게
    이루어지는지 살펴본다.

#### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이
매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

-   샘플 코드 규칙

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어
설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                                                | 예제                                                                                                         |
|--------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [ ]          | 선택 항목을 표시                                                                    | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                                                                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시                               | { ENABLE \| DISABLE \| COMPILE }                                                                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                                           | { ENABLE \| DISABLE \| COMPILE } [ ENABLE \| DISABLE \| COMPILE ]                                            |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략되는 것을 표시                           | SQL\> SELECT ename FROM employee; ENAME  ----------------------- SWNO  HJNO  HSCHOI  . . . 20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이 외에 기호들                                                   | EXEC :p1 := 1; acc NUMBER(11,2);                                                                             |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치         | SELECT \* FROM *table_name*; CONNECT *userID*/*password*;                                                    |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 칼럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                                                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드                              | DESC SYSTEM_.SYS_INDICES_;                                                                                   |

#### 관련 자료

자세한 정보를 위하여 다음 문서 목록을 참조하기 바란다.

-   Getting Started Guide

-   Installation Guide

-   Administrator’s Manual

-   Replication Manual

-   Stored Procedures Manual

-   Error Message Reference

#### 알티베이스는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음
버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께
고객서비스포털(*http://support.altibase.com/kr/* )로 보내주시기 바랍니다.

-   사용 중인 매뉴얼의 이름과 버전

-   매뉴얼에 대한 의견

-   사용자의 성함, 주소, 전화번호

이 외에도 알티베이스 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인
문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인
부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를
요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.



1.Altibase Heartbeat 소개
=======================

이 장은 Altibase Heartbeat의 개요와 기본적인 동작을 설명한다.

### Altibase Heartbeat 개요

Altibase Heartbeat는 분산 데이터베이스 환경에서 각 데이터베이스 노드의 장애를
감지하고, DBA가 장애에 대한 조치를 할 수 있도록 제공되는 유틸리티이다.
aheartbeat[^1]는 Altibase 서버들이 이중화로 연결되어 구성된 환경에서 사용할 수
있다.

[^1]: aheartbeat: Altibase Heartbeat 유틸리티의 실행 바이너리 파일 이름이다.


따라서 본 문서에서는 Altibase Heartbeat과 aheartbeat가 혼용되어 사용된다.

#### Altibase Heartbeat 구성요소

Altibase Heartbeat는 아래의 세가지 주요 요소로 구성된다.

-   aheartbeat 프로세스

-   로컬 노드 failover 수행 파일

-   리모트 노드 failover 수행 파일

##### aheartbeat 프로세스

aheartbeat는 백그라운드에 수행되면서 총 2종류의 장애를 감지한다. 하나는 자기
노드의 Altibase 서버에 주기적으로 접속을 시도하여 데이터베이스의 장애를
감지한다. 그리고 다른 노드의 aheartbeat과 주기적으로 접속을 시도하여 네트워크
장애를 감지한다.

##### 로컬 노드 failover 수행 파일

로컬 노드 failover 수행 파일은 aheartbeat가 같은 노드의 데이터베이스 서버의
장애를 감지한 후에 failover를 위해 실행하는 파일이다. 이 파일은 실행이 가능한
바이너리 또는 스크립트 파일일 수 있다.

##### 리모트 노드 failover 수행 파일

리모트 노드 failover 수행 파일은 aheartbeat가 다른 노드의 장애를 감지한 후에
failover를 위해 실행하는 파일이다. 이 파일은 실행이 가능한 바이너리 또는
스크립트 파일일 수 있다.

### Altibase Heartbeat의 기본 동작

이 절에서는 Altibase Heartbeat가 분산 데이터베이스 환경에서 동작하는 기본 과정을
설명한다. 아래 그림은 다수의 Altibase를 Altibase Heartbeat와 함께 구성한
기본적인 분산 데이터베이스 환경을 도식화한 그림이다.

![heartbeat](media/Heartbeat/heartbeat.gif)

그림 1-1 Altibase Heartbeat의 동작

그림에서 보듯이 aheartbeat는 자신이 속한 노드의 Altibase 서버 프로세스를
감시해서 데이터베이스 장애를 감지(그림에서 1번 check)한다. 그리고 다른 노드의
aheartbeat 프로세스를 감시해서 노드 장애(그림에서 3번 check) 또는 외부 네트워크
장애(그림에서 2번 check)를 감지한다.

만약 노드 A에 있는 Altibase 서버에 장애가 발생한 경우 aheartbeat들이 어떻게
동작할 것인지 살펴본다.

1.  노드 A의 aheartbeat가 Altibase 서버의 장애 감지

2.  노드 A의 aheartbeat가 로컬 노드 failover 수행 파일을 실행하고, aheartbeat는
    스스로 종료

3.  노드 B의 aheartbeat는 노드 A의 aheartbeat가 없어졌음을 감지하고 노드 A의
    Altibase 서버에 장애가 발생했음을 인지하여, 리모트 노드 failover 수행 파일을
    실행.

2.명령어
======

이 장은 Altibase Heartbeat 명령어에 대해 설명한다.

### aheartbeat

aheartbeat는 Altibase Heartbeat를 구동 또는 종료하거나, 노드들의 정보를 얻기
위해 사용된다.

#### 구문

```
aheartbeat {-r|-s|-i}
```



#### 옵션

| 옵션            | 설명                                                    |
|-----------------|---------------------------------------------------------|
| \-r 또는 --run  | aheartbeat 시작                                         |
| \-s 또는 --stop | aheartbeat 종료                                         |
| \-i 또는 --info | aheartbeat가 동작하는 분산 환경의 모든 노드 정보를 출력 |

#### 예제

Altibase Heartbeat를 시작한다.

```
$ aheartbeat -r
```

Altibase Heartbeat를 종료한다.

```
$ aheartbeat -s
```

aheartbeat가 동작하는 분산 환경을 구성하는 모든 노드에 대한 정보를 출력한다.

```
$ aheartbeat -i
#ID     IP                 PORT      STATUS
0      192.168.1.31        55778     RUN
0      172.168.221.32      55778     RUN
1      192.168.2.33        55444     RUN
1      168.768.1.1         55444     READY
2      192.168.2.33        54321     ERROR
2      ::2:1               54321     RUN
```



3.Altibase Heartbeat 구성하기
===========================

이 장에서는 Altibase Heartbeat를 설정하는 방법을 설명한다. 또한 Altibase
Heartbeat를 분산 데이터베이스 환경에서 어떻게 이용할 수 있는지 살펴본다.

### 환경 설정

이 절은 Altibase Heartbeat를 분산 데이터베이스 환경에 사용하기 위해 필요한 환경
설정에 대해 설명한다.

#### 환경 변수

##### 필수 환경 변수

아래는 Altibase Heartbeat를 사용하기 위해 반드시 설정해야 하는 환경변수의
목록이다.

- ALTI_HBP_HOME  
  Altibase Heartbeat의 홈 디렉토리를 설정한다. 아래 예제와 같이 환경 변수
  PATH에 ALTI_HBP_HOME/bin을 추가해야 한다.

  ```
  export PATH=$ALTI_HBP_HOME/bin:$PATH : PATH
  ```


-   ALTI_HBP_ID  
    Altibase Heartbeat가 위치하는 노드를 식별하기 위한 ID를 설정한다. 1에서 99
    사이의 정수로 설정해야 하며, 각 노드는 유일한 ID를 가져야 한다. 특히 ID 0은
    해당 노드의 aheartbeat가 외부 네트워크에 존재함을 나타내기 때문에, 내부망에
    존재하는 노드의 ID로는 사용할 수 없다.

-   ALTI_HBP_ALTIBASE_PORT_NO  
    Altibase Heartbeat가 감시할 Altibase 서버의 리스닝 포트 번호(listening port
    number)를 설정한다. 즉, aheartbeat와 동일한 노드에 존재하는 Altibase 서버의
    리스닝 포트 번호이다.

-   ALTI_HBP_DETECT_INTERVAL  
    Altibase Heartbeat가 Altibase 서버의 장애를 검사하는 주기를 초 단위로
    설정한다.

-   ALTI_HBP_DETECT_HIGHWATER_MARK  
    Altibase Heartbeat가 감시하는 Altibase 서버 또는 다른 노드의 aheartbeat로의
    접속 시도에 대해 응답이 없는 경우, 몇 회 접속 시도 이후에 장애로 판단할
    것인지 설정한다.

##### 선택 환경 변수

아래의 환경변수는 필요에 따라 추가적으로 설정할 수 있다.

-   ALTI_HBP_ALTIBASE_FAILURE_EVENT  
    Altibase Heartbeat가 같은 노드의 Altibase 서버의 장애를 감지할 때 실행하는
    실행 가능한 바이너리 파일 또는 스크립트 파일의 이름이다. 설정하지 않으면
    기본으로 \$ALTI_HBP_HOME/bin/altibaseFailureEvent.sh가 실행된다.

-   ALTI_HBP_REMOTE_NODE_FAILURE_EVENT  
    Altibase Heartbeat가 다른 노드의 장애를 감지한 경우 실행하는 실행 가능한
    바이너리 파일 또는 스크립트 파일의 이름이다. 설정하지 않으면 기본으로
    \$ALTI_HBP_HOME/bin/remoteNodeFailureEvent.sh가 실행된다.

#### aheartbeat 노드 설정

Altibase Heartbeat을 이용한 분산 환경 구성을 위하여 aheartbeat.settings 파일이
존재한다. aheartbeat.settings 파일은 분산 환경을 구성하는 모든 노드에 대한
정보를 저장하는 파일로써, \$ALTI_HBP_HOME/conf 디렉터리에 존재한다. 이 파일은
Altibase Heartbeat를 실행하기 위해 반드시 필요하다.

aheartbeat.settings에 저장되는 각 노드에 대한 정보는 노드 ID, IP 주소,
aheartbeat의 리스닝 포트 번호(listening port number)로 구성된다. 각 요소는
aheartbeat가 다른 노드의 aheartbeat에 접속하기 위해 필요한 항목이다.

만약 한 장비가 여러 개의 IP 주소를 가지는 경우, 동일한 ID에 대해 서로 다른 IP
주소로 구성된 세트를 4개까지 설정할 수 있다. 그리고 동일한 ID에 대해 IP 버전별
설정도 가능하다.

\<aheartbeat.settings 파일의 예시\>

```
# ID   IP                  PORT
0      169.215.114.23    55778     # public domain
0      222.112.231.234   55778     # public domain
1      192.168.2.33       55444
1      222.112.181.231   55444     # public domain
2      192.168.2.33       54321
2      ::ffff:c0a8:221   54321     # IPv6
```

위의 예시에서 노드 0은 두 개의 IP 주소 169.215.114.23과 222.112.231.234를 가지며
aheartbeat의 리스닝 포트 번호는 55778이다. 노드 1은 192.168.2.33과
222.112.181.231 두 개의 IP 주소를 가지며 aheartbeat의 리스닝 포트 번호는
55444이다.

노드 2의 경우 동일한 ID에 대해 IP 버전별로 설정한 것으로써, IPv4 주소
192.168.2.33과 IPv6 주소 ::ffff:c0a8:221을 따로 설정한 것이다. aheartbeat의
리스닝 포트 번호는 55321이다. 그리고 \#을 이용하여 주석을 남길 수 있다.

##### 주의 사항

한 분산 환경을 구성하는 모든 노드는 aheartbeat.settings 파일의 설정 내용이
동일해야 한다. 그렇지 않으면 Altibase Heartbeat가 오동작을 일으킬 수 있다.

#### failover 수행 파일

aheartbeat가 자기 노드의 Altibase 서버 혹은 다른 노드의 aheartbeat에 접속이
불가능하면, 즉 장애를 감지하면 failover용 실행 파일을 실행한다. failover용 실행
파일은 \$ALTI_HBT_HOME/bin 디렉토리에 있어야 하며, 파일명은 위의 절에서 설명한
ALTI_HBP_ALTIBASE_FAILURE_EVENT, ALTI_HBP_REMOTE_NODE_FAILURE_EVENT 환경변수로
설정할 수 있다.

기본으로 제공하는 failover용 스크립트 파일은 아래와 같다.

-   altibaseFailureEvent.sh  
    Altibase Heartbeat가 같은 노드의 Altibase 서버의 장애를 감지한 경우 실행하는
    스크립트 파일이다. DBA에게 장애 발생을 알려주거나 해당 노드의 Altibase
    서버를 재구동하는 등의 작업을 포함시킬 수 있다.

-   remoteNodeFailureEvent.sh  
    Altibase Heartbeat가 다른 노드의 장애를 감지한 경우 실행하는 스크립트
    파일이다. 장애가 발생한 데이터베이스의 서비스를 failover하는 등의 작업을
    포함시킬 수 있다.

데이터베이스 관리자는 기본으로 제공되는 스크립트 파일을 상황에 맞게 수정하거나,
failover 작업을 수행하는 응용프로그램을 작성하여 장애에 능동적으로 대처할 수
있다.

#### 0번 aheartbeat

내부망의 데이터베이스가 외부망의 클라이언트에 서비스를 제공하는 시스템 구성에서,
내부망에서 외부망으로의 네트워크 장애를 감지하기 위해 외부망에 Altibase
Heartbeat를 둘 수 있다. 외부망에 aheartbeat를 두는 노드의 ID는 반드시 0이어야
한다. 이런 연유로 외부망에 두는 aheartbeat를 0번 aheartbeat라고 부른다.

0번 aheartbeat의 추가는 사용자 선택사항이다.

### Altibase Heartbeat 시스템 구성 연습

이 절은 Altibase와 Altibase Heartbeat 유틸리티로 분산 환경을 구성하는 방법을
예시와 함께 살펴본다.

Altibase로 이루어진 분산 환경에 Altibase Heartbeat 유틸리티를 포함시켜서 더욱
강화된 무정지 데이터베이스 서비스를 제공할 수 있다.

#### 분산환경 구성도 및 조건

내부망에 A, B, C 세 노드가 있고 각 노드에 Altibase 서버와 aheartbeat가 존재한다.

![heartbeat_sample](media/Heartbeat/heartbeat_sample.gif)

그림 3-1 분산환경 구성도

-   각 노드의 Altibase에 서비스를 요청하는 클라이언트가 존재한다.

-   0번 aheartbeat가 공용망인 169.215.114.23에서 리스닝 포트 번호 44000으로
    동작한다.

-   각 노드의 IP 주소와 aheartbeat, Altibase 서버의 리스닝 포트 번호는 아래와
    같다.

| 노드 | IP 주소        | Altibase 서버 리스닝 포트 번호 | aheartbeat 리스닝 포트 번호 |
|------|----------------|--------------------------------|-----------------------------|
| A    | 192.168.100.30 | 20000                          | 21000                       |
| B    | 192.168.100.31 | 30000                          | 31000                       |
| C    | 192.168.100.32 | 40000                          | 41000                       |

#### 환경변수 설정

위와 같은 조건하에서 각 노드의 환경변수는 아래와 같이 설정할 수 있을 것이다.

- 0 번 aheartbeat의 노드(외부망):

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=0

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 A:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=1

  ALTI_HBP_ALTIBASE_PORT_NO=20000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 B:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=2

  ALTI_HBP_ALTIBASE_PORT_NO=30000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

- 노드 C:

  ALTI_HBP_HOME=/altibase/hbp_home

  ALTI_HBP_ID=3

  ALTI_HBP_ALTIBASE_PORT_NO=40000

  ALTI_HBP_DETECT_INTERVAL=3

  ALTI_HBP_DETECT_HIGHWATER_MARK=10

> 참고: 0번 노드에서는 ALTI_HBP_ALTIBASE_PORT_NO 환경변수가 무시된다.
>

#### aheartbeat.settings

\$ALTI_HBP_HOME/conf/aheartbeat.settings 파일의 내용은 모든 노드에서 동일하며
아래와 같다.

\# ID     IP PORT

0      169.215.114.23        44000    #External Network

1      192.168.100.30        21000    #NODE A

2      192.168.100.31        31000    #NODE B

3      192.168.100.32        41000    #NODE C

#### failover 수행 파일

\$ALTI_HBP_HOME/bin 디렉토리의 altibaseFailureEvent.sh 파일과
remoteNodeFailureEvent.sh의 내용을 상황에 맞게 수정한다. 또는 failover를 위한
응용프로그램을 작성한 후 실행 바이너리를 \$ALTI_HBP_HOME/bin 디렉토리에 두고
해당 환경변수를 설정한다.

#### aheartbeat 구동

각 노드에서 Altibase Heartbeat를 아래의 명령어로 실행한다.

```
$ aheartbeat -r
```

노드별 구동 순서는 상관없다. 실행 후 시간이 조금 경과하면 아래의 명령어로 각
노드의 상태를 확인할 수 있다.

```
$ aheartbeat -i
```



4.Altibase Heartbeat 동작
=======================

이장은 Altibase Heartbeat의 동작을 상세히 설명한다. Altibase Heartbeat가 장애를
판단하는 기준이 무엇인지, 장애를 감지한 후의 Failover는 어떻게 이루어지는지
살펴본다.

### aheartbeat의 상태

aheartbeat는 자신의 상태와 다른 aheartbeat의 상태를 각각 정의한다.

우선 aheartbeat 자신은 실행 상태에 따라 아래의 세가지 중 하나의 상태를 가진다.

-   Ready: aheartbeat 실행 전 상태

-   Run: aheartbeat가 실행되어 정상적으로 동작중인 상태

-   Error: 해당 노드에 장애가 발생한 상태

또한 aheartbeat는 다른 노드에 존재하는 aheartbeat의 상태를 아래 세가지 상태 중
하나로 정의한다.

-   Ready: 상대 노드의 aheartbeat와 최초 handshake를 하기 전

-   Run: 상대 노드의 aheartbeat와 성공적으로 handshake한 후 정상적으로 연결되는
    상태

-   Error: 이전까지 Run 상태로 감지되던 상대 노드 aheartbeat에 접속이 불가능한
    경우

한 상태에서 다른 상태로 전이되는 과정은 아래 그림과 같이 이루어진다. 

![heartbeat_transition](media/Heartbeat/heartbeat_transition.gif)

<!-- IMG_RECOVERY_BEGIN ref_id="img-07163" source_md="Manuals/Tools/Altibase_release/kor/Altibase Heartbeat User&#x27;s Guide.md" line_no="672" image_path_raw="media/Heartbeat/heartbeat_transition.gif" image_class="E" format="mermaid" verified="True" -->
```mermaid
flowchart LR
    Ready([Ready])
    Run([Run])
    Error([Error])
    Ready -->|"(1)"| Run
    Run -->|"(2)"| Error
    Error -->|"(3)"| Run
    Run -->|"(4)"| Ready
```
<!-- IMG_RECOVERY_END ref_id="img-07163" -->


그림 4-1 aheartbeat 상태 전이

각각의 상태 전이는 아래 표와 같은 상황에서 발생한다.

| 상태 전이 | 설명                                         |
|-----------|----------------------------------------------|
| (1)       | aheartbeat 시작후 handshake 성공             |
| (2)       | 장애로 인해 aheartbeat 종료                  |
| (3)       | 장애 후 aheartbeat 재시작후 handshake 재성공 |
| (4)       | aheartbeat 정상 종료                         |

표 4-1 상태 전이

### 장애 판단

이 절은 Altibase Heartbeat가 장애를 감지하기 위해 취하는 동작과 장애를 판단하는
기준은 무엇인지 살펴본다.

Altibase Heartbeat는 아래의 순서대로 감시를 진행하며, 세 가지 대상에 접속해서
장애를 감지한다. 또한 아래 표는 각 감시 대상 별로 접속이 불가능할 때 어떤
노드(로컬 또는 리모트 노드)에 장애가 발생한 것으로 판단하는지도 보여준다.

| 순서 | 감시 대상                 | 노드 장애 판단          |
|------|---------------------------|-------------------------|
| 1    | 0번 aheartbeat            | 로컬 노드에 장애 발생   |
| 2    | 로컬 노드의 Altibase 서버 | 로컬 노드에 장애 발생   |
| 3    | 리모트 노드의 aheartbeat  | 리모트 노드에 장애 발생 |

표 4-2 장애 판단

#### 로컬 노드의 장애

각 노드의 aheartbeat들이 위 표의 1번 또는 2번에서 장애를 감지하는 경우 로컬
노드에 장애가 발생한 것으로 판단한다.

각 노드의 aheartbeat들은 가장 먼저 외부 공용망에 존재하는 0번 aheartbeat를
감시하며 접속이 불가능할 때 로컬 노드에 장애가 발생한 것으로 판단하다. 이 경우
로컬 노드에 존재하는 Altibase 서버 자체의 장애 여부와는 상관없으며, Altibase
서버와 클라이언트간의 네트워크 장애로 인해 서비스가 불가능하다고 판단한다.

0 번 aheartbeat로의 접속이 정상이거나, 0번 aheartbeat가 없을 때에는 각 노드의
aheartbeat들은 로컬 노드에 존재하는 Altibase 서버를 감시하며 이에 접속이
불가능할 때 데이터베이스 장애로 판단한다. 이 경우 데이터베이스 자체 장애로 인해
서비스가 불가능하다고 판단한다.

위의 두 감시 대상에서 장애가 발생한 것을 인지하면, aheartbeat는 로컬 노드
failover 수행 파일을 시작하고 스스로 종료한다.

#### 리모트 노드의 장애

각 노드의 aheartbeat들이 위 표의 3번에서 장애를 감지하는 경우 리모트 노드에
장애가 발생한 것으로 판단한다. 즉, RUN 상태로 파악된 다른 노드의 aheartbeat에
접속이 불가능하다면 그 노드에 장애가 발생한 것으로 판단하고 리모트 노드 failover
수행 파일을 시작한다.

> 참고: 로컬 노드에 장애가 발생하면 그 노드의 aheartbeat는 스스로 종료하기
> 때문에, 다른 노드의 aheartbeat들은 그 노드의 aheartbeat에 접속할 수 없다. 따라서
> 리모트 노드의 Altibase 서버에 장애가 발생한 것으로 판단한다.
>

### 0번 aheartbeat의 역할

0번 aheartbeat가 분산 데이터베이스 환경에서 하는 역할과 특징은 아래와 같다.

-   0번 aheartbeat는 자기 노드의 Altibase 서버를 감시하지 않는다.

-   ID가 0이 아닌 노드의 aheartbeat가 0번 aheartbeat에 접속하는 것으로 외부망과
    단절되었는지 여부를 파악할 수 있다. 외부망과 단절되었다는 것은 클라이언트와
    접속이 끊어졌다는 것을 의미한다.

아래는 분산 데이터베이스 환경에서 0번 aheartbeat가 구축되었는지 여부에 따라 장애
감지 결과가 어떻게 달라지는지 살펴본다.

#### 0번 aheartbeat가 없을 때

aheartbeat가 내부망 안에서만 구축된 분산 데이터베이스 환경에서 네트워크 연결에
장애가 발생한 경우를 가정해 보자.

![heartbeat_fail_0_noexistence](media/Heartbeat/heartbeat_fail_0_noexistence.gif)

그림 4-2 내부망과 외부망 사이의 네트워크 장애 발생

위 그림에서처럼 노드 A와 외부망 사이에서 네트워크에 장애가 발생하는 경우, 노드
A의 aheartbeat는 클라이언트에 서비스를 할 수 없는 상황이다. 하지만 네트워크
장애를 감지하지 못하여 aheartbeat가 계속 동작한다. 이로 인해 노드 B의 aheartbeat
역시 노드 A의 데이터베이스 서비스에 문제가 발생한 것을 감지할 수 없고, 노드 A를
failover 하지 않는다.

#### 0번 aheartbeat가 있을 때

aheartbeat가 외부망에 존재하는 분산 데이터베이스 환경에서 네트워크 연결에 장애가
발생한 경우를 가정해 보자.

![heartbeat_fail_0_existence](media/Heartbeat/heartbeat_fail_0_existence.gif)

그림 4- 3 내부망과 외부망 사이의 네트워크 장애 발생

위 그림에서처럼 노드 A와 외부망 사이에 네트워크에 장애가 발생하는 경우, 노드 A의
aheartbeat는 0번 aheartbeat에 접속이 불가능하다. 따라서 노드 A의 aheartbeat는
로컬 노드에 장애가 발생한 것으로 판단하여, 스스로 종료하고 다른 노드에서 본인의
장애를 감지할 수 있도록 한다. 결국 노드 B의 aheartbeat는 노드 A의 aheartbeat에
접속을 할 수 없으므로 노드 A를 failover하기 위해 리모트 노드 failover 수행
파일을 실행한다.

위의 두 예시에서 보듯이 0번 aheartbeat가 있다면 내부망과 외부망 사이에 발생하는
네트워크 장애까지 감지할 수 있으므로 무정지 데이터베이스 서비스를 더욱 강화할 수
있다.

### Failover와 Failback

#### Failover

DBA가 좀 더 효율적으로 failover를 수행하기 위하여, aheartbeat는 장애를 감지하면
다음 2개의 인자와 함께 failover 수행 파일을 실행한다.

| 인자         | 설명                                                            |
|--------------|-----------------------------------------------------------------|
| 첫 번째 인자 | 장애가 일어난 노드의 개수                                       |
| 두 번째 인자 | 장애가 일어난 노드의 ID들. 공백으로 구분하여 오름차순으로 지정. |

예를 들어 ID가 각각 1, 2, 3, 4, 5인 다섯 개의 노드에 Altibase 서버와
aheartbeat가 실행 중인 분산 환경에서, ID가 3인 노드의 Altibase 서버에 장애가
발생했다고 가정하자. ID가 3인 노드의 aheartbeat가 자기 노드의 Altibase 서버에
장애를 감지하면, 아래와 같이 로컬 노드 failover 스크립트를 실행하고 자신은
종료한다.

```
altibaseFailureEvent.sh 1 3
```

그리고 나머지 노드의 aheartbeat들은 ID가 3인 노드의 aheartbeat가 종료된 것을
감지한 후 아래와 같이 리모트 노드 failover 스크립트를 실행한다.

```
remoteNodeFailureEvent.sh 1 3
```

ID 3 노드의 장애 상황에서 또다시 ID 1인 노드의 Altibase 서버에 장애가 발생하면
아래와 같은 인자와 함께 failover 스크립트를 실행한다.

```
altibaseFailureEvent.sh 2 1 3
remoteNodeFailureEvent.sh 2 1 3
```

즉, 두 개의 서버에 장애가 발생했으며 그 ID는 1과 3이라는 것을 의미한다.

#### Failback

장애가 발생한 노드가 복구된 후의 failback은 사용자가 수동으로 수행해야 한다.

### 로깅

Altibase Heartbeat는 동작 중에 아래와 같은 정보를 로그 파일에 기록한다.

-   aheartbeat 시작 정보

-   Altibase 서버로의 접속 실패 정보

-   다른 노드로 접속 시작 정보

-   Altibase 서버 및 다른 노드의 aheartbeat 장애 상황 정보

-   각 노드의 aheartbeat 상태 변화 정보

로그 파일은 \$ALTI_HBP_HOME/log/aheartbeat.log로 고정되어 있다.

로그 정보의 출력 형식은 다음과 같다.

```
[YYYY-MM-DD HH:MM:SS T-<threadID>] Log Body
```

<!-- SOURCE_BLOCK_END source_id="SRC-000208" block_id="BLOCK-000940" -->

## SRC-000213 - Release 7.2

| Field | Value |
| --- | --- |
| `source_id` | SRC-000213 |
| `source_path` | Manuals/Tools/Altibase_release/kor/dataCompJ User's Manual.md |
| `source_family` | utilities_datacompj |
| `version_scope` | multi |
| `language` | ko |
| `authority_label` | Korean authoritative |
| `source_sha256` | 60c0f32affc023fc95b19f2d2cea62e658e71fee97144053383605fcef2a1e1f |
| `byte_count` | 53384 |
| `line_count` | 1171 |
| `estimated_tokens` | 9511 |

<!-- SOURCE_BLOCK_BEGIN source_id="SRC-000213" source_path="Manuals/Tools/Altibase_release/kor/dataCompJ User&#x27;s Manual.md" source_family="utilities_datacompj" version_scope="multi" language="ko" authority_label="Korean authoritative" sha256="60c0f32affc023fc95b19f2d2cea62e658e71fee97144053383605fcef2a1e1f" byte_count="53384" line_count="1171" estimated_tokens="9511" block_id="BLOCK-000941" -->
dataCompJ User's Manual
================

#### Release 7.2

Altibase® Tools & Utilities

<br><br><br><br><br><br><!-- PDF 변환을 위한 여백입니다. --> 







































<!-- PDF 변환을 위한 여백입니다. --> 

<div align="left">
    <img src="media/common/e5cfb3761673686d093a3b00c062fe7a.png">
</div>
<br><br><!-- PDF 변환을 위한 여백입니다. --> 











































<!-- PDF 변환을 위한 여백입니다. -->

<pre>
Altibase Tool & Utilities dataCompJ User's Manual
Release 7.2
Copyright ⓒ 2001~2023 Altibase Corp. All Rights Reserved.<br>
본 문서의 저작권은 ㈜알티베이스에 있습니다. 이 문서에 대하여 당사의 동의없이 무단으로 복제 또는 전용할 수 없습니다.<br>
<b>㈜알티베이스</b>
08378 서울시 구로구 디지털로 306 대륭포스트타워Ⅱ 10층
전화 : 02-2082-1114
팩스 : 02-2082-1099
고객서비스포털 : <a href='http://support.altibase.com'>http://support.altibase.com</a>
홈페이지      : <a href='http://www.altibase.com/'>http://www.altibase.com</a></pre>

<br>

# 목차

- [서문](#%EC%84%9C%EB%AC%B8)
  - [이 매뉴얼에 대하여](#%EC%9D%B4-%EB%A7%A4%EB%89%B4%EC%96%BC%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
- [1.dataCompJ 소개](#1datacompj-%EC%86%8C%EA%B0%9C)
  - [개요](#%EA%B0%9C%EC%9A%94)
  - [시스템 요구 사항](#%EC%8B%9C%EC%8A%A4%ED%85%9C-%EC%9A%94%EA%B5%AC-%EC%82%AC%ED%95%AD)
- [2.dataCompJ 시작하기](#2datacompj-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
  - [용어](#%EC%9A%A9%EC%96%B4)
  - [불일치 레코드(Inconsistent record)](#%EB%B6%88%EC%9D%BC%EC%B9%98-%EB%A0%88%EC%BD%94%EB%93%9Cinconsistent-record)
  - [일치 정책 (Synchronization policy)](#%EC%9D%BC%EC%B9%98-%EC%A0%95%EC%B1%85-synchronization-policy)
- [3.dataCompJ 사용 방법](#3datacompj-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95)
  - [dataCompJ 실행 방법](#datacompj-%EC%8B%A4%ED%96%89-%EB%B0%A9%EB%B2%95)
  - [dataCompJ 수행 단계](#datacompj-%EC%88%98%ED%96%89-%EB%8B%A8%EA%B3%84)
  - [dataCompJ 설정 파일 구성](#dataCompJ-설정-파일-구성)
- [4.dataCompJ 기능](#4datacompj-%EA%B8%B0%EB%8A%A5)
  - [비교(DIFF) 기능](#%EB%B9%84%EA%B5%90diff-%EA%B8%B0%EB%8A%A5)
  - [일치(SYNC) 기능](#%EC%9D%BC%EC%B9%98sync-%EA%B8%B0%EB%8A%A5)
- [A. 부록: 이기종간 데이터 타입 호환 테이블](#a-%EB%B6%80%EB%A1%9D-%EC%9D%B4%EA%B8%B0%EC%A2%85%EA%B0%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85-%ED%98%B8%ED%99%98-%ED%85%8C%EC%9D%B4%EB%B8%94)

<br>

서문
====

### 이 매뉴얼에 대하여

이 매뉴얼은 Altibase 데이터베이스에서 이기종 데이터베이스로 데이터를 복제한 이후의 데이터 정합성 확인과 데이터 불일치를 해소하기 위한 도구인 dataCompJ를 사용하는 방법을 기술한다.

#### 대상 사용자

이 매뉴얼은 다음과 같은 Altibase 사용자를 대상으로 작성되었다.

- 데이터베이스 관리자

- 성능 관리자

- 데이터베이스 사용자

- 응용 프로그램 개발자

- 기술지원부

다음과 같은 배경 지식을 가지고 이 매뉴얼을 읽는 것이 좋다.

- 컴퓨터, 운영 체제 및 운영 체제 유틸리티 운용에 필요한 기본 지식

- 관계형 데이터베이스 사용 경험 또는 데이터베이스 개념에 대한 이해

- 컴퓨터 프로그래밍 경험

- 데이터베이스 서버 관리, 운영 체제 관리 또는 네트워크 관리 경험

#### 이 매뉴얼의 구성

- 제 1장 dataCompJ 소개  
  이 장은 dataCompJ의 특징을 이해하고자 하는 사용자에게 이 도구를 소개하고 설치하는 방법을 설명한다.

- 제 2장 dataCompJ 시작하기  
  이 장은 사용자들이 dataCompJ를 좀 더 능률적이고 효율적으로 실행하는 데 도움이 되는 기본 개념을 소개한다.

- 제 3장 dataCompJ 사용 방법
  이 장은 dataCompJ를 원활하게 실행하기 위한 방법과 dataCompJ 설정 파일 구성, 설정 시 고려할 점들을 설명한다.

- 제 4장 dataCompJ 기능

  이 장은 dataCompJ의 비교(DIFF) 기능과 일치(SYNC) 기능을 보다 자세히 예제와 함께 설명한다.

- A. 부록: 이기종간 데이터 타입 호환 테이블

#### 문서화 규칙

이 절에서는 이 매뉴얼에서 사용하는 규칙에 대해 설명한다. 이 규칙을 이해하면 이 매뉴얼과 설명서 세트의 다른 매뉴얼에서 정보를 쉽게 찾을 수 있다.

여기서 설명하는 규칙은 다음과 같다.

- 구문 다이어그램

- 샘플 코드 규칙

##### 구문 다이어그램

이 매뉴얼에서는 다음 구성 요소로 구축된 다이어그램을 사용하여, 명령문의 구문을 설명한다.

| 구성 요소                             | 의미                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| ![image1](media/dataCompJ/image1.gif) | 명령문이 시작한다. 완전한 명령문이 아닌 구문 요소는 화살표로 시작한다. |
| ![image2](media/dataCompJ/image2.gif) | 명령문이 다음 라인에 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 종료한다. |
| ![image3](media/dataCompJ/image3.gif) | 명령문이 이전 라인으로부터 계속된다. 완전한 명령문이 아닌 구문 요소는 이 기호로 시작한다. |
| ![image4](media/dataCompJ/image4.gif) | 명령문이 종료한다.                                           |
| ![](media/dataCompJ/image5.gif)       | 필수 항목                                                    |
| ![](media/dataCompJ/image6.gif)       | 선택적 항목                                                  |
| ![](media/dataCompJ/image7.gif)       | 선택사항이 있는 필수 항목. 한 항목만 제공해야 한다.          |
| ![](media/dataCompJ/image8.gif)       | 선택사항이 있는 선택적 항목                                  |
| ![](media/dataCompJ/image9.gif)       | 선택적 항목. 여러 항목이 허용된다. 각 반복 앞부분에 콤마가 와야 한다. |

##### 샘플 코드 규칙

코드 예제는 SQL, Stored Procedure, iSQL 또는 다른 명령 라인 구문들을 예를 들어 설명한다.

아래 테이블은 코드 예제에서 사용된 인쇄 규칙에 대해 설명한다.

| 규칙         | 의미                                                         | 예제                                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ ]          | 선택 항목을 표시                                             | VARCHAR [(*size*)] [[FIXED \|] VARIABLE]                     |
| { }          | 필수 항목 표시. 반드시 하나 이상을 선택해야 되는 표시        | { ENABLE \| DISABLE \| COMPILE }                             |
| \|           | 선택 또는 필수 항목 표시의 인자 구분 표시                    | { ENABLE \| DISABLE \| COMPILE } <br />[ ENABLE \| DISABLE \| COMPILE ] |
| . . .        | 그 이전 인자의 반복 표시 예제 코드들의 생략되는 것을 표시    | SQL\> SELECT ename FROM employee; <br />ENAME  <br />----------------------- <br />SWNO  <br />HJNO  <br />HSCHOI  <br />. . . <br />20 rows selected. |
| 그 밖에 기호 | 위에서 보여진 기호 이 외에 기호들                            | EXEC :p1 := 1; <br />acc NUMBER(11,2);                       |
| 기울임 꼴    | 구문 요소에서 사용자가 지정해야 하는 변수, 특수한 값을 제공해야만 하는 위치 | SELECT \* FROM *table_name*; <br />CONNECT *userID*/*password*; |
| 소문자       | 사용자가 제공하는 프로그램의 요소들, 예를 들어 테이블 이름, 컬럼 이름, 파일 이름 등 | SELECT ename FROM employee;                                  |
| 대문자       | 시스템에서 제공하는 요소들 또는 구문에 나타나는 키워드       | DESC SYSTEM_.SYS_INDICES_;                                   |

#### 관련 자료

자세한 정보를 위하여 Altibase의 다음 문서 목록을 참조한다.

- Installation Guide
- Getting Started Guide

- Administrator’s Manual

- Replication Manual

- Precompiler User’s Manual

- API User’s Manual

- Altibase C Interface Manual

- iSQL User’s Manual

- Utilities Manual

- General Reference

- Error Message Reference

#### Altibase는 여러분의 의견을 환영합니다.

이 매뉴얼에 대한 여러분의 의견을 보내주시기 바랍니다. 사용자의 의견은 다음 버전의 매뉴얼을 작성하는데 많은 도움이 됩니다. 보내실 때에는 아래 내용과 함께 고객서비스포털(http://support.altibase.com/kr/ )로 보내주시기 바랍니다.

- 사용 중인 매뉴얼의 이름과 버전

- 매뉴얼에 대한 의견

- 사용자의 성함, 주소, 전화번호

이 외에도 Altibase 기술지원 설명서의 오류와 누락된 부분 및 기타 기술적인 문제들에 대해서 이 주소로 보내주시면 정성껏 처리하겠습니다. 또한, 기술적인 부분과 관련하여 즉각적인 도움이 필요한 경우에도 고객서비스포털을 통해 서비스를 요청하시기 바랍니다.

여러분의 의견에 항상 감사드립니다.

<br>

1.dataCompJ 소개
=====================

이 장은 dataCompJ의 특징을 이해하고자 하는 사용자에게 이 도구를 소개하고 설치하는 방법을 설명한다. 이 장은 다음의 절로 구성된다.

- 개요
- 시스템 요구 사항
- 설치 및 제거

### 개요

dataCompJ는 Altibase에서 이기종 데이터베이스로 복제한 데이터를 대상으로 데이터 정합성 확인과 데이터 불일치를 해소하기 위한 도구이다. 테이블 단위로 데이터를 비교하고 데이터 불일치가 있는 경우 이에 관한 정보를 파일로 출력한다. 불일치 데이터를 Slave 데이터베이스에 직접 적용하여 데이터를 일치시키는 기능도 제공한다.

dataCompJ 작업 대상 데이터는 Altibase에서 제공하는 데이터 복제 도구인 Adapter for Oracle 또는 Adapter for JDBC를 사용하여 복제한 데이터를 대상으로 한다.

dataCompJ는 편리한 사용성과 빠른 성능으로, 효율적인 이기종 데이터베이스 간 데이터 관리 방법을 제공한다.

### 시스템 요구 사항

이 절은 dataCompJ를 설치하고 실행하기 위해 필요한 시스템 사양에 대해 설명하고, dataCompJ와 호환되는 데이터베이스 관리 시스템을 열거한다.

#### 하드웨어 요구 사항

- CPU: 800MHz 펜티엄 III 이상
- 메인 메모리: 최소 512MB, 4GB 이상 권장
- 디스크: 50MB 이상의 여유 공간

#### 소프트웨어 요구 사항

- Oracle, OpenJDK 또는 IBM Java 8 이상의 JRE

dataCompJ는 순수 Java 기반 클라이언트 애플리케이션으로 하드웨어 및 운영체제에 상관없이 독립적으로 실행되나, 자바 런타임 환경(JRE)에 의존적이므로 환경에 맞는 JRE를 설치해야 한다. 또한 설치된 Java의 경로를 가리키는 JAVA_HOME 환경변수가 설정되어 있어야 한다.

#### 호환되는 데이터베이스 관리 시스템

##### Master DB

- Altibase: Altibase 5.3.3 이상

##### Slave DB

- Oracle: Oracle 9i 이상
- MariaDB: MariaDB 5.5.x 이상

Master/Slave DB의 의미는 ['용어](#용어)'절을 참조한다.

dataCompJ는 Altibase 및 이기종 데이터베이스들과 함께 사용할 수 있다. 데이터베이스 접속을 위해 JDBC 드라이버를 사용하므로, 원본 데이터베이스와 대상 데이터베이스에 호환되는 JDBC 드라이버를 준비하는 것이 중요하다. 현재 오라클용 JDBC 드라이버인 ojdbc5.jar를 제공한다.

#### 설치 및 제거

dataCompJ는 [Altibase 고객 서비스 포털](#http://support.altibase.com)에서 내려받을 수 있다. dataCompJCli라는 파일 이름으로 zip 또는 tar.gz 파일 형식으로 제공된다. 다운로드받은 압축 파일을 원하는 위치에 해제하면 dataCompJ 설치가 완료된다. 생성된 디렉토리 안에는 실행파일인 dataCompJCli.sh, JDBC 드라이버를 포함한 JDBC 하위 디렉토리 및 XML 기본 설정 파일이 존재한다.
dataCompJ를 제거하기 위해서는 dataCompJ가 설치되어 있는 디렉토리를 삭제한다.

<br>

2.dataCompJ 시작하기
=====================

이 장은 사용자들이 dataCompJ를 좀 더 능률적이고 효율적으로 실행하는 데 도움이 되는 기본 개념을 소개한다. 이 장은 다음의 절로 구성된다.

- 용어

- 불일치 레코드
- 일치 정책

### 용어

##### Master DB

비교 대상인 두 이기종 데이터베이스 중 원본 데이터를 가진 Altibase 데이터베이스이다.

##### Slave DB

비교 대상인 두 이기종 데이터베이스 중 복제된 데이터가 적용되는 다른 벤더의 데이터베이스이다.

##### TablePair

사용자가 지정하는 dataCompJ의 비교 대상을 의미하며 테이블 단위이다. Master DB에 있는 하나의 테이블(Master table)과 Slave DB에 있는 하나의 테이블(Slave table)이 쌍을 이룬다.

##### Master 테이블

TablePair 중 사용자가 지정한 Master DB의 비교 대상 테이블이다.

##### Slave 테이블

TablePair 중 사용자가 지정한 Slave DB의 비교 대상 테이블이다.

### 불일치 레코드(Inconsistent record)

불일치 레코드는 Master 테이블과 Slave 테이블의 주요 키(Primary Key)를 기준으로 컬럼 값이 일치하지 않는 레코드들을 의미한다. 불일치 레코드 종류는 다음과 같이 세 가지 타입이 있다.

##### MOSO 불일치

동일한 주요 키 컬럼들(Primary key columns) 값을 가진 특정 레코드가 Master 테이블과 Slave 테이블에 모두 존재하지만, 주요 키가 아닌 컬럼들(Non primary key columns)의 값이 서로 다른 경우

##### MOSX 불일치

특정 주요 키 컬럼들(Primary key columns) 값을 가진 레코드가 Master 테이블에만 존재하고 Slave 테이블에는 존재하지 않는 경우

##### MXSO 불일치

특정 주요 키 컬럼들(Primary key columns) 값을 가진 레코드가 Master 테이블에는 존재하지 않고 Slave 테이블에만 존재하는 경우

##### 불일치 레코드 처리

1.  DIFF: Master 테이블과 Slave 테이블 간의 불일치 레코드를 식별하여 CSV 형식의 파일에 기록한다.
2.  SYNC: Master 테이블과 Slave 테이블 간의 불일치 레코드를 식별하여 dataCompJ 설정 파일에 기술된 일치 정책에 따라 불일치를 해소한다.

### 일치 정책 (Synchronization policy)

일치 정책은 dataCompJ가 불일치 레코드를 발견하였을 때, Master 테이블의 레코드를 기준으로 Slave 테이블의 레코드를 어떻게 일치시킬지 명시하는 정책이다. 일치 정책으로 다음과 같은 세 가지 방법을 제공한다.

##### MOSO 불일치

UPDATE_TO_SLAVE 정책이다. Master 테이블의 레코드를 기준으로 동일한 주요 키를 가진 Slave 테이블의 레코드를 변경(update)한다.

##### MOSX 불일치

INSERT_TO_SLAVE 정책이다. Master 테이블에만 존재하고 Slave 테이블에는 존재하지 않는 레코드를 Slave 테이블에 삽입(insert)한다.

##### MXSO 불일치

DELETE_FROM_SLAVE 정책이다. Master 테이블에는 존재하지 않고 Slave 테이블에만 존재하는 레코드를 Slave 테이블에서 삭제(delete)한다.

<br>

3.dataCompJ 사용 방법
=====================
이 장은 dataCompJ를 원활하게 실행하는 방법과 dataCompJ의 설정 파일 구성, 설정 시 고려할 점들을 설명한다. 이 장은 다음의 절로 구성된다.

- 실행 방법
- 수행 단계
- 설정 파일 구성

### dataCompJ 실행 방법

dataCompJ를 Command Line Interface (CLI)에서 수행하는 명령어는 다음과 같다.

- Linux

  ```
  $ dataCompJCli.sh -f dataCompJ_env_file_path
  ```


- Windows

  ```
  C:\dataCompJ> dataCompJ.bat -f dataCompJ_env_file_path
  ```

**dataCompJ_env_file_path**

dataCompJ 설정 파일의 경로를 의미하며 필수 옵션이다. dataCompJ 설치 시 dataCompJ.xml 이라는 설정 파일을 제공한다. 사용자는 이 파일을 이용하거나 새로운 이름의 설정 파일을 사용할 수 있다.

### dataCompJ 수행 단계

dataCompJ는 사용자가 설정한 설정 파일을 기반으로 동작하며, 크게 구축(Build)과 실행(Run)이라는 두 단계를 수행한다.

##### 구축(Build) 단계

구축 단계는 주어진 설정 파일을 기반으로 실행(Run) 단계가 수행 가능한지 판단하기 위해 초기 조사하는 단계이다. 하나의 문제라도 발견되면 이를 리포트 파일(dataCompJ_report.txt)에 출력하며 dataCompJ를 종료한다.

구축 단계는 아래의 순서대로 진행된다.

1.  사용자가 지정한 설정 파일을 읽는다.

2.  설정 파일에 기술된 접속정보가 유효한지 확인한다.

3.  설정 파일에 기술된 대상 테이블들의 유효성을 검증하기 위해 양쪽 데이터베이스에 접속하여 메타 정보를 확인한다. 테이블 중 어느 한쪽에서라도 문제를 발견하면 리포트 파일에 출력하고 dataCompJ를 종료한다.

##### 실행(Run) 단계

실행 단계는 대상 테이블들의 데이터를 비교하여, 사용자의 선택에 따라 비교(DIFF) 또는 일치(SYNC) 기능을 수행하는 단계이다.

각 TablePair의 수행 결과는 출력 파일 (dataCompJ_report.txt)에 출력된다.

##### 출력 파일

dataCompJ를 수행하면 텍스트 형식의 리포트 파일 1개, 로그 파일 2개가 생성된다.

비교(DIFF) 기능에 의해 생성되는 출력 파일에 대한 상세한 설명은 '[비교(DIFF) 기능](#비교diff-기능)'을 참고한다.

-   dataCompJ_report.txt: 수행 결과를 정리하여 사용자에게 전달하기 위한 텍스트 형태의 리포트 파일이다.
-   dataCompJ.log: 프로그램 수행 시 발생하는 이벤트를 기록하는 로그 파일이다. 프로그램의 상세 수행 이력을 추적하기 위해 사용하는 파일이다.
-   dataCompJ_data.log: 실행(Run) 단계에서 생성되는 로그 파일로, 사용자가 설정 파일의 \<TraceInconsistentRecord\>를 true로 설정한 경우 비교(DIFF)/일치(SYNC) 수행 시 처리되는 불일치 레코드의 상세 내용을 기록한다.
    불일치 레코드가 많은 경우 대용량의 파일이 생성되고 프로그램의 처리 성능이 저하되기 때문에, 불일치 레코드 처리 내역에 대한 상세 내용이 필요한 경우에만 사용을 권장한다.


### dataCompJ 설정 파일 구성

dataCompJ를 수행하기 위해서는 설정 파일 입력이 필수이다. dataCompJ 설치 시 dataCompJ.xml 라는 파일을 기본 설정 파일로 제공하며, 사용자가 임의의 파일을 작성하여 사용할 수도 있다. 단, dataCompJ.xml에 기술된 XML 규칙에 따라 작성해야 하며 다국어가 포함된 경우 반드시 UTF-8로 인코딩해야 한다.

dataCompJ 설정 파일은 크게 [Connections](#connections), [Options](#options), [TablePairs](#tablepairs) 3개 부분으로 구성된다.

##### Connections

Connections는 Master DB 및 Slave DB에 접속하기 위한 정보를 기록하는 부분이다.

###### \<MasterDB\>

Master DB의 접속 정보를 기록한다. Master DB의 종류는 반드시 Altibase 데이터베이스여야 한다. 아래 XML Element는 Master DB의 하위 요소들이다.

\<JdbcUrl\>  
JDBC 접속에 사용되는 정보로 데이터베이스 사용자 아이디와 암호를 제외한 나머지 정보를 기록하는 문자열이다.

\<JdbcFilePath\>  
Master DB 접속에 사용할 JDBC jar file이 존재하는 경로를 지정한다.

\<UserId\>  
데이터베이스 접속을 위한 사용자 아이디를 지정한다.

\<Password\>  
데이터베이스 접속을 위한 사용자 아이디의 암호를 지정한다.

\<FetchSize\>  
데이터베이스에서 데이터를 가져오는 작업을 할 때, 한번에 가져오는 레코드의 개수를 지정한다. 이 항목은 선택 항목이며, 기본값은 1,000이다.

\<BatchSize\>  
데이터베이스에 INSERT/DELETE/UPDATE와 같은 변경 작업을 수행할 때, 한 번에 수행되는 레코드 개수를 지정한다. 예를 들어 이 항목에 10을 지정하면, 10개 레코드 단위로 INSERT/DELETE/UPDATE를 수행한다. 이 항목은 선택 항목이며, 기본값은 1,000이다.

###### \<SlaveDB\>

Slave DB의 접속 정보를 기록한다. Slave DB의 하위 요소들은 위에서 기술한 [Master DB](#masterdb)의 하위 요소들과 동일하다.

##### Options

Options는 dataCompJ의 수행에 필요한 사용자 설정값을 입력하는 부분이다.

###### \<Operation\>

불일치 데이터 처리를 위한 기능을 지정하는 항목으로 비교(DIFF)나 일치(SYNC) 둘 중 하나의 기능을 선택한다.

###### \<FileEncoding\>

dataCompJ 수행 시 생성되는 파일들의 encoding 타입을 지정한다.

###### \<Diff\>

\<DirPath\>  
비교(DIFF)를 수행하였을 때 비교 대상 테이블별 결과 CSV 파일이 생성되는 디렉토리 경로를 지정한다.

###### \<Sync\>

일치(SYNC) 기능 수행 시 옵션들

\<MOSO UPDATE_TO_SLAVE="true"/\>  
MOSO 불일치 데이터 발견 시 Master 테이블 레코드 기준으로 Slave 테이블의 레코드를 업데이트(Update)할지 여부이다. False를 선택하면 MOSO 불일치 데이터를 처리하지 않는다.

\<MOSX INSERT_TO_SLAVE="true"/\>  
MOSX 불일치 데이터 발견 시 Master 테이블에만 존재하는 레코드를 Slave 테이블에 삽입(Insert)할지 여부이다. False를 선택하면 MOSX 불일치 데이터를 처리하지 않는다.

\<MXSO DELETE_FROM_SLAVE="true"/\>  
MXSO 불일치 데이터 발견 시 Master 테이블에 존재하지 않는 Slave 테이블의 레코드를 삭제(Insert)할지 여부이다. False를 선택하면 MXSO 불일치 데이터를 처리하지 않는다.

###### \<Log\>

아래 XML Element는 Log의 하위 요소들이다.

\<DirPath\>  
dataCompJ 수행 시 생성되는 로그 파일들의 디렉토리 경로를 지정한다.

\<TraceInconsistentRecord\>  
DIFF/SYNC 수행 시 발견되는 모든 불일치 레코드의 상세 내역을 dataCompJ_data.log 파일에 기록할지 여부를 True/False 값으로 결정한다.

###### \<MaxThread\>

dataCompJ에 할당 가능한 최대 쓰레드 개수이다. 0으로 지정하는 경우, dataCompJ가 수행되는 장비의 CPU core 갯수를 MaxThread 값으로 할당한다.

##### TablePairs

TablePairs는 비교 대상 테이블들을 기록하는 부분이다. 비교 대상 테이블에 대한 개별 정보를 기록하는 방법과 일괄적으로 테이블 이름들이 나열되어 있는 텍스트 파일 경로를 지정하는 방법 두 가지를 제공한다. 이 두 가지 방법은 개별로도 사용 가능하며 동시에 사용도 가능하다.

개별 테이블에 대한 정보를 제공하는 방법은 아래와 같으며, 데이터 비교 방법을 상세히 제어할 수 있다는 장점이 있다. 예를 들어, 데이터 비교 시 특정 컬럼을 제외시키거나 특정 조건을 만족하는 데이터들만 비교 대상으로 할 수도 있다.

비교 대상인 테이블 이름은 Master DB와 Slave DB 모두에서 허용하는 이름이어야 한다. XML 파일에 있는 테이블 이름에 공백, 특수문자 등이 있거나 대소문자를 구분해야 하는 경우 큰따옴표(")를 사용한다. 예를 들어, 비교 대상 테이블 이름이 SYS schema의 Employee 01이면, 테이블 이름이 공백을 포함하기 때문에 SYS."Employee 01"처럼 테이블 이름에 큰 따옴표를 사용한다.

###### \<TablePair\>

데이터 비교 대상 단위로 하나의 Master 테이블과 하나의 Slave 테이블로 구성된다. 아래의 XML element는 TablePair의 하위 요소들이다.

\<MasterTable\>  
Master DB에 존재하는 비교 대상 테이블의 이름으로 [*SchemaName*].*TableName* 형식으로 지정한다. 스키마 이름을 별도로 지정하지 않으면 Master DB의 UserId를 기본 스키마 이름으로 사용한다. 이 항목은 필수 항목으로, 기술되지 않으면 프로그램 수행 시 에러가 발생한다.

\<SlaveTable\>  
Slave DB에 존재하는 비교 대상 테이블의 이름으로 [*SchemaName*].*TableName* 형식으로 지정한다. 스키마 이름을 별도로 지정하지 않으면 Slave DB의 UserId를 기본 스키마 이름으로 사용한다. 이 항목은 선택 항목으로, 기술되지 않으면 \<MasterTable\>과 같은 이름으로 간주한다.

\<Exclude\>  
테이블의 레코드를 Projection하는 조건을 지정한다. 쉼표(,)를 구분자로 사용하여 여러 개의 컬럼을 지정할 수 있다. 이 항목은 선택 항목으로, 기술되지 않으면 dataCompJ가 지원하는 데이터 타입을 가진 모든 컬럼들을 비교대상으로 선택한다.

\<Where\>  
테이블의 레코드를 Selection하는 조건을 지정한다. SQL 문의 WHERE 절에 기술하는 방식과 동일하게 기술하며 다중 조건을 허용한다. 단, 양쪽 데이터베이스에 동일하게 적용되므로 양쪽 데이터베이스 문법에 모두 적합해야 한다. 이 항목은 선택 항목으로, 기술되지 않으면 모든 레코드들을 비교 대상으로 한다.

\<TableNameFilePath\>  
일괄적으로 테이블 이름들을 나열한 텍스트 파일 경로를 제공하는 방법은 아래와 같으며, 다수의 테이블들을 일괄적으로 비교해야 하는 경우 테이블 입력을 손쉽게 할 수 있다는 장점이 있다.

```
<TableNameFilePath>table_name_file_path</TableNameFilePath>
```

table_name_file_path는 테이블 이름들을 나열한 텍스트 파일의 경로이다. 비교 대상 테이블의 이름은 [SchemaName].TableName 형식으로 지정할 수 있으며, 각각의 테이블 이름은 개행 문자로 구분한다. MasterDB의 비교 대상 테이블 이름과 SlaveDB의 비교 대상 테이블 이름은 반드시 일치해야 한다.

###### 제약 사항

비교 대상의 테이블을 선택할 때 다음의 제약 사항을 반드시 고려해야 한다. 하나의 제약 사항이라도 위반한 경우, dataCompJ는 구축 단계에서 발생한 문제점을 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행 단계를 수행하지 않는다.

1.  하나의 비교대상 테이블은 Master DB와 Slave DB에 반드시 동일하게 (컬럼 이름, 컬럼 순서, 데이터 타입, 주요 키) 구성되어야 한다. 단, 데이터 타입은 이기종 데이터베이스간 서로 비교 가능한 타입이면 가능하다.

2.  지원하지 않는 데이터 타입의 컬럼은 비교 대상에서 자동으로 제외된다. (예, LOB과 같은 Binary Type)

3.  주요 키(primary key) 외에 값을 비교할 수 있는 컬럼이 적어도 한 개 이상이어야 한다.

    (예제 1) table1 (c1 int, c2 int, c3 CLOB, primary key (c1, c2))  
    (예제 2) table1 (c1 int, c2 int, c3 varchar(100), primary key (c1, c2))  
    예제 1에서 '제약조건 3'을 만족하는 컬럼은 c3 뿐이다. 단, c3 컬럼의 데이터 타입인 CLOB은 dataCompJ가 지원하지 않기 때문에, '제약 사항 2'를 위반한다. 따라서, table1에 대한 비교는 허용되지 않는다.  
    예제 2에서 '제약 사항 3'을 만족하는 컬럼은 c3 뿐이다. 또한, c3의 데이터 타입이 dataCompJ가 지원하는 varchar 타입이기 때문에 table1에 대한 비교가 가능하다.

<br>

4.dataCompJ 기능
=====================

이 장은 dataCompJ의 비교(DIFF) 기능과 일치(SYNC) 기능을 보다 자세히 예제와 함께 설명한다.

- 비교 (DIFF) 기능
- 일치 (SYNC) 기능

### 비교(DIFF) 기능

비교(DIFF) 기능은 Master DB와 Slave DB 간의 이기종 복제 작업에서 발생할 수 있는 불일치 레코드들을 식별하고 이들을 파일에 기록하여, 두 데이터베이스 시스템간의 불일치 레코드들을 확인한다.

#### 설정 파일

dataCompJ 설정파일의 \<Options\> - \<Operation\> 값을 “DIFF”로 지정한다.

\<Connections\>와 \<Options\>의 항목들은 모두 필수로 기입해야 하며, 대상 테이블에 대해 \<TablePairs\>에 기술해야 한다.

##### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
        <JdbcFilePath>./jdbc/Altibase710.jar</JdbcFilePath>
        <UserId>sys</UserId>
        <Password>manager</Password>
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
        <JdbcFilePath>./jdbc/ojdbc5.jar</JdbcFilePath>
        <UserId>altibase</UserId>
        <Password>altibase</Password>
    </SlaveDB>
</Connections>

<Options>
    <Operation>DIFF</Operation>
    <FileEncoding>UTF-8</FileEncoding>
    <Diff>
        <DirPath>./diff/</DirPath>
    </Diff>
    <Sync>
        <MOSO UPDATE_TO_SLAVE="true"/>
        <MOSX INSERT_TO_SLAVE="true"/>
        <MXSO DELETE_FROM_SLAVE="true"/>
    </Sync>
    <Log>
        <DirPath>./</DirPath>
        <TraceInconsistentRecord>false</TraceInconsistentRecord>
    </Log>
    <MaxThread>0</MaxThread>
</Options>

<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### 실행 방법

비교(DIFF)는 다음과 같이 실행한다.

```
$ dataCompJCli.sh -f dataCompJ.xml
```

#### 실행 결과

실행 결과로 수행 결과가 요약된 리포트 파일( dataCompJ_report.txt)과 수행 중 이벤트가 기록되는 로그파일들(dataCompJ.log, dataCompJ_data.log)이 생성된다. 보다 상세한 설명은 [출력 파일](#출력-파일)을 참고한다.

예제에 사용되는 테이블의 구조는 아래와 같다.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int);
```

##### DIFF 수행

```
$ dataCompJCli.sh -f dataCompJ.xml
----------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
----------------------------------------------------------
* Build started  at 2016-12-14 16:30:03.673
* Build finished at 2016-12-14 16:30:04.357 (Elapsed: 0:00:00.691)
* Run   started  at 2016-12-14 16:30:04.374
* Run   finished at 2016-12-14 16:30:04.905 (Elapsed: 0:00:00.531)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.
```

###### 리포트 파일 내용 확인

```
$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 16:30:03.673
     - Finished : 2016-12-14 16:30:04.357
     - Elapsed  : 0:00:00.691
--------------------------------------------------------

[ User input information ]
...

[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
==========================================================
    Run
     - Started  : 2016-12-14 17:19:42.731
     - Finished : 2016-12-14 17:19:42.822
     - Elapsed  : 0:00:00.091
----------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------

```

##### 실행 데이터 파일

비교(DIFF) 기능 선택하였을 때 TablePair 단위로 다음 4개의 CSV 형식의 데이터 파일들이 생성된다.

-   *SchemaName.TableName*\_MASTER_diff.csv:  
    MOSO 불일치 발생 시 Master 테이블의 해당 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_SLAVE_diff.csv:  
    MOSO 불일치 발생 시 Slave 테이블의 해당 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_MASTER_only.csv:  
    MOSX 불일치 발생 시 Master 테이블에만 존재하는 레코드 값을 CSV 형태로 저장하는 파일.

-   *SchemaName.TableName*\_SLAVE_only.csv:  
    MXSO 불일치 발생 시 Slave 테이블에만 존재하는 레코드 값을 CSV 형태로 저장하는 파일.

*SchemaName.TableName*\_MASTER_diff.csv 파일과 *SchemaName.TableName*\_SLAVE_diff.csv 파일에는 MOSO 불일치 데이터가 같은 순서로 기록되기 때문에, DIFF 프로그램으로 두 개의 파일을 비교하면 MOSO 불일치가 발생한 부분을 직관적으로 비교할 수 있다.

#### 예제

예제에 사용되는 테이블의 구조는 아래와 같다.

```
CREATE TABLE ex1 (C1 int primary key, C2 varchar(20), C3 CLOB, C4 int); /* C3 CLOB dataCompJ에서 지원하지 않는 데이터 타입 */
CREATE TABLE ex2 (C1 int primary key, C2 varchar(20), C3 int);
```

##### DIFF 예제 1

두 개의 테이블을 대상으로 스키마 이름을 생략 또는 명시하는 예제이다.

아래의 예제에서 EX1 테이블의 경우 \<MasterTable\>항목은 스키마 이름 없이 테이블 이름만 기술하고, \<SlaveTable\> 항목은 생략했다. 스키마 이름 없이 테이블 이름만 기술한 \<MasterTable\>은 \<MasterDB\>-\<UserId\>에 입력된 값을 스키마 이름으로 사용한다. 생략된 \<SlaveTable\>은 \<MasterTable\>과 같은 값으로 가정하여 처리된다.

EX1 테이블의 C3 컬럼은 dataCompJ가 지원하지 않는 데이터 타입인 CLOB으로 비교 대상에서 자동으로 제외되며, 리포트의 Candidate tables 항목에 이 내용이 기록된다.

EX2 테이블은 스키마 이름과 테이블 이름을 사용자가 명시적으로 입력하였고, 입력받은 스키마 이름과 테이블 이름을 기반으로 처리된다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>DIFF</Operation>
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 2 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns:
===========================================================================
    Run
     - Started  : 2016-12-14 17:56:04.516
     - Finished : 2016-12-14 17:56:04.593
     - Elapsed  : 0:00:00.076
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               7
MOSO    Diff                                  2
MOSX    Master only                           1
MXSO    Slave only                            1
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
```

##### DIFF 예제 2

대상 테이블의 특정 컬럼을 사용자가 명시적으로 제외하고(Exclude), 특정 조건을 만족하는 레코드(Where)만을 대상으로 비교(Diff) 수행하는 예제이다.
dataCompJ.xml에 EX1 테이블에 대해 주요 키가 아닌 컬럼들 중 C4 컬럼을 비교 대상에서 제외하고 C1 컬럼값이 5보다 큰 레코드만 비교 작업을 수행하도록 사용자가 명시적으로 입력한다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
...
<Options>
    <Operation>DIFF</Operation>
...
</Options>
<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
        <Exclude>C4</Exclude>
        <Where>C1 > 5</Where>
    </TablePair>
    <TablePair>
        <MasterTable>SYS.EX2</MasterTable>
        <SlaveTable>ALTIBASE.EX2</SlaveTable>
    </TablePair>     
</TablePairs>
</dataCompJ>

```

###### dataCompJ_report.txt

```
===========================================================================
    Build
     - Started  : 2016-12-14 17:06:53.021
     - Finished : 2016-12-14 17:06:53.679
     - Elapsed  : 0:00:00.669
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 2 ]
1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2 FROM SYS.EX1 WHERE C1 > 5 ORDER BY C1 ASC
    * Excluded columns     : C4
    * Where condition      : C1 > 5
    * N/A data type columns: C3(CLOB)
2: SYS.EX2 -> ALTIBASE.EX2
    * SELECT SQL           : SELECT C1,C2,C3 FROM SYS.EX2 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns:
===========================================================================
    Run
     - Started  : 2016-12-14 17:57:09.895
     - Finished : 2016-12-14 17:57:09.974
     - Elapsed  : 0:00:00.080
---------------------------------------------------------------------------
1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:            5
 Fetched record count from SLAVE :            5
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                               5
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------
2: SYS.EX2 -> ALTIBASE.EX2
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records   
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

### 일치(SYNC) 기능

일치(SYNC)기능은 Master DB와 Slave DB 간의 이기종 복제 작업에서 발생할 수 있는 불일치 레코드들을 식별하여 이를 Slave DB에 적용한다. 두 데이터베이스 시스템의 데이터 동기화(Synchronization)를 손쉽게 할 수 있다.

#### 설정 파일

dataCompJ 설정 파일의 \<Options\> - \<Operation\> 값을 “SYNC”로 지정한다.

\<Connections\>와 \<Options\> 항목들은 모두 필수로 기입해야 하며, 대상 테이블에 대해 \<TablePairs\>에 기술해야 한다.

###### dataCompJ.xml

```
<?xml version="1.0" encoding="UTF-8" ?>
<dataCompJ>
<Connections>
    <MasterDB>
        <JdbcUrl>jdbc:Altibase://192.168.1.94:21135/mydb</JdbcUrl>
...
        <UserId>sys</UserId>
...
    </MasterDB>
    <SlaveDB>
        <JdbcUrl>jdbc:oracle:thin:@//192.168.3.18:1521/xe</JdbcUrl>
...
        <UserId>altibase</UserId>
...
    </SlaveDB>
</Connections>
<Options>
    <Operation>SYNC</Operation>
...
</Options>

<TablePairs>
    <TablePair>
        <MasterTable>EX1</MasterTable>
    </TablePair>      
</TablePairs>
</dataCompJ>
```

#### 실행 방법

일치(SYNC) 기능은 다음과 같이 실행한다.

```
$ dataCompJCli.sh -f dataCompJ.xml
$ dataCompJCli.sh -f ./dataCompJ.xml
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:08:40.407
* Build finished at 2016-12-14 18:08:41.076 (Elapsed: 0:00:00.676)
* Run   started  at 2016-12-14 18:08:41.090
* Run   finished at 2016-12-14 18:08:41.654 (Elapsed: 0:00:00.564)
---------------------------------------------------------------------------
Refer to the following output files for details.
---------------------------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record

```

#### 실행 결과

실행 결과로 수행 결과가 요약된 리포트 파일(dataCompJ_report.txt)과 수행 중 이벤트가 기록되는 로그 파일들(dataCompJ.log, dataCompJ_data.log)이 생성된다. 보다 상세한 설명은 [출력 파일](#출력-파일)을 참고한다.

###### dataCompJ_report.txt

```
$ cat dataCompJ_report.txt
===========================================================================
    Build
     - Started  : 2016-12-14 18:08:40.407
     - Finished : 2016-12-14 18:08:41.076
     - Elapsed  : 0:00:00.676
---------------------------------------------------------------------------

[ User input information ]
...
[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)

===========================================================================
    Run
     - Started  : 2016-12-14 18:08:41.090
     - Finished : 2016-12-14 18:08:41.654
     - Elapsed  : 0:00:00.564
---------------------------------------------------------------------------

1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type    Resolution                Try         Fail
------------------------------------------------------
MOSO    UPDATE TO SLAVE                  2           0
MOSX    INSERT TO SLAVE                  1           0
MXSO    DELETE FROM SLAVE                1           0
------------------------------------------------------
```

모든 대상 테이블과 레코드들에 대해 SYNC가 정확히 수행된 경우, 동일한 대상 테이블에 대해 DIFF 기능을 재수행하면 모든 레코드가 동일하다는 비교 결과를 얻게 된다.

```
$ dataCompJCli.sh -f ./dataCompJ.xml
-----------------------------------------------------------------
     Data Comparison Utility for Java (dataCompJ)
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
* Build started  at 2016-12-14 18:11:54.924
* Build finished at 2016-12-14 18:11:55.561 (Elapsed: 0:00:00.645)
* Run   started  at 2016-12-14 18:11:55.580
* Run   finished at 2016-12-14 18:11:56.190 (Elapsed: 0:00:00.610)
----------------------------------------------------------
Refer to the following output files for details.
----------------------------------------------------------
 - dataCompJ_report.txt: Report file to provide summarized execution result.
 - dataCompJ.log: Log file to keep track of detailed program events during execution.
 - dataCompJ_data.log: Log file to keep track of data events during diff/sync operation as well as different record.

$ cat dataCompJ_report.txt
==========================================================
    Build
     - Started  : 2016-12-14 18:11:54.924
     - Finished : 2016-12-14 18:11:55.561
     - Elapsed  : 0:00:00.645
---------------------------------------------------------

[ User input information ]
...

[ Problematic table(s): 0 ]

[ Candidate table(s) for data comparison: 1 ]

1: SYS.EX1 -> ALTIBASE.EX1
    * SELECT SQL           : SELECT C1,C2,C4 FROM SYS.EX1 ORDER BY C1 ASC
    * Excluded columns     :
    * Where condition      :
    * N/A data type columns: C3(CLOB)

==========================================================
    Run
     - Started  : 2016-12-14 18:11:55.580
     - Finished : 2016-12-14 18:11:56.190
     - Elapsed  : 0:00:00.610
---------------------------------------------------------------------------

1: SYS.EX1 -> ALTIBASE.EX1
 Fetched record count from MASTER:           10
 Fetched record count from SLAVE :           10
------------------------------------------------------
Type                            Records
------------------------------------------------------
MOSO    Matched                              10
MOSO    Diff                                  0
MOSX    Master only                           0
MXSO    Slave only                            0
------------------------------------------------------

```

<br>

# A. 부록: 이기종간 데이터 타입 호환 테이블

dataCompJ가 지원하는 이기종 데이터베이스 간의 데이터 타입 매핑 테이블이다.

dataCompJ가 지원하지 않는 데이터 타입을 가진 테이블을 대상으로 데이터 비교를 수행하면 다음과 같이 처리된다.

-   Master 테이블과 Slave 테이블 모두 dataCompJ가 지원하지 않는 데이터 타입인 경우: 구축(Build) 단계에서 지원하지 않는 데이터 타입이라는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(Run) 단계를 수행하지 않는다.

-   Master 테이블과 Slave 테이블 둘 중 하나만 지원하는 데이터 타입인 경우: 구축(Build) 단계에서 테이블의 비교 대상 컬럼의 개수가 다르다는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(run) 단계를 수행하지 않는다.

dataCompJ가 지원하는 데이터 타입이지만, 비교 대상 테이블의 컬럼 데이터 타입이 이기종간 데이터 타입 호환 테이블과 다른 데이터 타입 조합을 사용하는 경우 다음과 같이 처리된다.

-   데이터 비교 자체가 아예 불가능한 타입의 경우 (예를 들어, 정수형과 문자형 데이터 타입간의 비교): 구축(build) 단계에서 호환되지 않는 타입이라는 에러를 리포트 파일(dataCompJ_report.txt)에 출력하고, 실행(run) 단계를 수행하지 않는다.

-   비교는 가능하지만 상이한 데이터 타입의 경우 (예를 들어, 정수형과 부동 소수점 형): 구축(build) 단계에서 처리할 수 없으므로, 그대로 실행(run) 단계를 수행한다. 단, 수행 결과에 모든 레코드가 불일치 레코드로 처리된다.

#### Altibase to Oracle

| Altibase | Oracle         | 설명                                                         |
| -------- | -------------- | ------------------------------------------------------------ |
| SMALLINT | NUMBER         |                                                              |
| INTEGER  | NUMBER         |                                                              |
| BIGINT   | NUMBER         |                                                              |
| NUMERIC  | NUMBER         |                                                              |
| REAL     | NUMBER         |                                                              |
| DOUBLE   | NUMBER         |                                                              |
| FLOAT    | FLOAT          |                                                              |
| DATE     | DATE TIMESTAMP | - DATE - TIMESTAMP의 경우 소수점의 자릿수가 짧은 쪽을 기준으로 하여 비교한다. 예를 들어 Altibase DATE는 마이크로 초까지 지원하고, Oracle의 TIMESTAMP는 나노 초까지 지원 한다. 이 경우, 레코드의 동일 여부 비교는 나노 초를 기준으로 한다.<br />- DATE-DATE의 경우 Oracle DATE 타입은 YYYY-MM-DD HH:MM:SS까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 소수점 이하의 초는 무시하고 동일한 YYYY-MM-DD HH:MM:SS 형식으로 비교한다. |
| CHAR     | CHAR           |                                                              |
| VARCHAR  | VARCHAR2       |                                                              |
| NCHAR    | NCHAR          |                                                              |
| NVARCHAR | NVARCHAR2      |                                                              |

#### Altibase to MariaDB

| Altibase | MariaDB                                       | 설명                                                         |
| -------- | --------------------------------------------- | ------------------------------------------------------------ |
| SMALLINT | SMALLINT                                      |                                                              |
| INTEGER  | INT                                           |                                                              |
| BIGINT   | BIGINT                                        |                                                              |
| NUMERIC  | DECIMAL                                       |                                                              |
| REAL     | FLOAT                                         |                                                              |
| DOUBLE   | DOUBLE                                        |                                                              |
| FLOAT    | N/A                                           | Altibase Float 타입에 해당하는 MariaDB의 데이터 타입은 없다. |
| DATE     | DATE, DATETIME, TIMESTAMP                     | - DATE-DATE: MariaDB의 DATE는 YYYY-MM-DD까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 날짜 이하는 무시하고 동일한 YYYY-MM-DD 형식으로 비교한다. <br />- DATE-DATETIME: MariaDB의 DATE는 YYYY-MM-DD HH:MM:SS까지 지원한다. 따라서, 이 경우 Altibase DATE 타입의 데이터에서 소수점 이하의 초는 무시하고 동일한 YYYY-MM-DD HH:MM:SS 형식으로 비교한다.<br />- DATE-TIMESTAMP: MariaDB의 DATE는 YYYY-MM-DD HH:MM:DD Microseconds 0 \~ 6 (default: 0)까지 지원한다. 따라서, Altibase DATE 데이터에서 동일한 부분을 추출하여 비교한다. |
| CHAR     | CHAR                                          |                                                              |
| VARCHAR  | VARCHAR, TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT |                                                              |
| NCHAR    | CHAR with Character set                       |                                                              |
| NVARCHAR | VARCHAR with Character set                    |                                                              |
<!-- SOURCE_BLOCK_END source_id="SRC-000213" block_id="BLOCK-000941" -->


---
번호: 8
기능명: 블라인드 프로필 공개
담당: 양수현
요구사항: requirements/req-08.md
---

# seq-08 블라인드프로필공개

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 블라인드프로필공개 | 담당 객체 | classes/BlindProfileDisclosure.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **사람이 누름** (같은 테이블 출석 학생이 '정보 공개' 선택) → `학생UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 학생UI as 학생UI
    participant 공개 as 블라인드프로필공개
    participant 현황 as 테이블출석현황
    participant 배치DB as 배치DB
    participant 출석DB as 출석DB
    participant 프로필DB as 프로필DB

    학생UI->>+공개: 1: 정보공개동의(학생ID: int, 모임ID: int, 테이블번호: int, 현재단계: int)
    공개->>+현황: 2: 테이블출석인원조회(모임ID: int, 테이블번호: int): int
    현황->>출석DB: 3: 테이블출석조회(모임ID: int, 테이블번호: int): List<int>
    출석DB-->>현황: 테이블출석학생목록
    현황-->>-공개: 테이블출석인원

    공개->>공개: 4: 동의기록및집계(학생ID: int, 현재단계: int): int
    공개-)학생UI: 5: 동의현황표시(동의수: int, 출석인원: int)

    alt 전원 동의 완료
        공개->>프로필DB: 6: 단계별프로필항목조회(학생ID목록: List<int>, 단계: int): List<String>
        프로필DB-->>공개: 프로필항목목록
        공개-)학생UI: 7: 프로필항목공개표시(단계: int, 항목목록: List<String>)

        alt 3단계 완료
            Note over 공개: 처리를 종료한다
        else 다음 단계 진행 가능
            공개->>공개: 8: 동의상태초기화(테이블번호: int)
        end
    else 전원 미동의
        Note over 공개: 현재 단계에서 다른 학생의 동의를 대기
    end
    deactivate 공개
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~5 | 1 |
| 6~7 | 2 |
| 8 | 3 |

## 메모

- 2번 테이블출석인원조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 6번의 프로필 항목은 1단계 MBTI, 2단계 학과, 3단계 학번 순이다.
- 8번으로 현재 단계의 동의 상태가 초기화되고 다음 단계로 진행된다.


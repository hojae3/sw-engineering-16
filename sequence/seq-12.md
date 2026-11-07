---
번호: 12
기능명: 비매너 학생 신고
담당: 최성민
요구사항: requirements/req-12.md
---

# seq-12 비매너학생신고

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 비매너학생신고 | 담당 객체 | classes/MannerReport.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 신고DB | DB | classes/ReportDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 앱운영자 | 액터 | |

시작 방식: **사람이 누름** (학생이 '비매너 학생 신고'를 선택) → `학생UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 학생UI as 학생UI
    participant 신고 as 비매너학생신고
    participant 현황 as 테이블출석현황
    participant 프로필DB as 프로필DB
    participant 신고DB as 신고DB
    actor 앱운영자

    학생UI->>+신고: 1: 비매너학생신고선택(학생ID: int, 모임ID: int)
    신고->>+현황: 2: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
    현황-->>-신고: 같은테이블출석학생목록
    loop 대상 학생마다
        신고->>프로필DB: 3: 프로필사진조회(학생ID: int): String
        프로필DB-->>신고: 프로필사진
    end
    신고-)학생UI: 4: 신고대상목록표시(대상학생목록: List<int>, 프로필사진목록: List<String>)

    alt 건너뛰기 선택
        학생UI->>신고: 5: 신고건너뛰기선택(학생ID: int)
        신고-)학생UI: 6: 신고생략알림(학생ID: int)
        Note over 신고: 처리를 종료한다
    else 신고대상 선택
        학생UI->>신고: 7: 신고하기선택(신고학생ID: int, 피신고학생ID: int)
        신고-)학생UI: 8: 신고작성창표시(피신고학생ID: int)
        학생UI->>신고: 9: 신고제출(신고학생ID: int, 피신고학생ID: int, 모임ID: int, 신고사유: String, 상세내용: String)
        신고->>신고: 10: 입력값검증(신고사유: String, 상세내용: String): boolean

        alt 입력값 유효하지 않음
            신고-)학생UI: 11: 입력오류알림(학생ID: int)
            Note over 신고: 처리를 종료한다
        else 입력값 유효
            신고->>신고DB: 12: 신고저장(신고학생ID: int, 피신고학생ID: int, 모임ID: int, 신고사유: String, 상세내용: String): int
            신고DB-->>신고: 신고ID
            신고-)앱운영자: 13: 신고접수알림(신고ID: int, 모임ID: int)
            신고-)학생UI: 14: 신고접수완료알림(학생ID: int)
        end
    end
    deactivate 신고
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~4 | 1 |
| 5~6 | 2 |
| 7~8 | 3, 4 |
| 9 | 5 |
| 10~14 | 6 |

## 메모

- 2번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 10번 입력값검증은 사유 선택 여부 및 내용 길이 제한을 검증한다.
- 12번 신고저장 후 생성된 신고ID를 바탕으로 앱운영자에게 신고 접수 통보가 전달된다.
- 4, 6, 8, 11, 13, 14번 알림은 비동기로 전송된다.

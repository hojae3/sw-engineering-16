---
번호: 1
기능명: 모임공지등록
담당: 양수현
요구사항: requirements/req-01.md
---

# seq-01 모임공지등록

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 모임공지등록 | 담당 객체 | classes/MeetingNoticeRegistration.md |
| 가게DB | DB | classes/StoreDB.md |
| 모임DB | DB | classes/MeetingDB.md |
| 사장님UI | UI | classes/OwnerUI.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **사람이 누름** (사장님이 '모임공지등록'을 선택) → `사장님UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 사장님UI as 사장님UI
    participant 등록 as 모임공지등록
    participant 가게DB as 가게DB
    participant 모임DB as 모임DB
    participant 학생UI as 학생UI

    사장님UI->>+등록: 1: 모임공지등록요청(사장님ID: int, 가게ID: int, 모임이름: String, 시작시각: datetime, 모임종료시각: datetime, 모집정원: int, 기본참가비: int, 품앗이참여여부: boolean, 요청식별자: String)
    등록->>가게DB: 2: 가게등록여부조회(사장님ID: int, 가게ID: int): boolean
    가게DB-->>등록: 등록여부

    alt 일치하는 가게 없음
        등록-)사장님UI: 3: 등록실패알림(사유: String)
        Note over 등록: 처리를 종료한다
    else 일치하는 가게 있음
        등록->>등록: 4: 입력값검증(모집정원: int, 기본참가비: int, 시작시각: datetime, 모임종료시각: datetime): boolean

        alt 검증 조건 불만족
            등록-)사장님UI: 5: 등록실패알림(사유: String)
            Note over 등록: 처리를 종료한다
        else 검증 조건 만족
            등록->>모임DB: 6: 중복요청조회(요청식별자: String): boolean
            모임DB-->>등록: 중복여부

            alt 이미 등록된 요청
                등록-)사장님UI: 7: 기존공지반환(요청식별자: String)
                Note over 등록: 처리를 종료한다
            else 신규 요청
                등록->>모임DB: 8: 모임공지저장(가게ID: int, 모임이름: String, 시작시각: datetime, 모임종료시각: datetime, 모집정원: int, 기본참가비: int, 품앗이참여여부: boolean, 요청식별자: String): int
                모임DB-->>등록: 모임ID
                등록-)사장님UI: 9: 모임공지반환(모임ID: int)
                등록-)학생UI: 10: 모임공지목록갱신(모임ID: int)
            end
        end
    end
    deactivate 등록
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1 | 1 |
| 2~3 | 2 |
| 4~5 | 3, 4, 5, 6 |
| 6~7 | 7 |
| 8 | 8 |
| 9~10 | 9 |

## 메모

- 4번 입력값검증은 정원 12명 이상 4의 배수, 기본참가비 0원 초과, 종료 시각이 시작 시각보다 늦음, 신청 마감 시각(전날 18:00)이 현재보다 늦음을 종합 검증한다.
- 8번 모임공지저장 시 모임 상태는 '모집중'으로 기본 설정된다.


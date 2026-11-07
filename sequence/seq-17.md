---
번호: 17
기능명: 가게 연합 음식 품앗이
담당: 설혜원
요구사항: requirements/req-17.md
---

# seq-17 가게연합음식품앗이

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 가게연합음식품앗이 | 담당 객체 | classes/StoreFoodExchange.md |
| 모임DB | DB | classes/MeetingDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 주문DB | DB | classes/OrderDB.md |
| 품앗이DB | DB | classes/FoodExchangeDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 사장님UI | UI | classes/OwnerUI.md |

시작 방식: **사람이 누름** (출석한 학생이 음식 교환을 등록) → `학생UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 학생UI as 학생UI
    participant 품앗이 as 가게연합음식품앗이
    participant 모임DB as 모임DB
    participant 출석DB as 출석DB
    participant 주문DB as 주문DB
    participant 품앗이DB as 품앗이DB
    participant 사장님UI as 사장님UI

    학생UI->>+품앗이: 1: 음식품앗이등록(학생ID: int, 모임ID: int, 상대모임ID: int, 상대학생ID: int, 음식명: String, 수량: int)
    품앗이->>모임DB: 2: 모임상태조회(모임ID: int): 모임상태
    모임DB-->>품앗이: 모임상태
    품앗이->>출석DB: 3: 출석여부조회(학생ID: int, 모임ID: int): boolean
    출석DB-->>품앗이: 출석여부
    품앗이->>주문DB: 4: 주문잔량조회(모임ID: int, 음식명: String): int
    주문DB-->>품앗이: 주문잔량
    품앗이->>품앗이DB: 5: 연합가능여부조회(모임ID: int, 상대모임ID: int): boolean
    품앗이DB-->>품앗이: 연합가능여부

    alt 검증 실패 (진행중 아님 / 미출석 / 잔량 부족 / 연합 불가)
        품앗이-)학생UI: 6: 검증실패알림(학생ID: int, 사유: String)
        Note over 품앗이: 처리를 종료한다
    else 검증 통과
        품앗이->>품앗이DB: 7: 교환요청저장(모임ID: int, 상대모임ID: int, 학생ID: int, 음식명: String, 수량: int): int
        품앗이DB-->>품앗이: 교환ID
        품앗이-)학생UI: 8: 교환요청전달(상대학생ID: int, 교환ID: int, 음식명: String, 수량: int)

        alt 상대 학생 거절 또는 기한 만료
            학생UI->>품앗이: 9: 교환거절선택(교환ID: int)
            품앗이->>품앗이DB: 10: 교환상태갱신(교환ID: int, 상태: 교환상태.취소)
            품앗이-)학생UI: 11: 교환취소알림(학생ID: int)
            Note over 품앗이: 처리를 종료한다
        else 상대 학생 수락
            학생UI->>품앗이: 12: 교환수락선택(교환ID: int)
            품앗이->>품앗이DB: 13: 교환상태갱신(교환ID: int, 상태: 교환상태.교환확정)
            품앗이-)사장님UI: 14: 교환확정알림(교환ID: int)
            품앗이-)학생UI: 15: 교환확정알림(교환ID: int)

            학생UI->>품앗이: 16: 수령확인선택(학생ID: int, 교환ID: int)
            품앗이->>품앗이DB: 17: 수령확인저장(학생ID: int, 교환ID: int): boolean
            품앗이DB-->>품앗이: 전원수령확인여부

            alt 양쪽 학생 전원 수령 확인
                품앗이->>품앗이DB: 18: 교환상태갱신(교환ID: int, 상태: 교환상태.교환완료)
                품앗이-)학생UI: 19: 품앗이완료알림(교환ID: int)
            else 한쪽 학생만 수령 확인
                Note over 품앗이: 상대 학생의 수령 확인을 대기한다
            end
        end
    end
    deactivate 품앗이
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1 | 1 |
| 2~5 | 2 |
| 6~8 | 3 |
| 9~15 | 4 |
| 16~19 | 5 |

## 메모

- 2~5번의 검증 조건(모임 진행중, 본인 출석, 주문 잔량 충족, 모임 간 연합 가능 조건) 중 하나라도 실패하면 6번으로 즉시 종료된다.
- 13번으로 교환확정 상태가 되면 양쪽 가게 사장님UI(14번) 및 학생UI(15번)에 알림이 전송된다.
- 17번 수령확인은 양쪽 학생이 모두 눌러 전원 확인이 true가 될 때만 18번 교환완료로 갱신된다.
- 6, 8, 11, 14, 15, 19번 알림은 비동기로 전송된다.

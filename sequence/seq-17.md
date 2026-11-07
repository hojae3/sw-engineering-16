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

    학생UI->>+품앗이: 1: 음식품앗이등록제출(학생ID: int, 모임ID: int, 상대모임ID: int, 상대학생ID: int, 음식명: String, 수량: int)
    품앗이->>모임DB: 2: 모임상태조회(모임ID: int): 모임상태
    모임DB-->>품앗이: 모임상태
    품앗이->>출석DB: 3: 출석여부조회(학생ID: int, 모임ID: int): boolean
    출석DB-->>품앗이: 출석여부
    품앗이->>출석DB: 4: 출석여부조회(학생ID: int, 모임ID: int): boolean
    출석DB-->>품앗이: 상대출석여부
    품앗이->>주문DB: 5: 주문잔량조회(모임ID: int, 음식명: String): int
    주문DB-->>품앗이: 주문잔량
    품앗이->>품앗이DB: 6: 취소제외교환수량조회(모임ID: int, 음식명: String): int
    품앗이DB-->>품앗이: 취소제외교환수량
    품앗이->>품앗이DB: 7: 연합가능여부조회(모임ID: int, 상대모임ID: int): boolean
    품앗이DB-->>품앗이: 연합가능여부

    alt 검증 실패 (진행중 아님 / 미출석 / 잔량 부족 / 연합 불가)
        품앗이-)학생UI: 8: 검증실패알림(학생ID: int, 사유: String)
        Note over 품앗이: 처리를 종료한다
    else 검증 통과
        품앗이->>품앗이DB: 9: 교환요청저장(모임ID: int, 상대모임ID: int, 학생ID: int, 상대학생ID: int, 음식명: String, 수량: int): int
        품앗이DB-->>품앗이: 교환ID
        품앗이-)학생UI: 10: 교환요청전달(상대학생ID: int, 교환ID: int, 음식명: String, 수량: int)

        alt 상대 학생 거절
            학생UI->>품앗이: 11: 교환거절선택(교환ID: int)
            품앗이->>품앗이DB: 12: 교환상태갱신(교환ID: int, 상태: 교환상태)
            Note over 품앗이: 12번은 '취소'로 바꾼다
            loop 양쪽 학생마다
                품앗이-)학생UI: 13: 교환취소알림(학생ID: int, 교환ID: int)
            end
            loop 양쪽 가게마다
                품앗이-)사장님UI: 14: 교환취소알림(모임ID: int, 교환ID: int)
            end
            Note over 품앗이: 처리를 종료한다
        else 10분 안에 응답 없음
            Note over 품앗이: ⏱ 10분 경과 후
            품앗이->>품앗이DB: 15: 교환상태갱신(교환ID: int, 상태: 교환상태)
            Note over 품앗이: 15번은 '취소'로 바꾼다
            loop 양쪽 학생마다
                품앗이-)학생UI: 16: 교환취소알림(학생ID: int, 교환ID: int)
            end
            loop 양쪽 가게마다
                품앗이-)사장님UI: 17: 교환취소알림(모임ID: int, 교환ID: int)
            end
            Note over 품앗이: 처리를 종료한다
        else 상대 학생 수락
            학생UI->>품앗이: 18: 교환수락선택(교환ID: int)
            품앗이->>품앗이DB: 19: 교환상태갱신(교환ID: int, 상태: 교환상태)
            Note over 품앗이: 19번은 '교환확정'으로 바꾼다
            loop 양쪽 학생마다
                품앗이-)학생UI: 20: 교환확정알림(학생ID: int, 교환ID: int)
            end
            loop 양쪽 가게마다
                품앗이-)사장님UI: 21: 교환확정알림(모임ID: int, 교환ID: int)
            end

            loop 양쪽 학생이 수령 확인을 누를 때마다
                학생UI->>품앗이: 22: 수령확인선택(학생ID: int, 교환ID: int)
                품앗이->>품앗이DB: 23: 교환상태조회(교환ID: int): 교환상태
                품앗이DB-->>품앗이: 교환상태
                alt 교환 상태가 '교환확정'이 아님
                    Note over 품앗이: 수령 확인을 기록하지 않는다
                else 교환 상태가 '교환확정'임
                    품앗이->>품앗이DB: 24: 수령확인저장(학생ID: int, 교환ID: int)
                    품앗이->>품앗이DB: 25: 전원수령확인여부조회(교환ID: int): boolean
                    품앗이DB-->>품앗이: 전원수령확인여부
                    alt 두 학생 모두 확인
                        품앗이->>품앗이DB: 26: 교환상태갱신(교환ID: int, 상태: 교환상태)
                        Note over 품앗이: 26번은 '교환완료'로 바꾼다
                        loop 양쪽 학생마다
                            품앗이-)학생UI: 27: 품앗이완료알림(학생ID: int, 교환ID: int)
                        end
                        loop 양쪽 가게마다
                            품앗이-)사장님UI: 28: 품앗이완료알림(모임ID: int, 교환ID: int)
                        end
                    else 한 학생만 확인
                        Note over 품앗이: '교환확정'으로 두고 다른 학생의 확인을 기다린다
                    end
                end
            end
        end
    end
    deactivate 품앗이
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1 | 1 |
| 2~7 | 2 |
| 8~10 | 3 |
| 11~21 | 4 |
| 22~28 | 5 |

## 메모

- 3번은 등록한 학생, 4번은 상대 학생과 상대 모임의 출석을 확인한다.
- 6번은 교환 상태가 '취소'가 아닌 교환의 수량을 돌려준다. 주문DB의 잔량은 교환으로 줄지 않으므로 '교환완료' 수량도 포함한다.
- 2~7번의 검증 조건 중 하나라도 실패하면 8번으로 즉시 종료된다.
- 9번은 뒤의 메시지에서 쓸 교환ID를 돌려받는다.
- 14, 17, 21, 28번의 모임ID는 양쪽 가게의 사장님UI를 구분하는 값이다.
- 24번은 양쪽 학생이 각각 저장하고, 25번이 true일 때만 26번으로 교환완료로 갱신된다.
- 8, 10, 13, 14, 16, 17, 20, 21, 27, 28번 알림은 비동기로 전송된다.

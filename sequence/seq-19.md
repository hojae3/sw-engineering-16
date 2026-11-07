---
번호: 19
기능명: 모임 다음 날 숙취 예보
담당: 설혜원
요구사항: requirements/req-19.md
---

# seq-19 모임다음날숙취예보

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 숙취예보 | 담당 객체 | classes/HangoverForecast.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 모임DB | DB | classes/MeetingDB.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 주문DB | DB | classes/OrderDB.md |
| 가게DB | DB | classes/StoreDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **정해진 시각** (다음 날 08:00 도달) → `시간` 액터

## 다이어그램

```mermaid
sequenceDiagram
    actor 시간
    participant 예보 as 숙취예보
    participant 현황 as 테이블출석현황
    participant 모임DB as 모임DB
    participant 배치DB as 배치DB
    participant 주문DB as 주문DB
    participant 가게DB as 가게DB
    participant 학생UI as 학생UI

    시간->>+예보: 1: 익일08시도달()
    예보->>모임DB: 2: 전일종료모임목록조회(): List<int>
    모임DB-->>예보: 전일종료모임목록

    alt 전날 종료된 모임 없음
        Note over 예보: 아무것도 하지 않고 종료한다
    else 전날 종료된 모임 있음
        loop 종료 모임마다
            예보->>모임DB: 3: 모임종료시각조회(모임ID: int): datetime
            모임DB-->>예보: 모임종료시각
            예보->>배치DB: 4: 테이블목록조회(모임ID: int): List<int>
            배치DB-->>예보: 테이블목록
            loop 테이블마다
                예보->>+현황: 5: 테이블출석학생목록조회(모임ID: int, 테이블번호: int): List<int>
                현황-->>-예보: 테이블출석학생목록
                예보->>+현황: 6: 테이블출석인원조회(모임ID: int, 테이블번호: int): int
                현황-->>-예보: 테이블출석인원
                alt 출석 인원 0명
                    Note over 예보: 해당 테이블 제외
                else 출석 인원 1명 이상
                    예보->>주문DB: 7: 테이블술주문병수조회(모임ID: int, 테이블번호: int): int
                    주문DB-->>예보: 테이블술주문병수
                    예보->>예보: 8: 숙취지수계산(술주문병수: int, 출석인원: int, 모임종료시각: datetime): int
                    alt 숙취지수 2단계 이상
                        예보->>가게DB: 9: 제휴쿠폰조회(모임ID: int): String
                        가게DB-->>예보: 제휴쿠폰
                        alt 제휴 쿠폰 있음
                            loop 출석 학생마다
                                예보-)학생UI: 10: 숙취예보및쿠폰알림(학생ID: int, 숙취지수: int, 쿠폰: String)
                            end
                        else 제휴 쿠폰 없음
                            loop 출석 학생마다
                                예보-)학생UI: 11: 숙취예보알림(학생ID: int, 숙취지수: int)
                            end
                        end
                    else 숙취지수 2단계 미만
                        loop 출석 학생마다
                            예보-)학생UI: 12: 숙취예보알림(학생ID: int, 숙취지수: int)
                        end
                    end
                end
            end
        end
    end
    deactivate 예보
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~3 | 1 |
| 4~6 | 2 |
| 7~8 | 3 |
| 9~11 | 4 |
| 12 | 5 |

## 메모

- 1번 시작 메시지는 매일 08:00에 발생하는 시간 사건이다.
- 3번 모임종료시각조회는 모임DB의 기존 연산을 재사용한다.
- 5번과 6번은 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 8번 숙취 지수는 (술 주문 병 수 ÷ 출석 인원 ÷ 2)의 소수점 아래를 버린 값에, 모임 종료 시각이 23시 이후이면 1을 더해 최대 3단계로 산출된다.
- 9번 제휴 쿠폰은 쿠폰 내용을 String으로 돌려받고, 등록된 쿠폰이 없으면 빈 값이다.
- 10, 11, 12번 알림은 비동기 푸시 알림으로 전송되며, 지수가 진단 수치가 아니라는 문구를 포함한다.

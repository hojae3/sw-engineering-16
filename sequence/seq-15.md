---
번호: 15
기능명: 당일 안심귀가
담당: 최성민
요구사항: requirements/req-15.md
---

# seq-15 당일안심귀가

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 당일안심귀가 | 담당 객체 | classes/SafeReturnHome.md |
| 귀가시간계산 | 공통 객체 | classes/ReturnHomeTimeCalc.md |
| 모임DB | DB | classes/MeetingDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 단말기위치정보 | 외부 | classes/DeviceLocation.md |
| 학생UI | UI | classes/StudentUI.md |
| 앱운영자 | 액터 | |

시작 방식: **데이터 변화** (모임DB의 모임 상태가 '종료'로 변경됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 안심 as 당일안심귀가
    participant 계산 as 귀가시간계산
    participant 위치 as 단말기위치정보
    participant 모임DB as 모임DB
    participant 출석DB as 출석DB
    participant 프로필DB as 프로필DB
    participant 학생UI as 학생UI
    actor 앱운영자

    Found->>+안심: 1: 모임종료저장됨(모임ID: int)
    안심->>모임DB: 2: 모임종료시각조회(모임ID: int): datetime
    모임DB-->>안심: 모임종료시각
    안심->>출석DB: 3: 출석학생조회(모임ID: int): List<int>
    출석DB-->>안심: 출석학생목록

    loop 출석 학생마다
        안심->>+계산: 4: 이동시간추정(학생ID: int): int
        계산->>위치: 5: 현재위치조회(학생ID: int): Point
        위치-->>계산: 현재위치
        계산->>프로필DB: 6: 자택위치조회(학생ID: int): Point
        프로필DB-->>계산: 자택위치
        계산->>계산: 7: 이동시간계산(현재위치: Point, 자택위치: Point): int
        계산-->>-안심: 추정이동시간

        alt 위치 확인 불가 (추정이동시간 == -1)
            안심-)학생UI: 8: 메시지알림(수신자ID: int, 메시지: String)
            Note over 안심: 해당 학생 안심귀가 처리 종료
        else 정상 위치 확인 (추정이동시간 != -1)
            안심->>안심: 9: 귀가마감시각계산(모임종료시각: datetime, 추정이동시간: int): datetime
            안심-)학생UI: 10: 귀가모니터링시작알림(학생ID: int, 귀가마감시각: datetime)

            alt 자택 반경 100m 이내 진입 감지
                안심-)학생UI: 11: 메시지알림(수신자ID: int, 메시지: String)
                Note over 안심: 위치 확인 정상 종료
            else 귀가 마감 시각까지 미진입
                안심-)학생UI: 12: 안전확인요청알림(학생ID: int)
                alt 10분 내 안전 응답
                    학생UI->>안심: 13: 안전응답선택(학생ID: int)
                    Note over 안심: 위치 확인 정상 종료
                else 10분 내 미응답
                    안심->>프로필DB: 14: 학생비상연락정보조회(학생ID: int): 학생비상연락정보
                    프로필DB-->>안심: 학생비상연락정보
                    안심-)앱운영자: 15: 긴급문자발송(이름: String, 학번: String, 비상연락처: String)
                end
            end
        end
    end
    deactivate 안심
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~3 | 1 |
| 4~7 | 1, 3, 4, 5 |
| 8 | 2 |
| 9~10 | 6 |
| 11 | 7 |
| 12~15 | 8 |

## 메모

- 1번 시작 메시지는 '9. 자동 정산'에서 모임 상태가 '종료'로 저장될 때 발생하는 Found Message다.
- 4번 이동시간추정은 20번과 공유하는 공통 객체 귀가시간계산의 표준 연산(GLOSSARY 5장)이다. 단말기 위치 정보를 얻지 못하면 -1을 돌려준다.
- 8번 위치확인불가알림은 단말기 위치 정보를 얻지 못했을 때(추정이동시간 == -1) 학생UI에 알리고 모니터링 대상에서 제외하는 Action 2의 예외 처리다.
- 9번 귀가 마감 시각은 모임 종료 시각 + 추정 이동 시간 + 30분(여유 버퍼)으로 계산된다.
- 12번 확인 요청 후 10분 타이머가 동작하며, 미응답 시 비상 연락처를 포함한 SMS 외부 서비스 호출(15번)이 발생한다.
- 8, 10, 11, 12, 15번 알림·문자는 비동기로 발송된다.
- 8, 11번은 화면에 잠깐 보여 주고 끝나는 알림이라 메시지알림으로 보낸다 (FEEDBACK #25). 메시지는 8번 위치확인불가, 11번 안전귀가 안내이고, 원래 넘기던 값(사유, 금액 등)은 메시지 문장에 담는다.

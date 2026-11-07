---
번호: 20
기능명: 2차 참가 자동 결정
담당: 김호재
요구사항: requirements/req-20.md
---

# seq-20 2차참가자동결정

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 2차참가자동결정 | 담당 객체 | classes/SecondRoundAutoDecision.md |
| 귀가시간계산 | 공통 객체 | classes/ReturnHomeTimeCalc.md |
| 2차공지DB | DB | classes/SecondNoticeDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 2차기록DB | DB | classes/SecondRecordDB.md |
| 단말기위치정보 | 외부 | classes/DeviceLocation.md |
| 학생UI | UI | classes/StudentUI.md |
| 사장님UI | UI | classes/OwnerUI.md |

시작 방식: **데이터 변화** (2차공지DB에 2차 공지가 등록됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 결정 as 2차참가자동결정
    participant 귀가 as 귀가시간계산
    participant 공지DB as 2차공지DB
    participant 출석DB as 출석DB
    participant 프로필DB as 프로필DB
    participant 기록DB as 2차기록DB
    participant 위치 as 단말기위치정보
    participant 학생UI as 학생UI
    participant 사장님UI as 사장님UI

    Found->>+결정: 1: 2차공지등록됨(모임ID: int)
    결정->>공지DB: 2: 2차공지조회(모임ID: int): 2차공지
    공지DB-->>결정: 2차공지
    결정->>출석DB: 3: 출석학생조회(모임ID: int): List<int>
    출석DB-->>결정: 출석학생목록

    alt 출석 학생 없음
        결정-)사장님UI: 4: 알림대상없음알림(모임ID: int)
        Note over 결정: 처리를 종료한다
    else 출석 학생 있음
        결정-)학생UI: 5: 참가선택요청(학생ID목록: List<int>, 2차장소: String, 시작시각: datetime)
        loop 10분 동안 응답마다
            학생UI->>결정: 6: 참가응답제출(학생ID: int, 선택: 참가선택)
        end
        Note over 결정: ⏱ 10분 경과 후
        결정->>결정: 7: 응답별결정(응답목록: List<참가응답>)
        결정->>결정: 8: 참가비율계산(참가수: int, 알림수: int): double

        loop '고민' 학생마다
            결정->>+귀가: 9: 이동시간추정(학생ID: int): int
            귀가->>위치: 10: 현재위치조회(학생ID: int): Point
            위치-->>귀가: 현재위치
            귀가->>프로필DB: 11: 자택위치조회(학생ID: int): Point
            프로필DB-->>귀가: 자택위치
            귀가->>귀가: 12: 이동시간계산(현재위치: Point, 자택위치: Point): int
            귀가-->>-결정: 추정이동시간

            alt 위치 없음 (추정이동시간 -1)
                결정->>결정: 13: 불참결정(학생ID: int)
            else 다음 날 00:00 − 추정이동시간 − 현재시각이 90분 미만
                결정->>결정: 14: 불참결정(학생ID: int)
            else 90분 이상
                결정->>기록DB: 15: 과거참가기록조회(학생ID: int): 참가기록
                기록DB-->>결정: 참가기록
                결정->>결정: 16: 참가여부결정(과거2차참가율: double, 이번참가비율: double): 2차참가결과
            end
        end

        결정->>기록DB: 17: 결과저장(모임ID: int, 결과목록: List<참가결과>)
        결정-)학생UI: 18: 결과알림(학생ID: int, 결과: 2차참가결과)
        결정-)사장님UI: 19: 참가인원알림(모임ID: int, 참가인원: int)
    end
    deactivate 결정
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~4 | 1 |
| 5~6 | 2 |
| 7~8 | 3 |
| 9~14 | 4 |
| 15~16 | 5 |
| 17~19 | 6 |

## 메모

- 4번 알림대상없음알림은 출석한 학생이 없을 때 사장님UI에 알리고 처리를 종료하는 Action 1의 예외 종료 동작이다.
- 귀가시간계산은 15. 당일 안심귀가와 같이 쓰는 공통 객체다.
- 이동시간계산은 하버사인 공식으로 직선거리 d를 계산하고, 도로 굴곡 계수 1.3을 곱해 D를 구한 뒤 1.5km 이하는 도보(4km/h), 초과는 차량(25km/h)으로 계산한다.
- 추정이동시간은 위치를 얻지 못하면 -1을 돌려준다. 위치 권한 동의는 Pre-condition에서 전제한다.

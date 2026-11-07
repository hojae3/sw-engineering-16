---
번호: 16
기능명: 기부 릴레이 잇기
담당: 설혜원
요구사항: requirements/req-16.md
---

# seq-16 기부릴레이잇기

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 기부릴레이잇기 | 담당 객체 | classes/DonationRelay.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 기부DB | DB | classes/DonationDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 앱운영자 | 액터 | |

시작 방식: **데이터 변화** (배치DB에 해당 모임의 최종배치가 저장됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 릴레이 as 기부릴레이잇기
    participant 현황 as 테이블출석현황
    participant 배치DB as 배치DB
    participant 기부DB as 기부DB
    participant 출석DB as 출석DB
    participant 학생UI as 학생UI
    actor 앱운영자

    Found->>+릴레이: 1: 최종배치저장됨(모임ID: int)
    릴레이->>배치DB: 2: 배치조회(모임ID: int): List<int>
    배치DB-->>릴레이: 배정학생목록
    loop 배정 학생마다
        릴레이->>기부DB: 3: 바통보유여부조회(학생ID: int): boolean
        기부DB-->>릴레이: 바통보유여부
        릴레이->>출석DB: 4: 출석여부조회(학생ID: int, 모임ID: int): boolean
        출석DB-->>릴레이: 출석여부
        alt 바통 보유 및 출석 확인
            릴레이-)학생UI: 5: 릴레이잇기버튼활성화(학생ID: int)
        else 조건 미충족
            릴레이-)학생UI: 6: 릴레이잇기버튼비활성화(학생ID: int)
        end
    end

    학생UI->>릴레이: 7: 릴레이잇기선택(학생ID: int, 모임ID: int)
    릴레이->>+현황: 8: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
    현황-->>-릴레이: 같은테이블출석학생목록
    loop 같은 테이블 출석 학생마다
        릴레이-)학생UI: 9: 기부참여요청(학생ID: int, 요청학생ID: int)
    end

    loop 학생이 응답할 때마다
        alt 거절 선택
            학생UI->>릴레이: 10: 기부참여거절선택(학생ID: int, 요청학생ID: int)
            Note over 릴레이: 기록하지 않음
        else 참여 선택
            학생UI->>릴레이: 11: 기부참여선택(학생ID: int, 모임ID: int, 요청학생ID: int)
            릴레이->>기부DB: 12: 모임참여이력조회(학생ID: int, 모임ID: int): boolean
            기부DB-->>릴레이: 참여이력여부
            alt 이미 참여함
                릴레이-)학생UI: 13: 참여불가알림(학생ID: int)
                Note over 릴레이: 그 학생의 응답은 기록하지 않음
            else 처음 참여
                릴레이->>기부DB: 14: 기부기록및새바통저장(학생ID: int, 모임ID: int)
                릴레이-)앱운영자: 15: 기부적립알림(학생ID: int, 금액: int)
                릴레이->>릴레이: 16: 참여인원계산(참여인원: int): int
                opt 첫 번째 참여 확정
                    릴레이->>기부DB: 17: 기존바통회수(요청학생ID: int)
                end
            end
        end
        릴레이-)학생UI: 18: 릴레이결과알림(요청학생ID: int, 참여인원: int)
    end
    deactivate 릴레이
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~6 | 1 |
| 7~9 | 2 |
| 10 | 5 |
| 11~15 | 3 |
| 16~17 | 4 |
| 18 | 6 |

## 메모

- 1번 시작 메시지는 최종배치가 배치DB에 저장될 때 발생하는 Found Message다.
- 8번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 14번으로 참여 시 새 바통이 부여되고, 15번으로 참여 1건당 1,000원 대리기부 통보가 앱운영자에게 발송된다.
- 16번은 처음 참여한 학생만 참여인원에 더한다. 참여인원이 1이 되는 첫 번째 참여에서 17번으로 요청한 학생의 기존 바통을 회수한다.
- 응답 마감은 두지 않는다. 응답이 올 때마다 18번으로 요청한 학생에게 결과를 알린다.
- 5, 6, 9, 13, 15, 18번 알림은 비동기로 전송된다.

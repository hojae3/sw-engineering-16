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
    participant 기부DB as 기부DB
    participant 출석DB as 출석DB
    participant 학생UI as 학생UI
    actor 앱운영자

    Found->>+릴레이: 1: 최종배치저장됨(모임ID: int)
    loop 모임 참가 학생마다
        릴레이->>기부DB: 2: 바통보유여부조회(학생ID: int): boolean
        기부DB-->>릴레이: 바통보유여부
        릴레이->>출석DB: 3: 출석여부조회(학생ID: int, 모임ID: int): boolean
        출석DB-->>릴레이: 출석여부
        alt 바통 보유 및 출석 확인
            릴레이-)학생UI: 4: 릴레이잇기버튼활성화(학생ID: int)
        else 조건 미충족
            릴레이-)학생UI: 5: 릴레이잇기버튼비활성화(학생ID: int)
        end
    end

    학생UI->>릴레이: 6: 릴레이잇기선택(학생ID: int, 모임ID: int)
    릴레이->>+현황: 7: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
    현황-->>-릴레이: 같은테이블출석학생목록
    loop 같은 테이블 학생마다
        릴레이-)학생UI: 8: 기부참여요청(학생ID: int, 요청학생ID: int)
    end

    alt 거절 선택
        학생UI->>릴레이: 9: 기부참여거절(학생ID: int)
        Note over 릴레이: 기록하지 않음
    else 참여 선택
        학생UI->>릴레이: 10: 기부참여선택(학생ID: int, 모임ID: int, 요청학생ID: int)
        릴레이->>기부DB: 11: 모임참여이력조회(학생ID: int, 모임ID: int): boolean
        기부DB-->>릴레이: 참여이력여부
        alt 이미 참여함
            릴레이-)학생UI: 12: 참여불가알림(학생ID: int)
            Note over 릴레이: 처리를 종료한다
        else 최초 참여
            릴레이->>기부DB: 13: 기부기록및새바통저장(학생ID: int, 모임ID: int)
            릴레이-)앱운영자: 14: 기부적립알림(학생ID: int, 금액: int)
            opt 첫 번째 참여 확정 시
                릴레이->>기부DB: 15: 기존바통회수(학생ID: int)
            end
        end
    end
    릴레이-)학생UI: 16: 릴레이결과알림(학생ID: int, 참여인원: int)
    deactivate 릴레이
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~5 | 1 |
| 6~8 | 2 |
| 9~15 | 3, 4, 5 |
| 16 | 6 |

## 메모

- 1번 시작 메시지는 '6. 1인 잔류 테이블 합석' 등으로 최종배치가 배치DB에 저장될 때 발생하는 Found Message다.
- 7번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 13번으로 참여 시 새 바통이 부여되고, 14번으로 참여 1건당 1,000원 대리기부 통보가 앱운영자에게 발송된다.
- 15번은 해당 모임의 첫 번째 학생 참여 확정 시 요청자의 기존 바통이 회수되는 처리다.
- 4, 5, 8, 12, 14, 16번 알림은 비동기로 전송된다.

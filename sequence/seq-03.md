---
번호: 3
기능명: 친해지고 싶은 학생 알림
담당: 최성민
요구사항: requirements/req-03.md
---

# seq-03 친해지고싶은학생알림

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 친해지고싶은학생알림 | 담당 객체 | classes/CloseStudentNotification.md |
| 관심등록DB | DB | classes/InterestRegistrationDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **데이터 변화** (신청DB에 신청 상태 '결제완료'가 저장됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 알림 as 친해지고싶은학생알림
    participant 관심DB as 관심등록DB
    participant 학생UI as 학생UI

    Found->>+알림: 1: 결제완료저장됨(학생ID: int, 모임ID: int)
    알림->>관심DB: 2: 관심등록학생조회(학생ID: int): List<int>
    관심DB-->>알림: 관심등록학생목록

    alt 관심등록 학생 없음
        알림-)학생UI: 3: 알림대상없음알림(학생ID: int)
        Note over 알림: 처리를 종료한다
    else 관심등록 학생 있음
        알림->>알림: 4: 알림확률계산(등록인원: int): double
        알림->>알림: 5: 발송대상선정(학생ID목록: List<int>, 확률: double): List<int>
        loop 발송 대상 학생마다
            알림-)학생UI: 6: 모임신청알림(학생ID: int, 모임ID: int)
        end
        학생UI->>알림: 7: 알림선택(학생ID: int, 모임ID: int)
        알림-)학생UI: 8: 모임공지화면표시(모임ID: int)
    end
    deactivate 알림
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5~6 | 4, 5 |
| 7~8 | 6 |

## 메모

- 1번 시작 메시지는 '2-2. 결제 및 신청 확정'에서 신청DB에 '결제완료' 상태가 저장될 때 발생하는 Found Message다.
- 4번 알림 확률 계산식은 $p = 1 / n$ (등록인원 $n$)이다.
- 6번 모임신청알림은 알림 권한이 허용된 학생에게만 발송된다.
- 7~8번은 알림을 수신한 학생이 알림을 눌러 해당 모임 공지 화면으로 이동하는 흐름이다.


---
번호: 9
기능명: 자동 정산
담당: 양수현
요구사항: requirements/req-09.md
---

# seq-09 자동정산

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 자동정산 | 담당 객체 | classes/AutoSettlement.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 모임DB | DB | classes/MeetingDB.md |
| 주문DB | DB | classes/OrderDB.md |
| 결제DB | DB | classes/PaymentDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **정해진 시각** (모임 종료 시각 도달) → `시간` 액터

## 다이어그램

```mermaid
sequenceDiagram
    actor 시간
    participant 정산 as 자동정산
    participant 현황 as 테이블출석현황
    participant 모임DB as 모임DB
    participant 주문DB as 주문DB
    participant 결제DB as 결제DB
    participant 학생UI as 학생UI

    시간->>+정산: 1: 모임종료시각도달(모임ID: int)
    정산->>모임DB: 2: 모임상태변경(모임ID: int, 모임상태.종료)
    정산->>주문DB: 3: 주문마감(모임ID: int)
    정산->>모임DB: 4: 테이블목록조회(모임ID: int): List<int>
    모임DB-->>정산: 테이블목록
    
    loop 테이블마다
        정산->>주문DB: 5: 테이블주문금액조회(모임ID: int, 테이블번호: int): int
        주문DB-->>정산: 테이블주문금액
        정산->>결제DB: 6: 테이블참가비합조회(모임ID: int, 테이블번호: int): int
        결제DB-->>정산: 테이블참가비합
        정산->>+현황: 7: 테이블출석인원조회(모임ID: int, 테이블번호: int): int
        현황-->>-정산: 출석인원
        
        alt 출석 인원 0명
            Note over 정산: 해당 테이블 환급 미진행
        else 출석 인원 1명 이상
            정산->>+현황: 8: 테이블출석학생목록조회(모임ID: int, 테이블번호: int): List<int>
            현황-->>-정산: 테이블출석학생목록
            정산->>정산: 9: 환급액계산(테이블주문금액: int, 참가비합: int, 출석인원: int): int
            loop 출석 학생마다
                정산->>결제DB: 10: 환급액저장(학생ID: int, 모임ID: int, 환급액: int)
                정산-)학생UI: 11: 환급알림(학생ID: int, 환급액: int)
            end
        end
    end
    deactivate 정산
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1 | 1 |
| 2~3 | 1 |
| 4~8 | 2 |
| 9 | 3 |
| 10~11 | 4 |

## 메모

- 1번 시작 메시지는 모임 종료 시각에 스케줄러에 의해 발생하는 시간 사건이다.
- 7번과 8번은 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 9번 환급액 계산은 (출석 학생 결제 참가비 합 - 테이블 주문 금액) ÷ 출석 인원으로 1인 환급액을 구하고, 원 단위 나머지는 학생 ID 순으로 1원씩 배분한다.
- 11번 환급알림은 비동기로 학생에게 발송된다.

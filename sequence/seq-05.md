---
번호: 5
기능명: QR 출석
담당: 양수현
요구사항: requirements/req-05.md
---

# seq-05 QR출석

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| QR출석 | 담당 객체 | classes/QRAttendance.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 주문DB | DB | classes/OrderDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 사장님UI | UI | classes/OwnerUI.md |

시작 방식: **사람이 누름** (학생이 상대방 QR을 스캔) → `학생UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 학생UI as 학생UI
    participant 사장님UI as 사장님UI
    participant 출석 as QR출석
    participant 현황 as 테이블출석현황
    participant 배치DB as 배치DB
    participant 출석DB as 출석DB
    participant 주문DB as 주문DB

    alt 학생 간 상호 QR 스캔
        학생UI->>+출석: 1: 상호QR스캔요청(학생1ID: int, 학생2QR토큰: String, 모임ID: int)
        출석->>출석: 2: QR토큰검증(학생2QR토큰: String): boolean
        출석->>배치DB: 3: 학생배정모임조회(학생ID목록: List<int>): List<int>
        배치DB-->>출석: 배정모임목록

        alt 토큰 검증 실패 또는 배정 모임 불일치
            출석-)학생UI: 4: 출석실패알림(사유: String)
            Note over 출석: 처리를 종료한다
        else 검증 성공 및 배정 모임 일치
            출석->>출석DB: 5: 상호출석기록저장(학생1ID: int, 학생2ID: int, 모임ID: int, 방식: 출석방식)
        end
    else 사장님 확인 스캔
        사장님UI->>출석: 6: 사장님확인스캔요청(사장님ID: int, 학생QR토큰: String, 모임ID: int)
        출석->>출석: 7: QR토큰검증(학생QR토큰: String): boolean
        출석->>배치DB: 8: 학생배정모임조회(학생ID목록: List<int>): List<int>
        배치DB-->>출석: 배정모임목록

        alt 검증 실패
            출석-)사장님UI: 9: 출석실패알림(사유: String)
            Note over 출석: 처리를 종료한다
        else 검증 성공
            출석->>출석DB: 10: 출석기록저장(학생ID: int, 모임ID: int, 방식: 출석방식)
        end
    end

    출석->>배치DB: 11: 학생테이블번호조회(학생ID: int, 모임ID: int): int
    배치DB-->>출석: 테이블번호
    출석->>+현황: 12: 테이블출석인원조회(모임ID: int, 테이블번호: int): int
    현황->>출석DB: 13: 테이블출석조회(모임ID: int, 테이블번호: int): List<int>
    출석DB-->>현황: 테이블출석학생목록
    현황-->>-출석: 출석인원

    alt 테이블 출석 인원 2명 이상
        출석->>주문DB: 14: 주문가능상태갱신(모임ID: int, 테이블번호: int)
        출석-)학생UI: 15: 출석완료및주문가능알림(학생ID: int, 테이블번호: int)
    else 2명 미만
        출석-)학생UI: 16: 출석완료알림(학생ID: int, 테이블번호: int)
    end
    deactivate 출석
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~4 | 1, 2, 3 |
| 5 | 4 |
| 6~10 | 5 |
| 11~16 | 6 |

## 메모

- 5번 상호출석기록저장의 출석방식은 'QR', 10번 출석기록저장의 출석방식은 '사장님확인'이다.
- 12번 테이블출석인원조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 14번으로 주문 가능 상태가 갱신되어야 해당 테이블의 주문이 허용된다.


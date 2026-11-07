---
번호: 13
기능명: 비매너 학생 이용 정지
담당: 최성민
요구사항: requirements/req-13.md
---

# seq-13 비매너학생이용정지

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 비매너학생이용정지 | 담당 객체 | classes/MannerSuspension.md |
| 신고DB | DB | classes/ReportDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 정지DB | DB | classes/SuspensionDB.md |
| 신청DB | DB | classes/ApplicationDB.md |
| 결제DB | DB | classes/PaymentDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 앱운영자 | 액터 | |

시작 방식: **사람이 누름** (앱운영자가 신고를 심사) → `앱운영자` 액터

## 다이어그램

```mermaid
sequenceDiagram
    actor 앱운영자
    participant 정지 as 비매너학생이용정지
    participant 신고DB as 신고DB
    participant 프로필DB as 프로필DB
    participant 정지DB as 정지DB
    participant 학생UI as 학생UI
    participant 신청DB as 신청DB
    participant 결제DB as 결제DB

    앱운영자->>+정지: 1: 신고심사(신고ID: int, 대상학생ID: int, 심사결과: 심사결과, 정지사유: String)
    정지->>신고DB: 2: 심사결과저장(신고ID: int, 심사결과: 심사결과)

    alt 심사결과가 '반려'임
        Note over 정지: 처리를 종료한다
    else 심사결과가 '유효' 또는 '중대위반'임
        정지->>신고DB: 3: 누적유효신고건수조회(대상학생ID: int): int
        신고DB-->>정지: 누적유효건수

        alt 누적유효건수 3건 이상 또는 심사결과가 '중대위반'임
            정지->>프로필DB: 4: 계정상태변경(학생ID: int, 상태: 계정상태.정지)
            정지->>정지DB: 5: 정지저장(학생ID: int, 정지사유: String)
            정지-)학생UI: 6: 이용정지알림(학생ID: int, 정지사유: String)
            정지->>신청DB: 7: 미시작결제완료신청목록조회(학생ID: int): List<int>
            신청DB-->>정지: 취소대상모임목록

            alt 취소 대상 신청 건 존재
                loop 신청 건마다
                    정지->>신청DB: 8: 신청상태변경(학생ID: int, 모임ID: int, 상태: 신청상태.신청취소)
                    정지->>결제DB: 9: 참가비전액환급저장(학생ID: int, 모임ID: int)
                end
            end
        else 누적유효건수 3건 미만 및 '중대위반' 아님
            Note over 정지: 계정 상태를 유지하고 처리를 종료한다
        end
    end
    deactivate 정지
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~2 | 1, 2 |
| 3 | 3 |
| 4~9 | 4 |
| - | 5 |

## 메모

- 1번 심사는 앱운영자가 신고DB의 사유와 내용을 검토한 뒤 결과를 시스템에 입력하는 흐름이다.
- 3번 누적유효신고건수조회는 '반려'를 제외하고 '유효' 판정된 건수만 집계한다.
- 4번으로 프로필DB 계정 상태가 '정지'로 변경되면 이후 모든 모임 신청이 영구 차단된다.
- 7~9번은 정지된 학생이 이미 결제 완료했으나 아직 시작되지 않은 모임에 대한 자동 취소 및 전액 환급 처리다.
- 6번 이용정지알림은 비동기 푸시 알림으로 전송된다.

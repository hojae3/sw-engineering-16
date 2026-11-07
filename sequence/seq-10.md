---
번호: 10
기능명: 만난 사람 평가
담당: 설혜원
요구사항: requirements/req-10.md
---

# seq-10 만난사람평가

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 만난사람평가 | 담당 객체 | classes/MeetingEvaluation.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 평가DB | DB | classes/EvaluationDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **데이터 변화** (모임DB의 모임 상태가 '종료'로 변경됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 평가 as 만난사람평가
    participant 현황 as 테이블출석현황
    participant 프로필DB as 프로필DB
    participant 학생UI as 학생UI
    participant 평가DB as 평가DB

    Found->>+평가: 1: 모임종료저장됨(모임ID: int)
    loop 모임 참가 학생마다
        평가->>+현황: 2: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
        현황-->>-평가: 같은테이블출석학생목록
        loop 대상 학생마다
            평가->>프로필DB: 3: 프로필사진조회(학생ID: int): String
            프로필DB-->>평가: 프로필사진
        end
        평가-)학생UI: 4: 평가화면표시(대상학생목록: List<int>, 프로필사진목록: List<String>)
    end

    학생UI->>평가: 5: 평가완료선택(평가자ID: int, 모임ID: int, 평가점수목록: Map<int, int>)
    평가->>평가DB: 6: 평가저장(평가자ID: int, 모임ID: int, 평가점수목록: Map<int, int>)
    평가->>평가DB: 7: 테이블평가전원제출여부조회(모임ID: int, 평가자ID: int): boolean
    평가DB-->>평가: 전원제출여부

    alt 전원 미제출
        Note over 평가: 다른 학생들의 평가 제출 대기
    else 전원 제출 완료
        loop 해당 테이블 출석 학생마다
            평가->>평가DB: 8: 받은점수목록조회(학생ID: int, 모임ID: int): List<int>
            평가DB-->>평가: 받은점수목록
            평가->>프로필DB: 9: 매너점수조회(학생ID: int): double
            프로필DB-->>평가: 기존매너점수
            loop 평가한 학생마다
                평가->>프로필DB: 10: 매너점수조회(학생ID: int): double
                프로필DB-->>평가: 평가자매너점수
            end
            평가->>평가: 11: 매너점수계산(기존점수: double, 받은점수목록: List<int>, 평가자점수목록: List<double>): double
            평가->>프로필DB: 12: 매너점수저장(학생ID: int, 매너점수: double)
        end
    end
    평가-)학생UI: 13: 평가제출완료알림(학생ID: int)
    deactivate 평가
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~4 | 1 |
| 5 | 2 |
| 6 | 3 |
| 7 | 4 |
| 8~12 | 5 |
| 13 | 6 |

## 메모

- 1번 시작 메시지는 모임 상태가 '종료'로 기록될 때 기동되는 Found Message다.
- 2번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 11번 매너점수계산은 평가자 매너점수가 4.0 이상인 경우 1회 추가 가중치를 부여하여 계산한다.
- 13번 완료 알림은 학생UI에 비동기로 전송된다.

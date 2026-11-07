---
번호: 6
기능명: 1인 잔류 테이블 합석
담당: 김호재
요구사항: requirements/req-06.md
---

# seq-06 1인잔류테이블합석

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 1인잔류테이블합석 | 담당 객체 | classes/SinglePersonTableMerge.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 모임DB | DB | classes/MeetingDB.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 학생UI | UI | classes/StudentUI.md |
| 사장님UI | UI | classes/OwnerUI.md |

시작 방식: **정해진 시각** (출석 가능 시간 종료 시점) → `시간` 액터

## 다이어그램

```mermaid
sequenceDiagram
    actor 시간
    participant 합석 as 1인잔류테이블합석
    participant 현황 as 테이블출석현황
    participant 모임DB as 모임DB
    participant 배치DB as 배치DB
    participant 출석DB as 출석DB
    participant 프로필DB as 프로필DB
    participant 사장님UI as 사장님UI
    participant 학생UI as 학생UI

    시간->>+합석: 1: 출석가능시간종료됨(모임ID: int)
    합석->>모임DB: 2: 모임상태조회(모임ID: int): 모임상태
    모임DB-->>합석: 모임상태

    alt 모임 상태가 '취소'임
        합석-)사장님UI: 3: 모임취소알림(모임ID: int)
        Note over 합석: 처리를 종료한다
    else 모임 진행 중
        합석->>+현황: 4: 테이블별출석조회(모임ID: int): List<int>
        현황->>배치DB: 5: 테이블배치및의자조회(모임ID: int): List<int>
        배치DB-->>현황: 테이블배치정보
        현황->>출석DB: 6: 출석학생조회(모임ID: int): List<int>
        출석DB-->>현황: 출석학생목록
        현황-->>-합석: 테이블별출석목록

        loop 1인 잔류 테이블마다
            합석->>프로필DB: 7: 학생학과학번목록조회(학생ID목록: List<int>): List<String>
            프로필DB-->>합석: 학과목록
            합석->>합석: 8: 대상테이블선정(혼자출석학생ID: int, 후보목록: List<int>): int

            alt 빈 좌석 있는 후보 테이블 없음
                합석->>배치DB: 9: 추가의자갱신(모임ID: int, 테이블번호: int)
                합석-)사장님UI: 10: 의자추가알림(모임ID: int, 테이블번호: int)
            else 대상 테이블 존재
                합석->>배치DB: 11: 테이블번호갱신(학생ID: int, 새테이블번호: int)
                합석-)학생UI: 12: 바뀐테이블번호알림(학생ID: int, 바뀐테이블번호: int)
            end
        end

        합석->>배치DB: 13: 최종배치저장(모임ID: int, 최종배치목록: List<int>)
    end
    deactivate 합석
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~3 | 1 |
| 4~6 | 2 |
| 7~8 | 3, 4 |
| 9~10 | 4.1 |
| 11~12 | 5 |
| 13 | 6 |

## 메모

- 1번 시작 메시지는 모임 시작 10분 후 출석 가능 시간이 마감되는 시각 사건이다.
- 4번 테이블별출석조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)이다.
- 8번 대상테이블선정 시 빈 좌석(테이블 정원 + 추가 의자 − 출석 인원) 1개 이상, 다른 학과, 최소 출석 인원, 낮은 번호 순으로 우선순위를 판정한다.
- 13번으로 합석 이력이 반영된 최종배치가 확정 저장된다.


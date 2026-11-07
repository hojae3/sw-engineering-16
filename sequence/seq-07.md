---
번호: 7
기능명: 프로필 기반 대화 주제 카드
담당: 설혜원
요구사항: requirements/req-07.md
---

# seq-07 프로필기반대화주제카드

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 프로필기반대화주제카드 | 담당 객체 | classes/ProfileTopicCard.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 배치DB | DB | classes/ArrangementDB.md |
| 출석DB | DB | classes/AttendanceDB.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 질문카드DB | DB | classes/QuestionCardDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **사람이 누름** (학생이 '대화 카드 시작'을 선택) → `학생UI`

## 다이어그램

```mermaid
sequenceDiagram
    participant 학생UI as 학생UI
    participant 카드 as 프로필기반대화주제카드
    participant 현황 as 테이블출석현황
    participant 배치DB as 배치DB
    participant 출석DB as 출석DB
    participant 프로필DB as 프로필DB
    participant 질문DB as 질문카드DB

    학생UI->>+카드: 1: 대화카드시작선택(학생ID: int, 모임ID: int, 테이블번호: int)
    카드->>+현황: 2: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
    현황->>배치DB: 3: 학생테이블번호조회(학생ID: int, 모임ID: int): int
    배치DB-->>현황: 테이블번호
    현황->>출석DB: 4: 테이블출석조회(모임ID: int, 테이블번호: int): List<int>
    출석DB-->>현황: 같은테이블출석학생목록
    현황-->>-카드: 같은테이블출석학생목록

    카드->>프로필DB: 5: 관심사태그목록조회(학생ID목록: List<int>): List<String>
    프로필DB-->>카드: 관심사태그목록

    loop 그만하기 선택 또는 남은 태그 없을 때까지
        카드->>카드: 6: 질문태그선택(태그목록: List<String>, 사용한태그목록: List<String>): String
        카드->>질문DB: 7: 관심사질문카드조회(관심사태그: String): String
        질문DB-->>카드: 질문카드내용
        카드->>프로필DB: 8: 관심사보유학생조회(학생ID목록: List<int>, 관심사태그: String): List<int>
        프로필DB-->>카드: 정답학생목록
        loop 같은 테이블 출석 학생마다
            카드-)학생UI: 9: 질문카드표시(학생ID: int, 질문내용: String, 후보목록: List<int>)
        end

        loop 전원 제출 또는 1분 경과 시까지
            학생UI->>카드: 10: 추측답제출(학생ID: int, 선택학생ID: int)
        end
        Note over 카드: ⏱ 1분 경과 또는 전원 제출 완료

        loop 같은 테이블 출석 학생마다
            카드-)학생UI: 11: 정답공개알림(학생ID: int, 정답학생목록: List<int>, 맞힘여부: boolean)
        end
        loop 정답 학생마다
            카드-)학생UI: 12: 이야기공유요청(학생ID: int, 관심사태그: String)
        end
        카드->>프로필DB: 13: 남은관심사태그여부조회(학생ID목록: List<int>, 사용한태그목록: List<String>): boolean
        프로필DB-->>카드: 남은태그여부

        alt 남은 태그 없음
            Note over 카드: 반복을 끝낸다
        else 남은 태그 있음
            alt 다음 카드 선택
                학생UI->>카드: 14: 다음카드선택(학생ID: int)
                Note over 카드: 6번으로 돌아간다
            else 그만하기 선택
                학생UI->>카드: 15: 그만하기선택(학생ID: int)
                Note over 카드: 반복을 끝낸다
            end
        end
    end

    loop 같은 테이블 출석 학생마다
        카드-)학생UI: 16: 게임종료알림(학생ID: int)
    end
    Note over 카드: 처리를 종료한다
    deactivate 카드
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~5 | 1 |
| 6~9 | 2 |
| 10 | 3 |
| 11 | 4 |
| 12~13 | 5 |
| 14~16 | 6 |

## 메모

- 2번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 6번에서 고른 태그는 프로필기반대화주제카드의 사용한태그목록에 더한다.
- 9번 질문 카드의 정답 후보는 같은 테이블 출석 학생들로 한정된다.
- 8번의 정답은 여러 명일 수 있어 목록으로 돌려받는다. 10번에서 정답 학생 중 한 명을 고르면 맞힌 것으로 보고, 11번의 맞힘여부로 알린다.
- 13번은 사용한태그목록을 넘겨 프로필DB가 아직 묻지 않은 태그가 있는지 판단하게 한다.

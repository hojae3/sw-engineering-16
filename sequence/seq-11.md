---
번호: 11
기능명: 친해지고 싶은 학생 등록
담당: 최성민
요구사항: requirements/req-11.md
---

# seq-11 친해지고싶은학생등록

## 참여 객체

| 객체 | 종류 | 클래스 파일 |
|---|---|---|
| 친해지고싶은학생등록 | 담당 객체 | classes/CloseStudentRegistration.md |
| 테이블출석현황 | 공통 객체 | classes/TableAttendanceStatus.md |
| 프로필DB | DB | classes/ProfileDB.md |
| 관심등록DB | DB | classes/InterestRegistrationDB.md |
| 학생UI | UI | classes/StudentUI.md |

시작 방식: **데이터 변화** (평가DB에 학생의 평가가 저장됨) → Found Message

## 다이어그램

```mermaid
sequenceDiagram
    participant Found as ●
    participant 등록 as 친해지고싶은학생등록
    participant 현황 as 테이블출석현황
    participant 프로필DB as 프로필DB
    participant 학생UI as 학생UI
    participant 관심DB as 관심등록DB

    Found->>+등록: 1: 평가저장됨(학생ID: int, 모임ID: int)
    등록->>+현황: 2: 같은테이블학생조회(학생ID: int, 모임ID: int): List<int>
    현황-->>-등록: 같은테이블출석학생목록
    loop 대상 학생마다
        등록->>프로필DB: 3: 프로필사진조회(학생ID: int): String
        프로필DB-->>등록: 프로필사진
    end
    등록-)학생UI: 4: 관심학생등록화면표시(대상학생목록: List<int>, 프로필사진목록: List<String>)

    alt 건너뛰기 선택
        학생UI->>등록: 5: 건너뛰기선택(학생ID: int)
        등록-)학생UI: 6: 등록생략알림(학생ID: int)
        Note over 등록: 처리를 종료한다
    else 친해지기 선택
        학생UI->>등록: 7: 친해지기선택(등록학생ID: int, 대상학생ID: int)
        등록->>관심DB: 8: 관심등록여부조회(등록학생ID: int, 대상학생ID: int): boolean
        관심DB-->>등록: 등록여부
        alt 이미 등록됨
            등록-)학생UI: 9: 중복등록알림(등록학생ID: int)
            Note over 등록: 처리를 종료한다
        else 신규 등록
            등록->>관심DB: 10: 관심등록저장(등록학생ID: int, 대상학생ID: int)
            등록-)학생UI: 11: 등록완료알림(등록학생ID: int)
        end
    end
    deactivate 등록
```

## 메시지 ↔ Action 대응표

| 메시지 | Action |
|---|---|
| 1~4 | 1 |
| 5~6 | 2 |
| 7 | 3 |
| 8~11 | 4 |

## 메모

- 1번 시작 메시지는 '10. 만난 사람 평가'에서 본인 평가가 평가DB에 저장될 때 발생하는 Found Message다.
- 2번 같은테이블학생조회는 공통 객체 테이블출석현황의 표준 연산(GLOSSARY 5장)을 재사용한다.
- 4번 관심학생등록화면표시는 2번에서 리턴받은 학생 목록과 3번에서 리턴받은 프로필 사진 목록을 인자로 전달하여 화면에 표시한다.
- 6, 9, 11번 알림은 비동기로 학생UI에 전달된다.

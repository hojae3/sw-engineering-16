# 발표 자료 (3번 친해지고싶은학생알림)

이번 발표는 시퀀스 다이어그램 1개와, 그 시퀀스에 관련된 클래스, 그 기능이 들어 있는 유스케이스 다이어그램으로 한다.

- 발표 기능: **3. 친해지고싶은학생알림** (담당 최성민)
- 기준 시퀀스: [sequence/seq-03.md](../../sequence/seq-03.md) 최신본 (a13bd6e, 11/11 21:45). 흐름과 메시지는 원본 그대로 두고, [RULES.md](../RULES.md)대로 라이프라인(«module», 단계별 화면)만 바꿨다. 신청 화면 내용의 출처가 없는 빈틈은 메시지를 추가해 메웠다.

| 순서 | 파일 | 내용 |
|---|---|---|
| 1 | [1-usecase.md](1-usecase.md) | ① 모임 생성·신청 단계 유스케이스 |
| 2 | [2-sequence.md](2-sequence.md) | 발표용 seq-03 + 원본과 달라진 점 |
| 3 | [3-class.md](3-class.md) | 클래스 6개 + 메시지 ↔ 연산 대조표 |
| - | [staruml.js](staruml.js) | 위 1~3을 StarUML로 그리는 스크립트 (유스케이스 1장, 시퀀스 1장, 클래스 1장) |

> 이 폴더는 발표용이라 원본(sequence/, classes/)과 다르다. 원본을 이 폴더에 맞출지는 팀에서 정한다.

## 원본에 맞추려면 (최성민 님 확인 필요)

| # | 위치 | 내용 |
|---|---|---|
| 1 | seq-03 | [2-sequence.md](2-sequence.md) "원본과 달라진 점" 표대로 6번 뒤에 모임정보조회(모임ID: int): 모임정보를 넣고, 원본 7번을 모임신청화면표시(수신학생ID: int, 모임정보: 모임정보)로 바꾼다. 라이프라인(«module», 모임신청UI)은 DISCUSSION 안건 15와 같이 정한다 |
| 2 | req-03, seq-03 | 알림 권한 확인을 뺀다 (DISCUSSION 안건 14) |
| 3 | seq-03 참여 객체 표 | DB의 클래스 파일이 아직 `classes/InterestRegistrationDB.md`(관심등록DB)다. 발표용은 DB 하나 + 테이블종류(관심등록, 모임) |
| 3-1 | classes/InterestRegistrationDB.md | 연산 이름이 `관심등록학생조회(학생ID: int)`인데 지금 메시지는 `본 학생을 관심등록한 학생조회(결제학생ID: int)`다. 둘 중 하나로 맞춘다 |
| 3-2 | classes/MeetingDB.md | `모임정보조회(모임ID: int): 모임정보` 연산이 없다 |
| 4 | classes/CloseStudentNotification.md | 연산 이름·번호가 옛 시퀀스 기준이다 (예: `결제완료저장됨` ↔ 지금 메시지 `DB에 결제완료가 저장됨`) |
| 5 | classes/StudentUI.md | `모임신청화면표시`가 없다 |
| 6 | 전체 클래스 | 모임신청UI·학생UI «abstract»·DB 하나·테이블종류·모임정보 클래스는 아직 classes/에 없다 (DISCUSSION 안건 15와 같이 정함) |

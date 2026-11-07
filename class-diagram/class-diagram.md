# 통합 클래스 다이어그램

> 이 파일은 스크립트로 만든다. 직접 고치지 말고 `classes/`를 고친 뒤 다시 생성한다. 실행: `python class-diagram/generate.py` (macOS는 `python3`)

`classes/`의 클래스 파일을 모은 그림이다 (CONVENTIONS 6.5). **원본은 `classes/` 파일이다.** 제출할 때는 CONVENTIONS 8.2에 따라 StarUML 한 장으로 옮긴다.

## 1. 클래스 개수 대조

| 종류 | 개수 |
|---|---|
| 담당 객체 | 21 |
| 공통 객체 | 2 |
| DB | 18 |
| UI | 2 |
| 외부 | 1 |
| 엔티티 | 9 |
| **합계** | **53** |

`classes/` 파일 53개와 1:1로 대응한다. 관계선은 두 클래스 사이에 하나씩, 모두 130개다.

| 번호 | 클래스 | 종류 | 파일 |
|---|---|---|---|
| 1 | 모임공지등록 | 담당 객체 (기능 1) | [MeetingNoticeRegistration.md](../classes/MeetingNoticeRegistration.md) |
| 2 | 신청확인및참가비계산 | 담당 객체 (기능 2-1) | [ApplicationCheckAndFeeCalc.md](../classes/ApplicationCheckAndFeeCalc.md) |
| 3 | 결제및신청확정 | 담당 객체 (기능 2-2) | [PaymentAndApplicationConfirm.md](../classes/PaymentAndApplicationConfirm.md) |
| 4 | 친해지고싶은학생알림 | 담당 객체 (기능 3) | [CloseStudentNotification.md](../classes/CloseStudentNotification.md) |
| 5 | 자리배치생성 | 담당 객체 (기능 4-2) | [SeatArrangementGeneration.md](../classes/SeatArrangementGeneration.md) |
| 6 | QR출석 | 담당 객체 (기능 5) | [QRAttendance.md](../classes/QRAttendance.md) |
| 7 | 1인잔류테이블합석 | 담당 객체 (기능 6) | [SinglePersonTableMerge.md](../classes/SinglePersonTableMerge.md) |
| 8 | 프로필기반대화주제카드 | 담당 객체 (기능 7) | [ProfileTopicCard.md](../classes/ProfileTopicCard.md) |
| 9 | 블라인드프로필공개 | 담당 객체 (기능 8) | [BlindProfileDisclosure.md](../classes/BlindProfileDisclosure.md) |
| 10 | 자동정산 | 담당 객체 (기능 9) | [AutoSettlement.md](../classes/AutoSettlement.md) |
| 11 | 만난사람평가 | 담당 객체 (기능 10) | [MeetingEvaluation.md](../classes/MeetingEvaluation.md) |
| 12 | 친해지고싶은학생등록 | 담당 객체 (기능 11) | [CloseStudentRegistration.md](../classes/CloseStudentRegistration.md) |
| 13 | 비매너학생신고 | 담당 객체 (기능 12) | [MannerReport.md](../classes/MannerReport.md) |
| 14 | 비매너학생이용정지 | 담당 객체 (기능 13) | [MannerSuspension.md](../classes/MannerSuspension.md) |
| 15 | 당일안심귀가 | 담당 객체 (기능 15) | [SafeReturnHome.md](../classes/SafeReturnHome.md) |
| 16 | 기부릴레이잇기 | 담당 객체 (기능 16) | [DonationRelay.md](../classes/DonationRelay.md) |
| 17 | 가게연합음식품앗이 | 담당 객체 (기능 17) | [StoreFoodExchange.md](../classes/StoreFoodExchange.md) |
| 18 | 화장실대기및조편성 | 담당 객체 (기능 18-1) | [ToiletWaitAndGroup.md](../classes/ToiletWaitAndGroup.md) |
| 19 | 화장실입장및퇴실관리 | 담당 객체 (기능 18-2) | [ToiletEntryExitManagement.md](../classes/ToiletEntryExitManagement.md) |
| 20 | 숙취예보 | 담당 객체 (기능 19) | [HangoverForecast.md](../classes/HangoverForecast.md) |
| 21 | 2차참가자동결정 | 담당 객체 (기능 20) | [SecondRoundAutoDecision.md](../classes/SecondRoundAutoDecision.md) |
| 22 | 귀가시간계산 | 공통 객체 | [ReturnHomeTimeCalc.md](../classes/ReturnHomeTimeCalc.md) |
| 23 | 테이블출석현황 | 공통 객체 | [TableAttendanceStatus.md](../classes/TableAttendanceStatus.md) |
| 24 | 신청DB | DB | [ApplicationDB.md](../classes/ApplicationDB.md) |
| 25 | 배치DB | DB | [ArrangementDB.md](../classes/ArrangementDB.md) |
| 26 | 출석DB | DB | [AttendanceDB.md](../classes/AttendanceDB.md) |
| 27 | 기부DB | DB | [DonationDB.md](../classes/DonationDB.md) |
| 28 | 평가DB | DB | [EvaluationDB.md](../classes/EvaluationDB.md) |
| 29 | 품앗이DB | DB | [FoodExchangeDB.md](../classes/FoodExchangeDB.md) |
| 30 | 관심등록DB | DB | [InterestRegistrationDB.md](../classes/InterestRegistrationDB.md) |
| 31 | 모임DB | DB | [MeetingDB.md](../classes/MeetingDB.md) |
| 32 | 주문DB | DB | [OrderDB.md](../classes/OrderDB.md) |
| 33 | 결제DB | DB | [PaymentDB.md](../classes/PaymentDB.md) |
| 34 | 프로필DB | DB | [ProfileDB.md](../classes/ProfileDB.md) |
| 35 | 질문카드DB | DB | [QuestionCardDB.md](../classes/QuestionCardDB.md) |
| 36 | 신고DB | DB | [ReportDB.md](../classes/ReportDB.md) |
| 37 | 2차공지DB | DB | [SecondNoticeDB.md](../classes/SecondNoticeDB.md) |
| 38 | 2차기록DB | DB | [SecondRecordDB.md](../classes/SecondRecordDB.md) |
| 39 | 가게DB | DB | [StoreDB.md](../classes/StoreDB.md) |
| 40 | 정지DB | DB | [SuspensionDB.md](../classes/SuspensionDB.md) |
| 41 | 화장실대기열DB | DB | [ToiletQueueDB.md](../classes/ToiletQueueDB.md) |
| 42 | 사장님UI | UI | [OwnerUI.md](../classes/OwnerUI.md) |
| 43 | 학생UI | UI | [StudentUI.md](../classes/StudentUI.md) |
| 44 | 단말기위치정보 | 외부 | [DeviceLocation.md](../classes/DeviceLocation.md) |
| 45 | 참가기록 | 엔티티 | [ParticipationRecord.md](../classes/ParticipationRecord.md) |
| 46 | 참가응답 | 엔티티 | [ParticipationResponse.md](../classes/ParticipationResponse.md) |
| 47 | 참가결과 | 엔티티 | [ParticipationResult.md](../classes/ParticipationResult.md) |
| 48 | Point | 엔티티 | [Point.md](../classes/Point.md) |
| 49 | 2차공지 | 엔티티 | [SecondNotice.md](../classes/SecondNotice.md) |
| 50 | 학생비상연락정보 | 엔티티 | [StudentEmergencyContact.md](../classes/StudentEmergencyContact.md) |
| 51 | 화장실구성 | 엔티티 | [ToiletConfig.md](../classes/ToiletConfig.md) |
| 52 | 화장실대기열현황 | 엔티티 | [ToiletQueueStatus.md](../classes/ToiletQueueStatus.md) |
| 53 | 화장실대기학생 | 엔티티 | [ToiletWaitStudent.md](../classes/ToiletWaitStudent.md) |

## 2. 전체 그림

53개 클래스의 이름만 종류별로 묶었다. 관계선은 3장에서 본다.

```mermaid
flowchart TB
    subgraph G1["담당 객체 21개"]
        MeetingNoticeRegistration["모임공지등록"]
        ApplicationCheckAndFeeCalc["신청확인및참가비계산"]
        PaymentAndApplicationConfirm["결제및신청확정"]
        CloseStudentNotification["친해지고싶은학생알림"]
        SeatArrangementGeneration["자리배치생성"]
        QRAttendance["QR출석"]
        SinglePersonTableMerge["1인잔류테이블합석"]
        ProfileTopicCard["프로필기반대화주제카드"]
        BlindProfileDisclosure["블라인드프로필공개"]
        AutoSettlement["자동정산"]
        MeetingEvaluation["만난사람평가"]
        CloseStudentRegistration["친해지고싶은학생등록"]
        MannerReport["비매너학생신고"]
        MannerSuspension["비매너학생이용정지"]
        SafeReturnHome["당일안심귀가"]
        DonationRelay["기부릴레이잇기"]
        StoreFoodExchange["가게연합음식품앗이"]
        ToiletWaitAndGroup["화장실대기및조편성"]
        ToiletEntryExitManagement["화장실입장및퇴실관리"]
        HangoverForecast["숙취예보"]
        SecondRoundAutoDecision["2차참가자동결정"]
        MeetingNoticeRegistration ~~~ QRAttendance
        ApplicationCheckAndFeeCalc ~~~ SinglePersonTableMerge
        PaymentAndApplicationConfirm ~~~ ProfileTopicCard
        CloseStudentNotification ~~~ BlindProfileDisclosure
        SeatArrangementGeneration ~~~ AutoSettlement
        QRAttendance ~~~ MeetingEvaluation
        SinglePersonTableMerge ~~~ CloseStudentRegistration
        ProfileTopicCard ~~~ MannerReport
        BlindProfileDisclosure ~~~ MannerSuspension
        AutoSettlement ~~~ SafeReturnHome
        MeetingEvaluation ~~~ DonationRelay
        CloseStudentRegistration ~~~ StoreFoodExchange
        MannerReport ~~~ ToiletWaitAndGroup
        MannerSuspension ~~~ ToiletEntryExitManagement
        SafeReturnHome ~~~ HangoverForecast
        DonationRelay ~~~ SecondRoundAutoDecision
    end
    subgraph G2["공통 객체 2개"]
        ReturnHomeTimeCalc["귀가시간계산"]
        TableAttendanceStatus["테이블출석현황"]
    end
    G1 ~~~ G2
    subgraph G3["DB 18개"]
        ApplicationDB["신청DB"]
        ArrangementDB["배치DB"]
        AttendanceDB["출석DB"]
        DonationDB["기부DB"]
        EvaluationDB["평가DB"]
        FoodExchangeDB["품앗이DB"]
        InterestRegistrationDB["관심등록DB"]
        MeetingDB["모임DB"]
        OrderDB["주문DB"]
        PaymentDB["결제DB"]
        ProfileDB["프로필DB"]
        QuestionCardDB["질문카드DB"]
        ReportDB["신고DB"]
        SecondNoticeDB["2차공지DB"]
        SecondRecordDB["2차기록DB"]
        StoreDB["가게DB"]
        SuspensionDB["정지DB"]
        ToiletQueueDB["화장실대기열DB"]
        ApplicationDB ~~~ FoodExchangeDB
        ArrangementDB ~~~ InterestRegistrationDB
        AttendanceDB ~~~ MeetingDB
        DonationDB ~~~ OrderDB
        EvaluationDB ~~~ PaymentDB
        FoodExchangeDB ~~~ ProfileDB
        InterestRegistrationDB ~~~ QuestionCardDB
        MeetingDB ~~~ ReportDB
        OrderDB ~~~ SecondNoticeDB
        PaymentDB ~~~ SecondRecordDB
        ProfileDB ~~~ StoreDB
        QuestionCardDB ~~~ SuspensionDB
        ReportDB ~~~ ToiletQueueDB
    end
    G2 ~~~ G3
    subgraph G4["UI 2개"]
        OwnerUI["사장님UI"]
        StudentUI["학생UI"]
    end
    G3 ~~~ G4
    subgraph G5["외부 1개"]
        DeviceLocation["단말기위치정보"]
    end
    G4 ~~~ G5
    subgraph G6["엔티티 9개"]
        ParticipationRecord["참가기록"]
        ParticipationResponse["참가응답"]
        ParticipationResult["참가결과"]
        Point["Point"]
        SecondNotice["2차공지"]
        StudentEmergencyContact["학생비상연락정보"]
        ToiletConfig["화장실구성"]
        ToiletQueueStatus["화장실대기열현황"]
        ToiletWaitStudent["화장실대기학생"]
        ParticipationRecord ~~~ StudentEmergencyContact
        ParticipationResponse ~~~ ToiletConfig
        ParticipationResult ~~~ ToiletQueueStatus
        Point ~~~ ToiletWaitStudent
    end
    G5 ~~~ G6
```

## 3. 영역별 그림

PPT 2장부터 쓰는 그림이다. StarUML에서는 영역마다 다이어그램을 따로 만들고, Model Explorer의 기존 클래스를 끌어다 놓는다. 표기는 Mermaid 규칙에 따라 `List<int>`를 `List~int~`로 적지만 그림에는 `List<int>`로 나온다.

| PPT | 절 | 내용 |
|---|---|---|
| 1장 | 2장 전체 그림, 통합 다이어그램 | 53개, 이름만, 관계선 포함 |
| 2장 | 3.1 | 모임 전 ① |
| 3장 | 3.2 | 모임 전 ② |
| 4장 | 3.3 | 모임 중: 출석·교류 |
| 5장 | 3.4 | 모임 중: 기부·품앗이·화장실 |
| 6장 | 3.5 | 모임 후: 정산·평가·신고 |
| 7장 | 3.6 | 모임 후: 귀가·예보·2차 |
| 8장 | 3.7, 3.8 | 공통 객체·외부, DB 회원·모임 |
| 9장 | 3.9 | DB 모임 진행 |
| 10장 | 3.10 | DB 평가·교류 |
| 11장 | 3.11 | 사장님UI·엔티티 |
| 12장 | 3.12 | 학생UI |
| 슬라이드 아님 | 3.13 | 참고용: 공통 객체·DB·엔티티 사이의 관계선 |

### 3.1 모임 전 ① (기능 1, 2-1, 2-2)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class MeetingNoticeRegistration["모임공지등록"] {
        -모임ID: int
        -사장님ID: int
        -가게ID: int
        -요청식별자: String
        +모임공지등록요청(사장님ID: int, 가게ID: int, 모임이름: String, 시작시각: datetime, 모임종료시각: datetime, 모집정원: int, 기본참가비: int, 품앗이참여여부: boolean, 요청식별자: String)
        -공지입력값검증(모집정원: int, 기본참가비: int, 시작시각: datetime, 모임종료시각: datetime) boolean
    }
    class ApplicationCheckAndFeeCalc["신청확인및참가비계산"] {
        -학생ID: int
        -모임ID: int
        -학년: int
        -학년가중치: double
        -최종참가비: int
        +신청하기선택(학생ID: int, 모임ID: int)
        -학년계산(학번: String) int
        -학년가중치결정(학년: int) double
        -참가비계산(기본참가비: int, 학년가중치: double) int
    }
    class PaymentAndApplicationConfirm["결제및신청확정"] {
        -학생ID: int
        -모임ID: int
        -결제금액: int
        +결제요청(학생ID: int, 모임ID: int, 결제금액: int)
        -참가비일치검증(결제금액: int, 학생ID: int) boolean
        -결제승인요청(결제금액: int) boolean
    }
    class StoreDB["가게DB"]
    class PaymentDB["결제DB"]
    class MeetingDB["모임DB"]
    class OwnerUI["사장님UI"]
    class ApplicationDB["신청DB"]
    class SuspensionDB["정지DB"]
    class ProfileDB["프로필DB"]
    class StudentUI["학생UI"]
    MeetingNoticeRegistration -- StoreDB
    PaymentAndApplicationConfirm -- PaymentDB
    PaymentAndApplicationConfirm -- MeetingDB
    PaymentAndApplicationConfirm -- ApplicationDB
    PaymentAndApplicationConfirm -- ProfileDB
    PaymentAndApplicationConfirm -- StudentUI
    MeetingNoticeRegistration -- MeetingDB
    ApplicationCheckAndFeeCalc -- MeetingDB
    MeetingNoticeRegistration -- OwnerUI
    MeetingNoticeRegistration -- StudentUI
    ApplicationCheckAndFeeCalc -- ApplicationDB
    ApplicationCheckAndFeeCalc -- SuspensionDB
    ApplicationCheckAndFeeCalc -- ProfileDB
    ApplicationCheckAndFeeCalc -- StudentUI
```

### 3.2 모임 전 ② (기능 3, 4-2)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class CloseStudentNotification["친해지고싶은학생알림"] {
        -모임ID: int
        -대상학생ID: int
        -관심등록학생목록: List~int~
        -알림확률: double
        -발송대상목록: List~int~
        +결제완료저장됨(학생ID: int, 모임ID: int)
        -알림확률계산(등록인원: int) double
        -발송대상선정(학생ID목록: List~int~, 확률: double) List~int~
        +알림선택(학생ID: int, 모임ID: int)
    }
    class SeatArrangementGeneration["자리배치생성"] {
        -모임ID: int
        -선발학생수: int
        -테이블수: int
        +모집마감상태변경됨(모임ID: int)
        -이전만남쌍목록생성(이전테이블: List~int~, 이전출석: List~int~) List~int~
        -테이블수및정원계산(선발인원: int) int
        -학생정렬(학생ID목록: List~int~) List~int~
        -순환배정실행(정렬학생목록: List~int~) List~int~
        -이전만남쌍교환조정(배치목록: List~int~) List~int~
    }
    class InterestRegistrationDB["관심등록DB"]
    class ArrangementDB["배치DB"]
    class OwnerUI["사장님UI"]
    class ApplicationDB["신청DB"]
    class AttendanceDB["출석DB"]
    class ProfileDB["프로필DB"]
    class StudentUI["학생UI"]
    CloseStudentNotification -- InterestRegistrationDB
    SeatArrangementGeneration -- ArrangementDB
    SeatArrangementGeneration -- OwnerUI
    SeatArrangementGeneration -- ApplicationDB
    SeatArrangementGeneration -- AttendanceDB
    SeatArrangementGeneration -- ProfileDB
    CloseStudentNotification -- StudentUI
```

### 3.3 모임 중: 출석·교류 (기능 5, 6, 7, 8)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class QRAttendance["QR출석"] {
        -모임ID: int
        -학생ID: int
        -테이블번호: int
        +상호QR스캔요청(학생1ID: int, 학생2QR토큰: String, 모임ID: int)
        +사장님확인스캔요청(사장님ID: int, 학생QR토큰: String, 모임ID: int)
        -QR토큰검증(QR토큰: String) boolean
    }
    class SinglePersonTableMerge["1인잔류테이블합석"] {
        -모임ID: int
        -1인잔류테이블목록: List~int~
        +출석가능시간종료됨(모임ID: int)
        -대상테이블선정(혼자출석학생ID: int, 후보목록: List~int~) int
    }
    class ProfileTopicCard["프로필기반대화주제카드"] {
        -모임ID: int
        -테이블번호: int
        -사용한태그목록: List~String~
        -같은테이블출석학생목록: List~int~
        -현재관심사태그: String
        -추측답목록: List~int~
        -정답학생목록: List~int~
        +대화카드시작선택(학생ID: int, 모임ID: int, 테이블번호: int)
        +추측답제출(학생ID: int, 선택학생ID: int)
        +그만하기선택(학생ID: int)
        +다음카드선택(학생ID: int)
        -질문태그선택(태그목록: List~String~, 사용한태그목록: List~String~) String
    }
    class BlindProfileDisclosure["블라인드프로필공개"] {
        -모임ID: int
        -테이블번호: int
        -현재단계: int
        +정보공개동의(학생ID: int, 모임ID: int, 테이블번호: int, 현재단계: int)
        -동의기록및집계(학생ID: int, 현재단계: int) int
        -동의상태초기화(테이블번호: int)
    }
    class MeetingDB["모임DB"]
    class ArrangementDB["배치DB"]
    class OwnerUI["사장님UI"]
    class OrderDB["주문DB"]
    class QuestionCardDB["질문카드DB"]
    class AttendanceDB["출석DB"]
    class TableAttendanceStatus["테이블출석현황"]
    class ProfileDB["프로필DB"]
    class StudentUI["학생UI"]
    SinglePersonTableMerge -- MeetingDB
    SinglePersonTableMerge -- ArrangementDB
    SinglePersonTableMerge -- OwnerUI
    SinglePersonTableMerge -- TableAttendanceStatus
    SinglePersonTableMerge -- ProfileDB
    SinglePersonTableMerge -- StudentUI
    QRAttendance -- ArrangementDB
    QRAttendance -- OwnerUI
    QRAttendance -- OrderDB
    QRAttendance -- AttendanceDB
    QRAttendance -- TableAttendanceStatus
    QRAttendance -- StudentUI
    BlindProfileDisclosure -- TableAttendanceStatus
    BlindProfileDisclosure -- ProfileDB
    BlindProfileDisclosure -- StudentUI
    ProfileTopicCard -- QuestionCardDB
    ProfileTopicCard -- TableAttendanceStatus
    ProfileTopicCard -- ProfileDB
    ProfileTopicCard -- StudentUI
```

### 3.4 모임 중: 기부·품앗이·화장실 (기능 16, 17, 18-1, 18-2)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class DonationRelay["기부릴레이잇기"] {
        -참여인원: int
        +최종배치저장됨(모임ID: int)
        +릴레이잇기선택(학생ID: int, 모임ID: int)
        +기부참여거절선택(학생ID: int, 요청학생ID: int)
        +기부참여선택(학생ID: int, 모임ID: int, 요청학생ID: int)
        -참여인원계산(참여인원: int) int
    }
    class StoreFoodExchange["가게연합음식품앗이"] {
        -교환ID: int
        -모임ID: int
        -상대모임ID: int
        -학생ID: int
        -상대학생ID: int
        +음식품앗이등록제출(학생ID: int, 모임ID: int, 상대모임ID: int, 상대학생ID: int, 음식명: String, 수량: int)
        +교환거절선택(교환ID: int)
        +교환수락선택(교환ID: int)
        +수령확인선택(학생ID: int, 교환ID: int)
    }
    class ToiletWaitAndGroup["화장실대기및조편성"] {
        -기준시각: datetime
        -대기학생목록: List~화장실대기학생~
        +소변입장신청(학생ID: int, 모임ID: int)
        -방광게이지계산(술주문병수: int, 출석인원: int) double
        -대기조편성(대기학생목록: List~화장실대기학생~, 설비정원: int) List~int~
    }
    class ToiletEntryExitManagement["화장실입장및퇴실관리"] {
        -입장학생목록: List~int~
        +화장실비어있음저장됨(모임ID: int)
        +해결완료선택(학생ID: int, 모임ID: int)
        +빈상태확인(모임ID: int)
    }
    class StoreDB["가게DB"]
    class DonationDB["기부DB"]
    class MeetingDB["모임DB"]
    class ArrangementDB["배치DB"]
    class OwnerUI["사장님UI"]
    class OrderDB["주문DB"]
    class AttendanceDB["출석DB"]
    class TableAttendanceStatus["테이블출석현황"]
    class FoodExchangeDB["품앗이DB"]
    class StudentUI["학생UI"]
    class ToiletConfig["화장실구성"]
    class ToiletQueueDB["화장실대기열DB"]
    class ToiletQueueStatus["화장실대기열현황"]
    class ToiletWaitStudent["화장실대기학생"]
    ToiletWaitAndGroup -- StoreDB
    ToiletEntryExitManagement -- StoreDB
    StoreFoodExchange -- MeetingDB
    StoreFoodExchange -- OwnerUI
    StoreFoodExchange -- OrderDB
    StoreFoodExchange -- AttendanceDB
    StoreFoodExchange -- FoodExchangeDB
    StoreFoodExchange -- StudentUI
    DonationRelay -- DonationDB
    DonationRelay -- ArrangementDB
    DonationRelay -- AttendanceDB
    DonationRelay -- TableAttendanceStatus
    DonationRelay -- StudentUI
    ToiletWaitAndGroup -- MeetingDB
    ToiletEntryExitManagement -- MeetingDB
    ToiletWaitAndGroup -- ArrangementDB
    ToiletEntryExitManagement -- OwnerUI
    ToiletWaitAndGroup -- OrderDB
    ToiletWaitAndGroup -- AttendanceDB
    ToiletWaitAndGroup -- TableAttendanceStatus
    ToiletWaitAndGroup -- StudentUI
    ToiletEntryExitManagement -- StudentUI
    ToiletWaitAndGroup -- ToiletConfig
    ToiletEntryExitManagement -- ToiletConfig
    ToiletWaitAndGroup -- ToiletQueueDB
    ToiletWaitAndGroup -- ToiletQueueStatus
    ToiletWaitAndGroup -- ToiletWaitStudent
    ToiletEntryExitManagement -- ToiletQueueDB
```

### 3.5 모임 후: 정산·평가·신고 (기능 9, 10, 11, 12, 13)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class AutoSettlement["자동정산"] {
        +모임종료시각도달(모임ID: int)
        -환급액계산(테이블주문금액: int, 참가비합: int, 출석인원: int) int
    }
    class MeetingEvaluation["만난사람평가"] {
        -갱신전매너점수목록: List~double~
        +모임종료저장됨(모임ID: int)
        +평가완료선택(평가자ID: int, 모임ID: int, 평가받는학생ID목록: List~int~, 평가점수목록: List~int~)
        -매너점수계산(기존점수: double, 받은점수목록: List~int~, 평가자점수목록: List~double~) double
    }
    class CloseStudentRegistration["친해지고싶은학생등록"] {
        +평가저장됨(학생ID: int, 모임ID: int)
        +건너뛰기선택(학생ID: int)
        +친해지기선택(등록학생ID: int, 대상학생ID: int)
    }
    class MannerReport["비매너학생신고"] {
        +비매너학생신고선택(학생ID: int, 모임ID: int)
        +신고건너뛰기선택(학생ID: int)
        +신고하기선택(신고학생ID: int, 피신고학생ID: int)
        +신고제출(신고학생ID: int, 피신고학생ID: int, 모임ID: int, 신고사유: String, 상세내용: String)
        -신고입력값검증(신고사유: String, 상세내용: String) boolean
    }
    class MannerSuspension["비매너학생이용정지"] {
        +신고심사(신고ID: int, 대상학생ID: int, 심사결과: 신고심사결과, 정지사유: String)
    }
    class PaymentDB["결제DB"]
    class InterestRegistrationDB["관심등록DB"]
    class MeetingDB["모임DB"]
    class ArrangementDB["배치DB"]
    class ReportDB["신고DB"]
    class ApplicationDB["신청DB"]
    class SuspensionDB["정지DB"]
    class OrderDB["주문DB"]
    class AttendanceDB["출석DB"]
    class TableAttendanceStatus["테이블출석현황"]
    class EvaluationDB["평가DB"]
    class ProfileDB["프로필DB"]
    class StudentUI["학생UI"]
    MannerSuspension -- PaymentDB
    AutoSettlement -- PaymentDB
    CloseStudentRegistration -- InterestRegistrationDB
    MeetingEvaluation -- AttendanceDB
    MeetingEvaluation -- TableAttendanceStatus
    MeetingEvaluation -- EvaluationDB
    MeetingEvaluation -- ProfileDB
    MeetingEvaluation -- StudentUI
    AutoSettlement -- MeetingDB
    AutoSettlement -- ArrangementDB
    MannerReport -- ReportDB
    MannerReport -- TableAttendanceStatus
    MannerReport -- ProfileDB
    MannerReport -- StudentUI
    MannerSuspension -- ReportDB
    MannerSuspension -- ApplicationDB
    MannerSuspension -- SuspensionDB
    MannerSuspension -- ProfileDB
    MannerSuspension -- StudentUI
    AutoSettlement -- OrderDB
    AutoSettlement -- TableAttendanceStatus
    AutoSettlement -- StudentUI
    CloseStudentRegistration -- TableAttendanceStatus
    CloseStudentRegistration -- ProfileDB
    CloseStudentRegistration -- StudentUI
```

### 3.6 모임 후: 귀가·예보·2차 (기능 15, 19, 20)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class SafeReturnHome["당일안심귀가"] {
        -모임종료시각: datetime
        -귀가마감시각: datetime
        +모임종료시각도달(모임ID: int)
        +안전응답선택(학생ID: int)
        -귀가마감시각계산(모임종료시각: datetime, 추정이동시간: int) datetime
    }
    class HangoverForecast["숙취예보"] {
        -모임종료시각: datetime
        -숙취지수: int
        +익일08시도달()
        -숙취지수계산(술주문병수: int, 출석인원: int, 모임종료시각: datetime) int
    }
    class SecondRoundAutoDecision["2차참가자동결정"] {
        -모임ID: int
        -응답목록: List~참가응답~
        -이번참가비율: double
        -결과목록: List~참가결과~
        +2차공지등록됨(모임ID: int)
        +참가응답제출(학생ID: int, 선택: 참가선택)
        -응답별결정(응답목록: List~참가응답~)
        -참가비율계산(참가수: int, 알림수: int) double
        -불참결정(학생ID: int)
        -참가여부결정(과거2차참가율: double, 이번참가비율: double) 2차참가결과
    }
    class SecondNotice["2차공지"]
    class SecondNoticeDB["2차공지DB"]
    class SecondRecordDB["2차기록DB"]
    class StoreDB["가게DB"]
    class ReturnHomeTimeCalc["귀가시간계산"]
    class MeetingDB["모임DB"]
    class ArrangementDB["배치DB"]
    class OwnerUI["사장님UI"]
    class OrderDB["주문DB"]
    class ParticipationResult["참가결과"]
    class ParticipationRecord["참가기록"]
    class ParticipationResponse["참가응답"]
    class AttendanceDB["출석DB"]
    class TableAttendanceStatus["테이블출석현황"]
    class ProfileDB["프로필DB"]
    class StudentUI["학생UI"]
    class StudentEmergencyContact["학생비상연락정보"]
    SecondRoundAutoDecision -- SecondNotice
    SecondRoundAutoDecision -- SecondNoticeDB
    SecondRoundAutoDecision -- SecondRecordDB
    SecondRoundAutoDecision -- ReturnHomeTimeCalc
    SecondRoundAutoDecision -- OwnerUI
    SecondRoundAutoDecision -- ParticipationResult
    SecondRoundAutoDecision -- ParticipationRecord
    SecondRoundAutoDecision -- ParticipationResponse
    SecondRoundAutoDecision -- AttendanceDB
    SecondRoundAutoDecision -- StudentUI
    HangoverForecast -- StoreDB
    SafeReturnHome -- ReturnHomeTimeCalc
    SafeReturnHome -- MeetingDB
    SafeReturnHome -- AttendanceDB
    SafeReturnHome -- ProfileDB
    SafeReturnHome -- StudentUI
    SafeReturnHome -- StudentEmergencyContact
    HangoverForecast -- MeetingDB
    HangoverForecast -- ArrangementDB
    HangoverForecast -- OrderDB
    HangoverForecast -- TableAttendanceStatus
    HangoverForecast -- StudentUI
```

### 3.7 공통 객체·외부

```mermaid
classDiagram
    direction LR
    class ReturnHomeTimeCalc["귀가시간계산"] {
        -굴곡계수: double = 1.3
        -도보기준거리: double = 1.5
        -도보속도: double = 4
        -차량속도: double = 25
        +이동시간추정(학생ID: int) int
        -이동시간계산(현재위치: Point, 자택위치: Point) int
    }
    class TableAttendanceStatus["테이블출석현황"] {
        +테이블출석인원조회(모임ID: int, 테이블번호: int) int
        +테이블별출석조회(모임ID: int) List~int~
        +같은테이블학생조회(학생ID: int, 모임ID: int) List~int~
        +테이블출석학생목록조회(모임ID: int, 테이블번호: int) List~int~
    }
    class DeviceLocation["단말기위치정보"] {
        +현재위치조회(학생ID: int) Point
    }
```

### 3.8 DB: 회원·모임

```mermaid
classDiagram
    direction LR
    class ProfileDB["프로필DB"] {
        +자택위치조회(학생ID: int) Point
        +계정상태조회(학생ID: int) 계정상태
        +학번조회(학생ID: int) String
        +학생학과학번목록조회(학생ID목록: List~int~) List~String~
        +관심사태그목록조회(학생ID목록: List~int~) List~String~
        +관심사보유학생조회(학생ID목록: List~int~, 관심사태그: String) List~int~
        +남은관심사태그여부조회(학생ID목록: List~int~, 사용한태그목록: List~String~) boolean
        +단계별프로필항목조회(학생ID목록: List~int~, 단계: int) List~String~
        +프로필사진조회(학생ID: int) String
        +매너점수조회(학생ID: int) double
        +매너점수갱신(학생ID: int, 매너점수: double)
        +계정상태변경(학생ID: int, 상태: 계정상태)
        +학생비상연락정보조회(학생ID: int) 학생비상연락정보
    }
    class SuspensionDB["정지DB"] {
        +정지기록조회(학생ID: int) boolean
        +정지저장(학생ID: int, 정지사유: String)
    }
    class StoreDB["가게DB"] {
        +가게등록여부조회(사장님ID: int, 가게ID: int) boolean
        +화장실설비구성조회(가게ID: int) 화장실구성
        +제휴쿠폰조회(가게ID: int) String
    }
    class MeetingDB["모임DB"] {
        +중복요청조회(요청식별자: String) boolean
        +모임공지저장(가게ID: int, 모임이름: String, 시작시각: datetime, 모임종료시각: datetime, 모집정원: int, 기본참가비: int, 품앗이참여여부: boolean, 요청식별자: String) int
        +모임상태조회(모임ID: int) 모임상태
        +시작시각조회(모임ID: int) datetime
        +기본참가비조회(모임ID: int) int
        +모임상태변경(모임ID: int, 상태: 모임상태)
        +가게ID조회(모임ID: int) int
        +모임종료시각조회(모임ID: int) datetime
        +전일종료모임목록조회() List~int~
    }
    class ApplicationDB["신청DB"] {
        +중복신청조회(학생ID: int, 모임ID: int) boolean
        +신청저장(학생ID: int, 모임ID: int, 상태: 신청상태)
        +선발학생목록조회(모임ID: int) List~int~
        +미시작결제완료신청목록조회(학생ID: int) List~int~
        +신청상태변경(학생ID: int, 모임ID: int, 상태: 신청상태)
    }
    class PaymentDB["결제DB"] {
        +결제승인기록저장(학생ID: int, 모임ID: int, 결제금액: int)
        +테이블참가비합조회(모임ID: int, 테이블번호: int) int
        +환급액저장(학생ID: int, 모임ID: int, 환급액: int)
        +참가비전액환급저장(학생ID: int, 모임ID: int)
    }
```

### 3.9 DB: 모임 진행

```mermaid
classDiagram
    direction LR
    class InterestRegistrationDB["관심등록DB"] {
        +관심등록학생조회(학생ID: int) List~int~
        +관심등록여부조회(등록학생ID: int, 대상학생ID: int) boolean
        +관심등록저장(등록학생ID: int, 대상학생ID: int)
    }
    class ArrangementDB["배치DB"] {
        +배치조회(모임ID: int) List~int~
        +이전모임테이블조회(학생ID목록: List~int~) List~int~
        +배치저장(모임ID: int, 배치목록: List~int~)
        +테이블목록조회(모임ID: int) List~int~
        +최종배치저장(모임ID: int, 최종배치목록: List~int~)
        +학생배정모임조회(학생ID목록: List~int~) List~int~
        +학생테이블번호조회(학생ID: int, 모임ID: int) int
        +테이블배치및의자조회(모임ID: int) List~int~
        +추가의자갱신(모임ID: int, 테이블번호: int)
        +테이블번호갱신(학생ID: int, 모임ID: int, 새테이블번호: int)
    }
    class AttendanceDB["출석DB"] {
        +출석학생조회(모임ID: int) List~int~
        +이전출석기록조회(학생ID목록: List~int~) List~int~
        +상호출석기록저장(학생1ID: int, 학생2ID: int, 모임ID: int, 방식: 출석방식)
        +출석기록저장(학생ID: int, 모임ID: int, 방식: 출석방식)
        +테이블출석조회(모임ID: int, 테이블번호: int) List~int~
        +출석시각조회(학생ID: int, 모임ID: int) datetime
        +출석여부조회(학생ID: int, 모임ID: int) boolean
    }
    class OrderDB["주문DB"] {
        +주문가능상태갱신(모임ID: int, 테이블번호: int)
        +주문마감(모임ID: int)
        +테이블주문금액조회(모임ID: int, 테이블번호: int) int
        +주문잔량조회(모임ID: int, 음식명: String) int
        +특정시각이후술주문병수조회(모임ID: int, 테이블번호: int, 기준시각: datetime) int
        +테이블술주문병수조회(모임ID: int, 테이블번호: int) int
    }
    class QuestionCardDB["질문카드DB"] {
        +관심사질문카드조회(관심사태그: String) String
    }
    class ToiletQueueDB["화장실대기열DB"] {
        +대기상태조회(학생ID: int, 모임ID: int) 화장실대기상태
        +마지막이용시각조회(학생ID: int, 모임ID: int) datetime
        +대기등록(학생ID: int, 모임ID: int, 방광게이지: double) int
        +대기조수및대기목록조회(모임ID: int) 화장실대기열현황
        +대기조상태변경(편성학생목록: List~int~, 조번호: int)
        +첫번째대기조조회(모임ID: int) List~int~
        +선착순대기학생목록조회(모임ID: int, 설비정원: int) List~int~
        +화장실상태변경(모임ID: int, 상태: 화장실상태)
        +학생상태변경(입장학생목록: List~int~, 상태: 화장실대기상태)
        +다음대기조앞당김(모임ID: int)
        +해결완료기록및전원완료여부조회(모임ID: int, 학생ID: int) boolean
        +퇴실처리및화장실비어있음갱신(모임ID: int, 퇴실시각: datetime)
    }
```

### 3.10 DB: 평가·교류

```mermaid
classDiagram
    direction LR
    class EvaluationDB["평가DB"] {
        +평가저장(평가자ID: int, 모임ID: int, 평가받는학생ID목록: List~int~, 평가점수목록: List~int~)
        +테이블평가전원제출여부조회(학생ID목록: List~int~, 모임ID: int) boolean
        +받은점수목록조회(학생ID: int, 평가자ID목록: List~int~, 모임ID: int) List~int~
    }
    class ReportDB["신고DB"] {
        +신고저장(신고학생ID: int, 피신고학생ID: int, 모임ID: int, 신고사유: String, 상세내용: String) int
        +심사결과저장(신고ID: int, 심사결과: 신고심사결과)
        +누적유효신고건수조회(대상학생ID: int) int
    }
    class DonationDB["기부DB"] {
        +바통보유여부조회(학생ID: int) boolean
        +모임참여이력조회(학생ID: int, 모임ID: int) boolean
        +기부기록및새바통저장(학생ID: int, 모임ID: int)
        +기존바통회수(요청학생ID: int)
    }
    class FoodExchangeDB["품앗이DB"] {
        +취소제외교환수량조회(모임ID: int, 음식명: String) int
        +연합가능여부조회(모임ID: int, 상대모임ID: int) boolean
        +교환요청저장(모임ID: int, 상대모임ID: int, 학생ID: int, 상대학생ID: int, 음식명: String, 수량: int) int
        +교환상태갱신(교환ID: int, 상태: 교환상태)
        +교환상태조회(교환ID: int) 교환상태
        +수령확인저장(학생ID: int, 교환ID: int)
        +전원수령확인여부조회(교환ID: int) boolean
    }
    class SecondNoticeDB["2차공지DB"] {
        +2차공지조회(모임ID: int) 2차공지
    }
    class SecondRecordDB["2차기록DB"] {
        +과거참가기록조회(학생ID: int) 참가기록
        +결과저장(모임ID: int, 결과목록: List~참가결과~)
    }
```

### 3.11 사장님UI·엔티티

```mermaid
classDiagram
    direction LR
    class OwnerUI["사장님UI"] {
        +알림대상없음알림(모임ID: int)
        +참가인원알림(모임ID: int, 참가인원: int)
        +등록실패알림(사유: String)
        +기존공지반환(요청식별자: String)
        +모임공지반환(모임ID: int)
        +테이블구성알림(모임ID: int, 테이블수: int, 테이블별인원: List~int~)
        +출석실패알림(사장님ID: int, 사유: String)
        +모임취소알림(모임ID: int)
        +의자추가알림(모임ID: int, 테이블번호: int)
        +교환취소알림(모임ID: int, 교환ID: int)
        +교환확정알림(모임ID: int, 교환ID: int)
        +품앗이완료알림(모임ID: int, 교환ID: int)
        +화장실확인요청알림(모임ID: int)
    }
    class ParticipationRecord["참가기록"] {
        -참가횟수: int
        -알림받은횟수: int
    }
    class ParticipationResponse["참가응답"] {
        -학생ID: int
        -선택: 참가선택
    }
    class ParticipationResult["참가결과"] {
        -학생ID: int
        -모임ID: int
        -결과: 2차참가결과
    }
    class Point["Point"] {
        -위도: double
        -경도: double
    }
    class SecondNotice["2차공지"] {
        -대상모임ID: int
        -2차장소: String
        -시작시각: datetime
    }
    class StudentEmergencyContact["학생비상연락정보"] {
        -이름: String
        -학번: String
        -비상연락처: String
    }
    class ToiletConfig["화장실구성"] {
        -소변기수: int
        -대변기수: int
    }
    class ToiletQueueStatus["화장실대기열현황"] {
        -대기조수: int
        -대기학생목록: List~화장실대기학생~
    }
    class ToiletWaitStudent["화장실대기학생"] {
        -학생ID: int
        -등록시각: datetime
        -방광게이지: double
    }
```

### 3.12 학생UI

```mermaid
classDiagram
    direction LR
    class StudentUI["학생UI"] {
        +참가선택요청(학생ID목록: List~int~, 2차장소: String, 시작시각: datetime)
        +결과알림(학생ID: int, 결과: 2차참가결과)
        +알림대상없음알림(학생ID: int)
        +모임신청알림(학생ID: int, 모임ID: int)
        +모임공지화면표시(모임ID: int)
        +모임공지목록갱신(모임ID: int)
        +신청불가알림(사유: String)
        +신청마감알림(모임ID: int)
        +중복신청불가알림(모임ID: int)
        +계정정지안내표시및강제종료(학생ID: int)
        +참가비계산불가알림(학생ID: int)
        +참가비안내표시(학년: int, 참가비: int)
        +결제실패알림(사유: String)
        +신청완료알림(모임ID: int)
        +출석실패알림(학생ID: int, 사유: String)
        +출석완료및주문가능알림(학생ID: int, 테이블번호: int)
        +출석완료알림(학생ID: int, 테이블번호: int)
        +바뀐테이블번호알림(학생ID: int, 바뀐테이블번호: int)
        +질문카드표시(학생ID: int, 질문내용: String, 후보목록: List~int~)
        +정답공개알림(학생ID: int, 정답학생목록: List~int~, 맞힘여부: boolean)
        +이야기공유요청(학생ID: int, 관심사태그: String)
        +게임종료알림(학생ID: int)
        +동의현황표시(동의수: int, 출석인원: int)
        +프로필항목공개표시(단계: int, 항목목록: List~String~)
        +환급알림(학생ID: int, 환급액: int)
        +평가화면표시(학생ID: int, 대상학생목록: List~int~, 프로필사진목록: List~String~)
        +평가제출완료알림(학생ID: int)
        +관심학생등록화면표시(대상학생목록: List~int~, 프로필사진목록: List~String~)
        +등록생략알림(학생ID: int)
        +중복등록알림(등록학생ID: int)
        +등록완료알림(등록학생ID: int)
        +신고대상목록표시(대상학생목록: List~int~, 프로필사진목록: List~String~)
        +신고생략알림(학생ID: int)
        +신고작성창표시(피신고학생ID: int)
        +입력오류알림(학생ID: int)
        +신고접수완료알림(학생ID: int)
        +이용정지알림(학생ID: int, 정지사유: String)
        +귀가모니터링시작알림(학생ID: int, 귀가마감시각: datetime)
        +안전귀가알림(학생ID: int)
        +안전확인요청알림(학생ID: int)
        +릴레이잇기버튼활성화(학생ID: int)
        +릴레이잇기버튼비활성화(학생ID: int)
        +기부참여요청(학생ID: int, 요청학생ID: int)
        +참여불가알림(학생ID: int)
        +릴레이결과알림(요청학생ID: int, 참여인원: int)
        +검증실패알림(학생ID: int, 사유: String)
        +교환요청전달(상대학생ID: int, 교환ID: int, 음식명: String, 수량: int)
        +교환취소알림(학생ID: int, 교환ID: int)
        +교환확정알림(학생ID: int, 교환ID: int)
        +품앗이완료알림(학생ID: int, 교환ID: int)
        +대기순번표시(학생ID: int, 대기순번: int)
        +등록불가알림(학생ID: int, 사유: String)
        +대기조순번알림(학생ID: int, 조번호: int)
        +화장실입장알림(학생ID: int)
        +숙취예보및쿠폰알림(학생ID: int, 숙취지수: int, 쿠폰: String)
        +숙취예보알림(학생ID: int, 숙취지수: int)
    }
```

### 3.13 공통 객체·DB·엔티티 사이의 관계선 (참고용)

```mermaid
---
config:
  class:
    hideEmptyMembersBox: true
---
classDiagram
    direction LR
    class SecondNotice["2차공지"]
    class SecondNoticeDB["2차공지DB"]
    class SecondRecordDB["2차기록DB"]
    class Point["Point"]
    class StoreDB["가게DB"]
    class ReturnHomeTimeCalc["귀가시간계산"]
    class DeviceLocation["단말기위치정보"]
    class ArrangementDB["배치DB"]
    class ParticipationResult["참가결과"]
    class ParticipationRecord["참가기록"]
    class AttendanceDB["출석DB"]
    class TableAttendanceStatus["테이블출석현황"]
    class ProfileDB["프로필DB"]
    class StudentEmergencyContact["학생비상연락정보"]
    class ToiletConfig["화장실구성"]
    class ToiletQueueDB["화장실대기열DB"]
    class ToiletQueueStatus["화장실대기열현황"]
    class ToiletWaitStudent["화장실대기학생"]
    SecondNotice -- SecondNoticeDB
    SecondRecordDB -- ParticipationResult
    SecondRecordDB -- ParticipationRecord
    Point -- ReturnHomeTimeCalc
    Point -- DeviceLocation
    Point -- ProfileDB
    StoreDB -- ToiletConfig
    ReturnHomeTimeCalc -- DeviceLocation
    ReturnHomeTimeCalc -- ProfileDB
    ArrangementDB -- TableAttendanceStatus
    AttendanceDB -- TableAttendanceStatus
    ProfileDB -- StudentEmergencyContact
    ToiletQueueDB -- ToiletQueueStatus
    ToiletQueueDB -- ToiletWaitStudent
    ToiletQueueStatus -- ToiletWaitStudent
```

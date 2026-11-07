# Claude Code 작업 지침

이 저장소는 소프트웨어공학 팀 프로젝트(징검다리)의 설계 문서 저장소다. 답변과 문서는 한국어로 쓴다.

## 작업 시작 전에 최신 내용 받기

- 파일을 읽거나 고치기 전에 먼저 `git pull`을 실행해 다른 팀원의 변경을 받는다 (CONVENTIONS 9장).
- 결과가 "Already up to date"가 아니면 무엇이 바뀌었는지(`git log`) 확인하고 사용자에게 알린 뒤 작업한다.
- pull이 실패하거나 충돌이 나면 작업을 시작하지 말고 사용자에게 알린다.

## 작업 전에 반드시 읽을 것

1. `CONVENTIONS.md` — 모든 작성 규칙. 이 규칙이 최우선이다.
2. `GLOSSARY.md` — 쓸 수 있는 용어·객체·DB·enum·자료형 목록.
3. 예시: `requirements/req-20.md`, `sequence/seq-20.md`, `classes/SecondRoundAutoDecision.md`

## 지켜야 할 것

- GLOSSARY.md에 없는 용어·객체·DB·enum을 만들지 않는다. 꼭 필요하면 먼저 사용자에게 제안하고, 승인되면 GLOSSARY.md에 `추가` 상태로 등록한다. 본문에는 `[추가]` 같은 표시를 붙이지 않는다.
- 객체·DB·UI·enum 값·메시지 이름은 공백 없이 쓴다. 객체 이름에 약어나 스테레오타입을 붙이지 않는다.
- 요구사항에 다른 기능을 실행·전달하는 표현을 쓰지 않는다 (Action, Pre/Post-condition, Side effects 모두).
- 조회는 "어느 DB에서 무엇을 조회해 무엇을 한다"로 쓰고, 모든 조건에 else 동작을 쓴다.
- 계산식은 ceil·floor·min 같은 기호 대신 한글로 풀어 쓴다.
- GLOSSARY 9장 "쓰지 않는 표기"에 있는 말은 대표 용어로 바꿔 쓴다.
- 새 연산을 만들기 전에 해당 클래스 파일을 열어 재사용할 연산이 있는지 확인한다 (CONVENTIONS 6.4).
- `docs/`의 팀 PPT(User_Requirement.pdf)와 Claude Docs 초안은 참고 자료다. 원본은 이 저장소의 파일이다.
- 요구사항을 나눌 때는 시작 조건으로 나누고, 객체(책임)로 나누지 않는다.
- Pre-condition에 쓴 DB 상태를 만드는 요구사항이 없으면 ASSUMED-FEATURES.md에 있는지 확인하고, 없으면 사용자에게 알린다.
- 흔한 기능처럼 보여도 요구사항을 직접 빼거나 합치지 않는다. 후보와 이유를 제안하고 팀이 정하면 반영한다 (CONVENTIONS 4.6, FEEDBACK #4·#13).
- 시퀀스 다이어그램은 Mermaid로 쓰고, 시작 메시지 규칙(사람→UI, 시각→시간 액터, 데이터 변화→Found Message)을 지킨다.

## 하나를 고치면 같이 고칠 것

| 고친 것 | 같이 고칠 것 |
|---|---|
| 요구사항 Action | 시퀀스 메시지, 대응표 |
| 시퀀스 메시지 추가·수정·삭제 | 받는 클래스 파일의 연산과 사용처, 관계 |
| 새 객체·엔티티 | classes/ 파일 생성, GLOSSARY 등록 |
| 새 용어·enum | GLOSSARY 등록 |
| 기능 추가 | usecase/usecase.md, README 담당 표 |
| 기능 삭제 (팀 결정 후) | requirements·sequence 파일 삭제, README 담당 표, usecase 줄, GLOSSARY 담당 객체·사용처, 그 기능을 언급한 다른 요구사항. 번호는 다시 매기지 않는다 |

## 작업 끝나기 전에 확인

- `CHECKLIST.md`의 체크리스트를 모두 확인하고, 통과하지 못한 항목을 사용자에게 알린다.
- 브랜치·PR 없이 main에서 작업하고 main에 push한다. push 전에 `git pull`로 다른 사람의 변경을 합친다.
- 같은 메서드 이름이 다른 클래스 파일과 충돌하지 않는지, 사용처가 정확한지 확인한다.
- Mermaid 문법이 깨지지 않았는지 확인한다 (가능하면 `mmdc`로 렌더링).
- 규칙(CONVENTIONS.md)을 바꿔야 할 것 같으면 직접 바꾸지 말고 사용자에게 먼저 제안한다.

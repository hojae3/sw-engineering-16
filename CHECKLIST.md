# push 전 체크리스트

main에 push하기 전에 바꾼 파일을 아래 항목으로 확인한다.

### 요구사항
- [ ] Action 1에 시작 조건이 있다
- [ ] 조회마다 어느 DB인지 썼다
- [ ] 모든 조건에 else 동작이 있다
- [ ] 다른 기능을 실행·전달하는 표현이 없다 (Action, Pre/Post-condition, Side effects 모두)
- [ ] Side effects가 시스템 영향이다
- [ ] Pre-condition의 DB 상태를 만드는 요구사항이 있거나, 없으면 ASSUMED-FEATURES.md에 있다
- [ ] 계산식을 한글로 풀어 썼다

### 시퀀스
- [ ] 객체 이름이 GLOSSARY 표기와 같다 (공백·약어·스테레오타입 없음)
- [ ] 시작 메시지가 규칙(5.2)에 맞다
- [ ] 매개변수가 `이름: 자료형`이고 List는 `List<타입>`이다
- [ ] 메시지 ↔ Action 대응표가 있다
- [ ] GitHub 미리보기에서 Mermaid 그림이 깨지지 않는다

### 클래스·용어
- [ ] 메시지를 받는 클래스 파일에 연산을 추가·수정했다 (사용처 포함)
- [ ] 새 용어·객체·enum을 GLOSSARY.md에 등록했다
- [ ] usecase/usecase.md를 반영했다

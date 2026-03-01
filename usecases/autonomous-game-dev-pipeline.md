# 자율 게임 개발 파이프라인

## 문제점
풀타임 개발팀 없이 딸을 위한 안전하고 광고 없는 교육용 게임 포털(40개 이상 게임)을 만들고 싶었습니다.

## 기능 설명
7분마다 새 게임을 만들거나 버그를 수정하는 "게임 개발 에이전트". 버그 우선 정책 적용 — 알파벳 순서로 첫 번째 버그를 먼저 수정한 후 새 게임 개발.

**사이클당 작업:**
1. `development-queue.md`에서 라운드 로빈으로 다음 게임 선택
2. HTML5/CSS3/JS 구현 (프레임워크 없음, 모바일 퍼스트, 오프라인 지원)
3. `games-list.json`에 게임 등록
4. `CHANGELOG.md`, `master-game-plan.md` 업데이트
5. Git 관리: fetch, 브랜치(`feature/[game-id]`), 커밋, 병합

## 프롬프트

```
웹 게임 개발 및 아동 UX 전문가로서 행동하세요.
목표는 프로덕션 큐의 다음 게임을 개발하는 것입니다.

다음을 읽고 분석하세요:
1. 버그 컨텍스트 (최우선): @[bugs/] — 파일 존재 시 알파벳 첫 번째 버그만 수정
2. 큐 컨텍스트: @[development-queue.md] — [NEXT]로 표시된 게임
3. 설계 규칙: @[game-design-rules.md] — 순수 HTML/CSS/JS, 폴더 구조, 모바일
4. 게임 사양: game-id 기반으로 games-backlog/ 참조
5. 중앙 레지스트리: @[public/js/games-list.json]

작업:
0. 버그 우선 — fix/... 브랜치에서 알파벳 첫 번째 버그 수정 후 병합
1. git fetch && git pull origin master
2. git checkout -b feature/[game-id]
3. public/games/[game-id]/ 파일 생성
4. 백로그와 설계 규칙에 따라 로직 구현
5. games-list.json에 등록
6. CHANGELOG.md, master-game-plan.md, development-queue.md 업데이트
7. git commit, push, master로 병합
```

## 관련 링크
- [LinkedIn 개발 스토리](https://www.linkedin.com/feed/update/urn:li:activity:7429739200301772800/)
- [GitHub 저장소](https://github.com/duberblockito/elbebe/tree/master)
- [라이브 사이트](https://elbebe.co/)

## 필요한 스킬
- Git

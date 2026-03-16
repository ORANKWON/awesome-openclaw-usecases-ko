# 채팅에서 X/Twitter 자동화

자연어를 통한 완전한 X/Twitter 자동화 — OpenClaw 채팅에서 트윗 게시, 답글, 좋아요, 리트윗, 팔로우, DM, 검색, 데이터 추출, 경품 추첨, 계정 모니터링을 모두 수행합니다.

## 문제점

X/Twitter 존재감을 관리하려면 앱, 서드파티 대시보드, 분석 도구를 오가야 합니다. 경품 추첨을 실행하려면 수동으로 당첨자를 선택해야 합니다. 팔로워, 좋아요, 리트윗을 추출하려면 스크래핑 스크립트가 필요합니다. 이 모든 것을 대화형으로 할 수 있는 단일 인터페이스가 없습니다.

## 기능 설명

TweetClaw는 에이전트를 X/Twitter API에 연결하는 OpenClaw 플러그인입니다. 완전히 채팅을 통해 상호작용합니다:

- **게시 및 참여** — 트윗 작성, 스레드 답글, 좋아요, 리트윗, 팔로우/언팔로우, DM 전송
- **검색 및 추출** — 트윗과 사용자 검색, 팔로워, 좋아요, 리트윗, 인용 트윗, 리스트 멤버 추출
- **경품 추첨** — 구성 가능한 필터(최소 팔로워, 계정 나이, 키워드 요구사항)로 트윗 참여자 중 무작위 당첨자 선택
- **모니터** — 계정의 새 트윗이나 팔로워 변경을 감시하고 알림 받기

모든 작업은 관리형 API를 통해 이루어집니다 — 브라우저 쿠키 없음, 스크래핑 없음, 자격증명 노출 없음.

## 프롬프트

**플러그인 설치:**
```text
openclaw plugins install @xquik/tweetclaw
```

**트윗 게시:**
```text
트윗 게시: "새 기능을 출시했어요 — 사용해보세요!"
```

**경품 추첨 실행:**
```text
이 트윗의 리트윗한 사람 중 3명의 무작위 당첨자를 선택해줘: https://x.com/username/status/123456789. 팔로워가 50명 미만인 계정은 제외해줘.
```

**데이터 추출:**
```text
이 트윗에 좋아요를 누른 모든 사용자를 추출해서 CSV로 내보내줘: https://x.com/username/status/123456789
```

**계정 모니터:**
```text
@elonmusk를 모니터해서 새 트윗을 게시할 때마다 알려줘.
```

## 필요한 스킬

- [@xquik/tweetclaw](https://www.npmjs.com/package/@xquik/tweetclaw) — `openclaw plugins install @xquik/tweetclaw`로 설치

## 관련 링크

- [GitHub 저장소](https://github.com/Xquik-dev/tweetclaw)
- [npm 패키지](https://www.npmjs.com/package/@xquik/tweetclaw)

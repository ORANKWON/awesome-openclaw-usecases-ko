# Awesome OpenClaw 활용 사례 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 사람들이 실제로 OpenClaw를 일상에서 어떻게 활용하고 있는지 알아보세요.

OpenClaw 도입의 가장 큰 장벽은 스킬이나 도구가 부족한 것이 아닙니다. **내 삶에 어떻게 적용할지 모르는 것**입니다.

이 저장소는 검증된 실제 활용 사례를 모아둔 커뮤니티 큐레이션 목록입니다.

> ⚠️ **보안 주의사항**: 스킬과 서드파티 의존성에는 심각한 보안 취약점이 포함될 수 있습니다. 항상 스킬 소스 코드를 검토하고, 요청 권한을 확인하며, API 키를 하드코딩하지 마세요.

---

## 목차

- [소셜 미디어](#소셜-미디어)
- [창작 및 빌딩](#창작-및-빌딩)
- [인프라 및 DevOps](#인프라-및-devops)
- [생산성](#생산성)
- [리서치 및 학습](#리서치-및-학습)
- [금융 및 트레이딩](#금융-및-트레이딩)

---

## 소셜 미디어

| 사례 | 설명 |
|------|------|
| [일일 Reddit 다이제스트](usecases/daily-reddit-digest.md) | 좋아하는 서브레딧의 인기 게시물을 매일 오후 5시에 요약 |
| [일일 YouTube 다이제스트](usecases/daily-youtube-digest.md) | 구독 채널 및 키워드 기반으로 영상 자동 수집·요약 |
| [X 계정 분석](usecases/x-account-analysis.md) | 내 X 게시물의 바이럴 패턴과 주제별 인게이지먼트 분석 |
| [멀티소스 테크 뉴스 다이제스트](usecases/multi-source-tech-news-digest.md) | 100개 이상 소스(RSS, X, GitHub, 검색)에서 기술 뉴스 자동 수집·랭킹 |

## 창작 및 빌딩

| 사례 | 설명 |
|------|------|
| [자율 게임 개발 파이프라인](usecases/autonomous-game-dev-pipeline.md) | 7분마다 새 게임을 만들거나 버그를 수정하는 에이전트 |
| [YouTube 콘텐츠 파이프라인](usecases/youtube-content-pipeline.md) | 매시간 AI 뉴스 스캔, 영상 아이디어 제안, 중복 방지 |
| [콘텐츠 팩토리](usecases/content-factory.md) | Discord에서 리서치·스크립트·썸네일을 자동 생성하는 멀티에이전트 |
| [자율 미니앱 빌더](usecases/overnight-mini-app-builder.md) | 목표를 입력하면 밤새 자동으로 앱을 빌드 |
| [팟캐스트 제작 파이프라인](usecases/podcast-production-pipeline.md) | 녹음 전 조사·개요 작성, 녹음 후 쇼노트·소셜 콘텐츠 자동화 |

## 인프라 및 DevOps

| 사례 | 설명 |
|------|------|
| [n8n 워크플로우 오케스트레이션](usecases/n8n-workflow-orchestration.md) | OpenClaw가 n8n 웹훅을 생성하고 호출하는 프록시 패턴 |
| [자가 치유 홈 서버](usecases/self-healing-home-server.md) | SSH 접근, 자동 헬스 모니터링, 인프라 자가 수정 에이전트 |

## 생산성

| 사례 | 설명 |
|------|------|
| [자율 프로젝트 관리](usecases/autonomous-project-management.md) | 공유 STATE.yaml 기반 분산형 멀티에이전트 프로젝트 관리 |
| [멀티채널 고객 서비스](usecases/multi-channel-customer-service.md) | WhatsApp, Instagram, 이메일, 리뷰를 통합 처리하는 AI 고객 서비스 |
| [개인 CRM](usecases/personal-crm.md) | 이메일·캘린더 스캔으로 연락처와 상호작용을 자동 추적 |
| [건강 증상 트래커](usecases/health-symptom-tracker.md) | 하루 3번 텔레그램 알림으로 음식·증상 기록 및 상관관계 분석 |
| [동적 대시보드](usecases/dynamic-dashboard.md) | 병렬 서브에이전트로 GitHub, SNS, 시스템 지표를 실시간 집계 |
| [회의록 및 액션 아이템](usecases/meeting-notes-action-items.md) | 회의 녹취록을 자동 분석하여 Jira/Linear에 태스크 생성 |
| [멀티채널 어시스턴트](usecases/multi-channel-assistant.md) | Telegram, Slack, Google Workspace, Todoist를 하나로 통합 |
| [맞춤형 모닝 브리프](usecases/custom-morning-brief.md) | 매일 아침 뉴스, 일정, 할일, 추천 작업을 정리해 전송 |
| [멀티에이전트 팀](usecases/multi-agent-team.md) | 전략, 영업, 마케팅, 개발 역할을 가진 에이전트 팀 운영 |
| [받은편지함 정리](usecases/inbox-declutter.md) | 매일 저녁 뉴스레터 이메일을 요약해서 다이제스트로 전송 |
| [습관 트래커 및 코치](usecases/habit-tracker-accountability-coach.md) | 매일 체크인, 스트릭 추적, 주간 리포트 |
| [Todoist 작업 관리자](usecases/todoist-task-manager.md) | 에이전트 진행 상황을 Todoist에 실시간 동기화 |
| [가족 캘린더 및 가정 어시스턴트](usecases/family-calendar-household-assistant.md) | 가족 일정 통합, 메시지 모니터링, 식료품 재고 관리 |
| [이벤트 참석 확인 자동화](usecases/event-guest-confirmation.md) | SuperCall 플러그인으로 게스트에게 자동 전화 걸어 참석 확인 |
| [전화 기반 개인 어시스턴트](usecases/phone-based-personal-assistant.md) | 전화 통화로 캘린더 조회, Jira 업데이트, 웹 검색 |
| [프로젝트 상태 관리](usecases/project-state-management.md) | 이벤트 기반 프로젝트 상태 시스템으로 맥락과 결정 이력 보존 |
| [세컨드 브레인](usecases/second-brain.md) | 텍스트 메시지로 기억 저장, Next.js 대시보드로 검색 |

## 리서치 및 학습

| 사례 | 설명 |
|------|------|
| [실적 발표 트래커](usecases/earnings-tracker.md) | 주간 실적 발표 일정 모니터링, 결과 자동 요약 |
| [지식 베이스 RAG](usecases/knowledge-base-rag.md) | URL 드롭으로 콘텐츠 수집, 자연어로 시맨틱 검색 |
| [시장 조사 및 제품 팩토리](usecases/market-research-product-factory.md) | Reddit·X에서 고객 페인포인트 발굴 후 MVP 빌드 |
| [사전 빌드 아이디어 검증](usecases/pre-build-idea-validator.md) | 코딩 시작 전 GitHub, HN, npm 등에서 경쟁자 자동 조사 |
| [시맨틱 메모리 검색](usecases/semantic-memory-search.md) | OpenClaw 마크다운 메모리를 벡터 DB로 변환해 시맨틱 검색 |

## 금융 및 트레이딩

| 사례 | 설명 |
|------|------|
| [Polymarket 자동 매매](usecases/polymarket-autopilot.md) | 3가지 전략으로 예측 시장 자동 페이퍼 트레이딩 |

---

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md)를 읽어주세요.

**규칙:**
- 직접 테스트하고 검증한 사례만 제출
- AI로 사례를 생성하지 마세요
- 암호화폐 관련 사례는 받지 않습니다

---

## 라이선스

[MIT](LICENSE)

---

*원본: [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)*

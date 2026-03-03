<div align="center">

<img width="1500" height="500" alt="Image" src="https://github.com/user-attachments/assets/4ae57dfb-4f18-4677-9136-43bf93017250" />

<br/>
<br/>

<strong>사람들이 일상생활에서 OpenClaw(이전 ClawdBot, MoltBot)를 실제로 어떻게 사용하는지 탐색해보세요.
</strong>
<br />
<br />

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Use Cases](https://img.shields.io/badge/usecases-34-blue?style=flat-square)
![Last Update](https://img.shields.io/github/last-commit/hesamsheikh/awesome-openclaw-usecases?label=Last%20Update&style=flat-square)
[![Discord](https://img.shields.io/badge/Discord-Open%20Source%20AI%20Builders-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/vtJykN3t)
</div>

# Awesome OpenClaw 사용 사례

> **⚠️ 번역 버전 안내**
> 이 문서는 커뮤니티에서 번역한 한국어 버전으로, 지연될 수 있습니다. 내용이 오래된 경우 [원본 영문 README](README.md)를 참조하세요.

---

OpenClaw 보급의 병목 현상 해결: ~~기술~~이 아니라 **삶을 개선할 수 있는 방법**을 찾는 것입니다. [OpenClaw](https://github.com/openclaw/openclaw)의 실제 커뮤니티 사용 사례 모음입니다.

> **경고:** 여기서 참조되는 OpenClaw 스킬 및 타사 종속성에는 심각한 보안 취약점이 있을 수 있습니다. 많은 사용 사례가 커뮤니티에서 만든 스킬, 플러그인 및 외부 저장소에 연결되며, 이는 **이 목록의 관리자가 감사하지 않았습니다**. 항상 스킬 소스 코드를 검토하고, 요청된 권한을 확인하며, API 키나 자격 증명을 하드코딩하지 마세요. 보안에 대한 모든 책임은 귀하에게 있습니다.

## 소셜 미디어

| 이름 | 설명 |
|------|-------------|
| [매일 Reddit 요약](usecases/daily-reddit-digest.md) | 선호도에 따라 좋아하는 subreddit의 엄선된 요약을 받아보세요. |
| [매일 YouTube 요약](usecases/daily-youtube-digest.md) | 팔로우하는 채널의 매일 새 동영상 요약 받기 — 관심 있는 크리에이터의 콘텐츠를 놓치지 마세요. |
| [X 계정 분석](usecases/x-account-analysis.md) | X 계정의 정성적 분석을 받아보세요.|
| [다중 소스 기술 뉴스 요약](usecases/multi-source-tech-news-digest.md) | 109개 이상의 소스(RSS, Twitter/X, GitHub, 웹 검색)에서 품질 점수가 매겨진 기술 뉴스를 자동으로 수집하고 배포합니다. |

## 창작 및 구축

| 이름 | 설명 |
|------|-------------|
| [목표 기반 자율 작업](usecases/overnight-mini-app-builder.md) | 목표를 입력하면 에이전트가 자율적으로 일일 작업을 생성, 예약 및 완료합니다 — 밤새 놀라운 미니 앱 구축 포함. |
| [YouTube 콘텐츠 파이프라인](usecases/youtube-content-pipeline.md) | YouTube 채널의 동영상 아이디어 발굴, 연구 및 추적을 자동화합니다. |
| [다중 에이전트 콘텐츠 팩토리](usecases/content-factory.md) | Discord에서 다중 에이전트 콘텐츠 파이프라인 실행 — 연구, 작성 및 썸네일 에이전트가 전용 채널에서 협업합니다. |
| [자율 게임 개발 파이프라인](usecases/autonomous-game-dev-pipeline.md) | 교육용 게임 개발의 전체 수명 주기 관리: 할 일 선택부터 구현, 등록, 문서화 및 git 커밋까지. "버그 우선" 정책 시행. |
| [팟캐스트 제작 파이프라인](usecases/podcast-production-pipeline.md) | 완전한 팟캐스트 워크플로우 자동화 — 게스트 연구, 쇼 개요, 쇼 노트 및 소셜 미디어 홍보 — 주제 선정부터 게시 가능한 자료까지. |
| [습관 추적 및 체크인](usecases/habit-tracker-checkins.md) | 사전 알림 및 목표 조정 기능이 있는 에이전트 기반 습관 추적기. |

## 인프라 및 DevOps

| 이름 | 설명 |
|------|-------------|
| [n8n 워크플로우 오케스트레이션](usecases/n8n-workflow-orchestration.md) | webhook를 통해 API 호출을 n8n 워크플로우에 위임 — 에이전트는 자격 증명을 전혀 처리하지 않으며 모든 통합은 시각적이고 잠금 가능합니다. |
| [자가 치유 홈 서버](usecases/self-healing-home-server.md) | SSH 액세스, 자동화된 cron 작업 및 홈 네트워크 전반의 자가 치유 기능을 갖춘 상시 가동 인프라 에이전트를 실행하세요. |

## 생산성

| 이름 | 설명 |
|------|-------------|
| [자율 프로젝트 관리](usecases/autonomous-project-management.md) | STATE.yaml 패턴을 사용하여 다중 에이전트 프로젝트 조정 — 서브 에이전트가 병렬로 작업하며 오케스트레이터 오버헤드가 없습니다. |
| [다중 채널 AI 고객 서비스](usecases/multi-channel-customer-service.md) | WhatsApp, Instagram, 이메일 및 Google 리뷰를 하나의 AI 기반 수신함으로 통합하여 연중무휴 자동 응답을 제공합니다. |
| [전화 기반 개인 비서](usecases/phone-based-personal-assistant.md) | 전화를 통해 AI 에이전트에 액세스하여 모든 휴대폰에 핸즈프리 음성 비서를 제공합니다. |
| [받은 편지함 정리](usecases/inbox-declutter.md) | 뉴스레터를 요약하고 이메일로 요약본을 보내줍니다. |
| [개인 CRM](usecases/personal-crm.md) | 이메일 및 캘린더에서 연락처를 자동으로 발견하고 추적하며 자연어 쿼리를 지원합니다. |
| [건강 및 증상 추적기](usecases/health-symptom-tracker.md) | 식품 섭취와 증상을 추적하여 유발 요인을 식별하며 정기 체크인 알림이 있습니다. |
| [다중 채널 개인 비서](usecases/multi-channel-assistant.md) | 단일 AI 비서에서 Telegram, Slack, 이메일 및 캘린더로 작업을 라우팅합니다. |
| [프로젝트 상태 관리](usecases/project-state-management.md) | 이벤트 기반 프로젝트 추적, 컨텍스트 자동 캡처, 정적 칸반 보드 대체. |
| [동적 대시보드](usecases/dynamic-dashboard.md) | API, 데이터베이스 및 소셜 미디어에서 병렬로 데이터를 가져오는 실시간 대시보드. |
| [Todoist 작업 관리자](usecases/todoist-task-manager.md) | 추론 및 진행 로그를 Todoist와 동기화하여 에이전트의 투명성을 극대화합니다. |
| [전화 기반 개인 비서](usecases/phone-based-personal-assistant.md) | 모든 휴대폰에서 음성 통화 또는 문자 메시지를 통해 OpenClaw에 액세스하세요. 핸즈프리로 캘린더 업데이트, Jira 티켓 및 웹 검색 결과를 받아보세요. |
| [가족 캘린더 및 가사 도우미](usecases/family-calendar-household-assistant.md) | 모든 가족 캘린더를 아침 브리핑으로 집계하고, 약속 메시지를 모니터링하며, 가정 재고를 관리합니다. |
| [다중 에이전트 전문가 팀](usecases/multi-agent-team.md) | 단일 Telegram 채팅을 통해 여러 전문 에이전트(전략, 개발, 마케팅, 비즈니스)를 조정된 팀으로 실행합니다. |
| [맞춤형 아침 브리핑](usecases/custom-morning-brief.md) | 완전히 맞춤화된 일일 브리핑 받기 — 뉴스, 작업, 콘텐츠 초안 및 AI 권장 작업 — 매일 아침 문자로 전송됩니다. |
| [제2의 뇌](usecases/second-brain.md) | 봇에게 무엇이든 보내서 기억하게 하고, 맞춤형 Next.js 대시보드에서 모든 기억을 검색하세요. |
| [이벤트 게스트 확인](usecases/event-guest-confirmation.md) | 이벤트 게스트 목록에 하나씩 전화하여 참석 확인, 메모 수집 및 요약 컴파일 — AI 음성 통화로 완전 자동화. |
| [자동 회의 노트 및 액션 아이템](usecases/meeting-notes-action-items.md) | 회의 기록을 구조화된 요약으로 변환하고 Jira, Linear 또는 Todoist에서 작업을 자동으로 생성 — 올바른 사람에게 할당. |
| [습관 추적 및 책임 코치](usecases/habit-tracker-accountability-coach.md) | Telegram 또는 SMS를 통한 사전 일일 체크인으로 습관 추적, 연속 기록 유지 및 진행 상황에 따라 톤 조정. |

## 연구 및 학습

| 이름 | 설명 |
|------|-------------|
| [AI 실적 추적기](usecases/earnings-tracker.md) | 자동화된 미리보기, 알림 및 상세 요약이 있는 기술/AI 실적 추적. |
| [개인 지식 베이스 (RAG)](usecases/knowledge-base-rag.md) | URL, 트윗 및 기사를 채팅에 드래그하여 검색 가능한 지식 베이스를 구축하세요. |
| [시장 조사 및 제품 팩토리](usecases/market-research-product-factory.md) | Last 30 Days 스킬을 사용하여 Reddit 및 X에서 실제 문제점을 파악한 다음 OpenClaw가 이를 해결하는 MVP를 구축하도록 합니다. |
| [의미론적 메모리 검색](usecases/semantic-memory-search.md) | 하이브리드 검색 및 자동 동기화를 사용하여 OpenClaw 마크다운 메모리 파일에 벡터 기반 의미론적 검색을 추가합니다. |
| [구축 전 아이디어 검증기](usecases/pre-build-idea-validator.md) | 새로운 것을 구축하기 전에 GitHub, HN, npm, PyPI 및 Product Hunt를 자동으로 스캔 — 영역이 혼잡하면 중지하고 열려 있으면 계속합니다. |

## 금융 및 거래

| 이름 | 설명 |
|------|-------------|
| [Polymarket 자동 조종](usecases/polymarket-autopilot.md) | 백테스팅, 전략 분석 및 일일 성과 보고서가 있는 예측 시장의 자동화된 모의 거래. |

## 🤝 기여

기여를 환영합니다! 가이드라인은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참조하세요.

- 새로운 사용 사례 추가
- 기존 사례 개선

> 최소 하루 이상 사용하고 작동하는지 확인한 사용 사례만 제출하세요. 우리는 삶을 더 나쁘게가 아니라 더 좋게 만드는 진정한 아이디어를 소중히 여깁니다!
>
> **참고:** 암호화폐 관련 사용 사례는 허용하지 않습니다.

---

**원문 링크**: [README.md](README.md)
**최종 동기화**: 2026-02-28

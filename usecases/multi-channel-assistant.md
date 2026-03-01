# 멀티채널 어시스턴트

## 문제점
태스크 관리, 일정 추가, 메시지 전송, 업무 추적을 위해 앱을 계속 전환해야 합니다.

## 기능 설명
Telegram(토픽 기반 라우팅), Slack, Google Workspace(캘린더, Gmail, Drive), Todoist, Asana를 통합하는 단일 AI 어시스턴트.

## Telegram 토픽 구성

- `config` — 봇 설정/디버깅
- `updates` — 상태/알림
- `video-ideas` — 콘텐츠 파이프라인
- `personal-crm` — 연락처 관리
- `earnings` — 금융 추적
- `knowledge-base` — RAG 수집/쿼리

## 필요한 스킬
- `gog` CLI (Google Workspace)
- Slack (봇 + 사용자 토큰)
- Todoist API
- Asana API
- Telegram (여러 토픽)

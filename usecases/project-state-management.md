# 프로젝트 상태 관리

## 문제점
Kanban 보드는 오래되고, 카드는 업데이트되지 않으며, 결정 뒤의 맥락이 사라집니다.

## 기능 설명
이벤트 기반 프로젝트 상태 시스템:
- 전체 이력과 함께 데이터베이스에 상태 저장
- 맥락 캡처: 결정, 차단 요소, 다음 단계, 핵심 인사이트
- 이벤트 기반: "X 완료, Y에 막힘" → 자동 상태 전환
- 자연어 쿼리: "[프로젝트] 현황은?", "왜 [기능]을 피봇했지?"
- git 커밋 + 대화에서 일일 스탠드업 요약
- Git 통합: 커밋을 프로젝트 이벤트에 연결

**이벤트 유형:** `progress`, `blocker`, `decision`, `pivot`

## 데이터베이스 스키마

```sql
CREATE TABLE projects (id, name, status, current_phase, last_update);
CREATE TABLE events (id, project_id, event_type, description, context, timestamp);
CREATE TABLE blockers (id, project_id, blocker_text, status, created_at, resolved_at);
```

## 필요한 스킬
- `postgres` 또는 SQLite
- `github` CLI
- Discord/Telegram
- 크론 작업
- 서브에이전트

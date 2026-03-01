# Todoist 태스크 관리자

## 문제점
장시간 에이전트 워크플로우가 실행되는 동안 에이전트가 현재 무엇을 하고 있는지 파악하기 어렵습니다.

## 기능 설명
외부 가시성을 위해 에이전트 진행 상황을 Todoist에 동기화합니다. 에이전트가 스스로 생성하는 셸 스크립트 3개:

1. `todoist_api.sh` — Todoist REST API용 curl 래퍼
2. `sync_task.sh` — 태스크 생성/업데이트, 상태 섹션에 할당 (In Progress / Waiting / Done)
3. `add_comment.sh` — 서브스텝 완료 시 실시간으로 태스크 댓글에 기록

**필요 조건:** 3개 섹션이 있는 Todoist 프로젝트, Todoist API 토큰, 프로젝트 ID, 섹션 ID

## 필요한 스킬
- Todoist API

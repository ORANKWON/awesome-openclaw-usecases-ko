# 자율 프로젝트 관리

## 문제점
기존 오케스트레이터 패턴은 병목을 만듭니다 — 메인 에이전트가 교통 정리원이 됩니다. 복잡한 프로젝트는 지속적인 감독 없이도 병렬로 작업하는 에이전트가 필요합니다.

## 기능 설명
공유 `STATE.yaml` 파일을 단일 진실 원천으로 사용하는 분산형 프로젝트 관리. 에이전트는 상태를 읽고 쓰면서 중앙 오케스트레이터 없이 병렬로 작업하고 스스로 조율합니다.

## STATE.yaml 예시

```yaml
project: website-redesign
updated: 2026-02-10T14:30:00Z

tasks:
  - id: homepage-hero
    status: in_progress
    owner: pm-frontend

  - id: api-auth
    status: done
    owner: pm-backend
    output: "src/api/auth.ts"

  - id: content-migration
    status: blocked
    owner: pm-content
    blocked_by: api-auth
```

## 패턴

1. 메인 에이전트가 특정 범위를 가진 서브에이전트 생성
2. 서브에이전트가 STATE.yaml을 읽고 할당된 태스크 탐색
3. 서브에이전트가 자율적으로 작업하고 진행 상황을 STATE.yaml에 업데이트
4. 다른 에이전트들이 STATE.yaml을 폴링하며 차단 해제된 작업 탐색
5. 메인 에이전트가 주기적으로 확인하고 우선순위 조정

## AGENTS.md 설정

```
메인 세션 = 조율만 담당. 모든 실행은 서브에이전트로.

워크플로우:
1. 새 태스크 도착
2. PROJECT_REGISTRY.md에서 기존 PM 확인
3. PM 존재 → sessions_send(label="pm-xxx", message="[태스크]")
4. 새 프로젝트 → sessions_spawn(label="pm-xxx", task="[태스크]")
5. PM 실행, STATE.yaml 업데이트, 보고
6. 메인 에이전트가 사용자에게 요약

규칙:
- 메인 세션: 최대 0–2 도구 호출
- PM이 자신의 STATE.yaml 파일 소유
- 모든 상태 변경은 git에 커밋
```

## 필요한 스킬
- `sessions_spawn` / `sessions_send`
- 파일 시스템
- Git

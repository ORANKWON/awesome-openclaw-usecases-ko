# 멀티에이전트 팀

## 문제점
에이전트 하나로는 모든 것을 잘 할 수 없습니다. 1인 창업자에게는 관리할 도구가 아닌 팀이 필요합니다.

## 기능 설명
OpenClaw 에이전트들을 조율된 팀으로 운영:
- **Milo** (전략 리더, Claude Opus): 기획, 조율, 모닝 스탠드업, OKR 추적
- **Josh** (사업 및 성장, Claude Sonnet): 가격 전략, KPI, 매출 모델링
- **마케팅 에이전트** (Gemini): 콘텐츠 기획, 경쟁사 모니터링, SEO 리서치
- **개발 에이전트** (Claude Opus/Codex): 코딩, 코드 리뷰, CI/CD 모니터링

공유 메모리 구조(`GOALS.md`, `DECISIONS.md`, `PROJECT_STATUS.md`) + 에이전트별 개인 컨텍스트. 단일 Telegram 그룹을 컨트롤 플레인으로 사용 — 필요한 에이전트를 태그.

## 라우팅 설정

```
- @milo → 전략 에이전트
- @josh → 사업 에이전트
- @marketing → 마케팅 에이전트
- @dev → 개발 에이전트
- @all → 브로드캐스트
- 태그 없음 → Milo가 기본 처리
```

## 예약 작업

- 오전 8시: Milo 모닝 스탠드업
- 오전 9시: Josh 핵심 지표 수집
- 오전 10시: 마케팅 에이전트 콘텐츠 아이디어 제안
- 오후 6시: Milo 일일 마감 요약

## 참고
Trebuh(@trebuh_x) — VPS에서 에이전트 4개를 운영하는 1인 창업자, `@jdrhyne` — 15개 이상 에이전트, 머신 3대, Discord 서버 1개

## 필요한 스킬
- `telegram`
- `sessions_spawn` / `sessions_send`
- 공유 파일 시스템
- 여러 모델 제공자 API 키
- VPS

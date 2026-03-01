# 사전 빌드 아이디어 검증기

## 문제점
에이전트에게 "AI 코드 리뷰 도구 만들어줘"라고 하면 6시간 동안 신나게 코딩합니다. 그러는 동안 이미 14만 3천 개 이상의 저장소가 존재합니다. 요청하지 않았으니 에이전트는 확인하지 않습니다.

## 기능 설명
코드 작성 전에 GitHub, Hacker News, npm, PyPI, Product Hunt에서 `idea_check`를 실행합니다. `reality_signal` 점수(0–100)를 반환합니다.

**규칙:**
- `reality_signal > 70`: 중단. 스타 수와 함께 상위 3개 경쟁자 보고. 진행, 피봇, 포기 중 선택 요청.
- `reality_signal 30-70`: 결과와 피봇 힌트 표시. 니치 각도 제안.
- `reality_signal < 30`: 진행. 이 분야가 열려 있다고 언급.

## 실제 예시

> "CLI AI 코드 리뷰 도구 만들어줘"
> reality_signal: 90/100 — 경쟁자: Gitea (53,940 스타), reviewdog (9,104 스타)
> 피봇 제안: Rust/Go 전용 리뷰, React/Vue 컴포넌트 리뷰, 금융/의료 컴플라이언스 리뷰

> "사전 빌드 아이디어 검증용 MCP 서버는?"
> reality_signal: 8/100 — 직접 경쟁자 0개. 빌드 진행.

## 설정

`uvx idea-reality-mcp`로 설치, MCP 설정에 추가, 에이전트 지시사항에 규칙 추가.

## 필요한 스킬
- [idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp)

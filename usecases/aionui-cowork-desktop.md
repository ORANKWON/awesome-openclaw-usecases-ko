# 데스크톱 Cowork로 OpenClaw 사용 (AionUi) — 원격 복구 및 멀티에이전트 허브

데스크톱 Cowork UI에서 OpenClaw를 사용하고, 외출 시 Telegram이나 WebUI에서 접근하고, 연결이 안 될 때 원격으로 수리하세요. AionUi는 무료 오픈소스 앱으로 **OpenClaw를 일급 에이전트로** 12개 이상의 다른 에이전트(Claude Code, Codex, Qwen Code 등)와 함께 실행하며, 설치, 진단, 복구를 위한 내장 **OpenClaw 배포 전문가**를 포함합니다 — OpenClaw가 다운되었고 당신이 머신에 없을 때도 **원격 복구**가 가능합니다.

## 왜 OpenClaw + AionUi인가

| 원하는 것 | AionUi가 제공하는 것 |
|----------|---------------------|
| **진짜 데스크톱 UI로 OpenClaw 사용** | OpenClaw(와 다른 에이전트)가 파일을 읽고/쓰고, 명령을 실행하고, 웹을 탐색하는 것을 볼 수 있는 Cowork 워크스페이스 — 터미널/채팅만이 아닙니다. |
| **OpenClaw가 고장났고 원격에 있을 때 수리** | 어디서든 **Telegram이나 WebUI**를 통해 AionUi를 열기 → **OpenClaw 배포 전문가**를 사용하여 `openclaw doctor` 실행, 설정 수정, 게이트웨이 재시작. 많은 사용자가 이것에 의존합니다. |
| **OpenClaw + 다른 에이전트를 한 곳에서** | OpenClaw, 내장 에이전트, Claude Code, Codex 등을 하나의 앱에서; 전환하거나 병렬로 실행, 모두를 위한 동일한 MCP 설정. |
| **OpenClaw에 원격 접근** | WebUI, Telegram, Lark, DingTalk — 휴대폰이나 다른 기기에서 동일한 AionUi 인스턴스(따라서 OpenClaw)와 대화하세요. |

## 문제점

이미 CLI나 Telegram에서 OpenClaw를 사용하고 있지만:

- 로그에서 추론하는 대신 에이전트가 무엇을 하는지(파일, 터미널, 웹) **보고** 싶습니다.
- **OpenClaw가 연결되지 않고** 머신에 없을 때, `openclaw doctor`를 실행하거나 설정을 수정할 방법이 없습니다 — OpenClaw를 복구할 수 있는 것에 원격 접근이 필요합니다.
- 여러 CLI 에이전트(OpenClaw, Claude Code, Codex, ...)를 사용하고 있으며 앱을 오가거나 각각에 대해 MCP를 재구성하고 싶지 않습니다.

## 기능 설명

- **Cowork 에이전트로서의 OpenClaw**: AionUi와 OpenClaw를 설치; AionUi가 OpenClaw를 자동 감지합니다. 동일한 Cowork UI에서 OpenClaw를 사용 — 파일 인식 워크스페이스, 가시적인 작업.
- **원격 OpenClaw 복구**: OpenClaw가 고장났거나 접근할 수 없을 때, **Telegram이나 WebUI**를 통해 AionUi를 열고 내장 **OpenClaw 배포 전문가**를 사용하세요. 설치를 도와주고, `openclaw doctor`를 실행하고, 설정을 수정하고, 게이트웨이를 재시작하고, 복구 과정을 안내합니다. OpenClaw를 헤드리스로 또는 다른 머신에서 실행하는 사용자에게 일반적인 패턴입니다.
- **한 앱에서 멀티에이전트**: 내장 에이전트(Gemini/OpenAI/Anthropic/Ollama), Claude Code, Codex, 12개 이상의 다른 에이전트와 나란히 OpenClaw를 실행 — 하나의 인터페이스, 병렬 세션.
- **한 번만 MCP, 모든 에이전트**: AionUi에서 한 번 MCP 서버를 구성; OpenClaw와 다른 모든 에이전트에 동기화 — 에이전트별 MCP 설정 없음.
- **원격 접근**: WebUI, Telegram, Lark 또는 DingTalk을 사용하여 어디서든 AionUi 인스턴스(및 OpenClaw)에 접근하세요.
- **선택적 자동화**: AionUi cron은 24/7 작업을 위해 일정에 따라 OpenClaw(또는 다른 에이전트)를 실행할 수 있습니다.

## 필요한 스킬

- **OpenClaw** (예: `npm install -g openclaw@latest`). AionUi의 **OpenClaw 설정** 어시스턴트가 설치, 게이트웨이, 설정을 안내할 수 있습니다.
- 모델을 위한 API 키나 인증 (OpenClaw 설정 + AionUi의 내장 에이전트 키).

## 설정 방법

1. **AionUi 설치**: [AionUi 릴리스](https://github.com/iOfficeAI/AionUi/releases) (macOS / Windows / Linux).
2. **OpenClaw 설치** (필요한 경우):
   ```bash
   npm install -g openclaw@latest
   openclaw onboard --install-daemon   # 선택사항: 24/7을 위한 데몬
   ```
3. **AionUi 열기**: OpenClaw를 자동 감지합니다. 그렇지 않으면 앱 내 **OpenClaw 설정** 어시스턴트를 사용하세요.
4. **Cowork 세션 생성**하고 OpenClaw를 선택하세요. 동일한 워크스페이스, MCP, (활성화된 경우) 원격 채널.

원격 접근이나 cron을 위해서는 AionUi 설정에서 채널과 자동화를 구성하세요.

## 관련 링크

- [AionUi GitHub](https://github.com/iOfficeAI/AionUi)
- [AionUi 웹사이트](https://www.aionui.com)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw 문서](https://docs.openclaw.ai)

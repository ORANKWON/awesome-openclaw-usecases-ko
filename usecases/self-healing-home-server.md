# 자가 치유 홈 서버

## 문제점
홈 서버를 운영하면 24시간 대기 상태가 됩니다. 서비스는 새벽 3시에 다운되고, 인증서는 조용히 만료되고, 디스크는 꽉 차고, 파드는 자는 동안 충돌 루프에 빠집니다.

## 기능 설명
SSH 접근, 자동화된 크론 작업, 자율 문제 감지·수정 기능을 갖춘 지속적 인프라 에이전트("Reef"):
- 자동 헬스 모니터링 (Gatus, ArgoCD, 서비스 엔드포인트)
- 자가 치유: 파드 재시작, 리소스 스케일링, 설정 수정
- 인프라 관리: Terraform, Ansible, Kubernetes 매니페스트
- 모닝 브리핑: 시스템 상태, 캘린더, 날씨, 태스크 보드
- 이메일 트리아지: 받은편지함 스캔, 액션 항목 라벨링, 노이즈 아카이브
- 지식 추출: 노트를 구조화된 검색 가능 지식베이스로 처리
- 블로그 게시 파이프라인: 초안 → 배너 → 게시 → 배포
- 보안 감사: 하드코딩된 비밀, 권한 있는 컨테이너 일일 스캔

## 보안 설정 (필수)
1. 모든 저장소에 TruffleHog pre-push 훅 적용
2. 공개 GitHub 푸시 전 스테이징으로 로컬 Gitea 인스턴스 사용
3. 공개 푸시 전 CI 스캔 파이프라인 (Woodpecker)
4. AI 에이전트 전용 1Password 볼트 (제한된 범위)
5. 일일 보안 감사

## 15분 크론 스케줄 (일부)
- 매 15분: Kanban에서 진행 중인 태스크 확인
- 매 1시간: 헬스 체크, Gmail 트리아지, 알림 모니터링
- 매 6시간: 지식베이스 데이터 입력, 자체 헬스 체크
- 매일 오전 4시: 야간 브레인스토밍
- 매일 오전 8시: 모닝 브리핑

## 참고
Nathan의 글 ["Everything I've Done with OpenClaw (So Far)"](https://madebynathan.com/2026/02/03/everything-ive-done-with-openclaw-so-far/) — 모든 머신에 SSH 접근, K3s 클러스터, 1Password, 5,000개 이상 Obsidian 노트, 15개 활성 크론 작업을 운영하는 에이전트 "Reef"

## 필요한 스킬
- `ssh`
- `kubectl`
- `terraform`
- `ansible`
- `1password` CLI
- `gog` CLI
- Calendar API
- Obsidian 볼트

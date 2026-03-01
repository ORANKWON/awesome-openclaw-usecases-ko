# 멀티채널 고객 서비스

## 문제점
소규모 사업체는 WhatsApp, Instagram DM, 이메일, Google 리뷰를 여러 앱에서 각각 관리합니다. 고객은 24시간 즉각적인 응답을 기대합니다.

## 기능 설명
- 통합 받은편지함: WhatsApp Business, Instagram DM, Gmail, Google 리뷰
- AI 자동 응답: FAQ, 예약 요청, 일반 문의 처리
- 복잡한 문제는 사람에게 에스컬레이션
- 실제 고객 영향 없이 시연할 수 있는 테스트 모드
- 다국어 지원 (한국어/영어 등)

## AGENTS.md 라우팅

```
고객 메시지 수신 시:
1. 채널 식별 (WhatsApp/Instagram/이메일/리뷰)
2. 테스트 모드 활성화 여부 확인
3. 의도 분류:
   - FAQ → 지식베이스에서 응답
   - 예약 → 가용 시간 확인, 예약 확정
   - 불만 → 사람 검토 플래그, 수신 확인
   - 리뷰 → 감사 인사 및 우려사항 처리
```

## 필요한 스킬
- WhatsApp Business API (360dialog 등)
- Instagram Graph API
- Gmail용 `gog` CLI
- Google Business Profile API

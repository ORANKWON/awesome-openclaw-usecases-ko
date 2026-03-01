# 개인 CRM

## 문제점
누구와 언제, 무슨 이야기를 했는지 수동으로 추적하기가 번거롭습니다.

## 기능 설명
- 매일 크론 작업으로 이메일과 캘린더에서 새 연락처와 상호작용 스캔
- SQLite 데이터베이스 유지: 이름, 이메일, 첫 연락일, 최근 상호작용, 빈도, 메모
- 자연어 쿼리: "2주 동안 연락 안 한 사람?", "Stripe의 John에 대해 뭘 알고 있어?"
- 모닝 미팅 브리핑: CRM + 이메일 기록으로 외부 참석자 리서치

## 데이터베이스 스키마

```sql
-- contacts 테이블: name, email, first_contact, last_contact, frequency, notes
```

## 필요한 스킬
- Gmail + Google Calendar (`gog` CLI)
- SQLite
- Telegram 토픽

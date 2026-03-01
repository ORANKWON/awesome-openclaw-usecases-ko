# Polymarket 자동 매매

## 문제점
차익 거래 기회를 찾고 거래를 실행하기 위해 예측 시장을 수동으로 모니터링하려면 끊임없는 주의가 필요합니다.

## 기능 설명
3가지 전략을 사용한 자동 페이퍼 트레이딩 (실제 돈 없음):
- **TAIL**: 거래량 급증과 모멘텀이 명확할 때 트렌드 추종 (확률 >60% + 거래량 급증)
- **BONDING**: 시장 과잉 반응 시 역추세 플레이 (뉴스로 10% 이상 급락)
- **SPREAD**: YES+NO > 1.05일 때 차익 거래

15분마다 지속적인 크론 작업 스캔. 매일 오전 8시 Discord에 일일 요약 전송: 거래 (진입/청산, 손익), 포트폴리오 가치, 승률, 전략별 성과, 시장 인사이트.

## 데이터베이스 스키마

```sql
CREATE TABLE paper_trades (market_id, market_name, strategy, direction, entry_price, exit_price, quantity, pnl, timestamp);
CREATE TABLE portfolio (total_value, cash, positions JSONB, updated_at);
```

## 필요한 스킬
- `web_fetch` (Polymarket API)
- `postgres` 또는 SQLite
- Discord
- 크론 작업
- 서브에이전트 실행

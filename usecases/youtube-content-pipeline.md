# YouTube 콘텐츠 파이프라인

## 문제점
매일 영상을 올리는 YouTube 크리에이터로서 웹과 X/Twitter에서 신선하고 시의적절한 영상 아이디어를 찾는 데 시간이 많이 걸립니다. 다뤘던 주제를 수동으로 추적하다 보면 중복이 생깁니다.

## 기능 설명
- 매시간 크론 작업으로 최신 AI 뉴스 스캔 (웹 + X/Twitter), 텔레그램으로 영상 아이디어 제안
- 조회수와 주제 분석이 포함된 90일치 영상 카탈로그로 중복 주제 방지
- 아이디어 시맨틱 중복 제거를 위한 벡터 임베딩 SQLite 데이터베이스
- Slack에 링크 공유 시: 주제 리서치, X 검색, 지식베이스 쿼리, 전체 개요가 담긴 Asana 카드 생성

## 데이터베이스 스키마

```sql
CREATE TABLE pitches (
  id INTEGER PRIMARY KEY,
  timestamp TEXT,
  topic TEXT,
  embedding BLOB,
  sources TEXT
);
```

## 설정 프롬프트

```
매시간 크론 작업 실행:
1. 웹과 X/Twitter에서 최신 AI 뉴스 검색
2. 90일치 YouTube 카탈로그와 비교 (gog YouTube Analytics 활용)
3. 과거 모든 아이디어와 시맨틱 유사도 확인
4. 새로운 내용이면 출처와 함께 텔레그램 "video-ideas" 토픽에 제안

또한 Slack #ai_trends에 링크 공유 시:
1. 주제 리서치
2. X에서 관련 게시물 검색
3. 지식베이스 쿼리
4. 전체 개요가 담긴 Asana 카드 생성 (Video Pipeline)
```

## 필요한 스킬
- `web_search` (기본 제공)
- `x-research-v2`
- `knowledge-base`
- Asana
- `gog` CLI (YouTube Analytics)
- Telegram 토픽

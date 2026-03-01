# 회의록 및 액션 아이템

## 문제점
회의 요약 작성, 액션 아이템 추출, Jira/Linear/Todoist 배포에 회의당 20분 이상 소요됩니다. 액션 아이템이 잊히기 쉽습니다.

## 기능 설명
- 새 회의 녹취록 감지 (붙여넣기, 폴더 감시, 또는 API)
- 핵심 결정사항, 토론 주제, 담당자·기한이 있는 액션 아이템 추출
- 담당자에게 할당된 Jira, Linear, Todoist, Notion 태스크 생성
- Slack/Discord에 요약 게시
- 선택: 기한 전에 담당자에게 알림

## 자동화 파이프라인 프롬프트

```
30분마다 ~/meeting-transcripts/에서 새 .txt 또는 .vtt 파일 확인. 발견 시:
1. 구조화된 요약과 액션 아이템으로 파싱
2. 각 액션 아이템에 대해 Linear에 태스크 생성
3. Slack #team-updates에 요약 게시
4. 처리된 파일을 ~/meeting-transcripts/processed/로 이동
5. 기한이 있는 각 액션 아이템에 대해 Slack으로 담당자에게 하루 전 알림
```

## 필요한 스킬
- Jira/Linear/Todoist/Notion
- Slack/Discord
- 파일 시스템
- 스케줄링/크론
- Otter.ai / Fireflies.ai / Google Meet API (선택)

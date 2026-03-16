# LaTeX 논문 작성

로컬 LaTeX 환경을 설정하는 것은 고통스럽습니다 — TeX Live를 설치하는 데 기가바이트가 걸리고, 컴파일 오류를 디버깅하는 것이 지루하며, 에디터와 PDF 뷰어를 오가는 것이 흐름을 깹니다. 로컬 설정 없이 대화형으로 LaTeX 논문을 작성하고 컴파일하고 싶습니다.

이 워크플로우는 에이전트를 즉시 컴파일이 가능한 LaTeX 작성 어시스턴트로 만듭니다:

- 에이전트와 협업하여 LaTeX를 작성 — 원하는 것을 설명하면 소스를 생성합니다
- pdflatex, xelatex 또는 lualatex로 즉시 PDF로 컴파일 (로컬 TeX 설치 불필요)
- 다른 앱으로 전환하지 않고 PDF를 인라인으로 미리보기
- 스타터 템플릿(article, IEEE, beamer, 중국어 article) 사용으로 보일러플레이트 건너뛰기
- BibTeX/BibLaTeX로 참고문헌 지원 — .bib 내용을 붙여넣기만 하면 됩니다

## 필요한 스킬

- [latex-compiler](https://github.com/Prismer-AI/Prismer/tree/main/skills/latex-compiler) 스킬 (4개 도구: `latex_compile`, `latex_preview`, `latex_templates`, `latex_get_template`)
- Prismer 워크스페이스 컨테이너 (전체 TeX Live가 포함된 LaTeX 서버를 포트 8080에서 실행)

## 설정 방법

1. Docker로 [Prismer](https://github.com/Prismer-AI/Prismer)를 클론하고 배포합니다 (전체 TeX Live가 포함된 LaTeX 서버가 자동으로 시작됩니다):
```bash
git clone https://github.com/Prismer-AI/Prismer.git && cd Prismer
docker compose -f docker/docker-compose.dev.yml up
```

2. `latex-compiler` 스킬이 내장되어 있습니다 — 설치가 필요 없습니다. OpenClaw에 프롬프트하세요:
```text
LaTeX로 연구 논문을 작성하는 걸 도와줘. 내 워크플로우는 이래:

1. IEEE 템플릿에서 시작해 (또는 필요에 따라 article/beamer)
2. 섹션을 설명하면 그에 대한 LaTeX 소스를 생성해줘
3. 주요 편집 후마다 컴파일하고 PDF를 미리보기해서 포맷을 확인할 수 있게 해줘
4. 컴파일 오류가 있으면 로그를 읽고 자동으로 수정해줘
5. BibTeX 항목을 제공하면 참고문헌에 추가하고 다시 컴파일해줘

중국어/CJK 지원이 필요하면 xelatex를 사용하고, 그렇지 않으면 pdflatex를 기본으로 사용해.
상호참조를 위해 항상 2번 실행해.
```

3. 시도해보세요: "제목이 'A Survey of LLM Agents'인 새 IEEE 논문을 시작해줘. 초록과 서론 섹션을 채워서 템플릿을 만든 다음 컴파일해줘."

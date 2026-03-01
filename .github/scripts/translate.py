"""
원본 레포에서 변경된 마크다운 파일을 가져와 한국어로 번역합니다.
"""

import os
import sys
import time
import urllib.request
import json
import anthropic

UPSTREAM_BASE = "https://raw.githubusercontent.com/hesamsheikh/awesome-openclaw-usecases/main"
CHANGED_FILES = "/tmp/changed_files.txt"

TRANSLATE_PROMPT = """다음 마크다운 파일을 한국어로 번역해주세요.

규칙:
- 코드 블록(``` ```) 안의 내용은 번역하지 마세요
- 제품명, 기술명, CLI 명령어, URL은 번역하지 마세요
- 섹션 제목(Pain Point → 문제점, What It Does → 기능 설명, Skills Needed → 필요한 스킬 등)은 한국어로 번역하세요
- 마크다운 구조와 포맷팅을 그대로 유지하세요
- 자연스러운 한국어로 번역하세요

번역할 파일:

{content}"""


def fetch_file(path: str) -> str:
    url = f"{UPSTREAM_BASE}/{path}"
    try:
        with urllib.request.urlopen(url) as resp:
            return resp.read().decode("utf-8")
    except Exception as e:
        print(f"  오류: {path} 가져오기 실패 - {e}", file=sys.stderr)
        return None


def translate(client: anthropic.Anthropic, content: str) -> str:
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": TRANSLATE_PROMPT.format(content=content),
            }
        ],
    )
    return message.content[0].text


def main():
    if not os.path.exists(CHANGED_FILES):
        print("변경된 파일 목록 없음")
        return

    with open(CHANGED_FILES) as f:
        files = [line.strip() for line in f if line.strip()]

    if not files:
        print("번역할 파일 없음")
        return

    client = anthropic.Anthropic()

    for path in files:
        print(f"번역 중: {path}")
        content = fetch_file(path)
        if content is None:
            continue

        translated = translate(client, content)

        # 파일 저장 (디렉토리 생성 포함)
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(translated)

        print(f"  완료: {path}")
        time.sleep(0.5)  # API 속도 제한 방지


if __name__ == "__main__":
    main()

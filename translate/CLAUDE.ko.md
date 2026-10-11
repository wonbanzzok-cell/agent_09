# 규칙

- 너의 이름은 **춘식**이다. 누구냐는 질문을 받으면 춘식이라고 소개한다.
- 사용자가 어떤 언어로 말하든 **항상 한국어로** 답변한다.

## 작업 절차

### 1. 할 일 목록 먼저 보고

- 사용자가 프롬프트로 작업을 요청하면, 다른 작업을 하기 전에 그 작업의 할 일 목록을 먼저 작성해 사용자에게 보고한다.
- 할 일 목록에는 다음을 담는다.
  - 순서대로 정리한 작업 단계
  - 만들거나 바꾸거나 옮기거나 지울 파일과 폴더
  - 사용자가 해야 할 일 (예: 열려 있는 파일 닫기)
- 할 일 목록을 쓰는 데 필요한 읽기 전용 확인(파일 목록 보기 등)은 보고 전에 해도 된다.

### 2. 승인 후 실행

- 사용자가 할 일 목록을 읽고 승인하기 전에는 작업을 시작하지 않는다.
- 사용자가 수정을 요청하면 할 일 목록을 고쳐 다시 보고하고, 다시 승인을 기다린다.
- 승인받은 할 일 목록을 벗어나는 작업이 필요하면 멈추고, 바뀐 내용에 대해 먼저 승인을 받는다.

### 3. 구조 정리로 마무리

- 작업 중에 파일이나 폴더가 추가되었다면, 마지막에 클로드 코드가 가장 잘 인식할 수 있는 파일·폴더 구조로 정리하고 작업을 마친다.
  - [프로젝트 구조](#프로젝트-구조)와 [파일 이름 규칙](#파일-이름-규칙)의 폴더와 이름 규칙을 따른다.
  - 결과 파일을 저장소 루트에 두지 않는다.
  - 이 파일의 구조도와 표를 결과에 맞게 고치고, 번역본도 함께 고친다.
- 이 단계를 할 일 목록의 마지막 항목으로 넣어 작업과 함께 승인받는다.

## Markdown 파일과 번역본

- 이 저장소의 모든 `.md` 파일은 **영어로** 작성한다.
- 각 `.md` 파일의 한국어 번역본을 `translate/` 아래에 둔다. 원본의 상대 경로를 그대로 따르고, 확장자 앞에 `.ko`를 붙인다.
  - `CLAUDE.md` → `translate/CLAUDE.ko.md`
  - `docs/guide.md` → `translate/docs/guide.ko.md`
- 원본을 변경하는 작업 안에서 번역본도 함께 맞춘다.
  - **생성:** 번역본을 만든다.
  - **수정:** 변경 내용을 번역본에 반영한다.
  - **이름 변경 또는 이동:** 번역본도 같이 이름을 바꾸거나 옮긴다.
  - **삭제:** 번역본을 삭제하고, 그 결과 `translate/` 안에 빈 폴더가 남으면 함께 지운다.
- `translate/` 안의 파일은 번역본일 뿐이다. 이 파일들의 번역본은 만들지 않는다.
- 이 규칙은 `CLAUDE.md` 자신에도 적용된다.

## 프로젝트 구조

이 저장소에는 클로드 코드가 만든 조사 노트, 보고서, 발표자료가 들어 있다.

```
agent_09/
├── CLAUDE.md        # 프로젝트 규칙 (이 파일)
├── .claude/
│   ├── rules/
│   │   └── ppt-rule-v1/  # 발표자료 제작 규칙 (ppt-rule-v1.md)
│   └── skills/
│       └── mk-ppt/  # .pptx 파일을 만들고 고치는 프로젝트 전용 스킬
├── references/
│   └── ppt/         # 발표자료 디자인 참고 자료 (slide-design-system.md)
├── research/        # 조사 노트 (.md, 영어)
├── report/          # 완성된 보고서 (.docx, 한국어)
├── presentation/    # 완성된 발표자료 (.pptx, 한국어)
├── scripts/         # 보고서(Node.js)와 발표자료(Python)를 만드는 스크립트
└── translate/       # 모든 .md 파일의 한국어 번역본
```

- 조사 노트는 `research/`에, 보고서는 `report/`에, 발표자료는 `presentation/`에 저장한다. 결과 파일을 저장소 루트에 두지 않는다.
- 기존 조사 노트, 보고서, 발표자료를 덮어쓰지 않는다. 대신 새 버전을 만든다.

## 파일 이름 규칙

- 조사 노트: `research/<주제>-v<N>.md` (예: `research/ai-development-research-v2.md`)
- 보고서: `report/<주제>_보고서_v<N>.docx` (예: `report/AI_발전_보고서_v2.docx`)
- 발표자료: `presentation/<주제>_발표자료_v<N>.pptx` (예: `presentation/AI_발전_발표자료_v2.pptx`)
- 발표자료 빌드 스크립트: `scripts/build-presentation-v<N>.py`
- 버전 번호가 같은 조사 노트와 보고서는 짝이다. 보고서 `v<N>`은 조사 노트 `v<N>`을 바탕으로 한다.
- 새 버전을 추가할 때는 기존 최고 번호의 다음 번호를 쓴다.

| 버전 | 조사 노트 | 보고서 |
|---|---|---|
| v1 | `research/ai-development-research-v1.md` | `report/AI_발전_보고서_v1.docx` |
| v2 | `research/ai-development-research-v2.md` | `report/AI_발전_보고서_v2.docx` |

| 버전 | 발표자료 | 빌드 스크립트 |
|---|---|---|
| v1 | `presentation/Anthropic_회사소개_발표자료_v1.pptx` | `scripts/build-presentation-v1.py` |
| v2 | `presentation/AI_발전_발표자료_v2.pptx` | `scripts/build-presentation-v2.py` |

- 발표자료 v2는 조사 노트 v2를 바탕으로 한다.

## 보고서 만들기

- `scripts/build-report.js`는 `docx` npm 패키지로 v2 보고서를 만든다. 출력 경로 하나만 인자로 받는다.
- v2 보고서를 다시 만들려면 `scripts/`에서 `npm install`을 한 번 실행한 뒤 `npm run build`를 실행한다.
- 새 버전의 보고서를 만들 때는 스크립트를 복사해 내용과 출력 경로를 고치고, 결과를 `report/`에 새 버전 파일로 저장한다.

## 발표자료 만들기

- `.claude/rules/ppt-rule-v1/ppt-rule-v1.md`의 발표자료 규칙(우선순위, 슬라이드 장수, 디자인 참고, 레이아웃)을 먼저 적용한다. 이 규칙은 자동으로 불러와진다.
- 기준끼리 서로 다르면 사용자의 요청, 발표자료 규칙, 디자인 참고 자료, `mk-ppt` 스킬의 기본값 순서로 따른다.
- `.pptx` 파일을 다루는 작업에는 `.claude/skills/mk-ppt/`의 `mk-ppt` 스킬을 쓴다. 이 스킬은 이 저장소에서만 불러와진다.
- 발표자료의 디자인 참고 자료는 `references/ppt/slide-design-system.md`이다 (색상, 폰트, 레이아웃, 구성 요소).
- 스킬에는 `python-pptx` 패키지가 필요하다: `python -m pip install python-pptx`.
- 발표자료마다 출력 경로 하나만 인자로 받는 빌드 스크립트가 있다. 저장소 루트에서 실행한다: `python scripts/build-presentation-v<N>.py "presentation/<주제>_발표자료_v<N>.pptx"`.
- 발표자료의 구조는 `python .claude/skills/mk-ppt/scripts/inspect_pptx.py <file.pptx>`로 확인한다.

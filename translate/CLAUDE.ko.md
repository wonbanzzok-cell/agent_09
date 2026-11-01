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
  - `output/research/ai-development/ai-development-research-v2.md` → `translate/output/research/ai-development/ai-development-research-v2.ko.md`
- 원본을 변경하는 작업 안에서 번역본도 함께 맞춘다.
  - **생성:** 번역본을 만든다.
  - **수정:** 변경 내용을 번역본에 반영한다.
  - **이름 변경 또는 이동:** 번역본도 같이 이름을 바꾸거나 옮긴다.
  - **삭제:** 번역본을 삭제하고, 그 결과 `translate/` 안에 빈 폴더가 남으면 함께 지운다.
- `translate/` 안의 파일은 번역본일 뿐이다. 이 파일들의 번역본은 만들지 않는다.
- 이 규칙은 `CLAUDE.md` 자신에도 적용된다.
- **예외:** `output/blog/<topic>/`의 블로그 원고는 한국어로 쓰며 `translate/`에 번역본을 두지 않는다.

## 프로젝트 구조

이 저장소에는 클로드 코드가 만든 조사 노트, 보고서, 발표자료, 카드뉴스 기획서, 블로그 원고, 웹 페이지가 들어 있다. 모든 결과물은 `output/<종류>/<주제>/` 아래에 둔다. 디자인 레퍼런스는 `references/<종류>/` 아래에 둔다.

```
agent_09_latest/
├── CLAUDE.md        # 프로젝트 규칙 (이 파일)
├── .claude/
│   ├── agents/      # 프로젝트 서브 에이전트 (research-agent.md, blog-agent.md, web-designer.md, developer.md)
│   ├── rules/
│   │   ├── browser-rule-v1/  # Playwright MCP 브라우저 제어 규칙 (browser-rule-v1.md)
│   │   ├── ppt-rule-v1/  # 발표자료 제작 규칙 (ppt-rule-v1.md)
│   │   └── web-dev-rule-v1/  # 웹 페이지 작성·배포 규칙 (web-dev-rule-v1.md)
│   └── skills/
│       └── mk-ppt/  # .pptx 파일을 만들고 고치는 프로젝트 전용 스킬
├── references/
│   ├── ppt/         # 발표자료 디자인 참고 자료 (slide-design-system.md)
│   └── web/         # 주제별 웹 디자인 레퍼런스 (<topic>/<topic>-web-reference-v<N>.md, 영어, 그리고 <topic>/images/ 스크린샷)
│       └── legodt/
├── output/
│   ├── research/    # 조사 노트 (.md, 영어)
│   │   ├── ai-development/
│   │   ├── csat-2027-checklist/
│   │   └── legodt/
│   ├── report/      # 완성된 보고서 (.docx, 한국어)
│   │   └── ai-development/
│   ├── presentation/  # 완성된 발표자료 (.pptx, 한국어)
│   │   ├── ai-development/
│   │   └── anthropic-company/
│   ├── cardnews/    # 카드뉴스 기획서 (.md, 영어)
│   │   └── camping-beginner-checklist/
│   │       └── images/  # 생성한 카드뉴스 이미지 (.png, 글자 없음)와 완성한 썸네일 디자인 (.png)
│   ├── blog/        # 네이버 블로그 원고 (.md, 한국어)
│   │   └── csat-2027-checklist/
│   └── web/         # 주제·버전별 웹 페이지 코드 (<topic>/v<N>/: index.html, css/, js/, images/, libs/)
│       └── legodt/
├── scripts/         # 보고서(Node.js)와 발표자료(Python)를 만드는 스크립트
└── translate/       # 모든 .md 파일의 한국어 번역본 (위 경로를 그대로 따름, 예: translate/output/research/<topic>/)
```

### 주제 폴더

- 작업의 종류가 같고 주제가 다르면, 그 종류의 폴더 안에 주제(작업명) 이름으로 폴더를 만들고 그 주제의 파일을 모두 그 안에 둔다.
  - 예: `output/blog/winter/`에는 `winter-blog-v1.md`와 `images/`를, `output/research/csat-2027-checklist/`에는 `csat-2027-checklist-research-v1.md`와 `images/`를 둔다.
- 조사 노트, 보고서, 발표자료, 카드뉴스 기획서, 블로그 원고, 그리고 새로운 종류의 문서까지 모든 작업에 적용한다.
- `<topic>`은 하이픈으로 이은 짧은 영어 소문자 슬러그다 (예: `ai-development`). 폴더를 만들기 전에 기존 주제 폴더를 확인하고, 같은 주제면 그 폴더를 다시 쓴다.
- 주제에 딸린 이미지와 기타 부속 파일은 `<topic>/images/`에 둔다.
- 버전 번호(`v<N>`)는 주제 폴더 안에서 매긴다.
- 새로운 종류의 작업이면 `output/<종류>/<topic>/`을 만들고 위 구조도에 추가한다.
- 옛 경로에는 저장하지 않는다. 저장소 루트의 `research/`, `report/`, `presentation/`, `cardnews/`나, 주제 폴더 없이 `output/<종류>/` 바로 아래가 여기에 해당한다.

### 결과물 저장

- 결과 파일을 저장소 루트에 두지 않는다.
- 기존 조사 노트, 보고서, 발표자료, 카드뉴스 기획서, 블로그 원고를 덮어쓰지 않는다. 대신 새 버전을 만든다.

## 파일 이름 규칙

- 조사 노트: `output/research/<topic>/<topic>-research-v<N>.md` (예: `output/research/ai-development/ai-development-research-v2.md`)
- 보고서: `output/report/<topic>/<주제>_보고서_v<N>.docx` (예: `output/report/ai-development/AI_발전_보고서_v2.docx`)
- 발표자료: `output/presentation/<topic>/<주제>_발표자료_v<N>.pptx` (예: `output/presentation/ai-development/AI_발전_발표자료_v2.pptx`)
- 발표자료 빌드 스크립트: 새 발표자료는 `scripts/build-presentation-<topic>-v<N>.py`로 짓는다. 기존 스크립트 `scripts/build-presentation-v1.py`, `-v2.py`는 이름을 그대로 둔다.
- 블로그 원고: `output/blog/<topic>/<topic>-blog-v<N>.md` (예: `output/blog/csat-2027-checklist/csat-2027-checklist-blog-v1.md`)
- 웹 디자인 레퍼런스: `references/web/<topic>/<topic>-web-reference-v<N>.md`, 스크린샷은 `references/web/<topic>/images/<topic>-reference-v<N>-<번호>.png`
- 웹 페이지: `output/web/<topic>/v<N>/`, 진입점은 `index.html`, 스크린샷은 `screenshots/`
- 카드뉴스 기획서: `output/cardnews/<topic>/<topic>-cardnews-v<N>.md` (예: `output/cardnews/camping-beginner-checklist/camping-beginner-checklist-cardnews-v1.md`)
- 카드뉴스 썸네일 이미지: `output/cardnews/<topic>/images/<topic>-thumbnail-v<N>-<번호>.png` (예: `output/cardnews/camping-beginner-checklist/images/camping-beginner-checklist-thumbnail-v1-1.png`). `v<N>`은 카드뉴스 기획서의 버전과 같다.
- 피그마에서 내보낸 완성 썸네일 디자인: `output/cardnews/<topic>/images/<topic>-thumbnail-design-v<N>-<시안>.png` (예: `output/cardnews/camping-beginner-checklist/images/camping-beginner-checklist-thumbnail-design-v1-a.png`). `<시안>`은 피그마 프레임 이름의 알파벳을 소문자로 쓴다 (`Thumbnail A` → `a`).
- 주제와 버전 번호가 같은 조사 노트와 보고서는 짝이다. 보고서 `v<N>`은 조사 노트 `v<N>`을 바탕으로 한다.
- 새 버전을 추가할 때는 같은 주제 폴더 안에서 기존 최고 번호의 다음 번호를 쓴다.

| 버전 | 조사 노트 | 보고서 |
|---|---|---|
| v1 | `output/research/ai-development/ai-development-research-v1.md` | `output/report/ai-development/AI_발전_보고서_v1.docx` |
| v2 | `output/research/ai-development/ai-development-research-v2.md` | `output/report/ai-development/AI_발전_보고서_v2.docx` |

| 버전 | 발표자료 | 빌드 스크립트 |
|---|---|---|
| v1 | `output/presentation/anthropic-company/Anthropic_회사소개_발표자료_v1.pptx` | `scripts/build-presentation-v1.py` |
| v2 | `output/presentation/ai-development/AI_발전_발표자료_v2.pptx` | `scripts/build-presentation-v2.py` |

- 발표자료 v2는 조사 노트 `output/research/ai-development/ai-development-research-v2.md`를 바탕으로 한다.
- 이동 전에 만든 보고서와 발표자료 파일의 본문에는 옛 출처 경로(`research/...`)가 그대로 남아 있다. 빌드 스크립트는 새 경로를 쓰도록 고쳤다.

| 버전 | 카드뉴스 기획서 | 주제 | 썸네일 이미지 | 완성 썸네일 |
|---|---|---|---|---|
| v1 | `output/cardnews/camping-beginner-checklist/camping-beginner-checklist-cardnews-v1.md` | 캠핑: 입문자 필수 준비물 체크리스트 | `output/cardnews/camping-beginner-checklist/images/camping-beginner-checklist-thumbnail-v1-1.png`, `-v1-2.png` | `output/cardnews/camping-beginner-checklist/images/camping-beginner-checklist-thumbnail-design-v1-a.png` (1080×1080) |

- 카드뉴스 기획서는 8장으로 구성하고, 1장은 썸네일로 한다.
- v1 썸네일 이미지는 컨셉 A(장비 플랫레이)로 힉스필드 MCP(`z_image` 모델, 1:1, 글자 없음)에서 생성했다.
- v1 썸네일 디자인(1번 이미지로 만든 `Thumbnail A`, 2번 이미지로 만든 `Thumbnail B`, 1080×1080)은 피그마에 있고, 이 중 `Thumbnail A`만 PNG로 내보냈다: [캠핑 카드뉴스 - 입문자 체크리스트 v1](https://www.figma.com/design/N1sTvSQ4FIrzfmc0m2P7dj).

| 버전 | 블로그 초안 | 주제 | 조사 노트 |
|---|---|---|---|
| v1 | `output/blog/csat-2027-checklist/csat-2027-checklist-blog-v1.md` | 2027학년도 수능(2026-11-19): 수험생·학부모 당일 체크리스트 | `output/research/csat-2027-checklist/csat-2027-checklist-research-v1.md` |

- 블로그 초안 v1은 조사 노트 `output/research/csat-2027-checklist/csat-2027-checklist-research-v1.md`를 바탕으로 한다.
- 블로그 초안 v1은 사용자의 네이버 블로그에 임시저장했고 발행하지 않았다. 태그는 발행 설정 창에서만 넣을 수 있어 입력하지 않았다.

## 보고서 만들기

- `scripts/build-report.js`는 `docx` npm 패키지로 v2 보고서를 만든다. 출력 경로 하나만 인자로 받는다.
- v2 보고서를 다시 만들려면 `scripts/`에서 `npm install`을 한 번 실행한 뒤 `npm run build`를 실행한다. 결과는 `output/report/ai-development/AI_발전_보고서_v2.docx`에 저장된다.
- 새 버전의 보고서를 만들 때는 스크립트를 복사해 내용과 출력 경로를 고치고, 결과를 `output/report/<topic>/`에 새 버전 파일로 저장한다.

## 발표자료 만들기

- `.claude/rules/ppt-rule-v1/ppt-rule-v1.md`의 발표자료 규칙(우선순위, 슬라이드 장수, 디자인 참고, 레이아웃)을 먼저 적용한다. 이 규칙은 자동으로 불러와진다.
- 기준끼리 서로 다르면 사용자의 요청, 발표자료 규칙, 디자인 참고 자료, `mk-ppt` 스킬의 기본값 순서로 따른다.
- `.pptx` 파일을 다루는 작업에는 `.claude/skills/mk-ppt/`의 `mk-ppt` 스킬을 쓴다. 이 스킬은 이 저장소에서만 불러와진다.
- 발표자료의 디자인 참고 자료는 `references/ppt/slide-design-system.md`이다 (색상, 폰트, 레이아웃, 구성 요소).
- 스킬에는 `python-pptx` 패키지가 필요하다: `python -m pip install python-pptx`.
- 발표자료마다 출력 경로 하나만 인자로 받는 빌드 스크립트가 있다. 저장소 루트에서 실행한다: `python scripts/build-presentation-<topic>-v<N>.py "output/presentation/<topic>/<주제>_발표자료_v<N>.pptx"`.
- 발표자료의 구조는 `python .claude/skills/mk-ppt/scripts/inspect_pptx.py <file.pptx>`로 확인한다.

## 서브 에이전트

프로젝트 서브 에이전트는 `.claude/agents/`에 있다. 에이전트를 추가하거나 고친 뒤에는 클로드 코드를 다시 시작하거나 `/agents`를 연다.

| 에이전트 | 파일 | 역할 | 결과물 |
|---|---|---|---|
| `research-agent` | `.claude/agents/research-agent.md` | 주제를 웹에서 조사한다 | `output/research/<topic>/<topic>-research-v<N>.md` (영어)와 `translate/output/research/<topic>/<topic>-research-v<N>.ko.md` |
| `blog-agent` | `.claude/agents/blog-agent.md` | 네이버 블로그 글을 쓰고 Playwright MCP로 임시저장한다 | `output/blog/<topic>/<topic>-blog-v<N>.md` (한국어)와 네이버 블로그 임시저장 글 |
| `web-designer` | `.claude/agents/web-designer.md` | GDWEB과 DBCUT에서 웹 디자인 레퍼런스를 찾아 디자인과 레이아웃을 분석한다 | `references/web/<topic>/<topic>-web-reference-v<N>.md` (영어), `references/web/<topic>/images/`, `translate/references/web/<topic>/<topic>-web-reference-v<N>.ko.md` |
| `developer` | `.claude/agents/developer.md` | 레퍼런스와 분석 자료를 바탕으로 `.claude/rules/web-dev-rule-v1/web-dev-rule-v1.md`에 따라 웹 페이지 코드를 작성하고 GitHub Pages에 배포한다 | `output/web/<topic>/v<N>/`와 GitHub Pages 사이트 |

- `blog-agent`는 실행할 때마다 사용자에게 네이버 블로그 ID를 확인받고, 무엇이든 입력하기 전에 로그인된 계정이 그 ID와 같은지 확인한다.
- `blog-agent`는 절대 발행하지 않고 로그인 정보도 입력하지 않는다. 로그인은 사용자가 브라우저 창에서 직접 한다.
- 네이버 블로그 임시저장 글에는 공개 URL이 없다. 에이전트는 저장 목록에서 이어 쓸 수 있는 에디터 링크(`https://blog.naver.com/<ID>?Redirect=Write`)를 보고한다.
- 조사 노트(예: `output/research/<topic>/<topic>-research-v<N>.md`)를 `blog-agent`의 자료로 넘길 수 있다.
- `web-designer`는 GDWEB과 DBCUT에서만 레퍼런스를 찾고 핀터레스트는 절대 쓰지 않는다. 스크린샷과 링크를 저장하고 디자인과 레이아웃을 분석한다.
- `developer`는 코드를 쓰기 전에 `.claude/rules/web-dev-rule-v1/web-dev-rule-v1.md`를 읽고, 순수 HTML, CSS, JavaScript로 만들며, 묻지 않고 GitHub Pages에 배포한다.
- 웹 작업 흐름: 조사 노트 → `web-designer`(레퍼런스) → `developer`(페이지).

## 웹 페이지 만들기

- `.claude/rules/web-dev-rule-v1/web-dev-rule-v1.md`의 웹 개발 규칙(파일 구조, 코딩, 라이브러리, 배포)을 적용한다. 이 규칙은 자동으로 불러와진다.
- 페이지는 순수 HTML, CSS, JavaScript로 만든다: `index.html`, `css/style.css`, `js/main.js`, `images/`, 그리고 내려받은 라이브러리용 `libs/`.
- 라이브러리는 정확한 버전으로 내려받아 라이선스와 함께 `libs/<library>-<version>/`에 저장한다. 설치한 라이브러리는 모두 사용자에게 보고한다.
- 작업마다 묻지 않고 바로 GitHub Pages에 배포한다. 레포지터리는 로그인된 `gh` 계정 아래에 작업명(`<topic>`)으로 공개 생성하며, 설명 끝에 `[agent_09 web]`을 붙인다. 같은 작업의 새 버전은 같은 레포지터리를 갱신하고 `v<N>` 태그를 붙인다.
- 배포 주소는 `https://<owner>.github.io/<task_name>/`이다. 배포할 때마다 아래 표에 기록한다.

| 작업 | 버전 | 페이지 폴더 | 레포지터리 | 배포 링크 |
|---|---|---|---|---|
| `legodt` | v1 | `output/web/legodt/v1/` | [wonbanzzok-cell/legodt](https://github.com/wonbanzzok-cell/legodt) | [https://wonbanzzok-cell.github.io/legodt/](https://wonbanzzok-cell.github.io/legodt/) |

| 작업 | 버전 | 조사 노트 | 웹 레퍼런스 |
|---|---|---|---|
| `legodt` | v1 | `output/research/legodt/legodt-research-v1.md` | `references/web/legodt/legodt-web-reference-v1.md` |

- `legodt` 페이지(오덴세의 텀블러 브랜드 레고트)는 비공식 소개 페이지다. 사진은 Unsplash(Unsplash License)에서 가져왔고, 텀블러·참·스티커 그래픽은 직접 그린 SVG이며, 한글 폰트는 `libs/`의 Pretendard 1.3.9다. JavaScript 라이브러리는 쓰지 않았다.

## 브라우저 제어

- 웹 브라우저를 쓸 수 있는 작업에는 `.claude/rules/browser-rule-v1/browser-rule-v1.md`의 브라우저 규칙을 적용한다. 이 규칙은 자동으로 불러와진다.
- 사용자가 "브라우저를 열어서 작업", "웹 제어", "직접 작업" 같은 키워드로 브라우저 작업을 요청하면 바로 Playwright MCP를 쓴다. 그렇지 않으면 쓰기 전에 동의를 구한다.

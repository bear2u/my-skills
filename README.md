# My Skills Hub

Claude Code를 위한 커스텀 스킬 모음입니다. 개발 생산성을 높이기 위한 다양한 자동화 스킬들을 제공합니다.

---

<div align="center">

### 🎴 카드로 배우는 개발 학습 플랫폼

[![CodeDeck](https://img.shields.io/badge/CodeDeck-카드로_배우는_개발_플랫폼-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTUgNEgxOUMyMC4xIDQgMjEgNC45IDIxIDZWMThDMjEgMTkuMSAyMC4xIDIwIDE5IDIwSDVDMy45IDIwIDMgMTkuMSAzIDE4VjZDMyA0LjkgMy45IDQgNSA0WiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+Cg==)](https://www.codedeck.kr)

프로그래밍 언어와 프레임워크를 **카드 뉴스 형태**로 쉽게 배우세요!
`Flutter` `React` `TypeScript` `JavaScript` `Python` `Dart`

**👉 [CodeDeck 바로가기](https://www.codedeck.kr)**

</div>

---

## 빠른 설치

| 스킬 이름 | 한줄 설명 | 마켓 설치 명령어 |
|----------|---------|---------------|
| **Flutter Init** | Flutter 프로젝트를 Clean Architecture로 자동 생성 | `/plugin marketplace install suji-father-marketplace@flutter-init` |
| **Next.js 15 Init** | Next.js 15 프로젝트를 App Router로 자동 생성 | `/plugin marketplace install suji-father-marketplace@nextjs15-init` |
| **Code Changelog** | AI 코드 변경사항을 자동 문서화하고 웹에서 실시간 확인 | `/plugin marketplace install suji-father-marketplace@code-changelog` |
| **Codex** | OpenAI Codex CLI로 코드 분석, 리팩토링, 자동 편집 | `/plugin marketplace install suji-father-marketplace@codex` |
| **Codex-Claude Loop** | Claude + Codex 이중 AI 엔지니어링 루프로 최고 품질 보장 | `/plugin marketplace install suji-father-marketplace@codex-claude-loop` |
| **Meta Prompt Generator** | 구조화된 커스텀 슬래시 커맨드를 자동 생성 | `/plugin marketplace install suji-father-marketplace@meta-prompt-generator` |
| **Prompt Enhancer** | 프로젝트 컨텍스트 분석으로 간단한 요청을 상세 요구사항으로 변환 | `/plugin marketplace install suji-father-marketplace@prompt-enhancer` |
| **Web to Markdown** | 웹페이지를 마크다운으로 변환 (일반/AI 최적화/듀얼 모드) | `/plugin marketplace install suji-father-marketplace@web-to-markdown` |
| **Card News Generator** | 600x600 인스타그램 스타일 카드 뉴스 시리즈 자동 생성 | `/plugin marketplace install suji-father-marketplace@card-news-generator` |
| **Card News Generator V2** | 배경 이미지 지원 카드 뉴스 생성기 (고급 기능) | `/plugin marketplace install suji-father-marketplace@card-news-generator-v2` |
| **Landing Page Guide** | 전환율 높은 랜딩페이지 제작 가이드 (11가지 필수 요소) | `/plugin marketplace install suji-father-marketplace@landing-page-guide` |

### 마켓플레이스 추가

```bash
/plugin marketplace add bear2u/claude-plugins
```

## 스킬 목록

### 1. [Code Changelog](./skills/code-changelog/)
AI가 생성한 모든 코드 변경사항을 자동으로 문서화하고 웹 브라우저에서 실시간으로 확인할 수 있는 스킬입니다.

**주요 기능:**
- 자동 문서 생성 (Markdown)
- HTML 뷰어 (설치 불필요, Python 서버)
- 다크 모드 UI (GitHub 스타일)
- 실시간 서버 (http://localhost:4000)

**사용 시나리오:**
- 코드 리뷰 문서 자동 생성
- 변경 이력 추적
- 팀원과 변경사항 공유

### 2. [Meta Prompt Generator](./skills/meta-prompt-generator/)
간단한 설명을 받아 단계별 병렬 처리가 가능한 구조화된 커스텀 슬래시 커맨드를 자동으로 생성합니다.

**주요 기능:**
- 지능형 지식 수집 (웹 검색)
- 단계 기반 워크플로우 설계
- 포괄적인 테스트 생성
- 병렬 처리 최적화

**사용 시나리오:**
- 복잡한 프로젝트 워크플로우 자동화
- 재사용 가능한 슬래시 커맨드 생성
- 체계적인 테스트 스위트 작성

### 3. [Prompt Enhancer](./skills/prompt-enhancer/)
프로젝트 컨텍스트를 분석하여 간단한 개발 요청을 명확하고 상세한 요구사항으로 변환합니다.

**주요 기능:**
- 프로젝트 구조 자동 분석
- 기존 패턴 인식
- 구조화된 요구사항 생성
- 프레임워크별 최적화

**사용 시나리오:**
- "로그인 기능 만들어줘" → 상세한 구현 요구사항
- Clean Architecture 기반 설계 제안
- 프로젝트 컨벤션 자동 적용

**지원 스택:**
- Flutter (Clean Architecture, Riverpod)
- Next.js/React (App Router, Zustand)
- Python (Django, FastAPI)

### 4. [Flutter Init](./skills/flutter-init/)
도메인 기반 Flutter 프로젝트를 Clean Architecture로 자동 생성합니다.

**주요 기능:**
- 도메인 선택 (Todo/Habit/Note/Expense/Custom)
- 스택 프리셋 (Minimal/Essential/Full Stack/Custom)
- Clean Architecture 자동 생성
- Riverpod 3.0, Drift, Freezed 설정

**기술 스택:**
- Riverpod 3.x (상태 관리)
- Drift (로컬 데이터베이스)
- Freezed (불변 모델)
- Easy Localization (다국어)
- FluentUI Icons

**사용 시나리오:**
- 새로운 Flutter 앱 빠른 시작
- Clean Architecture 보일러플레이트
- 도메인 중심 설계

### 5. [Next.js 15 Init](./skills/nextjs15-init/)
도메인 기반 Next.js 15 프로젝트를 App Router로 자동 생성합니다.

**주요 기능:**
- 도메인 선택 (Todo/Blog/Dashboard/E-commerce/Custom)
- 스택 프리셋 (Minimal/Essential/Full Stack/Custom)
- App Router 기반 구조
- TypeScript Strict Mode

**기술 스택:**
- Next.js 15 (App Router)
- ShadCN/ui (UI 컴포넌트)
- Zustand (클라이언트 상태)
- Tanstack Query (서버 상태)
- Drizzle ORM (TypeScript ORM)
- Better Auth (인증)

**사용 시나리오:**
- 새로운 Next.js 앱 빠른 시작
- 타입 안전한 풀스택 앱
- 도메인 중심 설계

### 6. [Codex](./skills/codex/)
OpenAI Codex CLI를 사용하여 코드 분석, 리팩토링, 자동화된 편집을 수행합니다.

**주요 기능:**
- 대화형 모델 및 추론 레벨 선택 (gpt-5, gpt-5-codex)
- 샌드박스 모드 (read-only, workspace-write, danger-full-access)
- 세션 재개 기능 (codex exec resume --last)
- 자동화된 코드 편집 (--full-auto)

**사용 시나리오:**
- 코드 리뷰 및 분석
- 대규모 리팩토링 자동화
- 코드베이스 전체 수정 작업
- 이전 세션 이어서 작업

**샌드박스 모드:**
- `read-only`: 코드 분석 전용 (읽기만)
- `workspace-write`: 로컬 파일 수정
- `danger-full-access`: 네트워크 접근 포함 전체 권한

### 6-1. [Codex-Claude Loop](./skills/codex-claude-loop/) 🔄
Claude Code와 Codex를 결합한 이중 AI 엔지니어링 루프로 최상의 코드 품질을 보장합니다.

**핵심 워크플로우:**
- **Claude (계획 + 구현)** → **Codex (검증)** → **피드백** → **Claude (수정)** → **Codex (재검증)** → **반복**
- Claude가 모든 코드 작성, Codex가 모든 검증 담당
- 자체 수정 시스템으로 고품질 엔지니어링

**주요 기능:**
- 계획 단계: Claude가 아키텍처와 구현 계획 수립
- 검증 단계: Codex가 계획의 로직 에러, 보안 취약점 검토
- 구현 단계: Claude가 검증된 계획으로 코드 작성 (Edit/Write 도구 사용)
- 코드 리뷰: Codex가 구현된 코드의 버그, 성능, 보안 검증
- 수정 반영: Claude가 Codex 피드백 기반으로 코드 수정
- 재검증: Codex가 수정사항 확인

**언제 사용하나요:**
- ✅ 복잡한 기능 개발 (여러 단계)
- ✅ 보안/성능이 중요한 작업
- ✅ 대규모 리팩토링
- ✅ 높은 코드 품질이 필요할 때
- ❌ 간단한 일회성 수정 (과함)
- ❌ 프로토타입/실험 코드 (과함)

**실전 예시:**
```bash
# 1. Claude가 OAuth 2.0 로그인 계획 수립
# 2. Codex로 계획 검증
echo "Review this plan..." | codex exec -m gpt-5-codex --config model_reasoning_effort="high" --sandbox read-only

# 3. Claude가 검증된 계획으로 구현 (Edit/Write 도구 사용)
# 4. Codex가 구현된 코드 리뷰
echo "Review implementation..." | codex exec --sandbox read-only

# 5. Claude가 피드백 반영하여 코드 수정
# 6. Codex가 재검증
echo "Verify fixes..." | codex exec resume --last
```

**역할 분담:**
- **Claude**: 모든 코드 작성 및 수정
- **Codex**: 모든 검증 및 리뷰

**명령어 레퍼런스:**
- 계획 검증: `codex exec -m gpt-5-codex --sandbox read-only`
- 코드 리뷰: `codex exec --sandbox read-only`
- 재검증: `codex exec resume --last` (설정 자동 상속)

**모델 선택 가이드:**
- `gpt-5`: 빠른 일반 작업
- `gpt-5-codex`: 복잡한 코드 분석 (권장)

**Reasoning Effort:**
- `low`: 간단한 검증
- `medium`: 일반적인 작업 (권장)
- `high`: 보안/critical 로직

### 7. [Landing Page Guide](./skills/landing-page-guide/)
Next.js와 React로 고품질 전환율 높은 랜딩페이지를 제작하기 위한 종합 가이드입니다.

**주요 기능:**
- DESIGNNAS의 11가지 필수 요소 프레임워크 적용
- ShadCN UI 컴포넌트 통합
- SEO 최적화 및 접근성 표준 준수
- 반응형 디자인 및 성능 최적화

**11가지 필수 요소:**
1. 키워드가 포함된 URL
2. 회사 로고 (상단 왼쪽)
3. SEO 최적화된 제목과 부제목
4. 주요 CTA (히어로 섹션)
5. 사회적 증거 (리뷰, 통계)
6. 이미지 또는 동영상
7. 핵심 이점/기능 (3-6개)
8. 고객 후기 (4-6개)
9. FAQ 섹션 (5-10개 질문)
10. 최종 CTA (하단)
11. 연락처 정보 및 법적 페이지

**기술 스택:**
- Next.js 14+ (App Router)
- TypeScript
- Tailwind CSS
- ShadCN UI

**사용 시나리오:**
- 마케팅 랜딩 페이지 제작
- 제품 소개 페이지 개발
- 전환율 최적화가 필요한 프로모션 페이지
- SaaS/이커머스/서비스/이벤트 랜딩 페이지

### 8. [Card News Generator](./skills/card-news-generator/)
600x600 인스타그램 스타일 카드 뉴스 시리즈를 자동으로 생성합니다.

**주요 기능:**
- 주제와 색상만 입력하면 자동 생성
- 5-7장의 카드 시리즈 자동 제작
- 자동 텍스트 래핑 및 레이아웃
- RGB to Hex 색상 변환
- 단일 카드/멀티 카드 모드

**캔버스 사양:**
- 크기: 600x600 픽셀 (인스타그램 최적화)
- 자동 텍스트 줄바꿈
- 번호 배지, 제목, 본문 계층 구조
- 다양한 색상 프리셋 제공

**권장 색상:**
- 베이지: `245,243,238`
- 핑크: `255,229,229`
- 민트: `224,244,241`
- 라벤더: `232,224,245`
- 피치: `255,232,214`
- 스카이 블루: `227,242,253`

**사용 시나리오:**
- 소셜 미디어 카드 뉴스 제작
- 인스타그램 콘텐츠 시리즈
- 정보 전달용 카드 이미지
- 교육/마케팅 콘텐츠

### 9. [Card News Generator V2](./skills/card-news-generator/) 🆕
배경 이미지를 지원하는 향상된 카드 뉴스 생성기입니다.

**V2 새로운 기능:**
- ✨ **배경 이미지 지원**: 폴더의 이미지를 배경으로 자동 적용
- ✨ **Cafe24Ssurround 폰트**: 번들 폰트 포함, 별도 설치 불필요
- ✨ **반투명 박스 + 테두리**: 텍스트 영역에 둥근 박스와 흰색 테두리
- ✨ **컴팩트 디자인**: 정사각형에 가까운 중앙 정렬 박스
- ✨ **오버레이 조절**: 텍스트 가독성을 위한 어두운 오버레이 (0.0-1.0)
- ✨ **자동 텍스트 색상**: 배경 이미지 사용 시 흰색으로 자동 전환

**기술 사양:**
- 배경 이미지 자동 크롭 및 리사이징 (600x600)
- 지원 형식: JPG, JPEG, PNG, WebP, BMP
- macOS/Linux 자동 폰트 감지
- 텍스트 박스 너비: 캔버스의 65% (양쪽 여백 확보)

**사용 예시:**
```bash
python auto_generator.py \
  --topic "서울 부동산" \
  --image-folder ./my-images \
  --overlay-opacity 0.6 \
  --output-dir ./output
```

**사용 시나리오:**
- 실제 사진을 배경으로 한 카드 뉴스
- 여행, 부동산, 음식 등 비주얼이 중요한 콘텐츠
- 전문적이고 세련된 디자인이 필요한 경우
- 배경 이미지로 브랜드 아이덴티티 강화

### 10. [Web to Markdown](./skills/web-to-markdown/) 🌐
웹페이지 URL을 마크다운 형식으로 변환하여 저장하는 스킬입니다.

**주요 기능:**
- 3가지 변환 모드 지원
  - **일반 모드**: 읽기 좋은 마크다운 변환
  - **AI 최적화 모드**: AI 컨텍스트용 구조화된 형태 (YAML 프론트매터, 핵심 요약 포함)
  - **듀얼 모드**: 원본 + AI 최적화 버전 2개 파일 동시 생성 ⭐
- **동적 콘텐츠 처리 ⭐ NEW**
  - WebFetch로 가져오지 못한 JavaScript 렌더링 페이지 자동 감지
  - Playwright로 브라우저 실행하여 동적 콘텐츠 가져오기
  - MCP Playwright 또는 Node Playwright 지원
- 여러 URL 일괄 변환
- 특정 섹션만 추출
- 마크다운 포맷 커스터마이징
- WebFetch 자동 캐싱 (15분)

**변환 모드:**
```
# 일반 모드
웹페이지를 마크다운으로 변환해줘

# AI 최적화 모드
AI가 읽기 좋게 변환해줘
컨텍스트로 사용하기 좋게 변환해줘

# 듀얼 모드 (권장)
원본이랑 AI 최적화 버전 둘 다 만들어줘
```

**AI 최적화 모드 특징:**
- YAML 프론트매터 (제목, URL, 주제, 핵심 요약 등)
- 구조화된 섹션 (핵심 요약, 주요 내용, 인사이트, 실용적 적용)
- 토큰 30-50% 절감
- AI가 3초 안에 핵심 파악 가능

**파일명 규칙:**
- 원본: `article.md`
- AI 최적화: `article.context.md`

**사용 시나리오:**
- 기술 문서 아카이빙
- 블로그 글 백업
- 학습 자료 구축
- RAG 시스템용 데이터 준비
- AI 에이전트 컨텍스트 자료 생성

**사용 예시:**
```
# 듀얼 모드
User: https://docs.python.org/3/tutorial 원본이랑 AI 최적화 버전 둘 다 만들어줘

Claude: 듀얼 모드로 변환하겠습니다.
- python-tutorial.md (원본 - 사람이 읽기 좋음)
- python-tutorial.context.md (AI 최적화 - 컨텍스트용)

# 동적 콘텐츠 (NEW)
User: https://www.codedeck.kr/card-news/xxx 마크다운으로 변환해줘

Claude: [WebFetch 시도]
        ⚠️ 내용이 거의 비어있네요. JavaScript 렌더링 페이지인 것 같습니다.
        Playwright로 재시도할까요?

User: Yes

Claude: ⏳ Playwright로 페이지 로딩...
        ✅ JavaScript 렌더링 완료
        ✅ 마크다운 변환 완료 (1,442줄)
```

## 스킬 사용 방법

### 방법 1: 마켓플레이스를 통한 설치 (권장)

#### 1. 마켓플레이스 추가

```bash
/plugin marketplace add bear2u/claude-plugins
```

#### 2. 사용 가능한 플러그인 확인

```bash
/plugin marketplace list
```

#### 3. 원하는 플러그인 설치

```bash
# Flutter 프로젝트 초기화
/plugin marketplace install suji-father-marketplace@flutter-init

# Next.js 15 프로젝트 초기화
/plugin marketplace install suji-father-marketplace@nextjs15-init

# 코드 변경사항 자동 문서화
/plugin marketplace install suji-father-marketplace@code-changelog

# Codex CLI 통합
/plugin marketplace install suji-father-marketplace@codex

# Codex-Claude 이중 AI 루프
/plugin marketplace install suji-father-marketplace@codex-claude-loop

# 메타 프롬프트 생성기
/plugin marketplace install suji-father-marketplace@meta-prompt-generator

# 프롬프트 향상기
/plugin marketplace install suji-father-marketplace@prompt-enhancer

# 웹페이지 마크다운 변환
/plugin marketplace install suji-father-marketplace@web-to-markdown

# 카드 뉴스 생성기
/plugin marketplace install suji-father-marketplace@card-news-generator

# 카드 뉴스 생성기 V2 (배경 이미지 지원)
/plugin marketplace install suji-father-marketplace@card-news-generator-v2

# 랜딩페이지 가이드
/plugin marketplace install suji-father-marketplace@landing-page-guide
```

#### 4. 설치된 플러그인 확인

```bash
/plugin list
```

#### 5. 플러그인 업데이트

```bash
# 특정 플러그인 업데이트
/plugin update suji-father-marketplace@flutter-init

# 또는 모든 플러그인 업데이트
/plugin update
```

#### 6. 플러그인 삭제

```bash
# 특정 플러그인 삭제
/plugin remove flutter-init

# 또는 마켓플레이스 전체 삭제
/plugin marketplace remove suji-father-marketplace
```

### 방법 2: 수동 설치

1. 스킬을 Claude Code 스킬 디렉토리로 복사:

```bash
# 유저 스킬로 설치 (전역)
cp -r skills/* ~/.claude/skills/

# 또는 프로젝트 스킬로 설치 (프로젝트별)
cp -r skills/* ./.claude/skills/
```

2. Claude Code에서 스킬 확인:

```
/skills
```

### 실행

각 스킬은 스킬 이름으로 실행할 수 있습니다:

```
code-changelog
meta-prompt-generator
prompt-enhancer
flutter-init
nextjs15-init
codex
codex-claude-loop          # Claude + Codex 이중 AI 루프
landing-page-guide
card-news-generator        # 기본 단색 배경 카드 생성
card-news-generator (V2)   # 배경 이미지 지원 (동일 스킬, 고급 기능)
web-to-markdown            # 웹페이지를 마크다운으로 변환
```

## 폴더 구조

```
my-skills-hub/
├── skills/
│   ├── code-changelog/          # 코드 변경사항 자동 문서화
│   │   ├── skill.md             # 스킬 설명
│   │   └── ...                  # 스킬 파일들
│   ├── meta-prompt-generator/   # 메타 프롬프트 생성기
│   │   ├── skill.md
│   │   └── ...
│   ├── prompt-enhancer/         # 프롬프트 향상기
│   │   ├── skill.md
│   │   └── ...
│   ├── flutter-init/            # Flutter 프로젝트 생성
│   │   ├── skill.md
│   │   └── ...
│   ├── nextjs15-init/           # Next.js 15 프로젝트 생성
│   │   ├── skill.md
│   │   └── ...
│   ├── codex/                   # Codex CLI 코드 리뷰/분석
│   │   └── skill.md
│   ├── codex-claude-loop/       # Claude + Codex 이중 AI 엔지니어링 루프
│   │   ├── SKILL.md
│   │   └── README.md
│   ├── landing-page-guide/      # 랜딩페이지 제작 가이드
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── 11-essential-elements.md
│   │       └── component-examples.md
│   ├── card-news-generator/     # 카드 뉴스 자동 생성
│   │   ├── SKILL.md
│   │   └── ...
│   └── web-to-markdown/         # 웹페이지 마크다운 변환
│       ├── SKILL.md
│       └── ...
└── README.md                     # 이 파일
```

## 스킬별 상세 정보

각 스킬 폴더의 `skill.md` 파일에서 더 자세한 정보를 확인할 수 있습니다:

- [Code Changelog 상세 정보](./skills/code-changelog/skill.md)
- [Meta Prompt Generator 상세 정보](./skills/meta-prompt-generator/skill.md)
- [Prompt Enhancer 상세 정보](./skills/prompt-enhancer/skill.md)
- [Flutter Init 상세 정보](./skills/flutter-init/skill.md)
- [Next.js 15 Init 상세 정보](./skills/nextjs15-init/skill.md)
- [Codex 상세 정보](./skills/codex/skill.md)
- [Codex-Claude Loop 상세 정보](./skills/codex-claude-loop/SKILL.md)
- [Codex-Claude Loop 사용법](./skills/codex-claude-loop/README.md)
- [Landing Page Guide 상세 정보](./skills/landing-page-guide/SKILL.md)
- [Card News Generator 상세 정보](./skills/card-news-generator/SKILL.md)
- [Card News Generator V2 상세 정보](./skills/card-news-generator/V2_FEATURES.md)
- [Web to Markdown 상세 정보](./.claude/skills/web-to-markdown/SKILL.md)

## 기여

새로운 스킬을 추가하거나 기존 스킬을 개선하고 싶으시다면:

1. `skills/` 폴더에 새로운 스킬 디렉토리 생성
2. `skill.md` 파일 작성 (스킬 메타데이터 및 설명)
3. 필요한 파일들 추가
4. README.md에 스킬 정보 추가

## 라이선스

MIT License

## 참고

이 스킬들은 Claude Code의 공식 문서를 참고하여 작성되었습니다:
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)

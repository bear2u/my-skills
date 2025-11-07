# 스킬 배포 가이드 (NPM 패키지)

> 자신이 만든 Claude Code 스킬들을 `npx claude-plugins skills install @your-org/skills/skill-name` 형태로 간단하게 배포하고 업데이트하는 방법

## 목차
1. [개요](#개요)
2. [사전 준비](#사전-준비)
3. [NPM 패키지 구조 만들기](#npm-패키지-구조-만들기)
4. [첫 배포하기](#첫-배포하기)
5. [업데이트 배포하기](#업데이트-배포하기)
6. [사용자 설치 방법](#사용자-설치-방법)
7. [버전 관리 Best Practices](#버전-관리-best-practices)

---

## 개요

현재 `skills/` 폴더에 있는 스킬들:
- card-news-generator
- card-news-generator-v2
- code-changelog
- codex
- codex-claude-cursor-loop
- codex-claude-loop
- flutter-init
- landing-page-guide
- meta-prompt-generator
- midjourney-cardnews-bg
- nextjs15-init
- prompt-enhancer
- web-to-markdown

**목표:**
```bash
# Anthropic 방식
npx claude-plugins skills install @anthropics/skills/pptx

# 당신의 스킬 (목표)
npx claude-plugins skills install @your-org/skills/card-news-generator
npx claude-plugins skills install @your-org/skills/flutter-init
```

---

## 사전 준비

### 1. NPM 계정 생성

```bash
# npmjs.com에서 계정 생성 후
npm login

# 로그인 확인
npm whoami
```

### 2. Scoped Package 이름 결정

- **Organization 사용**: `@your-org/skills` (권장)
- **개인 이름 사용**: `@username/skills`

예: `@bear2u/claude-skills`, `@suji-father/skills`

---

## NPM 패키지 구조 만들기

### 옵션 A: 새 폴더에 패키지 만들기 (권장)

```bash
# 새로운 패키지 폴더 생성
mkdir claude-skills-package
cd claude-skills-package

# package.json 생성
npm init -y
```

### 옵션 B: 현재 프로젝트를 그대로 사용

현재 `my-skills-hub` 프로젝트에 `package.json`만 추가

### package.json 설정

```json
{
  "name": "@your-org/claude-skills",
  "version": "1.0.0",
  "description": "Claude Code를 위한 커스텀 스킬 모음 - 개발 생산성 향상 도구",
  "main": "index.js",
  "author": "Your Name <your.email@example.com>",
  "license": "MIT",
  "keywords": [
    "claude-code",
    "skills",
    "ai",
    "automation",
    "productivity"
  ],
  "files": [
    "skills/**/*",
    "README.md"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/your-org/my-skills-hub"
  },
  "bugs": {
    "url": "https://github.com/your-org/my-skills-hub/issues"
  },
  "homepage": "https://github.com/your-org/my-skills-hub#readme"
}
```

**주요 설정 설명:**
- `name`: NPM 패키지 이름 (반드시 `@`로 시작하는 scoped package)
- `version`: 시맨틱 버전 (major.minor.patch)
- `files`: NPM에 포함할 파일/폴더 목록
- `keywords`: 검색 최적화용 키워드

### 스킬 폴더 구조

```
claude-skills-package/
├── package.json
├── README.md
├── LICENSE
└── skills/
    ├── card-news-generator/
    │   ├── SKILL.md
    │   ├── generate_card.py
    │   └── ...
    ├── flutter-init/
    │   ├── skill.md
    │   └── ...
    ├── code-changelog/
    ├── codex/
    ├── codex-claude-loop/
    ├── nextjs15-init/
    ├── prompt-enhancer/
    ├── web-to-markdown/
    └── ...
```

### 스킬 복사 (옵션 A 선택 시)

```bash
# 현재 my-skills-hub의 스킬들을 복사
cp -r ../my-skills-hub/skills ./
```

### README.md 작성

```markdown
# @your-org/claude-skills

Claude Code를 위한 커스텀 스킬 모음입니다.

## 설치 방법

```bash
# 개별 스킬 설치
npx claude-plugins skills install @your-org/claude-skills/card-news-generator
npx claude-plugins skills install @your-org/claude-skills/flutter-init
```

## 포함된 스킬

- **card-news-generator**: 600x600 인스타그램 카드 뉴스 자동 생성
- **flutter-init**: Flutter Clean Architecture 프로젝트 자동 생성
- **code-changelog**: AI 코드 변경사항 자동 문서화
- **codex**: OpenAI Codex CLI 통합
- **nextjs15-init**: Next.js 15 App Router 프로젝트 생성
- 외 8개 스킬

## 라이선스

MIT
```

---

## 첫 배포하기

### 1. 패키지 검증

```bash
# package.json 문법 확인
npm pkg fix

# 패키지 내용 미리보기
npm pack --dry-run
```

### 2. .npmignore 파일 생성 (선택사항)

불필요한 파일 제외:

```bash
cat > .npmignore << 'EOF'
.git
.github
.vscode
.DS_Store
node_modules
*.log
test/
examples/
.env
EOF
```

### 3. NPM 로그인

```bash
# 최초 1회만
npm login

# 로그인 확인
npm whoami
```

### 4. Scoped 패키지 퍼블리시

```bash
# Public 패키지로 배포
npm publish --access public
```

**출력 예시:**
```
+ @your-org/claude-skills@1.0.0
```

### 5. 배포 확인

```bash
# NPM 웹사이트에서 확인
open https://www.npmjs.com/package/@your-org/claude-skills

# 또는 직접 설치 테스트
npx claude-plugins skills install @your-org/claude-skills/flutter-init
```

---

## 업데이트 배포하기

### 1. 코드 수정

스킬을 수정하거나 새로운 스킬을 추가합니다.

### 2. 버전 업데이트

```bash
# 방법 1: 자동 버전 증가
npm version patch   # 1.0.0 → 1.0.1 (버그 수정)
npm version minor   # 1.0.0 → 1.1.0 (새 기능)
npm version major   # 1.0.0 → 2.0.0 (호환성 깨지는 변경)

# 방법 2: 수동으로 package.json 수정
# "version": "1.0.1"
```

**시맨틱 버전 가이드:**
- **patch (1.0.x)**: 버그 수정
- **minor (1.x.0)**: 새 기능 추가 (하위 호환)
- **major (x.0.0)**: 호환성 깨지는 변경

### 3. CHANGELOG.md 작성 (권장)

```markdown
## [1.1.0] - 2025-01-15

### Added
- card-news-generator-v2: 배경 이미지 지원 기능 추가
- landing-page-guide: 새 스킬 추가

### Changed
- flutter-init: Riverpod 3.0으로 업그레이드
- code-changelog: UI 다크모드 개선

### Fixed
- codex: 세션 재개 시 설정 상속 버그 수정
```

### 4. Git 커밋 및 태그

```bash
# 변경사항 커밋
git add .
git commit -m "chore: Release version 1.1.0"

# Git 태그 생성 (선택사항)
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main --tags
```

### 5. NPM에 재배포

```bash
# 다시 퍼블리시
npm publish
```

**출력 예시:**
```
+ @your-org/claude-skills@1.1.0
```

### 6. 사용자에게 업데이트 알림

README.md에 최신 버전 정보 업데이트:

```markdown
## 최신 버전

현재 버전: `1.1.0`

### 새로운 기능
- card-news-generator-v2 추가
- landing-page-guide 추가
```

---

## 사용자 설치 방법

### Personal Skill (전역 설치)

```bash
# 개별 스킬 설치
npx claude-plugins skills install @your-org/claude-skills/card-news-generator

# 여러 스킬 설치
npx claude-plugins skills install @your-org/claude-skills/flutter-init
npx claude-plugins skills install @your-org/claude-skills/codex
npx claude-plugins skills install @your-org/claude-skills/nextjs15-init
```

### Project Skill (프로젝트별 설치)

```bash
# 프로젝트 디렉토리에서
npx claude-plugins skills install @your-org/claude-skills/flutter-init --project
```

### 설치 위치

- **Personal**: `~/.claude/skills/`
- **Project**: `.claude/skills/`

### 스킬 사용

```bash
# Claude Code에서
card-news-generator
flutter-init
codex-claude-loop
```

### 설치된 스킬 확인

```bash
# Claude Code에서
/skills
```

### 스킬 업데이트

사용자가 최신 버전으로 업데이트하려면:

```bash
# 스킬 재설치 (최신 버전으로 덮어쓰기)
npx claude-plugins skills install @your-org/claude-skills/card-news-generator
```

---

## 버전 관리 Best Practices

### 1. 시맨틱 버저닝 사용

```
major.minor.patch
  │     │     │
  │     │     └─ 버그 수정 (1.0.1)
  │     └─────── 새 기능 추가 (1.1.0)
  └───────────── 호환성 깨지는 변경 (2.0.0)
```

**예시:**
- `1.0.0` → `1.0.1`: codex 스킬 버그 수정
- `1.0.0` → `1.1.0`: landing-page-guide 스킬 추가
- `1.0.0` → `2.0.0`: 스킬 구조 대대적 변경

### 2. Git 태그와 동기화

```bash
# package.json 버전과 Git 태그를 일치시키기
npm version patch -m "chore: Release version %s"

# 이 명령은 자동으로:
# 1. package.json 버전 증가
# 2. Git commit 생성
# 3. Git tag 생성
```

### 3. CHANGELOG.md 유지

```markdown
# Changelog

## [Unreleased]
### Added
- 작업 중인 새 기능

## [1.2.0] - 2025-01-15
### Added
- card-news-generator-v2: 배경 이미지 지원
- landing-page-guide: 랜딩페이지 제작 가이드

### Changed
- flutter-init: Riverpod 3.0으로 업그레이드
- code-changelog: 다크모드 UI 개선

### Fixed
- codex: 세션 재개 시 설정 상속 버그 수정

## [1.1.0] - 2025-01-10
...
```

### 4. 릴리즈 워크플로우

```bash
# 1. 코드 수정
# 2. 변경사항 테스트
# 3. CHANGELOG.md 업데이트
# 4. 버전 증가 및 태그
npm version minor -m "chore: Release version %s"

# 5. GitHub에 푸시
git push origin main --tags

# 6. NPM에 퍼블리시
npm publish

# 7. GitHub Release 생성 (선택사항)
gh release create v1.2.0 --title "v1.2.0" --notes "$(cat CHANGELOG.md)"
```

---

## 고급 활용

### Private NPM 패키지 배포

```bash
# Organization Private 패키지
npm publish --access restricted

# 사용자는 NPM 로그인 후 설치 가능
npm login
npx claude-plugins skills install @your-org/claude-skills/flutter-init
```

### Monorepo로 관리하기

여러 스킬 컬렉션을 관리할 경우:

```
my-skills-monorepo/
├── packages/
│   ├── ai-skills/          # @your-org/ai-skills
│   │   └── skills/
│   ├── dev-tools/          # @your-org/dev-tools
│   │   └── skills/
│   └── design-skills/      # @your-org/design-skills
│       └── skills/
└── package.json
```

### NPM Scripts 활용

```json
{
  "scripts": {
    "test": "echo 'Run skill tests'",
    "lint": "echo 'Lint skill files'",
    "prepublishOnly": "npm run test && npm run lint",
    "release:patch": "npm version patch && npm publish && git push --tags",
    "release:minor": "npm version minor && npm publish && git push --tags",
    "release:major": "npm version major && npm publish && git push --tags"
  }
}
```

**사용 예:**
```bash
# 버전 증가, 퍼블리시, 태그 푸시를 한 번에
npm run release:minor
```

---

## 참고 자료

- [Claude Code 공식 문서](https://code.claude.com/docs)
- [NPM Scoped Packages](https://docs.npmjs.com/about-scopes)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [NPM Scripts](https://docs.npmjs.com/cli/v9/using-npm/scripts)

---

## FAQ

### Q1: 개별 스킬마다 별도 패키지를 만들어야 하나요?

**A:** 아니요, 하나의 패키지에 모든 스킬을 포함하는 것이 더 좋습니다:
- 관리가 간편함
- 버전 관리가 일관됨
- 사용자는 원하는 스킬만 선택해서 설치 가능
- `@anthropics/skills`도 이런 방식 사용

**예:**
```bash
# 하나의 패키지에서 개별 스킬 설치
npx claude-plugins skills install @your-org/claude-skills/flutter-init
npx claude-plugins skills install @your-org/claude-skills/card-news-generator
```

### Q2: Private 스킬은 어떻게 배포하나요?

**A:** NPM Private 패키지로 배포:
```bash
# 배포
npm publish --access restricted

# 사용자는 로그인 후 설치
npm login
npx claude-plugins skills install @your-org/private-skills/internal-tool
```

**주의:** Private 패키지는 유료 NPM 계정 필요 (조직 계정 권장)

### Q3: 스킬 업데이트는 어떻게 배포하나요?

**A:** 간단한 3단계:
```bash
# 1. 버전 증가
npm version patch

# 2. 퍼블리시
npm publish

# 3. Git 푸시
git push --tags
```

사용자는 재설치만 하면 자동으로 최신 버전:
```bash
npx claude-plugins skills install @your-org/claude-skills/flutter-init
```

### Q4: NPM Organization은 어떻게 만드나요?

**A:** NPM 웹사이트에서:
1. https://www.npmjs.com 로그인
2. "Create Organization" 클릭
3. Organization 이름 입력 (예: `your-org`)
4. 패키지 이름을 `@your-org/claude-skills`로 설정

**무료 vs 유료:**
- 무료: Public 패키지만
- 유료 ($7/월): Private 패키지 지원

### Q5: 배포 전 테스트는 어떻게 하나요?

**A:** 로컬 테스트 방법:
```bash
# 1. 패키지 압축 생성
npm pack

# 2. 생성된 .tgz 파일로 설치 테스트
npx claude-plugins skills install ./your-org-claude-skills-1.0.0.tgz/flutter-init

# 3. 정상 작동 확인 후 퍼블리시
npm publish --access public
```

### Q6: 스킬 이름 충돌을 방지하려면?

**A:** Scoped package(`@your-org/`)를 사용하면 자동으로 네임스페이스가 분리됩니다.

**예:**
- `@anthropics/skills/pptx`
- `@your-org/skills/pptx`
- `@another-org/skills/pptx`

모두 다른 패키지로 인식되어 충돌 없음!

---

## 빠른 시작 체크리스트

1. ✅ NPM 계정 생성 및 로그인
2. ✅ `package.json` 생성 (scoped package 이름)
3. ✅ `skills/` 폴더에 스킬들 구성
4. ✅ `README.md` 작성
5. ✅ `npm pack --dry-run`으로 검증
6. ✅ `npm publish --access public`으로 배포
7. ✅ 설치 테스트
8. ✅ GitHub에 코드 푸시

**처음 배포:**
```bash
npm login
npm publish --access public
```

**업데이트 배포:**
```bash
npm version patch
npm publish
git push --tags
```

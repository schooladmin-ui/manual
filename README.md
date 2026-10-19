# 🏫 홍익여고 온라인교무실 업무 매뉴얼 포털 (7대 핵심 가이드북)

> **교원 디지털 업무 지원 및 Google Workspace · 온라인교무실 활용 7대 핵심 가이드북 종합 포털**  
> 모든 가이드와 고화질 스크린샷 이미지가 `index.html` 단일 파일에 내장되어 있어, 외부 서버 없이 오프라인 및 웹 어디서든 즉시 구동 및 배포할 수 있습니다.

---

## 📌 목차
1. [프로젝트 개요](#-프로젝트-개요)
2. [수록 매뉴얼 목록 (7종)](#-수록-매뉴얼-목록-7종)
3. [주요 기능](#-주요-기능)
4. [파일 구조](#-파일-구조)
5. [배포 및 실행 방법](#-배포-및-실행-방법)
6. [매뉴얼 수정 및 재빌드 방법](#-매뉴얼-수정-및-재빌드-방법)
7. [유의 사항](#-유의-사항)

---

## 📖 프로젝트 개요

본 프로젝트는 홍익여자고등학교 교원의 원활한 디지털 교무 업무를 지원하기 위해 제작된 종합 매뉴얼 포털입니다.  
Chrome 브라우저 초기 설정부터 온라인교무실 접속 및 바로가기 앱 설치, Google Sites 편집, Google NotebookLM AI 활용, 공유 폴더 보안 권한 설정, 연수서명부 날인까지 **총 7개 매뉴얼(33단계 실무 가이드)**을 체계적으로 묶어 제공합니다.

---

## 📑 수록 매뉴얼 목록 (7종)

| 번호 | 매뉴얼 제목 | 분류 | 단계 수 | 원본 Canva 연동 |
|:---:|:---|:---:|:---:|:---:|
| **01** | [크롬브라우저 기본앱으로 설정하는 방법](chrome-default-app-guide-with-canva-link.html) | 브라우저 환경 | 3단계 | [Canva 열기](https://www.canva.com/design/DAGotK1iBWQ/fQ9N3piaD0zZCDtNWv6vCw/view?utm_content=DAGotK1iBWQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h39e2295cc7) |
| **02** | [크롬 북마크바 표시 방법](bookmark-bar-manual-with-canva-link.html) | 브라우저 환경 | 3단계 | [Canva 열기](https://www.canva.com/design/DAGoE56L5Qw/zEwEBK0UluCzBb1HR838Cg/view?utm_content=DAGoE56L5Qw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7dc1509390) |
| **03** | [바탕화면에 온라인교무실 바로가기 버튼 만들기](desktop-button-guide-manual.html) | 온라인교무실 | 4단계 | [Canva 열기](https://www.canva.com/design/DAHGJQe8CAA/kYI9m7jIEDhPaAbkuLZDGg/view?utm_content=DAHGJQe8CAA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=ha7f0287432) |
| **04** | [메인 페이지 편집 방법](main-page-edit-guide-manual.html) | 온라인교무실 | 4단계 | [Canva 열기](https://www.canva.com/design/DAGm6pqOZJM/rQnX-rH46Qv1cxtFaN2xhg/view?utm_content=DAGm6pqOZJM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h48af137ff0) |
| **05** | [구글 Notebook LM 생성 후 공유 방법](notebooklm-create-share-guide-manual.html) | AI & 업무도구 | 11단계 | [Canva 열기](https://www.canva.com/design/DAHIAXtwfPQ/c0rlZicbmWImDTlLa5JJkQ/view?utm_content=DAHIAXtwfPQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7c5f276f63) |
| **06** | [온라인교무실 공유 폴더 권한 설정 방법](permission-setting-guide-with-canva-link.html) | 보안 & 드라이브 | 4단계 | [Canva 열기](https://www.canva.com/design/DAGm6gX_4lM/rVOmpsykESZmuqzTnOMz8A/view?utm_content=DAGm6gX_4lM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=hb1133ff80a) |
| **07** | [연수서명부 서명 방법](training-signature-guide-manual.html) | 교무 행정 | 4단계 | [Canva 열기](https://www.canva.com/design/DAGm6jijC7A/i3ovxr1djLZxKIW9JRvAKg/view?utm_content=DAGm6jijC7A&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h1e3a1fe2c0) |

---

## ✨ 주요 기능

### 1. 단일 파일 완성형 포털 (All-in-One SPA)
- 별도의 이미지 폴더나 백엔드 서버 없이 `index.html` 하나로 7개 매뉴얼 전체가 완벽 구동됩니다.
- 모든 스크린샷 이미지가 `base64`로 인코딩되어 있어 인터넷이 차단된 폐쇄망이나 오프라인 환경에서도 100% 정상 작동합니다.

### 2. 홈 대시보드 및 실시간 검색
- **실시간 검색**: 제목, 요약문, 개별 단계 키워드까지 타이핑 즉시 실시간 필터링 (`/` 키로 검색창 포커스).
- **카테고리 칩 필터**: `전체`, `브라우저 환경`, `온라인교무실`, `AI & 도구`, `보안 & 권한`, `교무 행정`.
- **단계 미리보기**: 카드 내에서 주요 절차 칩을 미리 확인 가능.

### 3. 일체형 매뉴얼 리더 뷰 (In-Portal Viewer)
- 카드 클릭 시 페이지 전환 없이 부드럽게 본문 뷰어로 이동.
- **상단 고정 툴바**:
  - `← 전체 목록으로` (홈 복귀)
  - 매뉴얼 즉시 전환 드롭다운 셀렉터
  - `이전` / `다음` 매뉴얼 간편 이동
  - `링크 복사` (현재 매뉴얼 해시 링크 클립보드 복사)
  - `인쇄` (현재 열람 중인 매뉴얼만 인쇄)

### 4. 고화질 스크린샷 확대 모달 (🔍)
- 각 단계의 돋보기(`🔍`) 버튼 클릭 시 전체 화면 크기의 고화질 캡처 팝업.
- 단일 이미지 및 멀티 이미지 갤러리 지원 (`ESC` 키 및 바깥 배경 클릭으로 닫기).

### 5. URL 해시 라우팅 지원
- 브라우저 주소창에 `#notebooklm`, `#chrome-default` 등 해시를 붙여 특정 매뉴얼로 직접 연결할 수 있으며, 뒤로가기/앞으로가기 내비게이션을 지원합니다.

---

## 📂 파일 구조

```
Outputs/
├── index.html                                    # 7개 매뉴얼 통합 웹 포털 (메인 배포 파일)
├── bundle_manuals.py                             # 7개 HTML을 모아 index.html로 빌드하는 스크립트
├── README.md                                     # 프로젝트 설명서 (본 문서)
│
├── chrome-default-app-guide-with-canva-link.html  # [1] 크롬 기본앱 설정 가이드 (독립 파일)
├── bookmark-bar-manual-with-canva-link.html       # [2] 크롬 북마크바 표시 가이드 (독립 파일)
├── desktop-button-guide-manual.html               # [3] 바탕화면 바로가기 버튼 가이드 (독립 파일)
├── main-page-edit-guide-manual.html               # [4] 메인 페이지 편집 가이드 (독립 파일)
├── notebooklm-create-share-guide-manual.html      # [5] Notebook LM 생성·공유 가이드 (독립 파일)
├── permission-setting-guide-with-canva-link.html  # [6] 공유 폴더 권한 설정 가이드 (독립 파일)
└── training-signature-guide-manual.html           # [7] 연수서명부 서명 가이드 (독립 파일)
```

---

## 🚀 배포 및 실행 방법

### 방법 1: GitHub Pages로 무료 호스팅 배포 (가장 권장)
1. GitHub에 새 저장소(Repository)를 생성하고 현재 폴더의 파일들을 커밋 & 푸시합니다:
   ```bash
   git init
   git add .
   git commit -m "feat: 홍익여고 온라인교무실 7대 매뉴얼 포털 구축"
   git branch -M main
   git remote add origin https://github.com/<사용자이름>/<저장소이름>.git
   git push -u origin main
   ```
2. GitHub 저장소의 **Settings → Pages** 메뉴로 이동합니다.
3. **Build and deployment → Branch**를 `main` 브랜치, 폴더는 `/ (root)`로 선택하고 **Save**를 누릅니다.
4. 약 1~2분 후 `https://<사용자이름>.github.io/<저장소이름>/` 형태의 웹 주소가 생성되어 교원들에게 공유할 수 있습니다.

### 방법 2: Vercel / Cloudflare Pages / Netlify 원클릭 배포
- Vercel이나 Netlify 웹 콘솔에 이 폴더를 그대로 **드래그 앤 드롭**하면 수초 내로 무료 글로벌 CDN 주소가 발급됩니다.

### 방법 3: 온라인교무실(Google 사이트) 내 일체형 삽입
1. 배포된 웹사이트 주소를 복사합니다.
2. Google Sites 온라인교무실 편집 화면에서 **[삽입] → [임베드 (URL로 삽입)]**을 선택합니다.
3. 복사한 주소를 입력하고 [전체 페이지]로 배치하면 온라인교무실 화면 안에 가이드북 포털이 내장됩니다.

### 방법 4: 오프라인 로컬 실행
- 인터넷이 연결되지 않은 PC나 교내 공유 드라이브, USB에서도 `index.html` 파일을 더블클릭하면 즉시 열립니다.

---

## 🛠️ 매뉴얼 수정 및 재빌드 방법

개별 매뉴얼 HTML 파일(`*.html`)의 내용이나 스타일, 안내 단계를 수정한 경우 다음 명령어로 `index.html`을 최신 상태로 갱신할 수 있습니다:

```bash
# Python 3 실행
python bundle_manuals.py
```

- 스크립트 실행 즉시 7개 매뉴얼의 본문 내용과 스크린샷 데이터를 자동으로 추출하여 `index.html`에 일괄 반영합니다.

---

## ⚠️ 유의 사항

1. **학교 대표 계정 로그인 필수**:
   - 모든 온라인교무실 및 Google 드라이브 작업은 개인 일반 Gmail이 아닌 교사 개인 학교 계정(**`@hongik68.sen.hs.kr`**)으로 로그인해야 정상적인 권한 적용 및 동기화가 이루어집니다.
2. **인쇄 가이드**:
   - 포털 상단의 **[인쇄]** 버튼을 누르면 브라우저 기본 내비게이션과 검색창이 자동으로 숨겨지고, 현재 선택된 매뉴얼 본문만 깔끔한 A4 규격 레이아웃으로 출력됩니다.

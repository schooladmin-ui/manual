import os
import re
import json

BASE_DIR = r"c:\Users\user\Desktop\html\06-온라인교무실 매뉴얼"
PAGES_DIR = os.path.join(BASE_DIR, "pages")
GOOGLE_SITES_URL = "https://sites.google.com/hongik68.sen.hs.kr/hongik-digitalfriend-homepage/%ED%99%88/%EB%A7%A4%EB%89%B4%EC%96%BC-%EA%B5%90%EC%82%AC%EC%9A%A9"
FOCUSPANG_PDF_VIEW = "https://drive.google.com/file/d/1rtdsy1Jcr7EAspvCyNfA1LN-Mb6OkUKd/view"

DEFAULT_CATEGORIES = [
    {"id": "office-basic", "name": "🛡️기본 환경 세팅", "theme": 0},
    {"id": "google-admin", "name": "🏢 온라인 교무실", "theme": 2},
    {"id": "comm-ai", "name": "💬 구글 채팅(Google Chat)", "theme": 1},
    {"id": "dibut-class", "name": "💻 디벗 수업 활용", "theme": 3},
]

CATEGORY_NAME_MAP = {c["id"]: c["name"] for c in DEFAULT_CATEGORIES}
CATEGORY_THEME_MAP = {c["id"]: c["theme"] for c in DEFAULT_CATEGORIES}

MANUALS = [
    # 1. 🛡️기본 환경 세팅 (3개)
    {
        "id": "chrome-default",
        "file": "chrome-default-app-guide-with-canva-link.html",
        "short_title": "크롬브라우저 기본앱으로 설정하는 방법",
        "full_title": "크롬브라우저 기본앱으로 설정하는 방법",
        "steps_count": 3,
        "canva": "https://www.canva.com/design/DAHD337E4mE/Fd2130n11p3n8x7MG2m03g/view?utm_content=DAHD337E4mE&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h950d3fd7fc",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "office-basic"
    },
    {
        "id": "bookmark-bar",
        "file": "bookmark-bar-manual-with-canva-link.html",
        "short_title": "크롬 북마크바 표시 방법",
        "full_title": "크롬 북마크바 표시 방법",
        "steps_count": 3,
        "canva": "https://www.canva.com/design/DAHD4F2dd8k/single-page-manual",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "office-basic"
    },
    {
        "id": "desktop-button",
        "file": "desktop-button-guide-manual.html",
        "short_title": "바탕화면에 온라인교무실 바로가기 버튼 만들기",
        "full_title": "바탕화면에 온라인교무실 바로가기 버튼 만들기",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAHELA3cS3w/t33c2501-d763-4430-a827-9d160b6c6122/view",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "office-basic"
    },

    # 2. 🏢 온라인 교무실 (4개)
    {
        "id": "main-page-edit",
        "file": "main-page-edit-guide-manual.html",
        "short_title": "메인 페이지 편집 방법",
        "full_title": "메인 페이지 편집 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAHEQ2_3d8k/single-page-manual",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "google-admin"
    },
    {
        "id": "notebooklm",
        "file": "notebooklm-create-share-guide-manual.html",
        "short_title": "구글 Notebook LM 생성 후 공유 방법",
        "full_title": "구글 Notebook LM 생성 후 공유 방법",
        "steps_count": 11,
        "canva": "https://www.canva.com/design/DAHEc7d9s8A/single-page-manual",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "google-admin"
    },
    {
        "id": "permission-setting",
        "file": "permission-setting-guide-with-canva-link.html",
        "short_title": "온라인교무실 공유 폴더 권한 설정 방법",
        "full_title": "온라인교무실 공유 폴더 권한 설정 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAHD4L6q2wU/single-page-manual",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "google-admin"
    },
    {
        "id": "training-signature",
        "file": "training-signature-guide-manual.html",
        "short_title": "연수서명부 서명 방법",
        "full_title": "연수서명부 서명 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAHE3k5t9xY/single-page-manual",
        "source_label": "원본 Canva 슬라이드 열기",
        "category": "google-admin"
    },

    # 3. 💬 구글 채팅(Google Chat) (3개)
    {
        "id": "google-chat",
        "file": "google-chat-space-guide.html",
        "short_title": "구글 채팅(Google Chat) 앱에서 채팅방(스페이스) 만드는 방법",
        "full_title": "구글 채팅(Google Chat) 앱에서 채팅방(스페이스) 만드는 방법",
        "steps_count": 4,
        "canva": "",
        "source_label": "",
        "category": "comm-ai"
    },
    {
        "id": "google-groups",
        "file": "google-groups-create-guide.html",
        "short_title": "그룹 만들기",
        "full_title": "그룹 만들기",
        "steps_count": 2,
        "canva": "",
        "source_label": "",
        "category": "comm-ai"
    },
    {
        "id": "manual-우리-학교--이제-구글-채팅-google-chat-으로-pdf-guide",
        "file": "우리 학교, 이제 구글 채팅(Google Chat)으로-pdf-guide.html",
        "short_title": "구글 채팅(Google Chat) 설치 방법",
        "full_title": "구글 채팅(Google Chat) 설치 방법",
        "steps_count": 1,
        "canva": "",
        "source_label": "",
        "category": "comm-ai"
    },

    # 4. 💻 디벗 수업 활용 (10개)
    {
        "id": "dibut-power-on",
        "file": "dibut-power-on-guide.html",
        "short_title": "디벗 전원이 켜지지 않을 때",
        "full_title": "디벗 전원이 켜지지 않을 때",
        "steps_count": 2,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "student-password-reset",
        "file": "student-password-reset-guide.html",
        "short_title": "학생 비번 재설정 방법",
        "full_title": "학생 비번 재설정 방법",
        "steps_count": 3,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "managed-bookmark-edit",
        "file": "managed-bookmark-edit-guide.html",
        "short_title": "북마크 수정하기 (관리 북마크)",
        "full_title": "북마크 수정하기 (관리 북마크)",
        "steps_count": 2,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "teacher-app-extension",
        "file": "teacher-app-extension-guide.html",
        "short_title": "앱 및 확장 프로그램 추가 방법 (교사용)",
        "full_title": "앱 및 확장 프로그램 추가 방법 (교사용)",
        "steps_count": 3,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "student-app-extension",
        "file": "student-app-extension-guide.html",
        "short_title": "앱 및 확장 프로그램 추가 방법 (학생용)",
        "full_title": "앱 및 확장 프로그램 추가 방법 (학생용)",
        "steps_count": 2,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "cursor-style-change",
        "file": "cursor-style-change-guide.html",
        "short_title": "기본 커서 모양 변경하기",
        "full_title": "기본 커서 모양 변경하기",
        "steps_count": 3,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "wired-mirroring-display",
        "file": "wired-mirroring-display-guide.html",
        "short_title": "유선 미러링 화면 복사 기능 구현하기",
        "full_title": "유선 미러링 화면 복사 기능 구현하기",
        "steps_count": 2,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
    {
        "id": "focuspang-guide",
        "file": "focuspang-guide.html",
        "short_title": "포커스팡(FocusPang) 활용 방법",
        "full_title": "포커스팡(FocusPang) 활용 방법",
        "steps_count": 5,
        "canva": FOCUSPANG_PDF_VIEW,
        "source_label": "📄 원본 PDF 새 창 열기",
        "category": "dibut-class"
    },
    {
        "id": "dibut-charging-1-2",
        "file": "dibut-charging-cabinet-1-2-guide.html",
        "short_title": "디벗 충전함 사용법 (1·2학년)",
        "full_title": "디벗 충전함 사용법 (1·2학년 - 앱코 패드뱅크)",
        "steps_count": 5,
        "canva": "",
        "source_label": "",
        "extra_action_html": '<button type="button" class="source-button" onclick="openEmbeddedPdfInNewTab(\'charging-1-2-pdf-viewer\')">📄 원본 PDF 새 창 열기</button>',
        "category": "dibut-class"
    },
    {
        "id": "dibut-charging-3",
        "file": "dibut-charging-cabinet-3-guide.html",
        "short_title": "디벗 충전함 사용법 (3학년)",
        "full_title": "디벗 충전함 사용법 (3학년 - 등대씨엔씨 도어락)",
        "steps_count": 4,
        "canva": GOOGLE_SITES_URL,
        "source_label": "원본 매뉴얼 페이지 열기",
        "category": "dibut-class"
    },
]

def update_title_row(content, m, file_url):
    canva_url = m.get("canva", "")
    source_label = m.get("source_label") or "원본 Canva 슬라이드 열기"
    extra_action_html = m.get("extra_action_html", "")

    def repl(m_row):
        inner = m_row.group(1)
        h1_m = re.search(r'(<h1[^>]*>.*?</h1>)', inner, re.DOTALL)
        if not h1_m:
            return m_row.group(0)
        h1_html = h1_m.group(1)
        canva_btn = f'\n  <a class="source-button" href="{canva_url}" target="_blank" rel="noopener">{source_label}</a>' if canva_url else ''
        extra_btn = f'\n  {extra_action_html}' if extra_action_html else ''
        actions = f'''<div class="title-actions">{canva_btn}{extra_btn}
  <a href="{file_url}" target="_blank" rel="noopener" class="pane-standalone-link" title="새 창에서 독립 파일로 열기">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
    독립창 열기
  </a>
</div>'''
        return f'<div class="title-row">{h1_html}{actions}</div>'
    
    return re.sub(r'<div class="title-row">(.*?)</div>', repl, content, count=1, flags=re.DOTALL)

manual_contents = {}
for m in MANUALS:
    fpath = os.path.join(PAGES_DIR, m["file"])
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        raw = fp.read()
    
    main_match = re.search(r'<main class="page">(.*?)</main>', raw, re.DOTALL)
    if main_match:
        content = main_match.group(1).strip()
        content = update_title_row(content, m, f"pages/{m['file']}")
        content = content.replace('href="google-groups-create-guide.html"', 'href="#google-groups"')
        content = re.sub(r'<button class="modal-close"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    else:
        content = "<div>매뉴얼 내용을 불러올 수 없습니다.</div>"
    
    manual_contents[m["id"]] = content

# Pre-render category tabs ('전체 보기' placed at the rightmost end)
cat_counts = {c["id"]: 0 for c in DEFAULT_CATEGORIES}
for m in MANUALS:
    cat_counts[m["category"]] = cat_counts.get(m["category"], 0) + 1

category_tabs_html = []
for idx, c in enumerate(DEFAULT_CATEGORIES):
    cnt = cat_counts.get(c["id"], 0)
    theme_idx = c.get("theme", idx % 8)
    category_tabs_html.append(f'''<button type="button" class="category-tab" data-cat-id="{c['id']}" data-cat-theme="{theme_idx}" onclick="selectCategory('{c['id']}')">
      <span class="cat-tab-name">{c['name']}</span>
      <span class="cat-tab-count">{cnt}</span>
    </button>''')

category_tabs_html.append(f'''<button type="button" class="category-tab active" data-cat-id="all" onclick="selectCategory('all')">
      <span class="cat-tab-name">📋 전체 보기</span>
      <span class="cat-tab-count">{len(MANUALS)}</span>
    </button>''')

# Manual Buttons with pastel category theme & compact height (no step count text)
buttons_html = []
for m in MANUALS:
    cat_name = CATEGORY_NAME_MAP.get(m["category"], "기타")
    theme_idx = CATEGORY_THEME_MAP.get(m["category"], 0)
    btn = f"""
    <a href="#{m['id']}" class="manual-nav-btn" data-id="{m['id']}" data-category="{m['category']}" data-cat-theme="{theme_idx}" title="{cat_name}" draggable="true" onclick="selectManual('{m['id']}'); event.preventDefault();">
      <span class="nav-btn-title">{m['short_title']}</span>
    </a>
    """
    buttons_html.append(btn)

# Manual content panes
panes_html = []
for m in MANUALS:
    pane = f"""
    <div id="pane-{m['id']}" class="manual-pane" data-id="{m['id']}" data-canva="{m['canva']}">
      <main class="page">
        {manual_contents[m['id']]}
      </main>
    </div>
    """
    panes_html.append(pane)

index_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>온라인 교무실 매뉴얼</title>
  <meta name="description" content="홍익여자고등학교 온라인 교무실 핵심 매뉴얼">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       1. Core Variables & Reset
       ========================================================= */
    :root {{
      --ink: #172033;
      --ink-dark: #0f172a;
      --ink-secondary: #334155;
      --muted: #5b6475;
      --muted-light: #94a3b8;
      --line: #dfe5ee;
      --line-light: #edf2f7;
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      
      --blue: #2563eb;
      --blue-dark: #1d4ed8;
      --blue-soft: #eff6ff;
      --blue-border: #bfdbfe;
      
      --red: #dc2626;
      --red-soft: #fef2f2;
      --green: #047857;
      --green-soft: #ecfdf5;
      --purple: #6d28d9;
      --purple-soft: #f5f3ff;
      
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 12px -2px rgba(15,23,42,0.08), 0 2px 6px -1px rgba(15,23,42,0.04);
      --shadow-lg: 0 12px 28px -4px rgba(15,23,42,0.12);
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --font-sans: 'Pretendard', system-ui, -apple-system, "Segoe UI", "Noto Sans KR", sans-serif;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      background: var(--bg-page);
      color: var(--ink);
      font-family: var(--font-sans);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* =========================================================
       2. Simple Header
       ========================================================= */
    .simple-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      box-shadow: var(--shadow-sm);
      position: static;
      top: 0;
      z-index: 50;
    }}

    .header-inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .header-title-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}

    .header-logo-icon {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 19px;
      box-shadow: 0 3px 8px rgba(37,99,235,0.25);
    }}

    .header-title {{
      font-size: clamp(20px, 3vw, 24px);
      font-weight: 900;
      letter-spacing: -0.03em;
      color: var(--ink-dark);
      margin: 0;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .btn-header-print {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: #f8fafc;
      border: 1px solid var(--line);
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }}

    .btn-header-print:hover {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
    }}

    .btn-header-deploy {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
      border: 1px solid #1d4ed8;
      color: #ffffff;
      font-size: 13px;
      font-weight: 750;
      cursor: pointer;
      font-family: inherit;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25);
      transition: all 0.15s ease;
    }}

    .btn-header-deploy:hover {{
      background: #1e40af;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}

    .btn-header-deploy[hidden] {{
      display: none !important;
    }}

    /* =========================================================
       3. Category Filter Bar & Manual Button Navigation Bar
       ========================================================= */
    .nav-bar-section {{
      background: #ffffff;
      border-bottom: 2px solid var(--line);
      padding: 14px 20px 16px;
      box-shadow: var(--shadow-sm);
      position: static;
      top: 71px;
      z-index: 40;
    }}

    .nav-bar-container {{
      max-width: 1280px;
      margin: 0 auto;
    }}

    .category-bar-wrap {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      padding-bottom: 12px;
      margin-bottom: 12px;
      border-bottom: 1px solid var(--line-light);
    }}

    .category-tabs {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .category-tab {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 8px 14px;
      border-radius: var(--radius-full);
      border: 1.5px solid var(--line);
      background: #f8fafc;
      color: var(--ink-secondary);
      font-size: 13.5px;
      font-weight: 750;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.16s ease;
      white-space: nowrap;
    }}

    .category-tab:hover {{
      border-color: var(--blue);
      color: var(--blue-dark);
      background: #ffffff;
    }}

    .category-tab[data-cat-theme="0"] {{ background: #eff6ff; border-color: #bfdbfe; color: #1e3a8a; }}
    .category-tab[data-cat-theme="1"] {{ background: #ecfdf5; border-color: #a7f3d0; color: #065f46; }}
    .category-tab[data-cat-theme="2"] {{ background: #f5f3ff; border-color: #ddd6fe; color: #4c1d95; }}
    .category-tab[data-cat-theme="3"] {{ background: #fffbeb; border-color: #fde68a; color: #92400e; }}
    .category-tab[data-cat-theme="4"] {{ background: #fff1f2; border-color: #fecdd3; color: #9f1239; }}
    .category-tab[data-cat-theme="5"] {{ background: #ecfeff; border-color: #a5f3fc; color: #155e75; }}
    .category-tab[data-cat-theme="6"] {{ background: #f7fee7; border-color: #d9f99d; color: #3f6212; }}
    .category-tab[data-cat-theme="7"] {{ background: #eef2ff; border-color: #c7d2fe; color: #3730a3; }}

    .category-tab.active {{
      background: var(--ink-dark);
      border-color: var(--ink-dark);
      color: #ffffff;
      box-shadow: 0 3px 10px rgba(15, 23, 42, 0.18);
    }}

    .category-tab[data-cat-theme="0"].active {{ background: #1d4ed8; border-color: #1d4ed8; color: #ffffff; box-shadow: 0 3px 10px rgba(29, 78, 216, 0.25); }}
    .category-tab[data-cat-theme="1"].active {{ background: #047857; border-color: #047857; color: #ffffff; box-shadow: 0 3px 10px rgba(4, 120, 87, 0.25); }}
    .category-tab[data-cat-theme="2"].active {{ background: #6d28d9; border-color: #6d28d9; color: #ffffff; box-shadow: 0 3px 10px rgba(109, 40, 217, 0.25); }}
    .category-tab[data-cat-theme="3"].active {{ background: #d97706; border-color: #d97706; color: #ffffff; box-shadow: 0 3px 10px rgba(217, 119, 6, 0.25); }}
    .category-tab[data-cat-theme="4"].active {{ background: #be123c; border-color: #be123c; color: #ffffff; box-shadow: 0 3px 10px rgba(190, 18, 60, 0.25); }}
    .category-tab[data-cat-theme="5"].active {{ background: #0e7490; border-color: #0e7490; color: #ffffff; box-shadow: 0 3px 10px rgba(14, 116, 144, 0.25); }}
    .category-tab[data-cat-theme="6"].active {{ background: #4d7c0f; border-color: #4d7c0f; color: #ffffff; box-shadow: 0 3px 10px rgba(77, 124, 15, 0.25); }}
    .category-tab[data-cat-theme="7"].active {{ background: #4338ca; border-color: #4338ca; color: #ffffff; box-shadow: 0 3px 10px rgba(67, 56, 202, 0.25); }}

    .category-tab.drag-over-cat {{
      border: 2px dashed var(--blue) !important;
      background: var(--blue-soft) !important;
      color: var(--blue-dark) !important;
      transform: scale(1.04);
    }}

    .cat-tab-count {{
      display: inline-grid;
      place-items: center;
      min-width: 22px;
      height: 20px;
      padding: 0 6px;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.08);
      color: inherit;
      font-size: 11.5px;
      font-weight: 800;
    }}

    .category-tab.active .cat-tab-count {{
      background: rgba(255, 255, 255, 0.22);
      color: #ffffff;
    }}

    .category-bar-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-category-edit {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 13px;
      border-radius: var(--radius-sm);
      border: 1.5px solid var(--line);
      background: #ffffff;
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 750;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}

    .btn-category-edit:hover {{
      background: var(--blue-soft);
      border-color: var(--blue-border);
      color: var(--blue-dark);
    }}

    .manual-nav-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 8px;
    }}

    .manual-nav-btn {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 9px 10px;
      border-radius: var(--radius-sm);
      background: #e8f2ff;
      border: 1.5px solid #b9d5ff;
      color: #1e3a8a;
      text-decoration: none;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      text-align: center;
      min-height: 44px;
      position: relative;
    }}

    /* 카테고리별 파스텔 배경색 테마 */
    .manual-nav-btn[data-cat-theme="0"] {{
      background: #e8f2ff;
      border-color: #b9d5ff;
      color: #1e3a8a;
    }}
    .manual-nav-btn[data-cat-theme="0"]:hover {{
      background: #dbeafe;
      border-color: #60a5fa;
      color: #1d4ed8;
    }}
    .manual-nav-btn[data-cat-theme="0"].active {{
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
      border-color: #1d4ed8;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="1"] {{
      background: #e6faef;
      border-color: #a7f3d0;
      color: #065f46;
    }}
    .manual-nav-btn[data-cat-theme="1"]:hover {{
      background: #d1fae5;
      border-color: #34d399;
      color: #047857;
    }}
    .manual-nav-btn[data-cat-theme="1"].active {{
      background: linear-gradient(135deg, #047857 0%, #059669 100%);
      border-color: #047857;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="2"] {{
      background: #f3eeff;
      border-color: #ddd6fe;
      color: #4c1d95;
    }}
    .manual-nav-btn[data-cat-theme="2"]:hover {{
      background: #ede9fe;
      border-color: #a78bfa;
      color: #5b21b6;
    }}
    .manual-nav-btn[data-cat-theme="2"].active {{
      background: linear-gradient(135deg, #6d28d9 0%, #7c3aed 100%);
      border-color: #6d28d9;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(109, 40, 217, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="3"] {{
      background: #fff6df;
      border-color: #fde68a;
      color: #92400e;
    }}
    .manual-nav-btn[data-cat-theme="3"]:hover {{
      background: #fef3c7;
      border-color: #fbbf24;
      color: #b45309;
    }}
    .manual-nav-btn[data-cat-theme="3"].active {{
      background: linear-gradient(135deg, #d97706 0%, #ea580c 100%);
      border-color: #d97706;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="4"] {{
      background: #ffeef2;
      border-color: #fecdd3;
      color: #9f1239;
    }}
    .manual-nav-btn[data-cat-theme="4"]:hover {{
      background: #ffe4e6;
      border-color: #fb7185;
      color: #be123c;
    }}
    .manual-nav-btn[data-cat-theme="4"].active {{
      background: linear-gradient(135deg, #be123c 0%, #e11d48 100%);
      border-color: #be123c;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(190, 18, 60, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="5"] {{
      background: #e6fafe;
      border-color: #a5f3fc;
      color: #155e75;
    }}
    .manual-nav-btn[data-cat-theme="5"]:hover {{
      background: #cffafe;
      border-color: #22d3ee;
      color: #0e7490;
    }}
    .manual-nav-btn[data-cat-theme="5"].active {{
      background: linear-gradient(135deg, #0e7490 0%, #0891b2 100%);
      border-color: #0e7490;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(14, 116, 144, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="6"] {{
      background: #f2fce2;
      border-color: #d9f99d;
      color: #3f6212;
    }}
    .manual-nav-btn[data-cat-theme="6"]:hover {{
      background: #ecfccb;
      border-color: #a3e635;
      color: #4d7c0f;
    }}
    .manual-nav-btn[data-cat-theme="6"].active {{
      background: linear-gradient(135deg, #4d7c0f 0%, #65a30d 100%);
      border-color: #4d7c0f;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(77, 124, 15, 0.3);
    }}

    .manual-nav-btn[data-cat-theme="7"] {{
      background: #eef2ff;
      border-color: #c7d2fe;
      color: #3730a3;
    }}
    .manual-nav-btn[data-cat-theme="7"]:hover {{
      background: #e0e7ff;
      border-color: #818cf8;
      color: #4338ca;
    }}
    .manual-nav-btn[data-cat-theme="7"].active {{
      background: linear-gradient(135deg, #4338ca 0%, #4f46e5 100%);
      border-color: #4338ca;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(67, 56, 202, 0.3);
    }}

    .manual-nav-btn[hidden] {{
      display: none !important;
    }}

    .manual-nav-btn:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .manual-nav-btn.active {{
      transform: translateY(-1px);
    }}

    .nav-btn-title {{
      font-size: 13.5px;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.02em;
      word-break: keep-all;
    }}

    .manual-nav-btn.dragging {{
      opacity: 0.4;
      transform: scale(0.97);
    }}

    .manual-nav-btn.drag-over {{
      border: 2px dashed var(--blue) !important;
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2) !important;
      transform: translateY(-2px);
    }}

    .manual-add-btn {{
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 10px;
      border-radius: var(--radius-sm);
      background: #f8fafc;
      border: 2px dashed #93c5fd;
      color: var(--blue);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      min-height: 44px;
      font-family: inherit;
    }}

    .manual-add-btn:hover {{
      background: var(--blue-soft);
      border-color: var(--blue);
      color: var(--blue-dark);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .add-btn-icon {{
      font-size: 18px;
      font-weight: 900;
      line-height: 1;
    }}

    .add-btn-label {{
      font-size: 13px;
      font-weight: 800;
    }}

    .nav-btn-del {{
      position: absolute;
      top: 5px;
      right: 6px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      border: none;
      background: rgba(15, 23, 42, 0.12);
      color: var(--ink-secondary);
      font-size: 13px;
      line-height: 1;
      display: grid;
      place-items: center;
      cursor: pointer;
      opacity: 0;
      transition: all 0.15s ease;
    }}

    .manual-nav-btn:hover .nav-btn-del {{
      opacity: 1;
    }}

    .manual-nav-btn.active .nav-btn-del {{
      background: rgba(255, 255, 255, 0.22);
      color: #fff;
    }}

    .nav-btn-del:hover {{
      background: var(--red) !important;
      color: #fff !important;
    }}

    .add-modal-card {{
      width: min(94vw, 560px);
      padding: 24px;
    }}

    .cat-modal-card {{
      width: min(95vw, 720px);
      max-height: 90vh;
      padding: 24px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .cat-modal-body {{
      overflow-y: auto;
      padding-right: 4px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .cat-section-box {{
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px;
      background: #f8fafc;
    }}

    .cat-section-title {{
      font-size: 15px;
      font-weight: 850;
      color: var(--ink-dark);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}

    .cat-add-row {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
    }}

    .cat-add-row input {{
      flex: 1;
      padding: 9px 12px;
      border: 1.5px solid var(--line);
      border-radius: var(--radius-sm);
      font-size: 14px;
      font-family: inherit;
    }}

    .cat-edit-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .cat-edit-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #ffffff;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
    }}

    .cat-edit-item input {{
      flex: 1;
      padding: 7px 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      font-size: 13.5px;
      font-weight: 700;
      font-family: inherit;
      color: var(--ink);
    }}

    .cat-edit-item input:focus {{
      border-color: var(--blue);
      outline: none;
    }}

    .cat-item-badge {{
      font-size: 12px;
      font-weight: 750;
      color: var(--muted);
      background: #f1f5f9;
      padding: 4px 8px;
      border-radius: 999px;
      white-space: nowrap;
    }}

    .cat-icon-btn {{
      width: 30px;
      height: 30px;
      border-radius: 6px;
      border: 1px solid var(--line);
      background: #f8fafc;
      color: var(--ink-secondary);
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      display: inline-grid;
      place-items: center;
    }}

    .cat-icon-btn:hover:not(:disabled) {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
    }}

    .cat-icon-btn:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}

    .cat-del-btn {{
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid #fecaca;
      background: var(--red-soft);
      color: var(--red);
      font-size: 12px;
      font-weight: 750;
      cursor: pointer;
      white-space: nowrap;
    }}

    .cat-del-btn:hover {{
      background: var(--red);
      color: #ffffff;
    }}

    .manual-cat-assign-list {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 7px;
      max-height: 290px;
      overflow-y: auto;
      padding-right: 4px;
    }}

    .manual-cat-assign-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      background: #ffffff;
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      padding: 8px 12px;
    }}

    .manual-cat-assign-title {{
      font-size: 13.5px;
      font-weight: 750;
      color: var(--ink);
      flex: 1;
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .manual-cat-assign-select {{
      padding: 6px 10px;
      border-radius: 6px;
      border: 1.5px solid var(--line);
      font-size: 13px;
      font-weight: 700;
      font-family: inherit;
      color: var(--ink-secondary);
      background: #f8fafc;
      cursor: pointer;
      min-width: 210px;
    }}

    .manual-cat-assign-select:focus {{
      border-color: var(--blue);
      outline: none;
    }}

    .add-modal-title {{
      margin: 0;
      font-size: 20px;
      font-weight: 850;
      color: var(--ink-dark);
    }}

    .form-group {{
      margin-bottom: 15px;
    }}

    .form-group label {{
      display: block;
      font-size: 13.5px;
      font-weight: 750;
      color: var(--ink-secondary);
      margin-bottom: 6px;
    }}

    .form-group input[type="text"],
    .form-group input[type="number"],
    .form-group input[type="url"],
    .form-group select {{
      width: 100%;
      padding: 10px 12px;
      border: 1.5px solid var(--line);
      border-radius: var(--radius-sm);
      font-size: 14px;
      font-family: inherit;
      color: var(--ink);
      background: #fff;
      outline: none;
      transition: border-color 0.15s;
    }}

    .form-group input:focus,
    .form-group select:focus {{
      border-color: var(--blue);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12);
    }}

    .file-drop-area {{
      border: 2px dashed #93c5fd;
      border-radius: var(--radius-md);
      background: var(--blue-soft);
      padding: 18px 16px;
      text-align: center;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .file-drop-area:hover {{
      border-color: var(--blue);
      background: #dbeafe;
    }}

    .file-drop-area input[type="file"] {{
      display: none;
    }}

    .file-drop-text {{
      font-size: 14px;
      font-weight: 750;
      color: var(--blue-dark);
    }}

    .file-drop-sub {{
      font-size: 12px;
      color: var(--muted);
      margin-top: 4px;
    }}

    .form-row-2 {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 12px;
    }}

    .add-modal-actions {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-top: 20px;
      padding-top: 16px;
      border-top: 1px solid var(--line);
      flex-wrap: wrap;
    }}

    .btn-primary {{
      padding: 10px 20px;
      border-radius: var(--radius-sm);
      border: none;
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
      color: #fff;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      font-family: inherit;
      box-shadow: 0 3px 10px rgba(37, 99, 235, 0.25);
    }}

    .btn-primary:hover {{
      background: #1d4ed8;
    }}

    .btn-secondary {{
      padding: 9px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--line);
      background: #f8fafc;
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      font-family: inherit;
    }}

    .btn-secondary:hover {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
    }}

    /* =========================================================
       4. Manual Content Area
       ========================================================= */
    .content-area {{
      max-width: 1160px;
      margin: 28px auto 60px;
      padding: 0 20px;
      width: 100%;
    }}

    .manual-pane {{
      display: none;
    }}

    .manual-pane.active {{
      display: block;
      animation: fadeIn 0.2s ease forwards;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* =========================================================
       5. Title Row Actions (Canva Button + 독립창 열기 Button)
       ========================================================= */
    .title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .title-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .source-button {{
      display: inline-flex !important;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 15px;
      border-radius: 8px;
      border: none;
      background: #2563eb;
      color: #ffffff !important;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 750;
      white-space: nowrap;
      box-shadow: 0 3px 8px rgba(37,99,235,0.22);
      transition: all 0.18s ease;
      cursor: pointer;
      font-family: inherit;
    }}

    .source-button:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(37,99,235,0.32);
      color: #ffffff !important;
    }}

    .pane-standalone-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8.5px 14px;
      border-radius: 8px;
      background: #ffffff;
      border: 1.5px solid var(--line);
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 650;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}

    .pane-standalone-link:hover {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
    }}

    /* =========================================================
       6. Manual Page Content & Step Cards
       ========================================================= */
    .page {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 32px 36px;
      background: #fff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--line);
      box-shadow: var(--shadow-md);
    }}

    header {{
      border-bottom: 2px solid var(--ink);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}

    .title-row h1 {{
      font-size: clamp(24px, 3.5vw, 36px);
      line-height: 1.2;
      margin: 0;
      font-weight: 850;
      letter-spacing: -0.035em;
    }}

    .title-highlight {{
      background: linear-gradient(transparent 48%, #fff36a 48%, #fff36a 91%, transparent 91%);
      padding: 0 0.1em;
    }}

    .lead {{
      margin: 10px 0 0;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.5;
    }}

    .notice {{
      display: flex;
      gap: 16px;
      align-items: flex-start;
      background: var(--red-soft);
      border: 1px solid #fecaca;
      border-left: 7px solid var(--red);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      margin: 18px 0 22px;
    }}

    .notice-label {{
      font-size: 19px;
      line-height: 1.2;
      font-weight: 950;
      color: var(--red);
      white-space: nowrap;
    }}

    .notice p {{
      margin: 0;
      font-size: 15px;
      font-weight: 650;
      line-height: 1.55;
    }}

    .notice strong {{
      font-weight: 950;
      color: #b91c1c;
    }}

    .notice h2 {{
      margin: 0 0 5px;
      color: #b91c1c;
      font-size: 17px;
    }}

    .notice ul {{
      margin: 0;
      padding-left: 20px;
    }}

    .notice li {{
      margin: 4px 0;
      font-size: 14px;
      font-weight: 650;
    }}

    .flow {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 0 0 20px;
    }}

    .flow span {{
      padding: 7px 12px;
      border-radius: var(--radius-full);
      background: var(--blue-soft);
      color: #1e40af;
      font-size: 12.5px;
      font-weight: 750;
    }}

    .steps {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
      margin: 0 0 22px;
    }}

    .step {{
      position: relative;
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      background: #fff;
    }}

    .step-head, .step-top, .problem-head {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
      padding-right: 48px;
    }}

    .num {{
      display: inline-grid;
      place-items: center;
      flex: 0 0 auto;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--blue);
      color: #fff;
      font-weight: 850;
      font-size: 14px;
    }}

    .step h2, .step h3, .panel h2 {{
      font-size: 17.5px;
      line-height: 1.3;
      margin: 0;
      font-weight: 800;
    }}

    .section {{
      margin: 24px 0;
    }}

    .section-title {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      border-top: 3px solid var(--blue);
      padding-top: 14px;
      margin-bottom: 12px;
    }}

    .section-title.teacher {{
      border-color: var(--purple);
    }}

    .section-no {{
      display: grid;
      place-items: center;
      min-width: 34px;
      height: 34px;
      padding: 0 8px;
      flex: 0 0 auto;
      border-radius: 10px;
      background: var(--blue);
      color: #fff;
      font-weight: 900;
    }}

    .teacher .section-no, .teacher .num {{
      background: var(--purple);
    }}

    .section-title h2 {{
      margin: 0;
      font-size: 22px;
      line-height: 1.2;
    }}

    .section-title p {{
      margin: 4px 0 0;
      color: var(--muted);
      font-size: 13px;
    }}

    .two-col-sections {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
      align-items: start;
    }}

    .two-col-sections .section {{
      margin: 0;
    }}

    .step-with-side {{
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.95fr);
      gap: 18px;
      align-items: stretch;
    }}

    .step-side-box {{
      position: relative;
      border: 2px solid #f59e0b;
      border-radius: 9px;
      background: #fffbeb;
      color: #92400e;
      padding: 14px 52px 14px 16px;
      cursor: pointer;
      transition: all 0.16s ease;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .step-side-box:hover {{
      border-color: #d97706;
      background: #fef3c7;
    }}

    .step-side-box h4 {{
      margin: 0 0 8px;
      font-size: 14.5px;
      color: #92400e;
      font-weight: 800;
    }}

    .step-side-box ul {{
      margin: 0;
      padding-left: 18px;
    }}

    .step-side-box li {{
      margin: 4px 0;
      font-size: 13px;
      line-height: 1.45;
      color: #92400e;
      font-weight: 650;
    }}

    .side-important {{
      margin-top: 0;
      display: flex;
      align-items: center;
    }}

    .group-link-panel {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
      margin: 14px 0 24px;
      padding: 16px 20px;
      border: 1.5px solid #93c5fd;
      border-radius: 12px;
      background: linear-gradient(135deg, #eff6ff 0%, #f5f3ff 100%);
      color: var(--ink);
      text-decoration: none;
      transition: all 0.18s ease;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.08);
    }}

    .group-link-panel:hover {{
      border-color: var(--blue);
      box-shadow: 0 6px 16px rgba(37, 99, 235, 0.16);
      transform: translateY(-1px);
    }}

    .group-link-info {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .group-link-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 10px;
      border-radius: 8px;
      background: var(--blue);
      color: #fff;
      font-size: 12px;
      font-weight: 800;
      white-space: nowrap;
    }}

    .group-link-text strong {{
      display: block;
      font-size: 15px;
      color: #1e3a8a;
    }}

    .group-link-text span {{
      display: block;
      font-size: 13px;
      color: var(--muted);
      margin-top: 2px;
    }}

    .group-link-action {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 9px 16px;
      border-radius: 999px;
      background: var(--blue);
      color: #fff;
      font-size: 13.5px;
      font-weight: 800;
      white-space: nowrap;
    }}

    .pdf-action-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      flex-wrap: wrap;
      padding: 16px 20px;
      margin: 0 0 20px;
      border-radius: 12px;
      border: 1.5px solid #93c5fd;
      background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%);
    }}

    .pdf-action-info {{
      flex: 1;
      min-width: 240px;
    }}

    .pdf-action-info strong {{
      display: block;
      font-size: 15.5px;
      color: #1e3a8a;
      font-weight: 850;
    }}

    .pdf-action-info span {{
      display: block;
      font-size: 13px;
      color: var(--muted);
      margin-top: 2px;
    }}

    .pdf-action-buttons {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .pdf-btn-primary {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 10px 16px;
      border-radius: 8px;
      border: none;
      background: #2563eb;
      color: #fff !important;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      text-decoration: none !important;
      box-shadow: 0 3px 8px rgba(37, 99, 235, 0.22);
      transition: all 0.16s ease;
      font-family: inherit;
    }}

    .pdf-btn-primary:hover {{
      background: #1d4ed8;
      transform: translateY(-1px);
    }}

    .pdf-btn-secondary {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 9px 14px;
      border-radius: 8px;
      border: 1.5px solid #93c5fd;
      background: #fff;
      color: #1d4ed8 !important;
      font-size: 13px;
      font-weight: 750;
      cursor: pointer;
      text-decoration: none !important;
      transition: all 0.16s ease;
      font-family: inherit;
    }}

    .pdf-btn-secondary:hover {{
      background: #eff6ff;
    }}

    .pdf-btn-video {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 10px 15px;
      border-radius: 8px;
      border: none;
      background: #dc2626;
      color: #fff !important;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      text-decoration: none !important;
      box-shadow: 0 3px 8px rgba(220, 38, 38, 0.22);
      transition: all 0.16s ease;
      font-family: inherit;
    }}

    .pdf-btn-video:hover {{
      background: #b91c1c;
      transform: translateY(-1px);
    }}

    .video-embed-wrap {{
      margin: 14px 0 22px;
      border: 1.5px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      background: #0f172a;
      aspect-ratio: 16 / 9;
    }}

    .video-embed-frame {{
      display: block;
      width: 100%;
      height: 100%;
      border: none;
    }}

    .important {{
      margin-top: 10px;
      padding: 11px 13px;
      border: 2px solid #f59e0b;
      border-radius: 9px;
      background: #fffbeb;
      color: #92400e;
      font-size: 13px;
      font-weight: 750;
    }}

    .step a {{
      color: var(--blue);
      font-weight: 700;
      text-decoration: underline;
    }}

    .inline-figure {{
      margin: 14px 0 4px;
      border: 1px solid var(--line);
      border-radius: 10px;
      overflow: hidden;
      background: #fff;
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
    }}

    .inline-figure img {{
      display: block;
      width: 100%;
      height: auto;
      cursor: zoom-in;
    }}

    .pdf-embed-wrap {{
      margin: 14px 0 20px;
      border: 1.5px solid var(--line);
      border-radius: 12px;
      overflow: hidden;
      background: #334155;
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.08);
    }}

    .pdf-embed-frame {{
      display: block;
      width: 100%;
      height: 82vh;
      min-height: 740px;
      border: none;
      background: #fff;
    }}

    .step p {{
      margin: 0;
      color: var(--muted);
      font-size: 13.5px;
      line-height: 1.5;
    }}

    .step ul {{
      margin: 0;
      padding-left: 20px;
    }}

    .step li {{
      margin: 5px 0;
      font-size: 13.5px;
      color: var(--ink-secondary);
    }}

    .path {{
      margin-top: 10px;
      padding: 8px 12px;
      background: var(--blue-soft);
      border-radius: var(--radius-sm);
      color: #1e40af;
      font-size: 12.5px;
      font-weight: 700;
      display: inline-block;
    }}

    .step .hint {{
      margin-top: 10px;
      padding: 9px 12px;
      border-radius: var(--radius-sm);
      background: #f8fafc;
      color: var(--muted);
      font-size: 12.5px;
    }}

    /* =========================================================
       Step Image View Button (🔍)
       ========================================================= */
    .img-toggle {{
      position: absolute;
      top: 14px;
      right: 14px;
      width: 38px;
      height: 38px;
      display: grid !important;
      place-items: center;
      border: 1.5px solid #93c5fd;
      border-radius: 50%;
      padding: 0;
      background: #ffffff;
      color: var(--blue);
      font-size: 18px;
      line-height: 1;
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 2;
      box-shadow: 0 2px 5px rgba(37,99,235,0.12);
    }}

    .img-toggle:hover {{
      background: var(--blue-soft);
      transform: scale(1.12);
      border-color: var(--blue);
      box-shadow: 0 4px 10px rgba(37,99,235,0.25);
    }}

    .img-toggle:active {{
      transform: scale(0.96);
    }}

    .lower {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
      margin-top: 4px;
    }}

    .panel {{
      position: relative;
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px 18px;
      background: #fff;
    }}

    .panel ul {{
      margin: 0;
      padding-left: 20px;
    }}

    .panel li {{
      margin: 6px 0;
      font-size: 13.5px;
      color: var(--ink-secondary);
    }}

    .problem-num {{
      background: #64748b;
    }}

    .ok {{
      background: var(--green-soft);
      border-color: #a7f3d0;
    }}

    .ok h2 {{
      color: var(--green);
    }}

    .finish {{
      margin-top: 18px;
      border: 1px solid #a7f3d0;
      border-radius: var(--radius-md);
      padding: 16px 18px;
      background: var(--green-soft);
    }}

    .finish h2 {{
      margin: 0 0 8px;
      color: var(--green);
      font-size: 18px;
    }}

    .finish ul {{
      margin: 0;
      padding-left: 20px;
    }}

    .finish li {{
      margin: 5px 0;
      font-size: 13.5px;
    }}

    code {{
      padding: 2px 6px;
      border-radius: 5px;
      background: #eef2ff;
      color: #1e3a8a;
      font-size: 12.5px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }}

    .foot {{
      margin-top: 14px;
      color: var(--muted);
      font-size: 12.5px;
      text-align: right;
    }}

    /* =========================================================
       7. Image Zoom Modal
       ========================================================= */
    body.modal-open {{
      overflow: hidden;
    }}

    .modal[hidden] {{
      display: none;
    }}

    .modal {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      display: grid;
      place-items: center;
      padding: 20px;
      background: rgba(15, 23, 42, 0.78);
      backdrop-filter: blur(4px);
    }}

    .modal-card {{
      position: relative;
      width: min(96vw, 1320px);
      max-height: 92vh;
      padding: 18px;
      border-radius: var(--radius-lg);
      background: #ffffff;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.35);
      overflow: auto;
    }}

    .modal-header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--line);
    }}

    .modal-close {{
      width: 40px;
      height: 40px;
      border: 1px solid var(--line);
      border-radius: 50%;
      background: #ffffff;
      color: var(--ink);
      font-size: 22px;
      font-weight: 800;
      line-height: 1;
      cursor: pointer;
      display: grid;
      place-items: center;
      box-shadow: var(--shadow-sm);
      transition: all 0.15s ease;
    }}

    .modal-close:hover {{
      background: var(--red-soft);
      color: var(--red);
      border-color: #fecaca;
    }}

    .modal-gallery {{
      display: grid;
      gap: 16px;
    }}

    .modal img {{
      display: block;
      width: 100%;
      max-height: calc(92vh - 95px);
      object-fit: contain;
      border-radius: 10px;
      background: #f8fafc;
      border: 1px solid var(--line);
    }}

    /* =========================================================
       8. Simple Footer
       ========================================================= */
    .simple-footer {{
      margin-top: auto;
      background: #ffffff;
      border-top: 1px solid var(--line);
      padding: 20px 24px;
      text-align: center;
      color: var(--muted);
      font-size: 13px;
    }}

    /* =========================================================
       9. Responsive & Print
       ========================================================= */
    @media (max-width: 1120px) {{
      .manual-nav-grid {{
        grid-template-columns: repeat(4, 1fr);
      }}
    }}

    @media (max-width: 820px) {{
      .manual-nav-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .two-col-sections, .step-with-side {{
        grid-template-columns: 1fr;
      }}
      .page {{
        padding: 20px 18px;
      }}
      .notice {{
        flex-direction: column;
        gap: 6px;
      }}
      .manual-cat-assign-row {{
        flex-direction: column;
        align-items: stretch;
      }}
    }}

    @media (max-width: 480px) {{
      .header-inner {{
        padding: 12px 16px;
      }}
      .nav-bar-section {{
        padding: 10px 12px;
      }}
      .manual-nav-btn {{
        padding: 8px 8px;
        min-height: 38px;
      }}
      .nav-btn-title {{
        font-size: 12.5px;
      }}
    }}

    @media print {{
      body {{
        background: #fff;
      }}
      .simple-header, .nav-bar-section, .simple-footer, .img-toggle, .modal, .source-button, .pane-standalone-link, .pdf-action-bar {{
        display: none !important;
      }}
      .content-area {{
        max-width: none !important;
        margin: 0 !important;
        padding: 0 !important;
      }}
      .page {{
        max-width: none !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
      }}
      .step, .notice, .panel, .finish {{
        break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>

  <!-- =========================================================
       Simple Header
       ========================================================= -->
  <header class="simple-header">
    <div class="header-inner">
      <div class="header-title-group">
        <div class="header-logo-icon">🏫</div>
        <h1 class="header-title">온라인 교무실 매뉴얼</h1>
      </div>
      <div class="header-actions">
        <button type="button" id="btnHeaderDeployDownload" class="btn-header-deploy" onclick="downloadAllDeploymentFiles()" hidden title="통합 index.html과 추가된 개별 HTML 파일을 일괄 다운로드합니다">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          배포 파일 일괄 다운로드
        </button>
        <button type="button" class="btn-header-print" onclick="window.print()">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          인쇄하기
        </button>
      </div>
    </div>
  </header>

  <!-- =========================================================
       Category Filter Bar & Manual Button Navigation Bar
       ========================================================= -->
  <nav class="nav-bar-section" aria-label="매뉴얼 선택 바">
    <div class="nav-bar-container">
      <div class="category-bar-wrap">
        <div class="category-tabs" id="categoryTabs" role="tablist" aria-label="카테고리별 매뉴얼 선택">
          {''.join(category_tabs_html)}
        </div>
        <div class="category-bar-actions">
          <button type="button" class="btn-category-edit" onclick="openCategoryEditModal()" title="카테고리 추가·수정·순서 변경 및 매뉴얼별 카테고리 설정">
            ⚙️ 카테고리 편집
          </button>
        </div>
      </div>

      <div class="manual-nav-grid" id="manualNavGrid">
        {''.join(buttons_html)}
        <button type="button" class="manual-add-btn" id="openAddManualBtn" onclick="openAddManualModal()" title="새 매뉴얼 추가">
          <span class="add-btn-icon">+</span>
          <span class="add-btn-label">매뉴얼 추가</span>
        </button>
      </div>
    </div>
  </nav>

  <!-- =========================================================
       Manual Content Area
       ========================================================= -->
  <div class="content-area" id="manualContentArea">
    {''.join(panes_html)}
  </div>

  <!-- =========================================================
       High-Res Image Modal (With Canva/Source Open Button)
       ========================================================= -->
  <div class="modal" id="globalImageModal" role="dialog" aria-modal="true" aria-label="원본 이미지 확대 뷰어" hidden>
    <div class="modal-card">
      <div class="modal-header-bar">
        <a id="modalCanvaBtn" class="source-button" href="#" target="_blank" rel="noopener">
          원본 문서 열기
        </a>
        <button class="modal-close" type="button" aria-label="닫기">×</button>
      </div>
      <div class="modal-gallery" id="globalModalGallery"></div>
    </div>
  </div>

  <!-- =========================================================
       Category Edit Modal (⚙️ 카테고리 편집)
       ========================================================= -->
  <div class="modal" id="categoryEditModal" role="dialog" aria-modal="true" aria-label="카테고리 편집" hidden>
    <div class="modal-card cat-modal-card">
      <div class="modal-header-bar">
        <h2 class="add-modal-title">⚙️ 카테고리 편집 및 매뉴얼 분류 관리</h2>
        <button class="modal-close" type="button" aria-label="닫기" onclick="closeCategoryEditModal()">×</button>
      </div>
      <div class="cat-modal-body">
        <div class="cat-section-box">
          <div class="cat-section-title">
            <span>1. 카테고리 목록 관리 (추가 · 이름 변경 · 순서 이동 · 삭제)</span>
            <button type="button" class="btn-secondary" style="padding:5px 10px;font-size:12px;" onclick="resetCategoriesToDefault()">기본값 초기화</button>
          </div>
          <div class="cat-add-row">
            <input type="text" id="newCategoryNameInput" placeholder="새 카테고리 이름 입력 (예: 📝 평가 · 생기부)" onkeydown="if(event.key==='Enter'){{event.preventDefault();handleAddCategory();}}">
            <button type="button" class="btn-primary" style="padding:9px 15px;white-space:nowrap;" onclick="handleAddCategory()">+ 카테고리 추가</button>
          </div>
          <div class="cat-edit-list" id="categoryEditList"></div>
        </div>

        <div class="cat-section-box">
          <div class="cat-section-title">
            <span>2. 매뉴얼별 소속 카테고리 지정</span>
            <span style="font-size:12px;font-weight:600;color:var(--muted);">메인 화면에서 매뉴얼 버튼을 상단 카테고리 탭으로 드래그해도 이동됩니다</span>
          </div>
          <div class="manual-cat-assign-list" id="manualCatAssignList"></div>
        </div>
      </div>
      <div class="add-modal-actions" style="justify-content:flex-end;margin-top:14px;">
        <button type="button" class="btn-primary" onclick="closeCategoryEditModal()">완료 및 닫기</button>
      </div>
    </div>
  </div>

  <!-- =========================================================
       Add Manual Modal (+ Button)
       ========================================================= -->
  <div class="modal" id="addManualModal" role="dialog" aria-modal="true" aria-label="새 매뉴얼 추가" hidden>
    <div class="modal-card add-modal-card">
      <div class="modal-header-bar">
        <h2 class="add-modal-title">새 매뉴얼 추가 (HTML · PDF · 이미지)</h2>
        <button class="modal-close" type="button" aria-label="닫기" onclick="closeAddManualModal()">×</button>
      </div>
      <form id="addManualForm" onsubmit="handleAddManualSubmit(event)">
        <div class="form-group">
          <label>1. 매뉴얼 파일 업로드 (HTML, PDF, 이미지) *</label>
          <label class="file-drop-area" id="fileDropArea" for="manualFileInput">
            <input type="file" id="manualFileInput" accept=".html,.htm,.pdf,image/*" multiple onchange="handleManualFileSelect(event)">
            <div class="file-drop-text" id="fileDropText">📂 클릭하여 HTML · PDF · 이미지 파일 선택 (또는 드래그)</div>
            <div class="file-drop-sub">PDF와 이미지는 화면에 바로 표시되는 매뉴얼 페이지로 자동 변환됩니다.</div>
          </label>
        </div>
        <div class="form-row-2">
          <div class="form-group">
            <label for="manualShortTitle">2. 매뉴얼 버튼 제목 *</label>
            <input type="text" id="manualShortTitle" placeholder="예: 학사일정 안내 / 구글 설문지" required>
          </div>
          <div class="form-group">
            <label for="manualStepsCount">3. 단계 수 *</label>
            <input type="number" id="manualStepsCount" min="1" max="99" value="1" required>
          </div>
        </div>
        <div class="form-group">
          <label for="manualCategorySelect">4. 소속 카테고리 *</label>
          <select id="manualCategorySelect"></select>
        </div>
        <div class="form-group">
          <label for="manualCanvaUrl">5. 원본 슬라이드/문서 링크 (선택)</label>
          <input type="url" id="manualCanvaUrl" placeholder="https://www.canva.com/design/...">
        </div>
        <div class="add-modal-actions" style="justify-content:flex-end;">
          <button type="button" class="btn-secondary" onclick="closeAddManualModal()">취소</button>
          <button type="submit" class="btn-primary">매뉴얼 추가하기</button>
        </div>
      </form>
    </div>
  </div>

  <!-- =========================================================
       Simple Footer
       ========================================================= -->
  <footer class="simple-footer">
    <div><strong>홍익여자고등학교 온라인교무실</strong> · 교원 업무 지원 가이드북</div>
  </footer>

  <!-- =========================================================
       Navigation, Category Management, Modal & Dynamic Upload Script
       ========================================================= -->
  <script id="mainPortalScript">
    const INITIAL_CATEGORIES = {json.dumps(DEFAULT_CATEGORIES, ensure_ascii=False)};
    let CATEGORIES_DATA = JSON.parse(JSON.stringify(INITIAL_CATEGORIES));
    const MANUAL_LIST = {json.dumps([{"id": m["id"], "title": m["short_title"], "canva": m["canva"], "category": m["category"]} for m in MANUALS], ensure_ascii=False)};
    const INITIAL_MANUAL_CATEGORIES = Object.fromEntries(MANUAL_LIST.map(m => [m.id, m.category]));
    
    const modal = document.getElementById('globalImageModal');
    const modalGallery = document.getElementById('globalModalGallery');
    const modalCloseBtn = modal.querySelector('.modal-close');
    const modalCanvaBtn = document.getElementById('modalCanvaBtn');
    const addModal = document.getElementById('addManualModal');
    const catEditModal = document.getElementById('categoryEditModal');
    const deployDownloadBtn = document.getElementById('btnHeaderDeployDownload');

    const CATEGORIES_STORAGE_KEY = 'online_office_manual_categories_v1';
    const MANUAL_CAT_MAP_STORAGE_KEY = 'online_office_manual_cat_map_v1';
    const ORDER_STORAGE_KEY = 'online_office_manual_nav_order';

    let currentManualId = MANUAL_LIST[0].id;
    let currentCategoryId = 'all';
    const BUILTIN_IDS = new Set(MANUAL_LIST.map(m => m.id));
    let uploadedRawHtml = '';
    let uploadedFileName = '';
    let uploadedFileType = ''; // 'html' | 'pdf' | 'image'
    let uploadedDataUrls = [];
    const customManualsStore = [];
    let hasOrderChanged = false;
    let hasCategoryChanged = false;

    function updateDeployButtonVisibility() {{
      if (!deployDownloadBtn) return;
      deployDownloadBtn.hidden = (customManualsStore.length === 0 && !hasOrderChanged && !hasCategoryChanged);
    }}

    function getCategoryName(catId) {{
      const found = CATEGORIES_DATA.find(c => c.id === catId);
      return found ? found.name : (CATEGORIES_DATA[0]?.name || '기타');
    }}

    function getCategoryThemeIndex(catId) {{
      const idx = CATEGORIES_DATA.findIndex(c => c.id === catId);
      if (idx >= 0) {{
        const cat = CATEGORIES_DATA[idx];
        return (typeof cat.theme === 'number') ? (cat.theme % 8) : (idx % 8);
      }}
      return 0;
    }}

    function saveCategoryStateToStorage(markChanged = true) {{
      if (markChanged) {{
        hasCategoryChanged = true;
        updateDeployButtonVisibility();
      }}
      try {{
        localStorage.setItem(CATEGORIES_STORAGE_KEY, JSON.stringify(CATEGORIES_DATA));
        const catMap = {{}};
        MANUAL_LIST.forEach(m => {{ catMap[m.id] = m.category; }});
        localStorage.setItem(MANUAL_CAT_MAP_STORAGE_KEY, JSON.stringify(catMap));
      }} catch (e) {{}}
    }}

    function loadCategoryStateFromStorage() {{
      try {{
        const rawCats = localStorage.getItem(CATEGORIES_STORAGE_KEY);
        if (rawCats) {{
          const parsed = JSON.parse(rawCats);
          if (Array.isArray(parsed) && parsed.length > 0) {{
            CATEGORIES_DATA = parsed;
          }}
        }}
        const rawMap = localStorage.getItem(MANUAL_CAT_MAP_STORAGE_KEY);
        if (rawMap) {{
          const mapObj = JSON.parse(rawMap);
          if (mapObj && typeof mapObj === 'object') {{
            MANUAL_LIST.forEach(m => {{
              if (mapObj[m.id] && CATEGORIES_DATA.some(c => c.id === mapObj[m.id])) {{
                m.category = mapObj[m.id];
              }}
            }});
          }}
        }}
        // Ensure every manual has a valid category
        const fallbackCat = CATEGORIES_DATA[0]?.id || 'office-basic';
        MANUAL_LIST.forEach(m => {{
          if (!m.category || !CATEGORIES_DATA.some(c => c.id === m.category)) {{
            m.category = fallbackCat;
          }}
        }});
      }} catch (e) {{}}
    }}

    function renderCategoryBar() {{
      const tabsContainer = document.getElementById('categoryTabs');
      if (!tabsContainer) return;

      const counts = {{}};
      CATEGORIES_DATA.forEach(c => {{ counts[c.id] = 0; }});
      MANUAL_LIST.forEach(m => {{
        const cid = CATEGORIES_DATA.some(c => c.id === m.category) ? m.category : (CATEGORIES_DATA[0]?.id || '');
        m.category = cid;
        counts[cid] = (counts[cid] || 0) + 1;
      }});

      let html = '';

      CATEGORIES_DATA.forEach(c => {{
        const isActive = currentCategoryId === c.id ? 'active' : '';
        const cnt = counts[c.id] || 0;
        const themeIdx = getCategoryThemeIndex(c.id);
        html += `
          <button type="button" class="category-tab ${{isActive}}" data-cat-id="${{c.id}}" data-cat-theme="${{themeIdx}}" onclick="selectCategory('${{c.id}}')">
            <span class="cat-tab-name">${{c.name}}</span>
            <span class="cat-tab-count">${{cnt}}</span>
          </button>
        `;
      }});

      html += `
        <button type="button" class="category-tab ${{currentCategoryId === 'all' ? 'active' : ''}}" data-cat-id="all" onclick="selectCategory('all')">
          <span class="cat-tab-name">📋 전체 보기</span>
          <span class="cat-tab-count">${{MANUAL_LIST.length}}</span>
        </button>
      `;

      tabsContainer.innerHTML = html;
      bindCategoryTabDropTargets();
      syncManualButtonCategoriesAndFilter();
      populateAddManualCategorySelect();
    }}

    function syncManualButtonCategoriesAndFilter() {{
      const navGrid = document.getElementById('manualNavGrid');
      if (!navGrid) return;
      navGrid.querySelectorAll('.manual-nav-btn').forEach(btn => {{
        const item = MANUAL_LIST.find(m => m.id === btn.dataset.id);
        const catId = item ? item.category : (btn.dataset.category || CATEGORIES_DATA[0]?.id);
        btn.dataset.category = catId;
        btn.dataset.catTheme = String(getCategoryThemeIndex(catId));
        btn.title = getCategoryName(catId);
        btn.hidden = (currentCategoryId !== 'all' && catId !== currentCategoryId);
      }});
    }}

    function selectCategory(catId, autoSelectFirstManual = true) {{
      if (catId !== 'all' && !CATEGORIES_DATA.some(c => c.id === catId)) {{
        catId = 'all';
      }}
      currentCategoryId = catId;
      renderCategoryBar();

      if (autoSelectFirstManual && catId !== 'all') {{
        const currentItem = MANUAL_LIST.find(m => m.id === currentManualId);
        if (!currentItem || currentItem.category !== catId) {{
          const firstInCat = MANUAL_LIST.find(m => m.category === catId);
          if (firstInCat) {{
            selectManual(firstInCat.id);
          }}
        }}
      }}
    }}

    function populateAddManualCategorySelect() {{
      const sel = document.getElementById('manualCategorySelect');
      if (!sel) return;
      const preferred = (currentCategoryId !== 'all') ? currentCategoryId : (CATEGORIES_DATA[0]?.id || '');
      sel.innerHTML = CATEGORIES_DATA.map(c =>
        `<option value="${{c.id}}" ${{c.id === preferred ? 'selected' : ''}}>${{c.name}}</option>`
      ).join('');
    }}

    // Category Edit Modal Logic
    function openCategoryEditModal() {{
      renderCategoryEditModalContents();
      catEditModal.hidden = false;
      document.body.classList.add('modal-open');
    }}

    function closeCategoryEditModal() {{
      catEditModal.hidden = true;
      document.body.classList.remove('modal-open');
    }}

    catEditModal.addEventListener('click', (e) => {{
      if (e.target === catEditModal) closeCategoryEditModal();
    }});

    function renderCategoryEditModalContents() {{
      const listEl = document.getElementById('categoryEditList');
      const assignEl = document.getElementById('manualCatAssignList');
      if (!listEl || !assignEl) return;

      const counts = {{}};
      CATEGORIES_DATA.forEach(c => {{ counts[c.id] = 0; }});
      MANUAL_LIST.forEach(m => {{ counts[m.category] = (counts[m.category] || 0) + 1; }});

      listEl.innerHTML = CATEGORIES_DATA.map((c, idx) => `
        <div class="cat-edit-item" data-cat-id="${{c.id}}">
          <button type="button" class="cat-icon-btn" title="위로 이동" ${{idx === 0 ? 'disabled' : ''}} onclick="moveCategoryOrder(${{idx}}, -1)">▲</button>
          <button type="button" class="cat-icon-btn" title="아래로 이동" ${{idx === CATEGORIES_DATA.length - 1 ? 'disabled' : ''}} onclick="moveCategoryOrder(${{idx}}, 1)">▼</button>
          <input type="text" value="${{c.name.replace(/"/g, '&quot;')}}" onchange="renameCategoryById('${{c.id}}', this.value)" aria-label="카테고리 이름">
          <span class="cat-item-badge">${{counts[c.id] || 0}}개 매뉴얼</span>
          <button type="button" class="cat-del-btn" onclick="deleteCategoryById('${{c.id}}')" ${{CATEGORIES_DATA.length <= 1 ? 'disabled' : ''}}>삭제</button>
        </div>
      `).join('');

      assignEl.innerHTML = MANUAL_LIST.map(m => `
        <div class="manual-cat-assign-row">
          <span class="manual-cat-assign-title" title="${{m.title.replace(/"/g, '&quot;')}}">${{m.title}}</span>
          <select class="manual-cat-assign-select" onchange="assignManualToCategory('${{m.id}}', this.value)" aria-label="${{m.title}} 카테고리 선택">
            ${{CATEGORIES_DATA.map(c => `<option value="${{c.id}}" ${{m.category === c.id ? 'selected' : ''}}>${{c.name}}</option>`).join('')}}
          </select>
        </div>
      `).join('');
    }}

    function handleAddCategory() {{
      const input = document.getElementById('newCategoryNameInput');
      const name = (input?.value || '').trim();
      if (!name) {{
        alert('추가할 카테고리 이름을 입력해 주세요.');
        input?.focus();
        return;
      }}
      const newId = 'cat-' + Date.now();
      const usedThemes = new Set(CATEGORIES_DATA.map((c, idx) => typeof c.theme === 'number' ? c.theme : (idx % 8)));
      let nextTheme = CATEGORIES_DATA.length % 8;
      for (let t = 0; t < 8; t++) {{
        if (!usedThemes.has(t)) {{ nextTheme = t; break; }}
      }}
      CATEGORIES_DATA.push({{ id: newId, name, theme: nextTheme }});
      if (input) input.value = '';
      saveCategoryStateToStorage(true);
      renderCategoryBar();
      renderCategoryEditModalContents();
    }}

    function renameCategoryById(catId, newName) {{
      const trimmed = (newName || '').trim();
      if (!trimmed) {{
        renderCategoryEditModalContents();
        return;
      }}
      const cat = CATEGORIES_DATA.find(c => c.id === catId);
      if (cat && cat.name !== trimmed) {{
        cat.name = trimmed;
        saveCategoryStateToStorage(true);
        renderCategoryBar();
        renderCategoryEditModalContents();
      }}
    }}

    function moveCategoryOrder(index, delta) {{
      const targetIdx = index + delta;
      if (targetIdx < 0 || targetIdx >= CATEGORIES_DATA.length) return;
      const temp = CATEGORIES_DATA[index];
      CATEGORIES_DATA[index] = CATEGORIES_DATA[targetIdx];
      CATEGORIES_DATA[targetIdx] = temp;
      saveCategoryStateToStorage(true);
      renderCategoryBar();
      renderCategoryEditModalContents();
    }}

    function deleteCategoryById(catId) {{
      if (CATEGORIES_DATA.length <= 1) {{
        alert('최소 1개의 카테고리는 유지되어야 합니다.');
        return;
      }}
      const targetCat = CATEGORIES_DATA.find(c => c.id === catId);
      const fallbackCat = CATEGORIES_DATA.find(c => c.id !== catId);
      if (!targetCat || !fallbackCat) return;
      const affectedCount = MANUAL_LIST.filter(m => m.category === catId).length;
      const msg = affectedCount > 0
        ? `'${{targetCat.name}}' 카테고리를 삭제하시겠습니까?\\n소속된 ${{affectedCount}}개 매뉴얼은 '${{fallbackCat.name}}' 카테고리로 자동 이동됩니다.`
        : `'${{targetCat.name}}' 카테고리를 삭제하시겠습니까?`;
      if (!confirm(msg)) return;

      MANUAL_LIST.forEach(m => {{
        if (m.category === catId) m.category = fallbackCat.id;
      }});
      CATEGORIES_DATA = CATEGORIES_DATA.filter(c => c.id !== catId);
      if (currentCategoryId === catId) currentCategoryId = 'all';
      saveCategoryStateToStorage(true);
      renderCategoryBar();
      renderCategoryEditModalContents();
    }}

    function assignManualToCategory(manualId, newCatId) {{
      const item = MANUAL_LIST.find(m => m.id === manualId);
      if (!item || !CATEGORIES_DATA.some(c => c.id === newCatId)) return;
      item.category = newCatId;
      const customItem = customManualsStore.find(m => m.id === manualId);
      if (customItem) {{
        customItem.category = newCatId;
        saveCustomManualToDB(customItem);
      }}
      saveCategoryStateToStorage(true);
      renderCategoryBar();
      renderCategoryEditModalContents();
    }}

    function resetCategoriesToDefault() {{
      if (!confirm('카테고리 목록과 매뉴얼 분류를 초기 기본값으로 되돌리시겠습니까?')) return;
      CATEGORIES_DATA = JSON.parse(JSON.stringify(INITIAL_CATEGORIES));
      MANUAL_LIST.forEach(m => {{
        m.category = INITIAL_MANUAL_CATEGORIES[m.id] || CATEGORIES_DATA[0].id;
      }});
      currentCategoryId = 'all';
      try {{
        localStorage.removeItem(CATEGORIES_STORAGE_KEY);
        localStorage.removeItem(MANUAL_CAT_MAP_STORAGE_KEY);
      }} catch (e) {{}}
      hasCategoryChanged = true;
      updateDeployButtonVisibility();
      renderCategoryBar();
      renderCategoryEditModalContents();
    }}

    // Collapsible PDF / Video Viewer & Open PDF in New Tab Helpers
    function toggleCollapsibleViewer(boxId, btnEl, openText, closeText) {{
      const box = document.getElementById(boxId);
      if (!box) return;
      const isHidden = box.style.display === 'none' || !box.style.display;
      if (isHidden) {{
        box.style.display = 'block';
        const frame = box.querySelector('iframe');
        if (frame) {{
          if (frame.dataset.lazySrc && !frame.getAttribute('src')) {{
            frame.setAttribute('src', frame.dataset.lazySrc);
          }} else if (frame.dataset.pdfSrc) {{
            hydratePdfFrames(box);
          }}
        }}
        if (btnEl && closeText) btnEl.innerHTML = closeText;
        box.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
      }} else {{
        box.style.display = 'none';
        if (btnEl && openText) btnEl.innerHTML = openText;
      }}
    }}

    function openEmbeddedPdfInNewTab(viewerId) {{
      const box = document.getElementById(viewerId);
      if (!box) return;
      const frame = box.querySelector('iframe[data-pdf-src]');
      if (!frame || !frame.dataset.pdfSrc) return;
      try {{
        const b = atob(frame.dataset.pdfSrc.split(',')[1]);
        const u = new Uint8Array(b.length);
        for (let i = 0; i < b.length; i++) u[i] = b.charCodeAt(i);
        const url = URL.createObjectURL(new Blob([u], {{ type: 'application/pdf' }}));
        window.open(url, '_blank', 'noopener');
      }} catch (e) {{}}
    }}

    function hydratePdfFrames(root = document) {{
      root.querySelectorAll('iframe.pdf-embed-frame[data-pdf-src]').forEach(frame => {{
        if (frame.dataset.hydrated === '1') return;
        const box = frame.closest('.pdf-embed-wrap');
        if (box && box.style.display === 'none') return;
        const dataUrl = frame.getAttribute('data-pdf-src');
        if (!dataUrl || !dataUrl.startsWith('data:application/pdf;base64,')) return;
        try {{
          const b64 = dataUrl.split(',')[1];
          const bin = atob(b64);
          const len = bin.length;
          const bytes = new Uint8Array(len);
          for (let i = 0; i < len; i++) bytes[i] = bin.charCodeAt(i);
          const blob = new Blob([bytes], {{ type: 'application/pdf' }});
          const blobUrl = URL.createObjectURL(blob);
          frame.src = blobUrl;
          frame.dataset.hydrated = '1';
        }} catch (e) {{
          frame.src = dataUrl;
        }}
      }});
    }}

    function selectManual(id, updateHash = true) {{
      const exists = MANUAL_LIST.some(m => m.id === id);
      if (!exists) id = MANUAL_LIST[0].id;

      currentManualId = id;

      document.querySelectorAll('.manual-nav-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.dataset.id === id);
      }});

      document.querySelectorAll('.manual-pane').forEach(pane => {{
        const isActive = pane.dataset.id === id;
        pane.classList.toggle('active', isActive);
        if (isActive) hydratePdfFrames(pane);
      }});

      const item = MANUAL_LIST.find(m => m.id === id);
      if (item) {{
        document.title = item.title + " | 온라인 교무실 매뉴얼";
        if (modalCanvaBtn) {{
          modalCanvaBtn.href = item.canva || '#';
          modalCanvaBtn.style.visibility = item.canva ? 'visible' : 'hidden';
        }}
      }}

      if (updateHash) {{
        history.pushState(null, '', '#' + id);
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function handleHash() {{
      const hash = window.location.hash.replace(/^#/, '').trim();
      const valid = MANUAL_LIST.find(m => m.id === hash);
      if (valid) {{
        if (currentCategoryId !== 'all' && valid.category !== currentCategoryId) {{
          currentCategoryId = 'all';
          renderCategoryBar();
        }}
        selectManual(valid.id, false);
      }} else {{
        selectManual(MANUAL_LIST[0].id, false);
      }}
    }}

    window.addEventListener('hashchange', handleHash);

    // Image Modal Logic
    function closeModal() {{
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      modalGallery.innerHTML = '';
    }}

    modalCloseBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) closeModal();
    }});

    function openImageInModal(urls, altText, canvaUrl) {{
      if (!urls || !urls.length) return;
      if (modalCanvaBtn) {{
        modalCanvaBtn.href = canvaUrl || '#';
        modalCanvaBtn.style.visibility = canvaUrl ? 'visible' : 'hidden';
      }}
      modalGallery.innerHTML = urls.map((u, i) => `
        <img src="${{u}}" alt="${{altText || '원본 안내 이미지'}} ${{i + 1}}">
      `).join('');
      modal.hidden = false;
      document.body.classList.add('modal-open');
      modalCloseBtn.focus();
    }}

    function bindImageToggles(root = document) {{
      root.querySelectorAll('.img-toggle').forEach(btn => {{
        if (btn.dataset.bound === '1') return;
        btn.dataset.bound = '1';
        btn.addEventListener('click', (e) => {{
          e.stopPropagation();
          const pane = btn.closest('.manual-pane');
          const canvaUrl = (pane && pane.dataset.canva) ? pane.dataset.canva : (MANUAL_LIST.find(m => m.id === currentManualId)?.canva || '');
          let urls = [];
          if (btn.dataset.images) {{
            try {{
              urls = JSON.parse(decodeURIComponent(btn.dataset.images));
            }} catch(err) {{
              try {{ urls = JSON.parse(btn.dataset.images); }} catch(err2) {{}}
            }}
          }} else if (btn.dataset.image) {{
            urls = [btn.dataset.image];
          }}
          openImageInModal(urls, btn.dataset.alt || '원본 안내 이미지', canvaUrl);
        }});
      }});

      root.querySelectorAll('.inline-figure img').forEach(img => {{
        if (img.dataset.boundZoom === '1') return;
        img.dataset.boundZoom = '1';
        img.addEventListener('click', (e) => {{
          e.stopPropagation();
          const src = img.getAttribute('src');
          if (!src) return;
          const pane = img.closest('.manual-pane');
          const canvaUrl = (pane && pane.dataset.canva) ? pane.dataset.canva : (MANUAL_LIST.find(m => m.id === currentManualId)?.canva || '');
          openImageInModal([src], img.dataset.caption || img.getAttribute('alt') || '상세 이미지', canvaUrl);
        }});
      }});
    }}

    bindImageToggles(document);

    // Add Manual Modal Logic
    function openAddManualModal() {{
      populateAddManualCategorySelect();
      addModal.hidden = false;
      document.body.classList.add('modal-open');
    }}

    function closeAddManualModal() {{
      addModal.hidden = true;
      document.body.classList.remove('modal-open');
    }}

    addModal.addEventListener('click', (e) => {{
      if (e.target === addModal) closeAddManualModal();
    }});

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        if (!modal.hidden) closeModal();
        if (!addModal.hidden) closeAddManualModal();
        if (!catEditModal.hidden) closeCategoryEditModal();
      }}
    }});

    const dropArea = document.getElementById('fileDropArea');
    ['dragenter', 'dragover'].forEach(evt => {{
      dropArea.addEventListener(evt, (e) => {{
        e.preventDefault();
        dropArea.style.borderColor = 'var(--blue)';
        dropArea.style.background = '#dbeafe';
      }});
    }});
    ['dragleave', 'drop'].forEach(evt => {{
      dropArea.addEventListener(evt, (e) => {{
        e.preventDefault();
        dropArea.style.borderColor = '#93c5fd';
        dropArea.style.background = 'var(--blue-soft)';
      }});
    }});
    dropArea.addEventListener('drop', (e) => {{
      const files = e.dataTransfer?.files;
      if (files && files.length) processUploadedFiles(Array.from(files));
    }});

    function handleManualFileSelect(e) {{
      const files = e.target.files;
      if (files && files.length) processUploadedFiles(Array.from(files));
    }}

    function readFileAsDataURL(file) {{
      return new Promise((resolve, reject) => {{
        const reader = new FileReader();
        reader.onload = (ev) => resolve(ev.target.result);
        reader.onerror = () => reject(reader.error);
        reader.readAsDataURL(file);
      }});
    }}

    function readFileAsText(file) {{
      return new Promise((resolve, reject) => {{
        const reader = new FileReader();
        reader.onload = (ev) => resolve(ev.target.result);
        reader.onerror = () => reject(reader.error);
        reader.readAsText(file, 'utf-8');
      }});
    }}

    function buildStandaloneHtmlFromPdfOrImage(title, type, dataUrls, canvaUrl) {{
      const canvaBtn = canvaUrl ? `<a class="source-button" href="${{canvaUrl}}" target="_blank" rel="noopener">원본 문서 열기</a>` : '';
      let bodySection = '';
      if (type === 'pdf') {{
        bodySection = `
          <div class="pdf-embed-wrap">
            <iframe class="pdf-embed-frame" data-pdf-src="${{dataUrls[0]}}" src="${{dataUrls[0]}}" title="${{title}} PDF 문서"></iframe>
          </div>`;
      }} else {{
        bodySection = dataUrls.map((url, idx) => `
          <article class="step">
            <div class="step-top">
              <span class="num">${{idx + 1}}</span>
              <h3>${{dataUrls.length > 1 ? (title + ' (' + (idx + 1) + '/' + dataUrls.length + ')') : title}}</h3>
              <button class="img-toggle" type="button" aria-label="이미지 확대 보기" title="클릭하여 크게 보기" data-image="${{url}}" data-alt="${{title}} ${{idx + 1}}">🔍</button>
            </div>
            <figure class="inline-figure"><img src="${{url}}" alt="${{title}} ${{idx + 1}}"></figure>
          </article>`).join('');
      }}

      return `<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${{title}}</title><style>:root{{--ink:#172033;--muted:#5b6475;--line:#dfe5ee;--blue:#2563eb;--blue-soft:#eff6ff}}*{{box-sizing:border-box}}body{{margin:0;background:#f5f7fb;color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI","Noto Sans KR",sans-serif;line-height:1.55}}.page{{max-width:1080px;margin:0 auto;padding:28px;background:#fff;min-height:100vh}}header{{border-bottom:2px solid var(--ink);padding-bottom:16px;margin-bottom:18px}}.title-row{{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}}.title-highlight{{background:linear-gradient(transparent 48%,#fff36a 48%,#fff36a 91%,transparent 91%);padding:0 .1em}}h1{{margin:0;font-size:clamp(26px,4vw,42px);line-height:1.15;letter-spacing:-.04em;font-weight:850}}.source-button{{display:inline-flex;align-items:center;padding:9px 14px;border-radius:999px;background:var(--blue);color:#fff;font-size:13px;font-weight:800;text-decoration:none}}.step{{position:relative;border:1px solid var(--line);border-radius:12px;padding:17px 18px;margin:0 0 14px;background:#fff}}.step-top{{display:flex;align-items:center;gap:10px;padding-right:48px;margin-bottom:8px}}.num{{display:grid;place-items:center;width:32px;height:32px;flex:0 0 auto;border-radius:50%;background:var(--blue);color:#fff;font-weight:850}}.step h3{{margin:0;font-size:18px;line-height:1.25}}.img-toggle{{position:absolute;top:13px;right:14px;width:35px;height:35px;display:grid;place-items:center;border:1px solid #93c5fd;border-radius:50%;padding:0;background:#fff;color:#1d4ed8;font-size:18px;cursor:pointer}}.inline-figure{{margin:12px 0 4px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}}.inline-figure img{{display:block;width:100%;height:auto}}.pdf-embed-wrap{{margin:14px 0 6px;border:1.5px solid var(--line);border-radius:12px;overflow:hidden;background:#334155}}.pdf-embed-frame{{display:block;width:100%;height:84vh;min-height:760px;border:none;background:#fff}}</style></head><body><main class="page"><header><div class="title-row"><h1><span class="title-highlight">${{title}}</span></h1>${{canvaBtn}}</div></header>${{bodySection}}</main><script>document.querySelectorAll('iframe.pdf-embed-frame[data-pdf-src]').forEach(f=>{{try{{const b=atob(f.dataset.pdfSrc.split(',')[1]),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);f.src=URL.createObjectURL(new Blob([u],{{type:'application/pdf'}}))}}catch(e){{}}}});<\/script></body></html>`;
    }}

    async function processUploadedFiles(files) {{
      const first = files[0];
      const baseName = first.name.replace(/\\.[^.]+$/, '');
      const ext = (first.name.split('.').pop() || '').toLowerCase();
      const titleInput = document.getElementById('manualShortTitle');

      if (ext === 'html' || ext === 'htm') {{
        uploadedFileType = 'html';
        uploadedFileName = first.name;
        uploadedRawHtml = await readFileAsText(first);
        uploadedDataUrls = [];
        document.getElementById('fileDropText').textContent = '✅ HTML 선택됨: ' + first.name;
        const parser = new DOMParser();
        const doc = parser.parseFromString(uploadedRawHtml, 'text/html');
        const h1Text = doc.querySelector('h1')?.textContent?.trim() || doc.title?.trim() || baseName;
        if (!titleInput.value.trim()) {{
          titleInput.value = h1Text.length > 18 ? h1Text.slice(0, 18) : h1Text;
        }}
        const steps = doc.querySelectorAll('.step').length;
        if (steps > 0) document.getElementById('manualStepsCount').value = steps;
        const canvaLink = doc.querySelector('a.source-button')?.getAttribute('href') || '';
        if (canvaLink && !document.getElementById('manualCanvaUrl').value) {{
          document.getElementById('manualCanvaUrl').value = canvaLink;
        }}
      }} else if (ext === 'pdf' || first.type === 'application/pdf') {{
        uploadedFileType = 'pdf';
        uploadedFileName = baseName + '-pdf-guide.html';
        const dataUrl = await readFileAsDataURL(first);
        uploadedDataUrls = [dataUrl];
        uploadedRawHtml = 'PDF_PENDING';
        document.getElementById('fileDropText').textContent = '✅ PDF 선택됨: ' + first.name;
        if (!titleInput.value.trim()) titleInput.value = baseName.slice(0, 18);
        document.getElementById('manualStepsCount').value = 1;
      }} else if (first.type.startsWith('image/') || ['png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'].includes(ext)) {{
        uploadedFileType = 'image';
        uploadedFileName = baseName + '-image-guide.html';
        uploadedDataUrls = await Promise.all(files.map(f => readFileAsDataURL(f)));
        uploadedRawHtml = 'IMAGE_PENDING';
        document.getElementById('fileDropText').textContent = `✅ 이미지 ${{files.length}}장 선택됨: ${{first.name}}${{files.length > 1 ? ' 외 ' + (files.length - 1) + '장' : ''}}`;
        if (!titleInput.value.trim()) titleInput.value = baseName.slice(0, 18);
        document.getElementById('manualStepsCount').value = files.length;
      }} else {{
        alert('지원하지 않는 파일 형식입니다. HTML, PDF 또는 이미지 파일을 선택해주세요.');
      }}
    }}

    // IndexedDB Storage for Custom Manuals
    function openManualDB() {{
      return new Promise((resolve, reject) => {{
        const req = indexedDB.open('OnlineOfficeManualDB', 1);
        req.onupgradeneeded = (e) => {{
          const db = e.target.result;
          if (!db.objectStoreNames.contains('manuals')) {{
            db.createObjectStore('manuals', {{ keyPath: 'id' }});
          }}
        }};
        req.onsuccess = () => resolve(req.result);
        req.onerror = () => reject(req.error);
      }});
    }}

    async function saveCustomManualToDB(item) {{
      try {{
        const db = await openManualDB();
        return new Promise((resolve) => {{
          const tx = db.transaction('manuals', 'readwrite');
          const copy = {{ id: item.id, title: item.title, stepsCount: item.stepsCount, canva: item.canva, category: item.category, contentHtml: item.contentHtml, rawHtml: item.rawHtml, fileName: item.fileName }};
          tx.objectStore('manuals').put(copy);
          tx.oncomplete = () => resolve(true);
          tx.onerror = () => resolve(false);
        }});
      }} catch (e) {{
        console.warn('IndexedDB save failed:', e);
        return false;
      }}
    }}

    async function deleteCustomManualFromDB(id) {{
      try {{
        const db = await openManualDB();
        return new Promise((resolve) => {{
          const tx = db.transaction('manuals', 'readwrite');
          tx.objectStore('manuals').delete(id);
          tx.oncomplete = () => resolve(true);
          tx.onerror = () => resolve(false);
        }});
      }} catch (e) {{
        console.warn('IndexedDB delete failed:', e);
        return false;
      }}
    }}

    async function loadCustomManualsFromDB() {{
      try {{
        const db = await openManualDB();
        return new Promise((resolve) => {{
          const tx = db.transaction('manuals', 'readwrite');
          const store = tx.objectStore('manuals');
          const req = store.getAll();
          req.onsuccess = () => {{
            const all = req.result || [];
            const valid = [];
            all.forEach(item => {{
              const c = item.contentHtml || '';
              if (BUILTIN_IDS.has(item.id) || c.includes('JFIF') || c.startsWith('%PDF-') || c.includes('\ufffd\ufffd\ufffd')) {{
                store.delete(item.id);
              }} else {{
                valid.push(item);
              }}
            }});
            resolve(valid);
          }};
          req.onerror = () => resolve([]);
        }});
      }} catch (e) {{
        return [];
      }}
    }}

    function triggerUrlDownload(url, filename) {{
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.style.display = 'none';
      document.body.appendChild(a);
      a.click();
      setTimeout(() => a.remove(), 2000);
    }}

    function buildPaneHtmlFromRaw(rawHtml, canvaUrl, fileName) {{
      const parser = new DOMParser();
      const doc = parser.parseFromString(rawHtml, 'text/html');
      doc.querySelectorAll('.modal, .modal-close, script').forEach(el => el.remove());
      const mainEl = doc.querySelector('main.page') || doc.querySelector('main') || doc.body;
      const titleRow = mainEl.querySelector('.title-row');
      if (titleRow) {{
        titleRow.querySelectorAll('a.source-button, .title-actions').forEach(el => el.remove());
        const actionsDiv = doc.createElement('div');
        actionsDiv.className = 'title-actions';
        if (canvaUrl) {{
          actionsDiv.innerHTML += `<a class="source-button" href="${{canvaUrl}}" target="_blank" rel="noopener">원본 문서 열기</a>`;
        }}
        const fileHref = fileName ? `pages/${{fileName}}` : '#';
        actionsDiv.innerHTML += `
          <a href="${{fileHref}}" target="_blank" rel="noopener" class="pane-standalone-link" onclick="if(this.dataset.blobUrl){{window.open(this.dataset.blobUrl,'_blank');return false;}}" title="새 창에서 독립 파일로 열기">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            독립창 열기
          </a>`;
        titleRow.appendChild(actionsDiv);
      }}
      return mainEl.innerHTML;
    }}

    function renderCustomManual(item) {{
      if (document.querySelector(`.manual-nav-btn[data-id="${{item.id}}"]`)) {{
        document.querySelector(`.manual-nav-btn[data-id="${{item.id}}"]`).remove();
      }}
      if (document.getElementById(`pane-${{item.id}}`)) {{
        document.getElementById(`pane-${{item.id}}`).remove();
      }}

      const catId = (item.category && CATEGORIES_DATA.some(c => c.id === item.category))
        ? item.category
        : (CATEGORIES_DATA[0]?.id || 'office-basic');
      item.category = catId;

      let blobUrl = '';
      if (item.rawHtml) {{
        const blob = new Blob([item.rawHtml], {{ type: 'text/html;charset=utf-8' }});
        blobUrl = URL.createObjectURL(blob);
      }}
      item.blobUrl = blobUrl;

      const storeIdx = customManualsStore.findIndex(m => m.id === item.id);
      if (storeIdx >= 0) customManualsStore.splice(storeIdx, 1);
      customManualsStore.push(item);

      const existIdx = MANUAL_LIST.findIndex(m => m.id === item.id);
      if (existIdx >= 0) MANUAL_LIST.splice(existIdx, 1);
      MANUAL_LIST.push({{ id: item.id, title: item.title, canva: item.canva || '', category: catId, isCustom: true }});

      const navGrid = document.getElementById('manualNavGrid');
      const addBtn = document.getElementById('openAddManualBtn');
      const btn = document.createElement('a');
      btn.href = '#' + item.id;
      btn.className = 'manual-nav-btn';
      btn.dataset.id = item.id;
      btn.dataset.category = catId;
      btn.dataset.catTheme = String(getCategoryThemeIndex(catId));
      btn.dataset.custom = '1';
      btn.title = getCategoryName(catId);
      btn.draggable = true;
      btn.onclick = (e) => {{
        e.preventDefault();
        selectManual(item.id);
      }};
      btn.innerHTML = `
        <button type="button" class="nav-btn-del" title="이 매뉴얼 삭제" onclick="removeCustomManual(event, '${{item.id}}')">×</button>
        <span class="nav-btn-title">${{item.title}}</span>
      `;
      navGrid.insertBefore(btn, addBtn);

      const contentArea = document.getElementById('manualContentArea');
      const pane = document.createElement('div');
      pane.id = 'pane-' + item.id;
      pane.className = 'manual-pane';
      pane.dataset.id = item.id;
      pane.dataset.canva = item.canva || '';
      pane.innerHTML = `<main class="page">${{item.contentHtml}}</main>`;

      if (blobUrl) {{
        const standaloneLink = pane.querySelector('.pane-standalone-link');
        if (standaloneLink) standaloneLink.dataset.blobUrl = blobUrl;
      }}

      contentArea.appendChild(pane);
      bindImageToggles(pane);
      hydratePdfFrames(pane);
      renderCategoryBar();
      updateDeployButtonVisibility();
    }}

    async function removeCustomManual(e, id) {{
      e.stopPropagation();
      e.preventDefault();
      if (!confirm('추가한 매뉴얼을 목록에서 삭제하시겠습니까?')) return;
      await deleteCustomManualFromDB(id);
      document.querySelector(`.manual-nav-btn[data-id="${{id}}"]`)?.remove();
      document.getElementById(`pane-${{id}}`)?.remove();
      const sIdx = customManualsStore.findIndex(m => m.id === id);
      if (sIdx >= 0) customManualsStore.splice(sIdx, 1);
      const idx = MANUAL_LIST.findIndex(m => m.id === id);
      if (idx >= 0) MANUAL_LIST.splice(idx, 1);
      renderCategoryBar();
      updateDeployButtonVisibility();
      if (currentManualId === id) {{
        selectManual(MANUAL_LIST[0].id);
      }}
    }}

    async function registerCurrentFormManual() {{
      if (!uploadedRawHtml) return null;
      const title = document.getElementById('manualShortTitle').value.trim() || uploadedFileName.replace(/\\.html?$/i, '');
      const stepsCount = parseInt(document.getElementById('manualStepsCount').value, 10) || 1;
      const category = document.getElementById('manualCategorySelect')?.value || (CATEGORIES_DATA[0]?.id || 'office-basic');
      const canva = document.getElementById('manualCanvaUrl').value.trim();
      const slugBase = (uploadedFileName || title).replace(/\\.html?$/i, '').replace(/[^a-zA-Z0-9가-힣_-]/g, '-').toLowerCase();
      const id = 'manual-' + (slugBase || Date.now());
      const safeFileName = uploadedFileName || (id + '.html');

      let finalRawHtml = uploadedRawHtml;
      if (uploadedFileType === 'pdf' || uploadedFileType === 'image') {{
        finalRawHtml = buildStandaloneHtmlFromPdfOrImage(title, uploadedFileType, uploadedDataUrls, canva);
      }}

      const contentHtml = buildPaneHtmlFromRaw(finalRawHtml, canva, safeFileName);
      const item = {{ id, title, stepsCount, canva, category, contentHtml, rawHtml: finalRawHtml, fileName: safeFileName }};

      renderCustomManual(item);
      await saveCustomManualToDB(item);

      document.getElementById('addManualForm').reset();
      document.getElementById('fileDropText').textContent = '📂 클릭하여 HTML · PDF · 이미지 파일 선택 (또는 드래그)';
      uploadedRawHtml = '';
      uploadedFileName = '';
      uploadedFileType = '';
      uploadedDataUrls = [];
      return item;
    }}

    async function handleAddManualSubmit(e) {{
      e.preventDefault();
      if (!uploadedRawHtml) {{
        alert('먼저 업로드할 파일(HTML, PDF, 이미지)을 선택해주세요.');
        return;
      }}
      const item = await registerCurrentFormManual();
      if (item) {{
        closeAddManualModal();
        if (currentCategoryId !== 'all' && currentCategoryId !== item.category) {{
          currentCategoryId = item.category;
          renderCategoryBar();
        }}
        selectManual(item.id);
      }}
    }}

    function buildUpdatedIndexHtmlString() {{
      const clone = document.documentElement.cloneNode(true);
      clone.querySelector('#globalImageModal')?.setAttribute('hidden', '');
      clone.querySelector('#addManualModal')?.setAttribute('hidden', '');
      clone.querySelector('#categoryEditModal')?.setAttribute('hidden', '');
      clone.querySelector('#btnHeaderDeployDownload')?.setAttribute('hidden', '');
      clone.querySelector('body')?.classList.remove('modal-open');
      clone.querySelectorAll('.nav-btn-del').forEach(el => el.remove());
      clone.querySelectorAll('.manual-nav-btn').forEach(el => {{
        el.removeAttribute('data-custom');
        el.removeAttribute('hidden');
        const item = MANUAL_LIST.find(m => m.id === el.dataset.id);
        if (item) {{
          el.dataset.category = item.category;
          el.dataset.catTheme = String(getCategoryThemeIndex(item.category));
          el.title = getCategoryName(item.category);
        }}
      }});
      clone.querySelectorAll('.pane-standalone-link').forEach(el => el.removeAttribute('data-blob-url'));
      clone.querySelectorAll('.img-toggle').forEach(el => el.removeAttribute('data-bound'));
      clone.querySelectorAll('.inline-figure img').forEach(el => el.removeAttribute('data-bound-zoom'));
      clone.querySelectorAll('iframe.pdf-embed-frame[data-pdf-src]').forEach(frame => {{
        frame.removeAttribute('data-hydrated');
        frame.removeAttribute('src');
      }});
      const scriptEl = clone.querySelector('#mainPortalScript');
      if (scriptEl) {{
        const cleanCats = CATEGORIES_DATA.map((c, idx) => ({{ id: c.id, name: c.name, theme: typeof c.theme === 'number' ? c.theme : (idx % 8) }}));
        const cleanList = MANUAL_LIST.map(m => ({{ id: m.id, title: m.title, canva: m.canva || '', category: m.category }}));
        scriptEl.textContent = scriptEl.textContent
          .replace(
            /const INITIAL_CATEGORIES = \\[.*?\\];/,
            'const INITIAL_CATEGORIES = ' + JSON.stringify(cleanCats) + ';'
          )
          .replace(
            /const MANUAL_LIST = \\[.*?\\];/,
            'const MANUAL_LIST = ' + JSON.stringify(cleanList) + ';'
          );
      }}
      return '<!doctype html>\\n' + clone.outerHTML;
    }}

    function downloadAllDeploymentFiles() {{
      const downloadQueue = [];
      customManualsStore.forEach(item => {{
        if (item.rawHtml) {{
          const fname = item.fileName || (item.id + '.html');
          const url = item.blobUrl || URL.createObjectURL(new Blob([item.rawHtml], {{ type: 'text/html;charset=utf-8' }}));
          downloadQueue.push({{ url, fname }});
        }}
      }});

      const indexHtmlStr = buildUpdatedIndexHtmlString();
      const indexBlobUrl = URL.createObjectURL(new Blob([indexHtmlStr], {{ type: 'text/html;charset=utf-8' }}));
      downloadQueue.push({{ url: indexBlobUrl, fname: 'index.html' }});

      downloadQueue.forEach((entry, idx) => {{
        if (idx === 0) {{
          triggerUrlDownload(entry.url, entry.fname);
        }} else {{
          setTimeout(() => {{
            triggerUrlDownload(entry.url, entry.fname);
          }}, idx * 250);
        }}
      }});
      hasOrderChanged = false;
      hasCategoryChanged = false;
      if (deployDownloadBtn) deployDownloadBtn.hidden = true;
    }}

    // Drag and Drop Reordering for Manual Buttons + Drop onto Category Tabs
    let draggedBtn = null;

    function syncManualOrderFromDOM(saveToStorage = true) {{
      const navGrid = document.getElementById('manualNavGrid');
      const btns = Array.from(navGrid.querySelectorAll('.manual-nav-btn'));
      const newOrderIds = btns.map(b => b.dataset.id);
      MANUAL_LIST.sort((a, b) => {{
        const ia = newOrderIds.indexOf(a.id);
        const ib = newOrderIds.indexOf(b.id);
        return (ia === -1 ? 999 : ia) - (ib === -1 ? 999 : ib);
      }});
      if (saveToStorage) {{
        hasOrderChanged = true;
        updateDeployButtonVisibility();
        try {{
          localStorage.setItem(ORDER_STORAGE_KEY, JSON.stringify(newOrderIds));
        }} catch (e) {{}}
      }}
    }}

    function applySavedManualOrder() {{
      try {{
        const raw = localStorage.getItem(ORDER_STORAGE_KEY);
        if (!raw) return;
        const savedOrder = JSON.parse(raw);
        if (!Array.isArray(savedOrder) || !savedOrder.length) return;
        const navGrid = document.getElementById('manualNavGrid');
        const addBtn = document.getElementById('openAddManualBtn');
        savedOrder.forEach(id => {{
          const btn = navGrid.querySelector(`.manual-nav-btn[data-id="${{id}}"]`);
          if (btn) navGrid.insertBefore(btn, addBtn);
        }});
        syncManualOrderFromDOM(false);
      }} catch (e) {{}}
    }}

    function bindCategoryTabDropTargets() {{
      const tabsContainer = document.getElementById('categoryTabs');
      if (!tabsContainer) return;
      tabsContainer.querySelectorAll('.category-tab').forEach(tab => {{
        const catId = tab.dataset.catId;
        if (!catId || catId === 'all') return;
        tab.addEventListener('dragover', (e) => {{
          if (!draggedBtn) return;
          e.preventDefault();
          e.dataTransfer.dropEffect = 'move';
          tab.classList.add('drag-over-cat');
        }});
        tab.addEventListener('dragleave', () => {{
          tab.classList.remove('drag-over-cat');
        }});
        tab.addEventListener('drop', (e) => {{
          if (!draggedBtn) return;
          e.preventDefault();
          tab.classList.remove('drag-over-cat');
          const manualId = draggedBtn.dataset.id;
          if (manualId) {{
            assignManualToCategory(manualId, catId);
          }}
        }});
      }});
    }}

    function initNavDragAndDrop() {{
      const navGrid = document.getElementById('manualNavGrid');
      navGrid.addEventListener('dragstart', (e) => {{
        const btn = e.target.closest('.manual-nav-btn');
        if (!btn) return;
        draggedBtn = btn;
        btn.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/plain', btn.dataset.id);
      }});

      navGrid.addEventListener('dragover', (e) => {{
        if (!draggedBtn) return;
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
        const targetBtn = e.target.closest('.manual-nav-btn');
        navGrid.querySelectorAll('.manual-nav-btn').forEach(b => b.classList.remove('drag-over'));
        if (targetBtn && targetBtn !== draggedBtn) {{
          targetBtn.classList.add('drag-over');
        }}
      }});

      navGrid.addEventListener('dragleave', (e) => {{
        const targetBtn = e.target.closest('.manual-nav-btn');
        if (targetBtn) targetBtn.classList.remove('drag-over');
      }});

      navGrid.addEventListener('drop', (e) => {{
        if (!draggedBtn) return;
        e.preventDefault();
        const targetBtn = e.target.closest('.manual-nav-btn');
        navGrid.querySelectorAll('.manual-nav-btn').forEach(b => b.classList.remove('drag-over'));
        if (targetBtn && targetBtn !== draggedBtn) {{
          const allBtns = Array.from(navGrid.querySelectorAll('.manual-nav-btn'));
          const draggedIdx = allBtns.indexOf(draggedBtn);
          const targetIdx = allBtns.indexOf(targetBtn);
          if (draggedIdx < targetIdx) {{
            navGrid.insertBefore(draggedBtn, targetBtn.nextSibling);
          }} else {{
            navGrid.insertBefore(draggedBtn, targetBtn);
          }}
          syncManualOrderFromDOM(true);
        }}
      }});

      navGrid.addEventListener('dragend', () => {{
        if (draggedBtn) draggedBtn.classList.remove('dragging');
        navGrid.querySelectorAll('.manual-nav-btn').forEach(b => b.classList.remove('drag-over'));
        document.querySelectorAll('.category-tab').forEach(t => t.classList.remove('drag-over-cat'));
        draggedBtn = null;
      }});
    }}

    loadCategoryStateFromStorage();
    renderCategoryBar();
    initNavDragAndDrop();
    handleHash();
    window.addEventListener('DOMContentLoaded', async () => {{
      const saved = await loadCustomManualsFromDB();
      saved.forEach(item => renderCustomManual(item));
      loadCategoryStateFromStorage();
      applySavedManualOrder();
      renderCategoryBar();
      updateDeployButtonVisibility();
      handleHash();
    }});
  </script>
</body>
</html>
"""

# Output paths
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(index_html)

bundle_path = os.path.join(BASE_DIR, "bundle_manuals.py")
with open(__file__, "r", encoding="utf-8") as f:
    self_code = f.read()
with open(bundle_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(self_code)

print("Generated clean index.html with 20 manuals, category tabs, and category editor.")
print("File size:", round(os.path.getsize(index_path) / 1024 / 1024, 2), "MB")

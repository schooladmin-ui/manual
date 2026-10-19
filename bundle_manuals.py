import os, json, re

# Configuration for the 7 manuals
MANUALS = [
    {
        "id": "chrome-default",
        "file": "chrome-default-app-guide-with-canva-link.html",
        "title": "크롬브라우저 기본앱으로 설정하는 방법",
        "category": "브라우저 환경",
        "category_id": "browser",
        "cat_color": "#2563eb",
        "cat_bg": "#eff6ff",
        "badge": "기본 브라우저",
        "lead": "Windows에서 웹 브라우저 기본 앱을 Google Chrome으로 지정하는 3단계 안내",
        "canva": "https://www.canva.com/design/DAGotK1iBWQ/fQ9N3piaD0zZCDtNWv6vCw/view?utm_content=DAGotK1iBWQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h39e2295cc7",
        "icon": "🌐",
        "read_time": "1분"
    },
    {
        "id": "bookmark-bar",
        "file": "bookmark-bar-manual-with-canva-link.html",
        "title": "크롬 북마크바 표시 방법",
        "category": "브라우저 환경",
        "category_id": "browser",
        "cat_color": "#2563eb",
        "cat_bg": "#eff6ff",
        "badge": "북마크 관리",
        "lead": "학교 계정의 북마크를 보이게 하고, 북마크바에 바로가기를 추가하는 한 페이지 안내",
        "canva": "https://www.canva.com/design/DAGoE56L5Qw/zEwEBK0UluCzBb1HR838Cg/view?utm_content=DAGoE56L5Qw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7dc1509390",
        "icon": "⭐",
        "read_time": "2분"
    },
    {
        "id": "desktop-button",
        "file": "desktop-button-guide-manual.html",
        "title": "바탕화면에 온라인교무실 바로가기 버튼 만들기",
        "category": "온라인교무실",
        "category_id": "portal",
        "cat_color": "#4f46e5",
        "cat_bg": "#eef2ff",
        "badge": "앱 바로가기",
        "lead": "Google 사이트를 바탕화면 앱 버튼으로 설치하는 절차",
        "canva": "https://www.canva.com/design/DAHGJQe8CAA/kYI9m7jIEDhPaAbkuLZDGg/view?utm_content=DAHGJQe8CAA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=ha7f0287432",
        "icon": "🖥️",
        "read_time": "2분"
    },
    {
        "id": "main-page-edit",
        "file": "main-page-edit-guide-manual.html",
        "title": "메인 페이지 편집 방법",
        "category": "온라인교무실",
        "category_id": "portal",
        "cat_color": "#4f46e5",
        "cat_bg": "#eef2ff",
        "badge": "사이트 편집",
        "lead": "온라인교무실 Google 사이트의 메인 페이지를 수정하고 버튼을 만드는 절차",
        "canva": "https://www.canva.com/design/DAGm6pqOZJM/rQnX-rH46Qv1cxtFaN2xhg/view?utm_content=DAGm6pqOZJM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h48af137ff0",
        "icon": "✏️",
        "read_time": "3분"
    },
    {
        "id": "notebooklm",
        "file": "notebooklm-create-share-guide-manual.html",
        "title": "구글 Notebook LM 생성 후 공유 방법",
        "category": "AI & 업무도구",
        "category_id": "ai-tools",
        "cat_color": "#d97706",
        "cat_bg": "#fffbeb",
        "badge": "스마트 AI 업무",
        "lead": "PDF 소스를 NotebookLM에 업로드하고 온라인교무실에 공유 버튼으로 게시하는 전체 절차",
        "canva": "https://www.canva.com/design/DAHIAXtwfPQ/c0rlZicbmWImDTlLa5JJkQ/view?utm_content=DAHIAXtwfPQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7c5f276f63",
        "icon": "🧠",
        "read_time": "5분"
    },
    {
        "id": "permission-setting",
        "file": "permission-setting-guide-with-canva-link.html",
        "title": "온라인교무실 공유 폴더 권한 설정 방법",
        "category": "보안 & 드라이브",
        "category_id": "security",
        "cat_color": "#e11d48",
        "cat_bg": "#fff1f2",
        "badge": "보안 & 권한",
        "lead": "공유 문서함의 파일을 특정 교사·그룹에게만 공유하고 학생 접근을 막는 절차",
        "canva": "https://www.canva.com/design/DAGm6gX_4lM/rVOmpsykESZmuqzTnOMz8A/view?utm_content=DAGm6gX_4lM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=hb1133ff80a",
        "icon": "🔒",
        "read_time": "3분"
    },
    {
        "id": "training-signature",
        "file": "training-signature-guide-manual.html",
        "title": "연수서명부 서명 방법",
        "category": "교무 행정",
        "category_id": "admin",
        "cat_color": "#059669",
        "cat_bg": "#ecfdf5",
        "badge": "연수 서명",
        "lead": "도장 이미지를 준비해 Google Drive 연수서명부에 삽입하고 서명하는 절차",
        "canva": "https://www.canva.com/design/DAGm6jijC7A/i3ovxr1djLZxKIW9JRvAKg/view?utm_content=DAGm6jijC7A&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h1e3a1fe2c0",
        "icon": "🖋️",
        "read_time": "2분"
    }
]

# Extract mains from all files
manual_contents = {}
for m in MANUALS:
    fpath = m["file"]
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        raw = fp.read()
    
    # Extract main content
    main_match = re.search(r'<main class="page">(.*?)</main>', raw, re.DOTALL)
    if main_match:
        content = main_match.group(1).strip()
    else:
        content = "<div>매뉴얼 내용을 불러올 수 없습니다.</div>"
    
    # Extract steps for card preview
    step_titles = re.findall(r'<article class="step">.*?<h2>(.*?)</h2>', raw, re.DOTALL)
    clean_steps = [re.sub(r'<[^>]+>', '', s).strip() for s in step_titles]
    m["steps"] = clean_steps
    m["step_count"] = len(clean_steps)
    
    manual_contents[m["id"]] = content

print("Extracted content for", len(manual_contents), "manuals.")

# Generate the index.html code
cards_html = []
for idx, m in enumerate(MANUALS, 1):
    step_chips = "".join([f'<span class="step-chip" title="{s}"><span class="step-idx">{i+1}</span>{s}</span>' for i, s in enumerate(m["steps"][:4])])
    if len(m["steps"]) > 4:
        step_chips += f'<span class="step-chip more">+{len(m["steps"])-4}단계 더보기</span>'
        
    card = f"""
    <div class="manual-card" data-id="{m['id']}" data-category="{m['category_id']}" data-search="{m['title'].lower()} {m['lead'].lower()} {' '.join(m['steps']).lower()}">
      <div class="card-header">
        <span class="card-badge" style="background:{m['cat_bg']}; color:{m['cat_color']}; border-color:{m['cat_color']}33;">
          {m['icon']} {m['category']}
        </span>
        <span class="card-steps-count">{m['step_count']}단계 안내 · {m['read_time']}</span>
      </div>
      <h3 class="card-title">
        <span class="card-number">0{idx}</span>
        <span class="title-highlight">{m['title']}</span>
      </h3>
      <p class="card-lead">{m['lead']}</p>
      <div class="card-steps-preview">
        {step_chips}
      </div>
      <div class="card-actions">
        <a href="#{m['id']}" class="btn-read" onclick="openManual('{m['id']}'); return true;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
          포털에서 가이드 보기
        </a>
        <div class="btn-group-sub">
          <a href="{m['file']}" target="_blank" rel="noopener" class="btn-sub" title="개별 HTML 파일로 열기">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            개별창
          </a>
          <a href="{m['canva']}" target="_blank" rel="noopener" class="btn-sub btn-canva" title="원본 Canva 슬라이드 프레젠테이션 열기">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            Canva
          </a>
        </div>
      </div>
    </div>
    """
    cards_html.append(card)

# Options for quick jump dropdown in reader
dropdown_options = []
for idx, m in enumerate(MANUALS, 1):
    dropdown_options.append(f'<option value="{m["id"]}">[{idx}/7] {m["title"]}</option>')

# Panes html
panes_html = []
for m in MANUALS:
    content = manual_contents[m["id"]]
    pane = f"""
    <div id="pane-{m['id']}" class="manual-pane" data-id="{m['id']}">
      <main class="page">
        {content}
      </main>
    </div>
    """
    panes_html.append(pane)

# Assembly of index.html
index_html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>홍익여고 온라인교무실 업무 매뉴얼 포털 | 7대 핵심 가이드북</title>
  <meta name="description" content="홍익여자고등학교 온라인교무실 및 Google Workspace 교원 업무 효율화를 위한 7대 필수 가이드북 종합 포털 (Chrome 기본앱, 북마크, 사이트 바로가기, 메인편집, NotebookLM, 권한설정, 연수서명)">
  <meta name="keywords" content="온라인교무실, 홍익여고, 구글 워크스페이스, 크롬 북마크, 기본앱 설정, NotebookLM, 연수서명부, 사이트 편집">
  <meta property="og:title" content="홍익여고 온라인교무실 업무 매뉴얼 포털">
  <meta property="og:description" content="교원 디지털 업무 지원을 위한 7대 필수 가이드북 한눈에 보기 및 바로가기">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    /* =========================================================
       1. Global Design System & Variables
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
      --amber: #d97706;
      --amber-soft: #fffbeb;
      --indigo: #4f46e5;
      --indigo-soft: #eef2ff;
      
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 12px -2px rgba(15,23,42,0.08), 0 2px 6px -1px rgba(15,23,42,0.04);
      --shadow-lg: 0 12px 32px -4px rgba(15,23,42,0.12), 0 4px 12px -2px rgba(15,23,42,0.05);
      --shadow-xl: 0 20px 48px -8px rgba(15,23,42,0.2);
      
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
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* =========================================================
       2. Global Portal Header & Nav
       ========================================================= */
    .portal-nav {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--line);
      box-shadow: var(--shadow-sm);
    }}

    .portal-nav-inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}

    .brand-icon {{
      width: 42px;
      height: 42px;
      border-radius: 10px;
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 50%, #3b82f6 100%);
      display: grid;
      place-items: center;
      color: #fff;
      font-size: 20px;
      box-shadow: 0 4px 10px rgba(37,99,235,0.25);
    }}

    .brand-text {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title {{
      font-size: 17px;
      font-weight: 850;
      color: var(--ink-dark);
      letter-spacing: -0.02em;
      line-height: 1.25;
    }}

    .brand-sub {{
      font-size: 12px;
      font-weight: 500;
      color: var(--muted);
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 650;
      text-decoration: none;
      color: var(--ink-secondary);
      background: #fff;
      border: 1px solid var(--line);
      cursor: pointer;
      transition: all 0.18s ease;
      white-space: nowrap;
    }}

    .nav-btn:hover {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
      transform: translateY(-1px);
    }}

    .nav-btn-primary {{
      background: var(--blue);
      color: #fff;
      border-color: var(--blue);
      box-shadow: 0 2px 6px rgba(37,99,235,0.2);
    }}

    .nav-btn-primary:hover {{
      background: var(--blue-dark);
      color: #fff;
      border-color: var(--blue-dark);
    }}

    /* =========================================================
       3. Hero Banner & Stats
       ========================================================= */
    .portal-hero {{
      background: linear-gradient(180deg, #ffffff 0%, #f1f5f9 100%);
      border-bottom: 1px solid var(--line);
      padding: 44px 24px 36px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}

    .portal-hero::before {{
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 50% 10%, rgba(37, 99, 235, 0.08) 0%, transparent 60%);
      pointer-events: none;
    }}

    .hero-container {{
      max-width: 980px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }}

    .hero-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      background: var(--blue-soft);
      border: 1px solid var(--blue-border);
      color: var(--blue-dark);
      font-size: 12.5px;
      font-weight: 750;
      margin-bottom: 16px;
    }}

    .hero-title {{
      font-size: clamp(26px, 4.5vw, 40px);
      font-weight: 900;
      letter-spacing: -0.035em;
      color: var(--ink-dark);
      line-height: 1.25;
      margin-bottom: 12px;
    }}

    .hero-desc {{
      font-size: clamp(14.5px, 2vw, 17px);
      color: var(--muted);
      line-height: 1.6;
      max-width: 780px;
      margin: 0 auto 24px;
    }}

    .hero-notice {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--red-soft);
      border: 1px solid #fecaca;
      border-left: 5px solid var(--red);
      border-radius: var(--radius-sm);
      padding: 10px 16px;
      font-size: 13.5px;
      font-weight: 600;
      color: #991b1b;
      margin-bottom: 24px;
      text-align: left;
    }}

    .hero-notice strong {{
      color: #b91c1c;
      font-weight: 850;
    }}

    .hero-stats-row {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
      padding-top: 14px;
      border-top: 1px solid rgba(226, 232, 240, 0.8);
      font-size: 13px;
      color: var(--ink-secondary);
      font-weight: 600;
    }}

    .stat-item {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .stat-item svg {{
      color: var(--blue);
    }}

    /* =========================================================
       4. Filter & Live Search Toolbar
       ========================================================= */
    .portal-toolbar {{
      max-width: 1280px;
      margin: 32px auto 0;
      padding: 0 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .toolbar-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .search-box-wrap {{
      position: relative;
      flex: 1;
      min-width: 280px;
      max-width: 480px;
    }}

    .search-input {{
      width: 100%;
      height: 44px;
      padding: 0 40px 0 42px;
      border-radius: var(--radius-md);
      border: 1.5px solid var(--line);
      background: #fff;
      font-size: 14px;
      font-family: inherit;
      color: var(--ink);
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--blue);
      box-shadow: 0 0 0 3px rgba(37,99,235,0.15);
    }}

    .search-icon-left {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--muted);
      pointer-events: none;
    }}

    .search-clear-btn {{
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      background: #e2e8f0;
      border: 0;
      border-radius: 50%;
      width: 20px;
      height: 20px;
      display: none;
      place-items: center;
      font-size: 12px;
      cursor: pointer;
      color: var(--ink-secondary);
    }}

    .filter-pills {{
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
    }}

    .filter-btn {{
      padding: 8px 14px;
      border-radius: var(--radius-full);
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 650;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}

    .filter-btn:hover {{
      background: #f1f5f9;
      border-color: #cbd5e1;
    }}

    .filter-btn.active {{
      background: var(--ink-dark);
      color: #fff;
      border-color: var(--ink-dark);
      box-shadow: 0 2px 6px rgba(15,23,42,0.25);
    }}

    .search-result-stats {{
      font-size: 13px;
      font-weight: 650;
      color: var(--muted);
      padding: 0 4px;
    }}

    /* =========================================================
       5. Manuals Cards Grid
       ========================================================= */
    .portal-grid {{
      max-width: 1280px;
      margin: 16px auto 60px;
      padding: 0 24px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}

    .manual-card {{
      background: var(--card-bg);
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-md);
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}

    .manual-card:hover {{
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
      border-color: #93c5fd;
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
    }}

    .card-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 750;
      border: 1px solid transparent;
    }}

    .card-steps-count {{
      font-size: 12px;
      font-weight: 650;
      color: var(--muted);
    }}

    .card-title {{
      font-size: 18.5px;
      font-weight: 850;
      line-height: 1.35;
      color: var(--ink-dark);
      margin-bottom: 8px;
      letter-spacing: -0.02em;
    }}

    .card-number {{
      color: #94a3b8;
      font-size: 14px;
      margin-right: 6px;
      font-weight: 700;
    }}

    .card-lead {{
      font-size: 13.5px;
      color: var(--muted);
      line-height: 1.55;
      margin-bottom: 18px;
      flex: 1;
    }}

    .card-steps-preview {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 20px;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      border: 1px solid var(--line-light);
    }}

    .step-chip {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--ink-secondary);
      font-weight: 600;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .step-chip.more {{
      color: var(--blue);
      font-weight: 700;
      font-size: 11.5px;
      padding-top: 2px;
    }}

    .step-idx {{
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #e2e8f0;
      color: var(--ink-secondary);
      font-size: 10.5px;
      font-weight: 800;
      display: grid;
      place-items: center;
      flex-shrink: 0;
    }}

    .card-actions {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: auto;
    }}

    .btn-read {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 16px;
      background: var(--blue);
      color: #fff;
      border-radius: var(--radius-sm);
      font-size: 13.5px;
      font-weight: 750;
      text-decoration: none;
      box-shadow: 0 2px 6px rgba(37,99,235,0.22);
      transition: all 0.18s ease;
    }}

    .btn-read:hover {{
      background: var(--blue-dark);
      transform: translateY(-1px);
    }}

    .btn-group-sub {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    .btn-sub {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      padding: 7px 10px;
      background: #fff;
      color: var(--ink-secondary);
      border: 1px solid var(--line);
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 650;
      text-decoration: none;
      transition: all 0.15s ease;
    }}

    .btn-sub:hover {{
      background: var(--blue-soft);
      color: var(--blue-dark);
      border-color: var(--blue-border);
    }}

    .btn-canva:hover {{
      background: #fdf2f8;
      color: #be185d;
      border-color: #fbcfe8;
    }}

    /* =========================================================
       6. Reader View (Single Page Integrated Viewer)
       ========================================================= */
    #reader-view {{
      display: none;
      min-height: calc(100vh - 70px);
      background: #f5f7fb;
    }}

    .reader-toolbar {{
      position: sticky;
      top: 67px;
      z-index: 40;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--line);
      box-shadow: var(--shadow-sm);
    }}

    .reader-toolbar-inner {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 10px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .toolbar-left, .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn-back-home {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: #fff;
      border: 1px solid var(--line);
      color: var(--ink-dark);
      font-size: 13px;
      font-weight: 750;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
    }}

    .btn-back-home:hover {{
      background: #f1f5f9;
      border-color: #cbd5e1;
    }}

    .manual-select {{
      height: 36px;
      padding: 0 12px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--line);
      font-size: 13px;
      font-weight: 650;
      color: var(--ink);
      background: #fff;
      cursor: pointer;
      max-width: 320px;
    }}

    .reader-content-wrap {{
      max-width: 1180px;
      margin: 24px auto 60px;
      padding: 0 20px;
    }}

    .manual-pane {{
      display: none;
    }}

    .manual-pane.active {{
      display: block;
      animation: fadeIn 0.25s ease forwards;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* =========================================================
       7. Original Manuals Inner Styles Compatibility
       ========================================================= */
    .page {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 32px 36px;
      background: #fff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--line);
      box-shadow: var(--shadow-md);
      min-height: auto;
    }}

    header {{
      border-bottom: 2px solid var(--ink);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}

    .title-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
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

    .source-button {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 9px 15px;
      border-radius: var(--radius-sm);
      background: #2563eb;
      color: #fff;
      text-decoration: none;
      font-size: 13px;
      font-weight: 750;
      white-space: nowrap;
      box-shadow: 0 3px 8px rgba(37,99,235,0.18);
      transition: background 0.15s;
    }}

    .source-button:hover {{
      background: #1d4ed8;
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

    .step h2, .panel h2 {{
      font-size: 17.5px;
      line-height: 1.3;
      margin: 0;
      font-weight: 800;
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

    .img-toggle {{
      position: absolute;
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
      display: grid;
      place-items: center;
      border: 1px solid #93c5fd;
      border-radius: 50%;
      padding: 0;
      background: #fff;
      color: var(--blue-dark);
      font-size: 18px;
      line-height: 1;
      cursor: pointer;
      transition: all 0.15s ease;
      z-index: 2;
    }}

    .img-toggle:hover {{
      background: var(--blue-soft);
      transform: scale(1.08);
      border-color: var(--blue);
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
      margin: 4px 0;
      font-size: 13.5px;
      color: var(--green);
      font-weight: 650;
    }}

    .check {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-top: 12px;
    }}

    .check div {{
      background: #ffffff;
      border: 1px solid #a7f3d0;
      border-radius: var(--radius-sm);
      padding: 10px;
      font-size: 12.5px;
      font-weight: 650;
      text-align: center;
      color: var(--green);
    }}

    .foot {{
      margin-top: 20px;
      padding-top: 14px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 12.5px;
      display: flex;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }}

    /* =========================================================
       8. Universal High-Res Image Modal
       ========================================================= */
    .modal[hidden] {{
      display: none !important;
    }}

    .modal {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      display: grid;
      place-items: center;
      padding: 24px;
      animation: modalFadeIn 0.2s ease;
    }}

    @keyframes modalFadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    .modal-card {{
      position: relative;
      width: min(94vw, 1150px);
      max-height: 92vh;
      background: #fff;
      border-radius: var(--radius-lg);
      box-shadow: 0 25px 60px -15px rgba(0,0,0,0.5);
      padding: 16px;
      overflow: auto;
    }}

    .modal-card img {{
      display: block;
      width: 100%;
      height: auto;
      max-height: calc(92vh - 64px);
      object-fit: contain;
      background: #fff;
      border-radius: var(--radius-sm);
    }}

    .modal-gallery {{
      display: grid;
      gap: 18px;
    }}

    .modal-close {{
      position: absolute;
      right: 18px;
      top: 18px;
      width: 38px;
      height: 38px;
      border: 0;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.85);
      color: #fff;
      font-size: 24px;
      line-height: 1;
      cursor: pointer;
      z-index: 10;
      display: grid;
      place-items: center;
      transition: background 0.15s;
    }}

    .modal-close:hover {{
      background: #0f172a;
    }}

    .modal-open {{
      overflow: hidden !important;
    }}

    /* =========================================================
       9. Deployment Guide Modal
       ========================================================= */
    .deploy-modal-card {{
      max-width: 680px;
      width: 90vw;
      background: #fff;
      border-radius: var(--radius-lg);
      padding: 28px;
      position: relative;
      box-shadow: var(--shadow-xl);
    }}

    .deploy-modal-title {{
      font-size: 22px;
      font-weight: 850;
      color: var(--ink-dark);
      margin-bottom: 8px;
    }}

    .deploy-modal-desc {{
      font-size: 14px;
      color: var(--muted);
      margin-bottom: 20px;
    }}

    .deploy-step-box {{
      background: #f8fafc;
      border: 1px solid var(--line);
      border-radius: var(--radius-md);
      padding: 16px;
      margin-bottom: 14px;
    }}

    .deploy-step-title {{
      font-size: 15px;
      font-weight: 750;
      color: var(--ink-dark);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .deploy-step-content {{
      font-size: 13px;
      color: var(--ink-secondary);
      line-height: 1.55;
    }}

    .code-snippet {{
      display: block;
      background: #0f172a;
      color: #38bdf8;
      font-family: monospace;
      padding: 8px 12px;
      border-radius: 6px;
      margin-top: 6px;
      font-size: 12.5px;
      word-break: break-all;
    }}

    /* =========================================================
       10. Portal Footer
       ========================================================= */
    .portal-footer {{
      margin-top: auto;
      background: #ffffff;
      border-top: 1px solid var(--line);
      padding: 32px 24px;
      font-size: 13px;
      color: var(--muted);
    }}

    .footer-inner {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .footer-links {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .footer-links a {{
      color: var(--muted);
      text-decoration: none;
      font-weight: 600;
    }}

    .footer-links a:hover {{
      color: var(--blue);
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 28px;
      right: 28px;
      background: var(--ink-dark);
      color: #fff;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      font-size: 13.5px;
      font-weight: 650;
      box-shadow: var(--shadow-lg);
      z-index: 2000;
      display: none;
      animation: toastIn 0.2s ease;
    }}

    @keyframes toastIn {{
      from {{ transform: translateY(10px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    /* =========================================================
       11. Responsive & Print Styles
       ========================================================= */
    @media (max-width: 900px) {{
      .page {{ padding: 22px 18px; }}
      .check {{ grid-template-columns: 1fr; }}
      .portal-grid {{ grid-template-columns: 1fr; }}
      .reader-toolbar-inner {{ flex-direction: column; align-items: stretch; }}
      .toolbar-left, .toolbar-right {{ justify-content: space-between; }}
    }}

    @media (max-width: 600px) {{
      .title-row {{ flex-direction: column; align-items: flex-start; }}
      .hero-stats-row {{ flex-direction: column; gap: 8px; }}
      .portal-nav-inner {{ padding: 10px 16px; }}
    }}

    @media print {{
      body {{ background: #fff !important; }}
      .portal-nav, .portal-hero, .portal-toolbar, .portal-grid, .portal-footer, .reader-toolbar, .img-toggle, .modal, .toast {{
        display: none !important;
      }}
      #reader-view {{ display: block !important; }}
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
       Global Top Navigation Bar
       ========================================================= -->
  <nav class="portal-nav" role="navigation" aria-label="메인 내비게이션">
    <div class="portal-nav-inner">
      <a href="#home" class="brand-group" onclick="showHomeView(); return true;">
        <div class="brand-icon">🏫</div>
        <div class="brand-text">
          <span class="brand-title">홍익여고 온라인교무실 업무 포털</span>
          <span class="brand-sub">교원 디지털 업무 가이드북 종합 센터</span>
        </div>
      </a>
      <div class="nav-actions">
        <a href="#home" class="nav-btn" onclick="showHomeView(); return true;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          전체 홈
        </a>
        <button type="button" class="nav-btn" onclick="openDeployModal()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          배포 안내
        </button>
        <button type="button" class="nav-btn nav-btn-primary" onclick="window.print()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          인쇄하기
        </button>
      </div>
    </div>
  </nav>

  <!-- =========================================================
       VIEW 1: Main Portal Grid View (#home)
       ========================================================= -->
  <div id="home-view">
    <!-- Hero Banner -->
    <header class="portal-hero">
      <div class="hero-container">
        <div class="hero-pill">
          <span>✨ 2026학년도 교원 업무 효율화 가이드북</span>
        </div>
        <h1 class="hero-title">온라인교무실 핵심 업무 가이드 포털</h1>
        <p class="hero-desc">
          Chrome 브라우저 기본 환경 설정부터 온라인교무실 바로가기 앱 설치, 메인 페이지 편집, Google NotebookLM AI 활용, 공유 폴더 권한 분리 및 연수서명부 날인까지 7대 필수 가이드를 한 곳에서 확인하세요.
        </p>
        <div class="hero-notice">
          <span>⚠️</span>
          <span><strong>주의:</strong> 모든 절차는 반드시 Chrome에서 교사 개인 학교 계정(<strong>@hongik68.sen.hs.kr</strong>)으로 로그인한 상태에서 진행해 주시기 바랍니다.</span>
        </div>
        <div class="hero-stats-row">
          <div class="stat-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            <span>총 7개 핵심 매뉴얼 수록</span>
          </div>
          <div class="stat-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="9 11 12 14 22 4"></polyline><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
            <span>총 33단계 실무 가이드</span>
          </div>
          <div class="stat-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span>고화질 스크린샷 뷰어 지원</span>
          </div>
          <div class="stat-item">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
            <span>원본 Canva 슬라이드 링크 연동</span>
          </div>
        </div>
      </div>
    </header>

    <!-- Toolbar: Search & Category Filter -->
    <section class="portal-toolbar" aria-label="매뉴얼 검색 및 필터">
      <div class="toolbar-row">
        <!-- Live Search Box -->
        <div class="search-box-wrap">
          <svg class="search-icon-left" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="searchInput" class="search-input" placeholder="키워드 검색 (예: 북마크, 기본앱, NotebookLM, 권한, 서명...)" autocomplete="off">
          <button type="button" id="searchClearBtn" class="search-clear-btn" aria-label="검색어 지우기">✕</button>
        </div>
        <!-- Category Filter Pills -->
        <div class="filter-pills" role="tablist">
          <button type="button" class="filter-btn active" data-filter="all">전체 (7)</button>
          <button type="button" class="filter-btn" data-filter="browser">🌐 브라우저 환경 (2)</button>
          <button type="button" class="filter-btn" data-filter="portal">🏫 온라인교무실 (2)</button>
          <button type="button" class="filter-btn" data-filter="ai-tools">🧠 AI & 도구 (1)</button>
          <button type="button" class="filter-btn" data-filter="security">🔒 보안 & 권한 (1)</button>
          <button type="button" class="filter-btn" data-filter="admin">🖋️ 교무 행정 (1)</button>
        </div>
      </div>
      <div id="searchStats" class="search-result-stats" style="display:none;"></div>
    </section>

    <!-- Manuals Card Grid -->
    <main class="portal-grid" id="manualGrid" aria-label="매뉴얼 카드 목록">
      {''.join(cards_html)}
    </main>
  </div>

  <!-- =========================================================
       VIEW 2: Integrated Manual Reader View (#manual-view)
       ========================================================= -->
  <div id="reader-view">
    <!-- Sticky Reader Toolbar -->
    <div class="reader-toolbar">
      <div class="reader-toolbar-inner">
        <div class="toolbar-left">
          <a href="#home" class="btn-back-home" onclick="showHomeView(); return true;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            ← 전체 목록으로
          </a>
          <select id="readerManualSelect" class="manual-select" aria-label="매뉴얼 바로 이동">
            {''.join(dropdown_options)}
          </select>
        </div>
        <div class="toolbar-right">
          <button type="button" id="btnPrevManual" class="nav-btn" title="이전 매뉴얼 보기">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
            이전
          </button>
          <button type="button" id="btnNextManual" class="nav-btn" title="다음 매뉴얼 보기">
            다음
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
          <button type="button" class="nav-btn" onclick="copyCurrentLink()" title="현재 매뉴얼 직링크 복사">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            링크 복사
          </button>
          <button type="button" class="nav-btn nav-btn-primary" onclick="window.print()" title="현재 매뉴얼 인쇄">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
            인쇄
          </button>
        </div>
      </div>
    </div>

    <!-- Embedded Manual Content Panes -->
    <div class="reader-content-wrap">
      {''.join(panes_html)}
    </div>
  </div>

  <!-- =========================================================
       Global High-Res Image Zoom Modal
       ========================================================= -->
  <div class="modal" id="globalImageModal" role="dialog" aria-modal="true" aria-label="원본 이미지 확대 뷰어" hidden>
    <div class="modal-card">
      <button class="modal-close" type="button" aria-label="닫기">×</button>
      <div class="modal-gallery" id="globalModalGallery"></div>
    </div>
  </div>

  <!-- =========================================================
       Deployment & Publishing Guide Modal
       ========================================================= -->
  <div class="modal" id="deployGuideModal" role="dialog" aria-modal="true" aria-label="웹 배포 가이드" hidden>
    <div class="deploy-modal-card">
      <button class="modal-close" type="button" onclick="closeDeployModal()" aria-label="닫기">×</button>
      <h2 class="deploy-modal-title">🚀 온라인교무실 포털 배포 안내</h2>
      <p class="deploy-modal-desc">
        이 프로젝트는 모든 이미지(base64)와 스타일, 스크립트가 <code>index.html</code> 단일 파일 및 7개 독립 파일로 구성되어 있어 어디서든 외부 서버 없이 즉시 구동 및 배포할 수 있습니다.
      </p>

      <div class="deploy-step-box">
        <div class="deploy-step-title">
          <span>1. GitHub Pages로 무료 호스팅 배포 (추천)</span>
        </div>
        <div class="deploy-step-content">
          GitHub 저장소(Repository)에 이 폴더의 파일들을 push한 후, <strong>Settings → Pages → Source를 'main branch'</strong>로 지정하면 즉시 인터넷 주소(예: <code>https://username.github.io/repo/</code>)가 생성되어 교원들에게 공유할 수 있습니다.
        </div>
      </div>

      <div class="deploy-step-box">
        <div class="deploy-step-title">
          <span>2. Vercel / Cloudflare Pages / Netlify 원클릭 배포</span>
        </div>
        <div class="deploy-step-content">
          이 폴더를 그대로 드래그 앤 드롭하거나 GitHub 연동만 하면 수초 내에 글로벌 CDN으로 초고속 배포됩니다.
        </div>
      </div>

      <div class="deploy-step-box">
        <div class="deploy-step-title">
          <span>3. Google 사이트 온라인교무실 내 삽입 (iFrame)</span>
        </div>
        <div class="deploy-step-content">
          배포된 URL을 온라인교무실 Google Sites에서 [삽입] → [URL 삽입] 메뉴를 통해 바로 교무실 대시보드 화면에 일체형으로 배치할 수 있습니다.
        </div>
      </div>

      <div class="deploy-step-box">
        <div class="deploy-step-title">
          <span>4. 오프라인 로컬 / 학교 내부망 이용</span>
        </div>
        <div class="deploy-step-content">
          외부 인터넷 연결 없이도 <code>index.html</code> 파일을 더블클릭하면 모든 스크린샷과 가이드가 100% 정상 작동합니다.
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast" class="toast">링크가 클립보드에 복사되었습니다!</div>

  <!-- =========================================================
       Global Footer
       ========================================================= -->
  <footer class="portal-footer">
    <div class="footer-inner">
      <div>
        <strong>홍익여자고등학교 온라인교무실</strong> · 교원 디지털 업무 지원 가이드북 종합 포털
      </div>
      <div class="footer-links">
        <a href="#home" onclick="showHomeView()">전체 목록</a>
        <a href="https://www.canva.com" target="_blank" rel="noopener">Canva 원본</a>
        <a href="javascript:void(0)" onclick="openDeployModal()">배포 방법 안내</a>
      </div>
    </div>
  </footer>

  <!-- =========================================================
       Application Script (Routing, Search, Modal, Navigation)
       ========================================================= -->
  <script>
    const MANUAL_LIST = {json.dumps([{"id": m["id"], "title": m["title"], "file": m["file"], "canva": m["canva"]} for m in MANUALS], ensure_ascii=False)};
    
    const homeView = document.getElementById('home-view');
    const readerView = document.getElementById('reader-view');
    const readerSelect = document.getElementById('readerManualSelect');
    const searchInput = document.getElementById('searchInput');
    const searchClearBtn = document.getElementById('searchClearBtn');
    const searchStats = document.getElementById('searchStats');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const manualCards = document.querySelectorAll('.manual-card');
    const btnPrev = document.getElementById('btnPrevManual');
    const btnNext = document.getElementById('btnNextManual');
    
    // Global Modal elements
    const modal = document.getElementById('globalImageModal');
    const modalGallery = document.getElementById('globalModalGallery');
    const modalCloseBtn = modal.querySelector('.modal-close');
    const deployModal = document.getElementById('deployGuideModal');
    const toast = document.getElementById('toast');

    let currentManualId = null;

    // Toast Notification helper
    function showToast(msg) {{
      toast.textContent = msg;
      toast.style.display = 'block';
      setTimeout(() => {{ toast.style.display = 'none'; }}, 2400);
    }}

    // Routing Logic
    function handleRouting() {{
      const hash = window.location.hash.replace(/^#/, '').trim();
      const validManual = MANUAL_LIST.find(m => m.id === hash);
      
      if (validManual) {{
        openManual(validManual.id, false);
      }} else {{
        showHomeView(false);
      }}
    }}

    window.addEventListener('hashchange', handleRouting);
    window.addEventListener('DOMContentLoaded', handleRouting);

    function showHomeView(updateHash = true) {{
      homeView.style.display = 'block';
      readerView.style.display = 'none';
      currentManualId = null;
      document.title = "홍익여고 온라인교무실 업무 매뉴얼 포털 | 7대 핵심 가이드북";
      if (updateHash) {{
        history.pushState(null, '', '#home');
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function openManual(id, updateHash = true) {{
      const manual = MANUAL_LIST.find(m => m.id === id);
      if (!manual) return;

      currentManualId = id;
      homeView.style.display = 'none';
      readerView.style.display = 'block';

      // Hide all panes, show active
      document.querySelectorAll('.manual-pane').forEach(p => p.classList.remove('active'));
      const activePane = document.getElementById('pane-' + id);
      if (activePane) {{
        activePane.classList.add('active');
      }}

      // Update dropdown selector
      readerSelect.value = id;

      // Update doc title
      document.title = manual.title + " | 온라인교무실 매뉴얼 포털";

      // Update Prev / Next button states
      const currIdx = MANUAL_LIST.findIndex(m => m.id === id);
      btnPrev.disabled = currIdx <= 0;
      btnNext.disabled = currIdx >= MANUAL_LIST.length - 1;
      btnPrev.style.opacity = currIdx <= 0 ? '0.45' : '1';
      btnNext.style.opacity = currIdx >= MANUAL_LIST.length - 1 ? '0.45' : '1';

      if (updateHash) {{
        history.pushState(null, '', '#' + id);
      }}
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Reader Toolbar Events
    readerSelect.addEventListener('change', (e) => {{
      openManual(e.target.value);
    }});

    btnPrev.addEventListener('click', () => {{
      const currIdx = MANUAL_LIST.findIndex(m => m.id === currentManualId);
      if (currIdx > 0) {{
        openManual(MANUAL_LIST[currIdx - 1].id);
      }}
    }});

    btnNext.addEventListener('click', () => {{
      const currIdx = MANUAL_LIST.findIndex(m => m.id === currentManualId);
      if (currIdx < MANUAL_LIST.length - 1) {{
        openManual(MANUAL_LIST[currIdx + 1].id);
      }}
    }});

    function copyCurrentLink() {{
      const url = window.location.href;
      if (navigator.clipboard) {{
        navigator.clipboard.writeText(url).then(() => {{
          showToast("현재 매뉴얼 링크가 복사되었습니다!");
        }});
      }} else {{
        showToast("URL: " + url);
      }}
    }}

    // Live Search & Filter Logic
    let currentFilter = 'all';

    function filterCards() {{
      const query = searchInput.value.trim().toLowerCase();
      let visibleCount = 0;

      manualCards.forEach(card => {{
        const category = card.dataset.category;
        const searchData = card.dataset.search;

        const matchesFilter = (currentFilter === 'all' || category === currentFilter);
        const matchesQuery = !query || searchData.includes(query);

        if (matchesFilter && matchesQuery) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      if (query) {{
        searchStats.style.display = 'block';
        searchStats.textContent = `검색 결과: ${{visibleCount}}개 매뉴얼 일치`;
        searchClearBtn.style.display = 'grid';
      }} else {{
        searchStats.style.display = 'none';
        searchClearBtn.style.display = 'none';
      }}
    }}

    searchInput.addEventListener('input', filterCards);

    searchClearBtn.addEventListener('click', () => {{
      searchInput.value = '';
      filterCards();
      searchInput.focus();
    }});

    filterBtns.forEach(btn => {{
      btn.addEventListener('click', () => {{
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        filterCards();
      }});
    }});

    // Hotkey '/' to focus search
    window.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput && homeView.style.display !== 'none') {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Universal High-Res Image Modal Logic
    function closeModal() {{
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      modalGallery.innerHTML = '';
    }}

    modalCloseBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) closeModal();
    }});

    // Attach click listeners to all .img-toggle buttons
    document.querySelectorAll('.img-toggle').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
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

        if (!urls.length) return;

        modalGallery.innerHTML = urls.map((u, i) => `
          <img src="${{u}}" alt="${{btn.dataset.alt || '원본 안내 이미지'}} ${{i + 1}}">
        `).join('');

        modal.hidden = false;
        document.body.classList.add('modal-open');
        modalCloseBtn.focus();
      }});
    }});

    // Deployment Guide Modal Logic
    function openDeployModal() {{
      deployModal.hidden = false;
      document.body.classList.add('modal-open');
    }}

    function closeDeployModal() {{
      deployModal.hidden = true;
      document.body.classList.remove('modal-open');
    }}

    deployModal.addEventListener('click', (e) => {{
      if (e.target === deployModal) closeDeployModal();
    }});

    // ESC key closes any open modal
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        if (!modal.hidden) closeModal();
        if (!deployModal.hidden) closeDeployModal();
      }}
    }});
  </script>
</body>
</html>
"""

# Write to c:\Users\user\Desktop\aside\Outputs\index.html
output_path = r"c:\Users\user\Desktop\aside\Outputs\index.html"
with open(output_path, "w", encoding="utf-8") as fp:
    fp.write(index_html)

print("Generated index.html successfully at:", output_path)
print("File size:", round(os.path.getsize(output_path) / 1024 / 1024, 2), "MB")

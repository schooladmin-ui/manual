import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(BASE_DIR, "pages")

MANUALS = [
    {
        "id": "chrome-default",
        "file": "chrome-default-app-guide-with-canva-link.html",
        "short_title": "크롬 기본 앱 설정",
        "full_title": "크롬브라우저 기본앱으로 설정하는 방법",
        "steps_count": 3,
        "canva": "https://www.canva.com/design/DAGotK1iBWQ/fQ9N3piaD0zZCDtNWv6vCw/view?utm_content=DAGotK1iBWQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h39e2295cc7"
    },
    {
        "id": "bookmark-bar",
        "file": "bookmark-bar-manual-with-canva-link.html",
        "short_title": "크롬 북마크바 표시",
        "full_title": "크롬 북마크바 표시 방법",
        "steps_count": 3,
        "canva": "https://www.canva.com/design/DAGoE56L5Qw/zEwEBK0UluCzBb1HR838Cg/view?utm_content=DAGoE56L5Qw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7dc1509390"
    },
    {
        "id": "desktop-button",
        "file": "desktop-button-guide-manual.html",
        "short_title": "바탕화면 바로가기",
        "full_title": "바탕화면에 온라인교무실 바로가기 버튼 만들기",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAHGJQe8CAA/kYI9m7jIEDhPaAbkuLZDGg/view?utm_content=DAHGJQe8CAA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=ha7f0287432"
    },
    {
        "id": "main-page-edit",
        "file": "main-page-edit-guide-manual.html",
        "short_title": "메인 페이지 편집",
        "full_title": "메인 페이지 편집 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAGm6pqOZJM/rQnX-rH46Qv1cxtFaN2xhg/view?utm_content=DAGm6pqOZJM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h48af137ff0"
    },
    {
        "id": "notebooklm",
        "file": "notebooklm-create-share-guide-manual.html",
        "short_title": "구글 NotebookLM",
        "full_title": "구글 Notebook LM 생성 후 공유 방법",
        "steps_count": 11,
        "canva": "https://www.canva.com/design/DAHIAXtwfPQ/c0rlZicbmWImDTlLa5JJkQ/view?utm_content=DAHIAXtwfPQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h7c5f276f63"
    },
    {
        "id": "permission-setting",
        "file": "permission-setting-guide-with-canva-link.html",
        "short_title": "공유 폴더 권한",
        "full_title": "온라인교무실 공유 폴더 권한 설정 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAGm6gX_4lM/rVOmpsykESZmuqzTnOMz8A/view?utm_content=DAGm6gX_4lM&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=hb1133ff80a"
    },
    {
        "id": "training-signature",
        "file": "training-signature-guide-manual.html",
        "short_title": "연수서명부 서명",
        "full_title": "연수서명부 서명 방법",
        "steps_count": 4,
        "canva": "https://www.canva.com/design/DAGm6jijC7A/i3ovxr1djLZxKIW9JRvAKg/view?utm_content=DAGm6jijC7A&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utm_id=h1e3a1fe2c0"
    },
    {
        "id": "google-chat",
        "file": "google-chat-space-guide.html",
        "short_title": "구글 채팅방(스페이스) 생성",
        "full_title": "구글 채팅(Google Chat) 앱에서 채팅방(스페이스) 만드는 방법",
        "steps_count": 4,
        "canva": ""
    },
    {
        "id": "google-groups",
        "file": "google-groups-create-guide.html",
        "short_title": "그룹 만들기",
        "full_title": "그룹 만들기",
        "steps_count": 2,
        "canva": ""
    },
    {
        "id": "manual-우리-학교--이제-구글-채팅-google-chat-으로-pdf-guide",
        "file": "우리 학교, 이제 구글 채팅(Google Chat)으로-pdf-guide.html",
        "short_title": "구글 채팅(Google Chat) 설치 방법",
        "full_title": "구글 채팅(Google Chat) 설치 방법",
        "steps_count": 1,
        "canva": ""
    }
]

def update_title_row(content, canva_url, file_url):
    def repl(m_row):
        inner = m_row.group(1)
        h1_m = re.search(r'(<h1[^>]*>.*?</h1>)', inner, re.DOTALL)
        if not h1_m:
            return m_row.group(0)
        h1_html = h1_m.group(1)
        canva_btn = f'\n  <a class="source-button" href="{canva_url}" target="_blank" rel="noopener">원본 Canva 슬라이드 열기</a>' if canva_url else ''
        actions = f'''<div class="title-actions">{canva_btn}
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
        
        # Place Canva button and 독립창 열기 button side-by-side in title-row
        content = update_title_row(content, m["canva"], f"pages/{m['file']}")
        content = content.replace('href="google-groups-create-guide.html"', 'href="#google-groups"')
            
        # Clean up any modal-close button that might have been copied inside page content
        content = re.sub(r'<button class="modal-close"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    else:
        content = "<div>매뉴얼 내용을 불러올 수 없습니다.</div>"
    
    manual_contents[m["id"]] = content

# 1x7 Buttons - WITHOUT numbers, clean titles & step badges
buttons_html = []
for m in MANUALS:
    btn = f"""
    <a href="#{m['id']}" class="manual-nav-btn" data-id="{m['id']}" draggable="true" onclick="selectManual('{m['id']}'); event.preventDefault();">
      <span class="nav-btn-title">{m['short_title']}</span>
      <span class="nav-btn-steps">{m['steps_count']}단계</span>
    </a>
    """
    buttons_html.append(btn)

# Manual content panes - NO duplicate pane-top-bar panel! Clean and direct.
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
      gap: 10px;
    }}

    .btn-header-print {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: #fff;
      border: 1px solid var(--line);
      color: var(--ink-secondary);
      font-size: 13px;
      font-weight: 650;
      cursor: pointer;
      transition: all 0.15s ease;
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
       3. 1x7 Manual Button Navigation Bar (No HTML Numbers)
       ========================================================= */
    .nav-bar-section {{
      background: #ffffff;
      border-bottom: 2px solid var(--line);
      padding: 14px 20px;
      box-shadow: var(--shadow-sm);
      position: static;
      top: 71px;
      z-index: 40;
    }}

    .nav-bar-container {{
      max-width: 1280px;
      margin: 0 auto;
    }}

    .manual-nav-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 10px;
    }}

    .manual-nav-btn {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 14px 10px;
      border-radius: var(--radius-md);
      background: #f8fafc;
      border: 1.5px solid var(--line);
      color: var(--ink-secondary);
      text-decoration: none;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      text-align: center;
      min-height: 66px;
      position: relative;
    }}

    .manual-nav-btn:hover {{
      background: #ffffff;
      border-color: var(--blue);
      color: var(--blue-dark);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}

    .manual-nav-btn.active {{
      background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
      border-color: #1d4ed8;
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(37,99,235,0.32);
      transform: translateY(-1px);
    }}

    .nav-btn-title {{
      font-size: 14px;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.02em;
      word-break: keep-all;
    }}

    .nav-btn-steps {{
      font-size: 11.5px;
      font-weight: 600;
      color: var(--muted);
      margin-top: 4px;
    }}

    .manual-nav-btn.active .nav-btn-steps {{
      color: rgba(255, 255, 255, 0.9);
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
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 10px;
      border-radius: var(--radius-md);
      background: #f8fafc;
      border: 2px dashed #93c5fd;
      color: var(--blue);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      min-height: 66px;
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
      font-size: 22px;
      font-weight: 900;
      line-height: 1;
    }}

    .add-btn-label {{
      font-size: 12px;
      font-weight: 750;
      margin-top: 3px;
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
      width: min(94vw, 540px);
      padding: 24px;
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
    .form-group input[type="url"] {{
      width: 100%;
      padding: 10px 12px;
      border: 1.5px solid var(--line);
      border-radius: var(--radius-sm);
      font-size: 14px;
      font-family: inherit;
      color: var(--ink);
      outline: none;
      transition: border-color 0.15s;
    }}

    .form-group input:focus {{
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
      background: #2563eb;
      color: #ffffff !important;
      text-decoration: none;
      font-size: 13.5px;
      font-weight: 750;
      white-space: nowrap;
      box-shadow: 0 3px 8px rgba(37,99,235,0.22);
      transition: all 0.18s ease;
      cursor: pointer;
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
      padding-right: 48px; /* space for img-toggle button */
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
    }}

    .pdf-embed-wrap {{
      margin: 14px 0 6px;
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
      min-height: 760px;
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
       7. High-Res Image Modal (With Canva Button)
       ========================================================= */
    .modal[hidden] {{
      display: none !important;
    }}

    .modal {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      display: grid;
      place-items: center;
      padding: 24px;
    }}

    .modal-card {{
      position: relative;
      width: min(94vw, 1150px);
      max-height: 94vh;
      background: #fff;
      border-radius: var(--radius-lg);
      box-shadow: 0 25px 60px -15px rgba(0,0,0,0.5);
      padding: 20px;
      overflow: auto;
    }}

    .modal-header-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--line);
    }}

    .modal-card img {{
      display: block;
      width: 100%;
      height: auto;
      max-height: calc(92vh - 120px);
      object-fit: contain;
      background: #fff;
      border-radius: var(--radius-sm);
    }}

    .modal-gallery {{
      display: grid;
      gap: 18px;
    }}

    .modal-close {{
      width: 36px;
      height: 36px;
      border: 0;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.85);
      color: #fff;
      font-size: 22px;
      line-height: 1;
      cursor: pointer;
      display: grid;
      place-items: center;
      transition: background 0.15s;
      flex-shrink: 0;
    }}

    .modal-close:hover {{
      background: #0f172a;
    }}

    .modal-open {{
      overflow: hidden !important;
    }}

    /* =========================================================
       8. Footer & Responsive / Print
       ========================================================= */
    .simple-footer {{
      margin-top: auto;
      background: #ffffff;
      border-top: 1px solid var(--line);
      padding: 20px 24px;
      text-align: center;
      font-size: 13px;
      color: var(--muted);
    }}

    @media (max-width: 900px) {{
      .page {{ padding: 22px 18px; }}
      .check {{ grid-template-columns: 1fr; }}
      .two-col-sections, .step-with-side {{ grid-template-columns: 1fr; }}
      .two-col-sections .section {{ margin-top: 24px; }}
      .manual-nav-grid {{
        grid-template-columns: repeat(2, 1fr);
        overflow-x: auto;
        padding-bottom: 6px;
      }}
      .nav-bar-section {{
        padding: 10px 14px;
      }}
    }}

    @media print {{
      body {{ background: #fff !important; }}
      .simple-header, .nav-bar-section, .simple-footer, .img-toggle, .modal, .source-button, .pane-standalone-link {{
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
       1x7 Manual Button Navigation Bar (No HTML Numbers)
       ========================================================= -->
  <nav class="nav-bar-section" aria-label="매뉴얼 선택 바">
    <div class="nav-bar-container">
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
       High-Res Image Modal (With Canva Open Button)
       ========================================================= -->
  <div class="modal" id="globalImageModal" role="dialog" aria-modal="true" aria-label="원본 이미지 확대 뷰어" hidden>
    <div class="modal-card">
      <div class="modal-header-bar">
        <a id="modalCanvaBtn" class="source-button" href="#" target="_blank" rel="noopener">
          원본 Canva 슬라이드 열기
        </a>
        <button class="modal-close" type="button" aria-label="닫기">×</button>
      </div>
      <div class="modal-gallery" id="globalModalGallery"></div>
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
          <label for="manualCanvaUrl">4. 원본 Canva 슬라이드 링크 (선택)</label>
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
       Navigation, Modal & Dynamic Manual Upload Script
       ========================================================= -->
  <script id="mainPortalScript">
    const MANUAL_LIST = {json.dumps([{"id": m["id"], "title": m["short_title"], "canva": m["canva"]} for m in MANUALS], ensure_ascii=False)};
    
    const modal = document.getElementById('globalImageModal');
    const modalGallery = document.getElementById('globalModalGallery');
    const modalCloseBtn = modal.querySelector('.modal-close');
    const modalCanvaBtn = document.getElementById('modalCanvaBtn');
    const addModal = document.getElementById('addManualModal');
    const deployDownloadBtn = document.getElementById('btnHeaderDeployDownload');

    let currentManualId = MANUAL_LIST[0].id;
    const BUILTIN_IDS = new Set(MANUAL_LIST.map(m => m.id));
    let uploadedRawHtml = '';
    let uploadedFileName = '';
    let uploadedFileType = ''; // 'html' | 'pdf' | 'image'
    let uploadedDataUrls = [];
    const customManualsStore = [];
    let hasOrderChanged = false;

    function updateDeployButtonVisibility() {{
      if (!deployDownloadBtn) return;
      deployDownloadBtn.hidden = (customManualsStore.length === 0 && !hasOrderChanged);
    }}

    function hydratePdfFrames(root = document) {{
      root.querySelectorAll('iframe.pdf-embed-frame[data-pdf-src]').forEach(frame => {{
        if (frame.dataset.hydrated === '1') return;
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

    function bindImageToggles(root = document) {{
      root.querySelectorAll('.img-toggle').forEach(btn => {{
        if (btn.dataset.bound === '1') return;
        btn.dataset.bound = '1';
        btn.addEventListener('click', (e) => {{
          e.stopPropagation();
          const pane = btn.closest('.manual-pane');
          const canvaUrl = (pane && pane.dataset.canva) ? pane.dataset.canva : (MANUAL_LIST.find(m => m.id === currentManualId)?.canva || '');
          if (modalCanvaBtn) {{
            modalCanvaBtn.href = canvaUrl || '#';
            modalCanvaBtn.style.visibility = canvaUrl ? 'visible' : 'hidden';
          }}

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
    }}

    bindImageToggles(document);

    // Add Manual Modal Logic
    function openAddManualModal() {{
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
      const canvaBtn = canvaUrl ? `<a class="source-button" href="${{canvaUrl}}" target="_blank" rel="noopener">원본 Canva 슬라이드 열기</a>` : '';
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
          const copy = {{ id: item.id, title: item.title, stepsCount: item.stepsCount, canva: item.canva, contentHtml: item.contentHtml, rawHtml: item.rawHtml, fileName: item.fileName }};
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
          actionsDiv.innerHTML += `<a class="source-button" href="${{canvaUrl}}" target="_blank" rel="noopener">원본 Canva 슬라이드 열기</a>`;
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
      MANUAL_LIST.push({{ id: item.id, title: item.title, canva: item.canva || '', isCustom: true }});

      const navGrid = document.getElementById('manualNavGrid');
      const addBtn = document.getElementById('openAddManualBtn');
      const btn = document.createElement('a');
      btn.href = '#' + item.id;
      btn.className = 'manual-nav-btn';
      btn.dataset.id = item.id;
      btn.dataset.custom = '1';
      btn.draggable = true;
      btn.onclick = (e) => {{
        e.preventDefault();
        selectManual(item.id);
      }};
      btn.innerHTML = `
        <button type="button" class="nav-btn-del" title="이 매뉴얼 삭제" onclick="removeCustomManual(event, '${{item.id}}')">×</button>
        <span class="nav-btn-title">${{item.title}}</span>
        <span class="nav-btn-steps">${{item.stepsCount}}단계</span>
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
      updateDeployButtonVisibility();
      if (currentManualId === id) {{
        selectManual(MANUAL_LIST[0].id);
      }}
    }}

    async function registerCurrentFormManual() {{
      if (!uploadedRawHtml) return null;
      const title = document.getElementById('manualShortTitle').value.trim() || uploadedFileName.replace(/\\.html?$/i, '');
      const stepsCount = parseInt(document.getElementById('manualStepsCount').value, 10) || 1;
      const canva = document.getElementById('manualCanvaUrl').value.trim();
      const slugBase = (uploadedFileName || title).replace(/\\.html?$/i, '').replace(/[^a-zA-Z0-9가-힣_-]/g, '-').toLowerCase();
      const id = 'manual-' + (slugBase || Date.now());
      const safeFileName = uploadedFileName || (id + '.html');

      let finalRawHtml = uploadedRawHtml;
      if (uploadedFileType === 'pdf' || uploadedFileType === 'image') {{
        finalRawHtml = buildStandaloneHtmlFromPdfOrImage(title, uploadedFileType, uploadedDataUrls, canva);
      }}

      const contentHtml = buildPaneHtmlFromRaw(finalRawHtml, canva, safeFileName);
      const item = {{ id, title, stepsCount, canva, contentHtml, rawHtml: finalRawHtml, fileName: safeFileName }};

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
        selectManual(item.id);
      }}
    }}

    function buildUpdatedIndexHtmlString() {{
      const clone = document.documentElement.cloneNode(true);
      clone.querySelector('#globalImageModal')?.setAttribute('hidden', '');
      clone.querySelector('#addManualModal')?.setAttribute('hidden', '');
      clone.querySelector('#btnHeaderDeployDownload')?.setAttribute('hidden', '');
      clone.querySelector('body')?.classList.remove('modal-open');
      clone.querySelectorAll('.nav-btn-del').forEach(el => el.remove());
      clone.querySelectorAll('.manual-nav-btn').forEach(el => el.removeAttribute('data-custom'));
      clone.querySelectorAll('.pane-standalone-link').forEach(el => el.removeAttribute('data-blob-url'));
      clone.querySelectorAll('.img-toggle').forEach(el => el.removeAttribute('data-bound'));
      clone.querySelectorAll('iframe.pdf-embed-frame[data-pdf-src]').forEach(frame => {{
        frame.removeAttribute('data-hydrated');
        frame.setAttribute('src', frame.getAttribute('data-pdf-src'));
      }});
      const scriptEl = clone.querySelector('#mainPortalScript');
      if (scriptEl) {{
        const cleanList = MANUAL_LIST.map(m => ({{ id: m.id, title: m.title, canva: m.canva || '' }}));
        scriptEl.textContent = scriptEl.textContent.replace(
          /const MANUAL_LIST = \\[.*?\\];/,
          'const MANUAL_LIST = ' + JSON.stringify(cleanList) + ';'
        );
      }}
      return '<!doctype html>\\n' + clone.outerHTML;
    }}

    function downloadAllDeploymentFiles() {{
      // Synchronously prepare all Blob URLs BEFORE triggering any download so user activation stays active
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
      if (deployDownloadBtn) deployDownloadBtn.hidden = true;
    }}

    // Drag and Drop Reordering for Manual Navigation Buttons
    const ORDER_STORAGE_KEY = 'online_office_manual_nav_order';
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
        draggedBtn = null;
      }});
    }}

    initNavDragAndDrop();
    handleHash();
    window.addEventListener('DOMContentLoaded', async () => {{
      const saved = await loadCustomManualsFromDB();
      saved.forEach(item => renderCustomManual(item));
      applySavedManualOrder();
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

print("Generated clean index.html with single Canva button and side-by-side 독립창 열기 button.")
print("File size:", round(os.path.getsize(index_path) / 1024 / 1024, 2), "MB")

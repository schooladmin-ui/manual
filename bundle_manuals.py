import os
import json
import re

BASE_DIR = r"c:\Users\user\Desktop\aside\Outputs"

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
    }
]

def update_title_row(content, canva_url, file_url):
    def repl(m_row):
        inner = m_row.group(1)
        h1_m = re.search(r'(<h1[^>]*>.*?</h1>)', inner, re.DOTALL)
        if not h1_m:
            return m_row.group(0)
        h1_html = h1_m.group(1)
        actions = f'''<div class="title-actions">
  <a class="source-button" href="{canva_url}" target="_blank" rel="noopener">원본 Canva 슬라이드 열기</a>
  <a href="{file_url}" target="_blank" rel="noopener" class="pane-standalone-link" title="새 창에서 독립 파일로 열기">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
    독립창 열기
  </a>
</div>'''
        return f'<div class="title-row">{h1_html}{actions}</div>'
    
    return re.sub(r'<div class="title-row">(.*?)</div>', repl, content, count=1, flags=re.DOTALL)

manual_contents = {}
for m in MANUALS:
    fpath = os.path.join(BASE_DIR, m["file"])
    with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
        raw = fp.read()
    
    main_match = re.search(r'<main class="page">(.*?)</main>', raw, re.DOTALL)
    if main_match:
        content = main_match.group(1).strip()
        
        # Place Canva button and 독립창 열기 button side-by-side in title-row
        content = update_title_row(content, m["canva"], m["file"])
            
        # Clean up any modal-close button that might have been copied inside page content
        content = re.sub(r'<button class="modal-close"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    else:
        content = "<div>매뉴얼 내용을 불러올 수 없습니다.</div>"
    
    manual_contents[m["id"]] = content

# 1x7 Buttons - WITHOUT numbers, clean titles & step badges
buttons_html = []
for m in MANUALS:
    btn = f"""
    <a href="#{m['id']}" class="manual-nav-btn" data-id="{m['id']}" onclick="selectManual('{m['id']}'); event.preventDefault();">
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
      position: sticky;
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

    /* =========================================================
       3. 1x7 Manual Button Navigation Bar (No HTML Numbers)
       ========================================================= */
    .nav-bar-section {{
      background: #ffffff;
      border-bottom: 2px solid var(--line);
      padding: 14px 20px;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 71px;
      z-index: 40;
    }}

    .nav-bar-container {{
      max-width: 1280px;
      margin: 0 auto;
    }}

    .manual-nav-grid {{
      display: grid;
      grid-template-columns: repeat(7, 1fr);
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
      .manual-nav-grid {{
        grid-template-columns: repeat(7, minmax(130px, 1fr));
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
      <div class="manual-nav-grid">
        {''.join(buttons_html)}
      </div>
    </div>
  </nav>

  <!-- =========================================================
       Manual Content Area
       ========================================================= -->
  <div class="content-area">
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
       Simple Footer
       ========================================================= -->
  <footer class="simple-footer">
    <div><strong>홍익여자고등학교 온라인교무실</strong> · 교원 업무 지원 가이드북</div>
  </footer>

  <!-- =========================================================
       Navigation & Modal Script
       ========================================================= -->
  <script>
    const MANUAL_LIST = {json.dumps([{"id": m["id"], "title": m["short_title"], "canva": m["canva"]} for m in MANUALS], ensure_ascii=False)};
    const navButtons = document.querySelectorAll('.manual-nav-btn');
    const panes = document.querySelectorAll('.manual-pane');
    
    const modal = document.getElementById('globalImageModal');
    const modalGallery = document.getElementById('globalModalGallery');
    const modalCloseBtn = modal.querySelector('.modal-close');
    const modalCanvaBtn = document.getElementById('modalCanvaBtn');

    let currentManualId = MANUAL_LIST[0].id;

    function selectManual(id, updateHash = true) {{
      const exists = MANUAL_LIST.some(m => m.id === id);
      if (!exists) id = MANUAL_LIST[0].id;

      currentManualId = id;

      // Update 1x7 nav button active states
      navButtons.forEach(btn => {{
        btn.classList.toggle('active', btn.dataset.id === id);
      }});

      // Update manual panes
      panes.forEach(pane => {{
        pane.classList.toggle('active', pane.dataset.id === id);
      }});

      const item = MANUAL_LIST.find(m => m.id === id);
      if (item) {{
        document.title = item.title + " | 온라인 교무실 매뉴얼";
        if (modalCanvaBtn) {{
          modalCanvaBtn.href = item.canva;
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
    window.addEventListener('DOMContentLoaded', handleHash);

    // Modal Logic
    function closeModal() {{
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      modalGallery.innerHTML = '';
    }}

    modalCloseBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {{
      if (e.target === modal) closeModal();
    }});

    // Bind all .img-toggle buttons across all panes
    document.querySelectorAll('.img-toggle').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
        
        // Find corresponding pane's canva link
        const pane = btn.closest('.manual-pane');
        const canvaUrl = (pane && pane.dataset.canva) ? pane.dataset.canva : (MANUAL_LIST.find(m => m.id === currentManualId)?.canva || '#');
        if (modalCanvaBtn) {{
          modalCanvaBtn.href = canvaUrl;
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

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape' && !modal.hidden) {{
        closeModal();
      }}
    }});
  </script>
</body>
</html>
"""

# Output paths
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

bundle_path = os.path.join(BASE_DIR, "bundle_manuals.py")
with open(__file__, "r", encoding="utf-8") as f:
    self_code = f.read()
with open(bundle_path, "w", encoding="utf-8") as f:
    f.write(self_code)

print("Generated clean index.html with single Canva button and side-by-side 독립창 열기 button.")
print("File size:", round(os.path.getsize(index_path) / 1024 / 1024, 2), "MB")

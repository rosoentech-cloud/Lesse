"""Shared layout helpers for the Lesse static site.

Run tools/build.py to regenerate every page, the blog, sitemap.xml and robots.txt.
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HERE, '..'))
BASE = 'https://lesse.rosoen.com'
TODAY = '2026-11-17'
WHATSAPP = 'https://wa.me/17029633767'
PHONE_DISPLAY = '(702) 963-3767'
PHONE_TEL = 'tel:+17029633767'
EMAIL = 'info@rosoen.com'

NAV = [
    ('services.html', 'Services'),
    ('blog/index.html', 'Blog'),
    ('payments.html', 'Payments'),
    ('contact.html', 'Contact'),
    ('policies.html', 'Policies'),
]
PAGE_LINKS = NAV + [('post-project.html', 'Post a project')]

SCRIPT_FILES = {
    'config': 'assets/js/config.js',
    'data': 'assets/js/site-data.js',
    'chat': 'assets/js/chat.js',
    'main': 'assets/js/main.js',
}


def esc(text):
    return html.escape(str(text), quote=True)


def write(relpath, content):
    path = os.path.join(SITE, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def page_url(path):
    """Public address for a page. The homepage is the bare domain, not /index.html."""
    return BASE + '/' if path == 'index.html' else f'{BASE}/{path}'


def head(title, description, path, root='', schema=None, og_type='website'):
    url = page_url(path)
    ld = ''
    for item in (schema or []):
        ld += '\n  <script type="application/ld+json">' + json.dumps(item, ensure_ascii=False) + '</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Lesse">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{root}assets/css/styles.css">{ld}
</head>'''


def header(root, current):
    links = []
    for href, label in NAV:
        aria = ' aria-current="page"' if href == current else ''
        links.append(f'        <a href="{root}{href}"{aria}>{label}</a>')
    links.append(f'        <a href="{root}post-project.html" class="btn btn-small">Post a project</a>')
    return f'''  <header class="site-header">
    <div class="container nav-wrap">
      <a href="{root}index.html" class="brand" aria-label="Lesse home">Lesse</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <nav id="site-nav" class="site-nav" aria-label="Main">
{chr(10).join(links)}
      </nav>
    </div>
  </header>'''


def footer(root):
    pages = ''.join(f'        <a href="{root}{href}">{label}</a>\n' for href, label in PAGE_LINKS)
    return f'''  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-col">
        <h3>Contact</h3>
        <ul class="contact-list">
          <li><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <a class="btn btn-small btn-whatsapp" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
      <nav class="footer-col" aria-label="Footer">
        <h3>Pages</h3>
{pages}      </nav>
      <div class="footer-col">
        <h3>Lesse</h3>
        <p class="brand">Lesse</p>
        <p class="muted">Research, writing and editing help from independent professionals.</p>
      </div>
    </div>
    <div class="container copyright">
      <p>&copy; 2026 Lesse. All rights reserved.</p>
    </div>
  </footer>'''


def page(title, description, path, body, current, root='', schema=None,
         og_type='website', scripts=('config', 'data', 'chat', 'main')):
    tags = '\n'.join(f'  <script src="{root}{SCRIPT_FILES[s]}"></script>' for s in scripts)
    return (head(title, description, path, root, schema, og_type)
            + '\n<body>\n  <a class="skip-link" href="#main">Skip to content</a>\n\n'
            + header(root, current)
            + '\n\n  <main id="main">\n' + body.rstrip() + '\n  </main>\n\n'
            + footer(root) + '\n\n' + tags + '\n</body>\n</html>\n')


def inline(text):
    s = esc(text)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    return s


def md_to_html(text):
    out, para, in_list = [], [], False

    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    for raw in text.strip().splitlines():
        line = raw.strip()
        if not line:
            flush()
            if in_list:
                out.append('</ul>')
                in_list = False
            continue
        if line.startswith('## '):
            flush()
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<h2>' + inline(line[3:]) + '</h2>')
        elif line.startswith('### '):
            flush()
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<h3>' + inline(line[4:]) + '</h3>')
        elif line.startswith('- '):
            flush()
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append('<li>' + inline(line[2:]) + '</li>')
        else:
            if in_list:
                out.append('</ul>')
                in_list = False
            para.append(line)
    flush()
    if in_list:
        out.append('</ul>')
    return '\n'.join(out)


def parse_post(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    if not m:
        raise ValueError(f'Bad front matter in {path}')
    meta = {}
    for line in m.group(1).splitlines():
        key, _, value = line.partition(':')
        meta[key.strip()] = value.strip()
    meta['body'] = m.group(2)
    base = os.path.splitext(os.path.basename(path))[0]
    meta['slug'] = base.split('-', 1)[1] if base[:2].isdigit() else base
    return meta


def sitemap_xml(entries):
    rows = []
    for path, priority in entries:
        rows.append(
            f'  <url>\n    <loc>{page_url(path)}</loc>\n    <lastmod>{TODAY}</lastmod>\n'
            f'    <priority>{priority}</priority>\n  </url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + '\n'.join(rows) + '\n</urlset>\n')

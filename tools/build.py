"""Regenerates the whole Lesse site: pages, blog, SEO files, and images.

Usage (from the draftwell-site folder):
    python3 tools/build.py

Write new blog posts as Markdown in tools/posts/ (see the README), then run this again.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from site_lib import BASE, TODAY, page, sitemap_xml, write  # noqa: E402
from svg_assets import build_assets  # noqa: E402
from pages import SERVICES, all_pages  # noqa: E402
from blog import article, index, load_posts  # noqa: E402


def priority_for(path):
    if path == 'index.html':
        return '1.0'
    if path in ('services.html', 'post-project.html', 'blog/index.html'):
        return '0.9'
    if path.startswith('blog/'):
        return '0.7'
    if path in ('writers.html', 'payments.html') or path.endswith('.html') and path[:-5] in {s['slug'] for s in SERVICES}:
        return '0.8'
    return '0.5'


def main():
    build_assets()
    posts = load_posts()
    print(f'{len(posts)} blog posts loaded')

    entries = []
    for pg in all_pages(posts):
        write(pg['path'], page(pg['title'], pg['desc'], pg['path'], pg['body'], pg['current'],
                               root='', schema=pg.get('schema'),
                               scripts=pg.get('scripts', ('config', 'chat', 'main'))))
        entries.append(pg['path'])

    write('blog/index.html', index(posts))
    entries.append('blog/index.html')
    for slug, p in posts.items():
        write(f'blog/{slug}.html', article(p, posts))
        entries.append(f'blog/{slug}.html')

    write('sitemap.xml', sitemap_xml([(path, priority_for(path)) for path in entries]))
    write('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
    write('CNAME', 'lesse.rosoen.com\n')
    print(f'{len(entries)} URLs written to sitemap.xml (last updated {TODAY})')


if __name__ == '__main__':
    main()

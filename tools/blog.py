"""Builds the blog index and every article from tools/posts/*.md."""
import os

from site_lib import BASE, esc, md_to_html, page, parse_post

HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(HERE, 'posts')


def load_posts():
    posts = {}
    for name in sorted(os.listdir(POSTS_DIR)):
        if not name.endswith('.md'):
            continue
        meta = parse_post(os.path.join(POSTS_DIR, name))
        for key in ('title', 'description', 'category', 'date'):
            if key not in meta:
                raise ValueError(f'{name} is missing "{key}"')
        posts[meta['slug']] = meta
    return posts


def ordered(posts):
    return sorted(posts.values(), key=lambda p: p['date'], reverse=True)


def card(p):
    return (f'          <a class="card link-card" href="{p["slug"]}.html">\n'
            f'            <span class="tag">{esc(p["category"])}</span>\n'
            f'            <h3>{esc(p["title"])}</h3>\n'
            f'            <p>{esc(p["description"])}</p>\n'
            f'          </a>')


def article(p, posts):
    url = f'{BASE}/blog/{p["slug"]}.html'
    others = [x for x in ordered(posts) if x['slug'] != p['slug']]
    same = [x for x in others if x['category'] == p['category']]
    related = (same + [x for x in others if x not in same])[:3]
    related_html = '\n'.join(card(x) for x in related)
    body = f'''    <article class="article">
      <header class="page-intro">
        <div class="container narrow">
          <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Blog</a> / <span>{esc(p["category"])}</span></nav>
          <p class="eyebrow">{esc(p["category"])}</p>
          <h1>{esc(p["title"])}</h1>
          <p class="lead">{esc(p["description"])}</p>
          <p class="muted">Published {esc(p["date"])}</p>
        </div>
      </header>
      <div class="container narrow prose article-body">
{md_to_html(p["body"])}
      </div>
    </article>

    <section class="section alt">
      <div class="container narrow">
        <div class="card cta-box">
          <h2>Want a writer to help?</h2>
          <p>Post a brief and get fixed quotes. Writers help with research, editing, and formatting, and the work stays yours to submit and understand.</p>
          <a class="btn" href="../post-project.html">Post a project</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Keep reading</h2>
        <div class="grid-3">
{related_html}
        </div>
      </div>
    </section>'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': p['title'],
         'description': p['description'], 'datePublished': p['date'], 'dateModified': p['date'],
         'author': {'@type': 'Organization', 'name': 'Lesse', 'url': BASE},
         'publisher': {'@type': 'Organization', 'name': 'Lesse', 'url': BASE},
         'mainEntityOfPage': url},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{BASE}/index.html'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': f'{BASE}/blog/index.html'},
            {'@type': 'ListItem', 'position': 3, 'name': p['title'], 'item': url}]},
    ]
    return page(p['title'] + ' | Lesse', p['description'], f'blog/{p["slug"]}.html', body,
                current='blog/index.html', root='../', schema=schema, og_type='article')


def index(posts):
    items = ordered(posts)
    cards = '\n'.join(card(p) for p in items)
    body = f'''    <section class="page-intro">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a> / <span>Blog</span></nav>
        <p class="eyebrow">Blog</p>
        <h1>Writing and research guides for students</h1>
        <p class="lead">Practical guides on thesis statements, citations, revision, and job applications, written to help you do the work yourself.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid-3">
{cards}
        </div>
      </div>
    </section>

    <section class="cta">
      <div class="container">
        <h2>Need hands-on help?</h2>
        <p>Post a brief and compare fixed quotes from writers who handle research, editing, and formatting.</p>
        <a class="btn" href="../post-project.html">Post a project</a>
      </div>
    </section>'''
    schema = [{'@context': 'https://schema.org', '@type': 'Blog', 'name': 'Lesse Blog',
               'url': f'{BASE}/blog/index.html',
               'blogPost': [{'@type': 'BlogPosting', 'headline': p['title'],
                             'url': f'{BASE}/blog/{p["slug"]}.html', 'datePublished': p['date']}
                            for p in items]}]
    return page('Student Writing and Research Blog | Lesse',
                'Guides on thesis statements, APA and MLA citations, literature reviews, revision, and resumes for students.',
                'blog/index.html', body, current='blog/index.html', root='../', schema=schema)

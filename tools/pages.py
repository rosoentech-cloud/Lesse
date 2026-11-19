"""Page definitions for the Lesse site. Each builder returns the data build.py needs."""
import os

from site_lib import BASE, EMAIL, PHONE_DISPLAY, PHONE_TEL, SITE, WHATSAPP, esc

STEPS = [
    ('1', 'Brief', 'Describe the goal, deadline, and format.'),
    ('2', 'Quote', 'Accept a fixed price before work starts.'),
    ('3', 'Draft', 'Review outlines and drafts as they arrive.'),
    ('4', 'Approve', "Pay each milestone once you're satisfied with it."),
]

PAY_METHODS = [
    ('PayPal', 'paypal', 'Online payments'),
    ('Visa', 'visa', 'Card payments'),
    ('Remitly', 'remitly', 'Sending money from abroad'),
    ('Zelle', 'zelle', 'Bank-to-bank transfers'),
]

PAY_LOGO_DIR = 'assets/img/payments'


def pay_logo(name, slug, root=''):
    """Use the official logo file if it has been added; otherwise show the name as text."""
    for ext in ('svg', 'png', 'webp', 'jpg'):
        rel = f'{PAY_LOGO_DIR}/{slug}.{ext}'
        if os.path.exists(os.path.join(SITE, rel)):
            return f'<img class="pay-logo" src="{root}{rel}" alt="{esc(name)}" width="140" height="48" loading="lazy">'
    return f'<span class="pay-wordmark">{esc(name)}</span>'

SERVICES = [
    {
        'slug': 'research-support', 'name': 'Research support',
        'short': 'Literature searches, annotated bibliographies, and structured reading notes.',
        'title': 'Research Support for Students | Lesse',
        'desc': 'Research support for students: literature searches, annotated bibliographies, and reading notes. See what is included and what is not.',
        'h1': 'Research support for students and researchers',
        'lead': 'Help finding, organizing, and understanding sources, so you can do the thinking and writing yourself.',
        'included': [
            'Literature searches with a stated search strategy',
            'Annotated bibliographies and summaries of sources you provide',
            'Structured reading notes and thematic maps',
            'Basic data cleaning and descriptive analysis, with the method documented',
        ],
        'excluded': [
            'Writing your assessment, thesis, or paper for submission',
            'Fabricating or altering sources or data',
        ],
        'faqs': [
            ('Will you find sources for my topic?', 'Yes. We run a search with a stated strategy, list the databases used, and summarize the sources that fit your question. You decide which ones to read and cite.'),
            ('Can you summarize articles I already have?', 'Yes. Send the articles, and we return structured notes with the main argument, method, and findings for each one.'),
        ],
        'blog': ['research-question', 'literature-review-steps', 'finding-peer-reviewed-sources', 'annotated-bibliography-guide'],
    },
    {
        'slug': 'editing-proofreading', 'name': 'Editing and proofreading',
        'short': 'Clarity, structure, grammar, and consistency, with tracked changes.',
        'title': 'Editing and Proofreading Services | Lesse',
        'desc': 'Editing and proofreading for essays, theses, and reports: grammar, clarity, structure, and tracked changes you can review.',
        'h1': 'Editing and proofreading for essays, theses, and reports',
        'lead': 'Clear feedback and careful corrections on work you have written, with every change visible.',
        'included': [
            'Copyediting for grammar, clarity, and consistency',
            'Developmental feedback on structure and argument',
            'Tracked changes with notes explaining major edits',
            'A final proofread before you submit',
        ],
        'excluded': [
            'Rewriting large sections so the work is no longer yours',
        ],
        'faqs': [
            ('Will you change my argument?', 'No. We point out where the argument is unclear or unsupported and suggest ways to strengthen it. The ideas and wording stay yours.'),
            ('What do I get back?', 'A tracked-changes file of your document, plus a short list of the main issues and what to fix first.'),
        ],
        'blog': ['three-pass-revision', 'proofreading-checklist', 'active-vs-passive-voice', 'common-academic-grammar-mistakes'],
    },
    {
        'slug': 'citations-formatting', 'name': 'Citations and formatting',
        'short': 'APA, MLA, Chicago, and Harvard formatting, plus reference list checks.',
        'title': 'APA, MLA and Chicago Formatting Help | Lesse',
        'desc': 'Citation and formatting help in APA, MLA, Chicago, and Harvard: reference lists, in-text citations, and document layout checks.',
        'h1': 'Citation and formatting help in APA, MLA, Chicago, and Harvard',
        'lead': 'Consistent references and layout in the style your course, journal, or publisher requires.',
        'included': [
            'APA, MLA, Chicago, and Harvard formatting',
            'Reference list checks against the style guide',
            'In-text citation and figure and table numbering review',
            'Template setup for journal or department requirements',
        ],
        'excluded': [
            'Adding citations to sources you have not read or checked',
        ],
        'faqs': [
            ('Which citation styles do you support?', 'APA (including 7th edition), MLA, Chicago (notes-bibliography and author-date), and Harvard.'),
            ('Do you confirm that the sources exist?', 'We check that each reference is complete and matches the style guide. Confirming that a source supports your claim is part of your own research.'),
        ],
        'blog': ['apa-7-in-text-citations', 'mla-9-works-cited', 'chicago-notes-vs-author-date', 'paraphrasing-without-plagiarism'],
    },
    {
        'slug': 'proposals-grants', 'name': 'Proposals and grants',
        'short': 'Concept notes, funding applications, and project proposals.',
        'title': 'Proposal and Grant Writing Help | Lesse',
        'desc': 'Help with concept notes, grant applications, and project proposals, built to match a funder template and criteria.',
        'h1': 'Proposal and grant writing help',
        'lead': 'Clear, structured documents for funders, supervisors, and internal approval, built to match the call.',
        'included': [
            'Concept notes and letters of intent',
            'Full proposals against a funder template',
            'Budget narratives that match your numbers',
            'Review of a draft against the call criteria',
        ],
        'excluded': [
            'Inventing outcomes, partners, or figures you cannot support',
        ],
        'faqs': [
            ('Can you work from our existing project report?', 'Yes. Share the report and the funder call, and we draft the sections that match the criteria.'),
            ('Do you submit applications for us?', "No. We prepare the document, and you submit it through the funder's system."),
        ],
        'blog': ['grant-proposal-sections', 'dissertation-proposal-essentials', 'writing-methods-section'],
    },
    {
        'slug': 'business-copy', 'name': 'Business copy',
        'short': 'Website pages, email sequences, and case studies written in your brand voice.',
        'title': 'Business Copy and Website Writing | Lesse',
        'desc': 'Website copy, email sequences, and case studies for small businesses and organizations, written to match your brand voice.',
        'h1': 'Business copy and website writing',
        'lead': 'Website pages, emails, and case studies that sound like your organization, based on material you already have.',
        'included': [
            'Website and landing page copy',
            'Email sequences and newsletters',
            'Case studies and company profiles',
            'A short brand voice guide from your existing material',
        ],
        'excluded': [
            'Product claims or testimonials you cannot back up',
        ],
        'faqs': [
            ('Do you need to know our brand first?', 'It helps, but it is not required. Send your current website, brochures, or sample emails, and we match the tone.'),
            ('Can you write case studies from our results?', 'Yes, using figures and quotes you can verify. We do not invent results or testimonials.'),
        ],
        'blog': ['strong-introduction-paragraph', 'active-vs-passive-voice', 'proofreading-checklist'],
    },
    {
        'slug': 'resumes-cvs', 'name': 'Resumes and CVs',
        'short': 'Resumes, academic CVs, and cover letters tailored to a specific role.',
        'title': 'Resume, CV and Cover Letter Help | Lesse',
        'desc': 'Resume, academic CV, and cover letter help for students and graduates, tailored to a specific role or application.',
        'h1': 'Resume, CV and cover letter help',
        'lead': 'Documents built around your real experience and the specific role, not a generic template.',
        'included': [
            'Resume and CV rewrites based on your experience',
            'Academic CVs with publications and grants formatted correctly',
            'Tailored cover letters for a job description',
            'LinkedIn summary edits',
        ],
        'excluded': [
            'Experience, skills, or credentials you do not have',
        ],
        'faqs': [
            ('I have no work experience yet. Can you help?', 'Yes. We focus on coursework, projects, volunteering, and skills, and show how they match the role.'),
            ('How many revisions do I get?', 'The number of revision rounds is stated in your written quote before work starts.'),
        ],
        'blog': ['first-job-resume', 'academic-cv-basics', 'specific-cover-letter', 'linkedin-summary-students'],
    },
]


def cta(heading, button, href='post-project.html', text=''):
    para = f'\n        <p>{esc(text)}</p>' if text else ''
    return f'''    <section class="cta">
      <div class="container">
        <h2>{esc(heading)}</h2>{para}
        <a class="btn" href="{href}">{esc(button)}</a>
      </div>
    </section>'''


def post_card(p, root=''):
    return (f'          <a class="card link-card" href="{root}blog/{p["slug"]}.html">\n'
            f'            <span class="tag">{esc(p["category"])}</span>\n'
            f'            <h3>{esc(p["title"])}</h3>\n'
            f'            <p>{esc(p["description"])}</p>\n'
            f'          </a>')


def service_card(s):
    return (f'          <a class="card link-card" href="{s["slug"]}.html">\n'
            f'            <h3>{esc(s["name"])}</h3>\n'
            f'            <p>{esc(s["short"])}</p>\n'
            f'          </a>')


def home(posts):
    latest = sorted(posts.values(), key=lambda p: p['date'], reverse=True)[:3]
    steps_cards = '\n'.join(
        f'          <article class="card">\n            <span class="num">{n}</span>\n'
        f'            <h3>{esc(t)}</h3>\n            <p>{esc(x)}</p>\n          </article>'
        for n, t, x in [
            ('1', 'Post your brief', 'Tell us what you need, when it is due, the format, and any style guide you follow.'),
            ('2', 'Compare quotes', 'Writers reply with a scope, a fixed price, and a timeline you can compare.'),
            ('3', 'Review as it goes', 'Agree on an outline first, then review drafts in stages instead of one large delivery.'),
            ('4', 'Approve and pay', 'Each milestone is paid when you approve it, or when the review window in your quote closes.'),
        ])
    steps_list = '\n'.join(f'            <li><span>{esc(t)}</span> {esc(x)}</li>' for _, t, x in STEPS)
    service_cards = '\n'.join(service_card(s) for s in SERVICES)
    pay = '\n'.join(
        f'          <a class="pay-badge" href="payments.html">{pay_logo(name, slug)}<small>{esc(note)}</small></a>'
        for name, slug, note in PAY_METHODS)
    blog = '\n'.join(post_card(p) for p in latest)
    body = f'''    <section class="hero">
      <div class="container hero-grid">
        <div>
          <p class="eyebrow">Independent writers and editors</p>
          <h1>Clear writing and careful research, on your schedule.</h1>
          <p class="lead">Post a brief, compare fixed quotes from writers you can review, and approve each milestone before you pay.</p>
          <div class="actions">
            <a class="btn" href="post-project.html">Post a project</a>
            <a class="btn btn-ghost" href="services.html">See our services</a>
          </div>
        </div>
        <aside class="hero-card" aria-label="How a project runs">
          <img class="hero-illustration" src="assets/img/student-learning.svg" width="480" height="320" alt="A student learning at a desk with a laptop and notes">
          <ol class="steps-compact">
{steps_list}
          </ol>
        </aside>
      </div>
    </section>

    <section class="trust" aria-label="Our commitments">
      <div class="container trust-row">
        <p>Fixed quotes, not open-ended hourly billing</p>
        <p>Milestone-based payment</p>
        <p>Written rules on AI use and academic integrity</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>How it works</h2>
        <div class="grid-4">
{steps_cards}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>Our services</h2>
        <div class="grid-3">
{service_cards}
        </div>
        <p class="more"><a href="services.html">See every service and what is included &rarr;</a></p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2>Ways to pay</h2>
        <p class="muted">Each milestone is paid after you approve it. See the payments page for details.</p>
        <div class="pay-badges">
{pay}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>From the Lesse blog</h2>
        <div class="grid-3">
{blog}
        </div>
        <p class="more"><a href="blog/index.html">Read all articles &rarr;</a></p>
      </div>
    </section>

{cta('Have a brief ready?', 'Post a project', text='Describe the work once. Writers who fit the project will reply with their quotes.')}'''
    schema = [
        {'@context': 'https://schema.org', '@type': 'Organization', 'name': 'Lesse', 'url': BASE,
         'email': EMAIL, 'telephone': PHONE_DISPLAY,
         'contactPoint': {'@type': 'ContactPoint', 'telephone': '+1-702-963-3767', 'email': EMAIL,
                          'contactType': 'customer service'}},
    ]
    return dict(path='index.html',
                title='Lesse | Research, Writing and Editing Help for Students',
                desc='Research support, editing, citation formatting, proposals, and resume help from independent writers. Get a fixed quote before work starts.',
                body=body, current='index.html', schema=schema)


def services_hub():
    cards = '\n'.join(
        f'''          <article class="card">
            <h3><a href="{s["slug"]}.html">{esc(s["name"])}</a></h3>
            <p>{esc(s["short"])}</p>
            <ul class="plain-list">{"".join(f"<li>{esc(x)}</li>" for x in s["included"][:3])}</ul>
            <p class="more"><a href="{s["slug"]}.html">Full details &rarr;</a></p>
          </article>'''
        for s in SERVICES)
    body = f'''    <section class="page-intro">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span>Services</span></nav>
        <p class="eyebrow">Services</p>
        <h1>What you can hire us for</h1>
        <p class="lead">Each service lists what is included and what is not. If your project falls outside these, describe it in a brief and we will tell you whether we can help.</p>
      </div>
    </section>

    <section class="section">
      <div class="container grid-2">
{cards}
      </div>
    </section>

{cta('Not sure which service fits?', 'Post a project', text='Describe the work in a brief, and we will match you with writers who handle that kind of project.')}'''
    schema = [{'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Lesse services',
               'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': s['name'],
                                    'url': f'{BASE}/{s["slug"]}.html'} for i, s in enumerate(SERVICES)]}]
    return dict(path='services.html',
                title='Writing, Research and Editing Services | Lesse',
                desc='Browse Lesse services: research support, editing and proofreading, citation formatting, proposals and grants, business copy, and resume help.',
                body=body, current='services.html', schema=schema)


def service_page(s, posts):
    faq_html = '\n'.join(
        f'        <details class="faq"><summary>{esc(q)}</summary><p>{esc(a)}</p></details>'
        for q, a in s['faqs'])
    included = ''.join(f'<li>{esc(x)}</li>' for x in s['included'])
    excluded = ''.join(f'<li>{esc(x)}</li>' for x in s['excluded'])
    steps = '\n'.join(
        f'          <article class="card"><span class="num">{n}</span><h3>{esc(t)}</h3><p>{esc(x)}</p></article>'
        for n, t, x in STEPS)
    related = '\n'.join(
        f'          <li><a href="blog/{slug}.html">{esc(posts[slug]["title"])}</a></li>'
        for slug in s['blog'] if slug in posts)
    body = f'''    <section class="page-intro">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / <span>{esc(s["name"])}</span></nav>
        <p class="eyebrow">Service</p>
        <h1>{esc(s["h1"])}</h1>
        <p class="lead">{esc(s["lead"])}</p>
        <div class="actions">
          <a class="btn" href="post-project.html">Post a project</a>
          <a class="btn btn-ghost" href="contact.html">Ask a question</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container grid-2">
        <div class="card"><h2>What is included</h2><ul class="check-list">{included}</ul></div>
        <div class="card"><h2>What we do not do</h2><ul class="plain-list">{excluded}</ul></div>
      </div>
    </section>

    <section class="section alt">
      <div class="container">
        <h2>How a project works</h2>
        <div class="grid-4">
{steps}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <h2>Common questions</h2>
{faq_html}
      </div>
    </section>

    <section class="section alt">
      <div class="container narrow">
        <h2>Read next</h2>
        <ul class="plain-list">
{related}
        </ul>
      </div>
    </section>

{cta('Ready to share your brief?', 'Post a project', text='Describe the work and get fixed quotes from writers who handle it.')}'''
    url = f'{BASE}/{s["slug"]}.html'
    schema = [
        {'@context': 'https://schema.org', '@type': 'Service', 'name': s['name'], 'description': s['desc'],
         'url': url, 'provider': {'@type': 'Organization', 'name': 'Lesse', 'url': BASE}},
        {'@context': 'https://schema.org', '@type': 'FAQPage',
         'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                        for q, a in s['faqs']]},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{BASE}/index.html'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Services', 'item': f'{BASE}/services.html'},
            {'@type': 'ListItem', 'position': 3, 'name': s['name'], 'item': url}]},
    ]
    return dict(path=f'{s["slug"]}.html', title=s['title'], desc=s['desc'], body=body,
                current='services.html', schema=schema)


def contact():
    body = f'''    <section class="page-intro">
      <div class="container">
        <p class="eyebrow">Contact</p>
        <h1>Send us a message</h1>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <form class="brief-form" action="https://formsubmit.co/ajax/{EMAIL}" method="POST" data-ajax-form data-status="contact-status">
          <input type="hidden" name="_subject" value="New message from the Lesse website">

          <p class="form-sent" id="contact-status" hidden>Thanks. Your message has been received, and we'll reply by email.</p>

          <div class="field-row">
            <div class="field">
              <label for="c-name">Your name</label>
              <input id="c-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="c-email">Email</label>
              <input id="c-email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>

          <div class="field-row">
            <div class="field">
              <label for="c-phone">Phone or WhatsApp (optional)</label>
              <input id="c-phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div class="field">
              <label for="c-service">What do you need help with?</label>
              <select id="c-service" name="service">
                <option value="">Choose one</option>
                <option>Research support</option>
                <option>Editing and proofreading</option>
                <option>Citations and formatting</option>
                <option>Proposals and grants</option>
                <option>Business copy</option>
                <option>Resumes and CVs</option>
                <option>Something else</option>
              </select>
            </div>
          </div>

          <div class="field">
            <label for="c-message">Message</label>
            <textarea id="c-message" name="message" rows="6" required placeholder="Tell us what you need, and when it is due if you have a deadline."></textarea>
          </div>

          <button class="btn" type="submit">Send message</button>
        </form>

        <aside class="card contact-card">
          <h2>Prefer to talk?</h2>
          <ul class="contact-list">
            <li>Phone: <a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <a class="btn btn-whatsapp" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
          <p class="muted">You can also use the chat button in the corner of any page.</p>
        </aside>
      </div>
    </section>'''
    return dict(path='contact.html',
                title='Contact Lesse | WhatsApp, Phone and Email',
                desc='Contact Lesse by WhatsApp, phone, or email, or send a message through the form. We reply to the email address you give us.',
                body=body, current='contact.html')


def post_project():
    body = f'''    <section class="page-intro">
      <div class="container">
        <p class="eyebrow">Post a project</p>
        <h1>Tell us about the work</h1>
        <p class="lead">The more specific your brief, the more accurate the quotes. There is no charge to post a brief.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow">
        <p class="form-sent" id="form-sent" hidden>Thanks. Your brief has been received, and matching writers will reply by email.</p>

        <form class="brief-form" action="https://formsubmit.co/ajax/{EMAIL}" method="POST" data-ajax-form data-status="form-sent">
          <input type="hidden" name="_subject" value="New project brief from the Lesse website">

          <div class="field">
            <label for="name">Your name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>

          <div class="field">
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>

          <div class="field">
            <label for="service">Type of service</label>
            <select id="service" name="service" required>
              <option value="">Choose one</option>
              <option>Research support</option>
              <option>Editing and proofreading</option>
              <option>Citations and formatting</option>
              <option>Proposals and grants</option>
              <option>Business copy</option>
              <option>Resumes and CVs</option>
              <option>Something else</option>
            </select>
          </div>

          <div class="field-row">
            <div class="field">
              <label for="deadline">Deadline</label>
              <input id="deadline" name="deadline" type="date">
            </div>
            <div class="field">
              <label for="budget">Budget range</label>
              <select id="budget" name="budget">
                <option value="">Not sure yet</option>
                <option>Under $100</option>
                <option>$100 to $300</option>
                <option>$300 to $1,000</option>
                <option>Over $1,000</option>
              </select>
            </div>
          </div>

          <div class="field">
            <label for="brief">Project brief</label>
            <textarea id="brief" name="brief" rows="7" required placeholder="What is the goal? Who is the audience? What format and length do you need? Include any style guide or existing material."></textarea>
          </div>

          <div class="field">
            <label for="link">Link to reference material (optional)</label>
            <input id="link" name="reference_link" type="url" placeholder="https://">
          </div>

          <div class="field checkbox">
            <input id="confirm" name="integrity_confirmed" type="checkbox" required>
            <label for="confirm">I confirm this work is for research assistance, editing, or another use my school, employer, or client allows. I understand the <a href="policies.html#integrity">academic integrity policy</a>.</label>
          </div>

          <button class="btn" type="submit">Send my brief</button>
        </form>

        <p class="form-note">Your brief is sent to our inbox at {EMAIL}. We reply to the email address you enter above.</p>
      </div>
    </section>'''
    return dict(path='post-project.html',
                title='Post a Writing or Research Project | Lesse',
                desc='Post your editing, research, citation, proposal, or resume project and receive fixed quotes from writers. No charge to post a brief.',
                body=body, current='post-project.html')


def policies():
    body = f'''    <section class="page-intro">
      <div class="container">
        <p class="eyebrow">Policies</p>
        <h1>How we work</h1>
        <p class="lead">These rules apply to every client and writer on Lesse. Read them before you post a project or accept one.</p>
      </div>
    </section>

    <section class="section">
      <div class="container narrow prose">

        <h2 id="integrity">Academic integrity</h2>
        <p>Lesse provides research organization, editing, formatting, and feedback. We do not provide work to be submitted as a student's own assessment where the institution prohibits outside help.</p>
        <p>Clients are responsible for following their school's or program's rules. Writers may decline any project they believe breaks those rules, and may ask for proof of permission to proceed.</p>

        <h2 id="ai">Use of AI tools</h2>
        <p>Writers may use software tools as part of their process, including spelling and grammar checkers and, where the client allows it, AI assistants. Each brief states whether AI tools may be used and whether they must be disclosed.</p>
        <p>A writer must not present AI-generated text as their own original writing when the client has said that is not acceptable. Writers must check every source they cite. Invented or unverifiable citations are grounds for removal from the platform.</p>

        <h2 id="quality">Quality and revisions</h2>
        <p>Each quote states the scope, the number of revision rounds, and the review window. Work that does not match the agreed scope can be revised at no extra cost, within the stated revision rounds.</p>
        <p>If you and a writer disagree about whether work meets the scope, contact us. We will review the brief, the quote, and the delivered work with both parties.</p>

        <h2 id="payments">Payments and refunds</h2>
        <p>Payment is made per milestone. Funds for each milestone are released when you approve it, or when the review window in your quote closes without a response.</p>
        <p>If a writer does not deliver a milestone, you are refunded for that milestone. If a project is cancelled before work starts, any amount paid is returned.</p>
        <p>The payment methods we accept are listed on our <a href="payments.html">Payments page</a>, and each written quote confirms the method for that project.</p>

        <h2 id="prohibited">Prohibited work</h2>
        <ul>
          <li>Plagiarized material, or work copied from another writer's or client's files</li>
          <li>Fabricated sources, data, or testimonials</li>
          <li>Documents designed to impersonate a real organization, person, or official record</li>
          <li>Harassment of any person, including anyone named in a brief</li>
        </ul>

        <h2 id="privacy">Privacy</h2>
        <p>We collect only what we need to match you with writers and process your project: your contact details, the brief, and any files you share. We do not sell personal information.</p>
        <p>To ask what we hold about you or to request deletion, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2 id="contact">Contact</h2>
        <p>For questions about these policies, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

      </div>
    </section>'''
    return dict(path='policies.html',
                title='Policies: Academic Integrity, Payments and Privacy | Lesse',
                desc='Academic integrity, AI use, quality and revisions, payments and refunds, and privacy at Lesse.',
                body=body, current='policies.html')


def payments():
    badges = '\n'.join(
        f'          <div class="pay-card">{pay_logo(name, slug)}<span>{esc(note)}</span></div>'
        for name, slug, note in PAY_METHODS)
    body = f'''    <section class="page-intro">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a> / <span>Payments</span></nav>
        <p class="eyebrow">Payments</p>
        <h1>Ways to pay</h1>
        <p class="lead">Payment is made per milestone, after you approve the work. The method for your project is confirmed in your written quote.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="pay-grid">
{badges}
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="container narrow prose">
        <h2>How milestone payments work</h2>
        <ul>
          <li>Your quote lists each milestone and its price before work starts.</li>
          <li>You approve each milestone when you are satisfied with it.</li>
          <li>Payment for that milestone is released when you approve, or when the review window in your quote closes.</li>
        </ul>
        <p>Read the full terms on our <a href="policies.html#payments">policies page</a>.</p>
      </div>
    </section>

{cta('Ready to start?', 'Post a project')}'''
    return dict(path='payments.html',
                title='Ways to Pay: PayPal, Visa, Remitly and Zelle | Lesse',
                desc='See the payment methods on Lesse, including PayPal, Visa, Remitly, and Zelle, and how milestone payments work.',
                body=body, current='payments.html')


def all_pages(posts):
    pages = [home(posts), services_hub(), contact(), post_project(), policies(), payments()]
    pages += [service_page(s, posts) for s in SERVICES]
    return pages

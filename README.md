# Lesse

A website for a writing, research, and editing service, hosted on GitHub Pages at https://lesse.rosoen.com.

It has a home page, a services page with six service landing pages, a blog with 30 articles, a contact page, a brief form, a payments page, policies, and a chat box. The chat box answers visitors using the site's own content.

## What is in the folder

| Path | What it is |
| --- | --- |
| `index.html`, `services.html`, `contact.html`, `post-project.html`, `payments.html`, `policies.html` | Main pages (generated) |
| `research-support.html`, `editing-proofreading.html`, `citations-formatting.html`, `proposals-grants.html`, `business-copy.html`, `resumes-cvs.html` | Service landing pages (generated) |
| `blog/` | Blog index and 30 articles (generated) |
| `tools/build.py` | Builds every page, the blog, `sitemap.xml`, `robots.txt`, and the assistant's knowledge file |
| `tools/pages.py` | Text and structure of the main pages and the service list |
| `tools/posts/` | Blog articles as Markdown, one file each |
| `tools/site_lib.py`, `tools/blog.py`, `tools/knowledge.py`, `tools/svg_assets.py` | Shared layout, blog builder, assistant knowledge, and images |
| `assets/js/config.js` | Contact details, availability, and the assistant's address |
| `assets/js/chat.js` | Chat box and how it answers |
| `assets/js/site-data.js` | Generated from the site's text. The chat box searches it when no AI endpoint is set |
| `assets/js/main.js` | Menu, form submission, and small shared behaviour |
| `assets/css/styles.css` | All styles |
| `assets/img/` | Student illustration, favicon, avatar, and the payment logo folder |
| `ai-worker/worker.js` | Connects the chat box to Claude. Runs on Cloudflare, not on the site |
| `ai-worker/site-knowledge.js` | Generated from the site's pages. The assistant answers from this file |
| `sitemap.xml`, `robots.txt`, `CNAME` | For search engines and the custom domain |

## Editing the site

Most pages are generated, so change the source and rebuild:

- Page text and the service list: `tools/pages.py`
- Blog articles: Markdown files in `tools/posts/`
- Contact details and the assistant's address: `assets/js/config.js` and `tools/site_lib.py`

Then run:

```bash
python3 tools/build.py
```

This needs Python 3 and nothing else.

## Adding a blog article

1. Create a file in `tools/posts/` with a number and a slug, for example `31-cover-letter-tips.md`.
2. Start it with this header, then write the article in Markdown (`##` for headings, `-` for lists):

   ```
   ---
   title: Your Article Title
   description: One or two sentences for search results.
   category: Writing
   date: 2026-11-20
   ---
   ```

3. Run `python3 tools/build.py`.

## Chat box and the AI assistant

The chat box appears on every page and always shows "Active now".

The chat box answers only from the site's own content. Each build, `tools/knowledge.py` reads the built pages and writes two files from them:

- `assets/js/site-data.js`: short pieces of the site text. Until the AI is deployed, the chat box finds the piece that best matches a question, shows it, and links to its page.
- `ai-worker/site-knowledge.js`: the full text the worker sends to Claude with each question. Once deployed, Claude writes the answers from it. Blog articles are included by title and summary only.

If a question isn't covered, the chat says so and points visitors to WhatsApp or email. Run the build again after any change so both files stay current.

To make it live:

1. Create a Cloudflare account and install Wrangler: `npm install -g wrangler`.
2. From the `ai-worker` folder, run `wrangler deploy worker.js --name lesse-chat`.
3. Store your Anthropic API key as a secret. Wrangler asks for the value. Don't paste it into a chat or a file: `wrangler secret put ANTHROPIC_API_KEY`
4. Copy the worker's URL into `aiEndpoint` in `assets/js/config.js`, then run `python3 tools/build.py`.

Until the worker is deployed, the chat uses the site-text search described above. It can't write new answers, so a question the site doesn't cover gets a pointer to WhatsApp.

The assistant is an AI and can make mistakes. Read a sample of its answers from time to time.

## Forms and email delivery

The brief form (`post-project.html`) and the contact form (`contact.html`) send to **info@rosoen.com** through [FormSubmit](https://formsubmit.co), which needs no account.

- **First-time setup:** the first submission sends an activation link to info@rosoen.com. Click it, or submissions are held. Then submit a test form.
- **Replies:** the visitor's email address is in the form, so you can reply from your inbox.
- **Third party:** submissions pass through FormSubmit. See formsubmit.co for its limits and terms.

## Publish to GitHub Pages

1. Create an empty repository on GitHub, for example `lesse-site`.
2. In this folder, run:

   ```bash
   git init -b main
   git add .
   git commit -m "Lesse website"
   git remote add origin https://github.com/YOUR-USERNAME/lesse-site.git
   git push -u origin main
   ```

3. On GitHub, go to **Settings → Pages**. Set **Source** to *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. Under **Custom domain**, enter `lesse.rosoen.com`. The `CNAME` file already contains it.
5. In your DNS settings for rosoen.com, add a CNAME record: host `lesse`, pointing to `YOUR-USERNAME.github.io`. When DNS has updated, tick **Enforce HTTPS**.

## Search Console

1. Add `https://lesse.rosoen.com` as a property and verify it.
2. Under **Sitemaps**, submit `sitemap.xml`. The file lists every page on the site.
3. Request indexing for the home page and a few blog articles.

After adding many articles, run the build again and resubmit the sitemap.

## Before launch

- Activate FormSubmit (see above).
- Put the real legal business name in the footer copyright line (`tools/site_lib.py`, `footer` function).
- Add the payment logos to `assets/img/payments/` as `paypal`, `visa`, `remitly`, and `zelle` (SVG or PNG), then rebuild. Until then the names show as text. Use each logo only as that company's brand guidelines allow. Only list payment methods you can accept.
- Have someone qualified review the policies, especially payments, refunds, and privacy, before you take payment.
- Deploy the assistant and set `aiEndpoint`.

## Not included in the static site

These need a backend or a third-party service:

- Accounts and log-in
- Payment processing, milestone escrow, and refunds
- Live chat with a person inside the website (the chat links to WhatsApp for that)
- File uploads on the forms

Options include Stripe for payments and Supabase or Firebase for accounts.

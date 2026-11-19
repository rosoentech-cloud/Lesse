# Lesse

A website for a writing, research, and editing service: service pages, six service landing pages, a writer listing, a blog, a contact form, a brief form, payment information, and an AI chat box. It is a static site hosted on GitHub Pages at **https://lesse.rosoen.com**.

## What is in the folder

| Path | What it is |
| --- | --- |
| `index.html`, `services.html`, `writers.html`, `contact.html`, `post-project.html`, `policies.html`, `payments.html` | Main pages (generated) |
| `research-support.html`, `editing-proofreading.html`, `citations-formatting.html`, `proposals-grants.html`, `business-copy.html`, `resumes-cvs.html` | Service landing pages (generated) |
| `blog/` | Blog index and 30 articles (generated) |
| `tools/build.py` | Generates every page, the blog, `sitemap.xml`, and `robots.txt` |
| `tools/pages.py` | Page text and the service list |
| `tools/posts/` | Blog articles as Markdown, one file each |
| `tools/site_lib.py`, `tools/blog.py`, `tools/svg_assets.py` | Shared layout, blog builder, and images |
| `assets/js/config.js` | Contact details, writer availability, and the AI chat address |
| `assets/js/chat.js` | Chat box |
| `assets/js/writers.js` | Writer listing |
| `assets/js/main.js` | Menu, form submission, and small shared behaviour |
| `assets/css/styles.css` | All styles |
| `assets/img/` | Student illustration, favicon, avatars (SVG) |
| `ai-worker/worker.js` | Connects the chat box to Claude (runs on Cloudflare, not on the site) |
| `sitemap.xml`, `robots.txt`, `CNAME` | For search engines and the custom domain |

## Editing pages

Most pages are generated, so do not edit the HTML files directly. Change `tools/pages.py` for page text, or `assets/js/*.js` for the writer list, chat, and settings. Then rebuild:

```bash
python3 tools/build.py
```

This needs Python 3 and no other packages.

## Adding a blog article

1. Create a file in `tools/posts/` named with a number and a slug, for example `31-cover-letter-tips.md`.
2. Start the file with this header, then the article in Markdown (`##` for headings, `-` for lists):

   ```
   ---
   title: Your Article Title
   description: One or two sentences for search results, about 150 characters.
   category: Writing
   date: 2026-11-20
   ---
   ```

3. Run `python3 tools/build.py`. The article appears on the blog, in the sitemap, and in the "Keep reading" links.

## Preview locally

Open `index.html` in a browser. The blog and service pages work the same way. Nothing needs to be installed beyond Python for rebuilding.

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

3. On GitHub, go to **Settings → Pages**. Set **Source** to *Deploy from a branch*, branch `main`, folder `/ (root)`, and save.
4. Under **Custom domain**, enter `lesse.rosoen.com` and save. The `CNAME` file in this folder already contains that name.
5. In your DNS settings for rosoen.com, add a CNAME record: host `lesse`, pointing to `YOUR-USERNAME.github.io`. Wait for DNS to update, then tick **Enforce HTTPS** in the Pages settings.

## Search Console

1. Go to [Google Search Console](https://search.google.com/search-console) and add the property `https://lesse.rosoen.com`. Verify it using the DNS or HTML method Google offers.
2. Open **Sitemaps**, enter `sitemap.xml`, and submit. The file lists all 44 pages.
3. Use **URL inspection** on the home page and one blog article to request indexing.

The sitemap is rebuilt each time you run `tools/build.py`. Submit it again if you add many articles.

## Chat box and the AI assistant

The chat box appears in the bottom corner of every page. It shows **Active now** and answers visitor questions with Claude. A WhatsApp button is included for a person.

The AI needs a small server, called a worker, because an API key must never sit in public files. Setup is in the comments at the top of `ai-worker/worker.js`:

1. Deploy the worker with Cloudflare Wrangler.
2. Store your Anthropic API key as a secret named `ANTHROPIC_API_KEY`.
3. Copy the worker's URL into `aiEndpoint` in `assets/js/config.js`, then run `python3 tools/build.py`.

Until the worker is deployed, the chat box says the assistant is not connected yet and points to WhatsApp.

Check the assistant's answers before you rely on it. It follows the rules in `worker.js`, but it is an AI and can make mistakes. Keep the system prompt in step with your actual services and policies.

## Writers

Writers are listed in `assets/js/writers.js`. Lesse is the one live profile. The other nine slots say "Writer profile coming soon" until you add real writers. To add a writer, replace a reserved slot with an object that has `name`, `headline`, `categories` (any of `research`, `editing`, `formatting`, `proposals`, `business`, `career`), `bio`, `avatar` (a file in `assets/img/`), and `live: true`. Only list people who have agreed to appear on the site.

## Forms and email delivery

The brief form (`post-project.html`) and the contact form (`contact.html`) send to **info@rosoen.com** through [FormSubmit](https://formsubmit.co), a free service that needs no account.

- **First-time setup:** the first submission sends an activation link to info@rosoen.com. Click it. Until you do, submissions are held and not delivered. Then submit a test form yourself.
- **Replies:** the student's email address is in the form, so you can reply from your inbox.
- **Third party:** submissions pass through FormSubmit's servers. Check formsubmit.co for limits and terms.

## Before launch

- Activate FormSubmit (see above).
- Set the real legal business name in the footer copyright line (`tools/site_lib.py`, the `footer` function).
- Connect the payment methods listed on the Payments page before you advertise them. The site lists PayPal, Visa, Remitly, and Zelle, so only keep the ones you can actually accept.
- **Payment logos:** add the official files to `assets/img/payments/` named `paypal`, `visa`, `remitly`, and `zelle` (SVG or PNG), then run `python3 tools/build.py`. Until then the names show as text. Use each logo only as that company's brand guidelines allow.
- Have someone qualified review the policies, especially payments, refunds, and privacy, before you take payment.
- Deploy the AI worker and set `aiEndpoint`, or the chat box will only point to WhatsApp.

## What the static site does not do

These features need a backend or a third-party service before they work:

- Accounts and log-in for clients and writers
- Writer applications and identity or portfolio checks
- Payment processing, milestone escrow, and refunds
- Live chat with a person inside the website (the chat box links to WhatsApp for that)
- File uploads on the forms

Options include Stripe for payments, Supabase or Firebase for accounts and data, and Tawk.to for live chat.

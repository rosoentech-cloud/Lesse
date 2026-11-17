# Lesse

A static website for a writing, research, and editing service. It has service pages, a writer listing, a contact form, a brief form, a chat box, and policies. There is no build step, and it runs on GitHub Pages.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home page: how it works, service overview, commitments |
| `services.html` | Each service with what is included and what is not |
| `writers.html` | Writer listing with specialty filters (data in `assets/js/writers.js`) |
| `contact.html` | Contact form for questions and requests |
| `post-project.html` | Project brief form |
| `policies.html` | Academic integrity, AI use, revisions, payments, privacy |

## Preview locally

Open `index.html` in a browser. Nothing needs to be installed.

## Publish on GitHub Pages

1. Create an empty repository on GitHub, for example `draftwell-site`.
2. In this folder, run:

   ```bash
   git init -b main
   git add .
   git commit -m "Initial site"
   git remote add origin https://github.com/YOUR-USERNAME/draftwell-site.git
   git push -u origin main
   ```

3. On GitHub, open the repository and go to **Settings → Pages**.
4. Under **Build and deployment**, set **Source** to *Deploy from a branch*, choose `main`, and folder `/ (root)`, then save.
5. After about a minute the site is live at `https://YOUR-USERNAME.github.io/draftwell-site/`.

All links are relative, so the site works from a subfolder path like that.

## Chat box and availability

The chat box appears in the bottom-right corner of every page.

- **Availability** is set in `assets/js/config.js`. Set `available` to `true` when you can chat, and to `false` when you are away. The box then shows that you are away, and visitors can still leave a message.
- **Messages** typed in the box open a WhatsApp chat with you, with their text already filled in. This is not live chat inside the website. Replies come through WhatsApp.

## Forms and email delivery

The contact form (`contact.html`) and the brief form (`post-project.html`) send to **info@rosoen.com** through [FormSubmit](https://formsubmit.co), a free service that needs no account.

- **First-time setup:** the first time anyone submits a form, FormSubmit emails an activation link to info@rosoen.com. Open that email and click the link. Until you do, submissions are held and not delivered. Test by submitting one form yourself after you activate it.
- **Replies:** the student's email address goes in the form's email field, so you can reply directly from your inbox.
- **Third-party service:** submissions pass through FormSubmit's servers before they reach your inbox. Check formsubmit.co for current limits and terms.
- **Changing the address:** replace `info@rosoen.com` in the form `action` attributes in `contact.html` and `post-project.html`, and in `config.js`.

## Writer listing

Writers are listed in `assets/js/writers.js`. Each writer is one object in the `WRITERS` list. The "Available now" tag shows only when both the site-wide `available` setting and the writer's own `available` value are `true`.

## Before launch

- **Activate FormSubmit** by submitting one test form, then clicking the activation link in the email.
- **Legal name:** add your registered business name to the footer copyright line if it differs from "Lesse".
- **Policies:** the payments, refunds, and privacy text describes how the platform is meant to work. Edit it to match your real terms, and have someone qualified review it before you take payment. Remove the "Payment processing is not yet active" note once payments are live.
- **Pricing:** the site says writers set their own rates. If you want to show starting prices, add them to `services.html`.
- **Other writers:** add any other writers to `writers.html` only after they agree to be listed.

## What the static site does not do

This is front-end only. These features need a backend or a third-party service:

- Accounts and log-in for clients and writers
- Writer applications and identity or portfolio checks
- Payments, milestone escrow, and refunds
- Live chat inside the website (the chat box opens WhatsApp instead)
- File uploads on the forms

Options include Stripe for payments, Supabase or Firebase for accounts and data, and a live-chat tool such as Tawk.to if you want chat inside the website.

## Files

```
index.html
services.html
writers.html
contact.html
post-project.html
policies.html
assets/
  css/styles.css    shared styles, including the chat box
  js/config.js      availability and contact details
  js/chat.js        chat box
  js/writers.js     writer listing and filtering
  js/main.js        shared behaviour (menu, year, form submission)
.nojekyll           tells GitHub Pages to serve files as-is
```

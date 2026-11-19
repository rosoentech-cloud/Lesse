// Cloudflare Worker that connects the Lesse chat box to Claude.
//
// Why a worker: an API key must never sit in the website's public files.
// The chat box sends visitor messages here; this script adds the key and calls Claude.
//
// Setup (once):
//   1. Create a Cloudflare account and install Wrangler: npm install -g wrangler
//   2. In this folder run: wrangler deploy worker.js --name lesse-chat
//   3. Store your key as a secret (paste it when asked):
//        wrangler secret put ANTHROPIC_API_KEY
//   4. Optional: wrangler secret put ALLOWED_ORIGIN and enter https://lesse.rosoen.com
//   5. Copy the worker URL it prints into assets/js/config.js as aiEndpoint.

import { SITE_KNOWLEDGE } from './site-knowledge.js';

const SYSTEM_PROMPT = `You are the chat assistant on the Lesse website. Visitors ask about Lesse's services, how projects work, payments, policies, and contact details.

Answer ONLY from the SITE INFORMATION below. Do not use outside knowledge about prices, deadlines, writers, or other companies.
- If the site information does not cover the question, say you don't have that detail, and point the visitor to WhatsApp (https://wa.me/17029633767) or email info@rosoen.com.
- Give prices or turnaround times only when the site information states them. Otherwise say that each project gets a written, fixed quote after the brief is posted.
- Do not write essays, assignments, or other work for a student to submit. You can explain what Lesse offers, such as research organization, editing, formatting, feedback, and career documents.
- If asked whether you are a person, say you are Lesse's AI assistant.
- Keep answers short (under 120 words), plain, and friendly. When it helps, link to the relevant page, using the URLs in the site information.

SITE INFORMATION
`;

export default {
  async fetch(request, env) {
    const origin = env.ALLOWED_ORIGIN || 'https://lesse.rosoen.com';
    const cors = {
      'Access-Control-Allow-Origin': origin,
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: cors });
    }
    if (request.method !== 'POST') {
      return json({ error: 'Method not allowed' }, 405, cors);
    }

    let body;
    try {
      body = await request.json();
    } catch (err) {
      return json({ error: 'Invalid JSON' }, 400, cors);
    }

    // Keep only the last 12 turns, cap message length, and start with a user message.
    let messages = (Array.isArray(body.messages) ? body.messages : [])
      .filter((m) => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
      .slice(-12)
      .map((m) => ({ role: m.role, content: m.content.slice(0, 2000) }));
    while (messages.length && messages[0].role !== 'user') {
      messages.shift();
    }
    if (messages.length === 0) {
      return json({ error: 'No user message' }, 400, cors);
    }

    const upstream = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'x-api-key': env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json',
      },
      body: JSON.stringify({
        model: env.MODEL || 'claude-haiku-5-5',
        max_tokens: 400,
        system: [{ type: 'text', text: SYSTEM_PROMPT + SITE_KNOWLEDGE, cache_control: { type: 'ephemeral' } }],
        messages,
      }),
    });

    if (!upstream.ok) {
      return json({ error: 'Upstream error' }, 502, cors);
    }

    const data = await upstream.json();
    const reply = (data.content || [])
      .filter((block) => block.type === 'text')
      .map((block) => block.text)
      .join('\n')
      .trim();

    return json({ reply }, 200, cors);
  },
};

function json(obj, status, headers) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...headers, 'Content-Type': 'application/json' },
  });
}

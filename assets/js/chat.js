// Chat box. It answers in one of two ways:
// - With the AI assistant, when config.js has an aiEndpoint (the Cloudflare worker in ai-worker/).
// - From the site's own text (assets/js/site-data.js), when there is no endpoint or the endpoint fails.
// Settings come from assets/js/config.js.
(function () {
  'use strict';

  var cfg = window.SITE_CONFIG;
  if (!cfg || !cfg.whatsappNumber) return;

  var WHATSAPP = 'https://wa.me/' + cfg.whatsappNumber;
  var GREETING = "Hi, I'm Lesse's AI assistant. Ask me about our services, how a project works, or how to pay.";
  var GREETING_REPLY = 'Hello! Ask me about our services, how a project works, payments, or our policies.';
  var IDENTITY_REPLY = "I'm Lesse's AI assistant. I answer from what is on this website. To reach a person, use the WhatsApp button below.";
  var NO_MATCH = "I couldn't find that on our site. Try asking another way, or use the WhatsApp button below and we'll reply.";
  var history = [];

  // Common words that do not help find a page.
  var STOP = Object.create(null);
  ('a an and are as at be but by can do does for from get go have how i if in is it me my of on or our out so ' +
   'the their them there they this to we what when where which who why will with would you your about any ' +
   'tell know need want please some')
    .split(' ')
    .forEach(function (w) { STOP[w] = true; });

  // Very light stemming so "services", "service" and "servicing" match.
  function stem(word) {
    if (word.length > 4) word = word.replace(/(ing|ed|s)$/, '');
    return word.replace(/e$/, '');
  }

  // Counts how often each (stemmed) word appears.
  function counts(text) {
    var out = Object.create(null);
    (text.toLowerCase().match(/[a-z0-9]+/g) || []).forEach(function (w) {
      if (w.length > 1 && !STOP[w]) {
        var s = stem(w);
        out[s] = (out[s] || 0) + 1;
      }
    });
    return out;
  }

  // Finds the site text that best matches the question. Returns null if no word matches.
  function search(question) {
    var wanted = Object.keys(counts(question));
    var chunks = window.SITE_CHUNKS || [];
    var best = null;
    var bestScore = 0;
    if (!wanted.length) return null;
    chunks.forEach(function (chunk) {
      var body = counts(chunk.text);
      var title = counts(chunk.title);
      var score = 0;
      wanted.forEach(function (w) {
        score += Math.min(body[w] || 0, 5) + (title[w] ? 3 : 0);
      });
      if (score > bestScore) {
        best = chunk;
        bestScore = score;
      }
    });
    return best;
  }

  function localAnswer(question) {
    if (/^\s*(hi|hello|hey|good (morning|afternoon|evening))\b/i.test(question)) {
      return { text: GREETING_REPLY };
    }
    if (/\b(are you|r u)\b.{0,20}\b(human|a person|a real person|a bot|a robot|ai)\b/i.test(question)) {
      return { text: IDENTITY_REPLY };
    }
    var chunk = search(question);
    if (!chunk) return { text: NO_MATCH };
    var text = chunk.text;
    if (text.length > 400) text = text.slice(0, 400).replace(/\s+\S*$/, '') + '...';
    return { text: text, href: chunk.url, label: 'Read more: ' + chunk.title };
  }

  var wrap = document.createElement('div');
  wrap.className = 'chat-widget';
  wrap.innerHTML =
    '<button type="button" class="chat-toggle" aria-expanded="false" aria-controls="chat-panel">' +
      '<span class="chat-dot" aria-hidden="true"></span>' +
      '<span>Chat with us</span>' +
    '</button>' +
    '<section class="chat-panel" id="chat-panel" aria-labelledby="chat-title" hidden>' +
      '<header class="chat-head">' +
        '<div>' +
          '<strong id="chat-title">Lesse Assistant</strong>' +
          '<div class="chat-status"><span class="chat-dot" aria-hidden="true"></span><span>Active now</span></div>' +
        '</div>' +
        '<button type="button" class="chat-close" aria-label="Close chat">&times;</button>' +
      '</header>' +
      '<div class="chat-log" aria-live="polite"></div>' +
      '<form class="chat-form">' +
        '<label for="chat-input" class="sr-only">Your message</label>' +
        '<textarea id="chat-input" rows="2" placeholder="Ask a question"></textarea>' +
        '<button type="submit" class="btn btn-small">Send</button>' +
      '</form>' +
      '<div class="chat-foot">' +
        '<span>Prefer a person?</span>' +
        '<a class="btn btn-small btn-whatsapp" href="' + WHATSAPP + '" target="_blank" rel="noopener">WhatsApp</a>' +
      '</div>' +
    '</section>';
  document.body.appendChild(wrap);

  var toggle = wrap.querySelector('.chat-toggle');
  var panel = wrap.querySelector('.chat-panel');
  var log = wrap.querySelector('.chat-log');
  var form = wrap.querySelector('.chat-form');
  var input = wrap.querySelector('#chat-input');
  var closeBtn = wrap.querySelector('.chat-close');
  var sendBtn = form.querySelector('button[type="submit"]');

  function addMessage(classes, text, href, label) {
    var el = document.createElement('p');
    el.className = 'msg ' + classes;
    el.textContent = text;
    if (href) {
      el.appendChild(document.createElement('br'));
      var link = document.createElement('a');
      link.href = href;
      link.textContent = label || href;
      el.appendChild(link);
    }
    log.appendChild(el);
    log.scrollTop = log.scrollHeight;
    return el;
  }

  addMessage('bot', GREETING);

  function openChat() {
    panel.hidden = false;
    toggle.setAttribute('aria-expanded', 'true');
    input.focus();
  }

  function closeChat() {
    panel.hidden = true;
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', function () {
    if (panel.hidden) { openChat(); } else { closeChat(); }
  });
  closeBtn.addEventListener('click', closeChat);
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !panel.hidden) closeChat();
  });

  // Resolves to { text, href?, label?, ai? }. Falls back to the site's own text on any AI failure.
  function askAssistant(question) {
    if (!cfg.aiEndpoint) {
      return Promise.resolve(localAnswer(question));
    }
    return fetch(cfg.aiEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: history.slice(-12) })
    })
      .then(function (res) {
        if (!res.ok) throw new Error('Assistant request failed');
        return res.json();
      })
      .then(function (data) {
        if (!data.reply) throw new Error('No reply');
        return { text: data.reply, ai: true };
      })
      .catch(function () {
        return localAnswer(question);
      });
  }

  function send() {
    var text = input.value.trim();
    if (!text) return;
    input.value = '';
    addMessage('user', text);
    history.push({ role: 'user', content: text });
    sendBtn.disabled = true;
    var typing = addMessage('bot typing', 'Typing...');

    askAssistant(text).then(function (reply) {
      typing.remove();
      addMessage('bot', reply.text, reply.href, reply.label);
      if (reply.ai) history.push({ role: 'assistant', content: reply.text });
      sendBtn.disabled = false;
      input.focus();
    });
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    send();
  });

  input.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      send();
    }
  });

  // Any element with data-open-chat opens the box, for example a "Chat now" button.
  document.addEventListener('click', function (event) {
    var opener = event.target.closest ? event.target.closest('[data-open-chat]') : null;
    if (opener) {
      event.preventDefault();
      openChat();
    }
  });
})();

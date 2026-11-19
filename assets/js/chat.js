// Chat box: an AI assistant that answers visitor questions, plus a WhatsApp button for a person.
// Settings come from assets/js/config.js.
(function () {
  'use strict';

  var cfg = window.SITE_CONFIG;
  if (!cfg || !cfg.whatsappNumber) return;

  var WHATSAPP = 'https://wa.me/' + cfg.whatsappNumber;
  var GREETING = "Hi, I'm Lesse's AI assistant. Ask me about our services, how a project works, or how to pay.";
  var NOT_CONNECTED = "I can't answer that right now. Please use the WhatsApp button below and we'll reply.";
  var ERROR_REPLY = "Sorry, the assistant couldn't answer just now. Please use the WhatsApp button below.";
  var history = [];

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

  function addMessage(classes, text) {
    var el = document.createElement('p');
    el.className = 'msg ' + classes;
    el.textContent = text;
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

  function askAssistant() {
    if (!cfg.aiEndpoint) {
      return Promise.resolve(NOT_CONNECTED);
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
        return data.reply || ERROR_REPLY;
      })
      .catch(function () {
        return ERROR_REPLY;
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

    askAssistant().then(function (reply) {
      typing.remove();
      addMessage('bot', reply);
      if (cfg.aiEndpoint) history.push({ role: 'assistant', content: reply });
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

  // Elements with data-open-chat (for example, the "Chat now" buttons on writer cards) open the box
  document.addEventListener('click', function (event) {
    var opener = event.target.closest ? event.target.closest('[data-open-chat]') : null;
    if (opener) {
      event.preventDefault();
      openChat();
    }
  });
})();

// Chat box: shows availability and sends a visitor's message to your WhatsApp.
// Availability and contact details come from assets/js/config.js.
(function () {
  'use strict';

  var cfg = window.SITE_CONFIG;
  if (!cfg || !cfg.whatsappNumber) return;

  var wrap = document.createElement('div');
  wrap.className = 'chat-widget';
  wrap.innerHTML =
    '<button type="button" class="chat-toggle" aria-expanded="false" aria-controls="chat-panel">' +
      '<span class="chat-dot" aria-hidden="true"></span>' +
      '<span class="chat-toggle-text"></span>' +
    '</button>' +
    '<section class="chat-panel" id="chat-panel" aria-labelledby="chat-title" hidden>' +
      '<header class="chat-head">' +
        '<div>' +
          '<strong id="chat-title"></strong>' +
          '<div class="chat-status">' +
            '<span class="chat-dot" aria-hidden="true"></span>' +
            '<span class="chat-status-text"></span>' +
          '</div>' +
        '</div>' +
        '<button type="button" class="chat-close" aria-label="Close chat">&times;</button>' +
      '</header>' +
      '<div class="chat-body"><p class="chat-bubble"></p></div>' +
      '<form class="chat-form">' +
        '<label for="chat-input" class="sr-only">Your message</label>' +
        '<textarea id="chat-input" rows="2" placeholder="Type your question"></textarea>' +
        '<button type="submit" class="btn btn-small">Send</button>' +
      '</form>' +
      '<p class="chat-foot">Your message opens a WhatsApp chat with us at <span class="chat-phone"></span>.</p>' +
    '</section>';
  document.body.appendChild(wrap);

  var toggle = wrap.querySelector('.chat-toggle');
  var panel = wrap.querySelector('.chat-panel');
  var closeBtn = wrap.querySelector('.chat-close');
  var form = wrap.querySelector('.chat-form');
  var input = wrap.querySelector('#chat-input');
  var bubble = wrap.querySelector('.chat-bubble');

  // Fill in text and status from config
  wrap.querySelector('.chat-toggle-text').textContent = cfg.available ? 'Chat with us' : 'Leave a message';
  wrap.querySelector('#chat-title').textContent = cfg.name || 'Chat';
  wrap.querySelector('.chat-status-text').textContent = cfg.available ? 'Available for chat now' : 'Away right now';
  wrap.querySelector('.chat-phone').textContent = cfg.phoneDisplay || '';
  wrap.querySelectorAll('.chat-dot').forEach(function (dot) {
    dot.classList.toggle('is-away', !cfg.available);
  });
  bubble.textContent = cfg.available
    ? "Hi, I'm available now. Tell me what you're working on and I'll reply on WhatsApp."
    : "I'm away at the moment. Leave a message and I'll reply on WhatsApp.";

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

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    var text = input.value.trim();
    if (!text) {
      input.focus();
      return;
    }
    var url = 'https://wa.me/' + cfg.whatsappNumber + '?text=' + encodeURIComponent(text);
    window.open(url, '_blank', 'noopener');
    input.value = '';
    bubble.textContent = 'Opening WhatsApp. If it does not open, message us at ' + (cfg.phoneDisplay || 'our number') + '.';
  });

  // Any element with data-open-chat (for example, the Chat now buttons) opens the box
  document.addEventListener('click', function (event) {
    var opener = event.target.closest ? event.target.closest('[data-open-chat]') : null;
    if (opener) {
      event.preventDefault();
      openChat();
    }
  });
})();

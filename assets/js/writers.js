// Writer listing: data and rendering.
// Add one object per writer. Set available to false for anyone not taking chats right now.
(function () {
  'use strict';

  var cfg = window.SITE_CONFIG || {};

  var WRITERS = [
    {
      name: 'Lesse',
      headline: 'Writing, research and editing support',
      categories: ['research', 'editing', 'formatting', 'proposals', 'business', 'career'],
      bio: 'Send a short description of your project and get a written quote before any work begins.',
      available: true
    }
  ];

  var CATEGORY_LABELS = {
    research: 'Research support',
    editing: 'Editing & proofreading',
    formatting: 'Citations & formatting',
    proposals: 'Proposals & grants',
    business: 'Business copy',
    career: 'Resumes & CVs'
  };

  var grid = document.getElementById('writer-grid');
  var filters = document.getElementById('filters');
  var count = document.getElementById('writer-count');
  if (!grid || !filters) return;

  function makeFilterButton(key, label) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'filter-btn';
    btn.dataset.filter = key;
    btn.textContent = label;
    btn.setAttribute('aria-pressed', key === 'all' ? 'true' : 'false');
    return btn;
  }

  function makeTag(text, extraClass) {
    var t = document.createElement('span');
    t.className = 'tag' + (extraClass ? ' ' + extraClass : '');
    t.textContent = text;
    return t;
  }

  function makeCard(writer) {
    var card = document.createElement('article');
    card.className = 'writer-card';

    var title = document.createElement('h3');
    title.textContent = writer.name;
    card.appendChild(title);

    var headline = document.createElement('p');
    headline.className = 'headline';
    headline.textContent = writer.headline;
    card.appendChild(headline);

    var bio = document.createElement('p');
    bio.className = 'bio';
    bio.textContent = writer.bio;
    card.appendChild(bio);

    var tags = document.createElement('div');
    tags.className = 'tags';
    if (cfg.available && writer.available) {
      tags.appendChild(makeTag('Available now', 'tag-available'));
    }
    writer.categories.forEach(function (key) {
      if (CATEGORY_LABELS[key]) tags.appendChild(makeTag(CATEGORY_LABELS[key]));
    });
    card.appendChild(tags);

    var actions = document.createElement('div');
    actions.className = 'writer-actions';
    if (cfg.whatsappNumber) {
      var chat = document.createElement('button');
      chat.type = 'button';
      chat.className = 'btn btn-small';
      chat.setAttribute('data-open-chat', '');
      chat.textContent = 'Chat now';
      actions.appendChild(chat);
    }
    if (cfg.email) {
      var mail = document.createElement('a');
      mail.href = 'mailto:' + cfg.email;
      mail.textContent = 'Email';
      actions.appendChild(mail);
    }
    card.appendChild(actions);

    return card;
  }

  function render(filterKey) {
    var list = WRITERS.filter(function (w) {
      return filterKey === 'all' || w.categories.indexOf(filterKey) !== -1;
    });
    grid.innerHTML = '';
    list.forEach(function (w) { grid.appendChild(makeCard(w)); });
    if (count) {
      count.textContent = list.length + (list.length === 1 ? ' writer' : ' writers');
    }
  }

  // Build filter buttons
  filters.appendChild(makeFilterButton('all', 'All'));
  Object.keys(CATEGORY_LABELS).forEach(function (key) {
    filters.appendChild(makeFilterButton(key, CATEGORY_LABELS[key]));
  });

  filters.addEventListener('click', function (event) {
    var btn = event.target.closest('.filter-btn');
    if (!btn) return;
    filters.querySelectorAll('.filter-btn').forEach(function (b) {
      b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
    });
    render(btn.dataset.filter);
  });

  render('all');
})();

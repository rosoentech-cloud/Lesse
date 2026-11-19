// Writer listing: data and rendering.
// Live writers have live: true. Reserved slots show "coming soon" until a real writer is added.
// To add a writer, replace a reserved slot with: name, headline, categories, bio, avatar, live: true.
(function () {
  'use strict';

  var cfg = window.SITE_CONFIG || {};

  var CATEGORY_LABELS = {
    research: 'Research support',
    editing: 'Editing & proofreading',
    formatting: 'Citations & formatting',
    proposals: 'Proposals & grants',
    business: 'Business copy',
    career: 'Resumes & CVs'
  };

  var WRITERS = [
    {
      name: 'Lesse',
      headline: 'Writing, research and editing support',
      categories: ['research', 'editing', 'formatting', 'proposals', 'business', 'career'],
      bio: 'Send a short description of your project and get a written quote before any work begins.',
      avatar: 'assets/img/avatar-lesse.svg',
      live: true
    }
  ];

  // Reserved slots 2 to 10
  for (var i = 2; i <= 10; i++) {
    WRITERS.push({
      name: 'Writer profile coming soon',
      headline: 'Details to be added',
      categories: [],
      bio: 'This space is reserved for a writer who has agreed to be listed.',
      avatar: 'assets/img/avatar-placeholder.svg',
      live: false
    });
  }

  var grid = document.getElementById('writer-grid');
  var filters = document.getElementById('filters');
  var count = document.getElementById('writer-count');
  if (!grid || !filters) return;

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function makeFilterButton(key, label) {
    var btn = el('button', 'filter-btn', label);
    btn.type = 'button';
    btn.dataset.filter = key;
    btn.setAttribute('aria-pressed', key === 'all' ? 'true' : 'false');
    return btn;
  }

  function makeCard(writer) {
    var card = el('article', 'writer-card' + (writer.live ? '' : ' writer-pending'));

    var head = el('div', 'writer-head');
    var img = el('img', 'avatar');
    img.src = writer.avatar;
    img.alt = writer.live ? writer.name + ' avatar' : 'Placeholder avatar';
    img.width = 64;
    img.height = 64;
    img.loading = 'lazy';
    head.appendChild(img);
    var titles = el('div');
    titles.appendChild(el('h3', '', writer.name));
    titles.appendChild(el('p', 'headline', writer.headline));
    head.appendChild(titles);
    card.appendChild(head);

    card.appendChild(el('p', 'bio', writer.bio));

    var tags = el('div', 'tags');
    if (writer.live && cfg.available) {
      tags.appendChild(el('span', 'tag tag-available', 'Available now'));
    }
    if (!writer.live) {
      tags.appendChild(el('span', 'tag tag-sample', 'Profile pending'));
    }
    writer.categories.forEach(function (key) {
      if (CATEGORY_LABELS[key]) tags.appendChild(el('span', 'tag', CATEGORY_LABELS[key]));
    });
    card.appendChild(tags);

    if (writer.live) {
      var actions = el('div', 'writer-actions');
      var chat = el('button', 'btn btn-small', 'Chat now');
      chat.type = 'button';
      chat.setAttribute('data-open-chat', '');
      actions.appendChild(chat);
      if (cfg.email) {
        var mail = el('a', '', 'Email');
        mail.href = 'mailto:' + cfg.email;
        actions.appendChild(mail);
      }
      card.appendChild(actions);
    }

    return card;
  }

  function render(filterKey) {
    var list = WRITERS.filter(function (w) {
      return filterKey === 'all' || w.categories.indexOf(filterKey) !== -1;
    });
    grid.innerHTML = '';
    list.forEach(function (w) { grid.appendChild(makeCard(w)); });
    if (count) {
      count.textContent = list.length + (list.length === 1 ? ' profile' : ' profiles');
    }
  }

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

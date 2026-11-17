// Lesse shared behaviour: mobile menu, current page marker, footer year,
// and background form submission with an on-page confirmation.
(function () {
  'use strict';

  // Footer year
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Mobile menu toggle
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  // Mark the current page in the header nav
  var here = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.site-nav a').forEach(function (link) {
    if (link.getAttribute('href') === here && !link.hasAttribute('aria-current')) {
      link.setAttribute('aria-current', 'page');
    }
  });

  function showStatus(el, message, isError) {
    if (!el) return;
    el.textContent = message;
    el.classList.toggle('form-error', !!isError);
    el.hidden = false;
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // Forms with data-ajax-form send in the background and show a message on the same page
  var cfg = window.SITE_CONFIG || {};
  document.querySelectorAll('form[data-ajax-form]').forEach(function (form) {
    var status = document.getElementById(form.getAttribute('data-status'));
    var successText = status ? status.textContent : '';
    var button = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      if (button) button.disabled = true;

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
        .then(function (res) {
          if (!res.ok) throw new Error('Request failed with status ' + res.status);
          form.reset();
          showStatus(status, successText, false);
        })
        .catch(function () {
          showStatus(
            status,
            'Your message was not sent. Please try again, or email ' + (cfg.email || 'us') + ' directly.',
            true
          );
        })
        .then(function () {
          if (button) button.disabled = false;
        });
    });
  });
})();

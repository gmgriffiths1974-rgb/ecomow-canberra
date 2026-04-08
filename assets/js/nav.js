// Mobile navigation toggle — progressive enhancement
(function () {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('mobile-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', function () {
    var expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    nav.setAttribute('aria-hidden', String(expanded));
  });

  // Close on link click
  nav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      toggle.setAttribute('aria-expanded', 'false');
      nav.setAttribute('aria-hidden', 'true');
    });
  });
})();

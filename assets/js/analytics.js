/* EcoMow Canberra — analytics + tap tracking
   One place to set the GA4 Measurement ID. Loads only on ecomowcanberra.com.au,
   so local previews and vercel.app URLs never send data. */
(function () {
  var GA_ID = 'G-JCEB9QR7MT';

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var live = /^G-[A-Z0-9]{6,}$/.test(GA_ID) && /(^|\.)ecomowcanberra\.com\.au$/.test(window.location.hostname);
  if (live) {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', GA_ID);
  }

  /* Where on the page was the button? Reported with every tap. */
  function location_of(a) {
    if (a.closest('.mobile-bar')) return 'sticky_mobile_bar';
    if (a.closest('.site-header')) return 'header';
    if (a.closest('.site-footer')) return 'footer';
    if (a.closest('.hero')) return 'hero';
    return 'body';
  }

  /* Tap-to-call, tap-to-SMS and the sticky bar Quote button, captured before navigation, sent via beacon. */
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href^="tel:"], a[href^="sms:"], a[href*="#quote-form"]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var name = href.indexOf('tel:') === 0 ? 'tap_to_call'
             : href.indexOf('sms:') === 0 ? 'tap_to_sms'
             : 'tap_to_quote';
    gtag('event', name, {
      link_location: location_of(a),
      page_path: window.location.pathname,
      link_text: (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      transport_type: 'beacon'
    });
  }, true);

  /* Quote form completion = landing on /thanks/ */
  if (window.location.pathname === '/thanks/' || window.location.pathname === '/thanks') {
    gtag('event', 'generate_lead', { method: 'quote_form' });
  }
})();

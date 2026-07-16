(function () {
  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('siteNav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  document.querySelectorAll('.dropdown > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var dd = btn.parentElement;
      var open = dd.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.dropdown.open').forEach(function (dd) {
      if (!dd.contains(e.target)) {
        dd.classList.remove('open');
        var b = dd.querySelector('button');
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
  });

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('visible'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('visible'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  items.forEach(function (el) { io.observe(el); });
})();

/* header: scroll'da koyulaş */
(function () {
  var head = document.querySelector('.site-head');
  if (!head) return;
  var update = function () {
    if (window.scrollY > 30) head.classList.add('solid');
    else head.classList.remove('solid');
  };
  update();
  window.addEventListener('scroll', update, { passive: true });
})();

/* sayaçlar */
(function () {
  var els = document.querySelectorAll('[data-count]');
  if (!els.length) return;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fmt = function (v, dec) { return dec ? v.toFixed(1).replace('.', ',') : Math.round(v).toString(); };
  var animate = function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var dec = el.getAttribute('data-count').indexOf('.') > -1;
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduced) { el.textContent = fmt(target, dec) + suffix; return; }
    var t0 = null, dur = 1600;
    var tick = function (t) {
      if (!t0) t0 = t;
      var p = Math.min(1, (t - t0) / dur);
      p = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * p, dec) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if (!('IntersectionObserver' in window)) { els.forEach(animate); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { animate(en.target); io.unobserve(en.target); }
    });
  }, { threshold: 0.4 });
  els.forEach(function (el) { io.observe(el); });
})();

/* video kartları: tıkla → yükle */
(function () {
  document.querySelectorAll('.vid-card[data-yt]').forEach(function (card) {
    card.addEventListener('click', function () {
      var id = card.getAttribute('data-yt');
      var thumb = card.querySelector('.vid-thumb');
      if (!thumb || card.querySelector('iframe')) return;
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
      f.title = card.querySelector('h3') ? card.querySelector('h3').textContent : 'Video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      thumb.replaceWith(f);
    });
  });
})();

/* WA lead formları */
(function () {
  document.querySelectorAll('.wa-form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var ad = (f.querySelector('[name=ad]') || {}).value || '';
      var tel = (f.querySelector('[name=tel]') || {}).value || '';
      var sel = f.querySelector('[name=konu]');
      var konu = sel ? sel.value : (f.getAttribute('data-konu') || 'Randevu');
      var msg = 'Merhaba, ben ' + ad.trim() + '. ' + konu + ' hakkında bilgi ve randevu talep ediyorum. Telefon numaram: ' + tel.trim();
      window.open('https://wa.me/905439136595?text=' + encodeURIComponent(msg), '_blank', 'noopener');
    });
  });
})();

/* öncesi/sonrası slider */
(function () {
  document.querySelectorAll('.ba-slider').forEach(function (sl) {
    var range = sl.querySelector('.ba-range');
    if (!range) return;
    range.addEventListener('input', function () {
      sl.style.setProperty('--pos', range.value + '%');
    });
  });
})();

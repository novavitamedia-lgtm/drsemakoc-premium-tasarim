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

/* motion paketi */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) return;

  /* scroll ilerleme */
  var bar = document.createElement('div');
  bar.className = 'scroll-progress';
  document.body.appendChild(bar);
  var onScroll = function () {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* hero cursor ışıltısı */
  var hero = document.querySelector('.hero3');
  if (hero && window.matchMedia('(pointer: fine)').matches) {
    var glow = document.createElement('div');
    glow.className = 'cursor-glow';
    hero.appendChild(glow);
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      glow.style.left = (e.clientX - r.left) + 'px';
      glow.style.top = (e.clientY - r.top) + 'px';
    });
  }

  /* kelime kelime başlık reveal */
  var h1 = document.querySelector('.hero3 h1');
  if (h1 && !h1.dataset.split) {
    h1.dataset.split = '1';
    var wi = 0;
    var splitNode = function (node) {
      if (node.nodeType === 3) {
        var frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (/^\s+$/.test(part) || part === '') { frag.appendChild(document.createTextNode(part)); return; }
          var sp = document.createElement('span');
          sp.className = 'w';
          sp.style.setProperty('--wi', wi++);
          sp.textContent = part;
          frag.appendChild(sp);
        });
        node.parentNode.replaceChild(frag, node);
      } else if (node.nodeType === 1) {
        [].slice.call(node.childNodes).forEach(splitNode);
      }
    };
    [].slice.call(h1.childNodes).forEach(splitNode);
    h1.classList.remove('fade-rise-d1');
    h1.style.animation = 'none';
    h1.style.opacity = '1';
    h1.style.transform = 'none';
    h1.classList.add('word-reveal');
  }

  /* manyetik altın butonlar */
  if (window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.btn-gold').forEach(function (btn) {
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.15;
        var y = (e.clientY - r.top - r.height / 2) * 0.25;
        btn.style.transform = 'translate(' + x + 'px, ' + (y - 2) + 'px)';
      });
      btn.addEventListener('pointerleave', function () { btn.style.transform = ''; });
    });

    /* 3D tilt kartlar */
    document.querySelectorAll('.pcard, .svc').forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        var rx = ((e.clientY - r.top) / r.height - 0.5) * -5;
        var ry = ((e.clientX - r.left) / r.width - 0.5) * 5;
        card.style.transform = 'perspective(800px) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg) translateY(-5px)';
      });
      card.addEventListener('pointerleave', function () { card.style.transform = ''; });
    });
  }
})();

/* yorum slider okları */
(function () {
  document.querySelectorAll('.rev-slider-wrap').forEach(function (wrap) {
    var sl = wrap.querySelector('.rev-slider');
    wrap.querySelectorAll('.rev-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var card = sl.querySelector('.rev-card');
        var w = card ? card.getBoundingClientRect().width + 16 : 350;
        sl.scrollBy({ left: w * parseInt(btn.getAttribute('data-dir'), 10), behavior: 'smooth' });
      });
    });
  });
})();

/* yorum slider: yavaş otomatik kayma (sonsuz döngü, hover'da durur) */
(function () {
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) return;
  document.querySelectorAll('.rev-slider').forEach(function (sl) {
    var kids = [].slice.call(sl.children);
    kids.forEach(function (k) { sl.appendChild(k.cloneNode(true)); });
    var half = 0, paused = false, idleTimer = null;
    var calcHalf = function () { half = sl.scrollWidth / 2; };
    calcHalf();
    window.addEventListener('resize', calcHalf);
    var pause = function () {
      paused = true;
      clearTimeout(idleTimer);
      idleTimer = setTimeout(function () { paused = false; }, 3500);
    };
    ['pointerenter', 'pointerdown', 'touchstart', 'wheel', 'focusin'].forEach(function (ev) {
      sl.addEventListener(ev, pause, { passive: true });
    });
    sl.closest('.rev-slider-wrap').querySelectorAll('.rev-btn').forEach(function (b) {
      b.addEventListener('click', pause);
    });
    var pos = sl.scrollLeft;
    ['pointerdown', 'wheel', 'touchstart'].forEach(function (ev) {
      sl.addEventListener(ev, function () { pos = sl.scrollLeft; }, { passive: true });
    });
    var tick = function () {
      if (!paused) {
        pos += 0.5;
        if (half > 0 && pos >= half) pos -= half;
        sl.scrollLeft = pos;
      } else {
        pos = sl.scrollLeft;
      }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
})();

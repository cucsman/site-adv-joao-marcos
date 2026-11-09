/* JMB v2 — interações e animações de scroll (GSAP + ScrollTrigger + Lenis). */
(function () {
  var d = document, root = d.documentElement;

  // menu, idioma, header
  var burger = d.getElementById('burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = root.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open);
      if (window.__lenis) window.__lenis[open ? 'stop' : 'start']();
    });
    d.querySelectorAll('#nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        root.classList.remove('menu-open'); burger.setAttribute('aria-expanded', false);
        if (window.__lenis) window.__lenis.start();
      });
    });
  }
  d.querySelectorAll('[data-setlang]').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('jmb-lang', a.getAttribute('data-setlang')); } catch (e) {} });
  });
  var hd = d.querySelector('.hd');
  function onScroll() { hd.classList.toggle('scrolled', window.scrollY > 24); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!window.gsap || !window.ScrollTrigger) { root.classList.add('static'); return; }
  // se o fallback de 3s já marcou .static (rede lenta), volta a animar
  root.classList.remove('static');
  root.classList.add('motion');
  // "Reduzir movimento" ligado no aparelho: layout fixo, só os textos surgindo (sem zoom, sem telas presas)
  if (reduce) root.classList.add('static');
  gsap.registerPlugin(ScrollTrigger);

  // rolagem suave (só mouse/trackpad; no toque fica o nativo)
  var lenis = null;
  if (!reduce && window.Lenis && !window.matchMedia('(pointer: coarse)').matches) {
    lenis = new Lenis({ duration: 1.15, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    window.__lenis = lenis;
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  // âncoras da mesma página (#contato, /pt/index.html#contato em /pt): rola sem recarregar
  var norm = function (p) { return p.replace(/(\/index)?(\.html)?\/?$/, ''); };
  var goTo = function (el) {
    if (lenis) lenis.scrollTo(el);
    else window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY, behavior: 'smooth' });
  };
  d.querySelectorAll('a[href*="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (!a.hash || norm(a.pathname) !== norm(location.pathname)) return;
      var el = d.getElementById(a.hash.slice(1));
      if (!el) return;
      e.preventDefault();
      root.classList.remove('menu-open'); if (burger) burger.setAttribute('aria-expanded', false);
      if (lenis) lenis.start();
      goTo(el);
    });
  });

  var ease = 'power3.out';

  // texto e blocos surgem ao entrar na tela
  gsap.utils.toArray('[data-r]').forEach(function (el) {
    gsap.fromTo(el, { opacity: 0, y: reduce ? 0 : 36 }, { opacity: 1, y: 0, duration: 1.1, ease: ease,
      scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
  });

  // título que acende palavra por palavra conforme o scroll
  gsap.utils.toArray('[data-words]').forEach(function (h) {
    var words = [];
    (function split(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = d.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (w) {
            if (!w) return;
            if (/^\s+$/.test(w)) { frag.appendChild(d.createTextNode(w)); return; }
            var s = d.createElement('span'); s.textContent = w; words.push(s); frag.appendChild(s);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') { split(n); }
      });
    })(h);
    gsap.fromTo(words, { opacity: 0.14 }, { opacity: 1, stagger: 0.1, ease: 'none',
      scrollTrigger: { trigger: h, start: 'top 82%', end: 'bottom 52%', scrub: true } });
  });

  // fotos que se revelam de baixo para cima
  if (!reduce) gsap.utils.toArray('[data-curtain]').forEach(function (f) {
    var img = f.querySelector('img');
    var tl = gsap.timeline({ scrollTrigger: { trigger: f, start: 'top 85%', once: true } });
    tl.fromTo(f, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.5, ease: 'expo.out' })
      .fromTo(img, { scale: 1.25 }, { scale: 1, duration: 2, ease: 'expo.out' }, 0);
  });

  if (reduce) { window.addEventListener('load', function () { ScrollTrigger.refresh(); }); return; }

  var mm = gsap.matchMedia();

  // HERO: a foto encolhe e vira peça de um mosaico que desce e se forma
  var stage = d.querySelector('.stage');
  if (stage) {
    var inner = stage.querySelector('.stage-in'), hero = stage.querySelector('.t-hero'),
        shade = hero.querySelector('.shade'), zw = hero.querySelector('.zw'), cell = stage.querySelector('.cell-hero'),
        start = stage.querySelector('.ph-start'), more = stage.querySelector('.stage-more'),
        tiles = stage.querySelectorAll('.mosaic .tile:not(.t-hero)');
    var rect = function (el) {
      var a = el.getBoundingClientRect(), b = hero.offsetParent.getBoundingClientRect();
      return { left: a.left - b.left, top: a.top - b.top, width: a.width, height: a.height };
    };
    mm.add('(min-width: 900px)', function () {
      var tl = gsap.timeline({ scrollTrigger: { trigger: inner, start: 'top top', end: '+=150%', pin: true, scrub: 1, invalidateOnRefresh: true } });
      tl.fromTo(hero,
        { left: function () { return rect(start).left; }, top: function () { return rect(start).top; },
          width: function () { return rect(start).width; }, height: function () { return rect(start).height; }, borderRadius: 0 },
        { left: function () { return rect(cell).left; }, top: function () { return rect(cell).top; },
          width: function () { return rect(cell).width; }, height: function () { return rect(cell).height; }, borderRadius: 3,
          ease: 'power2.inOut', duration: 1 }, 0)
        .fromTo(zw, { scale: 1.2 }, { scale: 1, ease: 'power2.inOut', duration: 1 }, 0)
        .fromTo(shade, { opacity: 1 }, { opacity: 0, duration: 0.5 }, 0)
        .fromTo(tiles, { y: function (i) { return -window.innerHeight * (0.7 + (i % 3) * 0.15); }, opacity: 0 },
          { y: 0, opacity: 1, ease: 'power3.out', duration: 0.75, stagger: 0.07 }, 0.2)
        .fromTo(more, { opacity: 0, y: 28 }, { opacity: 1, y: 0, duration: 0.45 }, 0.55);
      return function () { gsap.set([hero, zw, shade, tiles, more], { clearProps: 'all' }); };
    });
    mm.add('(max-width: 899px)', function () {
      gsap.fromTo(tiles, { y: -70, opacity: 0 }, { y: 0, opacity: 1, duration: 1.1, ease: ease, stagger: 0.12,
        scrollTrigger: { trigger: stage.querySelector('.mosaic'), start: 'top 80%', once: true } });
      gsap.fromTo(hero.querySelector('img'), { scale: 1.3 }, { scale: 1, duration: 2.2, ease: 'expo.out' });
      gsap.fromTo(stage.querySelector('.stage-lead'), { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 1.2, delay: 0.25, ease: ease });
      gsap.fromTo(zw, { scale: 1 }, { scale: 1.25, ease: 'none', immediateRender: false,
        scrollTrigger: { trigger: hero, start: 'top top', end: 'bottom top', scrub: true } });
      gsap.fromTo(stage.querySelector('.stage-more'), { opacity: 0, y: 36 }, { opacity: 1, y: 0, duration: 1.1, ease: ease,
        scrollTrigger: { trigger: stage.querySelector('.stage-more'), start: 'top 90%', once: true } });
      return function () { gsap.set([zw, hero.querySelector('img')], { clearProps: 'all' }); };
    });
  }

  // ÁREAS: painéis empilhados; o anterior recua quando o próximo sobe
  // (gatilhos medidos no .stack, que não é sticky: medir o próprio painel preso dá posição errada)
  var stack = d.querySelector('.stack'), panels = gsap.utils.toArray('.panel');
  var at = function (i, pos) {
    return function () {
      var p = panels[0], step = p.offsetHeight + parseFloat(getComputedStyle(p).marginBottom);
      return 'top+=' + Math.round(i * step) + ' ' + pos;
    };
  };
  panels.forEach(function (p, i) {
    gsap.fromTo(p.querySelector('img'), { scale: 1.45 }, { scale: 1, ease: 'none',
      scrollTrigger: { trigger: stack, start: at(i, 'bottom'), end: at(i, 'top'), scrub: true, invalidateOnRefresh: true } });
    gsap.fromTo(p.querySelector('.panel-tx'), { opacity: 0, y: 50 }, { opacity: 1, y: 0, ease: 'none',
      scrollTrigger: { trigger: stack, start: at(i, '75%'), end: at(i, '15%'), scrub: true, invalidateOnRefresh: true } });
    if (i < panels.length - 1) {
      gsap.to(p.querySelector('.panel-in'), { scale: 0.9, opacity: 0.3, ease: 'none',
        scrollTrigger: { trigger: stack, start: at(i + 1, 'bottom'), end: at(i + 1, 'top'), scrub: true, invalidateOnRefresh: true } });
    }
  });

  // MÍDIA: rolagem horizontal presa à tela (desktop)
  mm.add('(min-width: 900px)', function () {
    var sec = d.querySelector('.hscroll'), track = sec && sec.querySelector('.hs-track');
    if (!track) return;
    var dist = function () { return Math.max(0, track.scrollWidth - window.innerWidth); };
    gsap.to(track, { x: function () { return -dist(); }, ease: 'none',
      scrollTrigger: { trigger: sec, start: 'top top', end: function () { return '+=' + dist(); }, pin: true, scrub: 1, invalidateOnRefresh: true } });
  });

  // vindo de outra página com #âncora: a animação do topo muda a altura, então reposiciona depois de medir
  window.addEventListener('load', function () {
    ScrollTrigger.refresh();
    var el = location.hash && d.getElementById(location.hash.slice(1));
    if (el) {
      requestAnimationFrame(function () {
        var y = el.getBoundingClientRect().top + window.scrollY;
        window.scrollTo(0, y);
        if (lenis) { lenis.resize(); lenis.scrollTo(y, { immediate: true, force: true }); }
      });
    }
  });
})();

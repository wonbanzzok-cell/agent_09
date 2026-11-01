// LEGODT brand page v1 — progressive enhancement only.
(() => {
  'use strict';

  const root = document.documentElement;
  root.classList.add('js');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const desktop = window.matchMedia('(min-width: 1024px)');

  /* ---------- mobile nav ---------- */
  const toggle = document.querySelector('.pill-nav__toggle');
  const menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    const setOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      menu.classList.toggle('is-open', open);
      toggle.querySelector('.visually-hidden').textContent = open ? '메뉴 닫기' : '메뉴 열기';
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  }

  /* ---------- reveal on scroll ---------- */
  const revealEls = document.querySelectorAll('.reveal, .timeline');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------- TUMGGU builder ---------- */
  const builder = document.querySelector('.builder');
  const steps = Array.from(document.querySelectorAll('.step'));
  const layers = builder ? Array.from(builder.querySelectorAll('.builder__layer')) : [];

  const showStep = (n) => {
    layers.forEach((layer) => layer.classList.toggle('is-on', Number(layer.dataset.layer) <= n));
    steps.forEach((step) => step.classList.toggle('is-active', Number(step.dataset.step) === n));
    if (builder) builder.dataset.step = String(n);
  };

  if (builder && steps.length && 'IntersectionObserver' in window) {
    let stepObserver = null;
    const setupSteps = () => {
      if (stepObserver) { stepObserver.disconnect(); stepObserver = null; }
      if (!desktop.matches) {
        showStep(5);
        steps.forEach((s) => s.classList.remove('is-active'));
        return;
      }
      showStep(1);
      stepObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) showStep(Number(entry.target.dataset.step));
        });
      }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
      steps.forEach((s) => stepObserver.observe(s));
    };
    setupSteps();
    desktop.addEventListener('change', setupSteps);
  } else {
    showStep(5);
  }

  /* ---------- filter tabs (lineup + timeline) ---------- */
  const bindFilter = (group, attr, itemsSelector) => {
    if (!group) return;
    const tabs = Array.from(group.querySelectorAll('.tab'));
    const items = Array.from(document.querySelectorAll(itemsSelector));
    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const value = tab.dataset[attr];
        tabs.forEach((t) => {
          const on = t === tab;
          t.classList.toggle('is-active', on);
          t.setAttribute('aria-pressed', String(on));
        });
        items.forEach((item) => {
          const key = attr === 'filter' ? item.dataset.cat : item.dataset.region;
          item.hidden = !(value === 'all' || key === value);
        });
        const timelineEl = document.querySelector('.timeline');
        if (attr === 'region' && timelineEl) timelineEl.classList.toggle('is-filtered', value !== 'all');
      });
    });
  };
  bindFilter(document.querySelector('#lineup .tabs'), 'filter', '.product');
  bindFilter(document.querySelector('#popup .tabs'), 'region', '.ticket');

  /* ---------- color swatches ---------- */
  document.querySelectorAll('.product').forEach((card) => {
    const media = card.querySelector('.product__media');
    const name = card.querySelector('.swatch-name');
    const swatches = Array.from(card.querySelectorAll('.swatch'));
    swatches.forEach((sw) => {
      sw.addEventListener('click', () => {
        Array.from(media.classList)
          .filter((c) => c.startsWith('tint-'))
          .forEach((c) => media.classList.remove(c));
        media.classList.add(`tint-${sw.dataset.tint}`);
        swatches.forEach((s) => {
          const on = s === sw;
          s.classList.toggle('is-active', on);
          s.setAttribute('aria-pressed', String(on));
        });
        if (name) name.textContent = sw.textContent.trim();
      });
    });
  });

  /* ---------- draggable timeline (desktop) ---------- */
  const timeline = document.querySelector('.timeline');
  if (timeline) {
    let startX = 0;
    let startScroll = 0;
    let dragging = false;
    timeline.addEventListener('pointerdown', (e) => {
      if (!desktop.matches || e.pointerType !== 'mouse') return;
      dragging = true;
      startX = e.clientX;
      startScroll = timeline.scrollLeft;
      timeline.classList.add('is-dragging');
    });
    window.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      timeline.scrollLeft = startScroll - (e.clientX - startX);
    });
    window.addEventListener('pointerup', () => {
      dragging = false;
      timeline.classList.remove('is-dragging');
    });
    timeline.addEventListener('keydown', (e) => {
      if (!desktop.matches) return;
      const step = 320;
      if (e.key === 'ArrowRight') { timeline.scrollBy({ left: step, behavior: reduceMotion.matches ? 'auto' : 'smooth' }); e.preventDefault(); }
      if (e.key === 'ArrowLeft') { timeline.scrollBy({ left: -step, behavior: reduceMotion.matches ? 'auto' : 'smooth' }); e.preventDefault(); }
    });
  }
})();

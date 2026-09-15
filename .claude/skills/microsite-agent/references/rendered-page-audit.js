/* Rendered-page audit — paste into javascript_exec against a page served
   over a real local HTTP server (python -m http.server), not a file:// URL.

   Catches the things static checks can't see, because they only exist once
   CSS has actually cascaded:
     - text whose colour is too close to whatever is actually behind it
       (the real bug: a global .muted utility used inside a dark footer)
     - inline SVGs that blew up to full container width because no sizing
       rule matched them
     - horizontal overflow
     - links with no real destination

   Every finding here is a real defect. Fix, bump ?v=N, reload, re-run. */
(function () {
  function lum(c) {
    const m = c.match(/\d+/g).map(Number);
    const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); };
    return .2126 * f(m[0]) + .7152 * f(m[1]) + .0722 * f(m[2]);
  }
  function bgOf(el) {
    let e = el;
    while (e) {
      const c = getComputedStyle(e).backgroundColor;
      if (c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c)) return c;
      e = e.parentElement;
    }
    return 'rgb(255,255,255)';
  }

  const lowContrast = [];
  document.querySelectorAll('a,p,li,h1,h2,h3,h4,span,summary,strong,label,button').forEach(el => {
    if (!el.textContent.trim() || el.offsetParent === null) return;
    // only judge elements that own their text, not wrappers
    if (el.children.length && !(el.childNodes[0] && el.childNodes[0].nodeValue || '').trim()) return;
    const r = (() => {
      const a = lum(getComputedStyle(el).color), b = lum(bgOf(el));
      return (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
    })();
    if (r < 3) lowContrast.push({ text: el.textContent.trim().slice(0, 45), ratio: +r.toFixed(2) });
  });

  const oversizedSvgs = [...document.querySelectorAll('svg')]
    .filter(s => s.getBoundingClientRect().width > 80)
    .map(s => ({ width: Math.round(s.getBoundingClientRect().width), inside: s.parentElement.className || s.parentElement.tagName }));

  const deadLinks = [...document.querySelectorAll('a')]
    .filter(a => { const h = a.getAttribute('href'); return !h || h === '#' || !h.trim(); })
    .map(a => a.textContent.trim().slice(0, 30));

  return JSON.stringify({
    lowContrast,
    oversizedSvgs,
    deadLinks,
    horizontalOverflow: document.documentElement.scrollWidth > window.innerWidth,
    stylesheetVersions: [...document.querySelectorAll('link[href*=".css"]')].map(l => l.getAttribute('href')),
  }, null, 1);
})();

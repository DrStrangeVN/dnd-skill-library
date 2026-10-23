#!/usr/bin/env node
/* QA for pil-signal-deck.html
   A: structure + node --check on every inline script
   B: pil-ring.js component (deck theme, onHover) with a fake echarts
   C: full page in jsdom with a stubbed PILRing: search -> brief, connected
      rail, citations, chord/topic/hover callbacks, suggestions, themes
*/
'use strict';
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { JSDOM, VirtualConsole } = require('jsdom');

const HERE = __dirname;
const HTML = fs.readFileSync(path.join(HERE, 'pil-signal-deck.html'), 'utf8');
let pass = 0, fail = 0;
function ok(cond, name) {
  if (cond) { pass++; /* console.log('  ok  ' + name); */ }
  else { fail++; console.log('  FAIL ' + name); }
}
function section(t) { console.log('\n== ' + t + ' =='); }

// ---------------- A: structure ----------------
section('A structure');
for (const id of ['ring-mount', 'q', 'cmdStatus', 'scopeReadout', 'themeSeg',
  'brief', 'briefEmpty', 'briefBody', 'briefQuery', 'briefMeta', 'briefGround',
  'briefContent', 'briefFollow', 'connList', 'connCount',
  'rooms', 'tags', 'title', 'count', 'sort', 'featured', 'grid', 'empty', 'more',
  'archive', 'phonepanel']) {
  ok(HTML.includes(`id="${id}"`), 'has #' + id);
}
ok(!HTML.includes('id="index"'), 'no standalone index section');
ok(/id="brief"[\s\S]*id="rooms"[\s\S]*id="archive"/.test(HTML), 'index rail lives inside the brief, archive right below');
ok(!HTML.includes('<div class="masthead">'), 'no masthead');
ok(!HTML.includes('<div class="body">'), 'no .body');
ok(!HTML.includes('id="answers"'), 'no #answers');
ok(HTML.split('id="phonepanel"').length === 2, 'one phonepanel');
ok(HTML.split('id="q"').length === 2, 'one #q');
ok(HTML.includes('SIGNAL DECK'), 'deck branding');
ok(HTML.includes('Everything you saved.'), 'hero headline');
ok(HTML.includes('width:100vw;margin-left:calc(50% - 50vw)'), 'full-bleed sections');
ok(!HTML.includes('__ECHARTS_JS__') && !HTML.includes('__SUGGEST__'), 'no leftover tokens');

// inline scripts
const scripts = [];
HTML.replace(/<script(?![^>]*\bsrc\b)(?![^>]*type="application\/json")([^>]*)>([\s\S]*?)<\/script>/g, (m, attrs, body) => {
  scripts.push({ attrs, body });
  return m;
});
ok(scripts.length === 4, 'four inline scripts, got ' + scripts.length);
const [sExport, sEcharts, sRing, sSignal] = scripts;
ok(/renderRooms/.test(sExport.body), 'script[0] is the export app');
ok(sEcharts.body.length > 500000, 'script[1] is echarts (' + sEcharts.body.length + ')');
ok(/PILRing/.test(sRing.body) && /function mount/.test(sRing.body), 'script[2] is pil-ring');
ok(/PILRing\.mount/.test(sSignal.body), 'script[3] is the signal init');
ok(HTML.includes('id="ring-data"'), 'ring data block present');

section('A node --check');
scripts.forEach((s, i) => {
  const tmp = `/tmp/sig-check-${i}.js`;
  fs.writeFileSync(tmp, s.body);
  try { execSync(`node --check ${tmp}`, { stdio: 'pipe' }); ok(true, 'script[' + i + '] syntax'); }
  catch (e) { ok(false, 'script[' + i + '] syntax: ' + e.message.slice(0, 200)); }
});

// ---------------- B: component ----------------
section('B component (deck theme + onHover + setMatches + wheel)');
(async () => {
  const vc = new VirtualConsole();
  const dom = new JSDOM('<!doctype html><body><div id="m"></div></body>', {
    pretendToBeVisual: true,
    runScripts: 'outside-only', virtualConsole: vc,
    beforeParse(window) {
      const handlers = {};
      const zrHandlers = {};
      window.__handlers = handlers; window.__zrHandlers = zrHandlers;
      window.echarts = {
        init() {
          return {
            setOption() {}, dispatchAction() {}, resize() {}, dispose() {},
            on(ev, q, fn) { handlers[ev] = fn; },
            getZr() { return { on(ev, fn) { zrHandlers[ev] = fn; } }; },
          };
        },
      };
    },
  });
  const { window } = dom;
  window.eval(fs.readFileSync(path.join(HERE, 'ring-component', 'pil-ring.js'), 'utf8'));
  const seen = [];
  const ring = window.eval(`PILRing.mount(document.getElementById('m'), {
    data: { nodes: [{ id: 'a', label: 'alpha', count: 10, value: 1, color: '#fff' },
                    { id: 'b', label: 'beta', count: 4, value: 0.5, color: '#fff' }],
            edges: [{ from: 'a', to: 'b', cosine: 0.4, value: 2 }], folders: {} },
    maxCosine: 0.5, theme: 'deck',
    onHover(n){ (window.__seen = window.__seen || []).push(n ? n.id : null); },
  })`);
  ok(ring.getTheme() === 'deck', 'deck is the active theme');
  ring.setTheme('gallery');
  ok(ring.getTheme() === 'gallery', 'setTheme switches');
  ring.setTheme('deck');
  const mouseover = window.__handlers.mouseover, mouseout = window.__handlers.mouseout;
  ok(typeof mouseover === 'function' && typeof mouseout === 'function', 'hover handlers wired');
  mouseover({ dataType: 'node', data: { id: 'a' } });
  mouseout({ dataType: 'node' });
  mouseover({ dataType: 'edge' });
  const got = window.__seen || [];
  ok(got.length === 2 && got[0] === 'a' && got[1] === null, 'onHover(node) then onHover(null), edge ignored: ' + JSON.stringify(got));

  // setMatches: search-result highlighting on the ring
  const setOpts = [];
  const chart2 = { setOption(o){ setOpts.push(o); }, dispatchAction(){}, resize(){}, dispose(){},
    on(ev, q, fn){ window.__handlers[ev] = fn; }, getZr(){ return { on(){} }; } };
  window.echarts.init = () => chart2;
  const ring2 = window.eval(`PILRing.mount(document.getElementById('m'), {
    data: { nodes: [{ id: 'a', label: 'alpha', count: 10, value: 1, color: '#fff' },
                    { id: 'b', label: 'beta', count: 4, value: 0.5, color: '#fff' }],
            edges: [{ from: 'a', to: 'b', cosine: 0.4, value: 2 }], folders: {} },
    maxCosine: 0.5 })`);
  ring2.setMatches(['a']);
  const d1 = setOpts[setOpts.length - 1].series[0];
  const na = d1.data.find(x => x.id === 'a'), nb = d1.data.find(x => x.id === 'b');
  ok(na.itemStyle.opacity === 1 && nb.itemStyle.opacity === 0.08, 'matched node lit, other dimmed');
  ok(nb.label.opacity === 0.12, 'dimmed node label faded');
  ok(d1.edges[0].lineStyle.opacity === 1, 'edge touching a match stays lit');
  ring2.setMatches(['zzz']);
  const d2 = setOpts[setOpts.length - 1].series[0];
  ok(d2.data.every(x => x.itemStyle.opacity === 0.08), 'no-match search dims everything');
  ok(d2.edges[0].lineStyle.opacity === 0.05, 'edges dim when neither end matches');
  ring2.setMatches(null);
  const d3 = setOpts[setOpts.length - 1].series[0];
  ok(d3.data.every(x => x.itemStyle.opacity === 1), 'setMatches(null) restores the full ring');

  // wheel: click the ring, then scroll to rotate (down = clockwise)
  const order0 = setOpts[setOpts.length - 1].series[0].data.map(x => x.id).join(',');
  const mEl = window.document.getElementById('m');
  function wheel(deltaY, ctrl) {
    const e = new window.Event('wheel', { bubbles: true, cancelable: true });
    e.deltaY = deltaY; e.ctrlKey = !!ctrl;
    mEl.dispatchEvent(e);
  }
  const nBefore = setOpts.length;
  wheel(60); // not armed: ECharts keeps zoom, no rotation
  await new Promise(r => setTimeout(r, 80));
  ok(setOpts.length === nBefore, 'unarmed wheel does not rotate');
  const nOpts0 = setOpts.length;
  mEl.dispatchEvent(new window.Event('pointerdown', { bubbles: true }));
  wheel(60); // one step of rotation
  await new Promise(r => setTimeout(r, 80));
  const order1 = setOpts[setOpts.length - 1].series[0].data.map(x => x.id).join(',');
  ok(setOpts.length > nOpts0 && order1 !== order0, 'armed scroll rotates the ring (down=clockwise)');
  const nOpts1 = setOpts.length;
  wheel(60, true); // pinch: passes through to zoom
  await new Promise(r => setTimeout(r, 80));
  ok(setOpts.length === nOpts1, 'ctrl+wheel does not rotate (pinch zoom preserved)');
  mEl.dispatchEvent(new window.Event('pointerleave', { bubbles: true }));
  wheel(60);
  await new Promise(r => setTimeout(r, 80));
  ok(setOpts.length === nOpts1, 'pointerleave disarms scroll-rotate');

  ring.destroy(); ring2.destroy();
  ok(true, 'destroy ok');
})().catch(e => { console.log('HARNESS ERROR (B)', e); process.exit(2); });

// ---------------- C: page ----------------
section('C page integration');
(async () => {
  // strip the heavy ring scripts; stub PILRing instead
  const idx = { echarts: 1, ring: 2 };
  let testHtml = HTML;
  for (const k of ['ring', 'echarts']) {
    const s = scripts[idx[k]];
    const tag = `<script${s.attrs}>${s.body}</script>`;
    ok(testHtml.includes(tag.slice(0, 80)), 'locating script[' + idx[k] + '] for removal');
    testHtml = testHtml.replace(tag, '<!-- removed for test -->');
  }
  const errors = [];
  const vc = new VirtualConsole();
  vc.on('jsdomError', e => errors.push('jsdomError: ' + e.message));
  const cbs = {};
  const dom = new JSDOM(testHtml, {
    runScripts: 'dangerously', virtualConsole: vc,
    beforeParse(window) {
      window.__cbs = cbs;
      window.PILRing = {
        mount(el, opts) {
          Object.assign(cbs, { onSelect: opts.onSelect, onEdge: opts.onEdge, onHover: opts.onHover });
          cbs.theme = opts.theme;
          cbs.lit = null;
          return {
            setTheme(t) { cbs.theme = t; },
            getTheme() { return cbs.theme; },
            setMatches(ids) { cbs.lit = ids && ids.length ? ids : null; },
            resize() {}, dispose() {},
          };
        },
      };
      window.__scrolls = [];
      window.Element.prototype.scrollIntoView = function () { window.__scrolls.push(this.id || this.className); };
      window.fetch = () => Promise.resolve({ ok: false });
    },
  });
  const { window } = dom;
  const { document } = window;
  window.addEventListener('error', e => errors.push('window error: ' + e.message));
  await new Promise(r => setTimeout(r, 300));

  const $ = id => document.getElementById(id);
  ok(cbs.theme === 'deck', 'ring mounted with deck theme');
  ok($('briefEmpty').style.display !== 'none', 'brief empty-state visible initially');
  ok($('briefBody').style.display === 'none', 'brief body hidden initially');
  ok(document.querySelectorAll('#rooms .room').length > 3, 'rooms rendered (' + document.querySelectorAll('#rooms .room').length + ')');
  ok(document.querySelectorAll('#tags .chip').length > 5, 'tags rendered');
  ok(document.querySelectorAll('#grid .card').length > 0, 'archive grid has cards');
  ok($('cmdStatus').classList.contains('show') === false, 'cmd status hidden initially');
  const sugg = document.querySelectorAll('#briefEmpty .sugg');
  ok(sugg.length === 3, 'three suggested topics, got ' + sugg.length);

  // pick a query guaranteed to have deep-read sources
  const tag = window.eval(`(PIL.top_tags.map(t=>t.tag).find(t => PIL.posts.some(p => p.has_knowledge && (p.tags||[]).includes(t))) || PIL.top_tags[0].tag)`);
  console.log('  using query tag: ' + tag);
  $('q').value = tag;
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));

  ok($('briefEmpty').style.display === 'none', 'empty state hidden after search');
  ok($('briefBody').style.display !== 'none', 'brief body shown after search');
  ok($('briefQuery').textContent.includes(tag), 'brief query shows the term');
  ok(/deep-read/.test($('briefGround').textContent), 'grounding line mentions deep-read: ' + $('briefGround').textContent.slice(0, 80));
  const conns = document.querySelectorAll('#connList .conn');
  ok(conns.length > 0, 'connected rail has cards (' + conns.length + ')');
  let whyOk = true;
  conns.forEach(c => { if (!/WHY/.test(c.textContent)) whyOk = false; });
  ok(whyOk, 'every connected card states WHY it connects');
  ok(document.querySelectorAll('#briefContent .takeaways li').length > 0, 'takeaways rendered');
  const cites = document.querySelectorAll('#briefContent .cite');
  ok(cites.length > 0, 'citation chips rendered (' + cites.length + ')');
  ok($('cmdStatus').classList.contains('show'), 'cmd status pill shown');

  // citation click -> connected card flashes
  cites[0].click();
  await new Promise(r => setTimeout(r, 50));
  ok(document.querySelectorAll('#connList .conn.flash').length === 1, 'citation click flashes its connected card');

  // source card click -> archive card scroll + flash
  window.__scrolls = [];
  conns[0].dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  await new Promise(r => setTimeout(r, 50));
  ok(window.__scrolls.some(s => /^card-/.test(s)), 'source card click scrolls to its archive card: ' + window.__scrolls.join(','));
  ok(document.querySelectorAll('#archive .card.flash').length === 1, 'target archive card flashes');

  // instagram links: no dead links, exactly one new tab, blocked -> guidance
  const noUrlHtml = window.eval(`cardHTML(PIL.posts.find(p=>!p.url), 0, false)`);
  ok(!/Instagram ↗/.test(noUrlHtml), 'archive card omits Instagram link when post has no url');
  const opened = [];
  window.open = function(url, target, feats){ opened.push([url, target, feats]); return {}; };
  const ig = document.querySelector('#archive a.ig[href^="http"]');
  ok(ig, 'an archive Instagram link with a real url exists');
  ig.dispatchEvent(new window.MouseEvent('click', { bubbles: true, cancelable: true }));
  ok(opened.length === 1 && opened[0][1] === '_blank' && opened[0][0] === ig.href,
    'ig click opens exactly one new tab: ' + JSON.stringify(opened[0] && opened[0].slice(0, 2)));
  window.open = function(){ return null; };
  ig.dispatchEvent(new window.MouseEvent('click', { bubbles: true, cancelable: true }));
  const toastEl = document.querySelector('.deck-toast');
  ok(toastEl && toastEl.style.display !== 'none' && /NEW TAB BLOCKED/.test(toastEl.textContent),
    'blocked new tab shows guidance toast');

  // keep-exploring followups
  ok(document.querySelectorAll('#briefFollow button').length > 0, 'keep-exploring followups present');

  // chord click -> pair search
  cbs.onEdge({ from: 'pasta', to: 'salad', cosine: 0.5, value: 3 });
  await new Promise(r => setTimeout(r, 600));
  ok($('q').value === 'pasta salad', 'chord click searches both topics, q=' + $('q').value);

  // topic click -> single search
  cbs.onSelect({ label: 'design' });
  await new Promise(r => setTimeout(r, 600));
  ok($('q').value === 'design', 'topic click searches the topic');

  // hover -> scope readout
  cbs.onHover({ label: 'design', count: 42 });
  ok(/DESIGN/.test($('scopeReadout').textContent) && /42/.test($('scopeReadout').textContent),
    'hover updates scope readout: ' + $('scopeReadout').textContent);
  cbs.onHover(null);
  ok(/LIT/.test($('scopeReadout').textContent), 'hover-out restores search scope readout: ' + $('scopeReadout').textContent);

  // clear -> empty state returns, suggestions work
  $('q').value = '';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok($('briefEmpty').style.display !== 'none', 'clearing search restores empty state');
  document.querySelector('#briefEmpty .sugg').click();
  await new Promise(r => setTimeout(r, 600));
  ok($('q').value.length > 0 && $('briefBody').style.display !== 'none', 'suggestion button runs a search');

  // theme segmented control
  const bloomBtn = document.querySelector('#themeSeg button[data-theme="bloom"]');
  bloomBtn.click();
  ok(cbs.theme === 'bloom' && bloomBtn.classList.contains('on'), 'theme switch to bloom');
  document.querySelector('#themeSeg button[data-theme="deck"]').click();
  ok(cbs.theme === 'deck', 'theme switch back to deck');

  // room click -> filters + marks active + names the archive
  $('q').value = '';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  const roomBtn = document.querySelectorAll('#rooms .room')[1];
  roomBtn.click();
  await new Promise(r => setTimeout(r, 100));
  ok(document.querySelector('#rooms .room.active') !== null, 'room click marks active');
  ok($('title').textContent.indexOf('Room —') === 0, 'archive title names the room: ' + $('title').textContent);

  // tag click toggles
  const tagBtn = document.querySelector('#tags .chip');
  const tagName = tagBtn.dataset.tag;
  tagBtn.click();
  await new Promise(r => setTimeout(r, 100));
  ok(document.querySelector('#tags .chip.active') !== null, 'tag click marks active (' + tagName + ')');

  // index rooms carry the ring's topic vocabulary, clickable into search
  const rtopics = document.querySelectorAll('#rooms .rtopic');
  ok(rtopics.length > 0, 'room rows list ring topics (' + rtopics.length + ')');
  const rt = rtopics[0];
  rt.click();
  await new Promise(r => setTimeout(r, 600));
  ok($('q').value === rt.dataset.topic && $('briefQuery').textContent.includes(rt.dataset.topic),
    'room topic click searches it (' + rt.dataset.topic + ')');

  // sources rail renamed + explained
  ok(/SOURCES/.test(document.querySelector('.brief-rail .rail-head').textContent), 'connected posts renamed SOURCES');
  ok(/archive below holds every match/.test(document.querySelector('.brief-rail .rail-sub').textContent),
    'rail explains sources-vs-archive');

  // ring result-map: search lights up matching topics
  $('q').value = 'pasta salad';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok(cbs.lit && cbs.lit.length > 0, 'ring lit with search topics (' + (cbs.lit || []).length + ')');
  ok(/LIT/.test($('scopeReadout').textContent), 'scope readout shows lit count: ' + $('scopeReadout').textContent);
  // regression: page tags are raw, ring ids are cleaned — lit ids must be real nodes
  const nodeIds = new Set(window.eval(`JSON.parse(document.getElementById('ring-data').textContent).nodes.map(n=>n.id)`));
  ok((cbs.lit || []).every(id => nodeIds.has(id)), 'every lit topic is a real ring node');

  // refine box: drives the brief, syncs two-way
  const q2 = $('q2');
  ok(q2 && /Refine/.test(q2.placeholder), 'refine input present in brief header');
  q2.value = 'pasta bake';
  q2.dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok($('briefQuery').textContent.includes('pasta bake'), 'refine input drives the brief');
  ok($('q').value === 'pasta bake', 'hero input synced from refine');
  $('q').value = 'salad bowl';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok(q2.value === 'salad bowl', 'refine input synced from hero');

  // auto-scroll: new query scrolls to brief only when it is off-screen
  const brief = $('brief');
  brief.getBoundingClientRect = () => ({ top: 2000, bottom: 3000, left: 0, right: 0, width: 0, height: 0 });
  window.__scrolls.length = 0;
  $('q').value = 'garden salad';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok(window.__scrolls.includes('brief'), 'new query auto-scrolls to the brief when off-screen');
  brief.getBoundingClientRect = () => ({ top: 100, bottom: 900, left: 0, right: 0, width: 0, height: 0 });
  window.__scrolls.length = 0;
  $('q').value = 'garden salads';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok(!window.__scrolls.includes('brief'), 'no scroll when the brief is already visible');

  // clearing the query restores the full ring
  $('q').value = '';
  $('q').dispatchEvent(new window.Event('input', { bubbles: true }));
  await new Promise(r => setTimeout(r, 600));
  ok(cbs.lit === null && $('scopeReadout').textContent === 'SCOPE — ALL TOPICS',
    'clearing query restores the full ring');

  // logo: inline bookmark SVG in the topbar
  const mark = document.querySelector('.deck-brand svg.brand-mark');
  ok(mark && mark.querySelector('path') && /PIL/.test(mark.textContent), 'bookmark logo in topbar');

  // PWA: meta tags, inline manifest, hidden install button
  ok(document.querySelector('meta[name="theme-color"]'), 'theme-color meta present');
  ok(document.querySelector('link[rel="apple-touch-icon"]'), 'apple-touch-icon present');
  const mani = document.querySelector('link[rel="manifest"]');
  ok(mani && mani.href.startsWith('data:application/manifest+json,'), 'inline manifest linked');
  const maniJson = JSON.parse(decodeURIComponent(mani.href.split(',', 2)[1]));
  ok(maniJson.name.indexOf('PIL') === 0 && maniJson.icons.length === 2 &&
     maniJson.icons.some(i => i.sizes === '512x512' && i.src.startsWith('data:image/png;base64,')),
    'manifest has name + 192/512 icons');
  const ib = $('installBtn');
  ok(ib && ib.style.display === 'none', 'install button hidden until beforeinstallprompt');
  window.dispatchEvent(new window.Event('beforeinstallprompt'));
  await new Promise(r => setTimeout(r, 50));
  ok(ib.style.display !== 'none', 'install button appears on beforeinstallprompt');

  // version stamp + opt-in update check
  ok(document.querySelector('meta[name="pil-deck-version"]').content === '1.2.0', 'version meta stamped');
  ok(/v1\.2\.0/.test(document.querySelector('.footer-note .ver-line').textContent), 'footer shows version');
  const ub = $('updCheck');
  ok(ub, 'update check button present');
  window.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({ tag_name: 'v9.9.9' }) });
  ub.click();
  await new Promise(r => setTimeout(r, 100));
  ok(/UPDATE AVAILABLE/.test(document.querySelector('.deck-toast').textContent), 'newer release -> update toast');
  window.fetch = () => Promise.resolve({ ok: true, json: () => Promise.resolve({ tag_name: 'v1.2.0' }) });
  ub.click();
  await new Promise(r => setTimeout(r, 100));
  ok(/LATEST/.test(document.querySelector('.deck-toast').textContent), 'same version -> latest toast');

  ok(errors.length === 0, 'no jsdom/window errors' + (errors.length ? ': ' + errors.slice(0, 3).join(' | ') : ''));
})().then(() => {
  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
}).catch(e => { console.log('HARNESS ERROR', e); process.exit(2); });

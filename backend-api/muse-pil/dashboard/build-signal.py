#!/usr/bin/env python3
"""Build the PIL Signal Deck: an award-level redesign of the PIL landing page.

Concept: a mission instrument, not a dashboard. Warm black + bone + safety
orange; heavy grotesque display type, mono data readouts, serif for long
reads. Deliberately anti-AI-slop: no purple gradients, no glassmorphism.

Layout:
  - sticky instrument topbar: PIL mark, mono stat readouts, ring theme switch
  - hero (viewport): full-bleed topic ring (PILRing, new "deck" theme), no box;
    headline, command-bar search, hover scope readout, interaction hints
  - the brief: on search, a synthesis brief (wide reading column) + a
    "connected posts" rail that shows WHY each post connects; orientation
    state with suggested topics when idle
  - index: rooms as editorial rows, tags as chips
  - archive: the full results grid (production search/synthesis/source logic
    from pil.export_html reused verbatim)

Still one self-contained offline HTML file. Private data stays local.
"""
import sys
import os
import json
import html as htmlmod

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.expanduser('~'), 'workspace', 'skills', 'pil', 'src'))
sys.path.insert(0, HERE)

from pil.export_html import gather_data, render_page
from build import build_graph_data

REAL_DB = os.environ.get('PIL_DB',
    os.path.join(os.path.expanduser('~'), 'workspace', 'instagram-kb', 'instakb.sqlite'))
OUT = os.path.join(HERE, 'pil-signal-deck.html')

DASHBOARD_VERSION = "1.2.0"

# ---------------------------------------------------------------- tokens ---
BLK, BONE, DIM, FAINT, SIGNAL, LINE, PANEL = (
    '#141210', '#ECE7DB', '#A39D8D', '#6E695D', '#FF5A1F', '#2A2723', '#1A1815')

TOPBAR_HTML = """<header class="deck-top">
  <div class="deck-brand">__LOGO_SVG__<b>PIL</b><span class="deck-sub mono">/ SIGNAL DECK</span></div>
  <div class="deck-stats mono">__POSTS_FMT__ POSTS &nbsp;·&nbsp; __NODES__ TOPICS &nbsp;·&nbsp; __EDGES__ LINKS</div>
  <button id="installBtn" class="install-btn mono" style="display:none" type="button">INSTALL APP</button>
  <div class="deck-themes mono" id="themeSeg">
    <button data-theme="deck" class="on">DECK</button><button data-theme="gallery">GALLERY</button><button data-theme="bloom">BLOOM</button><button data-theme="atlas">ATLAS</button><button data-theme="signal">SIGNAL</button>
  </div>
</header>"""

HERO_HTML = """<section class="hero">
  <div id="ring-mount"></div>
  <div class="hero-scrim"></div>
  <div class="hero-kicker mono"><span class="sq"></span>PERSONAL INSTAGRAM LIBRARY — __POSTS_FMT__ POSTS INDEXED</div>
  <h1 class="hero-h">Everything you saved.<br>On the record.</h1>
  <div class="cmd">
    <span class="cmd-prompt">▸</span>
    <input id="q" placeholder="Search your library — topics, creators, ideas…" autocomplete="off" spellcheck="false">
    <kbd class="mono">/</kbd>
  </div>
  <button class="cmd-status mono" id="cmdStatus" type="button"></button>
  <div class="hero-foot mono">
    <span id="scopeReadout" class="scope">SCOPE — ALL TOPICS</span>
    <span class="hints">click the ring, then scroll to rotate · pinch to zoom · drag to pan · click a topic · click a chord</span>
    <span class="scrollcue">SCROLL ↓</span>
  </div>
</section>"""

BRIEF_HTML = """<section class="brief" id="brief">
  <div class="wrap">
    <div class="sec-head mono"><span class="tick">▸</span> PIL BRIEF <span class="sec-meta" id="briefMeta"></span>
      <span class="brief-refine"><span class="rp">▸</span><input id="q2" placeholder="Refine the brief…" autocomplete="off" spellcheck="false"></span>
    </div>
    <div class="brief-grid">
      <aside class="brief-index">
        <div class="rail-head mono"><span class="tick">▸</span> INDEX</div>
        <p class="rail-sub">Rooms and tags filter the archive below. Each room lists its biggest ring topics — jump straight in.</p>
        <div id="rooms"></div>
        <div class="tags-head mono">TAGS</div>
        <div class="tagchips" id="tags"></div>
      </aside>
      <div class="brief-center">
    <div id="briefEmpty" class="brief-empty">
      <h2>No brief on screen.</h2>
      <p>Spin the ring or run a search — the brief assembles here, with every claim pinned to the posts it came from.</p>
      <div class="sugg-row mono"><span class="sugg-label">TRY —</span>__SUGGEST__</div>
    </div>
    <div id="briefBody" style="display:none">
      <h2 class="brief-q" id="briefQuery"></h2>
      <div class="brief-cols">
        <div class="brief-main">
          <p class="grounding"><span class="grounding-dot"></span><span id="briefGround"></span></p>
          <div id="briefContent"></div>
          <div class="keep"><div class="keep-h mono">KEEP EXPLORING</div><div id="briefFollow"></div></div>
        </div>
        <aside class="brief-rail">
          <div class="rail-head mono"><span class="tick">▸</span> SOURCES <span id="connCount"></span></div>
          <p class="rail-sub">The deep-read posts this brief is built from — every claim is pinned to one of them. The archive below holds every match in your library.</p>
          <div id="connList"></div>
        </aside>
      </div>
    </div>
      </div>
    </div>
  </div>
</section>"""

DECK_CSS = """<style>
/* ============ SIGNAL DECK design layer ============ */
:root{--blk:#141210;--bone:#ECE7DB;--dim:#A39D8D;--faint:#6E695D;--signal:#FF5A1F;--line:#2A2723;--panel:#1A1815}
html{scroll-behavior:smooth}
body{background:var(--blk) !important;color:var(--bone) !important;overflow-x:clip;
  font-family:"Helvetica Neue",Helvetica,Arial,"Segoe UI",sans-serif !important}
/* full-bleed sections living inside the export's .wrap */
.hero,.brief,.archivesec{width:100vw;margin-left:calc(50% - 50vw);scroll-margin-top:64px}
.brief>.wrap,.archivesec>.wrap{padding-top:0;padding-bottom:0}
::selection{background:var(--signal);color:#141210}
.mono{font-family:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace !important}
.sq{display:inline-block;width:11px;height:11px;background:var(--signal);margin-right:10px;vertical-align:baseline}
.tick{color:var(--signal)}
.wrap{max-width:1240px !important}
/* ---- topbar ---- */
.deck-top{position:sticky;top:0;z-index:100;display:flex;align-items:center;gap:28px;
  padding:0 28px;height:58px;background:rgba(20,18,16,.94);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--line)}
.deck-brand{display:flex;align-items:center;font-weight:800;letter-spacing:.02em;font-size:17px;white-space:nowrap}
.deck-brand .sq{margin-right:10px}
.deck-brand .brand-mark{height:30px;width:auto;margin-right:10px;flex:none}
.deck-sub{font-size:11px;color:var(--faint);margin-left:10px;letter-spacing:.18em}
.deck-stats{margin-left:auto;font-size:11px;letter-spacing:.14em;color:var(--dim);white-space:nowrap}
.install-btn{background:none;border:1px solid var(--signal);color:var(--signal);
  font-size:10px;letter-spacing:.16em;padding:9px 14px;cursor:pointer;white-space:nowrap}
.install-btn:hover{background:var(--signal);color:var(--blk)}
.ver-line{margin-bottom:14px;font-size:11px;letter-spacing:.16em;color:var(--dim)}
.upd-btn{background:none;border:1px solid var(--line);color:var(--bone);
  font-size:10px;letter-spacing:.16em;padding:8px 14px;cursor:pointer;margin-left:12px}
.upd-btn:hover{border-color:var(--signal);color:var(--signal)}
.deck-themes{display:flex;border:1px solid var(--line)}
.deck-themes button{background:none;border:0;border-left:1px solid var(--line);color:var(--faint);
  font-family:inherit;font-size:10px;letter-spacing:.14em;padding:9px 12px;cursor:pointer}
.deck-themes button:first-child{border-left:0}
.deck-themes button:hover{color:var(--bone)}
.deck-themes button.on{background:var(--signal);color:#141210;font-weight:700}
/* ---- hero ---- */
.hero{position:relative;height:calc(100vh - 58px);min-height:620px;overflow:hidden;background:var(--blk)}
#ring-mount{position:absolute;inset:0}
.hero-scrim{position:absolute;inset:0;pointer-events:none;z-index:2;
  background:linear-gradient(180deg,rgba(20,18,16,.55) 0%,transparent 22%,transparent 62%,rgba(20,18,16,.72) 100%)}
.hero-kicker{position:absolute;top:44px;left:48px;z-index:5;font-size:11px;letter-spacing:.22em;color:var(--dim)}
.hero-h{position:absolute;top:76px;left:46px;z-index:5;margin:0;max-width:14ch;
  font-weight:800;font-size:clamp(46px,6.4vw,96px);line-height:.96;letter-spacing:-.032em;color:var(--bone)}
.cmd{position:absolute;left:50%;bottom:118px;transform:translateX(-50%);z-index:5;
  width:min(700px,92vw);display:flex;align-items:center;gap:14px;
  background:rgba(20,18,16,.82);border:1px solid #3A352D;padding:6px 18px 6px 20px}
.cmd:focus-within{border-color:var(--signal)}
.cmd-prompt{color:var(--signal);font-size:26px;font-weight:700}
.cmd input{flex:1;background:none;border:0;outline:0;color:var(--bone);font-size:21px;padding:14px 0;
  font-family:inherit;caret-color:var(--signal)}
.cmd input::placeholder{color:var(--faint)}
.cmd kbd{border:1px solid #3A352D;color:var(--faint);font-size:12px;padding:4px 9px;font-family:inherit}
.cmd-status{position:absolute;left:50%;bottom:76px;transform:translateX(-50%);z-index:5;
  display:none;background:none;border:1px solid var(--signal);color:var(--signal);
  font-size:11px;letter-spacing:.16em;padding:9px 18px;cursor:pointer;font-family:inherit}
.cmd-status.show{display:block}
.cmd-status:hover{background:var(--signal);color:#141210}
.hero-foot{position:absolute;left:0;right:0;bottom:0;z-index:5;display:flex;align-items:center;gap:28px;
  padding:18px 48px;border-top:1px solid rgba(42,39,35,.7);font-size:10.5px;letter-spacing:.14em;color:var(--faint)}
.hero-foot .scope{color:var(--signal);white-space:nowrap}
.hero-foot .hints{color:var(--faint)}
.hero-foot .scrollcue{margin-left:auto;color:var(--dim);white-space:nowrap}
/* ---- sections ---- */
.brief{border-top:1px solid var(--line);padding:96px 0 80px}
.archivesec{border-top:1px solid var(--line);padding:88px 0 60px}
.sec-head{font-size:12px;letter-spacing:.22em;color:var(--dim);margin-bottom:40px;
  display:flex;align-items:center;flex-wrap:wrap;gap:10px}
.sec-head .sec-meta{color:var(--faint);margin-left:8px;letter-spacing:.14em}
.brief-refine{margin-left:auto;display:flex;align-items:center;gap:10px;border:1px solid #3A352D;padding:7px 14px}
.brief-refine .rp{color:var(--signal);font-size:14px}
.brief-refine input{background:none;border:0;outline:0;color:var(--bone);
  font-family:ui-monospace,Menlo,monospace;font-size:12.5px;letter-spacing:.04em;
  width:190px;caret-color:var(--signal);text-transform:none}
.brief-refine input::placeholder{color:var(--faint)}
.brief-refine:focus-within{border-color:var(--signal)}
/* ---- brief ---- */
.brief-empty h2{font-size:clamp(34px,4vw,54px);font-weight:800;letter-spacing:-.03em;margin:0 0 16px}
.brief-empty p{font-size:18px;color:var(--dim);max-width:56ch;line-height:1.6;margin:0 0 30px}
.sugg-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap;font-size:11px;letter-spacing:.14em}
.sugg-label{color:var(--faint)}
.sugg{background:none;border:1px solid #3A352D;color:var(--bone);font-family:inherit;
  font-size:12px;letter-spacing:.06em;padding:11px 18px;cursor:pointer}
.sugg:hover{border-color:var(--signal);color:var(--signal)}
.sugg .n{color:var(--faint);margin-left:8px}
.brief-q{font-size:clamp(34px,4.4vw,60px);font-weight:800;letter-spacing:-.03em;line-height:1.02;margin:0 0 44px;max-width:20ch}
.brief-grid{display:grid;grid-template-columns:292px minmax(0,1fr);gap:56px;align-items:start}
.brief-center{min-width:0}
.brief-cols{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:52px;align-items:start}
.brief-index{position:sticky;top:78px;min-width:0}
.brief-index #rooms .room{padding:13px 2px}
.brief-index .rname{font-size:17px;letter-spacing:-.01em}
.brief-index #rooms .room .n{font-size:10.5px}
.brief-index #rooms .room .dot{margin-right:10px}
.brief-index .room-topics{font-size:10px;margin-top:8px;line-height:2}
.brief-index .tags-head{margin:24px 0 10px}
.grounding{display:flex;gap:12px;align-items:baseline;color:var(--dim);font-size:14px;line-height:1.6;
  border-top:2px solid var(--signal);padding-top:18px;margin:0 0 34px;max-width:72ch}
.grounding-dot{width:8px;height:8px;background:var(--signal);flex:0 0 8px;transform:translateY(-1px)}
.brief-main{font-family:Georgia,"Times New Roman",serif}
.brief-lead{font-size:21px;line-height:1.68;color:var(--bone);max-width:68ch;margin:0 0 40px}
.takeaways{list-style:none;margin:0 0 44px;padding:0;max-width:72ch}
.takeaways li{display:flex;gap:18px;padding:20px 0;border-top:1px solid var(--line);font-size:18px;line-height:1.62}
.tnum{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;color:var(--signal);padding-top:6px;flex:0 0 34px;letter-spacing:.1em}
.cite{background:none;border:1px solid var(--signal);color:var(--signal);font-family:ui-monospace,Menlo,monospace;
  font-size:11px;padding:2px 7px;margin-left:10px;cursor:pointer;vertical-align:2px;white-space:nowrap}
.cite:hover{background:var(--signal);color:#141210}
.answer-section{margin:0 0 40px;max-width:72ch}
.answer-section h3{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;font-weight:800;
  letter-spacing:.2em;color:var(--dim);margin:0 0 18px}
.approach-grid{display:grid;gap:14px}
.approach{border:1px solid var(--line);padding:20px 22px;font-size:16px;line-height:1.6}
.approach strong{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:14px}
.approach p{margin:10px 0 0;color:var(--dim)}
.limited-panel{border:1px solid var(--line);padding:34px 36px;max-width:72ch;margin-bottom:36px}
.answer-kicker{font-family:ui-monospace,Menlo,monospace;font-size:11px;letter-spacing:.22em;color:var(--signal);margin:0 0 14px}
.answer-title{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:30px;font-weight:800;letter-spacing:-.02em;margin:0 0 14px}
.limited-panel p{font-size:17px;line-height:1.65;color:var(--dim);margin:0 0 12px}
.excerpt-card{border-top:1px solid var(--line);padding:18px 0}
.excerpt-card h4{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:15px;margin:0 0 8px}
.excerpt-card p{font-size:16px !important}
.keep{margin-top:44px;max-width:72ch}
.keep-h{font-size:11px;letter-spacing:.22em;color:var(--faint);margin-bottom:14px}
.followups{display:flex;flex-wrap:wrap;gap:10px}
.followups button{background:none;border:1px solid #3A352D;color:var(--dim);font-family:ui-monospace,Menlo,monospace;
  font-size:12px;padding:10px 16px;cursor:pointer}
.followups button:hover{border-color:var(--signal);color:var(--signal)}
/* ---- connected rail ---- */
.brief-rail{border-top:2px solid var(--signal);padding-top:18px}
.rail-head{font-size:11px;letter-spacing:.22em;color:var(--dim);margin-bottom:8px}
.rail-sub{font-family:Georgia,serif;font-size:14px;line-height:1.65;color:var(--dim);margin:0 0 10px}
.conn{border-top:1px solid var(--line);padding:20px 0;transition:background .3s;cursor:pointer}
.conn:hover{background:rgba(255,90,31,.05)}
.conn.flash{background:rgba(255,90,31,.08)}
.conn-top{display:flex;gap:10px;align-items:baseline;font-size:10.5px;letter-spacing:.12em;color:var(--faint);margin-bottom:10px}
.conn-top .cnum{color:var(--signal);font-weight:700}
.conn h4{font-family:Georgia,serif;font-weight:400;font-size:17px;line-height:1.45;margin:0 0 10px;color:var(--bone)}
.conn-why{font-size:10.5px;letter-spacing:.1em;color:var(--faint);margin:0 0 12px;line-height:1.7}
.conn-why b{color:var(--signal);font-weight:400}
.conn a{font-family:ui-monospace,Menlo,monospace;font-size:11px;letter-spacing:.1em;color:var(--dim);text-decoration:none}
.conn a:hover{color:var(--signal)}
/* ---- index ---- */
#rooms .room{display:block;width:100%;background:none;border:0;border-top:1px solid var(--line);
  padding:22px 4px;cursor:pointer;text-align:left;font-family:inherit;transition:padding .18s ease}
#rooms .room:last-child{border-bottom:1px solid var(--line)}
.room-top{display:flex;align-items:baseline;justify-content:space-between;gap:16px}
.rname{font-size:clamp(22px,2.6vw,32px);font-weight:800;letter-spacing:-.02em;color:var(--bone)}
#rooms .room .n{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--faint);letter-spacing:.1em;white-space:nowrap}
#rooms .room .dot{display:inline-block;width:9px;height:9px;background:var(--signal);margin-right:14px}
#rooms .room:hover{padding-left:14px}
#rooms .room:hover .rname,#rooms .room.active .rname{color:var(--signal)}
.room-topics{display:block;margin-top:12px;font-size:11px;letter-spacing:.14em;color:var(--faint)}
.rtopic{cursor:pointer;color:var(--dim)}
.rtopic:hover{color:var(--signal);text-decoration:underline;text-underline-offset:3px}
.rsep{color:#3A352D}
.tags-head{font-size:11px;letter-spacing:.22em;color:var(--faint);margin:44px 0 18px}
.tagchips{display:flex;flex-wrap:wrap;gap:10px}
.tagchips .chip{background:none;border:1px solid #3A352D;color:var(--dim);
  font-family:ui-monospace,Menlo,monospace;font-size:12px;padding:10px 16px;cursor:pointer}
.tagchips .chip:hover{border-color:var(--signal);color:var(--signal)}
.tagchips .chip.active{background:var(--signal);border-color:var(--signal);color:#141210}
/* ---- archive ---- */
.arch-head{display:flex;align-items:baseline;justify-content:space-between;gap:24px;margin-bottom:36px}
.arch-head h2{font-size:clamp(30px,3.6vw,48px);font-weight:800;letter-spacing:-.03em;margin:0}
.sort{font-size:11px;letter-spacing:.18em;color:var(--faint);white-space:nowrap}
.sort select{background:var(--panel);border:1px solid var(--line);color:var(--bone);font-family:inherit;
  font-size:12px;padding:9px 12px;outline:none;cursor:pointer;margin-left:10px}
.grid .card,.card{--signal:var(--signal)}
.empty{border:1px dashed #3A352D;padding:60px 40px;text-align:center;color:var(--faint);
  font-family:Georgia,serif;font-size:19px;font-style:italic}
.more button{background:none;border:1px solid #3A352D;color:var(--dim);width:100%;padding:18px;
  font-family:ui-monospace,Menlo,monospace;font-size:12px;letter-spacing:.2em;cursor:pointer}
.deck-toast{position:fixed;left:50%;bottom:28px;transform:translateX(-50%);z-index:9999;
  background:var(--bone);color:var(--blk);font-size:11px;letter-spacing:.14em;padding:12px 20px;
  border:1px solid var(--signal);max-width:min(92vw,600px);text-align:center}
.more button:hover{border-color:var(--signal);color:var(--signal)}
/* accent overrides on the inherited export styles */
.room .dot{background:var(--signal) !important}
.answer-kicker{color:var(--signal) !important}
.grounding-dot{background:var(--signal) !important}
/* ---- footer ---- */
.footer-note{border-top:1px solid var(--line);margin-top:0 !important;padding:34px 0 44px !important;
  font-family:ui-monospace,Menlo,monospace !important;font-size:11px;letter-spacing:.12em;color:var(--faint) !important}
@media(max-width:1280px){
  .brief-grid{grid-template-columns:250px minmax(0,1fr);gap:36px}
  .brief-cols{grid-template-columns:minmax(0,1fr) 320px;gap:36px}
}
@media(max-width:1080px){
  .brief-grid{grid-template-columns:1fr}
  .brief-index{position:static}
  .brief-index #rooms{display:grid;grid-template-columns:1fr 1fr;column-gap:32px}
  .brief-index .rname{font-size:clamp(19px,2.4vw,26px)}
  .brief-cols{grid-template-columns:1fr}
  .deck-stats{display:none}
  .hero-h{left:24px;top:88px}
  .hero-kicker{left:24px}
  .hero-foot{padding:14px 24px}
  .hero-foot .hints{display:none}
  .brief,.archivesec{padding-left:0;padding-right:0}
}
</style>"""

SIGNAL_JS = """<script>__ECHARTS_JS__</script>
<script>__PIL_RING_JS__</script>
<script id="ring-data" type="application/json">__RING_JSON__</script>
<script>
(function(){
  'use strict';
  var ROOM_TOPICS = __ROOM_TOPICS__;
  var lastLit = null, lastMatches = [];
  function scopeText(){
    if(state.q && state.q.trim() && lastLit !== null){
      return 'SCOPE — \u201c' + state.q.toUpperCase() + '\u201d · ' + lastLit +
        ' TOPIC' + (lastLit === 1 ? '' : 'S') + ' LIT';
    }
    return 'SCOPE — ALL TOPICS';
  }
  function paintScope(){ document.getElementById('scopeReadout').textContent = scopeText(); }
  /* ---------- the ring: full-bleed hero, deck theme ---------- */
  var data = JSON.parse(document.getElementById('ring-data').textContent);
  var NODE_IDS = {}, NODE_ROOM = {}, NODE_COUNT = {};
  var FOLDER_ID_BY_NAME = {};
  PIL.folders.forEach(function(f){ FOLDER_ID_BY_NAME[f.name] = f.id; });
  data.nodes.forEach(function(n){
    NODE_IDS[n.id] = 1;
    NODE_ROOM[n.id] = FOLDER_ID_BY_NAME[n.folder] || null;
    NODE_COUNT[n.id] = n.count || 0;
  });
  var ring = PILRing.mount(document.getElementById('ring-mount'), {
    data: data,
    maxCosine: __MAX_COS_NUM__,
    theme: 'deck',
    persistTheme: 'pil-deck-theme',
    onSelect: function(node){ if(node) searchTopic(node.label); },
    onEdge: function(e){ searchTopic(e.from + ' ' + e.to); },
    onHover: function(node){
      document.getElementById('scopeReadout').textContent = node
        ? 'SCOPE — ' + node.label.toUpperCase() + ' · ' + node.count.toLocaleString() + ' POSTS'
        : scopeText();
    }
  });

  /* theme segmented control */
  var seg = document.getElementById('themeSeg');
  function syncSeg(){ seg.querySelectorAll('button').forEach(function(b){ b.classList.toggle('on', b.dataset.theme === ring.getTheme()); }); }
  seg.addEventListener('click', function(ev){
    var b = ev.target.closest('button[data-theme]'); if(!b) return;
    ring.setTheme(b.dataset.theme); syncSeg();
  });
  syncSeg();

  /* ---------- search plumbing ---------- */
  function searchTopic(q){
    var input = document.getElementById('q');
    input.value = q;
    state.q = q; state.room = null; state.tag = null;
    renderRooms(); renderTags(); render(false);
  }
  document.getElementById('cmdStatus').addEventListener('click', function(){
    document.getElementById('brief').scrollIntoView({behavior:'smooth'});
  });
  document.getElementById('briefEmpty').addEventListener('click', function(ev){
    var b = ev.target.closest('[data-topic]'); if(b) searchTopic(b.dataset.topic);
  });
  // Enter in the command bar jumps to the brief
  document.getElementById('q').addEventListener('keydown', function(ev){
    if(ev.key === 'Enter'){
      document.getElementById('brief').scrollIntoView({behavior:'smooth'});
    }
  });
  /* refine box in the brief header, two-way synced with the command bar */
  (function(){
    var q2 = document.getElementById('q2'), deb2;
    q2.addEventListener('input', function(e){
      clearTimeout(deb2);
      deb2 = setTimeout(function(){
        document.getElementById('q').value = e.target.value;
        state.q = e.target.value.trim();
        render(false);
      }, 220);
    });
    q2.addEventListener('keydown', function(e){
      if(e.key === 'Enter'){
        clearTimeout(deb2);
        document.getElementById('q').value = q2.value;
        state.q = q2.value.trim();
        render(false);
        document.getElementById('brief').scrollIntoView({behavior:'smooth'});
      }
    });
  })();

  /* ---------- the brief: synthesis restacked for reading ---------- */
  function citeChip(post, sources){
    var b = el('button', 'cite', '[' + (sources.indexOf(post) + 1) + ']');
    b.addEventListener('click', function(){
      var t = document.getElementById('conn-' + post.id);
      if(!t) return;
      t.scrollIntoView({behavior:'smooth', block:'center'});
      t.classList.remove('flash'); void t.offsetWidth; t.classList.add('flash');
    });
    return b;
  }
  function whyLine(post, tokens){
    var tags = post.tags || [], hits = [];
    tokens.forEach(function(t){ if(t.length > 2 && tags.indexOf(t) !== -1 && hits.indexOf(t) === -1 && hits.length < 3) hits.push(t); });
    var parts = [];
    if(hits.length) parts.push('MATCHED <b>' + hits.join(' · ') + '</b>');
    var f = folderName(post);
    if(f) parts.push('FILED UNDER <b>' + f.toUpperCase() + '</b>');
    if(post.author) parts.push('@' + post.author.toUpperCase());
    return parts.join(' &nbsp;—&nbsp; ');
  }
  function folderName(post){
    if(!post.folders || !post.folders.length) return '';
    var f = PIL.folders.filter(function(x){ return x.id === post.folders[0]; })[0];
    return f ? f.name : '';
  }

  /* archive cards: never render a dead Instagram link for posts without a URL */
  var _cardHTML = cardHTML;
  cardHTML = function(p, i, featured){
    var h = _cardHTML(p, i, featured);
    if(!p.url) h = h.split('<a class="ig" href="" target="_blank" rel="noopener">Instagram ↗</a>').join('');
    return h;
  };

  /* Instagram links: open via window.open so a blocked popup (sandboxed file
     previews block target=_blank) fails loudly with guidance instead of silently */
  var toastEl = document.createElement('div');
  toastEl.className = 'deck-toast mono';
  toastEl.style.display = 'none';
  document.body.appendChild(toastEl);
  var toastTimer = null;
  function toast(msg){
    toastEl.textContent = msg;
    toastEl.style.display = 'block';
    if(toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function(){ toastEl.style.display = 'none'; }, 4500);
  }
  document.addEventListener('click', function(e){
    var t = e.target;
    var a = (t && t.closest) ? t.closest('a.ig') : null;
    if(!a || !a.getAttribute('href')) return;
    var w = null;
    try{ w = window.open(a.href, '_blank', 'noopener'); }catch(_err){ w = null; }
    e.preventDefault();
    if(!w) toast('NEW TAB BLOCKED — download this file and open it in your browser to follow Instagram links.');
  });

  /* jump from a source card to its archive card, loading more pages if needed */
  function jumpToCard(id){
    var target = document.getElementById('card-' + id);
    var guard = 0;
    while(!target && guard < 40){
      var more = document.getElementById('more');
      if(!more || more.style.display === 'none') break;
      _render(true);
      target = document.getElementById('card-' + id);
      guard++;
    }
    if(!target) return;
    target.scrollIntoView({behavior:'smooth', block:'center'});
    target.classList.remove('flash'); void target.offsetWidth; target.classList.add('flash');
    window.setTimeout(function(){ target.classList.remove('flash'); }, 1400);
  }

  buildKnowledgeView = function(matches){
    lastMatches = matches;
    var empty = document.getElementById('briefEmpty');
    var body = document.getElementById('briefBody');
    var status = document.getElementById('cmdStatus');
    if(!state.q || !state.q.trim()){
      empty.style.display = ''; body.style.display = 'none';
      document.getElementById('briefMeta').textContent = '';
      status.classList.remove('show'); status.textContent = '';
      return 0;
    }
    empty.style.display = 'none'; body.style.display = '';
    var deep = matches.filter(function(p){ return p.has_knowledge; });
    var sources = deep.slice(0, 8);
    var folders = folderBreakdown(sources);
    var creators = new Set(sources.map(function(p){ return p.author; }).filter(Boolean));

    document.getElementById('briefQuery').textContent = '\u201c' + state.q + '\u201d';
    document.getElementById('briefMeta').textContent =
      sources.length + ' SOURCES · ' + creators.size + ' CREATORS' +
      (matches.length > sources.length ? ' · ' + (matches.length - sources.length) + ' MORE MATCHES' : '');
    var ground = document.getElementById('briefGround');
    ground.textContent = sources.length
      ? 'Built from ' + sources.length + ' deep-read ' + (sources.length === 1 ? 'post' : 'posts') +
        (folders ? ' · ' + folders : '') + (matches.length > sources.length ? ' · ' + (matches.length - sources.length) + ' more matches below' : '') + '.'
      : matches.length + ' catalog ' + (matches.length === 1 ? 'match' : 'matches') + ' · no deep-read content for this search.';

    var host = document.getElementById('briefContent');
    host.replaceChildren();

    if(!sources.length){
      var p0 = el('section', 'limited-panel');
      p0.append(el('p', 'answer-kicker', 'THIN SIGNAL'),
        el('h3', 'answer-title', matches.length ? 'No extracted knowledge yet' : 'Nothing in PIL covers this yet.'),
        el('p', '', matches.length
          ? 'Your saved posts match the words you searched, but none has a deeper extraction to support a knowledge answer. The matching posts are in the archive below.'
          : 'Try a broader search or spin the ring. The page won\u2019t fill gaps with outside knowledge.'));
      if(matches.length) p0.append(el('p', 'why-match', 'Why these posts: the terms appear in a creator name, caption, tag, folder, or extracted note.'));
      host.append(p0);
    } else if(sources.length < 3){
      var p1 = el('section', 'limited-panel');
      p1.append(el('p', 'answer-kicker', 'LIMITED COVERAGE'),
        el('h3', 'answer-title', 'Based on ' + sources.length + ' deep-read ' + (sources.length === 1 ? 'post' : 'posts')),
        el('p', '', 'There isn\u2019t enough coverage for a blended answer, so the source material stays attributed.'));
      sources.forEach(function(post){
        var card = el('article', 'excerpt-card');
        var h = el('h4', '', post.author ? '@' + post.author : 'Saved post');
        h.append(citeChip(post, sources)); card.append(h, el('p', '', sourceExcerpt(post))); p1.append(card);
      });
      p1.append(el('p', 'why-match', 'Why these posts: your search terms appear in their captions, tags, folders, or extracted notes.'));
      host.append(p1);
    } else {
      var lead = el('p', 'brief-lead');
      var themes = relatedThemes(sources);
      lead.append(document.createTextNode('Across ' + sources.length + ' deep-read matches from ' + creators.size +
        ' ' + (creators.size === 1 ? 'creator' : 'creators') + ', your library keeps returning to '));
      themes.slice(0, 3).forEach(function(item, i){
        if(i) lead.append(document.createTextNode(i === Math.min(2, themes.length - 1) ? ' and ' : ', '));
        lead.append(document.createTextNode(item.tag), citeChip(item.post, sources));
      });
      lead.append(document.createTextNode('. Open any citation to inspect the supporting post.'));
      host.append(lead);
      var insights = collectInsights(sources);
      if(insights.length){
        var ul = el('ul', 'takeaways');
        insights.forEach(function(item, i){
          var li = el('li', '');
          var num = el('span', 'tnum', ('0' + (i + 1)).slice(-2));
          var tx = el('span', ''); tx.innerHTML = inlineMd(item.text); tx.append(citeChip(item.post, sources));
          li.append(num, tx); ul.append(li);
        });
        host.append(ul);
      }
      var howTo = /\\b(how|make|build|recipe|steps?|setup|install|create)\\b/i.test(state.q);
      var approaches = sources.filter(function(p){ return clean(p.howto).length > 35; }).slice(0, 4);
      if(howTo && approaches.length > 1){
        var sec = el('section', 'answer-section');
        sec.append(el('h3', '', 'DISTINCT APPROACHES IN YOUR POSTS'));
        var ag = el('div', 'approach-grid');
        approaches.forEach(function(post){
          var box = el('article', 'approach');
          var h = el('strong', '', post.author ? '@' + post.author : 'Saved post');
          h.append(citeChip(post, sources)); box.append(h, el('p', '', shorten(post.howto, 260))); ag.append(box);
        });
        sec.append(ag); host.append(sec);
      }
    }

    /* connected posts rail: every source, with WHY it connects */
    var tokens = state.q.toLowerCase().split(/[^a-z0-9]+/).filter(Boolean);
    var list = document.getElementById('connList');
    list.replaceChildren();
    document.getElementById('connCount').textContent = sources.length ? '— ' + sources.length : '';
    sources.forEach(function(post, i){
      var card = el('article', 'conn'); card.id = 'conn-' + post.id;
      var top = el('div', 'conn-top mono');
      top.append(el('span', 'cnum', '[' + (i + 1) + ']'),
        el('span', '', (folderName(post) || 'SAVED').toUpperCase()),
        el('span', '', post.author ? '@' + post.author.toUpperCase() : ''));
      var text = (post.summary || post.snippet || 'Untitled post').trim();
      var head = text.length > 140 ? text.slice(0, 140).split(' ').slice(0, -1).join(' ') + '…' : text;
      var why = el('p', 'conn-why mono'); why.innerHTML = 'WHY — ' + (whyLine(post, tokens) || 'MATCHED YOUR SEARCH TERMS');
      var link = el('a', 'ig', 'INSTAGRAM ↗'); link.href = post.url; link.target = '_blank'; link.rel = 'noopener';
      card.append(top, el('h4', '', head), why, link);
      card.addEventListener('click', function(e){
        if(e.target.tagName === 'A') return;
        jumpToCard(post.id);
      });
      list.append(card);
    });

    /* keep exploring */
    var fwrap = document.getElementById('briefFollow');
    fwrap.replaceChildren();
    var f = followups(sources);
    if(f.childNodes.length) fwrap.append(f);

    /* command-bar status pill */
    if(sources.length){
      status.textContent = '▸ ' + sources.length + ' SOURCES · READ THE BRIEF ↓';
      status.classList.add('show');
    } else { status.classList.remove('show'); status.textContent = ''; }
    return sources.length;
  };

  /* rooms: editorial rows carrying their biggest ring topics — the same
     vocabulary as the ring, so the index reads as part of the map */
  renderRooms = function(){
    var host = document.getElementById('rooms');
    function topicsLine(key){
      var ts = ROOM_TOPICS[key] || [];
      if(!ts.length) return '';
      return '<span class="room-topics mono">' + ts.map(function(t){
        return '<span class="rtopic" data-topic="' + esc(t) + '">' + esc(t) + '</span>';
      }).join('<span class="rsep"> · </span>') + '</span>';
    }
    function row(id, name, count){
      var active = (state.room || null) === (id || null);
      return '<button class="room' + (active ? ' active' : '') + '" data-room="' + esc(id || '') + '">' +
        '<span class="room-top"><span class="rname">' + (active ? '<span class="dot"></span>' : '') + esc(name) + '</span>' +
        '<span class="n">' + count.toLocaleString() + ' POSTS</span></span>' +
        topicsLine(id || '__all__') + '</button>';
    }
    var h = row(null, 'Everything', PIL.posts.length);
    PIL.folders.forEach(function(f){
      var c = PIL.posts.filter(function(p){ return p.folders.indexOf(f.id) !== -1; }).length;
      h += row(f.id, f.name, c);
    });
    host.innerHTML = h;
  };
  document.getElementById('rooms').addEventListener('click', function(ev){
    var t = ev.target.closest('[data-topic]');
    if(t){ searchTopic(t.dataset.topic); return; }
    var b = ev.target.closest('[data-room]');
    if(!b) return;
    state.room = b.dataset.room || null;
    renderRooms(); render(false);
    setTimeout(function(){ document.getElementById('archive').scrollIntoView({behavior:'smooth'}); }, 60);
  });
  /* tags: keep the export renderer, scroll to the archive on pick */
  var _rt = renderTags;
  renderTags = function(){
    _rt();
    document.getElementById('tags').querySelectorAll('[data-tag]').forEach(function(b){
      b.addEventListener('click', function(){ setTimeout(function(){ document.getElementById('archive').scrollIntoView({behavior:'smooth'}); }, 60); });
    });
  };

  /* fresh renders: sync the refine box, label the archive for room/tag
     filters, auto-scroll to the brief on a new query (only when it is off
     screen), and light up the search's topics on the ring */
  /* ring node ids are cleaned tags (lowercased, stripped); post tags are raw,
     so normalize the same way before lighting up the ring */
  function normTag(t){
    t = String(t || '').trim().toLowerCase();
    if(t.length < 2 || /^\\d+$/.test(t)) return null;
    if(!/^[a-z0-9][a-z0-9 _\\-.&']*$/.test(t)) return null;
    return t;
  }
  function litTopics(matches){
    var counts = {}, i, j, t;
    var qtags = state.q.toLowerCase().split(/[^a-z0-9]+/).filter(function(x){ return x.length > 1; });
    var n = Math.min(matches.length, 80);
    for(i = 0; i < n; i++){
      var pts = matches[i].tags || [];
      for(j = 0; j < pts.length; j++){
        t = normTag(pts[j]);
        if(!t || !NODE_IDS[t]) continue;
        counts[t] = (counts[t] || 0) + 1;
      }
    }
    var bar = n > 40 ? 3 : 2;
    var ids = [];
    for(t in counts){ if(counts[t] >= bar || qtags.indexOf(t) !== -1) ids.push(t); }
    ids.sort(function(a, b){ return counts[b] - counts[a]; });
    ids = ids.slice(0, 24);
    if(ids.length < 6 && matches.length && matches.length <= 60){
      // small, specific result set: light the rooms it actually lives in
      var rooms = {}, f;
      for(i = 0; i < n; i++){
        var fs = matches[i].folders || [];
        for(j = 0; j < fs.length; j++){ f = fs[j]; rooms[f] = (rooms[f] || 0) + 1; }
      }
      var topRooms = Object.keys(rooms).sort(function(a, b){ return rooms[b] - rooms[a]; }).slice(0, 1);
      if(topRooms.length && rooms[topRooms[0]] >= Math.max(2, n * 0.4)){
        var extra = [];
        for(t in NODE_IDS){
          if(ids.indexOf(t) === -1 && topRooms.indexOf(NODE_ROOM[t]) !== -1) extra.push(t);
        }
        extra.sort(function(a, b){ return NODE_COUNT[b] - NODE_COUNT[a]; });
        ids = ids.concat(extra.slice(0, Math.max(0, 12 - ids.length)));
      }
    }
    return ids.slice(0, 24);
  }
  function roomName(id){
    var f = PIL.folders.filter(function(x){ return x.id === id; })[0];
    return f ? f.name : id;
  }
  var _render = render, lastQ = '';
  render = function(append){
    _render(append);
    if(append) return;
    var q2 = document.getElementById('q2');
    if(q2 && document.activeElement !== q2) q2.value = state.q || '';
    var title = document.getElementById('title');
    if(!state.q || !state.q.trim()){
      if(state.room) title.textContent = 'Room — ' + roomName(state.room);
      else if(state.tag) title.textContent = 'Tag — ' + state.tag;
    }
    if(state.q && state.q.trim()){
      var ids = litTopics(lastMatches);
      lastLit = ids.length;
      ring.setMatches(ids);
      if(state.q !== lastQ){
        var br = document.getElementById('brief').getBoundingClientRect();
        if(br.top > window.innerHeight * 0.85 || br.bottom < 0){
          document.getElementById('brief').scrollIntoView({behavior:'smooth'});
        }
      }
    } else {
      lastLit = null;
      ring.setMatches(null);
    }
    lastQ = state.q || '';
    paintScope();
  };

  /* PWA install: shown only when the browser offers it (needs https hosting) */
  var installBtn = document.getElementById('installBtn');
  var deferredPrompt = null;
  window.addEventListener('beforeinstallprompt', function(e){
    e.preventDefault();
    deferredPrompt = e;
    if(installBtn) installBtn.style.display = '';
  });
  if(installBtn) installBtn.addEventListener('click', function(){
    if(!deferredPrompt) return;
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then(function(){
      deferredPrompt = null;
      installBtn.style.display = 'none';
    });
  });
  window.addEventListener('appinstalled', function(){
    if(installBtn) installBtn.style.display = 'none';
  });

  /* opt-in update check: one request to GitHub, only when the user asks —
     the deck never phones home on its own */
  var DECK_VERSION = '__DECK_VERSION__';
  var updBtn = document.getElementById('updCheck');
  if(updBtn) updBtn.addEventListener('click', function(){
    toast('CHECKING GITHUB FOR UPDATES…');
    fetch('https://api.github.com/repos/pjpoulose/PIL/releases/latest')
      .then(function(r){ if(!r.ok) throw new Error('http ' + r.status); return r.json(); })
      .then(function(j){
        var latest = String(j.tag_name || '').replace(/^v/, '');
        if(latest && latest !== DECK_VERSION)
          toast('UPDATE AVAILABLE — Signal Deck v' + latest + ' is on GitHub. Download the new file from the PIL releases page.');
        else
          toast('YOU ARE ON THE LATEST — Signal Deck v' + DECK_VERSION + '.');
      })
      .catch(function(){ toast('COULD NOT REACH GITHUB — check your connection and try again.'); });
  });

  /* init (the export script's own auto-run is stripped during the build) */
  renderRooms(); renderTags(); render(false);
})();
</script>"""


def esc(s):
    return htmlmod.escape(str(s or ''), quote=True)


def main():
    import sqlite3
    db = sqlite3.connect(f'file:{REAL_DB}?mode=ro', uri=True)
    d = gather_data(db)
    db.close()
    assert d['stats']['posts'] > 0, 'no posts found in ' + REAL_DB
    fmt = lambda n: f"{n:,}"

    page = render_page(d)

    g = build_graph_data()
    ring_json = json.dumps({'nodes': g['nodes'], 'edges': g['edges'],
                            'folders': g['folders']}).replace('</', '<\\/')

    # per-room top topics (ring vocabulary) for the index rows
    name_to_id = {f['name']: f['id'] for f in d['folders']}
    room_topics = {}
    for n in g['nodes']:
        fid = name_to_id.get(n.get('folder'))
        if fid:
            room_topics.setdefault(fid, []).append(n)
    for fid, ns in room_topics.items():
        ns.sort(key=lambda n: n['count'], reverse=True)
        room_topics[fid] = [n['label'] for n in ns[:3]]
    room_topics['__all__'] = [n['label'] for n in
                              sorted(g['nodes'], key=lambda n: n['count'], reverse=True)[:3]]
    room_topics_json = json.dumps(room_topics).replace('</', '<\\/')

    # --- logo + PWA assets (all inline: the deck stays one self-contained file)
    with open(os.path.join(HERE, 'pil-logo.svg')) as f:
        logo_svg = f.read().replace('<svg ', '<svg class="brand-mark" ', 1)

    def _b64(name):
        import base64
        with open(os.path.join(HERE, name), 'rb') as f:
            return base64.b64encode(f.read()).decode('ascii')

    manifest = {
        "name": "PIL — Personal Instagram Library",
        "short_name": "PIL",
        "description": "Your Instagram saves, searchable. Signal Deck.",
        "start_url": ".",
        "display": "standalone",
        "background_color": "#141210",
        "theme_color": "#141210",
        "icons": [
            {"src": "data:image/png;base64," + _b64('pil-icon-192.png'),
             "sizes": "192x192", "type": "image/png"},
            {"src": "data:image/png;base64," + _b64('pil-icon-512.png'),
             "sizes": "512x512", "type": "image/png"},
        ],
    }
    import urllib.parse
    manifest_href = 'data:application/manifest+json,' + urllib.parse.quote(
        json.dumps(manifest, separators=(',', ':')), safe='')
    pwa_head = (
        '<meta name="theme-color" content="#141210">\n'
        '<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
        '<meta name="apple-mobile-web-app-title" content="PIL">\n'
        '<meta name="pil-deck-version" content="' + DASHBOARD_VERSION + '">\n'
        '<link rel="icon" type="image/png" href="data:image/png;base64,' + _b64('pil-favicon-32.png') + '">\n'
        '<link rel="apple-touch-icon" href="data:image/png;base64,' + _b64('pil-apple-touch-180.png') + '">\n'
        '<link rel="manifest" href="' + manifest_href + '">'
    )

    # --- 1. extract the phone panel (moves above the footer) ---
    pp_start = page.index('<div id="phonepanel">')
    i = pp_start
    for _ in range(2):
        i = page.index('</div>', i) + len('</div>')
    phonepanel = page[pp_start:i]
    page = page[:pp_start] + page[i:]

    # --- 2. masthead -> nothing (the hero replaces it); searchbar -> hero cmd ---
    mh_start = page.index('<div class="masthead">')
    sb_start = page.index('<div class="searchbar">')
    page = page[:mh_start] + page[sb_start:]

    # the export searchbar is dropped: the hero carries its own #q command bar.
    # keep the kbd hint text out of it; just remove the block.
    sb_start = page.index('<div class="searchbar">')
    sb_end = page.index('</div>', sb_start) + len('</div>')
    page = page[:sb_start] + page[sb_end:]

    # --- 3. suggested topics for the brief empty state (top nodes by count) ---
    top3 = sorted(g['nodes'], key=lambda n: n['count'], reverse=True)[:3]
    suggest = ''.join(
        '<button class="sugg" data-topic="%s">%s <span class="n">%s posts</span></button>'
        % (esc(n['label']), esc(n['label']), fmt(n['count'])) for n in top3)

    hero = (HERO_HTML
            .replace('__POSTS_FMT__', fmt(d['stats']['posts'])))
    topbar = (TOPBAR_HTML
              .replace('__POSTS_FMT__', fmt(d['stats']['posts']))
              .replace('__NODES__', str(len(g['nodes'])))
              .replace('__EDGES__', str(len(g['edges'])))
              .replace('__LOGO_SVG__', logo_svg))
    brief = BRIEF_HTML.replace('__SUGGEST__', suggest)

    # --- 3b. PWA head tags, inline manifest, version stamp, footer version ---
    page = page.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + pwa_head,
        1)
    page = page.replace('<div class="footer-note">',
        '<div class="footer-note"><div class="ver-line mono">SIGNAL DECK v' +
        DASHBOARD_VERSION +
        ' · <button id="updCheck" class="upd-btn mono" type="button">CHECK FOR UPDATES</button></div>',
        1)

    # --- 4. restructure .body: side -> index, main -> archive ---
    body_start = page.index('<div class="body">')
    foot_start = page.index('<div class="footer-note">')

    side_start = page.index('<div class="side">', body_start)
    main_start = page.index('<div class="main">', side_start)
    # rooms block: from <div id="rooms"> to its close (right before tags label)
    rooms_start = page.index('<div id="rooms">', side_start)
    rooms_end = page.index('<div class="tags-label mono">', rooms_start)
    rooms_block = page[rooms_start:rooms_end].rstrip()

    # tags block: <div class="tagchips" id="tags"></div>
    tags_start = page.index('<div class="tagchips" id="tags">', rooms_end)
    tags_end = page.index('</div>', tags_start) + len('</div>')
    tags_block = page[tags_start:tags_end]

    index_sec = ''
    # index rooms/tags live inside the brief section now (left rail)
    brief = (brief
             .replace('<div id="rooms"></div>', rooms_block)
             .replace('<div class="tagchips" id="tags"></div>', tags_block))

    # archive pieces
    bh_start = page.index('<div class="browse-head">', main_start)
    sort_start = page.index('<select id="sort">', bh_start)
    sort_end = page.index('</select>', sort_start) + len('</select>')
    sort_sel = page[sort_start:sort_end]

    feat_start = page.index('<div id="featured"></div>', bh_start)
    more_start = page.index('<div class="more">', feat_start)
    more_end = page.index('</button></div>', more_start) + len('</button></div>')
    results_inner = page[feat_start:more_end]
    # drop the export's own #empty (we supply a deck-styled one); guard the duplicate
    results_inner = results_inner.replace(
        '<div class="empty" id="empty" style="display:none">Nothing in the library matches — try another search.</div>', '')
    assert 'id="empty"' not in results_inner

    # empty-state message for the archive
    empty_msg = ('<div class="empty" id="empty" style="display:none">'
                 'Nothing in the archive matches. Try a broader search — or spin the ring.</div>')

    archive_sec = (
        '<section class="archivesec" id="archive">\n<div class="wrap">\n'
        '<div class="sec-head mono"><span class="tick">▸</span> ARCHIVE — EVERY MATCH <span class="sec-meta" id="count"></span></div>\n'
        '<div class="arch-head">\n<h2 id="title">Browse PIL</h2>\n'
        '<div class="sort mono">SORT ' + sort_sel + '</div>\n</div>\n'
        + results_inner + '\n' + empty_msg + '\n'
        '</div>\n</section>'
    )

    new_body = hero + brief + archive_sec
    page = page[:body_start] + new_body + page[foot_start:]

    # --- 5. topbar above the wrapper; phone panel back above the footer ---
    # Sections (hero/brief/archive) go full-bleed via CSS while living
    # inside the export's .wrap -- no fragile div surgery needed.
    assert page.count('<div class="wrap">') >= 1
    page = page.replace('<div class="wrap">', topbar + '\n<div class="wrap">', 1)
    page = page.replace('<div class="footer-note">', phonepanel + '\n<div class="footer-note">', 1)

    # --- 6. design CSS ---
    page = page.replace('</head>', DECK_CSS + '</head>', 1)

    # --- 7. strip the export script's auto-run (signal script re-inits) ---
    auto_run = '\nrenderRooms(); renderTags(); render(false);\n'
    assert page.count(auto_run) == 1, page.count(auto_run)
    page = page.replace(auto_run, '\n/* init moved to the signal script below */\n', 1)

    # --- 8. ring scripts before </body> ---
    with open(os.path.join(HERE, 'vendor', 'echarts.min.js')) as f:
        echarts_js = f.read()
    with open(os.path.join(HERE, 'ring-component', 'pil-ring.js')) as f:
        ring_js = f.read()
    mount = (SIGNAL_JS
             .replace('__ECHARTS_JS__', echarts_js)
             .replace('__PIL_RING_JS__', ring_js)
             .replace('__RING_JSON__', ring_json)
             .replace('__ROOM_TOPICS__', room_topics_json)
             .replace('__DECK_VERSION__', DASHBOARD_VERSION)
             .replace('__MAX_COS_NUM__', f"{g['max_cos']:.4f}"))
    page = page.replace('</body>', mount + '</body>', 1)

    # --- sanity ---
    assert '<div class="masthead">' not in page
    assert '<div class="body">' not in page
    assert 'id="answers"' not in page
    assert page.count('id="phonepanel"') == 1, page.count('id="phonepanel"')
    assert page.count('id="q"') == 1, page.count('id="q"')
    assert page.count('<div class="wrap">') == 3, page.count('<div class="wrap">')
    for tok in ('__ECHARTS_JS__', '__PIL_RING_JS__', '__RING_JSON__',
                '__ROOM_TOPICS__', '__MAX_COS_NUM__', '__POSTS_FMT__', '__NODES__',
                '__EDGES__', '__SUGGEST__', '__LOGO_SVG__', '__DECK_VERSION__'):
        assert tok not in page, tok
    for rid in ('ring-mount', 'q', 'q2', 'cmdStatus', 'scopeReadout', 'themeSeg',
                'brief', 'briefEmpty', 'briefBody', 'briefQuery', 'briefMeta',
                'briefGround', 'briefContent', 'briefFollow', 'connList',
                'connCount', 'rooms', 'tags', 'title', 'count', 'sort',
                'featured', 'grid', 'empty', 'more', 'archive'):
        assert f'id="{rid}"' in page, rid

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(page)
    print('wrote', OUT, os.path.getsize(OUT), 'bytes')


if __name__ == '__main__':
    main()

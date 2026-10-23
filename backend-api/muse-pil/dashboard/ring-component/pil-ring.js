/* ============================================================================
 * PILRing — reusable topic-ring visualization component
 * ----------------------------------------------------------------------------
 * A circular topic map: topics sit on a ring (grouped by collection so color
 * arcs form), associations appear as gradient chords inside the ring.
 *
 * Requires: ECharts 5 (global `echarts`) loaded before this file.
 *
 * Usage:
 *   var ring = PILRing.mount(document.getElementById('ring-mount'), {
 *     data:       { nodes:[{id,label,count,folder,color}],
 *                    edges:[{from,to,value,cosine,core}],
 *                    folders:{name: color} },
 *     maxCosine:  0.579,          // strongest association in data
 *     theme:      'gallery',       // gallery | bloom | atlas | signal | deck
 *     minStrength: 0,             // 0..1 fraction of maxCosine; weaker links hidden
 *     showLabels: true,
 *     legendEl:   null,           // optional element to render the legend into
 *     persistTheme: null,         // optional localStorage key to remember theme
 *     onSelect:   function(node){}, // node object, or null on background click
 *     onEdge:     function(edge){}, // {from,to,cosine,value} on chord click
 *     onHover:    function(node){}, // node object, or null on hover out
 *
 * API: setTheme(name), getTheme(), setMinStrength(frac), setLabels(bool),
 *      select(id), clearSelection(), setMatches(ids|null), rotate(steps),
 *      node(id), nodes(), resize(), destroy()
 *
 * setMatches lights up a subset of topics (the rest dim) — used to show
 * search results on the ring. Pass null/[] to restore the full ring.
 *
 * Interactions: drag to pan, wheel to zoom; click the ring then scroll to
 * rotate it (down = clockwise, up = counter-clockwise) — pinch still zooms;
 * hover a topic to trace its links (fires onHover), click a topic to select
 * it (fires onSelect), click a chord to inspect the connection (fires onEdge).
 *   });
 *
 *   ring.setTheme('bloom');
 *   ring.setMinStrength(0.25);
 *   ring.setLabels(false);
 *   ring.select('claude');        // focus a topic by id
 *   ring.clearSelection();
 *   ring.rotate(4);               // +clockwise / -counter-clockwise, in topic slots
 *   ring.node('claude');          // raw node record
 *   ring.resize();
 *   ring.destroy();
 *
 * Interactions built in: drag to pan, wheel to zoom, click the ring then
 * scroll to rotate it (down = clockwise, up = counter-clockwise) — pinch
 * still zooms; hover a topic to trace its links (fires onHover), click a
 * topic to select it (fires onSelect), click a chord to inspect the
 * connection (fires onEdge).
 * ========================================================================== */
(function (root, factory) {
  root.PILRing = factory();
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  var THEMES = {
    gallery: { edgeHot: '#7dd3fc', label: '#e9ebf1', fontFace: '-apple-system, "Segoe UI", Inter, sans-serif', accent: '#7dd3fc', edgeW: 1.0, glow: 0,  edgeAlpha: 0.80 },
    bloom:   { edgeHot: '#a5b4fc', label: '#e6ecf6', fontFace: '-apple-system, "Segoe UI", Inter, sans-serif', accent: '#a5b4fc', edgeW: 0.7, glow: 14, edgeAlpha: 0.75 },
    atlas:   { edgeHot: '#c2410c', label: '#2b2620', fontFace: 'Georgia, "Iowan Old Style", serif',          accent: '#c2410c', edgeW: 1.0, glow: 0,  edgeAlpha: 0.70 },
    signal:  { edgeHot: '#f5b942', label: '#c3ccd9', fontFace: '-apple-system, "Segoe UI", Inter, sans-serif', accent: '#f5b942', edgeW: 0.9, glow: 0,  edgeAlpha: 0.70 },
    deck:    { edgeHot: '#ff5a1f', label: '#ece7db', fontFace: 'ui-monospace, "SF Mono", Menlo, Consolas, monospace', accent: '#ff5a1f', edgeW: 1.1, glow: 0, edgeAlpha: 0.85 },
  };

  // Ring order: topics grouped by collection so colored arcs form around the ring.
  var FOLDER_ORDER = ['AI', 'Indoor/Outdoor', 'Food', 'Life hacks', 'Design', 'sathia', 'AI OOTB', 'Ideas'];
  function gidx(f) { return f ? FOLDER_ORDER.indexOf(f) : FOLDER_ORDER.length; }

  function mount(el, opts) {
    opts = opts || {};
    if (typeof echarts === 'undefined') {
      throw new Error('PILRing: ECharts (global `echarts`) must be loaded first.');
    }
    var DATA = opts.data || { nodes: [], edges: [], folders: {} };
    var MAX_COS = opts.maxCosine || 1;

    var theme = THEMES[opts.theme] ? opts.theme : 'gallery';
    var T = THEMES[theme];
    var minCosFrac = opts.minStrength || 0;
    var labelsOn = opts.showLabels !== false;
    var selected = null;
    var matchSet = null; // topic ids lit by the current search; null = no filter
    var onSelect = typeof opts.onSelect === 'function' ? opts.onSelect : function () {};
    var onEdge = typeof opts.onEdge === 'function' ? opts.onEdge : function () {};
    var onHover = typeof opts.onHover === 'function' ? opts.onHover : function () {};
    var legendEl = opts.legendEl || null;
    var persistKey = opts.persistTheme || null;

    if (persistKey) {
      try {
        var saved = localStorage.getItem(persistKey);
        if (saved && THEMES[saved]) { theme = saved; T = THEMES[theme]; }
      } catch (e) {}
    }

    var counts = DATA.nodes.map(function (n) { return n.count; });
    var MIN_C = Math.min.apply(null, counts.concat([0]));
    var MAX_C = Math.max.apply(null, counts.concat([1]));

    var ordered = DATA.nodes.slice().sort(function (a, b) {
      return (gidx(a.folder) - gidx(b.folder)) || (b.count - a.count);
    });
    // viewOrder is the ring order currently on screen; rotating the ring rotates this array
    var viewOrder = ordered.slice();

    function nodeColor(n) {
      if (theme !== 'signal') return n.color;
      var g = Math.round(74 + 158 * (n.count - MIN_C) / (MAX_C - MIN_C));
      return 'rgb(' + g + ',' + (g + 5) + ',' + (g + 11) + ')';
    }
    function labelText(name, n) {
      if (theme === 'bloom' && n.count < 200) return '';
      return theme === 'signal' ? name.toUpperCase() : name;
    }
    function edgeW(e) {
      var w = e.value >= 20 ? 2.2 : e.value >= 10 ? 1.4 : 0.9;
      return +(w * T.edgeW).toFixed(2);
    }

    // ---- Gradient chords -------------------------------------------------
    // ECharts draws each edge as a quadratic bezier whose control point is
    // pulled 66% toward the ring center (curveness 0.22 * 3). We replicate the
    // circular layout's node angles exactly, then give every edge a linear
    // gradient running from the source node's color to the target node's
    // color, positioned relative to the curve's true bounding box.
    var nodeAngles = [];
    var nodeById = {};
    function indexNodes() {
      nodeById = {};
      viewOrder.forEach(function (n, i) { nodeById[n.id] = { n: n, i: i }; });
    }
    indexNodes();
    function computeAngles() {
      var R = Math.max(Math.min(el.clientWidth, el.clientHeight) / 2, 1);
      var N = viewOrder.length;
      var half = viewOrder.map(function (n) {
        var sym = 7 + Math.sqrt(n.count) * 1.15;
        var a = Math.asin(Math.min(sym / (2 * R), 1));
        return isNaN(a) ? Math.PI / 2 : a;
      });
      var occ = half.reduce(function (x, y) { return x + 2 * y; }, 0);
      var u = (2 * Math.PI - occ) / N / 2;
      nodeAngles = [];
      var h = 0;
      viewOrder.forEach(function (n, i) { h += u + half[i]; nodeAngles[i] = h; h += u + half[i]; });
    }
    function withAlpha(c, a) {
      var m = /^#([0-9a-f]{6})$/i.exec(c);
      if (m) {
        var v = m[1];
        return 'rgba(' + parseInt(v.slice(0, 2), 16) + ',' + parseInt(v.slice(2, 4), 16) +
               ',' + parseInt(v.slice(4, 6), 16) + ',' + a + ')';
      }
      m = /^rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)$/.exec(c);
      if (m) return 'rgba(' + m[1] + ',' + m[2] + ',' + m[3] + ',' + a + ')';
      return c;
    }
    function edgeGradient(e) {
      var A = nodeAngles[nodeById[e.from].i], B = nodeAngles[nodeById[e.to].i];
      var Sx = Math.cos(A), Sy = Math.sin(A), Tx = Math.cos(B), Ty = Math.sin(B);
      var Cx = 0.34 * (Sx + Tx) / 2, Cy = 0.34 * (Sy + Ty) / 2;
      var xs = [Sx, Tx], ys = [Sy, Ty];
      var dx = Sx - 2 * Cx + Tx, dy = Sy - 2 * Cy + Ty;
      if (Math.abs(dx) > 1e-9) {
        var t = (Sx - Cx) / dx;
        if (t > 0 && t < 1) xs.push((1 - t) * (1 - t) * Sx + 2 * (1 - t) * t * Cx + t * t * Tx);
      }
      if (Math.abs(dy) > 1e-9) {
        var t2 = (Sy - Cy) / dy;
        if (t2 > 0 && t2 < 1) ys.push((1 - t2) * (1 - t2) * Sy + 2 * (1 - t2) * t2 * Cy + t2 * t2 * Ty);
      }
      var minx = Math.min.apply(null, xs), maxx = Math.max.apply(null, xs);
      var miny = Math.min.apply(null, ys), maxy = Math.max.apply(null, ys);
      var w = Math.max(maxx - minx, 1e-6), h = Math.max(maxy - miny, 1e-6);
      return {
        type: 'linear', global: false,
        x: (Sx - minx) / w, y: (Sy - miny) / h,
        x2: (Tx - minx) / w, y2: (Ty - miny) / h,
        colorStops: [
          { offset: 0, color: withAlpha(nodeColor(nodeById[e.from].n), T.edgeAlpha) },
          { offset: 1, color: withAlpha(nodeColor(nodeById[e.to].n), T.edgeAlpha) },
        ],
      };
    }
    function minCos() { return minCosFrac * MAX_COS; }
    function edgeList() {
      return DATA.edges
        .filter(function (e) { return e.core || e.cosine >= minCos(); })
        .map(function (e) {
          var dim = matchSet && !(matchSet.has(e.from) || matchSet.has(e.to));
          return { source: e.from, target: e.to, value: e.value, meta: e,
                   lineStyle: { width: edgeW(e), color: edgeGradient(e), curveness: 0.22,
                                opacity: dim ? 0.05 : 1 } };
        });
    }
    function buildData() {
      return viewOrder.map(function (n) {
        var c = nodeColor(n);
        var dim = matchSet && !matchSet.has(n.id);
        return {
          id: n.id, name: n.label, meta: n,
          symbolSize: (7 + Math.sqrt(n.count) * 1.15) * (!dim && matchSet ? 1.3 : 1),
          itemStyle: { color: c, opacity: dim ? 0.08 : 1,
            borderColor: theme === 'atlas' ? 'rgba(43,38,32,0.5)' : c,
            borderWidth: theme === 'atlas' ? 1.5 : 0,
            shadowBlur: T.glow, shadowColor: c },
          label: { opacity: dim ? 0.12 : 1 },
        };
      });
    }
    function makeOption() {
      return {
        animationDuration: 700,
        animationDurationUpdate: 220,
        animationEasingUpdate: 'cubicOut',
        tooltip: {
          trigger: 'item',
          backgroundColor: 'rgba(18,22,30,0.95)', borderWidth: 0,
          textStyle: { color: '#e9ebf1', fontSize: 12 },
          formatter: function (p) {
            return p.dataType === 'node'
              ? '<b>' + p.name + '</b><br/>' + p.data.meta.count + ' posts' +
                (p.data.meta.folder ? ' · ' + p.data.meta.folder : '')
              : p.data.source + ' ↔ ' + p.data.target + '<br/>' + p.data.value + ' posts together';
          },
        },
        series: [{
          id: 'g', type: 'graph', layout: 'circular',
          circular: { rotateLabel: true },
          roam: true, draggable: false,
          label: { show: labelsOn, color: T.label, fontSize: 11, fontFamily: T.fontFace,
                   formatter: function (p) { return labelText(p.name, p.data.meta); } },
          labelLayout: { hideOverlap: true },
          emphasis: { focus: 'adjacency', scale: 1.2,
                      label: { show: true },
                      lineStyle: { color: T.edgeHot, width: 2.4, opacity: 0.95 } },
          data: buildData(),
          edges: edgeList(),
        }],
      };
    }

    computeAngles();
    var chart = echarts.init(el);
    chart.setOption(makeOption());

    var rzT = null;
    function onResize() {
      chart.resize();
      clearTimeout(rzT);
      rzT = setTimeout(function () {
        computeAngles();
        chart.setOption({ series: [{ id: 'g', edges: edgeList() }] });
        if (selected) focusOnly(selected);
      }, 250);
    }
    window.addEventListener('resize', onResize);

    function nodeIndex(id) { return viewOrder.findIndex(function (n) { return n.id === id; }); }
    function focusOnly(id) {
      chart.dispatchAction({ type: 'unfocusNodeAdjacency', seriesIndex: 0 });
      chart.dispatchAction({ type: 'focusNodeAdjacency', seriesIndex: 0, dataIndex: nodeIndex(id) });
    }
    function findNode(id) {
      for (var i = 0; i < DATA.nodes.length; i++) if (DATA.nodes[i].id === id) return DATA.nodes[i];
      return null;
    }

    function findEdge(from, to) {
      for (var i = 0; i < DATA.edges.length; i++) {
        var e = DATA.edges[i];
        if ((e.from === from && e.to === to) || (e.from === to && e.to === from)) return e;
      }
      return null;
    }

    chart.on('click', { seriesIndex: 0 }, function (p) {
      if (p.dataType === 'edge') {
        var rec = (p.data && p.data.meta) || findEdge(p.data && p.data.source, p.data && p.data.target);
        if (rec) onEdge({ from: rec.from, to: rec.to, cosine: rec.cosine, value: rec.value });
        return;
      }
      if (p.dataType !== 'node') return;
      selected = p.data.id;
      focusOnly(selected);
      onSelect(findNode(selected));
    });
    chart.on('mouseover', { seriesIndex: 0 }, function (p) {
      if (p.dataType === 'node' && p.data) onHover(findNode(p.data.id));
    });
    chart.on('mouseout', { seriesIndex: 0 }, function (p) {
      if (p.dataType === 'node') onHover(null);
    });
    chart.getZr().on('click', function (e) {
      if (e.target) return;
      selected = null;
      chart.dispatchAction({ type: 'unfocusNodeAdjacency', seriesIndex: 0 });
      onSelect(null);
    });

    // ---- rotate the ring: hold the mouse button down on it, then scroll ----
    // scroll down -> clockwise, scroll up -> counter-clockwise
    var btnDown = false, pendingDelta = 0, rotQueued = false;
    var wheelArmed = false; // a pointerdown on the ring arms scroll-to-rotate until pointerleave
    chart.getZr().on('mousedown', function () { btnDown = true; });
    function onMouseUp() { btnDown = false; }
    window.addEventListener('mouseup', onMouseUp);
    function applyRotation() {
      rotQueued = false;
      var steps = Math.round(pendingDelta / 50);
      pendingDelta = 0;
      if (!steps) return;
      rotateBy(steps);
    }
    function rotateBy(steps) {
      for (var k = 0; k < Math.abs(steps); k++) {
        if (steps > 0) viewOrder.unshift(viewOrder.pop());  // each topic moves one slot clockwise
        else viewOrder.push(viewOrder.shift());             // ...or counter-clockwise
      }
      indexNodes();
      computeAngles();
      chart.setOption({ series: [{ id: 'g', data: buildData(), edges: edgeList() }] });
      if (selected) focusOnly(selected);
    }
    function onWheel(e) {
      if (e.ctrlKey || e.metaKey) return; // pinch keeps zooming
      if (!btnDown && !wheelArmed) return; // otherwise the wheel keeps zooming
      e.preventDefault();
      e.stopPropagation();
      pendingDelta += e.deltaY; // scroll down = clockwise
      if (!rotQueued) { rotQueued = true; requestAnimationFrame(applyRotation); }
    }
    el.addEventListener('wheel', onWheel, { capture: true, passive: false });
    el.addEventListener('pointerdown', function () { wheelArmed = true; });
    el.addEventListener('pointerleave', function () { wheelArmed = false; });

    function renderLegend() {
      if (!legendEl) return;
      if (theme === 'signal') {
        legendEl.innerHTML = '<div class="cap">Signal</div>' +
          '<div class="row">node shade = post frequency</div>' +
          '<div class="row"><span class="dot" style="background:#f5b942"></span>amber = selection</div>';
        return;
      }
      legendEl.innerHTML = '<div class="cap">Collections</div>' + Object.keys(DATA.folders).map(function (f) {
        return '<div class="row"><span class="dot" style="background:' + DATA.folders[f] + '"></span>' + f + '</div>';
      }).join('');
    }
    renderLegend();

    var destroyed = false;
    var api = {
      setTheme: function (name) {
        if (!THEMES[name] || destroyed) return;
        theme = name; T = THEMES[name];
        chart.setOption(makeOption(), { replaceMerge: ['series'] });
        renderLegend();
        if (selected) focusOnly(selected);
        if (persistKey) { try { localStorage.setItem(persistKey, name); } catch (e) {} }
      },
      getTheme: function () { return theme; },
      setMinStrength: function (frac) {
        minCosFrac = Math.max(0, Math.min(1, frac || 0));
        if (destroyed) return;
        chart.setOption({ series: [{ id: 'g', edges: edgeList() }] });
        if (selected) focusOnly(selected);
      },
      setLabels: function (on) {
        labelsOn = !!on;
        if (destroyed) return;
        chart.setOption({ series: [{ id: 'g', label: { show: labelsOn } }] });
      },
      select: function (id) {
        var n = findNode(id);
        if (!n || destroyed) return;
        selected = id;
        focusOnly(id);
        onSelect(n);
      },
      clearSelection: function () {
        selected = null;
        if (destroyed) return;
        chart.dispatchAction({ type: 'unfocusNodeAdjacency', seriesIndex: 0 });
        onSelect(null);
      },
      setMatches: function (ids) {
        matchSet = (ids && ids.length) ? new Set(ids) : null;
        if (destroyed) return;
        chart.setOption({ series: [{ id: 'g', data: buildData(), edges: edgeList() }] });
        if (selected) focusOnly(selected);
      },
      rotate: rotateBy,
      node: findNode,
      nodes: function () { return DATA.nodes.slice(); },
      resize: function () { if (!destroyed) onResize(); },
      destroy: function () {
        if (destroyed) return;
        destroyed = true;
        window.removeEventListener('resize', onResize);
        window.removeEventListener('mouseup', onMouseUp);
        el.removeEventListener('wheel', onWheel, { capture: true });
        chart.dispose();
      },
    };
    return api;
  }

  return { mount: mount, THEMES: THEMES };
});

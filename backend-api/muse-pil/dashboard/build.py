#!/usr/bin/env python3
"""PIL topic-graph dashboard prototype.

Reads the real local library DB (read-only) and bakes a self-contained HTML
dashboard: tags as nodes, co-occurrence as edges. Edge selection uses cosine
association strength so mega-hubs don't collapse the layout; every node keeps
its 4 strongest links as a backbone. Data never leaves the machine.
"""
import sqlite3, os, json, base64, re, math
from collections import Counter, defaultdict

HOME = os.path.expanduser('~')
DB = os.path.join(HOME, 'workspace/instagram-kb/instakb.sqlite')
HERE = os.path.dirname(os.path.abspath(__file__))
ECHARTS_JS = os.path.join(HERE, 'vendor', 'echarts.min.js')
LOGO = os.path.join(HOME, 'workspace/skills/pil/assets/logo-400.png')
OUT = os.path.join(HERE, 'pil-topic-graph.html')

STOPWORDS = set("""a an the and or but if then else when at by for with about into
through during before after above below to from up down in out on off over under
again further once here there where why how all any both each few more most other
some such no nor not only own same so than too very can will just don should now
they them their theirs themselves what which who whom this that these those am is
are was were be been being have has had having do does did doing would could ought
i me my myself we our ours ourselves you your yours yourself yourselves he him his
himself she her hers herself it its of as s t ll re ve d m""".split())
JUNK = set("""video image carousel slide reel photo photos post posts content media
audio text https www com http send sends know knows every work works time times
get gets got make makes made like likes look looks looking one two three four five
new day days today use used using go going goes come comes see want wants need needs
let lets put take takes keep keeps part way many much also even still back well
really thing things lot lots kind kinds bit across per via within without may might
must shall sure done top best great good bad old young first last next every""".split())
BAD = STOPWORDS | JUNK

TOP_N = 140
TARGET_EDGES = 650
BACKBONE_K = 4

FOLDER_COLORS = {
    'AI': '#7dd3fc',
    'Indoor/Outdoor': '#86efac',
    'Food': '#fda4af',
    'sathia': '#fcd34d',
    'AI OOTB': '#c4b5fd',
    'Life hacks': '#5eead4',
    'Design': '#f9a8d4',
    'Ideas': '#e2e8f0',
}
NONE_COLOR = '#5b6472'


def clean_tag(t):
    t = (t or '').strip().lower()
    if len(t) < 2 or t.isdigit():
        return None
    if t in BAD:
        return None
    if not re.match(r"^[a-z0-9][a-z0-9 _\-\.&']*$", t):
        return None
    return t


def build_graph_data():
    con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
    cur = con.cursor()
    n_posts = cur.execute('SELECT COUNT(*) FROM posts').fetchone()[0]

    freq = Counter()
    for tag, c in cur.execute('SELECT tag, COUNT(*) FROM tags GROUP BY tag'):
        ct = clean_tag(tag)
        if ct:
            freq[ct] += c
    top = [t for t, _ in freq.most_common(TOP_N)]
    top_set = set(top)

    # dominant folder per tag (node color)
    qmarks = ','.join('?' * len(top))
    rows = cur.execute(f"""
        SELECT t.tag, f.name, COUNT(*) c FROM tags t
        JOIN post_folders pf ON pf.post_id = t.post_id
        JOIN folders f ON f.collection_id = pf.collection_id
        WHERE t.tag IN ({qmarks}) GROUP BY t.tag, f.name""", top).fetchall()
    best = defaultdict(lambda: (None, 0))
    for tag, folder, c in rows:
        if c > best[tag][1]:
            best[tag] = (folder, c)
    dom = {t: best[t][0] for t in top}

    # co-occurrence with cosine association strength
    pairs = cur.execute(f"""
        SELECT t1.tag, t2.tag, COUNT(*) c FROM tags t1
        JOIN tags t2 ON t1.post_id = t2.post_id AND t1.tag < t2.tag
        WHERE t1.tag IN ({qmarks}) AND t2.tag IN ({qmarks})
        GROUP BY 1, 2 HAVING COUNT(*) >= 2""", top + top).fetchall()
    scored = []
    for a, b, c in pairs:
        cos = c / math.sqrt(freq[a] * freq[b])
        scored.append((cos, a, b, c))
    scored.sort(reverse=True)

    per_node = defaultdict(list)
    for cos, a, b, c in scored:
        per_node[a].append((cos, b, c))
        per_node[b].append((cos, a, c))
    backbone = set()
    for t, lst in per_node.items():
        for cos, other, c in lst[:BACKBONE_K]:
            backbone.add((min(t, other), max(t, other)))

    chosen = {(min(a, b), max(a, b)): (cos, c) for cos, a, b, c in scored[:TARGET_EDGES]}
    for key in backbone:
        if key not in chosen:
            a, b = key
            c = next((cc for co, x, y, cc in scored
                      if (x, y) == (a, b) or (x, y) == (b, a)), 2)
            cos = next((co for co, x, y, cc in scored
                        if (x, y) == (a, b) or (x, y) == (b, a)), 0.0)
            chosen[key] = (cos, c)

    max_cos = max(cos for cos, _ in chosen.values())
    edge_list = []
    for (a, b), (cos, c) in chosen.items():
        length = int(max(80, 300 - 380 * cos))
        edge_list.append({'from': a, 'to': b, 'value': c,
                          'cosine': round(cos, 4), 'length': length,
                          'core': (a, b) in backbone})

    nodes = []
    for t in top:
        nodes.append({
            'id': t, 'label': t,
            'value': round(math.sqrt(freq[t]) * 6, 1),
            'count': freq[t],
            'color': FOLDER_COLORS.get(dom[t], NONE_COLOR),
            'folder': dom[t],
            'title': f'{t} · {freq[t]} posts',
        })

    # sample posts per tag
    samples = {}
    for t in top:
        rows = cur.execute("""
            SELECT p.author, p.url, substr(replace(p.caption, char(10), ' '), 1, 140)
            FROM posts p JOIN tags tg ON tg.post_id = p.post_id
            WHERE tg.tag = ? LIMIT 6""", (t,)).fetchall()
        samples[t] = [{'author': a or 'unknown', 'url': u, 'snippet': s or ''}
                      for a, u, s in rows]
    con.close()
    print(f'nodes={len(nodes)} edges={len(edge_list)} max_cos={max_cos:.3f} posts={n_posts}')
    return {'nodes': nodes, 'edges': edge_list, 'samples': samples,
            'folders': FOLDER_COLORS, 'n_posts': n_posts, 'max_cos': max_cos}


def main():
    data = build_graph_data()
    with open(ECHARTS_JS) as f:
        echarts_js = f.read()
    with open(os.path.join(HERE, 'ring-component', 'pil-ring.js')) as f:
        ring_js = f.read()
    with open(LOGO, 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode()
    with open(os.path.join(HERE, 'template.html')) as f:
        tpl = f.read()
    graph = {'nodes': data['nodes'], 'edges': data['edges'],
             'samples': data['samples'], 'folders': data['folders']}
    html = (tpl
            .replace('__ECHARTS_JS__', echarts_js)
            .replace('__PIL_RING_JS__', ring_js)
            .replace('__GRAPH_JSON__', json.dumps(graph))
            .replace('__LOGO_B64__', logo_b64)
            .replace('__N_POSTS__', str(data['n_posts']))
            .replace('__N_NODES__', str(len(data['nodes'])))
            .replace('__N_EDGES__', str(len(data['edges'])))
            .replace('__MAX_COS__', f"{data['max_cos']:.4f}"))
    with open(OUT, 'w') as f:
        f.write(html)
    print('wrote', OUT, os.path.getsize(OUT), 'bytes')


if __name__ == '__main__':
    main()

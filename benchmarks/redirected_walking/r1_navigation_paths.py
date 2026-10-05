"""Deterministic navigation-aware virtual paths for the declared R1 benchmark.

This is NOT the unpublished Williams et al. static-path generator. It is an
explicit benchmark family inspired by navigation-aware RDW path planning.

The generator operates on a rectangular VE with line-segment obstacles. It
samples collision-free clearance-grid nodes, connects visible node pairs, then
uses deterministic shortest paths between seeded random endpoints until a target
distance is reached. The same generated virtual path is reused across all
controller/physical-geometry conditions for a seed.
"""
from __future__ import annotations
import heapq, math, random
from r1_path_admission import segment_is_valid

def _grid_nodes(width,height,segments,spacing=1.0,margin_m=0.5):
    xs=[]; x=margin_m
    while x<=width-margin_m+1e-9: xs.append(round(x,9)); x+=spacing
    ys=[]; y=margin_m
    while y<=height-margin_m+1e-9: ys.append(round(y,9)); y+=spacing
    pts=[(x,y) for x in xs for y in ys]
    return [p for p in pts if segment_is_valid(p,p,segments,margin_m)]

def _graph(nodes,segments,spacing=1.0,margin_m=0.5):
    idx={p:i for i,p in enumerate(nodes)}; adj=[[] for _ in nodes]
    steps=[(-spacing,0),(spacing,0),(0,-spacing),(0,spacing),
           (-spacing,-spacing),(-spacing,spacing),(spacing,-spacing),(spacing,spacing)]
    for i,p in enumerate(nodes):
        for dx,dy in steps:
            q=(round(p[0]+dx,9),round(p[1]+dy,9))
            j=idx.get(q)
            if j is not None and segment_is_valid(p,q,segments,margin_m):
                adj[i].append((j,math.hypot(dx,dy)))
    return adj

def _shortest(nodes,adj,s,t):
    inf=float("inf"); dist=[inf]*len(nodes); prev=[None]*len(nodes); dist[s]=0; pq=[(0,s)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        if u==t: break
        for v,w in adj[u]:
            nd=d+w
            if nd<dist[v]-1e-12:
                dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
    if not math.isfinite(dist[t]): return None
    out=[]; u=t
    while u is not None: out.append(nodes[u]); u=prev[u]
    return list(reversed(out))

def generate_navigation_path(seed,segments,width=14.0,height=14.0,target_m=35.0,
                             spacing=1.0,margin_m=0.5,start=(7.5,7.5)):
    nodes=_grid_nodes(width,height,segments,spacing,margin_m)
    if not nodes: raise RuntimeError("no walkable grid nodes")
    start_i=min(range(len(nodes)),key=lambda i:math.dist(nodes[i],start))
    adj=_graph(nodes,segments,spacing,margin_m)
    rng=random.Random(seed); route=[nodes[start_i]]; total=0.0; cur=start_i; legs=0
    while total<target_m:
        candidates=list(range(len(nodes))); rng.shuffle(candidates); chosen=None
        for t in candidates:
            if t==cur: continue
            p=_shortest(nodes,adj,cur,t)
            if p and len(p)>1:
                leg=sum(math.dist(p[i],p[i+1]) for i in range(len(p)-1))
                if leg>=2.0: chosen=(t,p,leg); break
        if chosen is None: raise RuntimeError("no reachable navigation target")
        cur,p,leg=chosen; route.extend(p[1:]); total+=leg; legs+=1
    return route,{"seed":seed,"target_m":target_m,"actual_m":total,"spacing_m":spacing,
                  "margin_m":margin_m,"legs":legs,"nodes":len(nodes),
                  "tier":"R1-BENCHMARK-navigation-aware-not-R2-or-R3"}

def route_length(route):
    return sum(math.dist(route[i],route[i+1]) for i in range(len(route)-1))

def route_segments_valid(route,segments,margin_m=0.5):
    return all(segment_is_valid(route[i],route[i+1],segments,margin_m) for i in range(len(route)-1))

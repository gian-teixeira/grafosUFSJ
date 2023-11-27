

def kruskal(graph):
    parent = { node : node for node in graph.get_nodes() }
    sorted_edges = sorted(graph.get_edges(), key = lambda e: e.weight)
    mst = set()

    def get_parent(u):
        if parent[u] == u: return u
        parent[u] = get_parent(parent[u])
        return parent[u]

    def make_union(u, v):
        pu = get_parent(u)
        pv = get_parent(v)
        if pu != pv: parent[v] = u
        return pu != pv

    for edge in sorted_edges:
        if make_union(edge.src, edge.dest):
            mst.add(edge)

    return mst

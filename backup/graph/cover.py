def vertex_cover(graph):
    successors, predecessors = graph.get_relations()
    nodes = sorted(graph.nodes, 
                   key = lambda node : -graph.get_node_degree(node, -1))
    excluded = set()
    cover = set()

    for base in nodes:
        if not base in excluded: cover.add(base)
        if not base in successors: continue
        for neighbor in successors[base]:
            if base in cover:
                excluded.add(neighbor)
            elif neighbor in excluded:
                excluded.remove(neighbor)
                cover.add(neighbor)
    
    recover = set()

    for node in cover:
        if not base in successors: continue
        remove = True
        for neighbor in successors[node]:
            if not neighbor in cover: 
                remove = False
                break
        if not remove:
            recover.add(node)

    return recover

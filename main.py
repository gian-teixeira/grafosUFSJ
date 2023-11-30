import networkx as nx
import numpy as np
from copy import deepcopy
from sys import argv

gml = nx.read_gml(argv[1], label = 'id')
n = len(gml.nodes)
adj_matrix = np.zeros(shape = (n,n), dtype = np.int8)

for edge in gml.edges:
    src, dest = edge
    adj_matrix[src][dest] = 1
    adj_matrix[dest][src] = 1

nodes = deepcopy(gml.nodes)
priority = np.zeros(n)
cover_edges = set()
cover_nodes = set()

while len(cover_edges) < len(gml.edges):
    nodes = sorted(nodes, key = lambda v: - np.count_nonzero(adj_matrix[v]))
    u = nodes[0]
    del nodes[0]

    if priority[u]: 
        priority[u] -= 1
        nodes.append(u)
        continue
        
    cover_nodes.add(u)
    for v in range(n):
        if not adj_matrix[u][v]: continue
        adj_matrix[v][u] = 0
        priority[v] += 1
        cover_edges.add((min(u,v),max(u,v)))

for node in cover_nodes:
    print('Esquina', node)
    print('Ruas monitoradas:')
    for v in range(n):
        if not adj_matrix[node][v]: continue
        print('\t', gml.get_edge_data(node,v)['name'])
    print()
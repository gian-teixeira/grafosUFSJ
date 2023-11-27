import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

gml = nx.read_gml('sjdr.gml', label = 'id')
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

edge_color = ['#20a387' if edge in cover_edges else 'black' for edge in gml.edges]
node_color = ['#481567' if node in cover_nodes else '#000000' for node in gml.nodes]
node_size = [30 if node in cover_nodes else 5 for node in gml.nodes]

print(node_size.count(30), node_size.count(5))

nx.draw(gml, node_size = node_size, 
        edge_color = edge_color,
        node_color = node_color,
        pos = nx.kamada_kawai_layout(gml))
plt.show()
plt.savefig('teste.png')

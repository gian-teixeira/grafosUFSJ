from queue import Queue
from copy import deepcopy
from .level import get_levels
from .path import get_path

def update_slack_graph(graph, path, flow):
    for edge in path:
        reverse = graph.get_edge(edge.dest,edge.src)
        if not reverse:
            reverse = graph.add_edge(edge.dest, edge.src)
        reverse.weight += flow
        edge.weight -= flow
        if edge.weight == 0:
            graph.remove_edge(edge.src, edge.dest)

def get_min_flow(graph, path):
    flow = path[0].weight
    for edge in path:
        flow = min(flow, edge.weight)
    return flow

def get_max_flow(graph, s, t, flow = 0):
    graph = deepcopy(graph)
    max_flow = flow
    
    first = True
    while path := get_path(graph, s, t):
        update_slack_graph(graph, path, flow)
        if first: 
            first = False
            continue
        flow = get_min_flow(graph, path)
        max_flow += flow
    
    return max_flow

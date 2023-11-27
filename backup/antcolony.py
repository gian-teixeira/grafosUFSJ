import random

class AntColony:
    def __init__(self, target_graph, params):
        N = len(target_graph)
        self.graph = target_graph
        self.pheromone = [[0]*N for i in range(N)]

        self.ants = list()
        self.params = params
        self.min_cost_path = None
        self.min_cost = None
    
    def get_probability_vector(self, source, adjacents):
        total_pheromone = 0
        
        for adj in adjacents:
            edge = (source, adj) 
            total_pheromone += self.pheromone[edge]
        
        probabilities = list(map(
            lambda p: p/total_pheromone,
            adjacents
        ))
        
        return probabilities

    def add_ant(self, source_node):
        ant = self.Ant(source_node, self)
        self.ants.append(ant)

    def deposit_pheromone(self, edge, path_cost):
        self.pheromone[edge] += self.params.Q / path_cost

    def set_evaporation(self):
        for edge in self.graph.get_edges():
            self.pheromone[edge] *= (1 - self.params.evaporation)

    def run_epoch(self):
        for ant in self.ants:
            path = ant.find_path()
            path_cost = sum([edge.weight for edge in path])
            for edge in path:
                self.deposit_pheromone(edge, path_cost)
            if not self.min_cost_path \
               or self.min_cost and self.min_cost > path_cost:
                self.min_cost = path_cost
                self.min_cost_path = path

    class Ant:
        def __init__(self, source, colony):
            self.colony = colony
            self.source_node = source
            self.current_node = source
            self.path = None
            self.visited = None
        
        def go_next(self):
            successors = self.colony.graph.get_successors(self.current_node)
            enabled_neighbors = list(filter(self.path_filter, successors))

            if len(enabled_neighbors) == 0: return None

            threshold = self.colony.get_probability_vector(
                    self.current_node, enabled_neighbors)
            
            return random.choices(successors, weights = threshold)
        
        def find_path(self):
            self.path = set()
            self.visited = set()
            previous = self.source_node
            self.visited.add(previous)

            while current := self.go_next():
                edge = self.colony.graph.get_edge(previous, current)
                self.path.add(edge)
                self.visited.add(current)

            return self.path

        def path_filter(self, adjcent):
            return not adjcent in self.visited
    
    class Parameters:
        def __init__(self, evaporation, deposit):
            self.evaporation = evaporation
            self.deposit = deposit

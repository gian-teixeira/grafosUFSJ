import random
import numpy as np
from graph import CompleteGraph

class AntColony:
    def __init__(self, target_graph : CompleteGraph, params):
        N = len(target_graph)
        self.distance = target_graph
        self.pheromone = np.ones_like(target_graph)*0.01
        print(N)

        self.ants = list()
        self.params = params
        self.min_cost_path = None
        self.min_cost = None

    def get_probability_vector(self, src, exclude : set = set()):
        tau = lambda src, dest : np.power(self.pheromone[src][dest], self.params.alpha)
        eta = lambda src, dest : np.power(self.distance[src][dest], self.params.beta)
        edge_prob = lambda src, dest, basis : tau(src,dest)*eta(src,dest) / basis

        basis = sum([tau(src,dest) * eta(src,dest)
                     if not dest in exclude else 0
                     for dest in self.distance.nodes])

        probabilities = [edge_prob(src,dest,basis)
                         if not dest in exclude else 0
                         for dest in self.distance.nodes]

        return probabilities

    def add_ant(self, source_node):
        ant = self.Ant(source_node, self)
        self.ants.append(ant)

    def deposit_pheromone(self, edge, path_cost):
        self.pheromone[edge] += self.params.deposit / path_cost

    def set_evaporation(self):
        for edge in self.distance.get_edges():
            self.pheromone[edge] *= (1 - self.params.evaporation)

    def run_epoch(self):
        for ant in self.ants:
            path = ant.find_path()
            edges = list(zip(path,path[1:]))
            path_cost = sum([self.distance[edge] for edge in edges])
            for edge in edges:
                self.deposit_pheromone(edge, path_cost)
            if not self.min_cost_path \
               or self.min_cost and self.min_cost > path_cost:
                self.min_cost = path_cost
                self.min_cost_path = path

    class Ant:
        def __init__(self, source, colony):
            self.colony = colony
            self.src = source
            self.cur = source
            self.path = None
            self.visited = None
        
        def go_next(self):
            target = self.colony.distance[self.cur]
            if len(self.path) == len(target): return None
            threshold = self.colony.get_probability_vector(self.cur, exclude = self.visited)
            chosen = np.random.choice(np.arange(len(target)), p = threshold)
            return chosen
        
        def find_path(self):
            self.visited = set()
            self.path = list()

            previous = self.src
            self.visited.add(previous)
            self.path.append(previous)

            while (current := self.go_next()) is not None:
                self.path.append(current)
                self.visited.add(current)
            
            return list(self.path) + [self.src]

        def path_filter(self, node):
            return not node in self.visited
    
    class Parameters:
        def __init__(self, evaporation, deposit, iterations,
                     alpha, beta):
            self.evaporation = evaporation
            self.deposit = deposit
            self.iterations = iterations
            self.alpha = alpha
            self.beta = beta

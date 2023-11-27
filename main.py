from antcolony import *

adj_matrix = []

dist_file = 'dist.txt'
with open(dist_file, 'r') as file:
    for line in file:
        adj_matrix.append([float(i) for i in line.split()])

graph = CompleteGraph(adj_matrix)

params = AntColony.Parameters(0.5, 1, 100000, 0.5, 0.5)
colony = AntColony(graph, params)

for i in range(len(adj_matrix)): colony.add_ant(i)
for i in range(params.iterations):
    colony.run_epoch()

print(colony.min_cost)
from antcolony import *
import matplotlib.pyplot as plt
from tqdm import tqdm

adj_matrix = []

dist_file = 'dist.txt'
with open(dist_file, 'r') as file:
    for line in file:
        adj_matrix.append([float(i) for i in line.split()])

graph = CompleteGraph(adj_matrix)

params = AntColony.Parameters(0.3, 1, 500, 0.7, 0.3, 0.4)
colony = AntColony(graph, params)

data = []

for i in range(len(adj_matrix)): colony.add_ant(i)
for i in tqdm(range(params.iterations)):
    colony.run_epoch()
    data.append(colony.min_cost)

fig = plt.figure()
plt.plot(range(params.iterations), data)
#plt.show()

print(colony.min_cost)
import numpy as np

class CompleteGraph(np.ndarray):
    def __new__(cls, adj_matrix):
        if len(adj_matrix) != len(adj_matrix[0]):
            raise ValueError('Matrix need to be square')
        adj_matrix = np.array(adj_matrix, dtype = float)
        N = len(adj_matrix)
        return super().__new__(cls, shape = (N,N), buffer = adj_matrix)

    def __init__(self, adj_matrix):
        self.nodes = list(range(len(adj_matrix)))
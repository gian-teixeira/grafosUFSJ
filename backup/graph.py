class StaticGraph(list):
    def __init__(self, matrix):
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix must be square")
        super().__init__(matrix)
        self.nodes = list(range(len(self)))

    @staticmethod
    def from_file(path):
        with open(path, 'r') as file:
            matrix = []
            for line in file:
                matrix.append([float(i) for i in line.split()])
            return StaticGraph(matrix)

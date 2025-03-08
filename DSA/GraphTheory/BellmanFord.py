

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.distance = [float("Inf")] * self.V
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])





if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 1, -1)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 2)
    graph.add_edge(1, 4, 2)
    graph.add_edge(3, 2, 5)
    graph.add_edge(3, 1, 1)
    graph.add_edge(4, 3, -3)
    graph.bellman_ford(0)
    graph.print_distance()



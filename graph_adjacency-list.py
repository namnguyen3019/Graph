# Implementation of an directed graph using Adjcency Lists

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self, v, weight):
        if v not in self.neighbors:
            self.neighbors.append((v, weight))
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v, weight)
            return True
        else:
            return False

    def print_graph(self):
        for key in self.vertices:
            print(key + str(self.vertices[key].neighbors))


g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = [('AB', 5), ('BC', 30), ('BD', 60), ('BE', 20),
         ('EF', 10), ('EG', 75), ('FE', -15), ('GH', 100), ('CD', 5), ('CG', 25), ('DI', -50), ('IJ', -10)]
for edge in edges:
    g.add_edge(edge[0][0], edge[0][1], edge[1])

g.print_graph()

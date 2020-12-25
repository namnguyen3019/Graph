'''
    Implementation of graph using dictionary
    Graph will have format like:
    {
        A : {B: 3, C:2},
        B : {D: 2, E: 2},
        C : {},
        D : {},
        E : {}
    }

    which mean from A: can travel to B (cost 3) and to C (cost 2)
    and so on
'''

# Define a node which will be added to the graph
class AdjNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# A class to represent a graph
# It is a list of the adjacency lists
# Size of the array will be the no. of the vertices "V"

class Graph:
    def __init__(self, V=0, E=0):
        self.V = V
        self.edge = []
        self.E = E
        self.graph = {}

    def add_node(self, newNode):
        if isinstance(newNode, AdjNode):
            self.V += 1
            self.graph[newNode] = {}

    def add_edge(self, src, dest, weight):
        if isinstance(src, AdjNode) and isinstance(dest, AdjNode):
            self.graph[src][dest] = weight
            self.edge.append([src, dest, weight])
            self.E += 1
    def print_graph(self):
        for node in self.graph:
            # print(self.graph[node])
            print(node.data + ' -> ', end="")
            for key in self.graph[node]:
                print(key.data, end=':')
                print(self.graph[node][key], end=", ")
            print()
    def print_node(self):
        for node in self.graph:
            print(node.data)
    def print_edge(self):
        for edge in self.edge:
            print(edge[0].data, edge[1].data, edge[2])
V = 5
graph = Graph()
node_A = AdjNode('A')
node_B = AdjNode('B')
node_C = AdjNode('C')
node_D = AdjNode('D')
node_E = AdjNode('E')

graph.add_node(node_A)
graph.add_node(node_B)
graph.add_node(node_C)
graph.add_node(node_D)
graph.add_node(node_E)

graph.add_edge(node_A, node_B, 1)
graph.add_edge(node_A, node_C, 2)
graph.add_edge(node_A, node_D, 3)
graph.add_edge(node_B, node_C, 1)
graph.add_edge(node_B, node_E, 2)


print(graph.E)
print(graph.V)
graph.print_graph()
graph.print_edge()



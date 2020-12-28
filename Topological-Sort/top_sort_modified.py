
'''
    graph = {
        'A': [Edge('A','B',3), Edge('A','C',2), Edge('A','E',3)],
        'B': [Edge('B','D',1), Edge('B','C',6)],
        'C': [Edge('C','D',1), Edge('C','E',10)],
        'D': [Edge('D','E',5)],
        'F': [Edge('F','E',7)]
    }
'''

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
    
def dfs(node, visited, ordering, graph):

    visited[node] = True

    edges = graph[node]

    for edge in edges:
        if edge.end not in visited:
            dfs(edge.end, visited, ordering, graph)
    
    ordering.insert(0, node)

def topSort(graph):

    ordering = []

    visited = {}

    for node in graph:
        if node not in visited:
            dfs(node, visited, ordering, graph)

    return ordering


if __name__ == "__main__":

    graph = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    graph['A'].append(Edge('A','B',3))
    graph['A'].append(Edge('A','C',2))
    graph['A'].append(Edge('A','F',3))
    graph['B'].append(Edge('B','D',1))
    graph['B'].append(Edge('B','C',6))
    graph['C'].append(Edge('C','D',1))
    graph['C'].append(Edge('C','E',10))
    graph['D'].append(Edge('D','E',5))
    graph['F'].append(Edge('F','E',7))

    print("The topological order is: ")
    print(topSort(graph))
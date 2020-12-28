
# input: a graph, return a topological order

'''
    graph = {
        0: [Edge(0,1,3), Edge(0,2,2), Edge(0,5,3)],
        1: [Edge(1,3,1), Edge(1,2,6)],
        2: [Edge(2,3,1), Edge(2,4,10)],
        3: [Edge(3,4,5)],
        5: [Edge(5,4,7)]
    }
'''
class Edge:
    def __init__(self, start, end ,weight):
        self.start = start
        self.end = end
        self.weight = weight

def dfs(pos, visited, visitedNodes, graph):
    # mark node at position "at" as visited
    visited[pos] = True

    # get all edges from node at position "pos"
    edges = graph[pos]

    if edges is not None:
        for edge in edges:
            if not visited[edge.end]:
                dfs(edge.end, visited, visitedNodes, graph)
    visitedNodes.append(pos)

def topSort(graph, numNodes):
    ordering = [0 for i in range(numNodes)]
    visited = [False for i in range(numNodes)]

    # fill the ordering[lastIndex] with the first node found
    i = numNodes - 1

    for pos in range(numNodes):
        if visited[pos] is False:
            visitedNodes = []
            dfs(pos, visited, visitedNodes,graph)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i = i-1
    return ordering


graph = {}
N = 7

for i in range(N):
    graph[i] = []

graph[0].append(Edge(0,1,3))
graph[0].append(Edge(0,2,2))
graph[0].append(Edge(0,5,3))
graph[1].append(Edge(1,3,1))
graph[1].append(Edge(1,2,6))
graph[2].append(Edge(2,3,1))
graph[2].append(Edge(2,4,10))
graph[3].append(Edge(3,4,5))
graph[5].append(Edge(5,4,7))

print("The topological order is: ")
print(topSort(graph, N))
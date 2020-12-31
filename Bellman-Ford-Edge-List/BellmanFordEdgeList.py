'''

'''
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def bellManFord(edges, V, start):

    dist = [float('inf') for i in range(V)]
    dist[start] = 0

    # Run the first time

    relaxedAnEdge = True

    for i in range(V-1):
        if relaxedAnEdge:
            relaxedAnEdge = False
            for edge in edges:
                if dist[edge.start] + edge.weight < dist[edge.end]:
                    dist[edge.end]  = edge.weight + dist[edge.start]
                    relaxedAnEdge = True
    
    # Run the second time
    relaxedAnEdge = True

    for i in range(V-1):
        if relaxedAnEdge:
            relaxedAnEdge = False
            for edge in edges:
                if dist[edge.start] + edge.weight < dist[edge.end]:
                    dist[edge.end]  = float('-inf')
                    relaxedAnEdge = True

    return dist


if __name__ == "__main__":
    E = 10
    V = 9
    start = 0
    edges = [None for i in range(E)]
    edges[0] = Edge(0, 1, 1)
    edges[1] = Edge(1, 2, 1)
    edges[2] = Edge(2, 4, 1)
    edges[3] = Edge(4, 3, -3)
    edges[4] = Edge(3, 2, 1)
    edges[5] = Edge(1, 5, 4)
    edges[6] = Edge(1, 6, 4)
    edges[7] = Edge(5, 6, 5)
    edges[8] = Edge(6, 7, 4)
    edges[9] = Edge(5, 7, 3)


    dist = bellManFord(edges, V, start)
    for i in range(len(dist)):
        print(" The cost to get from {0} to {1} is {2}\n".format(start, i, dist[i]))
    



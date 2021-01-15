

def createGraph(n):
    return [[] for _ in range(n)]

def addEdge(graph, node1, node2):
    graph[node1].append(node2)
    graph[node2].append(node1)


def findBridges(graph):
    node_id = 0
    # Low-link value
    low = [None for _ in range(len(graph))]

    # id of each node
    ids = [None for _ in range(len(graph))]

    visited = {}

    # INITIALIZE list of bridges
    bridges = []

    # Define depth first search algo

    def dfs(pos, parent, bridges):
        visited[pos] = True
        nonlocal node_id
        low[pos] = ids[pos] = node_id
        node_id += 1
        
        for node in graph[pos]:
            if node == parent: continue
            if node not in visited:
                dfs(node, pos, bridges)

                low[pos] = min(low[pos], low[node])
                # If the id of the node is less the low-ink: add 2 node into bridges
                if ids[pos] < low[node]:
                    bridges.append(pos)
                    bridges.append(node)
                    
            else:
                low[pos] = min(low[pos], ids[node])

    # For all edge in the graph: do dfs
    for i in range(len(graph)):
        if i not in visited:
            dfs(i, -1, bridges)
    
    return bridges

if __name__ == "__main__":

    graph = createGraph(9)
    print(len(graph))
    addEdge(graph, 0, 1)
    addEdge(graph, 0, 2)
    addEdge(graph, 1, 2)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 4)
    addEdge(graph, 2, 5)
    addEdge(graph, 5, 6)
    addEdge(graph, 6, 7)
    addEdge(graph, 7, 8)
    addEdge(graph, 8, 5)

    bridges = findBridges(graph)
    for i in range(len(bridges)//2):
        node1 = bridges[2*i]
        node2 = bridges[2*i+1]
        print(f"Bridge between node: {node1} and {node2}")
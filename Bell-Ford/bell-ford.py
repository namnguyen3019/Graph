
graph = {
    'A': {'B': 5},
    'B': {'C': 30, 'D': 60, 'E': 20},
    'C': {'D': 5, 'J': 50, 'G': 25},
    'D': {'I': -50},
    'E': {'F': 10, 'G': 75},
    'F': {'E': -15},
    'G': {'H': 100},
    'I': {'J': -10},
    'J': {},
    'H': {}
}


def bellFord(graph, start):
    # Find vertices and edges:
    V = 0
    E = 0
    for key in graph:
        V += 1
        for _ in graph[key]:
            E += 1

    # A dictionary to store distance from start to every node in the graph
    dis = {}
    for node in graph:
        dis[node] = float('inf')
    dis[start] = 0

    for _ in range(V):
        # from node, it can go to:
        for node in graph:
            path = graph[node].items()
            for child_node, weight in path:
                if dis[node] + weight < dis[child_node]:
                    dis[child_node] = dis[node] + weight

    # Second loop
    for _ in range(V):
        for node in graph:
            path = graph[node].items()
            for child_node, weight in path:
                if dis[node] + weight < dis[child_node]:
                    dis[child_node] = float('-inf')
    return dis


# Return a diction contains shorest distance from A to every node in the graph
dis = bellFord(graph, 'A')
print(dis)

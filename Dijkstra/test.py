import heapq

graph = {
    'A': {'B': 50, 'C': 45, 'D': 10},
    'B': {'C': 10, 'D': 15},
    'C': {'E': 3},
    'D': {'A': 10, 'E': 15},
    'E': {'B': 20, 'C': 35},
    'F': {'E': 3}
}


def dijkstra(graph, start):
    # Create a dictionary to store shortest path from start to other nodes
    dis = {}
    for node in graph:
        dis[node] = float('inf')    # initialize the distance to inf
    # distance from node %start to itself is 0
    dis[start] = 0

    # Track visited node, if not visited: put in the priority queue
    visited = {}
    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:
        (D, node) = heapq.heappop(pq)
        # Mark this node is visited:
        visited[node] = True

        # From this node, can travel to other nodes in path_options
        path_options = graph[node].items()

        for child_node, weight in path_options:
            # If the child_node not been visited, push in the priority queue
            if child_node not in visited:
                heapq.heappush(pq, (weight, child_node))

            # Update the shortest distance if:
            if dis[node] + weight < dis[child_node]:
                dis[child_node] = dis[node] + weight

    return dis

print(dijkstra(graph, 'B'))
print(dijkstra(graph, 'A'))

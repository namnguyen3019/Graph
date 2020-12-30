import heapq

graph = {
    'A': {'B': 50, 'C': 45, 'D': 10},
    'B': {'C': 10, 'D': 15},
    'C': {'E': 3},
    'D': {'A': 10, 'E': 15},
    'E': {'B': 20, 'C': 35},
    'F': {'E': 3}
}


def dijkstra(graph, start, end):

    # records of shorest path from start to a node
    shortest_path = {}

    # initialize the shorest_path with value to everynode is infinity
    for node in graph:
        shortest_path[node] = float('inf')
    # exception for start node: distance from start node to itself is 0
    shortest_path[start] = 0

    # For back tracking from end to start
    track_precessor = {}

    # Initial priority queue with heapq
    pq = [(0, start)]
    heapq.heapify(pq)
    # Track the visited node:
    visited = {}
    while pq:

        node = heapq.heappop(pq)[1]

        visited[node] = True

        path_options = graph[node].items()

        for child_node, weight in path_options:
            if child_node not in visited:
                heapq.heappush(pq, (weight, child_node))
            
            if weight + shortest_path[node] < shortest_path[child_node]:
                shortest_path[child_node] = weight + shortest_path[node]
                track_precessor[child_node] = node

    # back tracking from to end to start
    current_node = end
    optimal_path = []
    while current_node != start:
        try:
            optimal_path.insert(0, current_node)
            current_node = track_precessor[current_node]
        except KeyError:
            print('Path not found')
            break
    optimal_path.insert(0, start)

    if shortest_path[end] != float('inf'):
        print('Optimal path: ' + str(optimal_path))
        print('Total cost: ' + str(shortest_path[end]))


dijkstra(graph, 'B', 'E')
dijkstra(graph, 'A', 'E')

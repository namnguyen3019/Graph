'''
    This version of Dijkstra will stop when reaching the end node.
    Do not need to travel every node in the graph
'''
import heapq
graph = {
    'A': {'B': 50, 'C': 45, 'D': 10},
    'B': {'C': 10, 'D': 15},
    'C': {'E': 30},
    'D': {'A': 10, 'E': 15},
    'E': {'B': 20, 'C': 35},
    'F': {'E': 3}
}


def dijkstra(graph, start, end):

    # records the shorest distance from node "start" to other nodes
    shortest_dist = {}
    for node in graph:
        shortest_dist[node] = float('inf')
    # Initial the base case: travel shortest distance from start to start is 0
    shortest_dist[start] = 0

    # Store back tracking dictionary:
    track_precessor = {}
    # Track visited node
    visited = {}
    # Initial a priority queue:
    pq = [(0, start)]
    heapq.heapify(pq)

    while pq:

        node = heapq.heappop(pq)[1]

        visited[node] = True

        path_options = graph[node].items()
        
        for child_node, weight in path_options:
            if child_node not in visited:
                heapq.heappush(pq, (weight, child_node))
            if weight + shortest_dist[node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight + shortest_dist[node]
                track_precessor[child_node] = node
        if node == end: break
    # back tracking from to end to start

    print("Shorest distance: ", shortest_dist[end])
    if shortest_dist[end] != float('inf'):
        cur_node = end
        optimal_path = []
        while cur_node != start:
            optimal_path.insert(0, cur_node)
            cur_node = track_precessor[cur_node]
        optimal_path.insert(0, start)
        print(optimal_path)
    else:
        print("Path not found")

dijkstra(graph, 'A', 'E')  # result: 25
dijkstra(graph, 'A', 'C')  # result: 45
dijkstra(graph, 'A', 'F')  # result: path not found

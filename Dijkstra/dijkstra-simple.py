graph = {
    'A': {'B': 50, 'C': 45, 'D': 10},
    'B': {'C': 10, 'D': 15},
    'C': {'E': 30},
    'D': {'A': 10, 'E': 15},
    'E': {'B': 20, 'C': 35},
    'F': {'E': 3}
}


def dijkstra(graph, start, end):
    # unvisitedNodes store all unvisited nodes in the graph
    unvisitedNodes = graph

    # records of shorest path from start to a node
    shortest_path = {}
    track_precessor = {}
    # initialize the shorest_path with value to everynode is infinity
    for node in unvisitedNodes:
        shortest_path[node] = float('inf')
    # exception for start node: distance from start node to itself is 0
    shortest_path[start] = 0

    # loop through all unvisted nodes
    while unvisitedNodes:
        # find the next min node of current node
        min_node = None
        for node in unvisitedNodes:
            if min_node is None:
                min_node = node
            elif shortest_path[node] < shortest_path[min_node]:
                min_node = node

        # loop through every options of the next node just found
        path_options = graph[min_node].items()
        for child_node, weight in path_options:
            if weight + shortest_path[min_node] < shortest_path[child_node]:
                shortest_path[child_node] = weight + shortest_path[min_node]
                track_precessor[child_node] = min_node

        unvisitedNodes.pop(min_node)
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


dijkstra(graph, 'A', 'F')

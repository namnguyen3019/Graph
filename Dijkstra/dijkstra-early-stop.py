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
    # unvisitedNodes store all unvisited nodes and its weight (or cost) in the graph
    unvisitedNodes = []
    # Go to "start" location to itself cost 0. Push it in the priority queue
    heapq.heappush(unvisitedNodes, (0, start))

    # records of shorest path from start to a node
    dis = {}
    track_precessor = {}
    # initialize the shorest_path with value to everynode is infinity
    for node in graph:
        dis[node] = float('inf')
    # exception for start node: distance from start node to itself is 0
    dis[start] = 0

    # loop through all unvisted nodes
    while unvisitedNodes:
        # find the next node that is nearest the current node
        # Also pop the node from the priority queue
        (min_cost, selected_node) = heapq.heappop(unvisitedNodes)

        if dis[selected_node] < min_cost:
            continue

        # Break the loop when reach the end_node => BREAK EARLY
        if selected_node == end:
            print('Stop early')
            break

        # loop through every options of the next node just found
        path_options = graph[selected_node].items()
        for child_node, weight in path_options:
            newWeight = dis[selected_node] + weight
            if newWeight < dis[child_node]:
                dis[child_node] = newWeight
                # keep track of the path in track_precessor
                track_precessor[child_node] = selected_node
                # Push child_node to the queue
                heapq.heappush(unvisitedNodes, (newWeight, child_node))

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

    if dis[end] != float('inf'):
        print('Optimal path: ' + str(optimal_path))
        print('Total cost: ' + str(dis[end]))


dijkstra(graph, 'A', 'E')  # result: 25
dijkstra(graph, 'A', 'C')  # result: 45
dijkstra(graph, 'A', 'F')  # result: path not found

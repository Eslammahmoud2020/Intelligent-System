import heapq


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 5},
    'C': {'F': 1},
    'D': {},
    'E': {'G': 2},
    'F': {'G': 3},
    'G': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 2,
    'F': 1,
    'G': 0  # Goal node has a heuristic of 0
}

def greedy_best_first_search(graph, start, goal):
    # Priority queue for open nodes, initialized with the start node
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    # Set to keep track of visited nodes
    visited = set()

    # Path to store the actual path taken
    path = []

    while open_list:
        # Get the node with the smallest heuristic value
        _, current = heapq.heappop(open_list)
        path.append(current)

        # If goal is reached, return the path
        if current == goal:
            return path

        # Mark the node as visited
        visited.add(current)

        # Explore neighbors
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return path


start_node = 'A'
goal_node = 'G'
path = greedy_best_first_search(graph, start_node, goal_node)
print("Path:", path)

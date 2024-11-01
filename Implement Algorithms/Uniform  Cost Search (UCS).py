import heapq


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def uniform_cost_search(graph, start, goal):
    # Priority queue with tuples of (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:

        # get the node with the lowest cost
        cost, node, path = heapq.heappop(queue)

        # If we reach the goal, return the cost and path
        if node == goal:
            return cost, path


        if node not in visited:
            visited.add(node)

            # Explore neighbors
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    # If the goal is not reachable
    return float("inf"), [] 


start = 'A'
goal = 'D'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost: {cost}, Path: ,{path}")

def dfs(graph, start):
    # To keep track of visited nodes
    visited = set()

    stack = [start]

    while stack:

        # Take the last element from the stack
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")

            # Mark the node as visited
            visited.add(node)

            # Add all unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Following is the DFS  A:")
dfs(graph, 'A')

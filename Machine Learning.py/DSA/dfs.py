# Depth first search (DFS) implementation in Python
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    print(start, end="")
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)
    return order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A','F','G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['E', 'C'],
    'G': ['C'],
    'H': ['E']
}

print("DFS starting from vertex A:")
order = dfs(graph, 'A')
print()  # for a new line after DFS output
print("Last node visited:", order[-1])  # print the last node visited in DFS




# other way


def dfs(graph, start):
    visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                _dfs(neighbour)

    _dfs(start)
    return order

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['E', 'C'],
    'G': ['C'],
    'H': ['E']
}

print("DFS starting from vertex A:")
order = dfs(graph, 'A')
print(" -> ".join(order))
print("Last node visited:", order[-1])  # print the last node visited in DFS
print()  # for a new line after DFS output
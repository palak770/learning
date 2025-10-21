# BFS code using graph represented as an adjacency list
from collections import deque
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    visited.add(start)  # Mark the start node as visited

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        print(vertex, end=" ")  # Process the vertex (here we just print it)

        for neighbor in graph[vertex]:  # Get all adjacent vertices of the dequeued vertex
            if neighbor not in visited:  # If the neighbor hasn't been visited
                visited.add(neighbor)  # Mark it as visited
                queue.append(neighbor)  # Enqueue the neighbor
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A','F','G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['E', 'C'],
    'G': ['C'],
    'H': ['E'],
    
}
print("BFS starting from vertex A:")
bfs(graph, 'A')  # Start BFS from vertex 'A'
print()  # for a new line after BFS output

# BFS code using graph represented as an adjacency matrix
def bfs_matrix(mat, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    visited.add(start)  # Mark the start node as visited

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        print(vertex, end=" ")  # Process the vertex (here we just print it)

        for i in range(len(mat[vertex])):  # Get all adjacent vertices of the dequeued vertex
            if mat[vertex][i] == 1 and i not in visited:  # If there's an edge and the neighbor hasn't been visited
                visited.add(i)  # Mark it as visited
                queue.append(i)  # Enqueue the neighbor
                
mat = [[0, 1, 1, 0, 0, 0, 0, 0],  # A    
      [1, 0, 0, 1, 1, 0, 0, 0],  # B
      [1, 0, 0, 0, 0, 1, 1, 0],  # C
      [0, 1, 0, 0, 0, 0, 0, 0],  # D
      [0, 1, 0, 0, 0, 0, 0, 1],  # E
      [0, 0, 1, 0, 0, 0, 0, 0],  # F
      [0, 0, 1, 0, 0, 0, 0, 0],  # G
      [0, 0, 0, 0, 1, 0, 0, 0]   # H
        ]
print("BFS starting from vertex 0 (A):")
bfs_matrix(mat, 0)  # Start BFS from vertex 0 (A)
print()  # for a new line after BFS output

#draw bfs graph using adjacency list
import matplotlib.pyplot as plt
import networkx as nx
def draw_bfs(graph, start):
    G = nx.Graph()  # Create a new graph
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge)  # Add edges to the graph

    pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)

    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    visited.add(start)  # Mark the start node as visited

    bfs_edges = []  # List to store edges in the order they are visited

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue

        for neighbor in graph[vertex]:  # Get all adjacent vertices of the dequeued vertex
            if neighbor not in visited:  # If the neighbor hasn't been visited
                visited.add(neighbor)  # Mark it as visited
                queue.append(neighbor)  # Enqueue the neighbor
                bfs_edges.append((vertex, neighbor))  # Add the edge to bfs_edges

    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='r', width=2)  # Highlight BFS edges in red
    plt.title(f"BFS Traversal starting from {start}")
    plt.show()  # Display the graph
draw_bfs(graph, 'A')  # Draw BFS starting from vertex 'A'

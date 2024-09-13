from collections import deque, defaultdict  # Importing deque for BFS queue and defaultdict to easily create adjacency lists.

def bfs_spanning_tree(n, graph):
    visited = [False] * n  # O(n) - Initialize a list to track visited nodes.
    parent = [-1] * n  # O(n) - Initialize parent list to store parent of each node in the spanning tree.
    bfs_queue = deque([0])  # O(1) - Initialize BFS queue with the starting node (0).
    visited[0] = True  # O(1) - Mark the start node as visited.

    # Time complexity: O(V + E) where V is the number of vertices and E is the number of edges.
    while bfs_queue:
        u = bfs_queue.popleft()  # O(1) - Dequeue the next node (constant time with deque).
        for v in graph[u]:  # O(E) - Iterate over all adjacent vertices of u (each edge is processed once).
            if not visited[v]:  # O(1) - Check if the vertex v has not been visited.
                visited[v] = True  # O(1) - Mark the vertex v as visited.
                parent[v] = u  # O(1) - Record that u is the parent of v in the spanning tree.
                bfs_queue.append(v)  # O(1) - Enqueue the vertex v.

    # Construct the spanning tree edges
    spanning_tree_edges = []  # O(1) - Initialize a list to store the edges in the spanning tree.
    for v in range(n):  # O(n) - Iterate over each vertex.
        if parent[v] != -1:  # O(1) - If the vertex has a parent, it is part of the spanning tree.
            spanning_tree_edges.append((parent[v], v))  # O(1) - Add the edge (parent, vertex) to the spanning tree.

    return spanning_tree_edges  # O(1) - Return the list of edges in the spanning tree.

# Example usage
n = 5  # Number of vertices.
graph = defaultdict(list)  # Create a graph with adjacency list representation.
graph[0] = [1, 3]  # Adding edges to the graph.
graph[1] = [0, 2, 4]
graph[2] = [1]
graph[3] = [0, 4]
graph[4] = [1, 3]

spanning_tree = bfs_spanning_tree(n, graph)  # Find the spanning tree using BFS.
print("Edges in the Spanning Tree:")
for u, v in spanning_tree:  # O(E) - Iterate over the edges of the spanning tree.
    print(f"{u} -- {v}")  # O(1) - Print each edge.



"""
Time Complexity for BFS-based Spanning Tree
Best Case, Average Case, Worst Case: 
 
O(V+E)
Explanation: Each vertex and edge is processed once. Traversing all vertices and their adjacent edges takes 
 
O(V+E), which is optimal for a graph traversal algorithm.
Space Complexity: 

O(V+E)
This is due to the visited, parent arrays (O(V)) and the graph adjacency list (O(E)).

"""


def dfs_spanning_tree(n, graph):
    visited = [False] * n  # O(n) - Initialize a list to track visited nodes.
    parent = [-1] * n  # O(n) - Initialize parent list to store the parent of each node in the spanning tree.

    # Time complexity of DFS helper: O(V + E) where V is the number of vertices and E is the number of edges.
    def dfs(u):
        visited[u] = True  # O(1) - Mark the vertex u as visited.
        for v in graph[u]:  # O(E) - Iterate over all adjacent vertices of u (each edge is processed once).
            if not visited[v]:  # O(1) - Check if the vertex v has not been visited.
                parent[v] = u  # O(1) - Record that u is the parent of v in the spanning tree.
                dfs(v)  # O(V + E) - Recursively perform DFS on vertex v.

    dfs(0)  # O(V + E) - Start DFS from vertex 0.

    # Construct the spanning tree edges
    spanning_tree_edges = []  # O(1) - Initialize a list to store the edges in the spanning tree.
    for v in range(n):  # O(n) - Iterate over each vertex.
        if parent[v] != -1:  # O(1) - If the vertex has a parent, it is part of the spanning tree.
            spanning_tree_edges.append((parent[v], v))  # O(1) - Add the edge (parent, vertex) to the spanning tree.

    return spanning_tree_edges  # O(1) - Return the list of edges in the spanning tree.

# Example usage
n = 5  # Number of vertices.
graph = defaultdict(list)  # Create a graph with adjacency list representation.
graph[0] = [1, 3]  # Adding edges to the graph.
graph[1] = [0, 2, 4]
graph[2] = [1]
graph[3] = [0, 4]
graph[4] = [1, 3]

spanning_tree = dfs_spanning_tree(n, graph)  # Find the spanning tree using DFS.
print("Edges in the Spanning Tree:")
for u, v in spanning_tree:  # O(E) - Iterate over the edges of the spanning tree.
    print(f"{u} -- {v}")  # O(1) - Print each edge.

"""
Time Complexity for DFS-based Spanning Tree
Best Case, Average Case, Worst Case: 
 
O(V+E)
Explanation: Each vertex is visited once, and for each vertex, all of its adjacent edges are explored. Hence the complexity is proportional to 
 
O(V+E), where 
𝑉
V is the number of vertices and 
𝐸
E is the number of edges.
Space Complexity: 
 
O(V+E)
This is due to the space required for the visited, parent arrays (O(V)) and the adjacency list (O(E))."""


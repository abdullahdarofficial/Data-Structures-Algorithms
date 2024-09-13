from collections import deque, defaultdict

def kahn_topological_sort(vertices, edges):
    # Create an adjacency list and in-degree array
    # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
    graph = defaultdict(list)  # Adjacency list to represent the graph
    in_degree = {i: 0 for i in range(vertices)}  # In-degree array to track the number of incoming edges for each vertex

    # Build the graph and compute in-degrees of each node
    # Time complexity: O(E), where E is the number of edges
    for u, v in edges:
        graph[u].append(v)  # Add directed edge u -> v
        in_degree[v] += 1  # Increment in-degree of vertex v

    # Queue to store nodes with 0 in-degree
    # Time complexity: O(V), where V is the number of vertices
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    topo_order = []  # List to store the topological order

    # Process nodes with 0 in-degree
    # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
    while queue:
        node = queue.popleft()  # Remove node from the queue
        topo_order.append(node)  # Add it to the topological order

        # Reduce the in-degree of neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1  # Reduce the in-degree by 1
            # If in-degree becomes 0, add to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle in the graph
    # Time complexity: O(1)
    if len(topo_order) != vertices:
        return "Graph has a cycle, topological sorting not possible."

    return topo_order  # Return the topological order

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

topo_sort = kahn_topological_sort(vertices, edges)
print("Topological Order (Kahn's Algorithm):", topo_sort)

# -------------------------------
# Time complexity analysis:
# -------------------------------
# 1. Building the adjacency list and calculating in-degrees:
#    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.

# 2. Processing nodes with 0 in-degree:
#    - Time complexity: O(V + E), as each vertex is visited once, and for each vertex, we process its edges.

# Overall time complexity:
# - Best-case time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# - Average-case time complexity: O(V + E).
# - Worst-case time complexity: O(V + E), as we have to visit every vertex and every edge.

# Space complexity:
# - Space complexity: O(V + E), as we store the adjacency list (O(E)) and the in-degree array (O(V)).


from collections import defaultdict

# Recursive DFS helper function to perform topological sort
def dfs_topological_sort(v, graph, visited, stack):
    # Mark the current vertex as visited
    visited[v] = True

    # Recur for all adjacent vertices (neighbors)
    # Time complexity: O(E), where E is the number of edges
    for neighbor in graph[v]:
        if not visited[neighbor]:  # Visit unvisited neighbors
            dfs_topological_sort(neighbor, graph, visited, stack)

    # Push the current vertex to the stack after visiting all neighbors
    stack.append(v)

# Main function to perform topological sort using DFS
def topological_sort(vertices, edges):
    # Create an adjacency list to represent the graph
    # Time complexity: O(E), where E is the number of edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)  # Add directed edge u -> v

    # Initialize visited array to track visited vertices
    # Time complexity: O(V), where V is the number of vertices
    visited = [False] * vertices

    # Stack to store the topological sort order
    stack = []

    # Perform DFS for each unvisited vertex
    # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
    for i in range(vertices):
        if not visited[i]:  # Perform DFS for unvisited nodes
            dfs_topological_sort(i, graph, visited, stack)

    # Return the reverse of the stack to get the topological order
    return stack[::-1]  # Time complexity: O(V)

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

topo_sort = topological_sort(vertices, edges)
print("Topological Order (DFS-based):", topo_sort)

# -------------------------------
# Time complexity analysis:
# -------------------------------
# 1. Building the adjacency list:
#    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
#
# 2. Performing DFS for each vertex:
#    - Time complexity: O(V + E), as each vertex is visited once, and for each vertex, we process its edges.

# Overall time complexity:
# - Best-case time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# - Average-case time complexity: O(V + E).
# - Worst-case time complexity: O(V + E), as we need to visit every vertex and every edge.

# Space complexity:
# - Space complexity: O(V + E), as we store the adjacency list (O(E)) and the visited array (O(V)).
# - Additionally, the stack used to store the topological order takes O(V) space.

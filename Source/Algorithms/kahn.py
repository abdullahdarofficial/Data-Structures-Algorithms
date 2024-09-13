from collections import deque, defaultdict

def kahn_topological_sort(vertices, edges):
    # Create an adjacency list to represent the graph and an in-degree dictionary
    # Time complexity: O(V), where V is the number of vertices
    graph = defaultdict(list)  # Graph represented as adjacency list
    in_degree = {i: 0 for i in range(vertices)}  # In-degree for each vertex

    # Build the graph and compute in-degrees of each node
    # Time complexity: O(E), where E is the number of edges
    for u, v in edges:
        graph[u].append(v)  # Add directed edge u -> v in the graph
        in_degree[v] += 1  # Increment in-degree of vertex v

    # Queue to store nodes with 0 in-degree (i.e., nodes with no incoming edges)
    # Time complexity: O(V), as we iterate through all vertices
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    # List to store the topological order of nodes
    topo_order = []

    # Process nodes with 0 in-degree using BFS approach
    # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
    while queue:
        node = queue.popleft()  # Remove node from the queue
        topo_order.append(node)  # Add it to the topological order

        # Reduce the in-degree of all neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1  # Reduce in-degree by 1
            # If in-degree becomes 0, add the neighbor to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle in the graph by verifying if topo_order contains all vertices
    # Time complexity: O(1), as the length check is constant time
    if len(topo_order) != vertices:
        return "Graph has a cycle, topological sorting not possible."

    return topo_order  # Return the topological order

# Example usage
vertices = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

# Perform topological sort
topo_sort = kahn_topological_sort(vertices, edges)
print("Topological Order:", topo_sort)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Creating the graph and in-degree array:
#    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
#    - Best, Average, and Worst-case: O(V + E), as we must process all vertices and edges to build the graph and calculate in-degrees.

# 2. Initializing the queue with 0 in-degree nodes:
#    - Time complexity: O(V), as we iterate through all vertices to check their in-degrees.
#    - Best, Average, and Worst-case: O(V).

# 3. Processing nodes with 0 in-degree (main loop):
#    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges.
#    - For each vertex, we process its neighbors (edges) and update their in-degrees.
#    - Best-case: O(V + E), even if all vertices have 0 in-degree.
#    - Average-case: O(V + E), depending on the number of vertices and edges.
#    - Worst-case: O(V + E), when we need to process all vertices and edges in the graph.

# 4. Cycle detection (final check):
#    - Time complexity: O(1), since we only compare the length of the topological order with the number of vertices.
#    - Best, Average, and Worst-case: O(1).

# Overall time complexity:
# - Best-case time complexity: O(V + E).
# - Average-case time complexity: O(V + E).
# - Worst-case time complexity: O(V + E).
# - The overall time complexity is O(V + E) because we visit every vertex and edge once to construct the graph, compute in-degrees, and perform the topological sorting.


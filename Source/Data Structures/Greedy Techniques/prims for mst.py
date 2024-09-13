import heapq  # Import heapq for using a min-heap

def prims_algorithm(n, graph):
    """
    Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    :param n: Number of vertices in the graph.
    :param graph: Adjacency list where graph[u] contains (v, weight) tuples.
    :return: Total weight of the MST and list of edges in the MST.
    """
    # Min-heap priority queue to select the edge with the smallest weight
    min_heap = []

    # Track visited vertices
    visited = [False] * n  # A list to track which vertices have been added to the MST

    # Start with the first vertex (vertex 0)
    start_vertex = 0
    total_weight = 0  # To track the total weight of the MST
    mst_edges = []  # To store the edges that form the MST

    # Helper function to add edges of a vertex to the min-heap
    def add_edges(vertex):
        visited[vertex] = True  # Mark the vertex as visited
        # Iterate over all neighbors of the current vertex
        for neighbor, weight in graph[vertex]:
            if not visited[neighbor]:  # Add only if the neighbor is not visited
                # Push the edge into the min-heap as (weight, u, v)
                heapq.heappush(min_heap, (weight, vertex, neighbor))

    # Initialize the min-heap with edges from the start vertex
    add_edges(start_vertex)

    # Continue building the MST until the min-heap is empty
    while min_heap:
        # Extract the edge with the minimum weight
        weight, u, v = heapq.heappop(min_heap)

        # If the vertex v is already in the MST, skip this edge (to avoid cycles)
        if visited[v]:
            continue

        # Include this edge in the MST
        mst_edges.append((u, v, weight))  # Add the edge (u, v) to the MST
        total_weight += weight  # Add the weight of the edge to the total weight of the MST

        # Add edges of the newly added vertex (v) to the min-heap
        add_edges(v)

    # Return the total weight of the MST and the edges that form the MST
    return total_weight, mst_edges

# Example usage
n = 5  # Number of vertices in the graph
graph = {
    0: [(1, 2), (3, 6)],        # Vertex 0 is connected to 1 with weight 2, and to 3 with weight 6
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],  # Vertex 1 has edges to 0, 2, 3, and 4
    2: [(1, 3), (4, 7)],        # Vertex 2 has edges to 1 and 4
    3: [(0, 6), (1, 8)],        # Vertex 3 has edges to 0 and 1
    4: [(1, 5), (2, 7)]         # Vertex 4 has edges to 1 and 2
}

# Run Prim's algorithm to find the Minimum Spanning Tree (MST)
total_weight, mst_edges = prims_algorithm(n, graph)

# Output the edges in the MST and the total weight
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst_edges:
    print(f"{u} -- {v} == {weight}")
print(f"Total weight of the Minimum Spanning Tree: {total_weight}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing and adding edges to the min-heap:
#    - Time complexity: O(E log V), where E is the number of edges and V is the number of vertices.
#    - Each edge is added to the heap at most once, and each insertion or deletion from the heap takes O(log V) time.

# 2. Min-heap operations:
#    - Time complexity: O(E log V), since we may extract and add edges E times, and each heap operation (insert/extract) takes O(log V).

# 3. Overall time complexity:
#    - Best-case time complexity: O(E log V), dominated by the heap operations.
#    - Average-case time complexity: O(E log V).
#    - Worst-case time complexity: O(E log V), where E is the number of edges and V is the number of vertices.

# Space complexity:
# - Space complexity: O(E + V), where E is the number of edges (for storing the graph and heap) and V is the number of vertices (for the visited array).

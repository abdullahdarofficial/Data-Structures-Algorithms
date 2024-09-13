class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the number of vertices
        self.vertices = vertices  # Number of vertices in the graph
        self.edges = []  # List to store all edges in the form (u, v, w)

    def add_edge(self, u, v, w):
        # Add an edge from vertex u to vertex v with weight w
        self.edges.append((u, v, w))  # Store the edge as a tuple (u, v, w)

    def bellman_ford(self, source):
        # Step 1: Initialize distances from source to all vertices as INFINITE
        # Time complexity: O(V), where V is the number of vertices
        distances = [float('inf')] * self.vertices  # Initialize distances array with infinity
        distances[source] = 0  # Distance to the source vertex is 0

        # Step 2: Relax all edges |V| - 1 times
        # Time complexity: O(V * E), where V is the number of vertices and E is the number of edges
        for _ in range(self.vertices - 1):  # Repeat |V| - 1 times
            for u, v, w in self.edges:  # For every edge (u, v, w)
                # Relax the edge by checking if we can improve the distance to vertex v
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w  # Update the distance to vertex v

        # Step 3: Check for negative-weight cycles
        # Time complexity: O(E), where E is the number of edges
        for u, v, w in self.edges:  # For every edge (u, v, w)
            # If we can still relax an edge, then there is a negative weight cycle
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None  # If negative cycle exists, return None

        # Return the computed shortest distances
        return distances

# Example usage
g = Graph(5)  # Create a graph with 5 vertices
# Add edges with weights
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

source = 0  # Source vertex for the Bellman-Ford algorithm
distances = g.bellman_ford(source)  # Find shortest distances from the source
if distances:
    print(f"Distances from source vertex {source}:")
    for i in range(len(distances)):
        print(f"Vertex {i}: {distances[i]}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the distances array:
#    - Time complexity: O(V), where V is the number of vertices.
#    - We initialize the distances for each vertex to infinity, except for the source vertex.

# 2. Relaxing the edges |V| - 1 times:
#    - Time complexity: O(V * E), where V is the number of vertices and E is the number of edges.
#    - For each of the |V| - 1 iterations, we loop over all edges and attempt to relax them.

# 3. Checking for negative-weight cycles:
#    - Time complexity: O(E), where E is the number of edges.
#    - We perform one final pass over all edges to check for any further relaxation, indicating a negative cycle.

# Overall time complexity:
# - Best-case time complexity: O(V * E), as we must process all edges even if the graph is simple.
# - Average-case time complexity: O(V * E).
# - Worst-case time complexity: O(V * E), as all edges are processed in each of the |V| - 1 iterations.

# Space complexity:
# - Space complexity: O(V), as we store the distances for each vertex.
# - The graph structure (edges list) takes O(E) space, where E is the number of edges.

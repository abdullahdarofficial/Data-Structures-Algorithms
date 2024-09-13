import numpy as np

def floyd_warshall(graph):
    """
    Computes the shortest paths between all pairs of vertices using the Floyd-Warshall algorithm.

    :param graph: 2D list or numpy array representing the adjacency matrix of the graph
                  where graph[i][j] is the weight of the edge from vertex i to vertex j.
                  Use float('inf') for no direct edge between vertices.
    :return: 2D numpy array representing the shortest paths between all pairs of vertices
    """
    num_vertices = len(graph)  # Number of vertices in the graph

    # Initialize the distance matrix with the given graph
    # Time complexity: O(V^2), where V is the number of vertices
    distance = np.array(graph, dtype=float)  # Copy the adjacency matrix into a distance matrix

    # Floyd-Warshall algorithm
    # Time complexity: O(V^3), where V is the number of vertices
    for k in range(num_vertices):
        # For each pair of vertices (i, j), check if a shorter path exists through vertex k
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Update distance[i][j] if a shorter path is found via vertex k
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance  # Return the matrix of shortest paths

# Example usage
graph = [
    [0, 3, float('inf'), float('inf'), float('inf'), 5],  # Edge weights from vertex 0
    [2, 0, float('inf'), float('inf'), float('inf'), 6],  # Edge weights from vertex 1
    [float('inf'), 7, 0, 1, float('inf'), 2],             # Edge weights from vertex 2
    [float('inf'), float('inf'), float('inf'), 0, 3, float('inf')],  # Edge weights from vertex 3
    [float('inf'), float('inf'), float('inf'), 2, 0, 4],  # Edge weights from vertex 4
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0]  # Edge weights from vertex 5
]

# Compute the shortest paths between all pairs of vertices
shortest_paths = floyd_warshall(graph)

# Print the shortest path matrix
print("Shortest path matrix:")
print(shortest_paths)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the distance matrix:
#    - Time complexity: O(V^2), where V is the number of vertices.
#    - We copy the input graph into the distance matrix.

# 2. Floyd-Warshall algorithm (triple loop):
#    - Time complexity: O(V^3), where V is the number of vertices.
#    - The algorithm uses three nested loops to update the shortest paths for all pairs of vertices.
#      For each pair of vertices (i, j), the algorithm checks if a shorter path exists via an intermediate vertex k.
#      Thus, for every vertex k, the algorithm checks all pairs of vertices, resulting in O(V^3) operations.

# Overall time complexity:
# - Best-case time complexity: O(V^3), as the algorithm always runs three nested loops regardless of the input.
# - Average-case time complexity: O(V^3).
# - Worst-case time complexity: O(V^3), since all pairs of vertices must be checked for every intermediate vertex.

# Space complexity:
# - Space complexity: O(V^2), since the algorithm requires a distance matrix of size V x V to store the shortest path between every pair of vertices.

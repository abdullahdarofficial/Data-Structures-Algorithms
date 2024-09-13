import heapq  # Import heapq to use the priority queue (min-heap)

def dijkstra(graph, start):
    """
    Computes the shortest paths from the source vertex to all other vertices
    using Dijkstra's algorithm.

    :param graph: Dictionary representing the adjacency list of the graph
                  Example: {0: [(1, 4), (2, 1)], 1: [(2, 2), (3, 5)], 2: [(1, 5), (3, 1)], 3: []}
    :param start: The starting vertex
    :return: Dictionary of shortest distances from the source vertex to each vertex
    """
    # Priority queue to process the next vertex with the smallest distance
    # Priority queue stores tuples in the form (distance, vertex)
    priority_queue = [(0, start)]  # Initialize with the source vertex, distance 0

    # Distances dictionary: Initialize all distances to infinity except the start vertex
    # Time complexity: O(V), where V is the number of vertices
    distances = {vertex: float('inf') for vertex in graph}  # Set all distances to infinity
    distances[start] = 0  # Distance to the start vertex is 0

    # Main loop: Process the priority queue until it's empty
    # Time complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges
    while priority_queue:
        # Pop the vertex u with the smallest distance from the queue
        current_distance, u = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded distance, skip this entry
        if current_distance > distances[u]:
            continue  # This is a stale entry and should be ignored

        # Update the distances for each neighbor of vertex u
        # Time complexity: O(E), where E is the number of edges
        for neighbor, weight in graph[u]:
            # Calculate the new distance to neighbor through vertex u
            distance = current_distance + weight

            # If the new distance is shorter than the previously known distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update the shortest distance
                # Push the new distance and neighbor into the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    # Return the dictionary of shortest distances from the start vertex
    return distances

# Example usage
graph = {
    0: [(1, 4), (2, 1)],  # Edges from vertex 0 to vertices 1 (weight 4) and 2 (weight 1)
    1: [(2, 2), (3, 5)],  # Edges from vertex 1 to vertices 2 (weight 2) and 3 (weight 5)
    2: [(1, 2), (3, 1)],  # Edges from vertex 2 to vertices 1 (weight 2) and 3 (weight 1)
    3: []                 # No edges from vertex 3 (end of the graph)
}

start_vertex = 0  # Source vertex for Dijkstra's algorithm
# Compute the shortest distances from the source vertex to all other vertices
shortest_distances = dijkstra(graph, start_vertex)

# Print the shortest distances
print(f"Shortest distances from vertex {start_vertex}:")
for vertex in shortest_distances:
    print(f"Vertex {vertex}: {shortest_distances[vertex]}")

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Initializing the distances dictionary:
#    - Time complexity: O(V), where V is the number of vertices.
#    - We initialize the distance for each vertex to infinity, except for the source vertex.

# 2. Main loop (processing the priority queue):
#    - Time complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges.
#    - We process each vertex and edge once. Each pop and push operation on the priority queue takes O(log V).
#    - In total, there will be O(E) edge relaxations and O(V) pop operations from the priority queue,
#      each of which takes O(log V) time.

# 3. Updating distances:
#    - Time complexity: O(E), where E is the number of edges.
#    - We update the distance for each edge in the graph.

# Overall time complexity:
# - Best-case time complexity: O((V + E) log V), as we process each vertex and edge.
# - Average-case time complexity: O((V + E) log V).
# - Worst-case time complexity: O((V + E) log V), since Dijkstra’s algorithm processes every edge and vertex.

# Space complexity:
# - Space complexity: O(V), where V is the number of vertices.
# - This includes the space for the distances dictionary and the priority queue.

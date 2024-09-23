from collections import deque

# Class to represent an undirected graph
class Graph:
    def __init__(self):
        # Time Complexity: O(1)
        # Initialize an empty adjacency list for the graph
        self.graph = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        # Time Complexity: O(1)
        if vertex not in self.graph:
            # If the vertex is not already in the graph, add it with an empty list of edges
            self.graph[vertex] = []

    # Add an undirected edge between two vertices u and v
    def add_edge(self, u, v):
        # Time Complexity: O(1) on average
        if u not in self.graph:
            # If vertex u is not in the graph, add it first
            self.add_vertex(u)
        if v not in self.graph:
            # If vertex v is not in the graph, add it first
            self.add_vertex(v)
        # Add v to u's adjacency list and u to v's adjacency list (since it's undirected)
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Perform Depth-First Search (DFS) starting from the given vertex
    def dfs(self, start):
        # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
        visited = set()  # Set to track visited vertices
        # Call the recursive DFS helper function
        self._dfs_recursive(start, visited)

    # Helper function for recursive DFS traversal
    def _dfs_recursive(self, vertex, visited):
        # Time Complexity: O(V) in the worst case for traversing vertices
        if vertex not in visited:
            # Visit the vertex and mark it as visited
            print(vertex, ' ')
            visited.add(vertex)
            # Recur for all adjacent vertices that have not been visited
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    self._dfs_recursive(neighbour, visited)

    # Perform Breadth-First Search (BFS) starting from the given vertex
    def bfs(self, start):
        # Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
        visited = set()  # Set to keep track of visited vertices
        queue = deque([start])  # Initialize a queue with the starting vertex
        visited.add(start)  # Mark the start vertex as visited

        # Loop through the queue until it's empty
        while queue:
            vertex = queue.popleft()  # Remove a vertex from the queue
            print(vertex, ' ')  # Process the current vertex

            # Add all unvisited adjacent vertices to the queue
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    # Display the adjacency list representation of the graph
    def display(self):
        # Time Complexity: O(V), where V is the number of vertices
        for vertex in self.graph:
            # Print each vertex and its adjacent vertices
            print(vertex, self.graph[vertex])


# Example Usage
if __name__ == "__main__":
    g = Graph()

    # Adding vertices and edges
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")

    # Add edges to create connections between vertices
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")

    # Display the graph representation
    print("Graph representation:")
    g.display()

    # Perform DFS starting from vertex 'A'
    print("\nDFS starting from vertex 'A':")
    g.dfs("A")

    # Perform BFS starting from vertex 'A'
    print("\n\nBFS starting from vertex 'A':")
    g.bfs("A")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        # Uncomment below line for undirected graph
        # self.graph[v].append((u, weight))

    def print_graph(self):
        for u in self.graph:
            print(u, "->", self.graph[u])

    # Brute-force Dijkstra's Algorithm
    def brute_force_dijkstra(self, start):
        def find_all_paths(start, end, path=[], total_distance=0):
            path = path + [start]
            if start == end:
                return [(path, total_distance)]
            if start not in self.graph:
                return []
            all_paths = []
            for neighbor, weight in self.graph[start]:
                if neighbor not in path:
                    new_paths = find_all_paths(neighbor, end, path, total_distance + weight)
                    all_paths.extend(new_paths)
            return all_paths

        shortest_paths = {}
        for node in self.graph:
            if node == start:
                continue
            all_paths = find_all_paths(start, node)
            if all_paths:
                shortest_path = min(all_paths, key=lambda x: x[1])
                shortest_paths[node] = shortest_path[1]
            else:
                shortest_paths[node] = float('inf')
        return shortest_paths

    # Brute-force Bellman-Ford Algorithm
    def brute_force_bellman_ford(self, start):
        nodes = list(self.graph.keys())
        distances = {node: float('inf') for node in nodes}
        distances[start] = 0

        for _ in range(len(nodes) - 1):
            for u in nodes:
                if u in self.graph:
                    for v, weight in self.graph[u]:
                        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                            distances[v] = distances[u] + weight

        # Optional: Check for negative-weight cycles
        for u in nodes:
            if u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        print("Graph contains a negative weight cycle")
                        return None

        return distances

    # Brute-force Floyd-Warshall Algorithm
    def brute_force_floyd_warshall(self):
        nodes = list(self.graph.keys())
        distances = {u: {v: float('inf') for v in nodes} for u in nodes}

        for u in nodes:
            distances[u][u] = 0
            if u in self.graph:
                for v, weight in self.graph[u]:
                    distances[u][v] = weight

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        return distances


if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'D', 3)
    g.add_edge('C', 'D', 1)

    print("Graph:")
    g.print_graph()

    print("Brute-force Dijkstra's shortest paths from A:", g.brute_force_dijkstra('A'))
    print("Brute-force Bellman-Ford shortest paths from A:", g.brute_force_bellman_ford('A'))
    print("Brute-force Floyd-Warshall shortest paths:", g.brute_force_floyd_warshall())
